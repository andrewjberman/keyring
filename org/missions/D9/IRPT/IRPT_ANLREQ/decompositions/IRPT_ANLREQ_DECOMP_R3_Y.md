# IRPT_ANLREQ -- decomposition, round 3, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO round-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_3_20261011.md`
@430d79e86d, section 4, workstream Y's ENRICHMENT LIST (Y1-Y5 and row D2-S31). No PRD addendum; the endpoint is unchanged.
Workstream G (the resident releases) is `2.0.0_SA_COO~G2`'s and cuts its own issuance from the same section; its write surface is disjoint.

**Thread:** FWD-1 is not live (its last hop, the attach, has no code; workstream G, analysis G3). This round enriches the served reads and
closes what round 2's releases left unmeasured. It does not make the thread live.

## Cells

| cell | analysis item | what is built | write set | risk |
|---|---|---|---|---|
| `AR-y-31` | Y1, row D2-S20 | The ticket package's "Report" file opens the FINISHED report through `getOwnedAnalysisReport`, rendered with Investor Reporting's `RetainedSections`; the request record is never shown as the report | portal `TicketCenter/AnalysisRequestParts.tsx` + two test files | LOCAL (portal product file: candidate to the CTO before DEV) |
| `AR-y-32` | Y2, rows D2-S24 + D2-S21, and row IRPT_YCDGEN-D2-S38 (joined by the CTO's IRPT_YCDGEN round-8 ADDENDUM 8.1 @02689893e2, msg 4333) | irpt-status's served reads gain two members: `analysis-report` returns `retained_ref` in the shape Performance serves; each row of the owned-request history states `client_id`, the client its frozen selection names (null for an upload). Contract documents updated; both arms of each tested. AND `section_dates()` reads a report by its own provider branch: an `opal_engine` row with status NOT_AVAILABLE and a null date is an undated row | `ops/owned_report.py`, `ops/owned_requests.py`, `ops/entry.py`, `ops/prospect_dates.py`, three new test files, two contract documents | WORLD by the gate's floor for an `infra/` path (build only; the release is one apply order after the drain) |
| `AR-y-33` | Y3 row D2-W41-S17, and Y4's first item (row D2-S32) | The source map says, per function, which source-dir files are outside the package ON PURPOSE, and the parity check honours it, so the store function builds clean with no skip flag; the map records irpt-status's live digest | `ci/lambda-source-map.json`, `ci/build-and-upload.sh` | WORLD by the gate's floor (BUILD_ONLY builds only) |
| `AR-y-34` | Y4's remainder (row D2-S32) | Release 1's reads 3 and 4 re-run on revision 6; ONE measured read that the original-file route writes nothing (object versions before and after) | a result file; no product file | WORLD (live reads by the laptop's applier) |
| `AR-y-35` | Y5, row D2-S17 | The Analysis Request form's firm answer is a choice from the firms the caller's profile allows; no free text | portal `TicketCenter/AnalysisRequestParts.tsx` (the form half) + one test file | LOCAL (portal product file: candidate to the CTO before DEV) |
| `AR-y-36` | row D2-S31 | The `ycharts/generate` test suite stops depending on test order: the 34 custody tests pass inside the full run | `ycharts/generate/tests/` | WORLD by the gate's floor (test files only) |

Y4's last clause (each of the three widenings is exercised by its first real caller or stays stated UNEXERCISED) cuts no cell: no first
real caller exists this round. It stays stated UNEXERCISED in TO-APPLY-Y1's status and is re-read when a caller ships.

## Edges and chains

- `AR-y-31` and `AR-y-35` write the SAME portal file (`AnalysisRequestParts.tsx`): one chain, one worker's queue, `AR-y-31` first.
- `AR-y-32`, `AR-y-33`, `AR-y-34` and `AR-y-36` share no file with each other or with that chain, and none consumes another's output.
- So M = 5 chains. `AR-y-34` is not a worker cell (it needs the laptop's key access); the four worker chains take four slots.

fanout: 4 of 5 chains, cap 8, reason: the fifth chain (AR-y-34) is a live-read order to a Tier-2 applier, not a worker slot.

## Interfaces fixed at this cut

- **I8, the history row's client.** Member name `client_id` on each row of `analysis-request-history`; a string, or JSON null when the
  request's frozen selection names no client (an upload). The single read `analysis-request-read` does NOT gain it.
- **I9, the report's retained ref.** Member name `retained_ref` on `analysis-report`: the schema node of
  `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json`'s `retained_ref` (`report_id`, `revision`, `sha256`, `report_kind`,
  `immutable`), member for member, with ONE difference: `report_kind` is the const `ANALYSIS` (Performance's is `PERFORMANCE`).
- **The page halves** (the history filter by the header's client; Export on Analysis) are DSGN_IRPTV1's, a later round, after the release
  that carries `AR-y-32` is live. `2.0.0_SA_COO~D2` is told the two names at this cut.

## After the drain

One further irpt-status release (ONE tree, ONE never-widen pair, the reach read of the IB-pr-416 half re-run on the new zip) carries
`AR-y-32`. It is an apply order cut by this issuer after the drain; it is not a cell of this round's rectangle.

## Taxonomy record (rule 24) for the cell set

(i) Domain: the six items of the analysis's workstream-Y list. By subtraction: Y1 -> 31; Y2 -> 32; Y3 -> 33; Y4 -> 33 (source map) + 34
(reads 3 and 4, the write-nothing read) + no cell (the widenings, stated above); Y5 -> 35; D2-S31 -> 36. Uncovered: none.
(ii) Same grain: one build or one measured read per cell. (iii) One intent: enrich the served reads and close round 2's unmeasured items.
(iv) What this round does NOT move: the thread's liveness (workstream G), and the three widenings' exercise.
