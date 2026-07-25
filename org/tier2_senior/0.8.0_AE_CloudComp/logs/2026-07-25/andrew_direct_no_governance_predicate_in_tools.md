# ANDREW-DIRECT record — no governance predicate in any comp-tool (+ hard prohibition on `sovereign_held.py`)

**archetype:** SCRIBE
**Agent:** `0.8.0_AE_CloudComp` (base) · 2026-07-25

Recorded under the XXX.md Andrew-direct protocol: **record durably and broadcast, same turn.** Written
**before** the broadcast, deliberately — a ruling that exists only in my outbox is the failure mode this
session has been clearing all day.

## VERBATIM — never a paraphrase, the phrasing IS the ruling

**Channel:** Andrew → `1.0.0_SA_CTO` directly. **Time:** ~2026-07-25T185538Z.
**Relay:** `1.0.0_SA_CTO~Z` → this lane at 185814Z, same turn.

> *"our comp tools should absolutely never be limited on governance. governance is handled at the aws
> cli/aws user iam level, not at the tool level, If i am understanding properly what youre saying, that
> sounds like the tools have built in blind spots for absolutely no reason"*

## Scope — as stated, NOT adjudicated by me

**STANDING AND BINDING ON NFRA TOOL DESIGN GENERALLY**, not merely the bd instance. No comp-tool gets a
governance predicate, a hold check, or an `*_INCLUDE_HELD` env var. **If a tool must not see something,
that is an IAM decision, not a code branch.**

Per the protocol, the receiving agent does not adjudicate scope — I surface it as given. CTO~Z stated
the generalisation; I am recording it in their words, not extending it in mine.

## Why this is exactly this group's class

**A comp-tool exists to SEE the estate. An under-reporting instrument returns a well-formed answer over
a silently reduced denominator without announcing it.**

That is the sentence this group re-derived from the *retrieval* side repeatedly today — my own
fails-open harness rendering `[PASS]` after its setup collapsed, `grep -c` counting matches inside an
error message, ANSI-blinded greps, no-op mutations. **Andrew has now stated it as an architecture
rule.** *A `startswith` check is not an access control.*

**The sharper half, and the part worth keeping:** several retired guards gated **repo source reads**
(`data/black_diamond/scripts/gold/*.py`). **IAM does not govern local file reads.** So those paths were
**never governed — only pretend-governed.** No enforcement, real blindness: a tool lying about its own
coverage by design, with nothing behind the lie.

## ⚠ HARD PROHIBITION — do NOT "implement" this by deleting

**Nobody edits `org/modules/graph/sovereign_held.py`.** It holds **two** predicates that were fused once
already, and **the fusion was the bug** (07-22 ruling: *"SPLIT the predicate, do NOT rip it"*):

| predicate | status |
|---|---|
| `SOVEREIGN_HELD_PATHS = ()` | **governance** — retracted; what Andrew's ruling addresses |
| `PROD_WRITE_FORBIDDEN_PATHS` | **NOT governance** — stops an automated probe **WRITING to a production bd bucket** on every re-run. **Never retracted. IN FORCE.** |

Base CTO has asked Andrew to confirm and holds it in force pending his answer.

>> **A find-and-delete executed off this broadcast would RE-COMMIT THE EXACT BUG THE SPLIT FIXED**, and
>> would destroy the control whose regression detector base CTO repaired at `@1fcf560b8`. <<

**Reading that file is fine. Editing it is not.** Anything found there routes to **base CTO**.

## Forward-looking, the operative part

**If any tool this lane builds is about to grow a "should I be allowed to see this" branch — stop and
route it to `1.0.0_SA_CTO~Z`.** The answer is now always the same, and it is not a code branch.

## Broadcast performed

Relayed to `~A`, `~B`, `~E` (CTO~Z's explicit ask — `~C` and `~D` have it directly), and surfaced to
`2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR` per the XXX.md broadcast clause so `latest + most-restrictive` has
something to bind on.

## Work in flight — unaffected

Grain recertification **landed by CTO~Z at `fc8b81ec0`**; `stitch_graph.json` published (25.5 MB, 43,633
edges) — **the 17-day blackout is over.** The extractor defects I raised (4 real IAM users missing;
`root` and an OIDC provider mistyped as `IAM_USER`) are **unaffected and still wanted** — those are
*accuracy* defects, not governance.

## Compiler Tools

None run this entry — it is a record-and-broadcast action, not an investigation. The one tool-relevant
consequence is forward-looking and stated above: any future comp-tool that would grow a visibility
branch stops and routes instead.
