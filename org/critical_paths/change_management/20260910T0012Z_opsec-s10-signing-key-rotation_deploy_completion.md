# Deploy Completion Record
**Date opened:** 2026-09-10T00:12:38.800121+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T012637Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-10: ROTATE THE LOGIN SIGNING KEY WITH NO SIGN-OUT (FWD-10). Mint a new RSA-2048 keypair, publish the two-slot verification envelope, let all four consumers converge, THEN switch signing, and keep the old key accepted for the overlap. PRE-CHANGE BASELINE: both secrets ONE version at AWSCURRENT -- private 1acd44f3-d07e-486b-9ad8-66993a0b6716 LastChangedDate 2026-04-06T13:31:00.251000-04:00, public fabe94f0-019d-455d-8c72-47b3d709bd8b .259000-04:00, RotationEnabled unset on both, public secret a BARE PEM 450 bytes, matched RSA-2048 pair verified. ROLLBACK, NAMED BEFORE THE FIRST ACT: every PutSecretValue leaves the prior version as AWSPREVIOUS, so rollback is update-secret-version-stage moving AWSCURRENT back to the prior version id -- and the old material is ALSO held locally for the length of this act. NOTHING IS DELETED: no scheduled deletion is created and RotationEnabled stays unset
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT CAPTURE: a token signed by the OLD key minted and recorded BEFORE any write -- it is the no-sign-out evidence and S10-AC3 turns on it. Plus a token signed by a key that will be in NEITHER slot, as the negative control | the two tokens' identity and expiry, captured before the first PutSecretValue | PRE-ACT CAPTURE COMPLETE, AND THE BASELINE IS A REAL DISCRIMINATOR RATHER THAN AN ASSUMPTION.

THE KEYPAIR: a new RSA-2048 keypair was minted locally, matching the algorithm and size of the pair it replaces -- the outgoing pair was confirmed a MATCHED pair first (the public secret is byte-identical to the public half derived from the private secret) and measured at 2048 bits, so the replacement is like-for-like. New public sha256[:16] c7d9ff246d486c14 against the old 9b2bc47268f929b0; distinct, checked rather than assumed.

THE PRE-ACT TOKENS, all three signed BEFORE any PutSecretValue:
  old_refresh  signed with the OLD private key, type=refresh, exp +7d   <- the no-sign-out subject
  old_access   signed with the OLD private key, iss=opal-portal-auth aud=opal-portal-api, exp +900s
  ctl_refresh  signed with a THROWAWAY key that will be in NEITHER slot <- the negative control

*** THE BASELINE THAT MAKES THE AFTER-TEST MEAN ANYTHING, measured on the LIVE endpoint before the envelope was written: ***
  old-key refresh token   -> {"error":"User not found"}
  neither-slot token      -> {"error":"Internal server error"}
THE TWO ANSWERS DIFFER, AND THEY DIFFER EXACTLY AT THE CRYPTO BOUNDARY. "User not found" means the SIGNATURE VERIFIED -- the token got through verifyRefreshToken -- and then failed at the user lookup, because the sub is a fabricated opaque binding with no matching row. "Internal server error" means the signature was REJECTED (JsonWebTokenError, which index.ts:233-241 surfaces as a 500 because it has no specific catch). So the pair separates "crypto accepted" from "crypto rejected" on live traffic, which is precisely the axis a key rotation moves.

WITHOUT THIS BASELINE THE AFTER-TEST WOULD HAVE BEEN VACUOUS: "the old token still verifies" is worth nothing unless it verified BEFORE, and a probe that fails for a non-crypto reason both times would have looked like success. The user-lookup failure is not a defect in the probe -- it is what lets the probe isolate the crypto step, which is the only step this act changes. | CLOSED 20260910T001700Z |
| L2 | activation | PUBLISH THE VERIFICATION ENVELOPE: opal/auth/jwt-public-key becomes {current: NEW_PUB, previous: OLD_PUB}. Signing does NOT move here -- this write only widens what is ACCEPTED, so it is safe in isolation and reversible by stage-move | the PutSecretValue result + the new version id + the prior id still present as AWSPREVIOUS | THE VERIFICATION ENVELOPE IS PUBLISHED AND SIGNING HAS NOT MOVED.

opal/auth/jwt-public-key was a BARE PEM (450 bytes, one BEGIN block, measured) and is now the two-slot envelope {"current": NEW_PUB, "previous": OLD_PUB}, 947 bytes. PutSecretValue returned VersionId 01cfa582-621c-4fff-a320-44cbafa2ccc8 at stage AWSCURRENT.

WHY THIS WRITE IS SAFE IN ISOLATION, and why it is deliberately FIRST: it only WIDENS what is accepted. Every consumer reads current-or-previous, so a consumer that has converged accepts BOTH the new and the old key, and a consumer that has NOT yet converged still holds the old bare PEM and accepts the old key -- which is still the only key anything is signing with. There is no instant at which a live token is unacceptable to a converged or an unconverged reader. Signing does not move until L4, and only after L3 shows every consumer serving this envelope.

THE ROLLBACK IS LIVE AND WAS VERIFIED RATHER THAN ASSERTED: describe-secret now shows TWO versions -- 01cfa582 at AWSCURRENT and fabe94f0-019d-455d-8c72-47b3d709bd8b at AWSPREVIOUS. fabe94f0 is exactly the version id this session recorded as the baseline at 18:3xZ, so the pre-rotation material is retained by AWS itself and rollback is a stage move rather than a restore from a copy. DeletedDate is (none) and RotationEnabled is still unset -- this act creates no scheduled deletion and turns on no automatic rotation, per S10-AC5 and deliverable 4. | CLOSED 20260910T001700Z |
| L3 | verify | CONVERGENCE PER CONSUMER, on a DISCRIMINATING instrument (CloudTrail carries the secretId; REPORT Duration does not -- Z-S155). FOUR observations, not one generalised: the three verifiers AND the signer, each read separately with its timestamp, BEFORE signing moves. NO consumer is redeployed during the window | per-consumer CloudTrail reads with their timestamps | ALL FOUR CONSUMERS SERVE THE ENVELOPE AND ACCEPT BOTH SLOTS, EACH READ SEPARATELY, ALL BEFORE SIGNING MOVES. AND THE FIRST READING OF CONSUMER 3 WAS A FALSE BLOCKING FINDING THAT THE CONTROLS CAUGHT.

THE INSTRUMENT IS DISCRIMINATING BY CONSTRUCTION, not by timing. Two probe tokens: one signed by the NEW key, which exists ONLY in the envelope's `current` slot, and one signed by the OLD key, which exists ONLY in `previous`. A consumer still holding the pre-envelope bare PEM accepts the old and REFUSES the new. A single-slot consumer that has converged accepts the new and REFUSES the old. Only a two-slot consumer serving this envelope accepts BOTH. Each arm carries two controls: CTL, a key minted fresh into NEITHER slot, and EXP, the correct OLD key with exp in the past.

*** THE CORRECTION, AND IT IS THE REASON THIS LEG IS TRUSTWORTHY. *** The first session-analytics probe (00:29Z) read NEW accepted / OLD REJECTED -- the exact signature of a single-slot verifier, which would have been a third BLOCKING stop and would have halted the rotation. It was wrong. The fixture had aged out mid-experiment: old_access.jwt carried exp=1789000096 (00:28:16Z) and was decoded 342s past expiry, while new_access.jwt (exp 00:32:48Z) was still live at call time. AN EXPIRED TOKEN AND A WRONG-KEY TOKEN BOTH RETURN 401 {"error":"Unauthorized","details":"Invalid token"}, BYTE-IDENTICAL -- so a stale fixture is indistinguishable from the defect it imitates. Every arm was re-minted fresh and re-run.

THAT CONFOUND IS MEASURED HERE, NOT ASSERTED. The re-run carries an EXP arm on purpose -- the OLD key, correct and in `previous`, with exp 1026s in the past -- precisely so the record shows the two causes returning the same bytes rather than my claiming they would:
  opal-session-analytics, 2026-09-10T00:39:44Z, all four tokens minted at 00:37:48Z
    NEW  (current slot)          -> 400 "user or date parameter required"   PAST THE AUTH GATE = ACCEPTED
    OLD  (previous slot)         -> 400 "user or date parameter required"   PAST THE AUTH GATE = ACCEPTED
    CTL  (neither slot)          -> 401 Unauthorized \| Invalid token        REFUSED
    EXP  (old key, but expired)  -> 401 Unauthorized \| Invalid token        REFUSED, IDENTICAL BYTES TO CTL
The 400 is the route's own missing-parameter answer from BEYOND requireAdmin -> verifyAuth, so reaching it is proof the signature verified; it is not a failure. CTL proves the check can still refuse, so the two 400s are real accept decisions and not a disabled gate.

THE FOUR OBSERVATIONS, each its own read with its own timestamp, none generalised from another:
  [1] auth-validator-edge        00:22:20Z NEW 200 / OLD 200 ; re-read 00:40:58Z NEW 200 / OLD 200
  [2] opal-portal-authorizer     same two reads -- GET /v1/market/rsi traverses the edge THEN the origin
                                 authorizer, so a 200 requires BOTH to have verified; CTL 401, EXP 401,
                                 no-bearer 401 separate a real accept from a bypass
  [3] opal-session-analytics     00:39:44Z, direct invoke on the read-only /sessions route, table above
  [4] opalinvest-auth-handler    00:22:20Z and 00:40:58Z, POST /auth/refresh: NEW -> {"error":"User not
      VERIFY path                found"} and OLD -> {"error":"User not found"} (both crypto-ACCEPTED,
                                 failing later at the user lookup), CTL -> {"error":"Internal server
                                 error"} (crypto REJECTED). That is L1's pre-act baseline discriminator,
                                 unchanged, so the after-test is read on the same axis it was calibrated on.
Consumer 4 is the SIGNER, counted here in its VERIFIER role only -- the role Z-S160 found and TO-OP-S-10F fixed. Its SIGNING convergence is L4's subject and is not inferred from this.

CONDITION 3, NO CONSUMER REDEPLOYED DURING THE WINDOW -- measured on LastModified, not asserted. The envelope landed 2026-09-10T00:15:48Z (version CreatedDate, AWS-side and authoritative; the locally recorded epoch 1788999420 = 00:17:00Z is my script's wall clock AFTER the call). Every consumer's LastModified PREDATES that write:
  opal-session-analytics  2026-09-09T21:26:02Z   66qB33r/6QF+jkb/lcrSbRD+UvEnDhyDVK15rdV2+Ko=  Active
  opal-portal-authorizer  2026-09-09T18:50:07Z   KHwksfO1XjL0Jg66kc7L+gFIOEsZT/7l2i8STRgBvS4=  Active
  opalinvest-auth-handler 2026-09-09T23:39:18Z   sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw=  Active
  auth-validator-edge     2026-09-09T19:43:47Z   wRAHCaKdoJ+wGRe95gu0Yh0jcTEeXTAPahEhQ8sRiic=  Active
So every acceptance above is the deployed artifact re-reading a CHANGED SECRET on its TTL, which is the property the rotation depends on -- not a fresh deploy that would have masked whether convergence works at all.

GRAIN, because a write receipt is not a served state: the envelope was re-read from AWS and its halves fingerprinted against the local PEMs rather than trusted from the PutSecretValue response. 947 bytes, keys exactly ["current","previous"]; current sha256[:16] c7d9ff246d486c14 == newpub.pem, previous 9b2bc47268f929b0 == oldpub.pem. Versions: 01cfa582-621c-4fff-a320-44cbafa2ccc8 AWSCURRENT, fabe94f0-019d-455d-8c72-47b3d709bd8b AWSPREVIOUS -- the rollback still live as a stage move.

SIGNING HAS NOT MOVED. opal/auth/jwt-private-key LastChangedDate is still 2026-04-06T13:31:00.251-04:00, one version, RotationEnabled unset, no DeletedDate. L4 is now unblocked on the evidence this leg exists to produce. | CLOSED 20260910T005120Z |
| L4 | activation | SWITCH SIGNING: opal/auth/jwt-private-key becomes NEW_PRIV, and only after L3 shows every consumer serving the envelope | the PutSecretValue result + the signer observed converging on the NEW key | SIGNING IS SWITCHED AND THE SIGNER WAS OBSERVED CONVERGING. AND THE FIRST WRITE OF THIS LEG SILENTLY TRUNCATED THE PRIVATE KEY TO 27 BYTES AND RETURNED rc=0 WITH A VersionId -- THE SIGNING SECRET WAS INVALID IN PRODUCTION FOR 3m52s. That is reported here in full because the read-back is the only reason it is not still true.

=== WHAT HAPPENED, IN ORDER, WITH AWS-SIDE TIMESTAMPS ===

  01:09:42.364Z  VersionId 5bc63c94-7d91-4deb-b622-7ae0f8e71935 -> AWSCURRENT.
                 PutSecretValue returned rc=0 and a VersionId. THE STORED VALUE WAS 27 BYTES:
                 the single line "-----BEGIN PRIVATE KEY-----" and nothing else.
  01:13:34.378Z  VersionId 579af491-ab27-4463-978d-b076cd5ce44a -> AWSCURRENT, 1703 bytes,
                 re-written through boto3. THE INVALID WINDOW IS 232.014s = 3m52s.
  01:16:32Z      the signer observed minting NEW-key tokens. CONVERGED.
  01:18:14Z      AWSPREVIOUS moved off the truncated version onto the real baseline.

=== THE CAUSE, NAMED PRECISELY, BECAUSE THE NEXT LANE WILL HIT IT ===

The PEM was passed as ONE argv element to `.tools/aws.cmd`. That shim is a Windows CMD batch file, and CMD cannot carry an embedded newline inside an argument -- so the value was cut at the FIRST newline and everything after it was discarded. I had deliberately chosen argv-with-no-shell OVER `file://` precisely to avoid mangling, having been bitten before by the shim rewriting POSIX paths. THE REMEDY I REACHED FOR WAS THE ONE THAT CAUSED THE DEFECT: shell=False protects against the SHELL, and the shim is not the shell -- it is a CMD process downstream of it that re-parses argv on its own terms.

*** AND THE API CONFIRMED THE WRITE. *** PutSecretValue answered rc=0, VersionId, VersionStages ['AWSCURRENT']. A write receipt certifies that a version was CREATED; it says nothing about the BYTES it holds. Every signal available at the call site said the act had succeeded.

WHAT CAUGHT IT was reading the secret BACK from AWS and fingerprinting it, which this leg did because L2 had established that habit -- and the read-back did not report a mismatch, it reported that openssl could not parse the served value AT ALL ("Could not find private key"). AN INSTRUMENT ERROR AND A WORLD ERROR LOOK THE SAME AT FIRST GLANCE, and my first reading was that my fingerprint helper had broken. Measuring the served value directly -- 27 bytes, one line, raw sha256 differing from the local file -- is what separated them. A verdict of "ERROR" from a comparison helper is not evidence about the world until you read the object.

=== BLAST RADIUS, MEASURED RATHER THAN REASSURED ===

CloudWatch Errors for opalinvest-auth-handler over 01:00-01:20Z: ONE invocation in the whole span, at 01:11:32Z, INSIDE the invalid window, and it was a COLD START (INIT_START at 01:11:31.933Z) -- i.e. exactly the case with no cached key that would have had to read the broken secret. Errors = 0.

ERRORS=0 IS THE WEAK ARM AND IS NOT WHAT CLOSES THIS: a handled 500 never increments that metric. The log stream is what closes it. The 01:11:32Z request logged "POST /auth/refresh" and then END with NO ERROR line -- and the generic catch demonstrably DOES log, because my own CTL arm at 01:16:34Z produced "ERROR Error: W6 [JsonWebTokenError]: invalid signature" through that same path. So the 01:11:32Z request did not throw, which means it returned before reaching getJwtPrivateKey (no refresh cookie -> the early 401). It never touched the broken value.

WHAT I CAN AND CANNOT CLAIM: no user-facing failure is MEASURED, on 1 invocation with its log line read. I am NOT claiming the window was harmless -- a signing attempt in those 232 seconds WOULD have failed, and the only reason none did is that none arrived. The denominator is 1, and it is printed rather than dressed up.

=== THE SECOND DEFECT THE FIX CREATED, FOUND BY LOOKING FOR IT ===

Re-writing the correct key made AWSPREVIOUS point at the 27-BYTE TRUNCATED VERSION. Every rollback instruction on this order -- including this ledger's own title, "rollback is update-secret-version-stage moving AWSCURRENT back" -- would then have RESTORED A BROKEN KEY. The documented recovery path had been quietly converted into a second outage.

DISARMED at 01:18:14Z: AWSPREVIOUS moved from 5bc63c94 onto 1acd44f3-d07e-486b-9ad8-66993a0b6716, verified by reading the stage back (1704 bytes, SPKI DER 3051443047acf258..., equal to the local oldpriv.pem). NOTHING WAS DELETED -- the truncated version keeps its id and simply holds no stage, consistent with this order's standing rule that no version deletion is scheduled inside this face. RotationEnabled remains unset and DeletedDate remains absent on both secrets, re-read after every act.

=== THE SWITCH ITSELF, VERIFIED ON THE SERVED STATE ===

opal/auth/jwt-private-key AWSCURRENT = 579af491, 1703 bytes, raw text byte-equal to the local newpriv.pem, public half SPKI DER cb550976f5907f9f... -- equal to newpub.pem and to the envelope's CURRENT slot, which is the property that makes the switch safe rather than merely done. Shape is a BARE PEM, single CURRENT: TO-OP-S-10E's rationale is correct for THIS read, and Z-S160 was only ever about the PUBLIC one. It is also the shape-PRESERVING choice, since the secret already held a bare PEM.

=== CONDITION 5: THE SIGNER OBSERVED, NOT INFERRED ===

Instrument: POST /auth/refresh returns an accessToken minted by generateAccessToken -> getJwtPrivateKey, so it is signer output by construction; its signature is then verified LOCALLY against the two public halves. No verifier enters the reading.

  BEFORE (00:56:01Z, pre-write): minted token signed by OLD key [oldpub=true  newpub=false]
  AFTER  (01:16:32Z, post-fix ): minted token signed by NEW key [oldpub=false newpub=true]
  CTL at both vintages: a refresh token signed by a key in NEITHER slot -> 500, REFUSED.

The before/after flip on the SAME instrument with the CTL holding at both ends is the convergence evidence. The baseline is what makes it meaningful: without the 00:56Z read, "signed by NEW key" would be consistent with a signer that had always used it. | CLOSED 20260910T012605Z |
| L5 | verify | THE OUTCOME BAR: the OLD-key token from L1 still verifies AFTER the switch, and a fresh token from the signer resolves to the NEW key. Negative control: a token signed by a key in NEITHER slot is REFUSED. Old material retrievable, no DeletedDate, RotationEnabled still unset | the three token outcomes + describe-secret | THE OUTCOME BAR HOLDS ON THE PRE-ACT ARTIFACT ITSELF, NOT ON A RE-MINTED STAND-IN. FWD-10 is a no-sign-out rotation and the strongest available evidence is the token that existed BEFORE any secret was written, unchanged on disk, still accepted after the switch.

=== [A1] THE LOAD-BEARING ARM: the LITERAL L1 token, 01:21:40Z ===

old_refresh.jwt was signed at iat 1788999196 (00:13:16Z) with the OLD private key, BEFORE the envelope write and long before the signing switch, and has not been touched since. Its 7-day lifetime (exp 1789603996, 600696s still to run) is exactly why it survives as evidence where the 15m access tokens could not.

  presented to POST /auth/refresh at 01:21:40Z, AFTER the switch
  verified locally as OLD-key-signed: true
  -> HTTP 404 {"error":"User not found"}

"User not found" IS THE ACCEPT. It is L1's pre-act baseline discriminator, unchanged: the signature VERIFIED and the request then failed at the user lookup because the sub is a fabricated opaque binding with no row. The REJECT answer on that same axis is {"error":"Internal server error"}, and that is what a token signed by a key in neither slot returns -- measured again below. So a session minted before the rotation still authenticates after it. S10-AC3 is satisfied on the original artifact.

=== [A2] A REAL SESSION CROSSING THE SWITCH, END TO END ===

  OLD-key refresh for an ACTIVE account -> HTTP 200, and the minted accessToken verifies
      [oldpub=false newpub=true] -- signed by the NEW key
  CTL-key refresh (neither slot)        -> HTTP 500, REFUSED

That is the whole rotation in one exchange: a client holding a PRE-ROTATION refresh token is admitted, and is handed a fresh access token signed by the POST-ROTATION key. Nobody is signed out and nobody is left holding a key the estate no longer uses.

=== [B] ALL FOUR ARMS, EVERY CONSUMER, POST-SWITCH -- with the EXP arm kept, per the issuer ===

  auth-validator-edge + opal-portal-authorizer   GET /v1/market/rsi
      NEW (current slot)          -> 200   ACCEPTED
      OLD (previous slot)         -> 200   ACCEPTED   <- the no-sign-out bar at the edge
      CTL (neither slot)          -> 401   REFUSED
      EXP (old key, but EXPIRED)  -> 401   REFUSED
      no bearer                   -> 401   [reachability control]

  opal-session-analytics                          direct invoke, /sessions
      NEW -> 400 "user or date parameter required"  ACCEPTED (past requireAdmin -> verifyAuth)
      OLD -> 400 "user or date parameter required"  ACCEPTED
      CTL -> 401 Unauthorized \| Invalid token       REFUSED
      EXP -> 401 Unauthorized \| Invalid token       REFUSED

  opalinvest-auth-handler VERIFY path             POST /auth/refresh -- [A1] and [A2] above

WHY THE EXP ARM IS STILL HERE AND WHY IT MATTERS MOST IN THE AFTER-TEST. EXP is the correct OLD key with exp in the past. It returns bytes IDENTICAL to CTL. That is the point: it separates "the old key no longer verifies" -- which would be a rotation failure -- from "my fixture expired again", which is what manufactured a false single-slot finding at 00:29Z and would have halted this rotation on a defect that did not exist. In the after-test that confusion would have been the most expensive: an expired fixture reading as a broken rotation invites a rollback of a correct act. The arm is carried so the record MEASURES the separation rather than asserting it.

=== [C] NOTHING WAS DELETED AND NOTHING WAS ARMED ===

  opal/auth/jwt-private-key   RotationEnabled None   DeletedDate None
      1acd44f3-d07e-486b-9ad8-66993a0b6716  2026-01-04T04:53:25.550Z  AWSPREVIOUS  (the rollback)
      5bc63c94-7d91-4deb-b622-7ae0f8e71935  2026-09-10T01:09:42.364Z  (no stage)   (the truncated
                                            write from L4 -- retained, unlabelled, NOT deleted)
      579af491-ab27-4463-978d-b076cd5ce44a  2026-09-10T01:13:34.378Z  AWSCURRENT   (NEW_PRIV)

  opal/auth/jwt-public-key    RotationEnabled None   DeletedDate None
      fabe94f0-019d-455d-8c72-47b3d709bd8b  AWSPREVIOUS   (the pre-rotation bare PEM)
      01cfa582-621c-4fff-a320-44cbafa2ccc8  AWSCURRENT    (the {current, previous} envelope)

The OLD material is retrievable on BOTH secrets, no scheduled deletion exists on either, and RotationEnabled is unset on both -- re-read after every act of this order, not carried forward from the L1 baseline. S10-AC5 and deliverable 4's standing prohibition are satisfied as measured state.

ROLLBACK, STATED AS IT NOW IS RATHER THAN AS THE TITLE ASSUMED: a stage move restores a VALID key again, because L4 moved AWSPREVIOUS off the truncated version. Had that not been caught, the documented recovery path would itself have been an outage. | CLOSED 20260910T012605Z |

## Log

- 20260910T001238Z OPENED by 0.7.0_AE_CloudOps~V with 5 leg(s)
- 20260910T001700Z LEG L1 closed: PRE-ACT CAPTURE COMPLETE, AND THE BASELINE IS A REAL DISCRIMINATOR RATHER THAN AN ASSUMPTION.

THE KEYPAIR: a new RSA-20
- 20260910T001700Z LEG L2 closed: THE VERIFICATION ENVELOPE IS PUBLISHED AND SIGNING HAS NOT MOVED.

opal/auth/jwt-public-key was a BARE PEM (450 bytes, o
- 20260910T005120Z LEG L3 closed: ALL FOUR CONSUMERS SERVE THE ENVELOPE AND ACCEPT BOTH SLOTS, EACH READ SEPARATELY, ALL BEFORE SIGNING MOVES. AND THE FIR
- 20260910T012605Z LEG L4 closed: SIGNING IS SWITCHED AND THE SIGNER WAS OBSERVED CONVERGING. AND THE FIRST WRITE OF THIS LEG SILENTLY TRUNCATED THE PRIVA
- 20260910T012605Z LEG L5 closed: THE OUTCOME BAR HOLDS ON THE PRE-ACT ARTIFACT ITSELF, NOT ON A RE-MINTED STAND-IN. FWD-10 is a no-sign-out rotation and 
- 20260910T012637Z CLOSED -- all 5 legs proven
