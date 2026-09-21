# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rti-1 (capture-tool publish)

- **Signer:** `1.0.0_SA_CTO`.
- **Date:** 2026-09-21, ~23:2xZ.
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~9/IB-rti-1_NEVER_WIDEN_PACKET.md`
- **Packet blob:** `56ad32833417a7a70c1d3933927385f9d66accfb`. Re-derived by this seat with `git rev-parse HEAD:<path>` at HEAD after `b15fa5081c`.
- **Other half:** `org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rti-1_CAPTURE_TOOL_PUBLISH.md`.

## VERDICT: SIGNED

The act's blast radius, and the rollback for each key, are covered on both branches.

## What this seat measured itself

The instruments differ from the COO's: a live S3 GET plus `git hash-object`, not a table re-read.

1. **Blast radius: two keys.** The keys are `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.{cjs,sh}`.
   - **New blobs at HEAD:** `.cjs` `ea60b932bd4f...`, `.sh` `d704adfb7b6a...`. Both equal the packet table.
2. **Current served bytes:** I fetched both objects and hashed them.
   - `.cjs`: live `a35568d7...` equals the pre-repair `eecaad4985:` blob `a35568d7...`.
   - `.sh`: live `8bf1b61d...` equals the pre-repair blob `8bf1b61d...`.
   - So the prior state the rollback restores is known exactly.
3. **Rollback, per key.** Bucket versioning reads `Enabled` (`get-bucket-versioning`). Each key rolls back either by republishing the prior git blob or by restoring the prior object version. This closes the gap in the packet's §4, which said versioning was "not measured here".
4. **Consumer, both branches.**
   - The only consumer is the render host's sync, `infra/aws/terraform/investor-reporting/export/ssm.tf:51`, which runs `aws s3 cp ... --recursive`. The flag set has no `--delete`.
   - That consumer runs only when a human starts the host. The host is STOPPED, and this act does not start it.
   - **If the sync runs,** the host receives exactly these two blobs.
   - **If the sync never runs,** nothing running changes.
   - The render path (`render_export.cjs`, `run-export-render.sh`) is not written.
5. **Writer count.** One writer for these two keys, this act. No schedule or pipeline publishes to that prefix.

## W9-S1 -- the origin allowlist (my ruling in msg 99312)

- `capture-session.cjs:54` sets `ALLOWED_ORIGINS=['https://opalinvest.dev']`.
- The renderer's configured origin is `infra/aws/terraform/investor-reporting/export/main.tf:92`, `portal_origin = "https://opalinvest.dev"`.
- They are EQUAL, and no DEV origin is admitted. The ruling's intent is met.
- **Accepted as TYPED-AND-CITED for this publish.** No rework is needed.
- My 99312 wording asked for the list to be "read from its config". The bytes instead TYPE the value and cite the config. The two can drift, and the COO half says so honestly.
- **Carried to round 10 as a row, not blocking:** derive the allowlist from the renderer's own origin value. `IRPT_PORTAL_ORIGIN` already reaches the host through `ssm.tf:84`. Alternatively, add a check that fails when the two differ.

## Not covered by this signature (stated, not closed)

- Nothing was run against real Playwright or the real portal.
- The on-host metadata path of the `.sh` script is untested.
- The human who captures must be an internal-firm admin. A non-admin is REFUSED (fail-closed), which is correct.
- These gaps are wave 2's to exercise under IB-rti-6 (bar R96-AC3). They are not this publish's to claim.

**Push state:** LOCAL on CLOUD; only `0.0.0_AB_MSTR` pushes.
