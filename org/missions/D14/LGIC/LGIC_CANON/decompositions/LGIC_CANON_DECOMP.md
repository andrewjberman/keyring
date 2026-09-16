# LGIC_CANON — DECOMPOSITION (L5)

```json
{
 "project": "LGIC_CANON",
 "directive": "D14",
 "macro": "LGIC",
 "fabric": "laptop",
 "decomp_version": "v4",
 "step": 5,
 "prd_ref": "org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md@5b2336a5e4",
 "prd_half_hashes": {"brief": "SIGNED 4.0.0_SA_CRO, current at v1.3 (prd-signoff.py status, read at the L6 cut 2026-09-15)", "ratified-text": "SIGNED 3.0.0_SA_CVO, current at v1.3 (ENDPOINT and CONTRACTS unchanged)"},
 "author": "2.0.0_SA_COO~G",
 "cells": 12, "round2_cells": 10,
 "slots": 9, "round2_slots": 7,
 "candidates_not_cut": ["C6 -- FWD-5 held on Andrew's ~13:4xZ word"],
 "dag_levels": 3, "round2_dag_levels": 3,
 "frozen": false, "frozen_note": "round 1 CLOSED at L10; the freeze lifted at v4 s.0d and re-arms at the round-2 issuance"
}
```

**Author:** `2.0.0_SA_COO~G`, the lane leading the sequence. The authority is Andrew-direct 2026-09-14 ~16:3xZ, record @`507864b842`,
with the DIRECTED Step 1b-F row. `1.0.0_SA_CTO` set the L5 order in msg 96640; this project is second.
**Input:** the PRD's SURFACE MANIFEST at v1.1 @`56608aadd4` (v1), re-read at v1.3 @`5b2336a5e4` (v2, section 0b).
**v2, cut before any L6 issuance** (LGIC_CANON has no issuer: Andrew-direct ~18:2xZ, 96673 item 3). It changes one choice: the
judged tree for C2 (row LGIC_CANON-S2, 4.0.0_SA_CRO @48146fdd10; 1.0.0_SA_CTO's correction 96693).
**v3, the re-read at the L6 cut** (section 0c), 2026-09-15, after `1.0.0_SA_CTO` seated this project on `2.0.0_SA_COO~G`
(@`52ea4c8cac`). The PRD did not move; the register, the schema and the registry did. Cells, edges and constraints stand;
CN-n-2 moves to its own slot, and gate G-V19R is added. v3 writes LGIC_ENFORCE's cells as `LGIC_ENFORCE cell r-<n>` (its id
there is `EN-r-<n>`), as that project's v1.1 did: the L6 coverage limb reads every cell id in this document as one of
this project's own (LGIC_ENFORCE row S1), and refused this issuance for 12 of 15 cells on the three it counted.
**Sequence:** stage 1, no gate. `sequence-check --project LGIC_CANON` flags NEEDS-SLOT, which this cut and its row flip answer.
**Frozen at the cut.** A cell that looks wrong mid-round is a **surprise row, never an edit**
(`org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md`, 1 row at the cut).

**What every cell carries:**
- **DEC-9:** this project moves no data, repoints no trigger, edits no bucket policy, applies nothing and calls nothing off
  Opal infrastructure.
- **The canon is the RULE.** The names are LGIC_NAMING's; the registry, builders and gates are LGIC_ENFORCE's (remediation
  shape (a)).

---

## 0. WHAT THIS CUT READ, AND THE ONE CANDIDATE IT DOES NOT CUT

1. **C6 is NOT cut: FWD-5 is held on Andrew's word.** Andrew-direct 2026-09-14 ~13:4xZ, *"recs + sequence approved"*, record
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_134xZ_NEXT_CALLS_RECS_AND_SEQUENCE_APPROVED.md`, as the
   tree row's blocking item records it: *"a cutover of an EXISTING firm does NOT satisfy FWD-5's new-firm test; FWD-5 is
   graded only on a true new-firm act and is held until one exists."*
   - This is the one kind of wait Rule 27 admits: EXPRESSLY QUALIFIED on the outcome, with its reason and his word.
   - C6's act (the checklist's first real run) has no subject until a genuinely new firm exists. Cutting it against
     ADVI_FIRMBKTS's cutover would grade FWD-5 against a text he ruled it does not meet.
   - C5 (the checklist) IS cut, so the instrument exists when the firm does. Gate G-N.
2. **DEC-8 is APPLIED, measured.** `docs/doctrine/CLAUDE_ANNEX.md:444` cites
   `org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md` as the D14 PRD that carries D10's folded canon content. No cell
   is owed.
3. **Row LGIC_CANON-S1 is carried into CN-k-1**, as `1.0.0_SA_CTO` asked (96626: *"held for its round"*).
   - R1's non-application at `infra/logic/02_DOCTRINE.md:103` still exempts *"`code/` prefixes (R16)"*, re-read at this cut.
   - But LGIC_NAMING v1.3 (row LGIC_NAMING-S7, ruled) puts every NEW code home in the grammar's code tier,
     `{source}/{scope}/code/{built_tier}/{file}`.
   - CN-k-1 narrows R1's entry to the LEGACY root homes.
4. **`3.0.0_SA_CVO`'s N4 is carried into CN-k-1** (review @`abf61890f2`, on the tree row's phase).
   - The generated naming section binds to the STAMPED schema, so after a schema bump it goes stale while still matching its
     own stamp.
   - CN-k-1 names the trigger and makes it refusable: `render_naming_section.py --check` compares the section's stamped hash
     with the live schema's, and exits non-zero when they differ.
5. **The judged tree for C2 is chosen here, by measurement** (§3a.1). ⚠ **v1's choice below was WRONG on grain and is
   corrected in v2 to MDPF (section 0b).** The v1 text is kept, struck, because the reading of DEC-2 it states is right and
   the tree it names is not. The ledger's vocabulary has no CONTRADICTS value; its
   values are CONFORMANT, MIGRATE, RETIRE, DECLARED EXCEPTION and AWAITING. And the only contradiction reports are IRPT_BCKEND's
   and IRPT_FNTEND's, which carry no exception. So DEC-2's *"chosen from the ledger so that it carries at least one CONTRADICTS
   and one DECLARED EXCEPTION"* is read as **a ledger row where the tree breaks a rule, plus a DECLARED EXCEPTION**. The ETFs
   tree has both:
   - `opal-data-etfs/gold/` holds 32 JSON objects against R11's parquet rule (`06_CONFORMANCE_LEDGER.md:102`, MIGRATE-format);
   - X4 is GRANTED and PERMANENT (`:133`, Pathfinder and TrueShares), with X3 and X5 OWED (`:101`, `:103`, `:132`, `:134`).

---

## 0b. v2 -- THE RE-READ AGAINST PRD v1.3, AND THE TREE CORRECTED

**What moved in the PRD** (`git show d9977a0f40` and `git show 5b2336a5e4`): DEC-2 (v1.2) and C2's inputs column (v1.3) now
read *"at least one row where the tree breaks a canon rule (a MIGRATE or RETIRE row) and one DECLARED EXCEPTION"*. That is
this decomposition's own reading (v1's s.8 choice 3), now PRD text, ruled to stand by `1.0.0_SA_CTO` (96677). **Nothing else
moved:** ENDPOINT and CONTRACTS are byte-unchanged. So the cells, edges and constraints stand as cut in v1.

**What v1 got wrong, and this cut corrects: the TREE, on GRAIN.** v1 chose the ETFs tree on the strength of X4 (ledger `:133`).
But X4 is Pathfinder and TrueShares (*"no gold, no platinum"*), whose planes are in the monolith (`:52-54`), not a departure of
`opal-data-etfs`. The ETFs tree's own exceptions, X3 (`:132`) and X5 (`:134`), are both OWED, and `:101-103` read AWAITING. So
the ETFs tree carries no DECLARED exception and fails DEC-2. It was found by `4.0.0_SA_CRO` (row LGIC_CANON-S2 @48146fdd10) and
confirmed by `1.0.0_SA_CTO` (96693). **The corrected tree is MDPF**, because inside one pipeline it carries:
- MIGRATE rows at `infra/logic/06_CONFORMANCE_LEDGER.md:98` (bronze) and `:100` (the gold destination);
- X1, GRANTED and PERMANENT, at `:130` (the Orion JWT credential artifact).

This seat re-reads those three lines at HEAD before the cut, and L6 re-reads them again at the issuance base. Nothing was cut
on the wrong tree.

---

## 0c. v3 -- THE RE-READ AT THE L6 CUT (round 1's issuance, 2026-09-15)

**What moved since v2, measured at the issuance base CLOUD @`10894fdad1`.** The PRD did not: its latest commit is
`5b2336a5e4`, the one v2 read, and `prd-signoff.py status LGIC_CANON` reads ADMITTED (both halves SIGNED, current). What
moved is the estate the cells read.

1. **The seat.** `1.0.0_SA_CTO` seated this project on `2.0.0_SA_COO~G` @`52ea4c8cac`, on Andrew-direct ~16:1xZ, verbatim
   *"Yeah there is a lot of work to be doing here between ENFORCE and CANON and I want you parallelizing harder. Use more
   agents, go faster."* (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_161xZ_PARALLELIZE_HARDER_ENFORCE_AND_CANON~G.md`).
   `sequence-check --project LGIC_CANON` no longer flags NEEDS-SLOT.
2. **The exception register moved, in both of its carriers.** X2 GRANTED and X7 added @`9cf4a274db` (`1.0.0_SA_CTO`),
   cross-referenced @`c9048873d1` (`4.0.0_SA_CRO`), in `02_DOCTRINE.md` section 4 and `06_CONFORMANCE_LEDGER.md` section 6.
   - **CN-l-1:** *"X2, X3 and X5 each name their decider"* now reads the register's acknowledged column or a `decider:`
     line. X2's decider is its acknowledgement (GRANTED); X3 and X5 still read `--`.
   - **The MDPF tree (section 3a.1) now carries three declared exceptions** -- X1 (`:130`), X2 (`:131`), X7 (`:136`) --
     beside its MIGRATE rows (`:98`, `:100`, the monolith gold residue `:59-60`, the per-firm platinum `:110`). DEC-2 is met
     with room to spare, and the tree stands.
   - **Both files have live co-writers.** `1.0.0_SA_CTO` and `4.0.0_SA_CRO` write register entries in them. CN-k-1 and
     CN-l-1 hold them this round; an entry that lands mid-round is merged at the drain, never reverted.
3. **`NAMING_SCHEMA.json` is v1.8 (@`2f554182b6`), and v1.9 is scheduled (gate G-V19, cut beside LGIC_ENFORCE round 2
   and LGIC_NAMING round 4).** v1.9 removes `firm_forms` (the registry's `scopes.json` becomes their one carrier,
   LGIC_ENFORCE RULING ONE) and adds the Terraform-type-to-node-type map.
   - CN-k-1's generated section renders the naming content from the files that carry it AT HEAD: the schema, and the firm
     forms from `firm_forms` while the field exists, else the registry's FIRM rows. Its stamp names every file read, with
     that file's hash.
   - **Gate G-V19R (new; the issuer's drain act):** whichever of CN-k-1's drain and GROUP V19's merge lands SECOND re-runs
     `render_naming_section.py --write` in that same merge, and `--check` reads 0 on the merged tree. That is
     `3.0.0_SA_CVO`'s N4 trigger exercised, not a new rule.
4. **The registry exists, so G-R is CLEARED, measured:** `infra/logic/registry/{scopes,systems,tiers,exemptions,remediations}.json`
   at HEAD; LGIC_ENFORCE cell r-1 landed @`a925c8a642`. CN-n-1 spawns at issuance.
5. **CLAUDE.md Rule 30** (Andrew-direct ~14:2xZ, *"all future pipelines must abide by lgic structures patterns"*): every
   address and name comes from the builders. CN-n's key (section 3a.3) is builder output -- `key()`, `address()`, `name()`
   and the registry's `bucket` field -- never typed. CN-o-1's steps name their builders.
6. **Andrew's aim (msg 96910): LGIC is aimed at the MDPF, ADVI and IRPT pipelines.** Two cells take a population. The judged
   tree is MDPF (v2 already). The naming job's systems are MDPF, ADVI and IRPT, plus the Black Diamond integration for the
   refused-token case.

**The cross-project write census, by subtraction (Rule 24):**

```
  write surfaces of the 12 cells .................................. 13 paths
  minus records and exercises under org/missions/D14/LGIC/LGIC_CANON/ -9
  minus this project's own infra/logic/ surfaces (section 1) ....... -4
        02_DOCTRINE.md, render_naming_section.py, 06_CONFORMANCE_LEDGER.md, 10_ONBOARDING_CHECKLIST.md
  ------------------------------------------------------------------
  paths any other LGIC project writes this round .................... 0
```

No cell writes `lib/opal_naming.py`, `infra/logic/registry/*`, `NAMING_SCHEMA.json`, `GRADING_RULE.md` or any LGIC_ENFORCE
or LGIC_NAMING deliverable, so no cell is ordered after GROUP V19 or LGIC_ENFORCE cell r-2. The READ dependencies, disclosed:
- CN-k-1 reads the schema and the firm-forms carrier (G-V19R above).
- CN-n reads the registry and the builders. LGIC_ENFORCE cell r-2 adds SYSTEM rows and its cell r-3 moves the firm forms' carrier; neither moves
  `49financial`/`49f`, so no key value moves with them.
- CN-j's naming cases come from `GRADING_RULE.md` @`3cc090827f`. None turns on a step LGIC_NAMING round 4 re-cuts (G2's
  AWS-fixed exclusion, FN1d's one subtraction, V-2's placeholders).
- CN-o-1 reads LGIC_ENFORCE's CONTRACTS names (PRD v1.1, unchanged).

**Fixed inputs, committed with the issuance under `deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/`:** `CN_TREE_MDPF.md` (facts
only, no disposition); `CN_JUDGE_CASES.json` (3 cases: a CONFORMANT secret and two ALIAS names that turn on `bd` and the
per-slot firm form); `CN_JUDGE_NAMING_KEY.json`; `CN_NAMING_JOB.json` (6 items: 3 LONG, 2 SHORT, 1 refused-token trap);
`CN_NAMING_KEY.json`; and `check_canon_r1.py` (39 subcommands, one per mechanical criterion).

**The slots, v2's table with one change:**

| slot | cells | spawned |
|---|---|---|
| ~1 | CN-k-1 | at issuance |
| ~2 | CN-l-1 | at issuance |
| ~3 | CN-r-1, then CN-r-2 | at issuance |
| ~4 | CN-j-1 | after CN-k-1 drains |
| ~5 | CN-j-2 | after CN-k-1 drains, from slot 4's base |
| ~6 | CN-o-1 | after CN-k-1 drains |
| ~7 | the scorer: CN-j-3, CN-o-2, CN-n-3, each as its inputs drain | when the first input drains |
| ~8 | CN-n-1 | at issuance (G-R cleared) |
| ~9 | CN-n-2 | after CN-n-1 drains |

- **The change:** CN-n-2 takes its own slot ~9, not a second spawn in slot ~8. Two contexts on one serial would mint rows
  under one W-number (the row-id collision class, LGIC_ENFORCE C-S13) and blur the blindness check's attribution.
- **Fan-out:** 9 slots over M = 5 chains ({k-1, j-1, j-2, j-3, o-1, o-2}, {n-1, n-2, n-3}, {r-1}, {r-2}, {l-1}). N exceeds M by
  the distinct-worker cells, as `1.0.0_SA_CTO`'s S3 ruling allows (LGIC_NAMING round-3 analysis section 2). 4 spawn at
  issuance and at most 7 are live at once; ~9 spawns only after ~8's worker has ended, so the live count stays under the cap
  of 8.

**Unchanged from section 5:** blindness to the estate is NOT-EVALUATED for the judges and the naming workers (the preloaded
context). **L4-R at the cut:** ADMITTED at v1.3.

---

## 0d. v4 -- THE ROUND-2 RECUT (2026-09-16), ON THE CTO's ROUND-1 ANALYSIS

**Authority.** `1.0.0_SA_CTO`'s LGIC_CANON round-1 ANALYSIS @`26ae876d23` (msg 97317), the CTO's one send at L10, on
`3.0.0_SA_CVO`'s slug. Round 1 is CLOSED at L10 and the freeze lifts HERE: the decomposition was frozen from the round-1
issuance @`4058a56606` until this section. Recut base CLOUD @`14936be222`.

**The round-1 grade this recut answers (analysis s.1):** FWD-2, FWD-3, FWD-4 and FWD-6 REALIZED; **FWD-1 SHORT**
(K1-J1 FAIL, J3-AC2 and J3-AC3 FAIL, bounded by rows C-S9 and C-S10); **FWD-5 NOT EVALUATED**, because C6 stays NOT CUT
on Andrew's G-N word and its instrument reads SHORT. Not CLOSED. **No PRD addendum:** the analysis found no outcome
wrong, incomplete or obsolete, so `/endpoint` F0 is not re-entered and the PRD stays v1.3.

**The PRD halves were re-read at this cut, not carried forward.** `prd-signoff.py status LGIC_CANON` reads
`v1.3 @5b2336a5e4 dep_stage=EXECUTING -> ADMITTED`, ratified-text SIGNED by `3.0.0_SA_CVO` and brief SIGNED by
`4.0.0_SA_CRO`, **both `current`**. The halves bind to the sections' HASH and not to `prd_version`, so a re-read is the
only thing that says `current`; the version being unchanged says nothing.

### What moved since v3, measured

1. **Gate G-V19 is MET @`4730cec6ca` and G-V19R @`783e2f3887`.** `NAMING_SCHEMA.json` is v1.9 at HEAD, `firm_forms` is
   gone from it, and the scope registry's FIRM rows are the one carrier. The canon's generated section was re-rendered
   in the commit immediately after the merge, in the lane that owns the path, under RULING R-1. `--check` reads
   `FRESH -- 0 failure(s)` at HEAD, read by three seats on three checkouts.
   - ⛔ **G-V19R's wording in this file is a DEFECT and R-1 corrects it.** `:125` said the render runs *"in that same
     merge"*. No seat can do that: `safe-merge.sh --continue` REFUSES any path the merge itself did not stage, which is
     the guard that stops another seat's work riding a drain, and the canon is not in a group merge's staged set. The
     rule reads **"in the merge, or in the commit immediately following it, in the lane that owns the path."**
2. **Round 1's channel closed at 16 rows, not the 15 the hand-off named.** `2.0.0_SA_COO~G` appended `LGIC_CANON-S3` at
   05:52Z (@`5bdaa031c0`) while the L8 was being written, and `3.0.0_SA_CVO` caught it by counting the fence again at
   write time rather than trusting the handed figure. L9 dispositioned 16 of 16: **10 GRADUATED, 3 DISMISSED_WITH_REASON**
   in the adjudication, and `REMEDIATION_v1.md` carries 16 rows.
   - **Verified here by a different instrument** (the issuer's own cross-read, not the CVO's run): every one of the 10
     GRADUATED ids is named in the remediation file, 0 missing, and the remediation's own id list carries no duplicate.
     A graduated row with no remediation row is the failure this check exists for and there is none.
3. **Two ARMED rows stand into round 2, with different disarm owners.** `LGIC_CANON-W8-S1` is `1.0.0_SA_CTO`'s and its
   clock advance is `3.0.0_SA_CVO`'s one act in lane `TREE_CVO`. **`LGIC_CANON-S3` is this seat's** and it is what
   CN-k-3 disarms: `render_naming_section.py` reads a FIRM row's `long` and `short` on its registry path and never its
   `note`, so v1.9's move cost the canon the `demo` note carrying RULING DM. ⚠ `--check` reads FRESH over that loss,
   because the section IS a faithful render of what the renderer chose to read. **A freshness check cannot see a line no
   render produces.**
4. **`LGIC_LGCTFM` is now a D14 member and PLACED** in `SEQUENCE.yaml` stage 1 @`14936be222` (RULING R-4), fourth of the
   Platform Logic projects, `waits_on` this project's PRD among the three. Nothing of this recut waits on it.

### The cells -- 10, one issuance, C6 still NOT CUT

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, prefix `CN`, continuing round 1's axes.

| cell | what it is | rulings | serves | writes | depends on |
|---|---|---|---|---|---|
| `CN-k-2` | the canon edit: A1's rule set and R20 on every axis, the citation rule, the verdict vocabulary and severity order, the pipeline-instance rule, R1's census tag | A-1, A-2, A-4, A-9 | FWD-1, FWD-5 instrument | `infra/logic/02_DOCTRINE.md` | nothing |
| `CN-k-3` | the renderer: the FIRM-row `note` read (row `LGIC_CANON-S3`, this seat's disarm) plus the content-diff arm | A-11 | FWD-1 | `infra/logic/render_naming_section.py` | nothing |
| `CN-k-4` | the re-render once the schema carries the `bd` adjacency test | A-3 | FWD-1 | `infra/logic/02_DOCTRINE.md` | LGIC_NAMING's schema cell, a cross-project READ dependency, disclosed |
| `CN-j-4` | judge C, blind, on the SECOND tree, the canon alone, NO verdict scale in the order | A-1, A-13 | FWD-1 | deliverables only | `CN-k-2` |
| `CN-j-5` | judge D, blind, same brief, blind to C | A-1, A-13 | FWD-1 | deliverables only | `CN-k-2` |
| `CN-j-6` | judge E: the MDPF tree again, briefed WITHOUT the severity order -- the NEGATIVE arm | A-1 | FWD-1 | deliverables only | `CN-k-2` |
| `CN-j-7` | the comparison over C, D and E; every disagreement traced to a canon coordinate; the seven-rule reach printed | A-13 | FWD-1 | deliverables only | `CN-j-4`, `CN-j-5`, `CN-j-6` |
| `CN-o-3` | the checklist edit: sovereign inputs named; Step 6's second block; Step 10's STOP names ADVI_FIRMBKTS; Step 14's STOP names X8; steps 3, 7, 8 and 9 take the family | A-6, A-7, A-8, A-9, A-10 | FWD-5 instrument | `infra/logic/10_ONBOARDING_CHECKLIST.md` | `CN-k-2` for the instance rule |
| `CN-o-4` | the review, by a worker who did not write it: TWO bars, both printed -- zero JUDGEMENT marks, AND every MECHANICAL step either runnable today or STOPped with a named owner | the CVO's sequencing point | FWD-5 instrument | deliverables only | `CN-o-3` |
| `CN-l-2` | the ledger: X6 on its own axis; the checker scoped by section with `encoding='utf-8'` reads; the section-7 header workaround reverted | A-5, A-12 | FWD-6 hygiene | `infra/logic/06_CONFORMANCE_LEDGER.md` | nothing |
| `C6` | **STAYS NOT CUT** | -- | FWD-5 | -- | Andrew's G-N word AND, by A-8, ADVI_FIRMBKTS's router repoint |

**COVERAGE, and the gate does NOT grade it here.** `to-pipeline-gate.py`'s coverage limb grades the staged orders
against the cell set only at `dep_stage=DECOMP`; this project reads `EXECUTING`, so on a RECUT coverage is **NOTED, not
GRADED**. The denominator is therefore read by hand and printed: the analysis s.3 names **10 cells plus C6 held**, and
this issuance cuts **10**, C6 held for the same two reasons the analysis gives. A dropped cell here is nobody's refusal
but this seat's to catch.

### Levels, slots, and the two disjointness constraints

- **Level 0:** `CN-k-2`, `CN-k-3`, `CN-l-2`. **Level 1:** `CN-o-3`, `CN-j-4`, `CN-j-5`, `CN-j-6`. **Level 2:** `CN-j-7`,
  `CN-o-4`. **`CN-k-4`** is level 0 by its own edges but gated on another project's drain, so it spawns when
  LGIC_NAMING's schema cell lands, not at issuance.
- **WRITE-SURFACE DISJOINTNESS, MEASURED AT THIS CUT, not asserted.** The `<paths>` block of every NON-TERMINAL order of
  `LGIC_NAMING` and `LGIC_ENFORCE` was parsed -- **15 orders, the printed denominator** -- and intersected with this
  round's four write surfaces. **The intersection is EMPTY.** So no cell of this round contends with a live sibling cell.
- **INTERNAL contention, the one this round has:** `CN-k-2` and `CN-k-4` both write `infra/logic/02_DOCTRINE.md`. They
  take **ONE slot, sequenced**, never two. That is the queue rule, not a fan-out loss: the second depends on the first.
- **Distinct-worker constraints, as v3:** a scorer never scores its own work; `CN-j-7` is not written by any of C, D or
  E; the three judges are blind to each other and to `CN-k-2`'s author; `CN-o-4`'s worker did not write `CN-o-3`.

### The fixed inputs L6 cuts into round 2's faces

1. **`check_canon_r2.py`**, round 2's checker, under
   `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`, committed WITH the issuance and
   read-only to every worker. Every mechanical criterion of this round calls one of its subcommands.
   - ⛔ **Its `spawn_base()` must be PINNED to the issuance base, never `git merge-base HEAD CLOUD`** -- row
     `LGIC_ENFORCE-S20` measured that a moving base makes every diff-counting criterion read 0 changed lines once the
     cell is on CLOUD, so the criterion cannot be re-graded after its own drain and FAILs on every checkout.
2. **The SECOND tree** for `CN-j-4` and `CN-j-5`, named by path at the cut and read at the issuance HEAD, chosen so it
   engages the seven canon rules the MDPF tree never reached (A-13). The MDPF tree stays `CN-j-6`'s, unchanged, as the
   negative arm.
3. **The judges' brief** carries the canon alone. ⛔ **The verdict vocabulary and severity order go into `CN-j-4` and
   `CN-j-5`'s faces and are WITHHELD from `CN-j-6`'s** -- that withholding IS the negative arm, and a face that leaks it
   destroys the measurement.
4. **Row `LGIC_CANON-S3`** is inlined into `CN-k-3`'s face, with the measured fact that the registry's `demo` row is the
   one FIRM row of four whose key list includes `note`.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  SURFACE MANIFEST rows at 56608aadd4 ................................ 8   (denominator, parsed)
  minus the row marked "excluded" .................................... -1  (data moves, repoints, policy edits, applies,
                                                                              vendor calls; the pause)
  minus the row whose kind is "read only" ............................ -1  (the reference set, the schema, the registry,
                                                                              the folded and inherited PRDs, both IRPT PRDs)
  minus the row "observed and recorded, not executed here" ........... -1  (ADVI_FIRMBKTS's first cutover -- C6, not cut, s.0.1)
  minus the row whose writer is 1.0.0_SA_CTO ......................... -1  (CLAUDE_ANNEX.md Rule 17b's citation -- DEC-8,
                                                                              APPLIED, s.0.2)
  ------------------------------------------------------------------
  WRITE SURFACES FOR THIS ROUND ...................................... 4
     S1  infra/logic/02_DOCTRINE.md, 06_CONFORMANCE_LEDGER.md          edits to documents        CN-k-1, CN-l-1
     S2  infra/logic/10_ONBOARDING_CHECKLIST.md                        new document              CN-o-1
     S3  infra/logic/render_naming_section.py                          new script                CN-k-1
     S4  org/missions/D14/LGIC/LGIC_CANON/deliverables/                records                   CN-j-*, CN-r-*, CN-o-2, CN-n-*, CN-l-1
```

**Falsifier: the domain against every path the PRD cites.** `comp-adversary compose` over the PRD (read-vintage HEAD
@`8d1d4d3e2f`, 2026-09-14T18:18:35Z; artifact-vintage `56608aadd4`) returned:
- **11 of 11** cited commits verified.
- **17** cited paths: **13 stable, 4 flagged.**
  - **2 GONE, correctly.** `10_ONBOARDING_CHECKLIST.md` and `render_naming_section.py` are this project's to mint.
  - **2 MOVED.** `SEQUENCE.yaml` moved with no gate on this project. `NAMING_SCHEMA.json` is now v1.4, and **that move is
    load-bearing**: CN-k-1 renders the schema at HEAD (v1.4, with the entity partition, the code tier and legacy served
    paths), and row S1 follows from the same move.

No flagged path falls outside the manifest.

**Status vocabulary:** `MEASURED` / `DECLARED` / `NOT-EVALUATED` / `N/A`, as in LGIC_NAMING's and LGIC_ENFORCE's
decompositions. NOT-EVALUATED is a value, so non-evaluation is never encoded as a verdict.

---

## 2. THE RECTANGLE

| # | surface | current state | target state | collision set | evidence | cells |
|---|---|---|---|---|---|---|
| 1 | `02_DOCTRINE.md` | `MEASURED` v0.3 @`6dab0d76a7`: 29,299 bytes; §0-§7; R1 at `:88-105`, non-application `:103`; §4 holds the register schema AND its first entries | v1.0 (DEC-1 a-d); R1's `code/` narrowed (S1); §4 keeps the register SCHEMA and points at the ledger for its ENTRIES | none; sole writer | `MEASURED` | CN-k-1 |
| 2 | `render_naming_section.py` | `MEASURED` absent (GONE) | renders the canon's naming section from `NAMING_SCHEMA.json`; `--check` refuses a stale stamp (N4) | none | `MEASURED` | CN-k-1 |
| 3 | `06_CONFORMANCE_LEDGER.md` | `MEASURED` v0.3 @`6dab0d76a7`: 18,176 bytes, §0-§8; §6 carries the register (X1-X6: 3 GRANTED, 3 OWED); §7's counts *"re-derived by hand"* | v1.0 (DEC-7 a-d): recounted by script; deciders on X2, X3, X5; a decided/waiting column | none; sole writer. The register's ENTRIES get one home (here) and its SCHEMA another (the canon), §8 choice 2 | `MEASURED` | CN-l-1 |
| 4 | `10_ONBOARDING_CHECKLIST.md` | `MEASURED` absent | ordered steps from the identity row to the served dashboard, each naming its rule (canon v1.0) and its builder or gate (LGIC_ENFORCE's CONTRACTS names) | none | `MEASURED` | CN-o-1 |
| 5 | `deliverables/` | `MEASURED` absent | one record per exercise and grading cell | none: no file has two writers | `MEASURED` | 9 cells |

**Worker admission is `NOT-EVALUATED` and load-bearing.** The `infra/logic/` files sit in lane PLATFORM_LOGIC_DOCS, and files
directly under `deliverables/` sit in TREE_DELIVERABLES. A worker is admitted only by its order's `<paths>`, and that is
exercised at L6 (G-C).

---

## 3. THE CELLS — 12

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, prefix `CN`. Axes:
- `k` the canon
- `j` the blind judging
- `r` graded from the record
- `o` the onboarding checklist
- `n` the naming exercise
- `l` the ledger

Deliverable paths are under `org/missions/D14/LGIC/LGIC_CANON/deliverables/`. Each acceptance line below is **one
criterion**. `J` marks a judgment criterion, graded by `3.0.0_SA_CVO` at L9.

| cell | what it is | PRD cand. | serves | writes | acceptance, one clause per line |
|---|---|---|---|---|---|
| `CN-k-1` | the canon at v1.0, with its generated naming section | C1 | FWD-1, FWD-6 | `infra/logic/02_DOCTRINE.md`; `infra/logic/render_naming_section.py` | a census of the canon's rules prints its denominator and finds every rule carrying its authority, its census tag and its non-application · `render_naming_section.py --check` exits 0: the section's bytes equal a fresh render of the stamped schema · on a scratch copy with a doctored stamp, `--check` exits non-zero (N4) · a census of the schema's enumerations outside the generated section returns 0, denominator printed · every §6 item is closed or names its decider · D10 s.2 and s.6 are absorbed in place of the pointer · R1's non-application names only the LEGACY root `code/` homes (S1) · `J`: a seat can apply each rule from this document alone |
| `CN-j-1` | judge A | C2 | FWD-1 | `exercises/judge-a.tsv` | a verdict and a rule citation for each of the five axes of the fixed tree (§3a.1), briefed with the canon ALONE · a verdict and a citation for each fixed naming case (§3a.2) · the record states its worktree base commit |
| `CN-j-2` | judge B | C2 | FWD-1 | `exercises/judge-b.tsv` | as CN-j-1, blind to it |
| `CN-j-3` | the judges' comparison | C2 | FWD-1 | `exercises/judge-compare.md` | the two judgings give the same verdict per axis · the two give the same rule citations · the naming cases match the verdicts fixed at L6 · neither judge's base commit carries the other's answer file · `J`: every disagreement is traced to the canon rule it exposes |
| `CN-r-1` | FWD-2 from the record | C3 | FWD-2 | `FWD2_FROM_RECORD.md` | each clause of FWD-2's ACCEPT line stands beside its evidence line, cited by path@commit: one sitting; enough beside every row; the pre-decided rows pre-filled · `04_SCOPE_TICKLIST.md` is read at HEAD and its v0.2 TICKED state is quoted · `J`: the evidence supports each clause |
| `CN-r-2` | FWD-3 from the record | C4 | FWD-3 | `FWD3_FROM_RECORD.md` | for each IRPT project, the row that ended its pause is cited with the branch it took · IRPT_BCKEND's PRD version at HEAD is read, and whether it carries the three CONTRADICTS is stated as measured · `J`: the record supports the branch named for each project |
| `CN-o-1` | the onboarding checklist | C5 | FWD-5 (instrument) | `infra/logic/10_ONBOARDING_CHECKLIST.md` | ordered steps from the identity row to the served dashboard · every step names the canon v1.0 rule it applies · every step names the builder or gate it uses, by LGIC_ENFORCE's CONTRACTS name · a step whose builder or gate is not yet built says so and names the cell that builds it |
| `CN-o-2` | the checklist's review | C5 | FWD-5 (instrument) | `CHECKLIST_REVIEW.md` | each step is marked MECHANICAL or JUDGEMENT, with a reason, by a worker who did not write the checklist · zero steps are marked JUDGEMENT · `J`: every mark's reason holds |
| `CN-n-1` | naming worker A | C7 | FWD-4 | `exercises/naming-a.tsv` | every item of the fixed naming job (§3a.3) carries a name taken from the registry (`infra/logic/registry/*.json`) and the schema, with the registry row cited · the record states its worktree base commit |
| `CN-n-2` | naming worker B | C7 | FWD-4 | `exercises/naming-b.tsv` | as CN-n-1, blind to it, spawned only after CN-n-1's branch drains (§8 choice 4) |
| `CN-n-3` | the naming comparison | C7 | FWD-4 | `exercises/naming-compare.md` | both outputs equal the canonical value fixed at L6 for each job, surface and slot · the refused or wrong-slot item is caught in both · a sanctioned LONG or SHORT form is never counted as a failure · neither base commit carries the other's answer file |
| `CN-l-1` | the ledger at v1.0 | C8 | FWD-6 | `infra/logic/06_CONFORMANCE_LEDGER.md` | a script recount of every row prints its instrument and denominator per section, and reproduces or corrects §7 · X2, X3 and X5 each name their decider · every CONDITIONAL entry carries its condition and its owner · decided against waiting is a column, and its counts are re-derivable by the script · `J`: no row reads as finished while part of it waits |

**Coverage of the PRD's candidates: 7 of 8 cut.**
- C1 → CN-k-1
- C2 → CN-j-1, CN-j-2, CN-j-3
- C3 → CN-r-1
- C4 → CN-r-2
- C5 → CN-o-1, CN-o-2
- C7 → CN-n-1, CN-n-2, CN-n-3
- C8 → CN-l-1
- **C6 is NOT CUT, on Andrew's word** (§0.1; gate G-N)

**Coverage of the outcomes: 5 of 6 by this round, and FWD-5's instrument.**
- FWD-1: CN-k-1, CN-j-1, CN-j-2, CN-j-3
- FWD-2: CN-r-1
- FWD-3: CN-r-2
- FWD-4: CN-n-1, CN-n-2, CN-n-3
- FWD-6: CN-k-1, CN-l-1
- **FWD-5:** CN-o-1 and CN-o-2 build and review its instrument. Its grade waits on G-N by his word, and this document does
  not count it as covered.

### Why the re-cuts

- **C2 → three cells, and C7 → three cells.** Two blind acts and a comparison each. A worker cannot compare its own blind
  answer, which is the LGIC_NAMING pattern.
- **C5 → two cells.** The PRD's fixture is *"a reviewer marks each step"*, and the author of a checklist cannot be the one to
  find its judgement step.
- **C1, C3, C4 and C8 stay whole.** Each is one act by one worker on one file.

### 3a. THE FIXED INPUTS L6 CUTS INTO THE FACES

1. **The judged tree** (CN-j-1 and CN-j-2, identically). **v2: the MDPF pipeline** (section 0b). It has the MIGRATE rows at
   `06_CONFORMANCE_LEDGER.md:98` (bronze) and `:100` (gold destination), and X1 GRANTED and PERMANENT at `:130`.
   - ~~v1: the ETFs pipeline, on `:102` and X4 at `:133`.~~ It fails DEC-2, because X4 is not a departure of `opal-data-etfs`,
     and that tree's own X3 and X5 are OWED.
   - L6 re-reads those rows at the issuance HEAD and states the exact path set. If CN-l-1 has already changed them, L6 takes
     them at the base the two judges share.
   - The five axes are the canon's §2.
2. **The naming cases** (at least 2, in the judges' faces; the expected verdicts ONLY in CN-j-3's face). Drawn from LGIC_NAMING's
   `GRADING_RULE.md` worked cases @`ce7349b7cc`: one CONFORMANT, and one ALIAS or OUT-OF-PATTERN whose verdict turns on the
   schema's content (a per-slot firm form or the refused `bd`), so the judge must resolve it from the canon's generated
   section.
3. **The naming job** (CN-n-1 and CN-n-2, identically; the canonical key ONLY in CN-n-3's face). The firm is 49 Financial,
   the one whose spellings diverged. At least:
   - a LONG case: the name of a 49 Financial data bucket, and a key's scope segment;
   - a SHORT case: a resource name for a 49 Financial Lambda;
   - a refused or wrong-slot trap: the Black Diamond integration's role for 49 Financial, where the vendor is `blackdiamond`,
     the firm is `49f`, and `bd` is refused.

   The key is derived at L6 from `NAMING_SCHEMA.json` v1.4 and `05_IDENTITY_SPINE.md`, the same derivation as LGIC_NAMING's
   N3_KEY.
4. **CN-l-1's instrument.** A recount script under the worker's own `deliverables/<serial>/`. The ledger's §7 counts are
   either reproduced or corrected by it; they are never re-typed.
5. **Row S1 and `3.0.0_SA_CVO`'s N4** are inlined into CN-k-1's face (§0.3, §0.4).

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP** (D14's `fabric_ruling`). Every surface is a document, a script or a record in this
workspace. **No cell is owned by a seat.** Every cell is served by a worker at L7 (`0.9.0_WK_LGIC_CANON~<n>`).

---

## 5. DEPENDENCY EDGES, LEVELS, AND THE DISTINCT-WORKER CONSTRAINT

```
  CN-k-1 --+--> CN-j-1 --+
           +--> CN-j-2 --+--> CN-j-3
           +--> CN-o-1 -----> CN-o-2
  [G-R: LGIC_ENFORCE cell r-1 merged] ==> CN-n-1 --> CN-n-2 --> CN-n-3
                                         (CN-n-1 --------------^)
  CN-r-1        (no edge)
  CN-r-2        (no edge)
  CN-l-1        (no edge)
```

| level | cells | width |
|---|---|---|
| 0 | CN-k-1, CN-r-1, CN-r-2, CN-l-1 | 4 |
| 1 | CN-j-1, CN-j-2, CN-o-1; CN-n-1 once G-R clears | 3 (+1) |
| 2 | CN-j-3, CN-o-2; CN-n-2 | 2 (+1) |
| 3 | CN-n-3 | 1 |

**The distinct-worker constraint:**

| cell | must not share a worker with | why |
|---|---|---|
| CN-j-1, CN-j-2 | CN-k-1, and each other | *"two workers who did not write the canon"*, blind to each other (DEC-2) |
| CN-o-2 | CN-o-1 | the reviewer cannot be the checklist's author |
| CN-n-2 | CN-n-1 | *"two people doing the same job"*, blind to each other (FWD-4) |
| CN-j-3, CN-o-2, CN-n-3 | the cells they compare or review | a scorer is never the worker it scores |

⚠ **The preloaded-context disclosure applies here.** It was measured on LGIC_NAMING: row LGIC_NAMING-W6-S1, disarmed by
LGIC_NAMING-S12 @`3d671ff59c`. Every worker in this fabric loads the workspace CLAUDE.md and the auto-memory before its
first tool call. CLAUDE.md carries estate law, including Rule 17b and the firm tokens.
- So CN-j-1 and CN-j-2's *"briefed with the canon alone ... no prior knowledge"* (DEC-2), and CN-n-1 and CN-n-2's blindness
  to each other, are partly by instruction.
- Mutual blindness is checked mechanically by the base-commit criteria. Blindness to the estate is NOT-EVALUATED.
- The disclosure rides into every blind face and into L9. The remedy, if one is ruled, is LGIC_NAMING's round-N analysis's.

**The fan-out:** up to 4 at level 0 and 3 at level 1, well under the cap of 8 that `1.0.0_SA_CTO`'s rec (96626) sets across
the whole sequence. L6 states N against the live count at issuance. A slotting (L6's to choose and defend):

| slot | cells | spawned |
|---|---|---|
| 1 | CN-k-1 | at issuance |
| 2 | CN-l-1 | at issuance |
| 3 | CN-r-1, then CN-r-2 | at issuance |
| 4 | CN-j-1 | after CN-k-1 drains |
| 5 | CN-j-2 | after CN-k-1 drains, from slot 4's base |
| 6 | CN-o-1 | after CN-k-1 drains |
| 7 | the scorer: CN-j-3, CN-o-2, CN-n-3, each as its inputs drain | when the first input drains |
| 8 | CN-n-1; then CN-n-2 in a NEW spawn after CN-n-1 drains | after G-R |

---

## 6. BATTERY DISPOSITION

### `comp-adversary`: RUN

The run was over the PRD at read-vintage HEAD @`8d1d4d3e2f`, 2026-09-14T18:18:35Z:

| source | denominator | result |
|---|---|---|
| cited-commit verification | 11 attempted | **11 verified, 0 unverifiable** |
| cited-path vintage | 17 attempted | 13 stable, 2 MOVED-SINCE-AUTHORING, 2 GONE |

All four flags are resolved in §1. **Blindness:** `T11: decomposition neighborhood NOT RESOLVED`, so the complement is
filesystem adjacency, not the dependency chain.

### `comp-schedule`: RUN (the same-hour estate view)

`comp-schedule --budget 540` was run by this seat at ~17:4xZ for LGIC_ENFORCE's cut (the view is compiled at read time; nothing
is stored). It scanned **5 of 5 carriers** within budget (C1 230, C2 6, C3 12, C4 21, C5 334): **25 gates armed, 0 lines
naming LGIC_CANON** or any other sequenced project. It is cited, not re-run, because the view is under an hour old and this
project adds no carrier.

**The promises-to-check-later this project creates:**

| gate | owner | the condition that clears it |
|---|---|---|
| **G-C** worker admission | `2.0.0_SA_COO~G` | after the issuance commit, `owned-paths-validate --check-agent` on HEAD bytes PERMITs each slot on a named path and REFUSES it on an unnamed one |
| **G-R** the registry exists | `LGIC_ENFORCE`'s COO lane (this lane) | LGIC_ENFORCE cell r-1 merged (`infra/logic/registry/*.json` at HEAD). CN-n-1 is spawned only then. It is DEC-5's *"waits on it existing"*, as a driven edge, not a wait: that cell sits at level 1 of LGIC_ENFORCE's DAG |
| **G-N** a genuinely new firm | Andrew (his ~13:4xZ word) | a true new-firm act exists. C6 is then cut, and FWD-5 is graded on it. Until then, FWD-5 is EXPRESSLY held, with the reason and his word |

### `comp-iam`: DECLARED-NOT-APPLICABLE

The reason is measured on the write set: three documents in `infra/logic/`, one render script that reads the schema and writes
a section of one document, and records under `deliverables/`. DEC-9 moves nothing. No cell adds an operation, a policy, a
principal or a resource, so the lens would receive an empty input, and a vacuous pass reads as clean. ⚠ The bound on that
reason: the checklist (CN-o-1) DESCRIBES the fence and IAM steps, which LGIC_ENFORCE's cells apply, and their IAM surface is
LGIC_ENFORCE's battery.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is §1's subtraction: 8 manifest rows, each placed once (1 excluded,
1 read-only, 1 not executed here, 1 another seat's, 4 surfaces), falsified against every cited path.
- **Exhaustive:** 7 of 8 candidates are cut, and the eighth is not cut on Andrew's word, stated (§0.1).
- **Mutually exclusive on files:** yes. The register's entries and its schema get one home each (§8 choice 2).

**(ii) SAME GRAIN.** Every cell is one act by one worker producing one document, script or record, graded by a match or a
CVO judgment.

**(iii) INTENT COHERENCE.** One axis: **write the rule down so a seat can answer from it**, and prove that by blind use. No
cell enforces anything (LGIC_ENFORCE), names anything new (LGIC_NAMING), or moves anything (the migration projects).

**(iv) STATE COHERENCE, and what each remedy does NOT move:**
- CN-k-1 moves the canon's words and its generated section. It does **not** move `NAMING_SCHEMA.json`: a naming defect it
  finds is a row against LGIC_NAMING, never an edit.
- CN-l-1 moves the ledger's counts and deciders. It does **not** move a plane; every MIGRATE or RETIRE stays a separate
  project under R19.
- CN-o-1 moves the checklist. It does **not** grade FWD-5, which waits on G-N.
- CN-r-1 and CN-r-2 move nothing but records; they grade from what is already on file.

---

## 8. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

Each is this seat's call at L5, revertible at the round-N analysis.

1. **C6 is not cut.** This is Andrew's word applied, not this seat's choice (§0.1). It is listed so a reader looking for C6
   finds it here.
2. **The exception register gets one home for its entries (the ledger's §6) and one for its schema (the canon's §4).** Today
   the canon's §4 carries the first entries and the ledger's §6 carries them again: two carriers of one list.
3. **DEC-2's READING is a ledger row that breaks a rule plus a DECLARED EXCEPTION.** It was ruled to stand (96677) and is
   written into PRD v1.2 and v1.3. **The TREE is MDPF (v2, section 0b).** v1's ETFs choice failed on grain (row LGIC_CANON-S2).
4. **FWD-4's *"on different days"* is read as two workers in separate contexts, CN-n-2 spawned only after CN-n-1 drains**, so
   the two never run at once. It is not read as a calendar day, which would be a wait with no stated reason, forbidden by
   Rule 27. If Andrew or `1.0.0_SA_CTO` means a calendar day, it is a qualified wait and a row.
5. **The checklist names builders and gates by LGIC_ENFORCE's CONTRACTS names**, and marks the ones not yet built with the
   cell that builds them. So it does not wait on LGIC_ENFORCE landing.
6. **C5 has a separate reviewer cell** (CN-o-2), and **C2 and C7 each have a separate scorer.**

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **FWD-5 is not covered by this round.** Its instrument is; its grade waits on G-N by Andrew's word.
2. **Blindness to the estate is NOT-EVALUATED** for the judges and the naming workers (§5). The base-commit checks cover
   only mutual blindness.
3. **The MDPF tree's rows were read at the v2 cut** (`:98`, `:100`, `:130`). CN-l-1 may change them in the same round, and L6
   pins the base the judges share.
4. **Worker admission is not exercised** (G-C).
5. **No cell has been exercised.** No effort or duration estimate appears here, deliberately.
