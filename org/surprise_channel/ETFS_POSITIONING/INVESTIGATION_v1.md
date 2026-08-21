# ETFS_POSITIONING (D4) -- SURPRISE CHANNEL INVESTIGATION v1

**Channel owner:** `3.0.0_SA_CVO~Z` · **Round:** v1 · **Opened:** 2026-08-21 ~19:48Z
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (stage 5) · CLAUDE.md Rule 27
**Subject:** the site-Z **L1 leg** -- `integrations/bloomberg/pipeline/etf_daily_pull.py`, appended to
the `OPAL_BBGTML_daily_pull` 07:00 chain @`49501d1e55`.
**Status:** APPEND-ONLY during this round.

⛔ **THIS DOCUMENT CREATES NO SITE-Z D4 STAGE-3 LEG.** `1.0.0_SA_CTO~Z` ruled D4's placement
LAPTOP (msg 4594, on Andrew's ~05:5xZ placement, latest-binds), and I am not reopening it. A
surprise item about a script that **runs on this box** is site Z's to surface; the shaping work
stays where placement put it. This seat remains on D7 stage 3.

⛔ **PROPORTIONALITY, STATED FIRST BECAUSE THIS IS THE SOVEREIGN PRIORITY ITEM.** Andrew-direct
~19:3xZ: *"I want ETFS_POSITIONING DONE RIGHT NOW. IT IS PRIORITY FOR THIS SESSION."* **Nothing in
this document blocks tonight, touches the 08/22-08/24 fires, or argues for slowing D4 down.** The
dated trigger is **2026-09-08**, ~2.5 weeks out. These were surfaced when measured, not because
they are due. *Manufacturing urgency on a priority item is its own failure mode, and inventing a
blocker here would be exactly that.*

---

## 0. WHAT WAS CERTIFIED FIRST -- the half that IS verifiable tonight

`0.0.0_AB_MSTR~Z` reported L1 as BUILT / DEPLOYED / ARMED. **Re-derived at the live primitive, and
their claims are exact:**

```
OPAL_BBGTML_daily_pull   State Ready | NextRun 8/22/2026 07:00 | LastRun 8/21 07:00:01 | LastResult 0
s3://opal-data-etfs/bbg/2026-08-20/      7 objects, run_manifest.json present
08/21 07:00 fire ran 11:00Z; the ETF leg landed ~14:47Z @49501d1e55
  -> that fire correctly does NOT count toward L1-2. First countable fire is 08/22.
```

**Idempotency checked and CLEAN.** I went looking for a double-append trap (the banked month-end
class) and there is none: the CLAMP at `:117-123` anticipates the already-current case explicitly
(*"Re-pulling one already-held day is idempotent; an empty or malformed request is not"*), and
writes are `s3.put_object` to deterministic keys -- **overwrite, not append.**

**`0.0.0_AB_MSTR~Z`'s refusal to compress L1-2 is correct and LAW-BACKED, not discretionary** --
CLAUDE.md: *"AN AD-HOC RUN IS NEVER THE PRODUCTION PATH, AND ITS ARTIFACTS ARE NEVER PRODUCTION
EVIDENCE."* Three manual fires would satisfy the letter of "three fires" and destroy what the
criterion measures, and the artifacts would be byte-identical downstream.

---

## 1. HOW THESE WERE FOUND -- and the false finding I nearly filed instead

**I first hypothesised the script had NO trading-calendar handling at all.** My pattern census
(`trading_calendar|expected_last_trading_day|weekday|weekend|holiday`) returned **`count = 0`**,
and a positive control on the same engine returned 14. **That count was TRUE and the verdict would
have been FALSE:** the script handles business days via `pd.tseries.offsets.BDay`, a token my
pattern set did not contain.

⛔ **THE POSITIVE CONTROL PROVED THE INSTRUMENT WORKED AND SAID NOTHING ABOUT WHETHER MY PATTERN
COULD MATCH.** That is CLAUDE.md Rule 21's exact shape -- *a case-miss returns a true denominator
while the frame certifies the sweep* -- and it would have produced a confident, well-formed,
entirely wrong finding on the sovereign priority item. **The findings below survive because reading
the source falsified my own hypothesis first.**

---

## 2. ITEM NARRATIVE

### S1 -- the as-of TRIPWIRE compares an expression to ITSELF and cannot ever fire

```python
:57  today    = pd.Timestamp.today().normalize()
:58  asof     = today + pd.tseries.offsets.BDay(-1)
:59  expected = (pd.Timestamp.today().normalize() + pd.tseries.offsets.BDay(-1))
:60  if asof != expected:  ->  log("TRIPWIRE REFUSED"); return 60
```

`asof` and `expected` are **the same expression**. They can differ only if the wall clock crosses
midnight between `:57` and `:59` -- a sub-millisecond race. Proven across four dates:

```
today 2026-08-22: asof=2026-08-21 expected=2026-08-21  tripwire_fires=False
today 2026-09-08: asof=2026-09-07 expected=2026-09-07  tripwire_fires=False
today 2026-11-27: asof=2026-11-26 expected=2026-11-26  tripwire_fires=False
today 2026-12-26: asof=2026-12-25 expected=2026-12-25  tripwire_fires=False
```

**The author's intent, in their own comment at `:54-56`, is exactly right:** *"A run that cannot
establish that refuses rather than landing under a wrong key -- a wrong date is worse than a missing
day, because a consumer cannot tell it is wrong."* **The implementation cannot deliver it.** This is
CLAUDE.md's named class -- SELF-COMPARISON, and *an instrument that COULD NOT HAVE SAID OTHERWISE*
-- and it is the one control positioned to catch S2.

### S2 -- `BDay` is holiday-blind, and diverges from the estate's canonical calendar

`BDay` is Mon-Fri only. Measured:

```
fire 2026-09-08 -> as_of 2026-09-07   *** Labor Day    -- MARKET CLOSED ***
fire 2026-11-27 -> as_of 2026-11-26   *** Thanksgiving -- MARKET CLOSED ***
fire 2026-12-28 -> as_of 2026-12-25   *** Christmas    -- MARKET CLOSED ***
```

`lib/trading_calendar.py` **exists, knows holidays, and disagrees**: canonical `2026-09-08` vs
BDay `2026-09-07`. CLAUDE.md NEVER#1 names that file as **the ONE frontier definition**.

⚠ **WHAT I HAVE NOT DETERMINED, AND WHY I AM NOT PRESCRIBING THE FIX.** The canonical function uses
a **different convention** -- it returned `2026-09-08` for a Tuesday fire (inclusive, *last trading
day <= date*) where `BDay(-1)` returns the strictly-previous business day. **This pipeline wants
T-1, so the canonical is not obviously a drop-in.** I established that they disagree and that BDay
lands on holidays. I did **not** establish the correct replacement expression. That is the owner's
call.

### S1 x S2 -- why they compose, and why they are filed separately

**Together they produce precisely the harm the author's comment names: on the first fire after a
market holiday the run lands data under a holiday key, and its own refusal mechanism passes it
green.**

Filed as two items under Rule 24(iv), because **the remedies deliver different things**:
- Repair **S1 alone** (compare `asof` against an *independent* oracle) -> the run **REFUSES** on
  2026-09-08 rather than landing bad data. That is the designed behaviour, and it is arguably
  sufficient on its own.
- Repair **S2 alone** (swap the date source) -> correct date, but the guard is **still dead** and
  the next date defect is undetected.

A single change *can* move both (point the tripwire at the canonical calendar), but that is a
remedy choice, not evidence they are one defect.

### S3 -- the 08/22-08/24 acceptance window has a static as-of (a READ risk, not a defect)

All three fires in L1-2's window resolve to the **same** as-of:

```
fire 08/22 (Sat) -> as_of 2026-08-21 (Fri)
fire 08/23 (Sun) -> as_of 2026-08-21 (Fri)
fire 08/24 (Mon) -> as_of 2026-08-21 (Fri)
fire 08/25 (Tue) -> as_of 2026-08-24 (Mon)   <- first advance
```

**This is CORRECT.** NEVER#1: *Friday's data IS the weekend's right answer*, and the runs are
idempotent. **The risk is entirely at the ACCEPTANCE READ:** whoever evaluates continuity across
those three runs sees a static as-of and can read a healthy pipeline as stalled. NEVER#1 is explicit
that a false outage is not a safe error -- *"it manufactures pressure to fix a pipeline that is
working, which is how a guard gets removed"* -- and given S1, **the guard most likely to be "fixed"
under that pressure is the BDay logic, which is the correct half.**

⛔ **INFERRED, NOT GROUNDED.** I could not locate L1-4's exact wording in
`docs/briefs/etfs-positioning-bloomberg-pull-20260821.md` (my grep returned nothing), **so I do not
know whether L1-4 expects the window to advance.** This is a read-risk conditional on that wording,
**not** an asserted criterion defect. It cannot seed a remediation row while INFERRED.

### S4 x S5 -- THE COUPLED EDGE: the remedy one item invites is the act that fires the other

Found by `0.7.0_AE_CloudOps~Z` (msg 4624) answering a bucket-configuration question **nobody had
asked** -- *"if `bbg/` is ever emptied"* was sitting inside another item as an untested premise.
Cross-item sequencing ruled by `1.0.0_SA_CTO~Z` (msg 4628), who directed this channel to **record
the edge on BOTH items, because an edge written on only one side is found only by whoever reads
that side.** That is why S4 and S5 below each carry it in full rather than one pointing at the other.

**S4 -- PROVENANCE.** Seven ad-hoc objects sit in the production prefix and **no reader can
distinguish them from a scheduled landing** (`0.0.0_AB_MSTR~Z` item 4). The tidy, locally reasonable
response is: delete the ad-hoc objects out of `bbg/`.

**S5 -- THE HARDCODED FLOOR.** If `bbg/` yields no prior day prefix, the producer takes the
`prior_end=None` branch and starts from a hardcoded `2026-08-21`. From a fire months later that is a
multi-month Bloomberg history request for the full universe **that nobody sized**.

⛔ **THE EDGE, RE-DERIVED AT THIS SEAT:**

```
bbg/ day prefixes            -> ["bbg/2026-08-20/"]   COUNT 1, IsTruncated null
objects under it             -> 7    (the ad-hoc land)
=> THE SEVEN AD-HOC OBJECTS ARE THE ENTIRE CONTENTS OF bbg/

source, etf_daily_pull.py:
  :99   prior_end = None
  :101  paginate day prefixes under PREFIX (correctly paginated)
  :105  skip d == asof_key            <- the CURRENT day never supplies prior_end
  :110  prior_end = manifest["history_window_end"]
  :119  if prior_end: incremental top-up   ELSE -> :116  start = Timestamp("2026-08-21")  FLOOR

=> bbg/2026-08-20/ is THE ONLY prefix supplying prior_end today.
   Deleting it takes the prefix count 1 -> 0 -> prior_end None -> the floor fires.
```

**So S5 is dormant precisely as long as S4's objects stay where they are.** Tracked separately with
the same owner and the same window, **a reader disposing of them one at a time discharges the
provenance concern and arms the floor in the same act, each step locally reasonable.**

**RULED (`1.0.0_SA_CTO~Z`): THE CLEANUP DOES NOT RUN BEFORE THE FLOOR IS ADDRESSED, OR THEY MOVE
TOGETHER.** *"A remedy that fires another item's trigger is not a remedy, it is a trade -- and the
trade is invisible if the two items are read separately."*

**AND THE TRIGGER CANNOT ARRIVE ON A TIMER** -- measured at this seat, stderr kept because an error
would itself be a value:

```
lifecycle   ONE rule: abort-incomplete-mpu-7d, Expiration NULL   -> expires NO objects
versioning  EMPTY response body                                  -> NEVER enabled
```

⛔ **THE VERSIONING READ IS THE HALF WORTH KEEPING, AND IT CLOSES A FALSE-ABSENCE CLASS.** An
**empty** response means versioning was **never enabled**; an enabled-then-disabled bucket returns
`Status=Suspended`. **Two states that render nearly identically and mean different things.** Because
versioning was never on, there are no delete markers -- **so a listing that reads empty means the
bucket IS empty, not that objects are hidden behind markers.** An empty listing over a versioned
bucket and over an unversioned one are the same characters and different facts.

⚠ **BOUND, carried from the filer unsoftened:** they measured **lifecycle and versioning**, not
every conceivable deletion path (an agent or human delete, a future TF change, a replication
reconfiguration). The claim is that **no STANDING configuration on this bucket deletes anything** --
which *lowers* S5's standing without closing it. **It stays ARMED: deliberate acts happen, and the
most likely deliberate act is the one S4 invites.**

---

## 3. MACHINE BLOCK

```json
[
  {
    "id": "ETFS_POSITIONING-S1",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-21T19:48Z",
    "one_line": "The as-of TRIPWIRE in etf_daily_pull.py compares an expression to itself (asof vs an identical re-computation) and can never fire -- the one control positioned to catch a wrong as-of is structurally incapable of catching anything.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/bloomberg/pipeline/etf_daily_pull.py:57-61 read at source -- asof and expected are the same expression",
        "exercised across 4 dates (2026-08-22, 09-08, 11-27, 12-26): tripwire_fires=False in every case",
        "differs only if the wall clock crosses midnight between :57 and :59, a sub-millisecond race",
        "author's own comment :54-56 states the intent the code cannot deliver: 'a wrong date is worse than a missing day, because a consumer cannot tell it is wrong'"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.0.0_AB_MSTR~Z",
    "notes": "CLAUDE.md's named SELF-COMPARISON class and 'an instrument that COULD NOT HAVE SAID OTHERWISE'. A passing assertion never mutated has never been tested; this one passes on every input. Trigger 2026-09-08 -- DOES NOT block tonight and does not touch the 08/22-08/24 fires. Comment-at-the-config-site disarm available today at zero risk (precedent: 0.5.0_AE_OpalETL~Z @a4b1981cd5). DISARMED != REMEDIATED."
  },
  {
    "id": "ETFS_POSITIONING-S2",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-21T19:48Z",
    "one_line": "etf_daily_pull.py derives its as-of from pandas BDay, which is Mon-Fri and HOLIDAY-BLIND, so the first fire after each market holiday lands the as_of ON the closed day -- and it diverges from lib/trading_calendar.py, which CLAUDE.md NEVER#1 names as the ONE frontier definition.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured: fire 2026-09-08 -> as_of 2026-09-07 (Labor Day); 2026-11-27 -> 2026-11-26 (Thanksgiving); 2026-12-28 -> 2026-12-25 (Christmas)",
        "lib/trading_calendar.py exists (6,979 bytes) and carries holiday handling",
        "canonical vs BDay on 2026-09-08: canonical 2026-09-08, BDay 2026-09-07 -- they disagree",
        "CLAUDE.md NEVER#1 names lib/trading_calendar.py as the ONE frontier definition"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.0.0_AB_MSTR~Z",
    "notes": "Composes with S1 into the harm the author's own comment names: the run lands under a holiday key AND its refusal mechanism passes it green. Filed separately from S1 per Rule 24(iv) -- repairing S1 alone makes the run REFUSE on 09-08 (designed behaviour, arguably sufficient); repairing S2 alone leaves a dead guard. ⛔ THE REPLACEMENT EXPRESSION IS NOT DETERMINED: the canonical uses an inclusive 'last trading day <= date' convention while this pipeline wants T-1, so it is not obviously a drop-in. I measured the disagreement, not the fix. Trigger 2026-09-08."
  },
  {
    "id": "ETFS_POSITIONING-S3",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-21T19:48Z",
    "one_line": "All three fires in the L1-2 acceptance window (Sat 08/22, Sun 08/23, Mon 08/24) resolve to the SAME as_of 2026-08-21, so a reviewer checking whether the window advanced can read a correct, idempotent pipeline as stalled.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "as-of computation measured: 08/22, 08/23, 08/24 all -> 2026-08-21; first advance is 08/25 -> 2026-08-24",
        "the behaviour itself is CORRECT per CLAUDE.md NEVER#1 and the runs are idempotent (CLAMP :117-123, put_object overwrite)",
        "L1-4's exact wording NOT LOCATED in docs/briefs/etfs-positioning-bloomberg-pull-20260821.md -- grep returned nothing, so whether it expects advancement is UNKNOWN"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "A READ risk, not a pipeline defect -- filed at that strength deliberately. INFERRED because the conditional half (what L1-4 requires) is unmeasured, so it cannot seed a remediation row. NEVER#1 is explicit that a false outage is not a safe error: it manufactures pressure to fix a working pipeline. Given S1, the guard most likely to be 'fixed' under that pressure is the BDay logic -- the correct half. Blocks a zero-graduation close on this round."
  },
  {
    "id": "ETFS_POSITIONING-S4",
    "surfaced_by": "0.0.0_AB_MSTR~Z",
    "surfaced_at": "2026-08-21T19:56Z",
    "one_line": "Seven ad-hoc objects sit in the production prefix bbg/2026-08-20/ and no reader can distinguish them from a scheduled landing -- and they are the ENTIRE contents of bbg/, so the cleanup this invites is the act that fires S5's floor.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "re-derived at this seat: list-objects-v2 bbg/ delimiter / -> CommonPrefixes ['bbg/2026-08-20/'], COUNT 1, IsTruncated null",
        "7 objects under that prefix, manifest present -- they are the entire contents of bbg/",
        "CLAUDE.md: an ad-hoc run is never the production path and its artifacts are never production evidence; downstream the objects are byte-identical to a scheduled landing"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.0.0_AB_MSTR~Z",
    "notes": "⛔ COUPLED TO ETFS_POSITIONING-S5 -- THE EDGE IS RECORDED ON BOTH ITEMS BY 1.0.0_SA_CTO~Z's DIRECTION (msg 4628): 'an edge written on only one side is found only by whoever reads that side.' The tidy remedy this item invites -- delete the ad-hoc objects -- takes bbg/ prefix count 1 -> 0, which sends the producer down the prior_end=None branch onto S5's hardcoded 2026-08-21 floor. RULED: THE CLEANUP DOES NOT RUN BEFORE THE FLOOR IS ADDRESSED, OR THEY MOVE TOGETHER. A remedy that fires another item's trigger is not a remedy, it is a trade. Found by 0.7.0_AE_CloudOps~Z asking a bucket-configuration question nobody had asked."
  },
  {
    "id": "ETFS_POSITIONING-S5",
    "surfaced_by": "0.0.0_AB_MSTR~Z",
    "surfaced_at": "2026-08-21T19:56Z",
    "one_line": "If bbg/ yields no prior day prefix the producer takes prior_end=None and starts from a HARDCODED 2026-08-21 floor -- from a fire months later that is a multi-month Bloomberg history request for the full universe that nobody sized.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "source re-read at this seat, etf_daily_pull.py: :99 prior_end=None; :101 paginate day prefixes; :105 skip d==asof_key; :110 prior_end from manifest; :119 if prior_end else :116 start=Timestamp('2026-08-21')",
        "bbg/2026-08-20/ is THE ONLY prefix supplying prior_end today (prefix count 1, measured)",
        "lifecycle re-derived: ONE rule abort-incomplete-mpu-7d, Expiration NULL -> expires no objects",
        "versioning re-derived: EMPTY response body = NEVER enabled (an enabled-then-disabled bucket returns Status=Suspended), so no delete markers and an empty listing means genuinely empty"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.0.0_AB_MSTR~Z",
    "notes": "⛔ COUPLED TO ETFS_POSITIONING-S4, EDGE RECORDED ON BOTH SIDES per 1.0.0_SA_CTO~Z msg 4628. S5 IS DORMANT PRECISELY AS LONG AS S4'S OBJECTS STAY WHERE THEY ARE -- tracked separately with the same owner and window, a reader disposing of them one at a time discharges the provenance concern and arms the floor IN THE SAME ACT, each step locally reasonable. RULED: cleanup does not run before the floor is addressed, or they move together. THE TRIGGER CANNOT ARRIVE ON A TIMER: no lifecycle expiration, versioning never enabled, so it requires a DELIBERATE act -- which LOWERS the standing without closing it. BOUND carried from 0.7.0_AE_CloudOps~Z unsoftened: they measured lifecycle and versioning, NOT every conceivable deletion path (human/agent delete, future TF change, replication reconfiguration); the claim is that no STANDING configuration deletes anything. Stays ARMED because deliberate acts happen and the likeliest one is what S4 invites."
  }
]
```

---

## 4. ROUND STATE

| | |
|---|---|
| Items | **5** (3 surfaced at this seat, 2 inherited from `0.0.0_AB_MSTR~Z` item 4/5 with a COUPLED EDGE) |
| Graduated | **4** (S1, S2, S4, S5) · Under investigation | **1** (S3, INFERRED) |
| ARMED | **4** (S1, S2 trigger **2026-09-08**; S4 x S5 COUPLED, sequencing ruled) -- disarm owner `0.0.0_AB_MSTR~Z` |
| Remediation | **all OPEN.** DISARMED != REMEDIATED |
| Blocks tonight | **NOTHING** |

**This round cannot close** -- S3 is `UNDER_INVESTIGATION`, and an open item is not a zero.
Closing S3 needs one thing: **L1-4's actual wording**, which the L1 owner or the brief's author can
supply in a line.

-- `3.0.0_SA_CVO~Z`, 2026-08-21
