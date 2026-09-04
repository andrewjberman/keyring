# Session log -- 0.7.0_AE_CloudOps~Z -- 2026-09-03 2245-2359Z

**Archetype:** MEASURE-THEN-EXERCISE (a security-coverage measurement whose only build is
a reversible IAM deny used to create the condition under test, applied and reverted in one
window). **Scope:** NFRA_OPSEC202609 ONLY (Rule 27). **TO:** `NFRA_OPSEC202609.TO-OP-S-7`
(FWD-7), all five criteria, the proof and the complete flip.

---

## THE QUESTION, AND WHY IT IS NOT "MAKE IT FAIL CLOSED"

`throttle.ts` fails OPEN on a DynamoDB error BY DESIGN -- a rate limiter that takes down
login on a table blip converts bookkeeping loss into an outage, a WIDER door than FWD-7 is
about. Making it fail closed is a STOP, not a deliverable. The face's question is: while the
throttle is failing open, WHAT ELSE holds the login path, and is it enough?

## WHAT HOLDS THE PATH -- MEASURED, NOT RECALLED

- **The throttle** (`throttle.ts` @775dc28917) is ACCOUNT-keyed (sha256 of the submitted
  email), threshold **5**, in DynamoDB. THREE fail-open enforcement sites, not the cell's
  one: `:112` GetItem, `:147` UpdateItem, `:164` set-block. It cannot see the client IP --
  `:14` -- because `/auth/*` forwards no `CloudFront-*` headers, which is an upstream cause,
  not this file's defect.
- **The WAF `AuthLoginRateLimit`** (`opal-cloudfront-protection` p2, Action Block) is
  IP-keyed, **Limit 100 / 300s**, scope-down `/auth/login` + `/auth/forgot-password` +
  `/auth/reset-password` (decoded from the rule's own ByteMatch). **LIVE-associated** with the
  serving distribution: `get-distribution EVTSA9VEHNZVH` reads the ACL ARN as its `WebACLId`,
  and `/auth/*` is a live behavior. A rule that exists but is not attached protects nothing --
  so the association was read, not assumed.

**The two controls have DISJOINT dependencies:** the throttle needs DynamoDB; the WAF, at the
edge, does not. So a throttle-bookkeeping failure cannot widen the WAF's door -- which is
exactly FWD-7's bar.

## THE EXERCISE -- the discriminating pair, on the real fail-open condition

The face wanted this EXERCISED, not inferred, and pre-authorised a reversible IAM deny to
create the "throttle blind" condition. Ledger `opsec-s7-throttle-failopen-coverage` opened
first; a **GetItem-only** inline Deny added to `opalinvest-auth-lambda-role`
(`simulate`: GetItem explicitDeny, UpdateItem still allowed -- surgical); exercised; deleted
in the same window (`simulate`: GetItem allowed again, with a non-held-table control).

- **Throttle HEALTHY:** 8 POSTs to a fabricated non-account -> 401x5 then **429** at #6. The
  door is held by the throttle (Lambda JSON, at threshold 5), WAF counter ~8 so not the WAF.
- **Throttle BLIND:** the identical burst, 120 POSTs -> **120x401, ZERO 429** -- the throttle
  never blocks, because its GetItem is denied and `:112` fails open. Then, after WAF
  rate-aggregation, 60 POSTs -> **60x403 from CloudFront** (edge HTML, not Lambda JSON) --
  the WAF blocking at its IP threshold WHILE the throttle is blind.

**Both conditions block; the CONTROL differs (throttle 429 vs WAF 403); the second blocks
with the throttle unable to read its table.** FWD-7 SERVED by measurement.

## WHAT I GOT RIGHT BY REMEMBERING A PRIOR LESSON

- **The WAF did not trip on the first 120-request burst.** AWS rate-based rules aggregate
  over a trailing window and engage with a lag; the burst finished at 401 before the block
  engaged. I did not read that as "the WAF doesn't cover it" -- I sent a follow-on burst once
  the trailing count was aggregated above 100, and it 403'd throughout. The lag is an
  instrument property; the block's OCCURRENCE is the stable fact, its exact request index is
  not, and the proof claims only the occurrence.
- **Every IAM step was simulate-verified on the applied plane with a control run as a SEPARATE
  invocation** (per /cloud-ops 22a: one `--resource-arns` per call, positive control isolated
  from the target so mode-1 implicit-deny cannot disarm it).

## LEFT EXACTLY AS FOUND

`throttle.ts`: `git diff --stat HEAD` empty, 0 changes -- READ, never edited. Auth-handler
tree clean. Role back to its original four inline policies. **Functional re-confirmation:** a
fresh 8-request burst after the revert **429s at #6 again** (throttle restored end-to-end, not
just in the policy document). The WAF rate-state on the probe IP was transient -- a 3-request
probe between revert and re-confirm returned 401, not 403 -- so no standing block was left.

## THE HONEST EDGE (S7-AC4 residual, not remediated)

The WAF bounds an attacker to 100 login attempts per IP per 5 min but enforces no per-ACCOUNT
bound during the fail-open window, so a distributed low-per-IP stuffing run against one account
is loosely bounded when the throttle is blind. This is a NARROWER door than "no limit," so it
does not violate FWD-7's "never wider" bar; it is stated as the edge of the coverage, and no
remedy is invented in this measurement face.

## STATE AT CLOSE

Proof VALID rc=0 on S7-AC1..AC5. Face flipped complete. Ledger CLOSED 4/4, none in
`.open_deploys/`. No source changed; no standing IAM change; login path as found. **PUSH
STATE: LOCAL** (`origin/SITEZ` at `001709c96e` by ls-remote; commits LOCAL by is-ancestor,
origin tip ON-ORIGIN as the positive control). **NEXT:** `TO-OP-S-10` (signing-key rotation --
first deliverable is a gate: if either consumer is single-slot, that finding IS the
deliverable), then `TO-OP-S-12` (its first limb is STALE -- gateway access logs are ON since
OP-s-5; verify, do not rebuild, and claiming to build it is an explicit S12-AC1 FAIL).
