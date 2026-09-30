# Drive log -- 2.0.0_SA_COO~D, 2026-09-30 14:24Z - 15:0xZ (DSGN_IRPTV1: loop armed; FAST item 38 W2-19)

Substantive ticks only; NO-OP ticks sit in the gitignored runtime file `org/mcp/drive_ticks/2.0.0_SA_COO~D.md`.
Host `andrew` (laptop). Loop: cron d49f1666, `4,14,24,34,44,54 * * * *` (LIVE_ARMS DIRECTED row, `/canonical-drive 10m`).

| Tick (UTC) | Limb | Act |
|---|---|---|
| 14:2xZ | CTO 103261 | L4-R ADMITTED (CVO half @9914eab4f4); the review's one condition for F carried (the next lease arm excludes `tabs/reporting/` + `dashboard/` or holds); hop 5 cut as this lane's closer-drive item, PARKED on B's series contract -- STATUS.md @580ae9145b; one line to the CTO |
| 14:28Z | tick 1 | Lease FAST to 14:58Z; inbox empty; 9 live; `org/standards/IRPT_DASHBD_*` absent (position 0 stays parked); 5174 200; portal DEV = origin 1d7b8feb. Top unblocked item: W2-19 |
| 14:3xZ | FAST item 38 build | UIC-14's ruling (view comment, CTO 102443/102444): vendor words come from a REGISTRY vendor view, never a hand-typed map. Measured: systems.json's 23 VENDOR rows carry `key` + `long` slugs only; `lib/opal_naming.py` VIEWS has FIRM_DISPLAY_NAMES, no vendor view. So the in-surface half: `holdingsFooterSource(snapshot, vendorWords=null)` words-or-fallback, the coordinate off the face; DrillTree hands the card the same string. iv-e-117 OK; iv-e-45 UIR-45d + iv-e-63 IVE63-2b re-goldened (both pinned the coordinate on the face); tsc 0; eslint 0 errors |
| 14:5xZ | real run | Fixture-plane footer driver on 5174: three "Source:" lines on the Holdings tab, one distinct string, 0 function-named, 0 served coordinates on the face -- VERDICT FOOTER-SOURCE-REAL-OK; shot read (card line, map footer, table footer identical). The card tile did not open under the driver's selector (the card's source prop is source-inspected in iv-e-117 ARM (b)) |
| 14:57Z | land | portal `775c4261` (5 files, msg-verify MATCH), `origin/DEV..HEAD` = this commit only, pushed; ls-remote DEV `775c4261b848` at 14:57:58Z. IR suite 949 pass / 27 skip / 18 fail = the known 18 (967 tests); wire dir restored to HEAD after the run (0 modified) |
| 15:0xZ | ask | The words half is the LGIC lane's (registry display words + VENDOR_DISPLAY_NAMES view): one line to 1.0.0_SA_CTO; STATUS.md next-list 1 carries it. W2-19b (Performance footer's `lineage.sourceCoordinate`, same class) added at position 2 |

State at 15:0xZ: portal PROD ba8e971f (v2.1.191); origin DEV 775c4261. Open at Andrew: re-smoke 775c4261 on 5174; PROD
promote; FCASH fold scope. Next item: W2-19b, then W2-01 front residue; IRPT_DASHBD hop 5 parked on ~P's series contract.
