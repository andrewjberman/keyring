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

**CELL-ID CONFORMANCE, MEASURED not assumed** (`org/standards/DECOMP_CELL_ID_CONVENTION.md`): the ids
are SHAPE 1, the form the standard says to prefer for new decomps, so **no new regex branch is
requested and none of the standard's two controls is owed.** Verified against the enforcer object
itself (`.tools/proof-of-spec-check.py` `CELL_ID_RE`, loaded and applied, not eyeballed):
**MINE 12 of 12 match · POSITIVE CONTROL `OP-s-17`/`D1-i-2`/`ETFS-d-1` 3 of 3 · NEGATIVE CONTROL
`AMONG-THE-6`/`AWS-IAM-1`/`ARCH-GATE-2` 0 of 3** -- the negative control is the one that bites, and it
bites correctly.

**CELL STATUS VOCABULARY (rule 24 record below at section 2a).** Closed set, and it HAS a
not-evaluated value by construction, because the spine requires one:
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`.
- `NOT-EVALUATED` -- this decomp did not reach the cell. **No cell carries it at this cut**, and that
  is a MEASUREMENT (12 of 12 evaluated), not a vocabulary that lacks the value.
- `OPEN` cuttable now · `IN-FLIGHT` a worker holds it · `HELD` blocked on a named owner ·
  `COMPLETE` served and proven · `CLOSED` retired without being served, with its pointer.

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

### 2a. Rule 24 record for the CELL STATUS vocabulary this file AUTHORS

- **(i) MECE over the declared domain** = every cell of this rectangle at any moment. The uncovered
  member hunted and found: *"evaluated, and deliberately not cut this round"* -- which is `CLOSED`
  **with its pointer**, not a sixth value. A terminal status without its pointer is the rot with a
  tidier label.
- **(ii) SAME GRAIN** -- every value is a property of a CELL, none of a task order or a criterion.
- **(iii) INTENT COHERENCE** -- one axis: how far this cell has travelled. ⛔ `HELD` is on that axis
  (not travelling, with a named owner); WHY it is held is the `bound` column's job, deliberately not
  a status value, or the axis would carry two intents.
- **(iv) STATE COHERENCE -- which values one remedy does NOT move.** Spawning a worker moves
  `OPEN -> IN-FLIGHT`; it does **not** move `HELD` (that needs the named owner to act) and it does
  **not** move `NOT-EVALUATED` (that needs a re-decomposition, which is a COO act, not a worker's).
- **TOKEN CENSUS (word-boundary):** OWED AT L6, not run here, for the same reason the section 2
  census is owed -- the corpus these names must not collide with is the task-order and criteria text
  that does not exist yet. Recorded as a debt rather than claimed.

---

## 2b. BATTERY DISPOSITION PER LENS -- mandatory core, each RUN or DECLARED-NOT-APPLICABLE

Required by the spine's L5 (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` :135). **All three
mandatory lenses were RUN. None is declared not-applicable.**

### `comp-schedule` -- RUN. Denominators: C1=23 · C2=7 · C3=12 · C4=20 · C5=335

`GATES ARMED: 2`, and **neither is this project's**: `G-3` (owner CTO, never-widen co-sign) and `G-7`
(owner POD4). Decidability is carried per carrier rather than flattened: C1/C2/C3 DECIDABLE, C4
SEMI-DECIDABLE, C5 NOT-DECIDABLE (335 `blocking` fields, 137 non-null prose, **a reading list and
never gates -- this decomp does not count them as such**).

⭐ **TWO FINDINGS THAT TOUCH CELLS, which is the battery earning its cost:**
- **C3 = 12 standing NEVER clauses**, one of which is the alerting/monitor moratorium. It binds
  `RP-s-6` and `RP-s-8` directly: this project REPAIRS existing egress and REPORTS, and **mints no
  alerting**. Written into both cells' bounds rather than left to a worker's memory of the law.
- **`G-7` is a DRIFT CANDIDATE naming `lib/trading_calendar.py`, and comp-schedule measured FIVE
  files with that basename in the repo.** `RP-s-3` is the cell that must key on the trading-day
  frontier (`C-TRADING-DAYS`, CLAUDE.md NEVER#4: *one frontier*). **A cell that resolves the wrong
  copy of a five-copy basename would pass its own check and still send on a market holiday** -- the
  exact defect `S3` exists to fix, reintroduced one layer down. `RP-s-3`'s criterion names the
  frontier BY RESOLVED PATH, never by basename.

### `comp-iam` -- RUN. Denominator: 836 calls verdicted across 96 mapped roles; 31 services

`12 missing | 291 deny-present | 1 coverage-unknown | 2 resource-mismatch`. Resource plane: 630
UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD, 11 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE;
**266 calls in 26 role-UNMAPPED services NOT resource-checked -- the tool calls this an honest hole,
not a pass, and it is carried here as one.** The 51 GRANTED-BROAD rows are EXCLUDED, NOT CLEARED: a
wildcard grant cannot be falsified by a resource check.

**DISPOSITION FOR THIS DECOMP: no cell of the twelve creates, changes or requires an IAM grant.** The
project READS a posture it explicitly does not own (PRD section 2 relies-on: `NFRA_IAMROLES202609`).
So none of the 12 missing/2 mismatch rows is this project's to fix, and **no cell is cut against
them** -- they are named here so a worker does not discover them and think they are in scope.

⛔ **THE BLINDNESS, and it lands exactly where this decomp is most exposed:** comp-iam's
COVERAGE-UNKNOWN is **`wafv2`** -- *"boto3 services comp-iam does NOT model"*, instanced on
`opal-ipset-reconciler`. **That is the very plane `C-SENTINEL-STATE` lives on**, the DESIRED-not-APPLIED
case `RP-s-1` must render. So comp-iam **cannot** verify anything about the sentinel's enforcement
path either way, and `RP-s-1` must not treat comp-iam silence there as an ALLOW. Stated so the cell
does not inherit a clean read from a lens that never looked.

### `comp-adversary` -- RUN on this file at `@f060f2354e`

2 cited commits attempted / **2 VERIFIED** (`@1703e825d0`, `@37ff80867a`); 2 cited paths / 2 stable;
0 `file:line` cites.

⛔ **DECLARED BLINDNESS, in the lens's own words rather than paraphrased:** `T11: decomposition
neighborhood NOT RESOLVED (artifact carries no <decomp_ref> -- not a tree task order)`, so its
neighborhood **fell back to filesystem adjacency** and it digested 12 of 13 `org/` directory siblings
(`ORG_CHART.md`, audit logs) -- **not this decomposition's dependency chain, its dependencies' proof
instances, or the PRD rows it cites.** The spine names precisely this case (:137-138) and requires the
blindness be stated: **it is stated, and the lens's packet is therefore NOT evidence about these
cells.** It is structural, not fixable here -- a DECOMP carries no `<decomp_ref>`; the task orders at
L6 will, and the lens resolves properly against them.
Its own warning is carried verbatim: *"THE PACKET IS A SELECTION, NOT A SURVEY. A file's ABSENCE from
the digests is a BUDGET fact, never an assessment that it did not matter."*

### Non-core lenses -- DECLARED-NOT-APPLICABLE, with reasons

`comp-blast`, `comp-routes`, `comp-cache`, `comp-pipescript overlap` are the COO minimums for task
orders touching shared components, routes/CF behaviours, react-query keys or gold-pipeline I/O.
**No cell of this decomposition touches any of those surfaces** -- every cell is a report artifact, a
vocabulary, or an infrastructure enumeration. **They are OWED AT L6 by any individual task order that
does touch one**, and `RP-s-12` is the likeliest (it queries the dependency graph). Running them here
would produce a clean-sweep signal over a surface they never examined.

### 2c. BOUNDS THE BATTERY ADDED TO CELLS -- carried here, and inlined into the worker face at L6

The spine requires the battery's findings be inlined into the task order where they touch the owned
cells (:157). These are the three, stated as cell bounds so nothing depends on a worker recalling a
lens it never ran:

| cell | bound the battery added | lens |
|---|---|---|
| `RP-s-1` | **comp-iam is BLIND to `wafv2` and cannot verify the sentinel's enforcement path either way.** The DESIRED-not-APPLIED rendering may NOT be justified by comp-iam silence, and no criterion may cite comp-iam as evidence about that plane. | `comp-iam` COVERAGE-UNKNOWN |
| `RP-s-3` | **Name the trading-day frontier BY RESOLVED PATH, never by basename** -- FIVE files share the basename `lib/trading_calendar.py`. A cell resolving the wrong copy passes its own check and still sends on a market holiday, which is the exact defect `S3` exists to fix. | `comp-schedule` `G-7` |
| `RP-s-6`, `RP-s-8` | **The standing alerting/monitor moratorium is ARMED** (one of 12 NEVER clauses). These cells READ delivery state and RECORD suppression; they mint no alarm, topic, subscription or notification. Repairing an existing non-delivering topic is permitted; creating one is not. | `comp-schedule` C3 |

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

**THE MANDATORY CORE BATTERY IS AT SECTION 2b**, not here, and it is RUN rather than declared: this
table is the retrieval/navigation work that preceded it. ⛔ **AN EARLIER VERSION OF THIS SECTION SAID
THE CORE LENSES WERE "NOT RUN" AND OWED AT L6. THAT WAS WRONG AND IS CORRECTED RATHER THAN QUIETLY
REPLACED:** the spine requires `comp-schedule`, `comp-iam` and `comp-adversary` as an L5 obligation
(:135), not an L6 one, and this file was cut at v0.1 without them. The cut was reopened before L6 and
all three ran; two of them returned findings that changed cell text (the trading-calendar frontier on
`RP-s-3`, the `wafv2` blindness on `RP-s-1`). **A decomposition that had gone to L6 unbatteried would
have carried both defects into task orders**, and the only reason it did not is that the spine was
re-read rather than recalled.

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
