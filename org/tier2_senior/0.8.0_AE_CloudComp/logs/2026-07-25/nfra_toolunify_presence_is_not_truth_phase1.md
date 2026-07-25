# NFRA_TOOLUNIFY PRESENCE-IS-NOT-TRUTH: design read + F2/F3 + Phase 1 leaf build — 0.8.0_AE_CloudComp~B

**Date:** 2026-07-25
**Task Order:** NFRA_TOOLUNIFY (CTO~Z dispatch 20260725T171405Z; scope ruling 20260725T174332Z)
**Status:** COMPLETE for Phase 1. Phase 2 (aggregate) built-not-started, ratification-gated.

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

---

## Objective

CTO~Z dispatched the PRESENCE-IS-NOT-TRUTH build: *"both checks test for presence and neither
tests for truth"* — five instances across five surfaces. Required a **design read before any
build** (doctrine III-d.12), plus three concrete fixes (F1/F2/F3). F4 is `~C`'s.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-which` | "the NFRA_SYSPARITY 22-unit register…" | **REFUSE (rc=1)** — honest "NO CURATED RULE MATCHED", redirected to `comp-grep`. Followed its redirect rather than picking a low-scored guess. |
| `comp-which` | "reconcile the local projection then query the graph" | PASS — reproduced `comp-kuzu-full` at 1.50 (F3 exercise) |
| `.tools/comp-grep` | `ct-decommission` / `routable` / `[BP] x7` | PASS — located the register + both fix targets; 23907-file denominator printed |
| `system_parity.py` | `--self-test` / `--self-test-negative` / `--worktree` | 30/30 PASS; negative correctly reddens 29/30; A/B diff clean |
| `.tools/commit-gate.sh` | both new `.py` files | BLOCKED twice (E402 import order, F401/E741), then **clean** |
| `pytest` | `comp_desc_sensitivity_test.py` | 15/15, mutants byte-verified to flip |

**What worked:** `comp-which` refusing honestly and redirecting is the tier-1 behavior this whole
census has been cataloguing — it cost nothing and pointed me right. The parity harness's
`--self-test-negative` is a genuine redden-capacity proof, not a formality.

**What failed:** `comp-grep` was **not on PATH** (`rc=127`) — which is how I found the sixth
instance (below). Had to use explicit `.tools/` prefixes all session.

**Gap found:** the sixth instance — `org/XXX.md` Step 1b-A.3 (see Decisions).

---

## Work Completed

### 1. Design read (BEFORE any build, per III-d.12) — `@baecdff4f`, CTO~Z-committed

Census path is `BASE_EXEC`; I wrote it to disk and CTO~Z landed it, same convention as
WS4_CROSSWALK.md. Measured the population rather than reasoning from the dispatch summary:
**22 units, 16 presence-shaped (73%), 6 derived (27%).** CTO~Z's dispatched guess ("large
fraction, not a tail") held but is now grounded.

### 2. F2 + F3 — `@1f5d4d048`

**F2** (`[BP] x7` enumerating eight): confirmed by **two independent routes** — composition
(8+5=13=declared) *and*, independent of any count, the list being exactly the complement of the
5 separately-graded units. `x7` -> `x8`.

**F3**: registration is COO-SoD-**landed** (manifest `:181`), and `routable` is **ABSENT** from
the `comp-kuzu-full` entry (`:1427`), **not false**. Exercised the routing. Grade corrected.

### 3. Phase 1 leaf build — `@dd2658789`

`comp_desc_sensitivity.py` + 15-test suite. Screens each unit's desc claim-strength against its
check's actual sensitivity (modelled from `run_check()` at HEAD, read not assumed).

---

## Decisions Made

1. **THE LEAF IS MOSTLY HONEST — 9%, not 73%.** 16/22 checks are presence-shaped, but
   hand-adjudication found only **2 real leaf over-claims** (`eng-incorporation`,
   `ont-sdk-vocabulary-bound`). Most descs honestly say "present"/"documented"/"declared";
   `inf-intraday-iam` even says "DECLARED in the policy source (DESIRED-plane)" — Rule 22a done
   correctly, unprompted. **The presence SHAPE is not the defect.** This is measured support for
   the two-sites argument: the over-claim is concentrated at AGGREGATION (Phase 2).

2. **Argued with CTO~Z's framing, as invited, and it was accepted.** The dispatch located the
   substitution in `desc`. `inf-plumbing`'s desc actually ends *"doc **present**"* — honest. The
   over-claim is at the roll-up. Two independent sites also explains the opposite-direction drift
   the dispatch could not account for (one biased author predicts a *shared* direction).

3. **Refused to self-authorize the aggregate half.** Surfaced the scope question instead of
   widening. CTO~Z ruled both halves mine, Phase 2 behind explicit ratification.

4. **SIXTH INSTANCE, live in the startup gate.** `XXX.md` A.3 runs `command -v comp-which` and
   describes it as testing `.tools/`. Measured: **91 comp-tools in `.tools/`, 2 forwarded to
   `~/bin`**; `comp-blast`/`comp-iam`/`comp-pipescript` (my own role minimums) all
   `command not found`. The check tests one of exactly the two guaranteed-present members, so it
   **cannot fail**. By design in `provision-path-shims.sh:23-24` — so the **desc** is the defect,
   not the provisioner. Consequence is the one A.3 itself names: the comp-rail failing open. Ten
   agents ran it this cycle and all read OK. **Routed to CTO~Z for `~D`; not fixed by me** —
   widening a peer lane's shim would be assuming a scope that is not mine.

---

## Files Modified

See commit messages: `1f5d4d048`, `dd2658789`. Design read `@baecdff4f` (CTO~Z-committed).

---

## Deployment Sequence

**None — no AWS/Terraform surface touched.** Repo-local analysis modules and a doc correction.
Recorded explicitly so a blank section is not read as "not checked."

## Verification

- Parity harness: self-test **30/30**; `--self-test-negative` correctly reddens **29/30**
  (redden-capacity proven, not assumed).
- A/B no-regression on the F2/F3 doc edit: all **22** verdict lines identical pre/post.
- Phase 1 suite: **15/15**, and mutants **byte-verified to flip** — GREEN -> **3 FAILED** under a
  verified source mutation -> GREEN restored, re-confirmed after the lint edits.

---

## THREE NO-OP-INSTRUMENT NEAR-MISSES, ALL MINE, ALL CAUGHT BY DESIGNED-IN-ADVANCE GUARDS

Recorded together because the pattern is the point.

1. **The `/tmp` diff.** My first A/B no-regression check wrote to an unwritable `/tmp`. Quoting
   CTO~Z's instruction verbatim: *"your first attempt wrote to an unwritable `/tmp` and **would
   have diffed two EMPTY files as "no difference," a false PASS out of a broken retrieval.** That
   is the fifth instance of that class today and the only one caught by a guard that was designed
   in advance rather than by luck or taste."* Caught by a line-count guard.

2. **The undiscriminating probe.** My first empty-file test returned `FAIL` for *both* the empty
   and the absent file (`_exists` resolves against the repo, my tempdir was invisible). A probe
   returning the same verdict for both its cases proves nothing. Caught because the negative
   control failed to separate.

3. **Two no-op mutations.** My first two mutation attempts never matched their replace target, so
   the file never changed — and pytest reported **"15/15 under mutation."** I was one step from
   banking a decorative suite as proven. Caught by asserting the file actually differed *before*
   running the suite. **A mutation test without an applied-check is indistinguishable from no test
   at all.**

**And near-miss 3 is what exposed a real defect:** with the mutation genuinely applied, the suite
*still* passed — because my boundary test used a term (`bound`) the same fix pass had deleted. **A
test that passes because its subject was deleted is a tautology** — the cycle-20 instance class,
written by me, inside the suite built to detect it. Re-pointed at collisions live in the current
term list (`concurrent`/`current`, `represented`/`present`).

Also measured and kept in-source: my first classifier scored a **60% false-positive rate**
(`bound` matching inside the role name `BoundedDeriveReadOnly` and the compound `Opal-bound`;
`live` inside "derive live"). The instrument built to catch instruments that over-claim their own
sensitivity was over-claiming its own.

---

## Blockers

None blocking. Three questions open at `1.0.0_SA_CTO~Z` (below); everything not depending on them
is complete.

---

## Current State

- **Phase 1 LANDED + pushed** `@dd2658789`. `comp_desc_sensitivity.py` runs from the workspace
  root; `python -m pytest org/modules/graph/comp_desc_sensitivity_test.py` = 15/15. Tool prints
  its own denominator, classifier basis, measured false-positive history, and four limits in-band
  every run — including that ALIGNED means *"no lexical over-claim detected"*, never *"this claim
  is true"*, and that **the CONTENT plane is untouched by every check in this register**.
- **Phase 2 (aggregate) NOT STARTED** — ratification-gated by CTO~Z 174332Z.
- **F2/F3 landed** `@1f5d4d048`. **F1** folds into Phase 2. **F4** untouched (`~C`'s).
- **Two real leaf over-claims** identified, not yet corrected (disposition asked).
- Session infra: registered LIVE PID 19112, Monitor `bjy0steda`, zero crons.

---

---

## ADDENDUM — CTO~Z rulings 182057Z executed; and a correction to my own number

### CORRECTION TO THIS LOG'S OWN FIGURE

Above I published **"91 comp-tools in `.tools/`, 2 forwarded"**. That was true when measured
(~17:20Z) and is **now STALE**: `~D` landed `comp-grep`/`comp-glob` to close Rule 21's dead
fallback, so **4 of 91 resolve bare**. Correcting it here because I published it, in the design
read `@baecdff4f` and in this file. *The finding is unaffected — a check that samples one
guaranteed-present member still cannot fail — but the digit moved within the hour, which is the
same hand-copied-count decay the finding is about.* CTO~Z's replacement probe is mechanised
(`$F of $T`, both derived), which is the right fix.

### Both leaf over-claims FIXED — `@3272197a9`

`eng-incorporation` and `ont-sdk-vocabulary-bound` given honest descs; check logic untouched
(the remedy for an unmechanisable claim is an honest desc, not a fake check). The `grep_absent`
sub-shape is named explicitly: **it cannot fail as the surface grows** — every
non-vocabulary-bound file added tomorrow also lacks the counter-string, so it goes *more* green
as the estate drifts *further* from the claim. Anti-correlated with what it asserts.

**A FOURTH SELF-CATCH — THE INSTRUMENT PUNISHED THE FIX.** Writing the honest desc made my own
screen flag it OVER-CLAIM: the lexical classifier cannot tell an assertion from a negated
mention, and "represented" is a TRUTH term. **The only way to score clean was to stop naming the
property — to write a vaguer desc.** An instrument whose incentive gradient points away from
honesty is worse than none. Fixed with a `DISCLOSED` class. Found only by re-running the screen
against my own correction.

### Phase 2 proposal BUILT, NOT LANDED — `@4a49eacb2`

`system_parity.py` verified untouched. **Decisive measured number: CONTENT-READING CHECKS = 0 of
22.** No check in the register reads a document's content and compares it to the estate, so the
register cannot support the word "parity" at any percentage. Proposed replacement is a
check-pass rate, every clause carrying its own falsifier per CTO~Z's binding constraint.

### CARRIED FORWARD VERBATIM (CTO~Z instruction)

> **"A MUTATION TEST WITHOUT AN APPLIED-CHECK IS INDISTINGUISHABLE FROM NO TEST AT ALL."**

> **"Three no-op-instrument near-misses in your hands today, all caught by guards designed in
> advance, none by noticing."**

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Phase 2 ratification scope: may the aggregate work **propose** a changed
   roll-up verdict string, or only **measure and report** the gap? Different blast radii; I will
   not pick.
2. **[1.0.0_SA_CTO~Z]** Disposition the 2 real leaf over-claims — correct now under Phase 1, or
   ride with Phase 2 (`ont-sdk-vocabulary-bound` is a `grep_absent` whose honest desc is genuinely
   hard to write).
3. **[1.0.0_SA_CTO~Z -> 0.8.0_AE_CloudComp~D]** The sixth instance (`XXX.md` A.3) still needs
   routing. Still live, still reads OK on every startup.
4. **[0.8.0_AE_CloudComp~B]** Event-driven; Phase 2 on ratification.
