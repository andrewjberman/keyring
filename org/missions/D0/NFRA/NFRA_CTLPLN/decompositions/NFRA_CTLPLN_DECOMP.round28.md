# NFRA_CTLPLN decomposition -- round 28: check 6 platform-aware, the intake demands page, FWD-7 by class, and the seat acts for FWD-8, FWD-23 and FWD-25 (issuer 2.0.0_SA_COO~C; cut 2026-10-16)

**Status: ISSUED in one issuance. FROZEN at the cut.** (A cell cut later in the round is an AMENDMENT of this document stating its gate limb, as in rounds 22 and 24-27.)

**Input.** `ledger/ROUND_ANALYSIS.round27.md` (1.0.0_SA_CTO) @22207d353b section 3 and msg 109661; the CVO's `ADJUDICATION_v31.md` @e401bbec00; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND27.md` @7f8eee22dc. **PRD:** v0.31. **Coverage entering the round (CTO table):** REALIZED 1, 3, 5, 15, 16, 17, 18, 19, 24, 28 (10); ADVANCED 2, 4, 6, 7, 8, 10, 11, 12, 14, 21, 22, 23, 25, 27 (14); PARKED 9; MOVED 13, 20, 26.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-aw-1` | Intake check 6 becomes platform-aware: when the installed copy and the held wheel have different platform tags, compare after CRLF normalisation and after removing a delvewheel patch block; a residual on the one listed build-metadata file (`numpy/__config__.py`) is recorded, not failed; any other residual fails as today. The four yfinance wheels pass on the new rule with no waiver (a read-only arm); the four existing waivers stay as issued. | FWD-15, FWD-16 (the waiver stays exceptional; CTO ruling 3) | LOCAL (a tool change tested on synthetic wheels, one read-only pass over four local files) | `0.9.0_WK_NFRA_CTLPLN~135` |
| `CT-ax-1` | One page in the intake folder, `APPROVAL_AND_SIGNED_FILE_DEMANDS.md`: what the tools demand of the approval file and the signed file (the `name==version` line, the per-wheel names and the `CHECK 8 SIGNED` line, the `WAIVE` form, the batch order, the dry-run commands); a test grades every example against the tools' own gate functions. | FWD-15, FWD-16 (CTO ruling 2) | LOCAL (a page, a test, one README line) | `0.9.0_WK_NFRA_CTLPLN~136` |
| `CT-ay-1` | FWD-7: classify the cross-box write overlaps the placement read prints (64 at the cut) into carrier, not-same-file and project-same-file, and report the project-same-file lines alone, from a script that reconciles with the tool's own count. | FWD-7 (CTO ruling 4) | LOCAL (a read-only script and a report) | `0.9.0_WK_NFRA_CTLPLN~137` |
| `CT-az-1` | **AMENDMENT 3 (below).** The waiver test's arm `g1` follows the platform-aware check 6 (one stale expectation, `failed` -> `passed`, in `.tools/tests/test_round27_waiver.py`); direct act. | FWD-15, FWD-16 (a consequence of CTO ruling 3) | LOCAL (one test file) | `0.9.0_WK_NFRA_CTLPLN~138` |

## Amendments

1. **`CT-aw-1` re-seated with AMENDMENT 1, 2026-10-16 ~10:5xZ.** Worker `~135` stopped on two BLOCKING rows (`W135-S1`, `W135-S2`) with AC1 8/8 passed, AC2 2 of 4, AC3 59/60. S1: the order's "change no existing case" froze one case that pins the pair the ruled rule reverses; the issuer withdrew it for that ONE case (the issuer rules inside its own decomposition). S2: the ruled normalisation left empty-line residue around the delvewheel block in numpy and pandas `__init__.py`; the CTO ruled (msg 109671): remove the block with up to 4 empty lines directly before or after it, then compare exactly. Gate limb: none graded the modification (the order file is an existing file; GATE (viii) `<placeholders>` is NONE and unchanged); criteria text and ids are unchanged. The slot is re-seated on the same branch with its prior commits named as inherited state.

2. **`CT-aw-1` re-seated again with AMENDMENT 2, 2026-10-16 ~11:0xZ.** The second seating passed AC1 12/12 and AC3 60/60 and read AC2 3 of 4 (`pandas/__init__.py`, one wheel-side empty line at the seam; row `W135-S3`). The CTO ruled (msg 109673): collapse the blank run on both sides at the one seam where the block was removed (at most 4 lines each side), then compare exactly; anywhere else a blank-line difference still fails. Gate limb: none graded the modification (existing order file; criterion ids and text unchanged).

3. **`CT-az-1` cut, 2026-10-16 ~11:4xZ (a fourth cell, direct act).** After the merge of `CT-aw-1` (`528891b0b7`) the issuer re-ran the neighbouring intake suites: `INTAKE-CHECK-TEST 60/60`, `INTAKE-RECEIVE-TEST 36/36`, `INTAKE-CLOSURE-TEST 10/10`, `INTAKE-FETCH-TEST 21/21`, but `.tools/tests/test_round27_waiver.py` read `WAIVER arms=19/20 ok=False`: its arm `g1` pinned the old verdict (`failed`) for the cross-platform CRLF-only pair that the platform-aware rule now reads `passed` (the same stale-expectation class as row `W135-S1`, in a file outside `CT-aw-1`'s paths). Cell `CT-az-1`: change that one arm's expectation (one test file, about 5 lines, `<risk>LOCAL</risk>`, `<direct_act>true</direct_act>`), worker `0.9.0_WK_NFRA_CTLPLN~138`. Dependency: `CT-aw-1` merged. Gate limb: a NEWLY-ADDED tree order graded by `.tools/to-pipeline-gate.py` at the cut (EXECUTING stage: coverage not graded).

## Driven by the issuer in this round (not cells)

1. **FWD-8, the E8 conflict read.** Run in the issuance's tick: `python .tools/box-sync-conflicts.py --since 2026-10-16T00:00:00Z` over a window in which two boxes each closed a full round (laptop NFRA_CTLPLN round 27; dell1 ADVI_COTBKF round 96): 227 integrator merges, 2 conflicted, 3 paths, all `org/devices/crossbox/XB-*.json`, 0 on a project file, channel or shared list. File `deliverables/2.0.0_SA_COO~C/E8_BOX_SYNC_CONFLICTS_SINCE_20261016.txt` (committed `a5c875bb33`). The CVO grades.
2. **FWD-23, seats.json from three boxes.** Three crossbox calls, one body (`deliverables/2.0.0_SA_COO~C/XB_JOURNEY_R28_FWD23_SEAT_LIST.md`): `XB-20261016T101128Z-0ff7` (dell1), `XB-20261016T101128Z-bfaa` (dell2), `XB-20261016T101129Z-a856` (site Z). Each box's manager runs `python .tools/seat-list.py write`, commits `org/devices/state/<box>/seats.json` and names one graded piece of work. The calls are committed at `14c36139ea` (LOCAL); the bus line goes out when box-sync has pushed that commit.
3. **FWD-25, one real spawn per seat kind.** A message to `0.0.0_AB_MSTR` (msg of 10:12Z) asking for the seat-start half through `/mstr-spawn`; the forbidden-act half stands at `46831c5dfe` (WARN mode).
4. **FWD-11 and FWD-4, FWD-12, FWD-22** are the CVO's reads (round-27 analysis rulings 1 and 5): no act here. If the CVO grades FWD-11 short, the CTO takes the deliberate whole-box reboot, which waits on Andrew's word on his 2026-10-14 hold.

## Held and carried

- **Held for a later round (the CTO's item 7):** FWD-10 (a deliberate Dell deploy, a real refused delete and a refused audit-trail write) and FWD-21(a) (a deliberately hung seat on an unwatched box); each needs its box CTO's word and a quiet window.
- **Andrew's acts (ruling 6):** FWD-2 (a real new machine), FWD-6 (a client-facing PROD push held until his word), FWD-14 (`b87f`), FWD-27 (logins from rc and muse and from off the tailnet).
- **Carried with an OWNER and the CONDITION that un-parks each:** as in the round-24 to 27 decompositions: `W8-S7`, `S9103`, `S9120`, `W89-S3`, `W12-S1`, `Z-S3` (before 2027-12-01), `S9125` (dell1, before 2026-12-31), `S9119`, `S9128`, `W121-S3`/`S4`.

## Rule 24

**Domain:** the CTO's round-27 section 3 enrichment list (items 1-6 acted on; 7 held; 8 the CVO's) against the 14 ADVANCED FWDs. **Same grain; one intent; disjoint write surface:** `CT-aw-1` writes `intake_check.py`, its suite and one new test; `CT-ax-1` writes one page, one test and one README line; `CT-ay-1` writes only its own deliverables folder; no two cells share a file. **State coherence:** nothing in this round deploys, pushes or calls AWS; the one read outside the repo is the four release-folder wheels, read-only. `CT-aw-1` changes how check 6 reads a FUTURE batch; the four existing waivers and every released record stay as issued.

## Dependency chains and fan-out

Three chains, no edges: (1) check 6, (2) the demands page, (3) FWD-7 classification; the three issuer-driven items run beside them. `fanout: 3 of 3 chains, cap 8, reason: three cells with disjoint write sets and no data dependency; the page describes the approval and signed files only and does not describe check 6.`
