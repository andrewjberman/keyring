# CHECKPOINT -- `2.0.0_SA_COO~X` on AMGT_CORPUS, wind-down 2026-09-26 ~22:4xZ

**Why this exists.** Andrew, at this seat's terminal, 2026-09-26 ~22:0xZ, verbatim: *"wind down your session, closing any
workstreams into checkpoint document with any residue cleaned up and committed."* This file is the single carrier a
successor seat resumes from. Every figure below was read on the store or at the bytes in this session; pins are CLOUD commits.

## 1. Where the project stands

- **Round 6 CLOSED** (CTO L10 @`1e53f322f3`). FWD-17 (b) exercised and passes (IMB `--write` twice, `wrote 0` both).
- **Round 7 ISSUED** @`4051cbb215` (decomposition v7.0 in the same commit; source: round-6 analysis s.6). Five orders:

| order | cell | state | drain |
|---|---|---|---|
| `TO-CRPS-i-1` | continuation readers select the current `method_version` (Z-S45) | complete, re-graded VALID | `0c561835b6` |
| `TO-CRPS-i-2` | the band carries its calibration claim | complete, re-graded VALID | `afff33fe76` |
| `TO-CRPS-i-3` | the team's workbook Base-case cell, selected and cited | complete, re-graded VALID (AC4 is the CVO's) | `28912c4123` |
| `TO-CRPS-i-4` | key-glob census (Z-S39's `*`) | complete, re-graded VALID (`--plant` prints `plant_flagged 1`) | `0c309935f1` |
| `TO-CRPS-i-5` | fresh 19-outcome pass | **ISSUED, NOT SPAWNED** -- `<status>pending</status>`; by decomposition v7.0 s.4 it spawns only after act B's step 2 lands | -- |

## 2. The served drain acts (pair: COO `f283a6e15f`, CTO `8b27c6f2cc`)

- **Act A -- DONE and verified.** Model-block re-derive over 94 keys at HEAD `e2075ec93b`: derived 94 of 94; `band_basis` on
  exactly 53 (49 SERVED + 4 outside_band) and on 0 of the other 41; 0 disposition or served-ratio moves; 6861_JP, CSL_AU and
  NVDA_US on their prior stamps; CAT_US re-minted SERVED 0.597 with `band` and `currencies`. Evidence
  `deliverables/2.0.0_SA_COO~X/evidence/r7_actA_verify.txt`; change entry `amgt-corpus-r7-rederive-94` CLOSED @`6f0469ecb2`.
- **Act B step 1 -- RAN.** `continuation --write` at `amgt-corpus-continuation/2` from HEAD `50e4b87464`, 21:56-21:58Z:
  `names 95 rebuilt 95 existed 0 with_pillars 46 with_pdf_pillars 34`; 95 `put_performed True`, 0 `existed True`
  (`evidence/r7_actB_step1_continuation_write.log`). With i-1's readers, every name now serves its /2 continuation.
- **Act B step 2 -- NOT RUN, HELD.** The CTO's limb 4 is a GATE: step 2 (the dossier rewrite) runs only after the census
  reads `current_method_available 95 stale_pick 0`. The first gate run hit its 900 s timeout and printed no census line, so
  the gate was UNREAD when the wind-down came; step 2 was not started. A second run with a 3000 s timeout ALSO timed out
  (`evidence/r7_actB_gate.txt`: started 22:21:58Z, `rc=124` at 23:12:02Z) -- the census instrument is too slow as written (per
  name it recomputes current inputs and reads every stored object, and both readers recompute again). The gate is UNREAD. **The served plane is consistent meanwhile:** all 95 dossiers still
  reference their /1 continuation uniformly (none was rewritten), so no dossier corpus is split across methods.
- Change entry `amgt-corpus-r7-continuation-dossier` CLOSED: B1 LANDED (95 puts, proof above); B2 closed NOT RUN with a
  DELTA=0 proof (`evidence/r7_actB_step2_not_run.txt`: dossier partitions 95, objects 373, serves the last write 95 of 95 at
  22:47Z). The dossier rewrite is a NEW change entry for the resuming seat.

## 3. What a successor does next, in order

1. Read the limb-4 gate with a FASTER census first (the checked-in `checks/round7/continuation_pick_census.py` exceeds 50
   minutes): per name, list the partition once, read each object's `method_version` and `inputs` once, compute current inputs
   once, and call each reader once. If it reads `current_method_available 95 stale_pick 0`, run step 2: `python -m lib.research.corpus.dossier --write` (all names). Expected, from the pair: 95 new dossier objects, 373 ->
   468, no `unchanged ... wrote 0`; verify with `checks/round6/dossier_order_census.py` (`serves the last write 95 of 95`) and
   re-run the pick census (`stale_pick 0`). Stop limbs 5 and 6 of the CTO half apply. If the gate reads anything else, do NOT
   run step 2; file a row.
2. Close or release the act-B change entry with that proof; lift row `Z-S46` (its hold on `continuation --write` is spent:
   the /2 write ran under the pair).
3. Cut a worktree from CLOUD at that moment and spawn `TO-CRPS-i-5` (worker, slot `~5`); it must read the post-drain state.
4. Drain i-5, write the round-7 packet (`deliverables/2.0.0_SA_COO~X/ROUND7_DRAIN_END_PACKET.md`, the round-6 packet's
   shape, R-4 integers), and hand L8 to `3.0.0_SA_CVO~Z`. NOTE: `3.0.0_SA_CVO~Z` is itself WOUND DOWN (relayed by
   `1.0.0_SA_CTO~Z`, 23:18Z); its checkpoint `org/tier1_exec/3.0.0_SA_CVO/deliverables/SESSION_CHECKPOINT_20260926_Z.md`
   @`d8946646ab` parks AMGT_CORPUS round 7's L8/L9, un-parking when `TO-CRPS-i-5` reaches a terminal `<status>`. Whoever
   next holds that serial compiles it.

## 4. Rows open at this seat

| row | state | carries |
|---|---|---|
| `Z-S45` / `Z-S46` | BLOCKING, held | the reader split; i-1 fixed the reader; closes when step 2 lands with `stale_pick 0` |
| `Z-S47` | OBSERVATION | 6861_JP, CSL_AU, NVDA_US excluded from the re-derive: today's derive cannot reach the landed history their served blocks were built from (no raw-stamp selector). Round-8 input |
| `Z-W2-S11` / `Z-S48` | disarmed | i-3's selections are 0 of 42 plausible: the one-pager sets the Base-case numbers in a flanking column below a spanning title. Round-8 input |
| `Z-W2-S10` | carried | 1 of 3 pre-g-1 blocks re-minted (CAT_US); 6861_JP and CSL_AU wait on Z-S47 |

**Round-8 inputs already named by the CTO half @`8b27c6f2cc`:** the derive's stamp selection (Z-S47; a re-pull is vendor
egress and is not authorized by that half); `read_dossier` has no method-version preference (the same shape as Z-S45 on the
dossier's own `METHOD_VERSION`).

## 5. Residue -- cleaned

- Worktrees `C:/tmp/wk-crps6-1..5` and `C:/tmp/wk-crps7-1..4` REMOVED and their nine branches deleted (`git branch -d`, each
  measured merged into CLOUD first, none holding anything but its `.scratch/`), on the word quoted at the top.
- The MCP send path was down fabric-wide from ~17:0xZ; every message this seat sent since went by inbox file. Messages
  received in that window could not be acked (the ack tool is down); their files sit in `org/mcp/inbox/2.0.0_SA_COO/~X/read/`.
- NOT committed, by lane: `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/ingest_run.json` carries this
  seat's post-AIA re-ingest output (scan 2026-09-25T23:58Z, 95 resolved folders) over the 09-22 worker version, but the
  owned-paths gate refuses it (lane TREE_DELIVERABLES: the path's owner is `0.9.0_WK_AMGT_CORPUS~1`). It stays modified in
  the working tree; the evidence of that run is committed separately (`evidence/reingest_after_aia_20260925T235849Z.log`).
- Uncommitted files of other seats in the shared tree are theirs and untouched.

## 6. Pins

decomposition v7.0 + issuance `4051cbb215`; pair COO `f283a6e15f` / CTO `8b27c6f2cc`; act A `6f0469ecb2`; act B ledger-open
`50e4b87464`; rows Z-S47 `f283a6e15f`, Z-S48 `556b49c08d`. This lane does not push; push state is stated in the checkpoint commit.

-- `2.0.0_SA_COO~X`
