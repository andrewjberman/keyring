# ANDREW-DIRECT 2026-09-04 ~13:2xZ -- NFRA_OPSEC202609 C-4, the partner-egress allow list

**Channel:** direct to `0.7.0_AE_CloudOps~W` at this terminal, in response to `/exec-sum` naming the
allow list as one of three items waiting on him.
**Recorded by:** `0.7.0_AE_CloudOps~W`. **Broadcast:** COO, CTO, MSTR, same turn.

## VERBATIM -- his words, not a paraphrase

> "The IPs we'd block wouldn't be opal or partner firm users. So i don't fully understand the question
> on that. The ones we definitely would not block would be opal users and opal partner users."

## WHAT THIS IS

Two things at once, and they should not be collapsed:

1. **A QUESTION** -- he does not accept the premise that an allow list is needed, on the reasoning that
   the addresses the framework would block are attackers and not our own people.
2. **A STATEMENT OF INTENT** -- if a never-block set exists, its members are **Opal users and Opal
   partner-firm users**. That is the population, in his words.

## WHY IT MATTERS TO C-4

C-4 requires `allowlists/partner-egress.json` and states that **arming BLOCK with 0 ALLOW rows is a
violation**. `TO-OP-S-20` is the face that would populate it and it is STOPPED at its own GO condition
(row `Z-S90`).

⛔ **HIS ANSWER NAMES AN IDENTITY SET AND C-4 NEEDS AN ADDRESS SET, AND NOTHING MAPS ONE TO THE OTHER.**
That is the whole difficulty and it is not a quibble:

- The WAF log's `Cookie` header reads **REDACTED**, by `OP-s-5`'s deliberate design, so the security
  log is not the estate's largest bearer-token collection. Nothing in the source attributes an address
  to a firm or a user.
- `Z-S90` measured the consequence: a naive census to derive the list returned **60 distinct addresses
  topped by a Moldovan scanner at 2,357 hits**. Building the list from logs would have ALLOW-LISTED AN
  ATTACKER into the very control C-4 exists to protect.
- All four partner firms would file "log coverage unknown" -- **0 of 4 observed**.

## AND THE NUMBERS SUPPORT HIS INSTINCT, WHICH IS THE PART WORTH CARRYING UPWARD

Measured, not asserted:

| | |
|---|---|
| sign-in rate rule | **100 requests / 5 min / IP**, scoped to the three `/auth/*` paths |
| general rate rule | **2,000 requests / 5 min / IP** |
| actual sign-in traffic | **2 events in 19.7 days** across 111,904 WAF records |
| partner firm population | **4 firms, 23 users total** (11 / 4 / 7 / 1) |

**To be auto-blocked by the sign-in rule, one address must make 100 sign-in attempts in five minutes.
The entire estate produced two in twenty days.** A partner firm behind a single office address tripping
that through normal use is not a realistic scenario, and his reading that the blocked set and the
partner set do not overlap is quantitatively supported on this evidence.

**The residual exposure is NOT the rate rules.** It is the managed rule groups -- a false positive on
common-rule-set or known-bad-inputs flagging a legitimate request. Those currently sit in COUNT, so
they refuse nobody today; the exposure appears only if they graduate to BLOCK.

## THE FORK THIS PUTS TO THE PROJECT -- his call, not this seat's

- **(a) A SHORT KNOWN LIST.** If Opal has fixed office or VPN egress addresses, those are supplyable in
  one line and are not derivable from any log. Partner advisors on home broadband are not.
- **(b) CHANGE THE CONTROL TO MATCH HIS SENTENCE.** Never block a request carrying a valid login --
  identity, not address, which is exactly what he said. This is a design change to the rule's
  scope-down, not an allow list, and it would make C-4's list unnecessary rather than unpopulated.
- **(c) RELAX C-4 AND ARM WITHOUT A LIST**, accepting the residual because the audited unblock path now
  exists and was exercised end-to-end on a real address this morning, with the recovery path
  deliberately not travelling through the thing being blocked.

⛔ **(c) IS CURRENTLY FORBIDDEN BY C-4's OWN TEXT** -- "arming BLOCK with 0 ALLOW rows" is a named
violation -- so taking it requires him to relax the constraint, not merely to proceed.

## BOUND ON THIS RECORD

This seat holds `TO-OP-S-10C` and does **not** own `TO-OP-S-20`, C-4, or the sentinel chain. Nothing
here is adjudicated: the verbatim is recorded, the measurements are cited, and the fork is routed. Per
`org/XXX.md`, the receiving agent surfaces and does not adjudicate scope.
