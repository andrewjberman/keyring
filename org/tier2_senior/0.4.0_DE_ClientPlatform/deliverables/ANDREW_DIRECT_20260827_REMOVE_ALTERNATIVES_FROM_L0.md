# ANDREW-DIRECT 2026-08-27 ~21:1xZ — REMOVE `Alternatives` from L0

**Received by:** `0.4.0_DE_ClientPlatform~Z` at the site-Z terminal, answering this seat's flag that
`ALT Strategies` (an L1 bucket under SMAs) and `Alternatives` (an L0 node) sit one word apart.
**Recorded same-turn per `org/XXX.md`.**

> ⛔ **VERBATIM. THE PHRASING IS THE RULING — do not paraphrase this block.**

> *"We can just get rid of Alternatives at L0, they are differnet things but if its confusing easier
> to just get rid of it"*

---

## WHAT IT RULES

1. **`Alternatives` comes OUT of L0.** The rendered L0 set is **Models · SMAs · Client**.
2. **He CONFIRMS the two are different things** — *"they are differnet things"*. The removal is not a
   correction of a conflation; it is a decision that the collision is not worth carrying.
3. The stated reason is **cost, not semantics**: *"if its confusing easier to just get rid of it"*.

## ⭐ THIS ALSO CLOSES A CALL THAT HAD BEEN OPEN SINCE 08-26

`1.0.0_SA_CTO~Z` surfaced on 2026-08-26 that his layering word named **three** L0 nodes while the
persisted set carried **five**, and wrote: *"Whether this is elliptical or a narrowing is HIS to say
— surfaced as a question, not resolved by inference."* This seat re-raised it at `/open-calls`
~20:4xZ with a recommendation to KEEP the node.

⛔ **HE RULED THE OTHER WAY, AND THE REC WAS WRONG.** My argument was "(b) five, three present —
keep the node, the presence rule hides it at zero, it costs nothing now." **The cost I priced was
rendering cost. The cost he priced was a vocabulary collision in a tree a human has to read**, and
that is the cost that was actually being paid. A node that renders nothing still occupies a name.

## WHAT CHANGES, AND WHOSE ACT IT IS

| plane | change | owner |
|---|---|---|
| **registry / VIEW_TREE** | `Alternatives` leaves the declared L0 node set | **DS-class** — `data/mdpf/scripts/gold/mdpf_category_registry.py`. NOT this lane. |
| **emitted block** | `view_plane.peers` stops carrying it | follows the registry |
| **renderer** | **NO CHANGE** | it draws what the block declares; when the block stops declaring `Alternatives`, it stops rendering |
| **smoke fixture** | node + peer entry removed | this lane, this commit |

⛔ **THE RENDERER IS NOT WHERE THIS LANDS AND MUST NOT BE.** `CategoryViewTree.tsx` renders
`block.view_plane.peers`, ordered by a display constant, with unlisted peers appended rather than
dropped — deliberately, so a node the emitter starts carrying is never silently hidden by the
frontend. **Hardcoding the removal in the component would make the renderer disagree with the
block**, which is the exact defect the append-unlisted behaviour exists to prevent. The taxonomy is
the registry's to state.

## ✅ CLOSED ~21:4xZ — HIS PHRASE, ANSWERED

**Did "etf based smas" mean `idvz` and `pfde` belong INSIDE `ETF Strategies`? YES.** Andrew approved
it ~21:4xZ — *"yes approve all recs"*, relayed by `1.0.0_SA_CTO~Z` @10295 against their
`/open-calls` card 1. **SMA L1 = {ETF Strategies, ALT Strategies}**, with
**ETF = {pfoe, divz, idvz, pfde}** and **ALT = {tax, muni}**: 4 + 2 over a 6-member domain, MECE
closing with no uncovered member. Landed in the smoke fixture at portal `853c0a38`
(**LOCAL** — `origin/DEV` reads `60226c3209` by `ls-remote`).

⛔ **THIS SECTION WAS REWRITTEN IN PLACE, NOT APPENDED TO.** What stood here said the fixture
*"places them OUTSIDE both buckets, in the un-noded disclosure"* — now **false of the fixture**. An
append would have left the false sentence standing as the block a reader opens first, which is the
two-carriers defect committed against a single carrier.

⭐ **AND THE DISCLOSURE IS WHY THE ANSWER ARRIVED.** This section previously recorded the placement
as *"a choice this lane made without noticing it was a choice … disclosed rather than defended"*.
Naming it as an unresolved choice is what put it on a card he could rule on. `3.0.0_SA_CVO~Z`
confirmed the hunt was not vacuous: under the rival reading it was **4 of 6 with `idvz`/`pfde`
uncovered and postulate (i) FAILING** — *"the sovereign answer closed that branch; the arithmetic
did not."*

⛔ **`un_noded_members` IS DISSOLVED, NOT EMPTIED.** The category no longer exists; the two members
were **re-homed**, not dropped. Retiring the field from the schema is the producer's act
(`data/mdpf/scripts/gold/`) and is **NOT** done here — the fixture carries it empty so it does not
disagree with the type.
