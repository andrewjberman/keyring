# ANDREW-DIRECT 2026-10-04 ~18:4xZ -- opal_ai: push to DEV and merge forward to PROD

- **Channel:** the site-Z terminal of `1.0.0_SA_CTO~O` (session 56ca6db5-b4b3-4db9-a2f4-71c54ede0632), typed by Andrew.
- **Time:** 2026-10-04 ~18:4xZ (14:4x ET).
- **Recorded by:** `1.0.0_SA_CTO~O`, same turn.

## Verbatim

Andrew: "we need a push to DEV and merge forward to PROD or however we do it for opal_ai"

## Measured at the word (ls-remote and local reads, ~18:4xZ)

- opal_ai origin DEV = PROD = `bd7cd5d1ce`.
- Ahead of PROD, and READY: `nfra-opalai-r2-dev` @`e34ba40`, ONE commit.
  - It is NFRA_OPALAI's OA-f-13 fix: `wall-dapi-8194-wfp.ps1`'s sublayer read-back prints the engine-assigned weight.
  - It is complete (drained @7a673ae699), and its AC1 passed with the issuer's re-run.
  - It touches no launcher or launch-gate file.
- Ahead of PROD, and NOT routed: 5 NFRA_MCPMSP commits on `wk-NFRA_MCPMSP-6-opal_ai` (head `32abfdb`, "runtime-msp:
  sender-gate PreToolUse hook (MS-sh-1)", and others). The same 5 sit on a stale local `DEV` ref in the `/c/tmp/oa-dev`
  clone. NFRA_MCPMSP is PARKED (@66f7167c39), and no release review has covered them.

## How opal_ai ships (the shared-branch law, org/XXX.md)

`0.0.0_AB_MSTR~Z` pushes opal_ai `DEV` and `PROD` on Andrew's word. The release is a fast-forward of DEV to the
release head, then PROD to DEV, so that DEV = PROD.

## Scope routed (nothing wider)

- DEV fast-forwards `bd7cd5d1ce` -> `e34ba40`, then PROD fast-forwards to the same commit.
- The 5 MCPMSP commits are NOT in this push. They are put to Andrew as one question, since his words did not name them
  and their project is parked.

## Disposition of the MCPMSP question (1.0.0_SA_CTO~O, 2026-10-04 ~20:2xZ, at /open-calls)

Withdrawn from Andrew's queue and decided in this lane: HOLD. Leaving the commits out is the default and needs no word.
Only the ship branch is sovereign. The commits stay on `wk-NFRA_MCPMSP-6-opal_ai` @32abfdb (worktree `C:/tmp/ms-6`).
They reach opal_ai DEV/PROD only after NFRA_MCPMSP un-parks (G-MSPID answered, or Andrew's word; Andrew's last word was
"Not yet", CTO 27426) and a release review covers them.
