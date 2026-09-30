# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 25, `HVST-o-5` (Lenovo's backfill on barrons / bbg / ft / wsj, and its same-day repeat) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~04:0xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round25/NEVER_WIDEN_HALF_COO_O5.md` @`f17ca57280` (msg 26895, READ-acked; read to EOF,
4,813 B).
**Ruling it serves:** `ROUND_ANALYSIS.round24.md` @6c5b4339a1 ruling 3. **Vendor authority:** R-21 @b390c36444. Andrew's words:
*"you have all the egress you want for vendors"*, and the mechanism *"deterministic/scripted in nature"*. The collector is that
script.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (~04:0xZ), with instruments independent of the COO's

- **The harvest roots, from the builder** (`store.table_prefix(SOURCE_FOR_PUBLISHER[p], ...)`, run by this seat): `barrons/harvest/`,
  `bloomberg/harvest/`, `ft/harvest/`, `wsj/harvest/` and `seeking-alpha/harvest/`, in bucket `opal-data-harvest`.
- **Object counts, by `aws s3 ls --recursive | wc -l`** (not the COO's boto paginator): barrons **30**, bloomberg **978**, ft **28**,
  wsj **55**, seeking-alpha (control) **103**. **They equal the COO half's signing snapshot on all 5.** Positive control:
  `derived/model_block/8035_JP_Equity/` read 5, as the CVO's v20 read.
- **Readers unmoved by this act:**
  - `amgt-resapp-chatter-axis` reads `CHATTER_AXIS_SOURCE=legacy` (this seat's `get-function-configuration`), so it does not
    read harvest silver.
  - The scoped API's `/timeline` reads silver only for keys in the served mention snapshot, which this act does not rebuild.
  - So no served page moves until a gold rebuild, as the COO half states.
- **Writers:** 3 named, 1 runs. The Scheduled Task is Disabled with 0 triggers, read by this seat at ~03:3xZ (ruling-2 amendment
  @e49bbdb3d2).

## 2. CONDITIONS

1. **The code at the act is the code at signing.** The executor prints `git rev-parse HEAD` and
   `git diff --stat 65aa9251bc HEAD -- lib/opal_data_harvest lib/research/harvest` immediately before run 1. Any change to those
   paths is a STOP and a re-sign. `HVST-o-2`'s flag change (`run-local.ps1`) and `o-3`'s tie-break (`store.py`) are named
   exceptions only if the diff shows exactly those hunks and neither touches the grammar path's fetch or put.
2. **`o-5.before.py` (without `--signing`) reads BEFORE == signing on every publisher, immediately before run 1.** A drift STOPS
   the act, including an `o-4` sa write, as the COO half states.
3. **Only scripted egress:** every publisher request goes through the collector. An agent-side HTTP call is a STOP (R-21).
4. **Branch B is not retried in-session.** A challenge, deny or failure is recorded in the run record, and the next round reads
   it. There is no login and no browser session opened by the agent.
5. **After both runs:**
   - `o-5.AC1.py` / `o-5.AC2.py` pass: 0 pre-existing objects moved or removed on the 5 roots; 0 new sa objects; only
     `992_HK_Equity` jobs.
   - Run 2 reads `counts.fetched == 0`.
   - The printed plan (the ceiling, round-24 ruling 2) is recorded beside the ACTUAL pages walked per publisher.

## 3. ROLLBACK

The COO half stands: forward only, because every put is never-overwrite. Removing a new object is an S3 delete, which is Andrew's
act. The run records list every key. The exposure is new bronze and silver objects for one security, unread by any served page
until a gold rebuild.

## 4. NOT COVERED

- sa (the renewal is pending);
- any other security;
- any gold build;
- any schedule change (reserved to Andrew, HANDOFF `:81`);
- any deploy;
- a third run.

## AMENDMENT 1 -- RE-SIGNED (~04:4xZ, on 2.0.0_SA_COO~H msg 26908, COO half AMENDMENT 1 @a0134b0467)

**The act, amended:**
- `--publishers bbg ft wsj --max-jobs 3`, run twice.
- barrons is Branch B from attempt 1 (`request_rejected`, a challenge, 0 objects) and is not retried, per condition 4.
- barrons joins sa as a root that must gain no object.

**Re-measured by this seat:**
- **Roots, by `aws s3 ls --recursive | wc -l`:** barrons 30, bloomberg 978, ft 28, wsj 55, seeking-alpha 103. These are
  unchanged from signing, and attempt 1 wrote nothing.
- **The executor's code:** worktree `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r25-65` at `51f7dd7c6f`, with an empty
  `git status` on `lib`. `git diff --stat 65aa9251bc HEAD -- lib/opal_data_harvest lib/research/harvest` shows 2 files,
  `README.md` and `run-local.ps1`: `o-2`'s flag, outside the fetch and put path. **Condition 1 holds in that worktree.**
- **⚠ The shared trunk is NOT the signed code.** At CLOUD `a0134b0467` the same diff shows 10 files, including `worker.py`
  (+105, `o-1`), `store.py` (+36, `o-3`) and `publication_gold.py`. **Running the act from the trunk, or from any tree whose
  diff exceeds `o-2`'s two files, is a STOP and a re-sign.** The executor prints the worktree path, HEAD and that diff
  immediately before run 1.

Everything else in this half stands: conditions 2-5, the rollback, and NOT COVERED.
