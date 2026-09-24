# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rtj-1 (capture tool, second publish)

- **Signer:** `1.0.0_SA_CTO`
- **Date:** 2026-09-22 ~01:3xZ
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtj-1_NEVER_WIDEN_PACKET.md`
- **Packet blob:** `2450320a688a4740af81d3a72f281b2a06f05b23`, re-derived at HEAD with `git rev-parse`.
- **Other half:** `2.0.0_SA_COO~B` @`5b67db0397`.

## VERDICT: SIGNED

The act is a republish of exactly ONE changed key. `capture-session.sh` is byte-unchanged.

## What this seat measured

The instruments differ from the COO's: a git-blob sha256, a live S3 GET, a direct read of the diff, and a direct read of the README.

1. **The new bytes.**
   - `capture-session.cjs` at HEAD is blob `c5a18898...`, sha256 `defcb585...72c6d95a`.
   - `capture-session.sh` at HEAD is blob `d704adfb...`, sha256 `17ae44f0...`. This is unchanged since IB-rti-1.
2. **What is served now, which is the rollback target.**
   - The live `capture-session.cjs` has git-hash `ea60b932...`. That is the IB-rti-1 version. It exists and is retained, and bucket versioning is Enabled (read at the IB-rti-1 sign-off).
   - Rollback means republishing `ea60b932`, or restoring the prior object version.
3. **The change itself.** I read `git diff ea60b932 HEAD:<cjs>` directly. It is 56 insertions and 9 deletions.
   - It adds `walkRedirectHops` / `assertNoForeignHop`.
   - It applies them to the INITIAL `page.goto` response, before any port-forward command is printed.
   - It keeps the original final-URL check, unweakened.
   - The verification-navigation hop walk is factored into the same helper, and its behaviour there is unchanged.
   - **Edge case:** `walkRedirectHops` returns an empty set when a response exposes no `request()`. That branch is reachable only by a stub. A real Playwright `Response` always carries one, and the existing final-URL check still applies. It is not a gap on the real path.
4. **Runbook ordering (C-S156).**
   - `README.md` step 2 runs `aws s3 cp` on exactly the two keys, then `sha256sum`.
   - It prints the two expected hashes, which equal (1) above.
   - It says STOP on a mismatch.
   - All of this comes BEFORE step 3's wrapper invocation.
   - No render is used to side-load the tool.
5. **Consumer.** The consumer is unchanged from IB-rti-1. The host is STOPPED (EC2 read at 00:1xZ), and the act does not start it.

## rti-6 un-park condition (1)

- (a) and (b) are met at CODE level on `2.0.0_SA_COO~B`'s run of both CVO diagnostics.
- (c) is met by the README ordering above.
- **Condition (1) is MET only once this publish completes AND its S3 readback equals `defcb585`.** `2.0.0_SA_COO~B`'s rule is correct: the ask to Andrew waits for that readback, not for this signature.

## Not covered

- This signature does not cover any real-browser, real-portal or on-host execution. That is wave 2's job under R96-AC3.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
