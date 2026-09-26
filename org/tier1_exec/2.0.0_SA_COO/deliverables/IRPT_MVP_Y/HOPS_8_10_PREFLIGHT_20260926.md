# Hops 8-10 pre-flighted offline -- two status defects and one export scope gap found before any window

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~19:4xZ. **Order:** Andrew at the ~Y terminal, "do 1 3 and 4 in order": this is
option 3. CTO frame 101442.

## Result

| # | Hop | Finding | Measured by | Fix |
|---|---|---|---|---|
| A | 8-9 | **`irpt-status` does not package `interactive_access.py`.** `served.py` imports it lazily for every verified internal (Opal) subject (`current_principal` :796, `_handle_owner_read` :813, `_handle_prospect` :843). All four Opal owner-reads (sections, job status, history, request read) answer **UNEXPECTED** (`ModuleNotFoundError: interactive_access`, 4 of 4). | `status_read_proof.py` on the served zip `pfAr3uZE`: 0/4 as deployed; **4/4 with the one file added** (27/27 modules from the extract) | a `staged_from` row for `irpt-status` in `lambda-source-map.json`, identical to generate's (`_scope/interactive_access.py`, pin `9a3ec2a11f47`, sha256 `bba07a3f4eeb...`). Its imports (ids, loaders, prospect, resolve, served) are all already in the zip. |
| B | 8-9 | **`irpt-status-role` lacks `s3:GetObjectVersion`.** The readers fetch retained objects BY VERSION (the measured reads: versioned GetObject on `platinum/analysis_reports` and `state/request_compositions`); `ops/iam.tf:73-75` grants `s3:GetObject` only. The first sections or request read of a real report gets AccessDenied. Not seen live yet, because no report has ever been READY. | `iam_hop8_pairs.py simulate`: GetObjectVersion **implicitDeny** on both families; 8/10 met | `P_STATUS_READ_GRANT_20260926.patch`: actions become `["s3:GetObject", "s3:GetObjectVersion"]` over the same four families. apply-check rc=0 on P's tree, terraform fmt clean. |
| C | 10 | **Exporting an ANALYSIS report is not built.** `submit_installed.py:65` raises "only a Performance report exports"; `retained_export.py:69` refuses a non-PERFORMANCE ref. `irpt-export-render-role` has no read on `analysis_reports` or `vendor_documents` (it reads `performance_reports`). An Analysis export is refused BY NAME, not a crash. | a read of the served export zip `ryEMGlRu` and its live role; the export read pairs are 1/7 met (assumed pairs, not measured: a design gap, not a grant bug) | a scope decision (CTO): the "whole chain" window cannot pass hop 10 for Analysis as built |

## How it was measured

- `live_walk/status_read_proof.py`: the served `irpt-status` zip is extracted fresh and FIRST on sys.path (`--overlay` is
  the fix). The real `status_installed.compose_ports` + `build_boundary` + served Entry handle four GETs with Opal
  headers on the READY job `resident_job_preflight.py` produced (the phase-2 world: REPORT# row, ANALYSIS object, job
  READY).
  - Every read is logged. The 4 reads make 32 calls in 5 shapes:
    - GetItem on irpt-jobs;
    - GetItem and Query on irpt-requests;
    - versioned GetObject on analysis_reports and request_compositions.
  - Answers with the fix: `sections` data (extraction_coverage, request_ref, sections, undated_sections: the synthetic
    PDF carries no "as of" date, so its rows are truthfully undated), job status, history `items`, request `identity`.
- `iam_hop8_pairs.py`: those measured reads as pairs, simulated against the live `irpt-status-role` (plus the kms
  decrypt), with 2 negative controls denied.
  - Export's read side is simulated against `irpt-export-render-role` as a design check, not a measurement.
  - Output: `IAM_HOP8_SIMULATION_20260926.txt`.

## Limits

- Hop 10's write side (bundle, receipt, render host) was not exercised: export refuses Analysis before it.
- The status proof reads live AWS under the harness identity, and the role check is simulation. Both fixes are
  re-provable after apply: the status proof with no overlay on the new zip, and the simulation at 10/10.

## Served re-check (20:0xZ, asked by 2.0.0_SA_COO~P in 101481)

P served both fixes at 19:56:53Z (ledger `irpt-status-reads-20260926`); P reports the simulation at 10/10.

| Run | Zip | Overlay | Result |
|---|---|---|---|
| served | `irpt-status` CodeSha256 `bMMJ/bQ+5RKo...` (downloaded; b64 sha256 of the bytes matches) | none | **4 of 4 answered**; 27/27 first-party modules from the extract; 32 reads, 5 shapes, same as the overlay run |
| negative control | prior `pfAr3uZE` | none | 0 of 4 (`No module named 'interactive_access'`) |

The state is the same phase-2 READY world (`resident_job_preflight.py --out`).
