# /self-drive dell2-box -- tick 176 (2026-10-20 ~15:00Z-15:27Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** tick 176, since the tick 175 log (@bffa5709a9). state: ARMED.

## Run 7: STOP at B2 (IB2, `A_E2E7.txt`, 15:23Z)

- **Result:** the PROD page uploaded, then the ticket create was refused ("the ticket could not be created"). Nothing was filed.
  Six of 8 synthetic keys were deleted; two S3 state objects stay (row S229). Row S230 records the refusal.
- **Cause, read here:**
  - `portal src/pages/TicketCenter/AnalysisRequestParts.tsx:83-85` at origin/PROD drops a blank advisor (AR-y-429 assumed a
    service fallback).
  - `infra/aws/lambda/ticket_center/lambda_function.py:115` has `advisor` `required: True` with no fallback, and
    `_validate_answers` refuses "answer 'advisor' is required".
  - The run's staff filer left Advisor blank.
- **Ruling** (msgs 11384, 11385): the service is unchanged and the page always sends an Advisor.
  - `4.0.0_SA_CRO~TCKT` amends `cand/dell2/anlreq-andrew-walk` so Advisor is required for every filer: pre-filled, labelled
    required, a blank refused in words, and a test through the service's rule.
  - Then a re-posted row, the DT promote, and run 7b on the same terms.
- **Trade read-back:** run 7 is terminal, so TO-R21-RB1 may run before 7b. MSTR re-seats TV2 (msgs 11386, 11387); 7b waits for
  RB1 to be terminal.

## Rulings and approvals

| item | ruling |
|---|---|
| Row 500c, the Andrew-walk form f41b4fce (`~TCKT` 15:08Z) | APPROVED @7715e07aec, Opal-internal. `analysisRequest.ts` is unchanged. DEV now; PROD after run 7 is terminal (now superseded by the advisor amendment, which re-posts the row). |
| The firm-neutral Opal model source (design fork; CRO research @c05a6b6841) | R1 @665110f9c2: the model return series plus current weights for FWD-10; a dated extract at a builder address for FWD-11; MDPF rejected as firm-keyed; the model-code map written down. The key corrected @b9de1e559d: `json/benchmarks/model_portfolio_timeseries.json` (read here: 780,910 B, 11:06:27Z; the yang key is 404). |
| The swap model leg (`~TCKT` items, @15cfc42950) | R2: wired as C-SWAP states, under FWD-2; owner `~Y2`. |
| The audit record (the same file) | R3: a new `analysis-report` family, schema plus four linkages, kept 2,555 days; owner `~Y2`. |

All of R1 to R3 land in PRD v0.25 with FWD-9 to FWD-12 once Andrew confirms the DONE WHEN lines.

## Acts only Andrew can do

- **Confirm the DONE WHEN lines of FWD-9 to FWD-12.** Andrew-direct 2026-09-03: "I will confirm CTO's DONE WHEN from their
  /endpoint --forward".
- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"): `C:\dev\wk-irpt-dashbd-503`; row 544d; row 65a1; row a392.
- **S3 deletes:** row 6e7c; row 128f; the synthetic leftovers of runs 4 to 7 (run 7: row S229, two objects).

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
