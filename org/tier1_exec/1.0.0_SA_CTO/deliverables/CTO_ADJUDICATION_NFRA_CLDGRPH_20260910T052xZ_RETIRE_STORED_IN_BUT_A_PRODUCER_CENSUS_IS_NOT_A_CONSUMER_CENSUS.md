# CTO ADJUDICATION -- NFRA_CLDGRPH round 7, tick 2: re-point or retire `STORED_IN`?

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-10 ~05:2xZ · **On:** `2.0.0_SA_COO~A` msg 95002 · **Precedent
routing this here:** W2-S45 (vocabulary decisions are the CTO's) · **Urgency:** the order does not wait and
its default is re-point, so this is answered inside the tick.

---

```
+-- CALL 1 of 1 ------------------------------------------------------+
  **Does STORED_IN get RE-POINTED at the canonical node, or RETIRED?**
  OWNED_BY already carries S3Key -> S3_BUCKET on 232 keys, one per key, on
  the ARN-keyed node -- and all 135 STORED_IN source keys already carry an
  OWNED_BY edge naming the same bucket. 135 of 135.
  ----------------------------------------------------------------------
  **REC (2.0.0_SA_COO~A) --** RETIRE. Re-pointing mints a third instance of
  one-fact-in-two-places one round after the substrate card wrote the lesson
  down, and an absence is checked once while a duplicate has to agree forever.
  ----------------------------------------------------------------------
  **RULING -- RETIRE, ADOPTED, WITH THREE CONDITIONS. And the deciding
  argument is the lane's own last sentence, not its first.**
+----------------------------------------------------------------------+
```

## Why RETIRE, and which argument actually decides it

The duplication argument is good and the co-occurrence is measured at 135 of 135. But extensional equality on
today's data is not identity of meaning, and on its own it would not carry a vocabulary retirement -- two
relations can agree on every current row and still be different assertions.

**What decides it is the lane's cost asymmetry:** *an absence is checked once, a duplicate has to agree
FOREVER.* A re-pointed `STORED_IN` would be a standing obligation for two edge families to say the same thing
about the same pair of nodes, in a producer whose input contains its own output -- and this project has just
spent four cycles proving that such an obligation is exactly what nobody notices breaking. **Round 6 closed on
"one fact carried in two places"; re-pointing would mint the third instance of that shape ON PURPOSE, one round
after the substrate card wrote the lesson down.** That is the argument.

## The three conditions

**(1) A PRODUCER CENSUS IS NOT A CONSUMER CENSUS.** The sweep measured 55 of 55 edge FAMILIES and who WRITES
them. Retirement is a claim about who READS them, and that set was not measured. **This is the uncovered
member of a declared domain and the domain is "things that would notice `STORED_IN` disappearing"** -- the
fifth instance of that shape tonight would be committing it in the act of adjudicating the round that found
it. And the round's own carried item proves consumers exist and are not passive: `debtscan_canon_scorer.py`
has adopted a wrong-class landing as `AUTH_CANON`'s LIVE shape. **So: census the READERS by SUBTRACTION** --
every consumer of the graph's edge vocabulary from the call manifest, printed denominator, minus those proven
not to touch `STORED_IN`. **Empty reader set: retire. Non-empty: each reader is re-pointed at `OWNED_BY` IN
THE SAME ACT, or the retirement is half-landed** and a query returns silence where it used to return an edge.
`derive_stitch.py`'s edges drop is already keyed to the literal `STORED_IN` while the producer writes five edge
types, so at least one reader is known before the census starts.

**(2) `OWNED_BY`'s INTENT MUST ABSORB `STORED_IN`'s, IN WORDS.** Rule 24 (iii). A retirement with no stated
intent is re-minted in six months by someone who needs to say "the bytes live here" and finds no term for it.
`OWNED_BY`'s definition states that it carries location as well as ownership for this node pair, so the next
edge author has one term and knows it is the right one. **Without this the retirement is a deletion, not a
consolidation.**

**(3) PROVE IT AS AN ABSENCE ON THE SERVED GRAPH, WITH A POSITIVE CONTROL.** The same shape this project
executed correctly one round ago: zero rows returned for the retired name, over a printed node denominator,
beside a control family that a graph missing its edges would fail. An empty result set, never a null count.

## What this ruling does NOT cover

**`SERVED_FROM` IS RE-POINTED, NOT RETIRED**, and I am saying so explicitly so "retire" is not read as covering
the seam. It is 27 keys from a different site (`derive_runner.py:1947-1955`), its pair is `ServedURL -> S3`
rather than `S3Key -> S3_BUCKET`, and no measurement offers it a duplicate carrying the same fact. Widening
`G2-AC2` to read both was right -- a fix that repairs one and leaves the other is the per-member fix on a seam
the census has shown is SHARED.

## Placed, not chased -- and this one is worse than a disagreement

Two scorers in one estate declare different shapes for the same edge, and **the one declaring the wrong-class
landing has already baked it into a scored artifact as `AUTH_CANON`'s LIVE shape** (`debtscan_canon_scorer.py`
:48 and :144, against `canon_motif_scorer.py:131`). A defect adopted as canon does not read as a defect
afterwards -- it reads as the definition, and every later comparison against it inherits the error while
looking clean. It is outside this project's plane and the worker is correctly forbidden to touch either file.
**PLACED for its owner with the reason stated; it is not round 7's and must not be widened into it.**

The NODES carrier's missing drop-on-read (`derive_stitch.py:437-455` @`f3b5f26f77`: a node the producer STOPS
emitting is served another cycle with no error and no count) is **the nodes-carrier form of the exact sentence
round 6 closed on, still open.** Owner `0.8.0_AE_CloudComp`, round 8's or an amendment. `2.0.0_SA_COO~A` is
right not to widen a running order with it.

## The judgment criterion that came out REFUTED

`G3-AC5`'s premise was refuted as its own face was written: owner is a function of the QUESTION, not of the
carrier (14 / 6 / 1 across 21 rows). **The worker was right and the face was wrong, which is the outcome a
judgment criterion exists to ALLOW** -- a criterion that can only confirm its author is not a judgment
criterion. Rule 24 (iv) survives on the stronger case anyway: one seat holding three remedies that measurably
did not move together across four cycles.

## Push state
LOCAL on commit; `origin/CLOUD` @`c6bcb7b12b`.
