# NFRA_OPLGTW task order -- `OG-ap-32` -- APPLY: the round-40 batched gateway release -- the 49F window pages back with a cursor (newest first), and MI's re-emitted catalog (FWD-21, FWD-22; CTO ruling @0a15d90223; PRD v3.14)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-32</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-32</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- this release changes NO IAM and adds no env key. The adapter reads the same four prefixes through the same dedicated role (`gateway-49f-blackdiamond-live-read-role`, live from `OG-ap-29`); you re-read the role with `iam get-role` in Phase A.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 ruling W1 (`ledger/ROUND_ANALYSIS.round38.md` update @0a15d90223: measure, then a full read, else a continuation cursor), the measurement `OG-ev-3` (verdict OUTSIDE: transactions one full-window run of 239.9 s, fees p95 147.2 s, threshold 30 s) and `NFRA_MCPINDEX`'s signed catalog half.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-32` (decomposition addendum R3-T.103, round 40, workstream ENRICH-R40-C)

APPLY: ONE code-only release on the live ref (read it, do not assume it: `services.opal-gateway.deployed_commit` at HEAD; it was `4be300110e` when this order was cut). No Terraform, no IAM, no new env key, no change to `deploy-to-ec2.sh` or `EC2_MANIFEST.json`, one deploy. The builds are merged to trunk (`box/sitez`): `OG-en-17` (merge `4ebc1e781b`: `get_transactions` and `get_fees` page the 13-month window back in slices of at most 60 dated partitions read with 16 concurrent reads, newest slice first; `next_cursor` is the ISO date to pass back as `to_date`, null at the end of the data; `window_partial` is true while a cursor remains; exact-duplicate removal as in `OG-en-15`), and `NFRA_MCPINDEX`'s re-emitted catalog (blob `2cbe275d03c9a5af85afefabc604e26b71e9be12`, md5 `bdfee515ec348f0ea2ee716eff5acba5`, trunk merge `70cf87661a`; `2.0.0_SA_COO~MI`'s half `NEVER_WIDEN_CATALOG_R21_20261016.md` is signed on that blob and void on any other). The GO message names `trunk_sha`.

### PHASE A (only on the issuer's GO message, which names `trunk_sha`): re-cut, ask. NO deploy, NO apply IN ANY FORM

1. **Live ref.** Read `services.opal-gateway.deployed_commit` at HEAD and one SSM md5 read of the host against it over `app/`, `deploy/`, `dashboard/` and `lib/`. A mismatch is a STOP and a BLOCKING row. Record `tools_list_before` (103 at the last release), the `.env` key count (65) and the host memory percent (names and percentages only) for AC2. `MUSE_CLIENT_ID` must be ABSENT. `iam get-role gateway-49f-blackdiamond-live-read-role` resolves.
2. **Re-cut** in `C:/tmp/og-rel-batch4`, branch `rel-nfra-oplgtw-batch4`, at the live ref, with `infra/logic/`, `org/missions/DIRECTIVES.yaml`, `org/mcp/naming-gate.enforce`, `infra/aws/globgrph` AND one `org/<tier>/` CloudOps home folder (for example `org/tier2_senior/0.7.0_AE_CloudOps~Z`) in the sparse cone. **The two cures `OG-ap-31` Phase B needed (row Z-S324, ruled in `Z-S326`) are steps now:** lay the TRUNK copy of `.tools/halt-gate-check.sh` into the release tree UNCOMMITTED (the live ref's copy rejects a rule-34 lane such as `~NFRA1`), and restore it, with the naming-gate overlay, before the deploy tree's clean check. **Enumerate the seams first**: every app module a taken file imports; print each as in-base or in-take-list; a missing seam is a STOP and a row. The take list is the union of the `<paths>` of the complete order `OG-en-17` (app files and tests only: `app/client_adapter_bd49f.py`, `tests/test_og_en17.py`, `tests/test_og_en15.py`, `tests/test_og_cl2.py`) PLUS `app/refs/DATA_CATALOG.yaml` taken WHOLE at `trunk_sha` (`git rev-parse <trunk_sha>:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` must print `2cbe275d03c9a5af85afefabc604e26b71e9be12`, else STOP). Files that differ between the live ref and `trunk_sha` and belong to no order named here are NOT part of this release. `app/client_adapter_bd49f.py` may carry hunks other orders wrote: print the hunk count and attribute EACH hunk to `OG-en-17`, `OG-en-15`, `OG-en-13` (already live) or the live ref's own; an unattributable hunk is a STOP and a row. The naming gate: the live ref already carries the two registry files; if the ENFORCE gate refuses a string because a registry file at the live ref is older than `trunk_sha`'s, add ONE prelude commit under the audited `GIT_COMMIT_AUTHOR_OVERRIDE=PLATFORM_LOGIC_DOCS` carrying exactly those files byte-equal to `trunk_sha`; otherwise none. Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only; the gate must print NO REFUSE. Write `W/ap32_release.json` = `{"base_sha", "release_sha", "trunk_sha"}` (FULL 40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`).
   Run in the release tree: every taken test file; the pinned-count tests; the host-shaped import check; the touched test files together in BOTH orders. A failing taken test that also fails at the live ref is recorded by name and carried (`test_og_ch1.py` is red at the base); a failing taken test that passes at the live ref is a STOP.
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-32.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: (1) the `diff` by file (no manifest or deploy-script change; the catalog taken whole at the blob above); (2) the `widening`, stated plainly: NO new IAM, NO new env key, NO tool added or removed; a 13-month transactions or fees request now returns the newest slice of up to 60 dated files read with 16 concurrent reads plus a `next_cursor`, so ONE call reads up to 60 files at once (the measurement: 0.55 s per read, 16 in flight; peak host memory must be recorded in Phase B) and a caller pages back through the window; rows within a page are served NEWEST FIRST, where the base served oldest first (a change in what an analyst sees); the catalog gains `depth_kind` and `measured_at` on 39 depth claims, moves two definition anchors and three provenance lines, with no row, tool, visibility or value change; the 429 limit, the browser exemption roster and the allocation weight unit are NOT changed; (3) the `order` of acts (one deploy, then the served read); (4) `both branches` (a window within one page: the answer is complete and `next_cursor` is null; a window beyond a page: `window_partial` true and a cursor; an unreadable partition refuses the call); (5) the `rollback` (redeploy the base); (6) the `triggers` (health not 200 in 60 s, a tool of the 27 not answering, the `.env` key count not 65, `tools/list` changing from 103, host memory above 85 percent during the paging read-back); (7) the gate lines (WARN/RAISE) the release commit printed and the overlay disclosure. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

4. PRECONDITIONS: re-read the live ref and the `.env` (65 keys, `MUSE_CLIENT_ID` absent) and the host memory percent; else STOP. Ledger `nfra-oplgtw-gateway-release-batch4`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-batch4` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>` under the stale-base guard; no `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base and file an ARMED row naming `2.0.0_SA_COO~O`.
5. **The served read**, through the INSTALLED code on the host and the public endpoint, writing `W/CODE4_SERVED.json` = `{"body": {"read_at", "live_commit", "health_status": 200, "env_key_count": 65, "reader_env_keys_present": 7, "registry_count": 103, "per_tool_good": 27, "host_md5": {"equal": N, "differ": 0}, "tools_list_before": N, "tools_list_after": N, "muse_env_present": false, "arms": {"e1_cursor_first_page": bool, "e1_cursor_pages_to_window_start": bool, "e1_newest_first": bool, "e7_catalog_on_host": bool}, "arm_counts": {...}}}`. Counts, seconds, percentages and booleans only; every arm is one real call chain by an Opal master_admin stand-in (never a seat's identity). `e1_cursor_first_page`: `client_get_transactions` and `client_get_fees` asked for a 13-month window each return `partitions_read` 60, `window_partial` true, a non-null `next_cursor`, and the call's wall time is recorded (it must be under 30 s). `e1_cursor_pages_to_window_start`: following `next_cursor` as `to_date` until it is null, every dated partition of the window is read exactly once (transactions about 334 across 6 pages, fees about 396 across 7), record pages, partitions read, rows, and the longest page's wall seconds. `e1_newest_first`: within each page the row dates are non-increasing, and each next page's newest date is not later than the previous page's oldest. `e7_catalog_on_host`: the installed `app/refs/DATA_CATALOG.yaml` md5 on the host equals `bdfee515ec348f0ea2ee716eff5acba5`. Record the host memory percent before, at the peak during the paging and after (it must stay at or below 85). No row content, account number or person's name is printed; the account stays `****<last4>`.
6. **Standing clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once per phase. After the close, `2.0.0_SA_COO~O` tells `2.0.0_SA_COO~MI` (who runs the host checks of the catalog: `r13.AC2` should read 127 of 127) and `~MP` the live commit.

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no env key, no deploy-script or manifest change, no object or item written to any bucket or table.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; print an `.env` value, a credential, an account number, a person's name or email, or object content; set `MUSE_CLIENT_ID`; override a gate other than the audited lane escape named in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch4.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`. The manifest is NOT in your paths: it changes only at the close, when the deploy wrapper writes `deployed_commit` and the checksums.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-32"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap32.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the batch set 0 \(want 0\); terraform files differing 0 \(want 0\); tools.py or destructive_ops.py touched 0 \(want 0\).*catalog blob in the release is 2cbe275d03 \(want 2cbe275d03\), equal to trunk's: yes.*deploy script or manifest changed 0 \(want 0\); data copies committed 0 \(want 0\); registry files in the diff \d+, not byte-equal to trunk's 0 \(want 0\); ask has the three halves yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-32"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap32.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*tools/list before (\d+) after \1 \(want equal\); MUSE_CLIENT_ID present False.*reader env keys 7 of 7; registry 103 \(want 103\); per-tool 27 of 27; host md5 differ 0 \(want 0\); arms true 4 of 4.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-32" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly `OG-en-17`'s files and MI's catalog blob, no Terraform, no tool added, no deploy-script or manifest change, any registry file in the diff byte-equal to trunk's. `AC2`: the release landed and closed; the installed code pages the window back with a cursor, newest first, inside the request budget; the catalog on the host is MI's emit; the tool list and the env are unchanged.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the 13-month transactions and fees read as an analyst would want (the whole window reachable by paging, newest first, the window state stated). Graded on bodies the issuer relays (a page chain); never simulated here.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-32.round-40-batched-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-C (decomposition addendum R3-T.103). The release rides after `OG-ap-31` (live `4be300110e`) and `OG-en-17` (merged `4ebc1e781b`). Queue on the gateway host: THIS only.
- Staged: the GO for Phase A is the issuer's message citing this order and naming `trunk_sha`, sent when this order is committed. The three halves are signed on the ask your Phase A drafts.
- The catalog moves with this release because MI's frozen blob `3d47a95791` went stale after `MX-c-24`'s six lines (MI row Z-S136) and was re-emitted against the live commit; MI's COO half v2 is signed on the new blob.
- Pre-cut: `ap32.AC1` and `ap32.AC2` base FAIL as expected (records absent). `ap32.AC1` PASS arm exercised on a git-plumbing release commit built from the live ref; controls FAIL (tools.py touched; the deploy script changed; a registry file not byte-equal; the OLD catalog blob). `ap32.AC2` served-record arm: a good record OK, an arm false NO, a `tools/list` drift NO.
- Known carries, not in this release: the allocation weight unit (Z-S313), the browser-exemption roster (Z-S322), the 429 limit choice (Z-S177), the per-partition prefix listing (Z-S328).

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-C</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
