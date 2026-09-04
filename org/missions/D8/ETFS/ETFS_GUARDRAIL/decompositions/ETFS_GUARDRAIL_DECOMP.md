# ETFS_GUARDRAIL -- DECOMPOSITION (L5)

**v0.1** (2026-09-04 ~18:0xZ, `2.0.0_SA_COO~B`) -- the L5 act on PRD v0.3 at the tree home
`../prd/ETFS_GUARDRAIL_PRD.md` @`4e30d6b635` (byte-identical to the flat PRD @`7aa1554881`, ON ORIGIN; PRD_HEADER
`status: RATIFIED`; the step-6 RED/HOLD lifted by `3.0.0_SA_CVO` 2026-09-02 21:26Z). **Authority for this lane's
pickup:** Andrew-direct at the `1.0.0_SA_CTO` terminal 2026-09-04 ~17:0xZ, relayed verbatim in broker message 94225:
*"also I'm spawning coo~b so they can run the /dispatch drain on etfs_guardrails, i will need you to check that thing
out with /canonical-flow and see what state its in, if all the task orders exist already, if its registered, etc. that
needs to get handled end to end and start runnning with coo~b."* `/canonical-flow` measured the project at L4 with
class STALLED-AT-OWNER at L5 (the owner is this lane); this document is the L5 output.

**Input:** the PRD's 13-row surface manifest (s.7.2, one row split S7a/S7b), its rulings that bind (s.6), its
acceptance properties (s.4), its two ordering constraints (s.1) and the moratorium carve-out (s.0). **This document
adds the ORDER, the SEATING, the ROUND FENCE and the BATTERY. It re-litigates no row and invents no surface** -- the
manifest's MECE check was run at L4 (s.7.2, both directions) and is not re-derived here.

**Home:** `org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md` (lane TREE_COO; versioned in
place). **Directive:** D8 (placement LAPTOP, Andrew-direct 2026-09-01). **Fabric:** laptop, every cell.

---

## 0. The cell set -- 1:1 with the manifest, no cell invented

**`EG-s-n` IS manifest row `Sn`.** 13 rows in; the PRD's own split of S7 into S7a (rungs 1-2, unattended) and S7b
(rung 3, STOPS AND ASKS A PERSON -- a different ACTOR, postulate ii) gives **14 cells out**. The split row keeps its
manifest number: S7a is `EG-s-7`, S7b is `EG-sb-7` (shape 1 of `org/standards/DECOMP_CELL_ID_CONVENTION.md`, axis
`sb` = the stops-and-asks half of row 7; the digits-then-letter form `7a`/`7b` is UNEXPRESSIBLE under `CELL_ID_RE`
and was not minted). The `claim`, `MEASURED-BY`, `lane`, `verb`, `depends_on`, `accept` and `bound` columns are the
PRD's and are authoritative; this document does not restate them, so there is ONE carrier and it cannot drift.

| cell | manifest row | outcome_ref | surface (PRD s.7.2) | verb | depends_on (as cells) |
|---|---|---|---|---|---|
| `EG-s-1` | S1 | FWD-1 | `infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py` (177 lines at HEAD) -- the catch-up PORT | port | `EG-s-3`, `EG-s-10` |
| `EG-s-2` | S2 | FWD-1 | `infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py` (122 lines) -- the catch-up PORT, 49F tail 12-13 d | port | `EG-s-3`, `EG-s-10`, `EG-s-11` |
| `EG-s-3` | S3 | FWD-1 | `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:271-316` -- the PORT SOURCE, relied on, not owned | verify | -- |
| `EG-s-4` | S4 | FWD-4 | NEW `data/etfs/scripts/coverage/classifier.py` (ABSENT at HEAD) -- the A/B/C/D classifier | classify | `EG-s-10` |
| `EG-s-5` | S5 | FWD-3 | `data/etfs/scripts/presentation/render_month_end.py` (778 lines) -- the coverage line, every verdict | wire | `EG-s-4` |
| `EG-s-6` | S6 | FWD-2 | NEW precondition INSIDE `render_month_end.py` (RULED s.7.4) -- the pre-publish gate | wire | `EG-s-1`, `EG-s-2`, `EG-s-4` |
| `EG-s-7` | S7a | FWD-8 | NEW `data/etfs/scripts/coverage/remediate.py` (ABSENT at HEAD) -- rungs 1-2, unattended | wire | `EG-s-4`, `EG-s-12` |
| `EG-sb-7` | S7b | FWD-8 | same module, rung 3 -- STOPS AND ASKS; names the dates; no standing grant | wire | `EG-s-7` |
| `EG-s-8` | S8 | FWD-7 | `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py` (375 lines) -- the ONE terminal SES send, existing `_ses.send_raw_email` path | wire | `EG-sb-7` |
| `EG-s-9` | S9 | FWD-5 | the same orchestrator, FOUR sites `:158 :189 :221 :277` -- JOIN as a TYPE decision (header string, envelope list, both paths) | wire | `EG-s-13` |
| `EG-s-10` | S10 | -- | `lib/trading_calendar.py` (163 lines) + 3 vendored copies (`bd-served-vintage-alarm/`, `inf-etf-ownership-daily/`, `opal-assets-absence-check/`); neither target producer has one | verify | -- |
| `EG-s-11` | S11 | -- | `bd-49f-etf-ownership-daily` vs `bd-49f-etf-ownership-daily-canonical` (both dirs present at HEAD) -- which twin WRITES the served slices | verify | -- |
| `EG-s-12` | S12 | -- | Inflection lineage: deployed bytes vs the build input (`infra/aws/lambda/ci/lambda-source-map.json`), NEVER a source read | verify | -- |
| `EG-s-13` | S13 | FWD-6 | `orion_normalize_as_of` -- the Orion date-basis alignment, forward-only, PREREQUISITE TO THE SEND ONLY | align | -- |

**Re-pinned at HEAD `bc1d5cc0fd` by this seat (`git show HEAD:<path> | wc -l`, 8 of 8 paths probed):** the six
existing surfaces are PRESENT at the line counts the PRD carries (177 / 122 / 317 / 778 / 375 / 163); the two NEW
homes (`coverage/classifier.py`, `coverage/remediate.py`) are ABSENT, as a NEW surface must be; both `bd-49f` twins
exist; `CATCHUP_WINDOW_DAYS = 10` sits at `inf-etf-ownership-daily/lambda_function.py:271` and the port source's
walk-back at `:274-293`; the orchestrator's four recipient sites read exactly as s.7.3a lists them (`:158 :189 :221
:277`) plus the two cosmetic interpolations (`:325 :373`). Nothing the manifest names has moved since L4.

**Outcome coverage, run not asserted: 8 of 8 `FWD-n` in the PRD header have >= 1 cell** (FWD-1: s-1 s-2 s-3;
FWD-2: s-6; FWD-3: s-5; FWD-4: s-4; FWD-5: s-9; FWD-6: s-13; FWD-7: s-8; FWD-8: s-7 sb-7). The three RELIES-ON rows
(s-10, s-11, s-12) serve no outcome directly and are the shared dependencies beneath the ones that do -- Rule 22's
common-dependency limb, which is why they are cells and not footnotes.

**Cell vocabulary (Rule 24, a NOT-EVALUATED value present so non-evaluation is never a verdict):**
`status` = **DONE** (graded) / **IN-FLIGHT** (landed, grade pending) / **OPEN** (not started) / **HELD** (blocked on a
named decision, owner stated) / **NOT-EVALUATED** (this decomposition did not measure it and says so). Four-postulate
record: (i) MECE over the domain {a cell's state between the cut and the close} -- every cell is in exactly one; (ii)
one grain, the cell; (iii) one axis, progress toward a grade; (iv) a CVO grade moves `status`, a ruling moves the PRD's
`claim` and never this file -- the two do not move together, by design. At v0.1 **every cell reads OPEN** -- an
honest starting state, not a measurement. Reused from the NFRA_OUTSET and NFRA_COMPEFFICACY decompositions without
renaming.

The `status` column of a decomposition DRIFTS AGAINST ITS ORDERS and nothing links them mechanically (measured
twice on 2026-09-04 on two sibling projects). **The order is the truth; this column is bumped at a round close and is
one round behind between them.**

## 1. THE CHAIN READ -- computed from the manifest's `depends_on` edges, not chosen

```
  edges (15, from PRD s.7.2 depends_on, keyed to OBSERVED completion of the source cell):
    EG-s-3  -> EG-s-1     EG-s-10 -> EG-s-1     EG-s-3  -> EG-s-2     EG-s-10 -> EG-s-2     EG-s-11 -> EG-s-2
    EG-s-10 -> EG-s-4     EG-s-4  -> EG-s-5     EG-s-1  -> EG-s-6     EG-s-2  -> EG-s-6     EG-s-4  -> EG-s-6
    EG-s-4  -> EG-s-7     EG-s-12 -> EG-s-7     EG-s-7  -> EG-sb-7    EG-sb-7 -> EG-s-8     EG-s-13 -> EG-s-9

  heads releasable at spawn (no incoming edge) = 5 :  EG-s-3  EG-s-10  EG-s-11  EG-s-12  EG-s-13
  leaves (no outgoing edge)                     = 4 :  EG-s-5  EG-s-6   EG-s-8   EG-s-9

  M, the spine's chain = a maximal path through the edges = 10 :
    EG-s-3  -> EG-s-1 -> EG-s-6          EG-s-10 -> EG-s-1 -> EG-s-6          EG-s-10 -> EG-s-4 -> EG-s-5
    EG-s-3  -> EG-s-2 -> EG-s-6          EG-s-10 -> EG-s-2 -> EG-s-6          EG-s-10 -> EG-s-4 -> EG-s-6
    EG-s-11 -> EG-s-2 -> EG-s-6          EG-s-10 -> EG-s-4 -> EG-s-7 -> EG-sb-7 -> EG-s-8
    EG-s-12 -> EG-s-7 -> EG-sb-7 -> EG-s-8                                    EG-s-13 -> EG-s-9

  edge-connected components = 2  (the send pair EG-s-13 -> EG-s-9 shares no edge with the other twelve)
  longest dependency depth  = 5  (EG-s-10 -> EG-s-4 -> EG-s-7 -> EG-sb-7 -> EG-s-8)
```

**THE BINDING FACTS.** (a) Twelve of fourteen cells hang together through `EG-s-10` (the trading calendar) and
`EG-s-4` (the classifier): `EG-s-10` feeds both ports and the classifier, and the classifier feeds the coverage line,
the gate and the ladder. So the calendar cell and the classifier cell are the two shared dependencies beneath almost
everything, exactly the shape Rule 22 warns about -- **a per-cell check cannot see a defect in what the cells share,
so each of those two carries its own criteria and is finished BEFORE anything that consumes it is handed out.**
(b) The DAG is five wide at the head and one wide at the tail (the ladder pole, depth 5). A fan-out chosen against
the cell count (14) or the head count (5) spawns workers that block within two hand-offs; **the useful width is the
number of POLES a queue can drain in dependency order without waiting on another queue more than once**, and that
is three (s.4).

## 2. THE ROUND FENCE -- the dependency waves inside ONE issuance

| wave | cells | the fence's reason |
|---|---|---|
| **1** | `EG-s-3` `EG-s-10` `EG-s-11` `EG-s-12` `EG-s-13` | The five heads: four `verify` cells and the one `align`. Every one is a READ of a surface the project relies on but does not own, or (s-13) the send's prerequisite that the PRD says lands first and independently. Nothing is held back. |
| **2** | `EG-s-1` `EG-s-2` `EG-s-4` `EG-s-9` | Everything wave 1 alone releases: the two ports (on s-3 + s-10, and s-11 for 49F), the classifier (on s-10), the JOIN change (on s-13). |
| **3** | `EG-s-5` `EG-s-6` `EG-s-7` | Depth 3: the coverage line and the gate (both on the classifier; the gate also on both ports -- PRD s.1 "catch-up BEFORE the gate", ruled), and the ladder's unattended rungs (on the classifier and the Inflection lineage answer). |
| **4** | `EG-sb-7` | Depth 4: rung 3, on rungs 1-2. |
| **5** | `EG-s-8` | Depth 5, the last: the terminal SES send fires only from a ladder that terminated unresolved, so it is built on the ladder's stop. |

**THE FENCE IS A PLAN, NOT A COMMITMENT.** Spine v3 L6 requires ONE issuance covering EVERY cell; a wave here is
the dependency order inside a worker's queue and the order in which the COO hands cells across queues at the drain.
**No cell is deferred to a later round in the spine's sense** -- a later round exists only when the CTO's round-N
analysis sends work back.

**The PRD's two ordering rulings are edges, not prose, and the fence carries both:** catch-up (s-1, s-2) before the
gate (s-6) is edge `EG-s-1 -> EG-s-6` and `EG-s-2 -> EG-s-6`; alignment (s-13) before the automated send (s-9) is
edge `EG-s-13 -> EG-s-9`. Neither can be reordered by a queue without breaking an edge.

## 3. SEATING -- every cell is a worker's, and the two places that needed a decision

**All 14 cells go to worker slots (`0.9.0_WK_ETFS_GUARDRAIL~n`).** Andrew's word for this project names the
internal-subagent `/dispatch` drain (94225) and, for every COO lane, the `/canonical-flow` with "the internal
subagents/dispatch drain" (94224). Under RULING 1 (Andrew 2026-09-04 ~04:58Z, @`9ef9a40aae`) a worker's write surface
is exactly the `<paths>` its order names, so the PRD's `lane` column (AE_CloudOps / DS_ClientPlatform, written 09-02
under the v2 seat model) becomes, at L6, the answer to WHICH PATHS each order grants -- Lambda source and its
Terraform for the AE rows, the `data/etfs/scripts/` tree for the DS rows -- and not a seat assignment.

**Decision 1 -- the live-plane reads (`EG-s-11`, `EG-s-12`) stay worker cells, with the attribution stated.** The
sibling NFRA_OUTSET decomposition seated its two live-cloud audit cells to a `0.7.0_AE_CloudOps` SEAT because a
worker holds no cloud identity of its own and its AWS read carries the launching seat's credentials. That is true here
too. It is accepted here rather than routed around because (a) both cells are READS (Lambda configuration, CloudWatch
log events, S3 object metadata, a deployed zip) and change nothing on the plane; (b) the invocation and its output are
recorded VERBATIM in the proof instance, so the CVO grades what was printed and never the worker's summary; (c)
Andrew's word for this project is the worker drain. The blindness is carried in s.5 and inlined on both orders.

**Decision 2 -- the deploying cells (`EG-s-1`, `EG-s-2`, `EG-s-8`, `EG-s-9`) are worker cells under NEVER-2 and
NEVER-9, with the ledger paths GRANTED.** A Lambda change is EXERCISED only when deployed, and the deploy is
Terraform through `safe-apply` under a change-management entry opened at the start and closed at completion -- never
`aws lambda update-function-code`. A worker cannot write a ledger it was not granted, so every deploying order names
`org/critical_paths/change_management/` AND the sentinel `org/critical_paths/.open_deploys/<slug>.json` in `<paths>`
(the /dispatch rule; a staged-not-committed sentinel dies with a forced teardown). The NFRA_CLDGRPH round-4 workers
applied IAM on the live plane under the same shape, so this is the exercised precedent, not a first.

**What is NOT a cell, and why:** `3.0.0_SA_CVO` "exercises acceptance" (PRD s.3 lanes) -- that is L9's grading of the
judgment criteria and the row dispositions, reserved to the CVO by the spine; a worker inside it is the shape the
estate refused on the sibling project (the ~07:0xZ fork Andrew ruled "a"). `etfs-canon-fanin`'s retirement (PRD s.5,
brief s.9.1) is explicitly out of scope with its own owner; it is not a cell and no order names it.

## 4. THE FAN-OUT L6 WILL CARRY

```
fanout: 3 of 10 chains, cap 8, reason: three poles drain in dependency order -- slot 1 the ladder pole
        (EG-s-10, EG-s-12, EG-s-4, EG-s-7, EG-sb-7, EG-s-8: the calendar and classifier first because twelve
        cells hang off them), slot 2 the producer pole (EG-s-3, EG-s-11, EG-s-1, EG-s-2, EG-s-5, EG-s-6), slot 3
        the send pole (EG-s-13, EG-s-9); the 10 maximal paths share EG-s-10 and EG-s-4, so a 4th slot would wait
        on slot 1's first two merges and cost a live worktree for nothing; the two cross-slot waits (slot 2's
        ports on EG-s-10; slot 2's line and gate on EG-s-4) are hand-offs the COO sequences at the drain.
```

**The queues, in the order each slot drains them:**

| slot | queue (dependency order) | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` | `EG-s-10` -> `EG-s-12` -> `EG-s-4` -> `EG-s-7` -> `EG-sb-7` -> `EG-s-8` | none (every predecessor is in this queue) |
| `~2` | `EG-s-3` -> `EG-s-11` -> `EG-s-1` -> `EG-s-2` -> `EG-s-5` -> `EG-s-6` | `EG-s-1`/`EG-s-2` after `EG-s-10` merges; `EG-s-5`/`EG-s-6` after `EG-s-4` merges |
| `~3` | `EG-s-13` -> `EG-s-9` | none |

Each hand-off is a fresh worktree from `CLOUD` at hand-off time, so a slot's later order sees every merge that landed
before it -- which is what makes a cross-slot wait a sequencing act at the drain and not a blocked worker.

## 5. THE BATTERY -- run at L5, with each instrument's blindness stated

| instrument | disposition | result | what it does NOT cover |
|---|---|---|---|
| the chain read | RUN | 15 edges, 5 heads, 4 leaves, M=10 maximal paths, 2 components, depth 5 (s.1) | it trusts the PRD's `depends_on`; a MISSING edge shows as false width; L5 did not re-derive the dependencies from the surfaces |
| surface re-pin | RUN | 8 of 8 manifest paths probed at HEAD `bc1d5cc0fd`: 6 PRESENT at the PRD's line counts, 2 NEW ABSENT; both `bd-49f` twins present | existence and size only; not content -- `comp-read` cannot detect a WRONG file (Rule 21 limb ii), which is exactly `EG-s-11`'s question |
| outcome coverage | RUN | 8 of 8 `FWD-n` served by >= 1 cell (s.0) | a served outcome is not a REALIZED one; four outcomes are `EXERCISED` and need a real event (a real missed day, a real refusal, a real send, a real terminal message) that a worker's fixture cannot manufacture -- see s.6 |
| `comp-schedule` | RUN (18:0xZ) | WITHIN BUDGET, 5 of 5 carriers; reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; no armed gate names ETFS_GUARDRAIL, the two producers, the orchestrator or the renderer | the ledger of GATES, not of prose obligations; the 336 prose NEEDS-READ rows are a reading list it does not grade |
| `comp-iam` | RUN on the two Lambdas the cells change | `etfs-reports-orchestrator`: 16 calls / 9 statements; `ses:SendRawEmail` GRANTED-BROAD (Resource `*`) at `:189` and `:277`, so `EG-s-8` and `EG-s-9` need NO IAM change; 9 UNRESOLVABLE-RESOURCE, 1 UNGRANTED (an s3 call outside these cells). `cot-etf-ownership-daily`: 5 calls / 9 statements, all UNRESOLVABLE-RESOURCE (runtime keys) | DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard "cannot be falsified by a resource check"; `bd-49f-etf-ownership-daily` and the `-canonical` twin were NOT run here -- `EG-s-11` decides which twin the port lands in, and `comp-iam service <twin>` is inlined on `EG-s-2` as a Phase-1 step |
| `comp-adversary` | RUN on this document after it was written | see the commit message for the composed declaration's counts (cited commits verified / paths stable) | it validates CITATIONS in this file, not the decomposition's correctness; a fresh cut has no prior artifact for it to read, so on the orders it is DECLARED-NOT-APPLICABLE at the cut (the assignee's instrument at report time) |
| lane read | RUN | every cell's write surface is the order's `<paths>` (RULING 1); the tree paths this lane writes (decompositions/, task-orders/, project.json) checked against HEAD bytes of `.owned-paths.yaml` at L6 | reads the DECLARED grant; the first spawn is the exercise |
| worker-executability | JUDGED, not exercised | 14 of 14 cells are a worker's (s.3); the two live-plane reads and the four deploying cells carry their stated caveats | the first spawn is the test; a capability a worker lacks is a row, not a tool request |

## 6. Bounds that bind EVERY order, inlined at L6 where they touch a cell

1. **NEVER-class (absolute, quoted at the cut):** no rung and no test may write a value that was not measured (PRD
   s.4 property 9; brief s.5 "NO RUNG MAY FABRICATE"). **No worker deletes a SERVED object** -- acceptance property 1
   ("a deleted slice ... is regenerated") is exercised on a COPY under a scratch prefix or on a date whose slice is
   already absent, never by deleting `daily/<partner>/<date>.json` in the served bucket (S3 deletes need a human's
   word). **No vendor egress by anyone**: rung 3 (`EG-sb-7`) is exercised as a STOP that names the dates and the
   provider and waits; a call to a provider is outside every order (ruling card 4, per-use only).
2. **The carve-out's width (PRD s.0):** ONE SES send, on the TERMINAL FAILURE PATH ONLY, from the same act that
   writes the refusal. No monitor, alarm, SNS topic, freshness service, schedule or polling loop. A cell that decomposes
   `EG-s-8` into anything with a timer has EXCEEDED the carve-out.
3. **Deploys (NEVER-2, NEVER-9):** Terraform via `safe-apply` only; `aws lambda update-function-code` is forbidden; a
   change-management entry opened at the start and closed at completion; served bytes verified against the built
   input (CodeSha256 vs the zip), never by filename. Every deploying order grants the ledger directory AND the sentinel.
4. **Rulings that bind the ports (`EG-s-1`, `EG-s-2`):** the REPORTING-OBLIGATION window (s.6 r.1), its terminus a
   SHIPPED SIGNAL read from the existence of the month's report (r.2) -- `CATCHUP_WINDOW_DAYS = 10` is NOT ported and a
   day-count window is not re-proposed; the ZERO-vs-MISSING producer contract is TOUCHED BUT NOT CHANGED (s.3).
5. **Rulings that bind the send (`EG-s-9`, `EG-s-13`):** JOIN not replace (r.3) as a TYPE decision at FOUR sites (s.7.3a:
   header keeps the joined string, envelope takes a list, on BOTH paths); `EG-s-13` is a prerequisite to the SEND
   ONLY (r.5), forward-only, restates nothing, notifies no partner (card 2).
6. **Class B is the trap (`EG-s-4`, `EG-s-6`):** upstream present + `priced == 0` is EXPECTED, not a hole, and no
   backfill is attempted against it (property 4).
7. **The four `EXERCISED` outcomes need a real event.** FWD-1 (a real missed day caught up), FWD-2 (a real refusal
   that reached a person), FWD-5 (both people received a real monthly report), FWD-7 (a real terminal message sent
   and read). A worker's criteria can prove the MECHANISM on fixtures and on ad-hoc QA runs (permitted for QA, never
   production evidence); the real event is read by the CTO at the close against the exercised artifact -- for FWD-5
   that is the scheduled `etfs-reports-monthly-run` fire (`cron(0 10 1 * ? *)` America/New_York), which is the
   acceptance's own discriminator and is NOT pre-empted by an ad-hoc send to a third person of a report `EG-s-13` has
   not yet aligned. **A `NOT_EVALUATED` grade at the first close on those four is the honest state, not a defect of
   this decomposition**, and the CTO's round-N analysis decides whether a closing-pass order follows.
8. **The spec is FROZEN mid-round.** A cell that looks wrong to a worker is a ROW at
   `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted
   `ETFS_GUARDRAIL-W<n>-S<k>`, never an edit; a seat's row carries no `W<n>`.

## 7. What this decomposition does NOT decide

- **The `<paths>` block of any order.** That is L6's, per order, and under RULING 1 it IS the worker's grant -- a
  surface omitted there is a wall, not an oversight.
- **Which `bd-49f` twin the port lands in.** `EG-s-11` answers it; `EG-s-2` is cut against the served writer and its
  face says so. If `EG-s-11` finds the served writer is the `-canonical` twin, `EG-s-2`'s surface address moves and
  that is a ROW on `EG-s-2` (a premise that does not hold), not a re-decomposition.
- **Which bucket `inf-etf-ownership-daily` actually reads.** `EG-s-12` answers it by a deployed-bytes diff; rung 2
  (`EG-s-7`) consumes the answer. If the answer is that the deployed function is NOT the repo's build input, that is a
  finding for the CTO's round-N read, carried in the row, and the ladder checks the bucket the DEPLOYED code reads.
- **The stale brief line (brief s.6a "does aj@ replace andrew@").** Answered by ruling card 3 (JOIN); not decomposed.
- **`s.3`'s falsifier.** If a cell finds the reporting-obligation window cannot be bounded by a shipped signal because
  the shipped artifact's path is not what the PRD assumes, **that is a SCOPE CHANGE to L2 and not a cell** -- the PRD
  says the terminus is a shipped signal and L5 agrees rather than absorbing it.

-- `2.0.0_SA_COO~B`, L5
