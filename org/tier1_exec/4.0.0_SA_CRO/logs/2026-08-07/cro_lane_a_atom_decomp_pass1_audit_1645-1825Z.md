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
- **Coverage is stated, not implied: 20 of 72 read in full. `05` NOT READ. The 51 `case_study/` files
  NOT content-audited** — a scope call I declared (`01:73` scopes them as evidence, not requirements),
  **not coverage I achieved.** Neither is cleared by this pass.
- **Nothing was edited in the corpus.** Audit-only was the ruling and it was honored.
- **`comp-estate` refusal census: UNRUN**, deliberately, and the report says so rather than leaving it
  looking covered. If run: bounded sample, denominator printed, never 81 serial calls against a
  shared tool.
- **F-2 / F-4 / F-12 belong to the method owner** (`00:4` names `1.0.0_SA_CTO~A`). **I routed nothing**
  — CRO does not dispatch, and manufacturing a step neither base nor Andrew asked for is the
  gate-manufacture class. Surfaced to base as coordinator; the routing call is theirs or Andrew's.
- **Next pass, if authorized:** `05` + the 51 case-study files (fence permitting), and the refinement
  act on these 12 findings — which is a **separate authorization**, not implied by this audit.
