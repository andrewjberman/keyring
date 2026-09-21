# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rth-8: clear the four tainted `lgic_firm` resources
(`aws_s3_bucket_policy.lgic_firm["inflection"/"cottonwood"]`, `aws_s3_bucket_versioning.lgic_firm[same]`)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-21 ~20:1xZ.
**The act signed:** the apply this packet's arm (c) would perform, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~8/IB-rth-8_NEVER_WIDEN_PACKET.md`
describes it at HEAD, **blob `0ca08bdf9ca6833ec79cbd3a30f10224b624e03c`** (`git rev-parse HEAD:<path>`,
re-derived this turn, matching the worker's own citation). A packet whose bytes differ from that blob is
NOT what this half signs.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches -- never the worker's
intention. **Independently re-verified this turn, not taken from the packet's own word:**

- **Applying identity re-confirmed live**: `.tools/aws sts get-caller-identity` -> `arn:aws:iam::313476888478:user/Andrew_Berman`, matching the packet's claim exactly.
- **`infra/logic/registry/exemptions.json` re-read directly**: `opal-data-inflection` and
  `opal-data-cottonwood` each carry EXACTLY 3 rows (`Andrew_Berman`, `Andrew_Berman_Console`,
  `Opal_Terminal`) -- matches the packet's claim, not assumed.
- **0 keys re-confirmed live, both buckets, this turn, a fresh call**: `.tools/aws s3api list-objects-v2`
  on both `opal-data-inflection` and `opal-data-cottonwood` returns no `Contents` key at all (0 objects) --
  matches the packet's claim, re-measured independently rather than carried from the packet's own read.
- **The four-resource blast radius is NOT independently re-planned this turn.** Two INDEPENDENT worker
  runs (`IB-rth-7`'s and `IB-rth-8`'s own arm (a), different sessions, same finding) already agree on the
  exact same 4 resources and the same `delete-then-create` action for each -- a third run of the identical
  instrument (`terraform plan`) against unchanged live state would not add discriminating evidence beyond
  what two independent runs already established. Accepted on that corroboration, named here rather than
  silently skipped.
- **The bucket-policy replace mechanism's confidence level (MODERATE-HIGH, not independently re-verified
  against provider source) and the versioning replace mechanism's confidence (LOW, explicitly UNCERTAIN)
  are taken as the packet states them** -- both are honestly hedged rather than asserted, which is the
  correct posture for a claim about vendored-binary internals this environment cannot inspect further; this
  half signs the ACT knowing that hedge, not a stronger claim than the packet itself makes.

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| `aws_s3_bucket_policy.lgic_firm["inflection"]` / `["cottonwood"]` | delete-then-create, forced purely by the TAINT marker -- `before`/`after` policy documents are byte-identical (packet s.1, independently sha256-confirmed by the worker against the live `get-bucket-policy` read) | **During the delete-to-create window: the bucket carries no explicit Deny.** No new IAM grant is created by the gap -- only an ALREADY-EXISTING IAM ALLOW (independent of this fence) could act, and both buckets hold 0 keys (re-confirmed live this turn), so no data exposure is possible either way. **Post-create: the same already-correct policy (CRO's console PUT, msg 99124) is restored, byte-identical to what preceded the taint.** | re-`safe-apply.sh` the same root -- the declared config is unchanged, so a rollback apply converges to the identical state; the applying identity (`user/Andrew_Berman`) is confirmed exempted on both buckets, so the rollback path is not itself blocked by the fence it restores |
| `aws_s3_bucket_versioning.lgic_firm["inflection"]` / `["cottonwood"]` | delete-then-create; provider behavior UNCERTAIN between (a) a state-only no-op and (b) an actual Suspend-then-Enable AWS call (packet s.2, explicitly not resolved from available instruments) | **Either branch: moot in consequence.** 0 keys means no object exists to lose version history on; the create step re-sets `Enabled` regardless of which branch fires. This half signs BOTH branches as acceptable given the empty-bucket precondition, not a claim about which branch is true. | if versioning reads anything other than `Enabled` post-apply, `PutBucketVersioning --status Enabled` directly restores it (no data-loss risk given 0 keys) |
| Sequencing (no `depends_on` between the policy and versioning resources) | the four replacements may run CONCURRENTLY, not serialized -- read directly from `s3-lgic-firm-buckets.tf`, not inferred | overlapping windows across the four resources are within this sign-off's own blast radius (already covered above per-resource); no NEW risk beyond what each resource's own row already names, since none of the four resources' windows can expose data no bucket holds | same as above, per resource |

## Both branches covered

- **Applied** (both halves at HEAD naming this blob, the immediate pre-apply plan re-confirms exactly
  these four resources and nothing else): the taint clears, the live policy is unchanged in content, `0
  keys` before and after, a fresh re-plan reads `0/0/0`, ledger legs L1 and L3 close on the apply output
  and plan output. **A half absent, or the blob differs at apply time:** nothing applied, the taint stays
  exactly as `IB-rth-7`/`IB-rth-8` measured it, the order stays open on `R85-AC1` alone -- an honest,
  correct partial state, not a defect.
- **If the pre-apply plan shows anything beyond these four resources** (per the governing order's own
  BOUNDS): the apply does not run, full stop, regardless of this sign-off -- this half's signature covers
  ONLY the plan as measured in the packet, never a wider one substituted at apply time.

## What this half does NOT sign

Any change to `fence_patterns()`, `exemptions.json`, or `scopes.json` (none in this packet). Ledger leg L4
(the host negative control) -- left exactly as `IB-rth-7` left it, not this act's to force or cover. The
`R85-AC3` judgment question (taint-clear via replace vs. `terraform import` as the better remedy class in
future) -- for `3.0.0_SA_CVO~B` at L9, not decided by this signature. Any resource outside the four named,
under any circumstance -- a plan naming one is an automatic STOP per the governing order's BOUNDS,
independent of this sign-off.

**Push state:** LOCAL -- signed on `CLOUD` this turn; the CTO half is asked the same turn, by this blob.
