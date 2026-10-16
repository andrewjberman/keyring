# AMGT_HARVST task order -- `HVST-cc-5` -- ROUND 88, workstream RUNNER-ORDER: `wsj` AND `barrons` RUN THEIR FIRST COMPLETE DELL1 CYCLES AND EACH IS REPORTED (CTO round-87 analysis, item 5; CTO ruling msg 6776)

<!-- ===================== SEAT FACE -- read by 0.7.0_AE_CloudOps~HV1 ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-5.wsj-and-barrons-run-their-first-productive-dell1-cycles</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the registered `Opal Data Harvest - Continuous Cycle` is re-registered ONCE with the same set in a new order, from the SAME pin, by the same `install-cycle-schedule.ps1` path as `HVST-cb-15` step 9.
comp-iam: RUN at L5 -- no new grant, no key, no sign-in; the runner's own jobs only. The CTO bound this act (msg 6776): the SAME set `wsj,barrons,sa`, the SAME pin, NO seed, a new T0 after; the pin, the 5 GiB per-cycle bar including uploads, Branch F, C-i and C-k unchanged.
comp-adversary: RUN at L5 -- the adversary is a `sa` restart that re-stores articles it already holds (a duplicate, or an upload that reads a table), a `wsj` or `barrons` cycle whose zero uploads is read as a clean result, a report written from the runner's summary instead of its cycle record, and a stop that waits for a cycle end that is 10 hours away.
</preflight>

## 0. THE CELL

The runner takes publishers in series. Registered as `sa,wsj,barrons` (since `HVST-cb-15` Branch G, T0_3 `2026-10-16T08:40:17Z`) it is on the `sa` leg (about 22 of 242 jobs in 6 hours, a cycle of about 66 hours), so `wsj` and `barrons` have collected nothing on dell1 since 08:40Z and their uploader path under the pin rests on the `cb-13` pass. CTO addendum 4 owes each publisher's first dell1 cycle (run record, accepted count, GET bytes) or the measured cause of zero uploads. The CTO ruled YES (msg 6776) to the same mechanism amendment 2 used: stop at a job boundary, re-register the SAME set as `wsj,barrons,sa`.

## 1. START CONDITIONS (read at the start; any false: DO NOT START, file one row, and the issuer reads it)

- (a) The CTO's ruling msg 6776 (re-register as `wsj,barrons,sa`; condition on the `sa` restart below) and `HVST-cb-15` complete (`task-orders/AMGT_HARVST.TO-HVST-cb-15.sa-and-bbg-join-the-dell1-runner-seeded.md`, `<status>complete</status>`).
- (b) `<main>` is `C:\dev\ajb_workspace`; `<pin>` is the registered `WorkingDirectory` (`C:\dev\wk-harvest-runner-pin-ddd7dcdc38`); `<state>`, `<runtime>`, `<stop>` are exactly as in the registered task's own arguments. Read them, do not assume.
- (c0) You are a FRESH lane for this project (one project per Tier-2 seat instance: `0.7.0_AE_CloudOps~SC1` also holds an `MDPF_SECCLASS` order, so the runner work moves to you). `0.7.0_AE_CloudOps~SC1` has been holding the hourly reads of `HVST-cb-15` (its step 11): read the latest `deliverables/0.7.0_AE_CloudOps~SC1/round87/cb15_check_interim<N>.out` and `cb15_c_a4.out` first to learn the runner's state and its record forms, and read `task-orders/AMGT_HARVST.TO-HVST-cb-15.sa-and-bbg-join-the-dell1-runner-seeded.md` steps 2, 4, 5 and 9 for the stop, `-Plan`, registration and read forms this order cites. SC1's hourly reads end when YOUR `cc5_t0.txt` is written; do not run both.
- (c) The runner is Running on `sa`; record the log's last `JOB` line, the current `sa` cycle id and its pairs done in `cc5_before.out`.

## 2. THE ACT (dell1)

1. **Stop by the stop file, never a kill, at a JOB boundary:** create `<stop>`; wait for the log's `STOP-FILE ... no further cycle` line (a `sa` job can take an hour: if 90 minutes pass with none, STOP, file a row, change nothing); record the cycle record in `cc5_stopped.out`. `Stop-ScheduledTask`; the process census of `HVST-cb-15` step 2 (no `lib.opal_data_harvest` process left).
2. **Re-register, NO seed:** delete `<stop>` (`Test-Path` False); `install-cycle-schedule.ps1` as `HVST-cb-15` step 4 with `-Publishers wsj,barrons,sa` and the SAME `<pin>`, `<state>`, `<runtime>`, `<stop>`; `-Plan` first and read it (`--publishers wsj barrons sa`), then once without; `cc5_plan.out`, `cc5_register.out`. Just before `Start-ScheduledTask` write `cc5_t0.txt` with ONE line `T0=<UTC ISO ending Z>`, then `Start-ScheduledTask` once.
3. **The reads at +3 and +15 minutes** from that T0 in `cc5_reads.out`, in the `HVST-cb-15` step 5 form (R1 log fresh, R2 the exact list `wsj barrons sa`, R3 no console window, R4 checkpoint grows, R5 windows minimised, R6 per publisher the `JOB`/`STOP` lines, R7 the bar). If R7 exceeds 5 GiB: create `<stop>`, wait for the cycle record, do NOT re-register, tell the issuer at once.
4. **Each publisher's first cycle (the deliverable).** When `CYCLE wsj ...` and then `CYCLE barrons ...` appear in the log, read each one's `cycles/<publisher>/<cycle id>.cycle.json` and the ledger lines of its window and write, per publisher, ONE line in `cc5_first_cycles.out`:
   `CYCLE <publisher> <cycle id> asked=<n> new=<n> accepted=<n> failed=<n> upload_lines=<n> s3_get_count=<n> s3_get_bytes=<n>`
   (`accepted` = the sum of `stored` over that cycle's `JOB` lines; `s3_get_*` = the sum over that window's `run` and `upload-harvest` ledger lines), then the cycle's `run_record` paths. A cycle with `accepted=0` or `upload_lines=0` gets a following line `ZERO_UPLOADS_CAUSE=<what the run records show: no new articles, none acceptable, held, failed, or other>` read from the run records, never from the summary alone. `wsj` first (about 1 hour), `barrons` after (about 10 hours).
5. **THE `sa` RESTART CONDITION (CTO msg 6776, binding).** After `barrons` the runner starts `sa` as a FRESH cycle. It must not re-store articles it already holds: read the first `sa` `upload-harvest` lines after that restart and run `check --since <the sa restart time>` over `sa`; write `SA_RESTART_DUPLICATES=<n> SA_RESTART_UPLOAD_GETS=<sum>` in `cc5_first_cycles.out`. **A non-zero duplicate count, or any upload line above 50 GETs, is Branch F AT ONCE** (stop file, wait for the `STOP-FILE` line, `Stop-ScheduledTask`, delete `<stop>`, re-register `-Publishers wsj,barrons` from `<pin>`, start once) and the count comes back to the issuer, who tells the CTO.
6. **Hourly reads while you hold:** repeat the duplicate check over the publishers that have uploaded and the R7 projection into `cc5_check_interim<N>.out`; any `upload-harvest` line above 50 GETs, upload GETs above 1 GiB since T0, a duplicate, or R7 above 5 GiB is Branch F AT ONCE. The branches G and E of `HVST-cb-15` apply as written (G does not arise: `bbg` is off the list).
7. **While you hold (after step 3) also run `HVST-cc-4`** (`task-orders/AMGT_HARVST.TO-HVST-cc-4.the-bbg-page-closure-is-traced-to-its-cause.md`): it is independent of the runner and takes about an hour.
8. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when each of `wsj`, `barrons` and the `sa` restart check has its line.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cc5-runner-order-20261016.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-5"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--publishers wsj barrons sa --refresh-once</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/cc5_first_cycles.out</invocation><expect>(?s)CYCLE wsj \S+ asked=\d+ new=\d+ accepted=\d+ failed=\d+ upload_lines=\d+ s3_get_count=\d+ s3_get_bytes=\d+.*CYCLE barrons \S+ asked=\d+ new=\d+ accepted=\d+ failed=\d+ upload_lines=\d+ s3_get_count=\d+ s3_get_bytes=\d+</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cc-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/cc5_first_cycles.out</invocation><expect>(?m)^SA_RESTART_DUPLICATES=0 SA_RESTART_UPLOAD_GETS=0$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base AC1 reads `--publishers sa wsj barrons --refresh-once` (FAIL as expected, the registered list is `sa wsj barrons`); AC2 and AC3 files do not exist (FAIL as expected). If Branch F fires AC3 cannot read `=0`: write what happened, leave the cell `pending`, and the issuer reads it.
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-cc-5.wsj-and-barrons-run-their-first-productive-dell1-cycles.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cc-5.wsj-and-barrons-run-their-first-productive-dell1-cycles` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-5.wsj-and-barrons-run-their-first-productive-dell1-cycles.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- NEVER-2: open a ledger entry at the start (`org/critical_paths/.open_deploys/harvst-cc5-runner-order-20261016.json`, with its `change_management/` record) and close it at the end; the entry names the one scheduled task it re-registers.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-87 analysis (`ledger/ROUND_ANALYSIS.round87.md`, msg 6766) item 5; CTO ruling msg 6776 (YES, with the `sa` restart condition); CTO addendum 4 and its amendments 1 to 3 stand; Branch F and the 5 GiB bar unchanged; MSTR relays each publisher's first-cycle report to site Z (the CTO's analysis names it).
- **Measured at the cut (15:0xZ):** `sa` 22 of 242 jobs in 6 hours (AAPL and AMZN about 1 hour each); `barrons` 27 jobs in 70 minutes at the old pin (about 10 hours per 242 pairs); `wsj` 242 pairs in about 1 hour (cycle `20261016T054619Z`, new 0). So this cell holds about 12 hours before the `sa` restart check; it is this seat's long hold, and the `HVST-cb-15` hourly reads (SC1's) stop when this order's T0 is written (they are the same reads, restarted from this T0).
- **Not covered, named:** a per-leg budget with rotation (a later cell: the pass stays serial); `bbg` (off the list, `HVST-cc-4` names its cause); `ft`; an `sa` session expiry (a finding, no sign-in by any hand).
- **SENT:** with the round-88 issuance.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>88</round>
<workstream>RUNNER-ORDER</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
