# 0.4.0_DS_ClientPlatform -- 2026-07-28 ~1342Z-open -- MDPF Cottonwood P0: root cause, cutover, L1/L2 census

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

Window: cold start ~1342Z (NOT REGISTERED, no watcher, no orphan) to open. Dispatch: Andrew-direct P0 via
`1.0.0_SA_CTO` -- MDPF Global lost Cottonwood 07-25; scope widened same hour to L1 channel-freshness census
+ L2 gold-DDB aggregation correctness.

---

## Summary

**One cause explained two of CTO's three threads.** The scheduled mdpf runner has been executing
**2026-07-21 code**; every commit to the producer since has been repo-only, because **`mdpf` is not a
`PIPELINE_MAP` key -- a push cannot deploy that tree at all.**

| thread | outcome |
|---|---|
| (2) Cottonwood drop | ROOT-CAUSED. Deployed builder is 2-leg `build_global_artifact(a49, ainf)`; the fold landed 07-23T01:13Z, ~7.6h after the deployed copy froze. Never deployed. |
| (1) 425/425 sum-identity failure | ROOT-CAUSED, same cause. Deployed copy predates the basis-B fix `4ec837e728` (07-22T01:00Z) by ~7h, so it carries the original P0 by construction. Residual == `-inflection_non_model_aua` on **425/425 dates, exact to the cent**, and derives algebraically. |
| (3) L1 channel census | DONE. Andrew's premise is right about bronze/silver, **wrong about gold DDB**. |
| L2 gold DDB | **13 of 32 cohorts row-fresh but VALUE-stale since 07-21/22** -- every AUA-bearing cohort. |
| cutover | Deployed repo HEAD 14:08:26Z under CTO GO; verified from S3 by independent re-download. **L2/L3 legs OPEN pending a scheduled run.** |

---

## The mechanism (source-confirmed, Rule 22a desired + applied)

```
DEPLOYED s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
         51,999 B @2026-07-21T17:42:40Z   def build_global_artifact(a49, ainf)         <- TWO legs
REPO HEAD                                 124,241 B   def build_global_artifact(a49, ainf, acot)
token census DEPLOYED/REPO: cottonwood 0/27 - load_cottonwood_slice 0/2 - acot 0/17
                            cot_covered 0/13 - carry_forward_with_basis 0/2 - frontier_stamp_staleness 0/4
POSITIVE CONTROLS (both):   build_global_artifact 2/2 - build_49f_artifact 2/2 - SERVED_AS_OF_FIRST 7/7
```
`.tools/safe_deploy_core.py:22-26` PIPELINE_MAP = black_diamond / inf / cot only -> `file_to_s3_target()`
returns None for `data/mdpf/**`. Runner syncs `s3://opal-data-mdpf/code/scripts/ --delete`
(`mdpf-daily-dispatch.sh:125`), `REVAMP_DIR=$SCRIPTS_DIR/gold` (`:454`).

**~A's 07-24 deploy ledger had already MEASURED this** (`20260724T1824Z_ci-r11-...`, leg L2) and escalated it
as a "thirteenth-item candidate" -- but named the consequence as *"Row 11's guard is not live"*, not *"the
Cottonwood fold and the basis-B P0 fix are not live."* **The finding was on the record for 4 days, correctly
measured, under-scoped.**

## The producer-attribution question (COO raised; settled at source)

CVO measured 12 PASSING artifact versions on 07-22/07-23 while the runner ran pre-fix code. Apparent
conflict. Resolved from **runner telemetry rather than artifacts**:

**Zero runner logs exist for 07-19..07-24** (July inventory: 07-02, 06, 07, 08, 10, 16x2, 17, 18 | 25, 26, 27).
The 16 gold versions in that window landed at 04:55Z / 05:23Z / 12:26Z / 23:30Z -- **none near the run
window** -- with a byte ladder 165K -> 173-177K -> 242-256K -> 254,419. **A development session, not a daily
job.** Corroborated: instance STOPPED with last LaunchTime 07-22T21:02Z; `mdpf-daily-trigger` DEFERRED
`dispatched:false` 07-24.

**Consequence, adopted from COO:** *"the fix reproduces 07-23"* and *"the scheduled path will produce
07-23-quality output"* are different claims and **only the first is evidenced.** Sharper: the 07-23 artifact
I reproduced exactly **was itself hand-made**, so the 0.00 residual is *two hand runs agreeing*. I did not
label that evidence class when I first reported it.

## L1 CENSUS -- prefixes ENUMERATED, grammar-aware (T-1 bar 2026-07-27)

| channel | bronze | silver | verdict |
|---|---|---|---|
| Schwab / 49F custody | 07-27 (636) | 07-27 (544) | HEALTHY |
| SmartX / 49F model + roster | 07-28 (12) | 07-28 (15) | HEALTHY |
| Eclipse / INF model | 07-27 (61) | 07-27 (60) | HEALTHY |
| Orion / INF custody | 07-28 (2283) | 07-28 (2283) | HEALTHY |
| BD / COT allocations | 07-27 (89) | 07-27 (89) | HEALTHY |
| BD / COT rebalancer models | 07-28 (8) | 07-28 (8) | HEALTHY |
| BD / COT holdings | 07-24 (37) | 07-24 (37) | WATCH T-2 |
| BD / COT unrealized | 07-24 (88) | 07-24 (88) | WATCH T-2 |

Rule 17a: **0 `.parquet` under any of 8 bronze prefixes.** Bronze correctly raw (`.zip/.RPS/.jsonl.gz/.xlsx/.json`).
**Standing record corrected:** the "cot allocations+unrealized frozen since 07-17" caveat is DEAD --
allocations 07-27, unrealized 07-24. Both advanced. Memory index updated.
**Freshness != completeness:** newest-partition only, 9 tables. "Cottonwood is complete" stays a BELIEF.

## L2 -- THE GOLD DDB IS THE BIGGEST FINDING

`opal-assets-daily-aua`, 35,046 items, 32 cohorts. **A ROW census says 32/32 HEALTHY @07-27. A VALUE census
says 13 stopped being fed on 07-21/22** -- all nine `49f_*`, `inflection_models`, both `cottonwood_bd_*`,
and **`_global__aua_total`**. Stalls not sparse series (21-26 valued dates in the final 30, daily-dense to
the stop). `cottonwood_bd_models` excluded as newly-seeded (2 valued rows ever, both `124,376,009.73` --
independent third-surface corroboration of CTO's Cottonwood delta).

**The stall did NOT clear when the runner resumed 07-25/26/27** -> whatever feeds the table is not the mdpf
runner and has been down ~4 trading days. Correlation flagged, **mechanism NOT named** (emitter untraced).
COO escalated: *a perfect scheduled publisher would publish stale DDB values.*

## Marker-consumer enumeration (COO's L2 add)

Denominator: **141 EventBridge rules** (121 scheduled / 20 pattern-only) + 8 S3 notification configs.
- `gold/mdpf_revamp/meta/cycle-complete.json`: **zero live automated consumers** (publisher deliberately
  OFF; all 8 S3 configs are `bronze/ -> silver`, none on any `gold/` prefix). Never written -- Stage 6 exits
  rc=1 before reaching `:576`. Casualty = the parity streak, which **cannot accrue and reports nothing
  rather than reporting a failure.**
- `gold/meta/pipeline-complete.json` (opal-data-inf): `inf-portal-publisher` (S3 notification) +
  `mdpf-daily-refresh-trigger` (`ScheduleExpression: None`, ENABLED). **Both marker-only** -- the NEVER#4
  instance, re-confirmed on the applied plane.
- **Silver is NOT a frozen surface:** 6 independent daily crons (`opal-assets-silver-*-sweep-daily`) PLUS
  S3-event accelerators. The correct NEVER#4 pattern, already implemented.

## The cutover

CTO GO 14:05:46Z, time-boxed ahead of the next INF-triggered run. Deployed **one file** 14:08:26Z via boto3
`put_object` (avoiding the `--quiet` silent-no-op class CTO named). Verified **from S3 by independent
re-download**: 124,241 B, md5 `068bc089d436d296fe29e781a31bad04`, byte-identical to HEAD blob.
**Negative control: old 2-leg signature count = 0.** Siblings byte-identical (md5 match) -> one file moved.
Ledger `20260728T1407Z_mdpf-gold-aggregate-aua-cutover-cottonwood-restore`, L1 CLOSED, **L2/L3 OPEN**.

QA build (repo HEAD, local out-dir -- the producer has **no S3 write path at all**): reproduces 07-23
**exactly** (`1,951,676,164.42` @07-22, residual **0.00**, 47 cottonwood slots), sum identity **0 failing /
426 tested**, schema **purely additive** (8 top-level + 8 meta ADDED, 0 removed). 23 commits in the cutover
(I first told CTO ~14 -- an estimate I should have measured; corrected unprompted).
Known and accepted by CTO: the union axis (`:1617`) injects **18 non-trading dates** (16 weekend + Juneteenth
+ Independence Day obs.) -- pre-existing in the 07-23 artifact Andrew verified, W-7 AC-1 is a BASIS decision.

## Errors of mine this window (all caught, all corrected)

1. **Attributed a mechanism to COO's error without measuring it.** Claimed they hit the None trap; they had
   tested a constant-offset strawman. Did it in the same message where I asked CTO to hold my own claim as a
   hypothesis. COO's correction accepted in full; **two separate lessons banked, not merged.**
2. **"LENGTH 0" for an ABSENT key** (`.get(f) or []` flattens absent and empty). Key membership is the right
   instrument; `len(d[...])` KeyErrors.
3. **First L1 census constructed `blackdiamond/cot/...`** -- real scope `blackdiamond/cottonwood/`. Four
   false absences. Caught because DDB rows dated 07-27 made silence suspect.
4. **First L2 census counted ROW presence, not VALUE presence** -- printed 32/32 HEALTHY. Caught only by a
   targeted scan **disagreeing** with my own sweep.
5. **Nearly filed "8 silver Lambdas, zero schedules"** off `list-rules | head -30`; the API paginates at 100
   and there are 141. Caught by paginating on principle -- the only one of the five caught by method.
6. **Invented a clock reading:** wrote "at 15:05Z" in a message sent 14:41:22Z. Not a typo -- I was
   estimating elapsed time and stamping the estimate as an observation. COO caught it, then audited
   themselves and found they had called it *"the 15:10Z run"* for five hours for an event whose
   `ScheduleExpression` is **null**.

All six are one class, banked as `feedback_wrong_predicate_yields_a_well_formed_answer`:
**a wrong predicate returns a well-formed answer.** Danger ordering is INVERTED -- an absence invites
suspicion, a confident GREEN does not. **Five of six were caught by luck or by a second instrument
disagreeing, not by a control.**

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | "which artifact holds the MDPF global aggregate aua timeseries and is it fresh" | PARTIAL | routed to `comp-freshness`/`comp-pipescript io`; neither answers per-version BYTE SIZE, which was the actual symptom |
| `comp-pipescript deployed` | `dim_mdpf_aggregate_aua_timeseries.py` | **NO MATCH -- and that IS the finding** | swept `opal-data-bd`, returned "no scripts matched filter". mdpf is outside PIPELINE_MAP, so the deploy-verify tool is structurally blind to the tree whose deploy was broken |
| `comp-grep` | `cycle-complete`, `pipeline-complete`, `mdpf-daily-dispatch` | PASS | 20 matches / 23,988 files scanned; located the dispatch `:576` marker write + the Door-6 consumers |
| `commit-gate.sh` | n/a | NOT RUN | no `.py` edited this window -- the deploy moved an already-committed HEAD blob |
| `deploy_ledger.py` | 1 entry opened, L1 closed | PASS | L2/L3 deliberately left OPEN pending scheduled-run evidence |
| live primitives | `head-object`, `list-object-versions`, `get-role-policy` equivalents, `describe-rule`, `list-rules` (paginated), `describe-instances`, DDB `scan` | PASS | stage-2 verification per the standing two-stage order |

**What worked:** `comp-grep`'s systems-context footer pointed at `mdpf-daily-dispatch.sh` immediately, which
is where the ROLLUP-vs-REVAMP two-producer split became visible.
**What failed / gap found:** **`comp-pipescript deployed` cannot see the mdpf tree at all**, and it reports
that as `0 MATCH, 0 STALE, 0 MISSING` -- a clean-looking summary for a tree it does not cover. The DS-lane
mandate says run it before every gold run; on this pipeline it would have returned green-looking output for
7 days while the deployed code was 4 days stale. **UNCOVERED should not render as all-zeros.** Same gap
class as my 07-24 note that no comp-tool answers "which BUCKETS hold this key name".

## Open / next

1. **L2 + L3 ledger legs OPEN** -- require the next INF-triggered run's OWN log. **Do not close on the QA
   build.** COO ratified: if INF does not complete, they do not close today.
2. **Andrew-direct non-model trace** (CTO 142952Z, Andrew ~1427Z verbatim: *"the answer is 0824 schwab total
   value minus 49F smartx model aggregation, that is canonical balance"*): trace REVAMP `275,182,349.31` vs
   LEGACY `247,692,229.36` @07-22 against that definition. **Sequenced after the run.** Must label WHICH
   0824 quantity each consumed (BLENDED-PREFERRED ~$1,621.6mm vs SCHWAB-RPS ~$1,390mm+$23mm).
3. **Routed, not mine:** gold-DDB emitter identity/ownership (L2 escalation); Stage 6
   `build_dim_model_portfolio.py:392` AccessDenied (CloudOps); `mdpf` PIPELINE_MAP gate (CTO routing).
4. **CVO's independent re-derivation is NOT closed** by COO's fold -- explicitly held open.

## Guardrails held

Nothing written to `portal-v2/json/mdpf/*` (serve `5f758b47...` re-checked repeatedly, unchanged). No ad-hoc
gold run as a production path -- the one QA build wrote to a local scratchpad dir only. No silver/bronze
touched. Production `s3://opal-data-mdpf/code/` written **once**, under explicit CTO GO, verified from S3.
