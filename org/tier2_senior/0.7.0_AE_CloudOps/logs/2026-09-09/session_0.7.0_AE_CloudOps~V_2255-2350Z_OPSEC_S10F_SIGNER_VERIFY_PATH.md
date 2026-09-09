# Session log -- 0.7.0_AE_CloudOps~V -- 2026-09-09 2255-2350Z

## NFRA_OPSEC202609.TO-OP-S-10F: the signer's VERIFY path now holds two slots. The rotation's last blocker is cleared

**archetype:** DEPLOY

Sixth segment. Follows the third STOP (row `Z-S160`), which was against this lane's own
TO-OP-S-10E work and which the issuer accepted, naming the defect as its own criterion's.

## Outcome

`opalinvest-auth-handler` verifies with **two slots** and signs with **one CURRENT key**.
Proof-of-spec **VALID rc=0**, five of five; ledger CLOSED 5/5; TO `complete`. **Nothing rotated.**

| criterion | verdict |
|---|---|
| S10F-AC1 | PASS — baseline unmoved, single-CURRENT re-confirmed before the change |
| S10F-AC2 | PASS — **both halves**, graded as one |
| S10F-AC3 | PASS on the reachability limb; two-KEY limb **UNCOMPUTABLE-BY-CONSTRUCTION** |
| S10F-AC4 | PASS — refresh exercised through the cookie the route actually reads |
| S10F-AC5 | PASS — both secrets unchanged, 0 wafv2 |

## The phase-1 mandate, run as a table

The new obligation — enumerate every **read**, per read, and state what each is **used for** —
is what made the shape obvious rather than arguable:

```
private  getMfaCodeSealKey    -> HKDF input   (neither)
private  generateAccessToken  -> SIGNS
private  generateRefreshToken -> SIGNS
public   verifyAccessToken    -> VERIFIES
public   verifyRefreshToken   -> VERIFIES
```

All three private reads are non-verifying, so single-CURRENT stays. Both public reads verify,
so both get slots. No further role exists — which is the point of enumerating rather than
reasoning about the component.

## Three instrument failures, all mine, all caught

**1. A regex built on an assumed minified shape reported `verifyWithSlots` ABSENT** — a **false
FAIL on a correct deploy**. Re-run against literal markers with all seven `.previous`
occurrences enumerated, the result inverted. *A matcher built against a format you have not read
returns a clean zero, and on a minified bundle the format is never the one in your head.*

**2. My first refresh probe returned an answer byte-identical to its own control.** Two arms
agreeing is not evidence. Reading `extractRefreshToken` at source showed the token travels in a
`refresh_token` **cookie**, never the body.

**3. `Errors: 0` alongside two 500 responses** needed the distinction stated, not glossed: the
outer handler *returns* a 500 payload, so the invocation succeeds. A handled 500 and a Lambda
failure are different objects.

## The safest possible shape to land before a rotation

While `previous` is null the new path is **observably identical** to the old one — `jwt.verify`
threw `JsonWebTokenError` directly; `verifyWithSlots` now catches it, sees `previous` is null,
and rethrows **the same error object**. This deploy changes no behaviour until the envelope
exists. Confirmed on the wire: `JsonWebTokenError: invalid signature` on a bogus token.

## The mutant, and why it wasn't planted

Planting one would have meant deploying a knowingly defective signer to the live login path. It
wasn't needed — **the mutant already ran in production form**: TO-OP-S-10E deployed exactly the
single-rule-applied-to-both-roles artifact, its criterion graded PASS on accurate evidence, and
only re-grounding caught it. That *is* the control, and it is why S10F-AC2 grades the two halves
as one rather than ceremonially.

## Blockers

**None.** All four consumers are now correct: three verifiers two-slot, the signer bounded on
both reads and two-slot on the verify half. `TO-OP-S-10` remains barred pending the issuer's GO.
