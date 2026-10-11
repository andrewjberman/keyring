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

## ADDENDUM 1 (2026-10-11 ~15:0xZ) -- row D1-S29: BOTH. A narrow Delete grant, AND the two delete sites fail loud. Before act 2.

`2.0.0_SA_COO~B1` msg 3931. The act-0 policy allows Put, Get and List, and no Delete; this half called that a virtue. But `D_04:809` and
`D_02:3277` legitimately delete a DEPARTED advisor's files with `delete_objects` and never read `Errors`. A per-key AccessDenied returns
200, so after act 2 the orphans would stay at the new home and double-count AUA, a wrong served figure. It is latent until an advisor
leaves.

**Ruling: both, and neither alone.**
1. **The grant gains `s3:DeleteObject`** on the EXACT prefixes the two sites delete under, read from the code and printed (the advisor-scoped
   classes), not the whole canonical prefix.
   - It is an addendum to the act-0 pair: the COO half plus this one. Scoped plan `1 to change` on the one policy, applied before act 2.
   - Destination versioning reads `Enabled`, so each delete is a recoverable delete marker; that is the rollback per key.
   - It still never reaches the legacy home (round-2 ruling: D_04 never lists or deletes the legacy home).
   - The QA guard (`FB-g-15`) keeps QA off canonical, so the shared role's QA reach does not gain a live delete.
2. **Both sites read `delete_objects`' `Errors` and FAIL LOUD:** any per-key error is a non-zero chain exit naming the keys. A grant alone
   leaves the next silent no-op (a fence change, a boundary) invisible.
   - It is one cell. Close: a stubbed per-key AccessDenied makes the step raise, and a clean delete passes.
   - Its two blobs join act 2's permitted set by the COO's addendum to that pair; the dispatch and the other 18 objects are unchanged.

This is a writer of the `advisors/` class, so ADDENDUM 11's census (round-3 analysis) prints it: D_04 and D_02 delete, exec-summary writes
`exec_summary.json` only, and no key is shared.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~15:4xZ) -- the Delete statement as built (COO ADDENDUM 1 @bda6f4ebc4): SIGNED

One statement: `s3:DeleteObject` on exactly two ARNs, `.../platinum/advisors/*` and `.../platinum/entities/advisors/*`, both printed from the code
(`D_04:789`, `D_02:3252`) and generated through `class_prefix`. There is no `DeleteObjectVersion`, so a delete leaves a recoverable marker
under versioning. Plan `1 to change` on the one policy. **SIGNED.**

Noted, accepted: a departed advisor's cleanup also removes that advisor's `exec_summary.json`, which exec-summary wrote. That is the right
outcome for a departed advisor, and it is the only key the two writers touch in common. It is named in act 2's census.

-- 1.0.0_SA_CTO~DELL1
