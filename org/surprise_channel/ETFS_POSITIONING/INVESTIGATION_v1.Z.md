# ETFS_POSITIONING (D4) -- SURPRISE CHANNEL INVESTIGATION v1

**Channel owner:** `3.0.0_SA_CVO~Z` · **Round:** v1 · **Opened:** 2026-08-21 ~19:48Z
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (stage 5) · CLAUDE.md Rule 27
**Subject:** the site-Z **L1 leg** -- `integrations/bloomberg/pipeline/etf_daily_pull.py`, appended to
the `OPAL_BBGTML_daily_pull` 07:00 chain @`49501d1e55`.
**Status:** APPEND-ONLY during this round.
**Sibling file:** `INVESTIGATION_v1.md` on the CLOUD fabric -- a SEPARATE record carrying DIFFERENT findings under ids `ETFS_POSITIONING-S1..S7`. The two files are NEVER merged.
**Namespace rule:** site-Z items carry a FABRIC COORDINATE -- `ETFS_POSITIONING-Z-S{n}`. CLOUD keeps the bare `{PROJECT}-S{n}` form; a bare `S{n}` in a message ALREADY SENT is read in the SENDER's fabric.

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

### Z-S1 -- the as-of TRIPWIRE compares an expression to ITSELF and cannot ever fire

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
-- and it is the one control positioned to catch Z-S2.

### Z-S2 -- `BDay` is holiday-blind, and diverges from the estate's canonical calendar

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

### Z-S1 x Z-S2 -- why they compose, and why they are filed separately

**Together they produce precisely the harm the author's comment names: on the first fire after a
market holiday the run lands data under a holiday key, and its own refusal mechanism passes it
green.**

Filed as two items under Rule 24(iv), because **the remedies deliver different things**:
- Repair **Z-S1 alone** (compare `asof` against an *independent* oracle) -> the run **REFUSES** on
  2026-09-08 rather than landing bad data. That is the designed behaviour, and it is arguably
  sufficient on its own.
- Repair **Z-S2 alone** (swap the date source) -> correct date, but the guard is **still dead** and
  the next date defect is undetected.

A single change *can* move both (point the tripwire at the canonical calendar), but that is a
remedy choice, not evidence they are one defect.

### Z-S3 -- the 08/22-08/24 acceptance window has a static as-of (a READ risk, not a defect)

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
working, which is how a guard gets removed"* -- and given Z-S1, **the guard most likely to be "fixed"
under that pressure is the BDay logic, which is the correct half.**

⛔ **INFERRED, NOT GROUNDED.** I could not locate L1-4's exact wording in
`docs/briefs/etfs-positioning-bloomberg-pull-20260821.md` (my grep returned nothing), **so I do not
know whether L1-4 expects the window to advance.** This is a read-risk conditional on that wording,
**not** an asserted criterion defect. It cannot seed a remediation row while INFERRED.

### Z-S4 x Z-S5 -- THE COUPLED EDGE: the remedy one item invites is the act that fires the other

Found by `0.7.0_AE_CloudOps~Z` (msg 4624) answering a bucket-configuration question **nobody had
asked** -- *"if `bbg/` is ever emptied"* was sitting inside another item as an untested premise.
Cross-item sequencing ruled by `1.0.0_SA_CTO~Z` (msg 4628), who directed this channel to **record
the edge on BOTH items, because an edge written on only one side is found only by whoever reads
that side.** That is why Z-S4 and Z-S5 below each carry it in full rather than one pointing at the other.

**Z-S4 -- PROVENANCE.** Seven ad-hoc objects sit in the production prefix and **no reader can
distinguish them from a scheduled landing** (`0.0.0_AB_MSTR~Z` item 4). The tidy, locally reasonable
response is: delete the ad-hoc objects out of `bbg/`.

**Z-S5 -- THE HARDCODED FLOOR.** If `bbg/` yields no prior day prefix, the producer takes the
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

**So Z-S5 is dormant precisely as long as Z-S4's objects stay where they are.** Tracked separately with
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
which *lowers* Z-S5's standing without closing it. **It stays ARMED: deliberate acts happen, and the
most likely deliberate act is the one Z-S4 invites.**

---

## 3. MACHINE BLOCK

```json
[
  {
    "id": "ETFS_POSITIONING-Z-S1",
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
    "id": "ETFS_POSITIONING-Z-S2",
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
    "notes": "Composes with Z-S1 into the harm the author's own comment names: the run lands under a holiday key AND its refusal mechanism passes it green. Filed separately from Z-S1 per Rule 24(iv) -- repairing Z-S1 alone makes the run REFUSE on 09-08 (designed behaviour, arguably sufficient); repairing Z-S2 alone leaves a dead guard. ⛔ THE REPLACEMENT EXPRESSION IS NOT DETERMINED: the canonical uses an inclusive 'last trading day <= date' convention while this pipeline wants T-1, so it is not obviously a drop-in. I measured the disagreement, not the fix. Trigger 2026-09-08."
  },
  {
    "id": "ETFS_POSITIONING-Z-S3",
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
    "notes": "A READ risk, not a pipeline defect -- filed at that strength deliberately. INFERRED because the conditional half (what L1-4 requires) is unmeasured, so it cannot seed a remediation row. NEVER#1 is explicit that a false outage is not a safe error: it manufactures pressure to fix a working pipeline. Given Z-S1, the guard most likely to be 'fixed' under that pressure is the BDay logic -- the correct half. Blocks a zero-graduation close on this round."
  },
  {
    "id": "ETFS_POSITIONING-Z-S4",
    "surfaced_by": "0.0.0_AB_MSTR~Z",
    "surfaced_at": "2026-08-21T19:56Z",
    "one_line": "Seven ad-hoc objects sit in the production prefix bbg/2026-08-20/ and no reader can distinguish them from a scheduled landing -- and they are the ENTIRE contents of bbg/, so the cleanup this invites is the act that fires Z-S5's floor.",
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
    "notes": "⛔ COUPLED TO ETFS_POSITIONING-Z-S5 -- THE EDGE IS RECORDED ON BOTH ITEMS BY 1.0.0_SA_CTO~Z's DIRECTION (msg 4628): 'an edge written on only one side is found only by whoever reads that side.' The tidy remedy this item invites -- delete the ad-hoc objects -- takes bbg/ prefix count 1 -> 0, which sends the producer down the prior_end=None branch onto Z-S5's hardcoded 2026-08-21 floor. RULED: THE CLEANUP DOES NOT RUN BEFORE THE FLOOR IS ADDRESSED, OR THEY MOVE TOGETHER. A remedy that fires another item's trigger is not a remedy, it is a trade. Found by 0.7.0_AE_CloudOps~Z asking a bucket-configuration question nobody had asked."
  },
  {
    "id": "ETFS_POSITIONING-Z-S5",
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
    "notes": "⛔ COUPLED TO ETFS_POSITIONING-Z-S4, EDGE RECORDED ON BOTH SIDES per 1.0.0_SA_CTO~Z msg 4628. Z-S5 IS DORMANT PRECISELY AS LONG AS Z-S4'S OBJECTS STAY WHERE THEY ARE -- tracked separately with the same owner and window, a reader disposing of them one at a time discharges the provenance concern and arms the floor IN THE SAME ACT, each step locally reasonable. RULED: cleanup does not run before the floor is addressed, or they move together. THE TRIGGER CANNOT ARRIVE ON A TIMER: no lifecycle expiration, versioning never enabled, so it requires a DELIBERATE act -- which LOWERS the standing without closing it. BOUND carried from 0.7.0_AE_CloudOps~Z unsoftened: they measured lifecycle and versioning, NOT every conceivable deletion path (human/agent delete, future TF change, replication reconfiguration); the claim is that no STANDING configuration deletes anything. Stays ARMED because deliberate acts happen and the likeliest one is what Z-S4 invites."
  },
  {
    "id": "ETFS_POSITIONING-Z-S6",
    "surfaced_by": "0.7.0_AE_CloudOps~Z",
    "surfaced_at": "2026-08-21T20:12Z",
    "one_line": "Z-S3's conditional is RESOLVED and it INVERTS Z-S3: L1-4 does not read as stalled, it PASSES DEGENERATELY -- all three acceptance fires compute the identical window 2026-08-21 -> 2026-08-21, so the increment behaviour L1-4 exists to prove is never exercised.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L1-4 wording established: 'run N+1's history window starts where run N's manifest ended' -- the wording Z-S3 could not locate and declined to guess",
        "live manifest s3://opal-data-etfs/bbg/2026-08-20/run_manifest.json read at this seat: as_of 2026-08-20, history_window_start 2026-08-20, history_window_end 2026-08-20, prior_window_end None",
        "etf_daily_pull.py:105 skips d == asof_key, so the only prior prefix for fires 1/2/3 is 2026-08-20 -> prior_end 2026-08-20 -> start 2026-08-21",
        "computed independently at this seat: fires 08/22, 08/23, 08/24 each yield window 2026-08-21 -> 2026-08-21, IDENTICAL; the first fire that ADVANCES the window is 08/25 (08-21 -> 08-24)"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "SUPERSEDES ETFS_POSITIONING-Z-S3 AND CORRECTS ITS DIRECTION -- filed as a new item per append-only, and it is the THIRD self-correction by this seat tonight. Z-S3 said a correct pipeline might be MISREAD AS STALLED (a read risk). THE ACTUAL HAZARD IS THE OPPOSITE AND WORSE: L1-4 READS SATISFIED. Run 2 does start where run 1 ended, so continuity is technically met -- DEGENERATELY, because the window never advances and the increment is never tested. Z-S3's INFERRED marking was correct (the conditional was genuinely unmeasured and I declined to guess), but its conditional resolved AGAINST the direction I assumed. ⛔ THIS IS Z-S1'S CLASS ONE LAYER UP: an acceptance criterion that cannot fail over its own evaluation window is not a criterion. The tripwire could not fire on any input; L1-4 cannot fail across 08/22-08/24. CONSEQUENCE FOR THE SOVEREIGN PRIORITY ITEM: 'L1 accepted on 08/24' would mean the criterion passed without exercising what it measures. If L1-4 is to mean anything its window must include 08/25, the first fire whose window advances. EDGE RECORDED ON BOTH L1-2 AND L1-4 per 1.0.0_SA_CTO~Z's standing instruction and the filer's note -- an edge on one side is found only by whoever reads that side. Disposition of the criterion is the issuer's; the class call was mine."
  },
  {
    "id": "ETFS_POSITIONING-Z-S7",
    "surfaced_by": "0.7.0_AE_CloudOps~Z",
    "surfaced_at": "2026-08-21T20:10Z",
    "one_line": "L1-2's three fires land the SAME keys and, because versioning was never enabled, each overwrite is DESTRUCTIVE -- fires 1 and 2 leave no S3 trace, so the criterion's own named instrument cannot distinguish three fires from one Monday fire.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "as_of resolution re-derived at this seat: fires 08/22, 08/23, 08/24 all -> as_of 2026-08-21, ONE distinct date",
        "writes are s3.put_object to deterministic keys (verified at this seat during the idempotency check) -- overwrite, not append",
        "versioning re-derived at this seat: EMPTY get-bucket-versioning response = NEVER enabled, so no noncurrent versions and no delete markers",
        "composition: same keys + no versioning => after fire 3 the bucket holds exactly one object set, indistinguishable from a single Monday fire"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "⛔ THE PRODUCER IS CORRECT AND THIS IS NOT A STALENESS FINDING. The as_of resolution is NEVER#1 working as designed -- Friday's data IS the right answer on Saturday, Sunday and Monday. THE CRITERION is what mis-assumes, by expecting consecutive fires to produce distinct dated artifacts. ⛔ AND IT CORRECTS THE COMPLETENESS OF MY OWN Z-S5: I recorded 'versioning never enabled' with ONLY its BENIGN reading -- no delete markers, so an empty listing means genuinely empty, a false-absence class closed. THE SAME MEASURED FACT HAS AN OPPOSITE SECOND CONSEQUENCE I DID NOT DRAW: no versioning also means NO TRACE OF AN OVERWRITTEN FIRE. One fact, two implications, and I banked only the reassuring one -- the filer drew the other. COMPOSES WITH Z-S6: Z-S6 says L1-4 cannot FAIL across its window; Z-S7 says L1-2 cannot be EVIDENCED from S3 after the fact. Together the acceptance evidence for the priority item is thinner than either finding alone shows, and CTO's own fourth pass separately found the wrapper logs do not establish trigger provenance either. Disposition is the issuer's; routed there same-turn by the filer, recorded here because routing to the issuer does not discharge the channel's record obligation."
  },
  {
    "id": "ETFS_POSITIONING-Z-S8",
    "surfaced_by": "0.0.0_AB_MSTR~Z",
    "surfaced_at": "2026-08-21T20:19Z",
    "one_line": "The holdings-breakdown and weighted-characteristics sections are buildable for 2 of the 4 declared funds: DIVZ and IDVZ have NO constituent holdings in any tree, and Bloomberg does not serve them via reference data.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "re-derived at this seat on the latest partition silver/holdings/2026-08-20.parquet: fund_ticker = ['PFDE','PFOE'] only, 114 rows",
        "positive control silver/netassets/2026-08-20.parquet: ticker = ['DIVZ','IDVZ','PFDE','PFOE'] -- all four declared funds present, so the absence is specific to holdings",
        "like-for-like column comparison: declared-but-no-holdings = ['DIVZ','IDVZ'], matching the filer exactly",
        "top-level prefix enumeration re-derived: 7 prefixes (bbg-testpull, bbg, config, daily, platinum, silver, snapshots) -- matches the filer's enumerated denominator",
        "filer's bound: 4 dates spanning 2026-05 to 2026-08 over 69 partitions, PFDE/PFOE every time; Bloomberg returns ZERO NOT_AUTHORIZED, so it is not an entitlement gap"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "Class BLOCKING confirmed by the issuer; INERT because nothing fires today -- it bears on what the deliverable can CONTAIN, not on any executing act. Does not block the L1 leg. THE FILER ALSO PRE-EMPTED A FALSE-GAP READ WORTH KEEPING: EQY_DVD_YLD_IND_NET is 80/109 = 73.4%, and the 29 blanks are GENUINE NON-DIVIDEND-PAYERS (AMD, AMZN, ANET, BA...) -- a correct economic fact that a naive coverage read calls a 27% hole. Likewise the 4 GICS_SECTOR_NAME gaps are exactly the 4 funds, which is correct since an ETF has no single GICS sector; CONSTITUENT coverage is 105/105 = 100%. ⛔ NEAR-MISS RECORDED AT THIS SEAT: while verifying this item I nearly filed a SECOND, FABRICATED item claiming silver/holdings and silver/netassets disagree on ticker case and that a join between them silently returns zero. IT IS FALSE. My heuristic column-detector picked fund_key (lowercase) instead of fund_ticker (uppercase), twice; BOTH tables carry BOTH conventions consistently (ticker/fund_ticker UPPER, key/fund_key lower) and BOTH joins return 114 rows. What caught it was the join returning 114 beside a '<- silent zero' label I had PRE-WRITTEN into the print statement -- the number contradicted the verdict I had already typed. Recorded because a fabricated hazard in a permanent record is worse than a missed one, and because the estate's own rule names it: never pre-write the verdict into the same echo as the number, and never let a heuristic pick the column your claim rests on."
  },
 {
  "id": "ETFS_POSITIONING-Z-S9",
  "surfaced_by": "0.4.0_DE_ClientPlatform~Z (msg 11425), from the first actual RENDER of the Positioning page in Satellites mode -- the rung 11382 s.6 and 11414 s.5 both closed by declaring they had not reached it. FILED by 3.0.0_SA_CVO~Z as the channel seat; the id is minted here because the surfacing seat correctly did not self-allocate.",
  "surfaced_at": "2026-08-28T01:14Z",
  "one_line": "The Satellites empty-state notice asserts a CAUSE the renderer cannot observe: satelliteAdapter.ts:105-107 joins `!modelsData` and `registry.length === 0` with `||` into one `data: null`, and Positioning.tsx:316-320 renders ONE unconditional sentence naming only the registry limb -- so a failed or slow MODELS fetch tells a client-facing reader that the satellite registry is unpublished when it is published.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.4.0_DE_ClientPlatform~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "satelliteAdapter.ts:105-107 -- `if (!modelsData || registry.length === 0) { return { data: null, ... } }`; read via `git show HEAD:` at portal @f1180aad, NOT from the worktree",
    "Positioning.tsx:316-320 -- `{mode === 'satellites' && !activeData && (` ... SATELLITE_PENDING_NOTICE, one unconditional sentence naming only the registry cause",
    "no loading guard on the notice: `activeLoading` exists at Positioning.tsx:241 and is passed to a child only at :349, so it never gates this branch",
    "environment pinned: portal submodule DEV @f1180aad, 0 ahead / 0 behind origin/DEV, no tracked file modified; vite 5175, ui-smoke.mjs, LOC printed /positioning on both captures so the route is real and not an auth bounce",
    "NEGATIVE RESULT recorded as such: the two captures CANNOT discriminate the limbs -- both are true in this environment -- so the screenshots prove the page RENDERS and are not evidence for the failure mode. The evidence is the source at a named vintage.",
    "*** BOUND LIFTED 2026-08-28T01:2xZ -- THE CONFOUND ABOVE IS NO LONGER THE STATE. 0.4.0_DE_ClientPlatform~Z (msg 11511) varied EXACTLY ONE LIMB in an ISOLATED git worktree at portal HEAD f1180aad (never the shared tree; vite on 5176, the shared server untouched on 5175): SAME build, SAME seeded NON-EMPTY registry -- proven non-empty by the same worktree rendering a full satellite, treemap, characteristics and an 8-window performance grid -- with ONLY the models payload removed. The page then rendered \"No satellites to show. The satellite membership registry has not been published yet.\" THAT SENTENCE IS FALSE IN THAT BUILD: the registry IS published and the models fetch is what failed. The false cause is DEMONSTRATED, not predicted, and the screenshots ARE evidence for the failure mode now. Single-variable ablation, which is what the original bound said was missing. ***"
   ]
  },
  "notes": "*** EXTENDED 2026-08-28T01:4xZ -- THE CAUSE SET IS NOT FIXED AT TWO, IT GROWS WITH THE FETCH PATH, AND MY RECORD UNDERSTATES IT. This item was filed against the TWO causes joined by `||` at satelliteAdapter.ts:105-107 (!modelsData, registry.length === 0). 1.0.0_SA_CTO~Z's 11620 cell-1 measurement shows there is currently NO FETCH PATH AT ALL, so once one exists a THIRD cause appears: THE ROUTE ITSELF FAILING. A 404 or a 5xx would land in the same `data: null` and, unfixed, would render the same sentence claiming the registry is unpublished. ⛔ SO THE DISARM MUST BE WRITTEN AGAINST N CAUSES, NOT PATCHED FOR TWO -- a two-way split shipped now would be correct on the day it lands and silently wrong again the moment the fetch is wired, which is the same shape as the original defect one iteration later. *** AND 1.0.0_SA_CTO~Z REACHED THIS REQUIREMENT INDEPENDENTLY, FROM THE OTHER END: their ruled shape for the fetch cell carries '(e) A FETCH FAILURE IS NOT AN EMPTY REGISTRY. Distinguish them at the seam. Rendering \"no satellites\" because a route 404'd is the plausible-wrong-state twin of the plausible-wrong-number this page has already banked twice.' That IS this item's disarm, arrived at while specifying a route rather than while auditing a notice. ⭐ THE CONSEQUENCE FOR OWNERSHIP, and it is the actionable part: Z-S9's disarm should be CUT INSIDE the fetch-path cell rather than as a separate fix. Same seam, same edit, and 1.0.0_SA_CTO~Z's (c) already says the consumer seam must be USED rather than added. A disarm bundled into the act that would otherwise re-arm it cannot be lost. *** THIS SUPERSEDES THE COUPLING I NAMED IN THE 01:2xZ AMENDMENT BELOW -- I said the disarm bundles into 'whoever replaces satelliteSet.ts:93'. Sharper now: that replacement IS the fetch-path cell, and the cell has a ruled shape and a named lane split (DE for (c)(e), AE for (a)(b)). *** *** AMENDED 2026-08-28T01:2xZ BY 3.0.0_SA_CVO~Z -- I NAMED THE WRONG TRIGGER, AND THE EVENT I PREDICTED WOULD FIRE IT HAS NOW HAPPENED WITHOUT FIRING IT. My original text below reads: 'the event that falsifies limb A while leaving limb B live is ETFS_SATELLITES.TO-5-DS publishing platinum/satellites/registry.json.' THAT PUBLISH HAS OCCURRED -- 0.4.0_DS_ClientPlatform~L delivered it (msg 11500), opal-data-cot platinum/satellites/registry.json, 2182 bytes, LastModified 2026-08-28T01:09:51Z, VersionId D1iVAJ4LJOqx1BDPMLmcEXLOUJvcP7wb, 9 books. AND LIMB A IS UNCHANGED. MEASURED AT SOURCE: portal/src/pages/Positioning/shared/satelliteSet.ts:93 is `export const SATELLITE_REGISTRY: readonly SatelliteBook[] = []` -- a COMPILE-TIME CONSTANT with NO fetch and NO runtime population, defaulted into the three consuming functions at :106, :112 and :173. So an S3 artifact existing does not reach the frontend, `registry.length === 0` is still true in the shipped bundle, and the item is NOT yet live. *** THE CORRECTED TRIGGER: the act that REPLACES that empty constant with a populated or runtime-fetched registry -- which requires TO-4-AE serving the key AND the frontend wiring. *** DIRECTION OF MY ERROR, STATED BECAUSE IT DECIDES WHO WAS MISLED AND HOW: I named a trigger EARLIER than the true one, so the hazard has MORE slack than I claimed, not less. That is the conservative direction and it is still wrong -- a seat reading my original text after 01:09:51Z would conclude the page was ALREADY asserting a false cause and could have panic-fixed, or worse concluded the window had closed and stopped tracking it. A conservative error passes its own check because nobody challenges a claim of less time than you have. *** AND THE CORRECTION MAKES THE DISARM MORE ACTIONABLE, NOT LESS: because the trigger is now a SINGLE IDENTIFIED CODE ACT rather than a lane's completion, the disarm should be BUNDLED INTO THAT ACT. Whoever replaces satelliteSet.ts:93 with a real registry MUST, in the same change, split the two causes at satelliteAdapter.ts:105-107 so Positioning.tsx:316 can choose its sentence. Stated as a coupling on one edit, that is far harder to lose than a deadline expressed in another lane's schedule. *** MY ORIGINAL, UNEDITED, BELOW -- nothing struck, so a reader can see what was claimed and what replaced it. *** *** THE ORDERING CONSTRAINT, ADDED BY 3.0.0_SA_CVO~Z AND NOT PRESENT IN THE SURFACING MESSAGE -- IT IS THE REASON THIS IS ARMED RATHER THAN A BACKLOG NIT: the notice is TRUE BY COINCIDENCE today because BOTH limbs hold at once (SATELLITE_REGISTRY is a compile-time empty constant AND this environment has no models payload). The event that falsifies limb A while leaving limb B live is ETFS_SATELLITES.TO-5-DS publishing platinum/satellites/registry.json -- which is RANK-2 SEATED AND IN FLIGHT at 0.4.0_DS_ClientPlatform~L, resumed from the AC2 ruling in msg 11375. SO THE DISARM HAS A DEADLINE EXPRESSED IN ANOTHER LANE'S DELIVERABLE, NOT IN A CLOCK: it must land BEFORE the registry is published, or the first thing a correct, wanted deliverable does on arrival is make a client-facing page assert a false cause. Nobody had stated that ordering; both lanes are proceeding correctly in isolation. *** DISARM ACT (offered by the owner in 11425 s.4, NOT built, and correctly not built -- whether that seat builds on this page is the open call in 11395 s.3 with the cell choice at 2.0.0_SA_COO~Z): return the two causes DISTINGUISHABLY from the adapter, which already returns `problems` as DATA rather than throwing, and let :316 choose its sentence. Owner estimate: well under an hour. *** DISARMED != REMEDIATED and the two are separable here: naming the second cause disarms it; a loading guard on :316 is the wider remediation and is not required for the disarm. *** THE CLASS IS TWICE-BANKED AND THAT IS THE SHARP PART: 0.4.0_DE_ClientPlatform~Z removed this exact shape from D1_CATVIEWS tonight (@c0e23bd8, @f1180aad -- 'the L1 empty state asserted a CAUSE the renderer cannot observe'), swept the sibling file, and did not sweep this one -- an instance of 'fixing a defect does not reach whoever quoted it' pointed at the fixer's own surface. It is ALSO an instance of 'discharging one hazard can arm another': TO-5-DS is the wanted deliverable and landing it is precisely the trigger. *** OPEN AND NOT MEASURED, flagged by the surfacing seat rather than assumed: what the Holdings-Breakdown/Performance toggle does for a satellite is unobservable today because the empty registry masks it, and 11414 records the PERFORMANCE blend as NOT BUILT by declaration (satelliteAdapter.ts:21, SAT-e-3 'v1 is snapshot-only'). Whoever takes the performance cell renders it against a FIXTURED registry before trusting it."
 },
 {
  "id": "ETFS_POSITIONING-Z-S10",
  "surfaced_by": "0.4.0_DE_ClientPlatform~Z (msg 11511 s.4), from a PLANTED DISCRIMINATOR in an isolated worktree exercise. FILED by 3.0.0_SA_CVO~Z as the channel seat; standing set by me, and the reasoning for ARMED is mine rather than the surfacing seat's -- see notes.",
  "surfaced_at": "2026-08-28T01:27Z",
  "one_line": "The satellite blend resolves a ticker's carried fields (returns, sub_asset_class, fee) by FIRST-LEG-WINS, confirmed by exercise, and the premise it depends on -- that a ticker's carried values are identical across every model holding it (satelliteAdapter.ts:262-266) -- is ASSERTED NOWHERE: nothing compares a ticker's fields ACROSS legs, so a violation is silent and unfalsifiable on screen.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.4.0_DE_ClientPlatform~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "PLANTED DISCRIMINATOR, exercised: AGG given deliberately different returns per leg (UST 1D=0.11, ST 1D=90.11) so the render had to name a winner. It rendered +0.11 -- the FIRST leg (UST, 60%) -- and the 90.11 vanished with nothing on screen indicating a choice was made",
    "the premise the mechanism depends on is stated only as a COMMENT: satelliteAdapter.ts:262-266, 'a ticker's CHARACTERISTICS ... are identical across models'",
    "validateSatellite checks satellite DEFINITIONS; no check compares a ticker's carried fields across legs -- the gap is the absence of an assertion, measured by the surfacing seat",
    "same exercise's positive control that the harness itself is sound: blend (B) reproduced pre-stated predictions exactly (AGG .60*.60+.50*.40 = 0.56 -> rendered 56.00, ONE row not two; SHY 24.00; IEF 20.00; total 100.00)",
    "NOT PRODUCTION EVIDENCE AND THE SURFACING SEAT SAID SO FIRST: the fixture is synthetic (EXSAT = UST 60 / ST 40, invented returns) and DELIBERATELY VIOLATED the documented premise. It establishes the MECHANISM, never any claim about real data."
   ]
  },
  "notes": "*** ⛔ THE as_of DISARM RECORDED BELOW IS WITHDRAWN BY ITS OWN AUTHOR 2026-08-28T01:41Z (1.0.0_SA_CTO~Z, msg 11628) -- IT WAS A CONTROL THAT CANNOT FAIL. 0.4.0_DE_ClientPlatform~Z did the credentialed read nobody had done: s3://opal-data-portal-v2/json/positioning/positioning_data.json (LastModified 2026-08-27T11:05:20Z, GZIPPED AT REST -- a naive parse dies on 0x8b) shows as_of_date = None on UST/ST/INT/LT/ULT, ONE distinct value across five books. An assertion that all books share an as_of therefore compares None to None and PASSES UNIVERSALLY. *** ⛔⛔ AND THE FORK I WROTE INTO THE NOTES BELOW WAS THE SAME TRAP, SO THIS IS NOT ONLY THE RULING AUTHOR'S ERROR: I wrote 'if someone measures that and it CANNOT happen, this drops to INERT and that is a clean disarm.' 0.4.0_DE_ClientPlatform~Z REFUSED that branch and was right to -- the tripwire never fires, BUT NOT BECAUSE SKEW IS IMPOSSIBLE: prior_date varies 2-across-5 in the very same artifact (UST 2026-05-21 vs 2026-07-01 for the rest). TAKING MY OWN INERT BRANCH WOULD HAVE RETIRED THIS HAZARD BY MEASURING THE ONE FIELD STRUCTURALLY INCAPABLE OF SHOWING IT. A convenient branch reachable for the wrong reason is worse than no branch, because it closes the item while looking like measurement. *** THE REPLACEMENT RULING, and it guards the PREMISE rather than a correlate of it: WHEN A TICKER APPEARS IN MORE THAN ONE CONSTITUENT LEG, ASSERT ITS `returns` AGREE ACROSS THOSE LEGS; on disagreement SURFACE it rather than silently taking the first. Strictly better on four counts, and the second is the one this record cares about: it needs NO vintage field, so it is immune to as_of_date being null; IT CAN DEMONSTRABLY FIRE, and its negative control ALREADY EXISTS AND HAS BEEN RUN -- 0.4.0_DE_ClientPlatform~Z's planted AGG at 1D=0.11/90.11 produced exactly the failing condition and watched 90.11 vanish; it fires WHEN THE HARM OCCURS rather than when a correlate does (two books at different vintages that agree on every shared ticker cause no wrong number and should not be refused, and the withdrawn guard would have refused them while MISSING two same-vintage books that disagree); and the shared-ticker set inside one satellite is small. *** REMEDY CHANGED FROM REFUSE TO SURFACE, and the reason is a grain argument I am recording because it reverses my own earlier note: a VINTAGE mismatch corrupts the whole book, so refusal was right for the withdrawn guard; a SINGLE disagreeing ticker does not, so DROPPED-NOT-RENDERED is too blunt. The surface-vs-refuse choice is explicitly left to the DE lane rather than ruled blind. *** DO NOT BUILD A GUARD ON prior_date: the reading that it is a previous REBALANCE date rather than a data date is LABELLED AN INFERENCE by its author and is NOT verified -- confirm at the producer first. If it holds, NO FIELD ON THIS CONTRACT EXPRESSES PER-BOOK DATA VINTAGE, which is a PRODUCER-SIDE GAP and not a frontend assert. Recorded as an observation; the s.4 guard covers the actual harm without it. *** ORIGINAL NOTES BELOW, UNEDITED, INCLUDING MY WITHDRAWN FORK. *** *** DISARM ACT SUPERSEDED 2026-08-28T01:2xZ -- 1.0.0_SA_CTO~Z RULED IT (msg 11515) AND THE RULED FORM IS STRICTER THAN THE ONE THIS RECORD FIRST CARRIED. Ruled: FIRST-LEG-WINS IS THE CORRECT MECHANISM AND STAYS -- a ticker's return over a window is a property OF THE TICKER, so carrying rather than blending is the correct arithmetic and blending identical values would be a no-op dressed as rigour. The guard is an as_of ASSERTION, not a change to the blend: the adapter asserts that all constituent books of a satellite share an as_of and REFUSES a satellite whose legs disagree. *** THE DIFFERENCE MATTERS AND I AM NOT COLLAPSING IT: the disarm this record first carried (0.4.0_DE_ClientPlatform~Z's offer -- push one `problems` row) RENDERS the satellite with a warning beside it; the ruled form REFUSES TO RENDER IT. 1.0.0_SA_CTO~Z's ground for the stricter form: 'the remedy for a vintage mismatch is to REFUSE THE SATELLITE, never to pick a winner more cleverly', matching validateSatellite's existing DROPPED-NOT-RENDERED behaviour and the registry contract's as_of-NON-NULL-or-RAISE. Take the ruled form. *** ON THE as_of MECHANISM I NAMED BELOW AS AN UNMEASURED CANDIDATE: 1.0.0_SA_CTO~Z reached it independently and ruled it the ONLY way the premise breaks. ⛔ THAT IS NOT CORROBORATION AND I WILL NOT RECORD IT AS SUCH -- both of us derived it from the SAME source message (0.4.0_DE_ClientPlatform~Z's 11511) within the same minute, neither having seen the other. Two seats, one rung, one input: independent DERIVATION, and zero additional coverage of the underlying fact. *** THE SIZING QUESTION IS STILL UNMEASURED BY EVERY SEAT THAT HAS TOUCHED THIS: can the served models payload carry MIXED as_of DATES ACROSS BOOKS? If it cannot by construction, the assert is a tripwire that never fires and this drops to INERT. If it can, the assert is the only thing between the fabric and a silently wrong client-facing number. It needs a credentialed read of the served artifact and NOBODY HAS DONE IT. *** SCOPE, ruled and preserved: this is a SMALL DE-lane cell and is NOT a blocker on Andrew's item 2; cut it WITH the render work, not ahead of it. *** ORIGINAL NOTES BELOW, UNEDITED. *** *** STANDING IS MINE, NOT THE SURFACING SEAT'S, AND I AM SEPARATING THE TWO CLAIMS BECAUSE THEY HAVE DIFFERENT EVIDENCE. 0.4.0_DE_ClientPlatform~Z was emphatic and CORRECT that this is NOT a production defect -- their fixture broke the premise on purpose, and in production a ticker's return is a property of the ticker, so the premise is almost certainly true. I am filing it ARMED anyway, on a narrower ground: an UNASSERTED premise plus a SILENT resolution means that IF the premise is ever false, nothing in the system can tell anyone. The hazard is the absence of falsifiability, not a present wrong number. *** THE PATH I CAN NAME THAT WOULD VIOLATE IT, AND WHICH I HAVE NOT MEASURED -- flagged as a CANDIDATE, never as evidence, and it is not in the surfacing message: `returns` for one ticker is identical across models ONLY IF every model's payload carries the same as-of vintage. A per-model as-of skew (one model refreshed, another stale) would present as the SAME ticker with DIFFERENT returns in two legs -- exactly the input that makes first-leg-wins pick silently. I have NOT measured whether the served models payload can carry per-model as-of skew, and this record must not be read as saying it does. If someone measures that and it CANNOT happen, this drops to INERT and that is a clean disarm. *** WHY IT GENERALISES BEYOND `returns`: the surfacing seat named `sub_asset_class` and `fee` as carried the same way. sub_asset_class is the field 1.0.0_SA_CTO~Z's 11385 taxonomy ruling is about, so a future vocabulary act lands on a field whose cross-leg agreement nothing checks. *** DISARM, OFFERED BY THE OWNER AND NOT BUILT, AND IT REUSES WHAT EXISTS RATHER THAN ADDING A MECHANISM (build ladder): the adapter ALREADY returns `problems` as DATA and Positioning.tsx:326 ALREADY renders them, so a ticker appearing in 2+ legs with differing carried values pushes one problem row. *** RELATIONSHIP TO ETFS_POSITIONING-Z-S9, because they are NOT the same item and share a file: Z-S9 is a notice naming the WRONG CAUSE of an absence; this is a SILENT CHOICE among present values. Different failure, different remedy -- Z-S9's disarm (split the two `||` causes) does NOT move this one, which is the Rule 24(iv) test for filing them separately."
 },
 {
  "id": "ETFS_POSITIONING-Z-S11",
  "surfaced_by": "1.0.0_SA_CTO~Z (msg 11620 cell 1), carrying 0.4.0_DE_ClientPlatform~Z's census (msg 11540) as THEIRS rather than restating it as its own. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T01:40Z",
  "one_line": "There is NO FETCH PATH for the satellites registry: nothing in the portal reads platinum/satellites/registry.json, every use of SATELLITE_REGISTRY is a DEFAULT PARAMETER, and Positioning.tsx:225 calls satellitesToPositioningShape with ONE argument -- so the producer could run correctly on a schedule forever and the view would still render empty. This is the end-to-end blocker on Andrew's item 2, and he named the leg himself.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "census with a POSITIVE CONTROL that fires (0.4.0_DE_ClientPlatform~Z, msg 11540): satellites/registry 0 files; registry.json 0 files; satelliteRegistry 0 files; satellites.json 0 files; getSatellite 0 files; no apiRequest mentioning 'satel' -- against positioning_data.json returning 8 files, so the instrument demonstrably finds a real serving path when one exists",
    "SATELLITE_REGISTRY appears in exactly 2 files and EVERY use is a DEFAULT PARAMETER: satelliteAdapter.ts:100, satelliteSet.ts:106/112/173",
    "Positioning.tsx:225 calls satellitesToPositioningShape(positioningData) with ONE ARGUMENT, so the registry parameter always falls back to the compile-time constant that ships empty on purpose",
    "TO census this turn by 1.0.0_SA_CTO~Z: to-check --all, scanned=2147 task orders, ZERO match this cell",
    "ANDREW-DIRECT 2026-08-28 ~01:3xZ names the leg explicitly, VERBATIM: 'End to end full Satellites view mode on Positioning page, including all backend and api work'"
   ]
  },
  "notes": "*** WHY THIS IS THE ITEM THAT REORDERS THE OTHERS: every other satellites cell is UPSTREAM OF A DISCONNECT. The unit fix does not make the artifact reach the page; TO-5-DS landing does not; TO-6-AE's SCHEDULE does not. 1.0.0_SA_CTO~Z's sentence and I am not improving on it -- 'the producer could run correctly on a schedule forever and the view would still render empty, because no code reads the object.' ⛔ THE RISK THIS CREATES IS A FALSE SENSE OF COMPLETION: tonight produced a published registry, a passing 5-of-6 TO, an exercised end-to-end render on a SEEDED registry, and a spawned apply lane. Every one of those is real and NONE of them connects the artifact to the page. A reader summing tonight's good news would conclude item 2 is nearly done. *** SHAPE IS ALREADY RULED so the cut needs no design round (1.0.0_SA_CTO~Z, 11620 s.3), and the selection criterion is Andrew's own, VERBATIM ~22:1xZ 2026-08-27: 'we dont have to mess with the rest of the plumbing of the page ... if we decide later to handle this elsewhere, not a massive effort.' HE PRICED REVERSIBILITY OVER CORRECTNESS-TODAY. (a) SCOPED route, satellites only -- do NOT fold into positioning_data.json. (b) FIRM RESOLUTION IS THE BUCKET, NEVER A KEY SEGMENT: the key carries no firm segment ON PURPOSE and a firm-segmented key re-introduces the forgeable second expression of the boundary -- the exact defect 0.4.0_DS_ClientPlatform~L fixed hours ago. (c) the consumer seam ALREADY EXISTS and must be USED not added: pass the fetched value at Positioning.tsx:225; no new branch, no mode arm, Models and ETFs paths literally untouched. (d) wire shape already ruled { books, as_of }, as_of NON-NULL ALWAYS INCLUDING ON THE EMPTY SET, PUBLISH EMPTY NEVER DELETE -- an empty books array is a VALID served state, not an error and not a reason to fall back. (e) A FETCH FAILURE IS NOT AN EMPTY REGISTRY. *** (e) IS ETFS_POSITIONING-Z-S9's DISARM, REACHED INDEPENDENTLY FROM THE ROUTE END, and I have recorded on that item that its disarm should be cut INSIDE this cell rather than separately -- same seam, same edit, and a disarm bundled into the act that would otherwise re-arm it cannot be lost. THIS CELL ALSO GROWS Z-S9's CAUSE SET FROM TWO TO THREE. *** TWO OWNERS, DELIBERATELY, and 1.0.0_SA_CTO~Z gave the reason: DE-lane for (c)(e), AE-lane for (a)(b), 'bundled, you get a route with nothing reading it or a reader with no route, and neither failure announces itself.' disarm_owner is 2.0.0_SA_COO~Z as the seat that cuts; the executing lanes follow from the cut. *** SIBLING CELL, NOT FILED SEPARATELY BUT NAMED SO IT IS NOT LOST A THIRD TIME: Andrew's item 1 design half -- 'appropriately improving the formatting/design of the frontend for that function' -- surface ModelPortfolios.tsx / CategoryViewTree.tsx / aum.ts, still ZERO TOs. It has now been named twice (11505 s.B, 11620 cell 2) and picked up zero times. Its two constraints, restated so nobody re-derives them: it has NO stated acceptance criterion and one MUST NOT be invented -- his eye is the bar, as with D4's smoke test -- and THE INSTRUMENT IS A RENDERED SCREENSHOT, NOT A GREP, because a contrast defect on the silver canvas is invisible to every static check this estate owns."
 },
 {
  "id": "ETFS_POSITIONING-Z-S12",
  "surfaced_by": "0.7.0_AE_CloudOps~S (msg 11644), from a DRY-RUN exercise of the deployed Lambda -- and surfaced AGAINST THAT SEAT'S OWN ratified design decision, which is why it reads as a finding rather than a complaint. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T01:44Z",
  "one_line": "S3 returns 403 AccessDenied rather than 404 NoSuchKey for a missing object when the caller holds no s3:ListBucket -- it will not confirm non-existence to a principal that cannot list -- so at the satellites registry producer's read surface 'UPSTREAM IS LATE' and 'MY READ GRANT IS BROKEN' are BYTE-IDENTICAL.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "0.7.0_AE_CloudOps~S",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "observed in a DRY-RUN of the DEPLOYED bytes (writes nothing, does not touch the served key, does not muddy the AC3 discriminator) against a partition genuinely absent at 01:39Z: 'BLOCKED: no roster partition at .../rebalancer_models/2026-08-28/page_000.json (S3 said AccessDenied)'",
    "the benign reading was ESTABLISHED, not assumed: simulate-principal-policy returns allowed on both read prefixes and on the exact write key",
    "THREE NEGATIVE CONTROLS returned implicitDeny, each issued as a SEPARATE invocation with one --resource-arns per call, so the multi-ARN false-deny mode could not silently disarm the controls",
    "same dry-run independently confirmed what only an in-situ run can: the repo-mirroring zip layout imports under /var/task, and the producer resolved as_of=2026-08-28 (resolved today-UTC) in the DEPLOYED bytes; 96 MB used against 192 MB sizing"
   ]
  },
  "notes": "*** WHY THIS IS FILED AS A CLASS RATHER THAN A CONFIG NOTE: IT IS THE SECOND SURFACE ON WHICH THE SAME COLLAPSE HAS APPEARED. ETFS_SATELLITES.TO-5-DS AC3 records the identical shape for the SERVING layer -- an absent artifact and a forbidden read arriving as one status -- and that is why the edge synthesis was removed @24a8435642. Here it has reappeared ONE LAYER UP, on the PRODUCER'S READ side. This is CLAUDE.md Rule 28's substrate question 7 -- 'is the failure mode distinguishable from a genuine negative?' -- answered NO twice, on two different rungs of one pipeline. A remedy applied at one rung does not reach the other, which is the Rule 24(iv) test and the reason it gets its own id. *** STANDING IS INERT, NOT ARMED, AND THE DISTINCTION IS LOAD-BEARING HERE: the grant is MEASURED CORRECT today, so left alone this does not currently produce a wrong outcome through normal operation -- it degrades DIAGNOSIS on the day something else breaks. The harm is deferred and conditional, which is what INERT means; calling it ARMED would inflate it and spend the standing's meaning. ⚠ BUT INERT IS NOT HARMLESS: the day the grant DOES break, the producer's error surface will say the same words it says for a late upstream, and whoever is on that incident will chase the wrong lane first. *** ⛔ THE SCOPE NOTE IS THE SURFACING SEAT'S AND I AM PRESERVING IT VERBATIM IN SUBSTANCE BECAUSE IT PROTECTS A PRIOR RULING FROM BEING MIS-READ: the remedy -- a prefix-conditioned s3:ListBucket on the two rebalancer prefixes, which separates the states (late upstream reads NoSuchKey, broken grant reads AccessDenied) -- DOES NOT IMPLEMENT OPTION (C). (C) was a newest-partition RESOLUTION strategy; this is a grant that only changes which error code a failure carries. REJECTING (C) DOES NOT ENTAIL REJECTING THIS, and 2.0.0_SA_COO~Z's ratification of the no-ListBucket decision on the ground of 'consistent with rejecting (C)' should not be read as having settled a question it did not reach. *** NOT FIXED UNILATERALLY AND THAT IS CORRECT: the absence was EXPLICITLY RATIFIED by the issuer, and nothing is blocked because the grant measures correct. The surfacing seat says of the cost, 'I do not think either of us saw this cost when that was settled' -- which is the honest form: a ratification is not invalidated by a cost nobody priced, it is AMENDED by one. Remedy is the issuer's call, not this seat's and not mine. *** A SEAT SURFACING A COST OF ITS OWN RATIFIED DESIGN, AGAINST ITS OWN INTEREST, IS THE CHANNEL WORKING AS INTENDED and is recorded as such."
 }
]
```

---

## 4. ROUND STATE

| | |
|---|---|
| Items | **8** (3 at this seat, 2 inherited with a COUPLED EDGE, 1 inverting Z-S3, 1 completing Z-S5, 1 from `0.0.0_AB_MSTR~Z`) |
| Graduated | **7** (Z-S1, Z-S2, Z-S4, Z-S5, Z-S6, Z-S7, Z-S8) · Z-S3 SUPERSEDED by Z-S6 |
| ARMED | **4** (Z-S1, Z-S2 trigger **2026-09-08**; Z-S4 x Z-S5 COUPLED, sequencing ruled) -- disarm owner `0.0.0_AB_MSTR~Z` |
| Remediation | **all OPEN.** DISARMED != REMEDIATED |
| Blocks tonight | **NOTHING** |

**This round cannot close** -- Z-S3 is `UNDER_INVESTIGATION`, and an open item is not a zero.
Closing Z-S3 needs one thing: **L1-4's actual wording**, which the L1 owner or the brief's author can
supply in a line.

-- `3.0.0_SA_CVO~Z`, 2026-08-21
