# AMGT_HARVST task order -- `HVST-bz-5` -- ROUND 84 (`1.0.0_SA_CTO~DELL1` msg 4670, `ledger/ROUND_ANALYSIS.round83.md` section 3 item 2, row `AMGT_HARVST-D1-W135-S2`): READ THE FIRST ENDED BBG CYCLE UNDER THE NEW PIN -- DOES EVERY FAILURE NAME ITS REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-5.the-first-ended-cycle-names-its-failures</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- a READ of one file on the site Z box. NO write outside this seat's deliverables folder, NO scheduled task started, stopped or changed, NO process ended, NO key sent to any window.
comp-adversary: RUN at L5 -- the adversary is reading a cycle record from BEFORE the new pin (the 05:46Z stopped record names no reason), or a record whose failures were requeued from the old pin's cycle, or planting a failure to make the read pass.
</preflight>

## 0. THE CELL

On 2026-10-13 05:52:43Z the site Z cycle runner started from the pin `wk-harvest-runner-pin-1c69fa35a3`, which carries `HVST-bx-3`: a failed pair's
`detail` is `<ExceptionClassName>: <message>` or `HTTP <status>: <message>` (redacted, at most 303 characters), not the bare word `error`.
Until now the only cycle record from the live runner (`20261010T221526Z`, 8 failures) named none. This cell READS the first bbg cycle record that
ENDED under the new pin and says how many of its failures name their reason. It is the close read of row `AMGT_HARVST-D1-W135-S2`.

## 1. START CONDITION (read at the start, not assumed)

A bbg cycle record exists in the state dir with `started_at` at or after `2026-10-13T05:52:43Z` and an `ended_at`. A cycle takes about 11 hours, so
this reads true about 17:00Z. **If none exists, DO NOT ACT: nothing is read, nothing is written, and the order stays open.** Check once an hour at
most, by the existence of the file only.

## 2. THE ACT (site Z box, once, READ ONLY)

1. From the repo root of the site Z checkout, after a `git fetch origin CLOUD` and a fast-forward to the commit that holds the script
   (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz5_cycle_read.py`, which you READ and run and never write; if it is
   absent, say so in one row and stop), run the script in the proof below. It reads
   `<state>/cycles/bbg/*.cycle.json` and writes nothing. `<state>` is the state dir in the scheduled task's own `--state-dir` argument
   (`...\wk-harvest-runner-pin-c1be67f53c\.runtime\harvest-cycle\state`).
2. Copy the cycle record you read, byte for byte, to `bz5_cycle_record.json` and print its SHA-256 and length beside the source's, and paste the
   script's one line into `bz5_read.out`. Print the record's `failures` rows (key, status, detail) in `bz5_read.out`.
3. **Read the line, do not grade it past what it says.** `FAILED=<n> NAMED=<m>`: `m` equals `n` and `n` is at least 1 means every failure names its
   reason. The script reads the first ended record that HOLDS a failure; when none does it prints the newest ended record with `FAILED=0`, which is
   NOT the close. **`FAILED=0`: do NOT plant a failure, re-queue a pair or touch the state dir to make the read pass.** Keep the order OPEN and read
   again at the next ended record. **Count only COMPLETED cycles** (`STOPPED=none` in the line) toward "failure-free": a record that an operator stop
   (or any other stop) ended is TRUNCATED, never counts as failure-free (it sampled a part of a cycle, and the stop was this programme's own act), and
   a truncated record that DOES hold a failure still serves the read. After TWO consecutive COMPLETED records with `FAILED=0`, file ONE row naming
   both readings and stop: a planted pair is a separate order under its own pair (CTO half, ADDENDUM 1 @469a566fa1).
4. Anything odd: one row `AMGT_HARVST-Z-S<next free Z number>`, then keep working. Do not stop, start, or re-register the task.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (the invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz5_cycle_read.py --state-dir "C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/state" --since 2026-10-13T05:52:43Z</invocation><expect>(?m)^CYCLE=\S+ STOPPED=\S+ FAILED=([1-9]\d*) NAMED=\1$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression: `NAMED` must equal `FAILED` and be at least 1. AC1 is a site Z read and cannot run from dell1.
- **Dry-run at the base (issuer):** (the script now takes the first ended record that holds a failure, else the newest) against the round-79 record (8 failures, bare `error`) the script prints `FAILED=8 NAMED=0` and AC1 does NOT
  match (FAIL as expected); against a copy whose details carry `HTTPError: ...` it prints `FAILED=8 NAMED=8` and matches; with no record since the
  cut it prints `NO-ENDED-CYCLE-SINCE ...`, rc 1.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-5.the-first-ended-cycle-names-its-failures.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-5.the-first-ended-cycle-names-its-failures`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4670, `ledger/ROUND_ANALYSIS.round83.md` section 3 item 2 and section 1 (C-S34): "D1-W135-S2 closes on the first ENDED cycle
  record under the new pin that holds a failure carrying its own detail ... If that cycle has no failure, the arm is a planted one."
- **The plant is NOT cut here.** A planted failure writes the state dir (a requeue) on a live producer, so it needs its own half pair and its own order. If this
  read lands `FAILED=0`, the issuer reads the row and cuts that order; nothing here waits for it.
- **What this read does and does not prove:** it proves failures from the live runner on the new pin carry their reason in the cycle record. It is a
  read of what the runner wrote, by the seat that runs it, and the CVO's L9 read is the independent one (corroboration cap, CLAUDE.md rule 22).
- Delivered as a crossbox ORDER through MSTR (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`).

**COMPLETE 2026-10-13 ~19:1xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** `0.7.0_AE_CloudOps~ZW` @5142731071 (in box/dell1). The cycle `20261013T080909Z` (the first to end on its own under the windowless pin) started 08:09:09Z and ended
  17:37:08Z, `stopped` `bot_check`, `completed` False, one failure whose `detail` is `ChallengeFailed: bot_check challenge_failed (bloomberg_press_and_hold)` -- the
  `<ExceptionClassName>: <message>` shape HVST-bx-3 put in the pin, not the bare word `error`.
- **AC1 PASS:** the live line `CYCLE=20261013T080909Z STOPPED=bot_check FAILED=1 NAMED=1`. Proof instance VALID rc 0 (`proof-of-spec-check --governing-order`), re-run by
  this seat in its own tree. Independent read by this seat on the committed record (514 B, sha256 5e652eaf6594...), copied into a `cycles/bbg/` fixture and read by the
  order's own script: FAILED=1 NAMED=1; the prior truncated record (320 B, sha256 52e0451bad83...) reads FAILED=0 NAMED=0, so the pattern discriminates.
- **What this does NOT prove:** the cycle did not complete (`completed` False), so it does not count toward failure-free and the Z-S117 count stays 0 under amendment
  @cea877dfc9. The read is the seat's own on a copy of site Z's record; the CVO's L9 read is the independent one. Nothing was planted, re-queued or driven to move the line.

<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>84</round>
<slot>site-z</slot>
<fabric>dell1</fabric>
