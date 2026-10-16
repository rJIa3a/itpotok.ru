"""Local evidence/package helper. No network, publishing or LLM calls."""
import argparse
import hashlib
import html
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def local(folder, name):
    p = (folder / name).resolve()
    if not p.is_relative_to(folder.resolve()):
        raise ValueError('Path outside article folder')
    return p


def init(folder, kind, keyword, competitor):
    if not re.fullmatch(r'[a-z][a-z0-9-]*', folder.name):
        raise ValueError('Use a short lowercase English folder name')
    folder.mkdir(parents=True, exist_ok=False)
    (folder / 'README.md').write_text('# ' + keyword + '\n\nСтатус: unverified-draft.\nWordPress: не загружено.\nGitHub: не отправлено.\nСледующий шаг: бриф и проверка дублей.\n', encoding='utf-8')
    (folder / 'brief.md').write_text(f'# Бриф\n\nКлюч: {keyword}\nКонкурент: {competitor}\nФормат: {kind}\n\nЗаполнить аудиторию, задачу, границы, критерии и проверку дублей.\n', encoding='utf-8')
    save(folder / 'workflow.json', dict(schema_version=1, format=kind, status='unverified-draft', article_file='article.html', created_at=now(), stages={}))
    for name in ('sources', 'claims', 'screenshots', 'visuals'):
        save(folder / (name + '.json'), [])
    save(folder / 'review.json', dict(article_sha256='', coverage_checked=False, sources_reopened=False, visuals_checked=False, editor_reviewed=False, unresolved_material=['Проверка не выполнена'], corrections=[], reviewed_at=None))
    save(folder / 'procedure.json', dict(environment={}, runs=[]))
    save(folder / 'metrics.json', dict(started_at=now(), checked_at=None, factual_corrections=None, manual_edit_minutes=None, reproducibility='not-measured', screenshot_quality='not-measured', chart_quality='not-measured'))
    for name in ('research.md', 'outline.md', 'illustrations.md', 'review.md', 'faq.md', 'excerpt.txt'):
        (folder / name).write_text('', encoding='utf-8')
    (folder / 'article.html').write_text('', encoding='utf-8')


STAGES = {'article-brief', 'research', 'claim-ledger', 'outline', 'procedure-runner', 'screenshot-capture', 'visuals', 'draft', 'fact-and-procedure-check', 'edit-and-package', 'refresh'}


def checkpoint(folder, stage, files):
    if stage not in STAGES or not files:
        raise ValueError('Unknown stage or empty artifact list')
    state = read(folder / 'workflow.json')
    hashes = {f: digest(local(folder, f)) for f in files}
    state['stages'][stage] = dict(recorded_at=now(), files=hashes)
    state['status'] = 'unverified-draft'
    save(folder / 'workflow.json', state)


def check(folder):
    problems = []
    def need(ok, message):
        if not ok:
            problems.append(message)
    def exists(name):
        return bool(name) and local(folder, name).is_file() and local(folder, name).stat().st_size > 0
    def dated(value):
        try:
            return date.fromisoformat(str(value)[:10]) <= date.today()
        except ValueError:
            return False
    state = read(folder / 'workflow.json')
    need(state.get('schema_version') == 1, 'Unsupported schema version')
    kind = state.get('format')
    need(kind in ('explanation', 'comparison', 'manual'), 'Unknown format')
    article_file = state.get('article_file', 'article.html')
    for name in ('README.md', 'brief.md', 'research.md', 'outline.md', 'illustrations.md', 'review.md', 'faq.md', 'excerpt.txt', article_file):
        need(exists(name), 'Missing or empty: ' + name)
    body = local(folder, article_file).read_text(encoding='utf-8') if exists(article_file) else ''
    article_hash = digest(local(folder, article_file)) if exists(article_file) else ''
    sources = read(folder / 'sources.json')
    claims = read(folder / 'claims.json')
    need(isinstance(sources, list) and bool(sources), 'No sources')
    need(isinstance(claims, list) and bool(claims), 'No claims')
    if not isinstance(sources, list) or not isinstance(claims, list):
        raise ValueError('sources and claims must be arrays')
    source_ids = {s.get('id') for s in sources}
    claim_ids = {c.get('id') for c in claims}
    need(len(source_ids) == len(sources) and None not in source_ids, 'Duplicate/missing source ID')
    need(len(claim_ids) == len(claims) and None not in claim_ids, 'Duplicate/missing claim ID')
    for s in sources:
        need(all(s.get(k) for k in ('url', 'title', 'excerpt', 'checked_at')), 'Incomplete source: ' + str(s.get('id')))
        need(dated(s.get('checked_at')), 'Invalid source date: ' + str(s.get('id')))
    referenced = set()
    for value in re.findall(r'data-claims=["\']([^"\']+)["\']', body):
        referenced.update(value.split())
    need(referenced <= claim_ids, 'Unknown data-claims ID')
    for c in claims:
        cid = str(c.get('id'))
        need(c.get('status') in ('supported', 'uncertain', 'contradicted'), 'Unknown claim status: ' + cid)
        need(isinstance(c.get('material'), bool), 'Missing material flag: ' + cid)
        if c.get('material') is not False:
            need(c.get('status') == 'supported', 'Unresolved material claim: ' + cid)
            need(c.get('source_id') in source_ids, 'Missing source for: ' + cid)
            need(all(c.get(k) for k in ('claim', 'evidence', 'location')), 'Incomplete evidence: ' + cid)
            need(dated(c.get('checked_at')), 'Invalid claim date: ' + cid)
            need(cid in referenced, 'Material claim absent from article mapping: ' + cid)
            try:
                need(date.fromisoformat(c['next_review']) >= date.today(), 'Expired claim: ' + cid)
            except (KeyError, ValueError):
                need(False, 'Missing/invalid next_review: ' + cid)
    for tag in re.findall(r'<a\b[^>]*>', body, re.I):
        href = re.search(r'href=["\'](https?://[^"\']+)', tag)
        if href and not re.match(r'https?://(?:www\.)?itpotok\.ru(?:/|$)', href[1]):
            rel = re.search(r'rel=["\']([^"\']+)', tag)
            tokens = set(rel[1].split()) if rel else set()
            need('nofollow' in tokens, 'External link lacks nofollow')
            if re.search(r'target=["\']_blank', tag):
                need({'noopener', 'noreferrer'} <= tokens, 'New-tab link lacks security rel')
    for name in ('screenshots', 'visuals'):
        items = read(folder / (name + '.json'))
        for item in items:
            if item.get('required', True):
                need(item.get('status') == 'verified', 'Unverified ' + name + ': ' + str(item.get('file')))
            if item.get('status') != 'verified':
                continue
            for k in ('file', 'caption', 'alt'):
                need(bool(item.get(k)), 'Missing ' + name + ' field: ' + k)
            need(exists(item.get('file')), 'Missing visual file')
            if name == 'screenshots':
                for k in ('step_id', 'action', 'expected', 'captured_at', 'rights'):
                    need(bool(item.get(k)), 'Missing screenshot ' + k)
                need(item.get('privacy_checked') is True, 'Screenshot privacy not checked')
                need(exists(item.get('original')), 'Missing safe original')
                if item.get('annotated'):
                    need(item['annotated'] != item.get('original') and exists(item['annotated']), 'Annotations must be separate')
                env = item.get('environment', {})
                need(str(env.get('language', '')).startswith('ru'), 'Screenshot interface is not Russian')
                need(all(k in env and env[k] for k in ('version', 'platform', 'language', 'plan', 'permissions')), 'Incomplete screenshot environment')
            elif item.get('type') == 'chart':
                need(exists(item.get('data')) and exists(item.get('script')), 'Chart lacks data/script')
    review = read(folder / 'review.json')
    need(bool(article_hash) and review.get('article_sha256') == article_hash, 'Review does not cover current article')
    for key in ('coverage_checked', 'sources_reopened', 'visuals_checked', 'editor_reviewed'):
        need(review.get(key) is True, 'Review missing: ' + key)
    need(review.get('unresolved_material') == [], 'Open material review findings')
    need(dated(review.get('reviewed_at')), 'Review date invalid')
    if kind == 'manual':
        proc = read(folder / 'procedure.json')
        env = proc.get('environment', {})
        need(all(env.get(k) for k in ('version', 'platform', 'language', 'plan', 'permissions')), 'Incomplete procedure environment')
        initial_ids = set()
        for run in proc.get('runs', []):
            if run.get('kind') == 'initial':
                initial_ids.update(s.get('id') for s in run.get('steps', []))
        for image in read(folder / 'screenshots.json'):
            if image.get('status') == 'verified':
                need(image.get('step_id') in initial_ids, 'Screenshot refers to unknown procedure step')
        for run_kind in ('initial', 'rerun'):
            runs = [r for r in proc.get('runs', []) if r.get('kind') == run_kind]
            valid = []
            for run in runs:
                steps = run.get('steps', [])
                good = dated(run.get('executed_at')) and bool(steps) and all(s.get('status') == 'passed' and all(s.get(k) for k in ('id', 'action', 'expected', 'actual')) and exists(s.get('evidence')) for s in steps)
                if run_kind == 'rerun':
                    good = good and run.get('article_sha256') == article_hash and {s.get('id') for s in steps} == initial_ids
                valid.append(good)
            need(any(valid), 'No successful ' + run_kind + ' with saved evidence/current text')
    required = ['article-brief', 'research', 'claim-ledger', 'outline', 'draft', 'visuals', 'fact-and-procedure-check', 'edit-and-package']
    if kind == 'manual':
        required += ['procedure-runner', 'screenshot-capture']
    for stage in required:
        point = state.get('stages', {}).get(stage, {})
        need(bool(point.get('files')), 'Missing checkpoint: ' + stage)
        for name, old_hash in point.get('files', {}).items():
            need(exists(name) and digest(local(folder, name)) == old_hash, 'Stale checkpoint: ' + stage + '/' + name)
    state['status'] = 'checked-draft' if not problems else 'unverified-draft'
    save(folder / 'workflow.json', state)
    report = dict(checked_at=now(), status=state['status'], article_sha256=article_hash, blockers=problems, limits='Completeness checks only; source truth and visual quality require recorded editorial review. No publication.')
    save(folder / 'package-report.json', report)
    return report


def preview(folder):
    state = read(folder / 'workflow.json')
    body = local(folder, state.get('article_file', 'article.html')).read_text(encoding='utf-8')
    excerpt = html.escape((folder / 'excerpt.txt').read_text(encoding='utf-8'))
    (folder / 'preview.html').write_text('<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Редакционный предпросмотр</title><style>body{max-width:850px;margin:2rem auto;padding:0 1rem;font:18px/1.6 sans-serif}img,svg{max-width:100%;height:auto}table{border-collapse:collapse}td,th{border:1px solid;padding:.4rem}</style><p>Локальный предпросмотр; тема WordPress не проверена.</p><p>' + excerpt + '</p><article>' + body + '</article></html>', encoding='utf-8')


def refresh(folder):
    tasks = []
    for c in read(folder / 'claims.json'):
        try:
            expired = date.fromisoformat(c['next_review']) <= date.today()
        except (KeyError, ValueError):
            expired = True
        if expired:
            tasks.append('- ' + str(c.get('id')) + ': открыть источник, проверить применимость; при изменении повторить зависимые шаги и кадры.')
    (folder / 'refresh.md').write_text('# Задания на обновление\n\n' + '\n'.join(tasks or ['Сроки реестра не истекли. Изменения продукта и интерфейса автоматически не отслеживаются.']) + '\n', encoding='utf-8')
    if tasks:
        state = read(folder / 'workflow.json'); state['status'] = 'unverified-draft'; save(folder / 'workflow.json', state)
    return tasks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('init', 'checkpoint', 'check', 'preview', 'refresh'):
        p = sub.add_parser(name); p.add_argument('folder', type=Path)
        if name == 'init':
            p.add_argument('--format', choices=['explanation', 'comparison', 'manual'], required=True)
            p.add_argument('--keyword', required=True); p.add_argument('--competitor', default='')
        if name == 'checkpoint':
            p.add_argument('stage'); p.add_argument('files', nargs='+')
    a = parser.parse_args()
    try:
        if a.command == 'init': init(a.folder, a.format, a.keyword, a.competitor)
        elif a.command == 'checkpoint': checkpoint(a.folder, a.stage, a.files)
        elif a.command == 'preview': preview(a.folder)
        elif a.command == 'refresh': print(json.dumps(refresh(a.folder), ensure_ascii=False))
        else:
            result = check(a.folder); print(json.dumps(result, ensure_ascii=False, indent=2)); return int(bool(result['blockers']))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as e:
        print('Input error: ' + str(e), file=sys.stderr); return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
