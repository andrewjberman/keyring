# NFRA_OPLGTW task order -- `OG-ev-11` -- SIZE the inline audit-write repair before building it: complete OG-ev-8's table with per-tool call counts and the SDK's dispatch rule (round 44; round-43 analysis item 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-11</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-11</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~157</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. Any AWS call you make is a read-only `list`/`get`/`head`.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-43 analysis, item 2 (a table and a ranked proposal, no change).
EGRESS CLASS, declared: AWS read-only on the audit lake (COUNTS ONLY: no object body, principal or account value is printed, copied or kept) and ONE download of the public PyPI package `mcp==1.28.0` into a scratch folder to read its source.
</preflight>

## 1. THE CELL -- `OG-ev-11` (decomposition addendum R3-T.121, round 44, workstream ENRICH-R44-A)

WHY. `OG-ev-8` (round 43) listed the gateway's 81 inline audit-write call sites (`audit._emit` appends a file and, when `AUDIT_S3_BUCKET` is set, calls boto3 `put_object` with default timeouts) and could not fill two columns: how often each site runs (the lake key names no tool) and whether 12 sites run on the event loop (they sit under SYNC `@mcp.tool` bodies; row `Z-W154-S1`: whether FastMCP in the pinned `mcp==1.28.0` runs a sync tool body on the event loop or in a worker thread is decided by that package, which the cell did not read). A repair is a round-45 decision. YOU SIZE IT: you change nothing in the product.

START FROM `OG-ev-8`'s record, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~154/AUDIT_SITES.json` (81 sites at base `581ee61977256c4daf2d71189997f9b7f5335727`). Write `W/AUDIT_SITES_SIZED.json` (`W` below). The same 81 sites, re-listed in your record, each with `on_event_loop` `yes` or `no` (NEVER `unknown` now), `loop_reason`, `timeout_s` and `timeout_reason` as the record has them, and `calls_7d` (an integer, or `"ABSENT"` with `absent_reason`) with `calls_7d_source` when an integer. Pin the base: `"base_sha": "581ee61977256c4daf2d71189997f9b7f5335727"`; the check reads the call sites AT that sha (`git grep` on the sha), never at trunk, because trunk has moved.

THE FOUR PARTS (one record, exact shape in the header of `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/ev11.AC1.sh`, which you must read first):
1. THE DISPATCH RULE (`mcp_dispatch`). Download the package source ONLY into a scratch folder outside the repository: `python -m pip download mcp==1.28.0 --no-deps -d <scratch>`, unzip the wheel, and READ how `mcp.server.fastmcp` calls a tool function that is a plain `def` (not `async def`): directly on the event loop, or through a thread (`anyio.to_thread.run_sync` or similar). Record `package` `mcp`, `version` `1.28.0`, `source` (the command you ran), `rule` (one paragraph in your words, at least 40 characters), and `evidence`, at least two strings of the form `<file inside the package>:<line>`. Then set each of the 12 formerly-unknown sites `yes` or `no` from that rule (a sync tool body under the rule's answer) with `loop_reason` naming it. If you cannot obtain the package, file a BLOCKING row and stop that part; do NOT guess.
2. THE LAKE (`lake`). The audit lake is the S3 bucket `opal-mcp-audit`, keys `audit/dt=<YYYY-MM-DD>/<ts>-<id>.jsonl` (one record per object; `app/audit.py` `_lake_key` and `_emit` write them). LIST every key of the last 7 UTC days (`dt=` partitions; today's partition counts as a day only if it is the 7th) with boto3 `list_objects_v2` paginated, and record the exact count per day in `keys_listed` (seven `YYYY-MM-DD` keys). Then READ the bodies of every k-th key (sorted by key), where you choose the integer `sample_every_k` so that no more than 12000 objects are read (an order of 70000 keys needs k of about 6 to 10); record `sample_every_k`, `objects_read` and `read_errors` (must be 0: retry a failed get up to 3 times; a key that still fails is a BLOCKING row), `method` and `days` 7. Run the long read as a background script that writes progress to a file in your scratch folder and poll it; no single command may run over 120 seconds.
3. THE COUNTS (`per_tool_counts`). From the record BODIES you read, count per tool: the record's tool or event name field (read `app/audit.py` and two sample records' KEY NAMES only to find the field; never print a value that is a principal, email, account or token). Record one row per tool or event name: `{"tool": "<name>", "observed": n, "scaled_7d": n x sample_every_k}`. Then map each of the 81 sites to its tool or event if the site is plainly one tool's path and set `calls_7d` to that tool's `scaled_7d` with `calls_7d_source` naming the row; a site shared by many tools gets the sum of the tools that reach it or `"ABSENT"` with the reason. A value that cannot be derived is ABSENT with its reason, never 0.
4. THE RANKING (`ranking`). One to five proposals, ranked 1..n, each `{"rank": n, "proposal": "<at least 40 characters: what to change, e.g. a thread hop, a bounded botocore timeout, a queue, nothing>", "sites": <how many of the 81 it covers>, "basis": "<which counts or rule>"}`. The repair is NOT made.

The record carries no email address, no principal, no account value and no token.

## 2. BOUNDS

- Write only `W/AUDIT_SITES_SIZED.json`, your scratch folder (outside the repository) and, if a row is needed, the channel. NO product file, no test, no release, no deploy, no S3 write, no copy of lake objects into the repository.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~157/` (the tree convention grants it). You only READ the gateway source and the lake. Rows: id `NFRA_OPLGTW-Z-W157-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/ev11.AC1.sh; echo "exit=$?"</invocation><expect>(?s)call sites at base 581ee61977 matched by the pattern: 81 .*listed: 81; missing from the record 0 \(want 0\); not at that sha 0 \(want 0\); malformed rows 0 \(want 0\); event-loop column unknown on 0 site\(s\) \(want 0\).*mcp 1\.28\.0 dispatch rule with \d+ evidence lines: ok.*ranked proposals \d+: ok; email-shaped strings 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ev-11"><invocation>git log --author='0.9.0_WK_NFRA_OPLGTW~157 <' --name-only --format= | grep -v '^org/missions/D9/NFRA/NFRA_OPLGTW/' | grep -c . ; echo "exit=$?"</invocation><expect>(?s)^0\s*exit=[01]\s*$</expect></criterion>
</proof_of_spec>

- `AC1`: the 81 sites at the pinned base are all listed, none unknown, the dispatch rule is read from the package with evidence, the lake is listed in full for 7 days and sampled at a printed rate with scaled counts, a ranked proposal is given, and the record holds no email-shaped string. `AC2`: your commits touch no file outside the project tree.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-11.round-44-size-the-inline-audit-write-repair.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, the SDK's rule in one sentence, `sample_every_k` and objects read, the three highest-count tools, and your rank-1 proposal in one sentence).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 44, workstream ENRICH-R44-A. Source: the CTO's round-43 analysis (`ledger/ROUND_ANALYSIS.round43.md` @d35c913755, msg 35841), list item 2: "per-tool call counts over the last 7 days, from record BODIES (counts only, no content); read the pinned `mcp` SDK's dispatch rule for the 12 sync tools marked unknown; output: the 81-site table completed and a ranked repair proposal; the repair is a round-45 decision."
- READING DISCLOSED TO THE CTO: "per-tool counts over the last 7 days" is read as every key LISTED for 7 days (exact denominator) and the bodies read for a sample of at most 12000 objects (about 70000 keys at 11301 a day, measured by `OG-ev-9`), the counts scaled by the printed rate. Reading all 70000 bodies inside a worker's 120-second command limit is not a bounded job. If the CTO wants every body read, that is a second pass with a longer-lived reader.
- Standing condition 3 (pin the base sha) is applied in the check: it reads the sites at `581ee61977`.
- Read-only, no product path in `<paths>`: `<risk>LOCAL</risk>`.
- Pre-cut: `AC1` base FAIL as expected (the record is absent); a synthetic green record built from `OG-ev-8`'s sites passes it, and an `unknown` row, 20000 objects read and a scaled count off by the rate each fail it.

<status>pending</status>
<round>44</round>
<workstream>ENRICH-R44-A</workstream>
<slot>~157</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
