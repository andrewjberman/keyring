# NFRA_REPORT -- L5 decomposition, ROUND 2 -- v0.1

**Seat:** `2.0.0_SA_COO~ZZ` · **Limb:** L5 (recut) · **Round:** 2
**Input:** `1.0.0_SA_CTO~Z`'s round-N analysis @`9dae635237`
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md`)
**PRD:** `NFRA_REPORT_PRD.md`, manifest 13 rows · **archetype:** COORDINATE

**ROUND 1 IS CLOSED AT L10. Six of twelve outcomes REALIZED** (`FWD-2/5/6/9/10/11`); six not
(`FWD-1/3/4/7/8/12`). This is a CLEAN RECTANGLE -- round 1's twelve cells are terminal and none is
reopened. Cell ids continue the `RP-s-<n>` sequence from 13 so no id is ever reused.

---

## 0. THE CENTRAL FACT THIS RECUT IS BUILT ON

⛔ **ROUND 1 BUILT TWELVE ENGINES AND NINE OF TWELVE BARS CANNOT BE MET BY AN ENGINE.** Three bars are
`APPLIED`; **nine are `EXERCISED`**, and an `EXERCISED` bar asks whether the report has RUN and someone
has READ the answer. **Round 1 could not have closed this project however well it executed.**

⭐ **THAT IS THE BARS WORKING, NOT A PLANNING ERROR.** The project was commissioned over a report that
ran daily and said the same alarming thing every time -- an artifact that exists and is not read.
`EXERCISED` was chosen per-outcome and Andrew-confirmed to make exactly that ungradeable. **Six
NOT-REALIZED are not six failures**, and this decomposition does not treat them as such.

**SO ROUND 2'S CENTRE OF GRAVITY IS THE RUN, NOT MORE SPECIFICATIONS.** `FWD-1`, `FWD-3`, `FWD-7` and
`FWD-12` reduce to getting real trading-morning editions produced and read.

⛔ **AND THE RUN NEEDS AN ENGINE THAT DOES NOT EXIST.** round 1's coverage cell established it and this lane
re-measured it at the cut: **every report-content manifest row is verb `wire` with claim `absent`** --
round 1 produced SPECIFICATIONS (`STATE_MODEL.md`, `ROW_STRUCTURE.md`, `VERDICT.md` and the rest), not
a thing that runs. *"Not more engines"* in the analysis means **not more spec documents**; the run
requires the composer that turns those specs into an edition. That is `S2`'s own `wire` verb.

**NO NEW MANIFEST ROW IS REQUESTED, and that was measured rather than assumed.** `S2` carries "the
report ARTIFACT" (`wire`, `absent`) and `S3` carries "SCHEDULE and DELIVERY" (`align`, `measured`).
Between them the composition and the delivery of an edition are already carried. **Inventing a row
would be an L4 act and is not this lane's** -- which is the `FWD-4` lesson applied in the other
direction.

---

## 1. The rectangle -- SEVEN cells, `RP-s-13`..`RP-s-19`

**CELL STATUS VOCABULARY** (unchanged from round 1, rule 24 record there):
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`. All seven read `OPEN`; none reads
`NOT-EVALUATED`, and that is a measurement (7 of 7 evaluated).

| cell | row | outcome | act | round | slot |
|---|---|---|---|---|---|
| `RP-s-13` | S13 | FWD-4 | the PROPERTY+OWNER ATTRIBUTION axis and its mandatory rendered `UNGROUPED` value -- **the only structurally uncovered outcome of round 1** | A | ~2 |
| `RP-s-14` | S1 | FWD-2 | AMENDMENT (a): a fully-applied row renders an EXPLICIT value on the third axis; absence may not carry meaning | A | ~3 |
| `RP-s-15` | S2 | FWD-3 | **BUILD THE COMPOSER** -- the engine that turns round 1's specifications into a real edition, carrying the per-row delta against the previous one | A | ~1 |
| `RP-s-16` | S3 | FWD-1 | RUN it on trading mornings and DELIVER before Andrew's morning -- real editions, not a dry run | B | ~1 |
| `RP-s-17` | S4 | FWD-1 | the VERDICT rendered in a real edition, checkable against that edition's own rows | B | ~3 |
| `RP-s-18` | S8 | FWD-7 | the RETIREMENT ROUND-TRIP: something retired, and the NEXT edition stops raising it | C | ~1 |
| `RP-s-19` | S12 | FWD-12 | the ANOMALY BREAKDOWN in a real edition, plus AMENDMENT (b): `C-AI`'s grain is the REPORT | B | ~2 |

### 1a. Why `S2/FWD-1` gets NO separate cell, stated rather than omitted

The `(row, outcome)` one-cell rule this lane accepted would give `S2` two cells -- it names `FWD-3`
AND `FWD-1`. It gets one. **The rule's own stated exception applies and it is measured:** `FWD-1` is
carried by DEDICATED rows `S3` and `S4`, both of which have cells here (`RP-s-16`, `RP-s-17`), so a
partial cut of `S2` **cannot orphan it** -- which is exactly what was NOT true of `FWD-4`, carried by
`S1` alone, and is why round 1 lost it. The rule is applied WITH its exception rather than mechanically.

### 1b. What is NOT in this rectangle, and why

⛔ **`FWD-8`'s BOX GRAIN. NOT IN SCOPE, by the analysis §5.5.** Blocked on resource-level Cost Explorer
being opt-in DISABLED at the payer account -- a billing decision that is Andrew's -- and NOT on the
compute manifest, which `D3` wrongly assumed. Row `Z-S4`, already disarmed INERT. **A cell cut against
it could not pass and would manufacture a false blocker.** `FWD-8`'s SEGMENT limb is REALIZED and
untouched.
⛔ **`FWD-5`, `FWD-6`, `FWD-9`, `FWD-10`, `FWD-11`, `FWD-2` get no new cell.** All six are REALIZED.
Re-cutting a realized outcome for tidiness is work that cannot improve a grade.

---

## 2. Dependency edges, keyed to OBSERVED completion

```
  RP-s-13 <- (none)        RP-s-14 <- (none)        RP-s-15 <- (none)     <-- THREE READY ROOTS
  RP-s-16 <- RP-s-15
  RP-s-17 <- RP-s-15
  RP-s-19 <- RP-s-15
  RP-s-18 <- RP-s-15, RP-s-16

  dependency-INDEPENDENT chains (weakly connected components):  M = 3
    A = {RP-s-15, RP-s-16, RP-s-17, RP-s-18, RP-s-19}   B = {RP-s-13}   C = {RP-s-14}
```

⛔ **ONE EDGE WAS REMOVED AT THE CUT BECAUSE IT WAS NOT REAL, and it mattered.** A first draft of this
list carried `RP-s-19 <- RP-s-13` -- the anomaly breakdown depending on the attribution axis. **It does
not.** The breakdown answers *what feeds this, what reads it, what else is affected*; the attribution
axis answers *which part of the business owns it*. Different questions, no ordering between them.
**With the false edge, `M` collapses to 2** (`RP-s-13` joins component A) and the fan-out rule -- `N` is
bounded above by `M` -- would have made a three-slot issuance illegal, forcing five cells onto one
worker's queue for no reason. **A dependency written from association rather than from need does not
merely mislead a reader; it serialises the round.** Removing it was the difference between M=2 and M=3.

⭐ **THE FAN-OUT IS SIZED ON THE POST-UNBLOCK WIDTH, WHICH IS THIS RECUT'S ONE STRUCTURAL LESSON FROM
ROUND 1.** Round 1's `2 of 2 chains` was correct at issuance and stopped being correct the moment
round 1's vocabulary cell landed and four chains opened while slot `~2` idled -- and `<issued_to>` is frozen in
committed orders, so it could not be rebalanced. **The freeze is correct and must not change**; it is
what makes a worker face trustworthy. The remedy is at the CUT, and the analysis says so: size for the
width AFTER the critical cell lands, not before it.
Applied: **3 roots now, and 3 wide again the moment `RP-s-15` lands** (`16`, `17`, `19` all open). The
slot assignment above spreads the dependents so **no slot serialises behind another's queue**:
```
  ~1  RP-s-15 -> RP-s-16 -> RP-s-18      (the critical path, and its own successors)
  ~2  RP-s-13 -> RP-s-19
  ~3  RP-s-14 -> RP-s-17
```

**ROUNDS BY DEPTH: A=3, B=3, C=1.** Max width 3, inside the default cap of 8.

---

## 3. Placement axis

All seven are the `report` lane -- the artifact, its composition, its schedule, its verdict and its
registers. **No infra-lane cell this round:** round 1's compute-manifest cell's substrate work is done and `FWD-8`'s remaining
limb is out of scope.

---

## 4. BATTERY DISPOSITION -- mandatory core

`comp-schedule`, `comp-iam` and `comp-adversary` were RUN at round 1's cut with denominators
(C1=23/C2=7/C3=12/C4=20/C5=335; 836 calls / 96 roles / 31 services; 2 of 2 commits verified) and their
findings are carried into the cells below that they touch. ⚠ **THEY ARE NOT RE-RUN HERE AND THIS
DECOMPOSITION DOES NOT CLAIM THEY WERE.** Their round-1 vintage is stated so no reader takes a
carried figure for a fresh one; a cell whose act turns on a battery figure re-grounds it at its own
vintage, which is the L5 battery's stated contract.

**FINDINGS THAT STILL BIND, carried forward:**
- **The alerting moratorium is ARMED** (1 of 12 NEVER clauses). `RP-s-16` DELIVERS an existing report;
  it mints no alarm, topic, subscription or notification. Repair of an existing non-delivering topic
  is permitted; creation is not.
- **`comp-iam` is BLIND to `wafv2`.** Unchanged, and it still binds anything rendering the sentinel.
- **The trading-calendar frontier is a RESOLVED path, never a basename** -- five files share it, and
  round 1's schedule cell established that three are byte-identical vendored copies of one canonical source. `RP-s-16`
  inherits that finding rather than re-deriving it.

⛔ **DENOMINATOR HYGIENE, DIRECTED BY THE ANALYSIS §3 AND BINDING ON EVERY CELL HERE: DO NOT COMPUTE A
COVERAGE FIGURE OFF THE EC2 MANIFEST'S ROW COUNT.** It carries **27 entries, 26 with an id, 25
DISTINCT**. Three different denominators, and the wrong one inflates coverage -- in a project whose own
`FWD-10` exists to stop exactly that.

---

## 5. What this decomposition REFUSES to assume

1. **That "not more engines" means "build nothing".** It means no more SPEC DOCUMENTS. The composer is
   the thing that makes nine `EXERCISED` bars gradeable at all.
2. **That a realized outcome benefits from a fresh cell.** Six are REALIZED and get none.
3. **That `S2`'s two outcomes need two cells.** The exception is measured, not assumed (1a).
4. **That the round-1 battery figures are current.** They are round-1 vintage and labelled so.
5. **That `FWD-4`'s member NAMES must be settled before its cell can be cut.** They are an open call at
   Andrew. **`UNGROUPED` is precisely what makes `RP-s-13` cuttable without that answer** -- the cell
   builds the axis and its not-yet-grouped value, and Andrew's eventual naming cannot invalidate it.
6. **That an `EXERCISED` bar can be closed by this lane.** It closes when a real edition runs and a
   real reader reads it. **A cell can produce the edition; it cannot produce the reading.**

---

## 6. Holds

- **NONE held by this lane.** All seven cells are cuttable at this edit.
- `FWD-4`'s naming (Gateway / Graph / both) and the `trade-submission-api` disposition are **Andrew's**
  and block nothing here.
- ⛔ **The `EXERCISED` bars for `FWD-1`, `FWD-3`, `FWD-7` and `FWD-12` cannot be graded REALIZED by
  round 2's completion alone.** They need editions that have RUN and been READ on real trading
  mornings. **This is stated at the cut so the round is not later read as having failed** when its
  cells complete and its outcomes still do not flip.
