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

## ⚠ STILL OPEN — HIS PHRASE, NOT ANSWERED BY THIS WORD

**Does "etf based smas" mean `idvz` and `pfde` belong INSIDE `ETF Strategies`?** He answered the
naming collision, not this. The registry calls all four ETFs SMA-view members with `idvz`/`pfde` as
*"ETF-product members pending strategy registration"* (`mdpf_category_registry.py:33-35`), which
reads toward YES — but `1.0.0_SA_CTO~Z` priced the same census and explicitly declined to resolve
his wording, having been wrong twice in one evening doing exactly that. **This seat's fixture
currently places them OUTSIDE both buckets, in the un-noded disclosure. That is a choice this lane
made without noticing it was a choice, and it is disclosed rather than defended.**
