# NFRA_REPORT -- L5 decomposition, ROUND 3 -- v0.1

**Seat:** `2.0.0_SA_COO~ZZ` · **Limb:** L5 (recut) · **Round:** 3
**Input:** `1.0.0_SA_CTO~Z`'s round-2 analysis @`2b44f4a62b`
(`org/missions/D12/NFRA/NFRA_REPORT/ledger/ROUND_ANALYSIS.round2.md`), answering the slug
`surprise-channel/remediations/REMEDIATION_v1.Z.md` @`4fe64b8cac`
**PRD:** `NFRA_REPORT_PRD.md` at **v0.7**, manifest 13 rows · **archetype:** COORDINATE

**ROUND 2 IS `L10 answered` AND RECUTS. Eleven of twelve outcomes REALIZED; `FWD-4` alone cannot.**
Round 2's seven cells are terminal and none is reopened. Cell ids continue the `RP-s-<n>` sequence
from **20**, so no id is ever reused.

---

## 0. THE FINDING AT THE CUT THAT RESIZES THE ONE CELL

The analysis §3 describes `R3-1` as bringing `ATTRIBUTION.md` to v0.7 -- fixing two rows that render
`UNGROUPED` and a line 30 that still reads "OPEN CALL AT ANDREW". That is **limb A and it is correct.**

⛔ **MEASURED AT THIS CUT: THE RENDERED EDITION CARRIES NO ATTRIBUTION AXIS AT ALL.** Not a stale
axis -- an absent one.

```
EDITION_SPECIMEN.md sec.2, the row table's own header, and compose_edition.py:428 which emits it:
  | Property (`QUOTED`) | Previous state | This edition | Delta (`COMPUTED`) | Citation |
  -> FIVE columns. There is no attribution column.

census of the RENDERED edition for 'UNGROUPED|Dashboard|Website|Gateway|Graph':
  10 hits / 104 lines / 35 sections -- and ZERO is an axis VALUE.
  "Website security" is a row SUBJECT; "API Gateway" is a service NAME; the sole "Dashboard"
  is inside the function name getPlatinumFirmDashboard.
compose_edition.py census of the same terms: 33 hits, ALL of them `"property": "<description>"`
  -- the row's subject, never a Dashboard|Website|Gateway|Graph|UNGROUPED value.
```

**So `FWD-4`'s bar -- "every finding rolls up to a NAMED part of the business with an owner" -- is not
served by the artifact a reader actually reads.** Fixing `ATTRIBUTION.md` alone would bring the LAW to
v0.7 and leave the EDITION with no attribution at all, and the outcome would still not grade.

⭐ **AND NEITHER ROUND-2 CELL IS AT FAULT, which is why this is a resize and not a finding.**
`ATTRIBUTION.md` says so in its own words: *"the per-row rendering of every finding this axis governs,
is the composer's act (`RP-s-15`, `S2`), not this cell's."* `RP-s-13` correctly deferred the rendering;
`RP-s-15` was never told to render it. **The gap is between two correctly-executed cells, and it is
exactly the gap the analysis's own warning points at** -- "a criterion that greps the composer for a
four-member list would pass while the rendered artifact still shows UNGROUPED." The truth is one step
worse than the warning: the rendered artifact shows neither.

**CONSEQUENCE: `RP-s-20` carries BOTH limbs.** They are one outcome, and limb B is meaningless without
limb A -- you cannot render an axis whose members the law document has not ratified.

---

## 1. The rectangle -- ONE cell, `RP-s-20`

**CELL STATUS VOCABULARY** (unchanged, rule 24 record at round 1): `NOT-EVALUATED | OPEN | IN-FLIGHT |
HELD | COMPLETE | CLOSED`. `RP-s-20` reads `OPEN`; none reads `NOT-EVALUATED` (1 of 1 evaluated).

| cell | row | outcome | act | round | slot |
|---|---|---|---|---|---|
| `RP-s-20` | S13 | FWD-4 | the attribution axis at PRD **v0.7** -- FOUR ratified members in the LAW, **and rendered per row in the EDITION**, with `UNGROUPED` surviving as the sentinel for a live surface outside all four | A | ~1 |

### 1a. THE CELL ID IS `RP-s-20`, NOT `R3-1`, AND THAT WAS MEASURED

The analysis labels the cells `R3-1` / `R3-2`. **`R3-1` is REFUSED by the proof gate's own id
grammar.** Measured against `.tools/proof-of-spec-check.py::CELL_ID_RE`, imported and applied:

```
  RP-s-20   -> MATCH        RP-s-13  -> MATCH   (positive controls, one of them a landed round-2 id)
  R3-1      -> refused      bogus id -> refused (negative controls -- the matcher discriminates)
```

A cell cut as `R3-1` would have failed its own proof instance at L7. The analysis's labels are prose
handles; the project's id grammar is `RP-s-<n>` and it continues unbroken from round 2's `RP-s-19`.

---

## 2. `R3-2` IS AN L6 CUT MECHANIC AND IS NOT CUT AS A CELL

The analysis §3 names two cells. **This decomposition cuts ONE, and records why rather than departing
silently.**

`R3-2` is *"round 3's cut derives the deliverable folder from `<issued_to>`"*, and the analysis itself
says in the same breath: ***"This is an L6 mechanic and is cheap at the cut; it is expensive to
retrofit."*** An L6 mechanic is something the ISSUER does when writing the orders. There is no worker
ACT in it:

- it is not a build -- the remedy is a path string in the order this seat writes;
- it is not a retrofit -- the analysis rules retrofit out by cost, so no worker moves round 2's files;
- a cell asking a worker to verify the folder its own order named would be circular, and grading the
  issuer's artifact is the CVO's limb, not a worker's.

**HONOURED, NOT DROPPED.** `RP-s-20` is issued to `0.9.0_WK_NFRA_REPORT~1` and its deliverable folder
is `deliverables/0.9.0_WK_NFRA_REPORT~1/` -- derived from `<issued_to>`, which is the whole of `Z-S8`'s
remedy. §7 asks for "ONE issuance covering R3-1 and R3-2"; this issuance covers R3-2 by construction.

⚠ **REVERSIBLE AND ROUTED.** L5 is this lane's limb and the analysis is input rather than a
decomposition, but this is a departure from its literal count and `1.0.0_SA_CTO~Z` is told in this
lane's one send. If that seat reads `R3-2` as needing a cell, it says so and one is cut next tick.

⛔ **THE ONE-CELL ROUND IS ALSO WHY THIS IS WORTH STATING.** With `R3-2` folded into the cut, round 3
is a single cell -- and a reader comparing "two cells" in the analysis to one order in the tree would
otherwise read a dropped cell.

---

## 3. Dependency edges

```
  RP-s-20 <- (none)        <-- SINGLE READY ROOT

  dependency-INDEPENDENT chains (weakly connected components):  M = 1
    A = {RP-s-20}
```

**FAN-OUT: `1 of 1 chains, cap 8`.** `N` is bounded above by `M`, and `M = 1`, so a one-slot issuance
is the only legal width. **The cap is stated, never silent.**

⚠ **ROUND 2'S FAN-OUT LESSON DOES NOT APPLY HERE AND IS NOT INVOKED.** That lesson was to size on the
POST-UNBLOCK width -- round 2 had a critical cell that opened three chains when it landed. `RP-s-20`
has no dependents at all: nothing opens when it completes, because it is the last uncovered limb of
the last un-realized outcome. **There is no post-unblock width to size for**, and claiming one would
manufacture a second slot with nothing to put in it.

**ROUNDS BY DEPTH: A=1.** Max width 1, inside the default cap of 8.

---

## 4. Rule 24 four-postulate record

| postulate | how this rectangle satisfies it |
|---|---|
| **(i) MECE over a DECLARED domain** | Domain DECLARED: the outcomes the round-2 analysis grades NOT REALIZED. Denominator 12 outcomes, 11 REALIZED, **1 not** -- so the domain is `{FWD-4}`, and one cell covers it. **Uncovered member hunted:** the analysis's UNCOVERED partition is EMPTY (0 of 12) and `FWD-8`'s box-grain limb is out of scope by a prior analysis, so there is no uncovered member to find. Backward: 1 cell, 0 orphans. |
| **(ii) SAME GRAIN** | One cell, so grain is trivially uniform -- and it is stated rather than skipped: the grain is `(manifest row, outcome)` = `(S13, FWD-4)`, the same grain rounds 1 and 2 used. |
| **(iii) INTENT COHERENCE** | One axis, one intent: bring `FWD-4`'s attribution to the ratified v0.7 axis **in the artifact a reader reads**. Limbs A and B are not two intents -- they are the law and its application, and the outcome's bar needs both. |
| **(iv) STATE COHERENCE** | The remedy moves `FWD-4` from NOT REALIZED toward gradeable. ⛔ **NAMED: what it does NOT move** -- it does not move `FWD-1/3/7/12`'s `EXERCISED` bars, which need editions RUN and READ on real trading mornings and cannot be moved by any cell; and it does not move `FWD-8`'s box-grain limb, which is Andrew's billing decision. |

---

## 5. BATTERY DISPOSITION -- RE-RUN AT THIS CUT

**`comp-schedule` -- RUN at this cut, 5 of 5 carriers, 20.3 s.**
`C1=23 C2=6 C3=12 C4=20 C5=335`. **2 gates ARMED: `G-3` (owner CTO), `G-7` (owner POD4) -- NEITHER is
this project's, and neither binds `RP-s-20`.**
⚠ `C2` moved **7 -> 6** since the round-2 cut. Stated because round 2's orders carry `C2=7` and a
reader comparing the two should see a real change rather than a transcription error.

**`comp-iam stats` -- RUN at this cut.** 195 roles parsed, 188 services scanned, 1084 operations,
**304 permission gaps**. ⛔ **IT DOES NOT BIND `RP-s-20`** and is recorded for the denominator only:
the cell writes one markdown law document and one local python composer, and touches no IAM surface,
no role and no AWS plane. `comp-iam`'s standing BLINDNESS to `wafv2` is carried and is likewise
irrelevant here.
⚠ These figures are NOT comparable to round 2's `836 calls / 96 roles / 31 services` -- that was a
different subcommand over a different denominator. Recorded as what was actually run.

**`comp-adversary` -- RUN on this document at the cut; its grid is in the issuance commit.**

**FINDINGS THAT STILL BIND, carried:**
- **The alerting moratorium is ARMED** (1 of 12 NEVER clauses). `RP-s-20` mints no alarm, topic,
  subscription or notification. It renders an attribution column; it raises nothing.
- **The MAIN-CHECKOUT CENSUS CONSTRAINT**, ruled at msg 20822 and durable in `project.json` `blocking`
  fact (6) @`cf3e8fa7f6`: any census or absence claim is run from the MAIN checkout, never from the
  worker's own linked worktree, and a comp-rail zero obtained inside a worktree is **not evidence of
  absence**. Citable at `org/modules/graph/INSTRUMENT_LIMITS.md` LIMIT 4 / 4a. **This travels in the
  worker face.**
- **Denominator hygiene:** do not compute a coverage figure off the EC2 manifest's row count -- 27
  entries, 26 with an id, **25 distinct**. Not touched by this cell, carried so the round does not
  lose it.

---

## 6. What this decomposition REFUSES to assume

1. **That the analysis's cell COUNT binds L5.** It is input. One of its two items has no worker act;
   that is recorded in §2 and routed, not silently dropped.
2. **That the analysis's cell LABELS are ids.** `R3-1` is refused by the gate's own matcher, measured
   with controls (§1a).
3. **That `ATTRIBUTION.md` is the whole of `FWD-4`.** The rendered edition carries no attribution
   column at all (§0) -- measured, not assumed, and it is the reason the cell has two limbs.
4. **That a word-presence grep can score this cell.** It is the one cell where that instrument
   demonstrably fails, by the analysis's own warning and this lane's own 18-of-24 self-measurement.
   The criteria score the RENDERED EDITION.
5. **That round 3 completing closes the project.** `FWD-1/3/7/12` are `EXERCISED` bars needing real
   mornings RUN and READ. **A cell can produce the edition; it cannot produce the reading.**
6. **That a one-cell round should be padded.** Six outcomes were REALIZED at round 2 and re-cutting a
   realized outcome for tidiness is work that cannot improve a grade.

---

## 7. Holds

- **NONE held by this lane.** `RP-s-20` is cuttable at this edit.
- `FWD-4`'s member names are **RULED AND CLOSED at v0.7** (Dashboard | Website | Gateway | Graph,
  Andrew-direct) -- the open call that made round 2's cell render `UNGROUPED` is gone, which is
  precisely what makes this cell cuttable now and was not true then.
- ⛔ **`FWD-8`'s BOX-GRAIN limb is OUT OF SCOPE by the round-2 analysis §2 and is NOT re-raised.**
  Row `Z-S4` INERT; blocked on Andrew's payer-account billing setting.
- ⛔ **The two structural findings in the analysis §5 (the slug's W-coordinate refusal; the resolver
  clock-collapse) are NOT absorbed by this recut.** Both are held at `1.0.0_SA_CTO~Z`, both unownable
  until a CRO exists to open the comp-tool L1, and **no gate edit is authorized by any of it.**
