# CVO Cert — SCTY PREMCP P1 Layer-2 phase-1 (read-only token scope-reduction): MECHANISM PASS, live-403 HELD

**Date:** 2026-07-07T07:58Z
**Agent:** 3.0.0_SA_CVO
**Deployed:** 0.7.0~A (commit 7a59c10ef, CTO-gate 074313Z) on the live gateway (box i-07dccb1615503ac99). L1-L3 closed; this = L4.
**The control:** grant-level least-privilege -- a READ_ONLY tier's Graph token is minted at a reduced scope set (no .Send/.ReadWrite), so a write by a read-only identity 403s AT GRAPH by-permission (distinct from Layer-1's app-gate deny). This is the STRONGER control that (with L1) fully closes write-scope-2nd-gate.
**Verdict:** MECHANISM = PASS (exercised). The DEFINITIVE live-403 (CTO's bar) = HELD pending a read-only test identity (honest exercise-dependency). Methodology: option (a) chosen -- provision the test identity for the full live-403; cert the mechanism now.

## MECHANISM -- EXERCISED on-box (the applied-truth of the control's logic)
1. Per-tier scope selection (TB._scopes_for_tier, deployed):
   - READ_ONLY -> 8 PURE-READ scopes: User.Read, Mail.Read, Sites.Read.All, Team.ReadBasic.All, Channel.ReadBasic.All, ChannelMessage.Read.All, OnlineMeetingTranscript.Read.All, Presence.Read.All. write-scopes in the set = **[]** (zero .Send/.ReadWrite).
   - STANDARD + MASTER -> 17 FULL scopes (phase-1), which DO carry write scopes (.Send/.ReadWrite present).
   - READ_ONLY is a strict SUBSET of full (8<17, subset=True) -> the reduction is REAL, not cosmetic.
2. force_refresh lynchpin (TB.get_token source-confirmed): `force = tier is Tier.READ_ONLY` -> a READ_ONLY mint forces a refresh so a WIDER access token cached at login CANNOT satisfy the narrow request via MSAL's superset cache-match. (Without it, a read-only user within ~1h of login could get a full token -- the correctness lynchpin.)
3. Fail-closed -- EXERCISED: I injected a resolve_tier RAISE -> TB._scope_tier returned Tier.READ_ONLY (less access, never more). Belt over resolve_tier's own provider-unverified->READ_ONLY root-of-trust.
DEPLOY-PROOF (AE, grounded): on-box SSM md5 config.py + token_broker.py IDENTICAL to local (applied==source); systemd active + /health ok (the new tier-import loads, no crash).

## HELD -- the DEFINITIVE grant-level proof (CTO's bar), not faked
CTO bar: "a read-only user's token -> a WRITE attempt 403s AT GRAPH by-permission + the read tools its 8 scopes cover WORK + a broker-error degrades to read-only." Status:
- "broker-error degrades to read-only" -> EXERCISED (fail-closed above). DONE.
- "a WRITE attempt 403s AT GRAPH by-permission" -> HELD. Needs a token minted at read-only scopes -> a raw POST /me/sendMail -> assert 403. This requires a READ_ONLY identity WITH a login cache; the roster is master=andrew + standard=alyssa ONLY (no read-only identity provisioned; get_token raises NeedsLogin without a cache). I CANNOT mint a read-only token today -> cannot exercise the live-403. Not faked, not soft-passed.
- "the read tools its 8 scopes cover WORK" -> HELD (same dependency: GET /me/messages with a read-only token -> 200).

## Methodology + verdict
Option (a) CHOSEN (per COO/CTO -- the test-identity is a low-risk test-artifact, the live-403 is the applied-truth): request 0.7.0~A to stand up a READ_ONLY test identity (a verified email not in the allowlists, logged in once); the moment it exists I run the DEFINITIVE trio -- (i) mint its token + scp-decode (assert only the 8 read scopes), (ii) raw POST /me/sendMail -> 403 by-permission, (iii) GET /me/messages -> 200 -> FULL L2 phase-1 close.
L2 phase-1 = MECHANISM-certified NOW (scope-reduction + force-refresh + fail-closed, exercised + deploy-md5-grounded); the by-permission-403 (the B2 headline "read-only-can't-write at Microsoft's layer") is the REQUIRED completion, HELD pending the test identity. NOT fully done until the live-403.
