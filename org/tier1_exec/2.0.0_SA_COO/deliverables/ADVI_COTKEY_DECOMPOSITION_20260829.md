# ADVI_COTKEY -- COO ATOM-DECOMPOSITION (stage 3)

**Issuer:** `2.0.0_SA_COO` · **Clock:** 2026-08-29T15:2xZ · **Directive:** D2 · **Certifier of record:** `3.0.0_SA_CVO`
**Stage-2 input:** `docs/architecture/ADVI_COTKEY_PRD.md` (125 lines, read in full at this seat)
**Sovereign precondition: SATISFIED.** PRD s.3 key-of-record RULED by Andrew 2026-08-26 ~20:39Z, CALL 3 APPROVED --
*key of record = `Portfolio Group` (BD template 270648), value = advisor, `No Advisor` = an explicit unassigned book*;
record `deliverables/ANDREW_DIRECT_20260826_2039Z_FOUR_RECS_APPROVED_CATVIEWS_TODAY_WEALTHSCAPE_HAR.md`.
**No ruling open at Andrew.** Verified at the project record this tick, not carried from memory.

> **THIS DOCUMENT IS THE CELL SET. TOs ARE CUT FROM CELLS AND FROM NOTHING ELSE (Rule 27).**
> It is not a TO, not a build authorization, and not a serve authorization -- see s.5.

---

## 1. DECLARED DOMAIN (the thing the cells must be MECE over)

**The six operative surfaces named in PRD s.4, and only those:** (1) the silver key surface `account_attributes`;
(2) the producer `A_01.advisor_assignments.py`; (3) the book grain (group dim + membership bridge); (4) the consumers
that flip one book to four; (5) the tie-out oracle; (6) the downstream bindings.

⛔ **SURFACE 6 IS DECLARED OUT OF THIS DECOMP'S CELL SET, BY THE PRD'S OWN WORDS** -- *"Each is that project's own cell,
referencing this key -- this PRD does not enumerate them."* PERFRP's Cottonwood invocation, D3's Cottonwood models plane
and the ADVI_INSURE port are cells of THEIR projects. **Naming the exclusion so the domain is closed and the omission is
a decision rather than a gap.**

---

## 2. THE CELLS

| cell | act | owner class | discharges | inputs / sequence |
|---|---|---|---|---|
| **K-1** | **Observe the `account_attributes` schedule** -- is the daily pull ALREADY scheduled? An OBSERVED-schedule read (the fired cadence), never a plan read; plus snapshot semantics (0 rows = FREEZE) and the two-row multi-book form confirmed at the artifact. | DS | **P4** | none -- startable now. Answers PRD open-Q3. |
| **K-2** | **Read the BD Portfolio Group TREE** -- are the four values leaf groups of a larger tree, and is `No Advisor` a real group or BD's rendering of "no group"? One qt6/template read on the EXISTING cot session bundle. | DS | feeds K-4 | none -- startable now. Answers PRD open-Q2. |
| **K-3** | **Rule the multi-book account** (1 of 942, K6) -- EITHER add BD dim 436 `Primary Portfolio Group` to template 270648 (vendor-side re-pull) OR a DECLARED keep-first. ⛔ **Inventing `is_primary` from the name is ILLEGAL (49F precedent, K12).** The rule is PRINTED on the artifact, never silent. | DS | **P3** | after K-2 (the tree read may make dim 436 moot). Answers the PRD s.3 sub-question. |
| **K-4** | **Re-key the producer** `A_01.advisor_assignments.py` from `portfolio_group`: advisor = group, slug to `advisor_key`, `No Advisor` to the unassigned class; the synthetic-bridge guard RETIRES ITSELF on the run the real key lands; SCD history start DECLARED point-in-time-only before the first partition (2026-08-19) and STAMPED on the artifact. | DS | **P1 (build half), P6** | after K-2, K-3. |
| **K-5** | **Instantiate the book grain** -- group dim + membership bridge, **NO money on the bridge**, book figure at group grain ONLY. 49F pattern RE-INSTANTIATED under `data/cot/**`, never referenced across trees. | DS | (P5 constraint) | after K-4. |
| **K-6** | **Build + run the tie-out oracle** -- a qt6 "BI Billing" group-grain read on the existing cot BD session bundle (the `oracle_book_tieout_qt6.py` pattern re-instantiated): does our per-advisor book equal what that advisor sees in Black Diamond, for each of the three persons. Tolerance DECLARED by this cell. NEVER-sum-across-groups caveat carried in the oracle's own frame. | DS | **P2** | after K-4. **Read-only; the existing session bundle is the vehicle -- NO new egress.** |
| **K-7** | **Flip the consumers one book to four** -- `C_08`, `D_00c`, `D_02`, `D_04`, `D_00b`/`C_07`. Every per-advisor figure the Cottonwood tenant renders changes. | DS | **P1 (consumer half)** | after K-4 + K-6 PASS. |
| **K-8** | **Verify the tenant render on four books** -- `cottonwood/layout.ts` advisor-drill flags have been on since COTPPLADVFIX, so **expected code change is ZERO**; the deliverable is a RENDERED READ proving four books render, not an assumption that they do. | DE | **P7** | after K-7. |
| **K-9** | **Certification** -- decomp cert; proof-of-spec on each cell return; **the tie-out is the SEMANTIC axis**, not a row count. | CVO | all | per-return. |

**AE-class: NOTHING. Stated as a DECISION, not an omission** -- the cot chain is already scheduled and this remedy adds
no resource (PRD s.7). ⛔ **If K-1 measures the daily pull as NOT scheduled, that becomes an AE act and this line is
WRONG** -- which is exactly why K-1 is an observed-schedule read and is sequenced first.

---

## 3. RULE 24 FOUR-POSTULATE RECORD (a cell set is a schema)

- **(i) MECE over the declared domain.** Surfaces 1-5 of PRD s.4 map onto K-1..K-8 with no surface unclaimed and no cell
  spanning two surfaces; surface 6 is declared OUT (s.1). ⛔ **The uncovered member I hunted and did NOT find a home for:
  the `platinum/advisors/` SERVE act inside P1 -- see s.5. It is deliberately not a cell.**
- **(ii) SAME GRAIN.** Every cell is ONE lane's act with ONE artifact and its own acceptance. K-1 and K-2 are reads;
  K-3 is a ruling; K-4..K-7 are builds; K-8 is a verification; K-9 is certification. **No cell is a phase or a milestone.**
- **(iii) INTENT COHERENCE -- one axis: "what must be TRUE of the Cottonwood advisor key before it can be served."**
  ⛔ **P5 (no cross-tree reference; bd/cot gate + IAM unchanged) is NOT a cell and is not on this axis. It is a BINDING
  CONSTRAINT on every cell**, and folding a constraint into the member list is the intent-incoherence this postulate
  names. It is discharged by each cell's own gate, not by a cell of its own.
- **(iv) STATE COHERENCE -- which values one remedy does NOT move.** K-4 landing does NOT move K-1's schedule finding
  (a producer re-key cannot schedule a pull), does NOT move K-8's render state (flags are portal-side), and does NOT
  move P2 (the tie-out is an independent instrument and must be RUN, not inferred from a successful build).
  ⛔ **The tempting error this postulate blocks: reading a green K-4 as evidence for P1 in full. K-4 discharges the
  BUILD half only.**

---

## 4. ACCEPTANCE COVERAGE -- every property has a home, and the denominator is printed

```
  P1  four advisor values + 944 accounts + zero stray Unassigned   -> K-4 (build) + K-7 (consumers)   [SERVE half: s.5]
  P2  per-advisor AUA ties to the qt6 group-grain read             -> K-6
  P3  multi-book account handled by a NAMED, PRINTED rule          -> K-3
  P4  account_attributes lands DAILY, observed; start date stamped -> K-1
  P5  no cross-tree reference                                      -> BINDING CONSTRAINT on all cells (not a cell)
  P6  synthetic bridge retires by its own guard, no parallel path  -> K-4
  P7  Tier-B interface contract is Inflection's, no cot-specific   -> K-8
                                                    DENOMINATOR: 7 of 7 properties assigned, 0 orphaned
```

---

## 5. ⛔ THE SERVE LIMB IS NOT AUTHORIZED BY THIS DECOMP, AND I AM NOT ASSUMING IT IS CLEAR

P1's second clause -- *"and `platinum/advisors/` serves four prefixes"* -- is a **SERVE** act. `1.0.0_SA_CTO` 82953
measured that across `ADVI_BDPARITY`, `ADVI_INSURE` and `ADVI_PERFRP` the D2 hold tokens land on the **SERVE limb every
time**, behind **ONE shared arm-(a) sovereign gate**, and that *"seats can advance BUILD work on these projects but
CANNOT CLOSE them."* ✅ **`ADVI_COTKEY` was measured in that same scan as one of only TWO hold-token-free projects in
scope.** ⛔ **That is a PROJECT-LEVEL reading, and that seat stated its own bound: a project-level token says nothing
about a specific TO.** **So: every cell above is BUILD-class and legal now. The serve step is NOT a cell, is NOT
authorized here, and gets its own gate read at the moment it is proposed** -- by whoever proposes it, against the
arm-(a) gate, not against this document. **Naming it because a decomp that silently contained a serve act would be an
authorization nobody issued.**

---

## 6. SEQUENCE AND WHAT IS STARTABLE NOW

```
  NOW (no predecessor):        K-1, K-2         <- both are READS, both answer a PRD open question
  after K-2:                   K-3
  after K-2 + K-3:             K-4
  after K-4:                   K-5, K-6
  after K-4 + K-6 PASS:        K-7
  after K-7:                   K-8
  per-return:                  K-9
```
**SEAT REQUIREMENT: ONE DS-class lane (Rule 27 -- one project per instance).** The PRD names it: *"the remedy needs a
DS-class measuring/building lane on spawn (one project); the cot BD session bundle is the existing read vehicle."*
⛔ **NO SEAT IS ASSIGNED BY THIS DOCUMENT.** Seating is a `/mstr-spawn` act against measured headroom (`0.0.0_AB_MSTR`
82887: **11 slots, not the 1 its own skill doc's stale cap implied**), and it is sequenced against the other live COO
carry-forward -- the `0.4.0_DS_ClientPlatform` base respawn that roots the BDPARITY chain. **Which of those two takes a
slot first is a prioritisation call, and it is not made here.**

---

## 7. WHAT THIS DECOMP IS NOT

Not a TO. Not a build authorization (a cell becomes work when a TO is cut from it and a GO issued). **Not a serve
authorization (s.5).** Not a re-opening of the bd/cot separation or the uniformity law. **Not a seat assignment.**
