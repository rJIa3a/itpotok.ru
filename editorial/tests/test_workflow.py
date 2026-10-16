import importlib.util
import tempfile
import unittest
from pathlib import Path
from datetime import date, timedelta

spec = importlib.util.spec_from_file_location('workflow', Path(__file__).parents[1] / 'workflow.py')
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


class EvidenceGateTests(unittest.TestCase):
    """Synthetic attestations exercise gates, not editorial truth."""
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name) / 'example'
        w.init(self.folder, 'explanation', 'test', '')
        for name in ('research.md', 'outline.md', 'illustrations.md', 'review.md', 'faq.md', 'excerpt.txt'):
            (self.folder / name).write_text('Synthetic fixture', encoding='utf-8')
        (self.folder / 'article.html').write_text('<p data-claims="C1">Fixture claim</p>', encoding='utf-8')
        w.save(self.folder / 'sources.json', [dict(id='S1', url='https://example.org', title='Fixture', excerpt='Fixture evidence', checked_at=w.now())])
        w.save(self.folder / 'claims.json', [dict(id='C1', claim='Fixture claim', source_id='S1', evidence='Fixture evidence', checked_at=w.now(), next_review=(date.today()+timedelta(days=30)).isoformat(), status='supported', material=True, location='p')])
        w.save(self.folder / 'review.json', dict(article_sha256=w.digest(self.folder / 'article.html'), coverage_checked=True, sources_reopened=True, visuals_checked=True, editor_reviewed=True, unresolved_material=[], corrections=[], reviewed_at=w.now()))
        self.points()

    def points(self):
        for stage in ('article-brief', 'research', 'claim-ledger', 'outline', 'draft', 'visuals', 'fact-and-procedure-check', 'edit-and-package'):
            w.checkpoint(self.folder, stage, ['article.html'])

    def test_complete_attestation_passes(self):
        self.assertEqual(w.check(self.folder)['blockers'], [])

    def test_uncertain_material_blocks(self):
        claims = w.read(self.folder / 'claims.json'); claims[0]['status']='uncertain'; w.save(self.folder / 'claims.json', claims)
        self.assertTrue(any('Unresolved material' in p for p in w.check(self.folder)['blockers']))

    def test_old_review_and_checkpoint_block_changed_text(self):
        with (self.folder / 'article.html').open('a') as f: f.write('<p>Changed</p>')
        problems=w.check(self.folder)['blockers']
        self.assertTrue(any('current article' in p for p in problems))
        self.assertTrue(any('Stale checkpoint' in p for p in problems))

    def test_manual_without_real_runs_blocks(self):
        state=w.read(self.folder/'workflow.json'); state['format']='manual'; w.save(self.folder/'workflow.json',state)
        self.assertTrue(any('No successful rerun' in p for p in w.check(self.folder)['blockers']))

    def test_missing_and_english_screenshot_block(self):
        w.save(self.folder/'screenshots.json',[dict(status='verified', file='absent.png', environment=dict(language='en'))])
        problems=w.check(self.folder)['blockers']
        self.assertIn('Screenshot interface is not Russian',problems)
        self.assertIn('Missing safe original',problems)

    def test_chart_without_data_blocks(self):
        w.save(self.folder/'visuals.json',[dict(type='chart',status='verified',file='absent.svg')])
        self.assertIn('Chart lacks data/script',w.check(self.folder)['blockers'])

    def test_expiry_refresh_invalidates_status(self):
        claims=w.read(self.folder/'claims.json'); claims[0]['next_review']='2000-01-01'; w.save(self.folder/'claims.json',claims)
        self.assertTrue(w.refresh(self.folder))
        self.assertTrue(any('Expired claim' in p for p in w.check(self.folder)['blockers']))

    def test_paths_cannot_escape(self):
        with self.assertRaises(ValueError): w.local(self.folder,'../secret.txt')

    def test_init_preserves_existing_folder(self):
        with self.assertRaises(FileExistsError): w.init(self.folder,'manual','new','')

    def test_nofollow_rule(self):
        with (self.folder/'article.html').open('a') as f: f.write('<a href="https://example.org" target="_blank">source</a>')
        self.assertIn('External link lacks nofollow',w.check(self.folder)['blockers'])


if __name__ == '__main__': unittest.main()
