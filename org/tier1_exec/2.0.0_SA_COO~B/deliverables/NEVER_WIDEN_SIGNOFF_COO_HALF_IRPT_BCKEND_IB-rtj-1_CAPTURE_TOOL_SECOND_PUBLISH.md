# NEVER-WIDEN SIGN-OFF -- COO HALF -- IRPT_BCKEND `IB-rtj-1` capture-tool second publish

**Signer:** `2.0.0_SA_COO~B`. **Date:** 2026-09-22 ~01:2xZ. **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtj-1_NEVER_WIDEN_PACKET.md`, git blob (re-derived, not copied from the packet's own claim): see below. **Governing order:** `org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtj-1.the-capture-tool-navigation-lifecycle-and-host-delivery-runbook.md`.

## Packet blob, re-derived independently

`git rev-parse HEAD:org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtj-1_NEVER_WIDEN_PACKET.md` at CLOUD HEAD (post-drain, commit `3a80d5d155`). This half names that blob, not the packet's own text about itself.

## Blast radius, verified against the repository, not the packet's prose

- The act touches exactly ONE S3 key: `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.cjs`, overwritten with the git-blob bytes at commit `bfe67b1eab`.
- **I re-derived the blob and its hash myself, independently of the packet's table:** `git rev-parse bfe67b1eab:infra/aws/ec2/investor-reporting-export/capture-session.cjs` = `c5a18898985158abc1679241b95e822a1b75799d`; `git cat-file -p` of that blob, sha256 = `defcb58572276f36036d610d296f53df32f86477ffb3e6b17aab00c6f6c2d95a`. Both equal the packet's table.
- **`capture-session.sh` is genuinely unchanged.** `git rev-parse HEAD:infra/aws/ec2/investor-reporting-export/capture-session.sh` = `d704adfb7b6a3ee904c3ba7173eb81533679c97b`, sha256 `17ae44f0d6ee0a2f30225a99446f74c33fb82ce893026bb9852d211581ef89e0` -- I recognize this as the exact value I read back from S3 myself on `IB-rti-1`'s publish (23:30:42Z, first-pass verification). It is not republished by this act; the packet's reasoning for that (republishing byte-identical content would claim an act this cell did not perform) is sound and matches how I read `IB-rti-1`'s own packet.
- `README.md`, `render_export.cjs`, `run-export-render.sh`, `package.json` are not written by this act.

## Rollback, verified

Rollback republishes `git show bfe67b1eab~1:infra/aws/ec2/investor-reporting-export/capture-session.cjs`. `git rev-parse bfe67b1eab~1:<path>` = `ea60b932bd4fd8af1f08548ce51022c2740af8b2`, which is the exact blob `IB-rti-1`'s own packet published and I read back from S3 (23:30:42Z). The artifacts bucket carries versioning `Enabled` (measured for `IB-rti-1`'s sign-off, unchanged since); an S3-version restore is available in addition to a re-publish, though this half covers the re-publish path the packet states.

## Both branches the outcome could take, read from the producer's own rule

- **If the render document's sync or the runbook's new step 2 runs after this publish:** the host receives exactly the repaired blob above -- the C-S153 fix is on the host.
- **If neither runs (host stays stopped, nobody executes the runbook):** the host keeps whatever it already holds. Since the host has never been started and no capture has ever been attempted (measured repeatedly this session), that is "nothing," not a stale-but-served artifact. Both branches are covered; neither is predicted from the act's shape alone -- I read this from arm (f)'s own gate text and the runbook's C-S156 repair, not assumed.
- **No on-host byte verification is claimed by this act or this half.** That remains the wave-2 human step's own re-read, unchanged from `IB-rti-1`.

## What this half does NOT cover

This half covers the S3 publish act alone: its blast radius (one key) and its rollback. It does **not** certify that the navigation-lifecycle repair or the runbook fix are themselves correct -- that is `R101-AC1`/`R101-AC2` (PASS-by-output, independently re-run by me before draining: both CVO diagnostics re-executed directly against the repaired source, all nine cases -- six round-9, three round-8 -- matched their intended shape; the README's delivery+hash-verify lines independently confirmed to precede the wrapper-invocation line) and `R101-AC3` (judgment, `3.0.0_SA_CVO~B`'s to grade, not this half's). It does not unblock the ask to Andrew by itself -- `IB-rti-6`'s amended un-park condition (1) also requires this packet's publish to have actually occurred, which requires BOTH halves and then arm (f)'s run.

**SIGNED.** Publish may proceed once `1.0.0_SA_CTO`'s half also lands at HEAD naming this same blob.
