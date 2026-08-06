# TRIAL-1 — Suite-gate coverage census, under a MANDATED comp-find / comp-read tool-use trial

**Status:** staged — DO NOT START. No GO has been issued and none is coming until Andrew releases it.

> **WHY THIS BRIEF IS PARKED IN CVO's DELIVERABLES AND NOT IN CloudComp's `task_orders/`.**
> It was written to `org/tier2_senior/0.8.0_AE_CloudComp/task_orders/` and the **owned-paths gate
> refused the commit** — that lane's `task_orders/**` is routed by **ws COO**, and `3.0.0_SA_CVO~B`
> is not a permitted agent there (LD-0119). **The gate is correct and I did not override it.** An
> audited `GIT_COMMIT_AUTHOR_OVERRIDE` would have landed the file, but placing a TO in another
> pod's task_orders is a routing act I do not hold, and taking it would have manufactured the
> placement authority rather than requesting it.
> It is also the more honest location: **this is a prepared brief, not an issued task order.** A
> file sitting in the assignee's `task_orders/` implies an assignment that has not been made.
> **On release: COO (or MSTR) places it in CloudComp's `task_orders/` and issues the GO**, or
> Andrew directs otherwise. The content below is final and needs no rewrite — only a mover.

> ⚠ **THIS TO IS DELIBERATELY UNPAIRED WITH A GO, AND THAT IS NOT A PROTOCOL LAPSE.**
> `org/XXX.md` requires every TO commit to be paired with an MCP GO in the same operational window.
> That pairing is being **intentionally withheld** under Andrew-direct 2026-08-06 ~2115Z, VERBATIM:
> *"THey are in the middle of a task right now so I do not want them to be distracted from that, but
> prepare the brief and I will instruct you on when it is time to issue it."*
> The brief is written and parked. **Andrew holds the issue-timing personally.** If you are reading
> this because you found it on disk: it is not yours to start, and finishing your current work is not
> the trigger — the release is his word, not a capacity signal.

---

## Why this TO exists (read this part; it changes how you should work the task)

**You are the instrument, not the subject.** Two new tools — `comp-find` (graded, paginated repo
search) and `comp-read` (key-context file read) — are built, registered and test-covered, and Andrew
has ratified their end state: **`comp-find` replaces `grep`**, and **`comp-read` becomes HUD colour
surfaced while an agent is looking at files.** Neither is being instituted yet. Andrew-direct,
VERBATIM:

> *"I need to know that it works before instituting on the fabric as a whole, cant just route it if
> its broken or otherwise suboptimal."*

**This task is that evidence.** The rollout of both tools across the fabric turns on what you report.

**Why you and not the author (`3.0.0_SA_CVO~B`):** I built both tools, so my measurements of them are
worthless as acceptance evidence — the P8 contamination rule binds both CVO seats, and **EXPOSURE
disqualifies, not merely authorship** (transitive through XXX.md Step 2). The existing A/B result
(raw grep 0/5, find+read 3/5) is mine, on a corpus I assembled, and Andrew has separately ruled that
the tools **must not be tuned to make those cases pass**. A real task, run by someone who did not
build the tools and whose questions I do not control, is evidence I structurally cannot fit to.

**So the honest finding is the deliverable — including the unflattering one.** A report that comes
back "the tools worked" and nothing else is a FAILED trial, not a passed one: it cannot distinguish
*good* from *unfalsifiable*. Andrew's bar is two-sided — **"broken OR OTHERWISE SUBOPTIMAL"** — so
friction, dead ends, wrong rankings, and every moment you wanted to reach for raw `grep` are
first-class findings with the same standing as the census itself.

---

## The real work: census the 79 test files the commit gate does not run

`.tools/git-hooks/pipescript-suite-check.sh` runs a **14-file allowlist**. Measured 2026-08-06 at
`@9162c6950`:

| measured | value |
|---|---|
| test files in `org/modules/graph/tests/` | **93** |
| files the gate actually runs | **14** |
| **files outside the gate** | **79** |
| tests collected across the whole directory | **980** |
| files that FAIL COLLECTION | **2** (see KNOWN below) |

The gate observes on the *cause* (a staged path that can break the suite) rather than on a clock,
which is the right design — but its allowlist was assembled file-by-file as lanes landed batteries,
never from a predicate over what exists. **Nobody knows what the 79 are.** A test file outside the
gate is not necessarily wrong to be outside it; the defect is that no one can say which.

**Deliverable: a grounded per-file disposition for all 79**, each with the evidence that settles it.

### The four fields per file

1. **ENGINE** — what does this battery actually exercise? A repo-relative path, or `UNRESOLVED`.
2. **STATUS** — `LIVE` (collects and passes) · `RED` (collects, fails) · `BROKEN` (does not collect)
   · `ORPHANED` (its engine no longer exists).
3. **VERDICT** — `ENROLL` (a staged change to its engine should run it) · `LEAVE-OUT` (with the
   reason) · `RETIRE` (the thing it guards is gone).
4. **EVIDENCE** — for ENGINE and VERDICT, the specific line you read that settled it.

> **⛔ FIELD 1 IS WHERE THE TRAP IS, AND IT IS THE WHOLE POINT OF THE TRIAL.**
> **A test file's NAME IS A CLAIM ABOUT ITS ENGINE, AND THE CLAIM IS SOMETIMES FALSE.** Deriving
> ENGINE from the filename is exactly the right-file-wrong-conclusion failure `comp-read` was built
> to stop — so **ENGINE must come from what the file IMPORTS AND CALLS, never from what it is
> called.** If the tools help you here, that is the strongest possible result for them; if they do
> not, that is the finding that stops the rollout, and it is worth more than a clean report.
>
> **THIS IS GROUNDED, NOT RHETORICAL — I checked before asserting it.** Proof of existence, one
> specimen so you know the trap is real: **`test_boundary_report_conformance.py` loads `residue`.**
> Nothing in its name says so.
>
> **I am deliberately NOT giving you the count or the list, and you should not ask me for them.** My
> check was a crude regex over import forms; it produced a candidate set I know contains false
> positives (module aliases like `..._under_test` trip it), so **any number I quoted would be a
> guess wearing a measurement's clothing** — and it would anchor your census to my bad scan instead
> of your good one. Deriving the real set is the task. If your count and my impression disagree,
> **yours is the measurement and mine was never one.**

### KNOWN GOING IN — you get no credit for rediscovering these

Disclosed so the trial measures new ground, not a rigged find. Both are real, both are already owned:

- `test_adapter_audit.py` — **BROKEN**, its target `org/modules/graph/adapter_audit_cli.py` does not
  exist. Already routed to CTO.
- `test_surface_check_negative_control.py` — **BROKEN/ORPHANED**, asserts `.tools/comp-surface-check`
  is a file; that binary was retired 2026-08-06 by Andrew-direct. **This is my own residue from
  executing that retirement and I own it** — recorded here rather than left for you to find, because
  a trial seeded with the author's known bugs measures nothing.

Both are pre-existing collection failures, so **`pytest` on the whole directory exits non-zero before
you touch anything.** That is the starting state, not something you caused.

---

## THE MANDATE (the trial condition)

**`comp-find` and `comp-read` are your PRIMARY instruments for this task.** Reach for them first,
every time, for every search and every file inspection.

- **`comp-find`** for every search — content or filename. Not `grep`, not `Grep`, not `Glob`.
- **`comp-read <file> --for "<your actual question>"`** before concluding anything about a file's
  contents. Its `--for` takes a plain-English question; ask the question you actually have.

**Raw search is NOT forbidden — it is INSTRUMENTED.** If a comp-tool cannot get you there, use
whatever works and **log the fallback**: what you asked, what it returned, why it was insufficient,
what you used instead. **A logged fallback is a SUCCESSFUL trial outcome, not a failure to comply.**
An agent who forces the tools past the point of usefulness in order to look compliant destroys the
only measurement Andrew asked for.

**Scope bound:** this mandate covers **this task, for you, once.** It is not a fabric-wide tool
mandate and creates no precedent — the fabric-wide question is precisely what the trial decides.

---

## Reporting back (the second, co-equal deliverable)

A `TOOL TRIAL` section in your session log:

1. **CONTAMINATION DECLARATION (required; the report is UNVALIDATED without it).** State what you had
   already read about `comp-find` / `comp-read` before starting, or `NONE`. Exposure, not authorship,
   is the disqualifier — a declaration of NONE is expected and is not a claim of ignorance.
2. **Counts:** `comp-find` invocations · `comp-read` invocations · **raw-search fallbacks**.
3. **THE FALLBACK LOG** — one row per fallback: question asked → what the tool returned → why it was
   insufficient → what you used instead. **This is the highest-value output of the entire trial.**
4. **WHERE `comp-read` EARNED ITS KEEP, AND WHERE IT DID NOT.** Specifically: did the `QUALIFIERS`
   panel or the `UNREAD LEDGER` ever change a conclusion you would otherwise have drawn? Name the
   file and the line. **A "no" here is a real and publishable answer** — it is the difference between
   a tool that helps and one that merely runs.
5. **THE HUD QUESTION, answered from experience rather than opinion.** You are using `comp-read`
   manually; the ratified end state is it appearing automatically as colour on files you are already
   looking at. **Would that have helped you here, or would it have been noise?** You are the only
   person who can answer this, and your answer gates the wiring.
6. **VERDICT: would you keep using these if the mandate were lifted?** Yes/no + one sentence.
   Answer it as yourself. A polite yes is worth nothing to anybody.

---

## Acceptance criteria (machine-checkable)

1. **All 79 files carry all four fields.** `79` rows, no blanks — `UNRESOLVED` / `UNKNOWN` are valid
   values and MUST be used where true. *(Third state: **UNRESOLVED ≠ LEAVE-OUT.** A file whose engine
   you could not determine is an open question, never a silent exclusion. Recording an honest
   `UNRESOLVED` scores strictly higher than a guessed engine.)*
2. **Every `LIVE` verdict is exercised, not asserted:** `python -m pytest <file> -q` collects and
   passes. Every `BROKEN` names the exact import or path that fails.
   *(Easiest-pass check: the cheap way to pass criterion 1 is to mark everything `UNRESOLVED`. This
   criterion is what forbids it — an `UNRESOLVED` file must still carry its STATUS, exercised.)*
3. **Every `ENROLL` names the engine path that should trigger it**, so the recommendation is
   actionable as a `WATCH_EXACT` line without further research.
4. **The ENGINE field is derived from imports/calls, never from the filename.** For any file where
   name and engine disagree, the report says so explicitly. *(Forbidden shortcut, named so it cannot
   be taken by accident: **do not populate ENGINE by pattern-matching `test_<x>.py` → `<x>.py`.** That
   route re-commits the exact defect this trial is measuring.)*
5. **The fallback log is present.** Zero fallbacks is a legitimate result **only if the counts in (2)
   support it**; an empty log beside a high invocation count reads as unrecorded, not as frictionless.
6. **The contamination declaration is present.**

**Explicitly NOT in scope:** do not edit the gate, do not enroll anything, do not fix the two known
BROKEN files. **This TO produces a recommendation, not a change.** Whether to widen the gate is the
gate owner's scoping call, and manufacturing that decision from a census would be exactly the
inferred-gate pattern the fabric prohibits.

---

## Compiler tools mandate (three-phase)

**Phase 1 — before starting**
- `comp-find --name 'test_*.py' org/modules/graph/tests` — **expect 93 files.** If the count differs,
  the tree moved under this brief: re-derive the denominator and say so in the report rather than
  carrying this number forward.
- `comp-read .tools/git-hooks/pipescript-suite-check.sh --for "which test files does this gate run"`
  — expect the `WATCH_GLOBS` + `WATCH_EXACT` blocks. *If this call does not surface those two blocks,
  that is a FINDING and the single most important one in the trial: it is the exact question the tool
  exists to answer, on a file where the answer sits ~80 lines from prose that looks like it answers it.*

**Phase 2 — during**
- `comp-read <test file> --for "what module does this test exercise"` per file. Where the answer is
  ambiguous, say so — an honest `UNRESOLVED` beats a confident wrong engine.

**Phase 3 — before reporting**
- `python -m pytest <file> -q` for each `LIVE` claim (criterion 2). rc and the pass count go in the row.
- Results in the session log's **Compiler Tools** table per `org/standards/TO_COMPILER_GATE.md`.

## Cross-domain coordination

`<none/>` — read-only over `org/modules/graph/tests/`. No shared file or S3 key. **If you find
yourself editing anything outside your own session log and the census document, stop: this TO has no
write scope in the tree.**

## Deliverables

- **Document:** the 79-row census, in your `deliverables/`.
- **Document:** session log with the `TOOL TRIAL` section (all six items) + Compiler Tools table.
- **No commits to `.tools/`, the gate, or the tests.**

## Do not

- Do not treat your current task's completion as the trigger to start this. **Andrew releases it.**
- Do not derive a test's engine from its filename (criterion 4).
- Do not suppress an unflattering tool result. The trial's value is entirely in its honesty, and a
  favourable report from the tools' own beneficiary is worth nothing to the decision it feeds.
- Do not widen the mandate past this task, and do not enroll, fix, or edit anything.

---

**Issued by:** `3.0.0_SA_CVO~B` · **Issued to:** `0.8.0_AE_CloudComp` · **Date:** 2026-08-06
**Project:** NFRA_SCRIPTGEN (Part B acceptance) · **Status:** `staged`, GO withheld by Andrew
**Grounding:** counts measured at `@9162c6950`; tools at `@c2b6e828d` / `@fb67da754`
