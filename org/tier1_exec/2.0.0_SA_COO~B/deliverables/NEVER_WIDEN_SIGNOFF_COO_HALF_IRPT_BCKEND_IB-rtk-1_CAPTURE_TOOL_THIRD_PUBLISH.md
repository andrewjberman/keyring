# NEVER-WIDEN SIGN-OFF -- COO HALF -- IRPT_BCKEND `IB-rtk-1` capture-tool third publish

**Signer:** `2.0.0_SA_COO~B`. **Date:** 2026-09-22 ~03:5xZ. **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtk-1_NEVER_WIDEN_PACKET.md`, git blob at CLOUD HEAD post-correction = **`5d30a76a4e851064e9f5ff0e4a3b742fdd740e6b`**. This half names that literal blob, printed here, not described by a command that produces it.

## A defect in this packet was found and fixed before signing

The packet's original sha256 for the new `capture-session.cjs` blob was WRONG (`fffef738e90cf03bfb20cdfbeb8cbb310e3a44c6eee657974f8a3eeb92e8e35b`); I caught this by independently re-deriving the hash myself, twice, with two different git commands (`git cat-file -p <blob> | sha256sum` and `git show <commit>:<path> | sha256sum`), both agreeing with each other and disagreeing with the packet. Corrected @`2505e2c00a`, the packet's blob above is the POST-correction version. **This half is signed against the corrected packet, never the original.**

## Blast radius, independently re-derived

- The act touches exactly ONE S3 key: `s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/capture-session.cjs`, overwritten with the git-blob bytes at commit `0d0c8cdc4d`.
- **Blob and hash, re-derived myself, both methods agreeing:** `git rev-parse 0d0c8cdc4d:infra/aws/ec2/investor-reporting-export/capture-session.cjs` = `ded605028b2210b589735927868aacf92ceb852d`; `git cat-file -p` of that blob, sha256 = **`f03666ef827e7c6a169214c83b2a4fe593d7f1cbf181f728f1febb0235eacd0d`**. Equal to the corrected packet's table.
- **`capture-session.sh` is genuinely unchanged.** `git rev-parse HEAD:infra/aws/ec2/investor-reporting-export/capture-session.sh` = `d704adfb7b6a3ee904c3ba7173eb81533679c97b` -- the same value I have independently verified as the live S3 bytes twice before in this chain (`IB-rti-1`, `IB-rtj-1`). Not republished; the packet's reasoning (republishing byte-identical content would claim an act this cell did not perform) is sound.
- **`README.md` is deliberately NOT touched by this packet's commit, and I agree with that design.** The README's current expected-hash line for `capture-session.cjs` (`defcb58572276f36036d610d296f53df32f86477ffb3e6b17aab00c6f6c2d95a`) is still the TRUE live S3 value right now, since this publish has not run. Updating it early would make the runbook assert a value S3 does not yet hold, and an operator following step 2 TODAY would see a genuine mismatch against currently-live bytes and, per the runbook's own instruction, incorrectly escalate a non-problem. The README edit is correctly deferred to land in the SAME act as the publish, when both become true together.

## Both branches the outcome could take, read from the producer's own rule

- **If the publish runs (both halves land) and either the render document's sync or the runbook's step 2 subsequently runs:** the host receives exactly this repaired blob -- C-S158 and C-S159 are closed on the host.
- **If the publish runs but neither delivery path ever executes:** the host keeps whatever it already holds. The host has never been started and no capture has ever been attempted (measured repeatedly this project), so that is "nothing," not a stale-but-served artifact.
- **No on-host byte verification is claimed by this act or this half.** That remains the eventual human step's own re-read.

## What this half does NOT cover

This half covers the S3 publish act alone: its blast radius (one key) and its rollback (`git show 0d0c8cdc4d~1:<path>`, blob `c5a18898985158abc1679241b95e822a1b75799d`, plus reverting the README line to `defcb58572276f36036d610d296f53df32f86477ffb3e6b17aab00c6f6c2d95a` in the same act). It does **not** certify that the repair itself is correct -- that is `R107-AC1`/`R107-AC2` (PASS-by-output, independently re-run by me before draining: both residual counterexamples now refuse under a fresh diagnostic run I executed myself; R8/R9 diagnostics unchanged; the observer/latch code read directly, confirmed installed before the first navigation with no clear path) and `R107-AC3` (judgment, `3.0.0_SA_CVO~B`'s to grade, not this half's). It does not by itself unblock the ask to Andrew -- `IB-rti-6`'s condition (1) needs the CVO's judgment grade to read PASS, plus a fresh S3 readback once the publish runs.

**SIGNED.** Publish may proceed once `1.0.0_SA_CTO`'s half also lands at HEAD naming this same corrected blob (`5d30a76a4e851064e9f5ff0e4a3b742fdd740e6b`).
