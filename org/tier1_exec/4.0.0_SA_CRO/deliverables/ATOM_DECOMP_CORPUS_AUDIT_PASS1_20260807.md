# ATOM_DECOMP corpus audit — FIRST PASS, AUDIT-ONLY

**Author:** `4.0.0_SA_CRO~A` (ATOM_DECOMP corpus audit lane) · **Date:** 2026-08-07
**Mandate:** Andrew-direct via launcher + base-CRO coordination (`20260807T170606Z`) — dedicated lane
through the corpus because it is GPT-authored; **scope RULED audit-only on this pass, refinement
follows on findings.** Nothing in this document refines, rewrites or restructures the corpus.

**PINNED:** workspace HEAD @`bdac197ce359efa8a81c1f150807af17b2236e9a` (CLOUD) · corpus last touched
@`f9d1d2e73f`. Written **outside** `projects/ATOM_DECOMP/` deliberately: the corpus rests on an
authorization base-CRO **inferred and Andrew has not answered**, so a reversal must orphan this
artifact cleanly rather than leave debris in his folder. Precedent: `3.0.0_SA_CVO~C` @`8170937b60`.

---

## 0. DENOMINATOR FIRST — and the number I was given was wrong

Every count below is stated against a named population, because the first thing this audit found was
a count that did not say what it was a count of.

```
68   GPT-authored corpus (at import @66d83132d5)      <- THE SUBJECT OF THIS AUDIT
 4   authored by 4.0.0_SA_CRO base, 2026-08-07        <- 04, 05, 06, 07; PROPOSAL-bannered
72   tracked at HEAD                                   (= 68 + 4)
73   files on disk                                     (+1 gitignored .pyc)
 0   deletions in ATOM_DECOMP history                  (--diff-filter=D empty; no vintage held more)
```

**I was briefed "89 files" and it is unsupported at every git vintage** — including 72 at the grant
commit @`2a3b1ea408` itself, so the digit was **wrong when written, not drifted since**. It is live in
`.owned-paths.yaml:425`. I could not source it to any candidate denominator I measured and **I am
filing no mechanism for where it came from, because I have no grounding for one.**

The relay was CTO's grant commit → the lane description → MSTR's broadcast → base-CRO's briefing → my
launcher: **four hops, zero measurements, authority gained at each.** Base-CRO independently
re-derived all five figures (5/5 exact), named itself as a hop, and is routing the text fix to CTO.
**The grant itself is sound — both lanes verified, this lane can write.** Only the descriptive digit
is wrong.

Had I taken 89 as my coverage denominator, *"audited N of 89"* would have reported a 21-file gap that
does not exist — a **31% overstatement of my own subject.**

---

## 1. COVERAGE OF THIS PASS — stated before the findings

**Read in full and audited: 21 of 72 files.**

| set | n | disposition |
|---|---|---|
| Spine `00`, `01`, `02` | 3 | read in full |
| `skill/atomic-decomposition/**` (SKILL, workflow, evidence-model, output-contracts, tool-adapters, openai.yaml) | 6 | read in full |
| `templates/**` | 8 | read in full + parse-tested |
| CRO-authored `04`, `05`, `06`, `07` | 4 | read in full |
| **`case_study/ADVI_REFACTOR/**`** | 51 | ⚠ **NOT CONTENT-AUDITED.** Path/existence verified only. |

> **`05` was NOT READ when this report first landed @`0e1d847aa4` and is now read** — closed in the
> same session, because reading it is *audit*, not refinement, and needed no new authorization. It
> yielded **F-13** and **F-14** (§3). The figure above moved **20 → 21**; the earlier count is left
> visible in the commit history rather than silently overwritten.

**The 51 case-study files are a SCOPE CHOICE I am declaring, not coverage I achieved.** `01:73`
scopes them as *"case-study evidence, not generic requirements"* — the reusable method is the spine +
skill + templates, so that is where a first pass buys the most. **They remain unaudited and `05`
remains unread**; neither is cleared by this document.

> ⚠ **The held-out fence bears on any deeper pass.** `04:60-64` records that no file under
> `case_study/` was read for design input during RCN-0006, because the case study **is**
> `ADVI_REFACTOR` / `ADVI_PERFORMANCE`, which sits in the held-out set and the clause is **not
> discharged**. This audit read none of them either. **A future content pass over those 51 files
> needs that question answered first; it is not mine to answer.**

---

## 2. FINDINGS — GPT-authored corpus (the subject)

### F-1 · HIGH · The shipped charter template is invalid YAML

`templates/decomposition_charter.yaml` does not parse. Five unterminated double-quoted scalars
(`system:`, `objective:`, `decision_enabled:`, `authority:`, `denominator:`):

```
ScannerError: while scanning a quoted scalar, line 14 column 14: found unexpected end of stream
POSITIVE CONTROL: .owned-paths.yaml parses OK (3 top-level keys) -> the parser works
```

**Why this is the highest-severity mechanical defect in the corpus:** the charter is not incidental.
`00:38` makes it the *sole output of Layer A* (*"Output: a decomposition charter and required phase
set"*), `SKILL.md:26` opens the method with *"Create a charter containing…"*, and `02:15` specifies a
future engine that **"should accept a charter"** — i.e. it is machine-consumable **by design**.
**The one artifact in the package built to be parsed is the one that cannot be.**

### F-2 · HIGH · Two normative rule-lists that disagree — and the three laws the case study calls its most expensive are the three missing from the operative one

The corpus carries **two** numbered normative lists and neither references the other:

| | list | n |
|---|---|---|
| `00:46-56` | **"Non-negotiable laws"** | 8 |
| `SKILL.md:10-21` | **"Rules"** | 9 |

Neither contains the other. Measured against the Rules block: `identity parity` **0**, `recursive`
**0**, `dispatch` **0**. So spec laws **3, 4 and 5** are absent from the list an agent actually
operates from:

- **Law 3** *trigger counts are not trigger identity parity*
- **Law 4** *an immediate target map is not a recursive control graph*
- **Law 5** *a successful dispatch is not target, artifact, or consumer success*

Laws 3 and 5 survive only as an **unnumbered trailing sentence** at `SKILL.md:53` — *"Count parity is
not identity parity. Invocation success is not serving proof."* — inside a paragraph about resolving
conflicts. **Law 4 appears nowhere in SKILL.md**; it survives only as a procedural verb in
`workflow.md:31` (*"Follow targets recursively"*), which instructs a step rather than binding a claim.

**Why this is severe rather than editorial:** `SKILL.md` is the artifact an agent loads; **`00` is not
in the skill package at all.** And the three demoted laws are precisely `01`'s headline discoveries —
`01:36-38` *"Trigger inventory is not runtime architecture"* (laws 3+4) and `01:50-52` *"Dispatch
success is not serving success"* (law 5). **The corpus's own case study identifies these as the
hardest-won findings of the engagement, and they are the ones that did not make the enforceable
list.** A method whose most expensive lessons are demoted to prose has lost them for the next reader.

#### F-2 DELTA TABLE — ruled by `1.0.0_SA_CTO` (method owner, 2026-08-07 ~1945Z)

> **THE TABLE IS THE DELIVERABLE — NOT A REWRITTEN LIST.** CTO's ruling, and the reasoning is the
> load-bearing part: *"Reconciling two normative lists by union is a TAXONOMY ACT, and those are not
> yours or mine to perform quietly on Andrew's corpus."* **Ratifying a merged normative vocabulary is
> method authorship and goes to Andrew with this table in front of him.** So F-2 stays a **measured
> finding**, applied to nothing. It is also **not** what Andrew's refinement approval bought — that
> was scoped to mechanical defects, and a normative rewrite is not one.
>
> **Operative list ruled: `SKILL.md:10-21`.** *"It is what an agent actually executes; `00` §5 is prose
> ABOUT the method. When a description and an executable disagree, the executable is the state and the
> description is the claim."*

**The delta is BIDIRECTIONAL — this is sharper than what I originally filed.** I reported three laws
missing from the Rules block. Mapping both directions shows **neither list contains the other: 5 of 8
laws have a Rule; 5 of 9 Rules have a law.**

| `00` §5 law | counterpart in `SKILL.md:10-21` (the OPERATIVE list) |
|---|---|
| 1 separate states (declared→serving) | **Rule 3** ✅ |
| 2 static graph silence is not absence | **Rule 4** ✅ |
| **3 counts are not identity parity** | ⛔ **ABSENT from Rules.** Survives only as unnumbered prose at `SKILL.md:53`. |
| **4 immediate target map ≠ recursive control graph** | ⛔ **ABSENT FROM `SKILL.md` ENTIRELY.** Nearest trace is `workflow.md:31` *"Follow targets recursively"* — a procedural step, not a binding claim. |
| **5 dispatch success ≠ target/artifact/consumer success** | ⛔ **ABSENT from Rules.** Survives only as unnumbered prose at `SKILL.md:53`. |
| 6 consumer contracts fixed unless migrated | **Rule 8** ✅ |
| 7 tool errors reduce coverage, not verdicts | **Rule 6** ✅ |
| 8 no deletion before replacement…negative proof | **Rule 9** ✅ |

| `SKILL.md` Rule | counterpart in `00` §5 (the "non-negotiable laws") |
|---|---|
| **1 start read-only unless mutation authorized** | ⛔ **NO LAW.** |
| **2 pin identity, environment, scope, denominator, consumer boundary** | ⛔ **NO LAW.** |
| 3 keep the six states separate | Law 1 ✅ |
| 4 treat static graphs as lower bounds | Law 2 ✅ |
| **5 every claim carries source, locator, measurement time, scope, denominator, limitation** | ⛔ **NO LAW** — and this is the method's own evidence contract. |
| 6 tool failure is a coverage limitation | Law 7 ✅ |
| **7 expand every discovered node until classified** | ⛔ **NO LAW** — it is `00` **§6** (closure model), a different section from the law list. |
| 8 preserve consumer contracts | Law 6 ✅ |
| 9 delete nothing before…absence proof | Law 8 ✅ |

**What the table shows that the one-directional finding did not:** the two lists are not
*list-plus-omissions*, they are **two independently drafted normative vocabularies that overlap on
five items.** `00` §5 carries the three *epistemic* laws (3/4/5 — the "X is not Y" cautions) that the
executable dropped; `SKILL.md` carries four *procedural* obligations (read-only default, pinning, the
claim contract, frontier expansion) that the law list never elevated. **Each list is missing the
other's characteristic content**, which is a Rule-24 intent-coherence break rather than an oversight:
they were built to answer different questions and are both presented as *the* rules.

**⛔ NOT RATIFIED, NOT APPLIED, NOT MERGED.** The decision — one list, and which content survives into
it — is Andrew's. It is cheap to rule once with this table and expensive to unpick if guessed.

### F-3 · MEDIUM-HIGH · The method's first repository instruction is gate-DENIED in this estate

`tool-adapters.md:7` — *"Start with `rg --files` and `rg` for names, paths, bucket keys, ARNs…"*

This is the **opposite** of CLAUDE.md Rule 21, under which comp-tools are the default and raw search
is the gated exception. Grounded on the live gate, not on the prose:

```
marker  org/mcp/comprail-gate1.enforce            PRESENT (0 bytes -- presence is the signal)
hook    .tools/hooks/comp-tool-hud.sh:241         reads [ -f "$WS/org/mcp/comprail-gate1.enforce" ]
rail log org/mcp/comp-which-rail.log              1,783 DENY lines / 35,379 total
most recent DENY                                  2026-08-07T16:19:12Z  (today, live)
```

**An agent following the method's stated first move gets denied at step one.**

Second, opposite-direction conflict: `tool-adapters.md:16` — *"Do not invoke `comp-pipescript` unless
the operator explicitly authorizes it"* — against `org/XXX.md:478/480/481/483`, which **mandate**
`comp-pipescript` as a role minimum for DS, DT, AE and COO.

> **The honest other half, and it matters:** every tool this file names **exists** —
> `comp-blast`, `comp-trace`, `comp-heat`, `comp-kuzu`, `comp-pipescript` all present in `.tools/`,
> and `infra/aws/globgrph/kuzu_cli.py` (cited at `:14`) resolves. **I expected fabricated tool names
> and found none.** The file is well-grounded on *existence* and wrong on *policy* — which is the
> harder defect to see, because nothing dangles.

### F-4 · MEDIUM · The method mandates 11 ledgers and ships 7 templates

`evidence-model.md` **"Required ledgers"** is an 11-item numbered list. `templates/` ships 7 CSVs.
Mapping them:

| # | required ledger | template |
|---|---|---|
| 1 | System inventory | `system_inventory.csv` |
| 2 | Script I/O | `script_io_contract.csv` |
| **3** | **Artifact lineage** | **— none —** |
| **4** | **Resource inventory** | **— none —** |
| 5 | Control edges | `control_edges.csv` |
| **6** | **Runtime observations** | **— none —** |
| **7** | **Consumer contracts** | **— none —** |
| **8** | **Contradictions and unknowns** | **— none —** |
| 9 | Migration waves | `migration_waves.csv` |
| 10 | Replacement ledger | `replacement_ledger.csv` |
| 11 | Decision register **and** validation matrix | `validation_matrix.csv` — **half**: no decision register |

**Five mandated ledgers have no template, and #11 ships one of its two halves.** (`evidence_ledger.csv`
is an eighth template implementing the `evidence-model.md` *claim contract*, which is not one of the
11.) Ledgers 7 and 8 are load-bearing for the method's own gates — G2 turns on contradictions, G3 on
consumer contracts — so the kit does not equip the gates it enforces.

### F-5 · MEDIUM · The skill is vendor-coupled to a non-Claude agent

`SKILL.md:3` frontmatter: *"Use when **Codex** must prove script I/O…"* — the `description` field is
the **routing surface** by which a skill is selected. `agents/openai.yaml` ships an OpenAI-shaped
invocation (`default_prompt: "Use $atomic-decomposition to…"`), CRLF-terminated.

`00:9-12` presents the skill as **Layer A of the product**, so this is not a stray file: adopting the
package here requires the trigger text to name this fabric's agent. Filed as an adoption blocker, not
a style note.

### F-6 · LOW · Mixed line endings — 9 of 72

`06`, `07`, `openai.yaml`, and 6 files under `case_study/`. Cosmetic; recorded for completeness only.

> **METHOD NOTE — I caught this only because I ran a control, and my first sweep was garbage.**
> `grep -c $'\r'` returned **0 on a known-CRLF positive control**, so my initial sweep was
> structurally incapable of detecting the thing it was pointed at, and returned a clean well-formed
> answer anyway. `file(1)` discriminates and produced the real figure. **Separately, an earlier count
> ran `git ls-tree` from the wrong cwd, so the pathspec matched nothing and I got a well-formed `0`
> about an empty set.** Both are CLAUDE.md's *"an upstream stage silently redefines the domain the
> downstream stage measures over"* class — **twice, in the audit written to find that class.**

---

## 3. FINDINGS — the four CRO-authored files (audited harder, per base's own instruction)

Base-CRO's brief was explicit: *"Do not spare the 04/05/06/07 files, do not treat my PROPOSAL banners
as endorsements, and do not route a finding about my work through me for softening."* These are filed
accordingly. **All four are now covered** — `05` was read after the first landing and produced F-13
and F-14.

### F-7 · MEDIUM · `06` §2's "core move" mischaracterizes the method, and the error points the remedy at the wrong gap

`06:78` — *"Today that is a single global claim, and a global claim is unfalsifiable at the grain
where work actually happens."*

**The method states closure PER NODE, three independent times:**

```
00:61            "every discovered node is in scope, a named boundary, external, or an owned unknown"
SKILL.md:18      "Expand every discovered node until it is in scope, a named boundary, external, ..."
workflow.md:5    "Closure exists only when each endpoint is in scope, an explicit boundary, ..."
```

All three quantify over **every discovered node**. The criterion is therefore already at **node**
grain — which is **finer** than the layer grain the base proposes. **Taken at face value, §2's own
argument would justify the opposite conclusion:** if fineness of grain were the issue, an 11-row
layer matrix is a coarsening.

**The gap the base actually demonstrates — and it is real — is a DENOMINATOR gap, not a
falsifiability gap.** Closure is defined relative to the **discovered** set, and nothing in the method
supplies an independent population against which to test whether discovery was complete. That is
exactly what the base's layer partition supplies: named buckets in which *emptiness becomes visible*.
**Coverage, not falsifiability.**

**Why this matters beyond wording:** §2 is the document's declared **CORE MOVE**, so its weakest
sentence is load-bearing on the framing — and the two defects imply different remedies. A
falsifiability defect is fixed by a matrix; a denominator defect is fixed by an independent
population enumeration, **which the base's own §4 concedes it often cannot obtain** (the two
structural blind regions, where *"a traversal returns zero, and zero is indistinguishable from
nothing there"*). Stated as a denominator gap, the base's central limitation and its central claim
are visibly the same problem. Stated as a falsifiability gap, they look unrelated.

### F-8 · MEDIUM · `06` §3 and §4 directly contradict each other

```
06:84   "## 3. THE BASE - one row per layer, four columns, NO BLANKS PERMITTED"
06:165  "A PARTLY-FILLED BASE IS A LEGITIMATE OUTPUT"
```

The v0.4 correction landed in §4 — including the required three-state declaration for an empty cell —
but **§3's heading was never updated** and still forbids what §4 mandates. A reader obeys whichever
section they reach first, and §3 is the section that tells them how to fill it in.

### F-9 · MEDIUM · `06` is titled v0.4 and has no v0.4 changelog entry

Header block carries `**v0.2**` and `**v0.3**` lines; the H1 reads **v0.4 DRAFT**; **zero** v0.4
entries. What changed in v0.4 is recoverable only by hunting inline `*(v0.4…)*` annotations scattered
through §4. The document's version record stops one version short of the document.

### F-10 · LOW-MEDIUM · No fillable template for the coherence base exists anywhere

`06:84` promises *"one row per layer, four columns"*, but the table actually rendered in §3 is a
**three-column explanatory** table (`layer | the question it forces | why it catches…`). The real
four-column artifact (`TOUCHES | INVARIANT | OUT | OWNED UNKNOWN`) appears **only** as a retro-filled
instance inside `07:41-55`. `find -iname '*coherence*'` outside `06` returns **0**; `templates/` holds
nothing for it.

This is the mechanical form of what `3.0.0_SA_CVO~C` found conceptually (*"cannot be handed to an
agent as fill-this-in"*) — **and it is the cheaper half to fix**, though fixing is not this pass.

### F-13 · MEDIUM · `05` claims four re-derived laws; **three** of the four are laws

`05:20` — *"It independently arrived at **four** of Atomic Decomposition's own laws without consulting
them"* — and `05:24` makes the count load-bearing: *"the laws held **four times**."*

The law list is `00:46-56`, eight numbered entries. Mapping `05`'s four table rows against it:

| `05` row | maps to |
|---|---|
| *"Static graph silence is not absence"* | **law 2** ✅ |
| *"Trigger counts are not trigger identity parity"* | **law 3** ✅ |
| *"A successful dispatch is not target, artifact, or consumer success"* | **law 5** ✅ |
| *"Source systems are not semantically equal…"* | ❌ **NOT A LAW.** `01:28` — a **case-study section heading**. `semantically equal` appears in `00` **0 times**. |

**Three laws re-derived, plus one case-study observation, reported as four laws.**

**This does not overturn the result — it corrects its magnitude.** Three of eight non-negotiable laws
independently re-derived by a different team on a different substrate, unstaged, is a strong finding
and `05` is right that it *"is worth more to the method than any extension below."* But the strength
is stated as a **ratio against the law list**, and the numerator is inflated by one — **the same
class as the 89** (§0): a count whose population is not quite the one it names. It is filed
specifically because `05` is the document arguing that a quoted figure must carry the instrument that
produced it (its own **E1**).

### F-14 · LOW-MEDIUM · `05:22` makes two claims, cites two sources jointly, and neither source supports both

> **CORRECTED 2026-08-07 after `4.0.0_SA_CRO` (base) audited this finding back and measured it.**
> **My original framing was wrong in both directions and the corrected defect is slightly worse than
> the one I filed.** Superseded text is in the commit history at @`69c8527f0d`; the finding is real
> either way.

`05:22` — *"`00_ATOMIC_DECOMPOSITION_SPEC.md` **§5** and `02_ADOPTION_AND_EVALUATION.md` §3 both
**assert** the method generalizes and propose forward-testing it."*

**One sentence, two claims, two citations offered jointly — and each citation supports only one half:**

```
'generaliz' in 00, WHOLE FILE      1   -> at 00:5, the Purpose line. 00 DOES assert generalization.
'generaliz' in 00 sec5 (46-56)     0   -> but NOT in the section cited. Wrong SECTION, right DOCUMENT.
'generaliz' in 02, WHOLE FILE      0   -> 02 sec3 does NOT support "asserts the method generalizes".
'forward-test' in 02               1   -> positive control: 02 sec3 supports the FORWARD-TEST half only.
```

So: `00` carries the generalization assertion **at `:5`, not `§5`**; `02 §3` carries the forward-test
proposal and **not** the generalization claim. **A conflated pair, not a transposition** — and my
original filing called it "the wrong document" (it is the right document, wrong section) and called
the `02` half "correct" (it supports one of the two claims it is cited for).

**Still LOW-MEDIUM: the underlying claim is true and is supported, just not by the pointers given.**
It remains the third distinct cross-reference defect in the corpus (with F-11 and F-12) and the only
one inside a document whose thesis is that attribution must survive the quote.

> **One precision retained rather than conceded, because the correction record should itself be
> accurate:** my original *"`00` §5 … `generaliz` appears **there** 0 times"* was **scoped to §5 and
> is correct as written** (§5 = lines 46-56, zero hits). The defects were the two clauses **after**
> it. **This is the fourth instance today of a scan whose scope and whose *reported* scope were not
> the same set — and it landed inside the finding about scope defects, on both sides of the exchange.**

### F-11 · LOW · `07`'s pin held; the unpinned prose beside it decayed the same day

`07:4-5` correctly pins the version under test at @`0ad081a918` — **and in the same sentence asserts
the current file "is now v0.3".** It is **v0.4** (@`f82f96e66b`). The note exists to warn that a
moving filename makes a discharged test read as outstanding; **its own unpinned half went stale within
hours.** A pin protects the clause it is attached to and nothing else.

---

## 4. WHAT HELD — claims I tried to break and could not

Recorded because a one-sided audit is not a measurement.

| claim | verdict |
|---|---|
| `01:64-71` — the 6-file "Durable ADVI source set" | **HOLDS.** 6 of 6 present. |
| `tool-adapters.md:14-16` — 5 comp-tools + `kuzu_cli.py` | **HOLDS.** All 6 exist. |
| `06:52-59` — zero ontology terms across spine + skill | **HOLDS** on spot-check (`substrate`/`territory`/`vertical` = 0/0/0; positive control `denominator` = 13, so the grep reads the files). |
| `06`/`07` commit pins @`0ad081a918` @`61794af2d0` @`22509c931d` @`8170937b60` @`f82f96e66b` | **HOLD.** 5 of 5 resolve. |
| `04`'s 7 cited repo paths | **HOLD.** 0 dangling of 7. |

> **The sharpest comparative result in this audit:** the **CRO-authored** files carry **0 dangling
> references of 7 and 5/5 valid commit pins**, while the **GPT-authored** spine's package map carries
> **3 dangling of 5** (F-12 below). **The pinning discipline demonstrably works** — and F-11 shows
> precisely where it stops working: at the prose the pin is not attached to.

### F-12 · MEDIUM · `00` §7's package map — 3 of 5 paths dangle

Filed here because it is the direct comparator above. `00:70-71` cite full paths
(`skill/atomic-decomposition/…`); `00:72-74` drop the prefix:

```
references/evidence-model.md        DANGLING   (no top-level references/ exists)
references/tool-adapters.md         DANGLING
references/output-contracts.md      DANGLING
  -> all three resolve at skill/atomic-decomposition/references/
```

A reader following §7 — the corpus's own map of itself — fails on three of five entries.

---

## 5. ASSESSMENT

**The method is rigorous where it reasons and unreliable where it must be executed.** Its evidence
model, absence standard, gate assertions and multi-state separation are genuinely strong, and its
central discipline — *tool failure is a coverage limitation, never absence proof* — is exactly the
estate's own doctrine, independently arrived at. **Nothing here argues against the method.**

The defects cluster with a single shape, and it is worth naming because it predicts where the rest
will be: **the corpus is strongest in its prose and weakest at every point where prose becomes an
artifact.** The laws are sound and the enforceable list drops three of them (F-2). The ledger model is
complete and the template set is not (F-4). The charter is well-specified and does not parse (F-1).
The package map is correct in intent and dangles in three of five paths (F-12). The tool doc names
every tool correctly and gets the policy backwards (F-3).

**That is a consistent signature of authored-not-executed material** — which is what a GPT-authored
corpus that has never been run would look like. `02:5` proposes the remedy itself: *"Use the packaged
skill manually on one read-only system audit."* **The corpus has not had its own stage 1.** Every
finding in §2 except F-3 would surface in the first ten minutes of one honest attempt to run it.

### 5a. One finding about the method that came out of auditing, not out of reading

This audit and its review produced **four measured instrument failures across two seats in one
afternoon** (mine: a `grep` that failed its own positive control, a pathspec that matched nothing,
and F-14; base's: an `awk` against a wrong path). They **do not form one class, and the split is the
finding:**

- **CLASS A — RETRIEVAL** *(3 of 4)*: the scan's scope and its *reported* scope were not the same
  set. Each returned a well-formed, confident, wrong-domain answer. **Each was caught by a control on
  the retrieval, none by care.**
- **CLASS B — INFERENCE** *(1 of 4, mine, F-14)*: the scan was **right** and the sentence built on it
  was wrong. **No control on the retrieval could have caught it** — the measurement underneath was
  sound. It was caught only by **an independent seat re-deriving the claim.**

**The method's remedies are almost entirely aimed at Class A.** `05`'s **E1** (*a quoted figure
carries the instrument that produced it*), `evidence-model.md`'s claim contract, the denominator and
scope discipline, `06`'s COVERAGE/GRAIN/SCOPE columns — all are controls on **retrieval**. Class B is
what `06`/`07` already concede from the other direction (*"it types POSITION, never INSTRUMENT
HONESTY"*), and they are right that **adding rows cannot reach it.**

**What reaches Class B is already in the corpus and is not treated as load-bearing:** `02:47` —
*"Another agent must reproduce material claims from the cited locators."*

**And the sharp cut is not Class A vs Class B — it is WHO CAN RUN THE CHECK.** *(Sharpening by
`4.0.0_SA_CRO` base, re-derived from the locator, which is the only honest way to endorse a finding
whose subject is re-deriving from locators. Verified here 8/8 before adoption.)* `02` §4 carries
**eight** acceptance targets, lines 40-47:

```
40-46   targets 1-7   EVERY ONE IS RUNNABLE BY THE AUTHOR ON THEIR OWN WORK
                      (use two sources - classify your endpoints - timestamp your evidence -
                       fail your own parity check). Most are mechanically gateable.
47      target 8      "ANOTHER AGENT must reproduce material claims from the cited locators."
                      THE ONLY ONE WHOSE SUBJECT IS A SECOND PARTY. It STRUCTURALLY CANNOT BE
                      RUN BY THE PARTY BEING CHECKED.
```

**So the list is seven self-checks and one independent re-derivation, presented as eight equivalent
bullets, with the categorically different one last.** A reader ticking down it has no way to see that
the eighth is not like the seven — **and it is the only one aimed at the failure class where the
author's own measurement is sound.**

**Class B is not uncontrollable; it is controllable only by a SECOND PARTY** — the control exists, it
is *social rather than mechanical*, and it cannot be automated away because the thing it checks is
judgement. *(Base's correction to its own earlier phrasing, adopted.)*

**The evidence is this exchange.** My F-14 scan was right and my inference from it was wrong; nothing
I could have run on my own retrieval would have caught that, because there was nothing wrong with the
retrieval. It was caught by base re-deriving my claim from my cited locator — **`02:47` executing, on
this audit, against this auditor. The method's weakest layer and its own remedy for that layer met in
one event, and the finding and its evidence are therefore the same event.**

> ## ⚠ THE BOUND ON §5a — AND IT APPLIES TO **ONE OF THE TWO CLAIMS, NOT BOTH**
> *(My first bound downgraded both. `4.0.0_SA_CRO` base corrected it: collapsing them undersells the
> solid half. Adopted — the split is sharper than my version and than base's original overclaim.)*
>
> **CLAIM A — STRUCTURAL.** *`02` §4 carries 8 acceptance targets; 7 are runnable by the author on
> their own work; target 8 at `:47` is the only one whose subject is a second party; and it is last in
> a flat list of equivalent-looking bullets.*
> **STATUS: SOLID.** This is **a fact about the text**, re-derived independently by both seats from
> the locator. **It does not depend on our exchange having happened at all** — anyone can check it in
> thirty seconds and it comes out the same. **N is irrelevant to a structural reading.**
>
> **CLAIM B — IMPORTANCE.** *That the asymmetry MATTERS, because target 8 catches a failure class the
> other seven structurally cannot.*
> **STATUS: HYPOTHESIS.** It rests on **ONE instance, self-generated, by interested parties.** We are
> base and lane under a single serial, auditing a corpus one of us wrote, and the "independent
> re-derivation" that demonstrates `02:47` was performed by the author of the document being examined.
> **Weaker independence than `3.0.0_SA_CVO~C` had** (@`8170937b60` — selection rule fixed *before*
> looking, written outside the folder; we did neither). At least **two degrees of freedom** are live by
> `07`'s own accounting: **we chose the subject, and we are scoring our own exchange.**
> **A hypothesis cannot authorize a ruling**, a change to the acceptance list, or a re-ordering of
> `02` §4 — and this one will not.
>
> **THE TEST CLAIM B WOULD NEED, so it is not left vague:** a seat with **no authorship stake in the
> corpus**, scoring whether target-8-class failures (**sound retrieval, wrong inference**) are caught
> by anything other than second-party re-derivation, **on a subject nobody in the loop wrote.** The
> method's bar is **three unlike systems.** This has **one, from an interested party.**

Filed as an **observation for the method owner, not a proposed change** — refinement is not this pass.

On the four CRO-authored files: they are markedly more disciplined than the corpus they sit beside —
pinned, controlled, self-refuting, and carrying their own bias statements. **The findings against them
are real but second-order**, and F-7 is the only one that touches an argument rather than an artifact.
Base-CRO's instruction to audit them harder was the right call and did not change the ranking: the
severe defects are in the GPT-authored subject.

---

## 6. WHAT THIS PASS DID NOT DO

- **No refinement.** Audit-only was the ruling; nothing in the corpus was edited.
- **51 `case_study/` files not content-audited** (§1) — a deeper pass over them needs the **held-out
  fence** question resolved first (`04:60-64`), which is not mine to resolve. *(`05` WAS the other
  gap and is now closed — reading it is audit, not refinement, so it needed no new authorization and
  was not left sitting.)*
- **The `comp-estate` refusal census is UNRUN.** Base named it as a high-value open target
  (all 81 active projects, count refusals, sizing `06`'s unreachable class). I declined to open with
  it: it hammers a shared tool to refine a point already made, and `06:230-235` already narrows the
  class after refuting its own 37% proxy. **If run, it should be a bounded sample with the denominator
  printed — not 81 serial calls.** Status unchanged: *size unknown — exact method named — unrun.*
- **No mechanism filed for the "89"** — the digit is refuted, its origin is not grounded, and a
  plausible story is worth less than the honest gap.

---

## 7. COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise probe | **PASS** | forwarder RAN (own banner); 96 of 97 resolve bare |
| `git ls-tree` / `ls-files` | corpus denominator at 3 vintages | **72 / 72 / 68** | refuted the briefed 89; `--diff-filter=D` = 0 confirms no vintage held more |
| `file(1)` | CRLF census | **9 of 72** | adopted **after** `grep $'\r'` failed its own positive control |
| `python yaml.safe_load` | charter template parse test | **FAIL (F-1)** | positive control `.owned-paths.yaml` parses — the parser works |
| `git cat-file -e` | 5 commit pins in `06`/`07` | **5/5 resolve** | |
| raw `grep`/`find` | scoped to `projects/ATOM_DECOMP` + named files | used | in-scope for a single-folder corpus audit; no estate-wide sweep run, so Gate-1 was not engaged |

**What worked:** printing the denominator before every count — it is what caught the 89 before it
became my coverage figure. **What failed:** two of my own retrievals silently redefined their domain
and returned well-formed answers about the wrong population (§2 F-6 method note); both were caught by
controls, neither by care. **Gap found:** none new in the tooling.

---

## 8. BLOCKERS

**None at me.** Carried, none owed to this lane:

- **At Andrew:** the ATOM_DECOMP **proceed-authorization** base-CRO inferred and he has not answered.
  This audit is structured to orphan cleanly if he reverses it — nothing here depends on the corpus
  surviving.
- **At Andrew:** whether **refinement** is authorized on these findings (his relay said refinement
  follows on findings; the findings now exist).
- **At CTO (routed by base, not by me):** the `.owned-paths.yaml:425` "89 tracked files" text fix.
- **Unresolved, and named rather than assumed:** the **held-out fence** governing any content pass
  over the 51 `case_study/` files.
