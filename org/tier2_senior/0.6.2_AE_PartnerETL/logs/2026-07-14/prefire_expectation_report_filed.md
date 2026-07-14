# 0.6.2_AE_PartnerETL -- the pre-fire EXPECTATION REPORT filed (the swap gate's input), with the backlog refusal family measured to the day

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE
**Date:** 2026-07-14 | **Window:** ~16:2xZ -> ~16:5xZ | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Queue head executed: the pre-fire expectation report for CTO's V2-8 swap gate is FILED @ fbdb335b4
(pushed) and on CTO's desk (165407Z), in the 113326Z shape + the 162512Z dtype addendum CTO added
mid-session. Method was exercise, not assertion: the committed conversion path (parse -> T1 -> dedup ->
typed_table -> project) run IN MEMORY, zero S3 writes, over 87 real bronze objects both lanes -- all 29
newest partitions (29/29 clean, every pipe file T1-tied, 8/8 projection parity, dedup=0, census
reproduced byte-for-byte on shared partitions) + 58 oldest/middle backlog vintages.

**The dtype-refusal class (CTO 162512Z, eclipse live datum) is priced both ways:** structurally the class
cannot fire (schwab_schemas @ e9d1a6817 carries ZERO integer declarations; 275 decimal128 pinned from
VENDOR field widths; whole-looking numerics stay string) and by exercise (0 cast errors in 87 parses,
2023->2026 vintages).

**The vintage exercise FOUND the one real refusal family pre-fire (predicted, not to-be-discovered):**
(1) vendor APPENDED `schwab_order_id` + `versmrkr_7/8` to RLD/RLU/RLY on **2025-07-18 exactly**
(binary-searched on rld, 10 probes; boundary identical both lanes; rlu/rly brackets consistent; rlw born
post-boundary; rtu/rty unaffected) -> 538 pre-boundary partitions/lane refuse SchemaDriftError, loud,
landing nothing; (2) one zero-row rld shell per lane @ 2025-01-09 (markets closed -- trading-calendar
resolved BEFORE calling it a defect) -> CrsFormatError quarantine. Steady-state residual = 539/lane until
a delta-5 pin extension (module's own remedy: reclassify APPENDED @ census 2025-07-18) + a shell ruling
(0-row-shell law vs stay-quarantined). Both flagged as CTO gate decisions; NO code changed.

**Also enumerated, not assumed:** rld day-law sweep refusals = ZERO (all 754 dates both lanes carry rld);
bronze key recount ties the guard baseline (5,978 / 6,945); sweep #1 (12:15Z 07-15) predicted
TIMEOUT-KILLED mid-backlog as nominal (no per-run bound in _sweep_lane vs ~12.9K backlog; landings
durable+idempotent; that run's manifest will NOT land -- documented so nobody reads it as a broken deploy).

MCP: report to CTO (gate owner), FYI to COO (board), apply-facts to 0.7.0 (swap vehicle), contract-touch
heads-up to DS (delta-5 + shell ruling will land on the contract). Startup this session: /watcher armed
(Monitor bivxrm2lf), LD-0290 serial file written, re-registered (was STALE).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| comp-to | session TO context (OPAL_ASSETS.V2-2) | OK, race-free per-session file |
| comp-grep x5 / comp-glob x3 | locate verdict vocabulary, B-compressed precedent, dictionary, TF schedules, constants | OK on-rails; 1 gotcha self-caught (escaped-pipe warning -> re-ran with bare pipe) |
| .tools/commit-gate.sh | Rule 14 on the 2 evidence .py | PASS (1 F401 caught -> fixed -> clean) |
| aws s3api list-objects-v2 (operational, read-only) | run-time denominators: latest keys, full-lane walks, size census, rld/rlu/rly date lists | ties guard baseline exactly |
| committed path exercise (parse_crs/cs_reader/typed_table/project, in-memory) | THE report's instrument: 29 newest + 58 vintage objects | 75/87 clean, 12 refusals = the measured finding |

**What worked:** exercising the real code path over real bytes beat every static answer -- it reproduced
the census (positive control), priced the dtype class empirically, and surfaced the rl* boundary + shells
that NO amount of newest-vintage care would have caught. Binary search made the boundary exact for 10
downloads. **What failed/caught:** my first vintage-run tail truncated the 0824 head (tail -75 vs 218
lines) -- re-read the full file before concluding; ruff F401 on a copied script. **Gap found:** none in
the tools; the sweep's missing time-bound is a DESIGN fact now documented in the report rather than a
day-2 surprise.

## Blockers

None on my lane. The swap is correctly GATED on CTO signing the filed report; the delta-5 pin extension +
shell ruling are CTO/DS decisions I do not pre-empt.

## Next Steps

- **[0.6.2 self]** On CTO signoff: coordinate the swap with 0.7.0 (their saved 0/2/0 plan), then watch the
  evening fires (21:45/22:15Z) + tomorrow's 12:15Z sweep against the report's S2/S6 tables. On a CTO
  delta-5 GO: the rl* pin extension (APPENDED @ 2025-07-18) + shell-law change, gate-checked, DS-reviewed.
- **[1.0.0_SA_CTO]** the gate: sign / amend / hold the report; rule delta-5 + the shell disposition.
- **[0.7.0_AE_CloudOps]** apply on CTO's GO (facts for the apply already MCP'd).
- **[0.4.0_DS_ClientPlatform]** contract touch lands with delta-5 when ruled.
