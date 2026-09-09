# NFRA_OUTSET — DECOMPOSITION (L5)

**v0.5** (2026-09-09 ~15:3xZ, `2.0.0_SA_COO`) — the L5 act on PRD **v0.5** @`1ac8679844` (the CTO’s mid-round addendum on the S23 ruling @`98722f9355`): `OS-s-21` re-worded to the ruling (its face already re-cut @`2e1d755943`), `OS-s-22` added. Round 3’s addendum sections are §19–§22 below; §0–§18 are LEFT UNEDITED.

**v0.4** (2026-09-09 ~14:4xZ, `2.0.0_SA_COO`) — the L5 act on the CTO’s ROUND-2 ANALYSIS @`d6fd9eca07` (merged @`5f0cd1a318`) and PRD **v0.4**, which adds two manifest rows (`OS-s-20`, `OS-s-21`) to §7. The analysis directs: *"2.0.0_SA_COO recuts from this analysis: two rows, both CloudOps, no worker fan-out; OS-s-20 after OS-s-19 (done), OS-s-21 buildable beside it with its accept gated on OS-s-20’s."* Round 3’s sections are §13–§18 below; §0–§12 are rounds 1 and 2’s and are LEFT UNEDITED.

**v0.3** (2026-09-06 ~03:1xZ, `2.0.0_SA_COO`) — the L5 act on the CTO's ROUND-1 ANALYSIS
@`a0500abe18` and PRD **v0.3**, which adds two manifest rows (`OS-s-18`, `OS-s-19`) to §7. The analysis
directs: *"2.0.0_SA_COO recuts from this analysis: two rows, both CloudOps, no worker fan-out."* Round 2's
sections are §7–§9 below; §0–§6 are round 1's and are LEFT UNEDITED so the record of what was decided
before the round ran is not rewritten by what the round found.

**v0.1** (2026-09-04 ~15:5xZ, `2.0.0_SA_COO`) — the L5 act on PRD v0.1 @`7fb59f239b` (RATIFIED; Andrew's
"all approved" on FWD-1..FWD-8 @`26da5ec0fa` and the L4 notifier frame id 94205). **Input:** the PRD's
17-row surface manifest (s.7), its two ordering rulings (s.8) and its one architectural choice (s.3).
**This document adds the ORDER, the SEATING and the ROUND FENCE. It re-litigates no row and invents no
surface** — the manifest's MECE check was run at L4 and is not re-derived here.

**Home:** `org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md` (lane TREE_COO;
versioned in place). **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b`. **Fabric:** laptop.

---

## 0. The cell set — 1:1 with the manifest, no cell invented

**`OS-s-n` IS manifest row `OS-s-n`.** (Re-identified from `OS-n` on `1.0.0_SA_CTO`'s ruling, Andrew-relayed 2026-09-04 ~16:3xZ: the gate's `CELL_ID_RE` requires a lowercase middle segment, so `OS-n` was UNEXPRESSIBLE and `OS-s-n` is the sibling shape every other project already uses. 353 ids moved across the PRD, this document and all 17 orders in one act; nothing was dispatched, so nothing is renumbered under a running worker.) 17 rows in, 17 cells out. The `claim`, `evidence`, `lane`, `verb`,
`depends_on` and `accept` columns are the PRD's and are authoritative; this document does not restate
them, so there is ONE carrier and it cannot drift. What follows is what L5 owns: the chain read, the
round fence, and the seating.

**Cell vocabulary (Rule 24, a NOT-EVALUATED value present so non-evaluation is never a verdict):**
`status` = **DONE** (graded) · **IN-FLIGHT** (landed, grade pending) · **OPEN** (not started) ·
**HELD** (blocked on a named decision, owner stated) · **NOT-EVALUATED** (this decomp did not measure it
and says so). **State coherence:** a CVO grade moves `status`; a ruling moves the PRD's `claim`, never
this file. At v0.1 **every cell reads OPEN** — an honest starting state, not a measurement.

⛔ **The `status` column of a decomposition DRIFTS AGAINST ITS ORDERS and nothing links them
mechanically** — measured twice on 2026-09-04, on NFRA_COMPEFFICACY (ten cells reading OPEN against
COMPLETE orders) and on NFRA_CLDGRPH (the same defect, found by the check-out). **The order is the
truth; this column is bumped at a round close and is one round behind between them.**

## 1. THE CHAIN READ — computed from the manifest's `depends_on` edges, not chosen

```
  M (dependency-independent chains) = 3
    chain A  15 cells  OS-s-1 -> {OS-s-2, OS-s-4, OS-s-5, OS-s-8, OS-s-15} -> {OS-s-3, OS-s-10, OS-s-12, OS-s-16}
                       -> {OS-s-9, OS-s-11} -> {OS-s-13, OS-s-17} -> OS-s-14
    chain B   1 cell   OS-s-6   (CloudOps, audit, no edges)
    chain C   1 cell   OS-s-7   (CloudOps, audit, no edges)

  longest dependency depth in chain A = 6
```

⛔ **THE BINDING FACT, AND IT IS A CEILING NO WORKER COUNT BEATS: 15 of 17 cells hang off ONE chain
rooted at `OS-s-1`, six levels deep.** `OS-s-1` is the Rule T budget fix, and the PRD's own ruling puts it
before everything that prints a denominator. So the project is *structurally* serial for its first
step, and wide only afterwards. **A fan-out chosen against the cell COUNT (17) rather than the chain
COUNT (3) would spawn workers that immediately block**, and each blocked worker is a live worktree, an
open branch and a drain the COO owes.

**M = 3 is therefore the cap on useful workers for round 1, and the real width is 1 until `OS-s-1` lands.**

## 2. THE ROUND FENCE — where L5 cuts the rounds, and why here

| round | cells | the fence's reason |
|---|---|---|
| **1** | `OS-s-1` · `OS-s-6` · `OS-s-7` | The only three cells with NO unmet dependency. `OS-s-1` is the PRD's own first ruling; `OS-s-6`/`OS-s-7` are the two `unmeasured` audits, and the PRD says plainly they "release `OS-s-4` and `OS-s-10`". Round 1 is the whole releasable frontier and nothing is held back. |
| **2** | `OS-s-2` `OS-s-4` `OS-s-5` `OS-s-8` `OS-s-15` | Everything that `OS-s-1` alone releases — the width the project actually has, five parallel cells at depth 2. |
| **3** | `OS-s-3` `OS-s-10` `OS-s-12` `OS-s-16` | Depth 3. `OS-s-16` sits here **only if `OS-s-15` decided BUILD**; if `OS-s-15` decides RETIRE, `OS-s-16` is struck by that ruling and the round is three cells. |
| **4** | `OS-s-9` `OS-s-11` | Depth 4, both on the seam `OS-s-10` builds. |
| **5** | `OS-s-13` `OS-s-17` | Depth 5. |
| **6** | `OS-s-14` | Depth 6, the last. |

⛔ **THE FENCE IS A PLAN, NOT A COMMITMENT.** Spine v3 L6 requires ONE issuance covering EVERY cell of
the decomposition; a *round* here is the dependency wave inside that issuance, and a worker holds a
QUEUE it drains in order. **No cell is deferred to "a later round" in the spine's sense** — a later
round exists only when the CTO's round-N analysis sends work back.

## 3. SEATING — and the two cells that are NOT a worker's

**Chain A (15 cells) → worker slots.** The verbs are `fix`, `build`, `wire`, `record` and one `decide`
against a repo surface; the lane is `0.8.0_AE_CloudComp`'s code, which a worker holds under the task
order's `<paths>` grant (RULING 1, Andrew 2026-09-04 ~04:58Z).

⛔ **`OS-s-6` AND `OS-s-7` ARE NOT WORKER CELLS, AND THE REASON IS THE LANE, NOT THE TOOL.** A worker has
`Bash`, so it *could* run an AWS read. But the PRD re-homes both to `0.7.0_AE_CloudOps` because each
reads a LIVE CLOUD PLANE — who holds `ecs:RunTask` on the trino task definition and `logs:GetLogEvents`
(`OS-s-6`), and a glue-bound parquet's refresh cadence and owner (`OS-s-7`). **A worker subagent is
registered nowhere, holds no cloud identity of its own, and its answer would carry the launching seat's
credentials while reading as the worker's** — an attribution the estate cannot check. These two go to a
`0.7.0_AE_CloudOps` SEAT as ordinary task orders.

⛔ **`OS-s-17` IS THE CVO's.** Its lane in the manifest is `CVO` and its acceptance is that a day's
proposals each cite the tool row behind them — a certification act. **The spine reserves that to
`3.0.0_SA_CVO`; a worker of the issuing COO inside it is the shape this estate has refused twice
(NFRA_COMPEFFICACY's passcraft roll-up cell, and the 2026-09-04 ~07:0xZ fork Andrew ruled "a").** ⚠ That sibling cell is named in PROSE and not by id: the gate's `CELL_ID_RE` cannot tell a CITATION of another project's cell from a DECLARATION of one of this project's, so an id written here would be counted as an 18th cell this issuance must cover -- measured, it was.

**So the seating is: 15 → 13 worker cells (chain A minus `OS-s-17`, which is chain A by dependency but not
by lane) + `OS-s-17` to `3.0.0_SA_CVO` + `OS-s-6`/`OS-s-7` to `0.7.0_AE_CloudOps`.**

## 4. THE FAN-OUT L6 WILL CARRY

```
fanout: 3 of 3 chains, cap 8, reason: 15 of 17 cells hang off ONE chain rooted at OS-s-1 at depth 6, so
        the useful width is the CHAIN count (3) and not the cell count (17); a fourth worker would
        block on OS-s-1 immediately and cost a live worktree, an open branch and a drain for nothing.
```

**One slot per chain**: `~1` drains chain A's 13 worker cells in dependency order; `~2` and `~3` take
`OS-s-6` and `OS-s-7`. ⚠ **`OS-s-6`/`OS-s-7` are SEAT orders, not worker orders** — the fan-out line counts
chains for the record, and the issuance addresses those two to `0.7.0_AE_CloudOps`, not to a
`0.9.0_WK_*` slot.

## 5. THE BATTERY — run at L5, with each instrument's blindness stated

| instrument | result | what it does NOT cover |
|---|---|---|
| the chain read | M=3, depth 6, computed from the manifest's own `depends_on` | it trusts the PRD's edges; a MISSING edge would show as false width, and L5 did not re-derive the dependencies from the surfaces |
| lane read | `OS-s-6`/`OS-s-7` CloudOps, `OS-s-17` CVO, 14 CloudComp — from the manifest's `lane` column | it reads the DECLARED lane, not `.owned-paths.yaml`; the `<paths>` grant is settled per order at L6, not here |
| worker-executability | 13 of 17 cells are a worker's | judged from verb + lane + surface; **not exercised** — the first spawn is the test |
| `comp-schedule` | NOT RUN at L5 | the gate ledger is an L6 preflight per order; running it here would date-stamp a reading L6 must take fresh |

## 6. What this decomposition does NOT decide

- **The `<paths>` block of any order.** That is L6's, per order, and under RULING 1 it IS the worker's
  grant — a surface omitted there is a wall, not an oversight.
- **`OS-s-15`'s answer.** It is a `decide` cell. L5 fences `OS-s-16` behind it and takes no position on
  whether the O2–O4 legs are reachable or retired.
- **§3's falsifier.** If a decomposed cell finds the artifact seam cannot be produced on a cadence the
  09:00 window relies on, **that is a SCOPE CHANGE to L2 and not a cell** — the PRD says so and L5
  agrees rather than absorbing it.

— `2.0.0_SA_COO`, L5


---

## 7. ROUND 2 — the two cells the round-1 analysis placed

**Input:** PRD **v0.3** §7 rows `OS-s-18` and `OS-s-19`, added by the CTO's L10 addendum @`a0500abe18`.
**This document invents neither.** Both are the manifest's, verb and lane included; L5 adds only the order,
the seating and the fan-out.

| cell | outcome | verb | lane | depends_on | why it exists |
|---|---|---|---|---|---|
| `OS-s-18` | FWD-3 | build | CloudOps | `OS-s-10` — COMPLETE | THE PUBLISH. Nothing publishes to the consumption seam and the runner's role holds no grant on any seam prefix. |
| `OS-s-19` | FWD-2, FWD-4, FWD-7 | deploy | CloudOps | `OS-s-11` — COMPLETE | THE DEPLOY. The served runner is dated 2026-08-25 and the upload belongs to no cell. |

⛔ **NEITHER IS A NEW IDEA AND THAT IS THE POINT.** Round 1 passed every criterion it was cut for while the
estate kept reading an eleven-day-old runner. The analysis names the cause as the PRD's own §3: it COSTED a
publishing step and assigned it to an ACCEPTANCE LIMB rather than to a MANIFEST ROW. **Naming a cost is not
assigning it.** These two rows are that cost, finally placed where work is owned.

## 8. THE CHAIN READ — round 2

```
  M (dependency-independent chains) = 2
    chain D  1 cell   OS-s-18   (depends_on OS-s-10, COMPLETE -> free)
    chain E  1 cell   OS-s-19   (depends_on OS-s-11, COMPLETE -> free)

  longest dependency depth = 1;  no edge joins OS-s-18 and OS-s-19
```

**Both are free NOW.** Their dependencies landed in round 1, so nothing sequences them against each other.

⛔ **BUT THE FAN-OUT IS 1, NOT 2, AND THE REASON IS NOT DEPENDENCY.** Row `NFRA_OUTSET-S10` recorded that
DEPENDENCY WIDTH and CONTENTION WIDTH are different quantities and that only the first is what a chain read
computes. Here a third quantity binds tighter than either: **both cells act on the SAME LIVE CLOUD ESTATE**,
and `OS-s-19` is a DEPLOY of the very runner `OS-s-18` must prove readable. Running them concurrently means
one seat granting an IAM role and publishing an artifact while another replaces the binary that reads it.
Neither a dependency graph nor a file-contention read shows that; the shared object is the ESTATE, not a file.

## 9. SEATING — one CloudOps seat, in order, and no worker

**Both cells to a single `0.7.0_AE_CloudOps` lane, `OS-s-18` first, `OS-s-19` second.**

⛔ **NEITHER IS A WORKER'S, AND THE BOUNDARY IS THE ONE THAT SENT `OS-s-6`/`OS-s-7` TO CLOUDOPS AT THE
ORIGINAL CUT** — an S3 deploy and an IAM grant are LIVE CLOUD ACTS. That ruling is now stronger than it was:
`OS-s-6` MEASURED that a worker subagent holds no cloud identity of its own and inherits the box's ambient
credentials, resolving to `Action:*` on `Resource:*`. Andrew accepted that posture for now @`8e89f1127f` as a
standing item for the next PRD that seats workers. **A worker performing these two cells would do so holding
unrestricted credentials under an attribution the estate cannot check.** The analysis says "no worker fan-out"
and the measurement says why.

**ORDER MATTERS AND IS NOT ARBITRARY:** `OS-s-18` proves the seam is readable by the runner's own role;
`OS-s-19` replaces the runner. Deploying first would put a new binary in front of a seam it cannot yet read,
and `OS-s-18`'s accept would then be graded against a runner that changed underneath it.

⛔ **`OS-s-19` IS A NEVER-2 CELL AND ITS ORDER MUST SAY SO.** It is a deploy to a served artifact, so its
`<paths>` grant names `org/critical_paths/change_management/` and `org/critical_paths/.open_deploys/`, its
accept requires the ledger entry OPENED at start and CLOSED at completion, and the assignee measures the
ARTIFACT before acting on any open entry it finds. A deploy cell whose order does not grant the ledger is the
same defect class as round 1's `<paths>` omissions — the assignee can do the work and cannot record it.

## 10. THE FAN-OUT L6 WILL CARRY — round 2

```
fanout: 1 of 2 chains, cap 8, reason: both cells are dependency-free and mutually independent, but both act on
        ONE LIVE CLOUD ESTATE and OS-s-19 replaces the runner OS-s-18 must prove readable. The binding
        constraint is neither dependency nor file contention but a shared live substrate, so the useful width
        is 1 and the two are seated in order on one CloudOps lane.
```

## 11. WHAT ROUND 2's DECOMPOSITION DOES NOT DECIDE

- **Which `0.7.0_AE_CloudOps` lane.** Seating is settled at L6 against a live read, not asserted here.
- **The IAM shape of the grant.** `OS-s-18`'s accept names the property (readable at the seam by the runner's
  own role); how it is expressed is the assignee's, on the estate's own IAM traps.
- **Whether the deploy needs a never-widen sign-off beyond the ledger.** That is CTO+COO at the act, per the
  standing NEVER rule, and is not pre-granted by this document.

## 12. A ROUND-1 CORRECTION CARRIED FORWARD, NOT SILENTLY FIXED

§3 above states *"`OS-s-17` IS THE CVO's. Its lane in the manifest is `CVO`"*. **That is FALSE against the
manifest, which reads `CloudComp` / `build`** — recorded as row `NFRA_OUTSET-S13`, disarm owner
`1.0.0_SA_CTO`. The issuance addressed `OS-s-17` to a worker and was right; only this document's prose was
wrong, and its downstream cost was a `build` cell cut with no write surface, repaired at `ed5c4e2b5b`.
**§3 is left as written rather than edited**: it is round 1's record, the row carries the correction, and the
disarm is not this seat's to take. This section exists so a reader of §3 meets the correction in the same
document.

— `2.0.0_SA_COO`, L5 round 2

---

## 13. ROUND 3 — the two cells the round-2 analysis placed

**Input:** PRD **v0.4** §7 rows `OS-s-20` and `OS-s-21`, added by the CTO's L10 addendum @`d6fd9eca07` (merged
@`5f0cd1a318`) on the CVO's round-2 slug @`11e9902247`. **This document invents neither.** Both are the manifest's,
verb and lane included; L5 adds only the order, the seating and the fan-out.

| cell | outcome | verb | lane | depends_on | why it exists |
|---|---|---|---|---|---|
| `OS-s-20` | FWD-3 | deploy | CloudOps | `OS-s-19` — COMPLETE @`9e023d20b5` (a DEPENDENCY EDGE: the host boots whatever runner sits in S3, `instance.tf:94-96`) | THE CONSUMER SWITCH. `ESTATE_OUTSET_SEAM_PREFIX` is set nowhere on the report host (`instance.tf:130-151`, eleven variables, not this one), so the served runner's `_stratum_propagation` returns `INSTRUMENT_UNAVAILABLE` without composing a key; setting it REPLACES the host (`instance.tf:83`). Row S16. |
| `OS-s-21` | FWD-3 | build | CloudOps | `OS-s-20` on the ACCEPT edge only (buildable in parallel) | THE CADENCE. The 13:03:50Z publish was by hand; `OUTSET_SEAM_MAX_AGE_HOURS` defaults to 26 and `runtime.env` does not override it, so the artifact reads STALE -> `INSTRUMENT_FAILED` from ~2026-09-10T15:03Z. Row S17. |

⛔ **A SEAM IS TWO ENDS AND A CLOCK** (the analysis §2). v0.3 placed the producer's publish and the consumer's read
grant; round 2 landed both and the served report renders exactly as before. v0.4 places the consumer's SWITCH and
the CLOCK. These are the last two members; the analysis names the test that would have found all four at L4.

## 14. THE CHAIN READ — round 3

```
  M (dependency-independent chains) = 1
    chain F  2 cells   OS-s-20 -> OS-s-21   (OS-s-20 depends_on OS-s-19, COMPLETE -> free NOW;
                                             OS-s-21 depends_on OS-s-20 on the ACCEPT edge only)

  longest dependency depth = 2 on the accepts, 1 on the builds
```

**`OS-s-20` is free NOW.** `OS-s-21` is BUILDABLE now and its ACCEPT cannot be read before `OS-s-20`'s: a scheduled
publish into a prefix the consumer never reads is a duplicate output path with a timer on it (the CTO's sharpening 3).
**Both accepts read on a SERVED DAY, the earliest being the 2026-09-10 13:00Z scheduled fire of the replaced host** — so
neither order can flip today, and that is correct: an accept read on the served day is the whole point of the row.

## 15. SEATING — one CloudOps seat, the act of `OS-s-20` first, and no worker

**Both cells to `0.7.0_AE_CloudOps~W`, `OS-s-20`'s replace first, `OS-s-21`'s build beside it.** Measured before
addressing (Rule 27, one project per instance): `~W` holds 0 open orders at 14:37Z (`to-check --all --assignee`,
denominator 2347 faces), is LIVE, and holds this project's whole context (`OS-s-6`, `OS-s-7`, `OS-s-18`, `OS-s-19`).

**NEITHER IS A WORKER'S** — a host replacement and a scheduler are LIVE CLOUD ACTS, the boundary that sent every
CloudOps cell of this project to that lane, and `OS-s-6` measured why a worker must not hold them (ambient `*` on `*`).

**THE ORDER IS THE ANALYSIS'S EDGE:** `OS-s-19 -> OS-s-20 -> OS-s-21` on the accepts. `OS-s-19` is done, so
`OS-s-20`'s replace is the first act, OUTSIDE the run window: the host self-stopped at 13:11:04Z today and the next
scheduled fire is 2026-09-10 13:00Z, so the window is open from now until then.

⛔ **`OS-s-20` IS THE "STOPPING EC2 / UNRECOVERABLE" CLASS AND ANDREW'S GO IN PRINCIPLE IS ON THE RECORD**
@`e1b44ba4cc` (his "All recs approved" ~14:2xZ at the CTO terminal): ONE host, ONE replace, to set the prefix, under its
OWN NEVER-2 entry, outside the run window, after `OS-s-19`, **with the orchestrator's target instance ID re-pointed and
verified LIVE before the entry closes** (`instance.tf:114-121`: the orchestrator starts the box BY ID; a stale ID makes
the 13:00Z fire start nothing, silently). The GO rides `OS-s-20`'s face; the executing lane does not ask again for the
same act; it authorises no other replace, no other host and no mechanism change.

⛔ **ONE REPLACE, NOT TWO — A SEQUENCING FACT THE SEAT MUST READ BEFORE ACTING.** If `OS-s-21`'s mechanism lives in
this host's bootstrap (a systemd timer or cron in `user_data`), every edit to `user_data` is ANOTHER replacement
(`instance.tf:83`). In that case the cadence lands in the SAME `user_data` change as the prefix, so the host is replaced
ONCE under ONE ledger entry, with the two accepts still read separately. If the mechanism lives off the host
(EventBridge Scheduler / SSM / a Lambda), the replace carries only the prefix. The choice is the assignee's (§17) and
the ledger entry names which.

## 16. THE FAN-OUT L6 WILL CARRY — round 3

```
fanout: 1 of 1 chains, cap 8, reason: the two cells form one chain on the accept edge (OS-s-20 -> OS-s-21), both act on
        ONE LIVE CLOUD ESTATE (the same host, the same Terraform state, the same seam prefix), and a second CloudOps
        seat would contend on the estate-report state lock and could force a second host replacement. Width 1, one
        seat, the replace first and the cadence built beside it.
```

## 17. WHAT ROUND 3's DECOMPOSITION DOES NOT DECIDE

- **The cadence's mechanism and its compute.** Where the two producers run on a schedule (on the host before the
  13:00Z run; an EventBridge Scheduler; SSM; a Lambda) and under which identity is the assignee's, inside the accept's
  bounds: the PRODUCER'S OWN trigger, never success-of-upstream as the only trigger, never a watcher on the consumer,
  writes ONLY the two seam keys. A pipeline trigger is not a monitor; the moratorium does not reach it (CTO @`e18317d0e0`).
- **How the orchestrator's target follows the replace.** `orchestrator.tf:37` reads
  `ESTATE_INSTANCE_ID = aws_instance.estate_report_runner.id` — a Terraform reference, so the apply re-points the
  Lambda's environment — and the Lambda reads it at import (`lambda_function.py:34`). Whether the applied function
  configuration and a fresh container carry the NEW id is VERIFIED LIVE (`get-function-configuration` against
  `describe-instances`) before the entry closes; the reference is the mechanism, the live read is the evidence.
- **The rollback shape of a replaced host.** A destroyed instance is not restored; the rollback is a further replace
  under the prior `user_data`. The ledger entry states it before the act.

## 18. THE S18 LESSON, APPLIED AT THIS CUT RATHER THAN LEARNED AGAIN

Row `NFRA_OUTSET-S18` (round 2, RULED @`cb43d05200`): **a `<paths>` block is a GRANT only for a `0.9.0_WK_*` serial**
(`owned-paths-validate.py` `_WORKER_SERIAL_RE`); for a SEAT the lane registry decides and the block can only narrow.
Both round-3 faces therefore name only surfaces `0.7.0_AE_CloudOps~W`'s lanes admit — resolved at this seat with the
resolver before the cut (8 of 8 candidate paths PERMITTED, rc=0; see the issuance commit) — and both batteries live
in the seat's own deliverables folder from the start (clause 4, the serial in the path). No `.tools/tests/` line, no
`org/modules/heatmap/` line.

— `2.0.0_SA_COO`, L5 round 3

---

## 19. ROUND 3, ADDENDUM v0.5 — one cell the S23 ruling placed, cut mid-round

**Input:** PRD **v0.5** @`1ac8679844` (`1.0.0_SA_CTO`, mid-round on Andrew's 2026-09-03 scope-change word), which RE-WORDS
`OS-s-21` to the S23 ruling @`98722f9355` and ADDS `OS-s-22`. **This document invents neither.** `OS-s-21`'s face was
already re-cut to the ruling @`2e1d755943` and the v0.5 row agrees with it (freshness cloud-side under a new role with the
minimum Put; drift device-side on the device's own timer, per-device key, the artifact carrying its device and tree
denominators; the accepts as ruled). `OS-s-22` is the one new cell.

| cell | outcome | verb | lane | depends_on | why it exists |
|---|---|---|---|---|---|
| `OS-s-22` | FWD-3 | wire | CloudOps (the runner's deploy path, OS-s-19's; code in `estate_report_runner.py`) | `OS-s-21` (the key layout), `OS-s-19` (DONE @`9e023d20b5`) | THE PER-DEVICE CONSUMER. `estate_report_runner.py:1844` reads ONE key; two devices on one key is last-writer-wins, a confident partial. Group A composes every `outset/<device>/comp_heat_drift.json`, renders each device with its own vintage and ceiling, reads QUIET and SILENT as different states, never sums devices; the single-key read is retired WITH the composition. |

## 20. THE CHAIN READ — round 3 with v0.5

```
  M (dependency-independent chains) = 1
    chain F  3 cells   OS-s-20 -> OS-s-21 -> OS-s-22
      OS-s-20  act LANDED (host replaced @2686fc81d6); accept pending the 2026-09-10 13:00Z served day
      OS-s-21  BUILDING (freshness cloud-side; drift device-side); accept on a served day
      OS-s-22  depends on OS-s-21's KEY LAYOUT (buildable once the per-device key is named, which it is on the face
               and in the row) and on OS-s-19 (done); accept on a served day with a real device artifact and a planted
               second-device control

  longest dependency depth = 3 on the accepts; the builds overlap
```

**`OS-s-22` is BUILDABLE now** against the key layout the ruling names (`outset/<device>/comp_heat_drift.json`); its
ACCEPT needs a real device artifact under that layout (OS-s-21's drift half) on a served day, so it reads no earlier than
the first 13:00Z fire after both the consumer deploy and a device publish have landed.

## 21. SEATING AND FAN-OUT — unchanged: one CloudOps seat, width 1

**`OS-s-22` to `0.7.0_AE_CloudOps~W`**, the seat holding `OS-s-20` and `OS-s-21` (continuity on one project, Rule 27).
It is a runner code change and a single S3 upload of the runner — the OS-s-19 shape exactly — so it is a NEVER-2 cell
with its own ledger entry, outside the run window, the consumer census (one functional consumer, the host's boot pull),
and the served bytes proven against HEAD by content. It does NOT replace the host (no `user_data` change; the host pulls
the runner at boot).

```
fanout: 1 of 1 chains, cap 8, reason: the three round-3 cells form one chain (OS-s-20 -> OS-s-21 -> OS-s-22) on one live
        estate and one served runner; OS-s-22 is the runner's deploy path, which OS-s-19 already exercised from this seat.
        Width 1, the same seat, cut mid-round on the addendum.
```

## 22. WHAT THIS ADDENDUM'S DECOMPOSITION DOES NOT DECIDE

- **The composition's rendering** (how group A lays out N devices, QUIET vs SILENT wording) — the assignee's, inside the
  accept: each reporting device by name with its vintage; a silent device `INSTRUMENT_FAILED` for that device only while
  the others render; a planted second-device artifact renders as a second row and never merges into the first's n.
- **Whether the planted control key lives on** — it is a QA artifact under a non-device name on the seam prefix, untouched
  after the exercise under R-5, exactly as the R2 probe is.

— `2.0.0_SA_COO`, L5 round 3 addendum v0.5
