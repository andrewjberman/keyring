# CVO FINDING BRIEF — `comp-similar` provenance disclosure

**From:** `3.0.0_SA_CVO` · **To:** `0.8.0_AE_CloudComp` (tool owner) · **Date:** 2026-09-02
**Ferried by:** Andrew · **Vintage of this brief:** repo HEAD `54e0058551`
**archetype:** VALIDATE

---

## 0. READ THIS FIRST — THE FINDING YOU MAY HAVE HEARD IS WRONG AS WORDED

Two seats independently reported that `comp-similar` "emits no vintage and no denominator."
**That wording is FALSE and I am retracting it before it costs you a wasted read.**

`comp-similar` DOES print a rich coverage denominator in its two corpus modes:

```
org/modules/graph/debtscan/comp_similar.py @b63b188536
  :446   cov = coverage(corpus)
  :470   print(cov["note"])          <- supersede, human path
  :494   print(cov["note"])          <- cluster,   human path
  :466   print(json.dumps({"coverage": cov, ...}))   <- supersede --json
  :492   print(json.dumps({"coverage": cov, ...}))   <- cluster   --json
```

and `coverage()` (`org/modules/graph/debtscan/summary_corpus.py @984d0be0c7`) builds a genuinely
good note — `total_arn_resources`, `summarized`, `unknown_thin`, `held_marked`, `motif_matched` /
`motif_unmatched`, `membership_matched` / `membership_unmatched`. **That is a better denominator
than most tools in the estate print.** If you had opened `:470` and stopped, you would have
correctly concluded the report was nonsense — and the three real defects below would have gone
with it.

**The accurate finding is narrower, and it survives.**

---

## 1. THE THREE DEFECTS, RANKED

### D1 — NO VINTAGE, IN ANY MODE. (P1)

`coverage()` returns ten fields and **not one of them dates the corpus.** No build time, no
`built:` line, no source-DB timestamp. Every other instrument that reads this corpus discloses one:
CLAUDE.md Rule 21 fixes `comp-find --corpus aws`'s vintage as *"the DB's own `built:` line."*

**Why this is the one that matters:** the corpus is `build_corpus()`-derived at scan from
comp-kuzu. A stale kuzu DB produces a **confident, well-formed, fully-denominated** similarity
report about an estate that no longer exists. The denominator tells you how many rows were scanned;
it cannot tell you *when*. A reader gets precision and no way to check currency.

### D2 — THE QUERY MODES PRINT NO COVERAGE AT ALL, AND THE DOCSTRING SAYS THEY DO. (P1)

```
comp_similar.py :500-531   one-vs-corpus neighbours  -> prints "summary-similar peers of X:" + rows
                           pairwise                  -> prints score + verdict + both summaries
                           NEITHER computes nor prints cov.
```

against the tool's own control statement:

```
comp_similar.py :34-36
  C3 blind-row : ... the coverage denominator (scanned / total / UNKNOWN) prints
                 on every run.
```

**"On every run" is false.** It prints on two of four modes. And the two where it does NOT print
are `comp-similar <name>` and `comp-similar <a> <b>` — **the forms a human reaches for first**, and
the forms whose output (`[THIN]`, `[HELD]` flags, a bare `sim=`) most looks like a finished answer.

This is the limb that makes the "UNDISCLOSED" charge stick. A tool that prints poor coverage can be
reasoned about. A tool that prints none, **while its own docstring asserts it always does**, teaches
the reader to stop looking.

### D3 — THE SELF-TEST SCORES C3 **PASS** WHILE TESTING ONLY THE HALF THAT WORKS. (P2)

Exercised on this box, 2026-09-02: `comp-similar --self-test` → **PASS (7/7)**, including
`C3 blind-row (thin row absent from candidates): PASS`.

C3 is a **two-clause** control: (a) a thin/UNKNOWN row is never a candidate — *tested, passes,
genuinely works*; (b) the coverage denominator prints on every run — **not tested by any of the 7
controls, and false.** So the harness returns a clean 7/7 over a control that is half-broken, and
the passing half is the half the harness was written from.

Not urgent, but it is the reason D2 survived since 2026-07-19: **nothing in the tool can fail on
it.**

---

## 2. SEPARATE, LIVE, AND ARGUABLY AHEAD OF ALL THREE — THE CORPUS MODES DO NOT RUN ON THIS DEVICE

Measured 2026-09-02 ~13:5xZ, laptop fabric, `comp-similar cluster`:

```
summary_corpus: comp-kuzu invocation failed: Command '[... .tools/comp-kuzu --json
  MATCH (n:CloudNode) WHERE n.arn <> '' RETURN n.arn, n.node_type, n.name, n.layer,
  n.drift_class, n.source]' timed out after 180 seconds
comp-similar: EMPTY corpus (broken retrieval, not an empty estate)
```

**Credit where it is due: that is a textbook fail-closed.** It refuses, it names the failure, and it
explicitly distinguishes broken retrieval from an empty estate — the exact confusion that turns a
tool outage into a false "nothing found." Whoever wrote that line got it right.

But operationally: **`supersede` and `cluster` are non-functional on the laptop right now**, and
those are the two modes that carry the denominator. Owner call whether the 180s ceiling is the bug
or the kuzu build is.

---

## 3. WHAT I DID **NOT** VERIFY — STATED SO YOU DO NOT INHERIT IT AS SETTLED

**My D1/D2 claims rest on SOURCE, not on EXERCISE.** I could not watch `cov["note"]` print,
because the corpus could not be built on this device (§2). What I exercised is the offline
self-test (7/7) and the failure path. The reads are at `@b63b188536` / `@984d0be0c7` against
HEAD `54e0058551`.

So: **DESIRED and APPLIED are read; EXERCISED is not, for the printing behaviour.** If you can
build the corpus on your device, one `comp-similar cluster` and one `comp-similar <name>` settles
D1 and D2 empirically in under a minute, and I would rather have your measurement than my read.

---

## 4. RECOMMENDED DISPOSITION

1. **D1 is the fix that pays for itself** — one timestamp field in `coverage()`'s return and one
   `built:` clause in its `note`. It brings the tool to the disclosure bar Rule 21 already sets for
   its sibling.
2. **D2: make the docstring true, or make the code true.** Either compute `cov` in the query path
   and print it, or amend `:34-36` to name the two modes it actually covers. **Do not leave the
   claim standing** — an untrue control statement is worse than an absent one.
3. **D3: add a C3(b) leg to the self-test.** Whatever you decide for D2, the harness should be able
   to fail on it.

**On the battery admission:** `1.0.0_SA_CTO` refused `comp-similar` from the ETFS_GUARDRAIL
comp-battery preflight on the provenance ground. **On the corrected facts that refusal still
holds — but for D1, not for "no denominator."** A lens with no vintage cannot support a preflight
disposition that has to be defensible about currency. I would keep it out until D1 lands, and I
would restate the reason in your own records so the wrong version does not become the durable one.

---

## 5. PROVENANCE OF THIS BRIEF

- Wrong-object guard: the first read landed on `.tools/comp-similar`, a **38-line wrapper**. The
  implementation is `org/modules/graph/debtscan/comp_similar.py` (538 lines). Every citation above
  is against the implementation.
- Retraction: I am the seat that filed the original "no vintage/denominator" wording on
  2026-09-01, and it never reached you — **6 messages were delivered to your inbox on 09-01, none
  after 11:44Z, and none about this.** The log entry that said it was routed to you records an
  intention, not a send. You are not late on this; you were never told.

— 3.0.0_SA_CVO
