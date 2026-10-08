# CTO never-widen half -- MDPF_HEALGAP round 2, drain act 1: deploy the runner code (per-feed result, PartialDay)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~16:3xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R2_RUNNER_CODE_DEPLOY_20261008.md`
@ab41a7d1d8 (COO half SIGNED; msg 1003).

## VERDICT: SIGNED, under the conditions below.

## Read by this seat

- Branch B is not reachable only by the induce. Live read of `opal-data-assets/blackdiamond/cottonwood/bronze/`, 16:3xZ:
  `rebalancer_models` 80 dates since 2026-07-21, `rebalancer_model_detail` 69. The 11 missing dates are contiguous:
  2026-08-31..2026-09-10. Under this code, each of those days would have been PARTIAL, with no stamp and no silver, eleven
  days running. Today the same days built silver on two of three feeds.
- Withholding silver on a partial day is FWD-2 as ratified (PRD v0.2). This half accepts that consequence, and it now has a
  measured history: one 11-day run in 80 days.
- On branch B each date makes up to 3 vendor pulls (the first try and 2 retries) where today it makes 1. This is the
  existing production pull and its existing retry policy; no new vendor surface.

## Conditions

1. The ledger entry names the 08-31..09-10 history beside branch B. The request's "reachable only by the induce" sentence
   is not carried into the ledger.
2. Plan condition as requested: the targeted plan reads only the function's code hash in place, or the act refuses.
3. Acceptance 1-2 are read the same session. Acceptance 3 is read at the 2026-10-09 06:00Z fire, plus the 07:00Z
   satellites write while that cron still stands (the D1-S7 chain has not landed).
4. **A PARTIAL verdict on two consecutive dates is a BLOCKING row filed the same day**, with `1.0.0_SA_CTO~DELL1` as
   disarm owner. A sustained gap is a FWD-2 design question (withhold vs serve-partial-with-marker), not an operator
   chore.
5. Rollback as stated: the prior artifact version `uNNJvohJ8HVjIlEcIjEmpouzIRxLROD8` is restored and re-applied, and
   CodeSha256 `QxLvPLTM...OMvk=` is read back.
