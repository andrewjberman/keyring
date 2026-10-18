# NFRA_OPLGTW task order -- `OG-ev-9` -- a read-only TRACE of the gateway's per-identity limiter (round 43; round-42 analysis item 9; row `Z-S177`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-9</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-9</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~155</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only trace; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. Any AWS call you make is a read-only `get`/`list`/`describe`.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (round-42 analysis, item 9: a table and a recommendation, no change).
EGRESS CLASS, declared: AWS read-only, COUNTS ONLY (the audit lake, if you can reach it); no object body is printed or copied.
</preflight>

## 1. THE CELL -- `OG-ev-9` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

WHY. Row `Z-S177`: the gateway's per-identity limiter answers 429 `{"error":"rate_limited","scope":"identity"}` to interactive seats. The hazard is live: the issuer's own `opalgateway` MCP connection failed with exactly that answer (HTTP 429, `rate_limited`, scope `identity`) on 2026-10-18 while this round was running. YOU TRACE; you change nothing.

THE TRACE (read-only). Four things, in one record `W/LIMITER_TRACE.json`:
1. THE LIMITER. Read `infra/aws/ec2/opal-gateway/app/ratelimit.py` (the sliding-window-log `check` and `enforce_identity_counted`), `app/config.py` (`RL_MCP_IDENTITY_LIMIT` and `RL_MCP_IDENTITY_WINDOW`, lines about 397 and 398) and `app/server.py` (the `GuardMiddleware` branch that answers 429, about lines 170 to 190; the `Retry-After` header). State: the limit, the window in seconds (the check reads the DEFAULTS from `config.py` and requires your numbers to equal them; if the host overrides them by environment, say so in your report, do not put an override in the record), what the bucket is keyed on (`principal.key`, in words: the validated identity), whether the 429 carries `Retry-After` (and what value, derived from the window and the oldest request), the fail mode (the limiter fails OPEN), and the `source` as a list of `file:line` strings (at least two).
2. THE IDENTITIES. Which identities hit the limiter in the last 24 hours, COUNTS ONLY. The limiter writes ONE audit row per identity per 10 seconds on a refusal (`audit.log_ratelimit`: event `gw_ratelimit`, outcome `rate_limited`, with `count_in_window` and `by_client`). Find the audit lake as in `app/audit.py` (`_lake_key`, `AUDIT_S3_BUCKET`) and the project registry (`comp-estate`; do not guess a bucket name) and count, READ-ONLY, the `gw_ratelimit` rows of the last 24 hours per principal. Record `{"source": "<where you counted>", "absent_reason": null, "denominator": <number of refusal rows you counted in all>, "rows": [{"principal_hash": "<the first 8 hex characters of the sha256 of the principal field, computed by you; never the principal itself>", "refused": <rows>, "client_keys": <the distinct by_client keys seen>}]}`. If you cannot reach the lake read-only inside this cell, write `{"source": null, "absent_reason": "<why>", "denominator": null, "rows": []}`: an ABSENT with its reason is a finding.
3. THE RECONNECT PATH. From the 429's `Retry-After` and the window, answer: does a client that retries INSIDE the window re-hit the limit? Record `{"retry_after_seconds_max": <the largest Retry-After the code can send>, "client_retry_inside_window_rehits": "yes|no|unknown", "evidence": "<one line: the sliding-window rule (a refused request is NOT appended to the log, so waiting Retry-After seconds clears one slot) and what that implies for a reconnect loop that opens several requests at once>"}`. You cannot read the MCP client's code; say `unknown` for anything about the client that you did not read in this repository.
4. THE RECOMMENDATION: one paragraph, `recommendation`, of at least 40 characters: what (if anything) a later cell should change (the limit, the window, the keying, the audit visibility), grounded in your rows. NO CHANGE is made by this cell.
The record carries no email address, no principal, no account value and no token: `principal_hash` is at most 8 hex characters.

## 2. BOUNDS

- Write only `W/LIMITER_TRACE.json` and (if a row is needed) the channel. NO product file, no test, no release, no deploy, no S3 write, no copy of lake objects into the repository.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~155/` (the tree convention grants it). You only READ the gateway source. Rows: id `NFRA_OPLGTW-Z-W155-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ev9.AC1.sh; echo "exit=$?"</invocation><expect>(?s)limiter: limit \d+ per \d+ s \(config defaults read here: \d+\.0 per \d+\.0 s\).*Retry-After header True, fail mode open.*ok.*email-shaped strings in the record 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ev-9"><invocation>git log --author='0.9.0_WK_NFRA_OPLGTW~155 <' --name-only --format= | grep -v '^org/missions/D9/NFRA/NFRA_OPLGTW/' | grep -c . ; echo "exit=$?"</invocation><expect>(?s)^0\s*exit=[01]\s*$</expect></criterion>
</proof_of_spec>

- `AC1`: the limiter's numbers equal the code's defaults, the identities are counted or ABSENT with a reason, the reconnect answer is given, the recommendation is written, and the record holds no email-shaped string. `AC2`: your commits touch no file outside the project tree (no product file).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-9.round-43-trace-the-per-identity-limiter.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, the limit and window, how many identities and refusal rows or why ABSENT, the reconnect answer, the recommendation in one sentence).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 9 ("the trace reads the limiter's window, key and limit; the identities hitting it in the last 24 hours (counts only); and whether the MCP reconnect path retries into the same window; the output is a table and a recommendation; no change"). The last clause reads, for a gateway-only cell, as the Retry-After arithmetic: the MCP client's retry code is not in this repository.
- Issuer read at the cut: limit 120 per 60 s per identity key (config defaults), fail-open, `Retry-After` set on the 429, one audit row per identity per 10 s (`record_identity_refusal`). The check compares the record with `config.py`'s defaults, not with these words.
- Read-only, no product path in `<paths>`: `<risk>LOCAL</risk>`.
- Pre-cut: `AC1` base FAIL as expected (the record is absent).

<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~155</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
