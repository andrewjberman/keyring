# NFRA_DEVPLN round 1 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-13 ~20:40Z)

Issuance `5570ac9eee` (PRD v0.2 @d2b7385bee). Decomposition `org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md`. Push state (ls-remote and merge-base reads at ~20:40Z): every round commit (5570ac9eee through ab5128bd63, and the amendments d0564a0d90, 0b70cbd93a) is on origin/box/laptop @f32bf864f2 and on origin/CLOUD; the slug itself and the stage flip below are LOCAL until the next box-sync.
`python .tools/round-close-check.py --project NFRA_DEVPLN --round 1` reads `reviewer=present (3.0.0_SA_CVO~L) orders=6 judgment=0 verdict=MAY-CLOSE`.

## 1. What the round built (6 orders, 6 complete, 6 proof instances VALID; each self-test re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-b-1 | `approval` kind in `.tools/open-calls.py` (add, close `--decision`, `approval-status`), Rule 24 record; 13/13 | `9f45a5616e` |
| DP-b-5 | registration facts (`head_sha`, `commits`, `dev-overlap` refusal), `--check-only`, `approval-lease`; 10/10 | `ab5128bd63` |
| DP-b-2 | `.tools/portal-merge-forward.sh`; 18/18 | `9008e2fa78` |
| DP-b-3 | `.tools/portal-release-build.sh` and the `/prod-deploy` chosen-set step; 10/10 | `eb3b801650` |
| DP-b-4 | `portal/CONTRIBUTING-BOXES.md` (branch `origin/cand/laptop/contributing-boxes`, 1 commit on PROD) and the worker definition's portal step | `528f269785` |
| DP-s-1 | `.tools/portal-settlement-list.py` and `ledger/SETTLEMENT_LIST.md` | `e4efa6c434` |

## 2. The real run so far (issuer act A4, the seam)

The real `approval-status` feeds the real merge-forward and release-builder on the real portal repo, with a scratch store (`OPAL_STATE_ROOT`) and no push: merge = 2 parents with `Feature:` and `Approved-By:` trailers; release `unapproved=0` READY. The first real row is `laptop-20261013T200117Z-9e8a` (opal-internal, OPEN, at the box CTO lane). Not yet run for real: the row's close, the DEV push, the chosen-set promote and the client page (hop 7).

## 3. Settlement (FWD-6) -- moved under the round

At 19:24Z a DT promoted DEV whole into PROD (`63c4f9e3`, "Andrew-direct promote"); the integrator fast-forwarded DEV to it (msg 108868): DEV = PROD = `63c4f9e3`, 0 commits apart. Call 1e0b closed superseded by you. OWED: the disposition of the 9 branches. Measured: all 9 are PROD-cut (0 DEV-only overlap); 5 hold nothing not already on DEV (`cand-dell1-secclass-e53-r9`, `cand-dell1-secclass-e59-r10`, `q/dell2/wk-IRPT_BCKEND-167-portal/r1`, `irpt-dev-candidate-7-20260924`, `sitez/merge-trial-20260915`); 4 hold a unique patch (`wk-dsgn-irptv1-r25-61-prodcut`, `irpt-dev-candidate-3-20260924`, `irpt-opal-scope-p-portal-20260923`, `wk-IRPT_ANLREQ-51-portal-r4`). `ledger/SETTLEMENT_LIST.md` headline counts are stale after the promote.

## 4. Channel watermark and ARMED rows

Channel `surprise-channel/investigations/INVESTIGATION_v1.md`: 23 rows, 0 adjudication rows, so no CVO watermark yet (the CVO's L8 read is still to come). ARMED: 4.
- `W1-S1` (disarm owner YOU): the approval close skips the CLOSED-BOTH gate because NFRA_DEVPLN reads CROSS-BOX. Your ruling is owed.
- `W1-S4` (mine): an older tool refuses a list holding an approval row. Disarmed by measurement: `origin/box/dell1`, `box/dell2`, `box/sitez`, `box/laptop` and `origin/CLOUD` each carry `approval-status` (8 references each, read with `MSYS_NO_PATHCONV=1 git show` and a positive control).
- `W1-S6` and `W1-S10` (mine): `--portal` becoming required, and case 1's interim null assertion, broke `DP-b-1`'s test. Amended in `d0564a0d90` and `0b70cbd93a`; `test_open_calls_approval.py` re-run on the merged tree 13/13.
- BLOCKING rows `W1-S5` and `W1-S9` were my premise errors (the AC2 branch); amended, closed by the amendment.
- My row `S1`: C-PROMOTE read first-parent plus per-feature binding; C-MERGE-FORWARD (iii) read as a lease-written row. Your reading is owed.

## 5. Per outcome (advance, not a grade)

FWD-1 thread built, one real trace owed. FWD-2 row and list exist, approve/decline answer owed. FWD-3 script exists, gate edit (S03) owed. FWD-4 trailers exist in the script, the read is not built. FWD-5 builder exists, not run for real. FWD-6 trunks agree; branch dispositions owed. FWD-7 class rule lives in `approval-status`; the gate's copy is owed.

## 6. ENRICHMENT candidates for round 2 (thread-breaking first)

1. Run hops 3-7 for real on row 9e8a: close, DEV push (integrator or S03), chosen-set promote by the DT.
2. S03 gate edit (yours); then the refusal arm on every box (FWD-3).
3. A dell2 Investor Reporting feature through the route (the brief's named first case); none of the 9 branches qualifies.
4. The nine-branch dispositions; re-run the settlement list.
5. FWD-4's per-commit read; FWD-7's line in the gate and `CONTRIBUTING-BOXES.md`; FWD-2's declined arm; FWD-5's negative-arm promote.
6. ONE batch cell for repairs: `test_open_calls.py` red at base (W1-S8); the merge-forward never fetches (W2-S2); merge-forward prints no merge sha without `--push`; `approval-lease` default `--project` (W1-S7); the `/prod-deploy` Step 8 receipt wording (W3-S3).
