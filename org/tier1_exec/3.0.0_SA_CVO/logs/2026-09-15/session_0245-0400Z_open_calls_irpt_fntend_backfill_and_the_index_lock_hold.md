# 3.0.0_SA_CVO -- session 2026-09-15 ~02:45Z to ~04:00Z -- /open-calls; the IRPT_FNTEND remediation backfill; the index-lock hold this seat caused

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Continues:** `session_2330-0245Z_oplgtw_closure_lgic_naming_r2_irpt_r7_and_the_remediation_census.md` (@ce91364847).

**Watchers:** no crons.
- Both Monitors were re-armed from the main root at each 30-minute expiry and confirmed with TaskOutput. Now: inbox
  `b12s0kryu`, surprise intake `bhc3peyco`.

## DONE (every act committed; LOCAL -- origin/CLOUD was last read at 6a5b276f8b)

### /open-calls (Andrew, ~02:5xZ) -- 0 sovereign calls at this lane

- **The sweep.** `git grep` over this seat's 5 session logs of 2026-09-14 and 2026-09-15 found exactly one item marked
  as Andrew's: the backfill scope.
  - The native Grep's glob first returned a false 0. The positive control (a known phrase in @ce91364847) exposed
    it, and the search was re-run with a different instrument.
- **The correction.** The backfill scope is NOT sovereign. Remediation rows are this seat's alone (lane `TREE_CVO`),
  so this seat decided it in lane and did not list it.
  - Decision (b): backfill projects still EXECUTING, one at a time, as the gate's L10 limb admits each; pre-issuance
    intake graduations EXCLUDED; closed projects recorded only.
  - Earlier messages had wrongly presented this as Andrew's call. The answer said so.
- **NOT-MINE pointers.** 2.0.0_SA_COO~D holds the DSGN_REBRND calls. The clean-context seat's standing mechanism was
  placed at Andrew by 1.0.0_SA_CTO.

### The IRPT_FNTEND backfill -- REMEDIATION_v4 @18c2d2a8aa

- **The rows** (built by the fork, checked by the parent): 42 rows. The id set EQUALS the census's missing set,
  re-derived by the parent in numeric file order, and 0 were excluded (every carrier is post-issuance).
- **Round split:** 24 from round 4 (C-S56..C-S58 and the backlog pass C-S65..C-S72) and 18 from round 5
  (C-S81..C-S84).
- **States:** 38 OPEN and 4 REMEDIATED. The REMEDIATED four are S27, S53, W4-S7 and S56, each citing the row that
  records the fix: C-S79 and C-S85.
- **The 17 ARMED rows** each carry `disarm`:
  - 6 are DISARMED with the citing row;
  - 11 remain ARMED with `at` null, because no row records their disarm.
- **Flagged:** 14 rows are written `per carrier <id>:`, because the carrier states no remedy in so many words.
- **Checks:** jsonschema reads 0 violations. The gate admitted it: 45 orders, 0 open; 227 items, 0 undispositioned.
  IRPT_FNTEND now reads 0 graduated without a row.

### The census record's section 5, and a duplicate this seat caused

- The fork committed section 5 @f2b9067e9f. That commit carried TWO copies of it, because the parent had appended its
  own copy on disk while the fork was writing.
- De-duplicated @c518b609af. The fork's copy is kept: it reads carriers from both files and cites every disarm. The
  parent's one unique item, the lock incident, is kept too, and the de-duplication is disclosed in the file.
- **The next candidates.** None can be admitted at this HEAD: each has an open order or undispositioned items.
  NFRA_CLDGRPH, for example, has 0 open orders but 49 undispositioned items.
- **Remaining:** at most 241 round-graduations are left to backfill, as their projects reach a gap between rounds.

### The index-lock hold -- this seat's

- The backfill commit ran in the background. Its post-commit hooks held the shared `.git/index.lock` from 03:22:47Z
  until some time between 03:32Z and 03:33:55Z, which blocked 1.0.0_SA_CTO~A's commit.
- This seat inspected and found the lock clear and PID 32684 gone. A later lock was traced by Win32_Process to
  2.0.0_SA_COO~D's commit, PID 38228.
- It replied to 1.0.0_SA_CTO~A at 03:43Z. That seat's commit landed as ee268aa92a, and it closed the issue at 03:46Z.
- Lessons, added to memory:
  - never background a commit on the shared index;
  - never edit a file a live fork of this seat may also write.

### Inbox

READ-acked: 96844, 96854, 96870 and 96873, all from 2.0.0_SA_COO~D (DSGN_REBRND Andrew-directs, and the Tax SMA brief
for a CTO). Nothing was asked of this seat.

## OPEN

- **Backfill (b):** the next project, when its gap between rounds admits it.
- **Undispositioned items:** NFRA_CLDGRPH and NFRA_COMPEFFICACY carry undispositioned investigation items. Carrying
  them is L9 work of this seat at each project's next drain-end.
- **LGIC_ENFORCE round 1:** L8/L9 at drain-end. Carry S5 against RULING DM, W5-S1's ordering question, S9's duplicate
  ids (count by id and content), and W7-S1's 504 of 1805 RAISE.
- **LGIC_NAMING round 3:** L9. S14's remedy is @3e8cf9e288, and FN1b and FN1c bind the grade.
- **DSGN_REBRND:** re-review the ratified-text half if the close batch changes it, including whether the fee-basis
  disclosure survives.
