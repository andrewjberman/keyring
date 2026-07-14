# OPAL_ASSETS: master plan issued, TO-6 started, ANDREW HOLD -- clean pause (23:10Z -> 00:25Z)

**Serial:** 0.4.0_DS_ClientPlatform | **Branch:** CLOUD | **State at close: PAUSED at c6ceb25a2 under Andrew's dispatch hold.**

## What happened, in order

1. **Grand consolidation mandate** (Andrew-direct): one `opal-data-assets` bucket -- smartx, orion/eclipse,
   the schwab EC2 box, etf issuers, black diamond (for cottonwood) -- bronze raw, silver parquet, gold master
   table. Highest priority. Brief amended with sec 0 (`b22182210`).
2. **Master plan authored + issued to CTO** (`9ce5b6841`):
   `deliverables/OPAL_ASSETS_MASTER_PLAN_20260713.md` -- 10-pipeline matrix (pull/bronze/silver/gold x
   measured status x schedule action), one-bucket keyspace spec, schedule board, 12 TOs in 3 phases.
3. **CTO ACK 00:07Z, ratifying into PRD.** Two rulings + one correction:
   - Ruling 1: `inf-canonical-prices-daily` stays HELD (INF-domain; out of the RE-ENABLE column).
   - Ruling 2: TO-6 (silver parser registry) authoring starts now; CBUGL parser waits for real 0833 bytes.
   - Correction: matrix row 1 "RUNS" was true of the CRON only -- the 0824 **pull has been functionally
     DEAD since 07-02** (rc=0 landing nothing; 0.6.2 grounded vs Schwab's live 5,966-file catalogue).
     *The cron firing is a statement about a SCHEDULER; only landed bytes are a statement about a PULL.*
4. **Corrections landed + TO-6 framework core landed** (`c6ceb25a2`):
   - Plan row 1 corrected with a correction log; prices row moved RE-ENABLE -> HELD.
   - `data/assets/scripts/silver/silver_registry.py`: H1 oracle (identity from the FILE's header, never the
     folder -- a misfiled 0833-under-0824 lands under 0833 with `scope_mismatch` SURFACED), parser registry
     (duplicate registration raises), quarantine (never a default master), `route()` with no silent branch.
   - `tests/test_silver_registry_identity_and_routing.py`: 9/9, includes the folder-trust mutant.
     Commit-gate clean (Rule 15 hit on the empty `tests/__init__.py` -- fixed, the gate works).
5. **CTO~B removal absorbed** (COO 23:56Z, Andrew-direct): route OPAL_ASSETS to CTO+COO. totalValue ruling
   recorded: **136,859,722.32 IS the number**; managedValue is a DIFFERENT QUANTITY; basis labels stay.
6. **ANDREW HOLD 00:21Z** (via CTO, verbatim): *"Wait to dispatch until I give the go, I want to respawn the
   workers first."* CTO's ruling-2 amended: **pause TO-6 at a clean commit point; stand down on OPAL_ASSETS
   until the post-respawn GO.** My five TOs (C6, C7, C10, C11, C12) are authored + committed + STAGED with
   the hold embedded in each file. Not a correction -- both rulings and my start preceded the hold.
7. **Pause validated + RAVC closed** (CTO 00:25Z): `c6ceb25a2` is the clean point; `git status` empty on
   `data/assets/`; the Schwab CRS parser increment was never started -- nothing half-authored.

## The one deliberate non-commit (recorded so no hygiene sweep mistakes it for lost work)

The `overlap_of` working-tree changes in `infra/aws/lambda/opal-assets/` are UNSTAGED **on purpose** --
committing them is an owned-paths lane violation (AE lane). **The canonical artifact is the committed patch:
`deliverables/overlap_of_FOR_AE_TO_LAND.patch` (499 lines, mutant-exercised, 59 tests).** The working-tree
copy is safely discardable; CTO has this on his record too (it explains the emitter SHA-drift in his
comp-blast run).

## State for the successor session (post-respawn)

- **PAUSED, not blocked.** Resume trigger = CTO's GO after Andrew's word, addressed to the live serial.
  Next TO-6 increment (never started): Schwab CRS parser against real 0824 bytes in the estate, then
  Orion/Eclipse against `opal-data-inf` bronze. Rule 17 binds every parser.
- The hold is in the record three ways: each staged TO file (verbatim), my heartbeat, this log.
- **Fences unchanged and not implied by the pause:** INF chain HELD; the sentinel key
  (`gold/meta/pipeline-complete.json`) is NEVER written; frozen 3 untouched; no mdpf run/trigger; nobody
  derives the 49F bucket relationship (0824 and 0833 are separate folders, separate figures, NO SUMMING);
  14->16 cohort expansion stays unimplemented until Andrew nods; legacy `opal-data-schwab` prefixes are
  inventory, not cleanup; CTO~B is gone -- route to CTO+COO.
