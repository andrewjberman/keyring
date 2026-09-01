# CVO ADJUDICATION: the canonical workflow, its five forks, and what is GATED vs SUGGESTED

**Andrew-direct 2026-09-01, transcript `9-1 flow_6519.txt`. ANDREW AGREED TO ALL FIVE ANSWERS BELOW**
(*"This is all good I agree with these"*). **Ten steps, five forks, each answer classified GATED
(mechanical, refuses) or SUGGESTED (judgment, owned).**

Andrew's standard, verbatim: *"anything that is simply 'guidance' may dissipate or otherwise be
inconsistent over long-running sessions."*

⚠ **REWRITTEN 2026-09-01 ~19:0xZ**: the first copy was destroyed on disk by another seat's live merge
in the shared worktree before it could be committed. Recovered from context.

---

## 0 · THE TEN STEPS, AND WHAT EACH ALREADY HAS

| step | act | state |
|---|---|---|
| 1 | CRO analyses a topic -> brief | exists, unstructured |
| 2 | CTO writes the PRD | exists. **ENDPOINT-FIRST is Andrew's new addition and is load-bearing -- see F4** |
| 3 | register as project, tag to `DIRECTIVES.yaml`, declare fabric (laptop vs site Z) | exists |
| 4 | handoff to COO | exists |
| 5 | COO atom-decomp + lens battery | decomp exists; **the battery is new** |
| 6 | dispatch TOs | **NOW GATED** -- `.tools/to-pipeline-gate.py`, wired in `safe-commit.sh` + `pre-commit` |
| 7 | worker hits a surprise | **trigger was undefined -- F3** |
| 8 | surprise -> investigations JSON | **schemas + 18 dirs EXIST**; `comp-surprise` is the rollup reader |
| 9 | CVO legitimises / invalidates | **disposition enum EXISTS** with a Rule 24 record |
| 10 | remediation handoff | **split was undefined -- F4** |

⭐ **Steps 8-9 are far more built than the transcript assumes.** `investigation_item.schema.json` and
`remediation_row.schema.json` exist; 17 projects carry an INVESTIGATION doc; the disposition axis is
`UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING`. **`comp-surprise
--armed --project --all --json` already reads them.**

---

## FORK 1 · THE STEP-5 LENSES AND THE COVERAGE-COMPILATION GATE

Andrew: *"We cannot have lenses that are using outdated surfaces when they come to their conclusions."*
**That constraint is MEASURABLE, so it should BE the gate.**

```
  comp-pipescript      RUNTIME-COMPILED -- 4x ast.parse + 10x glob/os.walk per call. MEASURED.
  the dependency graph EXPLICITLY CACHED -- rule 20: "QUERY, never rebuild; read the provenance header"
  comp-find --corpus aws  CACHED with a DECLARED vintage ("the DB's own built: line", rule 21)
```
>> **THE GATE (quantitative): a lens is admissible to the canonical step-5 battery only if it EITHER
compiles its corpus at runtime OR prints its corpus vintage -- AND the `<preflight>` record captures
which.** One extra field on the block already built. <<
⛔ **This disqualifies nothing outright but forces disclosure**: the dependency graph is cached BY
RULING, so any lens reading it enters as CACHED and must print the provenance vintage.

> ## ⛔ MEASURED 2026-09-01 -- THE GATE HAS NOW BEEN RUN. TWO CLAIMS ABOVE ARE FALSE.
> Full record: **`CVO_FORK1_LENS_ADMISSIBILITY_MEASUREMENT_20260901.md`**. Result: **7 ADMITTED,
> 1 REFUSED.** Corrections to THIS table, so nobody reads the pre-measurement version as settled:
>
> **(a) The "cached dependency graph" clause does not apply to `comp-blast`.** It does not read that
> graph -- `cli.py:812`, *"the main path's universe is kuzu"*; the old trace universe is **retired**.
> It **already prints a richer vintage than this gate demands** (`built:` + age + both Nessie snapshot
> ids + per-table cadence). The clause was inherited from Rule 20's prose about a different artifact.
>
> **(b) `comp-iam` is NOT "lambda entry points only"** -- measured `Lambda 166 / EC2 21`. Its real
> self-declared holes: **24 policy blocks NEVER SEEN** and **2 unparsed deny statements**, and its own
> banner says it **CANNOT answer "is this denied?"** -- covering NEVER#1's cross-firm Deny belts.
> **Silence from this tool must not be read as allowed.** That is the bound a decomp must carry.
>
> **(c) REFUSED: `comp-similar`** -- emits no vintage and no denominator on EITHER carrier (`--json`
> top-level keys are exactly `['arn','neighbors']`), while reading the same kuzu corpus `comp-blast`
> prints a header over. Self-test is 7/7; the tool is not weak, it is **undisclosed**. Withheld from
> the battery pending a provenance header (`0.8.0_AE_CloudComp`).
>
> **(d) PROPOSED THIRD LIMB, at Andrew:** admissible only if the lens prints a **DENOMINATOR or an
> explicit BLIND/COVERAGE statement** with its answer. A vintage dates the corpus; it cannot say the
> lens was blind on YOUR subject. Specimen: `comp-dataflow origin perfrp_emit_core.py` returned
> `2 reads scanned, 2 unresolved-dynamic (blind)` -- vintage alone would have looked like an answer.
> Disqualifies none of the seven; costs one `<preflight>` field.

**THE BATTERY (from a 106-tool scan):**
| lens | answers | note |
|---|---|---|
| `comp-blast` | blast radius of the change | the most decomp-relevant question there is |
| `comp-pipescript` | pipeline script dependencies | runtime-compiled, measured |
| `comp-dataflow` | value-origin trace + canonical-source assertion | "where does this number come from" |
| `comp-similar` | BM25 on what a resource DOES | BUILD-LADDER rung 2, mechanized |
| `comp-schedule` | the gate ledger: what is armed, on whom, still real | found a gate SATISFIED 2026-07-13 still armed |
| `comp-iam` | permissions on the touched resources | ⚠ **population is LAMBDA ENTRY POINTS ONLY** -- the EC2/SSM chain is invisible; that hole cost five seats an afternoon on 09-01 |
| `comp-trigger` | EventBridge **/ Scheduler** forensics | **would have answered the 12:45Z question in one call instead of four wrong-plane censuses** |
| `comp-denytest` | proves an IAM change against LIVE evaluation | the EXERCISED rung `comp-iam simulate` cannot reach |

⛔ **NOT admitted:** `comp-atomcheck` is not a decomp checker (`--product/--firm/--atom 1-9`, data
archetypes). `comp-heat` is ADVISORY estate hygiene -- possible exception `comp-heat drift` (writes
not in a commit) as a pre-decomp stability check.
⚠ **UNMEASURED: the compilation property for most of the battery.** One read per tool, and it must
**precede** admission.

---

## FORK 2 · comp-adversary AT STEP 5

**ANSWER: step 5.**
>> Its product is the **UNCITED-SIBLING LIST** -- *what did this decomp not look at.* That is a
DECOMP-COMPLETENESS question and has **no meaning at step 9**, where there is one finding and no
complement to compute. <<
⚠ **THE BOUND THAT DECIDES HOW TO RUN IT:** it expands from **CITED paths**. A thin decomp yields
*"0 uncited siblings"* over a directory holding six live files -- nothing wrong and nothing examined.
**So: run it AFTER the decomp is written, and RECORD THE CITED-PATH DENOMINATOR. A 0 over 0 is an
unrun check, not a clean bill.**
**GATED** that it ran and that its denominator is recorded. **SUGGESTED** what to do with the list --
the list is an assignment, not a finding.

---

## FORK 3 · THE SURPRISE TRIGGER

>> ### **Did I have to do something the TO did not say to do, or could I not do something the TO said to do?** <<

Binary, answerable by the worker without judgment, needs no taxonomy at file time. It is the
definition of a **SPEC-vs-WORLD MISMATCH**.

⭐ **VALIDATED AGAINST ALL 17 ROWS ALREADY FILED on `ADVI_PERFRP`. Zero exceptions:**
```
  S1  the oracle names a build artifact THAT DOES NOT EXIST
  S4  the gains-identity assertion is ALGEBRAICALLY INCAPABLE OF FAILING
  S5  the ruled per-entity fan-out COLLIDES with the single serving producer
  S6  contract SI is DEFINED; 'max' is DATA-DEFINED -- two quantities, one name
  S8  AC7 requires a CUSTODIAN and there is NO CUSTODIAN SOURCE ANYWHERE
  S9  two tables carry a column named `security_key` AND THEY ARE DIFFERENT KEY SPACES
```
**The trigger is not invented -- it is DESCRIPTIVE of what this fabric already files.**

**EXCLUDES, deliberately:** *"I noticed something interesting elsewhere"* and *"this could be
better."* ⛔ **Both are what turn a worker into a debugger** -- Andrew: *"We are not fucking debugging."*

**GATED: the trigger.** A row can be required to carry both halves (`spec_asserts` / `world_is`).
**SUGGESTED: whether it MATTERS** -- that is CVO's at step 9.
>> **The worker judges FORM. Never SIGNIFICANCE.** <<

---

## FORK 4 · SCOPE CHANGE vs SPEC ERROR

Andrew's split is two-way. **The protocol already carries a third route -- `DECOMP_INVALIDATING`,
which routes BACKWARD into stage 3.** Using it makes the test a lookup instead of an argument.

>> ### **What does the remedy need that does not exist yet?** <<
```
  a cell the decomp ALREADY CONTAINS   -> SPEC ERROR           -> COO -> loop to STEP 6
  a CELL the decomp does not contain   -> DECOMP-INVALIDATING  -> COO -> loop to STEP 5
                                          (the CURRENT round's completion claim is over-scoped)
  an OUTCOME the PRD does not name     -> SCOPE CHANGE         -> CTO -> loop to STEP 2
```
⭐ One axis (what is missing), three grains, three different remedies with three different owners --
Rule 24 (i)-(iv) satisfied. ⭐ **It converts *"is this foundational?"* into *"does the decomp contain
a cell for this?"***
⛔ **AND LIMB 3 IS UNDECIDABLE WITHOUT ANDREW'S ENDPOINT-FIRST PRD.** Without a named desired outcome
there is no way to ask whether the PRD names it. **That is the strongest argument for his step-2
addition, and it is not the argument the transcript makes.**
**GATED:** the remediation row carries `route` and `loop_target` as required fields.

---

## FORK 5 · THE LOOP

>> **The loop-back target is not a separate decision. It IS fork 4's output.** `spec error -> 6` ·
`decomp-invalidating -> 5` · `scope change -> 2`. Round increments to `v(n+1)` on any. <<
**GATED:** remediation is CUT AT ROUND CLOSE ONLY -- already the protocol's rule, and the thing that
stops mid-round debugging.
**SUGGESTED:** the COO drive cadence. 20 minutes is a sane default and should stay a knob.

---

## 1 · THE STRUCTURAL ASKS

- **JSON not markdown.** ⭐ The ROWS are already JSON against real schemas; only the CONTAINER is
  markdown-with-a-fenced-block. Cheap to change; keep the narrative as a `narrative` field.
- **Workers append directly to the investigations file.** Agree -- it is what makes the monitor work
  and it removes MCP thrash.
- **A `/watcher`-style monitor on the investigations JSON.** Buildable now, same shape as the inbox
  Monitor. ⛔ **A NOTIFIER, not a gate.**
- **CTO self-drive scoped to OPEN CALLS ONLY.** ⭐ Today is the argument: a driver that also
  investigates becomes a fifth debugger.

---

## 2 · WHAT THIS DOCUMENT DOES NOT DO

⛔ **Steps 7-10 are DESIGN, not mechanism. Nothing here refuses anything until it is built.** The only
part now GATED is steps 5-6, via `.tools/to-pipeline-gate.py`.
⚠ `comp-heat`'s admissibility and most of the battery's compilation property are UNMEASURED.
⚠ The pure-JSON container change has not been censused against existing readers of the 17 docs.
