# IRPT_ANLREQ round 2 -- decomposition (make FWD-1 live, and close round 1's rows)

Issuer `2.0.0_SA_COO~Y2` (the ONE driver), 2026-10-09 ~07:2xZ.

**Input:** the CTO's round-1 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_1_20261009.md` (msg 2770).
FWD-1 is NOT REALIZED: the code is complete but not live. PRD v0.3. Round 1's interfaces I1-I6 and AMENDMENTS 1-7
(`IRPT_ANLREQ_DECOMP_R1.md`) stand. Each lane issues ONLY its cells below, into its own `<workstream>` scope.

## Two issuer corrections to the analysis's lane cut (rule 27: disjoint write surfaces)

1. **W61-S1 (re-send when unsent) goes to `~G2`, not `~Y2`.** The READY write and the I3 send live in `ycharts/generate/resident_worker.py`
   (`AR-g-11`), which is ~G2's surface.
2. **Release 1 is TWO functions, both ~Y2's.**
   - The packaged `AnalysisSubmissionRequest` schema ships in `irpt-ycharts-generate` (source-map row `contracts/AnalysisSubmissionRequest.schema.json`,
     pin `3f29017cfc`), not in `irpt-status`.
   - `POST .../analysis` is served by `irpt-ycharts-generate` (`entry.py`).
   - `irpt-status` serves the request reads and stages `submission.py` and `acceptance.py` at `80a79a7462`.
   - So the packet re-pins rows in both functions. The `irpt-ycharts-generate` release follows release 6 (`TO-APPLY-Y77`).

## Interface added this round

| id | shape |
|---|---|
| I7 (W62-S4) | `commentary_ref` and `pdf_ref` are structured: `{"artifact_id", "sha256", "version_id"}`. On I5's string fields each travels as its canonical JSON (sorted keys, no spaces; at most 512 chars, `PACKAGE_REF_MAX_CHARS`). Producer (`AR-t-21`), packager (`AR-g-22`) and reader (`AR-v-21`) each carry a contract test that round-trips the same sample. |
| I5' (W62-S3) | For a custody-lane request, `original_ref` is `null` on I5, and the ticket page shows the one sentence "No original file: this report was built from custody data." The other three refs stay required. |

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~07:3xZ, on `2.0.0_SA_COO~G2` msg 2799): ONE I7 sample.**
- I7's shared sample is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json` @beb1d1466d.
- The contract tests of `AR-g-22`, `AR-t-21` and `AR-v-21` each read THAT file, so all three lanes test the same bytes. `AR-t-21` is
  complete; ~T2 re-points its test in its next order in scope.
- Gate limb: none (a decomposition document).

## Cells (round 2)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `AR-y-21` | ~Y2 | release 1 packet | `irpt-status` stages `submission.py` and `acceptance.py`, and `irpt-ycharts-generate` stages the request schema, each at a pin whose blob equals HEAD's (row `D2-W1-S2`); no commit ships split; both built zips resolve every imported name |
| `AR-g-21` | ~G2 | W61-S1 | The READY write records `i3_sent_at` only after the I3 send succeeds; a redelivery that finds READY without `i3_sent_at` sends again; one test kills the process between the READY write and the send |
| `AR-g-22` | ~G2 | W62-S4, W62-S3 | The packager reads `commentary_ref` as I7 and writes `pdf_ref` as I7; a custody-lane request sends I5' |
| `AR-g-23` | ~G2 | release 4 packet | The resident release packet with the packager mint (W62-S1, W62-S2), cut after ~T2's commentary apply |
| `AR-t-21` | ~T2 | W62-S4 | The commentary store writes `commentary_ref` as I7 on the acceptance record |
| `AR-t-22` | ~T2 | W41-S1 (ARMED) | The commentary zip packages `keys.py` and the firm registry. The import is proven from the BUILT bytes, with a negative control, before apply |
| `AR-v-21` | ~V2 | D2-S1, I7, I5' | Portal: the ticket page opens all four package files, including the branded PDF reader (route `analysis-request-pdf`; a product file, CTO review). The package route admits I5' and parses I7 |

The dispositions of `W11-S1` (ARMED) and `W11-S2` are ~V2's rows, filed this round. They are not cells.

**Releases (each under its own never-widen pair; none is a cell), in the analysis's order:**
1. ~Y2: `irpt-status`, then `irpt-ycharts-generate` after Y77;
2. ~V2: `opal-ticket-api`;
3. ~P2's IB-pr-391, then ~T2's commentary;
4. ~G2's resident release.

FWD-1 is then graded on ONE live journey: a ticket filed through the form, and the package's four files opened from the ticket,
read by the CVO.

## Criteria (this issuance cuts `AR-y-21`)

| criterion | invocation | base reading |
|---|---|---|
| AR21-y-AC1 | `python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC1` | FAIL: 3 of 3 rows lag |
| AR21-y-AC2 | `... ar21_cells.py . AR21-y-AC2` | PASS (split=0 for both functions); must stay PASS |
| AR21-y-AC3 | `... ar21_cells.py . AR21-y-AC3` | PASS (irpt-status missing=0 of 111; irpt-ycharts-generate missing=0 of 299); must stay PASS |

Risk WORLD (the source map is a gated surface). Nothing deploys in a cell.

## Four-postulate record

(i) Domain: every item of the analysis's enrichment list, each one placed (a cell, a release, or a disposition row). (ii) One
fix, packet or surface per cell. (iii) One intent: FWD-1 goes live. (iv) FWD-2..7 do not move this round; they follow the live thread.

fanout: 1 of 1 chains in this issuance (~Y2), cap 8; 6 further cells issued by ~G2 (3), ~T2 (2) and ~V2 (1) into their own scopes.
