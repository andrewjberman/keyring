# CANONICAL FABRIC WORKFLOW — L1–L10, one owner per step, and where every gate actually is

**AUTHORED:** `1.0.0_SA_CTO`, 2026-09-01. **REWRITTEN 2026-09-03 ~04:0xZ** from the atom-decomp water test of this
document's own mechanisms (run `canonical-fabric-workflow-spec__20260903T0305Z`: 74 mechanism entities × 12 fields =
888 cells, 888 MEASURED, DRY at cycle 5; `workflows/atom_decomposition/runs/canonical-fabric-workflow-spec/20260903T0305Z/`;
certification OPEN — see §8). **STATUS: THE STATE OF RECORD GOVERNS** — Andrew, 2026-09-03, at the `0.0.0_AB_MSTR`
terminal, memorialized L1–L10 with role exclusivity (record @`716a9bc7ce`, LD-0521; the "Limb check" transcript verbatim in
its s.2 and in @`9a4d508ae5`; the drawing he called *"completely correct"* in its s.3). This file is the spec that record
points at and that CLAUDE.md Rule 27 links to. **Where this text and @`716a9bc7ce` s.3 differ, s.3 governs and this file
is the defect.** Every measurement below is pinned to HEAD `2718cffc45` (origin/CLOUD 03:42Z) or the worktree at 03:5xZ
unless a cell says otherwise; the cell is in the run's `rectangle.c4.json`, keyed by the `Ln.slug` ids used here.

**WHY IT EXISTS — Andrew's diagnosis, and it is the whole design constraint:** *whole projects were becoming thrashing
debug sessions with no hierarchy.* The measured instance was `ADVI_PERFRP` on 2026-09-01: five seats, one producer
question, nine hypotheses raised and nine dead, no frame holding them. **The loop is the frame. It runs in order.**

**VOCABULARY (measured drift, now fixed here):** the steps are **L1…L10** and nothing else. "step n" in older text is Ln.
The 2026-08-21 five-stage doc (`org/ref/DIRECTIVE_EXECUTION_PIPELINE.md`) maps stage 1 → L3, stage 2 → L4, stage 3 →
L5 + L6, stage 4 → L7, stage 5 → L8–L10; it keeps its MECHANISMS (they are what the gates cite) and carries dated VOID
markers on the three clauses this ruling retired. Route tokens are the gate's enum — `SPEC_ERROR`, `DECOMP_INVALIDATING`,
`SCOPE_CHANGE` — never their prose forms.

---

## 1. THE TEN STEPS — owner, instrument, artifact, stage, and what REFUSES

```
  L    OWNER (exclusive)      INSTRUMENT / ACT                       ARTIFACT                                 dep_stage      WHAT REFUSES (measured)                    NOTIFIES
  ---  ---------------------  -------------------------------------  ---------------------------------------  -------------  -----------------------------------------  ----------------------------
  L1   4.0.0_SA_CRO ONLY      /brief-create (after discussing the    docs/briefs/<f>.md, or an ANDREW_DIRECT  (no row)       nothing at L1; the brief_ref SHAPE is      --
                              topic with Andrew)                     record -- both admitted by PRD_HEADER                   refused at L6 (limb 5 pattern)
  L2   1.0.0_SA_CTO ONLY      /endpoint --forward <brief>            FWD-n QUALITATIVE outcomes (no numbers), (no row)       limb 4 + limb 5(d) at L6: the outcomes     --
                                                                     landing in the PRD's ENDPOINT section                   must be DEFINED in the PRD, both ways
  L3   1.0.0_SA_CTO ONLY      missions-tree-index.py derive --write  org/missions/D<n>/<MACRO>/<CODE>/         REGISTERED     missions-tree-check.sh at commit           --
                              (project + macro under the tree,       project.json + the GENERATED flat index                 (R1-R5, ROW-*, INDEX-*); DIRECTIVES.yaml
                              tagged fabric + directive)             org/projects/<CODE>.json (carries `home`)               members (R5), MACROS.yaml RATIFIED (R2)
  L4   1.0.0_SA_CTO ONLY      the PRD: fenced PRD_HEADER json +      prd/<CODE>_PRD.md at the tree home        PRD            lane ANY_CTO (writes); limb 5 at L6:       prd-header-notify R3 ->
                              ENDPOINT section + SURFACE MANIFEST                                                            header schema, identity vs the row,       2.0.0_SA_COO, re-offered
                              (one row per engine)                                                                           manifest present, FWD ids both ways        until READ
  L5   2.0.0_SA_COO ONLY      /atom-decomp over the manifest's       decompositions/<CODE>_DECOMP.md --        DECOMP         lane TREE_COO; consumed at L6 through      --
                              surfaces + the battery (3 mandatory    cells born UNMEASURED, ids per                          <decomp_ref>. NOBODY certifies before L6
                              preflight lenses)                      DECOMP_CELL_ID_CONVENTION                               (VOID clause)
  L6   2.0.0_SA_COO ONLY      TO + GO message to the EXACT serial    task-orders/<CODE>.TO-*.md carrying       EXECUTING      pre-commit stage 8 to-proof-of-spec-       --
                                                                     <decomp_ref><owned_cells><preflight>     (row owner     check.sh; stage 9 to-pipeline-gate.py
                                                                     <proof_of_spec><issued_to Tier-2>        flips on the   (layer 3, preflight, limb 4, limb 5,
                                                                                                              first TO)      R-iv, GATE (i) Tier-0/1 refused); lane
  L7   TIER-2 WORKERS ONLY    execute the TO; a surprise = ONE ROW   proof_of_spec instance at                 EXECUTING      surprise-row-gate.py stage 10 (row form);  --
                              appended to surprise-channel/          deliverables/<serial>/                                  proof-of-spec-check.py at completion
                              investigations/INVESTIGATION_v{N}.md                                                           (schema, alignment, artifacts, SURPRISES
                              (spec_asserts + world_is)                                                                      limb) -> no VALID instance, no `complete`
  L8   3.0.0_SA_CVO -- its    surprise-watch.sh (read-only           --                                       EXECUTING      nothing refuses                            surprise-watch: one line per
       FIRST engagement       watermark, both roots); comp-surprise                                                                                                     new row, at-least-once
  L9   3.0.0_SA_CVO           disposition per row; graduation is a   surprise-channel/remediations/            EXECUTING      row gate: required fields, closed enums    --
                              GROUNDING bar                          REMEDIATION_v{N}.md (lane TREE_CVO)                     (disposition), GRADUATED requires GROUNDED
  L10  3.0.0_SA_CVO stamps;   route + loop_target on the remediation route row                                ROUND_CLOSE    GATE (iii): route row REFUSED while any TO  prd-header-notify R7 ->
       the ROUTE OWNER acts   row; ONLY after every TO is complete                                            -> CLOSED      under the project is not terminal; LOCKED   the route owner, re-offered
                              AND every investigation is CVO-checked                                          (row owner)    map; SCOPE_CHANGE kind + outcome_ref       until READ
```

**L10 routing — the LOCKED map (`surprise-row-gate.py ROUTE_TO_STEP`, exercised):** `SPEC_ERROR → L6` (owner
`2.0.0_SA_COO`, re-cuts the TO) · `DECOMP_INVALIDATING → L5` (owner `2.0.0_SA_COO`, re-decomps; it REOPENS the round's
scope) · `SCOPE_CHANGE → L2` (owner `1.0.0_SA_CTO`, `/endpoint` F0 against the PRD's named outcome). Nothing routes until
the job is over: *"no LIM-10 routing until all task orders are complete. The surprise channel, all investigations,
completely checked by CVO."* A round whose remediation doc graduates ZERO items proceeds to the next L6 dispatches;
a project closes on a zero-graduation round (the 2-step atomic close).

**`0.0.0_AB_MSTR` INTEGRATES AND NEVER WORKS A PROJECT** — it holds the register (`DIRECTIVES.yaml`), the push windows
(pre-push deploy gate), and the seating; it holds no task order and no L-step.

---

## 2. ROLE EXCLUSIVITY — what enforces each half, measured

| step(s) | owner only | WRITES refused by (lane, `owned-paths-validate.py` exercised 03:1xZ–03:3xZ) | engagement BY MESSAGE |
|---|---|---|---|
| L1 | `4.0.0_SA_CRO` | `docs/briefs/` is lane ANY; nothing refuses another author | unguarded (prose) |
| L2–L4 | `1.0.0_SA_CTO` | `prd/**` = ANY_CTO: `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, Tier-2 all REFUSED; the tree row = TREE_PROJECT_ROW (CTO) | **UNGUARDED** — measured: before the ruling CVO drafted the PRD, read v0.3 row by row and graded the decomp by message; no mechanism refused it. A gate here needs Andrew's ask (§6). |
| L5–L6 | `2.0.0_SA_COO` | `decompositions/**` + `task-orders/**` = TREE_COO: CTO, CVO, MSTR, Tier-2 REFUSED | same class |
| L7 | Tier-2 workers | **GATE (i)** @`caa8b5c3a5`: a NEW tree TO whose `<issued_to>` names `0.0.<n>_*` or `*_SA_*` is REFUSED (16 of 16 red-first; the withdrawn `TO-CE-DISC-2 → 1.0.0_SA_CTO` is refused by it, `TO-CE-T-1 → 0.8.0_AE_CloudComp` admitted) | — |
| L8–L10 | `3.0.0_SA_CVO` | `remediations/**` = TREE_CVO (a Tier-2 worker REFUSED); `investigations/**` = ANY on BOTH roots (any seat appends its own row; flat root widened @`bfec7d99b5`) | — |
| integrator | `0.0.0_AB_MSTR` | pre-push deploy gate refuses deploy-scope pushes | **UNGUARDED** — nothing refuses a non-MSTR push; the role is convention (§6) |

---

## 3. THE ENFORCEMENT PLANE — every refusal and ping in the loop, with how it was exercised

Forty of the seventy-four mechanisms REFUSE, three NOTIFY, seven READ, twenty-four bind by reading. **"THE ONLY GATE" was
never true of this loop and is retired**: four pre-commit gates refuse inside it, plus the completion checker.

| fires at | mechanism | refuses / pings | exercised (locator) |
|---|---|---|---|
| commit, stage 8 | `.tools/git-hooks/to-proof-of-spec-check.sh` | a NEW TO (either root) without `<proof_of_spec>`, or without `<decomp_ref>` on a `dep_stage` project | CVO 92872: 6 of 6 in an isolated git; live @`4d9cd02e40` |
| commit, stage 9 | `.tools/to-pipeline-gate.py` | layer 3 (project row exists, `dep_stage` in the six-value enum, `fabric` in {laptop, site-z}); `<preflight>` with `comp-schedule`/`comp-iam`/`comp-adversary` each `RUN` + denominator or `DECLARED-NOT-APPLICABLE` + reason; limb 4 ENDPOINT section; limb 5 PRD_HEADER + identity + SURFACE MANIFEST + FWD ids both ways; R-iv row/folder identity; **gate (i)**; the `complete`-flip limb (no VALID proof instance → no terminal flip); `# pipeline-override:` written to `org/to-pipeline-override-audit.log` | limb 5 on the v0.4 bytes 0 complaints + 2 controls (02:4xZ); gate (i) 16 of 16 (03:2xZ); live @`4d9cd02e40`; bare-reason control 2026-09-01 |
| commit, stage 10 | `.tools/surprise-row-gate.py` | a NEW investigation row without `spec_asserts` + `world_is`; a NEW row off the closed enums (`disposition`); a NEW remediation row without `route` + `loop_target` or off the LOCKED map; `SCOPE_CHANGE` without `scope_change_kind` + `outcome_ref`; **gate (iii)**: a route row while any TO under the project is not terminal; HEAD rows byte-identical or refused | planted rows 03:3xZ (no `world_is` → refused; `BOGUS_STATE` → refused; `SPEC_ERROR→5` → refused); live census: 3 TOs, 1 open → a route row today is REFUSED; live row S1 @`03eb9e3dba` admitted |
| commit, stage 10 | `.tools/git-hooks/missions-tree-check.sh` → `missions-tree-index.py check` | R1 folder grammar, R2 macro not RATIFIED, R3 flat twin, R4 row/folder identity, R5 absent from DIRECTIVES.yaml members, ROW-ENUM, INDEX-MISSING/DRIFT/ORPHAN; fail-closed if the generator cannot run. BOUND: reads the worktree, not the staged index | CVO 92840 (two RED classes, control, fail-closed, GREEN); live @`19bf1c7322`, @`2e90f4e06c` |
| commit, every stage | `.owned-paths.yaml` via `safe-commit.sh` | the wrong author on `prd/**`, `decompositions/**`, `task-orders/**`, `remediations/**`, the register files | resolver-level 4 seats × 2 paths (03:1xZ); commit-level: CloudComp refused on an ANY_EXEC path (PRD :352-353) |
| completion | `.tools/proof-of-spec-check.py` | schema; `decomp_ref` vintage resolves; cell↔criterion alignment both ways; artifact rows resolve at their pins; **SURPRISES limb** @`7968221ef5`: every `surprises` entry opens with a row id that resolves in the project's channel (tree TOs ENFORCE, flat ANNOUNCE) | `--self-test` 6 of 6; live probe on row S1 VALID / phantom row REFUSED |
| post-commit | `.tools/prd-header-notify.py` (R3 + R7) | pings, never blocks: a new-or-bumped PRD_HEADER → `2.0.0_SA_COO`; a new remediation route row → its route owner; re-offered every 30 min until READ, up to 6 attempts | R3 live: `hook.log` 02:51:37Z → id 92935 → READ-acked by COO; **R7 UNEXERCISED** (no route row routed yet) |
| poll | `org/surprise_channel/surprise-watch.sh <serial> stream` | pings `3.0.0_SA_CVO` one line per NEW row on both roots; read-only watermark, at-least-once, cannot steal a row | CVO: fired on S1 within one poll (92976) |
| pre-push | `.tools/git-hooks/pre-push-safe-deploy.sh` | deploy-scope files (`data/*/scripts/**.py`) must reach S3 with ETag verified before the push lands | three integrator windows 2026-09-03 |

**Read-only readers of the loop (no refusal):** `to-check.py` (both roots), `to-decomp-ref-lint.py`, `to-liveness-join.py`,
`comp-state`, `comp-surprise` (both roots since 2026-09-03 — it read the flat root only until the water test found it),
`get_delivery_state` / `ack_messages` (the READ clock every notifier waits on: SENT ≠ EMITTED ≠ READ).

**UNEXERCISED at this vintage, declared:** the `complete`-flip limb on a TREE task order (no tree TO has flipped terminal
yet — `TO-CE-T-1`'s completion is its exercise); R7's route notification (no remediation row routed yet); the
`ROUND_CLOSE → CLOSED` transitions (never reached by any of the 37 staged rows); `/brief-create` on the water-test
project (its L1 artifact was an ANDREW_DIRECT record, the admitted second shape).

---

## 4. THE SURPRISE PATH — the ROW is the carrier (Andrew-direct 2026-09-03 ~03:1xZ, record @`007481053a`)

A seat that finds it had to do something the TO did not say, or could not do something the TO said, **appends one row**
— `spec_asserts` + `world_is`, class `{OBSERVATION, BLOCKING}` × `hazard_standing {ARMED, INERT}`, `disarm_owner` when
ARMED — and keeps working. The worker judges FORM, never significance.

- **Where:** tree project `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v{N}.md`;
  legacy flat project `org/surprise_channel/<CODE>/INVESTIGATION_v{N}.md`. Both lane ANY. One file per fabric per round
  (site Z writes `INVESTIGATION_v{N}.Z.md`, ids `{PROJECT}-Z-S{n}`). The flat root is FROZEN for new projects: every
  project registered since 2026-09-02 is a tree project.
- **A broker message is NEVER the carrier.** A notifier that watches files is structurally blind to an inbox; measured
  2026-09-03: one surprise routed by message cost three broker messages, an issuer reply and a CVO assembly in place of
  one append.
- **What binds it:** the row gate at commit (form); the step-8 watcher (delivery to CVO with the exact path); the
  proof-of-spec SURPRISES limb (a tree TO whose instance names a surprise with no resolving row id cannot flip to
  `complete`).
- **Remediation rows are CVO's** (`remediations/**` = TREE_CVO / CVO_WORKSPACE) — the one lane that still refuses a
  worker, by design: a route is an L9/L10 act.

---

## 5. THE HANDOFF ARTIFACTS — what crosses each seat boundary

```
  brief (L1)  --cites-->  FWD-n (L2)  --land in-->  PRD ENDPOINT + SURFACE MANIFEST (L4)  --decomposed by-->  DECOMP cells (L5)
  --> TO <decomp_ref><owned_cells> + GO to the exact serial (L6)  --> proof_of_spec instance, criterion <-> cell both ways (L7)
  --> INVESTIGATION rows (L7 writes, L8 reads, L9 dispositions)  --> REMEDIATION rows route + loop_target (L10)  --> the route owner
```
Every hop after L2 has a machine reader: the header schema, the manifest heading, `CELL_ID_RE`, the alignment join, the
row schemas, the LOCKED map. The two hops that bind by reading alone are L1 → L2 (a line to cite) and L2's rule that
outcomes carry no numbers.

---

## 6. MEASURED BREAKS AND THEIR OWNERS (from the run's `FINDINGS.md`; 52 of 74 entities carried a break at 03:05Z)

**Fixed inside the run window (each cites its hash):**

| break | class | fix |
|---|---|---|
| CLAUDE.md Rule 27 carried the five-stage framing | STALE_CLAUSE | the L1–L10 stub, linking here @`6e8805eb90` |
| CLAUDE.md, doctrine and protocol named a broker message as the surprise carrier | STALE_CLAUSE | the row rule @`6e8805eb90`, lanes reconciled @`835a7e1785` |
| the 08-21 doc: "CTO runs the decomp on a dark COO", "certifier of record = CVO", "executing seats do not write the channel" | STALE_CLAUSE ×3 | dated VOID markers @`6e8805eb90` + this rewrite's commit |
| nothing refused a Tier-0/1 seat in `<issued_to>`; nothing refused a route row before all TOs were complete | WORLD_ABSENT ×2 | gates (i) + (iii) @`caa8b5c3a5` |
| the proof-of-spec `surprises` field was free text | MISSING_MECHANISM | the SURPRISES limb @`7968221ef5` |
| `comp-surprise` read only the flat root (0 items for a project with rows S1/S2 at the tree home) | MISSING_MECHANISM | both roots, this rewrite's sibling commit |
| the L6 `# pipeline-override:` was "audited" in prose and only printed in fact | MISSING_MECHANISM | `org/to-pipeline-override-audit.log`, sibling commit |
| the tree row's `dep_stage` read DECOMP with a live task order since 02:14Z | TWO_CARRIERS_DRIFT | flipped to EXECUTING + index regenerated by the row owner |
| this file: silent on the tree, the header, the manifest, the notifiers, four gates, Rule 27; stale on comp-adversary's HELD clause, the "349 of 349" fabric count, `@40bf270dec` / `:45` pins; "I do not know which governs" | STALE_CLAUSE / STALE_VINTAGE_CITE (38 + 3 cells) | this rewrite |

**Open, with owners:**

| break | class | owner | what closes it |
|---|---|---|---|
| CVO (or any Tier-1) engaging an L2–L6 artifact BY MESSAGE has no mechanical guard (lanes guard writes only) | ROLE_VIOLATION_UNGUARDED | **Andrew** | his ask for a gate; candidate: none that reads the broker plane cleanly — the honest control is the record + this rule |
| the integrator-only push is convention | ROLE_VIOLATION_UNGUARDED | **Andrew** | his ask; candidate: a pre-push identity check against `0.0.0_AB_MSTR` |
| "every investigation completely checked by CVO" — the second half of the L10 precondition — has no gate | MISSING_MECHANISM | **Andrew** | his ask; candidate (~10 lines in the row gate): refuse a tree route row while any row of the project's INVESTIGATION file is `UNDER_INVESTIGATION` |
| four register rows carry off-enum `dep_stage` values the gate refuses a new TO on: `ADVI_ROSTERCOLS`, `ASSETCLASS_TAXONOMY` = BRIEF; `D1_NAMEDISCOVERY`, `ETFS_SATELLITES` = TOS_CUT | TWO_CARRIERS_DRIFT | `2.0.0_SA_COO` (register sweep) | re-key to the six-value enum |
| the 08-21 text says a TO names an executor CLASS, "never a serial"; every live TO and gate (i) read serials | TWO_CARRIERS_DRIFT | `2.0.0_SA_COO` (L6 template) with `1.0.0_SA_CTO` (the clause) | decide the grain; this file adopts the SERIAL, which is what the GO must be addressed to anyway |
| the L6 template's TO face no longer carries the verbatim worker line (it carries the SURPRISE GATE paragraph in row form) | STALE_CLAUSE | `1.0.0_SA_CTO` (this file, fixed: §4 names the paragraph) | done here |
| CVO's 09-01 as-built lists `/drive` as "the primary driver" while `/drive` is OFF | STALE_CLAUSE | `3.0.0_SA_CVO` (its deliverable; OBSERVATION, INERT) | a dated marker |
| `/brief-create` unexercised on the water-test project | (expected; L1 owner not live) | `4.0.0_SA_CRO` | the next project's L1 |

---

## 7. WHAT IS NOT MECHANICAL — stated plainly (updated from the 2026-09-01 text)

L1 and L2 bind by reading (a citable brief; qualitative outcomes). L4 binds by reading for its CONTENT (arc, defined
outcome) and by refusal for its SHAPE. L5's method binds by reading (nothing forces the package validator). L7's
significance judgment is deliberately not the worker's. L8's engagement, L9's grounding bar and L10's "CVO-checked" half
bind by reading. **Role exclusivity by MESSAGE binds by reading at every step.** Everything else in §3 refuses, and every
refusal in §3 was exercised at the vintage stated or is listed as unexercised.

CVO's 2026-09-01 summary stands corrected by the count: *"A loop with one gate is not a deterministic loop."* At this
vintage the loop has four commit gates, a completion checker, two notifiers with a READ clock, and lanes on every
artifact home — and the three remaining unguarded properties are named above with their owner.

---

## 8. THE WATER TEST — provenance, and the open certification

- Run home: `workflows/atom_decomposition/runs/canonical-fabric-workflow-spec/20260903T0305Z/` — `DOMAIN_BAR.md`
  (written before measurement), `axis_declaration.json` (74 entities, the enum's Rule 24 record, exclusions),
  `rectangle.c0.json` → `rectangle.c4.json` (five cycles; the package validator merged every patch), `FINDINGS.md`
  (a rendering; the rectangle is the source), `run.json` (trajectory, DRY basis, the mutant seal's sha256).
- Method: `projects/ATOM_DECOMP` Rule 14, SINGLE_AUTHOR_DIRECT (declared — `org/XXX.md` bans the fan-out agents);
  every plane-A cell carries the re-runnable act or the peer transcript it cites.
- **Certification is OPEN and this file says so rather than self-signing.** The standing certifier is `3.0.0_SA_CVO`;
  Andrew's 2026-09-03 word places CVO's first engagement at L8 of a *project*; this run is the spec's own water test,
  not a project step. Whether CVO certifies it, or `4.0.0_SA_CRO` as the independent seat does, is his call — surfaced
  as a card. A sealed coherence-violating mutant awaits the verifier (M-C: withheld in the author's scratchpad).

---

## POINTERS

- `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_024xZ_CANONICAL_WORKFLOW_L1_L10_STATE_OF_RECORD.md` @`716a9bc7ce` — the ruling this file serves (LD-0521).
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_021xZ_LIMB_CHECK_CANONICAL_WORKFLOW_L1_L10_COMPEFFICACY_PICKUP.md` @`9a4d508ae5` — the transcript, verbatim.
- `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` — the 08-21 mechanisms (stage-3 decomp rules, stage-4 execution rules, the surprise taxonomy); three clauses VOID, dated.
- `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` · `docs/doctrine/THE_SURPRISE_CHANNEL.md` — the channel's schemas and doctrine (row is the carrier).
- `org/standards/PROJECT_TREE.contract.json` · `org/standards/PRD_HEADER.schema.json` · `org/standards/DECOMP_CELL_ID_CONVENTION.md` · `org/standards/PROOF_OF_SPEC.schema.json` — the data contracts the gates read.
- `.claude/skills/brief-create/SKILL.md` (L1) · `.claude/skills/endpoint/SKILL.md` (L2, L10 scope-change) · `.claude/skills/atom-decomp/SKILL.md` (L5).
- `.tools/to-pipeline-gate.py` — the L6 neck; `.tools/surprise-row-gate.py` — L7/L9/L10 rows; `.tools/proof-of-spec-check.py` — completion; `.tools/git-hooks/missions-tree-check.sh` — L3.
