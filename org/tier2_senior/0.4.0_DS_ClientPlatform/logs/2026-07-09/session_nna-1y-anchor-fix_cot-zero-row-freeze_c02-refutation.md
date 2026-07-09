# Session: advisor-NNA 1Y window-anchor fix; cot 18-day 0-row snapshot freeze (self-caused, self-found); C_02 cert-freeze refutation

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-07-09 (~18:55Z - 21:35Z; see ADDENDUM at end -- the period-roll defect ALREADY FIRED in production)
**Branch:** CLOUD

---

## Current State

Three threads, all landed or correctly parked. Written for a reader with zero prior context.

### 1. GCONTR advisor-NNA 1Y cross-route divergence -- FIXED + DEPLOYED, NOT SERVED

**Root cause (SOURCE-CONFIRMED + EXERCISED).** `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py:1234`
anchored ROLLING window STARTS on wall-clock `_today()` (`lib/gold_utils.py:102-103`,
`pd.Timestamp.now(tz='UTC')`) while the window END stayed the data date `latest_date = detail['date'].max()`
(`D_00c:817`). `D_00f.advisor_nna_canonical.py:319-337` anchors BOTH bounds on
`data_as_of = nna['date'].max()` (`D_00f:814`). With the live 2-day ingest lag (data_as_of=2026-07-07,
today=2026-07-09) the leaderboard's 1Y window was `[2025-07-09 .. 2026-07-07]` vs canonical
`[2025-07-07 .. 2026-07-07]` -- it silently dropped the leading 2 days of flow.

**Why only 1Y presented (the other windows were not fine -- they were lucky).** QTD/YTD/MAX are
calendar-anchored, so a 2-day skew cannot move them. 3Y is rolling and was EQUALLY mis-anchored; its
dropped band was 2023-07-08 Sat + 2023-07-09 Sun -- **0 business days, $0.00 firm flow** -> converged by
calendar accident. 1Y's band was 2025-07-07 Mon + 2025-07-08 Tue -- **2 business days, $3,516,778.16** ->
65/158 advisors diverged, MIXED direction because per-advisor band flows carry both signs.

**Exercised (falsifiable, could have failed).** Predicted `canonical_1Y(adv) - leaderboard_1Y(adv) ==
sum(nna_txn)` over the dropped band, per advisor. **HELD 158/158, residual <= $0.01**, reproducing AE's
counts exactly (65 divergent; 38 canon>lb / 27 canon<lb; worst Hunter Lloyd $1,566,083.10). Recomputing the
FIXED window off the atomic source: 1Y **0/164 divergent**, 3Y 0/164 and **0 advisors' 3Y value moves**
(value-neutral where already correct).

**Second, more severe latent defect closed by the same fix.** A `today`-anchored QTD/YTD/MTD start lands
AFTER `latest_date` at a month/quarter/year roll (e.g. today=2026-10-01, data=2026-09-29).
`_employee_entries_for_window` returns `[], {}, {}` on an empty window (`D_00c:394`), so the SERVED
leaderboard would emit **ZERO advisors for QTD on the first days of every quarter**. bd's lag is 2 days,
so 2026-10-01/02 would have hit it. Now unreachable + a fail-loud tripwire raises instead.

**Commits (both sha256-verified repo == S3):**
- `2af63847d` D_00c: `anchor = latest_date`; all rolling + calendar windows derive from it. `_emit_window()`
  single emit path + tripwire (`raise` if `w_start > latest_date`). Publishes per-window `window_bounds`.
- `3ea2bdbf9` D_04: the REAL publisher is `build_firm_leaderboard` (`D_04:2188`), NOT `build_firm_dashboard`
  -- it rebuilds the served artifact field-by-field, slimming 9 windows to 5 and dropping unnamed keys, so
  `window_bounds` would have died at `gold/artifacts/employee_leaderboard.json`. Now propagated; degrades to
  `{}` against a pre-fix source artifact (no run-order coupling).

**STATUS: deployed, NOT served.** No ad-hoc gold run (CLAUDE.md NEVER rule). `3.0.0_SA_CVO` is
HARD-WITHHOLDING the SEV1 `advisor-intelligence-nna` ratification until the served artifact confirms
post-nightly -- at my request, on my own work. F-1 on 1Y correctly reads RED right now.

### 2. cot 18-day 0-row snapshot freeze -- self-caused, self-found, escalated (P0-class)

`cot silver/allocations` + `silver/unrealized` have been header-only 0-row stubs since **2026-06-22** (18
days). Row-counted, never bytes: bronze `ALLOCATIONS_DAILY_2026-06-15` = 1,278 data rows;
`2026-07-08` = **0**. `silver/allocations/2026-07-09.parquet` = **0 rows, 59 cols** (the constant 32,535 B is
bare parquet schema). PERIOD tables (realized, transactions) unaffected -- the SNAPSHOT-vs-PERIOD split
`SNAPSHOT_TABLES` predicts.

**Cause: my own commit `a7a4d974c` (06-22)** set the snapshot tables `CurrentDay -> ("Custom",14)`. Under
Custom the as-of END is `run_date = args.date or _today_utc()` (`cot_bronze_ingest.py:890/:264`, wall-clock
UTC) and the runner fires 02:00Z. `CurrentDay` had masked it by ignoring dates. The AUAFIX traded a
mis-stamp freeze for a zero-row freeze.

**MECHANISM AMENDED -- my stated reason was FALSIFIED, retracted in both places I asserted it.** I claimed
"BD returns header-only for a date not yet complete in ET" (reading `cot_bronze_ingest.py:79-80` as
grounded). 0.6.0's COTTONWOOD probe at 15:53 ET on 07-09, before the close, same tenant/as-of/minute:
`allocations(qt5) = 0`, `unrealized(qt4) = 0`, **`holdings(qt1) = 11,754 rows`**. **The discriminator is
QUERY TYPE, not day-completeness.** Why qt4/qt5 withhold is `HYPOTHESIS, NOT CONFIRMED`. If it is a
settlement/T+1 cycle, **no business-date arithmetic fixes this and the lever is the CRON TIME.** Root-fix
design HELD pending 0.6.0's publish-lag curve rather than built on the falsified premise.

Corollary correction: holdings is not spared by "its retry-net catching a stub." BD *hands* it real rows;
they return **unvalued** (604,078 B vs 853,273 B last real) and the nzf floor -- my own `fdd5f28d4` guard --
rejects them, so it HOLDS at 07-07.

**Lineage, SOURCE-CONFIRMED (CTO made his severity ruling provisional when I flagged it rested on a code
comment):** served cot AUA <- `D_00:287` (snapshot-first) <- `account_performance` (`C_03:175,199-207`,
`aua = sum(canonical_holdings.market_value)`) <- `B_00` <- **`silver/holdings`**. `silver/allocations` is NOT
on the AUA path. `gold/canonical/holdings/` last partition = 2026-07-07 == served `data_as_of`. `unrealized`
reaches `B_00` only as a CUSIP->name **dict** (try/except) + an **additive** self-heal -- neither is a
row-filtering merge, so an empty unrealized cannot drop holdings rows. **AUA: stale, not corrupt.** P0-class
HOLDS; CTO independently re-verified.

**Measured collateral (SEV2-live, separate finding):**
- `gold/dimensions/accounts_dimension_latest.parquet`: `account_type` and `account_registration_type` =
  **0/828 non-null**. `A_00` selects `sorted(alloc_keys)[-1]` -- the latest partition -- with no row check.
- `gold/positions_cube/`: 2026-06-19 = 9,322 rows / **677** accounts; 2026-07-07 = 9,038 rows / **570**
  accounts. Universe NOT empty (CTO's worst case refuted). The -107-account drop's **attribution is
  `INFERRED`**, non-actionable -- a counterfactual run would be needed.
- Branching consumers read `silver/allocations` DIRECTLY (not the nulled dimension): `C_04.validate_aua:130,141`
  and `D_04:3363,3688`. On a 0-row frame every mask is empty -- no branch at all, not a wrong branch.

**Hypothesis FALSIFIED (a dead hypothesis is a result):** served `fee_earning_aua = 0.00` is NOT caused by
the freeze -- `D_00:619` `fee_mask` keys off `fee_rate_history.is_billable` (`A_02`). Open, unattributed:
`new_client_aua == existing_client_aua == 0.00` while `total.aua = $434,451,347.11`.

### 3. C_02 49F cert freeze -- REFUTED the framing I was handed (`b8ee3a08a`)

COO tasked "write up the C_02 partition-selection defect, root of a live client-facing freeze." **The
grounding does not support it.** Brief:
`docs/briefs/c02-aua-cert-freeze-and-the-partition-picker-trap-20260709.md`.

- **C_02 fails CLOSED.** `:331`'s `certified_aua <= 0` floor (added 06-30 for this exact class) fires,
  refuses a degenerate `$0` cert, logs the row count, and hands to hold-last-good. `:310`'s
  `s3_object_exists` IS a proxy guard, but the floor catches it -- **correcting `:310` un-freezes nothing.**
- **THE TRAP.** `:306 data_date` co-derives `gold_aua` (`:307`) AND the allocations key (`:309`) -- that
  co-derivation is what makes `gap_abs`/`gap_pct` a RECONCILIATION gap. Repointing the picker at "latest
  partition with rows" selects 07-08 (6,870 rows) while `gold_aua` stays at 07-07: a cert lands, the freeze
  visibly ends, and the file keyed `{07-07}` carries a 07-08 number -- **the artifact lies about its own
  as-of.** The `+$6,862,595.49` is real flow, not an error corrected.
- **What actually un-freezes 49F:** gold's `data_date` advancing to 07-08, where a 6,870-row partition
  exists **only because `bd-allocation-processor` wrote it**. This is the mechanism under COO's `[STOP]`.
- **The real defect (accepted as "finding of the night," routed to 0.7.0):** both skip paths `log()` and
  `return`. **Nothing watches for cert ABSENCE.** mtime, ETag, size, `generated_at`, `data_as_of` all
  advanced correctly; only the value was dead. Build `cert_age > N`, not a better guard in C_02.

Row counts: bd `silver/allocations` 07-02 = 6,833 | 07-06 = 0 | 07-07 = 0 | 07-08 = 6,870.

### The unifying class -- five instruments, one disease

A **0-row parquet is not small**: bd = 46,277 B (94 cols), cot = 32,535 B (59 cols).

| layer | guard | property it should bind |
|---|---|---|
| bronze `_ingest_one` | existence | row count (fixed by 0.6.0 today) |
| silver | `bytes > N` | row count |
| gold `A_00` | `sorted(keys)[-1]` | latest partition WITH data |
| gold `C_02:310` | `s3_object_exists` | data-presence predicate |
| validation `C_04:108` | `s3_object_exists` | data-presence predicate (**the validator could not fail**) |

**CTO amendment, adopted:** `row_count > 0` is **NECESSARY, NOT SUFFICIENT** -- holdings returned 11,754
**unvalued** rows. A *valued* table also needs a non-zero-value floor. The predicate must bind the property
the **consumer** depends on. Four hand-rolled copies of one question should be one `has_data(partition)`
helper.

---

## Files Modified

See commit messages: `2af63847d`, `3ea2bdbf9`, `53074cf4a`, `0498a79e7`, `05f7c0f8e`, `b8ee3a08a`.

| File | Note |
|---|---|
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | data-date anchor + `_emit_window` tripwire + `window_bounds` |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | propagate `window_bounds` to the SERVED artifact |
| `data/black_diamond/scripts/gold/C_05.client_tax_liability.py` | `\$` escape + missing `from __future__` + 2x F541 |
| `data/cot/scripts/gold/C_05.client_tax_liability.py` | `\$` escape + 2x F541 -- **independent**, defect set DIFFERS from bd's |
| `org/.../task_orders/ADVI_COTETL.AUAFIX-L6...md` | (b)/(c) HARD-BLOCKED; fail-closed ABSTAIN predicate recorded |
| `docs/briefs/c02-aua-cert-freeze-and-the-partition-picker-trap-20260709.md` | the refutation |

**Firm separation (Rule 13):** bd and cot C_05 carry a byte-identical bad docstring line. Fixed as **two
independent commits against two trees, never mirrored.** Gating each tree separately proved the point --
their defect sets differ (bd was ALSO missing `from __future__ import annotations`; cot already had it). A
mirrored diff would have written a redundant import and, worse, trusted a firm-crossing assumption.

## Briefs Written (DS)

| Brief | Commit | Verdict |
|---|---|---|
| `docs/briefs/c02-aua-cert-freeze-and-the-partition-picker-trap-20260709.md` | `b8ee3a08a` | C_02 is NOT the root; the proposed fix corrupts the cert's as-of; build a cert-absence alarm |

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | `D_00c` | PASS | I/O manifest unchanged pre/post fix; surfaced `EMPLOYEE_LEADERBOARD -> D_04`, which led to the D_04 publisher catch |
| `comp-pipescript io` | `D_04` | PASS | mapped 27 reads; confirmed it consumes D_00c's artifact |
| `comp-pipescript io` | `C_03` | **WARN -- GAP** | resolved to **bd** `C_03` (`[bd-gold]`) when I was investigating **cot** `C_03`. No firm disambiguation. Used cot's source directly instead. |
| `comp-pipescript deployed` | `D_00c`, `D_04`, `C_05` x2 | PASS | MATCH each; then sha256-verified repo == S3 independently (rc=0 is not evidence) |
| `comp-blast` | `build_employee_leaderboard` | PASS | 12 gold nodes + `D_04`; confirmed the fix's blast radius. Emitted `STALE_NODE_WARN` (2 lambda nodes drifted) |
| `commit-gate.sh` | 5 files | PASS | Surfaced 3 pre-existing defects in bd `C_05` that had never been gated (the gate only runs on touched files) |
| `safe-commit.sh` | 6 commits | PASS | `surface-check` clean each time; hit shared-index `.git/index.lock` contention 3x (multi-agent worktree) -- retried with backoff, never forced |
| `safe-deploy.sh` (pre-push) | D_00c, D_04, C_05 x2 | PASS | each deployed to its OWN firm bucket; verified |

**What worked.** `comp-pipescript io D_00c` is what caught the real defect scope: it showed D_00c writes to
`D_04`, which made me check the publisher rather than assume D_00c's emit reached S3. That single call is
why `window_bounds` actually reaches the served artifact. `comp-pipescript deployed` + an independent sha256
compare is the right pairing -- the comp-tool answers "is it MATCH", the sha answers "are the bytes I think
I deployed the bytes that will run."

**What failed.** `comp-pipescript io C_03` silently answered for the **wrong firm**. I asked about cot's
`C_03` and got `[bd-gold]`'s manifest. On a day whose entire theme is "the instrument reports on something
other than what it measures," a graph tool that resolves a bare script id across firm boundaries without
saying so is a live hazard -- bd and cot are gate- and IAM-separated precisely so this cannot happen in code.
I caught it because the READS list looked wrong for cot; a less suspicious pass would have taken it.

**Gap found (routed to CTO / comp-tools owner).** `comp-pipescript io <ID>` needs a firm qualifier (or must
print the resolved tree loudly and refuse an ambiguous bare id). Same class as `comp-iam`'s DESIRED-vs-APPLIED
default: the tool answers a question adjacent to the one asked.

## Verification / Deploys

```
comp-pipescript deployed D_00c -> [bd-gold] D_00c  MATCH
sha256(local D_00c) = 135559900f1a53882d09c2e7 = sha256(s3://opal-data-bd/code/gold/D_00c...)
  deployed contains 'anchor = latest_date' -> PRESENT ; 'w_start = today' -> ABSENT
D_04 deployed == repo -> True ; carries 'window_bounds' -> True
bd C_05 -> opal-data-bd ; cot C_05 -> opal-data-cot   (own buckets, byte-identical, escape gone)
```
Served-artifact verification for the 1Y fix is DEFERRED to the scheduled nightly. No ad-hoc gold run.

## MCP Traffic

~16 messages. Significant: AE brief received (1Y divergence) -> RAVC-4 closed by AE. CVO endorsed my
hard-withhold + independently source-confirmed the mechanism; contributed "coincidence masquerading as
correctness" and the 3-conjunct F-1 limb. CTO: gate ruling (probe first, accept the loud reject, file the
root, GO on L6), then an ADDENDUM making his own severity call provisional after I flagged it rested on a
docstring, then the `row_count > 0` NECESSARY-NOT-SUFFICIENT amendment. COO: `[STOP]` on
`bd-allocation-processor`; tasked the C_02 write-up; accepted the refutation without qualification. MSTR:
amended safety broadcast -- TWO poisoned SSM docs. 0.6.0: the COTTONWOOD probe that falsified my mechanism.

## Blockers

**BLOCKED-EXTERNAL, all evidence-cited. Nothing assumption-blocked, nothing idling.**

- **[1.0.0_SA_CTO]** Gate on the `A_00` fix (3 conditions accepted: provenance stamp, max-age ABSTAIN,
  fail-loud) and on the four `has_data(partition)` call sites. It touches a dimension every gold consumer
  reads -- not self-authorized.
- **[0.6.0_AE_PartnerETL]** Publish-lag curve (21:00Z/23:00Z/00:45Z/01:30Z). It decides whether my ET/cron
  root fix is even the right SHAPE. Building business-date arithmetic before it reads would encode a
  falsified premise.
- **[scheduled nightly]** 1Y served-verify. `D_00c ~09:53Z / D_04 ~10:18Z`. CVO's SEV1 ratification waits on
  it. Deferring here is legal because an ad-hoc gold run is a NEVER rule, not because it is convenient.
- **[ADVI_COTETL.AUAFIX-L6 (b)/(c)]** HARD-BLOCKED on a corrupt grounding source: an automated
  snapshot-zeroed predicate against a 0-row allocations table marks the **entire book** zeroed, silently and
  plausibly. Ratified by CTO. Unblocks when the forward path unfreezes.

## Next Steps

1. **[0.4.0_DS_ClientPlatform -- me]** `[act on/after 2026-07-10T02:30Z]` verify BOTH 02:00Z runs by **row
   count**: cot rejects loudly (no lag); bd's first-ever lagged run either lands `row_count > 0` (49F
   un-freezes) or REJECTS -- and if it rejects, confirm BRANCH-A held last-good **and the alarm actually
   fired** (an alarm that exists is not an alarm that fires).
2. **[0.4.0_DS_ClientPlatform -- me]** `[act on/after 2026-07-10T10:30Z]` 1Y served-verify on the nightly's
   artifact: `window_bounds` present, `1Y.start == data_as_of - 365d`, 0/158 divergent, every window
   `entry_count > 0`. Report to `3.0.0_SA_CVO` (cert gate) + `0.7.0_AE_CloudOps`.
3. **[1.0.0_SA_CTO]** Rule on: the `A_00` predicate; `C_02:310` (defense-in-depth, NOT an un-freeze); the
   `lag=1` sentinel/`run_date` bug INSIDE tonight's mitigation (surfaced, not patched).
4. **[0.7.0_AE_CloudOps]** Cert-absence alarm (`cert_age > N`), complementary to `served-value-freeze-check`
   (`8cf252a5a`).
5. **[0.4.0_DS_ClientPlatform -- me, after the P0]** script-side `DRY_RUN` (implement or strip -- I lean
   strip); the off-path silver writer (92 vs 94 cols, no provenance); `cot/D_00c:1152-1167`'s identical
   wall-clock anchor (firm-separated, independent fix); backfill 06-22..07-09 (idempotent via `_should_skip`
   ETag content-skip) only AFTER the forward path unfreezes.
6. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** ~8 candidate wall-clock-anchor sites across bd/cot gold;
   `inf`'s `INF_D_00c._window_date_range(window, data_as_of)` is the correct reference pattern.

## Discipline notes (for the next agent in this lane)

- **A converging test tells you nothing until you know it could have diverged.** 3Y "passed" on a weekend.
- **`sorted(keys)[-1]` is a freshness check bound to the wrong property.** So is `exists`, so is `bytes > N`.
- **Two SSM docs lie about `DryRun`.** `opal-cot-bronze-run` writes S3; `opal-cot-bd-session-fetch`
  **rotates a live BD credential**. Neither reads `DRY_RUN` (verified absent from the DEPLOYED object on
  BOTH planes). Build a read-only probe; never pass `DryRun`.
- **Do not touch `bd-allocation-processor` or `silver/allocations/2026-07-08.parquet`.** The "stray legacy
  Lambda writing a wrong-schema partition" is the ONLY producer of real 49F allocation silver. Cleaning it
  re-freezes $1.837B. Every local signal endorses the cleanup.
- **I was wrong twice tonight** and both were the same failure: I read a docstring (`cot_bronze_ingest.py:80`)
  and wrote it as mechanism. On C_02 I read the source before writing. That is the entire delta.

---

## ADDENDUM (post-log, ~21:00-21:35Z): the period-roll defect ALREADY FIRED in production

Written after the log above was committed (`48943c343`). Andrew asked why a deployed fix needed the nightly
to prove it. Chasing that question produced the headline finding of the session.

### 1. The rule I was over-applying

"NEVER trigger ad-hoc gold runs to validate" forbids **triggering the production gold run** (it writes S3,
overwrites served artifacts, races the nightly). It does **not** forbid **executing the code read-only.**
I had collapsed the two. Verified the no-write property by READING `_save_json` (`gold_utils.py:68-82`:
`if dry_run: return` before `put_object`) rather than trusting the flag's name -- the same `DryRun` trap MSTR
found in two SSM docs tonight. CVO independently found the guarantee is STRONGER: `_save_json` is called only
from `main():1360`, unreachable from `build_employee_leaderboard():798`, so a harness calling the builder
**cannot reach `put_object` at all.**

### 2. Value limb PROVEN, tonight, not tomorrow

Real `build_employee_leaderboard`, real S3 inputs, read-only, wall-clock `2026-07-09` deliberately injected:
`1Y 0/158 divergent` (was 65); `window_bounds` byte-matches served canonical on all 5 windows;
`entry_count > 0` on all 9; tripwire silent.

Also verified the assumption under my own "wait for the nightly": `run-gold-layer.sh:88-90` +
`gold_dispatch.sh:526` `aws s3 sync s3://$BUCKET/code/gold/` at run start. **Pull-at-runtime, nothing baked.**
So the nightly is now load-bearing for **DELIVERY ONLY**. CVO re-scoped the withhold (`842dd9040`).

### 3. THE FINDING: it was never latent -- it fired

Per CVO's `[A]` remedy ("add a period-roll case"), ran pre-fix vs post-fix at a simulated quarter-end as-of:
pre-fix `MTD=0, QTD=0` (silent empty windows, no raise); post-fix `MTD=154, QTD=156`. Then stopped reasoning
forward and read the **versioned served bytes**:

```
s3://opal-data-bd/platinum/firm/leaderboard.json  (S3 versioning)
  2026-07-01 .. 2026-07-02   QTD entry_count = 0   -- EIGHT consecutive served writes, 39.8h continuous
  2026-07-02T17:42:00Z       QTD entry_count = 151 -- self-recovered when data_as_of crossed into Q3
```
**Clients were served ZERO advisors in the QTD window for 39.8 hours.** YTD/MAX/1Y/3Y held 155-156 throughout,
so the tab rendered a FULL leaderboard with an empty QTD -- worse than a blank page, which gets reported.
CTO confirmed independently (SEV1-historical); CVO walked every version and found 8 writes, not my 2.

### 4. Exposure bounded at BOTH ends -- by source, not by the artifact

The served-history oracle has a **lifecycle horizon**: `expire-noncurrent-platinum-14d` / `-gold-14d`, so only
~15 days of served bytes survive (42 versions, oldest 2026-06-24). CVO ruled 2026-04-01 "permanently
unprovable." **It is not.** A git pickaxe over the defect's own text has no lifecycle policy:

```
git log --reverse -S 'w_start = today - pd.Timedelta' -- data/black_diamond/scripts/gold/
  a3b2d2099  2026-04-06   <- the wall-clock anchor is BORN, five days AFTER the April roll
  2af63847d  2026-07-09   <- the fix
```
`2026-04-01` = **excluded at source, not unobserved.** Every boundary in `[2026-04-06 .. 2026-07-09]`:
one quarter roll (07-01, fired), three month rolls (MTD is slimmed out of the served artifact by
`D_04:2166` -> never reaches a client), zero year rolls. **Total client impact, ever: ONE event.**
CVO retracted (`6b58f0f7a`).

> *"Did clients see it"* decomposes into *"did the artifact show it"* AND *"did the code that produces it
> exist."* Read-the-artifact fails at detection AND at forensics. The **emit-time tripwire** fixes detection;
> the **pickaxe** fixes forensics. **When the bytes are gone, ask when the bug was born.**

### 5. Two of MY OWN instruments lied during this check

- `aws s3 cp "s3://..." "$SPW\$f.log"` -> **exit 0, wrote nothing** (MSYS path mangling). My `&& echo "pulled"`
  printed success. Caught only because the parse found no file. Re-ran streaming to stdout with `wc -c`
  asserted **before** parsing.
- `git log --until=2026-04-02 -1 --format=%H -- <path>` -> **empty SHA**, so `git show ":path"` silently
  rendered the **index** version and printed plausible `latest_date = perf['date'].max()` lines. I almost
  reported *"April's code was already data-anchored."* **Discarded rather than reported.**

**An empty variable interpolated into a ref is an instrument that answers confidently about nothing.** Both
would have produced a wrong finding in the reassuring direction.

### 6. New, filed, mine, NOT fixed (in-window; touches a served key)

`prior_week` is structurally broken. `build_firm_dashboard:359-369`'s `if size_kb > 200:` split branch writes
the raw **9-window gold** `employee_lb` to `platinum/firm/leaderboard.json`; `build_leaderboard`'s rotation
~2000 lines later faithfully copies *that* to `.prior_week`, then overwrites with the trimmed 5-window object.
The sequencing comment is correct about its own two lines and blind to the earlier write. Live proof:
`dashboard.json = 577 B` with `"split": true`; `prior_week = 3,362,611 B` == the gold artifact exactly.
Consequences: **structurally guaranteed zero week-over-week delta** (`exec_summary/trigger_eval.py:8-9` cannot
fire on a real change), a 9-vs-5 shape mismatch, and a **transient wrong-shaped served artifact** between the
two writes. Conditional on a 200KB threshold -- it appeared silently the day the payload crossed it.
**Not mirrored to `cot/D_04:2533`** (same rotation code, separate firm, own evidence required).

### 7. Also measured (client-facing plane, previously unmeasured)

`bd gold/dimensions/accounts_dimension_latest.parquet`: `account_type` non-null = **0 / 10,545** (cot was
0/828). Same `sorted(alloc_keys)[-1]` defect, 12.7x scale, on the 49F plane. Corroborates 0.6.0's point that
`gap_pct`'s operands are **not independent** (`certified_aua` <- stubbed allocations; `gold_aua` <- `C_03` <-
the dimension those stubs nulled). The ~$115M `gold_aua` drop remains **0.6.0's `INFERRED` claim**, not mine.

### Compiler Tools (addendum)

| Tool | Target | Result | Note |
|---|---|---|---|
| `aws s3api list-object-versions` | `platinum/firm/leaderboard.json` | PASS | the served-history oracle; **has a 15-day lifecycle horizon** -- CTO is registering `comp-served-history`, and it must PRINT its horizon rather than return empty |
| `git log -S` (pickaxe) | `w_start = today - pd.Timedelta` | PASS | bounded the exposure window from below; **no lifecycle policy** -- the forensic oracle that survives when bytes do not |
| `comp-pipescript io` | `A_01` (via 0.6.0) | PASS | `A_01`'s docstring claims a `silver/allocations` read it does not perform -- a false record, my lane, filed |
