# Filling a field that says how to compute a key — and four times my own fill said PASS wrongly — 0.4.0_DT_ClientPlatform~X

**Date:** 2026-08-28
**Task Order:** NFRA_SUBSTRATECARDING.TO-KEYFILL-DTX (the key_expression fill)
**Status:** COMPLETE on the fill, the validator and the instance. Report issued.
**Window:** 19:55–20:50Z
**Archetype:** FILLER-UNDER-A-FROZEN-CONTRACT

## Objective

Fill `trust.key.key_expression` on the 18 v3 cards this seat carded — stated so a consumer can
COMPUTE a member's key, not merely name its space — with a basis that says whether anyone actually
exercised it.

## Outcome

**11 measured / 6 held / 1 absent / 0 refused = 18.** `inferred`: 0, which is what all 18 rows
carried before. v3 validation **PASS 18 of 18**; the contradiction fixture refused; the clean-extract
replay identical with the extract released (0.97 GB, removed: True). Proof-of-spec **VALID**.

## The through-line: my own fill reported PASS four times when it should not have

Every one was caught by printing what was actually computed, never by re-reading the code.

1. **The reachability probe picked the wrong population.** It chose `$.edges[*]` for the motif cards
   because edges outnumber nodes 36 to 7 — while the declared space is *motif node_id strings*,
   which live on `$.nodes[*]`. A plausible answer about the wrong collection.
2. **A source read that found nothing returned the string `"(pattern not found)"`** — which is
   non-empty and therefore *satisfied* the `p_nonempty` predicate. A failed retrieval returning a
   value that passes the check.
3. **Two loader scripts were being called `measured`** on the strength of a line of source
   (`arn = n.get("arn", "")`). That is a citation, not an exercise: neither loader was run and
   neither output table was opened. Both are now `held`.
4. **The risk-edge key is not a bare path.** Its space says "repo-relative file paths"; the observed
   key is `file:.tools/deploy_ledger.py`. My predicate was weak enough to accept both, so the prefix
   would have travelled unmentioned and a consumer stripping it would mis-key.

And a fifth, caught by the validator rather than by me: **I invented two fields** —
`key_expression_unexercised_reason`, `key_expression_absent_reason` — to carry the absence reasons.
v3's `trust.key` is `additionalProperties: false`, so 7 of 18 cards went INVALID. *A value needs a
whole path, not a slot I wish existed.* The reasons now append to `evidence`, the slot the contract
has.

A sixth, structural: **the first run of the fill script exited 0 having found ZERO cards**, because
`0 + 0 + 0 + 0 == 0` satisfies the reconciliation I wrote to prove completeness. An empty population
is the easiest way to balance a census. The denominator is now asserted against the re-derived
expectation.

## What "measured" cost, and why 11 not 18

`measured` is claimed only where the expression was exercised on a real member **in this fill**, with
the triple printed: `motif:silent-display-fork`, `49financial`, `gold:A_00.accounts_dimension`,
`event_rule:inf-gold-incremental-daily`, `sysi:compute-orchestration:d0365a15beb8`, `Estate`,
`.tools/comp-heat`, `file:.tools/deploy_ledger.py`, and three repo-relative paths that resolve.

The other seven are honest about why not: two S3/Iceberg tables and one local kuzu projection were
not opened, two loader scripts were not run, one subject is **absent from this device**, and one was
never observed at all.

## Findings Filed

| class | substance |
|---|---|
| OBSERVATION | `c2_instances.json` (W2-hffm's subject) is absent here and not at that path at HEAD; the card recorded it UNTRACKED at 10,329,963 bytes, so its disappearance leaves no git evidence |
| OBSERVATION | `0.8.0_AE_CloudComp~X` cards the SAME subject — two lanes, one subject, which the JOIN must know |
| OBSERVATION | the 72-card census has exactly one exclusion, and it is not a card: `W4-FILE.cells.json` is a cell manifest in a wave directory |
| OBSERVATION | **all six KEYFILL faces** put `<owned_cells>` outside `<decomp_ref>`, so proof-of-spec backward alignment degrades to "NOT asserted" while still printing VALID |

## Decisions Made

- **Author every expression against the card's DECLARED identity_space**, not against whatever
  collection the file happens to make convenient. The space is the specification; the file is not.
- **Do not raise any row-level `trust.key.basis`.** The row basis is the floor and this fill's scope
  is one field; re-basing a whole row on one exercised field would overstate its other sub-claims.
- **Report a source citation as `held`, never `measured`.** Reading an assignment states an
  expression; it does not exercise it.

## Current State

Fill `8de6cabc12`, validator `fc6da7186b`, instance VALID. Push state MEASURED: **LOCAL** — push on
CLOUD is integrator-only; MSTR's next window carries it.

## The transferable half

Today's other two task orders taught that a control can report on a world it cannot reach. This one
sharpened it: **four of my six errors were predicates that accepted a value the retrieval had
already failed to produce** — a not-found string, a source line, a prefixed key, a wrong collection.
In each the check was *correct about what it examined* and the examination was of the wrong thing.

**The question that catches this class is not "did the check pass?" but "print the value it passed
on, and ask whether that value is the thing I meant."** Every one of these died the moment the
member → key → space triple was printed instead of counted. A census tells you how many passed; only
the printed value tells you *what* passed.
