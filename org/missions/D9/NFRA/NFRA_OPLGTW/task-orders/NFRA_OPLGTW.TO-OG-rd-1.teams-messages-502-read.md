# NFRA_OPLGTW task order -- `OG-rd-1` -- READ the cause of every 502 on `/hx/teams/channels/.../messages` (E3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rd-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rd-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~62</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads of logs already written; nothing scheduled is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the operator's identity; nothing is granted.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-35 analysis E3 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round35.md @682d1ced78), row Z-S95: "READ first ... No retry layer until the cause is read."
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-rd-1` (decomposition addendum R3-T.48, E3)

Row Z-S95 (in the investigation file below): the gateway route `GET /hx/teams/channels/{team}/{channel}/messages` (live
since OG-ap-7) answers 502 on about 2 of 1440 COMM_ASSIST polls. The cause is unread.

1. **Find the gateway's own record of each 502.** Find where the gateway writes request and error lines: its application
   log on the host, shipped to CloudWatch (read `infra/aws/ec2/opal-gateway/` for the log group and logger names), and
   the audit lake `s3://opal-mcp-audit/audit/dt=<day>/` (records written by `app/audit.py`). Name the source you used.
2. **The window.** From the route's first live day (OG-ap-7's release, 2026-10-11) to now. List EVERY 502 on that route in
   the window. For each, read the gateway's error body or log line and classify the cause from this closed set:
   - `gateway_timeout`: the gateway's own timeout;
   - `gateway_error`: an exception in gateway code, with its type;
   - `graph_throttled`: Graph 429 or a Retry-After;
   - `graph_5xx`: Graph 500, 502, 503 or 504;
   - `graph_4xx`;
   - `unreadable`: no body or line found.
3. **Positive control.** Count the route's 200s in the same window from the same source. It must be at least 1, or the
   instrument does not see the route.
4. Write `W/RD1_502.json` = `{"source", "window", "count_502", "items": [{"ts", "route", "cause_class", "detail"}],
   "positive_control_200", "verdict": "gateway"|"upstream"|"mixed", "fix_if_gateway"}`. `fix_if_gateway` names the code
   line to change, if the cause is the gateway's. Build NO fix and NO retry layer: the fix is a later cell.

## 2. BOUNDS

- Reads only. No code change, no deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a message body's content (route, status and error class
  only); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~62/`. Rows: id `NFRA_OPLGTW-Z-W62-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/rd1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)count_502 (\d+); items \1; items with a closed-set cause \1; verdict (gateway|upstream|mixed); positive control 200s [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every 502 in the window has a read cause, and the instrument provably sees the route.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rd-1.teams-messages-502-read.proof_of_spec.json`. Validate it after your
last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE
`<status>` tag to `complete` only if it PASSes, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 36, E3. Pre-cut: rd1.AC1 base FAIL as expected (file absent).

<status>pending</status>
<round>36</round>
<slot>~62</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
