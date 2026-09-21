# AMGT_RESAPP task order -- `AMGT-rk-91` -- MOVE M2: `filings/v1/*.source.json` moves to the harvest grammar -- the 14 RESOLVED source objects COPIED losslessly into `filing_source` SILVER (sec 13, issuer-site 1), the 180 `UNRESOLVED-SOURCE` markers VERBATIM to `amgt/harvest/state/filing_attempt/`, every reader and writer switched in the SAME window, the adapter's read grant swapped (new state grant first, re-read, then `filings/v1/*` removed) and the adapter redeployed; the 12 `.analysis.json` are gold and untouched; no S3 delete

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-91</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~91</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and touches no schedule.
  It OPENS one deploy-ledger entry before its first live write and CLOSES it on the post-act read-back.
comp-iam: RUN -- measured by a live iam get-role-policy at the cut: 1 role (opal-amgt-scoped-api-role), 1 inline
  policy (opal-amgt-scoped-api-grants), 4 statements, sha256 0c6b3cf46bdff811; object-read resources include
  filings/v1/* (1 of them) and the list limb names filings/v1/; 0 resources or list prefixes name amgt/harvest/state/.
  This order ADDS amgt/harvest/state/filing_attempt/ on BOTH limbs and REMOVES filings/v1/ on BOTH limbs, in that
  order, with a live re-read between (CTO msg 24112). BLIND: the chatter role is not read here; the chatter Lambda's
  18 build inputs carry no filings/v1 reader (measured), so it is not changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~91`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~91;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined -- `AMGT-rk-91` (move M2, harvest chain wave 3; runs AFTER M1)

**The ruling of record:** CTO round-21 analysis msg 24119 (`ledger/ROUND_ANALYSIS.round21.md` @739eb5f288), items 4-7,
verbatim: *"4-7. M1-M4 moves. COPY with vintage, then readers switched and the old path retired in ONE window (v0.17
"retire": no S3 delete). One never-widen pair per move. Each move re-reads that its new grant is present before
removing the old one. They run as a SEQUENTIAL chain, each waiting on the prior move's read-back."* CTO msg 24112:
*"a move that REMOVES an old grant re-reads that its matching new grant is present first, so no reader is ever left
with neither."* PRD v0.17 @1f7459456a C-FORMAT-SEQUENCE: "retire" = readers switched + writers stopped + read grant
removed in ONE window, no S3 delete; the filings/v1 derived records go to SILVER; filings BRONZE comes only from the
backfill's first fetch. CTO msg 24106 item 3: the UNRESOLVED markers are STATE at the builder's
`amgt/harvest/state/filing_attempt/` address; item 4: the silver table is `filing_source`, one row per `.source.json`,
a lossless copy graded by round-trip. `.analysis.json` is GOLD, rebuilt after the backfill (C-FORMAT-SEQUENCE) -- NOT
moved here.

**THE MEASURED STATE (read-only, 2026-09-21T23:32Z). RE-READ at your HEAD before acting:**
- `filings/v1/` in `opal-data-harvest`: **206 objects**, 193 entity keys: **194 `.source.json`** (**180
  `UNRESOLVED-SOURCE.source.json` placeholders + 14 RESOLVED**, which `lib.research.harvest.filings.vendor_source`
  routes as `sec` 13, `issuer-site` 1) and **12 `.analysis.json`** (gold; untouched).
- **1 of the 14 resolved entities ALSO carries a placeholder.** The reader's existing rule (`roster.pick_source_key`,
  rk-65) ranks a resolved source above a placeholder; after the move a reader consults SILVER first and STATE second,
  so that ranking is preserved.
- **Slash-bearing entities:** `BP/_LN_Equity`, `NG/_LN_Equity` -- the entity is the text between `filings/v1/` and
  the LAST segment, never a split on `/`.
- New homes EMPTY: `sec/` 0, `issuer-site/` 0, `filings-xbrl/` 0, `amgt/harvest/state/` 0 (plus M1's pull logs once M1
  lands). Live builder addresses (0 refusals):
  `s3://opal-data-harvest/sec/harvest/silver/filing_source/date=2026-09-19/part-x.parquet`,
  `s3://opal-data-harvest/issuer-site/harvest/silver/filing_source/date=...`,
  `s3://opal-data-harvest/amgt/harvest/state/filing_attempt/security_key=CSL_AU_Equity/UNRESOLVED-SOURCE.json`.
- **Readers (census over `lib`, `integrations`, `infra`: `filings/v1` literal 49 occurrences / 18 files; minus tests
  and `.json`; plus the prefix constants):**
  - SERVED: `lib/research/api/scoped_amgt.py` `_read_filing_source_object` (`:1945 FILINGS_PREFIX`, `:1959`) -- it
    reads ONLY `<key>/UNRESOLVED-SOURCE.source.json`, so after the move it reads the STATE object (JSON, no parquet).
  - BOX-SIDE: `lib/research/management/roster.py:99` (+`:492`), `lib/research/management/enrich.py`,
    `lib/research/management/batch.py`, `integrations/bloomberg/research/management_posture_batch.py:49`,
    `lib/research/filings/fetch.py:61,462`, `lib/research/filings/batch.py:43,138,239`, `lib/research/filings/analyze.py`
    (its SOURCE read only; its `.analysis.json` write stays), `lib/research/filings/drafting_build.py`. Box-side
    readers read resolved rows from silver through `lib.research.harvest.filings.source_object_from_row` (the box has
    pyarrow).
- **Writers of `.source.json`:** `fetch.py:426` (`persist`), `batch.py:341,553`, `battery.py:1314` -> switched to
  `lib.research.harvest.filings` (resolved -> `write_filing_source_silver`; unresolved -> a new
  `state_put_filing_attempt`). The `.analysis.json` writers (`analyze.py:1388,1496,1546`) are NOT changed.
- **The adapter:** after M1, its CodeSha256 is M1's post-act value (re-read -- it is this order's rollback target); its
  57 derived build inputs must carry, since M1's served source, EXACTLY this order's commits.

**RULED, what you build and do:**
1. **Copy (silver).** `python -m lib.research.harvest.filings --move-m2 --report <path>` (a CLI you add): for each of
   the 14 resolved objects, `filing_source_row` -> `write_filing_source_silver`, then read the row back and
   `source_object_from_row` must EQUAL the original object (the per-object round-trip, v0.17). Record old key, old
   VersionId, silver part key, equality.
2. **Copy (state).** For each of the 180 placeholders, `state_put_filing_attempt(security_key, body, client)` (new, in
   `filings.py`): the OLD BYTES verbatim, conditional put, same-bytes-is-present, builder address only.
3. **Switch every writer and reader** listed above in the SAME commit. After it, **no production file reads or writes
   a `.source.json` key under `filings/v1/`** (AC5); `.analysis.json` reads and writes remain (gold, chain G).
   Cross-module test patches import qualified `lib.<pkg>.<mod>` names and carry one `is` identity arm (W85-S1).
4. **IAM, in this order:** (a) ADD `amgt/harvest/state/filing_attempt/` to BOTH limbs of `opal-amgt-scoped-api-grants`
   (`infra/aws/terraform/harvest/scoped-amgt-api.tf`), targeted apply, **live re-read shows it present**; (b) redeploy
   the adapter (its reader now reads state); (c) only then REMOVE `filings/v1/` from BOTH limbs, targeted apply,
   live re-read shows it absent and the state grant still present.
5. **No S3 delete.** The 194 old `.source.json` objects stay for Andrew's one batched delete word.

**Tests pinning the old phrase (CTO msg 24100):** `filings/v1` is pinned in `lib/research/management/tests/test_management.py`
(18), `lib/research/api/tests/test_fallback_roster_served.py` (4), `integrations/bloomberg/research/tests/test_management_posture_batch.py`
(4), `lib/research/filings/tests/test_filings.py` (1), `lib/research/management/tests/test_jp_president_and_readable_reasons.py`
(1), and `lib/research/harvest/tests/test_filings.py` (2, which assert the WRITER module does not name it -- keep
true). All are in `<paths>`; fixtures move to the new grammar, never deleted.

## 2. WHERE THIS CAME FROM

ROUND 22, decomposition s.30, on the CTO's round-21 analysis @739eb5f288 (msg 24119); the chain proposal's M2 row;
rk-84 (H2, merged @fb8ff7fd28) built the writer this move calls. **Sequential:** M1 (`AMGT-rk-90`) must be complete
and read back first -- both redeploy the adapter.

## 3. SURFACES

<paths>
lib/research/filings/fetch.py
lib/research/filings/batch.py
lib/research/filings/battery.py
lib/research/filings/analyze.py
lib/research/filings/drafting_build.py
lib/research/filings/tests/test_filings.py
lib/research/management/roster.py
lib/research/management/enrich.py
lib/research/management/batch.py
lib/research/management/tests/test_management.py
lib/research/management/tests/test_jp_president_and_readable_reasons.py
integrations/bloomberg/research/management_posture_batch.py
integrations/bloomberg/research/tests/test_management_posture_batch.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_fallback_roster_served.py
lib/research/harvest/filings.py
lib/research/harvest/tests/test_filings.py
lib/research/harvest/tests/test_m2_move.py
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~91/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-91.filings-source-to-silver-and-state.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- A surface not named here is a WALL; `lib/research/harvest/store.py` is a WALL. Scratch `<worktree>/.scratch/r91/`.
- COMMITTING: `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~91 <0.9.0_WK_AMGT_RESAPP~91@opal.agent>" -F <msgfile> -- <paths>`.
  Code commits land BEFORE any live act. Never push, merge, rebase, stash, `checkout --`. Read the harvest module's
  owned-paths lane BEFORE any apply (safe-apply does not check lanes).

## 4. BOUNDS

- **Live writes, exactly:** 14 silver rows (in `filing_source` parts under `sec/` and `issuer-site/`), 180 conditional
  puts under `amgt/harvest/state/filing_attempt/`, 2 targeted IAM applies on ONE inline policy, 1 artifact upload,
  1 targeted Lambda apply. **No S3 delete. No EDGAR, issuer-site or ESEF fetch** -- every byte comes from the stored
  object. `.analysis.json` untouched.
- **AC0 STOPs** unless `AMGT-rk-90`'s order reads complete at your HEAD and the never-widen pair
  `ledger/NEVER_WIDEN_ROUND22_RK91_{COO,CTO}_HALF.md` carries both halves signed.
- Any reader of `filings/v1/*.source.json` found at spawn not in section 1's list: STOP with a BLOCKING row.
- Any criterion carrying a backslash escape is written by you as a FILE under `.scratch/r91/` (row W84-S1).
- **Refusal clause:** as rk-90.

## 5. PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import re, os, subprocess; t = open("org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-90.bloomberg-raw-to-bronze.md", encoding="utf-8").read(); print("m1_complete", bool(re.search("^<" + "status>complete</" + "status>$", t, re.M))); d = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/"; print("pair", [os.path.exists(d + "NEVER_WIDEN_ROUND22_RK91_%s_HALF.md" % h) for h in ("COO", "CTO")]); out = subprocess.run(["git", "grep", "-l", "-e", "filings/v1", "-e", "FILINGS_PREFIX", "-e", "POOL_PREFIX", "--", "lib", "integrations", "infra"], capture_output=True, text=True).stdout.split(); prod = sorted(p for p in out if "/tests/" not in p and not p.endswith(".json")); print("old_prefix_files", len(prod)); print(*prod, sep=chr(10))'</invocation><expect>m1_complete True; pair [True, True] (read both, signed); then every production file listed is in section 1's reader/writer list (or names only .analysis.json) -- any other file is a STOP with a BLOCKING row before any edit</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests lib/research/filings/tests lib/research/management/tests lib/research/api/tests integrations/bloomberg/research/tests/test_management_posture_batch.py -q -p no:cacheprovider 2>&1 | tail -3</invocation><expect>"N passed" with failures EQUAL to the spawn-time baseline (re-measure before editing; the bar is no NEW failure, no fewer passes), and test_m2_move.py's arms among the passes: resolved object -> silver row -> object round-trips EQUAL; placeholder -> state verbatim; a second copy is a no-op; a resolved-plus-placeholder name resolves to the silver source (ranking kept); the adapter reads the state object; one `is` identity arm per cross-module patch</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import boto3, json, hashlib, urllib.parse; s3 = boto3.client("s3", region_name="us-east-1"); l = boto3.client("lambda", region_name="us-east-1"); iam = boto3.client("iam"); B = "opal-data-harvest"; ls = lambda p: [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", [])]; f = ls("filings/v1/"); print("filings_v1", len(f), "source", sum(k.endswith(".source.json") for k in f), "placeholders", sum(k.endswith("/UNRESOLVED-SOURCE.source.json") for k in f), "analysis", sum(k.endswith(".analysis.json") for k in f)); print("sec", len(ls("sec/")), "issuer_site", len(ls("issuer-site/")), "state_fa", len(ls("amgt/harvest/state/filing_attempt/"))); c = l.get_function_configuration(FunctionName="opal-amgt-scoped-api"); print("CodeSha256", c["CodeSha256"]); print("ArtifactVersionId", s3.head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip").get("VersionId")); d = iam.get_role_policy(RoleName="opal-amgt-scoped-api-role", PolicyName="opal-amgt-scoped-api-grants")["PolicyDocument"]; d = json.loads(urllib.parse.unquote(d)) if isinstance(d, str) else d; flat = json.dumps(d); print("policy_sha", hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16], "statements", len(d["Statement"]), "has_filings_v1", "filings/v1" in flat, "has_state_fa", "amgt/harvest/state/filing_attempt" in flat)'</invocation><expect>filings_v1 206 source 194 placeholders 180 analysis 12; sec 0 issuer_site 0 state_fa 0; CodeSha256 = M1's post-act value; policy statements 4, has_filings_v1 True, has_state_fa False -- all written to .scratch/r91/pre.json as the ROLLBACK TARGETS; any other value: STOP, read-only</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py open --slug amgt-rk91-filings-source-to-silver-and-state --legs 3 2>&1 | tail -2</invocation><expect>"OK: OPENED deploy ledger" before any live write; L1 = the copies, L2 = the state grant + adapter redeploy, L3 = the filings/v1 grant removal</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.harvest.filings --move-m2 --report .scratch/r91/copy.json 2>&1 | tail -6</invocation><expect>silver_rows 14 (sec 13, issuer-site 1), round_trip_equal 14 of 14, state_puts 180, sha_equal 180 of 180, refused 0; a second run writes 0; no key outside sec/harvest/silver/filing_source/, issuer-site/harvest/silver/filing_source/ or amgt/harvest/state/filing_attempt/ written (count of written keys by prefix printed)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess; out = subprocess.run(["git", "grep", "-n", "-e", "source.json", "--", "lib", "integrations"], capture_output=True, text=True).stdout.splitlines(); prod = [l for l in out if "/tests/" not in l and "filings/v1" in l]; print("production_lines_filings_v1_source", len(prod)); print(*prod, sep=chr(10))'</invocation><expect>0 production lines build or read a filings/v1 .source.json key (prefix constants now name only the .analysis.json gold path, or are removed)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import boto3, json, urllib.parse; iam = boto3.client("iam"); d = iam.get_role_policy(RoleName="opal-amgt-scoped-api-role", PolicyName="opal-amgt-scoped-api-grants")["PolicyDocument"]; d = json.loads(urllib.parse.unquote(d)) if isinstance(d, str) else d; flat = json.dumps(d); print("statements", len(d["Statement"]), "has_state_fa", "amgt/harvest/state/filing_attempt" in flat, "has_filings_v1", "filings/v1" in flat)'</invocation><expect>run THREE times, each after its step: after 4(a) "statements 4 has_state_fa True has_filings_v1 True"; after 4(b) the adapter CodeSha256 moved and a direct invoke of the thesis leaf for CSL_AU_Equity, 6861_JP_Equity and CAT_US_Equity returns 200 with the SAME management_status, roster_status and roster_reason as pre; after 4(c) "statements 4 has_state_fa True has_filings_v1 False" and the three invokes still 200 and equal -- the removal is refused (not run) unless the second read shows has_state_fa True</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py check 2>&1 | tail -3</invocation><expect>all three legs closed with AC4/AC6 output as proof, the entry CLOSED and its sentinel removed</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-91"><invocation>cd "$(git rev-parse --show-toplevel)" && HALT_ACK=1 bash .tools/safe-apply.sh infra/aws/terraform/harvest plan -target=module.scoped_amgt_api.aws_lambda_function.this -target=aws_iam_role_policy.scoped_amgt_api_grants 2>&1 | grep -E "^Plan:|No changes"</invocation><expect>"No changes. Your infrastructure matches the configuration." after all three steps (the inline policy is `aws_iam_role_policy.scoped_amgt_api_grants`, scoped-amgt-api.tf:178, measured at the cut; re-read it at spawn)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~91/AMGT_RESAPP.TO-AMGT-rk-91.filings-source-to-silver-and-state.proof_of_spec.json`,
grade with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8`
(rc 0), flip the status tag to complete, commit. **ROLLBACK:** restore `filings/v1/` to both limbs FIRST (re-read
present), then re-point the adapter to the pre artifact VersionId (targeted apply; CodeSha256 equals pre), then revert
the code switch by a NEW commit; the copied silver/state objects stay (nothing reads them after the revert) and are
named in a BLOCKING row. Never delete.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes:** spawn only after `AMGT-rk-90` drains and reads back, with this order's pair complete.

<status>pending</status>
<round>22</round>
<slot>~91</slot>
<fabric>site-z</fabric>
