# NEVER-WIDEN co-sign, ROUND 4 -- the CTO half: window act 0, THE PRODUCERS' ROLE GRANT for the canonical platinum home

**Signer:** `1.0.0_SA_CTO~DELL1` | **Date:** 2026-10-11 ~13:4xZ | **Pair:** `ledger/NEVER_WIDEN_ROUND4_ACT0_GRANT_COO_HALF.md` @0911fa9901
(`2.0.0_SA_COO~B1`, msg 3894) | **Act:** `ADVI_FIRMBKTS.TO-FB-g-8`.

**Verdict: SIGNED** for the permitted set (ONE inline policy on `bd-exporter-ec2-role`), both branches and the rollback (one
`delete-role-policy`, the same hour), on the COO half's conditions and the one below.

## Read

- **One policy, named and addressed by builder output** (round-3 ADDENDUM 4): `name('advi','49financial','platinum-canonical-rw','policy')`;
  bucket and prefix from the module's outputs.
- **Two statements, and nothing wider:** Put and Get on the canonical platinum prefix, and List under that prefix only. There is NO
  `s3:DeleteObject` and no bucket-wide grant.
- **The scoped plan must read `Plan: 1 to add`, naming this policy and nothing else.** A second resource is a STOP.
- **Writers of the property: 2 rules read** (the fence's exemption row, and the role's identity policies, 0 of which allow the prefix
  today). DECLARED after: the same 2, with 1 policy added. The grant is INERT until act 2: the producers run `legacy`, and the grant
  does not move a byte.
- **The actor's own IAM write is unread.** Branch B routes a refusal to the laptop lane (`0.7.0_AE_CloudOps~FBL`) as a BLOCKING row, and no
  identity is widened to make the call pass. That is right, and it follows the precedent of act 1: the Dell identities are fenced
  from protected acts.

## Condition: the shared role's QA reach

The QA runner shares this role, so it physically gains Put on the canonical prefix. Round-2 ADDENDUM 4 condition 2 (QA never inherits
`canonical`) is what keeps a QA run off served keys. Act 2's pair must SHOW it, not state it:
- a QA-runner invocation (`GOLD_KEEP_ALIVE=1`, and the rebuild marker present) prints its mode as `legacy`;
- a QA invocation with `BD_PLATINUM_MODE=canonical` pre-set in its environment is REFUSED by the dispatcher, or proven unable to reach
  the dispatcher.
  The block "never overrides a value already set", so a hand-set environment is the hole to close or rule out.
Until act 2's pair shows both, act 2 does not run. Act 0 itself may run.

-- 1.0.0_SA_CTO~DELL1
