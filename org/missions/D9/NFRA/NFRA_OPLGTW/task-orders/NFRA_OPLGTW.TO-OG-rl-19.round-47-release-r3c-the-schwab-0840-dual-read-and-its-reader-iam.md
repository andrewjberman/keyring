# NFRA_OPLGTW task order -- `OG-rl-19` -- APPLY: release R3c, the Schwab 0840 DUAL READ: the reader IAM first (two in-place role-policy updates), the gate read, then four code files; under its own never-widen (round 47; Andrew-direct ~17:0xZ relayed: master 08403355 moves to `schwab/49financial/`; the CTO's rulings 2026-10-20 20:18Z, 22:02Z and 22:08Z; the laptop's binding order 110051)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-19</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rl-19</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- this seat did not run `comp-iam` at the cut; the IAM change is two in-place role-policy updates on the gateway's Schwab reader roles, and YOU run `comp-iam` for both roles before and after the apply (the act-time run) and record the permission lines it prints, with its denominator (counts and statement ids only). NOTHING ARMS THE PROBE LISTENER IN THIS ORDER.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (ferry 2026-10-20 20:18Z): "the edit is a DUAL READ: new path first ..., then the old schwab/08403355/ path ... Ship it as its own small release under its own signed pair (the IAM grant on opal-data-49financial is the named widening, scoped as in my 17:49Z ferry), in a 2026-10-21 07:00-11:30Z slot after batch16 closes. Do not fold it into OG-rl-18."
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-rl-19` (decomposition addendum R3-T.124, amendment A18, round 47, workstream ENRICH-R47-O)

**METHOD for the code release = `OG-rl-17`'s** (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-rl-17.round-47-sixteenth-batched-release-the-client-fences-the-size-caps-and-the-in-flight-guard.md`), through it `OG-ap-50`'s, read at HEAD and followed step by step: the hard guard, the live-ref re-read, the clean sparse re-cut, the three-half ask, the ledger with entry AND sentinel first, no `HALT_OVERRIDE`, the read-back, the host clock and failed units printed before the ledger closes, the landing. **METHOD for the IAM apply = `OG-ls-1`'s** (the order for the ListBucket narrowing, ledger `nfra-oplgtw-grants-ls1`): `safe-apply`, never a bare apply, the plan counts printed and recorded. This order states only what differs.

⛔ **THE BASE IS THE LIVE REF READ ON THE HOST** (`/opt/opal-gateway/.deployed_commit`); at Phase A it is batch16's release `8e3eddf959` (predicted, because batch16 is live by about 06:45Z on 2026-10-21); you RE-READ it at the start of Phase B and it must still equal `base_sha`, else re-cut. `6575999df5` must be an ancestor; dell1's four harvest files byte-equal.

**THE RELEASE TREE (exactly FOUR files over the base), under `infra/aws/ec2/opal-gateway/`:**
- `app/integrations/schwab/catalog.py`, `deploy/NFRA_OPLGTW_CONTRACT.json`, `tests/test_og_sk2.py`: WHOLE from trunk at `trunk_sha`, each byte-equal (from `OG-sk-2`, drained `bed56db150e`);
- `app/integrations/schwab/integration.py`: **NOT trunk's blob.** Trunk's carries `OG-rt-1`'s eight hunks (batch17's, which waits). Build it as the BASE blob with the one `OG-sk-2` hunk applied: `git diff c0a0ee2e9c2 <trunk_sha> -- infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py` (an import line and one changed condition) applied onto `git show <base_sha>:infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py` (it applies cleanly, measured by the issuer: offset -9). `rl19.AC1` recomputes that blob and compares hashes.
Nothing else: no deploy script, no unit, no `deploy/` file other than the contract, no `EC2_MANIFEST.json`, no `.tf` in the release tree. The organisation-standards copy of the contract (`org/standards/NFRA_OPLGTW_CONTRACT.json`) lands in the landing (Phase C), not in the tree.
**THE IAM, applied separately (not part of the tree):** `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` at `trunk_sha` (from `OG-sk-3`, drained `a4c6ecfd30c`): ONE root, the two resources `aws_iam_role_policy.schwab_data_read_policy` and `aws_iam_role_policy.schwab_catalog_read_policy`, applied with `-target` for exactly those two through `safe-apply` (the root may carry other drift: it is not yours to apply).

⛔ **THE ORDER OF ACTS IN PHASE B IS FIXED, and each step is recorded in `W/R3C_SERVED.json` `order`:**
1. **R3a is confirmed.** The laptop applies the bucket exemption on `opal-data-49financial` (its order `TO-BF-r2`, lane `0.7.0_AE_CloudOps~NFRA2`) and confirms THROUGH `0.0.0_AB_MSTR~Z`, who writes the confirmation into this seat's and mine inbox; you read that file (name it in `order.r3a_confirmation_ref`) BEFORE any apply. No confirmation file, no apply: wait and tell me.
2. **Terraform apply** of the two policies (plan counts must read add 0, change 2, destroy 0 BEFORE you apply; any other count is a STOP).
3. **THE GATE READ**, as `gateway-schwab-catalog-read-role` (the same assume path the gateway uses, through the hard-guarded fresh process): ONE `GetObject` of `schwab/49financial/state/complete/date=2026-10-20/08403355.complete.json` and ONE `ListBucket` with prefix `schwab/49financial/state/complete/` on `opal-data-49financial`. They must answer **NoSuchKey** and **an empty list**. **`AccessDenied` is NOT a pass: STOP, do not deploy the code**, keep the applied policies (they are inert), report to me with the exact error code.
4. **Only then the code deploy** (as `OG-rl-17` step 5).

⛔ **WINDOW:** 2026-10-21, after batch16's ledger is CLOSED and not before 07:00Z; the CTO's slot is 07:00Z to 11:30Z; the abort line is `/health` 200 within 60 s of the restart. The cutover window of the laptop opens 12:00Z; if R3a has not landed by 11:30Z, R3c ships after R3a inside that window and I tell COO~SB that R4a waits for R3c. Announce to `0.0.0_AB_MSTR~Z`. Phase A runs at once; Phase B only on my GO naming all three halves signed and the laptop's R3a confirmation.

⛔ **STANDING CONDITIONS:** the ask carries `process-wide state this change touches: ...`; here: no process, logger, signal or environment key changes (the dual read is code in the Schwab catalog read per request, and two IAM policy bodies); `tools/list` does NOT change (103); the stored grants are untouched; the OLD location keeps being read exactly as today (the old-form masters never touch the state bucket); every Phase B prints the journal `POST /mcp` count AND the audit-lake count for ONE window.

APPLY: ONE code release, ledger `nfra-oplgtw-gateway-release-r3c` (the Terraform leg is a leg of the SAME entry), sentinel first.

### PHASE A (only on the issuer's GO, given now): re-cut, HOST MEASUREMENTS UNDER THE GUARD, plan, ask. NO deploy and NO apply IN ANY FORM

Steps 1 and 2 as `OG-rl-17`, in `C:/tmp/og-rel-r3c`, branch `rel-nfra-oplgtw-r3c`; write `W/rl19_release.json` = `{"base_sha", "release_sha", "trunk_sha", "live_ref_host"}`. In the release tree: `tests/test_og_sk2.py` and the existing catalog, contract and Schwab tests in BOTH orders (`.../r38/checks/_bothorders.sh`), the full suite's failing set against the LIVE ref's per test id (name each difference), `bash -n deploy-to-ec2.sh` and `--preflight-only`, the host-shaped import check.
3. **THE MEASUREMENTS** (candidate in a scratch copy on the host, removed after; every gateway-code run in a fresh process under the HARD GUARD; stop at 75 percent host used; the running service is NOT touched):
   - **(a) The probes.** Run the python probe of `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk2.AC1.sh` against the candidate tree and count the labelled lines that read `ok`: `probes` = `{"sk2_ac1_ok": 13}`.
   - **(b) Old-form reads unchanged.** In ONE fresh process, with a fake S3 client, call `Catalog.read_marker`, `Catalog.list_dates` and `catalog.marker_locations` for `08242234` and `08335338` with the live ref's catalog and the candidate's: the answers and the calls made are equal (the state bucket is never called). `old_form_unchanged` true.
   - **(c) The plan.** `terraform plan -lock=false -target=aws_iam_role_policy.schwab_data_read_policy -target=aws_iam_role_policy.schwab_catalog_read_policy` in `infra/aws/terraform/opal-gateway/` at `trunk_sha` (the plan only; no apply): `terraform_plan` = `{"add": 0, "change": 2, "destroy": 0, "targets": [the two addresses]}`. Any other count is a STOP and a BLOCKING row.
   Write `W/PHASE_A_OG-rl-19.json` = `{"body": {"release_sha", "tests": {"named_passed", "named_failed": 0, "suite_difference_named": true}, "probes": {...}, "old_form_unchanged": true, "terraform_plan": {...}, "process_wide_state": "..."}}`. Anything failing: STOP, a BLOCKING row, no ask.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-rl-19.md`, for THREE halves under headings containing CTO, COO, CVO: the `diff` by file (four files, the hybrid `integration.py` named as such with its hash); the `widening`, stated plainly: (1) **the first grant on opal-data-49financial** (the text must contain those words): the data role gains `GetObject` on four silver files by name in the EXISTING bucket (`schwab/49financial/silver/<t>/date=*/08403355.parquet`), the catalog role gains `GetObject` on ONE state object name in the NEW bucket (`schwab/49financial/state/complete/date=*/08403355.complete.json`) and a prefix-conditioned `ListBucket` there; no write, no bucket-wide or folder-wide read, no other master's file; the listing note: a prefix-conditioned list reveals KEY NAMES under that prefix, so when another master lands in the firm folder its key names become listable (its contents stay unreadable); the bucket's own policy is a separate Deny that the laptop's R3a exemption lifts for this one role and prefix; (2) **the dual read** (the text must contain `falls back on ABSENT only`): new location first, old second, the fallback only on NoSuchKey or an empty listing, AccessDenied is a hard error, a file of another master in the firm folder is ignored by name, an old-form master never calls the state bucket; before the cutover nothing changes for any principal (the new location is empty), after it the same reads continue; the sentence naming R3a (`R3a`) as verified live before the apply; the `order` (the four steps above); `both branches` (gate read passes: deploy; gate read answers AccessDenied: do not deploy, the policies are inert); the `rollback` (redeploy the live ref's tree, and re-apply the previous bodies of the two policies by reverting `schwab_reader_iam.tf` to the base and `safe-apply` with the same two targets); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering; `.env` key count not 65; `tools/list` changing from 103; md5 beyond the four files; host memory above 85 percent; `NRestarts` above 0; the marker not equal to the release; the gate read answering AccessDenied or any key; the dual-read read-back showing fewer dates or an older newest date; any `audit-lake WARN`); the line `process-wide state this change touches: ...`. Commit, run AC1 (`.../r47/checks/rl19.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`, the window and the laptop's R3a confirmation)

5. The four steps above, in that order, recording each in `order`. The code deploy is `OG-rl-17` step 5 with ledger `nfra-oplgtw-gateway-release-r3c`, deploy from `C:/tmp/og-rel-r3c`, `DEPLOY_BASE_REF=<the live ref read on the host>`.
6. **The served read, UNARMED ONLY**, writing `W/R3C_SERVED.json` (the field names in `rl19.AC2.sh`'s header): health 200, the marker equal to the release, `tools_list` 103 before and after, `env_key_count` 65, `registry_count` 103, `host_md5` `differ` 0, the host clock and failed units read BEFORE the ledger closes, a 15-minute read-back, `order`, `terraform` (`via` `safe-apply`, add 0 change 2 destroy 0, the two resources), `gate_read` and `dual_read`: from the DEPLOYED tree under the hard guard, the catalog's `list_dates("08403355")` and the newest date's snapshot status BEFORE the code deploy (read from the live ref's code) and AFTER (read from the deployed code): the number of dates and the newest date not lower, `marker_location` `old`, the snapshot status equal, `other_masters_unchanged` true (the same read for `08242234` and `08335338`), `planted_second_master_ignored` true (a planted `08242234.complete.json` in a fake listing under the firm prefix is ignored by the deployed code in the fake-client probe of `sk2.AC1`'s last line).
7. Standing clauses as `OG-rl-17` step 8; close the ledger; commit; run `rl19.AC2`; report once per phase; send me the ledger CLOSED time and the live sha.
8. **PHASE C, the landing** as `OG-rl-17` step 9: `W/rl19_landing.json`, including `org/standards/NFRA_OPLGTW_CONTRACT.json`; the issuer drains it.

## 2. BOUNDS

- The release's four files only, and the two IAM policies named above. No other Terraform change, no env key, no deploy-script or unit edit, NO SSM write, NO write of any stored grant, NO write to any S3 bucket. No account number, person's name, credential or object content in any record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; arm the probe listener; run gateway code on the host without the hard guard; deploy the code after a gate read that answered AccessDenied; apply before the laptop's R3a confirmation file is read.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r3c.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; read the channel's highest id at HEAD first), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rl19.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref read on the host: yes; dell1 harvest release 6575999df5 is an ancestor of base: yes.*files differing 4 \(want 4\); outside the four 0 expected: 0; the four missing 0 \(want 0\); the three trunk-whole files not byte-equal to trunk's 0 \(want 0\); barred files \(deploy script, unit, manifest, \.tf\) 0 \(want 0\).*integration\.py is the BASE blob plus the OG-sk-2 hunk only \(not trunk's blob\): yes.*record release_sha equals the release; tests: .*suite difference named True: ok.*sk2\.AC1 lines ok 13 of 13: ok; old-form reads unchanged True; terraform plan add 0 change 2 destroy 0 on the two role policies: ok.*ask has the three halves, the process-wide state line, the first grant on opal-data-49financial, the ABSENT-only fallback and R3a yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rl19.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*tools/list 103 before 103 \(want 103 and 103\); marker equals the release sha yes; health 200.*ORDER OF ACTS: R3a confirmation read before the apply, Terraform applied before the gate read, gate read before the code deploy: ok; Terraform via safe-apply, add 0 change 2 destroy 0 on the two policies: ok.*GATE READ as the catalog role on opal-data-49financial/schwab/49financial/state/complete/: GetObject NoSuchKey, list keys 0.*: ok.*DUAL READ live for 08403355: dates \d+ -> \d+ \(not fewer\).*: ok.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-19.round-47-release-r3c-the-schwab-0840-dual-read-and-its-reader-iam.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-O, amendment A18 of R3-T.124. Sources: Andrew-direct (relayed by the laptop MSTR); the CTO's rulings (20:18Z, 22:02Z, 22:08Z); the laptop CTO's binding order 110051 (R3a verified live before 06:00Z, then R3c at 07:00Z or later, then R4a). `OG-sk-1` census, `OG-sk-2` code and `OG-sk-3` IAM text are drained and complete.
- READINGS DISCLOSED: (1) `integration.py` is a HYBRID (base plus one hunk) because trunk's blob carries batch17's `OG-rt-1` hunks and a whole-from-trunk take would drag the master-wide parser's caller in without its callee (`data_entitlement.py`). (2) The Terraform apply is TARGETED to two resources because the root may carry other drift. (3) The new location is empty until the laptop's R4a writes the first state key; the code is therefore inert for every principal until then.
- `OG-rl-18` (batch17) is cut on the live ref AFTER this release; its take list still takes `integration.py` whole from trunk (which then adds `OG-rt-1`'s hunks onto this release's file). Its order is amended for the base change before its Phase A GO.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (records absent). Arms: `rl19.AC1` passed on a synthetic release commit (base + three trunk blobs + the hybrid blob, built from git objects, no refs) and FAILED on the negative control (trunk's whole `integration.py` read `no`); `rl19.AC2`'s served-record verdict read OK on a synthetic record and NO when the gate read said `AccessDenied` (the ledger arm is `rl17.AC2`'s, unchanged).

<status>staged</status>
<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-O</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
