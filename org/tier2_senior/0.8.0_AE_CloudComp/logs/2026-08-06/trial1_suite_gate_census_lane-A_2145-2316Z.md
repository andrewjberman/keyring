# TRIAL-1 — suite-gate coverage census under a mandated comp-find / comp-read trial

**archetype:** VALIDATE

**Agent:** `0.8.0_AE_CloudComp~A` · **Window:** 2026-08-06 ~2145Z–2316Z · **Project:** NFRA_SCRIPTGEN (Part B acceptance)

---

## Andrew-direct instruction (RECORDED VERBATIM — org/XXX.md record+broadcast law)

**Channel:** direct, at my terminal. **Time:** 2026-08-06 ~2145Z. **VERBATIM:**

> "This is your task : @07d5e7927 — org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_SCRIPTGEN.TRIAL-1.BRIEF-PARKED.suite-gate-census-mandated-tooluse.md"

This RELEASED the TRIAL-1 brief (`3.0.0_SA_CVO~B`, `@07d5e79278`), which had been parked at `staged`
with its GO deliberately withheld under his earlier ~2115Z word (*"prepare the brief and I will
instruct you on when it is time to issue it"*). He held the issue-timing personally and issued it
personally.

**BROADCAST same turn** to `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` (MSTR under the XXX.md
record+broadcast clause specifically, which names all three — not as a routine worker→MSTR message,
which LD-0116 otherwise forbids). Delivery receipts: `20260806T224750Z`, `20260806T224803Z`,
`20260806T224824Z`.

**Scope surfaced, NOT adjudicated:** the brief's `<issued_to>` reads the BASE serial
`0.8.0_AE_CloudComp`; Andrew directed it to the `~A` lane at my terminal. Executed as `~A` on his
word (XXX.md Step 1 precedence #1). Base seat is separately live (PID 21840). Flagged to COO as the
routing owner; I did not hold on the ambiguity.

---

## Deliverable

`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_SCRIPTGEN.TRIAL-1_suite-gate-census-79_20260806.md`

**Denominator re-derived, not carried forward:** 93 test files / 14 gate-run / **79 outside** —
matches the brief exactly. All 14 confirmed present in the 93. `WATCH_GLOBS` = 10 literals +
`test_pipescript_*.py` → 4.

| STATUS | n | | VERDICT | n |
|---|---|---|---|---|
| LIVE | 61 | | ENROLL | 61 |
| RED | 15 | | LEAVE-OUT | 16 |
| BROKEN | 1 | | RETIRE | 2 |
| ORPHANED | 2 | | | |
| **UNRESOLVED engines** | **0** | | | |

All 79 carry all four fields, every `LIVE` exercised (`python -m pytest <file> -q`, rc + counts in
the row), every engine derived from an **import or a call**.

**Findings:** F1 `test_comp_system_metrics.py` is not a pytest file at all — 0 test defs, own
`check()` at `:31`, `__main__` at `:169`, rc=5, **1 of 93** (isolated, I checked the whole tree).
F2 the brief's disclosed specimen is **REFUTED** — `test_boundary_report_conformance.py` imports
`boundary_report` at `:23`; the sole `residue` hit is `:29` `"tool": "comp-residue"`, a fixture
string. F3 real mismatch specimens found instead (`test_blast_discrimination.py` → `compproof/
tool_probe.py`, comp-blast stubbed by an injected lambda; 6 batteries share that engine).
F4 my own two false positives, caught before publication (below).

**Gate cost handed to the owner, decision NOT made:** enrolling all 61 = **562.9s (9.4 min)** if one
commit touched every engine; 4 batteries carry ~7 min of it. I did not recommend a tier split,
timeout, or subset — widening the gate is the owner's scoping call.

---

## TOOL TRIAL

### 1. CONTAMINATION DECLARATION — **NOT `NONE`**

Before starting I had read: **(a)** two `MEMORY.md` index lines — *"comp-read=HUD color, comp-find
REPLACES grep, trial-gated"* and *"NO overfitting a scorer to its own eval cases — comp-read stays
3/5"*; **(b)** the commit subject of `07d5e79278`; **(c)** the TRIAL-1 brief in full, during startup
orientation, before the GO.

**The material exposure is (a) + (c): I knew the expected A/B result (raw grep 0/5, find+read 3/5)
and both disclosed BROKEN files before I ran anything.** I had NOT read either tool's source, its
PRD, its test files, or any prior trial output. I did not tune anything and could not have — the
brief is read-only over the tests and I hold no write route to `.tools/`.

### 2. Counts

| instrument | invocations |
|---|---|
| `comp-find` | **7** |
| `comp-read` | **7** (+1 `--help`) |
| **raw-search fallbacks** | **9** |

### 3. THE FALLBACK LOG

| # | question I asked | what the tool returned | why insufficient | what I used instead |
|---|---|---|---|---|
| 1 | verbatim contents of the gate's `WATCH_EXACT` block | `comp-read --at 70` PINNED the section (`score=999`) and printed its QUALIFIERS — **but rendered no excerpt of the pinned lines** | I needed the 21 literal filenames, not a pointer to them. `--help` says *"Excerpts are VERBATIM"*, and `--at` produced none | `Read` lines 60–129 |
| 2 | what module does `test_boundary_report_conformance.py` exercise | 35 `def`/`class` sections, **zero import lines** | the answer is at `:23`; comp-read's python-ast SHAPE starts at the first `def` (`:26`), so the import block is **not a section and cannot surface** | `Read` lines 1–26 |
| 3 | same, rephrased *"what does this file import"* | same sections, ranked differently | rephrasing cannot reach a region the sectioner never emits | — |
| 4 | same, `--at 1` | pinned nothing (no section covers line 1) | structural, not a phrasing problem | — |
| 5 | what executable does `test_blast_discrimination.py` invoke | 9 `def` sections, no engine | the engine is an `os.path.join` at `:21` inside the import preamble | `Read` lines 1–36 |
| 6 | engines of 4 then 6 unresolved files | n/a — did not attempt after 2–5 | pattern established: imports/calls are outside comp-read's section model | `grep -nE "^(import\|from)\|spec_from\|_CLI"` |
| 7 | the literal filename passed to each `_load(name, filename)` helper | n/a | needs call-site argument extraction; no tool offers it | `grep -nE "_load\(\|import_module"` |
| 8 | **ENGINE for all 79, criterion-4 compliant** | n/a — ruled out by 2–6 | criterion 4 forbids the filename shortcut and comp-read cannot read imports, so neither the tool nor the shortcut was available | **purpose-built AST extractor**, 6 channels (import / path-literal / `os.path.join` / `pathlib`-div / bare-`.py`-literal / `import_module`), 3 positive controls, 79/79 resolved |
| 9 | how many of the 93 have zero pytest test defs | n/a | a count over a per-file predicate; `comp-find` returns hits, not per-file aggregates | `grep -cE` loop over all 93 |

**Fallback 8 is the load-bearing one.** The brief calls Field 1 *"where the trap is, and the whole
point of the trial."* `comp-read` could not answer it on a single file, so it could not answer it 79
times. **That is the finding, and it is adverse.**

### 4. WHERE `comp-read` EARNED ITS KEEP, AND WHERE IT DID NOT

**EARNED — one clear, nameable case.** `test_comp_system_metrics.py`, asked *"why does this file
collect zero tests"*:
- **SALIENT returned an honest measured zero** — *"NO region matched the question. That is a MEASURED
  zero over 1 section(s) — the file may still contain the answer under different words. Do not read
  this as 'the file does not say'."* It refused to manufacture a match. That is the single best
  behaviour I saw from either tool.
- **QUALIFIERS then handed me the mechanism**: line 58, *"NOT a bare `assert`: this module body runs
  at IMPORT…"*, plus the `check()` def at `:31`. **That changed a conclusion**: without it I would
  have read all 170 lines to work out why pytest collected nothing.

**EARNED, with a caveat that matters.** On the gate, the SHAPE panel surfaced `WATCH_EXACT` (66–86)
and `WATCH_GLOBS` (87–123) immediately — the brief's designated most-important test, **passed**. But
**SALIENT ranked `WATCH_EXACT` 5th of 6 at `score=0.53`**, below three less relevant blocks, for a
question that is literally *"which test files does this gate run."* **The unranked, complete SHAPE
panel answered; the ranking did not.** The panel the tool leads with is the one that got it wrong.

**DID NOT.** The **UNREAD LEDGER never changed a conclusion** for me — not once across 7 invocations.
I never returned for a section on its prompting. It is an honest disclosure of what was withheld, and
I read it as reassurance rather than as a pointer. **On the gate's QUALIFIERS, line 86 (*"is RETIRED
(guard deleted @f9ddda52f), not enrolled"*) was genuinely relevant context but changed nothing** — I
already had the enrolled list verbatim from fallback 1.

### 5. THE HUD QUESTION — would automatic comp-read colour have helped here?

**Mostly noise for this task, with one exception, and one active hazard.**

- **The hazard, and it is the important part:** my most frequent file question by far was *what does
  this depend on* — and that is exactly what comp-read structurally cannot show. Auto-surfacing it
  would have put a confident, well-formatted panel next to every file I opened that **consistently
  omitted the answer I needed**. A panel that looks like it answered is the right-file-wrong-conclusion
  failure the tool was built to prevent, pointed at itself. On a 73-line file where I needed lines
  1–36, it is strictly worse than reading the file.
- **The exception:** on a large unfamiliar file (the 212-line gate, the 272-line conformance suite)
  SHAPE is a real map and QUALIFIERS is the highest-value panel in the tool.
- **If it is wired, wire it conditionally:** QUALIFIERS on by default; SHAPE above ~150 lines;
  SALIENT off or last. And **fix the import blind spot before the HUD ships**, or the HUD will teach
  agents that a file's dependencies are whatever the panel showed.

### 6. VERDICT — would I keep using these if the mandate were lifted?

- **`comp-find`: YES, unreservedly.** The `DENOMINATOR` line is the feature — it gave me a count I
  could trust in one call, and the BANDS classification is what let me refute F2 in a **single
  invocation** by separating a fixture-string hit (`[TEST]`) from a real source hit (`[SURFACED]`).
  A raw grep would have returned the same line and left the interpretation to me.
- **`comp-read`: PARTIALLY — not as a default reach.** I would open it on a large unfamiliar file for
  QUALIFIERS and SHAPE. I would **not** reach for it to answer *"what does this file depend on"*,
  which is my most common question about a file, because it cannot answer it. Today it is a
  **skimming aid, not a dependency instrument** — and the brief framed it as the latter.

---

## F4 — I reproduced the author's own error class twice, and caught both (method note)

Recorded because the trial is about honest measurement, and my first two numbers were not.

1. My first name-vs-engine metric reported **62 of 79 mismatches** (60 after a later fix). It was a
   crude bidirectional substring test. **Junk — discarded, never published as a finding.** Replaced
   with the precise question criterion 4 actually asks, which yields: shortcut lands on the real
   engine **10**, on a real-but-wrong file **0**, on **nothing at all 69 (87%)**.
2. My extractor mis-resolved `test_comp_keys.py` to `__init__.py` because it read only `node.module`
   on an `ImportFrom` and ignored the imported name. That single artifact **would have been published
   as "1 actively-misleading file."** Fixed; the true count of actively-misleading names is **0**.

Both were caught by opening one member of the set before publishing its count — the same discipline
that falsified F2. **A count is not a measurement until you have looked at one of its members.**

A third, in my own rendering: the two RETIRE rows initially displayed an incidental fixture path
(`safe-commit.sh:212`) as the ENGINE, because I ranked engine references by list order rather than by
line. The verdicts were right and the evidence cells were misleading — the exact defect this trial
measures, in the census about it. Fixed by ranking on line number; both rows now cross-validate
against their pytest error text (`:23` FileNotFoundError, `:40` AssertionError).

---

## Compiler Tools

| tool | invocation | result | verdict |
|---|---|---|---|
| `comp-find` | `--name 'test_*.py' org/modules/graph/tests` | `DENOMINATOR: 93` | **PASS** — matched the brief; denominator in one call |
| `comp-find` | `--name 'test_pipescript_*.py' … --all` | 4 hits | **PASS** — resolved the gate's only glob |
| `comp-find` | `--name 'test_*.py' … --all` (×3) | full 93 list | **PASS** |
| `comp-find` | `residue <test file>` | 1 hit, band `[TEST]`, `:29` fixture string | **PASS** — the band is what refuted F2 |
| `comp-find` | `residue boundary_report.py` | 3 hits, band `[SURFACED]`, all comments | **PASS** |
| `comp-read` | gate `--for "which test files does this gate run"` | SHAPE surfaced `WATCH_EXACT`+`WATCH_GLOBS` | **PASS w/ CONCERN** — SHAPE answered; SALIENT ranked the right block 5th of 6 |
| `comp-read` | gate `--at 70` | pinned, **no excerpt** | **CONCERN** — fallback 1 |
| `comp-read` | 3× on `test_boundary_report_conformance.py` | zero import lines, 3 phrasings | **FAIL** — cannot answer the ENGINE question |
| `comp-read` | `test_blast_discrimination.py` | zero engine refs | **FAIL** — same class |
| `comp-read` | `test_comp_system_metrics.py --for "why … zero tests"` | honest measured-zero SALIENT + QUALIFIERS `:58` | **PASS** — the one conclusion-changing call |
| `python -m pytest <file> -q` | ×79 + 3 re-checks | 61 rc=0 · 15 rc=1 · 2 rc=2 · 1 rc=5 | criterion-2 exercise for every row |
| AST extractor (scratchpad) | 6 channels, 79 files | 79/79 resolved, 0 UNRESOLVED, 3 positive controls | the criterion-4 instrument comp-read could not be |

**Gap found (routed, not fixed):** `comp-read`'s python-ast sectioner emits only `def`/`class`
regions, so a Python file's import/preamble block — lines 1 to the first `def` — is unreachable by
`--for`, `--at`, or any phrasing. On this corpus that is where the engine lives in every single file.

---

## Scope discipline

No edit to the gate, the tests, or `.tools/`. Nothing enrolled, nothing fixed, no gate-widening
decision made. Writes this session: this log + the census deliverable. Analysis scripts live in the
session scratchpad, outside the tree.

## RAVC-4 AMENDMENT (2026-08-06 ~2323Z) — issuer validated, ACCEPTED IN FULL

`3.0.0_SA_CVO~B` validated as issuer, re-deriving the load-bearing claims independently rather than
accepting them. **Accepted in full, nothing returned for rework.** Two amendments belong in the
record because they change the GROUNDING of this trial's central finding, not merely its reception.

### A1 — the comp-read finding is now SOURCE-CONFIRMED, and it was mine to qualify

Above, I wrote that comp-read *"structurally cannot"* reach the import block. **That was an inference
from behaviour.** I exercised three phrasings plus `--at 1` and saw zero import lines — which
establishes the **symptom**, not the **mechanism**. Under Rule 22 that was an EXERCISED-behavioural
claim, and "structurally" leaned harder than my evidence carried.

The issuer has now named the mechanism at source, and both defects reproduce on their side:

- **Defect A — import block unreachable.** `_scan_tree` collects spans only for `FunctionDef` /
  `AsyncFunctionDef` / `ClassDef`. Module-level imports therefore sit in **no section at all**: they
  cannot be ranked by SALIENT, cannot be pinned by `--at`, and no rephrasing reaches them. On this
  specimen SHAPE's first section starts at `:26`; the `import boundary_report as B` at `:23` is
  outside every span.
- **Defect B — pinned-but-no-excerpt.** The excerpt loop emits only lines with query-token overlap,
  and a pinned section is by definition the case where overlap is **zero** — so the pin succeeds and
  then renders empty, precisely when the user has told the tool where to look.

**Status upgrade: EXERCISED → SOURCE-CONFIRMED.** Both defects are the author's to fix; neither is
fixed, and they are deliberately held pending Andrew's read. **Nothing in my verdict changes** — the
mechanism confirms the behaviour I measured.

### A2 — a second instance of F1's failure mode, found by the author in their own battery

Recorded here with attribution rather than left in an inbox message, because it belongs beside F1.

`test_at_line_pins_the_containing_section_into_the_ranking` (authored the day before this trial)
asserts that the section header renders and that the `PINNED` disclosure renders. **It never asserts
that an excerpt renders.** So it passes **green against defect B** — the exact defect it covers.

**This is F1's failure mode arriving from the opposite direction.** F1 (`test_comp_system_metrics.py`)
collects **nothing**, so it cannot redden. This one collects and passes, but **asserts around** the
defect, so it also cannot redden. Two mechanisms, one failure mode — *a battery that cannot fail on
the thing it covers* — found in a single session on a single toolchain. Neither would be caught by
"does the suite pass?", which is the question the gate this census is about actually asks.

**Attribution:** found and disclosed unprompted by `3.0.0_SA_CVO~B`, the author of both the tool and
the test.

### A3 — F2, confirmed by the author at source

`test_boundary_report_conformance.py:23` is `import boundary_report as B`; the sole `residue` hit is
`:29` fixture data. Cause identified: an alternation `"(?:comp-|\.tools/)([\w-]+)"` scraped a fixture
string. The author's own note on the aggravating factor — that the brief disclosed the instrument's
unreliability and then exempted one output of it from that unreliability, unopened, because a
specimen was needed — is theirs and I am not restating it as mine.

**Ownership after validation:** F1 needs an owner and it is neither of us. Defects A and B are the
author's. The 61-battery enrollment map and its 9.4-min cost remain the gate owner's scoping call.

## POST-TRIAL VERIFICATION AMENDMENT (2026-08-07 ~0015Z) — the tool moved after the measurement

**The trial deliverables above are NOT rewritten and must not be.** They measure `comp-read` at
`@c2b6e828d`/`@fb67da754`. The tool has since changed. Two dated states, both legible, is the record;
a trial report edited to match a tool that moved after the measurement is no longer a measurement.
*(Issuer concurs: "Correct, and do not.")*

### V1 — a position changed under an agent who was acting on it

At ~2323Z the issuer wrote *"neither is fixed yet, and I am not fixing them ahead of Andrew's read."*
At **2333Z** they landed `@1e9d2e59d2` fixing both, and sent no notice. Andrew then instructed me to
carry the blind-spot finding to them; I checked the tool before writing and found it already fixed.
**I nearly sent a finding about a tool state that no longer existed.**

Their reasoning for changing position (Andrew's hold is on ROLLOUT; refusing to fix their own tool
would manufacture a gate on their own work) is sound and I do not dispute it. The issuer names the
failure precisely and owns it: **a change of position is not complete until the people acting on the
old one are told.** Recorded here as a fabric-level lesson, not as a grievance — the cost was one
re-run, and the only reason it was not a false report is that I checked the artifact before writing
about it (Rule 22a: never trust a producer's self-report *or its absence*).

### V2 — what the fix actually closed, measured

Same corpus, 93 files / 17,300 lines.

| | in NO section | share |
|---|---|---|
| pre-fix (my AST model of `_scan_tree`, issuer source-confirmed) | 7,159 lines | **41.4%** |
| post-fix `@1e9d2e59d2` (parsed from the tool's own SHAPE output) | 1,189 lines | **6.9%** |

**Recovered: 5,970 lines.** Pre-fix, **93 of 93** files had at least one unreachable module-level
import; 28 had >50% of the file dark; worst 95.3%.

**Caveat, unlaundered: the two figures come from two different instruments** — mine modeled the
sectioner, the post figure reads the tool's real output. The comparison rests on the issuer's source
confirmation that `_scan_tree` collected exactly `FunctionDef`/`AsyncFunctionDef`/`ClassDef`.

**The reframe was the load-bearing part.** It was never an *import* blind spot — it was a
**module-level code** blind spot, imports being one resident. A fix scoped to the narrow framing would
have closed ~6 lines per file, left ~40% dark, and been declared complete.

### V3 — defects verified against the live binary, not the self-report

- **Defect B (pin renders nothing): CLOSED.** `--at 70` on the gate now renders `WATCH_EXACT` verbatim.
- **R2 (pin renders the wrong lines): CLOSED `@31a646c4c`**, verified on my exact original call —
  `--at 23` now emits `AUTHORITATIVE 23: import boundary_report as B  # noqa: E402`.
- **R1 (engine-phrased question does not surface the import): NOT a ranking defect — REPRODUCED and
  RE-DIAGNOSED.** The issuer built an IDF-weighting fix on a principled hypothesis, **measured it,
  found it did not fix the case, and discarded it — nothing landed.** The real cause is **zero lexical
  overlap**, which I re-derived independently rather than accepting: tokenising lines 1–25 and
  checking each query token of *"what module does this test exercise"* — `what`/`module`/`does`/
  `this`/`test`/`exercise` — **all six are absent** from the header's token set. The answering text is
  `import boundary_report as B`. **No term-weighting scheme can rank a section with no matching
  terms; the score is 0 by construction.**

**So R1 is not fixable within the tool's ruled constraints** — bridging question-vocabulary to
answer-vocabulary is semantic matching, and the millisecond budget rules out embeddings. That is a
different and more useful statement than "not fixed."

### V4 — the HUD conclusion REVERSES, and I am recording it because honesty is symmetric

My §TOOL TRIAL item 5 said: do not wire the HUD until the import blind spot is fixed, because a panel
that consistently omits the answer is worse than none. After V3 I narrowed that to: the *ranking*
still misses on engine-shaped phrasing. **Both were reasoning from the `--for` path. The HUD does not
use it.**

Measured: `comp-read <file>` with **no** `--for` prints `SALIENT: (no --for question given; pass one
to rank regions)`. **SALIENT does not render at all.** The surviving panels — SHAPE, QUALIFIERS,
CONTRADICTIONS, UNREAD LEDGER — are **query-independent**, and are precisely the two I independently
rated as the tool's real value.

**And bare SHAPE on the F1 file prints `39-170 module __main__ entry -- module-level execution`** —
it states the file is a script, with no question asked. **The HUD condition would have handed me F1
directly**, which I found by counting test definitions by hand.

**Stronger than I first wrote it (issuer's correction, re-verified by me on the query-less call):
the bare form yields BOTH halves of F1.** SHAPE gives the structural tell above, and the
query-independent QUALIFIERS panel separately surfaces `:58` *"this module body runs at IMPORT, so a
module-level assertion that fails…"* — the exact mechanism that saved me reading 170 lines — plus
`:63-64`, the `check(...)` calls that are the file's real assertions. **Neither half needs a
question.** I understated this in the first pass and am correcting it in the direction that favours
the tool, for the same reason I published the adverse findings.

**Therefore R1 does not bear on the HUD at all, and my objection to wiring it is withdrawn.** It
bears on manual `--for` use, where the mitigation is that the user can rephrase — and I did: *"what
does this file import"* ranks the header #1 at score 1.46.

⚠ **The one open unknown, stated rather than papered over: this assumes the HUD renders the
no-query form.** If it instead auto-generates a question from agent context, **R1 returns in full**,
because a generated question is exactly the case where the user cannot rephrase. **That is an
unmade design decision, and it is the decision that determines whether R1 matters.** It is not mine
to make and I am not making it.

**Net for the rollout call:** the question is no longer *"is comp-read broken"* but *"is a
phrasing-dependent ranked panel worth surfacing by default"* — and if the HUD ships query-less, that
question does not arise, because the ranked panel is not what ships.

### V5 — THREE retrieval-layer deceptions in one trial, one of them mine

Recorded because CLAUDE.md's *"put the control on the RETRIEVAL, not the pattern"* earned three
separate instances inside a single ~3h task, and the third nearly inverted a verdict.

| # | who | the retrieval | what it produced |
|---|---|---|---|
| 1 | me | `pytest … \| tail -15; echo "rc=$?"` | **`rc=0` — `tail`'s rc, not pytest's.** The file actually exits **5**. Read as a clean pass on the one file in 93 that runs zero tests. Caught by re-running unpiped. |
| 2 | issuer | `… \| head -8` over the QUALIFIERS panel | cut the panel at `:11`, hiding `:58`. **One keystroke from reporting my TRUE correction as UNREPRODUCED** — a false refutation manufactured entirely by their own retrieval, on the claim they had just said they were checking hardest. Caught by arithmetic: 16 qualifiers declared, 12 shown, 6 visible. |
| 3 | me | comp-read `--for` returning zero import lines | **true output, but I generalised "structurally cannot" from it** — a mechanism claim from a behavioural retrieval. Corrected in V3 only because the issuer named `_scan_tree` at source. |

**The generalisation, and it is the pairing that makes it useful:** #1 and #2 are the same shape from
opposite directions — a pipe stage silently changed what we reasoned from, and in **both** cases the
corrupted result was *plausible*. **The tell was never the content; it was arithmetic that did not
add up.** Neither of us noticed by reading harder.

**And this sits directly beside the producer-silence point as its mirror:**
- **SILENCE** deceived me about a state that **HAD** changed (the tool moved; nobody said).
- **TRUNCATION** nearly deceived the issuer about a state that had **NOT** changed (the panel was
  right; the pipe hid it).

**Both are the shape of the instrument, not of the subject.** *(Mirror framing: issuer's.)*

**Bounded form of the producer half, adopted by both of us:** not *"consumers should re-check"* —
unbounded, and it would have every agent re-verifying every tool before every use — but
**"a producer who changes a state someone is acting on owes them notice,"** which puts the duty on
the party already holding the information, at no cost.

### V6 — the issuer's correction to my closing framing, which I am adopting

I closed by crediting their conduct — disclosing residue, inviting refutation, discarding a fix that
failed. They declined the framing, and their version is better for the record: **every one of those
was a control catching them, not a virtue.** The refutation was mine; the battery hole surfaced only
because I found the defect it missed; the IDF fix died on a measurement they nearly did not run; the
truncation above was caught by luck plus arithmetic.

**What this trial demonstrates is that the CONTROLS worked** — and the load-bearing ones were held by
the party who did not build the tool. That is the transferable finding, and it is the argument for
why acceptance evidence must come from a non-author. Not "CVO~B was rigorous," but **"an author
cannot hold their own controls, and this trial is 79 rows of evidence for that."**

## Blockers

None. Both deliverables complete; RAVC closed by the issuer.

## Next

Awaiting Andrew's read. The rollout decision on `comp-find` / `comp-read` is his; my input is
§TOOL TRIAL items 5 and 6. Two items sit with the gate owner (not me): the 61-battery enrollment map
with its 9.4-min cost, and F1.
