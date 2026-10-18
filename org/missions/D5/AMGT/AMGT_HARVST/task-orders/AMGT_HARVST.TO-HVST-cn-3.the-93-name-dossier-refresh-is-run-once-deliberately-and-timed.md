# AMGT_HARVST task order -- `HVST-cn-3` -- ROUND 99, workstream REFRESH-RUN: 93 `research_dossier` OBJECTS ARE ADDED BY THE REFRESH DRIVER, RUN ONCE DELIBERATELY WITH `--write`, TIMED (STAGED behind a signed never-widen pair and the host owner's CLEAR) (CTO round-98 analysis item 1 and addendum 2: the deliberate run's wall time decides the schedule's host)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cn-3.the-93-name-dossier-refresh-is-run-once-deliberately-and-timed</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cn-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task is created, changed or run by this order; the seat reads the scheduled-task list (step 0) for any task that runs a dossier, continuation or fund-form build in its window. The induction task `amgt-induction-daily` (site Z, 09:00 America/New_York = 13:00Z) writes the model blocks the run reads; the window closes by 12:30Z on 2026-10-19.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; the only writes are `PutObject` of new objects under `amgt/harvest/gold/research_dossier/security_key=<partition>/` (the driver's `dossier.write_one`, add-only). The BLAST RADIUS is 93 new gold objects that the gateway serves the moment they land, named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree whose `lib/research` is not the pin `56bacbc853`, a `--write` run over a name outside the 93, a run that skips the canary, a driver sliced or restarted so that the wall time is not the refresh's, one manifest path reused (the driver OPENS the manifest with mode `w`, so a second process on the same path ERASES the first process's lines), a guard whose printed block key differs from the written object's `inputs` model-block key (the CTO's A-3, a STOP per name), an object under the RAW slash spelling `security_key=BP/_LN_Equity/`, a `continuation.write_one` beside, a retry loop, and a half-landed write (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cn-1` (merged `56bacbc853`) built the refresh driver; its dry run over the 95 names reads `would_write=93 unchanged=1 skipped_guard=1`. **This is the first and deliberate `--write` run:** 93 dossiers are rebuilt to the 2026-10-18 model blocks, add-only, and the wall time of the whole refresh is MEASURED, because the CTO's host ruling for the schedule turns on it (over 600 s, the host is Fargate, not Lambda). State plainly in `cn3_before.out`: the served values that move are `model_rows` (the gateway returns it for these dossiers, see your `cl-4` reads) and the pointers (`dossier_key`, `content_sha256`, the dossier entry of `source_keys`, the counts); every other served value stays equal; the rollback is an S3 delete that is not yours to take; `NG/_LN_Equity` (level) and `PBR_US_Equity` (a guard stop, `HVST-cn-2`) are NOT in the list.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cn-1` and `HVST-cn-2` are `<status>complete</status>` and merged (`56bacbc853`, `8685b961ca`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/NEVER_WIDEN_HALF_COO_CN3_DOSSIER_REFRESH_DELIBERATE_RUN.md` (sha256 `f4bff167da62e20e9f8a22a1aaee2268cb828b3e989053a13db2175fd0b285e8`, committed `184cfe4b73`) and the CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CN3_DOSSIER_REFRESH_DELIBERATE_RUN_CTO_HALF.md` (`98c304e18f`). Read both; their conditions bind you. The order is STAGED until the issuer sends GO; the GO also names site Z's CLEAR (to 2026-10-19 12:30Z).
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cn3-dossier-refresh-deliberate-run.json`), with the window, the manifest and the keys written (or their count) in the close.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. **Work in a worktree of your own cut AT `56bacbc853` exactly** (the sparse set must include `lib/research`, `lib/`, `.tools/` and **`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/`**: `dossier.build` reads `research_docx_kpi_census.json` there, and two workers failed on its absence this round; check by running the canary name DRY first, below): print `git rev-parse HEAD` and `git diff 56bacbc853 HEAD -- lib/research` (it must print empty) in `cn3_before.out`. The list files `deliverables/2.0.0_SA_COO_W1/round99/cn3_names.txt` (sha256 `ebf416daab882f81a53352c0bc9a6d58844b06cf07bab3cdfd1135bcfbd6d291`, 93 lines) and `cn3_expected_moves.txt` (sha256 `c0612d22f6b08cf4705521fa621c168b5f017cc2651bcd293c84dd0cfe3f0414`, 93 lines `<name> model_rows <input kinds>`) are read from the repo at the issuer's branch (they are not in your pinned tree: read them from the shared checkout and print their sha256). You build NO new driver: the act is `lib/research/corpus/dossier_refresh.py` as merged, with its flags.
0. **Before-state, read only (`cn3_before.out`):** (i) the sha256 and line count of both list files; (ii) the count of objects under `amgt/harvest/gold/research_dossier/` and `amgt/harvest/gold/research-continuation/` (print them, paginated, with the denominator; the table held 1558 and 446 after `cl-4`; a different count: print it and name its writer or STOP); (iii) the scheduled-task list with its control (none runs a dossier, continuation or fund-form build in the window); (iv) the newest `model_block` stamp of `UNH_US_Equity` and of `BP/_LN_Equity` (BP's is the 17:06Z one on 2026-10-18; UNH's the 13:0xZ one; a NEWER stamp than the dry run saw means the list is stale: STOP); (v) the BEFORE gateway reads for `UNH_US_Equity`, `BP/_LN_Equity` and `BP-SLASH-_LN_Equity` with `fields` `["fund_form_ref","fund_of_record","last_stated_position","model_rows"]`, printing every returned `dossier_fields` and `continuation_fields` entry, `continuation_key`, `dossier_key`, `source_keys`, `content_sha256`, `as_of`, `duplicates_dropped`, `denominator_note`, `truncated`, `omitted_items` and `research_reports[]` entry; (vi) a DRY run of the canary name (`python -u lib/research/corpus/dossier_refresh.py --only UNH_US_Equity`, NO `--write`): it must read `status=WOULD_WRITE moved=model_rows` (any other status: STOP). DO NOT call `etfs_compare_peers`.
1. **Canary:** `python -u lib/research/corpus/dossier_refresh.py --only UNH_US_Equity --write --manifest cn3_manifest_canary.txt` (foreground). It must print `REFRESH UNH_US_Equity status=WRITTEN moved=model_rows ...` and a census with `written=1`. Read the object back (Branch A of the COO half, A-1 to A-3: the guard's printed block key equals the model-block key in the written object's `inputs`, else STOP). Then the gateway read of step 0 (v) for `UNH_US_Equity` again as `cn3_canary.out`: every returned entry other than the pointers is EQUAL to the before read, and the `dossier_key` is the NEW object. Anything else: STOP.
2. **The other 92, ONE process, TIMED:** print `date -u +%FT%TZ`; run `python -u lib/research/corpus/dossier_refresh.py --only <the 92 names of cn3_names.txt without UNH_US_Equity, comma-joined> --write --manifest cn3_manifest_main.txt` (foreground; **a manifest path that differs from the canary's**: the driver opens it with mode `w`); print `date -u +%FT%TZ` and the seconds between the two lines as `STEP2_WALL_SECONDS=<n>`. The census line must read `names=92 written=92 would_write=0 unchanged=0 no_new_model_block=0 no_today_model_block=0 skipped_allowed=0 skipped_guard=0 errors=0 mode=write`; any other count is printed and judged under section 3 (a name the driver SKIPPED by its guard or the allowed-moves rule is a correct stop that wrote nothing: Branch B). The driver prints request and byte counts only if it stops with `REFRESH-STOPPED budget-exceeded`; on a normal finish write `requests/bytes: UNMEASURED` (the pair says so). Do not slice the run, unless a `REFRESH-STOPPED` forces it: then say so, keep the output, run the remainder from the names not in the manifest and SUM the times.
3. **After (`cn3_after.out`):** (i) the dossier count equals step 0 (ii) plus the number WRITTEN (canary plus step 2) and the continuation count equals its start count; (ii) for EACH written name read the object back (Branch A, A-1 to A-3: `fields` equal to the build's outside `model_rows`, valued `model_rows` not lower than the stored one, the `inputs` model-block key equal to the guard's printed key) and print `branch_a_ok=<n of N>`; (iii) the gateway's dossier pick (`harvest_research.py::_pick_dossier`, read at the pinned tree) over a fresh listing of each written name's partition names the manifest key: print `pick_equals_manifest=<n of N>` (all names if your request budget allows, never fewer than 10, and always `BP/_LN_Equity` and `KMB_US_Equity`; name the denominator); (iv) the `BP/_LN_Equity` and `BP-SLASH-_LN_Equity` gateway reads after, against the before reads (only the pointers and `model_rows` move; BP's `dossier_key` is the new object for BOTH spellings); (v) no object sits under the RAW slash spelling; (vi) both manifests hold one line per name (1 and 92).
4. **Write `cn3_served.out`** ending with exactly these lines: `DOSSIERS_WRITTEN_AND_READ_BACK=PASS|FAIL`, `CANARY_GATEWAY_MOVES_AS_NAMED=PASS|FAIL`, `PICK_NAMES_MANIFEST_KEYS=PASS|FAIL`, `COUNTS_AS_EXPECTED=PASS|FAIL`, then `STEP2_WALL_SECONDS=<n>` (not a criterion: the number the CTO's host ruling waits on). In the ledger close say: no continuation was written; no object sits under the raw spelling; `NG/_LN_Equity` and `PBR_US_Equity` and the other names outside the list were not touched; the keys written (or their count).
5. Commit the ledger close WITH both manifests. Tell the issuer when the canary is written and read, when step 2 starts and ends (UTC times; the issuer owes them to site Z), and when `cn3_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rules: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, write nothing further, file one row and tell me:** the worktree is not at `56bacbc853` or the `lib/research` diff is not empty, or either list sha256 differs; a scheduled task runs a dossier, continuation or fund-form build in the window, or the induction task is about to fire (the window closes by 12:30Z); a name not in the list; the canary's dry run is not `WOULD_WRITE moved=model_rows`; **A-3 fails for a name** (the guard's printed block key differs from the written object's `inputs` model-block key; that name is a STOP, nothing further is written); a name WRITTEN whose moved field is other than `model_rows` or whose input kind is outside `{continuation, fund_form, model_block}`; `write_one` prints `unchanged` for a name the list says moves; the object key is not under the encoded (or plain) partition where the stored objects sit; AccessDenied, `GoldImmutableError` or a throttle (print its exact text); a read-back that differs; a count that is not +1 per name written; a missing manifest line; the canary read differs in anything the COO half does not name as expected.
- **After the last write, a difference not named here:** write it plainly, do NOT self-grade, finish the read-only steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted.
- **Expected and NOT a failure:** `KMB_US_Equity` reads `inputs_differ=continuation,model_block` (the build cites today's continuation; no continuation is written); the new objects carry the SAME `as_of` date (2026-10-18) as the stored ones and a different `inputs_sha16` and win the pick on `LastModified`; the printed key of BP is the raw `BP/_LN_Equity` and the object sits under `security_key=BP-SLASH-_LN_Equity/`; the driver prints no request or byte counts on a normal finish; a run slower than 600 s is a RESULT, not a failure (it moves the schedule to Fargate); site Z's `OG-ap-44` gateway release (one restart of about a minute) and its read-back may overlap your window and write no object: if a gateway read fails during the restart, repeat that one read.
- **Window:** from my GO to 90 minutes later, and never past 12:30Z on 2026-10-19; if step 2 has not landed by then, stop and tell me.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round99/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round99/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cn3-dossier-refresh-deliberate-run.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cn-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round99/cn3_served.out</invocation><expect>(?m)^DOSSIERS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cn-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round99/cn3_served.out</invocation><expect>(?m)^CANARY_GATEWAY_MOVES_AS_NAMED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cn-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round99/cn3_served.out</invocation><expect>(?m)^PICK_NAMES_MANIFEST_KEYS=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cn-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round99/cn3_served.out</invocation><expect>(?m)^COUNTS_AS_EXPECTED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that no continuation was written and that the dossier count rose by exactly the number written (the pair's counts); AC2 is the proof that the canary's served moves are only the named ones; AC3 is the proof that the gateway's pick names each written object.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cn-3.the-93-name-dossier-refresh-is-run-once-deliberately-and-timed.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cn-3.the-93-name-dossier-refresh-is-run-once-deliberately-and-timed` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cn-3.the-93-name-dossier-refresh-is-run-once-deliberately-and-timed.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads N insertions and 0 deletions; run the row gate against your row WITHOUT any override first (the `Z-S106` override must cover that pre-existing pair only).
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** every command in this order is foreground and unbuffered; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.
- The hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the bucket and prefix are AMGT's own).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, then sent with the GO.** Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34). Authority: the CTO's round-98 analysis (msg 8174) item 1 and addendum 2 (`6135e9a0fb`); pair COO half `f4bff167...` (`184cfe4b73`) and CTO half (`98c304e18f`, msg 8207); site Z CLEAR from both seats to 2026-10-19 12:30Z (msg 8208: CTO~Z 35778, COO~O 35777); owed to site Z through MSTR: the run's start and end times. Decomposition section 136, cell `HVST-cn-3`.
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; I check SC1's READ ack within 10 minutes of the handing and type a nudge if the seat is idle.
- **Why the order carries three things the cl-4 order did not:** (1) the sparse-set line for the CRO scan folder (my provisioning miss twice this round); (2) the distinct manifest paths (the driver opens its manifest with mode `w`, read at `dossier_refresh.py:435`); (3) the wall-time line, which the CTO's host ruling waits on.
- Dry run at the base (issuer, dell1, 2026-10-18 ~18:4xZ): all four criteria FAIL as expected (the file does not exist).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>99</round>
<workstream>REFRESH-RUN</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
