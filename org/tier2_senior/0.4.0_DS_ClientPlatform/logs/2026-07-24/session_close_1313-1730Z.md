# 0.4.0_DS_ClientPlatform -- 2026-07-24 1313-1730Z -- retry-net + D_00 cliff + the 6d clock

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

Window: session start 1313Z (fresh session, NOT REGISTERED, no watcher -- genuine cold start) to 1730Z.
Dispatch: COO three items (6d clock ~1347Z; D_00 + retry-net implementation; cot quarantine lift).

---

## Summary

All three dispatched items closed, plus a fourth picked up mid-window. Two of the three arrived
inaccurate and were corrected by their own authors within the first 30 minutes -- I built against the
corrected versions, not the dispatch.

| item | outcome |
|---|---|
| (3) cot 07-22 quarantine lift | ALREADY DONE @`b76f7534e` -- verified deployed MATCH independently, nothing to redo |
| (2a) cot retry-net generalization | `545bde4e9` -- CTO **ACCEPTED** 141355Z, deployed, ledger closed |
| (2b) D_00 08-01 cliff | `f204e97cb` -- 0.6.2~A **VERIFY=PASS** 151207Z, deployed, ledger closed |
| (1) 6d-wiring co-read | **UNEXERCISED, 7th day** -- never-triggered, NOT failed. Cause found. |
| (+) canonical date axis | `3b0113227` -- committed, **NOT pushed** (COO [STOP PUSHING] 161125Z) |

---

## The 6d clock -- the substantive finding

INF chain **CLEARED 15:01:40Z**, first since 2026-07-18 (`gold/meta/pipeline-complete.json`;
`pipeline-failed.json` did NOT advance). 0.7.0_AE's excusals stage at 13:39:36Z landed before the gold
stage ran 14:34-14:35Z, so INF_C_01 cleared on the five excusals.

`mdpf-daily-trigger` FIRED 15:01:43Z -- 3s after the marker, so the **event wiring is correct** -- and
DEFERRED: `dispatched:false`, 49financial `schwab/silver/rps` `latest_partition 2026-07-15`,
`trading_days_behind 7` (max_lag 2); inflection fresh. Runner `i-02448edb624a7a7cf` never started
(still STOPPED, last LaunchTime 2026-07-22T21:02:00Z); zero mdpf gold writes. So `revamp_stage` never
ran and there is **no rc to read**.

**INSTRUMENT DEFECT (routed CTO 152057Z, unresolved).** The trigger logged
`ROLL_SOURCE_UNREADABLE 2026-07-15.json (403) -- a CONFIG/IAM fault that will NOT clear on its own`.
That diagnosis is **wrong**, measured on three primitives:
- roll source `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-07-15.json` -> **404, absent**
- `simulate-principal-policy` role `mdpf-daily-trigger-lambda-role` `s3:GetObject` on the EXACT arn,
  ONE `--resource-arns` -> **allowed**
- `s3:ListBucket` on `arn:aws:s3:::opal-data-portal-v2`, **separate invocation** (Rule 22a) ->
  **implicitDeny**

S3 returns 403 (not 404) for a MISSING key when the caller cannot list. So ABSENT is indistinguishable
from UNREADABLE to this role, and `lambda_function.py:361-365` files a DATA condition as a CONFIG
fault. The taxonomy at `:337-349` exists *precisely* to separate those (its docstring cites 0.6.0 BLOCK
000837Z, "cannot read it and it does not exist print the same nothing") -- a missing ListBucket grant
defeats the very distinction it was built for.
**SIZING: granting ListBucket UNBLOCKS NOTHING** -- ABSENT and UNREADABLE both DEFER, identical
decision. It is a TRUTH fix. But the docstring says UNREADABLE must be alarmed on by
mdpf-freshness-checker "and never on ABSENT", so as it stands it fires a config alarm on a data
condition and sends the responder after a grant that is already present.

**BLOCKER CLEARED AFTER MY REPORT:** 0.6.2~C ran `/49-schwab-conv`; rps reached `date=20260723` at
15:44Z, ~23 min after the 15:01:43Z deferral. Report accurate when written; gate should clear on the
**next** chain fire. 6d stays UNEXERCISED until then.

**`keys_staged: 11` IS A HARDCODED HEREDOC LITERAL** (`mdpf-daily-dispatch.sh:537`) -- a CODE-VERSION
signal, never a landing count. It was sitting in an acceptance path. CTO escalated it. Split agreed with
0.7.0 (I enumerate the 11 declared keys; they take per-key freshness + run-log rc) so we do not read one
literal twice. Denominator grounded writer-by-writer: 6a=3, 6b=3, 6c=1, 6d=4 (slice ->
cottonwood/aggregate_aua_timeseries; pair -> account_distribution + aum_metrics + account_units `:489`)
= 11. **6a+6b+6c IS the old 7** -- which is exactly why the echo strings say 7 and the marker says 11.

My limb, measured 15:13Z: 0 fresh / 11 pre-existing / 0 absent; cycle-complete ABSENT; cottonwood
`covered_dates ['2026-07-21','2026-07-22']` NONEMPTY (no regression); fold 294 / 223,96,104,12,7 /
source cited INTACT on both the revamp artifact and the portal-v2 served key.

---

## Errors of mine this window (all caught, all corrected)

1. **Mutant harness measured nothing.** First run's filter `^(FAIL|ERROR): |^Ran |^OK|^FAILED` matched
   the script's OWN `OK: ingested...` stdout -- six well-formed result lines carrying zero information.
   Re-ran with a correct filter rather than reading the first result.
2. **False axis "correction", [STOP]ped by COO 143746Z.** I read
   `opal-data-assets/json/portfolios/account-distribution.json` (ETag 0a2978d4, 4 versions, no fold) and
   concluded the served key had never carried a cottonwood fold. **The served bucket is
   `opal-data-portal-v2`** (ETag 14d668ef, 17 versions, fold present at 294). Worse than the bucket slip:
   I treated an **ETag as key identity** -- it is a CONTENT hash, so byte-identical objects across
   buckets necessarily share one, and the shared ETag was never evidence of mis-attribution. I also
   offered "4 versions, no delete markers" as the decisive control -- a real query returning real rows
   against the wrong bucket. Retracted 144203Z; never reached CTO. Would have been a false P0 on what
   Andrew ruled ~1432Z is the PRIMARY item.
3. **My own check instrument nearly repeated the premature-read class I had warned 0.7.0 about.** It
   printed "6d block did NOT complete" **three minutes** after the chain cleared, because its verdict was
   two-state and could not distinguish NOT-YET-DUE from FAILED. Rebuilt four-state with a 20-min
   threshold.
4. **Sent 0.7.0 a caution I had not grounded**, then withdrew it (150901Z) -- their 11/11-fresh bar was
   correct; I attached a directional guess to an honest "I have not checked".
5. **A regression test that escaped its mutant** (see below).

---

## The test-methodology finding (the most transferable thing this window)

**A fixture parameterised by the constant under test cannot detect a change to that constant -- it moves
with the code.**

- D_00: my first site-2 regression test asserted arithmetic over CONSTANTS. Mutating
  `total_aua = served.value` -> `gold_total` left the ENTIRE suite green -- nothing executed the line
  under test. Rewritten to call `build_snapshots` and read the denominator the artifact actually carries,
  on both the `total_aua` field and the emitted `aua_pct` rows.
- canonical date axis: every fixture was keyed off the module's own `MONOLITH_FEED_PREFIX`, so mutating
  it back to the dead `01_raw/` tree made the fake serve the same dates at the new prefix -- **eight
  behavioural tests passed against the original defect**, caught by ONE structural assertion. Added a
  class capturing the real `(Bucket, Prefix)` pairs passed to `paginate`, which a fixture cannot fake
  away. That also caught a **bucket-only revert the first suite would have missed entirely**.

Banked to memory as `feedback-an-instrument-must-not-inherit-what-it-measures.md` (indexed in
MEMORY_FULL) with 0.6.2~C's two corollaries: **a remediation can erase the evidence that would have
proven the remediation** (their catch-up destroyed the discriminating condition, after which fixed and
broken code return identical live values), and **a guard that refuses UNKNOWN cannot refuse
WRONG-BUT-KNOWN** (`master_for('model_portfolios')` is a legal call returning the wrong book).

---

## Rulings received / findings raised

- **CTO 141355Z:** retry-net ACCEPTED; **ratified my strict predicate split** (`_table_complete` stays
  MEASURED-ONLY so an inferred sidecar cannot advance the bronze->silver chain sentinel; the 3-state
  predicate lives only in `_retry_net_state`). Explicitly: "an inferred-present record is good enough to
  stop re-asking; it is NOT good enough to advance silver."
- **CTO 141355Z:** bd/cot shared single-source RULED -- **HOLD bd, do NOT sync**. Took my sentence
  verbatim: *"a scope that is enforced by drift is not enforced."* `cot_bronze_ingest.py` deploys to BOTH
  `opal-data-cot` and `opal-data-bd` (ledger 20260625T1547Z L2, Model-B firm-bound, runtime-guarded).
  bd's copy stays at `fa9fd5a9` @2026-07-09, 15 days behind.
- **CTO 141355Z: amended his own item-5 gate condition** on a finding I raised -- "aua_pct rows sum ~100"
  was already FALSE at **90.03%** on live data, and the obvious way to make it pass (re-point site 2's
  denominator at gold_total) would have silently re-based the snapshots while header_metrics serves the
  held cert. A control satisfiable by breaking the thing it guards. Replaced with my proposed
  DIFFERENTIAL axis (denominators unchanged pre/post; ratio identical across the change).
- **RAISED, open at CTO:** the ROLL_SOURCE ListBucket misclassification (152057Z); a gate candidate to
  lint `master_for(<string literal>)` outside a module declaring its own PURPOSE (164949Z).
- **PREVENTED:** 0.6.2~C's routed fix recommended `master_for('model_portfolios')` or
  `opal-data-bd/schwab/silver/rps/` -- **both 0824**; the canonical store is **0833**. A literal
  implementation would have been a cross-master SUBSTITUTION on the ADVISOR INTELLIGENCE tree. Blocked by
  method (anchor on the consuming module's declaration), not by my spotting it -- stated as such to them,
  to CTO, and here. They amended @`4ae8bf78b` / `08e47e863` and retracted fabric-wide; CTO's acceptance
  message was already in flight carrying the wrong clause.

---

## Files Modified

See commit messages: `545bde4e9`, `d2dc4be74`, `f204e97cb`, `6cccbaf6c`, `3b0113227`.

| file | note |
|---|---|
| `data/cot/scripts/bronze/cot_bronze_ingest.py` | `backfill_snapshot_net` + 3-state `_retry_net_state` + heal-forward sidecar + per-run marker |
| `data/cot/scripts/bronze/tests/test_retry_net.py` | 57 -> 81 tests; rewrote case (b), which mocked a predicate the new sweep never calls |
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | `ServedAUA` tuple, uncapped one-LIST hold, `aua_provenance` at both sites |
| `data/black_diamond/scripts/gold/tests/test_d00_aua_provenance.py` | NEW, 26 tests |
| `data/canonical/schwab/build_canonical_daily.py` | date axis -> monolith bronze; master via `master_for(PURPOSE)` |
| `data/canonical/schwab/tests/test_canonical_daily_date_axis.py` | NEW, 14 tests |

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-pipescript deployed` | `cot_silver_merge.py` | PASS | MATCH -- proved the quarantine lift was DEPLOYED, not merely committed |
| `comp-pipescript deployed` | `cot_bronze_ingest.py` | PASS | MATCH -- ledger L2 proof line |
| `comp-pipescript deployed` | `D_00.portal_aggregates.py` | PASS | MATCH (4 MATCH/0 STALE) -- ledger L2 proof line |
| `comp-grep` | `cycle-complete`, `backfill-holdings-net`, `account_units`, `ROLL_SOURCE_UNREADABLE`, `514` | PASS | located `ssm.tf:140` (the alias's whole point), `build_cottonwood_mdpf_pair.py:489`, the trigger classifier |
| `comp-platinum reverse` | `aua_provenance` | PASS | 0/58 field paths, case [a] genuine-empty -- CTO Condition 1 DISCHARGED |
| `comp-aws` | mdpf trigger / cot bucket rules | PARTIAL | returned nothing useful for the EventBridge question; fell back to `get-bucket-notification-configuration` + the Lambda log group |
| `commit-gate.sh` | 6 files across 3 commits | PASS | caught 2x ruff E702 in my test file |
| `deploy_ledger.py` | 2 entries opened+closed | PASS | 3/3 legs each |
| pre-commit risk-reflex | auto in safe-commit | PASS | **FLAGGED `cot_bronze_ingest.py`** -> reading the citation is what surfaced the bd/cot shared single-source |

**What worked:** the risk-reflex citation was the single highest-value tool output of the window -- it
turned a routine commit into the shared-single-source finding CTO ruled on. `comp-platinum reverse`'s
own empty-vs-broken DIAGNOSTIC (case [a]) let me discharge a gate condition without guessing.
**What failed:** `comp-aws` did not answer "what EventBridge rules fire on this bucket" -- I could not
tell an empty result from an unsupported query and went to live primitives.
**Gap found:** no comp-tool answers "which BUCKETS hold this key name" -- the exact question behind my
false axis correction. `comp-which` routed me to `pipescript --resource`, which is resource-thread
scoped, not key-name scoped across buckets. A `comp-where <key>` that sweeps candidate buckets and prints
bucket+ETag+size per hit would have prevented that error outright.

---

## Blockers

**BLOCKED-ASK RAISED 165420Z, ANSWERED 165526Z -- now UNBLOCKED, not started.** I could not find any
definition of the `$514K nm-vintage residual` (COO 132736Z, 142218Z) -- searched my 07-18..07-23 logs,
deliverables and full inbox for `nm-vintage`, `nm_vintage`, `514K`, `$514`, `non_model`+`residual`; only
adjacent hits were `income_non_model_residual` (a cottonwood meta field) and `etf_public_residual` (A4-D5,
deferred at N=3). I declined to reconstruct a client-facing dollar figure from inference -- same discipline
CTO and 0.6.2~A applied to D_00 this morning.
**COO's answer (grounded, from `drive_log_20260723T2214Z.md:10`):** `$514,428.86` is the **2-day non-model
roll-forward VINTAGE diff** -- non_model_assets at as-of 07-22 (`$275,182,349.31`) minus as-of 07-20
(`$274,667,920.44`), to the cent. `nm` = non_model. **It is a vintage difference, not a computation error.**
The v2.1.148 tooltip's non-model leg reads a 2-day-older vintage than the aggregate.
**It is a CHOICE already on the record, not an investigation:** either (a) let the next `non_model_assets`
07-22 emission close it naturally -- fixes today's number, leaves the mechanism -- or (b) re-source the
tooltip's nm leg to the aggregate so the vintages cannot diverge (the durable fix). **Not started; owner not
yet established** (the tooltip is a v2.1.148 surface, plausibly DE's lane rather than mine). Not assuming it
is mine.
COO recorded this as the **fourth** aged-or-unanchored record they propagated today by repetition rather
than by file.

**Not blocked, held by design:** W-7 (GC-W7 @`269047874`) STAGED, no clock, explicitly not to be picked
up yet; cross-lane gate noted -- `0.4.0_DS_ClientPlatform~A` is READ-ONLY on
`dim_mdpf_aggregate_aua_timeseries.py` for W-1 and I MCP them before any commit that moves the date
spine. I have not touched that file.

---

## Current State

- **Retry-net:** `545bde4e9` on origin/CLOUD, deployed `s3://opal-data-cot/code/bronze/cot_bronze_ingest.py`
  md5 `ed5097de2e5d4d073d12e8f11818d5ac` @13:53:50Z. Ledger
  `20260724T1358Z_cot-retrynet-snapshot-generalization` CLOSED 3/3. CTO ACCEPTED. **Acceptance still
  outstanding:** 0.6.2~A's 07-25 ~02:00Z unattended re-land of allocations+unrealized @2026-07-23, two
  axes + sidecars. First run is the CONVERGENCE run -- expect a batch of heal-forward inferred sidecars;
  run two is steady state.
- **D_00:** `f204e97cb` on origin/CLOUD, deployed `s3://opal-data-bd/code/gold/D_00.portal_aggregates.py`
  md5 `8fe11a9dd113a20f575819eb278e99ce` @14:51:57Z. Ledger `20260724T1455Z_bd-d00-aua-basis-provenance`
  CLOSED 3/3. 0.6.2~A VERIFY=PASS. **Cliff closed at CODE level only** -- artifact evidence needs the next
  SCHEDULED run (NEVER#4, no ad-hoc gold run).
- **Canonical date axis:** `3b0113227` **COMMITTED, NOT PUSHED**. Queued with COO 164249Z.
- **Both deploys fired by a PEER's push, not mine** -- `safe-commit.sh` contains no `git push`; CLOUD is
  shared, so any agent's push carries every commit on the branch AND runs `safe-deploy --commit-range`.
  Surfaced to COO 161511Z: under the new process **COO's push is the fabric's single deploy trigger** for
  everyone's gold/silver/bronze code.
- **My ~$88.3mm observation is now MOOT, not wrong (COO 165526Z).** 0.6.2~A measured the tax buckets
  exhausting `total_aua` **EXACTLY (gap 0.00)** on `client_performance.parquet`, and the `gold_aua` field
  inside the cert (`$1,780,856,838.03`) turned out to be **a field nobody had computed**, quoted through
  two honest relays. I had used it as a candidate denominator. Resolved above me; CTO has it.
- **>> D_00 @`f204e97cb` IS `MOOT-ON-ARRIVAL` -- RULED (CTO 170155Z on ANDREW-DIRECT ~1701Z).**
  Andrew VERBATIM: *"I do not give a single fuck about certified AUA, that is a deprecated concept and
  will not even exist by August."* **The deprecation lands BEFORE 2026-08-01, so the cliff CANNOT
  ARRIVE** -- the mechanism that produces it will not exist when the date comes. **The 08-01 date comes
  off every board.** (This SUPERSEDES the `CONDITIONAL` marking CTO issued at 170002Z, which was
  provisional pending a timeline he did not then hold.)
  **NOT reverted, NOT live protection.** Left in place because it HOLDS a value rather than substituting
  one (harmless inert) and because reverting deployed+verified code to satisfy a records question is the
  worse trade. **Work PRESERVED not deleted:** the mutant reproducing the -$99.1mm substitution on demand
  is a reusable instrument, and the basis-carrying pattern is correct INDEPENDENTLY of certified AUA --
  the same carry-the-basis shape is being applied to the MDPF count series. **Retire the CLIFF RATIONALE,
  keep the pattern.** No fourth `basis` value: certification is not replaced by another certified-like
  basis; 49F moves to Schwab explicitly.
  **RECORD FIX APPLIED IN THE CODE ITSELF** -- a MOOT-ON-ARRIVAL banner in `D_00.portal_aggregates.py`
  above `ServedAUA` and in the test-suite docstring, because the cliff narrative sitting un-annotated in
  my own source WAS the false record. CTO's instruction, verbatim and now in three places:
  **"A FIX EVERYONE BELIEVES IS GUARDING SOMETHING IS WORSE THAN NO FIX."**
  **CERTIFIED-AUA WORK IS CLOSED ACROSS ALL LANES:** the cliff rationale, the shared certified-vs-gold
  resolver, the ~$97.1mm cert-gold_aua-vs-perf gap (CLOSE AS SUPERSEDED, do not explain it), and the
  -9.97% divergence (a SYMPTOM of holding the certified basis -- watch, do not fix). 0.6.2~A verifies
  nothing further against the cliff premise.
  **Provenance of the catch:** I raised the premise check at 1736Z having deployed at 14:51Z -- the
  build-verify loop completed ~50 min before the sovereign signal. I did not revert on the relayed
  one-liner; acting on it without scope or timeline would have been the reconstruct-a-spec error in the
  opposite direction. CTO: *"Do it again next time without hesitating."*
  **What the afternoon actually produced** (CTO, so it is not filed as wasted): three of us worked a
  question whose subject was being retired and none of the work was wrong -- the lasting output is the
  METHOD. **Our instruments read the system as it IS and are structurally blind to where it is GOING.**
  That is the one thing none of us could have measured.
- **Not mine, flagged to me and unfixed:** ~719 monolith bronze partitions carry a broken object-name
  grammar (`CRS{d8}.{FEED}` vs `{master}.CRS{d8}.{FEED}.zip`) -- **a `--force` or full silver rebuild will
  fail on ~120 dates per feed.** Recorded in `test_canonical_daily_date_axis.py`. Bronze immutable (17a);
  remedy is a re-land/alias ruling.

---

## Next Steps

1. **[2.0.0_SA_COO]** push `3b0113227` (queued 164249Z) -- and note the deploy exposure of the range.
2. **[2.0.0_SA_COO]** scope the `$514K nm-vintage residual` (165420Z) -- artifact + the two quantities.
3. **[1.0.0_SA_CTO]** ROLL_SOURCE ListBucket misclassification (152057Z); `master_for(<literal>)` gate
   candidate (164949Z).
4. **[0.6.2_AE_PartnerETL~A]** retry-net acceptance at the 07-25 ~02:00Z nightly.
5. **[0.4.0_DS_ClientPlatform]** W-7 when COO releases it -- AC-1 is *which is wrong, the rows or the
   declaration*, NOT "remove the 16 weekend rows"; resolve the trading calendar first and count weekend
   vs market-holiday exclusions SEPARATELY.
6. **[0.4.0_DS_ClientPlatform]** re-read the 6d observables on the next chain fire -- 49F gate should now
   clear; instrument is written, four-state, and exercised.
