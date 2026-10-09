# NFRA_CTLPLN decomposition -- round 6, workstream THREAD: read what the fabric already does, end to end (issuer 2.0.0_SA_COO~C; cut 2026-10-09 ~06:5xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** The L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.20261009.md` @333d2b37b3, ENRICHMENT LIST
E1-E8 (1.0.0_SA_CTO msg 107787: "cut E1-E8 in one issuance").

**Cut on.** PRD v0.22. Two reads of `python .tools/prd-signoff.py status NFRA_CTLPLN`:
- ~06:3xZ: ratified-text SIGNED, current.
- ~06:4xZ, after a later PRD edit (@6c5cf02601): ratified-text STALE. It was signed against ENDPOINT hash 33c11e398e69, and the
  section now hashes b6c8d5290b25. OWED BY 3.0.0_SA_CVO. The brief half is SIGNED (auto).

`.tools/to-pipeline-gate.py` LIMB 6 refused this issuance at the first attempt for that reason. The whole issuance, not E1 alone, lands
once the CVO re-signs; it was asked at ~06:4xZ. Re-read ~07:1xZ: ratified-text SIGNED by 3.0.0_SA_CVO, current, on v0.22
@6c5cf02601. The issuance goes out on that read.

**Why most of this round is not code.** Grades: 0 REALIZED, 18 advanced. Almost every advanced outcome is BUILT, and what it lacks
is one real exercise read from the record. A worker in a laptop worktree cannot run a Dell, message a seat or speak to Andrew. So
the round has three kinds of cell:
- **BUILD (worker, laptop):** an instrument that reads the exercise from git and the shared files. These are the five `CT-t-*` cells.
- **EXERCISE (a Tier-2 seat on the box):** a task order to that box's CloudOps. These are the two `CT-x-*` cells.
- **ISSUER ACT:** a read the issuer takes, or asks a non-Tier-2 seat for, at the close. These are listed below. The COO's one real run
  of each outcome is these acts.

## Measured at the base (issuer, ~06:4xZ, box/laptop @175217b43e)

1. `org/devices/state/`: laptop holds `open_calls.json` and `seats.json`; dell1, dell2 and sitez hold `open_calls.json` only. That
   leaves 3 of 4 boxes with no `seats.json` (E7).
2. `org/devices/crossbox/`: 10 files. One is CLOSED-BOTH with an ack (XB-...-a3f0, dell2 -> laptop). Nine are OPEN with no ack
   (E4). The gap: managers cannot commit `org/devices/crossbox/**` (lane NFRA_CTLPLN_FAST_C). The laptop asked 0.0.0_AB_MSTR for a
   one-folder grant (msg to 107719).
3. Hand-listed boxes (E5): `comp-find '(dell1|DELL1).{0,80}(dell2|DELL2)'` over `.tools lib org/devices`, corpus default, 1,262
   files. Source hits are `.tools/open-calls-scan.py`, `.tools/to-pipeline-gate.py`, `.tools/fabric-activity.py`,
   `.tools/open-calls-scan-schedule.ps1` and `org/devices/kit_python_install.py`, with 5 tests behind them. The analysis also names
   `.tools/remote-job.py` `DEVICES`. The census in `CT-t-3` widens this read (sitez and laptop lists too) before any edit.
4. Instruments that already exist: `org/devices/deploy_readback_check.py`, `.tools/named_commit_check.py`,
   `.tools/crossbox-call.py`, `.tools/box-sync.sh`, `org/devices/intake/intake_receive.py`, `.tools/seat-list.py`,
   `.tools/mstr-record-check.py`, and `.tools/open-calls.py list --all --cloud`.
5. Box branches on origin: `box/laptop`, `box/sitez`, `box/dell1`, `box/dell2`. `CLOUD` is written by 0.0.0_AB_MSTR through
   `.tools/box-sync.sh`.

## Rule 24

**Domain:** the eight enrichment items E1-E8 of the analysis.

**Subtraction:**

| Item | Served by |
|---|---|
| E1 | `CT-t-1` (the trace) plus issuer act A1 (the round on dell1) |
| E2 | `CT-x-1` |
| E3 | `CT-x-2` plus issuer act A3 (read aloud) |
| E4 | `CT-t-2` (the matrix read) plus issuer act A4 (the messages) |
| E5 | `CT-t-3` |
| E6 | issuer act A6 only (three reads by named seats and Andrew; nothing to build) |
| E7 | `CT-t-4` (the manager-day read, a JUDGMENT criterion) plus issuer act A7 (spawns, seats.json) |
| E8 | `CT-t-5` (the conflict census) plus issuer act A8 (one held-deploy read) |

No item is unowned. Not cut, per the analysis: FWD-9, FWD-11, FWD-13, FWD-14, FWD-16 and FWD-24.

**Same grain:** one instrument or one exercise per cell. **One intent each.**

**State coherence:** no `CT-t` cell changes a live seat, pushes, applies or sends. `CT-x-1` deploys one named commit and makes one
refused IAM write. `CT-x-2` installs one checked package and makes one refused download. Each is a WORLD order with its own ledger.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-t-1` | `.tools/thread-trace.py`: one round's hops read from git with start and end times (plan on the laptop, work on a box branch, integrate into CLOUD, grade on the laptop) | FWD-1, FWD-4 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~51` |
| `CT-t-2` | `.tools/crossbox-matrix.py`: the 4x4 directed matrix of cross-box files across all box branches, each pair's newest file with state, ack and age | FWD-3, FWD-22 | LOCAL | `~52` |
| `CT-t-3` | no hand-listed boxes: a census of every script and data file that lists boxes, each moved onto `lib/devices.py`; a fixture box then needs no edit | FWD-2 | LOCAL | `~53` |
| `CT-t-4` | the manager-day read: `mstr-record-check.py` over one day of each box manager's record, written as a read file; JUDGMENT criterion "no project ruling", graded by 3.0.0_SA_CVO | FWD-21 | LOCAL | `~54` |
| `CT-t-5` | `.tools/box-sync-conflicts.py`: box-sync merge conflicts per shared file and per box over a window, with the writers named | FWD-8 | LOCAL | `~55` |
| `CT-x-1` | one deliberate Dell deploy of a commit no other box has merged, read back byte for byte, plus one real IAM write the Denies refuse | FWD-10, FWD-5 | WORLD | `0.7.0_AE_CloudOps~DELL1` |
| `CT-x-2` | the click route finished on a Dell: receive, verify, prove, receipt, the lane's work run, outbound counted, one deliberate blocked install | FWD-15, FWD-17, FWD-18, FWD-19 | WORLD | `0.7.0_AE_CloudOps~DELL1` |

## Dependency chains and fan-out

The five `CT-t` cells share no file. Each writes only its own new tool and test, and `CT-t-3` writes the census-named files.
`CT-t-3`'s census list is disjoint from the other four tools by construction, since they are new files. `CT-x-1` and `CT-x-2` run on
dell1 and share no file with any `CT-t` cell.

There is no chain. `fanout: 7` (5 workers, run at most 3 at once for laptop disk; 2 dell1 orders).

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A1 (E1):** LGIC_BLANKFIX round 9 on dell1 is the thread. Its laptop COO plans it, dell1 works and pushes `box/dell1`, the
  integrator merges, and the laptop grades. The issuer asks the round's issuer and 0.0.0_AB_MSTR for nothing beyond their normal
  acts, then runs `thread-trace.py` on it and records the hop times.
- **A3 (E3):** the `CT-x-2` record is read aloud to Andrew, including the account-takeover question (his act, at his time).
- **A4 (E4):** 0.0.0_AB_MSTR is asked for one cross-box file per directed pair, carried by the managers and ACKed by bus id, once
  the crossbox lane grant lands. `crossbox-matrix.py` reads the result.
- **A6 (E6):**
  - 3.0.0_SA_CVO reads XB-20261008T203134Z-a3f0 against FWD-12 and FWD-22.
  - Andrew reads `open-calls.py list --all --cloud` once.
  - One call that a Dell CTO settles and that never reaches Andrew is recorded.
- **A7 (E7):** 0.0.0_AB_MSTR spawns one seat of each kind and asks what it is. Each box's manager runs `seat-list.py` so that its
  `seats.json` exists.
- **A8 (E8):** one box push carrying an unnamed pipeline script is read for its `SKIP: no deploy ran` / HELD-DEPLOY line.

## Carried rows ruled by the analysis (issuer acts)

- **W14-S32:** read the live step-G Deny once, then close.
- **D2-S1:** carry the windows_amd64 builds in the Dell kit.
- **S27:** one `.gitattributes` `eol=lf` line for the two files, in the next hygiene cell.
- **S37 half 2:** one naming line per APPLY pair, for ordinals 11, 19 and 20.
- **W14-S40:** compare to the post-edit render.
- **W13-S31:** dismissed.
- **The 9 INBOUND rows:** move to COMM_ASSIST.
