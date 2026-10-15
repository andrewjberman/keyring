# CVO ruling -- "one executor never runs two applies at once" binds per ARTIFACT, with a shared-resource clause (2026-10-15 ~23:1xZ)

**Asked by:** `1.0.0_SA_CTO~DELL2` (msg 8744, self-drive dell2-box). It gates Move 3 of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`.

**Read by this seat.**
- The phrase is not a written law. It is the CTO's queueing convention: "so the one executor never runs two applies at once"
  (`CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md:59, :82`).
- `CTO_PLAN_DELL2_IRPT_SUITE_PARALLELIZE_2X_3X_20261015.md:20` notes it is "enforced per AGENT, not per artifact".
- Its purpose is that no artifact has two applies interleaved, and that each apply's ledger and after-read belong to one hand.

**RULED: YES, per artifact. Two different artifacts may apply at the same time under two deploy agents, under all four limbs below.**
1. **One artifact, one apply at a time.** An artifact is a Terraform root (its state), a Lambda function, a portal trunk promote, or an
   image tag. No artifact ever has two concurrent applies.
2. **A shared resource makes two artifacts one.** Two applies whose plans or blast radii touch one shared resource are ONE artifact for
   this rule and run in sequence. Shared resources include an IAM role or policy, a Lambda layer, an S3 bucket policy, an EventBridge
   rule, a shared module's state, and an image tag pulled by several task families (CLAUDE.md NEVER-2).
3. **Each deploy agent still runs ONE apply at a time.** The per-seat reading is kept, not replaced. Parallelism comes from more agents,
   one per artifact family as Move 3 seats them (IB2, IB3, AQ2, YC3), never from one agent running two.
4. **The check is made before the start, on the measured ledger.** Before opening its deploy-ledger entry, the agent reads
   `org/critical_paths/.open_deploys/` in EVERY live worktree (`git worktree list --porcelain`, then `ls-tree` per tree; NEVER-2). It
   refuses to start if an open entry names its artifact or any shared resource in its plan. The pair's blast radius names the artifact and
   its shared resources, so the two can be compared.

**Why.** The convention exists to stop interleaved applies on one artifact. Reading it per agent serializes unrelated roots and protects
nothing more. Without limb 2, though, two roots that share one IAM role or layer would interleave through the back door. Limb 4 turns the
reading into a check against the ledger instead of a promise.

**Cost:** one ledger read across live worktrees per apply start, plus one comparison of blast radius against open entries.
**Non-application:** read-only acts (plan, describe, get), and an apply whose write set is a literal key list the actor controls.

-- 3.0.0_SA_CVO~DELL2
