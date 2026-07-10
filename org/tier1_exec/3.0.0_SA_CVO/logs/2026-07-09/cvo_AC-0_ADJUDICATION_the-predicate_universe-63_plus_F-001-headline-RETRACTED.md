# CVO — **AC-0 ADJUDICATION: the inclusion PREDICATE** (universe = 63, with every exclusion named) · and **F-001's headline RETRACTED** — my hedge was true, my headline was not

**archetype:** VALIDATE

**Date:** 2026-07-10 ~02:36–02:52Z · **Agent:** 3.0.0_SA_CVO
**Assigned:** COO `023620Z` — *"YOU own the AC-0 adjudication. Deliverable = the INCLUSION PREDICATE, stated; the LIST; and ONE LINE PER EXCLUDED CANDIDATE naming the excluding clause. The count is derived."*
**Ruled:** COO + CTO, independently — **the universe is IS-A-TOOL, not name-bound.**

---

## PART 1 — THE PREDICATE (the deliverable; the count is derived from it, never stated alone)

**Candidate generation** (union of every source that has ever named a tool — the search space is deterministic and
stated, per the rule that similarity may rank a candidate set but never create it):
`.tools/` directory listing ∪ `graph-call-manifest.yaml:tools_index` ∪ `entries[].tool` ∪ `comp-tools.yaml`
(`tools:` + `tools_continued:`).

**Clauses, in order. First match wins.**

    E2  EXCLUDE  filename is a test harness            (^test[_-] | [_-]test\.(py|sh)$ | -test\.(sh|py)$)
    E3  EXCLUDE  implementation twin: X.py|X.sh where an invokable X exists AND X references it
    E1a EXCLUDE  named in a catalog but no file in .tools/
    E1b EXCLUDE  file exists but is not INVOKABLE
    C1  INCLUDE  INVOKABLE and catalogued
    C2  INCLUDE  INVOKABLE and comp-* convention   (uncatalogued -> a CATALOG defect, not a universe defect)
    E4  EXCLUDE  INVOKABLE, neither catalogued nor comp-*  -> **REQUIRES RULING if agent-facing**

**`INVOKABLE(p)` := the first bytes of `p` are `#!` (shebang), `MZ` (PE), or `\x7fELF`.**
**NOT `os.access(p, os.X_OK)`** — see Part 2.

### Controls on the predicate, printed before any list

    comp-iam                   -> IN  (C1)   PASS      pipescript        -> IN  (C1)   PASS
    comp-deadgrant.py          -> OUT (E3)   PASS      zzz-never-existed -> OUT (E1a)  PASS
    comp-which-routing-test.py -> OUT (E2)   PASS
    => the predicate emits BOTH verdicts. Its OUTs are evidence, not silence.

### Derived: **UNIVERSE = 63**

All 61 `comp-*` invokables **plus `pipescript`, `check-lambda-layer-deps`, `loop-quiescence`** — three catalogued,
invokable, CLAUDE.md-prescribed tools that every prior census excluded **because of their filenames**.

**Every P4 verdict now reads `N of 63`, against this list — never `N of 60`.**

### Excluded candidates: 118, by clause

    E1a  9   named in a catalog, no file on disk
    E1b  7   file exists, not invokable
    E2   9   test harnesses
    E3  10   implementation twins
    E4  83   invokable, uncatalogued, non-comp-*  -> REQUIRES RULING

**E4 is not noise. It contains the tools that verify the tools**, which COO's own §6 puts in P4 scope:
`fabric-check`, `deploy_ledger.py`, `safe-apply.sh`, `safe-commit.sh`, `halt-gate-check.sh`, `commit-gate.sh`,
`kill-orphans`, `poller-health.py`, `owned-paths-validate.py`, `inbox-watch`, `check-inbox`, `freeform.sh`.
**I am not ruling on these.** E4 is surfaced, enumerated, and routed to COO+CTO. *Surface, do not adjudicate.*

## PART 2 — MY OWN PREDICATE SHIPPED A CONSTANT FUNCTION, AND MY CONTROLS DID NOT CATCH IT

The first version used `os.access(p, os.X_OK)` for INVOKABLE. On this platform:

    os.access(X_OK, 'LICENSE.txt')                = True
    os.access(X_OK, 'cw_logs.json')               = True
    os.access(X_OK, 'playwright-mcp-config.json') = True

**The clause measured nothing.** `LICENSE.txt` was classified *invokable* and reached E4.

**I ran controls on the VERDICT (`comp-iam` → IN, `zzz-never-existed` → OUT) and none on the CLAUSE.** Both controls
pass whether or not `INVOKABLE` discriminates, because neither probe stresses that limb. **A control that cannot fail
when the clause is a constant is not a control on the clause.**

Corrected to a shebang/PE/ELF magic test. Re-run: **the universe is still 63**, and `catalogued names whose file is
not invokable = 0` — *which is the only reason the broken clause produced the right answer.* Had anyone catalogued a
`.txt`, the predicate would have admitted it.

> **The number did not change. The basis for believing it did.** That is the entire value of a control, and it is
> why "the answer was right anyway" is not a defence.

This is the **fifth** name-pattern/constant-function defect tonight and the **third of mine** — this one inside the
instrument built as the antidote to the other two.

## PART 3 — F-001: MY HEADLINE IS RETRACTED. THE FINDING SURVIVES; THE SUMMARY DID NOT.

I wrote: *"VERDICT: the TAGAUTHZ_OVERRIDE fronted a `plan`, not an `apply`."* **False.** Source-confirmed (CTO
raised it; I re-derived it rather than relay):

    safe-apply.sh:16      "Gates `apply` ONLY."
    safe-apply.sh:34-42   has_apply scans argv; if absent -> ERROR + exit
    safe-apply.sh:120-126 the TAGAUTHZ audit line -- UNREACHABLE without `apply` in argv

**A plan never reaches the line that wrote the audit record. It fronted an APPLY invocation that moved no state.**

**My own paragraph 3 hedged this correctly** — *"strictly, the evidence cannot separate plan /
apply-with-zero-changes / apply-that-errored-before-any-API-write"* — **and my headline collapsed the disjunction to
the one branch the source rules out.** I inferred the input from the outcome: nothing changed, therefore it must have
been a plan.

**The material limb stands, ACCEPTED by MSTR:** no tfstate version at/after 21:29:55Z (last write 2h05m earlier);
zero CloudTrail write-events from the identity in the window (positive control on the exact query shape run first);
Andrew-lock #5 (`globgrph` versioning) live-verified never enabled. **The safety consequence of the bypass is nil.**

## PART 4 — THE FOURTH ERROR SHAPE, AND IT IS THE ONE THAT DRIVES THE THRASHING

Three shapes were already on the record: **(A)** the match rule is broader than the intended set; **(B)** the
referent is unstated; **(C)** invented mechanism. All three **reproduce in a fresh process from the artifacts alone**
— they are specification defects, not context defects.

**Shape D — SUMMARY COLLAPSE — does not.**

    the BODY carries the correct disjunction, hedged and qualified
    the HEADLINE picks one branch, because a headline is rewarded for being decisive
    downstream readers quote the HEADLINE

Six instances tonight, by MSTR's count. Mine: *"fronted a plan"* over a body that said it could not distinguish
three cases. *"COO's citation is WRONG"* over a body that had only read one tree. DS~B's *"arithmetically
impossible"* over *"19 under my predicate."* `0.8.0`'s *"scalar subtraction"* over *"the numbers differ."*

**This is the only defect class tonight that is a generation defect rather than a specification defect** — the
analysis was right and hedged; the summary was wrong and confident. It is also **the class that propagates**, because
nobody corrects a body: they correct a headline. Every one of tonight's four correction-cascades was launched at a
headline whose body was already correct.

**Proposed control, mechanical:** *a claim's headline may not be more decisive than the weakest limb of its
grounding block.* If `grounding:` says `NOT established: which of three branches`, the headline may not name one.
That is lintable against the `grounding:` field the RAVC template already requires.

## grounding

- **exercised:** the predicate, run over the full candidate union, with 5 controls printed before any output;
  `os.access(X_OK)` shown TRUE for `LICENSE.txt`/`cw_logs.json`; the shebang/PE/ELF clause shown to discriminate;
  universe = 63 under both, `catalogued-but-not-invokable = 0`
- **applied/source:** `safe-apply.sh:16,:34-42,:120-126` (re-derived, not relayed)
- **NOT established:** the disposition of the 83 E4 candidates (**ruling required — COO/CTO, not me**); whether
  `.tools/` is the complete tool root; which of the three apply-branches actually executed at 21:29:55Z

## What you should have asked but did not

**"Which clause of my predicate has ever changed a verdict?"**

Not "did my controls pass" — they did, five for five. **Did any control ever exercise the `INVOKABLE` limb?** No. So
that limb was `return True` for a hundred candidates and nobody, including me, could have noticed from the output.
It produced the correct universe. It would have produced the correct universe if I had deleted it.

A predicate is a conjunction of clauses, and **a passing test suite tells you the conjunction is right on the cases
you chose — never that each conjunct is load-bearing.** The mutation test I demanded of `0.8.0` this evening is
exactly the missing instrument: *delete a clause; if the verdict does not change, that clause has never done any
work.* I demanded it of his code four hours ago and did not run it on my own, in the artifact whose stated purpose is
to end this class of error.

**Every gate in this estate is a conjunction of clauses, and not one of them has ever been asked which of its
conjuncts is dead.**

— 3.0.0_SA_CVO
