# AMGT_HARVST task order -- `HVST-bz-11` -- ROUND 85, workstream REFRESH-SITEZ (`1.0.0_SA_CTO~DELL1` msg 5209, `ledger/ROUND_ANALYSIS.round84.md` section 2 item 1 "close", row `AMGT_HARVST-Z-S119`): THE REFRESH IS READ CLOSED FOR `wsj` AND `barrons`

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-11.the-refresh-is-read-closed-for-wsj-and-barrons</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-11</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- READ ONLY; no schedule is touched.
comp-iam: RUN at L5 -- READ ONLY. NO sign-in, NO mint, NO refresh, NO Secrets Manager call, NO S3 write, NO task or process touched, NO plant.
comp-adversary: RUN at L5 -- the adversary is a read that grades a cycle that started before the new pin, a read that counts a still-running cycle as finished, and a seat that drives the line (a re-sign-in, a re-queue, a stop) to make it read MET.
</preflight>

## 0. THE CELL

`HVST-bz-10` re-registers the site Z runner with `--refresh-once`. This cell READS whether that closed Z-S119: for each of `wsj` and `barrons`, over the cycles that started at or after the new pin's start, exactly one verdict from `bz11_close_read.py`:
`ALIVE` (one ended cycle record with `completed` true and `stopped` none: the session lasted a full cycle), `NON_EXPIRY:<class>` (a `REFUSAL` in the cycle checkpoint whose class is `blocked`, `entitlement` or `other`: the refresh cannot fix it, and the class is the finding),
`REFRESH_FAILED`, `NOT_CURED` (the refresh was `done` and two `expired` refusals of that publisher are still recorded: it did not hold), or `WAITING`. The last line is `CLOSE=MET` when both publishers are `ALIVE` or `NON_EXPIRY`, `CLOSE=NOT_MET` when either is `REFRESH_FAILED` or `NOT_CURED`, else `CLOSE=WAITING`.

## 1. START CONDITION (read, not assumed)

`HVST-bz-10` is terminal and its seat wrote the file `deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_t0.txt` holding the line `T0=<UTC ISO>` just before it started the task. If the file is absent, this cell does not start (the script prints `CLOSE=WAITING reason=no-t0-file`).

## 2. THE READ (site Z box, read only, repeat until it reads a closing verdict)

1. Run AC1's invocation. Save the output of each run, with its UTC time, appended to `deliverables/0.7.0_AE_CloudOps~ZW/round85/bz11_reads.out`.
2. `CLOSE=WAITING` is an ORGANIC wait, not a failure: a runner pass is `bbg`, then `wsj`, then `barrons`, so `wsj`'s first cycle under the new pin starts only after the current `bbg` cycle ends, and a cycle runs several hours. **Read about once an hour. Do nothing else: no sign-in, no mint, no re-queue, no stop, no plant, no change to the task or any file under the state dir.**
3. `CLOSE=MET` or `CLOSE=NOT_MET`: stop reading. File the instance and report to the issuer with the last output and the two checkpoint paths the verdicts came from.
4. Anything odd: one row `AMGT_HARVST-Z-S<next free Z number>`, then keep reading.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-11"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round85/bz11_close_read.py --state-dir "C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/state" --t0-file org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_t0.txt</invocation><expect>(?m)^CLOSE=MET$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-11"><invocation>python -m pytest org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round85/test_bz11_close_read.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 is a site Z read and cannot run from dell1. AC2 is the instrument's own test (10 tests: every verdict, the CLOSE line, the cut, a control showing the cut discriminates, the t0 file) and runs anywhere.
- **Dry-run at the base (issuer, dell1, 2026-10-13 ~23:3xZ):** AC1 base FAIL as expected (no `bz10_t0.txt`: `CLOSE=WAITING reason=no-t0-file`); AC2 base PASS as expected (`10 passed`).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-11.the-refresh-is-read-closed-for-wsj-and-barrons.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-11.the-refresh-is-read-closed-for-wsj-and-barrons` and `decomp_ref.to_ref` the path of THIS order file.
  If the final read is `CLOSE=NOT_MET`, record AC1 as FAIL with that output: it is a RECORDED RESULT, not an error to engineer away.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS.** Append a row by BYTES and check the diff reads only insertions.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `ledger/ROUND_ANALYSIS.round84.md` section 2 item 1: "close: one full cycle per publisher with the session alive at its end, or the named non-expiry cause", and "if [Barron's refusal class] is not expiry, the refresh cannot fix it, and that is the finding".
- **The close this order reads is the CTO's two outcomes, plus two named negatives:** `REFRESH_FAILED` and `NOT_CURED` are not in his sentence; they are what a refresh that does not work looks like, so they read `NOT_MET` and go to his round-85 analysis (the bz-7 shape), not a re-try by this seat.
- **Why a `T0` file and not a typed time:** the start of the new pin is a fact the seat writes just before `Start-ScheduledTask` (bz-10 step 5); a time typed here would be a guess. The script also compares cycle ids (`YYYYMMDDTHHMMSSZ`) against it, so a cycle that was already running at the stop cannot be graded.
- **Organic wait, qualified:** a publisher cycle runs several hours (wsj 69 min then refused on 2026-10-13; bbg 9.5 h). It cannot be driven on demand, and driving it (a plant, a re-queue) would grade the seat, not the runner. Andrew's park order (CTO msg 5209) ends this seat after round 85; this read is the round's last act.
- Delivered as a crossbox ORDER through MSTR (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`), cut with HVST-bz-10.

**COMPLETE AS A READ, OUTCOME NOT MET, 2026-10-14 ~13:4xZ (issuer `2.0.0_SA_COO~W1`):** `~ZW`'s closing read (thirteenth, 2026-10-14T12:33:33Z, commit `c5134bfbc2` on origin/CLOUD) prints `CLOSE=NOT_MET`: wsj and barrons each had ONE refresh reported `done` (17 s and 16 s) and the same publisher's next job was refused `class=expired` again (`SignInRefused: 401 under --no-sign-in: no refresh`). The order directs AC1 FAIL as a RECORDED RESULT, so the delivery is complete and its outcome is NOT MET; this status does not say the refresh works. Verified by this seat on a detached checkout of origin/CLOUD @9098d3db03 (removed after): the instance reads `VALID (rc=0)` under `proof-of-spec-check --governing-order` and AC2 re-ran `10 passed`; AC1's `CLOSE=NOT_MET` is read from `bz11_AC1.out` on the committed record. NOT verified here: the two checkpoint files and `cycle_runner.log` live on site Z and were not read from dell1 (`~ZW` re-derived both verdicts from them). Row `AMGT_HARVST-Z-S121` (OBSERVATION / INERT, disarm_owner this seat, UNDER_INVESTIGATION) carries it to the CTO's round-85 analysis; why the refresh did not hold is undiagnosed.

<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>85</round>
<workstream>REFRESH-SITEZ</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>
