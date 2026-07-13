# HANDOFF -- device reboot / clean restart (1.0.0_SA_CTO, 2026-07-13T19:41Z)

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE, DIAGNOSE
**purpose:** Andrew is rebooting the device. Every agent session dies. This is the zero-context
handoff for the next session. READ THIS FIRST, then `org/XXX.md` startup.

---

## TL;DR FOR THE REBOOTING OPERATOR (read this, then the DO-NOT-TOUCH list)

- **INF gold pipeline is DELIBERATELY FROZEN and SAFE.** Nothing has served since 2026-07-10.
  The freeze is CORRECT -- do not "fix" it to unblock the chain.
- **Nothing was served, stamped, or deployed tonight.** An Andrew-ordered production serve was
  GROUNDED TO A FULL STOP by the fabric before any irreversible write. All rollback material unused.
- **Two Andrew-direct SOVEREIGN rulings today** (see below): (1) NNA time-locked by account to
  advisor; (2) bronze is RAW ingest -- `.jsonl.gz`/JSON at bronze, `.parquet` is a SILVER format.
- **The real fix serves 2026-07-14+, in the order FOLD-THEN-LOCK, co-signed.** NOT tonight.
- **Patrick Scanlan is short $52,604.80 on the served spine** (a phantom advisor holds his money).
  That shortfall is currently a LOAD-BEARING GUARD -- see DO NOT TOUCH #4.

---

## CURRENT STATE (grounded on live primitives at 19:41Z, not memory)

```
DISPATCH HOLD:   inf-gold-trigger  INF_GOLD_DISPATCH_RELEASE = None (ABSENT = HELD, fails closed)
                 EventBridge: inf-gold-full-on-bronze-complete = DISABLED
                              inf-canonical-prices-daily        = DISABLED
SERVED SPINE:    platinum/firm/advisor_nna_canonical.json  LastModified 2026-07-10 (UNTOUCHED)
NOTHING STAMPED: gold/canonical/canonical_nna_2026-07-13.parquet -> 0 objects
                 scratch/timelock_observe_* -> 0 objects (the guard blocked the write, by design)
SSOT (NEW):      gold/dimensions/aor_resolution.parquet -> CREATED TONIGHT 15:11:46Z (INF_A_0's
                 first run ever; 873 accts, fold OFF, 0 movers, 0 unresolved; reads only fresh
                 accounts_v2; fired no downstream trigger). This is a real, clean step forward.
BACKUPS (unused, for rollback if ever needed):
   s3://opal-data-inf/backup/gold_canonical_PRE_REDERIVE_20260713T1012Z/   (8,805 obj, ETag-verified)
   s3://opal-data-inf/backup/served_spine_PRE_TIMELOCK_2026-07-13T184646Z/
```

## *** DO NOT TOUCH (each one would cause a client-facing, often IRREVERSIBLE, defect) ***

1. **DO NOT SERVE / RUN the gold chain to production.** Serving NOW is LOCK-WITHOUT-FOLD: the
   time-lock stamp is IMMUTABLE by design, and tonight the AoR fold (the thing that CORRECTS the
   attribution) is a NO-OP (0 movers; `advisor_of_record_raw` lands ~13:22Z on 07-14). Measured:
   time-lock output tonight == current numbers, $0.00 delta on EVERY advisor. **Serving now would
   FREEZE the $2.6M misattribution + Patrick's $52,604.80 PERMANENTLY.** Correct order: FOLD then LOCK.

2. **DO NOT de-collide `build_assets_dim.py` OR `_orion_api_silver_lib.py`.** Both exist in BOTH
   `code/gold/` and `code/silver/` (different content). `sync_scripts()` FATALs on them at STEP ZERO
   -- which is WHY the whole chain (bronze pull AND gold) has been dead since 07-10. **That accidental
   bad deploy is the ONLY thing protecting the served spine.** De-colliding == opening "door 5" ==
   releasing gold. No `aws s3 cp`, no `aws s3 rm`, no "tidy code/silver", into those two prefixes.

3. **DO NOT repair/restart/kick the EC2 bronze runner to unblock the chain.** Repairing bronze ==
   de-colliding == releasing gold (same object as #2). The bronze runner is dead since 07-10 (2 dims
   -- transactions + performance -- DARK, no other producer). Reviving it is entangled with the
   collision + the guards; it is a deliberate daylight sequence, not a fix.

4. **DO NOT deploy the SILVER rep_id rescue tonight** (`data/inf/scripts/silver/convert_transactions_to_silver.py`,
   the household-rep rescue for accts 560/703/1225, SERVE-HELD/NEVER#2). **Patrick's $52,604.80 phantom
   is currently THE GUARD** -- `assert_no_residual_advisor` fired on it and blocked tonight's write.
   "Fixing" Patrick removes the guard, and then a LOCK-WITHOUT-FOLD run would SUCCEED and stamp the
   defect forever. Deploy it 07-14 AFTER the fold, not before.

5. **DO NOT rewrite `data/` bronze producers to `.parquet`.** Andrew's ruling (below) makes jsonl.gz
   the CORRECT bronze pattern. My earlier "parquet direction" ruling is STRUCK. code/silver + code/gold
   are frozen (COO). Rewriting data/ would cement an architectural violation into the canonical repo.

## ANDREW-DIRECT SOVEREIGN RULINGS (2026-07-13) -- both binding, both in memory

1. **NNA IS TIME-LOCKED BY ACCOUNT TO ADVISOR.** *"backfill the first appearing AoR per account";
   history NEVER re-attributes; a later AoR change applies FORWARD only.* + **HONOUR THE HOUSE ACCOUNT**
   (`inflection_wealth_management` IS an AoR for the period an account sits in it; do NOT normalize).
   The two poisoned roster snapshots (2026-04-28 = 96% catchall; 2026-05-08 = 0 rows) MUST raise, not
   skip. Full: `memory/project_nna_time_locked_by_account_to_advisor_andrew_ruling.md`.

2. **BRONZE IS RAW INGEST.** *"bronze ingestion is a raw ingest, it does not convert to parquet on raw
   ingestion. we do a parquet conversion at the SILVER layer, silver files are parquets, that is the
   pattern."* -> `bronze/{dim}/{snap}.jsonl.gz` (and raw JSON) is CORRECT; `.parquet` at bronze is the
   VIOLATION. The 4 deployed Lambda producers are the violators; the dead EC2 jsonl.gz runner was the
   only compliant one. **`bronze/orion-api/**` raw JSON IS compliant.** CLAUDE.md Rule 17a patch
   prepared (`20966ecb6`, "patch for CTO") -- VERIFY it landed and is committed.

## THE 07-14 SERVE PLAN (the fix, in the correct order)

```
07-14 ~13:22Z: advisor_of_record_raw lands (from inf-accounts-v2-daily's OWN raw-JSON pull of
               bronze/orion-api/{date}/accounts_roster.json -- CLEAN of the dead EC2 runner AND
               of the parquet violation; 0.7.0 traced it on deployed bytes).
THEN, in order (NEVER lock-before-fold):
  1. FOLD runs -> performs the AoR correction ($2.6M drift, movers re-keyed).
  2. LOCK/STAMP the CORRECTED attribution (immutable, once).
  3. Deploy the SILVER rep_id rescue -> Patrick's $52,604.80 comes home; phantom gone; guard passes.
  4. Serve -> co-signed (CTO + COO; COO's 3 conditions banked, cond.1 = lift scoped to ONE run,
     re-arm on CVO's served-row read).
```
**CAVEAT the next session MUST verify (0.7.0, 194202Z):** advisor_of_record coverage is **28.9%,
not 100%** (900 of 3,118 rows AoR-populated), and the **07-11 roster is MISSING**. So the 07-14 fold
may correct only ~29% of movers. Ground the coverage before promising a complete serve.

## FABRIC FIXES LANDED TODAY (do NOT re-investigate -- they are done + exercised)

- **The 08:19Z "crash" was NOT a reboot** -- WindowsTerminal.exe faulted under a 43GB runaway python
  (commit limit 46.2GB). `mem-sentinel.ps1` armed to name the next one (`3edf3b029`). python PID 19224
  UNIDENTIFIED -- if it recurs the sentinel names it; a quiet week is UNRESOLVED, not fixed.
- **never-rules-gate** hardened: override-marker disarm (`0332d5d55`), P1 negative-control-red +
  commit-msg-execution hole (`071fbda9f`). 9/9 neg-controls PASS, real hazards DENY.
- **NFRA_IDENTITY:** `deregister_agent` ~lane-suffix bug F-024 (`47163c850`); deregister audit F-004
  (`e5fcb9e58`); orphan-cleanup hook (`920a7bb77`) + its marker-version fix F-003b (`8dfece4dc`).
- **Governance audit logs** (13 logs, 34,180 lines) were UNTRACKED -> now snapshot-archived + tracked
  (`fcff61ebc`); live logs stay gitignored (no merge conflicts).
- **CLAUDE.md** refactored 15,118 -> 3,652 words; doctrine -> `docs/doctrine/`, incidents ->
  `docs/references/INCIDENTS_2026-07-13.md` (`71b37d07d`).

## NEXT SESSION -- FIRST ACTIONS (in order)

1. `/watcher` + `org/XXX.md` startup. Expect the broker to show STALE agents post-reboot -- re-register.
2. **Re-confirm the DO NOT TOUCH state on live primitives** (dispatch RELEASE absent, spine at 07-10,
   nothing in gold/canonical 07-13). If ANY changed, the hold was breached -- investigate before anything.
3. **Verify CLAUDE.md Rule 17a (bronze=raw) is committed** (`20966ecb6`).
4. **Trace the 07-14 coverage caveat** (28.9% AoR, missing 07-11 roster) before committing to a complete serve.
5. Do NOT drive the serve until 07-14 fold-inputs land AND CVO clears the corrected numbers on the artifact.

## OPEN THREADS / OWNERS (event-driven; nothing on a clock)

- **DS (0.4.0):** the time-lock is deployed + proven-sound; owns the 07-14 fold->lock->silver-rescue serve.
- **0.7.0_AE_CloudOps:** owns the bronze-runner root cause + the layer-consolidation gate (now DIRECTION
  = raw/jsonl per Andrew; my parquet ruling struck). Owns the dispatch-hold control.
- **CVO (3.0.0 / ~B):** validation lane; must read the served/scratch artifact (NEVER#5) before any serve.
- **COO (2.0.0):** drive + co-sign (granted, banked for 07-14, 3 conditions).
- **Andrew:** $2.6M advisor-credit correction is his ruling (done); the 07-14 serve is his GO.

**Nothing is degrading. The freeze holds itself. The fix lands 07-14 in the right order. Every dangerous
action tonight was caught by the fabric grounding it -- including two of the CTO's own.**
