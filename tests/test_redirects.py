"""Old installed-app URLs must reach their corresponding canonical pages."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://banjonay1992.github.io/days-and-dues/'


class RedirectPage(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.refresh, self.canonical, self.links, self.robots = [], [], [], []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.refresh.append(attrs['content'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs['href'])
        if tag == 'a':
            self.links.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.robots.append(attrs['content'])


class RedirectTests(unittest.TestCase):
    def test_all_original_pages_have_immediate_matching_redirects(self):
        for name in ('index.html', 'support.html', 'privacy.html', 'terms.html'):
            target = BASE + ('' if name == 'index.html' else name)
            page = RedirectPage(ROOT / name)
            self.assertEqual(page.refresh, ['0; url=' + target], name)
            self.assertEqual(page.canonical, [target], name)
            self.assertIn(target, page.links, name)
            self.assertFalse(any('noindex' in value for value in page.robots), name)

    def test_matching_destinations_exist_in_the_canonical_checkout(self):
        canonical_root = ROOT.parent / 'days-and-dues'
        if not canonical_root.is_dir():
            self.skipTest('Canonical checkout is not available alongside this repository')
        for name in ('index.html', 'support.html', 'privacy.html', 'terms.html'):
            self.assertTrue((canonical_root / name).is_file(), name)
            self.assertNotIn('http-equiv="refresh"', (canonical_root / name).read_text(), name)


if __name__ == '__main__':
    unittest.main()
