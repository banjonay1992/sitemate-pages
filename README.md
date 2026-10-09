# Days & Dues compatibility pages

The full website now lives at https://banjonay1992.github.io/days-and-dues/.

Keep this repository and its Pages deployment available: existing installed versions can still link to these support, privacy and terms URLs. Each original page has an immediate meta refresh, a canonical URL and a visible link to its **corresponding** new page. Existing content and navigation remain available as a fallback when automatic navigation is disabled.

GitHub Pages cannot configure an HTTP 301. These are zero-second HTML redirects; [Google documents immediate meta refresh as a permanent redirect](https://developers.google.com/search/docs/crawling-indexing/301-redirects). Do not add `noindex` or block crawlers from these pages, as they need to discover the migration.

Run `python3 -m unittest discover -s tests -v` before changes. If the canonical site later moves to a custom domain, update all four destinations together and verify each live route. No custom domain is currently configured.
