# QUARANTINE RELEASE -- NFRA_C3MATERIALIZE TO-B4-COX, the two bare `c3materialize-b4/out/` keys

- Seat: `2.0.0_SA_COO~X`, the issuer of the disposition. Written 2026-10-03 ~18:1xZ.
- Order: Andrew-direct 2026-10-03 ~17:3xZ, verbatim "Release any quarantine that may have been initiated in any capacity".
  Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261003_17xxZ_RELEASE_ALL_QUARANTINE_NO_DATA_OPS_CHANGES_WITHOUT_DIRECTIVE.md`
  (@4d393e3521). Relay: `0.0.0_AB_MSTR~Z` msg 28910.

## What this lane held

Census: 950 commits by `2.0.0_SA_COO~X`. One of them names a quarantine (552a8de672, 2026-08-28). The AMGT_CORPUS project
tree has 0 quarantine hits.

That commit added the **B4-AC4 LEGACY-KEY DISPOSITION** at line 89 of
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_C3MATERIALIZE.TO-B4-COX.sbm-producer-in-aws-container.md`. It marks the bare
keys `c3materialize-b4/out/SBM_RUN_RECORDS.json` and `W_STRUCTURE_FACTORIZED.json` "FROZEN / QUARANTINED": no write, no delete,
no overwrite-with-pointer.

## Released

That FROZEN / QUARANTINED label is released. No S3 object was written or deleted by this act. The same paragraph's
evidentiary-credit clause (credit only to run-addressed objects) is a citation rule, not a quarantine, and it stands.

The release is recorded here, not on the order. The order was flipped complete on 2026-08-28. `.tools/to-pipeline-gate.py`
refuses any edit to it that lacks a proof-of-spec instance (line 3028), and the `# pipeline-override:` line does not lift that
limb.
