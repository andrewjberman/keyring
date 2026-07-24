# Session Close: MDPF Global-Count Audit -> Channel-Independence Program -> Andrew-Paused Validation (1306-1949Z)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE, SCRIBE

**Date:** 2026-07-24
**Task Order:** ad-hoc (main-fabric CTO gate desk; Andrew-direct audit assignment ~1310Z)
**Status:** PAUSED BY ANDREW ~1946Z — validation between CTO + CVO only, fabric stood down

---

## Objective

Andrew-direct ~1310Z: personally audit the Global holdings-COUNT choppiness in the MDPF
aum-timeseries chart, determine data-vs-frontend, author a closeout PRD, route to COO, call
MSTR for spawn. Scope expanded through the session by seven further Andrew-direct rulings into
a full partner-channel-independence + monolith-migration program.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-which` | 4 routing questions (byte-verify, FE component, provenance, gold DDB) | PARTIAL | routed correctly twice; **MIS-ROUTED the mdpf lineage question** — returned `comp-freshness chain <bd\|inf\|cot>` / ranked `comp-dataflow` 3rd at 0.40 below two tools that do not answer it. Gate candidate. |
| `comp-grep` | `aum.timeseries`, `fact_taxsma_report`, `silver/rps` | PASS | located both producers + the served/staging keys; entry point for the whole trace |
| `pipescript mdpf` | named-thread traversal | **PASS — decisive** | surfaced `mdpf-freshness-checker` + its cron + alarm, which **do not exist live**. Also warned its own 39-day vintage and told me to verify. Instrument working exactly as designed. |
| `comp-dataflow gate` | 2 mdpf producer .py | **PASS — found what I missed** | 2 BLOCKING served-origin reads incl. one I had not identified (`dim_mdpf_aum_timeseries.py:92`); **printed its own blind spot** (4 of 8 unresolved-dynamic, counted in denominator) |
| `comp-dataflow origin` | served key | REFUSED (clean) | *"input-resolution refusal, NOT a clean 'no served reads'"* — correct third-state behaviour |
| `lib/trading_calendar.py` | 40 null dates + 83-feed sweep | PASS | 18 of 40 non-trading (correct nulls) / 22 real; source = hardcoded 2024-2027 fallback, stated |
| direct S3 + boto3 | served artifacts, spine, 83 silver feeds, bucket structure, live AWS resources | PASS | the measurement base for every finding below |

**What worked:** `pipescript` + `comp-dataflow` produced two findings no amount of hand-tracing
had reached, and both declared their own limits. **What failed:** my own instruments — a regex
that missed hyphenated partitions (returned empty, nearly reported as data), and a scratchpad
reaped mid-analysis by a concurrent process. **Gap found:** THREE — `comp-which` mis-routes
mdpf lineage; `pipescript --resource` has no mdpf thread (39d snapshot); `comp-pipescript io` is
**blind to `SERVED_BUCKET` reads on every tree** and emits a clean-looking manifest rather than
declaring the omission. That third is a modelling gap in the tool the fabric was just told to
use as primary for lineage.

---

## Work Completed

### 1. The audit (Andrew's actual ask) — VERDICT: DATA, not frontend
Global count series `account_count_total`: **407/447 present, 40 null**; trading calendar
resolved FIRST — 18 non-trading (correct), **22 real trading days**. FE is correct by design
and guard-blocked from client-summing (`pairedProvenanceRead.ts:70-72`), preserves honest nulls
(`connectNulls`, not `?? 0`). PRD `docs/architecture/MDPF_REVAMP_GLOBAL_COUNT_CLOSEOUT.md`
@`5d7522128`, amended 4x.

### 2. My own mechanism was WRONG — corrected by W-1 (`DS~A`)
I reported the poison as the model-cell rule (`:1719-1721`). **It is real in source and has
never once fired** — the poison is at the **FIRM axis** (`:1656`), one level up. **A fix to what
I described would have changed ZERO of the 40 dates.** Cottonwood attribution refuted on
magnitude (+442 not +408), sufficiency, AND mechanism (CVO: cottonwood is `measured`;
`frontier_stamp` belongs to 49F).

### 3. Program: MDPF_CHANNEL_INDEPENDENCE (7 Andrew-direct rulings)
`docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md` — three named event contracts (C1/C2/C3,
the gold->platinum leg did not exist), carry-forward Global with labelled held values,
manifest-only failure surface (no SES/alarms), normalised divergence (**raw cross-partner would
fire daily on a healthy estate — BD is D+2 by design**), roster-derived expectations,
**MIGRATE TO THE MONOLITH ENTIRELY** incl. platinum serve. **Closure set 12 -> 19 rows, growth
recorded explicitly.** Every row carries a **LIVENESS** obligation (repo-true AND runtime-true).

### 4. The findings that changed the diagnosis
- **MDPF has NO SCHEDULE** — `mdpf-daily-refresh-trigger` `ScheduleExpression: None`, event-only
  on the inf marker. A client-facing product is a passenger on an unrelated pipeline.
- **The documented freshness monitor DOES NOT EXIST** — `mdpf-freshness-checker` Lambda +
  `mdpf-freshness-check-trigger` cron + `mdpf-daily-freshness-stale` alarm all named in the
  estate census, all absent live. The 3 alarms that DO exist are FAILURE alarms; **none fires
  when the chain simply does not run.** That is why 6 days passed silently.
- **The deployed gold producer is 20 commits / +67,500 bytes behind** (51,999 vs 119,499 B).
  Every mechanism today's analysis reasoned about has ZERO occurrences in the running code.
- **`C1` ALREADY EXISTS AND NEVER STOPPED** (`0.6.2~C`): 8 live bronze->silver S3-event configs,
  fact_rps landing every trading day ~4 min behind bronze. **MDPF consumes an unwired LEGACY
  lineage while a wired one runs beside it.** My "six days unconverted" was true of the lineage
  MDPF reads and FALSE of the estate.
- **The bd rps converter drops 5 real positions** — `:41` binds `quantity_settled` to the raw
  `Quantity Settled/Unsettled` header; `:138`'s zero-quantity filter deletes them.

### 5. Law + doctrine
- `CLAUDE.md` **NEVER#4 AMENDED** @`7d2b8cf6f8` (Andrew-direct): ad-hoc gold runs PERMITTED for
  QA; **PRODUCTION PIPELINES MUST BE SCHEDULED** — a pipeline whose only trigger is another
  pipeline's success has no schedule and is a defect.
- `CLAUDE.md` R20 + `org/XXX.md` @`8419c5e6b3`: comp-surface-check **BLOCKS** on the portal side
  — corrected a stale record that under-promised a LIVE gate (all three copies, one commit).
- `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md` @`d3681d1d0`.
- `docs/architecture/NFRA_SENDGUARD_SPEC.md` @`ea4044d94`/`13ed31bb8` (Andrew-approved, secondary).

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Global carry-forward per feature, **labelled** | Andrew ~1703Z. Keeps BASIS constant, lets only VINTAGE go stale — unlike partner-summing which changes what the number IS |
| REFUSED "sum whichever partners are present" | CVO measured it: publishes `0` on 26 of 40 dates, reproduces the `0/94/255` historical defect |
| RC-1 landing **REFUSED** — close at ZERO recovered | No clean mechanism for INF; the only path silently reverts on the next producer run. A repair with a hidden expiry is worse than a visible gap |
| Divergence metric NORMALISED, never raw | BD is D+2 BY DESIGN (14/14 measured) — raw comparison alarms daily on a healthy estate |
| Bronze write for arbitrary-date test **REFUSED** | Rule 17a; and the test would not prove the property anyway. UNEXERCISED is the honest record |
| Liveness column on every closure row | The deployed producer is 20 commits behind; 16 rows verified against the repo would be true about a FILE and false about a RUNTIME |

---

## Blockers

**PAUSED BY ANDREW ~1946Z** — not a defect blocker. Validation between CTO + CVO only.
**GitHub Actions billing-blocked org-wide since ~14:22Z** (Andrew-only fix): all Lambda/EC2/
portal PROD deploys refused at dispatch; 100/100 workspace runs failed.

---

## Current State

> **NOTHING WAS APPLIED TO LIVE AWS THIS SESSION.** No terraform apply, no EC2 deploy, no Lambda
> update. The M3 code refresh was authorized then HELD — **verified: no bytes moved**, all four
> `s3://opal-data-mdpf/code/scripts/gold/` objects unchanged (rollback VersionIds recorded in
> COO's 194702Z handoff). Both GOs withdrawn, neither acted on. Nothing half-landed.

Repo HEAD `c5acbcf04c`, all my commits pushed. Programme design is settled and sovereign-ruled;
**19 closure rows with named owners, and essentially none is runtime-verified.** The chain last
built 2026-07-23T21:44Z; the served artifacts are fresh but were **NOT produced by the deployed
code** (they carry classes it cannot emit) — leading explanation is Andrew's own hand-invocation
of `opal-assets-mdpf-portal-publisher`, **INFERRED not confirmed** (Lambda `Invoke` is a DATA
event; the management-event query structurally cannot see it).

**Corrections I owe forward:** (1) the "~$81K of dropped holdings" is **one of two defensible
readings** — $0.00 is the other and the monolith's own stored value agrees with zero; I
multiplied `quantity_settled` x price while the stored market value pairs with
`quantity_settled_unsettled`, **the same two-similar-columns error I had just diagnosed in the
converter**. (2) My cadence inference dismissed 15 of 18 lagged silver feeds — derived from
median inter-partition gaps, not a declared cadence. Both are with CVO.

---

## Next Steps

1. **[3.0.0_SA_CVO]** Validation verdict on my ESTABLISHED/INFERRED/UNVERIFIED list (my
   194517Z) — specifically re-measure the three load-bearing facts and attack the cadence
   inference.
2. **[Andrew]** Clear the GitHub Actions billing block; decide when the fabric resumes.
3. **[1.0.0_SA_CTO + 0.7.0_AE_CloudOps]** M3 refresh — census + `--delete` casualty list first,
   ONE writer, then ONE scheduled run to establish what actually works.
4. **[deferred]** Rows 1-19 runtime verification; the three comp-tool gate candidates.
