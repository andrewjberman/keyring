# 0.4.0_DS_ClientPlatform -- 2026-07-28 1451-2004Z -- scheduled run VERIFIED, legacy DEPRECATED (Andrew-direct), P1 accrual landed

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, IMPLEMENT, SCRIBE

Window: 1451Z (prior log `d27a2913c`) -> 2004Z. Continuation of the MDPF Cottonwood P0 session.
4 commits, ~12 MCP exchanges with CTO/COO (+1 MSTR custody copy), 1 sovereign ruling received.

---

## Summary

| item | outcome |
|---|---|
| L2/L3 ledger legs | **CLOSED 3/3 on SCHEDULED-run evidence** -- identity 0/426 failing, cottonwood restored, serve held |
| Andrew-direct ruling | **DEPRECATE LEGACY, move full force to REVAMP canonical** -- recorded verbatim, broadcast same turn |
| Non-model trace | **REVAMP satisfies the canonical; LEGACY does not** -- and the quoted `$27.49mm @07-22` pair does not exist |
| Cottonwood emit gap | **ROOT-CAUSED: same defect as Stage 6 rc=1**, plus an independent `_interpolated` read-preference defect |
| P1 accrual | **11 objects live**, R4 + R5 both exercised, `advi`-generalisable by construction |

---

## 1. The scheduled run VERIFIED the morning's cutover (L2/L3 closed)

Run `mdpf_daily_20260728_164452`; runner launched 16:44:36Z on INF's marker (INF completed 15:04:07Z).

**The discriminating evidence is not the timestamp -- it is that the run emitted a 3-firm global**, which
the pre-deploy two-leg `build_global_artifact(a49, ainf)` cannot produce at all.
```
gold/mdpf_revamp/global/aggregate_aua_timeseries.json  16:48:04Z  275,860 B
  450 dates - cohort_provenance n=450 - cottonwood non-absent slots 47
  SUM IDENTITY  426 tested, FAILING 0            (was 425/425 FAILING)
  @2026-07-22 = 1,951,676,164.42                 EXACT vs the 07-23 reference
SERVE UNCHANGED  ETag 5f758b47... / 254,419 B
DEPLOYED CODE re-hashed after the --delete sync: 124,241 B md5 068bc089... INTACT
```
**Both portal-v2 denies were EXERCISED IN PRODUCTION, not simulated** -- 4x AccessDenied on
`json/mdpf/{,global,49financial,inflection}` (ROLLUP try/except -> WARN+continue, rc=0, exactly as CTO
predicted) and 1x on `json/portfolios/aum-timeseries.json` from the second statement
`P0DenyLegacyPortfoliosClobber20260728`.

Ledger `20260728T1407Z_mdpf-gold-aggregate-aua-cutover-cottonwood-restore` **CLOSED 3/3** @`bb2a42e0c`.

## 2. ANDREW-DIRECT 20260728T171003Z -- recorded @`bf986d81a`, broadcast same turn

> **"we dont care what legacy does, we want to move full force into the REVAMP canonical structure and deprecate legacy"**

VERBATIM, timestamp read from `date -u` (not inferred). Broadcast to CTO + COO + MSTR per XXX.md. Scope
stated, **not adjudicated** -- the ROLLUP step, `platinum/mdpf/*`, the legacy emit and the cutover
sequencing are CTO+COO's to route. It answered an open question I had put to CTO minutes earlier (take the
sanctioned SmartX new-vs-legacy dig? **no**). Consequence surfaced, not decided: **deprecating legacy removes
the only producer ever wired to the serve, and its replacement does not exist** -- L3's publisher goes from
"next" to "only".

## 3. Non-model trace (Andrew's canonical: `0824 total - 49F smartx model aggregation`)

**REVAMP SATISFIES IT** @07-27: custody `1,684,259,082.58` == `fact_rps_s2.net_mv_plus_cash` EXACT; model
`1,406,447,440.23` == ALL-rmids minus the 2 SMA sleeves = core-only(5); non_model == custody - model, to the
cent. **Basis LABELLED per the never-SUBSTITUTE law: it consumes the SCHWAB-RPS full envelope (the C2 spec),
NOT the BLENDED-PREFERRED ~$1,621.6mm quantity.**

**LEGACY DOES NOT** -- implied total `1,641,269,345.33` reconciles to **no** 0824 quantity (nearest miss
~$11.9mm). *Measured that it does not reconcile; its source is NOT traced and I named no mechanism.*

**Two premise corrections:** (a) the quoted `REVAMP 275,182,349.31 vs LEGACY 247,692,229.36 @2026-07-22`
**pair does not exist** -- legacy has no 07-22 (5-trading-day hole 07-20..07-24) and its `247,692,229.36`
sits at **07-18**, where REVAMP is None. (b) But the disagreement is REAL and **understated**: on the 408
shared dates, **0 identical / 408 differing**, median `39,341,353.48`, max `167,391,370.89`.
**Third finding:** 25 legacy-only dates are **market holidays** REVAMP correctly excludes -- the producers
differ on the CALENDAR as well as the basis, so any date-join between them mixes both.

## 4. Cottonwood emit gap -- ONE defect with Stage 6 rc=1, plus a second independent one

`mdpf-daily-dispatch.sh` 6d block, source-confirmed:
```
:523  build_dim_model_portfolio.py   --upload || return 1   <- AccessDenied TODAY
:524  build_cottonwood_mdpf_pair.py  --upload || return 1   <- NEVER EXECUTED
:525  build_cottonwood_mdpf_slice.py --upload || return 1   <- NEVER EXECUTED (writes the artifact)
```
**Stage 6 rc=1 and the missing cottonwood artifact are the SAME defect.** It had been filed as a cosmetic
streak-blocker; it is what produced the mixed-vintage set that cancelled CTO's bridge publish. CTO
re-prioritised AE's grants to #1 on this.

The aggregate producer has **no cottonwood emit path at all** (`:2014` choices, `:2022` want-set, `:2036`
emit loop -- cottonwood in none; zero write sites). CTO's inference ("the gap is in the EMIT step") was
right in direction, **wrong in location** -- it is the READ path.

**SECOND, INDEPENDENT DEFECT:** `load_cottonwood_slice:1552-1553` prefers
`aggregate_aua_timeseries_interpolated.json`, whose producer appears in the daily dispatch **0 times** (a
one-off backfill, last written 07-23T21:45:49Z). **So even with the IAM fixed and `:524`/`:525` running, the
aggregate would still read the 07-23 one-off and ignore the fresh artifact.** CTO: *"we would have landed the
grants, seen `:525` write a fresh artifact, and declared cottonwood fixed."* Removal is mine to land, **held**
until AE's grants land and a fresh cottonwood artifact demonstrably exists (PRD §16 A4 already rules it).

**Caveat volunteered against my own good result:** today's global folds a cottonwood leg covering
2026-05-28..2026-07-22 onto an axis reaching 2026-07-27 -- **correct in composition, stale in vintage.**

## 5. P1 accrual (CTO GO 193933Z) -- `portal/gold/{product}/{scope}/{artifact-type}/{DATA-as-of}.json`

`data/mdpf/scripts/gold/build_portal_gold_accrual.py` @`6493257fc`, re-declared @`9e69057c9`.

**A2 by construction:** `{product}` is a parameter, scopes DERIVED from `partner_roster.json`
(`['49financial','cottonwood','inflection']` + literal `global`), types DECLARED per product. **Adding `advi`
is two data entries and zero code.**

**Dates are DATA as-of, derived from each artifact's own content** -- `as_of_last` / `period` /
`time_series[-1].period` / `value_date` (NOT `assignment_date`). **A type whose as-of cannot be derived is an
ERROR and the run refuses it rather than stamping a run date** -- under R5 a wrong date is never overwritten,
only accompanied, so a false vintage would be PERMANENT. The platinum artifact committed that defect once
today.

**11 objects landed**, verified by independent S3 listing. **The layout earned its keep on day one:**
cottonwood lands at its TRUE vintage (07-20/07-22) beside three scopes at 07-27/07-28 -- the split-brain is
legible from key names alone, where this morning the same fact cost hours of `list-object-versions`
archaeology.

**Two open calls I surfaced rather than let my code silently rule; CTO ruled BOTH:**
- **`aum-metrics` = DRIFT, not by-design.** I had declared it cottonwood-only, **disarming R4 on three real
  gaps while implementing R4.** Re-declared on all scopes -> R4 now errors on 3 (rc=1), which is the correct
  output. Verified CTO's citation myself (`aum.ts:696` firmId-templated, per-firm cache `:690`, comment
  `:632-634`) **and found a second consumer he did not cite** -- `portal-proxy.ts:268,277` fetches
  `/api/general/portfolios/aum-metrics.json`, which under R2 is global-scope. Two independent consumers.
- **R5 refuse-to-clobber RATIFIED**; PRD wording amended by CTO, code unchanged, `--allow-overwrite` stays
  explicit and OFF.
- **`account-units` marked `UNVERIFIED -- needs a consumer trace`** in the declaration itself. 0 hits across
  `portal/src` `*.ts/*.tsx` -- **stated with its denominator, because an empty grep and a true absence are
  indistinguishable** and I would not launder it into evidence merely because it agrees with the cautious
  answer.

## Errors of mine this window (all caught, all corrected)

1. **Invented a clock reading** -- "at 15:05Z" in a message sent 14:41:22Z. Not a typo: I was estimating
   elapsed time and stamping the estimate as an observation. COO caught it, then audited themselves and found
   they had called it *"the 15:10Z run"* for five hours for an event whose `ScheduleExpression` is **null**.
   Adopted: read `date -u` before stamping any time; never name an event by a clock it does not have.
2. **Flagged `LEGACY-EMIT rc=1` as unpredicted collateral from a mis-scoped deny** -- wrong; live
   `get-role-policy` shows TWO deliberate same-dated Deny statements. **I nearly reported a working control as
   a bug**, stopped only by reading the applied policy instead of the description of it. COO's framing: the
   error direction would have caused someone to REMOVE a control doing its job.
3. **Nearly raised a false blocker on the accrual path** (§13.2 `gold/mdpf/` vs §16 `portal/gold/mdpf/`) --
   §16 is the LATER Andrew-direct ruling and explicitly supersedes; I had read §13 and not §16.
4. **Declared `aum-metrics` cottonwood-only**, encoding three real gaps as by-design (see above).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-grep` | `mdpf_revamp/cottonwood`, `cycle-complete`, `pipeline-complete`, `portal/gold/{product}` | PASS | located the 3 cottonwood producers + the PRD accrual spec; systems-context footer pointed at the dispatch |
| `commit-gate.sh` | `build_portal_gold_accrual.py` x2 | PASS | clean both times (py39 target) |
| `deploy_ledger.py` | close-leg L2, L3; close | PASS | 3/3 legs proven, sentinel removed |
| `comp-which` | (earlier window) MDPF global artifact freshness | PARTIAL | routes to `comp-freshness`; neither answers per-version BYTE SIZE, which was the symptom |
| live primitives | `head-object`, `list-object-versions`, `get-role-policy`, `describe-rule`, `list-rules` (paginated), `describe-instances`, DDB `scan`, `ec2 describe-instances` | PASS | stage-2 verification per the standing two-stage order |

**What worked:** `comp-grep`'s dependency footer put me on `mdpf-daily-dispatch.sh` immediately, which is
where the `|| return 1` short-circuit -- the whole cottonwood answer -- became visible.
**What failed / gap found (repeat of my 07-24 filing):** `comp-pipescript deployed` **cannot see the mdpf
tree at all** and reports that as `0 MATCH, 0 STALE, 0 MISSING` -- a clean-looking summary for a tree it does
not cover. On this pipeline the DS-lane mandate would have returned green-looking output for 7 days while the
deployed code was 4 days stale. **UNCOVERED must not render as all-zeros.**

## Files Modified

See commit messages: `bb2a42e0c`, `bf986d81a`, `6493257fc`, `9e69057c9`.

| file | note |
|---|---|
| `data/mdpf/scripts/gold/build_portal_gold_accrual.py` | NEW -- P1 accrual writer, product-parameterised, roster-derived scopes, R1/R4/R5/A3/A4 |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260728T1710Z_*.md` | NEW -- sovereign ruling, verbatim + scope + consequences |
| `org/critical_paths/change_management/20260728T1407Z_*_deploy_completion.md` | CLOSED 3/3 |

## Blockers

**None BLOCKED.** Two items HELD BY DESIGN, both on an external gate with a named owner:
- **Read-preference removal (`load_cottonwood_slice:1552-1553`)** -- held until AE's IAM grants land AND a
  fresh cottonwood artifact demonstrably exists. CTO-ruled ordering (production before consumption);
  removing it first would swing the producer onto a 07-23 PARTIAL, strictly worse than today.
- **Publish of any kind** -- L1 gates it and `portal-v2/json/mdpf/*` is CTO-held. I have written nothing there.

## Current State

- **Producer:** `dim_mdpf_aggregate_aua_timeseries.py` deployed at
  `s3://opal-data-mdpf/code/scripts/gold/`, 124,241 B md5 `068bc089d436d296fe29e781a31bad04`, == repo HEAD
  == origin/CLOUD. Verified intact after the run's `--delete` sync.
- **Gold (scheduled, correct):** `gold/mdpf_revamp/global/aggregate_aua_timeseries.json` @16:48:04Z,
  275,860 B, 450 dates, identity 0-failing, cottonwood 47 slots -- **cottonwood leg stale to 07-22**.
- **Accrual (new, nothing reads it):** 11 objects under
  `s3://opal-data-assets/portal/gold/mdpf/{scope}/{artifact-type}/{date}.json`. R4 currently errors on 3
  (`aum_metrics` absent for 49financial/inflection/global) -- **that is the correct output.**
- **Serve:** `portal-v2/json/mdpf/global/aggregate-aua-timeseries.json` ETag `5f758b47...`, 254,419 B, the
  hand-restored 07-23 artifact @2026-07-28T13:41:05Z. Fed by NEITHER producer; both denies exercised.
- **Unfixed and not mine:** gold DDB value-stall (13/32 cohorts incl. `_global__aua_total`, since 07-21/22,
  untraced/unowned); `mdpf` absent from `PIPELINE_MAP`; Stage 6 rc=1 IAM gap;
  `json/portfolios/aum-timeseries.json` frozen 07-27 by deny leg 2 (COO owns the consumer question).

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** land the `_interpolated` read-preference removal ONCE AE's grants are in and
   a fresh cottonwood artifact exists; exercise it and report WHICH artifact the producer actually read.
2. **[0.7.0_AE_CloudOps]** the `build_dim_model_portfolio.py` PutObject grant -- now #1, it gates the
   cottonwood emitters at dispatch `:524`/`:525`.
3. **[1.0.0_SA_CTO]** `account-units` consumer trace (routed by him); `mdpf` PIPELINE_MAP gate; the publisher
   (now the only thing between correct gold and the serve).
4. **[2.0.0_SA_COO]** `json/portfolios/aum-timeseries.json` consumer question; gold-DDB emitter ownership.
5. **[0.4.0_DS_ClientPlatform]** `account-distribution` within-run vintage divergence (49F+global 07-28,
   inflection 07-27) -- logged as a PRD open item, not chased.
