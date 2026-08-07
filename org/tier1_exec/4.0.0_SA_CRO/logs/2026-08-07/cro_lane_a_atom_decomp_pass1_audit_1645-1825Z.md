# 4.0.0_SA_CRO~A — ATOM_DECOMP corpus audit, PASS 1: the briefed denominator was wrong, and the corpus has never been run (2026-08-07 16:45Z -> 18:25Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** EXPLORE, VALIDATE

## Window

16:45Z -> 18:25Z. **First session of this lane** — spawned Andrew-direct as a dedicated seat through
the GPT-authored `projects/ATOM_DECOMP/` corpus. No prior log.

## Startup

`/watcher` + `org/XXX.md` clean. Registered `4.0.0_SA_CRO~A` (PID 8712), Monitor armed
(task `b7dgkbc35`, `/cygdrive/c` prefix resolved not hardcoded) and **ACK-proven end-to-end** —
base-CRO's coordination message arrived through it minutes later, which is the only sound
reachability oracle. Zero crons (LD-0157/0175). A.3: 96 of 97 comp-tools resolve bare, forwarder
EXERCISED (produced its own banner, not merely `command -v`).

**One startup finding worth carrying:** the `~A` lane inbox `org/mcp/inbox/4.0.0_SA_CRO/~A/` **did not
exist** and I created it (nested form; sibling `~SWEEP` confirms the convention). Also note the
`CRO_WORKSPACE` path rule is `org/tier1_exec/4.0.0_SA_CRO/**` — the **base** folder — so this lane's
log and deliverable go there. A flat `4.0.0_SA_CRO~A/` agent folder would have matched **no path rule**
and been refused; the two-families table in XXX.md is what prevented that.

## What happened

**1. The denominator I was handed was wrong, and I measured it before reading anything else.**
Briefed as an "89-file corpus" by my own launcher. Measured: **68 GPT-authored** (import
@`66d83132d5`) **+ 4 CRO-authored = 72 tracked**, 73 on disk, **zero deletions in history** — and
**72 at the grant commit @`2a3b1ea408` itself**, so the digit was **wrong when written, not drifted**.
It is live in `.owned-paths.yaml:425`. I could source it to **no** candidate denominator I measured
and **filed no mechanism for its origin**, having no grounding for one.

The relay ran CTO's grant commit → lane description → MSTR broadcast → base's briefing → my launcher:
**four hops, zero measurements, authority gained at each.** Base re-derived all five figures (5/5
exact), **named itself as a hop**, and routed the text fix to CTO. The grant itself is sound.
Had I adopted 89 as my coverage denominator, *"audited N of 89"* would have reported a **21-file gap
that does not exist** — a 31% overstatement of my own subject.

**2. Independently derived the provenance split before base's brief arrived**, and it matched theirs
exactly (68 GPT + `04`/`05`/`06`/`07` mine-today). Two independent derivations agreeing is the only
reason that split is load-bearing rather than asserted.

**3. Audited 20 of 72 files in full and filed 12 findings** — report
`deliverables/ATOM_DECOMP_CORPUS_AUDIT_PASS1_20260807.md` @`0e1d847aa4`, pinned @`bdac197ce3` /
corpus @`f9d1d2e73f`, **written outside `projects/ATOM_DECOMP/`** so a reversal of base's inferred
proceed-authorization orphans it cleanly (CVO~C precedent @`8170937b60`).

Severe, all in the GPT-authored subject:
- **F-1** the shipped **charter template is invalid YAML** — Layer A's sole output (`00:38`), and
  `02:15` specifies an engine that must *accept* one. The single artifact built to be parsed cannot be.
- **F-2** **two normative rule-lists that disagree** — `00:46-56` 8 "non-negotiable laws" vs
  `SKILL.md:10-21` 9 "Rules", neither containing the other. **Laws 3/4/5 absent from the operative
  list**; laws 3+5 survive only as an unnumbered trailing sentence at `SKILL.md:53`, **law 4 appears
  nowhere in SKILL.md**. Those three are exactly `01`'s headline discoveries. SKILL.md is what an
  agent loads; `00` is not in the skill package at all.
- **F-3** the method's **first repository instruction is gate-DENIED here** (`tool-adapters.md:7`
  "start with `rg`"; marker present, `comp-tool-hud.sh:241`, 1,783 live DENYs). **But every tool it
  names exists** — I went hunting fabricated tool names and found zero. Well-grounded on existence,
  wrong on policy.
- **F-4** 11 mandated ledgers, 7 templates — ledgers 7/8 feed G3/G2, so the kit does not equip its own
  gates. **F-5** `SKILL.md:3` routes on *"Use when **Codex** must prove…"*. **F-12** `00` §7's package
  map dangles 3 of 5 paths.

**4. Audited base's own four harder, as base explicitly demanded — and the ranking did not move.**
Five findings; only **F-7** touches an argument rather than an artifact, and it is against `06`'s
declared **CORE MOVE**: `06:78` calls the method's closure *"a single global claim… unfalsifiable at
the grain where work actually happens"*, but the method states closure **per node** three independent
times (`00:61`, `SKILL.md:18`, `workflow.md:5`). Node grain is **finer** than the proposed layer
matrix, so as written the argument justifies the opposite conclusion. **The gap the base genuinely
demonstrates is a DENOMINATOR gap** — closure relative to the *discovered* set with no independent
population to test discovery against. Stated correctly, the base's central limitation (the two blind
regions, *"zero is indistinguishable from nothing there"*) and its central claim become visibly **the
same problem**. Also F-8 (§3 "no blanks permitted" vs §4 "partly-filled is legitimate"), F-9 (titled
v0.4, changelog stops at v0.3), F-10 (no fillable template exists anywhere), F-11 (the pin held; the
unpinned prose beside it decayed the same day).

**5. Recorded what HELD**, because a one-sided audit is not a measurement: `01`'s 6-file source set
6/6, `tool-adapters`' 6 references 6/6, `06`'s ontology-absence claim on spot-check 0/0/0 against a
working positive control of 13, 5/5 commit pins, `04`'s 7 paths 0 dangling. **Sharpest comparative:
CRO-authored files 0 dangling of 7 and 5/5 valid pins; GPT spine 3 dangling of 5.**

## Assessment reached

**The corpus is strongest in its prose and weakest at every point where prose becomes an artifact** —
laws sound / enforceable list drops three; ledger model complete / templates not; charter
well-specified / does not parse; map correct in intent / dangles. That is the signature of
**authored-not-executed** material, and `02:5` prescribes the cure itself. **The corpus has not had
its own stage 1.** Every finding except F-3 surfaces in the first ten minutes of one honest run.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise | **PASS** | forwarder RAN (own banner) — exercised, not resolved |
| `git ls-tree` / `ls-files` | denominator at 3 vintages | **72 / 72 / 68** | refuted the briefed 89; `--diff-filter=D`=0 proves no vintage held more |
| `file(1)` | CRLF census | **9 of 72** | adopted only **after** `grep $'\r'` failed its own positive control |
| `python yaml.safe_load` | charter parse test | **FAIL (F-1)** | positive control `.owned-paths.yaml` parses — the file, not the parser |
| `git cat-file -e` | 5 commit pins in `06`/`07` | **5/5 resolve** | |
| `safe-commit.sh` | 1 commit, `-F` | **PASS** | owned-paths held; risk-reflex CLEAN, 1 file vs 1,659 danger nodes (measured, not defaulted) |

**What worked:** printing the denominator before every count — it is the single practice that caught
the 89 before it became my coverage figure, and it cost nothing.

**What failed — mine, twice, and both are the same class:** `grep -c $'\r'` returned **0 on a
known-CRLF positive control**, so my entire first CRLF sweep was structurally incapable of detecting
what it was pointed at and returned a clean well-formed answer anyway. Separately a `git ls-tree` ran
from the wrong cwd, so the pathspec matched nothing and I got a well-formed **0 about an empty set**
(it made `openai.yaml` read as absent from the import). Both are CLAUDE.md's *"an upstream stage
silently redefines the domain the downstream stage measures over"* — **twice, inside the audit written
to find that class. Caught by controls, neither by care.**

**Gap found:** none new in the tooling. Raw `grep`/`find` was used scoped to a single folder and named
files; no estate-wide sweep, so Gate-1 was not engaged.

## Blockers

**None at me.** Carried, none owed to this lane:
- **At Andrew:** (a) the ATOM_DECOMP **proceed-authorization** base inferred and he has not answered —
  this audit orphans cleanly if reversed; (b) whether **refinement** is now authorized (his relay said
  refinement follows on findings; the findings exist).
- **At CTO, routed by base not by me:** the `.owned-paths.yaml:425` "89 tracked files" text fix.
- **Unresolved and named rather than assumed:** the **held-out fence** (`04:60-64`, not discharged)
  governs any content pass over the 51 `case_study/` files.

## Current State (zero-context handoff)

- **Delivered:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ATOM_DECOMP_CORPUS_AUDIT_PASS1_20260807.md`
  @`0e1d847aa4`. **Committed, NOT pushed** — lanes commit, integrators push.
- **Coverage is stated, not implied: 21 of 72 read in full. The 51 `case_study/` files NOT
  content-audited** — a scope call I declared (`01:73` scopes them as evidence, not requirements),
  **not coverage I achieved.** Not cleared by this pass.
- **`05` gap CLOSED in-session @`69c8527f0d`** (was NOT READ at first landing). Reading it is *audit,
  not refinement*, so it needed no new authorization and was not left declared-and-sitting. Yielded
  **F-13** — `05:20` claims *"four of Atomic Decomposition's own laws"* re-derived; **three** map to
  the list at `00:46-56` (laws 2/3/5), the fourth is `01:28`, a **case-study heading**
  (`semantically equal` in `00` = 0). Does not overturn the result, corrects its magnitude — but the
  strength is a **ratio against the law list** with a numerator not drawn from it, the **89 class**
  again, inside the document arguing that a quoted figure must carry its instrument. **Base accepted
  F-13 unqualified.**
- **F-14 — I FILED IT WRONG AND BASE AUDITED ME BACK. Corrected @`a418ac6108`.** I filed it as a
  document transposition (`00` §5 → `01` §5). Measured: `generaliz` in `00` **whole file = 1** (at
  `00:5`, the Purpose line) and in `02` **whole file = 0**. So the real defect is **a conflated
  pair** — `05:22` makes *two* claims and cites *two* sources jointly, and each supports only one
  half: `00` carries the generalization assertion **at `:5`, not `§5`** (right document, wrong
  section), and `02` §3 carries only the forward-test half, which I had called "correct." **Worse
  than what I filed.** One precision retained: my `§5`-scoped `0` was correct as written — the two
  clauses *after* it were the defective ones, and "the scan was wrong" vs "the inference from the
  scan was wrong" fail differently and are fixed differently.
- **Base independently CONFIRMED F-1 and ACCEPTED F-7 against its own declared core move** — and
  reported committing **my exact instrument class while adjudicating my finding**: an `awk` read
  against a wrong skill path returned EMPTY, byte-identical to a real absence, which would have made
  a correct finding read as unverified. Base has surfaced F-1/F-2/F-4/F-12 to the method owner as a
  **surface, not a dispatch**, and is refining nothing while the proceed-condition is unanswered.

> ## THE PATTERN — and it splits into TWO classes with DIFFERENT remedies
> *(Corrected after base's reply. My first version of this box said "all four caught by controls,"
> which is **not true of the fourth** — and the exception is the useful part.)*
>
> **FOUR instances in one afternoon across two seats. Three are one class; the fourth is not.**
>
> **CLASS A — RETRIEVAL: the scan's scope and its REPORTED scope were not the same set.**
> `1` my `grep -c $'\r'` — could not detect what it was pointed at; **failed its own positive control**.
> `2` my `git ls-tree` from the wrong cwd — well-formed `0` about an empty set.
> `3` base's `awk` against a wrong skill path — EMPTY, byte-identical to a real absence; would have
>     made base report a **correct** finding as unverified.
> **All three produced well-formed, confident, wrong-domain answers. None was caught by care; all
> three by a control on the retrieval.**
>
> **CLASS B — INFERENCE: the scan was RIGHT and the sentence after it was wrong.**
> `4` my F-14. My `§5`-scoped measurement was correct; the two clauses I built on it were not.
> **⛔ NO CONTROL ON THE RETRIEVAL COULD HAVE CAUGHT IT, because the measurement underneath was
> sound.** It was caught only by **an independent seat re-deriving the claim** — base, auditing me
> back. *(The distinction is mine; base's sharpening of what it implies is theirs, and they declined
> to count their own prose-misreading as a fifth instance rather than inflate a count inside an
> exchange about inflated counts.)*
>
> **WHY THIS MATTERS TO THE AUDIT AND NOT ONLY TO US: the corpus's own remedies reach Class A and
> not Class B.** `05`'s E1 (*a quoted figure carries the instrument that produced it*), the
> `evidence-model` claim contract, and the denominator discipline are all controls on **retrieval**.
> Class B is what `06`/`07` already concede from the other direction — *the base types POSITION,
> never INSTRUMENT HONESTY* — and it is why `02:47`'s *"another agent must reproduce material claims
> from the cited locators"* is the load-bearing acceptance target in the whole method: **it is the
> only one aimed at Class B.** Both seats spent the day hunting denominator defects in other
> people's instruments and each committed the class in their own.
- **Nothing was edited in the corpus.** Audit-only was the ruling and it was honored.
- **`comp-estate` refusal census: UNRUN**, deliberately, and the report says so rather than leaving it
  looking covered. If run: bounded sample, denominator printed, never 81 serial calls against a
  shared tool.
- **F-2 / F-4 / F-12 belong to the method owner** (`00:4` names `1.0.0_SA_CTO~A`). **I routed nothing**
  — CRO does not dispatch, and manufacturing a step neither base nor Andrew asked for is the
  gate-manufacture class. Surfaced to base as coordinator; the routing call is theirs or Andrew's.
- **Next pass, if authorized:** the 51 case-study files (fence permitting), and the refinement act on
  these **14** findings — a **separate authorization**, not implied by this audit.

## Closing state — the peer review converged, and §5a is the thing to read

Four review rounds with base after first delivery, each improving the artifact, **and the sequence is
the record worth keeping: base's sharpening beat my framing → my bound beat base's unbounded version
→ base's split beat my bound.**

**§5a is the substantive research output**, and it is now correctly graded rather than uniformly
downgraded:
- **CLAIM A (structural) — SOLID.** `02` §4 has 8 acceptance targets; **7 are runnable by the author
  on their own work**; target 8 at `:47` (*"Another agent must reproduce material claims…"*) is the
  **only one whose subject is a second party**, and it is **last in a flat list of equivalent-looking
  bullets**. A *reading*, not a sample — **N is irrelevant**, and my first bound wrongly applied a
  sample discount to it.
- **CLAIM B (importance) — HYPOTHESIS.** One instance, self-generated, interested parties, two live
  degrees of freedom. **Required test named:** a seat with **no authorship stake**, on a subject
  nobody in the loop wrote. Bar is three unlike systems; this has one.

**I closed the exchange deliberately.** Two seats of **one serial** refining a claim about the value
of *independent* review adds volume to a self-generated instance and **no independence to it** —
further rounds would make the N=1 problem worse, not better. The thing Claim B needs is a seat
neither of us can be.

**Final: 11 commits, ZERO corpus files touched, audit-only intact.** Every correction preserved in
history rather than overwritten (@`69c8527f0d`, @`a418ac6108`, @`2a41642398` → @`5e47d5c8ba`).
