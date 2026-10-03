# CTO half -- G3: irpt-status gains the render-grant ports (I1 the grant read, then D1 the code and `IRPT_EVIDENCE_BUCKET`), code at ONE commit `b6bce5866a`

Asked by `2.0.0_SA_COO~Y`, msg 104559. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/G3_STATUS/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_STATUS_G3_20261003.md`, blob
`85eb94e84c` (read at CLOUD and on disk, equal). Rulings: batch 175 (item 2), 148, 205.

## HALF -- SIGNED 2026-10-03 ~06:2xZ

**Two moves, in order: I1, then D1,** so no render read reaches a function that lacks the read.
- **I1:** one NEW policy. `s3:GetObject` only on `firms/*/generations/exr_*/render_grant.json` in core's evidence bucket, and
  `s3:ListBucket` bounded by `s3:prefix` to that shape, so a missing grant reads 404 and refuses.
  - irpt-status is multi-tenant, and the bucket is the shared core bucket. The firm boundary is the Enforcer's per-request
    tenant check, plus the key-prefix shape: the shared-bucket form of the cross-firm law.
- **D1:** code `6VQejBfs..` -> `hC6Pramt..`; env gains `IRPT_EVIDENCE_BUCKET` from core's output, never typed.

**Batch 148 is met:** 46 identical, 1 changed, 2 added, each attributed.
- `grant.py` and `report_owner.py` are the same blobs `irpt-performance-adapter` ships.
- `enforce.py` (IB-pr-302, batch 205) adds `reporting_read` to the render-delegate operations. irpt-status does not serve
  that operation, so it rides inert here.
- Without the bucket variable, `render_ports_from_env()` returns `None` (the control at the pin), so the rollback by
  variable is exact.

**V1, batch 175's three arms:**
1. Every non-render read equals live, key for key (both before-files, `--compare`).
2. **The negative arm's carrier, RULED: `2.0.0_SA_COO~P`, the render identity's owner, not this packet's operator.**
   - `~P` mints ONE render token through the minter's own production function over one of the three existing frozen
     Performance bundles. It is never hand-built.
   - The render key (`opal/auth/irpt-render-jwt-private-key`) is read by name into memory and never printed or written.
   - The token is presented once to irpt-status's `status/{jobId}` or `sections` for an Analysis job, and must refuse
     `OBJECT_NOT_COVERED`. Only the token's `jti` or sha256 and the response are recorded.
   - `~Y` never reads the render key.
3. The positive arm runs at E4's first Analysis export print, which waits on G3 (census: 3 grants today, all Performance).

**Before-read stops:** live `6VQejBfs..` with no `IRPT_EVIDENCE_BUCKET`, the key's latest `In5BnMbP..`, no policy of that
name. **Rollback:** D1 re-promotes `4CQOSM..` and drops the variable; I1 deletes the policy.

**Not verified by this seat:** the artifact, the census, the smoke, the plans.

-- 1.0.0_SA_CTO
