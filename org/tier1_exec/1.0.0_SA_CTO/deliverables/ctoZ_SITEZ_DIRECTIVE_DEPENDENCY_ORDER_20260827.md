# SITEZ DIRECTIVE SET -- DEPENDENCY ORDER

**Author:** `1.0.0_SA_CTO~Z`, 2026-08-27 ~14:0xZ.
**Authority:** Andrew-direct 2026-08-27 at the MSTR~Z terminal, VERBATIM: *"instantiate CTO~Z and let
them know to get organized in the sense of identifying any dependency order in sitez directives and
begin full-forcing, bring COO~Z on as well"* (relayed `0.0.0_AB_MSTR~Z` msg 9134).
**Set:** D1 D4 D6 D7 D8 D9 -- all SITEZ-placed at `origin/CLOUD` HEAD.

## s.0 -- HOW THIS WAS DERIVED, AND WHY NEITHER REGISTER COPY ALONE IS SUFFICIENT

The ordering fields do not exist in the register schema (0 of 12 rows carry timeframe/depends_on --
the fields are ABSENT, not empty). Schedules, dependencies and device legs rode in the TITLE
PARENTHETICAL, and the 2026-08-27 rename removed them from 8 of 12 rows.

| source | good for | WRONG about |
|---|---|---|
| SITEZ HEAD `@59bb2c153d` | the ONLY surviving ordering evidence (old titles) | placement -- D1 reads LAPTOP; its "D8" is the RETIRED modal directive |
| `origin/CLOUD` HEAD | CURRENT placement + stances | carries no ordering at all |

**Both were read. Every edge below cites which.**

> ⛔ **THE PARENTHETICALS ARE EVIDENCE OF A PRIOR ORDERING, NOT A LIVE SCHEDULE** -- and this bites
> immediately. The recovered D7 parenthetical says **"THIS WEEK"** as of 2026-08-19. The CLOUD stance
> records Andrew putting **D7 ON HOLD on 2026-08-25**. *A seat forcing on the recovered parenthetical
> alone would have driven hardest at the one directive he had just stopped.*

## s.1 -- THE DEPENDENCY EDGES

### E1 -- D1 BEFORE D4 :: RECOVERED, CORROBORATED FROM BOTH ENDS
- SITEZ title: `D4 "ETF positioning variant (3-8wks, behind D1)"` -- the only explicit ordering token in the set.
- CLOUD D4 stance, independently: *"the four ETFs join D1's taxonomy as SMA-category members -- one registry serves both."*

Two carriers, one from each end, one per fabric.  **Strongest edge in the set.**

⚠ **GRAIN: this binds D4's TAXONOMY/CANON layer ONLY.** D4's ingest, pull and producer legs consume
no D1 output and are **not** behind D1. Reading E1 as directive-level would idle 8 open TOs behind a
directive that has 2.

⛔ **AND THE EDGE IS NOW INVISIBLE.** When *"behind D1"* was written, D1 was LAPTOP and D4 SITEZ -- the
constraint crossed fabrics and therefore *had* to be written down. Since 2026-08-26 **both are mine**,
so the edge became internal, and the sentence carrying it was deleted the next day.
**A dependency stops being recorded exactly when it stops crossing an organisational boundary --
which is exactly when it also stops being obvious.**

### E2 -- D1 BEFORE D3 :: RECOVERED, OUTBOUND, CROSS-FABRIC
SITEZ title: `D3 "Account-level model overlay (~6-7wks, pends D1+D2)"`. D3 is **LAPTOP's**.
**An obligation FROM me, not a constraint ON me:** my D1 work unblocks their D3. It raises D1's rank;
it gates nothing here. The laptop cannot see this edge either -- same deleted parenthetical.

### ~~E3 -- D8's COTREMEDIATION LEG BEFORE D1's ACCEPTANCE~~ :: ⛔ **RETRACTED 2026-08-27 ~14:03Z BY ITS AUTHOR, SAME SESSION**

> ⛔ **E3 IS WITHDRAWN ENTIRELY, NOT WEAKENED. THE FINDING BENEATH IT IS FALSE.**
>
> **COTTONWOOD IS EXACTLY HEALTHY.** Its value-bearing feeds (`bd_holdings_s2`, `bd_allocations_s2`)
> are declared **D+2** cadence in `data/mdpf/config/partner_roster.json` -- the ONE authority the
> producer reads by name. Measured with `lib/trading_calendar.py`:
> `expected_last_trading_day = 2026-08-27`; minus 2 trading days = **2026-08-25**; cottonwood
> measured frontier = **2026-08-25** -> **LAG 0.**
> Roster verbatim: *"D+2 ... BY DESIGN, not a defect -- Black Diamond measured 14 of 14 instances
> 2026-07-24. **Cottonwood at D+2 is lag 0; Cottonwood at D+4 is lag 2, and THAT is the signal.**"*
> **The D8 remediation is COMPLETE, not partial** -- the opposite of what this section claimed.
>
> **HOW IT WAS WRONG, which is the part worth keeping.** I resolved the trading calendar, printed
> denominators, and quoted no wall-clock age -- and still committed NEVER#1's error one level up.
> The control I leaned on, and *named in this document as the thing that made it rigorous*, was a
> **partner-to-partner comparison at a single instant.**
> **THAT CONTROL IS VOID WHEN THE PARTNERS HAVE DIFFERENT DECLARED CADENCES.** cottonwood is D+2 and
> the other three are same-day, so a difference between them is **the expected state and carries no
> information**. The control could not have returned "healthy" for a D+2 partner -- an instrument
> that could not have said otherwise (Rule 22a).
> **NEVER#1 reads as a CALENDAR rule and is also a CADENCE rule: the calendar is only half the
> frontier. The other half is per-partner and DECLARED.**
> And the tell was already on screen: the producer's header says *"Cottonwood sidecar VINTAGE gate"*
> and `_cot_carry_policy`. **I read "cottonwood is special-cased" as evidence something was WRONG
> with it, when it was the declaration of what is RIGHT for it.**
>
> **WHAT SURVIVES:** the four measured frontier values are correct and reproduce; only the verdict on
> them was wrong. **WHAT DOES NOT:** E3, and D8's rank-1 position, whose sole claim was "the only
> live client-facing defect." **NOT ESTABLISHED and not asserted:** that the root cause cannot
> re-freeze -- today's output being correct is not proof of that. It is a real D8 question and it is
> not urgent.

*Original section preserved below for provenance. **Its conclusion is false; do not act on it.***

Marked `DERIVED` because no parenthetical carries it. I am not laundering my own reading as recovery.

- D1 and D8 share the subgroup `PORTAL.MODEL_PORTFOLIOS`.
- D1's acceptance (CLOUD stance): *"Cottonwood display acceptance (~$7M Custom + ~$30M Client Advised/Residual) = DONE."*
- **MEASURED 2026-08-27 ~13:5xZ, live, AFTER today's 13:30Z fire** -- served payload frontier at
  `s3://opal-data-assets/portal/gold/mdpf/{partner}/account-distribution/`, max partition materialised
  client-side (denominators printed: cottonwood 16 / global 16 / 49financial 20 / inflection 24):

| partner | latest partition | payload `generated_at` |
|---|---|---|
| **cottonwood** | **2026-08-25** | 2026-08-27T13:30:48Z |
| global | 2026-08-27 | 2026-08-27T13:31:12Z |
| 49financial | 2026-08-27 | 2026-08-27T13:31:10Z |
| inflection | 2026-08-27 | 2026-08-27T13:31:11Z |

**All four regenerated today; cottonwood is 2 trading days behind its three siblings.**
Not a wall-clock age and **not** a NEVER#1 candidate: this is a **within-instrument, same-instant,
partner-to-partner** comparison -- the control that makes it a finding rather than a clock reading.
The 08-25 stance recorded cottonwood AND global both frozen at 08-19; **global is now restored and
cottonwood is not.** The remediation is PARTIAL, not complete.

**THEREFORE:** D1's acceptance criterion is read on the exact partner whose payload D8 has not
restored. Run it now and it **passes or fails for reasons that have nothing to do with D1's taxonomy.**

## s.2 -- THE THREE NON-EDGES: GATED ON INPUTS NO ORDERING CAN MOVE

Rule 24(iv) STATE COHERENCE -- these do **not** move on the same remedy as D1/D4/D8, and naming that is the point.

- **D7 -- ON HOLD by his word** (Andrew-direct 2026-08-25 ~16:2xZ). Its one live leg is **DONE**:
  the `Submit a Request` nav item is **ABSENT on `origin/DEV` AND `origin/PROD`** (positive control:
  16 `path:` entries in the same file, so the search reaches). *My local portal tree still carried it
  at `App.tsx:122` and was 2 commits stale -- the wrong plane.* D7 also has a **standing weekly
  Andrew/AJ cadence**, so quiet here is EXPECTED, not a staffing gap.
- **D9 -- gated on the Yang/Alyssa meeting** (human, external) for its Tax half. YCharts folded in
  08-26 and **deliberately deferred** (*"time to discuss later next week"*). **IN SCOPE and DEFERRED
  are two different facts.**
- **D6 -- no hard edge, but a soft one INTO a held surface.** Re-scoped to agent mechanics and
  *"tooling interfaces (Ticket Center foremost)"* -- and the Ticket Center is D7, which is HELD.
  **D6's Ticket-Center legs inherit D7's hold; its other legs do not.**

## s.3 -- THE EXECUTABILITY LAYER, AND THE LIMIT OF ITS DENOMINATOR

`2.0.0_SA_COO~Z` (msg 9140) walked every sitez TO candidate against its own gate rows and device-split
table and found **exactly ONE ungated site-Z-executable workstream: D9 TO-A** (*"Gate: none -- START
NOW eligible"*, inputs in-tree @`ad01cca427`). `0.0.0_AB_MSTR~Z` (msg 9143) drew the inference:
*"IF ONLY ONE ITEM CAN START, THE FIRST STEP IS DETERMINED BY EXECUTABILITY AND NOT BY THE DEPENDENCY GRAPH."*

**The inference is sound in form. I am accepting the finding and declining the conclusion, on the denominator.**

⛔ **THAT SWEEP COVERS FOUR OF SIX DIRECTIVES.** Its table enumerates **D9, D7, D6, D4** -- and those
are precisely the four that were placed here on **2026-08-19**, when my atom-decomp runs produced the
s6 TO tables the sweep reads. **D1 and D8 moved here on 2026-08-26 and appear nowhere in it.**
D8 was RE-MINTED on 08-25, *after* those decomps; its PRD is not even on this fabric.

**So "exactly one executable item" is TRUE of the surveyed four and says nothing about D1 or D8.**
A clean, well-formed, correct answer about the wrong plane -- the class CLAUDE.md's retrieval law names.
*This is not a criticism of the sweep: it could not have covered a directive whose specification does
not exist on the fabric it swept.*

**D8's ungated executable leg, verified this session:** its producer code IS on this fabric
(`data/mdpf/scripts/gold/dim_mdpf_account_distribution.py` -- the account-distribution producer I
measured), the divergence its PRD predicted IS present in source (`gold/mdpf_revamp/cottonwood/...`
staging grammar vs the served `portal/gold/mdpf/cottonwood/`), and the investigation is read-only
AWS + source. **No laptop deliverable, no Andrew answer, no closed gate.** Rule 26 is satisfied
because D8 is SITEZ-placed, so the seat that builds it applies it here.

>> ~~**THE EXECUTABLE SET IS TWO, NOT ONE: D9 TO-A and D8's cotremediation investigation.**~~ <<

⛔ **RETRACTED SAME SESSION -- THE EXECUTABLE SET IS ONE, AND IT IS `2.0.0_SA_COO~Z`'s ORIGINAL
MEASUREMENT STANDING UNAMENDED.** D8's "executable leg" was the investigation of a defect that does
not exist (see E3's retraction). **`0.0.0_AB_MSTR~Z`'s inference -- that step 1 is forced by
EXECUTABILITY rather than by the dependency graph -- CARRIES. I declined it, and my sole
counter-example was my own false finding.**

**THE DENOMINATOR POINT ITSELF IS UNAFFECTED AND STILL TRUE:** the sweep does cover 4 of 6 and is
silent on D1/D8, for the reason stated. What changed is that the gap it correctly identified turned
out to contain nothing urgent. **A correct observation about a blind spot is not evidence that
something is hiding in it** -- and that leap is the second error in this document, distinct from the
cadence one and worth naming separately.

## s.4 -- THE ORDER

```
   D8 (COTREMEDIATION)  --E3-->  D1  --E1 (taxonomy layer only)-->  D4 (canon/registry legs)
                                  |
                                  +--E2--> D3   [LAPTOP -- outbound; unblocks them]

   D9 TO-A  --------- ungated, START NOW eligible, runs in parallel from minute one
   D4 ingest/pull/producer legs ---- parallel; gated by SEATING, not by D1
   D6 (non-Ticket-Center legs) ----- parallel; continuation needs decomp first
   D7 ------------------------------ HELD by his word. Nothing to force.
```

**⛔ REVISED 14:03Z after the E3 retraction. This table is the OPERATIVE order.**

| rank | directive | why here |
|---|---|---|
| **1** | **D9 TO-A** | Ungated, START-NOW eligible, read-only, self-contained, inputs in-tree @`ad01cca427`. **The sole site-Z-executable item.** Its blocker is a SEAT, not a dependency. |
| **2** | **D1** | Unblocks D4 internally (E1) and laptop D3 externally (E2). Highest leverage per unit of work in the set. **Its Cottonwood acceptance is READABLE now** -- cottonwood is at its correct D+2 frontier. |
| **3** | **D4** | Holds **8 of the set's 8 open TOs**. Ingest legs start immediately; only the taxonomy join waits on D1. |
| **4** | **D6** | Continuation is the one genuine decomp gap (four sovereign-worded bodies, zero projects, zero TOs). Ticket-Center legs inherit D7's hold. |
| **5** | **D8** | Conformance census + gold-bucket architecture, on **D8's own clock** -- its PRD s.5 says explicitly NOT the outage's. **No live defect.** |
| **6** | **D7** | Held by his word; live leg already shipped to PROD. |

**E1 and E2 ARE UNTOUCHED BY THE RETRACTION** -- both are recovered from the parentheticals and
neither depended on the cottonwood reading. **The dependency spine stands; only the item that had
been placed in front of it does not.**

~~*Superseded rank table (D8 at 1, D9 TO-A at 1=) -- withdrawn with E3.*~~

## s.5 -- THE CONSTRAINT THAT OUTRANKS THE ORDERING

**Two of the four live sitez directives terminate at a seat family with no live instance.**
`0.5.0_AE_OpalETL~A` is DEAD (holds D9's three projects + stalled TOs #42/#48);
`0.5.0_AE_OpalETL~Z` is DARK on six unread (holds D7's site-Z intake workstream + every teams-watch
engine item, including the ARMED cursor hazard).
And D4's assignee set drifted: **5 of 6 assigned TOs name BASE (laptop) serials** on a SITEZ-placed
directive; 2 are unassigned.

**A fabric with three Tier-0/Tier-1 seats and zero worker seats cannot execute any of this.**
That is a fact about the fabric, not a caveat on the plan. **The order is correct and inert until seats exist.**

## s.6 -- WHAT I AM NOT DOING

- **NOT editing the register** -- `org/missions/.register-owner` names the laptop MSTR (LD-0341).
- **NOT reviving a date** -- the recovered parentheticals are prior-ordering evidence. Where ordering
  is load-bearing I ask Andrew rather than manufacture a deadline from an 08-26 vintage.
- **NOT arming `/self-drive D4`** -- see the open call in the broadcast.
- **NO gate is created by this document.** It is an ordering, not an approval step. Nothing is held.
