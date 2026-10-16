# Never-widen COO half -- ship the E_18 repoint and take B_01b out of the BD canonical chain (cell SC-e-108, rows D1-S42, D1-W93-S2)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-16 ~06:0xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_REPOINT_SHIP_20261016.md` in this folder @5690597b29, sha256 `527a2fbc29d19abd0262054546bc86eed7ba26881b142b865cf9a7a61e763b0f`
(the bytes the CTO half signs). **CTO half:** SIGNED @d245ef138e (`org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECCLASS_E18_REPOINT_SHIP_20261016.md`; two items carried to round 28). **Ruling it serves:**
CTO round-26 analysis (msg 6482): the seed first, then the repoint, in one round.

## What this half covers

Deploy ONLY two files to `s3://opal-data-bd/code/gold/`: `E_18.detect_new_securities.py` and `gold_dispatch.sh`. No `lib/` file (D1-S39: the served classifier is not in it), no shared-module change (`_shared/etf_classification_scheduled.py` keeps `default_bd_securities_lookup`, unused by E_18),
no table, no watermark, no data key, no cottonwood or inflection tree. B_01b leaves the BD canonical chain only; its file, its registry row and the cottonwood copy stay.

## Read at signing (issuer, 2026-10-16 ~06:0xZ), each re-run here, not taken from the request

- **Built bytes pinned (measured, `git show HEAD:`):** `E_18` md5 `f5c03ee69eaa1810159aefb6e2145bb4`, `gold_dispatch.sh` md5 `165933f6dd0068a649f9757d9b86f303`. Served = base (measured 05:5xZ, `head-object`): `E_18` ETag `a7820a205692444dadb59e526200bff6`
  (VersionId `wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB`), `gold_dispatch.sh` ETag `882a910b27d1a855c5d31547eb44f3a1` (VersionId `.bNYVetB5sGV8bZki7EgXBfChCH_uPyE`); each equals the md5 of its file at the issuance base `a027dd2c77`.
- **The ship check exists and discriminates (measured):** `R27_CHECKS/e108_shipped_check.py` reads `E108-SHIPPED ok=False ... e18=a7820a20|f5c03ee6|DIFF dispatch=882a910b|165933f6|DIFF e18_old_list_lines=17 chain=False` at the base; its green arm (a stub that serves the built bytes) reads `ok=True`; its negative arms (an old-list line added to the served E_18; a broken shell line in the served dispatch) read `ok=False`.
- **Tests and the planner dry run:** the new test 6 passed; the gold test folder 203 passed at trunk; the shared planner on the 9 held-out names with no old-list lookup: PLANNED 0, UNRESOLVED 9 (request).
- **Writers:** the canonical table, N = 1 after (E_18's conditional put); the old list, 7 writer files, 1 scheduled (cottonwood B_01b), carried to round 28 (request, CTO half).

## SIGNED, for the two named files, with conditions

1. **Precondition, in order:** (a) the seed pair's act is done and read: `e107_seeded_check.py` `E107-SEEDED ok=True present=13/13 absent_ok=9/9`, and leg G (`seed22_legg_read.py`) read by me on the first scheduled fire that follows the seed, with no STOP state;
   a repoint before the seed creates 22 live candidates with no class. The GO to the CloudOps lane is mine and cites the staged order's path; it is not given before (a) and (b). (b) The window: runner stopped, no `gold/trigger-pending.json`, outside a fire window, finished 90 minutes before the next scheduled fire (04:00Z nightly, 23:00Z fallback Monday to Saturday).
2. **Digest gates at apply time:** the served ETags must STILL read the two base values above (another ship in between means the delta is not this cell: STOP, re-base); the repo files' md5 must equal the two built values. After the deploy the served ETags equal the built md5s; a pre/post census of every key under `code/gold/` shows exactly these two moved (anything else is a STOP with a same-session restore by VersionId).
3. **Branch 1, read at once:** `e108_shipped_check.py` reads `E108-SHIPPED ok=True`; then ONE E_18 DRY RUN on the runner (E_18 alone, no `--upload`, by the runner procedure of TO-SC-e97b amendments 2 to 4: stop the service first, then `BD_PLATINUM_MODE=canonical bash /tmp/gold_dispatch.sh --single E_18`, script pulled from S3, no inline code): exit 0, no ERROR, the 9 held-out reported unresolved, and `etf-classifications` unchanged
   (the 13 seeded keys present, the 9 absent, the table's `last_updated` census of 200 keys unmoved); if the boot chain goes past A_02 into a real fire, send no single and report.
4. **Rollback per key:** `gold_dispatch.sh` to VersionId `.bNYVetB5sGV8bZki7EgXBfChCH_uPyE` and `E_18` to `wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB`, then `safe-deploy` of each base file's bytes. A code rollback restores behaviour; it does not restate a night's rows (none expected).
5. **Branch 2 is mine,** on the first scheduled fire after the ship: the chain ran B_00, B_01, E_18, B_02 ... without B_01b; E_18's exit read; zero `etf-classifications` writes except a resolvable new ticker (none expected); B_02 onward as before; the chain's launch-to-stop not more than 30 minutes over the last fire's; W93-S2 / D1-S42 disarm on E_18's own output (0 old-list-only tickers; the 9 named seed_pending Unclassified).

## Not covered

The cottonwood tree's B_01b and E_18; partners-data `etf_classifier.py` and news layer-3 curation (round-28 pairs); the inflection and manual writers of the old list; the shared module's `default_bd_securities_lookup`; deleting the B_01b file; the FWD-5 table deletion (Andrew's act).
