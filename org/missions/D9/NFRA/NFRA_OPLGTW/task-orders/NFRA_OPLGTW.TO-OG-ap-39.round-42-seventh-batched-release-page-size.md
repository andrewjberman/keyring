# NFRA_OPLGTW task order -- `OG-ap-39` -- APPLY: the round-42 seventh batched gateway release -- the measured window page size, the db3 test that reads the worktree, the `absent_reason` codes documented in the client tools' notes

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-39</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-39</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- this release changes NO IAM and adds no env key; the same objects are read through the same roles.
comp-adversary: DECLARED-NOT-APPLICABLE -- the acts are the CTO's round-41 analysis items 1 to 3.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 0. AMENDMENT A3 (2.0.0_SA_COO~O, round 42, ~03:0xZ) -- READ THIS FIRST; it overrides section 1 where they differ

The page-size sweep `OG-ev-6` CHOSE 30 (`W/PAGE_SWEEP.json`; `ev6.AC1` PASS on my run; 60 partitions fails the growth clause at 38.8, 39.3 and 29.6 MB run medians, 120 fails growth and also returns 127 rows over the newest 120 partitions against 222, because `client_core._project`'s byte cap drops tail rows). So `OG-en-29` is SUPERSEDED and THIS RELEASE CHANGES NO PAGE SIZE. The release has TWO files only: `infra/aws/ec2/opal-gateway/app/tools.py` (`OG-en-28`) and `infra/aws/ec2/opal-gateway/tests/test_og_db3.py` (`OG-en-27`). Wherever section 1 names `client_adapter_bd49f.py`, `tests/test_og_en29.py`, `PAGE_PARTITIONS`, the chain step (c), `rows_hash_120_equal_live`, `served_page`, the arm `e13_page_size_in_effect`, or a first-page time, it NO LONGER APPLIES. In its place:
- Phase A: steps 1 and 2 as written (the take list is the two files; the live ref is `4257a2aa42`, the release is cut on it, `harvest_research.py` carried at blob `574959b682d4a13a0a429c45fa00b77b6caa2ab5`), then ONLY step 3(e), the 27-tool read live against candidate. `W/PHASE_A_OG-ap-39.json` = `{"body": {"release_sha", "tool27": {...as written, with `tools_list_names_equal`}}}` (no `chain`). The ask's widening reads: NO IAM, NO env key, NO tool added or removed, NO behaviour change (the answers are equal tool by tool); the only change a caller sees is the longer tool descriptions served by `tools/list`.
- Phase B: `W/CODE8_SERVED.json` carries `served_notes` = `{"tools_list_count": 103, "client_tools_with_notes": n, "window_read_busy_in_windowed_tools": true}` read from the INSTALLED code's tool registry in a fresh guarded process (the `client_*` tools whose served description carries an `absent_reason` code; 2 to 5) in place of `served_page`, and the arm `e13_notes_served` in place of `e13_page_size_in_effect`; every other field and the order of acts are as written (27 of 27 under the guard, the clock and failed units read BEFORE the ledger closes, `NRestarts` 0 through the 30-minute read-back, the unit limits unchanged).
- Checks: `ap39.AC1` and `ap39.AC2` were amended with this (dry-run: the good records read OK, the bad ones NO).

## 1. THE CELL -- `OG-ap-39` (decomposition addendum R3-T.119, round 42)

**METHOD = `OG-ap-38`'s, AS AMENDED (A1 to A3), read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-38.round-41-sixth-batched-release-hazard-repair.md` and followed step by step; this order states only what differs.** That includes the HARD-GUARD RULE (no gateway code runs on the host without it; the memory limit may be the address-space cap or the cgroup limit), the live-ref re-read, the re-cut in a clean sparse tree with the overlay disclosure, the three-half ask, the order of Phase B, the ledger opened with entry AND sentinel first, no `HALT_OVERRIDE`, the 30-minute read-back, and the host clock (`chronyc tracking`) and `systemctl --failed` read and PRINTED BEFORE THE LEDGER IS CLOSED.

APPLY: ONE code release on the live ref (read `services.opal-gateway.deployed_commit` at HEAD; it was `d077cef04333500595a7a531ebddc2f43e5f8789` when this order was cut; if another seat has moved it, STOP and file a row). No Terraform, no IAM, no env key, no change to the unit file, `deploy-to-ec2.sh` or `EC2_MANIFEST.json` by hand, one deploy, ledger `nfra-oplgtw-gateway-release-batch8`. The take list is taken whole from trunk (`box/sitez`) at `trunk_sha` (the GO names it), each file byte-equal to trunk's blob; for each, `git diff <live ref> <trunk_sha> -- <file>` must be exactly the hunks of the cell named (any other hunk is a STOP and a row):
- `infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py`: `OG-en-29` (`PAGE_PARTITIONS` set to the size of `W/PAGE_SWEEP.json` `chosen_partitions`, and the text that states the old size).
- `infra/aws/ec2/opal-gateway/app/tools.py`: `OG-en-28` (docstring lines only: the `absent_reason` codes; the line count is unchanged).
- `infra/aws/ec2/opal-gateway/tests/test_og_db3.py`: `OG-en-27`; `tests/test_og_en29.py` (new) and the existing window tests `OG-en-29` updated for the new size: `OG-en-29`.
NOT in this release (the check counts them at 0): `client_core.py`, `typed_scope.py`, `etfs_rivals_flow.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, `deploy/opal-gateway.service`, `EC2_MANIFEST.json`, the catalog and `app/refs/`, Terraform. If `OG-en-29` was CANCELLED (the sweep chose 30), the release carries `tools.py` and `test_og_db3.py` only and the issuer amends `ap39.AC1` before the GO.

### PHASE A (only on the issuer's GO, which names `trunk_sha`): re-cut, HOST MEASUREMENTS UNDER THE GUARD, ask. NO deploy IN ANY FORM

Steps 1 and 2 as `OG-ap-38`, in `C:/tmp/og-rel-batch8`, branch `rel-nfra-oplgtw-batch8`; write `W/ap39_release.json` = `{"base_sha", "release_sha", "trunk_sha"}` (FULL 40-character shas). In the release tree: every taken test file; the thirteen window test files plus `test_og_db3.py`, `test_og_en9.py`, `test_og_sv1.py` and `test_og_sv2.py` in BOTH orders; the full suite's failing set compared with the live ref's (name each difference; the baseline reds stay carried; `test_ogdb3_ac03` must now PASS in the release tree); `bash -n deploy-to-ec2.sh` and `--preflight-only`; the host-shaped import check.
3. **THE HOST MEASUREMENTS** (candidate staged in a scratch folder on the host, removed after; every run in a fresh process under the HARD GUARD; stop at 75 percent host used). Write `W/PHASE_A_OG-ap-39.json` = `{"body": {"release_sha", "chain": {"partitions_per_page": <the chosen size>, "guard": "<named guard>", "runs": [5 x {"median_growth_mb", "max_page_wall_s", "host_peak_pct", "rows_hash_120_equal_live": bool}]}, "tool27": {"tools": 27, "equal": n, "both_failed": [names], "candidate_answered_live_failed": [names], "live_answered_candidate_refused": [], "answers_differ": [], "guard": "<named guard>", "tools_list_names_equal": bool}}}`:
   - (c) THE 49F CHAIN AT THE NEW SIZE: the newest 120 partitions of the `OG-ap-36` test account paged at the chosen size, candidate against live code (the live code pages at 30), one call at a time, FIVE fresh runs under the cgroup guard (stated before the runs): the median of the five run medians of RSS growth per page 20 MB or less, no run median above 30 MB, the longest page of every run under 15 s, host peak under 75 in every run, and the combined rows of the newest 120 partitions equal (sha256) to the live code's in EVERY run (`rows_hash_120_equal_live`). The sweep (`OG-ev-6`) is the basis; this is the check on the release code itself.
   - (e) THE 27-TOOL READ, LIVE CODE AGAINST CANDIDATE, exactly as `OG-ap-38` step 3(e) (each tool in its own fresh guarded process, hashes only): `equal` plus the two lists must make 27; a tool that answered on live and is refused on the candidate, or whose answer differs, is a STOP and a BLOCKING row. Also record `tools_list_names_equal`: the set of 103 tool NAMES from `tools/list` is the same on live and candidate (the DESCRIPTIONS differ by the `OG-en-28` notes; say how many tools' descriptions differ, counts only).
   If either fails: STOP, file a BLOCKING row with the numbers, write NO ask, report.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-39.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: the `diff` by file with the hunk attribution; the `widening`, stated plainly (NO new IAM, NO new env key, NO tool added or removed; a window page reads the chosen number of partitions instead of 30, so one call can read more partitions and take longer, bounded by the measured numbers; the tool descriptions served by `tools/list` grow by the `absent_reason` notes; the honest limits: measured in guarded fresh processes, not in the service; the service has served zero window calls in earlier read-backs, so `Z-S338` stays open); the `order` of acts; `both branches`; the `rollback` (the live ref's tree redeployed through the same wrapper, PROVEN by a host md5 walk equal to the pre-deploy walk; the live ref's tarball sha256 in the ledger); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering under the guard; the `.env` key count not 65; `tools/list` changing from 103; host md5 differing beyond the released paths; host memory above 85 percent during the read-back; `NRestarts` above 0; the unit limits no longer reported; the marker not equal to the release sha; the first window page over 15 s); the gate lines and the overlay disclosure. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ap39.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. As `OG-ap-38` step 5 with ledger `nfra-oplgtw-gateway-release-batch8`, deploy from `C:/tmp/og-rel-batch8`, `DEPLOY_BASE_REF=<the live ref>`.
6. **The served read**, writing `W/CODE8_SERVED.json` (fields as in `ap39.AC2.sh`'s header: counts, seconds, bytes, words and booleans only): the 27-tool served read UNDER THE HARD GUARD must read 27 of 27; `unit_limits` unchanged (1468006400, 1258291200, 300, cgroup 1468006400); `served_page` = the first window page of the test account called on the INSTALLED code in a fresh guarded process: `partitions_per_page` equal to the chosen size, `partitions_read_on_first_page`, `first_page_wall_s` under 15; arms `e10_marker_equals_release_sha`, `e13_page_size_in_effect`, `e14_unit_limits_unchanged`, `e15_window_pages_equal_phase_a` (the first pages equal the hashes Phase A produced); the host clock and failed units READ AND PRINTED BEFORE THE LEDGER IS CLOSED (`clock_read_before_close`); the 30-minute service read-back every 60 s with `NRestarts` 0 and the count of `/mcp` window calls served (zero said in those words; `Z-S338` is re-read, never closed on zero).
7. Standing clauses as `OG-ap-38` step 7; close the ledger AFTER the reads; commit; run `ap39.AC2`; report once per phase; send me the ledger CLOSED time (I tell the CTO).

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no env key, no deploy-script, unit or manifest edit by hand, no object or item written to any bucket or table (scratch folders on the host removed after).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; print an `.env` value, a credential, an account number, a person's name or email, or object content; set `MUSE_CLIENT_ID`; override a gate other than the audited lane escape in step 2 of `OG-ap-38`; **run gateway code on the host without the hard guard**.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch8.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`. The manifest is NOT in your paths: it changes only at the close, when the deploy wrapper writes `deployed_commit` and the checksums.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-39"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ap39.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref before this release: yes.*: equal; the CTO-verified blob of the live ref 4257a2aa42 \(msg 35603\) is 574959b682: carried.*outside the take list 0 \(want 0\); take-list files missing 0 \(want 0\); not byte-equal to trunk's 0 \(want 0\).*the 27-tool read, live code against candidate under the guard: 2[5-7] of 27 equal.*ask has the three halves yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-39"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ap39.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*the 27-tool read 27 of 27 under the hard guard yes.*read BEFORE the ledger closed True: ok.*service restarts during it 0 \(want 0\).*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Report once per phase (counts, seconds, megabytes, hashes and booleans only). Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-39.round-42-seventh-batched-release-page-size.proof_of_spec.json` after Phase B and validate it with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). One release of the three LOCAL/WORLD builds `OG-en-27`, `OG-en-28`, `OG-en-29`, under its own never-widen (the CTO: "ships in a batched release under its own never-widen"). Staged behind `OG-ev-6` and the three builds; the GO names `trunk_sha`. The listener is NOT in this release (it ships alone as `OG-ap-40`, so a rollback of one never undoes the other).
- The method is `OG-ap-38`'s by reference because the applier reads the order file in full; the conditions that cost a round to learn travel by reference and are named above (hard guard, clock before close, `NRestarts` 0, the A2-style five-run chain rule stated first, the CT1 27-tool read, no relaxing a limit after a failed measurement).
- A1 (2.0.0_SA_COO~O, round 42, ~01:4xZ; the CTO's msg 35600): dell1's `HVST-cg-3` deploys a release off `d077cef043` on the gateway host between 01:50Z and 03:30Z (it touches `app/harvest_research.py` and two tests, and adds the key `fund_relation` to `research_reports`). NEVER OVERLAP IT: no host run of this order (Phase A measurements, Phase B) inside that window or before the `HVST-cg-3` ledger reads CLOSED. If `cg-3` landed, the live ref is ITS release commit, and the base of this release is THAT ref (read `deployed_commit` at HEAD at the GO). `harvest_research.py` is NOT in the take list and is carried unchanged (the release is cut on the live ref); CT4 as for `1753c741d9`: the ask NAMES the `harvest_research.py` blob hash (live ref = release), and `ap39.AC1` now prints and requires that equality. The CTO half binds that blob hash. Gate limb: none graded this amendment (the order stays staged).
- A2 (2.0.0_SA_COO~O, round 42, ~02:2xZ; the CTO's msg 35603): dell1's `cg-3` release LANDED at 02:06:03Z (once its ledger reads CLOSED the host is free for this order): the live marker is `4257a2aa42` (origin `rel-amgt-harvst-cg3`, parent `d077cef043`). THIS release is cut with `DEPLOY_BASE_REF=4257a2aa42` and carries `harvest_research.py` at the CTO-verified blob `574959b682d4a13a0a429c45fa00b77b6caa2ab5` (md5 `596c2995...`); a candidate on `d077cef043` or `efcc8ae19f` reverts `fund_relation` and is REFUSED. `ap39.AC1` now pins that blob (the release blob must equal it and the live ref's). The ask NAMES both the live ref `4257a2aa42` and the blob; the CTO half binds both. The trunk the take list is taken from may not carry `cg-3`; that is fine, the take list's files are not `cg-3`'s (STOP if any is). Gate limb: none graded this amendment.
- A4 (2.0.0_SA_COO~O, round 42, ~04:3xZ): Phase A of release `43a6659615` passed (`ap39.AC1` PASS on my run) and the CTO half (`03ba21f316`) and the CVO half (`fa5f0b30e9`) are SIGNED on ask `942adaf1e59e`, BUT the CVO's row `Z-S385` found that the `client_get_fees` note tells a calling model "a true zero ... report zero" about an unmeasured completeness. The issuer rules the fix BEFORE the deploy: cell `OG-en-30` (worker `~150`) rewords the note and audits the others. THIS RELEASE IS THEREFORE RE-CUT once `OG-en-30` has drained: a new `trunk_sha` (the GO names it), a new `release_sha` on the live ref `4257a2aa42` (unless it has moved), a new ask and a new hash, and the three halves re-sign on the one changed docstring; the take list (`app/tools.py`, `tests/test_og_db3.py`), the harvest blob pin, the page size (30) and every condition are unchanged. The signed Phase A of `43a6659615` is superseded and NO Phase B is run on it. Gate limb: none graded this amendment.
- A5 (2.0.0_SA_COO~O, round 42, ~05:5xZ): the re-cut `aa2efa2cf3` passed Phase A (`ap39.AC1` PASS on my run; ask `034d2c346e5d`); my half is re-signed on it (condition C13: the served fee note read from the installed registry). Phase B's `served_notes` record gains the boolean `client_get_fees_note_source_scoped` (the installed `client_get_fees` description names the source, does not claim a total, and holds none of "true zero", "report zero", "zero fees"); `ap39.AC2` requires it. Phase B waits on the CTO and CVO halves on the new bytes. Gate limb: none graded this amendment.
- Pre-cut: `ap39.AC1` base FAIL as expected (no records); `ap39.AC2` base FAIL as expected; the record controls (a run median 31, a page 16 s, rows that differ from live, four runs, a size that differs from the sweep, a tool refused on the candidate, tool names that differ, 27 not summing, no guard; and for AC2 a page size of 30, the clock read after the close, `NRestarts` 1, 26 of 27, a slow first page, a changed unit limit) all read NO in the dry-run.

- C4 READ (2.0.0_SA_COO~O, ~07:1xZ 2026-10-18): `ap39.AC1` PASS (blob `61d03a1610b9`, on `aa2efa2cf3`) and `ap39.AC2` PASS (blob `d7002c442739`) on my runs in the main tree; the proof instance is VALID (rc=0); ledger `nfra-oplgtw-gateway-release-batch8` CLOSED 2026-10-18T07:01:17Z, live release `aa2efa2cf3dee82030c00f85425f686132adcf4a` (the manifest reads it, previous `4257a2aa42`); 27 of 27 under the guard; the clock (Leap Normal, synchronised) and 0 failed units read 06:55:17Z, BEFORE the close; `NRestarts` 0 over a 30-minute read-back (157 `/mcp` requests, ZERO window calls: `Z-S338` re-read, not closed); the host md5 of `harvest_research.py` `596c2995...` equals the blob; the installed registry carries the notes on 5 of 5 client tools and `client_get_fees_note_source_scoped` is true (the CVO's `Z-S385` is closed on the live text; ruling row `Z-S387`). Gate limb: none graded this flip.

<status>complete</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
