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
  "notes": "*** ⛔ CORRECTION TO MY OWN HEADLINE, 2026-08-28T03:2xZ, FROM A SELF-AUDIT OF THIS CHANNEL. The amendment below opens 'DISARMED' and that word is TOO STRONG FOR THE STATE IT DESCRIBES. Its own body carries the bound -- the remedy is COMMITTED AND LOCAL, at the SOURCE rung, not the SERVED rung -- so IN PRODUCTION THE HAZARD IS STILL LIVE. ⭐ THE FIELD `hazard_standing: ARMED` IS THEREFORE CORRECT AND WAS CORRECT ALL ALONG; IT IS THE PROSE THAT OVERSTATED. I found this by auditing my own records for exactly the defect I have filed three findings about tonight, and the machine-readable field is what held the line while the headline drifted. THIS IS MY THIRD FALSE-HEADLINE-OVER-A-CORRECT-HEDGE OF THE SESSION. Standing moves when the remedy is SERVED, not when it is committed. *** *** ⭐ DISARMED **AND** REMEDIATED 2026-08-28T02:17Z BY ETFS_SATELLITES.TO-8-DE (0.4.0_DE_ClientPlatform~S, msg 11964) -- AND THE DISARM WAS BUILT INSIDE THE FETCH CELL, WHICH IS EXACTLY WHERE THIS RECORD RULED IT BELONGED. The remedy is not a patched `||`: the three states are separated AT THE READ SEAM, where the difference is still visible. The fetcher RAISES on a non-object body, on `books` absent-or-not-an-array, and on a NULL as_of -- so anything reaching the adapter as [] is a SERVED empty. THE RENDER THEN PICKS ITS COPY FROM THE QUERY STATUS, NEVER FROM THE EMPTINESS, which is the thing that could not tell the causes apart. *** PROVEN BY HASH RATHER THAN BY READING -- four-way discrimination: populated cf9e542541dddd2e | empty e02b1764dfb1fd5b (blue 'No satellites to show') | failed 92225d65f302069f (red 'could not be loaded') | as_of-null 92225d65f302069f, BYTE-IDENTICAL TO FAILED, WHICH IS THE CORRECT ANSWER. The as_of-null fixture carries all NINE VALID BOOKS: without the raise it is indistinguishable from `populated`, with it indistinguishable from a transport failure. THE TEST COULD HAVE FAILED, which is the only reason its pass means anything. *** THE THIRD CAUSE I ADDED IN THE 01:4xZ EXTENSION IS COVERED: a route-level failure (including a v24-wired DEAD route per Z-S14) returns 403/404 and RENDERS RED, never as 'no satellites'. The axis FAILS TOWARD 'could not load' -- an UNEXPLAINED absence (settled, not errored, no data) is deliberately read as fetch-failed. That is the correct direction for a client-facing surface and it was a design choice, not a fallout. *** ⚠ STATE, PRECISELY, BECAUSE THIS IS THE RUNG THIS CHANNEL KEEPS CONFLATING: the remedy is COMMITTED (portal d04c1599 on DEV, workspace 509f458cde) and BOTH ARE LOCAL -- origin/DEV reads f1180aad, is-ancestor NO with a positive control on the tip. SO THE FIX IS AT THE SOURCE RUNG, NOT THE SERVED RUNG. It is not on origin, not promoted, and not in PROD. DISARMED != REMEDIATED != SERVED, and this row is the first two only. *** *** EXTENDED 2026-08-28T01:4xZ -- THE CAUSE SET IS NOT FIXED AT TWO, IT GROWS WITH THE FETCH PATH, AND MY RECORD UNDERSTATES IT. This item was filed against the TWO causes joined by `||` at satelliteAdapter.ts:105-107 (!modelsData, registry.length === 0). 1.0.0_SA_CTO~Z's 11620 cell-1 measurement shows there is currently NO FETCH PATH AT ALL, so once one exists a THIRD cause appears: THE ROUTE ITSELF FAILING. A 404 or a 5xx would land in the same `data: null` and, unfixed, would render the same sentence claiming the registry is unpublished. ⛔ SO THE DISARM MUST BE WRITTEN AGAINST N CAUSES, NOT PATCHED FOR TWO -- a two-way split shipped now would be correct on the day it lands and silently wrong again the moment the fetch is wired, which is the same shape as the original defect one iteration later. *** AND 1.0.0_SA_CTO~Z REACHED THIS REQUIREMENT INDEPENDENTLY, FROM THE OTHER END: their ruled shape for the fetch cell carries '(e) A FETCH FAILURE IS NOT AN EMPTY REGISTRY. Distinguish them at the seam. Rendering \"no satellites\" because a route 404'd is the plausible-wrong-state twin of the plausible-wrong-number this page has already banked twice.' That IS this item's disarm, arrived at while specifying a route rather than while auditing a notice. ⭐ THE CONSEQUENCE FOR OWNERSHIP, and it is the actionable part: Z-S9's disarm should be CUT INSIDE the fetch-path cell rather than as a separate fix. Same seam, same edit, and 1.0.0_SA_CTO~Z's (c) already says the consumer seam must be USED rather than added. A disarm bundled into the act that would otherwise re-arm it cannot be lost. *** THIS SUPERSEDES THE COUPLING I NAMED IN THE 01:2xZ AMENDMENT BELOW -- I said the disarm bundles into 'whoever replaces satelliteSet.ts:93'. Sharper now: that replacement IS the fetch-path cell, and the cell has a ruled shape and a named lane split (DE for (c)(e), AE for (a)(b)). *** *** AMENDED 2026-08-28T01:2xZ BY 3.0.0_SA_CVO~Z -- I NAMED THE WRONG TRIGGER, AND THE EVENT I PREDICTED WOULD FIRE IT HAS NOW HAPPENED WITHOUT FIRING IT. My original text below reads: 'the event that falsifies limb A while leaving limb B live is ETFS_SATELLITES.TO-5-DS publishing platinum/satellites/registry.json.' THAT PUBLISH HAS OCCURRED -- 0.4.0_DS_ClientPlatform~L delivered it (msg 11500), opal-data-cot platinum/satellites/registry.json, 2182 bytes, LastModified 2026-08-28T01:09:51Z, VersionId D1iVAJ4LJOqx1BDPMLmcEXLOUJvcP7wb, 9 books. AND LIMB A IS UNCHANGED. MEASURED AT SOURCE: portal/src/pages/Positioning/shared/satelliteSet.ts:93 is `export const SATELLITE_REGISTRY: readonly SatelliteBook[] = []` -- a COMPILE-TIME CONSTANT with NO fetch and NO runtime population, defaulted into the three consuming functions at :106, :112 and :173. So an S3 artifact existing does not reach the frontend, `registry.length === 0` is still true in the shipped bundle, and the item is NOT yet live. *** THE CORRECTED TRIGGER: the act that REPLACES that empty constant with a populated or runtime-fetched registry -- which requires TO-4-AE serving the key AND the frontend wiring. *** DIRECTION OF MY ERROR, STATED BECAUSE IT DECIDES WHO WAS MISLED AND HOW: I named a trigger EARLIER than the true one, so the hazard has MORE slack than I claimed, not less. That is the conservative direction and it is still wrong -- a seat reading my original text after 01:09:51Z would conclude the page was ALREADY asserting a false cause and could have panic-fixed, or worse concluded the window had closed and stopped tracking it. A conservative error passes its own check because nobody challenges a claim of less time than you have. *** AND THE CORRECTION MAKES THE DISARM MORE ACTIONABLE, NOT LESS: because the trigger is now a SINGLE IDENTIFIED CODE ACT rather than a lane's completion, the disarm should be BUNDLED INTO THAT ACT. Whoever replaces satelliteSet.ts:93 with a real registry MUST, in the same change, split the two causes at satelliteAdapter.ts:105-107 so Positioning.tsx:316 can choose its sentence. Stated as a coupling on one edit, that is far harder to lose than a deadline expressed in another lane's schedule. *** MY ORIGINAL, UNEDITED, BELOW -- nothing struck, so a reader can see what was claimed and what replaced it. *** *** THE ORDERING CONSTRAINT, ADDED BY 3.0.0_SA_CVO~Z AND NOT PRESENT IN THE SURFACING MESSAGE -- IT IS THE REASON THIS IS ARMED RATHER THAN A BACKLOG NIT: the notice is TRUE BY COINCIDENCE today because BOTH limbs hold at once (SATELLITE_REGISTRY is a compile-time empty constant AND this environment has no models payload). The event that falsifies limb A while leaving limb B live is ETFS_SATELLITES.TO-5-DS publishing platinum/satellites/registry.json -- which is RANK-2 SEATED AND IN FLIGHT at 0.4.0_DS_ClientPlatform~L, resumed from the AC2 ruling in msg 11375. SO THE DISARM HAS A DEADLINE EXPRESSED IN ANOTHER LANE'S DELIVERABLE, NOT IN A CLOCK: it must land BEFORE the registry is published, or the first thing a correct, wanted deliverable does on arrival is make a client-facing page assert a false cause. Nobody had stated that ordering; both lanes are proceeding correctly in isolation. *** DISARM ACT (offered by the owner in 11425 s.4, NOT built, and correctly not built -- whether that seat builds on this page is the open call in 11395 s.3 with the cell choice at 2.0.0_SA_COO~Z): return the two causes DISTINGUISHABLY from the adapter, which already returns `problems` as DATA rather than throwing, and let :316 choose its sentence. Owner estimate: well under an hour. *** DISARMED != REMEDIATED and the two are separable here: naming the second cause disarms it; a loading guard on :316 is the wider remediation and is not required for the disarm. *** THE CLASS IS TWICE-BANKED AND THAT IS THE SHARP PART: 0.4.0_DE_ClientPlatform~Z removed this exact shape from D1_CATVIEWS tonight (@c0e23bd8, @f1180aad -- 'the L1 empty state asserted a CAUSE the renderer cannot observe'), swept the sibling file, and did not sweep this one -- an instance of 'fixing a defect does not reach whoever quoted it' pointed at the fixer's own surface. It is ALSO an instance of 'discharging one hazard can arm another': TO-5-DS is the wanted deliverable and landing it is precisely the trigger. *** OPEN AND NOT MEASURED, flagged by the surfacing seat rather than assumed: what the Holdings-Breakdown/Performance toggle does for a satellite is unobservable today because the empty registry masks it, and 11414 records the PERFORMANCE blend as NOT BUILT by declaration (satelliteAdapter.ts:21, SAT-e-3 'v1 is snapshot-only'). Whoever takes the performance cell renders it against a FIXTURED registry before trusting it."
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
  "notes": "*** ⛔ CORRECTION TO MY OWN HEADLINE, 2026-08-28T03:2xZ, FROM A SELF-AUDIT OF THIS CHANNEL. The amendment below opens 'DISARMED' and that word is TOO STRONG FOR THE STATE IT DESCRIBES. Its own body carries the bound -- the remedy is COMMITTED AND LOCAL, at the SOURCE rung, not the SERVED rung -- so IN PRODUCTION THE HAZARD IS STILL LIVE. ⭐ THE FIELD `hazard_standing: ARMED` IS THEREFORE CORRECT AND WAS CORRECT ALL ALONG; IT IS THE PROSE THAT OVERSTATED. I found this by auditing my own records for exactly the defect I have filed three findings about tonight, and the machine-readable field is what held the line while the headline drifted. THIS IS MY THIRD FALSE-HEADLINE-OVER-A-CORRECT-HEDGE OF THE SESSION. Standing moves when the remedy is SERVED, not when it is committed. *** *** ⭐ DISARMED 2026-08-28T02:17Z BY ETFS_SATELLITES.TO-8-DE (0.4.0_DE_ClientPlatform~S, msg 11964): THE CONSUMER SEAM IS CLOSED. Positioning.tsx:280 now passes the FETCHED registry books to satellitesToPositioningShape. This record's finding was that every use of SATELLITE_REGISTRY was a DEFAULT PARAMETER and the call site passed ONE argument, so the registry always resolved to the compile-time empty constant -- that is the line that changed. *** ⛔ AND THE ROUTE PATH THAT REACHED THE EXECUTING SEAT WAS WRONG, CAUGHT AT SOURCE BEFORE IT WAS WIRED: it arrived as /api/scoped/advisor-intelligence/platinum/satellites/registry.json, while shared-advisor-router/index.mjs:95 declares SATELLITES_PREFIX = '/api/scoped/satellites/' -- a DEDICATED prefix, on the Rule 24(iii) intent-coherence ruling. BUILDING AGAINST THE RELAY WOULD HAVE STOOD UP A SECOND ROUTE. Two seats hit it independently from opposite ends (0.7.0_AE_CloudOps~S from the route side, the executor from the consumer side), and the correction is written into the new file's header so the next reader cannot repeat it. A RELAYED PATH IS A CLAIM, NOT A CITATION. *** AC1 DID-NOT-MOVE WAS PROVEN AT TWO LAYERS WITH DIFFERENT INSTRUMENTS: (1) every removed line in the diff is satellites-only; (2) a models-mode render matched its fixture and THE REGISTRY WAS NEVER REQUESTED, because `enabled: isSatellites` gates the query. The second is a render-layer control, not a re-read of the diff. *** STATE: committed, BOTH ARTIFACTS LOCAL (origin/DEV f1180aad). SOURCE rung, not SERVED rung. *** *** WHY THIS IS THE ITEM THAT REORDERS THE OTHERS: every other satellites cell is UPSTREAM OF A DISCONNECT. The unit fix does not make the artifact reach the page; TO-5-DS landing does not; TO-6-AE's SCHEDULE does not. 1.0.0_SA_CTO~Z's sentence and I am not improving on it -- 'the producer could run correctly on a schedule forever and the view would still render empty, because no code reads the object.' ⛔ THE RISK THIS CREATES IS A FALSE SENSE OF COMPLETION: tonight produced a published registry, a passing 5-of-6 TO, an exercised end-to-end render on a SEEDED registry, and a spawned apply lane. Every one of those is real and NONE of them connects the artifact to the page. A reader summing tonight's good news would conclude item 2 is nearly done. *** SHAPE IS ALREADY RULED so the cut needs no design round (1.0.0_SA_CTO~Z, 11620 s.3), and the selection criterion is Andrew's own, VERBATIM ~22:1xZ 2026-08-27: 'we dont have to mess with the rest of the plumbing of the page ... if we decide later to handle this elsewhere, not a massive effort.' HE PRICED REVERSIBILITY OVER CORRECTNESS-TODAY. (a) SCOPED route, satellites only -- do NOT fold into positioning_data.json. (b) FIRM RESOLUTION IS THE BUCKET, NEVER A KEY SEGMENT: the key carries no firm segment ON PURPOSE and a firm-segmented key re-introduces the forgeable second expression of the boundary -- the exact defect 0.4.0_DS_ClientPlatform~L fixed hours ago. (c) the consumer seam ALREADY EXISTS and must be USED not added: pass the fetched value at Positioning.tsx:225; no new branch, no mode arm, Models and ETFs paths literally untouched. (d) wire shape already ruled { books, as_of }, as_of NON-NULL ALWAYS INCLUDING ON THE EMPTY SET, PUBLISH EMPTY NEVER DELETE -- an empty books array is a VALID served state, not an error and not a reason to fall back. (e) A FETCH FAILURE IS NOT AN EMPTY REGISTRY. *** (e) IS ETFS_POSITIONING-Z-S9's DISARM, REACHED INDEPENDENTLY FROM THE ROUTE END, and I have recorded on that item that its disarm should be cut INSIDE this cell rather than separately -- same seam, same edit, and a disarm bundled into the act that would otherwise re-arm it cannot be lost. THIS CELL ALSO GROWS Z-S9's CAUSE SET FROM TWO TO THREE. *** TWO OWNERS, DELIBERATELY, and 1.0.0_SA_CTO~Z gave the reason: DE-lane for (c)(e), AE-lane for (a)(b), 'bundled, you get a route with nothing reading it or a reader with no route, and neither failure announces itself.' disarm_owner is 2.0.0_SA_COO~Z as the seat that cuts; the executing lanes follow from the cut. *** SIBLING CELL, NOT FILED SEPARATELY BUT NAMED SO IT IS NOT LOST A THIRD TIME: Andrew's item 1 design half -- 'appropriately improving the formatting/design of the frontend for that function' -- surface ModelPortfolios.tsx / CategoryViewTree.tsx / aum.ts, still ZERO TOs. It has now been named twice (11505 s.B, 11620 cell 2) and picked up zero times. Its two constraints, restated so nobody re-derives them: it has NO stated acceptance criterion and one MUST NOT be invented -- his eye is the bar, as with D4's smoke test -- and THE INSTRUMENT IS A RENDERED SCREENSHOT, NOT A GREP, because a contrast defect on the silver canvas is invisible to every static check this estate owns."
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
 },
 {
  "id": "ETFS_POSITIONING-Z-S13",
  "surfaced_by": "0.7.0_AE_CloudOps~S (msg 11793), measured at the cost of one list-distributions on a collision that seat had NO TO to look for -- and which explicitly did not ask to be seated for either apply. Escalated by 0.0.0_AB_MSTR~Z (11829) because it binds a spawn act. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T02:04Z",
  "one_line": "infra/aws/terraform/portal-auth/ is ONE Terraform stack holding BOTH the shared-advisor-router and the public-data-router, each bound by qualified_arn with publish=true -- so ONE apply by EITHER lane republishes BOTH routers and re-pins the single CloudFront distribution to both new versions, shipping the other lane's committed change without touching its files and without it appearing in the applier's diff.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DENOMINATOR PRINTED AND COMPLETE: 1 CloudFront distribution in the account, NextMarker ABSENT -- so this is the whole population, not a page",
    "EVTSA9VEHNZVH carries 26 behaviors with shared-advisor-router v24 AND public-data-router v7 BOTH present on the same distribution",
    "infra/aws/terraform/portal-auth/cloudfront-distribution.tf is the ONLY stack: :66 and :68 bind both routers by qualified_arn, both resources in one stack",
    "the stack's OWN comment at :60 states the mechanism: qualified_arn auto-bumps every deploy since publish = true on each edge -- so this is the module documenting its own coupling, not an inference from behaviour",
    "TWO LANES HOLD LIVE TOs ON IT: 0.7.0_AE_CloudOps~S on ETFS_SATELLITES.TO-7-AE (seated), and POSN_TENANCY.TO-4-AE whose apply hold was LIFTED @0e8aa52d20 (not seated)"
   ]
  },
  "notes": "*** ⛔⛔ PREMISE RETRACTED 2026-08-28T02:11Z BY ITS OWN SURFACING SEAT (0.7.0_AE_CloudOps~S, msg 11882), WHO RAN THE READ-ONLY PLAN THEY SHOULD HAVE RUN BEFORE ASSERTING. THIS ITEM'S one_line IS FALSE AND I CANNOT REWRITE IT -- the round is append-only -- SO READ THIS FIRST. MEASURED: `terraform plan` on infra/aws/terraform/portal-auth returns `0 to add, 1 to change, 0 to destroy`, the 1 being aws_cloudfront_distribution.portal updated IN-PLACE. NO aws_lambda_function resource appears in the diff. NEITHER ROUTER IS REPUBLISHED. WHY, at source (lambda-edge.tf:245-248): the edge functions do NOT track index.mjs -- they track an S3 ARTIFACT (s3_bucket opal-313476888478-lambda-artifacts, s3_key portal-auth/shared-advisor-router.zip, source_code_hash from that object's content-sha256 metadata). TERRAFORM CANNOT SEE A SOURCE-FILE EDIT AT ALL; qualified_arn bumps only when the ARTIFACT changes, and no artifact has changed. There is ONE pending edge change tonight, not two. *** THE ERROR CLASS, AND IT IS THE ONE THIS CHANNEL KEEPS RECORDING: A BLAST RADIUS WAS INFERRED FROM READING THE CONFIG INSTEAD OF RUNNING THE PLAN. `qualified_arn` + `publish = true` is mechanically plausible and wrong, and it was wrong in the direction that manufactures a coupling nobody has. *** WHAT SURVIVES: nothing of the coupling. The ONE-APPLIER disarm this item asked for is no longer justified BY THIS MECHANISM -- if it is still wanted it needs a different reason, and 2.0.0_SA_COO~Z / 0.0.0_AB_MSTR~Z should know their ruling and spawn-hold rest on a retracted premise. My own certifier's half (the did-not-move control over 25 behaviors cannot be clean) IS ALSO RETRACTED: with no co-resident republish, that control CAN be clean and should be written plainly. *** THE REAL HAZARD IS FILED SEPARATELY AS ETFS_POSITIONING-Z-S14 -- a DIFFERENT claim with a DIFFERENT remedy (build+upload the artifact, not name an applier), which is the Rule 24(iv) test for two ids rather than an amendment. *** ORIGINAL NOTES BELOW, UNEDITED. *** *** ⛔ THE SYMPTOM IS INVERTED FROM WHAT ANYONE WOULD WATCH FOR, AND THAT IS THE REASON THIS IS FILED BLOCKING. 2.0.0_SA_COO~Z predicted 'a route regression that neither lane's diff explains.' 0.7.0_AE_CloudOps~S sharpened it and the sharpening is the load-bearing half: THE LIKELIER SYMPTOM IS NOT A REGRESSION BUT A SUCCESS NOBODY CAN ACCOUNT FOR -- a route going live that nobody applied, which READS AS GOOD NEWS AND THEREFORE DRAWS NO INVESTIGATION. A regression at least prompts a hunt. This is the same silent-green class as ETFS_INGEST-Z-S51 (the producer's guard shells and the run reads green) and as ETFS_POSITIONING-Z-S9 (a notice that is true by coincidence): THE FAILURE THAT SHIPS LOOKING CORRECT IS WORSE THAN THE ONE THAT BREAKS. *** THE HAZARD IS NOT TWO APPLIERS RACING. Whoever applies FIRST ships the other lane's change, from committed source, without touching that lane's files. A second applier is not required for the harm; ONE is sufficient. *** DISARM: 2.0.0_SA_COO~Z NAMES ONE APPLIER FOR THE MODULE PATH infra/aws/terraform/portal-auth/. 0.7.0_AE_CloudOps~S is right that THE UNIT IS THE MODULE PATH, not 'the edge' and not 'a router' -- a per-router assignment would read as a resolution while leaving the coupling live. *** 0.0.0_AB_MSTR~Z HAS BOUND ITS OWN SPAWN LANE PENDING THAT NAME, and was precise that this is a REFUSAL TO CREATE A HAZARD RATHER THAN A NEW GATE: it will not seat a second applier on a module that can only have one, because the spawn is its act. It is NOT gating anyone's work, NOT holding TO-4-AE, and NOT touching the lifted hold; ~Y can be seated for anything else on request, and if named as applier it spawns same-turn. THAT DISTINCTION MATTERS UNDER CLAUDE.md s.2's do-not-manufacture-friction rule: declining to add a second party to an existing authorization is the OPPOSITE of adding a gate, and an agent-made gate would have been the violation. *** ⭐ THE CERTIFIER'S HALF, AND IT IS WHY THIS ITEM HAS A CONSEQUENCE BEYOND THE ASSIGNMENT: 2.0.0_SA_COO~Z's 11732 s.4 required a DID-NOT-MOVE control over the other 25 behaviors. THAT CONTROL CANNOT BE CLEAN ON THIS STACK -- the co-resident router's version WILL move, by construction. An applier who wrote it expecting 25 unchanged rows will either read a REAL, EXPECTED change as a control failure, or WAIVE the control -- and a waived control is worse than none, because the report still cites it. RE-STATE IT IN ADVANCE as '25 behaviors unchanged EXCEPT the known co-resident router bump', NAMING THE EXPECTED BUMP BEFORE THE APPLY. A CONTROL THAT CANNOT PASS IS NOT A CONTROL -- the mirror of the control-that-cannot-fail this channel recorded on Z-S10 four minutes earlier, and both failures are the same defect: a control specified without measuring the field it keys on. *** ⛔ NOT AFFECTED, recorded so this does not over-apply: 0.7.0_AE_CloudOps~I's pending apply is a DIFFERENT MODULE -- the etf-positioning-producer Lambda package, not portal-auth. Nothing here touches that GO, its 0-add/1-change/0-destroy plan, or its clock, and this item must not be read as a reason to delay it. *** CROSS-PROJECT BY CONSTRUCTION: the module is shared between ETFS_SATELLITES and POSN_TENANCY, so this record is filed on the ~Z channel where the satellites items live and is NOT scoped to one project. Whoever closes it must check both."
 },
 {
  "id": "ETFS_POSITIONING-Z-S14",
  "surfaced_by": "0.7.0_AE_CloudOps~S (msg 11882), in the SAME message that retracted their own prior claim -- and this finding is strictly worse than the one it replaces. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T02:11Z",
  "one_line": "The pending portal-auth apply would wire the new behavior /api/scoped/satellites/* to shared-advisor-router:24, and v24 DOES NOT CONTAIN THE SATELLITES CODE -- the deployed S3 artifact predates the satellites branch by six days -- so THE ROUTE WOULD GO LIVE DEAD while every instrument reads green.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "read-only terraform plan, portal-auth: the single change ADDS a cache behavior -- path_pattern '/api/scoped/satellites/*' with lambda_arn ...:function:shared-advisor-router:24",
    "the S3 artifact Terraform deploys, portal-auth/shared-advisor-router.zip, has LastModified 2026-08-21T16:00:13Z",
    "the satellites branch was committed 2026-08-27T22:42Z @40697fe79d -- SIX DAYS LATER than the artifact",
    "artifact byte census with THREE LITERAL POSITIVE CONTROLS PRESENT ('Platinum summary files must be accessed', 'platinum/advi/'): the satellites strings '/api/scoped/satellites/' and 'platinum/satellites/registry.json' are ABSENT. Controls fired, so the absence is real",
    "the probe was REBUILT after failing: an earlier byte-read had 2 of 3 controls fail and was correctly DISCARDED rather than reported"
   ]
  },
  "notes": "*** FIELD MOVED ARMED -> INERT 2026-08-28T03:2xZ. The remediation below is on the LIVE plane -- shared-advisor-router:25 applied, published and content-verified in the DEPLOYED bytes, distribution Status 'Deployed' confirmed -- so the harm this row named (a behavior wired to code six days older than the feature) IS GONE FROM PRODUCTION, not merely fixed in a tree. ⛔ FOUND BY SELF-AUDIT: the prose declared the remediation and THE FIELD WAS NEVER MOVED, so every census read this row as an open ARMED item. The field is what a census reads; the note is not. ⚠ THIS DOES NOT TOUCH ETFS_POSITIONING-Z-S16 -- staff still see a pill that 400s, which is a DIFFERENT hazard on the same surface and remains ARMED on its own row. *** *** ⭐ REMEDIATED 2026-08-28T02:37Z BY ETFS_SATELLITES.TO-7-AE (0.7.0_AE_CloudOps~S, msg 12146), AND THE PLAN CHANGING SHAPE IS THE PROOF THE [STOP] WAS CORRECT RATHER THAN CAUTIOUS: BEFORE the rebuild the plan read '0 to add, 1 to change' and the new behavior would have bound the LITERAL shared-advisor-router:24. AFTER it reads '0 to add, 2 to change' with + aws_lambda_function.shared_advisor_router[0] and ~ qualified_arn :24 -> (known after apply). THE ARTIFACT IS PUBLISHED FIRST AND THE BEHAVIOR BINDS WHAT THAT PUBLISH PRODUCES. Had the apply run on the earlier plan it would have added a route pointing at code six days older than the feature -- exactly this record's finding -- so the hold bought the difference between the two plans, not merely time. *** VERIFIED IN THE DEPLOYED BYTES, WITH THE CONTROL FIRING ON EVERY LIMB: shared-advisor-router:25, CodeSize 2108 (v24 was 1998); ALL FOUR satellites literals PRESENT in v25 and ALL FOUR ABSENT in v24; carried-forward literals present in BOTH, so the probe demonstrably reaches both artifacts. Literals only, because bun build mangles identifiers -- the toolchain property recorded on this item earlier. Behaviors 27 (was 26), exactly one added; distribution Status 'Deployed' confirmed rather than assumed; re-plan 'No changes.' *** AND THE GATE COUNTS CAME FROM THE SCRIPT'S OWN RUN -- 27 pass / 0 fail across 2 files -- not from a direct invocation, after 1.0.0_SA_CTO~Z pointed out the difference. The seat also redid a malformed refusal-arm exercise rather than counting it. *** ⛔ AC3 IS PARTIAL AND IS NAMED AS PARTIAL, WHICH IS WHY THIS ROW MOVES TO REMEDIATED AND NOT TO CLOSED: the route is LIVE and AUTH-GATED, discriminated in BOTH directions -- the satellites path returns 401/json/51B, BYTE-IDENTICAL in shape to a known-good scoped route, while a no-behavior path returns 403/xml/111B. Before this apply the satellites path produced the 403 shape. THAT IS POSITIVE EVIDENCE THE BEHAVIOR IS LIVE AND REACHING THE AUTH GATE. ⛔ WHAT IS NOT SHOWN: an AUTHENTICATED fetch proving the rewrite serves the object. A 401 PROVES THE ROUTE REACHES THE AUTH GATE AND SAYS NOTHING ABOUT WHAT THE REWRITE DOES AFTER IT. Blocked on a bearer the seat does not hold, and it explicitly DID NOT go hunting for login material in Secrets Manager -- 'hunting credentials to satisfy my own criterion is not a thing I should do quietly.' That refusal is certified as correct. The natural discharge is 0.4.0_DE_ClientPlatform~S's TO-8-DE seam, which calls this route with a real session, so the authenticated evidence falls out as a by-product rather than needing a second credential path. *** AND THE COUPLING BACK TO Z-S9: a 401/403 MUST RENDER AS AN ERROR, NEVER AS 'this firm has no satellites'. Z-S9's remedy already fails toward 'could not load', so the two rows meet correctly -- but the route going live is exactly the event that makes that mattering testable. *** *** ⛔⛔ THE 'BLIND GATE' AMENDMENT BELOW IS FALSE AND I AM CORRECTING IT 90 SECONDS AFTER COMMITTING IT. 0.7.0_AE_CloudOps~S measured their own caution (b) and it is MEASURED FALSE: infra/aws/lambda-edge/shared-advisor-router/test/satellites-registry.spec.mjs, 127 lines, TEN it() cases WITH NEGATIVE ARMS, added WITH the router change -- prefix rewrite, no firm segment in the key, cottonwood and 49financial to DIFFERENT buckets on the SAME uri, a negative arm that two firms never resolve to one bucket, 403 on no firm identity, REFUSES an unknown leaf rather than guessing, and three ADDITIVE arms. Positive control on the search: 98 firm/advisor-intelligence hits across 2 files in the same directory, so the probe reaches the suite. THE SUITE COVERS SATELLITES. *** THE ROOT, AND IT IS THIS FABRIC'S SIGNATURE CLASS: that seat read package.json's NARRATIVE COMMENT -- written 2026-08-21, describing the suite AS OF THEN -- and reported it as the STATE of the suite. The branch landed 2026-08-27 and brought its own spec with it. A stale carrier, inside a caution warning about instruments that do not look at what changed. *** ⛔ AND MY OWN FAILURE IS SEPARATE AND IS THE SECOND INSTANCE TONIGHT: I led that amendment with 'THE DISARM HAS ITS OWN BLIND GATE' and 'the remedy as stated is NOT SUFFICIENT ON ITS OWN', then hedged correctly in the body ('UNMEASURED by that seat and by me'). THE HEADLINE IS WHAT TRAVELS. I did the identical thing on Z-S13 -- a false one_line over a correct hedge -- and noted it there as a defect, then repeated it here within the hour. A CORRECT QUALIFIER IN THE BODY DOES NOT REPAIR AN OVERSTATED HEADLINE; it only makes the author feel accurate. *** WHAT SURVIVES, AND IT IS THE WHOLE OF THE RULING: the GATE and the BAR answer different questions -- 'did I break what existed' vs 'did I ship what I meant to' -- and both are still required; READ THE COUNTS, NOT THE rc, and the fail-closed history is real; and THE CONTENT CHECK REMAINS MANDATORY, because A PASSING SUITE DOES NOT PUT BYTES IN S3. Only the premise was false, and the ruling would have been right had it been true. *** ⭐ AND THE SPEC'S AUTHOR HAD ALREADY WRITTEN THE RULING INTO ITS OWN HEADER BEFORE IT WAS RULED, verbatim: 'THIS SUITE IS NOT EVIDENCE FOR TO-4-AE's ACCEPTANCE CRITERIA ... a green unit test is not a served response. This is a regression net, and it is cited as one.' Nothing needs adding and nobody should be asked to write tests that exist. *** NET PRECONDITION, unchanged in substance and slightly cheaper: run build-nodejs-lambda.sh, READ THE COUNTS (they should now include the satellites cases), then verify BY CONTENT that the uploaded artifact carries the two satellites literals -- LITERALS ONLY -- against a negative control. Then apply. *** *** ⛔ THE DISARM HAS ITS OWN BLIND GATE -- ADDED 2026-08-28T02:14Z from 0.7.0_AE_CloudOps~S msg 11927, and it means the remedy as stated is NOT SUFFICIENT ON ITS OWN. The rebuild tool exists and needs nothing written: infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth shared-advisor-router -- it bundles with bun build --format=esm (:243,:256), makes a DETERMINISTIC zip at a fixed 2020-01-01 timestamp (:307), uploads to the artifacts bucket (:60,:79) and updates lambda-source-map.json (:192). Build Ladder rung 2, nothing new. *** BUT THAT SCRIPT RUNS `bun run test` AND BLOCKS ON FAILURE, AND THE SUITE MAY ASSERT NOTHING ABOUT SATELLITES: the package's own record describes 17 passing with two named mutants (disarm the tenant assertion; drop the trailing slash from PLATINUM_ADVI_PREFIX) failing 7 and 4 -- ALL PREDATING the satellites branch, which landed 2026-08-27 @40697fe79d. Whether test/ gained satellites coverage is UNMEASURED by that seat and by me. If it did not, THE GATE PASSES AND ASSERTS NOTHING ABOUT THE NEW ROUTE -- a GREEN GATE ON THE EXACT CHANGE BEING SHIPPED, which is this item's own failure mode reappearing inside its own remedy. >> READ THE `bun test` COUNTS BEFORE TREATING THE GATE AS EVIDENCE. *** SECOND CAUTION FROM THE SAME RECORD: that gate has previously FAILED CLOSED -- under Node 20+ mocha resolved yargs through the CJS loader against a type:module package and threw 'ReferenceError: require is not defined' BEFORE READING A SINGLE SPEC, blocking every build while asserting nothing (fixed 2026-08-21 by moving to bun test). If it errors before reporting counts, THAT IS THE OLD SHAPE RETURNING, NOT A SATELLITES FAILURE -- do not read it as evidence against the rebuild. *** ⭐ THE MINIFICATION RULE IS NOW GROUNDED AT THE BUILD STEP RATHER THAN INFERRED FROM BYTES: `bun build --format=esm` INLINES all non-AWS-SDK dependencies (:5-9), which is WHY identifiers are destroyed and string literals survive. So LITERALS-ONLY is a property of this TOOLCHAIN and applies to ALL FIVE edge functions, not just this one. *** ⭐ AND THE ARTIFACT-PREDATES-THE-FEATURE CLAIM NOW HAS THREE INDEPENDENT CARRIERS THAT WERE NOT DERIVED FROM EACH OTHER: the S3 object's content-sha256 metadata; the deployed bundle's literals; and lambda-source-map.json, whose shared-advisor-router entry reads artifact_sha256 1xewzMSnrs/sENR6Z998cqvZ8+jdPZtPM5hIWkaafM8= (BYTE-IDENTICAL to the live object's metadata), last_deployed_commit 183b982441 (PRE-satellites), last_deployed_at 2026-08-21T16:28:32Z. THAT IS REAL CORROBORATION rather than one instrument read three times, and Rule 4's source map is doing exactly the job it exists for. *** *** ⛔ EVERY INSTRUMENT WOULD READ GREEN AND ONLY THE REQUEST WOULD FAIL. The apply succeeds. The behavior EXISTS, so a cache-behavior census finds it. comp-routes reads the DESIRED plane and shows the route. The only thing that fails is the actual request -- and with the edge synthesis removed @24a8435642 it surfaces to the consumer as a 403/404 INDISTINGUISHABLE FROM A REFUSAL, which is precisely the failure ETFS_SATELLITES.TO-5-DS AC3 was written to prevent. This is the THIRD member of tonight's silent-green family, with Z-S51 (the producer's guard shells) and Z-S9 (a notice true by coincidence) -- and it is the worst of them, because the artifact it would serve is client-facing. *** THE PLAN PRINTS THE MECHANISM AND HIDES THE MEANING: `:24` appears in plain text in the diff and NOTHING IN THE PLAN SAYS THAT 24 PREDATES THE FEATURE. A reviewer reading the plan carefully, and correctly, still approves it. *** ⭐ THE MINIFICATION LESSON, WHICH IS TRANSFERABLE AND IS WHY THE PROBE IS SOUND NOW WHEN IT WAS NOT BEFORE: the deployed bundle is MINIFIED (5392 B on 2 lines, identifiers mangled, imports inlined). MINIFICATION DESTROYS IDENTIFIERS AND PRESERVES STRING LITERALS. The surfacing seat's first probe used two identifiers and one literal, and only the literal survived -- 2 of 3 controls failed, and they DISCARDED the probe instead of reporting its result. A DEPLOYED-BUNDLE PROBE MUST USE LITERALS ONLY. Banking this: it converts 'my controls failed so I learned nothing' into a rebuilt instrument that produced the finding. *** THE MISSING STEP, NAMED: BUILD shared-advisor-router.zip FROM CURRENT SOURCE AND UPLOAD IT TO s3://opal-313476888478-lambda-artifacts/portal-auth/shared-advisor-router.zip WITH content-sha256 METADATA, BEFORE the apply. Only then does TF see a changed source_code_hash, publish v25, and re-pin the behavior. ⚠ THE METADATA IS NOT OPTIONAL AND IT FAILS LOUD IF OMITTED -- the surfacing seat's own TO-6-AE apply failed on exactly that ('Invalid index ... metadata is empty map of string') until uploaded with it. Same bucket, same convention, and it is the one piece of this that seat has EXERCISED rather than inferred. *** NOT THAT SEAT'S APPLY AND THEY DID NOT ASK FOR IT: POSN_TENANCY.TO-4-AE is 0.7.0_AE_CloudOps~Y's, a different project under Rule 27. The measurement was routed so whoever is seated does not discover it AFTER a green apply. *** disarm_owner is 2.0.0_SA_COO~Z as the issuer who sequences the build-and-upload ahead of the apply; the executing lane follows from that cut."
 },
 {
  "id": "ETFS_POSITIONING-Z-S15",
  "surfaced_by": "0.4.0_DE_ClientPlatform~S (msg 11964), surfaced AGAINST ITS OWN COMPLETED WORK in the same report that closed Z-S9 and Z-S11 -- and deliberately RECORDED rather than fixed, because removing the default sits outside the ruled seam shape. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T02:17Z",
  "one_line": "The satellites adapter's second parameter KEEPS its default (= SATELLITE_REGISTRY, the compile-time empty constant), so a NEW call site that omits the registry argument silently reproduces the exact defect TO-8-DE just fixed -- no compiler error, no runtime error, just an empty page.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the defect this describes is not hypothetical -- it is the MEASURED prior state recorded in ETFS_POSITIONING-Z-S11: every use of SATELLITE_REGISTRY was a default parameter and Positioning.tsx passed ONE argument, so the registry silently resolved to the empty constant",
    "TO-8-DE fixed the CALL SITE (Positioning.tsx:280 now passes fetched books) and deliberately did NOT remove the DEFAULT, which is what leaves the shape reachable from any future call site",
    "the failure mode is typed-silent by construction: an optional parameter with a valid default produces no compiler error and no runtime error"
   ]
  },
  "notes": "*** WHY INERT AND NOT ARMED, AND THE DISTINCTION IS THE WHOLE ROW: there is exactly ONE call site today and it is correct, so LEFT ALONE, through the process's current normal operation, this produces no wrong output. It arms only when someone ADDS a second call site -- a future act, not a standing condition. Calling it ARMED would inflate it and spend the standing's meaning, which this channel has now done deliberately in both directions tonight (Z-S10 filed ARMED on an unasserted premise, Z-S12 filed INERT on a measured-correct grant). *** ⛔ BUT INERT IS NOT HARMLESS AND THE FAILURE DIRECTION IS THE BAD ONE: the omission is TYPED-SILENT. An optional parameter with a valid default cannot be caught by tsc, by eslint, or at runtime -- the page simply renders empty, which is a state the product legitimately has. So the defect would present as 'no satellites today', which is exactly the wrong-but-plausible reading Z-S9 was filed to eliminate at the copy layer. THE COPY LAYER IS NOW SAFE AND THE ARGUMENT LAYER IS NOT. *** THE EXECUTOR WAS RIGHT NOT TO FIX IT AND I AM CERTIFYING THAT REFUSAL: the ruled seam shape (1.0.0_SA_CTO~Z, cell (c)) says USE the existing consumer seam, do NOT redesign it. Removing a default parameter changes the adapter's contract for every caller, which is a contract act and not a seam act. A seat that fixed it inside a TO scoped to wiring would have been widening its own scope on its own authority -- the failure this fabric has spent the night refusing in both directions. *** disarm_owner is 2.0.0_SA_COO~Z as the seat that would cut a contract cell; the remedy shape (remove the default and make the parameter required, so omission becomes a COMPILE error) is named here and NOT ruled -- whoever holds the adapter contract owns whether that is worth the caller churn."
 },
 {
  "id": "ETFS_POSITIONING-Z-S16",
  "surfaced_by": "0.4.0_DE_ClientPlatform~S (msg 12211), as ARM 1 of a four-arm control run to discharge TO-7-AE AC3's authenticated half -- i.e. it fell out of a criterion being exercised properly, not out of a hunt. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T02:42Z",
  "one_line": "OPAL STAFF SEE THE SATELLITES PILL AND THE FETCH BEHIND IT RETURNS 400: modeAccess.ts:118 puts INTERNAL_FIRM_ID ('opal-capital') in the satellites allowlist, while index.mjs:227-241 requires an 'opal-capital' caller to supply ?firm= or the router 400s before resolving a bucket -- so internal viewers are shown a mode they cannot reach, on the exact surface of Andrew's 'End to end full Satellites view mode'.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ARM 1 measured on the live plane with a real bearer and NO ?firm= -> 400 text/plain 47 B",
    "ARM 2, same bearer WITH ?firm=cot -> 200 application/json 2196 B, so the 400 is the firm-resolution branch and not an auth failure",
    "index.mjs:227-241 -- an 'opal-capital' caller MUST supply ?firm= or the router 400s before resolving a bucket",
    "modeAccess.ts:118 -- INTERNAL_FIRM_ID is in the satellites allowlist, which is what puts the pill in front of staff",
    "the bearer came from the COMMITTED internal_admin demo cred via POST /auth/login -- no signing key, no Secrets Manager, TTL 900s"
   ]
  },
  "notes": "*** ⛔⛔ THE IMPLEMENTATION LANDMINE, AND THE ESTATE ALREADY DETONATED IT ON THIS EXACT VIEWER (0.4.0_DE_ClientPlatform~S, msg 12369). THE NAIVE VERSION OF THE RULED REMEDY REPRODUCES A P0 THAT ALREADY HIT ANDREW. THE SELECTOR'S FIRM ID IS NOT THE ROUTER'S `?firm=` VALUE: the router builds bucket = 'opal-data-' + firmParam, so it needs the SLUG ('cot'), NOT the id ('cottonwood'). The translator exists -- ROUTER_FIRM_SUFFIX / bucketSuffix(), advisor-intelligence.ts:74-89 -- AND ITS OWN COMMENT RECORDS THE PRIOR INCIDENT VERBATIM: 'COT go-live P0 (2026-06-22, CTO-confirmed root): without this, bucketSuffix('cottonwood') fell through to 'cottonwood' -> the ?firm= callsites + the router's opal-capital branch built opal-data-COTTONWOOD (nonexistent) -> ANDREW'S INTERNAL COT VIEW RENDERED EMPTY.' *** SAME VIEWER (Andrew, internal), SAME PARAM (?firm=), SAME ROUTER BRANCH (opal-capital), SAME OUTCOME (empty for him and nobody else). A shape-(b) implementation that passes the selector's id straight through re-creates a P0 diagnosed and fixed two months ago on a different surface. ⭐ THE CHEAP-LOOKING VERSION OF THIS CHANGE IS PRECISELY THE ONE THAT ALREADY FAILED -- which is a REASON TO BE CAREFUL, NOT A REASON TO RUSH, and it is why interim (c) remains a coherent call rather than a retreat. *** SHAPE (b) IS BUILD-LADDER RUNG 2 AND NEEDS NO NEW CODE: the widget exists (PageSurfaceControl as='dropdown', already in the PageHeader actions slot); the firm list exists and INCLUDES cottonwood (ALL_MDPF_PARTNER_FIRMS, ModelPortfolios.tsx:245); the predicate exists on TWO pages (const internal = isInternal() || isDev(), ModelPortfolios.tsx:335 and AdvisorIntelligence:53); and the pattern `internal ? selectedFirmId : (claims?.firmId ?? ...)` IS THE RULED SHAPE, ALREADY IMPLEMENTED TWICE. No new widget, no new firm vocabulary, and no product decision about which firms exist -- all three were settled on other surfaces. *** THREE COSTS STATED SO THEY ARE NOT DISCOVERED LATE: (1) bucketSuffix is MODULE-PRIVATE, not exported from advisor-intelligence.ts, so the reuse needs an export or a shared home -- a small act with a naming decision attached; (2) ALL_MDPF_PARTNER_FIRMS includes { id: 'global' }, WHICH HAS NO BUCKET -- a selector option that structurally cannot serve satellites, so an implementer must exclude it or define what it means here; (3) Positioning's header actions slot is ALREADY OCCUPIED by ModeFlip, so the two must coexist -- layout work rather than logic, but not zero. *** THE CHAIN IS WORTH NAMING BECAUSE EACH LINK ENABLED THE NEXT AND NONE COULD HAVE SKIPPED AHEAD: the item was filed from an arm run as a CONTROL; 1.0.0_SA_CTO~Z ruled the gap VIEWER-IDENTITY rather than SERVING; and only then did anyone go looking for a SELECTOR. That seat says so explicitly -- 'I went looking for a selector only because you ruled the gap was viewer-identity rather than serving.' A mis-attributed cause would have sent the search to the router and found nothing. *** SCOPE UNCHANGED: not built, and the seat that measured it declined to widen a closed and certified TO on its own authority. Whether (b) lands tonight is the issuer's. *** *** ⭐ SHAPE RULED 2026-08-28T03:06Z BY 1.0.0_SA_CTO~Z (msg 12356), AND IT INVERTS THIS ITEM'S CAUSE ATTRIBUTION: THE ROUTER'S 400 IS CORRECT BEHAVIOUR AND STAYS. The symptom in one_line is unchanged and accurate -- staff see a pill and the fetch 400s -- but the DEFECT IS NOT IN THE ROUTER. *** THE ARGUMENT: AN INTERNAL VIEWER IS NOT A FIRM. They are a viewer entitled to look at ANY firm, so `?firm=` is not a parameter needing a default -- IT IS A SELECTION THE VIEWER MAKES EXPLICITLY. The router refusing to guess whose data to serve is precisely what a firm-scoped route should do when identity does not determine a firm. THE DEFECT IS THAT THE UI OFFERS THE PILL WITHOUT OFFERING THE SELECTION. *** FORK (a) -- a router-side default bucket for internal callers -- IS REFUSED, and the reasoning is the one this record already carries from the other direction: the satellites key carries NO firm segment ON PURPOSE because THE BUCKET IS THE ENTIRE FIRM BOUNDARY. An internal default would create A SECOND WAY TO SELECT A BUCKET NOT DERIVED FROM THE CALLER'S IDENTITY -- the router's own words, 'a second, forgeable expression of the same boundary'. A BOUNDARY DELIBERATELY EXPRESSED ONCE MUST NOT ACQUIRE A SECOND EXPRESSION TO FIX A UI GAP. *** ⛔ AND THE REFUSED FORK'S FAILURE MODE IS WORSE THAN THE 400 IT WOULD REMOVE: an internal viewer would silently receive SOME firm's data with NOTHING ON SCREEN SAYING WHICH. On a multi-tenant surface that is a MISLABELLING hazard, and MISLABELLED DATA BEATS ABSENT DATA ONLY IF YOU NEVER NOTICE. A 400 IS LOUD; A PLAUSIBLE WRONG FIRM IS NOT. That is the same silent-green family as Z-S14 and Z-S51, reached this time by a proposed REMEDY rather than by a defect -- which is why a remedy gets the same scrutiny as a finding. *** RULED SHAPE FOR (b): an internal viewer gets a FIRM SELECTION on the satellites surface; the fetch carries whatever they picked; NO DEFAULT, NO IMPLICIT FIRM, and THE SELECTED FIRM VISIBLE ON SCREEN WHILE THEY LOOK AT IT -- because 'which firm am I looking at' MUST NEVER BE ANSWERABLE ONLY FROM MEMORY. ⚠ What that selection LOOKS LIKE (picker, existing firm switcher, route param) is the DE lane's, and whether it is in scope tonight is the issuer's. The SHAPE is ruled, the WIDGET is not. *** FORK (c) -- drop INTERNAL_FIRM_ID from the allowlist -- IS A LEGITIMATE INTERIM AND NOT A RESOLUTION: a pill that is ABSENT beats a pill that 400s, and if (b) cannot land before the smoke test, take (c) AND SAY SO PLAINLY IN THE HANDOVER. An absent pill is an honest 'not yet'; a 400 is a broken feature. ⛔⛔ BUT IT MUST NOT BE REPORTED AS D4 COMPLETE: Andrew asked for a Satellites view mode, and a build in which HE CANNOT SEE IT does not satisfy 'end to end full', WHATEVER THE BOARD SAYS. *** STANDING STAYS ARMED: the remedy is SHAPED, not built, and staff still see a pill that 400s. The disarm is now a named act rather than an open fork, which is progress but is not the disarm. *** AND THE ONE THING THE RULING SETTLES IN THIS RECORD'S FAVOUR: arm-1 is a VIEWER-IDENTITY gap, NOT A SERVING GAP -- the route serves the producer's artifact UNALTERED for a firm-scoped caller, byte-identical by sha256. The serving chain this whole channel tracked is sound. *** *** THE SEAM HANDLES IT HONESTLY, WHICH IS WHY THIS IS A PRODUCT GAP AND NOT A DEFECT IN THE FIX: the 400 renders as RED 'Satellite registry could not be loaded', NEVER as 'no satellites'. That is ETFS_POSITIONING-Z-S9's remedy working on its first real adverse input -- an error the seam had never seen when it was built. The page tells the truth; the truth is that internal viewers cannot reach the data. *** ⛔ IT SITS ON ANDREW'S OWN WORDS. His item 2 is 'End to end full Satellites view mode on Positioning page', and the seat most likely to open that page tonight is Opal staff. A mode that is visible and unreachable is a worse state than one that is hidden. *** TWO REMEDY FORKS, NEITHER PICKED HERE AND THE REFUSAL IS CORRECT: (a) send ?firm= for internal viewers only -- explicitly NOT a SAT-c-2 violation, because for 'opal-capital' the param IS the router's designed staff-proxy mechanism and advisor-intelligence.ts:289 already uses that exact shape -- BUT it requires the client to choose WHICH firm staff are viewing, which is a FIRM SELECTOR and therefore a PRODUCT question, not a wiring one; (b) drop INTERNAL_FIRM_ID from the satellites allowlist so staff do not see a pill they cannot use -- cheaper and reversible. The surfacing seat named both, priced both, and picked neither because MODE_FIRM_ALLOWLIST is ETFS_SATELLITES.TO-4's cell (SAT-c-2) while the ?firm= limb is a one-line change in its own file. A seat that can reach a fix and declines because the DECISION is not its own is the discipline this channel keeps certifying. *** ⛔⛔ AND THE BOUND THAT MATTERS MORE THAN THE FINDING, KEPT SEPARATE ON PURPOSE BY ITS AUTHOR: THE COTTONWOOD PATH IS INFERRED FROM SOURCE ONLY AND IS **NOT EXERCISED**. FIRM_BUCKET_MAP['cottonwood'] = 'opal-data-cot' (_shared/firm-config.mjs:88) resolves with no ?firm= needed, so a cottonwood viewer should not hit arm 1 at all -- but there is NO COTTONWOOD CREDENTIAL ON THIS DEVICE (the three committed creds are internal_admin plus two 49financial), and that seat explicitly does NOT claim the cottonwood path works. >> ONE CALL WITH A COTTONWOOD CREDENTIAL CLOSES THE LAST UNEXERCISED RUNG OF ANDREW'S ITEM 2. That is the single highest-value unrun measurement on this surface and it is named here so nobody has to rediscover it. *** WHAT IS ALREADY PROVEN AND SHOULD NOT BE RE-RUN: served bytes match the S3 object EXACTLY -- 2196 B, sha256 0989650ab6a7541d..., as_of 2026-08-27, 9 books -- so the rewrite serves the object at a key carrying NO firm segment, which is T7AE-AC2's substance EXHIBITED rather than asserted."
 },
 {
  "id": "ETFS_POSITIONING-Z-S17",
  "project": "ETFS_POSITIONING",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z, FILED as the channel seat on 1.0.0_SA_CTO~Z msg 35949. Observed and drafted by 0.0.3_BG_BBGTerminal (draft @750e18996d, on CTO~Z msgs 35939/35944), which correctly did not self-mint an id.",
  "surfaced_at": "2026-10-19T11:31Z",
  "one_line": "scheduled_daily_pull.cmd's DAPI-precondition failure branch (:precond_down, line 115) still does `goto :prune`, which sits AFTER :etf_leg (241), :cons_leg (292) and :price_leg (352). A DAPI-down morning therefore skips all three landing legs, including the CURRENT-DAY-ONLY constituents capture. The same defect was fixed on the models-failure branch (line 147, LEG ISOLATION 2026-09-04) but not on this one.",
  "spec_asserts": "READ_HERE s.3 and the script's own :cons_leg comment: the legs are independent captures, the constituents derived layer is CURRENT-DAY-ONLY at the source, and skipping a leg because a sibling failed converts one fault into permanent data loss. The leg is reached from both the success path and :etf_missing.",
  "world_is": "Line 115 sets RC=50 and does `goto :prune` (:prune at 389). On 2026-10-19 the 07:00 local run (bbg_tplus1_20261019_070002.log, 24 lines) logged PULL NOT ATTEMPTED and holds no ETF LEG EXIT CODE and no CONSTITUENTS LEG EXIT CODE line. S3 held zero constituents objects for the day until a manual recovery (bbg_cons_MANUAL_RECOVERY_20261019.log, CONSTITUENTS LEG EXIT CODE: 0).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:107 :precond_down; :114 set RC=50; :115 goto :prune; labels :etf_leg 241, :cons_leg 292, :price_leg 352, :prune 389 (read by the filer at box/sitez HEAD 2026-10-19 ~11:45Z)",
    "scheduled_daily_pull.cmd:144-150, the LEG ISOLATION comment (1.0.0_SA_CTO~Z 2026-09-04): 'This branch used to goto :prune ... converted one leg fault into TWO legs of PERMANENT data loss'. The fix landed on that branch only",
    "C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261019_070002.log: 24 lines; line 12 'PRECONDITION: FAILED -- DAPI DOWN and not self-healed. PULL NOT ATTEMPTED.'; 0 leg-exit lines (grep, read by the filer)"
   ]
  },
  "notes": "ARMED because it repeats unattended: every morning the DAPI precondition fails (including the false DOWN of Z-S18), the constituents capture for that day is lost unless a seat recovers it by hand the same day. disarm_owner is 1.0.0_SA_CTO~Z, which ruled the line-147 leg isolation; the remedy shape (route :precond_down through the legs the way the line-147 branch does, or a recorded reason why DAPI-down must skip them) is NOT ruled here. Coupled with Z-S18: a host policy that fails the precondition makes this branch fire on a day the Terminal is up."
 },
 {
  "id": "ETFS_POSITIONING-Z-S18",
  "project": "ETFS_POSITIONING",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z, FILED as the channel seat on 1.0.0_SA_CTO~Z msg 35949. Observed and drafted by 0.0.3_BG_BBGTerminal (draft @750e18996d).",
  "surfaced_at": "2026-10-19T11:31Z",
  "one_line": "An Application Control policy (WDAC/AppLocker, WinError 4551) blocks `import blpapi` under the cma interpreter. The pull's DAPI check reports it as 'DAPI: DOWN', so a host-policy fault reads as a vendor outage and points the next reader to the sign-in procedure, which has a 2-attempt budget and an account-lock risk, for a fault no sign-in can fix.",
  "spec_asserts": "bloomberg_health / dapi_check report whether the Terminal is reachable and entitled. READ_HERE s.1 maps 'could not start blpapi session' to 'Terminal not running, or signed out'.",
  "world_is": "The 2026-10-19 07:00 local run logged 'DAPI: DOWN (blpapi import failed: [WinError 4551] An Application Control policy has blocked this file)'. Per the drafting seat, the Terminal was signed in from 09:19:42Z and answered its own reads in the same window, and the rivalfunds legs landed under PY_AWS with 0 historical request failures. What failed is the import under one interpreter, not the vendor session.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261019_070002.log:11 'DAPI: DOWN (blpapi import failed: [WinError 4551] An Application Control policy has blocked this file)' (read by the filer)",
    "the Terminal-up readings (sign-in 09:19:42Z, AAPL PX_LAST 343.46, rivalfunds historical_request_failures 0, rc 90/94) are the drafting seat's, recorded in its draft @750e18996d; NOT re-read by the filer"
   ]
  },
  "notes": "ARMED because it repeats: while the policy stands, every scheduled run under cma fails the precondition and, through Z-S17, loses the day's landing legs. disarm_owner is 0.0.0_AB_MSTR~Z, the seat that runs this box's infrastructure; whether the policy is lifted, the interpreter is allow-listed, or the pull moves to an allowed interpreter is that seat's. The diagnostic half is separate and cheap: dapi_check could name an import failure as IMPORT-BLOCKED rather than DOWN, so the symptom stops pointing at sign-in. Who owns dapi_check is not settled here. NOT CLAIMED: when the policy arrived, or whether it blocks anything else on the box."
 },
 {
  "id": "ETFS_POSITIONING-Z-S19",
  "project": "ETFS_POSITIONING",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z, FILED as the channel seat on 1.0.0_SA_CTO~Z msg 35949. Surfaced by 1.0.0_SA_CTO~Z (msg 35944) about a recovery run on its own ruling; drafted by 0.0.3_BG_BBGTerminal (draft @750e18996d).",
  "surfaced_at": "2026-10-19T11:31Z",
  "one_line": "The 2026-10-19 manual constituents recovery wrote run_manifest.json with run_class 'scheduled', because it ran exactly as :cons_leg sets it (ETF_RUN_CLASS=scheduled, line 297). A consumer reading the manifest alone cannot tell the run was a hand recovery.",
  "spec_asserts": "s3://opal-data-etfs/bbg/{as-of}/constituents/run_manifest.json IS the record of the run (the script says so; there is no alert machinery by design), and run_class distinguishes scheduled from adhoc.",
  "world_is": "The recovery ran by hand at 11:15:55Z under the ruling 'exactly as :cons_leg'. :cons_leg sets ETF_RUN_CLASS=scheduled (scheduled_daily_pull.cmd:297, and :246 for :etf_leg), so bbg/2026-10-16/constituents/run_manifest.json reads run_class scheduled. The object is NOT rewritten (CTO~Z's instruction). The join to the truth is the run log bbg_cons_MANUAL_RECOVERY_20261019.log, which carries the MANUAL RECOVERY tag and names the manifest key.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:246 and :297 set ETF_RUN_CLASS=scheduled unconditionally (read by the filer)",
    "C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_cons_MANUAL_RECOVERY_20261019.log exists (25 lines; CONSTITUENTS LEG EXIT CODE: 0 at line 25), read by the filer",
    "the manifest's run_class value is the drafting seat's reading; the S3 object was NOT re-read by the filer"
   ]
  },
  "notes": "INERT, not ARMED: it is one mislabelled manifest from one recovery, and it does not recur unattended. It recurs only when a seat runs another hand recovery the same way. disarm_owner is 1.0.0_SA_CTO~Z, which surfaced it and whose ruling produced it. The tension is real: 'run it exactly as the scheduler does' and 'label it as what it was' cannot both be met with the script as written. Remedy shape (a run_class the caller can set for a manual run) is not ruled here. The manifest key bbg/2026-10-16 is consistent with the trading calendar: 2026-10-19 is a Monday, so T-1 is Friday 2026-10-16."
 },
 {
  "id": "ETFS_POSITIONING-Z-S20",
  "project": "ETFS_POSITIONING",
  "fabric": "site-z",
  "surfaced_by": "1.0.0_SA_CTO~Z",
  "surfaced_at": "2026-10-19T12:11Z",
  "one_line": "Disarm-owner ruling on Z-S17 (ARMED) and Z-S19 (INERT). Z-S17: every DAPI-precondition failure path reaches the landing legs, because the precondition is measured under cma and the legs run under PY_AWS, so a cma DOWN is not evidence the legs would fail. Z-S19: no script change; a hand recovery runs the leg script WITHOUT setting ETF_RUN_CLASS, so the script's own default labels it adhoc.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "adjudicates": [
   "ETFS_POSITIONING-Z-S17",
   "ETFS_POSITIONING-Z-S19"
  ],
  "spec_asserts": "Z-S17 asked for the remedy shape: route :precond_down through the legs the way the line-147 branch does, or record why a DAPI-down morning must skip them. Z-S19 asked for a run_class a caller can set for a manual run.",
  "world_is": "Z-S17 RULED: route :precond_down to the landing legs. (1) The skip rested on 'the ETF pull would fail for the same reason' (scheduled_daily_pull.cmd:153-154). That holds only when the fault is the Terminal. dapi_check runs under %PY% (cma) and the legs run under %PY_AWS%, and Z-S18 measured a cma-only fault on a morning the Terminal was up. (2) The costs are not symmetric: a leg run on a truly-down Terminal costs one non-zero leg exit line, while a skipped leg on a false DOWN loses the current-day-only constituents capture for good (READ_HERE s.4). (3) The same holds for the 'DAPI state UNVERIFIED' skip at :157-158, which takes the same route. Constraints for the edit: :etf_leg must be reached only after the `set PY_AWS` line (:139); jumping past it is the Z-S248 defect (empty interpreter, nothing lands, quietly). The wrapper's final rc stays 50 on this path, so the 07:15 backstop still fires. Z-S19 RULED: no script change. etf_constituents_pull.py:255 and etf_daily_pull.py:540 default run_class to adhoc ('only the scheduled chain sets it'). My 'exactly as :cons_leg' wording made the recovery set ETF_RUN_CLASS=scheduled. A hand recovery runs the leg with ETF_RUN_CLASS unset. The 2026-10-16 manifest stays as written (no S3 rewrite); the join to the truth is bbg_cons_MANUAL_RECOVERY_20261019.log.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "integrations/bloomberg/pipeline/scheduled_daily_pull.cmd at box/sitez HEAD (file last changed e465eabe7b): :107 :precond_down runs %PY% dapi_check; :115 goto :prune; :139 set PY_AWS; :153-158 the UNVERIFIED skip and its stated reason; :246 and :297 set ETF_RUN_CLASS=scheduled; read by 1.0.0_SA_CTO~Z 2026-10-19 ~12:0xZ",
    "comp-find run_class over integrations/bloomberg/pipeline/*.py: 6 hits across 7 files; etf_constituents_pull.py:255 and etf_daily_pull.py:540 log 'default adhoc; only the scheduled chain sets it'",
    "Z-S18 (filed @5012389f79): the cma import blocked by Smart App Control while the PY_AWS copy loads; 0.0.0_AB_MSTR~Z msg 35951 measured the per-instance block"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Z-S17 stays ARMED until the edit lands. Its next fire is the 2026-10-20 11:00Z run. Write surface: 0.0.3_BG_BBGTerminal (the pipeline's owner). It was ordered before this row (CTO~Z 2026-10-19 ~11:4xZ) to land the fix before that run, with a dry-run in which the precondition is forced to fail and the log then shows ETF, CONSTITUENTS and PRICE LEG EXIT CODE lines. Z-S17 disarms on that run's log. Z-S19 needs no further act."
 },
 {
  "id": "ETFS_POSITIONING-Z-S21",
  "project": "ETFS_POSITIONING",
  "fabric": "site-z",
  "surfaced_by": "0.0.0_AB_MSTR~Z",
  "surfaced_at": "2026-10-19T12:30Z",
  "one_line": "Disarm-owner disposition on Z-S18: the policy stands and nothing is loosened; the residual after Z-S20's fix is the cma models leg failing each morning, for as long as Smart App Control judges the cma blpapi file instance unreputable.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "adjudicates": [
   "ETFS_POSITIONING-Z-S18"
  ],
  "spec_asserts": "Z-S18 asked whether the policy is lifted, the interpreter allow-listed, or the pull moved to an allowed interpreter, and named this seat the owner of that choice.",
  "world_is": "Measured 2026-10-19 ~11:15-11:45Z by 0.0.0_AB_MSTR~Z, session not elevated (WDAC_BLPAPI_CMA_FINDING_20261019.md @56ff4365a5). Smart App Control is in ENFORCE (VerifiedAndReputablePolicyState=1). It blocks ffiutils.cp311-win_amd64.pyd (unsigned) when loaded by C:/Anaconda/envs/cma/python.exe. cma's and PY_AWS's copies have the same SHA-256; PY_AWS's loads, cma's and a copy of it under %TEMP% are blocked, so the verdict is per file instance. Last good cma pull 2026-10-18 07:03 local, first bad 2026-10-19 07:01 local. DISPOSITION: (a) the policy is NOT lifted: Smart App Control cannot be re-enabled without resetting Windows, and the choice is Andrew's; (b) the interpreter is NOT allow-listed and blpapi is NOT preloaded in place: 1.0.0_SA_CTO~Z ruled no preload at msg 35951/35952 as a workaround of a code-integrity control; (c) the pull is NOT moved: the cma env carries tia, which PY_AWS lacks (READ_HERE s.3, two interpreters by design). RESIDUAL: after Z-S20's route lands, the PY_AWS landing legs run on a cma DOWN and Z-S18 costs only the cma models leg, each morning, until a sanctioned route exists. NOT KNOWN: whether that leg can be backfilled for a lost morning (the CTO asked 0.0.3_BG_BBGTerminal); why the file instance was allowed on 10-18 and not on 10-19.",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier0_exec/0.0.0_AB_MSTR/deliverables/WDAC_BLPAPI_CMA_FINDING_20261019.md @56ff4365a5: registry state, CodeIntegrity events 3077/3033, SHA-256 match, the three load tests, the daily-pull log dates",
    "1.0.0_SA_CTO~Z msg 35952 (no in-place preload; the cma leg waits on a sanctioned route) and msg 35956 (the recommended disposition), both read by this seat",
    "C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261018_070002.log (cma pull ran, DAPI UP) and bbg_tplus1_20261019_070002.log (WinError 4551), both read by this seat"
   ]
  },
  "notes": "ARMED because the residual repeats unattended every morning while the policy stands. It disarms on one of: a signed or reputable build of the blocked pyd is landed in the cma env by that env's owner (0.0.3_BG_BBGTerminal), or Andrew's recorded word on Smart App Control. This seat has the infrastructure half: the candidate sanctioned route is a clean reinstall of the vendor blpapi wheel into the cma env, to be tried only on the env owner's word; it is a candidate, not a measured fix. Nothing was changed on the box."
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
