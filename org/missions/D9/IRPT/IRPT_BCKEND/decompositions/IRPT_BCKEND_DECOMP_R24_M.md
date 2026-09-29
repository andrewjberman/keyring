# IRPT_BCKEND decomposition -- ROUND 24, WORKSTREAM ~M (2026-09-29, 2.0.0_SA_COO~M, on row IRPT_BCKEND-S217)

Cut on row `IRPT_BCKEND-S217` (@43aa2951dc, the issuer's). The CTO asked for ~M's AD-10 step-3 census of the
restamped directory-bundle bytes (102945, after transcripts step 1 @73896b6c42). That census found the bundle's fixed
member list in `.tools/safe_deploy_core.py` lacks `schwab_account_codes.py` and `.json`, while `directory_runner.py`
imports `schwab_account_codes` at module level (:121, from IB-mr-213). A mint as defined would fail every directory
fire. Interim control: 0.0.0_AB_MSTR keeps skipping investor-reporting.tar.gz (asked 18:00Z). Rounds 20-23 ~M are
issued, so this rides round 24 (GATE (x)). It is a remediation of ~M's own miss.

| cell | item | ruling carried | outcome served | risk | depends on |
|---|---|---|---|---|---|
| `IB-mr-241` | The directory bundle ships what its runner imports: add `schwab_account_codes.py` and `schwab_account_codes.json` to the `investor_reporting` bundle's members in `.tools/safe_deploy_core.py` (each with its own sha metadata key), and prove a LOCALLY built bundle imports -- no upload, no mint | the AD-10 halves already sign step 3 (CTO 102945); this cell only makes the bundle the halves signed shippable | FWD-2 (the directory) -- unblocks AD-10 step 3 | LOCAL | none |

Chains: A = 241, worker slot `0.9.0_WK_IRPT_BCKEND~82` (S197: 1 + max(authors 81, issued_to 81, branches 61) = 82).
Direct act: one cell, LOCAL, about 10 lines.
