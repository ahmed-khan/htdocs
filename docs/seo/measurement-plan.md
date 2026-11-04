# Measurement plan

Two different measurements are tracked here. Lab scores come from PageSpeed Insights. Search performance comes from Google Search Console, which this project cannot open. Fill the Search Console cells yourself. Do not invent them.

## Lab baseline (authoritative before)

Source: PageSpeed Insights, Lighthouse 13.6.0, run by the owner on the live site `https://www.connectingahmad.info/` on 4 November 2026. No Chrome User Experience Report field data was available, so there is no field INP, LCP, or CLS to record.

| | Mobile | Desktop |
| --- | --- | --- |
| When | 23:35 GMT+3 | 23:41 GMT+3 |
| Device / network | Moto G Power, simulated slow 4G | Desktop |
| Performance | 100 | 97 |
| Accessibility | 100 | 100 |
| Best Practices | 96 | 96 |
| SEO | 100 | 100 |
| FCP | 1.3 s | 0.9 s |
| LCP | 1.3 s | 0.9 s |
| TBT | 0 ms | 30 ms |
| CLS | 0 | 0.002 |
| Speed Index | 2.2 s | 1.4 s |
| Field INP | not available (no CrUX data) | not available (no CrUX data) |

Mobile LCP of 1.3 s is already under 2.5 s, and CLS is already under 0.1. The work on this branch must not regress those lab scores. Best Practices at 96 is the score this branch is meant to move.

## Search Console baseline (owner fills this)

Export **Performance → Search results** for the 28 days ending the day before this change is published. Paste the top 10 queries by impressions. Leave a cell blank rather than guessing.

Date range exported: `FILL IN`

| # | Query | Clicks | Impressions | CTR | Average position |
| --- | --- | --- | --- | --- | --- |
| 1 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 2 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 3 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 4 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 5 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 6 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 7 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 8 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 9 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |
| 10 | FILL IN | FILL IN | FILL IN | FILL IN | FILL IN |

Also record these name queries even if they are outside the top 10. Use the query text exactly as Search Console shows it.

| Query | Clicks | Impressions | CTR | Average position |
| --- | --- | --- | --- | --- |
| dr ahmad raza khan | FILL IN | FILL IN | FILL IN | FILL IN |
| ahmad raza khan | FILL IN | FILL IN | FILL IN | FILL IN |
| ahmed raza khan | FILL IN | FILL IN | FILL IN | FILL IN |
| dr. ahmad raza khan | FILL IN | FILL IN | FILL IN | FILL IN |

## Targets after publish

Count days from the day the change is live on `https://www.connectingahmad.info/`.

**30 days**

- URL Inspection shows `/`, `/research/`, `/teaching/`, `/certifications/`, and `/contact/` as indexed (or “URL is on Google”).
- On the primary name query (`dr ahmad raza khan`, or the spelling that has the most impressions), CTR is at least 5%. If the baseline CTR in the table above is already above 5%, the target is double that baseline CTR.
- Write down clicks, impressions, CTR, and average position for the four name queries.

**60 days**

- CTR on that primary name query is at least 8%.
- Average position on that query is 5 or better.
- At least one impression exists for a query containing “cloud security” or “artificial intelligence” whose landing page is `/` or `/research/`.

**90 days**

- CTR on the primary name query is at least 10%.
- Average position on that query is 3 or better.
- Clicks on the four name queries combined are at least three times the baseline click total from the table above.
- `/research/` has impressions of its own in the Pages report.

Certificate PDF URLs were removed from the index on purpose. Impressions that used to come from those PDFs should fall. Judge success by clicks and CTR on the name, not by total impressions.

## How to measure

1. Search Console → Performance → Search results.
2. Set the date range to the 28 days you are judging. Compare it with the previous 28 days.
3. Filter queries with the query box. Filter pages with the Pages tab (`/`, `/research/`, `/teaching/`, `/certifications/`, `/contact/`).
4. After publish, open Sitemaps and confirm `https://www.connectingahmad.info/sitemap.xml` is read without errors.
5. Use URL Inspection on each new URL once, then request indexing if it is not yet known.
6. Re-run PageSpeed Insights on `/` and on `/research/` at 30 days. Keep a row for Performance, LCP, and CLS next to the baseline table. Mobile LCP should stay under 2.5 s and CLS under 0.1.
7. Field INP will appear in PageSpeed Insights only after Chrome User Experience Report has enough visits. Until then, record “no CrUX data” rather than a number.

## Lab result on this branch (not yet published)

Lighthouse 13.6.0, 4 November 2026, against this branch served locally with the same Apache compression and security headers the site will use. This is not a second PageSpeed Insights run of production. Production still has the “before” numbers above until this branch is published.

| | Mobile | Desktop |
| --- | --- | --- |
| Performance | 100 | 99 |
| Accessibility | 100 | 100 |
| Best Practices | 100 | 100 |
| SEO | 100 | 100 |
| FCP | 1.2 s | 0.4 s |
| LCP | 1.2 s | 0.9 s |
| TBT | 40 ms | 0 ms |
| CLS | 0 | 0 |
| Speed Index | 1.2 s | 0.5 s |
