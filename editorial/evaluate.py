"""Run three bounded editorial pilots and reproduce the CLI manual.

These are editorial examples, not WordPress publications or human evaluations.
The source excerpts were opened during implementation on 2026-10-16.
"""
import json
import platform
import subprocess
import sys
import tempfile
import time
from datetime import date, timedelta
from pathlib import Path
import workflow as w

BASE = Path(__file__).parent.resolve()
OUT = BASE / 'evaluation'


def write(folder, name, text):
    p=folder/name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text+'\n',encoding='utf-8')


def run_cli(folder, run_id, target, instructions):
    steps=[]
    for n,(args,expected) in enumerate(instructions,1):
        result=subprocess.run([sys.executable,str(BASE/'workflow.py'),*args],capture_output=True,text=True,encoding='utf-8')
        log=f'evidence/{run_id}-{n}.txt'
        # No environment variables, credentials or unrelated files are read.
        safe_args=[value.replace(str(target),'<temporary>/sample-article') for value in args]
        write(folder,log,json.dumps(dict(command=['python','editorial/workflow.py',*safe_args],exit_code=result.returncode,stdout=result.stdout.replace(str(target),'<temporary>/sample-article'),stderr=result.stderr.replace(str(target),'<temporary>/sample-article')),ensure_ascii=False,indent=2))
        actual=f'exit={result.returncode}'
        ok=result.returncode==expected
        if args[0]=='init': ok=ok and (target/'README.md').exists()
        if args[0]=='preview': ok=ok and (target/'preview.html').exists()
        if args[0]=='check': ok=ok and w.read(target/'package-report.json')['status']=='unverified-draft'
        steps.append(dict(id=f'S{n}',action=' '.join(args).replace(str(target),'<новая-папка>'),expected=f'exit={expected}',actual=actual,status='passed' if ok else 'failed',evidence=log))
    return dict(id=run_id,kind=run_id,executed_at=w.now(),steps=steps)


def main():
    if OUT.exists():
        raise SystemExit('evaluation already exists; preserve evidence, use another output for a new evaluation')
    OUT.mkdir()
    sources={
        'google':dict(id='S1',url='https://developers.google.com/search/docs/fundamentals/using-gen-ai-content',title='Google Search: generative AI content',checked_at='2026-10-16',excerpt='It is critical to manually factcheck and review all AI-generated content',limitations='Рекомендации для веб-контента, не эксперимент об эффективности.'),
        'diataxis':dict(id='S1',url='https://diataxis.fr/',title='Diátaxis',checked_at='2026-10-16',excerpt='tutorials, how-to guides, technical reference and explanation',limitations='Практическая система организации документации.'),
        'local':dict(id='S1',url='editorial/workflow.py',title='CLI и сохранённые реальные прогоны',checked_at='2026-10-16',excerpt='init refuses existing folder; check emits blockers; preview creates local wrapper',limitations='Собственный код; доказательства в evidence/, только текущая Python/Windows среда.')
    }
    samples=[
        ('ai-factcheck','explanation','Почему ИИ-текст требует проверки','google',
         '<h1>Почему ИИ-текст требует проверки</h1><p data-claims="C1">Перед публикацией текст, подготовленный ИИ, нужно проверить по источникам и отредактировать. Google прямо рекомендует ручную проверку точности и надёжности такого контента.</p><h2>Что считать проверкой</h2><p>В этом проекте редактор открывает источник, сопоставляет его с формулировкой и сохраняет основание в реестре. Это правило нашего процесса: наличие ссылки само по себе не показывает, подтверждает ли она весь вывод.</p><h2>Как сохранить возможность обновления</h2><p>В реестре остаются формулировка, короткий фрагмент, дата сверки и ограничение источника. После изменения продукта редактор видит, какое основание нужно проверить повторно.</p><p><a href="https://developers.google.com/search/docs/fundamentals/using-gen-ai-content" rel="nofollow">Рекомендации Google</a></p>',
         'Google рекомендует вручную проверять точность и надёжность ИИ-контента перед публикацией.'),
        ('explanation-or-manual','comparison','Объяснение или мануал: какой формат выбрать','diataxis',
         '<h1>Объяснение или мануал: какой формат выбрать</h1><p>Выбирайте объяснение, если читателю нужно понять устройство или причину. Для выполнения конкретной задачи в нашем процессе используется мануал с проверяемыми действиями.</p><p data-claims="C1">Diátaxis различает четыре формы документации: учебное руководство, практическое руководство, справочник и объяснение. Ниже сравниваем два формата для задач редакции.</p><table><tr><th>Критерий</th><th>Объяснение</th><th>Мануал в этом проекте</th></tr><tr><td>Вопрос читателя</td><td>Почему это устроено так?</td><td>Как получить конкретный результат?</td></tr><tr><td>Основа</td><td>Связи и основания выводов</td><td>Исходное состояние, действия и наблюдаемый результат</td></tr><tr><td>Проверка редакции</td><td>Сверка существенных утверждений</td><td>Сверка фактов и повторный прогон</td></tr></table><h2>Если нужны оба формата</h2><p>В этой системе краткое объяснение может предварять действие. Развёрнутую теорию лучше вынести отдельно, когда она мешает читателю найти нужный шаг. Это редакционное решение, а не результат сравнительного испытания форматов.</p><p><a href="https://diataxis.fr/" rel="nofollow">Diátaxis</a></p>',
         'Diátaxis различает tutorials, how-to guides, technical reference и explanation.'),
        ('local-draft-manual','manual','Как создать локальный редакционный черновик','local',
         '<h1>Как создать локальный редакционный черновик</h1><p>Из корня репозитория запустите init для новой папки, затем check и preview. Вы получите заготовку и локальную страницу для чтения.</p><h2>Подготовка</h2><p>Нужны Python 3.10 или новее и этот репозиторий. Команды ниже используют новую папку sample-article. Если такая папка уже есть, выберите другое имя: init не перезаписывает существующую папку.</p><ol data-claims="C1"><li>Запустите <code>python editorial/workflow.py init sample-article --format explanation --keyword "Пример"</code>. В новой папке должны появиться README.md и workflow.json.</li><li>Запустите <code>python editorial/workflow.py check sample-article</code>. Для пустой заготовки ожидается код возврата 1, статус unverified-draft и список блокировок в package-report.json. Это ожидаемый результат: содержимое ещё не подготовлено.</li><li>Запустите <code>python editorial/workflow.py preview sample-article</code>. Откройте sample-article/preview.html в браузере. Файл создаётся локально и не подтверждает вид темы WordPress.</li></ol><h2>Если команда не сработала</h2><p>При отсутствии Python проверьте установленный интерпретатор. Если init сообщил о существующей папке, выберите новое имя, сохранив текущие материалы. Пустой исходник нужно заполнить до проверки готовности.</p><h2>Возврат</h2><p>Если заготовка больше не нужна, сначала проверьте её содержимое. Удалять можно только созданную для этого примера папку, если в ней нет нужных материалов. Команды не меняют WordPress.</p>',
         'В текущей среде init создаёт новую заготовку, check пустой заготовки возвращает 1, preview создаёт preview.html.')
    ]
    rows=[]
    for slug,kind,title,source_key,body,claim in samples:
        started=w.now(); tick=time.perf_counter(); folder=OUT/slug
        w.init(folder,kind,title,'Не применимо: внутренний пилот редакционного процесса')
        write(folder,'brief.md',f'# Бриф\n\nАудитория: редактор itpotok.ru. Задача: {title}. Формат: {kind}. Границы: короткий внутренний пилот, не публикация на сайте. Критерии: доказательства и честный статус. Дубли WordPress не проверялись, размещение не планируется.')
        write(folder,'article.html',body)
        write(folder,'excerpt.txt','Короткий внутренний материал для проверки редакционного процесса и его ограничений.')
        w.save(folder/'sources.json',[sources[source_key]])
        w.save(folder/'claims.json',[dict(id='C1',claim=claim,source_id='S1',evidence=sources[source_key]['excerpt'],checked_at='2026-10-16',next_review=(date.today()+timedelta(days=90)).isoformat(),status='supported',material=True,location='data-claims=C1')])
        write(folder,'research.md',f'# Основания\n\n{sources[source_key]["url"]}\nСверено 2026-10-16. {sources[source_key]["limitations"]}\nПрактические правила проекта помечены как редакционные решения. Конкурент не нужен для внутреннего пилота; исследование поисковой выдачи не проводилось.')
        write(folder,'outline.md','# План\n\nПрямой ответ → условия/основания → конкретный результат → ограничения. C1 связан с основным проверяемым утверждением. Сравнение использует общие критерии задачи, основы и проверки.')
        write(folder,'illustrations.md','# Иллюстрации\n\nДля короткого пилота иллюстрации не требуются: интерфейс продукта не описан. В CLI-мануале нужны команды и результаты, сохранённые в evidence/. Настоящие скриншоты, графики и обложка не создавались; их производственный цикл этим пилотом не проверен. Для публикационного пакета потребуется отдельный план обложки и проверка темы.')
        write(folder,'faq.md','# FAQ\n\nДля короткого внутреннего примера не требуется. WordPress ID и зависимостей нет.')
        if kind=='manual':
            runs=[]
            for run_id in ('initial','rerun'):
                with tempfile.TemporaryDirectory(prefix='editorial-pilot-') as temp:
                    target=Path(temp)/'sample-article'
                    instructions=[(['init',str(target),'--format','explanation','--keyword','Пример'],0),(['check',str(target)],1),(['preview',str(target)],0)]
                    run=run_cli(folder,run_id,target,instructions)
                    if run_id=='rerun': run['article_sha256']=w.digest(folder/'article.html')
                    runs.append(run)
            w.save(folder/'procedure.json',dict(environment=dict(version=platform.python_version(),platform=platform.system(),language='ru (текст), en (диагностика CLI)',plan='not-applicable',permissions='обычные права пользователя, временная папка'),runs=runs))
        write(folder,'review.md','# Проверка\n\nСверены существенное утверждение и применимость источника; редакционные решения отделены от внешних фактов. Повторов ответа в таблице нет. Фактических исправлений при этом проходе: 0. Редактура человеком и оценка времени ручной редактуры не проводились. Для manual сохранены два реальных прогона CLI; открытие preview в браузере, удаление и установка Python практически не выполнялись.\n\nСтатус ограничен: это внутренний пилот без обложки, WordPress и независимого редакторского решения.')
        # Leave editor attestation false: do not manufacture a human acceptance result.
        w.save(folder/'review.json',dict(article_sha256=w.digest(folder/'article.html'),coverage_checked=True,sources_reopened=True,visuals_checked=True,editor_reviewed=False,unresolved_material=[],corrections=[],reviewed_at=w.now()))
        for stage in ('article-brief','research','claim-ledger','outline','draft','visuals','fact-and-procedure-check','edit-and-package'):
            w.checkpoint(folder,stage,['brief.md','article.html','sources.json','claims.json','review.json','illustrations.md'])
        if kind=='manual':
            for stage in ('procedure-runner','screenshot-capture'): w.checkpoint(folder,stage,['procedure.json','screenshots.json','illustrations.md','article.html'])
        w.preview(folder); report=w.check(folder)
        elapsed=round(time.perf_counter()-tick,3)
        metrics=dict(started_at=started,checked_at=None,package_assembled_at=w.now(),assembly_seconds=elapsed,factual_corrections=0,manual_edit_minutes=None,reproducibility='CLI 3/3 twice; browser opening and rollback not exercised' if kind=='manual' else 'not-applicable',screenshot_quality='not-exercised',chart_quality='not-exercised')
        w.save(folder/'metrics.json',metrics)
        write(folder,'README.md',f'# {title}\n\nСтатус: {report["status"]}, внутренний пилот.\nБлокировка: нет решения редактора.\nWordPress: не загружено; публикация не разрешена.\nGitHub: ветка editorial/article-system, папка editorial/evaluation/{slug}.\nЛокальный preview.html создан; тема сайта не проверена.\nИсточники и границы: research.md, review.md, metrics.json.\nСледующий шаг: редакторская оценка и производственный пилот с реальными кадрами.')
        rows.append((slug,elapsed,metrics['reproducibility']))
    table='\n'.join(f'| {slug} | {seconds} | не достигнут | 0 | {repro} |' for slug,seconds,repro in rows)
    write(OUT,'REPORT.md','# Проверка системы: три ограниченных материала\n\nДата: '+w.now()+'\n\nЭто реальные короткие пилоты по проверенным основаниям, не полные публикационные статьи. Время ниже — только выполнение evaluate.py (сборка заранее подготовленного текста); исследование, разработка системы и редакторское время туда не входят. Оно не измеряет скорость создания качественной статьи.\n\n| Материал | Сборка, с | Проверенный редактором результат | Фактические исправления при сверке | Воспроизводимость |\n|---|---:|---|---:|---|\n'+table+'\n\nВсе три check честно оставляет unverified-draft: editor_reviewed=false. Время до проверенного редактором результата и объём ручной редактуры неизвестны (null в metrics.json). Ноль исправлений означает только отсутствие обнаруженных ошибок в этих коротких текстах, не оценку точности ИИ.\n\nМануал: два реальных прогона трёх CLI-команд в отдельных временных папках, с проверкой файлов, статуса и кодов возврата. Журналы initial/rerun сохранены. Не проверены действия установки Python, открытия страницы браузером и ручного удаления; вся инструкция целиком не аттестована. Скриншоты и числовые графики не требуются содержанию выбранных пилотов, поэтому корректность их производственного цикла не оценивалась. Это остаётся задачей интеграционного пилота в русском продукте.\n\nАвтотесты в tests/ проверяют блокировки: неподтверждённый факт, устаревший текст/проверка, непрогнанный мануал, английский или отсутствующий кадр, график без исходных данных, просрочка, выход пути за папку, перезапись и внешние ссылки. Положительный тест использует явно синтетическую редакторскую аттестацию; не считать его проверкой качества статьи.\n\nСледующий производственный прогон: выбрать реальную тему Windows, русскую тестовую среду, собрать исходные кадры и аннотации, построить график только при наличии чисел, измерить полный цикл, передать редактору с сохранением исправлений и времени. WordPress и публикацию этот запуск не затрагивает.')
    print(json.dumps(rows,ensure_ascii=False))


if __name__=='__main__': main()
