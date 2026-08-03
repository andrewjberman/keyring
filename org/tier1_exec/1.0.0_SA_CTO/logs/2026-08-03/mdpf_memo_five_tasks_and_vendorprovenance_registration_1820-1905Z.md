# MDPF memo transcription -> five-task fold + OPAL_VENDORPROVENANCE registration (1820-1905Z)

**archetype:** SCRIBE
**secondary_archetypes:** TRACE, VALIDATE

Andrew-direct: transcribe `MDPF architecture and cleanup_2971.m4a`, review against the associated
workstream record (incl. the ETFS Orion briefing), then land analysis + project registry, bucketed
MDPF_GLOBAL vs OPAL_VENDORPROVENANCE (his explicit split).

## What landed (all committed this window)

1. **Transcript reference** `docs/references/MDPF_ARCH_CLEANUP_ANDREW_MEMO_20260803.md` — verbatim
   9m12s machine transcript (openai-whisper `small`, provenance disclosed), the five tasks extracted,
   and the typed half of the ruling (as-of prerequisite + NYSE sync + the project split) quoted verbatim.
2. **MDPF_GLOBAL PRD Addendum C** — T1-T5 execution plan, each task live-grounded 2026-08-03; the C.3
   structural finding (two producer families writing platinum is itself the defect) surfaced for the
   decomposition, with a producer-unification recommendation.
3. **`docs/architecture/OPAL_VENDORPROVENANCE_PRD.md` v1.0** — As-Of Contract Registry design, NYSE
   calendar unification, ingest provenance stamps, stable-key census, completeness verdicts; 5 WS;
   3 CTO decisions with recommendations.
4. **Registry:** MDPF_GLOBAL.json (phase -> PHASE 1 execution-plan-ruled; five tasks as
   `execution_tasks_20260803`; blocking compacted, M9 still-binding clauses preserved;
   pending_from_andrew resolved), OPAL_VENDORPROVENANCE.json created, REGISTRY.md both rows,
   MACRO_CODES.md OPAL row extended.

## Live-grounded findings folded into Addendum C (the load-bearing ones)

- `mdpf-daily-refresh-trigger` is STILL `ScheduleExpression: None` (ENABLED) — and this morning INF wrote
  `pipeline-failed.json` (10:50), the completion sentinel never appeared, the runner chain never fired:
  **the memo's named anti-pattern reproduced the delay Andrew observed, live, the same day.**
- Twin platinum producer planes diverge: accrual/hyphen ran 08-03 12:15 ET but ends 07-30; runner/underscore
  ends 07-31 but did not run. Served Global view (`/api/general/mdpf/*` -> `platinum/mdpf/*` per
  comp-routes DESIRED trace) = the 07-30-ending file. Delay CONFIRMED at content level; truncation
  mechanism labeled INFERRED, first T2 work item.
- Cottonwood: no dedicated scheduled MDPF leg (cron(0 2) seed -> cot-bd-session-trigger event-chain),
  absent from the underscore plane entirely — Andrew's observation confirmed.
- `opal-data-mdpf` is NOT dead-only: `code/mdpf-daily-dispatch.sh` is the live runner pull path — T5 must
  migrate the code store (or retire the runner chain per C.3) before any kill.

## Compiler Tools

| tool | result |
|---|---|
| comp-estate (--list, model-portfolios, mdpf) | PASS — vertical maps; census honestly 5d stale vs live (disclosed in outputs) |
| comp-routes trace /api/general/mdpf/aggregate-aua-timeseries.json | PASS — platinum rewrite pinned (DESIRED plane; live-CF grounding assigned to T3) |
| comp-grep aggregate-aua-timeseries.json data/mdpf | PASS — producer/consumer census, 14 hits/7 files |
| comp-freshness | consulted usage only (bd/inf/cot chains scope; mdpf artifact freshness taken from live s3 ls + content reads instead) |
| live primitives (s3 ls x6, s3 cp x3 + content parse, events list-rules/list-targets, scheduler get-schedule — rail-checked markers on inspections) | PASS — every Addendum-C claim carries a live grounding or an INFERRED label |

Gap noted (pre-existing, CVO register): comp-routes cache-policy blindness — bound into T3's gate.

## Open at close

- COO decomposition of T1-T5 + OPAL_VENDORPROVENANCE WS-1..5 (broadcast sent this window).
- CTO owes C.3 producer-unification ruling at decomposition; D-1/D-2/D-3 VENDORPROVENANCE decisions.
- A.2 audit-archive coverage finding from startup (org/tombstone-gate-audit.log not in MANIFEST) — unrouted.
