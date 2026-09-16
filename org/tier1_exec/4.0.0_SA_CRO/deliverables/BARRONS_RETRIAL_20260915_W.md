# Barron's click-and-drag retrial: passed

Seat `4.0.0_SA_CRO~W`; measured 2026-09-15 13:18–13:22Z.
Authority: `ANDREW_DIRECT_20260915_BARRONS_RETRIAL_W.md@4c20ac6c7f`.

## Result

Two genuine visible slider challenges cleared with the existing canonical headful helper. Each recorded one scripted drag, no detected Windows operator input, no credential entry, valid structured search JSON and verified subscriber access. The second trial then used its recovered browser bundle in the canonical HTTP client, retrieved a fresh native REST article successfully, and saved the recovered bundle in the current-user DPAPI vault.

This supplies the independent slider evidence missing from the earlier commissioning report. Andrew's original manual drag remains human-assisted. Two passes do not establish indefinite reliability; the worker's automatic Barron's recovery gate remains disabled pending its separate retry-path acceptance check.

## Trials and screenshots

Folders below are under `.runtime/opal-data-harvest/verification/`. Each contains visually inspected `before.png` and `after.png`, plus `verification-proof.json`.

| Run folder | Challenge | Script drags | Operator input detected | Outcome |
|---|---:|---:|---|---|
| `20260915T131803Z-barrons-user-trial` | No | 0 | No | Existing session, subscriber check and fresh REST article passed; not a CAPTCHA pass. |
| `20260915T131928Z-barrons-home-trial` | Yes | 1 | No | Slider cleared; search JSON and subscriber check passed. Probe did not save recovered bundle. |
| `20260915T132022Z-barrons-user-trial` | Yes | 1 | No | Slider cleared; search and subscriber checks passed; fresh REST article passed; bundle saved. |

Both homepage runs visibly progressed from the verification screen to the signed-in homepage. The prompt was **Slide right to secure your access**. The canonical helper located the prompt, then used one mouse-down, a 35-step horizontal drag, and mouse-up. No NopeCHA request or article DOM extraction occurred. The existing Windows input-clock instrument recorded no activity during either browser run; that is its measured evidence, not a claim of detecting every possible input mechanism.

## Article and saved session

- Route: `https://www.barrons.com/articles/api/articles/navys-next-fighter-boeing-vs-northrop-6c3b691f`.
- Fresh HTTP 200, response 134,370 bytes; ID `WP-BAR-0001908718`.
- Clean JSON: **507 words**, publisher count **524**, `content_status=complete_candidate`, `issues=[]`, `transport=json`.
- Body SHA-256: `339822f0a415a7b2abcdb311be7ddbbe365e9782f01ed05a7441cb614cbba0ad`.
- This deliberately refetched one known article to isolate recovery; it is not new discovery or batch coverage evidence.
- Recovered session saved to `.runtime/opal-data-harvest/secrets/barrons.dpapi` only after the article passed. No token values appear in this report.

## Reproduction and hashes

Wrapper `.runtime/opal-data-harvest/trial_barrons_20260915.py --homepage` loads the current vault, calls canonical `repair(... allow_experimental=True)`, then `Publisher.check_auth()` and `DowJones.article()`. The separate probe is `trial_barrons_home_20260915.py`. No canonical helper implementation change was required.

Canonical `lib/opal_data_harvest/verification.py` SHA-256: `a2811f9f817c362fac4224543172fd32f47b2f25b2f254df1accb2f480dab2a4`.

Final run evidence hashes:

- `before.png`: `f87037bf0d951ab1c2b5aa953fd5113d5fb0cb683f230ff801bff0838a456161`.
- `after.png`: `2fd15905945e000290b459a31b28f9f5982e80a9c2d99967dc7e581257cca1a0`.
- `trial-summary.json`: `4e930a872c7deaab00124bbd0f6c492cc31d2a50408f60f7742c7f8788ea9b9a`.
- `article.json` holds the normalized body in that same final run folder.

The local Windows harvest task was checked: Disabled, zero triggers. Config flags `recurring_schedule_enabled=false` and `automatic_uploads_enabled=false`. No upload or recurring collection was started. Gradual backfill cadence remains Andrew's decision.
