# IRPT_FNTEND ROUND 6 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer).

**Input:**
- `2.0.0_SA_COO~F`'s drain-end packet, msg 96714. It reports 5 of 5 orders complete and drained (FE-s-37 .. FE-s-41).
- One issuance, @`79b2ddf558`, on decomposition v0.6 @`d4d8ae6f9a`.
- The round-5 analysis @`942e4ff992`, RULINGS S, U, V, T (the renderer half) and W.

**Push state:** LOCAL. This seat does not push. Portal DEV 35797660 is LOCAL too, and the PORTAL FREEZE stands.

**Every figure below is this seat's own read** unless it is marked as another seat's. The packet was treated as input
to re-derive, not as a verdict to inherit:
- every JSON fence of both investigation documents was parsed, at HEAD and at the issuance;
- all four ARMED fixes were read and quoted at portal DEV 35797660;
- a three-arm discriminator was run on the checker;
- the F40 re-capture was viewed;
- the source checks for F38, F39 and F41 were done at DEV.

**Result:**
- **L8:** 21 new rows, all dispositioned: 11 DISMISSED_WITH_REASON and 10 GRADUATED, over carriers `C-S87`..`C-S92`.
- **L9:** 5 judgment criteria graded:
  - 4 PASS, 3 of them with a named qualification;
  - 1 FAIL: F39-AC10, at the DirectoryEntry use site.

---

## 1. L8 -- THE COMPILE

**The population, by set difference over two git states:** round 6's new rows are those at HEAD that were absent at
the issuance commit `79b2ddf558`.

| | at HEAD | at issuance |
|---|---|---|
| `INVESTIGATION_v1.md` | 41 | 41 |
| `INVESTIGATION_v2.md` | 176 | 155 |
| total | 217 | 196 |

- **217 - 196 = 21 new. Rows lost: 0.** An independent `"id":` count agrees (41 and 176), with 217 unique ids.
- **By class and hazard:**
  - BLOCKING/ARMED: 4 (`W3-S27`, `W3-S28`, `W5-S5`, `S64`), each owned by `2.0.0_SA_COO~F`.
  - OBSERVATION/INERT: 17.
- **Before this record:** over BOTH adjudication files (v1 carries 44 rows and v2 carries 42), exactly 21 of 217 rows had no carrier, and they are exactly the 21 new rows. They match the packet's list.
- **Highest existing carrier:** C-S86.
- **After:** 0 of 217.

## 2. THE PER-ID LEDGER -- EVERY ROUND-6 ROW, ITS DISPOSITION AND ITS CARRIER

| row | class / hazard at intake | disposition | carrier | why, one line |
|---|---|---|---|---|
| `W3-S27` | BLOCKING / ARMED | DISMISSED | `C-S88` | no-status.test.ts:268-273: the view-NULL arm expects the absence wording; :297 negative control. DISARMED |
| `W3-S28` | BLOCKING / ARMED | DISMISSED | `C-S88` | holdings-in-a-browser.test.ts:56 imports the one flag rule; :424 flagged is accepted, unflagged rejected. DISARMED |
| `W5-S5` | BLOCKING / ARMED | DISMISSED | `C-S88` | holdings-no-answer.json reads perf-9 x0 and rev-49f-000091 x3, and is written by gen-fixtures.ts:463. DISARMED |
| `S64` | BLOCKING / ARMED | DISMISSED | `C-S88` | one-writer.test.ts:104-107 uses `git cat-file blob HEAD:`; there is a CRLF control at :620-623. DISARMED |
| `S63` | OBSERVATION / INERT | DISMISSED | `C-S88` | the resolution record for the three above, verified |
| `S65` | OBSERVATION / INERT | DISMISSED | `C-S88` | the resolution record for S64, verified |
| `W4-S13` | OBSERVATION / INERT | DISMISSED | `C-S89` | to_id is slug-tolerant and to_ref exact; neither steers a limb once bound (arm B) |
| `W3-S32` | OBSERVATION / INERT | DISMISSED | `C-S89` | one import line keeps one rule; the alternative is a forbidden second copy |
| `W5-S6` | OBSERVATION / INERT | DISMISSED | `C-S89` | 4 of 4 out-of-grant outputs byte-identical and unstaged |
| `W1-S66` | OBSERVATION / INERT | DISMISSED | `C-S89` | both true, per instrument (python ~2.03 s, node ~1 ms; this seat's measurement); no verdict moves |
| `W2-S32` | OBSERVATION / INERT | DISMISSED | `C-S89` | the contract's code list is IRPT_BCKEND's (round-5 s.6, IRPT_BCKEND-S52) |
| `W4-S14` | OBSERVATION / INERT | GRADUATED | `C-S90` | unbound callers still steerable, including this seat's own scripts |
| `W4-S15` | OBSERVATION / INERT | GRADUATED | `C-S90` | org/standards artifact-coverage battery 3/6 red at the cut, pre-existing |
| `W5-S7` | OBSERVATION / INERT | GRADUATED | `C-S90` | F41-AC5 reads the working copy, not the committed blob |
| `W1-S63` | OBSERVATION / INERT | GRADUATED | `C-S91` | vite-temp transient write through the junction |
| `W1-S64` | OBSERVATION / INERT | GRADUATED | `C-S91` | fe-s-19 comment still says "documented default" |
| `W1-S65` | OBSERVATION / INERT | GRADUATED | `C-S91` | two per-cell cacheDir overrides survive |
| `W3-S29` | OBSERVATION / INERT | GRADUATED | `C-S92` | adapt.ts:585 still renames an out-of-enum directory advisory to 'unknown' (the F39-AC10 FAIL) |
| `W3-S30` | OBSERVATION / INERT | GRADUATED | `C-S92` | validate.ts:448 pins advisory to three values |
| `W2-S33` | OBSERVATION / INERT | GRADUATED | `C-S92` | ReceiptPanel shows one code flagged and bare |
| `W3-S31` | OBSERVATION / INERT | GRADUATED | `C-S92` | fe-s-32's browser test rewrites ~2's committed captures |

**Totals:** 11 DISMISSED_WITH_REASON, 10 GRADUATED. `C-S87` is the grade record.

## 3. L9 -- THE FIVE JUDGMENT CRITERIA

**Vocabulary:** MET, MET WITH A NAMED QUALIFICATION, NOT MET. The verdicts are carried in `C-S87`'s `grades`, which is
the schema pattern `^[A-Za-z0-9]+-(AC|J)[0-9]+R?$` at HEAD @120afe354e. MET maps to PASS, and a qualification goes in
`reason`.

### F37-AC9 -- MET WITH A NAMED QUALIFICATION

**Criterion:** F29-AC15 clause 3, re-graded on this instance: *"no limb of the checker can be steered by the party it
grades."*

**This seat's discriminator:** `proof-of-spec-check.py` at HEAD, run on FE-s-29's instance in a workspace `.scratch`
copy, which was removed afterwards.

| arm | instance | run | result |
|---|---|---|---|
| A | committed | `--governing-order TO-FE-s-29` | VALID rc=0 |
| B | `to_ref` doctored to TO-FE-s-28 | `--governing-order TO-FE-s-29` | INVALID rc=1 |
| C | the same doctored instance | UNBOUND | limbs read TO-FE-s-28 |

- **Arm B** was refused by *"VIOLATION: governing-binding: the order being flipped is ...TO-FE-s-29... but the instance's decomp_ref.to_ref names ...TO-FE-s-28... -- REFUSED before any limb runs"*. Its count-bar and drives frames read TO-FE-s-29 (NEW).
- **Arm C** was steered: count-bar mode ANNOUNCE, and drives 8 of 8 NEITHER.

**The flip path is bound:** `to-pipeline-gate.py:2543` runs the checker with `"--governing-order", rel`, and self-test
arm `:865` asserts it. Under RULING S, whose scope is the flip, clause 3 is MET.

**Qualification:**
- Every unbound caller can still be steered: `receiving-check.py`'s L7->L8 route, and this seat's own intake/audit scripts (W4-S14).
- An instance edited after its flip never reaches the bound path.
- Arms B and C also carry an artifact-resolution violation, which comes from the scratch copy and is orthogonal to the binding.

### F38-AC9 -- MET WITH A NAMED QUALIFICATION

**Every browser verdict names its server.**
- At DEV, 8 files carry the precondition line: the helper, its own test, and six consumers (fe-s-19, fe-s-30, fe-s-31, fe-s-32, fe-s-38 and fe-s-40).
- The set of files importing `_dev-server` minus the set carrying the line is EMPTY.

**F35's "never seen mounted" is decided:** F19-AC4 reads *"BODIES MOUNTED: 2 of 2"* and F19-AC5 reads *"2 of 2"* on the
worker's own server, with 0 page crashes.

**Qualification:**
- This seat's instrument is a source census, not a browser re-run.
- RULING U leaves three residuals: W1-S63, W1-S64 and W1-S65 (C-S91).

### F39-AC10 -- NOT MET, AT ONE OF THE TWO USE SITES THE ORDER NAMES

**Criterion:** *"nothing the adapter hands the view says more, or less, than the document did."*

**What holds:** at DEV, `contracts/adapt.ts:466` hands the Holdings view an out-of-enum token as `{ outOfEnum: token }`.
F39-AC6 reads 3 of 3, and F32-AC5 reads 6 of 6 in a browser.

**What fails:**
- `adapt.ts:585` still reads `ADVISORY_FOR_WIRE[wire.cohort.advisory_status] ?? 'unknown'` for the DirectoryEntry cohort.
- That is the rename RULING W forbids, at the site W2-S29 names (`:558` at the cut).
- The worker's own record says *"STILL LESS THAN THE DOCUMENT"*.

**Named in mitigation:**
- The cut's grant did not reach it: `CohortValue` is shared by three axes, and `ScopeSummary.tsx` was not granted.
- No emitter sends an out-of-enum directory advisory today.

**The defect is W3-S29,** graduated in C-S92 for the recut.

### F40-AC10 -- MET

**Read from the re-capture** `fe-s-40_print_frozen_as_committed_1440.png`, 3 pages, which this seat viewed.

**The print no longer contradicts itself about its window.**
- Page 1 reads *"Period answered by the source 2026-01-02 to 2026-09-09"*.
- Page 3 lists requested 2026-01-01 and answered 2026-01-02 to 2026-09-09.
- It says *"The requested and answered dates differ only by days the market was closed (NYSE trading calendar (lib/trading_calendar.py)) ... the first trading day on or after either is 2026-01-02"*, beside *"The source answered the requested window"*.

**A flagged code reads as flagged:** all three bands and the Report availability row read *"REQUESTED_WINDOW_ANSWERED
[code not defined by the v1 contract]"*.

### F41-AC8 -- MET WITH A NAMED QUALIFICATION

**One writer:** the only `writeFileSync` of `fe-s-14-global.json` at DEV is `fe-s-14/gen-maps.ts:147`.

**The narrative speaks for its report:**
- In `fe-s-18-frozen.json`, the narrative's `performance_report_revision` = `rev-49f-000091` = its own performance member's `status.operation.revision`.
- 5 of 5 descendants read `rev-49f-000091` x3 and `perf-9` x0 as committed blobs. That is a different instrument than the worker's working-copy read.

**Qualification:**
- The second-writer census covers the Global map only.
- F41-AC5 still reads the working copy (W5-S7, C-S90).

## 4. THE ISSUER DEFECTS -- carried as a class, not re-opened

The packet names four of `2.0.0_SA_COO~F`'s own:
1. **Three cut-reach misses** (W3-S27, W3-S28, W5-S5). Tests and a map were enumerated by recall, not by subtraction from the corpus.
2. **One verification miss** (S64). The pre-drain re-run was made in the worker's own worktree, so it repeated the worker's instrument.

Each was caught before any drain, or by the owner's integrated re-run, and each is closed in drained code (C-S88). The
class is Rule 24's subtraction law and Rule 22's "a second seat's confirmation via the first seat's method is
repetition". It is the slug's to carry.

## 5. NOT CLAIMED

- **No browser re-run by this seat.** F38 and F40 are graded from source and from the committed capture.
- **No whole-suite run by this seat.** The four fixes are read in code; their green runs are the owner's (S63, S65).
- **No re-run of any mechanical criterion.**
