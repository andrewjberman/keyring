# CVO~Z session log — 2026-07-25, GRAPHUNI TERMINAL RULING + my stale-artifact error

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`
**Andrew-delegated:** *"reopen it, have CVO deal with it."* This closes it.

---

## 1 · TERMINAL RULING: PRODUCER NON-VIABLE

`extract_gold_compute.py`'s output is **NOT a viable fixture-equivalent source** for the GRAPHUNI re-point.
The harness audit came back CLEAN (3609 raw edges / 3609 accounted, zero unmapped source or target, zero
dedup collisions — I verified the fresh artifact's edge count myself). Per my own pre-committed condition,
**a clean audit means 19 is real and non-viability rules. No further measurement passes. The chain
terminates.**

**The wire-in premise is CLOSED, not deferred.** Neither candidate source works: the producer is non-viable,
and `build_graph` is a scope retreat (it reads the local working tree — the divergent-vintage source
GRAPHUNI exists to leave). The original 2026-07-01 deferral's *"needs an architectural decision"* is
vindicated a second time, and the honest landing is that the architectural question remains open with no
in-hand answer.

**Cause 1 (lambda / `:94`, 6 members, deterministic) proceeds** — it rests on a source-level structural fact,
not on any harness measurement.

## 2 · WHY THE RULING WAS NEARLY WRONG — MY STALE-ARTIFACT ERROR

I held the gate one pass longer than my pre-commitment allowed, on a claim that **the harness demonstrably
misreports the artifact.** That claim was false. **There are two artifacts and I measured the wrong one:**

| artifact | edges from `pipeline:inf:gold:INF_build_canonical_prices` | writers into the key |
|---|---|---|
| `org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` — **month-old committed** | 13, incl. **1 WRITES_S3** | **18** |
| `.../NFRA_GRAPHUNI_REASSERT/gold_compute_producer_FULL_20260725.json` — **fresh `--full`, 3609 edges, what the harness consumes** | 12, **ZERO WRITES_S3** | **16** |

I measured the stale one. Three times. **~D's 16 was right, their zero-WRITES_S3 was right, and their
content-gap attribution for class C was right.**

**There is no mitigation, because I flagged that artifact as stale MYSELF, in this same thread.** My own
words to CTO~Z, earlier: *"do NOT treat the month-old committed artifact as ready-to-ingest; it predates the
flip, carries a null vintage."* I wrote that, then measured it as operative, then **used those measurements
to override a correct verdict from ~D and to hold a gate.** I cited my own staleness warning and walked past
it.

**RETRACTED:** (1) the 18-writer count → 16 in the operative artifact. (2) "firm-qualification splits the
convergence node" → ~D corrected me twice and was right both times; `un_s3_id` collapses both firm variants.
(3) **"the harness demonstrably misreports the artifact"** → **there was no harness defect at all.**

**CTO~Z was right and I was wrong on the substance.** Their *"five passes in, at some point the number stops
being an artifact and starts being the answer"* was correct. My counter — *stability is not validity* — was
formally sound but rested on a defect that did not exist. **The pre-commitment is the only reason this
resolved cleanly instead of becoming a standoff**, and I made it while I still expected to win the argument.

## 3 · WHAT CAUGHT IT — and it was not me

~D wrote: *"I'm copying you specifically because this directly disagrees with your count and I want you
checking my check, not just my conclusion"* — and shipped the **raw 30-edge dump** rather than the number.
They also named **both** possibilities explicitly (*"I have a bug in how I dumped, or your reproduction
picked up something that isn't there"*) instead of deferring to a verifier who contradicted them.

**Had they sent the conclusion alone, my stale number would have stood, their correct verdict would have
been overridden by a month-old file, and a non-viable producer could have been ruled viable.** The
raw-data-with-the-conclusion discipline caught a confidently-wrong verifier. That is the finding worth
keeping from this pass.

## 4 · MY FAILURE PATTERN THIS THREAD — recorded as a VERIFIER pattern, not theirs

Four errors, all the same shape: **a test aimed at the wrong layer or the wrong file, producing a refutation
of a hypothesis that was actually right.**
1. **seed COUNT vs seed IDENTITY** — tested whether match counts differed (43=43), concluded "not seeds";
   the seed is `matches[0]`, an identity question. ~D's instinct to keep pulling on find_node was right.
2. **WRITES_S3 "healthy"** — called it the sound direction; it LEADS the missing set 14-13.
3. **canonicalization terminal vs intermediate** — refuted their key-form hypothesis at the terminal-edge
   layer; it was correct at the intermediate-node layer, where they had aimed it.
4. **stale vs fresh artifact** — the worst, because I used it to override a correct finding and extend a gate.

In all four, ~D's instincts were right and my tests were misaimed. **A refutation is scoped to the layer and
the artifact it was tested against** — and a verifier who forgets that manufactures false negatives with
authority. **Being the party whose job is catching errors does not exempt me from the error classes I
enforce; today it made mine more costly, because a verifier's wrong number overrides rather than merely
adds.**

## 5 · WHAT STANDS (unaffected by my error)

SHALLOW mechanism verdict · the `:94` lambda rule (6/6 across two targets, structural — the most solid single
result in the thread) · cause-1 wiring spec · two-causes-not-one · function-grain clean across 4 targets ·
`build_graph` is not a free fallback · ~D's node-order bug catch · ~D's OPT1 self-correction · the harness
audit itself.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| Python exact-match over BOTH producer artifacts | **PASS — found MY error** | 13/1/18 (stale) vs 12/0/16 (fresh, 3609 edges) — resolved the dispute against myself |
| `find` for a second artifact version | **PASS — the decisive step** | surfaced `gold_compute_producer_FULL_20260725.json`; the whole dispute was two files |
| Replication of `PIPELINE_RE` / `un_s3_id` / guard | PASS — but on the WRONG input | transforms replicated correctly; the input file was stale, so the output was worthless |
| `sed`/`grep` on `canon_walk.py`, `chain_trace.py` | PASS | `un_s3_id` does collapse both firm variants — ~D's correction of me confirmed |

**Own errors this pass:** measured a month-old artifact I had personally flagged as stale, three times, and
used it to override a correct peer verdict and extend a gate by one pass. Caught only because the peer
shipped raw data and invited the check.
