# NFRA_COMPEFFICACY -- step-5 atom-decomp (COO) -- v0.1, the tree's first decomposition

**Author:** `2.0.0_SA_COO` · 2026-09-03 ~00:4xZ · **Step 5 of the canonical loop. NO TO IS CUT BY THIS FILE.**
**Home:** `org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md` (lane TREE_COO; versioned in place).
**PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` **v0.3 @`264bc9fa92`** (`1.0.0_SA_CTO`; v0.2 @`e906c6f156` was read in full for v0.1 of this file, and v0.3's diff -- 15/-7 lines -- reconciled at 00:4xZ: the AC reading rule (NOTE A/B, already adopted below), the result-file home = the tree's `deliverables/<serial>/`, row T-16 CLEARED, and **G-4's `outcome_ref` FWD-6 -> FWD-9** (applied to CE-g-4)) -- FWD-1..FWD-9, AC-1..AC-7, rulings R-1..R-7, s.7 manifest T-1..T-24 + G-1..G-4.
**Authority:** Andrew GO at the CTO terminal ~23:1xZ (*"lets take compefficacy through the whole canonical process"*) on the pre-notice @`a258e3060f`; the tree set reviewed @`580c4f72a2`.
**Reads that ground this file:** the PRD in full (581 lines, 59 sections, `comp-read --for` then every section named here read at full width); the proof-of-spec gate's `CELL_ID_RE` (`.tools/proof-of-spec-check.py:361`) -- every cell id below was tested against it before writing (18 ids: 15 MATCH, and `T-16` / `G-4` / `S1` do NOT, which is why the manifest ids are MIRRORED rather than reused); CVO's L4 read (92846: no wrong row in the re-pointing; NOTE A / NOTE B adopted below).

⛔ **ONE ID SPACE, STATED MECHANICALLY.** The PRD's s.7 manifest ids (`T-n`, `G-n`) are the gate's `outcome_ref`
rows; they do not match the proof-of-spec cell regex. **`CE-t-n` IS manifest row `T-n`; `CE-g-n` IS `G-n`** -- same
number, same surface, same lane; a TO's `<owned_cells>` cites the `CE-` form and the reader resolves the `T-`/`G-` row
by the number alone. The ten cross-cutting cells (`CE-enum/sch/disc/tp/grd/q/mrq/pass/org`) exist ONLY here; whether
`1.0.0_SA_CTO` lifts them into s.7 at v0.3 is CTO's call (the CLDGRPH precedent lifted the decomp verbatim).

---

## 1. The rectangle

**Domain (postulate i):** the PRD s.3 **OWNS** cell, six items, plus ONE member Andrew added by ruling (G-4, "Both
recs accepted" ~23:0xZ at the CTO terminal: *"carry a row 'Codex-runtime rail: design' in that project"*) -- stated as
an extension of the domain by his word, not smuggled in.

```
  OWNS item                                                     cells
  1 the per-tool result SCHEMA (s.4)                            CE-sch-1 · CE-disc-2 (the 4.3 spellings the schema binds by)
  2 the ENUMERATION (s.7) and each row's DISPOSITION            CE-enum-1 · CE-t-1..CE-t-24 · CE-grd-1 · CE-q-1 · CE-mrq-1 · CE-pass-1
  3 the GRADING of every CloudComp deliverable                  every CE-t / CE-g cell's DONE test (CVO's grade IS the flip) · CE-grd-1 · CE-org-1 (FWD-9 leg of every grade)
  4 the DISCLOSURE CONTRACT every CLEARED tool must meet        CE-disc-1 · CE-disc-2
  5 the TIMEOUT / PAGINATION POLICY as a spec (s.4.4)           CE-tp-1 · CE-tp-2
  6 the GLOBGRPH BRIEF WORKSTREAM at the agent-facing surface   CE-g-1 · CE-g-2 · CE-g-3 (+ CE-t-12, CE-t-17, CE-t-22 touch it)
  + Andrew's added member (ruling 2a)                           CE-g-4
  DENOMINATOR: 6 of 6 OWNS items covered, 0 uncovered; 39 cells, 39 of 39 map to an OWNS item or the added member;
  RELIES-ON appears only in depends_on / bound; MUST-NOT-CHANGE appears only as a bound (KUZUSPLIT NEVER-full, GLOBGRPH derive, CTO ruling 3, truthful non-application).
```

**Cell vocabulary (Rule 24, with a NOT-EVALUATED value so non-evaluation is never a verdict):**
- `value` = the row's disposition target: **CLEARED · RETIRED · DOES-NOT-EXIST · CARRIED** (PRD s.2, no fifth state) or, for a cross-cutting cell, the deliverable/decision it names.
- `status` = **DONE** (graded by the certifier, or ruled) · **IN-FLIGHT** (a deliverable or fix landed, grade pending) · **OPEN** (not started) · **HELD** (blocked on a named decision, owner stated) · **NOT-EVALUATED** (this decomp did not measure it and says so).
- **State coherence (iv):** a CVO grade moves `status`; Andrew's or the owner's ruling moves `value` for RETIRED/CARRIED; CTO's ratification moves CE-disc-2; MSTR's push moves CE-org-1. **No single act moves two cells.**
- **NOTE A / NOTE B (CVO 92846) adopted:** a cell whose verb is a 4.3 grade closes on **AC-2** (four rejectable answer-states, planted not asserted), not on a disclosure sentence; a G cell closes on **AC-7** (answer from a bounded-age graph), not on FWD-7's "has an owner".

### 1a. The tool rows -- `CE-t-n` IS `T-n` (24 of 24; surface, lane and bound as the manifest states them; here the STATE)

| cell | = | outcome_ref (+AC) | value target | status now | evidence now (vintage) | lane | depends_on | closes on |
|---|---|---|---|---|---|---|---|---|
| CE-t-1 | T-1 comp-find | FWD-2,3,4,9 + AC-2 | CLEARED | **IN-FLIGHT** -- battery landed (unit 3b @`1e6206a267`), logging unit 1 @`f34122edfb` ON origin; **s.4 deliverable NOT yet filed**; sequenced as CloudComp's next per-tool pass (COO 92822 row 3) | s.7 T-1; CVO 92769/92792 | CloudComp | -- | s.4 deliverable graded + **Rule T**: 600 s internal > 120 s outer, reached denominator at expiry (CE-tp-1's first target) |
| CE-t-2 | T-2 comp-read | FWD-2,3,4,9 + AC-2 | CLEARED | **IN-FLIGHT** -- unit 1 ON origin, shebang routing @`8ed23144cb`, battery 8/8; s.4 deliverable not filed; `--enumerate` writes no rail row (finding, not this cell's fix) | s.7 T-2 | CloudComp | CE-t-1 (sequenced after) | s.4 deliverable graded + Rule T |
| CE-t-3 | T-3 comp-which | FWD-2,3,4 + AC-2 | CLEARED | OPEN | s.7 T-3 (520 + 9,643 runs) | CloudComp | CE-t-2 | the NOFIT-POSTERIOR path graded as a 4.3 case |
| CE-t-4 | T-4 comp-hud | FWD-2,4 | DOES-NOT-EXIST | **DONE** -- recorded in s.7 by CVO (the HUD is a hook, CloudComp's, OUT) | s.7 T-4 | CVO | -- | recorded, never dropped (AC-1) |
| CE-t-5 | T-5 comp-schedule | FWD-2,3,4 | CLEARED | OPEN -- audit only; NOT-DECIDABLE is a designed result; **no remediation on this run's evidence** | s.7 T-5; PRD s.5 | CloudComp | CE-disc-2 (its spelling is the adopted one) | graded; "ARNs absent BY DESIGN" recorded, not fixed |
| CE-t-6 | T-6 comp-blast | FWD-2,3,4 + AC-2 | CLEARED | OPEN | s.7 T-6 (167 runs, no timeout) | CloudComp | CE-t-19 | subject-existence + graph vintage + node denominator; NOT-FOUND != zero radius |
| CE-t-7 | T-7 comp-dataflow | FWD-2,3,4 + AC-2 | CLEARED | OPEN | s.7 T-7 (11 runs) | CloudComp | -- | 4/4 honest-unresolved PRESERVED; unresolved print enriched; never guesses through deploy-time config |
| CE-t-8 | T-8 comp-iam | FWD-2,3,4 + AC-2 | CLEARED | OPEN | s.7 T-8 (113 runs) | CloudComp | -- | effective-deny three-state; "no parsed deny" is never "allowed" |
| CE-t-9 | T-9 comp-trigger | FWD-2,3,4 + AC-2 | CLEARED | OPEN | s.7 T-9 (80 runs; blind to S3 notifications -- the CLDGRPH decomp's S1 instrument gap) | CloudComp | -- | scope declared in header OR S3-notification backend via existing machinery; existing machinery checked FIRST |
| CE-t-10 | T-10 comp-pipescript | FWD-2,3,4 | CLEARED | OPEN -- F9 gate GREEN @`4a6f564c6f` is the GATE, the tool itself untouched | s.7 T-10 (571 runs) | CloudComp | -- | shim self-identification; ETFS NOT added to the registry on one preflight |
| CE-t-11 | T-11 comp-denytest | FWD-2,3,4 | CLEARED (audit) / RETIRE-candidate | OPEN -- audit; zero population without an IAM change is CORRECT | s.7 T-11 (2 runs/30d) | CloudComp | -- | graded; RETIRE-candidate on usage SURFACED to Andrew, never acted here |
| CE-t-12 | T-12 comp-similar | FWD-2,3,4,7,9 + AC-2 | CLEARED | **IN-FLIGHT** -- D1-D3 fixed @`b8a73cc064` ON origin (vintage/disclosure half); s.4 deliverable owed; **DEPLOYED != COMMITTED**: `summary_corpus.py` baked into the globgrph derive IMAGE with PRE-fix bytes (owner `0.7.0_AE_CloudOps`) -- carried to CE-g-* , not this cell's fix | s.7 T-12; CloudComp 92718 | CloudComp | -- | s.4 deliverable graded; the image finding carried with its owner named |
| CE-t-13 | T-13 comp-dups | FWD-2,4,5,8 | RETIRED / CLEARED | **HELD at 1.0.0_SA_CTO** -- R-5: separate engine by CTO ruling 3; 0 runs ever; disposition is CTO's | s.7 T-13 | CTO | -- | CTO's disposition recorded, with the replacement named if RETIRED |
| CE-t-14 | T-14 comp-drift | FWD-2,4,5,8 | CLEARED | OPEN | s.7 T-14 (1 run/30d) | CloudComp | -- | graded; overlap with comp-similar recorded as BY NAME ONLY |
| CE-t-15 | T-15 comp-legacy | FWD-2,4 | DOES-NOT-EXIST | **DONE** -- 0 of 106 entrypoints; recorded | s.7 T-15 | CVO | -- | recorded, never dropped |
| CE-t-16 | T-16 comp-adversary | FWD-2,3,4,9 + AC-2 | CLEARED | **DONE** -- CLEARED by CVO @`bbba0db0e9` 00:2xZ (92843): identity by engine, 4.2 present, 4.3 four states in the tool's voice, 4.4 ceiling exercised + deferred bucket visible, 4.5 passcraft 8/8, 4.6 two grains. **Push state of `bbba0db0e9`: UNREAD at grade** -> the FWD-9 leg rides CE-org-1 | 92843; CloudComp 92836 | CloudComp | -- | closed; FWD-9 exercised when used from another seat: **this decomp's `comp-adversary compose` run (s.3) IS that use** |
| CE-t-17 | T-17 comp-estate | FWD-2,3,4,7 | CLEARED / CARRIED | OPEN -- his word *"need to lock in C(N) ontology"* = `NFRA_C3MATERIALIZE` (D11 sibling) | s.7 T-17 (281 runs) | CloudComp | CE-t-22; NFRA_C3MATERIALIZE (RELIES-ON) | graded; if C(N) is the blocker the value is CARRIED with C3MATERIALIZE named |
| CE-t-18 | T-18 comp-pulse | FWD-2,3,4 | CLEARED | OPEN -- it is a HOOK (8,359 of 8,364 runs = `diff` from the commit hook); re-measure after unit 1 | s.7 T-18 | CloudComp | CE-t-1, CE-t-2 | graded with the hook nature stated in purpose_1line |
| CE-t-19 | T-19 comp-trace | FWD-4,5,8 | RETIRED | OPEN -- **R-4 RULED, condition MET** (strict subset of blast, `cli.py:1478-1530`); executable any time; 45 callers to redirect (CloudOps~F 18, ~D 14, CVO 11) | s.7 T-19 | CloudComp | -- (CE-t-6 depends on THIS) | retired THROUGH the estate's own alias mechanism (the T-22 pattern: declared successor, callers told first, executable last); his ruling cited |
| CE-t-20 | T-20 comp-heat | FWD-2,3,4 | CLEARED | OPEN -- 0 CLI runs; library consumer only; invoked by nothing | s.7 T-20 | CloudComp | -- | graded; the daily-report wiring is `@09355b6d93`'s, not this cell's |
| CE-t-21 | T-21 comp-system | FWD-2,3,4 | CLEARED | OPEN -- his ask "understand what this one does" is answered by purpose_1line + 4.2 | s.7 T-21 (584 runs) | CloudComp | -- | graded; the unit-1 regen recorded as a side effect |
| CE-t-22 | T-22 comp-kuzu (+ retired -inc/-full) | FWD-4,5,7,8 | RETIRED (wrappers) / CLEARED (engine) | **IN-FLIGHT** -- code + registry half LANDED @`dffbee781c`, CLEARED by exercise (CVO 92769); **PRD half (KUZUSPLIT PRD P1/P3) at 1.0.0_SA_CTO**; the two dated briefs are records, never rewritten | s.7 T-22; R-3 RULED (a) 18:12Z | CloudComp (done) + CTO (open) | -- | CTO's PRD amendment lands; NEVER-full on `--mode inc` in every carrier (MUST-NOT-CHANGE bound) |
| CE-t-23 | T-23 comp-cache | FWD-2,3,4 | CLEARED | OPEN | s.7 T-23 (35 runs) | CloudComp | -- | graded; "not comp-platinum" recorded |
| CE-t-24 | T-24 comp-platinum | FWD-2,3,4 | CLEARED | OPEN -- his question ("what coverage universe?") answered by corpus_or_backend + denominator | s.7 T-24 (7 runs) | CloudComp | CE-t-10 | graded |

### 1b. The globgrph workstream + the added member -- `CE-g-n` IS `G-n`

| cell | = | outcome_ref (+AC) | value target | status now | evidence now | lane | depends_on | closes on |
|---|---|---|---|---|---|---|---|---|
| CE-g-1 | G-1 `comp-graph status` freshness surface | FWD-7 + AC-7 | CLEARED (fixed) | **HELD -- re-homes to the comp-graph owner (NFRA_GRAPHS lane)**; reports `kuzu_db 81d` + `stitch_graph 38d`, canonical is `kuzu_nessie_db` | s.7 G-1 (CRO F6, attributed, not re-measured) | NFRA_GRAPHS owner | -- | reports `kuzu_nessie_db` with its `built:` vintage (AC-7) |
| CE-g-2 | G-2 stale-served path bound | FWD-7 + AC-7 | CLEARED (bounded or disclosed) | OPEN -- T-22's code half landed, so this is UNBLOCKED; 16 `inc-served-labeled-stale` events ~34 h behind (CRO F5) | s.7 G-2 | CloudComp | CE-t-22 (met) | the age is bounded by a schedule OR stated on the answer -- never silent (AC-7) |
| CE-g-3 | G-3 `kuzu_nessie_load` key asymmetry | FWD-7 + AC-7 | CLEARED (carried or fixed, never silently ported) | OPEN -- carded QUALIFIED @`5da9e7fffc` (F4) | s.7 G-3 | CloudComp | CE-t-22 (met) | carried with the card cited, or fixed with a control at `:150` vs `:184` |
| CE-g-4 | G-4 Codex-runtime rail: design | FWD-9 (v0.3; was FWD-6 at v0.2) | a DESIGN deliverable (never a gate on any seat's word) | OPEN -- Andrew ruling 2(a); 2(b) EFFECTIVE NOW (no comp-tool-grounded adjudication from a Codex seat until a rail exists) | s.7 G-4; `FINDING_COMPRAIL_DENY_NOT_ENFORCED_20260902.md` add. 2 | CVO drives, CloudComp executes | CE-t-1, CE-t-2 | a rail EXERCISED at a Codex seat: a DENY observed as the BODY NOT EXECUTING (a rail-log row is not a block) |

### 1c. The cross-cutting cells -- decomp-only ids (not in s.7 until CTO lifts them)

| cell | OWNS | outcome_ref | the deliverable / decision | status now | lane | depends_on | closes on |
|---|---|---|---|---|---|---|---|
| CE-enum-1 | 2 | FWD-1 | the list: 22 named tools + 3 roll-up questions = 25 names -> 24 rows, 0 uncovered, both directions RUN (PRD s.7 MECE block) | **DONE** (APPLIED in the PRD @`e906c6f156`; CVO's census, CTO's landing) | CVO / CTO | -- | Andrew can find every name (FWD-1 ACCEPT) |
| CE-sch-1 | 1 | FWD-2 | the per-tool result schema s.4.1-4.7 with its Rule 24 record | **DONE** -- APPLIED in the PRD; **EXERCISED** by T-16's deliverable (31 of 31 required fields, graded CONFORMING) -- the shape survived one reading | CVO | -- | met (FWD-2 DONE WHEN); every further deliverable re-exercises it |
| CE-disc-1 | 4 | FWD-3 | the disclosure contract s.4.2 (engine path, corpus/backend, vintage, denominator, resolved/unresolved, blind_spots, pagination, timeout) | **DONE** as contract; exercised on T-16 | CVO | -- | per-tool via each CE-t cell's 4.2 grade |
| CE-disc-2 | 1, 4 | FWD-3 + AC-2 | **the 4.3 answer-state SPELLINGS ratified** -- adopt `NOT-DECIDABLE` (comp-schedule's), reconcile the `NOT_APPLICABLE` / `DECLARED-NOT-APPLICABLE` split, mint the two carrier-less states (`SUBJECT_ABSENT_FROM_CORPUS`, `PRESENT_WITH_ZERO_RESULTS`) reconciled with comp-find's `OUT-OF-CORPUS` prose; the 4.7 record + census exist | **OPEN at 1.0.0_SA_CTO (the gate)** -- *"until the spellings are ratified, 4.3 binds deliverables by reading, not code by enforcement"* (PRD s.4.7) | CTO ratifies; CVO authored | -- | a DECIDE-FIRST cell: every 4.3 grade before it closes is a grade BY READING and is re-read once against the ratified enum |
| CE-tp-1 | 5 | FWD-2, FWD-4 + AC-4 | **Rule T (work)**: a tool never exceeds a ceiling it was not told; prints the reached denominator with a resume cursor at expiry -- the spec exists in s.4.4; the BUDGET FORM (how a caller's ceiling reaches the tool) is not yet decided; first target T-1 (600 s > 120 s) | OPEN -- "carried project-wide, same standing as T-1/T-2/T-16 alike" (CVO 92843) | CVO (spec) + CloudComp (first application on T-1) | -- | a DECIDE-FIRST cell: the form ratified, then T-1 exercised past its ceiling with the disclosure distinguishable from a clean empty (AC-4) |
| CE-tp-2 | 5 | FWD-2 + AC-4 | **Rule P (pagination)**: PAGE i of N + TRUE TOTAL on every page; 5 of 106 paginate today; comp-find / comp-read / comp-which are the references | **DONE** as spec (s.4.4); EXERCISED by T-1's battery arm A5 (PAGE contract) | CVO | -- | per-tool via each CE-t cell where pagination exists |
| CE-grd-1 | 2, 3 | FWD-4 | **the dispositions carrier** -- where "cleared / retired-or-merged / short list, never 'we have not got to it'" is READ: today the s.7 `evidence` column, prose, re-versioned by CTO on each CVO grade (L4 did exactly that for T-16). DECISION: **s.7 stays the ONE carrier** (a sibling ledger is a second carrier that drifts); each grade = a PRD version bump of the row by CTO | **DONE as a decision (mine, here); the READ is exercised at every grade** | CVO grades -> CTO versions | -- | FWD-4 DONE WHEN: the last tool's state read by Andrew -- i.e. when every CE-t cell reads DONE |
| CE-q-1 | 2 | FWD-5 | **his seven questions answered in writing**, each pointing at the row that answers it: platinum's universe (T-24), what system does (T-21), cache vs platinum (T-23), is trace just dataflow (T-19: it is a subset of BLAST, not dataflow), is denytest needed (T-11), does similar supplant the three roll-ups (T-12/T-13/T-14: NO -- dups is its own engine by CTO ruling 3, drift is propagation not function), what pulse/heat do and whether they work (T-18/T-20) | OPEN -- fed by the rows; the written-answers section lands in the PRD (CTO versions) from CVO's per-row grades | CVO authors, CTO lands | CE-t-11,12,13,14,18,19,20,21,23,24 | each answer says what the thing actually does, and "is this just X?" gets yes/no and why (FWD-5 ACCEPT); each disputable by Andrew |
| CE-mrq-1 | 2 | FWD-8 | **the marquis short list**: the EVIDENCE PACK from s.7 (usage at two grains, overlap, disposition) -> a DRAFT proposal for his word (CVO announced it 92759 item 4) -> Andrew ratifies -> a seat starts from it | **IN-FLIGHT at CVO (the draft)**; the DECISION is Andrew's and is not made here (PRD s.5, "not cut, deliberately") | CVO drafts; Andrew rules | CE-t-* (usage evidence) | FWD-8 DONE WHEN EXERCISED: a seat has started a piece of work from the ratified list |
| CE-pass-1 | 2 | FWD-6 | **the passcraft findings used up**: per tool, s.4.5's 8 moves run and the 12 shapes hunted (in each deliverable); the ROLL-UP -- every finding "fixed" or "not fixing, and here is why", read by someone other than the fixer | OPEN -- T-16's leg is 8/8 (one tool); the roll-up waits on the rows | CloudComp (per tool), CVO (roll-up) | every CE-t cell | FWD-6 DONE WHEN EXERCISED: the last finding's disposition read by a non-fixer |
| CE-org-1 | 3 | FWD-9 + AC-6 | **CLEARED is ON ORIGIN and behaves as cleared from another seat/machine**: every CLEARED commit measured `is-ancestor` of origin/CLOUD (never claimed), and one use from a seat other than the fixer's | OPEN -- the integrator push is `0.0.0_AB_MSTR`'s (LD-0367); T-16's `bbba0db0e9` push state UNREAD at grade; the other-seat use is EXERCISED for T-16 by this decomp's compose run (s.3) | MSTR (push) + CVO/COO (the other-seat exercise) | every CE-t cell that reads DONE | a CLEARED status is never granted on a LOCAL commit (AC-6); the push is the act, the is-ancestor read is the evidence |

---

## 2. The arc as an ordering -- CVO~A's default (PRD s.8) adopted, with today's state applied

```
  STAGE 0  DECIDE / RATIFY FIRST -- none is tool work; each changes how the rows are graded
           CE-disc-2  the 4.3 spellings (CTO gate)          -- every 4.3 grade before it is BY READING, re-read once after
           CE-tp-1    Rule T's budget form (CVO)            -- T-1 is its first target; grading T-1's 4.4 without it is a grade against prose
           CE-org-1   the push cadence for CLEARED commits  -- MSTR; a CLEARED on a LOCAL commit is not CLEARED (AC-6)
        |
        v
  STAGE 1  THE RAIL PAIR + THE ROUTER (highest traffic, Rule 21)          CE-t-1 -> CE-t-2 -> CE-t-3
        |                                                               (T-16 is DONE; PRD s.8 item (1) discharged)
        v
  STAGE 2  THE 4.3 ANSWER-STATE FIXES (each closes on AC-2)             CE-t-8 (deny mode) -> CE-t-6 (subject existence; needs CE-t-19 first)
        |                                                               -> CE-t-9 (trigger scope) -> CE-t-7 (unresolved diagnostics)
        v
  STAGE 3  THE REMAINING AUDITS + the shim self-identification sweep    CE-t-5, 10, 11, 12, 14, 17, 18, 20, 21, 23, 24
        |
        v
  STAGE 4  THE CROSS-CUTTING CLOSES                                     CE-q-1 (the seven answers) · CE-pass-1 (the roll-up)
                                                                        · CE-mrq-1 (Andrew's decision on the evidence) · CE-grd-1 reads DONE

  ANY TIME   CE-t-19 (retire trace: RULED, condition met -- callers told first, the T-22 alias pattern)
             CE-t-13 (CTO disposes dups) · CE-t-4 / CE-t-15 (DONE, recorded)
  PARALLEL   CE-t-22 PRD half (CTO) · CE-g-2, CE-g-3 (CloudComp; unblocked now that T-22's code half landed)
             CE-g-1 (re-homes; its owner's queue) · CE-g-4 (CVO design; after CE-t-1 / CE-t-2)
```

⛔ **THE ONE ORDERING THAT IS A RULING, NOT A PREFERENCE:** CE-t-6 (blast) after CE-t-19 (trace retired INTO blast,
R-4 condition met) -- auditing blast before trace is folded in grades a surface that is about to change.
⭐ **AND STAGE 0 SITS FIRST DELIBERATELY** (measure/decide before build, the CLDGRPH lesson): a per-tool 4.3 grade
issued before CE-disc-2 is a grade against unratified spellings, and a 4.4 grade before CE-tp-1 is a grade against
prose. Neither is wrong to issue -- the PRD says they bind by reading -- but each is re-read once, and the decomp says
so here rather than discovering it at row 20.

---

## 3. `<preflight>` -- what this decomp ran, and what it refused to run

```
<preflight>
comp-read --for + full-width section reads: RUN on the PRD @e906c6f156 -- 581 lines / 59 sections;
  every section cited here read in full; the UNREAD ledger's remaining sections are the arc prose and
  4.3-4.5 method text, read at width 300 (not skipped).
comp-read --enumerate: RUN on .tools/proof-of-spec-check.py for CELL_ID_RE (21 hits) -> the id
  mapping in the header; 18 candidate ids tested by regex before writing: 15 MATCH, 3 do NOT.
comp-adversary compose: RUN on THIS file after writing (result line recorded in the commit message and
  in s.5) -- comp-adversary is CLEARED @bbba0db0e9 and this run from a seat that did not fix it is the
  FWD-9 "used from another seat" exercise for CE-t-16.
missions-tree-index check: RUN before the commit (and by the R-i pre-commit hook on this path).
comp-find · comp-blast · comp-dataflow · comp-iam · comp-trigger · comp-pipescript · comp-denytest:
  NOT RUN -- the subject of this project IS those tools; running them on themselves at step 5 would
  produce the self-report the PRD forbids taking (s.4.1, "the wrong-object trap"). Each is exercised
  at its own row by the executor and graded by the certifier.
</preflight>
```

---

## 4. What this decomp REFUSES to assume

- **No tool's status is taken from its own output or its fixer's report.** Every DONE above cites the CERTIFIER's grade (T-16: CVO 92843). Every IN-FLIGHT names what is still owed.
- **"runs" are TOOL-INVOCATION counts under R-7**, sound as usage, never a seat-coverage claim. T-22's third wrapper count is `?` in the PRD and stays `?` here.
- **G-1..G-3 are CARRIED from CRO's brief, attributed, not re-measured** (agreement is not corroboration when one artifact inherited the claim).
- **CE-t-16's FWD-9 leg is NOT closed by the grade**: `bbba0db0e9`'s push state was UNREAD at grade; the is-ancestor read after MSTR's push is the evidence (CE-org-1).
- **No marquis decision, no retirement on this project's judgment, no gate.** CE-mrq-1 ends at a draft for his word; CE-t-11's RETIRE-candidate is surfaced, not acted; PRD s.5 "Any gate" stands.
- **The image-vs-repo finding on T-12** (`summary_corpus.py` pre-fix bytes baked into the derive image, owner `0.7.0_AE_CloudOps`) is CARRIED with its owner, not folded into CloudComp's row.

## 5. Holds, and whose they are -- and what step 6 waits on

1. **CE-disc-2 (4.3 spellings)** -- `1.0.0_SA_CTO` gate; binds by reading until then.
2. **CE-t-22 PRD half** -- `1.0.0_SA_CTO` (KUZUSPLIT PRD P1/P3 amendment).
3. **CE-t-13** -- `1.0.0_SA_CTO`'s disposition of comp-dups (R-5).
4. **CE-g-1** -- re-homes to the comp-graph owner (NFRA_GRAPHS lane); recorded as a dependency.
5. **CE-org-1** -- the integrator push (`0.0.0_AB_MSTR`); nothing reads CLEARED-on-origin until it runs.
6. **CE-g-4 / Rule 21's Codex enforcement bound** -- HELD by Andrew's ruling 2(b) until the rail is exercised.
7. **The 4.6 battery field's DIRECTORY grain** -- dead until CloudComp's F6 closes (needs `1.0.0_SA_CTO`'s word on three CTO/CTO~X files); every battery grade until then is written "FILE-grain only".

**STEP 6 (the first TREE task order) is NOT opened by this file**, and not only by Rule 27's "no TO before the decomp"
(now met): CVO's review sequence (@`580c4f72a2`) reads that **R-ii** (six one-root TO readers, the proof-of-spec ISSUANCE
HOOK first -- a tree TO without `<proof_of_spec>` is admitted today, and is invisible to `/to-check`) and **R-iv** close
before the first tree TO is cut, and both sit at `1.0.0_SA_CTO`. Andrew's process-wide GO does not overrule that
reading in words; it can in one. **When step 6 opens, the first TOs are STAGE 0 + STAGE 1:** CE-disc-2 and CE-tp-1
(decide-first, CTO/CVO), CE-t-1 (already sequenced at CloudComp as the next s.4 pass), then CE-t-2, CE-t-3 -- each
cut into `../task-orders/` (lane TREE_COO) with `<decomp_doc>` pointing at this file and `<owned_cells>` naming the
`CE-` ids, through `to-pipeline-gate.py` reading both roots.
