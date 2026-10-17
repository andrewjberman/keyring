# 3.0.0_SA_CVO~IRPT -- session 2026-10-16 18:45Z to 2026-10-17 01:10Z (dell2): IRPT L8 compiles, L9 grades

**archetype:** VALIDATE

Continues `../2026-10-16/session_CVO-IRPT_0950Z-1845Z.md`. Same mechanism (in-session fork; every criterion re-run;
live state read-only; one ADJUDICATION and one slug per round to 1.0.0_SA_CTO~DELL2).

## Work (6 adjudications)

| project | lane | round | adj | commit | note |
|---|---|---|---|---|---|
| IRPT_DASHBD | ~F2 F-SHIP | 136 | v146 | ed7c7c5388 | J1/J2 PASS 20/20 (newest snapshot); one-snapshot read in code; S6 final INTERNAL (CTO msg 9669) |
| IRPT_ANLREQ | ~T2 | FWD-5 | v26 | 46ac9ad58f | FAIL unproven: 7/7 refused vs working control; packaged ticket never tried; 5 read routes + metrics + no-tenant not driven |
| IRPT_DASHBD | ~F2 F-SHIP | 135 | v147 | f9efd824fa | owed packet; one criterion narrowed to added lines while the script still holds 10 non-ASCII chars |
| IRPT_DASHBD | ~D2 | 149 pkt 5 | v148, v149 | 1050831467, e4fcb3a160 | served moves match signed counts (both halves); composed account ids contradict the contract (:126, :157); 3 pair ledger closures uncommitted |
| IRPT_ANLREQ | ~T2 | FWD-5 add. 1 | v27 | fb038e1278 | FAIL unproven: 26/26 refused, but the packaged leg has no working control; METRICS and writes not driven |

## Routing

TCKT_VNEXT r18/r19 (msg 9841) is non-IRPT: routed to the CTO (20:30Z); 3.0.0_SA_CVO~DELL2 graded it (TCKT_VNEXT
ADJUDICATION_v8 @a08573509a). This seat did not grade it.

## MCP traffic

Received and acked: 9841, 9937, 9971, 9973, 10050, 10094. Sent: one slug per round above; the TCKT routing note.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criterion invocations on trunk | PASS / FAIL as tabled | |
| raw live-sitting records read call by call | PASS | v26, v27 |
| live identity read (principals removed) | PASS | v26, v27 |
| live S3 per-day counts vs signed tables (read-only) | PASS | v148 |

What worked: refusing EXERCISED-AGAINST credit to refusals with no working positive control on the same route (v27).
What failed: an instruction of mine carried a stale S6 premise (EXTERNAL); the fork read the later ruling (v146).
Gap found: deploy-ledger closures can sit uncommitted in the shared tree while HEAD reads OPEN (v148).

## Current State

- Watcher re-armed on each expiry; inbox empty at 01:11Z. Zero crons.
- Adjudications this window: IRPT_DASHBD v146-v149; IRPT_ANLREQ v26-v27.
- Push state: origin box/dell2 reads e309694628 (ls-remote 01:11Z).

## Blockers

None in this lane.

## Next Steps

- [2.0.0_SA_COO~D2] Commit the three pair ledger closures (v148); contract update for composed account ids.
- [2.0.0_SA_COO~T2] FWD-5: a sitting where the request owner is served each packaged file, plus METRICS and writes.
- [Andrew] v143's 49F Performance-page change is now COO-signed after the fact; approve or roll back stands.
- [3.0.0_SA_CVO~IRPT] Compile and slug every new IRPT L8 packet.

-- 3.0.0_SA_CVO~IRPT
