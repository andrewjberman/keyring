# NFRA_OPLGTW task order -- `OG-ev-8` -- MEASURE the inline audit-write call sites before any repair (round 43; round-42 analysis item 7; worker row `Z-W147-S1`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-8</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-8</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~154</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. Any AWS call you make is a read-only `get`/`list`/`describe`.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (round-42 analysis, item 7: measure before any repair; the repair is a round-44 decision made on your table).
EGRESS CLASS, declared: AWS read-only, COUNTS ONLY (the audit lake, if you can reach it); no object body is printed or copied.
</preflight>

## 1. THE CELL -- `OG-ev-8` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

WHY. Worker row `Z-W147-S1` found that `audit._emit` (`infra/aws/ec2/opal-gateway/app/audit.py`, line 40) appends a JSONL record to a file and, when `AUDIT_S3_BUCKET` is set, also calls boto3 `put_object` to the audit lake with default timeouts, and that it is called INLINE from async code: a slow or unreachable S3 stalls the whole single-worker gateway event loop. The probe listener was repaired for its own calls (`OG-pr-2`); the rest of the gateway still writes inline. Before any repair is designed, the CTO wants the table: which sites run on the event loop, how often each is called, and what timeout each is under. YOU MEASURE; you change nothing.

THE TABLE (read-only). The call sites are every line under `infra/aws/ec2/opal-gateway/app/` (all `.py` files, including `integrations/` and `audit.py` itself) that matches `\baudit\.[A-Za-z_]+\(|\b_emit\(` (the check measures the denominator itself with `git grep -nE` over those files and requires every matching line in your record; at the cut it matches 81 lines). For EVERY matching line write one row in `W/AUDIT_SITES.json`:
`{"body": {"sites": [{"file": "<path under app/>", "line": <n>, "call": "<the call text, 120 characters or fewer>", "on_event_loop": "yes|no|unknown", "loop_reason": "<one line: the enclosing function is `async def` and the call is not wrapped in run_in_threadpool / to_thread / an executor (yes); it runs in a sync function only ever called from a thread or at import (no); or you could not tell (unknown)>", "timeout_s": <number, or null when the write has no timeout of its own>, "timeout_reason": "<one line: what bounds the write, for example the boto3 client config, or that it uses botocore defaults>", "calls_7d": <integer, or "ABSENT">, "calls_7d_source": "<when an integer: what you counted and where>", "absent_reason": "<when ABSENT: why you could not read it>"}], "frequency_source": "<where calls_7d came from, or null>", "frequency_absent_reason": "<when no site has a count: why>"}}`.
- `on_event_loop`: read the enclosing function of each call. An `async def` (or a function an `async def` calls directly, with no thread hop) means `yes`. A function that is only called from `run_in_threadpool`, `asyncio.to_thread` or an executor, or only at import time, means `no`. State which you read in `loop_reason`. If the enclosing function is called from both, it is `yes` (the worse case) and you say so.
- `timeout_s`: read how `audit._emit` builds its S3 client and its `put_object` call (`app/audit.py`). If it sets no `connect_timeout`/`read_timeout`/`retries`, the botocore defaults apply (60 s connect and read, up to 5 attempts in `standard` mode or 4 in `legacy`): write `null` and say so in `timeout_reason` (do not invent a number you did not read).
- `calls_7d`: the number of audit records the site writes over the last 7 UTC days, counted READ-ONLY from the audit lake. Find where the lake is from `app/audit.py` (`_lake_key`, `AUDIT_S3_BUCKET`) and `comp-estate` / `infra/logic` (use the registry, do not guess a bucket name); count by LISTING the lake's own date partitions and, where a key encodes the tool or event, counting keys by that name; do NOT download or print an object body. Several sites that write the same tool or event share one count: say so in `calls_7d_source`. If you cannot reach the lake read-only inside this cell (no credentials, no list permission, no key structure that encodes the event), write `"ABSENT"` with the reason on every site and the record-level `frequency_absent_reason`: an ABSENT count with its reason is a finding; a 0 you did not measure is a defect.
Do not print an environment value, a secret, an email address or a client value anywhere.

## 2. BOUNDS

- Write only `W/AUDIT_SITES.json` and (if a row is needed) the channel. NO product file, no test, no release, no deploy, no S3 write, no copy of lake objects into the repository.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~154/` (the tree convention grants it). You only READ the gateway source. Rows: id `NFRA_OPLGTW-Z-W154-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ev8.AC1.sh; echo "exit=$?"</invocation><expect>(?s)inline audit-write call sites matched by the pattern under app/: (\d+) \(the cut counted 81\); listed in the record: \1; matched lines missing from the record: 0 \(want 0\); malformed rows: 0 \(want 0\).*every site ABSENT carries the record-level reason: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ev-8"><invocation>git log --author='0.9.0_WK_NFRA_OPLGTW~154 <' --name-only --format= | grep -v '^org/missions/D9/NFRA/NFRA_OPLGTW/' | grep -c . ; echo "exit=$?"</invocation><expect>(?s)^0\s*exit=[01]\s*$</expect></criterion>
</proof_of_spec>

- `AC1`: every inline audit-write line the pattern finds is a row, each row is complete (every column is a value or an ABSENT/unknown/null with its reason), and the record states whether the frequency column was read. `AC2`: your commits touch no file outside the project tree (no product file).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-8.round-43-measure-the-inline-audit-write-sites.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, how many sites are on the event loop, how many are unknown, whether the frequency column was read or ABSENT and why, the timeout finding in one line).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 7 ("read-only: per site, whether it runs on the event loop, its call frequency over the last 7 days of logs, and its timeout; the repair is a round-44 decision made on that table"). The issuer cannot tell from the cut where the audit lake lives or whether a worker's credentials can list it, so the frequency column degrades to ABSENT-with-reason rather than to a guess; the CTO decides in round 44 whether an ABSENT frequency needs its own cell.
- The slug's 82 became 81 under the pattern above (one grep in the issuer's hands: `audit.<name>(` plus `_emit(` over `app/*.py`); the check prints the count it measures. Disclosed so the difference is not a surprise.
- Read-only, no product path in `<paths>`: `<risk>LOCAL</risk>`.
- Pre-cut: `AC1` base FAIL as expected (the record is absent).

<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~154</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
