# SPEC: the project tree -- `org/missions/D{n}/{MACRO}/{PROJECT}/` and the artifact inventory

**Author:** `2.0.0_SA_COO` · 2026-09-02 · **Status:** SPEC FOR ANDREW'S REVIEW. **PROSPECTIVE ONLY -- nothing retroactive** (Andrew, ~19:3xZ: *"we dont need to do any of this retroactively, this would all be for prospective work"*). Water-test projects: **`ETFS_GUARDRAIL` · `NFRA_CLDGRPH` · `NFRA_COMPEFFICACY`**.
**Occasion:** Andrew-direct at the COO terminal, ~19:2xZ, after two water tests through L1-L5 produced
fourteen process defects in one afternoon. VERBATIM, the three instructions this spec answers:

> "we need to know every single artifact (e.g. prd, to, surprise, etc.) and its components (e.g.
> surface_check in prd) created at each point and who creates it + where it lands in the repo. We also
> need to know every single tool that is used step by step."

> "PRDs, TOs, surprises, investigations, remediations, etc. the entire thing, should sit in a pathed
> folder like directive -> macro -> project, each a nested folder in the prior, where in that project
> folder sits all the prds, briefings, tos, surprises, worker deliverable files, everything."

> "all of it should be stored in an org/missions/directives/macros/projects folder, where that projects
> folder maybe nests /prd /task-orders /deliverables /surprise-channel etc, and /surprise-channel has a
> nested /investigations and /remediations" · "maybe even include /decompositions as well for the
> atom-decomp runs"

⛔ **RULE 24 BINDS THIS DOCUMENT.** A folder tree is a schema. The four-postulate record is s.9.

---

## 0. The measured problem -- why a tree, stated as numbers

**One project's artifacts, today.** `comp-find --name 'ADVI_PERFRP*'`: **36 hits across 9+ directories**
-- five `deliverables/` dirs under five different seats and lanes, four `task_orders/` dirs, and that is
NAME-match only. Its PRD is at `workflows/atom_decomposition/runs/`, its surprise rows in
`org/surprise_channel/`, its row in `org/projects/`. **To read one project end to end you open ~12
directories and know which seat did what.**

**PRDs today sit in seven different directories** (`prds[].path` across 352 rows): `docs/architecture`
355 · **no path 157** · `docs/briefs` 32 · CTO deliverables 23 · `/` 6 · `docs/references` 5 ·
`deck_generation` 5 · CVO deliverables 4.

**Three naming layers, and only one is clean:**

| layer | state, measured |
|---|---|
| `project_code` | **CLEAN.** `project_code == filename` on 352 of 352 rows. |
| `macro_code` | **NOT an enum.** 38 distinct values; only **12 carry an active project**; several are name fragments, not macros (`GLOBALALARM`, `ASSETCLASS`, `PLATFORM_OPS`, `OPAL_TICKET`). |
| `directive` | **SOUND as a partition.** 13 directives; 0 projects in more than one; 0 active rows whose `directive` disagrees with `DIRECTIVES.yaml` membership. |

**Two carriers of membership already, and the split has been measured live.** `DIRECTIVES.yaml`
lists projects per directive; `org/tier0/missions.yaml` attaches projects to subgroups by GLOB
(`attribution / classify / meta_paths / drift`). The glob `NFRA_GRAPH*` did not match `NFRA_CLDGRPH`
today; the D8 row read D8 while `DIRECTIVES.yaml` did not list it for an hour. **A path would be a
THIRD carrier unless it is made the ONLY one.** That is the central design choice (s.2, choice A).

**Lanes are entirely seat-keyed.** `.owned-paths.yaml`: 61 lanes, ~34 seat-directory patterns,
**0 artifact-type globs**. Authority today answers "whose directory is this"; a project tree needs it
to answer "what kind of artifact is this, and who may author that kind" (s.6).

---

## 1. The tree

Reading Andrew's *"org/missions/directives/macros/projects"* as LEVELS, not literal names -- the root
is where `DIRECTIVES.yaml` already lives:

```
org/missions/
  DIRECTIVES.yaml                       the directive register (STAYS; membership DERIVED from the tree, s.2)
  D8/                                   directive  -- ONE level per directive, D0..D12
    MDPF/                               macro      -- a RATIFIED macro enum (s.5), not free text
      MDPF_COTREMEDIATION/              project    -- the project_code, verbatim, one folder
        project.json                    the register row (moved here; index stays flat, s.2 choice B)
        brief/                          step 1   CRO
        prd/                            step 2-4 CTO   (ENDPOINT lives INSIDE the PRD, never beside it)
        decompositions/                 step 5   COO   (atom-decomp runs + the rectangle)
        task-orders/                    step 6   COO   (one file per TO; the ONLY step-6 gate reads here)
        deliverables/                   step 7   worker (proof-of-spec, evidence, outputs)
        surprise-channel/               steps 7-10
          investigations/               rows the worker appends; INVESTIGATION_v1.md + .Z. variant
          remediations/                 rows CVO routes at step 10
        ledger/                         deploy-completion + change-management entries for THIS project
        cards/                          substrate cards for resources THIS project builds on
```

**Concrete path for a live project:** `org/missions/D8/MDPF/MDPF_COTREMEDIATION/prd/MDPF_COTREMEDIATION_PRD.md`.

**What the path ENCODES, and therefore what a move means:** the directive assignment and the macro
are IN the path. **A directive move is a `git mv` of the whole project folder** -- visible, atomic,
diffable, and impossible to half-do. D8's placement flip and ETFS_GUARDRAIL's D4->D8 both happened
today as JSON edits that nothing displayed; under the tree they are a rename that shows in `git log`.

---

## 2. The three design choices, each with the alternative it rejects

**A. THE PATH IS THE MEMBERSHIP. `DIRECTIVES.yaml` `projects:` lists become DERIVED.**
The tree is the single source of truth for "which directive, which macro, which project". A
generator (or a validator on commit) reads `org/missions/D*/*/*/project.json` and either WRITES the
`projects:` lists or REFUSES a commit where they disagree. `missions.yaml`'s glob attach lists are
replaced by the same read. *Rejected alternative:* keep three carriers and add a sweep. That is the
D8 split with a monitor on it -- and a monitor on an unsettled route measures the wrong thing
precisely (CLAUDE.md s.5).

**B. `project.json` MOVES INTO THE FOLDER. `org/projects/` BECOMES A GENERATED INDEX.**
The row is the project's own record and belongs with it. But **six gates and tools read
`org/projects/<CODE>.json` by path today** (`to-pipeline-gate.py:184` with its `FOO_BAR_BAZ -> FOO_BAR
-> FOO` walk-back, `to-check.py`, `registry-check.py`, `fabric-check.py`, `/drive`'s hot-registry read,
`surprise-row-gate.py`'s identity read). So `org/projects/` stays as a **flat index** -- one small
generated file per project carrying `home:` (the folder path) plus the fields gates compare
(`dep_stage`, `fabric`, `directive`, `status`) -- until each reader is repointed. *Rejected
alternative:* symlinks. Git-on-Windows, `autocrlf`, and MSYS path conversion make a symlink the least
trustworthy object in this estate.

**C. LANES RE-KEY BY ARTIFACT TYPE, NOT BY SEAT DIRECTORY.** See s.6. *Rejected alternative:* keep
seat-keyed lanes and give every seat a lane into every project folder -- that is no lane at all.

---

## 3. THE ARTIFACT INVENTORY -- every step, every artifact, its components, its author, its home, its tools

The ten steps are the canonical loop's (`SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md`, Andrew's
step-4 fill, ownership CRO 1 | CTO 2,3,4 | COO 5,6 | worker 7 | CVO 8,9,10). **`home:` is the path
under the project folder.** Gates are the only mechanical enforcement; everything else binds by reading.

| step | owner | ARTIFACT | its COMPONENTS (each a named section or field) | `home:` (under `{PROJECT}/`) | TOOLS used | GATE |
|---|---|---|---|---|---|---|
| **1** | `4.0.0_SA_CRO` | **BRIEF** | measured findings with denominators · what it REFUSES to claim · open items for Andrew · design ancestors · the bound the PRD must carry | `brief/<topic>-<date>.md` | `comp-find` · `comp-kuzu-inc` (live plane) · `comp-read` · `/brief-create` | none. **L1 is the only step with zero mechanical grounding** (CTO 92551 s.4: `brief-create` invokes no comp-tool) |
| **2** | `1.0.0_SA_CTO` | **ENDPOINT** | `FWD-1..n` outcomes, each with DONE-WHEN (EXERCISED/APPLIED) + ACCEPT + SOURCE · ids permanent, never reused · a retired outcome leaves its number vacant | **inside the PRD** (`prd/…_PRD.md` ENDPOINT section) -- never a sibling file | `/endpoint --forward <brief>` | limb 5 of the step-6 gate checks the section EXISTS (**it does not check FWD-n existence** -- `surprise-row-gate.py:53` validates shape only) |
| **3** | `1.0.0_SA_CTO` (row) · `0.0.0_AB_MSTR` (register) | **PROJECT ROW** + **REGISTER ENTRY** | `project_code` · `macro_code` · `directive` · **`fabric`** (Andrew's call) · `dep_stage` (6-value enum) · `status` · `prds[]` · `blocking` · `fabric_ruling` (verbatim + record path) | `project.json` **+ the folder itself** (`mkdir` IS registration, s.5) · index entry in `org/projects/` · `DIRECTIVES.yaml` row (DERIVED, choice A) | none today -- hand-written JSON. **GAP: no `comp-register`.** | `to-pipeline-gate.py` L3: row exists · `dep_stage` in enum · `fabric` in `laptop\|site-z` (5 refusal conditions, `:176-215`) |
| **4** | `1.0.0_SA_CTO` | **PRD** | `PRD_HEADER` fenced json (project/directive/fabric/version/step/brief_ref/FWD range/status) · ENDPOINT · 1 arc · 2 purpose · 3 territory (OWNS / RELIES-ON / MUST-NOT-CHANGE) · 4 acceptance properties · 5 out of scope · 6 rulings that BIND · **7 SURFACE MANIFEST** (`outcome_ref` · `surface` · `claim` · `evidence` · `lane` · `verb` · `depends_on` · `acceptance` · `bound`) · change log | `prd/{PROJECT}_PRD.md` | `_PRD_TEMPLATE.md` @`75ead40079` (carries header + s.7 by construction) | limb 5: header block present, ENDPOINT title present, manifest heading present. ⚠ **an EMPTY manifest heading passes** (`~A` @`d019922d68`, PARTIAL) |
| **5** | `2.0.0_SA_COO` | **DECOMP** (the rectangle) | cells `{value, status, evidence}` born UNMEASURED · MECE check over the OWNS cell, bidirectional, denominator printed · ordering with the rulings that make an order a RULING not a preference · **`<preflight>`** (every lens: RUN + denominator/blindness, or DECLARED-NOT-APPLICABLE + reason at the SUBJECT grain) · what the decomp REFUSES to assume | `decompositions/{PROJECT}_DECOMP_<date>.md` + `comp-adversary` declaration alongside | `/atom-decomp` · the battery: `comp-blast` `comp-dataflow` `comp-schedule` `comp-iam` `comp-trigger` `comp-pipescript` `comp-denytest` (+ `comp-similar`, admitted @`0d272d257c`) · `comp-adversary compose <decomp>` · `comp-read --enumerate` for surface census | none at step 5. The preflight is CONSUMED by step 6 |
| **6** | `2.0.0_SA_COO` | **TASK ORDER** | header (to / by / issued / project / lane) · `<status>` · scope from ONE decomp cell · acceptance = the PRD property number, EXERCISED · `<preflight>` (3 enforced lenses minimum: `comp-schedule` `comp-iam` `comp-adversary`) · the step-7 trigger VERBATIM (*"Did I have to do something the TO did not say to do, or could I not do something the TO said to do?"*) · `decomp_ref` · surprise channel named | `task-orders/{PROJECT}.TO-<NAME>.md` | `safe-commit.sh -F <msgfile>` · `comp-to` (sets the per-session TO context) | ⛔ **THE ONLY GATE OF TEN.** `to-pipeline-gate.py`: L1 (no VALID instance -> no `complete` flip) · L2 (preflight dispositions for `PREFLIGHT_TOOLS`) · L3 (row/stage/fabric) · limb 5 (PRD conformance) |
| **7** | the worker lane | **DELIVERABLE** + **SURPRISE ROWS** | deliverable: proof-of-spec with evidence pins `file:line @ commit` · surprise row: `id` (`{PROJECT}-S{n}` / `{PROJECT}-Z-S{n}`) · `class` {OBSERVATION, BLOCKING} · `standing` {ARMED, INERT} · `spec_asserts` + `world_is` (BOTH required) · `outcome_ref` · `project` + `fabric` (schema, gate-required on NEW rows) | `deliverables/<name>.md` · `surprise-channel/investigations/INVESTIGATION_v1.md` (append-only rows; `.Z.` variant per fabric) | the lane's own comp-tools · `safe-commit.sh` | `surprise-row-gate.py` on NEW rows (shape only -- **nested enum/pattern/minLength/allOf NOT enforced**, `~A` P0) |
| **8** | `3.0.0_SA_CVO` | *(no artifact -- a NOTIFICATION)* | `[SURPRISE] <file>` events; read-only watermark; at-least-once; **its state file is NOT an oracle for "CVO read it"** | -- | `org/surprise_channel/surprise-watch.sh` (moves to `.tools/`; it is a tool, not a row) | none. A notifier never gates |
| **9** | `3.0.0_SA_CVO` | **DISPOSITION** (a field on the row) | enum {UNDER_INVESTIGATION, GRADUATED, DISMISSED_WITH_REASON, DECOMP_INVALIDATING} + the `obligation_resolution` orthogonal axis `~A` ruled for "the world overtook it" | the same investigation row | -- | none |
| **10** | `3.0.0_SA_CVO` | **REMEDIATION ROW** | `id == the graduated investigation id` · `route` {spec-error -> 6, decomp-invalidating -> 5, scope -> 2} · `loop_target` · `scope_change_kind` + real `FWD-n` or REQUIRED-NULL (FWD-NONE rejected) · `project` + `fabric` | `surprise-channel/remediations/REMEDIATION_v1.md` | -- | `surprise-row-gate.py:175-183` (`outcome_ref` required when `route=SCOPE_CHANGE`) |
| **any** | deploying lane | **DEPLOY-COMPLETION LEDGER ENTRY** | opened at start, closed at completion · `**Status:**` · stranded legs · the act's pre-registered read of results (*"PER-KEY MANIFEST STATUSES, never rc"*) | `ledger/<ts>_<act>.md` (today: `org/critical_paths/change_management/`) | `deploy_ledger.py open/check/close` · `record-terraform-deploy.sh` | `deploy_ledger.py check --red` every drive cycle (**crashes on non-ASCII under cp1252 -- fix pending**) |
| **any** | the building lane | **SUBSTRATE CARD** | 7 questions × 3 grains (PROCESS 1-2, ARTIFACT 3-4, TRUST 5-7) · every row carries its OWNER · verdict + named blocking defect | `cards/<resource>.card.json` | `substrate-card-check.py` (`BASIS_RANK` at `:126`) | `substrate-card-check.py` on the card |

**Seat artifacts that do NOT move into the tree** -- they are scoped to a SEAT, not a project:
session logs (`org/{tier}/{serial}/logs/`), handoffs, the inbox (`org/mcp/inbox/`), drive logs, the
seat README/prompt. **Law and doctrine do not move**: `CLAUDE.md`, `docs/doctrine/`, `org/XXX.md`,
`org/ref/`. **Cross-project registers do not move**: `DIRECTIVES.yaml`, `REGISTRY.md` (derived),
`.owned-paths.yaml`, `org/tier0/ledger/`.

---

## 3a. FORM -- a gate-read component is DATA, never prose (Andrew, ~19:5xZ)

> *"this is why we need structured/enumerated formatting, because none of this should be variable"*

**The rule:** every component in s.3 has a FORM, and **any component a gate READS must be STRUCTURED
DATA against a declared schema** -- a fenced JSON/YAML block, a JSON row, a JSON file. Markdown is the
prose AROUND the data and is never the carrier of anything a gate has to find. **A gate that parses
headings is a gate that has been handed prose, and every fence form, indent, and decoy heading is a
falsifier it did not need to have.**

**Measured on today's record -- the six open carrier falsifiers (`3.0.0_SA_CVO~A` @`df87b39f6e`)
cluster exactly on the prose-encoded, gate-read components:**

| gate-read component | FORM today | where today's defects sit |
|---|---|---|
| `PRD_HEADER` | fenced **JSON** | falsifiers 5-6 only -- path UNDER-CONSTRAINT, not structure recovery. The block itself is found without ambiguity |
| ENDPOINT section | markdown `##` heading + fenced FWD cards | **falsifiers 1, 2, 3** -- title in prose, in indented code, inside a `~~~` fence. Three ways to fake a heading |
| SURFACE MANIFEST | markdown `##` heading + a markdown TABLE | **falsifier 4** -- manifest only inside a `~~~` fence passes; and an EMPTY heading passed at `d019922d68`. A table cannot be schema-validated |
| TO `<preflight>` | pseudo-XML block, regex-parsed (`DISPOSITION_RE`) | the "NOT RUN is neither RUN nor DNA" class -- correct today, but a regex over prose is one rewording from wrong |
| TO `<status>` | free text | `/to-check` renders `[??]` on an absent field; 30 of 62 D2 status blocks carry BOTH open and closed words (CVO 2026-09-01) |
| surprise-channel ROW | **JSON** against a schema | `~A` P0: nested enum/pattern/minLength/allOf NOT enforced -- a SCHEMA-DEPTH gap, not a structure-recovery gap |
| `project.json` · `dep_stage` · `fabric` | **JSON** / enum | ZERO structure falsifiers all day. The off-enum defects (`BRIEF`, `TOS_CUT`) were VALUE defects, caught by the enum |

**The line is clean: every structure-recovery falsifier is on a prose-encoded component; every
JSON-encoded component's defects are value/schema-depth defects, which a schema catches.** The
repair bar `~A` set -- "one shared anchored heading parser outside all admitted fence forms" -- is the
BEST parser for prose. The rule above says: stop handing the gate prose.

**Consequence for the inventory -- three components change FORM under the tree:**

| component | today | under the tree |
|---|---|---|
| ENDPOINT | `## ENDPOINT` section | `prd/endpoint.json` -- `{ "FWD-1": {done_when, accept, source}, ... }` against `org/standards/endpoint.schema.json`; the PRD RENDERS it, the gate READS the file. FWD-n existence becomes CHECKABLE (the `^FWD-[0-9]+$` shape-only defect at `surprise-row-gate.py:53` closes for free) |
| SURFACE MANIFEST | `## 7. SURFACE MANIFEST` + table | `prd/manifest.json` -- rows against `org/standards/surface_manifest.schema.json` (the contract's 9 fields + the claim/evidence-rank binding). `comp-adversary compose` reads it directly; the "empty heading passes" class cannot exist |
| TO `<preflight>` + `<status>` | XML-ish + free text | `task-orders/{TO}.json` sidecar, or a fenced JSON block: `{ "status": <enum>, "preflight": { "comp-iam": {"disposition": "RUN", "denominator": "...", "blind": "..."} } }`. `DISPOSITION_RE` retires; the enum is the check |

**What stays prose, deliberately:** the arc (s.1), purpose (s.2), out-of-scope (s.5), rulings (s.6),
deliverable narrative, the `bound` column's reasoning. **Prose is for humans; no gate reads it; no
gate should.** The four-postulate record's intent axis (iii) holds: FORM is one axis -- *"does a gate
read this"* -- and the answer decides JSON vs markdown, nothing else.

⛔ **NOT PROPOSED AS A GATE.** This is a FORM rule for the three water-test projects going forward;
the existing gate limbs keep parsing prose until the JSON components exist to point them at. **The
first project to carry `endpoint.json` + `manifest.json` is the water test of this section.**

---

## 4. Components that exist today but have no home, exposed by the inventory

- **The ENDPOINT as a separate deliverable.** Today `ENDPOINT_FORWARD_*.md` lands in the CTO lane's
  `deliverables/`. Under the tree it is a SECTION of the PRD and nothing else -- one carrier.
- **`comp-adversary`'s declaration** (33 KB markdown; `--json` ruled emitting the L0a family's native
  form). It is decomp evidence and lands in `decompositions/` beside the rectangle.
- **The `fabric_ruling`** CTO~A added today (verbatim + record path on the row). Keep it: it is the
  provenance of the one field Andrew sets by hand.
- **`.comp-graph/.agent_context`** is NOT a project artifact and never was -- `comp-to` writes a
  per-session file. Nothing here changes that.

---

## 5. Naming and registration -- what step 3 becomes

**Today:** a seat hand-writes `org/projects/{CODE}.json`; MSTR edits `DIRECTIVES.yaml`; nothing
checks the two agree; `macro_code` is whatever the author typed (38 values, 12 live).

**Under the tree, registration IS `mkdir` + ONE commit:**

```
  org/missions/D8/MDPF/MDPF_COTREMEDIATION/project.json     <- the row, with fabric + dep_stage=REGISTERED
  org/projects/MDPF_COTREMEDIATION.json                      <- GENERATED index entry, home: + compared fields
  org/missions/DIRECTIVES.yaml                               <- DERIVED (or validated) projects: list
```

**Naming becomes: choose the path.** `{PROJECT_CODE}` = `{MACRO}_{NAME}`, where `{MACRO}` MUST be a
folder that exists under the directive, and the macro folder set is a **RATIFIED ENUM** carried in
`DIRECTIVES.yaml` per directive (Rule 24: MECE, same grain, one intent, state coherence). **A project
whose code's prefix is not a ratified macro cannot be registered** -- which is the L3-style refusal
this layer needs and does not have. That retires the 26 dead/malformed macro values at the moment of
migration rather than by a sweep.

⚠ **THE MACRO LAYER IS THE ONE PART OF ANDREW'S PROPOSAL THAT DOES NOT EXIST CLEANLY TODAY.** The
directive layer is sound (0 multi-membership). The project layer is sound (352/352 code==filename).
The macro layer has 38 values, 12 live, and includes fragments. **Before any folder is created the
macro enum has to be ratified per directive** -- that is a Rule 24 authoring act with a token census,
and it is the first prerequisite in s.8.

**`fabric` stays Andrew's** and stays a field on `project.json` (not encoded in the path): a fabric
is where work EXECUTES, a directive is what work is FOR, and today both D8 and its members moved
fabric without changing directive. Two axes, two carriers, on purpose.

---

## 5a. NAMING -- how MACRO and PROJECT codes are named and honored (Andrew's four questions)

Andrew, ~19:3xZ: *"how should MACRO codes and PROJECT codes be named and honored. if theres any benefit
from making them stable character amounts, how we define a macro versus a project, if projects accept
multiple PRDs, etc."* Answered from the census, not from taste.

### The grammar

```
  PROJECT_CODE  ::=  MACRO "_" NAME
  MACRO         ::=  [A-Z]{4}                 exactly four uppercase letters
  NAME          ::=  [A-Z0-9]{4,12}           four to twelve, no underscore inside
  regex         ::=  ^[A-Z]{4}_[A-Z0-9]{4,12}$
```

**Why exactly four for the macro -- it is the EXISTING convention, measured:** 31 of 38 macro codes are
exactly 4 uppercase letters (`ADVI NFRA MDPF OPAL ETFS YALP AUTH ADHC DATA MDLP MKOV SSCN` ...). **Every
one of the 7 violators is a malformed code** -- `GLOBALALARM` (11), `PLATFORM_OPS` (12),
`NFRA_VELOCITY` (13), `OPAL_TICKET` (11), `ASSETCLASS` (10), `PORTAL` (6), `BD` (2). So a stable
character count is not a new rule; it is the rule the estate already follows, never enforced, and the
drift IS the non-conforming set. Four letters gives 456,976 macros and stays scannable in a column.

**Why 4-12 for the name, no inner underscore:** the three test codes fit -- `GUARDRAIL` 9, `CLDGRPH` 7,
`COMPEFFICACY` 12. **The underscore is the SEPARATOR and nothing else.** Today 7 active codes carry a
second underscore (`D12_PHONE_OTP_ALL_AWS`, `OPAL_TAXSMA_PT2`, `PLATFORM_OPS_USERMGMT` ...) and every
one is ambiguous to split -- `to-pipeline-gate.py:184`'s walk-back exists BECAUSE of that ambiguity.
One underscore makes the walk-back unnecessary and the macro folder resolvable by string split alone.
Twelve is a ceiling, not a target: `COMPEFFICACY` sits at it, and a longer name costs a wider register
column, not a lost meaning.

**Honored HOW -- three refusals at registration, none of which exist today:**
1. code fails the regex -> REFUSE (the code IS the path, so a bad code is an un-mkdir-able path);
2. `MACRO` is not a ratified macro under that directive -> REFUSE (s.5);
3. `NAME` collides with an existing project under ANY directive -> REFUSE (codes are estate-unique,
   352/352 today; keep it).

### Macro vs project -- the definition, by what each one HAS

| | MACRO | PROJECT |
|---|---|---|
| **is** | a NAMESPACE for a product/system line that outlives any one arc | ONE arc with ONE defined outcome set (`FWD-1..n`) |
| **has** | a name, a folder per directive it appears in, a one-line charter | a row, a `fabric`, a `dep_stage`, a PRD, a DONE |
| **does not have** | an endpoint, a status, a DONE -- a macro never completes | siblings inside it -- a second arc is a second project |
| **repeats?** | YES across directives -- `NFRA` sits under D0 AND D11 today | NO -- one project, one directive, one path (0 of 38 violate) |
| **who ratifies** | Andrew, as the per-directive enum (Rule 24 record) | CTO at step 3, on the macro Andrew ratified |

**The one-sentence test:** *if it can be DONE, it is a project; if it can only be ABANDONED, it is a
macro.* `ADVI` will never read complete; `ADVI_PERFRP` will.

### Do projects accept multiple PRDs? -- NO, and the field that says otherwise is measuring something else

`prds[]` is a list today and `NFRA_CLDGRPH` carries SIX entries. Read them: **one step-4 PRD, one
step-1 brief, one step-2 endpoint record, one ancestor ruling, one CLOSED sibling, one gateway
contract.** That is not six PRDs; it is six artifact KINDS in a field named for one of them. Under the
tree each kind has its own home (`brief/`, the ENDPOINT inside `prd/`, ancestors and siblings as
`related:` on the row), so **`prds[]` collapses to ONE path: `prd/{PROJECT}_PRD.md`, versioned IN
PLACE** -- v0.1 -> v0.2 -> v0.3, which is exactly what `1.0.0_SA_CTO~A` did today in three hours.

**A project that needs a second PRD needs a second project.** The D12 precedent is the ruling in
practice: send-fix and SMS-OTP were split into SIBLINGS (`PLATFORM_OPS_USERMGMT` / `D12_PHONE_OTP_ALL_AWS`)
rather than one project carrying two arcs, and `2.0.0_SA_COO~Z` recorded the reason -- a clean
boundary off a complete arc. One arc, one outcome set, one PRD; the moment there are two DONEs there
are two projects.

### The three water-test codes under the grammar

```
  ETFS_GUARDRAIL      ETFS + GUARDRAIL (9)      conforms   -> org/missions/D8/ETFS/ETFS_GUARDRAIL/
  NFRA_CLDGRPH        NFRA + CLDGRPH (7)        conforms   -> org/missions/D0/NFRA/NFRA_CLDGRPH/
  NFRA_COMPEFFICACY   NFRA + COMPEFFICACY (12)  conforms   -> org/missions/D11/NFRA/NFRA_COMPEFFICACY/
                                                             NO ROW EXISTS YET -- register ask is
                                                             at 0.0.0_AB_MSTR (CVO 92622/92632)
```
All three conform without renaming. `NFRA` appears under two directives -- the namespace behaviour
defined above, not a defect.

---

## 6. Authority -- lanes re-keyed by artifact type

Today's 61 lanes answer *"whose directory"*. The tree needs *"whose artifact"*. The re-key, longest-match:

```
  **/prd/**                          ANY_CTO             (+ CTO~A etc. as today)
  **/decompositions/**               2.0.0_SA_COO (+ lanes)
  **/task-orders/**                  2.0.0_SA_COO (+ lanes)     <- step 6 is COO's and only COO's
  **/deliverables/**                 the ASSIGNED worker lane, resolved from the TO's `to:` field
  **/surprise-channel/investigations/**   the assigned worker + 3.0.0_SA_CVO
  **/surprise-channel/remediations/**     3.0.0_SA_CVO
  **/ledger/**                       the deploying lane (AE by rule 13) + CTO/COO co-sign
  **/cards/**                        the building lane
  **/project.json                    1.0.0_SA_CTO (row) -- and the DERIVED index/DIRECTIVES.yaml need NO lane, a generator writes them
  **/brief/**                        4.0.0_SA_CRO
```

**The one hard part:** `deliverables/` is owned by *whoever the TO assigned*, which is a value in a
file, not a path. `.owned-paths.yaml` cannot express that today. Two honest options, neither chosen
here: (i) the TO's `to:` field is read by `owned-paths-check.sh` (a new resolver, CTO's), or (ii)
`deliverables/{serial}/` sub-folders so the path carries the owner again. **(ii) is simpler and keeps
the gate a path gate**; it costs one more level.

---

## 7. What this does to the gates and tools -- the things that break on day one

| reader | reads today | must become |
|---|---|---|
| `to-pipeline-gate.py:184` L3 | `org/projects/<CODE>.json` + walk-back | reads the INDEX (choice B) -- unchanged path, generated content. **Walk-back `FOO_BAR_BAZ -> FOO_BAR` becomes UNSAFE** once macro folders exist: it would resolve a project to its MACRO. Retire the walk-back; the TO's `project:` header field carries the code. |
| `to-pipeline-gate.py` TO discovery | `org/**/task_orders/*.md` | `org/missions/**/task-orders/*.md` (note the hyphen -- pick ONE spelling estate-wide; today it is `task_orders`) |
| `surprise-row-gate.py` | `org/surprise_channel/**` | `org/missions/**/surprise-channel/{investigations,remediations}/**` |
| `surprise-watch.sh` | `org/surprise_channel/` watermark | the same glob; the watermark file moves to `.tools/state/` |
| `to-check.py`, `registry-check.py`, `fabric-check.py`, `/drive` step 2 | `org/projects/*.json` | the index, unchanged path |
| `comp-adversary` FILELINE_RE | any repo path | unchanged |
| `.owned-paths.yaml` + `owned-paths-check.sh` | seat-dir globs | s.6 |
| `DIRECTIVES.yaml` `projects:` | hand-edited (MSTR lane) | DERIVED by a generator, or VALIDATED on commit against the tree |
| `missions.yaml` attach globs | `org/projects/NFRA_GRAPH*` | RETIRED -- the tree is the attach |

⛔ **`task_orders` vs `task-orders`.** Andrew wrote `/task-orders`; the estate has `task_orders/` in 34+
seat dirs and in `to-pipeline-gate.py`'s glob. **Pick one before migration; a mixed estate is a gate
that reads half the TOs.** This spec uses Andrew's hyphen and names the cost.

---

## 8. PROSPECTIVE ONLY -- the three water tests, and nothing retroactive

Andrew, verbatim: *"we dont need to do any of this retroactively, this would all be for prospective
work, the test project codes here that we'd want to focus on are ETFS_GUARDRAIL NFRA_CLDGRPH
NFRA_COMPEFFICACY."*

**So there is no migration.** The 350 existing rows stay exactly where they are. `org/projects/` stays
the register for them. `DIRECTIVES.yaml` keeps its hand-edited lists for them. Nothing closed or
complete is touched. **The tree starts EMPTY and grows only with new projects** -- the three named are
the water tests, in the order their state permits:

| project | state today | what it exercises | first act |
|---|---|---|---|
| `NFRA_CLDGRPH` | registered, `fabric: laptop`, PRD v0.3 conformant, decomp done, **all 3 tool-side blocks closed** (limb 5, fabric, comp-adversary RC5 GREEN @`5dbca15a4a`) -- held at L5 only by Andrew's water-test word | **the full L1-L5 path** with every artifact already in hand: brief, PRD w/ header + s.7, decomp, adversary declaration | `mkdir org/missions/D0/NFRA/NFRA_CLDGRPH/` and move ITS OWN artifacts in -- the only "migration" there is, one project's, from this session |
| `ETFS_GUARDRAIL` | registered, `fabric: laptop`, PRD w/ s.7, decomp done, RED/HOLD 1-4+7 | **a project already mid-loop** -- whether the tree can adopt work in flight without breaking gates that already passed on it | same, after CLDGRPH proves the mkdir + gate path |
| `NFRA_COMPEFFICACY` | **NO ROW YET**; PRD drafted @`51c63e23a9`; register ask at MSTR | **registration FROM SCRATCH under the tree** -- step 3 as `mkdir` + `project.json` + fabric in ONE commit (s.5). The only one of the three that tests the NEW step 3 rather than adopting an old one | register it INTO the tree, never into flat `org/projects/` |

⛔ **THE DUAL-REGISTER PERIOD IS REAL AND MUST BE NAMED, NOT HIDDEN.** While old projects live in
`org/projects/*.json` and new ones live in `org/missions/**/project.json`, **every reader in s.7 must
read BOTH** or it is blind to one population. That is the cost of "prospective only", it is the right
trade, and it is bounded: it ends when the last flat-registered project closes. The index (choice B)
is what makes it cheap -- the generator emits a flat index entry for every tree project, so readers
that only know `org/projects/` keep working unchanged, and **the only reader that must learn the tree
is the generator.**

**Prerequisites, in order -- they are about the TREE, not about moving anything:**
1. **Ratify the macro enum** for the three directives in play -- D0, D8, D11 -- with `NFRA` and `ETFS`
   as the first entries. Three directives, two macros. Rule 24 record + census.
2. **Pick `task-orders` vs `task_orders`.** One word.
3. **The index generator + `DIRECTIVES.yaml` derive/validate**, RED-FIRST: run against today's flat
   register it must reproduce today's 38 `projects:` entries exactly, 0 diff, before it writes anything.
4. **Re-key lanes for `org/missions/**` ONLY** -- old seat-dir lanes untouched, no incumbent displaced.
   Exercised both directions before landing (CTO's 15-row-matrix discipline from today).
5. **Repoint each gate to read BOTH roots** (s.7), each with a falsifier THROUGH THE REAL HARNESS -- the
   5 s hook timeout and the 90 s collection ceiling were both invisible in isolation today.
6. `NFRA_CLDGRPH` in. Then `ETFS_GUARDRAIL`. Then `NFRA_COMPEFFICACY` registered fresh.
7. **No fourth project enters the tree until all three have carried a TO through step 6** -- the
   L1-L5 water-test discipline Andrew set, applied to the tree itself.

---

## 9. Rule 24 -- the four-postulate record for THIS schema

- **(i) MECE over a declared domain.** Domain = *every artifact the canonical loop produces at any
  step, plus the two cross-step artifacts (ledger, card)*. s.3 enumerates 12 artifact kinds over 10
  steps + 2; every kind has exactly ONE `home:`; the uncovered-member hunt found the ENDPOINT
  (currently a sibling file) and the adversary declaration (currently in scratch) and gave each one
  home. **Not covered, stated:** ad-hoc deliverables with no TO (CTO ruled today that lane-owned
  maintenance is not a project -- those stay in seat dirs, by that ruling).
- **(ii) Same grain.** Every level of the tree is a PARTITION: directive partitions the estate, macro
  partitions a directive, project partitions a macro, artifact-kind partitions a project. No level
  mixes a partition with a tag.
- **(iii) Intent coherence.** The tree answers *"where does this artifact live and who may author
  it"* -- one axis. It is NOT a status tracker (status lives in `project.json`), NOT a schedule, NOT
  a fabric map (fabric is a field, s.5).
- **(iv) State coherence.** A directive move = `git mv` (path changes). A fabric change = a field
  edit (path does not). A status change = a field edit. **No remedy moves a project between MACROS**
  -- a macro is a naming ratification, and re-macro-ing a project is a RENAME with a new code, not a
  move.

**Word-boundary token census, run not asserted:** `org/missions/` = 1 existing occupant
(`DIRECTIVES.yaml`); `D0`..`D12` = 13, all in that file; `task-orders` (hyphen) = 0 hits in `.tools/`
and `org/` vs `task_orders` (underscore) = the estate convention. The hyphen is NEW vocabulary and
s.7 flags it as a decision, not a default.

---

## 10. Open for Andrew -- the calls this spec does not make

1. **`task-orders` or `task_orders`.** One word; it decides a gate glob.
2. **Does `project.json` move into the folder (choice B, with a generated index), or stay flat with a
   `home:` field only?** B is recommended; the alternative is cheaper on day one and drifts on day two.
3. **`deliverables/` ownership: read the TO's `to:` field (new resolver), or `deliverables/{serial}/`
   sub-folders (path carries owner)?** (ii) recommended.
4. **Is the macro layer worth its cost?** It is the one layer that is not clean today and the one
   Andrew called "hazy". The directive->project tree is sound WITHOUT it. If the macro is kept it
   must be a ratified enum per directive; if it is dropped, `{MACRO}_` stays a naming prefix only and
   the tree is two levels. **Recommendation: keep it, ratify it, because 12 live macros over 13
   directives is exactly the grouping a human navigates by** -- but it is the call with the most
   cleanup behind it.
