# TO IRPT_BCKEND.TO-IB-pr-531 -- CENSUS the holdings producer, READ ONLY: how it is deployed and scheduled, its code hash, and its rollback by manifest version per firm (CTO round-190 analysis item 3 @6e527b13c6; row D2-W375-S4; the rearm test `test_holdings_rearm_trigger.py`, row S71)

<to_id>IRPT_BCKEND.TO-IB-pr-531</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~378</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>190</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-190 analysis (item 3: "how the holdings producer is deployed and scheduled, which function or task, which code hash, which schedule, and its rollback by manifest version per firm. Both halves are signed only after this read") | **Decomp cell:** `IB-pr-531` (decomposition section 182) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-378` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~378 <0.9.0_WK_IRPT_BCKEND~378@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read; print what a search covered before you read a zero as an absence). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-531` (inlined).** A later release will move the holdings producer's code (two changes to `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: the cash rule on both layers, and the publish-gate directory exemption). Round 189's packet could not say how that producer is deployed. What is already known (read it, then measure): the file `data/assets/scripts/gold/investor_reporting/tests/test_holdings_rearm_trigger.py` documents that the enabled EventBridge Scheduler schedule `irpt-holdings-snapshot` dispatches, through `infra/aws/lambda/investor-reporting/holdings_refresh/refresh_dispatch.py` (env `IRPT_HOLDINGS_BUNDLE_MAP`), ONE SSM command per firm that fetches that firm's own standalone package `s3://opal-data-<firm>/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz` and runs `holdings_snapshot.py --firms <firm> --upload`; the test's last run (2026-10-14) printed that three served bundles each lack four registry files the runner opens (`infra/logic/registry/feeds.json`, `firm_pages.json`, `legacy_addresses.json`, `platinum_destinations.json`) while the schedule reads ENABLED, and it FAILS; yet Cottonwood's `publish_refusal.json` was written by a scheduled fire at 2026-10-13T14:17:45Z, so fires run. **This order measures the producer's deployment and reconciles those two facts. It writes and invokes nothing.**

**Client data rule:** counts, dates, version ids, hashes and object names only in any tracked file; no account id, client id, position value or holding name; objects are read into memory or scratch OUTSIDE the worktree (`C:/dev/_scratch378/`), and the scratch is deleted at the end with a short bounded script.

**Do, in this order (every fact is a MEASUREMENT with its source named in `notes`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it).
2. **Read the code.** `test_holdings_rearm_trigger.py`, `refresh_dispatch.py` and what it names (the bundle map, the SSM command shape), and the standalone-bundle declaration the test cites (`safe_deploy_core.STANDALONE_BUNDLES`; find the file with Glob), and `.tools/safe-deploy*` or the deploy tool that puts a standalone bundle on S3 (name the tool and say whether it opens a change-management ledger; the NEVER rule requires one for a confirmed deploy).
3. **The schedule (READ).** `.tools/aws scheduler get-schedule --name irpt-holdings-snapshot` (and its group if the call needs one): record name, state, schedule expression and target.
4. **The bundles (READ), per firm** (`49financial`, `cottonwood`, `inflection`): the object `s3://opal-data-<firm>/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz` (confirm the exact key shape from the code; never type a bucket by guess): `head-object` for its VersionId, LastModified and size; download it into scratch and record its sha256, the member count of the tarball and whether any member's text contains `apply_cash_rule` (a boolean). Record `has_apply_cash_rule` per firm.
5. **The S71 reconciliation.** From the tarball's own `SHA256SUMS` member list and the files `holdings_snapshot.py` opens (the rearm test's derivation), count the repo files the runner opens that the bundle lacks (`missing_member_count`; the test printed four), and state whether scheduled fires nonetheless wrote records (`scheduled_fires_wrote_records`: true when each firm's `current/manifest.json` or a refusal record carries a LastModified from a scheduled fire window after the bundle's LastModified; read the SSM command history for the last invocation per firm if your identity may, and say so if it may not). The `reading` is one or two sentences: why fires run despite the missing members (for example the runner tolerates their absence, or reads them another way) or that it does not know.
6. **The release path and rollback.** `release_path` = `{"deploy_tool": "<name>", "ledger_required": true|false, "rollback": "<one sentence: restoring the prior bundle object version, naming how it is read>"}`. `rollback_by_manifest_version` = per firm `{"manifest_key": "irpt/<firm>/platinum/holdings/current/manifest.json" (the address() output; confirm), "version_id": "<IsLatest version served NOW>", "last_modified": "<UTC>"}` by `list-object-versions` on that ONE named key (round 189's packet read these on 2026-10-14 ~03:3xZ; re-read and state if any moved).
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~378/IB190-3_producer_census.json`: `{"base_commit":"<40hex>","producer":{"runner":"<repo path>","dispatch":"<one sentence naming the dispatcher and the SSM command>","schedule":{"name","state":"ENABLED|DISABLED","expression","target"},"bundles":{"49financial":{"key_shape","version_id","sha256":"<64 hex>","last_modified","members":n,"has_apply_cash_rule":bool},"cottonwood":{...},"inflection":{...}}},"release_path":{...},"rollback_by_manifest_version":{"49financial":{...},"cottonwood":{...},"inflection":{...}},"s71_reconciliation":{"missing_member_count":n,"scheduled_fires_wrote_records":bool,"reading":"..."},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}` and a short readable `deliverables/0.9.0_WK_IRPT_BCKEND~378/PRODUCER_CENSUS_SUMMARY.md` (no more than 40 lines).
8. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB190-3_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the deliverables FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB190-3-AC1" cell_refs="IB-pr-531"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-3-AC1</invocation><expect>IB190-3-AC1 PASS</expect></criterion>
<criterion id="IB190-3-AC2" cell_refs="IB-pr-531"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-3-AC2</invocation><expect>IB190-3-AC2 PASS</expect></criterion>
<criterion id="IB190-3-AC3" cell_refs="IB-pr-531"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-3-AC3</invocation><expect>IB190-3-AC3 PASS</expect></criterion>

<expected_criteria>IB190-3-AC1, IB190-3-AC2, IB190-3-AC3</expected_criteria>

What the checks grade: AC1 the producer (runner, dispatch, the schedule's name, state, expression and target, and per firm the bundle's key shape, version id, 64-hex sha256, last modified, member count above 0 and `has_apply_cash_rule`); AC2 the deploy tool with its ledger rule and rollback sentence, and per firm a manifest key ending `current/manifest.json` with its version id and last-modified date; AC3 the S71 reconciliation (missing-member count, whether scheduled fires wrote records, a reading), notes, no long digit run and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. READ ONLY. **Nothing is invoked, written, uploaded, applied or deployed:** no Lambda invoke, no SSM `send-command`, no S3 write, no terraform, no sign-in, no vendor call. Allowed AWS calls (READ): `scheduler get-schedule`, `s3api head-object`, `get-object` of each firm's one named bundle object into scratch, `list-object-versions` on each firm's one named `current/manifest.json`, `ssm list-commands` or `list-command-invocations` if your identity may (a denial is recorded, not worked around), `lambda get-function-configuration` of the dispatcher if the code names one, `sts get-caller-identity`.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends a command; a value, name or identifier of a client or account in a tracked file; a figure you cannot source (say so; do not estimate). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W378-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~378/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 182 (round 190, workstream ~P), cell `IB-pr-531`.
<owned_cells>IB-pr-531</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB190-3-AC1, IB190-3-AC2, IB190-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~378/IRPT_BCKEND.TO-IB-pr-531.holdings-producer-census.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads one schedule, three named bundle objects (downloaded into scratch and hashed), three manifest key version lists and, if permitted, SSM command history; it writes and invokes nothing and sends no command; the release of the producer and its pair are later cells with their own blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; a denied read is recorded as a statement, never widened.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is READ, never created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p190_cells.py IB190-3 dry-run at base on dell2 2026-10-14 ~04:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (a synthetic record; removed): all three PASS; negatives, each failing its own arm: a schedule state outside ENABLED or DISABLED, a bundle sha256 not hex, a firm missing from the bundles, has_apply_cash_rule absent, no ledger rule, a manifest key of the wrong shape, a firm missing from the rollback, a write counter above 0, a long digit run, no reconciliation reading, empty notes.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~378` (worktree `C:/dev/wk-IRPT_BCKEND-378`). Class SERVED (reads the live schedule, served bundles and manifest versions; writes only the worker's records). The premises are the rearm test's documentation and its 2026-10-14 output; what the producer IS in the live estate is what this order measures.
</preflight>
