# CTO ADJUDICATION -- NFRA_OPSEC202609, C-4 (the partner-egress ALLOW list)

**Seat:** `1.0.0_SA_CTO~Z` (L4 owner) · **UTC:** 2026-09-04 ~13:45Z
**Routed by:** `2.0.0_SA_COO~Z` (msg 20414), on `0.7.0_AE_CloudOps~W`'s record @`c6da666116`
**Sovereign input:** Andrew ~13:2xZ, verbatim ->

> "The IPs we'd block wouldn't be opal or partner firm users. So i don't fully understand the
> question on that. The ones we definitely would not block would be opal users and opal partner
> users."

`2.0.0_SA_COO~Z` asked that whoever rules RE-DERIVE the figures rather than take them from the
relay. That was the right condition and it changed the answer twice.

---

## 1. WHAT I RE-DERIVED, AND THE TWO CORRECTIONS IT FORCED

### CORRECTION 1 -- THE ARITHMETIC MEASURED A DIFFERENT CONTROL FROM THE ONE C-4 GUARDS

The routed argument: *the sign-in rule needs 100 attempts in 5 minutes, the estate produced two
sign-ins in twenty days, therefore no Opal or partner user could trip it, therefore the allow list
protects against a collision that cannot occur.*

**The 100-in-5-min figure is CORRECT and I confirmed it on the applied plane** --
`AuthLoginRateLimit` on `opal-cloudfront-protection`: `Limit 100`, `EvaluationWindowSec 300`,
`AggregateKeyType IP`, `Action Block`, scoped down to three paths (base64-decoded: `/auth/login`,
`/auth/forgot-password`, `/auth/reset-password`). The general rules read `2000 / 300s / Block` on
both ACLs.

⛔ **BUT THAT IS A WAF RATE RULE, AND C-4 DOES NOT GOVERN IT.** C-4 read at source
(`PRD:392-398`): the ALLOW list is one *"that an automatic block can NEVER override ... populated
from MEASURED sign-in addresses per firm BEFORE **the sentinel is armed to BLOCK**"*, binding
`FWD-14`, violated by *"arming BLOCK with 0 ALLOW rows"*. **C-4 guards the SENTINEL's automatic
BLOCK rows.** A rate rule blocks by itself and consults no allow list.

**This is the project's own recurring class -- a measurement true on one plane, offered as
certification of another.**

### CORRECTION 2 -- AND THEN MY OWN, WHICH RAN THE OTHER WAY

`opal-sentinel`'s live config reads `SENTINEL_TRIP_THRESHOLD = 3`. **I first read that as three
failed logins and was about to rule that the collision C-4 prevents is not merely possible but
likely.** That would have been badly wrong.

Read at source -- `infra/aws/lambda/opsec/opal-sentinel/lambda_function.py:215` and its comment:

```
    if hits < TRIP_THRESHOLD:
        # C-3: a persistent block needs MORE than one rate trip.
```

**`hits` counts WAF RATE TRIPS, not requests.** So the COMPOSED bar for one automatic block is
**three separate rate trips** -- i.e. 100+ auth requests inside a 5-minute window, three times over.
Not 3 requests. Roughly 300+ auth requests across three distinct windows.

⭐ **So the arithmetic argument SURVIVES, and survives more strongly than as routed** -- but only
once composed across both controls. Neither the relay (which measured the rate rule and attributed
the conclusion to C-4) nor my first reading (which measured the sentinel and misread its unit) had
it right alone.

### WHAT THE TRAFFIC ACTUALLY SHOWS

`AuthLoginRateLimit` `BlockedRequests`, 20-day window, CloudWatch:

```
  total blocked                       60
  distribution                        ALL 60 on ONE day, 2026-09-03
  positive control (Rule=ALL, same query shape)   700   -> the shape works; the numbers are real
```

My first query returned empty for every series INCLUDING its control -- the dimension set is
`WebACL` + `Rule` with **no `Region` dimension**, so the query matched nothing. A zero whose control
also reads zero certifies nothing, and it was discarded rather than believed.

**The rule has fired exactly once, in a single burst, on the day this project was actively probing**
-- consistent with `2.0.0_SA_COO~Z`'s independent finding that 97.8% of the observable window is our
own probes. **No legitimate user has ever come close, and neither has any attacker on this rule.**

---

## 2. THE FAIL-SAFES ALREADY IN CODE -- WHICH THE FORK'S OPTION (c) DID NOT ACCOUNT FOR

`decide()` refuses a BLOCK on **three independent grounds**, and the ALLOW check is ordered first:

1. `is_allowed()` short-circuits to `WATCH` -- *"no threshold and no arming flag can override it"*,
   checked on BOTH carriers (file and table), either one sufficing, failing safe by construction.
2. `if not BLOCK_ARMED: return "WATCH"` -- and `SENTINEL_BLOCK_ARMED` reads **`false`** live.
3. `if not allow_list_present: return "WATCH"` -- **C-4 IS ENFORCED IN CODE, NOT ONLY IN THE
   CONSTRAINT TEXT**: *"Refused in code as well as in configuration, so that a single careless
   variable flip cannot produce the violated state."*

⛔ **Option (c) of the routed fork -- "relax C-4 and arm without a list" -- is therefore not merely
forbidden by C-4's wording; it is UNREACHABLE without a code change.** Anyone electing it is
electing to edit the sentinel, and that should be said out loud rather than discovered.

---

## 3. THE RULING

**C-4 STANDS, AND ITS UNSATISFIABLE CLAUSE IS AMENDED.** Andrew's sentence contains two acts and the
ruling honours both.

**(i) HIS QUESTION -- "is the list needed?" -- is answered ON THE MEASUREMENT, and he is right on the
merits.** At a composed bar of three rate trips, an Opal or partner user tripping the sentinel is not
a realistic scenario on any evidence the estate holds. The allow list is NOT load-bearing as
collision-prevention.

**(ii) HIS INTENT -- "the ones we definitely would not block would be opal users and opal partner
users" -- is the operative half, and it is satisfiable TODAY.** It does not require the per-firm
census C-4 currently demands.

**AMENDMENT.** C-4's clause *"populated from MEASURED sign-in addresses per firm"* is **STRUCK and
replaced with**: *"non-empty, carrying Opal's own known egress addresses (office / VPN), supplied by
a named human."*

⛔ **THE STRUCK CLAUSE IS UNSATISFIABLE BY CONSTRUCTION AND THAT IS MEASURED, NOT ASSERTED** -- from
the sentinel's own `SENTINEL_COVERAGE_BOUND`: *"any request body, so NO firm attribution is possible
from this source at all."* `OP-s-5` redacts the Cookie header by deliberate design. **A constraint
that requires per-firm address attribution from a source that cannot attribute is a constraint no
lane can ever discharge**, and `Z-S90` already measured the cost of trying: a naive census over
111,904 records would have ALLOW-LISTED a Moldovan scanner into the control C-4 exists to protect.

**WHAT SURVIVES UNCHANGED:** the never-override property, the both-carriers check, the arming
precondition, and the violation *"a BLOCK row on an ALLOW-listed address"*. The list stays a real
gate; it stops pretending to be a census.

**WHY NOT OPTION (b)** (*"never block a request carrying a valid login"*): it does not work on this
surface. The rate rule's scope-down is exactly the three UNAUTHENTICATED `/auth/*` paths -- **a user
signing in has no session by construction**, so an identity-based exemption has nothing to test
there. It is a sound idea aimed at the wrong control; it would apply to the general 2000/5-min rule,
which is not what C-4 guards.

---

## 4. WHAT THIS UNBLOCKS, AND THE ONE THING IT DOES NOT

`OP-s-14`'s BLOCK arm was held on a chain -- no clean window, no allow list, no C-4, no BLOCK arm.
**The chain's first link is now a one-line human input rather than an unbuildable census**, so
`2.0.0_SA_COO~Z` may sequence the cell.

⛔ **IT DOES NOT SELF-EXECUTE, AND THE RESIDUE IS ANDREW'S:** somebody must supply Opal's office /
VPN egress addresses. They are not derivable from any log -- that is the whole finding -- and this
seat does not know them. **That is a one-line answer from him or from whoever administers the
network, and it is the only thing standing between here and an armable BLOCK.**

**NOT RULED HERE:** whether BLOCK should be armed at all, and the managed-rule-group COUNT->BLOCK
graduation, which `0.7.0_AE_CloudOps~W` correctly identified as the real residual exposure and a
separate decision with its own moment.

**BOUND ON THIS RULING:** I re-derived the rate-rule thresholds, the sentinel threshold and its
unit, the 20-day block distribution with a positive control, and the sentinel's decision order at
source. I did NOT re-derive the "two sign-in events in twenty days" figure, the 23-user / 4-firm
partner population, or `Z-S90`'s 111,904-record census -- those remain `0.7.0_AE_CloudOps~W`'s
measurements, cited and not re-taken, and the ruling does not rest on them.


---

# AMENDMENT 2026-09-04 ~17:2xZ -- SECTION 3's REMEDY IS STRUCK. IT WAS THE SAME AXIS.

**Cause:** Andrew-direct ~16:5xZ, /open-calls Card 1 (record: `0.0.0_AB_MSTR~Z` msg 20469), verbatim:

> "there are none is probably the best we can do at this time. The issue is that there are really
> just are no stable IPs. There are opal users who don't... who do not even come to the office. So
> it's just not really viable to approach it that way."

## WHAT THIS RULING GOT WRONG

Section 3 struck *"populated from MEASURED sign-in addresses per firm"* as unsatisfiable by
construction -- **that half stands** -- and replaced it with *"non-empty, carrying Opal's own known
egress addresses (office / VPN), supplied by a named human."*

⛔ **THE REPLACEMENT IS THE SAME AXIS.** The defect was never that the partner half could not be
MEASURED; it is that **SOURCE ADDRESS is not a property this population has**. I diagnosed an
unmeasurable census and prescribed a smaller census on the identical axis. The card I sent even
carried the escape hatch -- *"'there are no fixed addresses' is an equally usable answer"* -- and the
remedy still assumed there were some. **A rec can name the fact that refutes it and still be wrong.**

## AND THE OBVIOUS REPLACEMENT FAILS TOO -- THE COMPOSED FINDING

Re-deriving on IDENTITY rather than origin is the natural read, and msg 20469 assigns it here and to
`2.0.0_SA_COO~Z`. ⛔ **It cannot live in the sentinel.** From `SENTINEL_COVERAGE_BOUND`, live on the
function: *"...and any request body, so NO firm attribution is possible from this source at all."*
`OP-s-5` redacts the Cookie header by design, and `is_allowed(address, allow_list)` is address-keyed
in code.

⭐ **SO THE AUTOMATIC BLOCK CANNOT BE ARMED SAFELY ON EITHER AXIS: the axis the sentinel CAN see does
not identify our people, and the axis that WOULD is invisible to it.** Two correct decisions meeting,
not a gap. A never-block control belongs where identity is known -- the auth layer, not the WAF plane.

## AMENDED DISPOSITION

- **STRUCK:** the "Opal's own known egress addresses" replacement. C-4's list is not populatable on
  the address axis at all; no seat builds or applies one. The `Z-S90`-derived candidate list must NOT
  be applied (msg 20469, and because it would allow-list a Moldovan scanner).
- **RULED:** `SENTINEL_BLOCK_ARMED` stays `false`. The code's own `if not allow_list_present ->
  WATCH` fail-safe and this ruling now agree rather than one holding the other back.
- ⛔ **NOT RULED, AND DELIBERATELY NOT ABSORBED:** `FWD-14`'s automatic-block half is unreachable on
  the plane it was specified for. That is a **SCOPE_CHANGE at L2**, not a cell to re-cut at L6, and
  routing it is `2.0.0_SA_COO~Z`'s -- a ratified outcome should not be quietly narrowed from L4. The
  WATCH / case-file / evidence half of `FWD-14` is untouched and still delivers.

**UNCHANGED AND STILL LOAD-BEARING:** the composed rate bar (3 trips x 100-in-5-min) means no Opal or
partner user plausibly trips the sentinel anyway. **The exposure this closes is small; the wrongness
of the remedy was not.**
