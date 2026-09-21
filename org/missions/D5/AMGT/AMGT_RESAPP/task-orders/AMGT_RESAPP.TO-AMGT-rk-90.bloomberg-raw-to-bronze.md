# AMGT_RESAPP task order -- `AMGT-rk-90` -- MOVE M1: the Bloomberg raw landing `raw/bloomberg/` moves to the harvest grammar -- 110 request objects COPIED as received to `bloomberg/harvest/bronze/`, 9 pull logs to `amgt/harvest/state/pull_log/`, every reader and writer of the old prefix switched in the SAME window, the adapter redeployed for its freshness reader; no S3 delete; `derived/model_block/` is NOT in this move (held, issuer question Q1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-90</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~90</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and touches no schedule;
  the only scheduled writer of raw/bloomberg/ (the Terminal pull consumer) is repointed in code, not re-scheduled. It
  OPENS one deploy-ledger entry before its first live write and CLOSES it on the post-act read-back.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant changes in THIS move: the adapter's read on
  bloomberg/harvest/bronze/ (both limbs) was added by AMGT-rk-82 (measured present at the cut, below), and its "raw/"
  grant is SHARED with raw/seekingalpha/ (M3), so it is NOT removed here -- it retires in M3's window. AC6 asserts the
  scoped role's inline policy hash is IDENTICAL before and after (coverage: 1 role, 1 inline policy, 4 statements).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~90`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~90;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined -- `AMGT-rk-90` (move M1, harvest chain wave 3)

**The ruling of record (CTO round-21 analysis, msg 24119, `ledger/ROUND_ANALYSIS.round21.md` @739eb5f288 -- items
4-7, verbatim):** *"4-7. M1-M4 moves. COPY with vintage, then readers switched and the old path retired in ONE window
(v0.17 "retire": no S3 delete). One never-widen pair per move. Each move re-reads that its new grant is present before
removing the old one. They run as a SEQUENTIAL chain, each waiting on the prior move's read-back."* And CTO msg 24112:
*"CONDITION on M1-M4: a move that REMOVES an old grant re-reads that its matching new grant is present first, so no
reader is ever left with neither."* PRD v0.17 @1f7459456a C-FORMAT-SEQUENCE: "retire" = readers switched, writers
stopped and read grant removed in ONE window; **no move performs an S3 delete**; deletion is ONE batched human word.

**Why `derived/model_block/` is NOT in this move (issuer's Q1, measured).** The served adapter reads
`derived/model_block/<key>/<stamp>/model_block.json` as JSON (`lib/research/api/scoped_amgt.py:181, :1016,
:3478-3541`). Its silver home is PARQUET (`bloomberg/harvest/silver/model_block/`), and the adapter carries NO parquet
reader: its build vendors exactly ONE non-pure wheel, rpds_py (`infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh:59-71`),
plus the `opal-amgt-print-deps` layer. Switching that reader in this window would need a pyarrow-capable artifact or a
served gold projection -- a spec call held for `1.0.0_SA_CTO~Z`. This move therefore leaves `derived/model_block/`,
its readers and its writer (`model_block_pull.py:1063`) EXACTLY as they are. A worker that finds itself editing a
model_block reader or writer STOPs.

**THE MEASURED STATE (read-only, SITEZ HEAD `8573b625b4`+, 2026-09-21T23:32Z). RE-READ at your HEAD before acting:**
- `raw/bloomberg/` in `opal-data-harvest`: **119 objects, 541,382 bytes, 37 entity keys**. By file: refdata 48,
  histdata 48, bestdata 6, exec_officers 4, identity 3, histdata_daily_px 1 (**110 bronze-eligible**, the six
  `lib.research.harvest.bloomberg.BRONZE_REQUESTS`), and **pull_log 9** (refused as bronze by rk-83 -> STATE).
- **4 objects sit under slash-bearing entity keys** `BP/_LN_Equity` and `NG/_LN_Equity`
  (`raw/bloomberg/BP/_LN_Equity/20260916T201833Z/histdata.json` ...). **The entity is NEVER cut from the key by
  splitting on `/`**: it is the text between `raw/bloomberg/` and the LAST TWO segments (`<stamp>/<file>`).
- New-grammar homes are EMPTY: `bloomberg/` 0 objects, `amgt/harvest/state/` 0 objects.
- Live builder addresses (`lib/opal_naming.py`, 0 refusals):
  `s3://opal-data-harvest/bloomberg/harvest/bronze/refdata/security_key=BP-SLASH-_LN_Equity/20260916T201833Z.json`;
  `s3://opal-data-harvest/amgt/harvest/state/pull_log/security_key=BP-SLASH-_LN_Equity/20260916T201833Z.json`.
- **Readers and writers of `raw/bloomberg/` (census by pattern over `lib`, `integrations`, `infra`; `raw/bloomberg`
  literal 34 occurrences / 13 files; minus 6 test files = 7 production files; plus the vendor-generic `raw/%s/` and
  `raw/{vendor}/` builders, which reach Bloomberg when `vendor == "bloomberg"`):**
  - READERS: `integrations/bloomberg/research/model_block_pull.py` (:455-458, :611, :714, :937-939 and `_latest_stamp`),
    `integrations/bloomberg/research/build_unit_map.py:255`, `integrations/bloomberg/research/derive_fye_fixed.py:89`,
    `lib/research/management/bloomberg_fallback.py:54`, `lib/research/coverage/run_reader.py:86`,
    `lib/research/coverage/run_sa_reexercise.py:68,89`, `lib/research/freshness/build_view.py:188`, and the SERVED
    `lib/research/api/scoped_amgt.py` `read_coverage_freshness` (`:3085 RAW_PREFIX`, `:3231-3234`).
  - WRITERS: `model_block_pull.py:336` (raw put) and `:393` (pull_log), `pull_baba_daily_px.py:82`,
    `lib/research/identity/add_security.py:130`, `bloomberg_fallback.py:100`.
  - `lib/research/identity/crosswalk.py:139-148` NAMES the prefix in message text only -- not a read; untouched.
- **The adapter** `opal-amgt-scoped-api`: CodeSha256 `hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=`, artifact
  VersionId `.BKJHDt8u.NTMdFQHOGf6pgAVdXpE52f`; its build-input list, DERIVED from its build script, is **57 members**;
  **0 commits** on those 57 since its served source `3a7afd3316` (rk-77). `scoped_amgt.py` and `freshness/build_view.py`
  are IN it; `crosswalk.py` is in it but not edited. The chatter Lambda (18 members) contains no reader of this prefix.
- The adapter's inline policy `opal-amgt-scoped-api-grants`: 4 statements, sha256 (sorted, compact JSON) `0c6b3cf46bdff811...`,
  carrying `raw/*` and `bloomberg/harvest/bronze/*` (both limbs).

**RULED, what you build and do:**
1. **Copy (bronze), run as `python -m lib.research.harvest.bloomberg --move-m1 --report <path>`** (a CLI you add to
   `bloomberg.py`, reading only `raw/bloomberg/` and writing only the two new prefixes). For each of the 110 bronze-eligible objects, `lib.research.harvest.bloomberg.bronze_write(request,
   security_key, fetched_at, body, client)` with `body` = the OLD OBJECT'S BYTES UNCHANGED (never re-serialised),
   `fetched_at` = the old key's `<stamp>` parsed as UTC, `request` = the file stem. Record per object: old key, old
   VersionId, new key, sha256 of both (must be EQUAL). A second run is a no-op (`existed` True).
2. **Copy (state).** The 9 `pull_log.json` objects go VERBATIM to the builder's `amgt/harvest/state/pull_log/` address
   (partition `security_key=<slash-safe key>`, object `<stamp>.json`) by ONE new function you add,
   `lib.research.harvest.bloomberg.state_put_pull_log(security_key, stamp, body, client)`: a conditional put
   (`IfNoneMatch="*"`), same-bytes-is-present, different-bytes raises. Address from the builder only.
3. **Switch every writer.** `model_block_pull.py:336` raw puts -> `bronze_write`; `:393` pull_log -> `state_put_pull_log`;
   `pull_baba_daily_px.py:82`, `add_security.py:130`, `bloomberg_fallback.py:100` -> `bronze_write`. After the switch,
   **no production file writes a `raw/bloomberg/` key** (AC5).
4. **Switch every reader** listed above to the new grammar in the SAME commit: raw landings are read as
   `bloomberg/harvest/bronze/<request>/security_key=<safe>/<stamp>.json` (stamp from the object name; the
   `(refdata, histdata)` raw-pair rule of rk-70 kept); pull logs from state. `build_view.py` and the adapter's
   `read_coverage_freshness` list the new bronze prefix for the Bloomberg vendor and KEEP `raw/<vendor>/` for any other
   vendor (seekingalpha moves at M3). Cross-module test patches import the QUALIFIED `lib.<pkg>.<mod>` /
   `integrations.<...>` name and each test file carries ONE `is` arm proving the patched object is the one the
   production caller reaches (CTO ruling on W85-S1, msg 24119).
5. **Redeploy the adapter** through `build-and-upload-scoped-amgt.sh` and a TARGETED
   `HALT_ACK=1 .tools/safe-apply.sh ... -target=module.scoped_amgt_api.aws_lambda_function.this` (plan 0/1/0). The
   carry-along on the 57 build inputs since `3a7afd3316` must be EXACTLY this order's own commit(s).
6. **No grant removed, no S3 delete, no `derived/model_block/` change.** The old `raw/bloomberg/` objects stay for
   Andrew's one batched delete word.

**Tests pinning the old phrase (standing rule, CTO msg 24100):** `raw/bloomberg` is pinned by test fixtures in
`lib/research/api/tests/test_surfaced_outcome_routes.py` (6), `test_fallback_roster_served.py` (3),
`lib/research/identity/tests/test_add_security.py` (2), `integrations/bloomberg/research/tests/test_fye_join.py` (3),
`test_latest_stamp_raw_pair.py` (1), and `lib/research/harvest/tests/test_bloomberg.py` (1, which asserts the writer
module does NOT name it -- keep it true). These are in `<paths>`; each fixture is moved to the new grammar, never
deleted, and the suite counts in AC1 are re-measured at spawn.

## 2. WHERE THIS CAME FROM

ROUND 22, decomposition s.30 (cut by `2.0.0_SA_COO~Z`) on the CTO's round-21 analysis @739eb5f288 (msg 24119); the
harvest chain proposal's M1 row; rk-83 (H1, merged @91ce5cd1f6) built the bronze writer this move calls; rk-82
(merged @bf0f9a30ce) granted the adapter's read on the new prefix. M2 (`AMGT-rk-91`) waits on this order's read-back.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/derive_fye_fixed.py
integrations/bloomberg/research/pull_baba_daily_px.py
integrations/bloomberg/research/tests/test_fye_join.py
integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py
lib/research/management/bloomberg_fallback.py
lib/research/identity/add_security.py
lib/research/identity/tests/test_add_security.py
lib/research/coverage/run_reader.py
lib/research/coverage/run_sa_reexercise.py
lib/research/freshness/build_view.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_surfaced_outcome_routes.py
lib/research/api/tests/test_fallback_roster_served.py
lib/research/harvest/bloomberg.py
lib/research/harvest/tests/test_bloomberg.py
lib/research/harvest/tests/test_m1_move.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~90/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-90.bloomberg-raw-to-bronze.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- A surface not named here is a WALL. **`lib/research/harvest/store.py` is a WALL** (call its public names only).
  `derived/model_block` readers/writers are WALLS in this move. Scratch is `<worktree>/.scratch/r90/` (never committed).
- COMMITTING: `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~90 <0.9.0_WK_AMGT_RESAPP~90@opal.agent>" -F <msgfile> -- <paths>`,
  the message file written by the Write tool. Code commits land BEFORE any live act. Never push, merge, rebase, stash,
  `checkout --`.

## 4. BOUNDS

- **Live writes, exactly:** 110 conditional puts under `bloomberg/harvest/bronze/`, 9 under
  `amgt/harvest/state/pull_log/`, 1 artifact upload, 1 targeted apply. **No S3 delete. No IAM change.** No Bloomberg
  Terminal call -- every copied byte comes from the stored object.
- **The never-widen pair** `ledger/NEVER_WIDEN_ROUND22_RK90_{COO,CTO}_HALF.md` must carry BOTH halves signed before
  AC3. Absent or unsigned: STOP after AC2, write nothing.
- Any reader of `raw/bloomberg/` found at spawn that is NOT in section 1's list: STOP with a BLOCKING row (the census
  is re-run by AC0). Any criterion that would carry a backslash escape is written by you as a FILE under
  `.scratch/r90/` from this text and run with `python <file>` (row W84-S1's rule).
- **Refusal clause:** a criterion not satisfiable as written is REFUSED with its measurement and a row; never repaired
  by an unnamed route, never by editing a WALL.

## 5. PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import re, subprocess; t = open("org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-85.sa-publications-writer.md", encoding="utf-8").read(); print("round21_last_order_complete", bool(re.search("^<" + "status>complete</" + "status>$", t, re.M))); out = subprocess.run(["git", "grep", "-l", "-e", "raw/bloomberg", "-e", "raw/%s", "-e", "raw/{", "--", "lib", "integrations", "infra"], capture_output=True, text=True).stdout.split(); prod = sorted(p for p in out if "/tests/" not in p and not p.endswith(".json")); print("old_prefix_files", len(prod)); print(*prod, sep=chr(10))'</invocation><expect>round21_last_order_complete True (round 21 drained), then the production files naming the old prefix: every one of them is in section 1's reader/writer list or is crosswalk.py (message text) -- any file NOT in that list is a STOP with a BLOCKING row before any edit</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests lib/research/api/tests lib/research/identity/tests lib/research/management/tests integrations/bloomberg/research/tests -q -p no:cacheprovider 2>&1 | tail -3</invocation><expect>"N passed" with the failures EQUAL to the spawn-time baseline (re-measure before editing; integrations/bloomberg/research/tests carried pre-existing failures and 2 collection errors at the H1 cut -- the bar is "no NEW failure, no fewer passes"), and test_m1_move.py's arms among the passes: copy-as-received (bytes equal), slash-key entity parse, pull_log to state, a second copy is a no-op, the freshness reader lists the new prefix for bloomberg and raw/ for seekingalpha, and one `is` identity arm per cross-module patch</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import boto3, json, hashlib, urllib.parse; s3 = boto3.client("s3", region_name="us-east-1"); l = boto3.client("lambda", region_name="us-east-1"); iam = boto3.client("iam"); B = "opal-data-harvest"; ls = lambda p: [o for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", [])]; print("raw_bloomberg", len(ls("raw/bloomberg/")), "new_bronze", len(ls("bloomberg/")), "state_pull_log", len(ls("amgt/harvest/state/pull_log/"))); c = l.get_function_configuration(FunctionName="opal-amgt-scoped-api"); print("CodeSha256", c["CodeSha256"]); print("ArtifactVersionId", s3.head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip").get("VersionId")); d = iam.get_role_policy(RoleName="opal-amgt-scoped-api-role", PolicyName="opal-amgt-scoped-api-grants")["PolicyDocument"]; d = json.loads(urllib.parse.unquote(d)) if isinstance(d, str) else d; print("policy_sha", hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16], "statements", len(d["Statement"]))'</invocation><expect>raw_bloomberg 119, new_bronze 0, state_pull_log 0 (measured so at the cut); CodeSha256 hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=, ArtifactVersionId .BKJHDt8u.NTMdFQHOGf6pgAVdXpE52f, policy_sha 0c6b3cf46bdff811, statements 4 -- write these to .scratch/r90/pre.json; they are the ROLLBACK TARGETS. Any differing value: STOP, read-only</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND22_RK90_COO_HALF.md && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND22_RK90_CTO_HALF.md && python .tools/deploy_ledger.py open --slug amgt-rk90-bloomberg-raw-to-bronze --legs 2 2>&1 | tail -2</invocation><expect>both halves present (read both, signed) and "OK: OPENED deploy ledger" before any live write; legs L1 = the copy, L2 = the adapter redeploy</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.harvest.bloomberg --move-m1 --report .scratch/r90/copy.json 2>&1 | tail -6</invocation><expect>copied_bronze 110, copied_state 9, sha_equal 119 of 119, existed 0 on the first run (a second run prints existed 119, put 0); no key outside bloomberg/harvest/bronze/ or amgt/harvest/state/pull_log/ written (the report lists every written key; the worker prints the count of written keys by prefix)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess; out = subprocess.run(["git", "grep", "-n", "-e", "raw/bloomberg", "--", "lib", "integrations", "infra"], capture_output=True, text=True).stdout.splitlines(); prod = [l for l in out if "/tests/" not in l and not l.split(":")[0].endswith(".json")]; print("production_lines_naming_raw_bloomberg", len(prod)); print(*prod, sep=chr(10))'</invocation><expect>only crosswalk.py message-text lines (and none that read or write a key) -- 0 production reads or writes of raw/bloomberg remain; the vendor-generic raw/{vendor} builders are reached for bloomberg nowhere (their bloomberg branch reads the new grammar, proven by AC1's arms)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && HALT_ACK=1 bash .tools/safe-apply.sh infra/aws/terraform/harvest plan -target=module.scoped_amgt_api.aws_lambda_function.this 2>&1 | grep -E "^Plan:|No changes"</invocation><expect>after build-and-upload-scoped-amgt.sh ran (its carry-along check prints only this order's commits on the 57 derived build inputs): "Plan: 0 to add, 1 to change, 0 to destroy."; then the targeted apply; then a live read prints the new CodeSha256 (moved from pre), policy_sha 0c6b3cf46bdff811 UNCHANGED, and a direct invoke of the coverage-freshness GET route (its path read from scoped_amgt.scoped_amgt_route_table(), rawPath prefixed /api/scoped/amgt) returns 200 with the same row count as pre and a bloomberg stamp on every name that had one before</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py check 2>&1 | tail -3</invocation><expect>both legs closed with AC4/AC6 output as proof, the entry CLOSED and its sentinel removed; the slug absent from check's OPEN list</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-90"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess; fs = subprocess.run(["git", "diff", "--name-only", "HEAD~3", "HEAD", "--", "lib", "integrations"], capture_output=True, text=True).stdout.split(); [print(f, "crlf", open(f, "rb").read().count(bytes([13, 10])), "non_ascii", sum(1 for b in open(f, "rb").read() if b > 127)) for f in fs if f.endswith(".py")]'</invocation><expect>every changed .py prints crlf 0 and non_ascii equal to its pinned base figure (0 for every file measured at the cut)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~90/AMGT_RESAPP.TO-AMGT-rk-90.bloomberg-raw-to-bronze.proof_of_spec.json`,
grade with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8`
(rc 0), flip the status tag to complete, commit. **ROLLBACK (any AC4/AC6 trigger):** re-point the adapter to the pre
artifact VersionId (copy_object from it, then the same targeted apply; CodeSha256 must equal pre); the copied objects
are left (new prefixes, nothing reads them after the code revert) and named in a BLOCKING row; the code switch is
reverted by a NEW commit (never a reset).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes:** spawn only after round 21's L10 and with the pair complete. M2 (`AMGT-rk-91`) waits on this order's
complete status and read-back. Q1 (model_block served format) is pitched to `1.0.0_SA_CTO~Z` beside this order.

<status>pending</status>
<round>22</round>
<slot>~90</slot>
<fabric>site-z</fabric>
