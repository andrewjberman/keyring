# NFRA_REPORT -- L5 decomposition (COO) -- v0.1

**Seat:** `2.0.0_SA_COO~ZZ` · **Limb:** L5 · **PRD:** `org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md` **v0.2 @`1703e825d0`**
**Directive:** D12 Platform Operations · **Fabric:** site-z · **archetype:** COORDINATE

**The rectangle is RECEIVED, not derived here.** PRD section 8's SURFACE MANIFEST is the domain; this
file mirrors it. The fork over whether L5 should derive its own manifest was put to `1.0.0_SA_CTO~Z`
at msg 20590 and ruled (A) at msg 20591 -- the manifest is an L4 deliverable. **That matters to how
this file may be graded:** the domain against which its MECE is checked was authored by a different
seat, so author and grader do not collapse.

---

## 1. The rectangle -- twelve cells, `RP-s-<n>` mirroring manifest row `S<n>`

**INVARIANT THIS FILE COMMITS TO:** *every cell mirrors a manifest row, and every manifest row has at
least one cell.* ⛔ **IT IS NOT A BIJECTION AND IS NOT DECLARED AS ONE.** PRD section 8 records the
12-and-12 as a measurement at that edit and warns that `NFRA_OPSEC202609` asserted an
`OP-s-<n>` IS `S<n>` bijection in a heading which then went FALSE with nothing able to fail. A later
cell mirroring `S1` twice, or a row acquiring a second cell in a round-2 recut, breaks nothing here.
**MEASURED AT THIS EDIT: 12 `RP-s-` cells over 12 manifest rows; every cell mirrors a row; every row
carries at least one cell.**

| cell | row | outcome | act | state | round | lane |
|---|---|---|---|---|---|---|
| `RP-s-1` | S1 | FWD-2, FWD-4 | the two-axis STATE MODEL as the report's rendering law, incl. the two expressibility gaps below | OPEN | 1 | report |
| `RP-s-2` | S2 | FWD-3, FWD-1 | row structure + the PER-ROW delta against the previous edition | OPEN | 2 | report |
| `RP-s-3` | S3 | FWD-1 | schedule + delivery on TRADING DAYS, before Andrew's morning | OPEN | 3 | report |
| `RP-s-4` | S4 | FWD-1 | the VERDICT rule, COMPUTED from the rows | OPEN | 3 | report |
| `RP-s-5` | S5 | FWD-9 | the COMPUTE MANIFEST substrate -- EC2 **and ECS**, schema fix, backfill | OPEN | 1 | infra |
| `RP-s-6` | S6 | FWD-5 | the ALERT-DELIVERY read, alarm-anchored to a CONFIRMED subscriber | OPEN | 2 | report |
| `RP-s-7` | S7 | FWD-6 | the DEPRECATION determination -- consumer walk to the client-facing terminus | OPEN | 2 | report |
| `RP-s-8` | S8 | FWD-7 | the RETIREMENT REGISTER -- suppression as recorded state, owner + reason + date | OPEN | 3 | report |
| `RP-s-9` | S9 | FWD-8 | the COST-ANOMALY detector at SEGMENT grain now, BOX grain after `RP-s-5` | OPEN | 2 | report |
| `RP-s-10` | S10 | FWD-10 | the COVERAGE / DENOMINATOR carrier on every count | OPEN | 2 | report |
| `RP-s-11` | S11 | FWD-11 | the MONITORED-vs-SERVED reconciler | OPEN | 3 | report |
| `RP-s-12` | S12 | FWD-12 | the ANOMALY BREAKDOWN (COMPUTED) + its written account (GENERATED) | OPEN | 4 | report |

### 1a. `RP-s-1` carries TWO EXPRESSIBILITY GAPS, and they are the reason it is round 1 alone

`S1`'s `bound` column requires the vocabulary to express a **PERMANENT blind** (`C-WEBSITE-BLIND`) and
a **DESIRED-not-APPLIED row** (`C-SENTINEL-STATE`). Ruling 12's ratified Axis-1 enum
(`CHECKED | BLIND | INERT | COARSE | UNCHECKED | DENY-BY-DESIGN`) expresses NEITHER, and this was
found by running rule 24(i) against the declared domain rather than by reading the enum for style.

**GAP 1 -- permanent vs temporary blind.** `BLIND` means "could not look". It does not separate
*nothing looks at this yet* (an instrument gap with an owner) from *nothing can ever look at this*
(the Website edge, settled: bare EC2 elastic IP, no CloudFront, AWS WAF cannot attach, every
candidate edge needs a GoDaddy change Andrew has ruled out). A reader triaging BLIND asks *who is
fixing this*; for the settled case the honest answer is *nobody, ever* -- and a vocabulary that
cannot say so manufactures a permanent open item every future reader re-investigates. **The report
would generate work rather than retire it, which inverts FWD-7.**

**GAP 2 -- DESIRED-not-APPLIED.** The sentinel runs watch-only (`TO-OP-S-14-21` complete, reconciler
`TO-OP-S-15-19` staged), so a `BLOCKED` address row is INTENT no IP set enforces. Tested against all
six: `CHECKED` is wrong (we looked, but this is not the world's state); `BLIND` wrong (we see the
table perfectly); `COARSE` wrong (the grain is exact); `UNCHECKED` wrong (it is asserted);
`DENY-BY-DESIGN` wrong (nothing is denied); `INERT` is CLOSEST **and still wrong** -- INERT is
defined as a control that CANNOT FIRE, whereas the sentinel CAN and is deliberately watch-only.
**Rendering a designed intermediate phase as INERT reports it as a defect.**

⭐ **THE SHAPE, which is why neither gap is a wording quibble:** Axis 1 asks *did the check happen*,
Axis 2 asks *what was found*. **Neither asks whether what was found is DESIRED or APPLIED.** That is
a third question, and folding it into either axis violates postulate (iii), INTENT COHERENCE.

**RESOLUTIONS THIS DECOMP DIRECTS, both chosen to leave ruling 12's ratified VALUE SET untouched:**
- **Gap 1 -> a rejectable FIELD, not a new enum member:** `BLIND` carries a mandatory
  `resolvable: yes | no` plus a `reason`. Reuses the estate's a-value-carries-its-claim discipline
  that `C-AI` already directs this project to reuse rather than mint a second vocabulary.
- **Gap 2 -> a THIRD, ORTHOGONAL AXIS:** `state: desired | applied | exercised`, rendered only when
  it is not `applied`. Reuses CLAUDE.md rule 22's existing vocabulary verbatim.

⛔ **AND THE LIMIT OF THIS LANE'S AUTHORITY IS STATED RATHER THAN ASSUMED.** Both resolutions ADD
(a field; an orthogonal axis) and neither edits, removes or redefines a ruling-12 value, so this lane
treats them as L5 decomposition decisions. **If either is instead read as AMENDING a sovereign-ratified
enum, it is not this lane's to make** and routes to `1.0.0_SA_CTO~Z` and Andrew. The cell says so, so
a worker cannot land a widening under cover of a decomposition.

⚠ **ONE READING HAZARD IN THE MANIFEST ITSELF, surfaced not corrected** (PRD section 8 is `ANY_CTO`):
`S1`'s surface text abbreviates Axis 1 as *"instrument axis CHECKED vs BLIND"*. The RATIFIED enum has
**SIX** values (ruling 12, `ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md`). A worker
reading only the manifest cell would build a two-value axis and silently drop `INERT`, `COARSE`,
`UNCHECKED` and `DENY-BY-DESIGN` -- and `INERT` is the one ruling 12 names in its own worked example
(`opal-login-abuse-alerts` is INERT, never RED). **`RP-s-1`'s worker face carries the six-value enum
verbatim from ruling 12 and cites it, never the manifest's shorthand.**

### 1b. `RP-s-1`'s acceptance CANNOT be self-graded, and the cell names its grader

`FWD-2`'s ACCEPT is *"someone who knows nothing about how this is put together can look at any line
and tell 'we have no way of seeing this' from 'we looked, and here is how bad it is'."* ⛔ **A
legibility bar graded by the seat that authored the vocabulary is the author-and-grader collapse this
whole project exists to remove** -- it is the same defect as a generated sentence sitting beside a
computed number. `RP-s-1`'s criterion therefore routes its legibility limb to **`3.0.0_SA_CVO~Z` at
L9**, on rendered specimen rows including the two gap cases, and is NOT gradeable by the worker or by
this seat. The MECHANICAL limbs (the enum is present; every value is defined; the two gap cases render
distinctly) the worker proves; the READER limb it cannot.

---

## 2. Four-postulate record (rule 24) for what this file ADOPTS and ADDS

Rule 24 binds any schema an agent authors **or ADOPTS**. This file adopts ruling 12's two axes and
adds one field and one axis (section 1a).

- **(i) MECE over a DECLARED domain.** Domain = every row the report can render, declared as PRD
  section 2's twelve OWNS items. **The uncovered members were HUNTED and TWO were found** (section
  1a) -- which is the postulate doing work rather than being cited.
- **(ii) SAME GRAIN.** Axis 1 is a property of the INSTRUMENT, Axis 2 of the WORLD, the added axis of
  the STATE of what was found. Each is a property of the row, none of a sub-part of another.
- **(iii) INTENT COHERENCE.** One axis, one intent -- and this is precisely why gap 2 gets its own
  axis rather than a smuggled Axis-1 value.
- **(iv) STATE COHERENCE -- which values one remedy does NOT move.** Building an instrument moves
  `BLIND -> CHECKED`; it does **not** move `resolvable: no` (the Website edge stays unbuildable), and
  it does **not** move `state: desired -> applied` (that needs the reconciler to run, which is
  `NFRA_OPSEC202609`'s act and not this project's). **Naming this is only possible because the axes
  are separate**; folded together, one remedy would appear to move all three.
- **TOKEN CENSUS (word-boundary), owed with any value-enum proposal:** OWED BY `RP-s-1` AT PHASE 1,
  not run here -- the six ratified names plus `resolvable`, `desired`, `applied`, `exercised`, against
  the report's own corpus, to catch a value name that already means something else nearby. This decomp
  records the debt rather than pretending the census exists.

---

## 3. Placement axis

`report` lane = the report artifact, its vocabulary, schedule, verdict and every read that composes
it. `infra` lane = `RP-s-5` only, the compute manifest as a substrate (EC2 + ECS enumeration, schema
fix, backfill) -- infrastructure enumeration, not report rendering. ⛔ **The manifest's `lane` column
is a LANE, never a seat assignment** (PRD section 8 says so in terms); `2.0.0_SA_COO~ZZ` seats workers
at L6.

---

## 4. Dependency edges, keyed to OBSERVED completion, never to a status word

```
  RP-s-1  <- (none)                RP-s-5  <- (none)          <-- TWO INDEPENDENT ROOTS
  RP-s-2  <- RP-s-1                RP-s-9  <- RP-s-5
  RP-s-6  <- RP-s-1
  RP-s-7  <- RP-s-1
  RP-s-10 <- RP-s-1
  RP-s-3  <- RP-s-2                RP-s-8  <- RP-s-7
  RP-s-4  <- RP-s-1, RP-s-2        RP-s-11 <- RP-s-10
  RP-s-12 <- RP-s-1, RP-s-11
```

⭐ **`RP-s-5` IS A SECOND ROOT AND IS NOT BLOCKED BY THE CRITICAL PATH.** `C-FWD2-FIRST` makes
`RP-s-1` the critical path *into the OPSEC relationship*; it does not make it the critical path into
everything. The compute manifest depends on no vocabulary, so round 1 is **two cells wide, not one** --
and reading `C-FWD2-FIRST` as "nothing else may start" would idle the infra lane for a whole round.

⛔ **`RP-s-9` AT BOX GRAIN CANNOT PASS BEFORE `RP-s-5` LANDS** (PRD `D3`): the manifest is EC2-only
with ECS absent entirely, and 18 of 27 rows carry a lifecycle word where a machine type belongs.
**SEGMENT grain is available now**, so `RP-s-9` is cut with its segment limb in round 2 and its box
limb explicitly conditioned on `RP-s-5` -- not deferred wholesale, and not written as though box grain
were reachable.

---

## 5. The arc as rounds

- **ROUND 1 (2 cells):** `RP-s-1` (the vocabulary -- everything downstream renders through it),
  `RP-s-5` (the substrate).
- **ROUND 2 (5 cells):** `RP-s-2`, `RP-s-6`, `RP-s-7`, `RP-s-10` on `RP-s-1`; `RP-s-9` on `RP-s-5`.
- **ROUND 3 (4 cells):** `RP-s-3`, `RP-s-4`, `RP-s-8`, `RP-s-11`.
- **ROUND 4 (1 cell):** `RP-s-12`.

Max round width 5, inside the default fan-out cap of 8. **`fanout:` data is stated in the L6 issuance
commit, derived from these chains, not chosen.**

---

## 6. `<preflight>` -- what this decomp actually ran, with denominators

| instrument | invocation | result |
|---|---|---|
| `comp-find --name` | `'*NFRA_REPORT*'` | 2 hits / 54,576 files scanned, corpus=all |
| `comp-find --name` | `'*owned-path*'` | 7 hits / 54,576 |
| `comp-find --name` | `'*infrastructure*report*'` | 1 hit / 54,941 |
| `comp-read --enumerate` | `.owned-paths.yaml` `'SA_COO'` | 104 hits / 2,141 lines; **0 whole-value, 104 substring** -- the tool WARNed that an anchored probe would return zero, which is why no anchored claim is made from it |
| `comp-which` | "where is the daily infrastructure report generated" | **NO CURATED RULE MATCHED**; top score 0.43 of 79 tools. Recorded as a MEASURED negative -- the catalog does not cover it -- and no candidate was picked, per the tool's own instruction |
| `owned-paths-validate --check-agent` | `2.0.0_SA_COO_ZZ` over decompositions/, task-orders/, project.json, surprise-channel/, prd/ | rc=0 on the first four; **prd/ REFUSED (lane ANY_CTO)** -- positive control: base serial passes the same paths; negative control: `0.1.1_RD_MarketPerformance` refused on the COO home |
| `git` blob identity | CLAUDE.md, org/XXX.md at 3 refs | identical at all three; positive control `.tools/comp-find` = 42 ins/40 del, so the diff instrument fires |

⛔ **NOT RUN, AND WHY** -- so no reader infers a clean sweep from silence: `comp-blast`, `comp-routes`,
`comp-cache` and `comp-pipescript overlap` are the COO minimums for TOs touching routes, cache keys,
shared components or gold-pipeline I/O. **This decomposition touches none of those surfaces** -- every
cell is a report artifact, a vocabulary, or an infrastructure enumeration. They are owed at L6 by any
individual task order that does touch one, and `RP-s-12` is the likeliest (it queries the dependency
graph). Claiming them here would be a clean-sweep signal over a surface they never examined.

---

## 7. comp-adversary declaration

This file's evidence context is **PRD v0.2 @`1703e825d0` read in full; the L2 endpoint; the L1 brief's
`F<n>` ids AS CITED BY THE MANIFEST AND NOT INDEPENDENTLY RE-READ; ruling 12 and rulings 7-20 at
`ANDREW_DIRECT_20260909_1458Z...`; the `NFRA_OPSEC202609` decomposition read for FORM only.**
⛔ **What it is NOT:** no live AWS was read by this seat for this file; no `measured` cell in the
manifest was re-grounded here -- PRD section 8 states nothing in it was re-measured at L4 either, so
**every `measured` claim reaching a worker carries the BRIEF's vintage (`@37ff80867a`, 2026-09-09) and
not this decomp's.** The L5 battery re-grounds each cell at its own vintage; that is the cell's job
and is written into each one.

---

## 8. What this decomp REFUSES to assume

1. **That `RP-s-1`'s vocabulary is gradeable by whoever builds it.** Section 1b.
2. **That the manifest's `S1` shorthand is the enum.** Section 1a; the ratified six-value set governs.
3. **That the 12-and-12 is an invariant.** Section 1; coverage in both directions is the invariant.
4. **That `absent` means unexamined.** Every `absent` row names what was measured about the current
   state's failure to serve it; a worker must not read `absent` as "nobody looked".
5. **That `RP-s-9` is deferred.** Its SEGMENT limb is live now; only its BOX limb waits on `RP-s-5`.
6. **That the VINTAGE residual is still open.** PRD section 7 records `comp-find --corpus aws` printing
   `VINTAGE: UNREAD` as a live unowned problem; it was **CLOSED** by the R7 served-graph port and now
   prints a real vintage (`1.0.0_SA_CTO~Z` msg 20584/20591, re-exercised at the merged head).
   **No cell is cut against it.** The PRD's own text overstates it and its author has said it will
   amend at the next touch -- recorded here so a worker reading section 7 does not chase a closed item.

---

## 9. Holds, and whose they are

- **NONE held by this lane.** All twelve cells are cuttable at this edit.
- `RP-s-9`'s BOX limb is CONDITIONED on `RP-s-5` (section 4) -- a dependency, not a hold.
- **`NFRA_OPSEC202609` is a CONTENT dependency on three security rows, never a structural one**
  (PRD section 7, verbatim: *zero of the twelve outcomes are BLOCKED by it*). Its completion is a
  QUALITY gate on those rows, not a LAUNCH gate on any cell here.
- ⚠ **Out of this lane's hands and named so it is not mistaken for a hold:** whether the two
  section-1a resolutions are read as amending ruling 12. If they are, `1.0.0_SA_CTO~Z` and Andrew own
  it; until anyone says so, they are additive and `RP-s-1` proceeds.
