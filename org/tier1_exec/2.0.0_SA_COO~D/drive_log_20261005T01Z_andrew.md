# Drive log -- 2.0.0_SA_COO~D, 2026-10-05 00:1xZ-02:3xZ (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 00:1xZ | DSGN_REBRND R4-2 (FAST) | FWD-10 population | RULING: C10's population is the 18 content pages inside the shell's `<main>`. Census 15 of 18. Auth (4) and print sit outside `<main>`, /cma is a redirect, and /dev/page-surface-control is a test fixture. CLOUD 0dc80bec30 | DRIVE FORWARD |
| 00:3xZ | DSGN_IRPTV1 Y-2 (~Y 105051) | live thread | Driver case Bproxy. Offline drives showed the comparison step needs the selection's tenant, which the fixture lacks. The driver now records the page's own words. Queued for the walker behind ~M (MSTR 105067) | DRIVE FORWARD |
| 00:4xZ-01:4xZ | DSGN_REBRND R4-2 density part 1 (FAST) | FWD-10 page end | New `ui-smoke.mjs --density`. It found /market's page end at 0px (outside its column), eleven 24px columns, and no page end on failed /valuations and /correlations. Fixed: 15 of 15 at 20px, and failed/empty pages end. Pin page-end-spacing (DEV fails); batches 3-5 census at least one. LANDED portal DEV `e2315890` (ls-remote); pin to the CVO | DRIVE FORWARD |
| 01:11Z-01:41Z | DSGN_IRPTV1 Y-2 live | live thread | ARM (a collision with ~M was resolved by MSTR 105075 in this seat's favour). Bproxy live: NORMALIZED, Comparison card, Opal Ultra Long-Term picked; SUBMIT REQ-c1b537728b221742e335a0c8 01:18:56Z. READY 01:37:07Z (~Y 105086). DISARMED 01:41:31Z (login refused after); MSTR told | DRIVE FORWARD |
| 01:4xZ | IRPT_BCKEND (row) | surprise | The request never listed. The history pages by request id (ops/owned_requests.py:286-293); 22 reads, one body, 0 with the REQ. Row IRPT_BCKEND-S326 BLOCKING, owner ~Y; CLOUD d5068d85a4; ~Y told | RULED (row) |
| 02:0xZ-02:3xZ | DSGN_IRPTV1 item 100 (FAST) | live thread | The upload review read only v1 rows: blank Holding/Original amount and a raw total on the live run. It now reads v2 (symbol, amount + unit, dollars to the cent). Pin upload-review-v2-rows (DEV fails). LANDED portal DEV `56b71adb` (ls-remote). Real run: the live NORMALIZED answer replayed into 5174 (driver `--replay-normalized`), looked at | DRIVE FORWARD |

## Open

- R4-2 density part 2: the FWD-10 PROOF before/after on /market, /positioning and /portfolio-management with the named populated fixtures (rb-s-9 plus a new /portfolio-management fixture), and the sparse control. "Before" = a build at RB-s-9's parent (e216de95^).
- /portfolios and /security-analysis page ends: parked with their lease holders.
- IRPT_BCKEND-S326 (~Y): a newest-first history read.
- The next PROD promote carries 7b053135 through 56b71adb (Andrew's word).
