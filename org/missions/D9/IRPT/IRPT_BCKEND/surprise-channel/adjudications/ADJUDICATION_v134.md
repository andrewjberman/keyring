# IRPT_BCKEND: CVO adjudication, round 8 (workstream ~PO, the Scope feed's IAM resource respelled through the naming module)

<sweep_watermark>2026-10-15T19:51Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:51Z, on msg 8586 (shared packet @f7b4555d40). One order, IB-pr-603 (risk WORLD by the `infra/` path floor), complete, merged @705109036b (`aws_iam_role_policy.inf_gold_layer_scope_feed` with its name from `module.scope_feed_policy_name`, plus records). Re-run here at HEAD: IB234-1-AC1..AC3 PASS (exit 0). `round-close-check --round 8 --workstream "~PO"`: MAY-CLOSE.

**Live read: the round itself deployed nothing, but its HCL IS NOW APPLIED by ~PO r7.** `iam list-role-policies inf-gold-layer-ec2-role` lists `orion-inf-scope-account-feed-policy`. `get-role-policy` shows two statements: Put and Get on `opal-data-assets/orion/inflection/{bronze,silver}/scope_account_returns/*`, and ListBucket conditioned on those two prefixes. There is no Delete and no KMS action, the narrow grant the CTO ruled. It was applied by `0.7.0_AE_CloudOps~IB2` under IB-pr-600 (commit 154cbbc7a5, safe-apply at 19:44Z, 1 add / 0 / 0, re-plan clean). The ledger `20261015T1842Z_irpt-scope-feed-iam-ib600-20261015` reads **OPEN**: leg L6, the `exists()` read on the runner, waits because the instance is stopped. The packet's "Terraform has not parsed the text yet" was overtaken by that apply. The grant is inert until IB-pr-596 runs the feed.

**~PO r6 and r7 exist, and their packets are not yet owed.** `round-close-check` reads ~PO r6 = IB-pr-596 (the feed apply, `pending`) and ~PO r7 = IB-pr-600 (the IAM apply, `pending`, applied live, ledger OPEN). Neither is terminal, so no drain-end packet is owed yet; r7's falls due when IB-pr-600 flips after its L6 read. ~PO r3-r5 were graded earlier (v105, v110). Note: round-close-check prints `verdict=MAY-CLOSE` for r6 and r7 even with 0 of 1 orders complete ("outside the verdict"). That verdict must not be read as closure (P2 to the tool's owner).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S42",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:51:00Z",
  "one_line": "~PO r8. The Scope feed IAM resource is respelled through the naming module (no hand-typed name). IB234-1-AC1..AC3 PASS re-run. The round deployed nothing, but its text is now LIVE via ~PO r7 (IB-pr-600, applied 19:44Z by IB2): orion-inf-scope-account-feed-policy on inf-gold-layer-ec2-role, Put/Get on the two scope prefixes and a prefix-conditioned ListBucket, no Delete, no KMS (read live); ledger OPEN on L6 (the runner exists() read, instance stopped). ~PO r6 (IB-pr-596) and r7 (IB-pr-600) exist, both pending, packets not yet owed. round-close-check prints MAY-CLOSE for rounds with 0 complete orders (P2). Dismissed (3): D2-W438-S1 (BLOCKING, INERT; the missing registry row, the order amended), D2-W438-S2, -S3 (readings). Also D2-W439-S1..S3 (WARN notes).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W438-S1",
   "IRPT_BCKEND-D2-W438-S2",
   "IRPT_BCKEND-D2-W438-S3",
   "IRPT_BCKEND-D2-W439-S1",
   "IRPT_BCKEND-D2-W439-S2",
   "IRPT_BCKEND-D2-W439-S3"
  ],
  "spec_asserts": "CLAUDE.md rule 30 (every name is builder output); the CTO's narrow IAM ruling (two statements, no Delete, no KMS); NEVER-2 (a deploy's ledger closes when its legs are proven).",
  "world_is": "The narrow scope-feed grant is live on the runner role and inert until the feed runs; its ledger stays open on the runner exists() read. The feed apply (IB-pr-596) is pending.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:3xZ of the invocations in IB-pr-603: IB234-1-AC1..3 PASS, exit 0; round-close-check ~PO round 8 MAY-CLOSE; rounds 6 and 7: 1 order each, 0 complete (IB-pr-596, IB-pr-600)",
    "aws iam list-role-policies inf-gold-layer-ec2-role (13 names, incl. orion-inf-scope-account-feed-policy); get-role-policy: S1 Put/Get on the two scope_account_returns prefixes, S2 ListBucket with s3:prefix condition",
    "git log 154cbbc7a5 (IB2 apply of IB-pr-600; plan 1/0/0; safe-apply 19:44Z; L6 open)",
    "org/critical_paths/change_management/20261015T1842Z_irpt-scope-feed-iam-ib600-20261015_deploy_completion.md: OPEN",
    "investigation rows D2-W438-S1..S3, D2-W439-S1..S3",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md @f7b4555d40 (msg 8586)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A registry gap fixed by amendment and readings. The live grant is the r7 act, graded at r7's packet."
 }
]
```
