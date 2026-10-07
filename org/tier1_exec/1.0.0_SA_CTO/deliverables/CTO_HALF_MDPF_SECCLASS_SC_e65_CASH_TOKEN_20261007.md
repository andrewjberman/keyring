# CTO never-widen half -- MDPF_SECCLASS SC-e-65 (C-CASH-TOKEN, PRD v0.16) to the two firm `_shared` copies of `etf_classification_scheduled.py`

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~15:2xZ, the first half of release mode (round-11 analysis @fc96f7c48c).
**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_TOKEN_20261007.md` @00e7bf2cb5
(COO half SIGNED). Candidate `16092a4806`, line head `858c1d3b5d`.

## VERDICT: SIGNED, with the act CORRECTED: the merge PLUS an explicit `.tools/safe-deploy.sh` of the one file. The push gate will not upload it.

## Read by this seat

- **The request's mechanism will not fire.** `.tools/safe_deploy_core.py:1042` describes the `_shared` members as "Declared SHIPPED
  ARTIFACTS that ride along with a deploy of rel_paths", so they ship only alongside a gold-script deploy. This was measured on
  2026-10-07 for SC-e-21 (relay msg 137): the push printed "no deploy-scope script files detected, nothing to do", and the keys stayed
  at the pre-state until the explicit deploy. A merge of this line, which changes no gold script, uploads nothing. Trunk and S3 then
  disagree, and the next BD/COT gold push carries the module at a time nobody chose.
- Otherwise the half reads true. One shipped file (`etf_classification_scheduled.py`). Both keys are at the base md5 `cfe898d1`, with
  rollback VersionIds read at 15:18Z. Put-on-absence only: the rule runs after the existing-row and seed-source skips, so no served
  class moves. Branch A writes new `cash`/`Cash` rows for held cash-token keys, with `input=cash_token`; branch B changes nothing. It
  carries v0.16 (8 phrases, whole-name match, contract 0.8.0 data, pin test). AC1 reads BDCASHIN and FCASH cash, CASHMERE None.

## Conditions

1. **The act:** `0.0.0_AB_MSTR` merges the line, and a laptop seat in safe-deploy's lane (as `0.7.0_AE_CloudOps~S` did for SC-e-21)
   runs `.tools/safe-deploy.sh` for `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` to `opal-data-bd` and
   `opal-data-cot` `code/gold/lib/_shared/`, in the same window. A change-management ledger entry names both keys and their VersionIds.
2. Read back both keys at ETag `3f1e6be8910952f33c88bf100c610ab6`. Until that read, no BD or COT gold-script push (the same hold as
   SC-e-21).
3. The first BD E_18 run after the upload (23:00Z) is read for its `cash_token` plan lines. Each row written names its key; any row
   whose class is not `cash`/`Cash`, or whose key is not a cash token, triggers rollback (the key and the row).
4. The test also pins "Cash Flow Dividend Fund" and "Cash Cow" OUT (PRD v0.16). If the pin test lacks them, add them before the merge.
