# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-performance-adapter decrypts the render grant under the S3 Bucket Key

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_RENDER_GRANT_KMS_20260927.md`
blob `f7aa7b3cba9ef8c65c73bb0ea660b80eb07569a2` @`03de7272cd`. The blob is the same at HEAD and on disk (read
2026-09-27 ~21:4xZ).
**Code read here:** backend `c8572cb1bd`, `infra/aws/terraform/investor-reporting/performance/render_grant.tf`
(+9/-3). **Asked by:** 2.0.0_SA_COO~P msg 102146. This seat is not in the act.

## VERDICT: SIGNED on blob f7aa7b3c

- **The cause holds.** The evidence bucket uses an S3 Bucket Key, so S3 presents the BUCKET ARN as the KMS encryption
  context. The old statement conditioned on the OBJECT path, which could never match, so window 18's render read was
  refused AccessDenied. "exr_ is absent" on the print page only named the revision of the failed fetch.
- **On balance the change narrows, and it is bounded.**
  - `Resource` narrows from `*` to core's ONE key (`key/7f4d3042..`).
  - The context widens from an object path to the bucket ARN `opal-data-ycharts`, with `kms:ViaService` = S3 kept.
  - Decrypt is therefore reachable only through S3 reads the role already holds. In `opal-data-ycharts` that is
    ONLY `firms/*/generations/exr_*/render_grant.json`.
  - All 7 of the role's GetObject statements, across its 6 inline policies (0 attached), are printed, and no other
    statement names this bucket.
- **The simulator carries its negative arms.** Old deny, new allow (the W18 failure reproduced). The following stay
  denied:
  - another key;
  - a call without the S3 ViaService;
  - GetObject of `narrative_packet.json` in the same folder.
- **The move:** the plan is 0/1/0, policy only, and the function is untouched. Rollback is `12a67ed5ee`'s
  `render_grant.tf`. The proof runs in the next K8 window: a render read with no AccessDenied, and READY with a %PDF.

Not measured by this seat: the live policy census and the simulator runs (the packet's).
