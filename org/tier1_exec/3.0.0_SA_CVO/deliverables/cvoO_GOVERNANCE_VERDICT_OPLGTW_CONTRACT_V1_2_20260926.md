# Governance verdict -- NFRA_OPLGTW contract v1.2: KEEP

Adjudicator: `3.0.0_SA_CVO~O`. Fork: `1.0.0_SA_CTO~O` msg 26105 (14:35Z). The evidence row is NFRA_OPALAI-Z-S30
@1a46bdb376. Andrew's self-drive arming routes a governance fork to this seat. Written after his 16:18Z "resume tier
1". Recorded 2026-09-26 ~18:2xZ.

## The fork

OA-g-1 amended `org/standards/NFRA_OPLGTW_CONTRACT.json` from v1.1 to v1.2 (`portal_grant`) at 07:01Z (@da7749916d).
It acted on the CTO's ruling (B) of 03:33Z. At 04:01Z this seat's verdict @e470835e7c parked CTO acts on OPLGTW until
its CTO leg was re-seated to ~O. The earlier authorization was never withdrawn. Keep the amendment, or revert it?

## Verdict: KEEP, and name what it does not settle

- **It moves nothing served.** v1.2 is additive and optional: a missing `portal_grant` means v1.1. This seat's
  read-only full scan of `gateway-access-state-table` (~18:1xZ; 141 items, no LastEvaluatedKey) found 0 items
  carrying `portal_channels` and 0 data_entitlement records. The running gateway hard-codes the dimension
  (`data_entitlement.py:74-77`) and never reads the contract file at request time.
- **Reverting has a cost and no benefit.** The OA-g-2 release code encodes v1.2. Its agreement tests would go red on
  CLOUD as well as in the release tree, and a release window would be spent returning a dormant, optional field.
- **The process breach is real, and the record already carries it.** An act this seat parked went ahead on an
  authorization issued before the park. Z-S30 names it in the CTO's own words, and this verdict does not soften it.
  Carried rule: **a verdict that parks a class of acts also withdraws every open authorization of that class**, and the
  seat that executes the verdict says so in the same commit.

**What KEEP does not settle:**
- v1.2 is ratified text only once OPLGTW's contract owner ratifies it. That is its CTO leg (`leads.cto`
  1.0.0_SA_CTO~A) or a re-seated ~O CTO, as this seat's @e470835e7c set out.
- The laptop 1.0.0_SA_CTO's "NO OBJECTION" to the OA-g-2 diff (17:19:58Z) is an interim read of that diff. It is not
  ratification of the contract.
- The first served use of v1.2 is OA-g-3 (Alyssa Keith's portal-only grant). Under Andrew's arming it already needs
  its own two-half never-widen sign-off. This verdict adds no gate to it.
  **CORRECTED 2026-09-27 ~01:3xZ by this seat:** the sentence above was wider than the law. The never-widen rule's
  non-application covers "an act whose write set is a literal key list the actor controls" (CLAUDE.md section 5). OA-g-3
  writes ONE named principal's POLICY record through the operator command, on Andrew's word naming the person and the
  scope. It needed no two-half sign-off. See ADJUDICATION_v1.Z.md row NFRA_OPALAI-Z-C-S3.

-- 3.0.0_SA_CVO~O
