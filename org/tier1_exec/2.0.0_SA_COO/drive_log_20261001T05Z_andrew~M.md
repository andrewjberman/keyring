# 2.0.0_SA_COO~M -- drive log 2026-10-01 04Z-05Z (laptop `andrew`), IRPT_BCKEND workstream ~M

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE

Loop: `/canonical-drive IRPT_BCKEND` 10m (cron 9965f84e, armed off the LIVE_ARMS RELAUNCH row on Andrew-direct
2026-10-01 ~04:0xZ). Lease `IRPT_BCKEND~M`: FULL at launch, FAST from 04:31:33Z (`org/mcp/drive-mode.log` lines 30, 35;
Andrew-direct ~04:2xZ via 1.0.0_SA_CTO 103440), so the body is `/closer-drive`.

## Tick 39 (04:0xZ-04:5xZ) -- relaunch, then the FULL -> FAST boundary

| project | limb | act fired |
|---|---|---|
| IRPT_BCKEND ~M | L10 analysis in hand (sweep 5 @a50d8207bc) -> boundary | DRIVE FORWARD |

- Relaunch: registered, watcher armed, CTO 103429 / 103432 / 103440 / 103451 / 103470 and MSTR 103474 read and acked.
- A round-30 cut of three orders was drafted and dry-run at the base (5 build checks FAIL as expected, 2 controls
  PASS), then DROPPED uncommitted when the lease went FAST ("cut nothing new").
- Boundary @ad8e18d5f8 (merged CLOUD b749c4df8f): five stale Holdings orders `superseded` with pointers
  (m25-251, m26-261, m27-271, m27-272, m28-281); `STATUS~M.md` rewritten.

## Tick 40 (04:5xZ-05:3xZ) -- items 1-3 built, re-shaped by the real run

- First shape (pin 1f5d1049c3): the IB-mr-261 producer-level fold ported onto the IB-mr-291 classifier. Tests green.
- **The one real run refused at Cottonwood** (one ticker, two classes), and the hop walk showed the shape was wrong:
  the deployed route returns `snapshot.project()`, which re-derives totals per selection and drops unknown keys.
  A firm-wide fold is another client's money; the same drop is why `source_vendor_keys` (W2-19) never arrived.
- **Measured on the 49 Financial build:** 1,444,365,532.85 USD sits in TARGET nodes; positions of all bases exceed
  custody in 3,891 of 7,565 accounts. The bases are never summed.
- Second shape (route code 4e2feb5a32, contract cc99dea562): the fold lives in `holdings/snapshot.py::project`, takes
  actual positions only, serves `class_totals_remainder` as its own block, and carries the vendor keys. The producer
  is back at its base bytes.
- Checks: `test_aggregates.py` 12 passed; holdings Lambda suite 159 passed; investor_reporting suite 324 passed;
  `stage.py --check` 4 of 4.
- Real run: 9,295 slices over three real builds, 0 not tied, 0 invalid
  (`R30_SELECTION_CENSUS_20261001.json`).
- Half written and COO half signed; merged CLOUD 9a3eef4cb1 (LOCAL; origin/CLOUD 0abf99fcd4 by ls-remote ~05:29Z).
- Sends: 1.0.0_SA_CTO (half request), 2.0.0_SA_COO~P (who moves the two source-map pins after leg F5),
  2.0.0_SA_COO~D (interface published). The half-request message states the ls-remote time as "05:4xZ"; the read was
  at ~05:29Z.

## Not done, and why

- Release of the candidate: gated on the CTO half and on 2.0.0_SA_COO~P's leg F5 (same function).
- MDPF_SECCLASS BD_THREAD_R3 window: both halves are signed; the BD gold runner was still up from the 04:00Z fire at
  05:32Z, so invariant (i) is not met yet.
- H5 (the 14:15Z Holdings publication read): not due.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-pipescript deployed --firm bd | PASS | C_06, D_03, D_04 read STALE, as expected with the fix-forward not deployed |
| comp-read / comp-find | BLOCKED by the rail's pipe rule twice | used native Grep and Read instead |
| drive-mode.py arm | PASS after one refusal | refused a surface inside open order IRPT_DASHBD.TO-DB-b-4's paths; narrowed |
| safe-merge.sh | PASS x2, one refusal | refused once on another seat's staged channel row; clean on the retry |
| stage.py (holdings) | PASS | restaged four members from committed blobs; `--check` 4 of 4 |

**Gap found:** no instrument showed that a producer-level block cannot reach the page; the route's projection has to
be read. The earlier cut (IB-mr-261) and its census passed every check at the wrong grain.
