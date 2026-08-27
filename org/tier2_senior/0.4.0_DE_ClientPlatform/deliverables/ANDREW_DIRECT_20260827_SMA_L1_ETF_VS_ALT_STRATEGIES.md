# ANDREW-DIRECT 2026-08-27 ~20:5xZ — SMAs break into ETF Strategies and ALT Strategies

**Received by:** `0.4.0_DE_ClientPlatform~Z` (D1_CATVIEWS DE lane), at the site-Z terminal,
immediately following this seat's `/open-calls`.
**Recorded same-turn per `org/XXX.md`.**

> ⛔ **VERBATIM. THE PHRASING IS THE RULING — do not paraphrase this block.**

> *"I think there is a better way to do this, let's make SMAs break down into ETF Strategies and
> ALT Strategies. ETFS would include PFOE DIVZ, etf based smas, whereas ALT would be Tax and Muni"*

> **and immediately following, the generalisation:**

> *"i think that makes a nice little organizational function which should be relayed to CTO~Z for
> wherever we're memorializing this, because the shapes should all be the same in layout"*

---

## ⭐ THE SECOND SENTENCE IS THE BIGGER RULING, AND IT IS A GENERAL ONE

The first sentence restructures ONE node. **The second makes it a LAW OVER THE WHOLE TREE:
"the shapes should all be the same in layout."** Every L0 card takes the same form —
L1 buckets, L2 members beneath — rather than each node carrying a bespoke shape.

```
UNIFORM SHAPE                L0        L1 (buckets)                       L2 (members)
                             Models    Primary | Custom                   the member models
                             SMAs      ETF Strategies | ALT Strategies    the member SMAs
                             Client    Opal Supervised | Opal Unsupervised   ??? (see below)
```

**He named the relay target himself:** `1.0.0_SA_CTO~Z`, "for wherever we're memorializing this".
Routed there this turn. The likely carrier is CTO's
`org/tier1_exec/1.0.0_SA_CTO/deliverables/MP_TAXONOMY_COMPILED_REFERENCE_20260826.md` — **naming the
carrier is CTO's call, not this seat's**, which is why it is relayed rather than written there.

### ⚠ THE EDGE THE UNIFORM RULE EXPOSES — surfaced, NOT adjudicated

**Client has no L2 defined anywhere in the record.** Models has one (member models), SMAs now has
one (member SMAs), Client's L1 is `Opal Supervised | Opal Unsupervised` and nothing states what sits
beneath. Under "the shapes should all be the same in layout" that is either (a) an L2 nobody has
named yet, or (b) a node where the uniform rule stops at L1. **His to say.** Also note his ~19:5xZ
word deferred the Client-side derivations explicitly: *"Eventually we can get into the fees and the
client-supervised as opposed to opal-supervised derivations and etc., but im not sure yet how that
will take shape so its not a priority at this stage."*

> **and the ORDERING RULING, ~21:0xZ, resolving the two-terminal collision below:**

> *"ETF/ALT stands, Tax has no leaves beneath it"*

---

## ⛔ THE COLLISION THIS RESOLVES — recorded because the reasoning is the reusable part

Two sovereign words landed **~20:5xZ at two different terminals** and neither carried a timestamp
finer than that:

| terminal | word | reading |
|---|---|---|
| `1.0.0_SA_CTO~Z` | *"They are all meant to be rolled up into tax, not two diff strategies or deeper drills/leaves"* | Tax is ONE strategy; nothing beneath it. CTO concluded L1 SMAs = Tax/Muni/DIVZ/PFOE "confirms the shipped shape". |
| `0.4.0_DE_ClientPlatform~Z` | *"let's make SMAs break down into ETF Strategies and ALT Strategies"* | those four move from L1 to **L2**, under two L1 buckets. |

**Both could not be the current L1**, and "latest + most-restrictive binds" needs an ORDER that
neither seat had. **Escalated rather than adjudicated** — inventing an order to break the tie would
have been manufacturing the ruling.

**HIS ANSWER: BOTH HOLD.** They govern OPPOSITE DIRECTIONS on the same node —

```
ABOVE Tax   ETF/ALT bucketing STANDS      -> Tax sits under ALT Strategies (a new L1 above it)
BELOW Tax   no leaves                     -> Tax is a LEAF; no 145/200 split, no L3
```

⭐ **The apparent conflict was an artefact of both words being read as "about the SMA tree" rather
than as "about what sits above" and "about what sits below".** The only thing that was actually
wrong was CTO's LEVEL for the four members, not their membership.

---

## THE STRUCTURE HE NAMED

```
L0   SMAs
L1     ETF Strategies      <- PFOE, DIVZ, "etf based smas"
L1     ALT Strategies      <- Tax, Muni
L2       the member SMAs under each bucket
```

## ⛔ WHAT THIS SUPERSEDES, STATED SO NOBODY BUILDS THE OLD ONE

His 2026-08-26 16:36Z word gave **L1 SMAs as a FLAT FOUR** — *"L1 SMAs is Tax Muni DIVZ PFOE"*
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260826_1636Z_MP_LAYERING_L0_L1_L2_WITH_CUSTOM_DISCOVERY_RULE.md`).
This word inserts a LEVEL: those four become **L2 members under two L1 buckets**. Latest binds.
His own framing is "a better way to do this", i.e. an explicit improvement on his prior structure,
not an elliptical restatement of it.

## ⭐ IT IS ALSO THE CONCRETE FORM OF HIS ~19:5xZ SYNCHRONIZATION RULING

At ~19:5xZ he ruled *"I do not like that SMAs have a different path with no dollars, that is not
right we need to synchronize these things"*
(`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260827_SMA_SYNCHRONIZE_AND_CLIENT_L1.md`).
**This word says what "synchronized" looks like:** SMAs gains the same two-level shape Models
already has.

```
Models   L1 Primary | Custom          L2 the member models
SMAs     L1 ETF Strategies | ALT      L2 the member SMAs      <- now the SAME shape
Client   L1 Opal Supervised | Opal Unsupervised
```

## ⛔ IT BEARS ON THE A-vs-B SCOPE FORK, WHICH IS NOT MINE TO RULE

`2.0.0_SA_COO~Z` and `1.0.0_SA_CTO~Z` hold an open fork on how SMA gains dollars:

| | shape | can it express THIS word? |
|---|---|---|
| **A (narrow)** | `MdpfCategorySmaL1Node` gains `aum`; `l1_nodes` stays a flat positional array | **NO** — a flat array cannot carry L1 buckets with L2 members beneath them |
| **B (wide)** | SMA adopts `children: Record<label, MdpfCategoryChildNode>` like Models/Client | **YES** — `children` carries `aum` per bucket and `members[]` beneath each |

**SURFACED, NOT ADJUDICATED** (`org/XXX.md`: the receiving seat does not adjudicate scope). But the
structure he named is not expressible in shape A, and that is a measured property of the two shapes
rather than a preference.

## ✅ ONE VOCABULARY COLLISION — SURFACED HERE, CLOSED BY HIM ~21:1xZ

**"ALT Strategies" (an L1 bucket under SMAs) and "Alternatives" (an L0 node in the persisted
five-peer set) are different things at different levels**, and surfacing that is what produced the
ruling. Andrew removed the L0 node:

> *"We can just get rid of Alternatives at L0, they are differnet things but if its confusing easier
> to just get rid of it"*

Verbatim record: `ANDREW_DIRECT_20260827_REMOVE_ALTERNATIVES_FROM_L0.md`. **The rendered L0 set is
Models · SMAs · Client.** He CONFIRMED the two are different things and removed the node anyway —
the ruling is priced on **cost, not semantics**.

⛔ **MY RECOMMENDATION ON THIS WAS WRONG AND THE ERROR IS THE REUSABLE PART.** I argued to KEEP the
node because a zero-AUM node renders nothing, therefore costs nothing. **I priced RENDERING cost; he
priced a VOCABULARY COLLISION in a tree a human reads.** A node that renders nothing still occupies
a name.

⛔ **The registry change is DS-class and NOT performed by this lane**
(`data/mdpf/scripts/gold/mdpf_category_registry.py` VIEW_TREE). Only the smoke fixture and these
records moved.

## RENDERER IMPACT — measured, not estimated

**ZERO renderer change required**, and this was EXERCISED rather than reasoned:
`CategoryViewTree.tsx` `l1RowsOf()` falls through to `categoryChildrenForDisplay(node)` whenever
`l1_nodes` is absent, so an SMA node emitted as `children` renders L1 rows with dollar amounts, a
colour-coded bar, and L2 members on click — identical to Models. Verified 2026-08-27 by re-emitting
a fixture scope's SMA in the `children` shape and reading the render.

**The producer change is DS-class** (`data/mdpf/scripts/gold/mdpf_category_registry.py:909`, which
today emits `l1_nodes` as three fields with no `aum`). Not this lane's.
