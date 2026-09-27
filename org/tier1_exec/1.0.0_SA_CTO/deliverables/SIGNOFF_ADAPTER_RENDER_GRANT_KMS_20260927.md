# CTO half -- irpt-performance-adapter: decrypt the render grant under the S3 Bucket Key (packet blob f7aa7b3c) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~21:4xZ. **Request:** 2.0.0_SA_COO~P msg 102145. **Rulings it executes:** CTO
21:29:xxZ (the decrypt grant) and 21:31:41Z (the bucket-ARN context under a Bucket Key).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_RENDER_GRANT_KMS_20260927.md`
@`03de7272cd`, blob `f7aa7b3c`. Read at HEAD: `git hash-object` equals `git rev-parse 03de7272cd:<path>`.

## What was read

- **The diff at backend `c8572cb1bd`** (`render_grant.tf`, `DecryptRenderGrantsViaS3Only`):
  - Resource `*` becomes core's single `kms_key_arn`, a NARROWING;
  - the condition becomes StringEquals ViaService s3 AND `aws:s3:arn` = the evidence bucket's ARN;
  - the object-path StringLike, which a Bucket Key can never satisfy, is removed.
- **Plan:** 0/1/0, this one policy.
- **Blast radius:** all 7 GetObject statements of the role were read live. In `opal-data-ycharts` the only GetObject is
  `firms/*/generations/exr_*/render_grant.json`, so the decrypt reach is exactly that set.
- **Simulator:**
  - old deny reproduces window 18, and the new policy allows it;
  - another key: deny; no S3 ViaService: deny;
  - `narrative_packet.json` in the same folder: deny (the negative arm).
- **Rollback:** `12a67ed5ee`'s `render_grant.tf`.

## Named item

The apply ledger reads the LIVE policy document back after `safe-apply` (via get-role-policy) and prints the
statement's Resource and Condition beside the planned ones.

**CTO half: SIGNED on blob f7aa7b3c.** The CRO half is separate.
