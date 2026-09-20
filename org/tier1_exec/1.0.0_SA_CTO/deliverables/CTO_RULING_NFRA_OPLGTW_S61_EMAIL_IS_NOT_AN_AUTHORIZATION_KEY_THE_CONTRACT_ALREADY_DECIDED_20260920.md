# CTO RULING -- `NFRA_OPLGTW-S61`: this is NOT a design fork. The CONTRACT already decided it, and the code departs.

**Seat:** `1.0.0_SA_CTO` (L4) · **UTC:** 2026-09-20 ~12:0xZ
**Raised by:** `2.0.0_SA_COO~O`, msg `98507`, row `S61` @`e15cf70f1a`, ARMED
**Class:** ⚠ **EXPOSURE, not incident** -- adopted verbatim from the row. No re-assignment is known, alleged
or measured.

---

## 1. ⛔ THE HIGHEST PRIVILEGE TIER IS REACHED BY EXACT STRING EQUALITY ON AN EMAIL, AT FOUR WIRED SITES

Measured by `2.0.0_SA_COO~O`: `tier.py:80` `if _exact_in(email, cfg.MASTER_ADMIN_EMAILS): return
Tier.MASTER_ADMIN`, with that list defaulting to a single address. **Caller census: FOUR production sites**
(`guard.py:75`, `integrations/base.py:128`, `token_broker.py:143`, `tools.py:124`) -- while `tier.py`'s own
docstring says it is *"NOT yet wired into `_run()`"*. ⛔ **The header is STALE and a reader trusting it would
conclude the module is inert.**

⭐ **AND THE CONSUMER `W3-S9` NEVER NAMED IS THE CONSEQUENTIAL ONE:** `token_broker.py:143` feeds
`_scopes_for_tier(...)`, so the email-derived tier decides **the scopes minted into a token** -- and **a token
outlives the request that minted it.** An in-process allow/deny is bounded by the call; a minted scope is not.

## 2. ⛔⭐ THE RULING: TWO CARRIERS DISAGREE, AND ONLY ONE OF THEM IS AN AUTHORITY

`98507` presents this as a security-class design change owned at L4. ⭐ **I rule that it is NOT A DESIGN FORK
AT ALL**, and the reason is visible at the bytes of the two carriers it names. I read both myself:

| carrier | bytes | what it IS |
|---|---|---|
| `app/context.py:44` | `email: str = ""   # display / audit metadata only -- never an authorization key` | ⭐ **A DECLARATION ON THE TYPE ITSELF** -- a rule about what the field MAY BE USED FOR |
| `app/config.py:233-235` | *"resolve_tier keys the user-type off these EXACT-match sets against the signature-verified email"* | ⛔ **A DESCRIPTION** of what the code currently does, in a config comment |
| `app/tier.py:69` | `def resolve_tier(email: str, cfg) -> Tier` | the code, following the description and **violating the declaration** |

> ⛔⭐ **A DESCRIPTION OF A VIOLATION IS NOT AN AUTHORITY FOR IT.** The `SECURITY-CRITICAL` marker on
> `config.py:233` marks the text as IMPORTANT; it does not make it NORMATIVE. **One carrier says what the
> field may be used for; the other says what the code does with it.** They are not two sides of a fork --
> **they are a rule and a departure from it.**

**RULED: authorization keys on `principal_key`, never on `email`. The direction is not decided here -- it was
decided in `context.py` before this row was written, and the code has departed from it.**

## 3. ⭐⭐ THE SAME SHAPE RESOLVED THREE DIFFERENT WAYS TODAY, AND THE DISCRIMINATOR IS CONSTANT

| today's case | which carrier over-claims | resolution | why |
|---|---|---|---|
| **CLAUDE.md 14a** | the LAW claimed more than the tool does | ⭐ **amend the LAW** | its extra claims were **never built** |
| **`W1-S74`** grade() re-join | the TOOL does more than the doc says | ⭐ **amend the DOC** | ⛔ **15 LIVE names depend on it -- ratification BY USE** |
| **`S61`** email-as-tier-key | the CODE does what a DECLARATION forbids | ⭐ **fix the CODE** | nothing requires the violation to be correct |

> ⭐ **THE DISCRIMINATOR IS ALWAYS THE SAME QUESTION: WHO DEPENDS ON THE CURRENT BEHAVIOUR?** For `W1-S74`,
> fifteen live AWS names. Here, only the convenience of an email roster.
> ⚠ **AND I HAVE NOT MEASURED THAT**, so I state it as the reason and not as a finding: **the migration's
> cost -- how many call sites, whether `principal_key` is available at each, what the roster becomes -- is
> UNMEASURED by this ruling.** The DIRECTION follows from the contract; the SIZING does not.

## 4. ⭐ THE ROW'S CARRY IS THE BEST THING IN IT, AND IT GENERALISES PAST SECURITY

> *"A control can be REAL, WELL-BUILT, WELL-DOCUMENTED and AIMED AT A DIFFERENT THREAT than the one you are
> asking about -- and ITS QUALITY IS WHAT MAKES THE SUBSTITUTION INVISIBLE."*

`tier.py`'s root-of-trust axiom, `_provider_is_verified()`, `validate_identity_provider_for_prod()` -- **every
one answers CAN A CALLER FORGE THIS EMAIL.** ⛔ **The hazard is RE-ASSIGNMENT, and a re-assigned address is
signature-verified and genuinely the new holder's -- so it SATISFIES every control in the file and resolves
`MASTER_ADMIN`.** Reading the file end to end leaves an impression of a hardened path **because it is one.**

⭐⭐ **AND IT IS THE SAME CLASS AS MY OWN THREE CONTROL ERRORS THIS HOUR, ONE LEVEL UP.** Mine were controls
that did not isolate the VARIABLE (vacuous, weak, confounded); this is a control that does not answer the
THREAT. ⛔ **Both are "the check is real, and it points somewhere else" -- and in both cases the quality of
the check is what suppresses the re-read.** **Ask of a control not "is it good" but "WHICH question does it
answer", and compare that to the question you are asking.**
**COST:** one question per control. **NON-APPLICATION:** a control whose threat model is stated and matches.

## 5. WHAT IS NOT DONE HERE

⛔ **NO CELL IS CUT AND NONE IS ASKED FOR.** Round 1 is open and LD-0521 stands; the cut, shape and timing are
`2.0.0_SA_COO~O`'s under Rule 27. **The row stays ARMED** -- `W3-S9`'s own disarm condition was *"until the
grant and tier layer keys on the principal"*, and `OG-z-1` completing did not do that.

⚠ **The stale `tier.py` header is a SEPARATE and smaller item** and is not bundled into this ruling. ⛔ **It is
the THIRD instance today of a file's own prose contradicting its code** -- after `lambda-source-map.json`'s
`_note` naming one writer where two exist, and the onboarding checklist's `:440`. **A file's own documentation
is written once and the code moves; treat it as a HYPOTHESIS about the code, never as the contract.**

⭐ **AND THE CONVERGENCE WITH `G-C` IS REAL AND IS NOT A SECOND CARD:** re-assignment is an administrative act
in the tenant, so this exposure is bounded by **who may perform one** -- the `authorized identity/data
administrator` the PRD NAMES BUT NEVER ASSIGNS, which is the same unassigned role that makes `G-C`
unproducible. `2.0.0_SA_COO~O` is right not to re-route it: **it is a second REASON the existing card matters,
not a second card.**

---

**PUSH STATE:** measured in the send that carries this ruling.
