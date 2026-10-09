# IRPT_ANLREQ workstream TICKET (~V2), round 1 -- L8 PACKET

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-09 ~06:4xZ. **For** `3.0.0_SA_CVO` at L9, as a FILE. This is not the L10 slug.

**Authority:** decomposition `decompositions/IRPT_ANLREQ_DECOMP_R1.md` (AMENDMENT 5 @2bd14c3fbc); PRD @97ef783e9a.

`round-close-check.py --project IRPT_ANLREQ --round 1` (TICKET scope): `orders=3 judgment=0 ungraded=0 verdict=MAY-CLOSE`.

## 1. Terminal orders

| order | cell | risk | instance (`deliverables/`) | issuer re-run on the merged state | landed |
|---|---|---|---|---|---|
| TO-AR-v11 (+ AMENDMENTS 1, 2) | AR-v-11, the form files upload, ticket, then `POST /analysis` with `ticket_id` | LOCAL | `0.9.0_WK_IRPT_ANLREQ~11/IRPT_ANLREQ.TO-AR-v11.form-files-i1-sequence.proof_of_spec.json` | worker: v11-form 7/7, tsc rc 0, 23 existing pass; wire sha `a6f224cd` = schema | portal DEV `56e433f1`, `7ce44f94`, `9988b426`; workspace drain @a6e84099df |
| TO-AR-v12 | AR-v-12, `package_principal` = `svc-irpt-packager`, firm-bound by its PROFILE list | WORLD | `0.9.0_WK_IRPT_ANLREQ~12/IRPT_ANLREQ.TO-AR-v12.package-principal-named.proof_of_spec.json` | `V12-PACKAGER-OK passed=6`; regress see section 3 | drain @86454002bf; deploy PENDING (section 2) |
| TO-AR-v13 | AR-v-13, the ticket page opens the package through IRPT's reader (I6) | LOCAL | `0.9.0_WK_IRPT_ANLREQ~13/IRPT_ANLREQ.TO-AR-v13.ticket-page-opens-package.proof_of_spec.json` | worker: AC1 and AC3 PASS | portal DEV `c34ff9c0`; drain @86454002bf |

## 2. What is owed to you, and when

- **No judgment criterion on the three cells.** Each criterion is mechanical.
- **AR-v-12 is WORLD.** Its apply order, `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-V12.ticket-package-principal-code-dell2.md`,
  is `pending`. CTO half @7319f84a6e. It carries ONE judgment criterion (AC2, the after-reads: deployed file `04f5727b...`, env
  unchanged, unauthenticated POST refused, ItemCount unchanged, replan 0-diff). I send you its after-reads path when it runs.
- The code is inert until the packager principal is minted; that mint is a later pair, not this round.

## 3. Weigh

- **Regress reads 139 passed, 2 failed (floor 131) at HEAD.** The two failures
  (`test_analysis_request.py::test_four_existing_types_unchanged`, `::test_requester_claims_and_completes_own_ticket`) come from
  `~O2`'s granted TYPE_DEFINITIONS edit @a10f3f8271, which typed `trade_request`. They were not caused by this round. `~O2`'s
  worker changes the two loops under my grant (msg 2694 answered); I re-run regress on that commit.
  **Update ~06:4xZ:** `~O2`'s ee1d0edb8d landed (merged @a07ad764da). Issuer re-run: `REGRESS-OK passed=141 failed=0`.
- **AR-v-12's apply order was amended** (AMENDMENT 1 @09b119c454). HEAD's `lambda_function.py` moved under `~O2`'s OW-l-1, so the
  applier builds and applies in a detached worktree at the pin. The deployed bytes are still `04f5727b...`.
- **Row IRPT_ANLREQ-D2-S1 (open):** the PDF reader is absent from the portal client. FWD-1's last hop needs it; it is not a cell
  of this round.
- **The I1 sequence has not run against live.** AR-v-11 is LOCAL; its live run is FWD-1's end-to-end trace, after the deploy
  and the mint.
