# RULING -- `global` HAS NO CLIENT L1 RULE, THE ABSENCE IS DELIBERATE, AND THE ALL_SCOPE FLIP DOES NOT UNBLOCK THE GLOBAL VIEW

**Ruled by:** `1.0.0_SA_CTO`, 2026-08-25 ~06:5xZ. **Archetype:** COORDINATE.
**Push state:** landed LOCAL, rides MSTR integration. **Distribution:** not CRO.
**Grounded at source:** `data/mdpf/scripts/gold/mdpf_category_registry.py` at HEAD -- `CLIENT_L1_HELD`
(:642), `client_l1_split` (:654-681), `ViewPlaneError` raise (:724).

> **THIS RECORD EXISTS BECAUSE THE RULING IS AN ABSENCE, AND AN ABSENCE ANNOUNCES NOTHING.** It is the
> type specimen of `CONTROLS_OVER_CARE.md` section 9, landed the same hour @`000a22c637`: *a missing
> entry in a registry is not evidence of a gap -- the absence may be the decision.* **Without this
> file the next competent agent reads `CLIENT_L1_RULE`, sees no `global` key, files a gap, and adds
> one.** That act would manufacture a false fact, and it would look like diligence.

## 1. RULED: GLOBAL HAS NO CLIENT L1 RULE OF ITS OWN AND MUST NEVER BE GIVEN ONE

`client_l1_split(firm_id, client_aum)` takes ONE firm and ONE scalar and resolves a per-firm rule.
**GLOBAL IS NOT A FIRM.** It has no advisors, no fee arrangement, and no supervision fact -- it is a
**roll-up of three firms that each have their own.**

**DO NOT ADD A `global` KEY TO `CLIENT_L1_RULE`.** That entry would assert a fee-taking fact about a
client base that does not exist as a client base. **The function's `raise`-rather-than-default is the
guard working, and the missing key is the ruling it carries.** Its own message already says why:
*"never default it; a default here would assert a fee-taking fact about a client population nobody
has ruled."*

**GLOBAL'S CLIENT L1 AGGREGATES ITS CONSTITUENTS. IT NEVER COMPUTES.** Mechanism belongs to the
implementing lane; the policy is fixed here.

## 2. THEREFORE THE ALL_SCOPE FLIP RELOCATES THE BLOCKER, IT DOES NOT CLEAR IT

`cottonwood` sits in `CLIENT_L1_HELD` and `client_l1_split` returns `None` for it. **A roll-up cannot
be struck while a constituent is held.** So flipping `category-views` to ALL_SCOPE moves the failure
from a `raise` at the scope gate to a held marker at Client L1: global gains its object, and that
object's Client L1 still carries no number.

`0.4.0_DE_ClientPlatform~C` said this of the scope `raise` and was right one layer shallower than it
goes -- *"removing :726 alone moves the failure, it does not fix it."* **The second gate is gated on
Cottonwood, which is under a STOP. NOBODY SHOULD CARRY THE FLIP AS "GLOBAL UNBLOCKED."**

## 3. RULED: GLOBAL EMITS ANYWAY, WITH THE ONE NODE DECLARED UNAVAILABLE

Same shape as `COT-e-1` and for the same reason: **a correct object with one declared gap beats no
object, and beats a fabricated number by a wider margin.** Global's object emits; its Client L1
carries the predicate-unavailable marker **naming Cottonwood as the held constituent**, so a reader
sees which firm holds the line rather than an absence they must diagnose. Every other L0 node renders.
**Holding serves nothing -- it keeps whatever global shows today.**

## 4. THE ORDERING CONSTRAINT, ELEVATED OUT OF A SOURCE COMMENT

**THE SCOPE-SET CHANGE AND THE GLOBAL OBJECT'S FIRST EMISSION LAND IN ONE COMMIT.** `a4_expected`
derives from the scope map, so a type declared before it emits reads 15-against-12 and goes
**permanently red** -- the defect the axis exists to prevent.

This lived only at `mdpf_gold_consolidator.py:136-140`. `2.0.0_SA_COO` surfaced it and their framing
is the keeper: **this is not a bug to fix, it is a CHANGE TO SEQUENCE**, and it touches every site at
once (COO measures THREE sites -- take their count). **A load-bearing sequencing rule living only in a
source comment is one refactor from gone, and it gets rediscovered by the red it causes.**

## 5. THE COTTONWOOD HOLD'S STATED REASON IS STALE -- AND WOULD GET THE HOLD LIFTED

`CLIENT_L1_HELD["cottonwood"]` says the held input is whether Opal Moderate Income and Opal 15/85
count as Models, *"(at CTO)"*, offering Client-Supervised of `303,397,550.13` or `310,042,269.95`.
**Three things wrong, and they compound:**
1. **I RULED IT.** Name+location supersession granted -- an Opal-named portfolio from that location IS
   a Custom Model. The "at CTO" is discharged.
2. **`303,397,550.13` IS A WITHDRAWN FIGURE.** I struck it on the Cottonwood-supervision basis; Andrew's
   Opal-definition ruling landed ten minutes later. It should not sit in production code as a live option.
3. **THE REAL BLOCKER IS ABSENT FROM IT** -- the 30-of-64 rebalancer ingest gap and the STOP, both later.

**THE HOLD IS STILL CORRECT; ITS STATED REASON WOULD GET IT LIFTED FOR THE WRONG REASON.**
`0.4.0_DS_ClientPlatform~F`: update the reason to the ingest gap + the STOP on next touch. **DO NOT
LIFT THE HOLD.**

> **THE CLASS, AND IT IS THE MIRROR OF COO'S:** theirs was a **withdrawn ruling still cited as live
> authority** in code; this is a **live hold citing a discharged reason**. *A withdrawal that does not
> sweep its citations has not landed -- and neither has a RULING that does not sweep the holds waiting
> on it.* **That second half is mine, and I had not swept either.**

## 6. NOT A PROBLEM -- DO NOT "FIX" IT

The emitter keys `Client > Opal Supervised` / `Client > Opal Unsupervised`. That is the **VIEW PATH**;
Andrew's `Client - Opal Supervised` is the **DISPLAY LABEL**. Same node, two renderings, and the code
comment is explicit that keying by path rather than by munged label is deliberate. **NOT a naming
conflict.**

It does confirm the drift direction: **the code carries Andrew's 2026-08-25 naming and the D1 PRD does
not** (`Client - Opal Supervised` occurs zero times there). **The PRD is the stale surface, not the
implementation** -- and the PRD amendment is a Rule 24 authoring act on a ruled axis, routed to D1's decomp.
