# NFRA_OPLGTW task order -- `OG-ev-12` -- READ-ONLY: who answered the organic per-identity 429 of 2026-10-18 about 19:2xZ that left no `gw_ratelimit` row? (round 45; round-44 analysis item 1; row `Z-W155-S1`, ARMED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-12</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-12</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform, no SSM write, no S3 write. Every AWS and host call is a read-only `get`/`list`/`describe`/`journalctl`.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-44 analysis, item 1 (journal, response shape, the limiter's throttle rule; a verdict and its evidence; no change).
EGRESS CLASS, declared: Opal's own AWS and the gateway host only; COUNTS ONLY (no principal, email, account or object content is printed or kept).
</preflight>

## 1. THE CELL -- `OG-ev-12` (decomposition addendum R3-T.122, round 45, workstream ENRICH-R45-A)

WHY. Round 44's `OG-ev-10` proved that the refusal writer's row reaches the audit lake under the service's instance role (the one-object writer test, `WRITES`), yet the CTO's own `opalgateway` connection received `{"error":"rate_limited","scope":"identity"}` at about 2026-10-18 19:2xZ and the lake holds NO `gw_ratelimit` row for that hour (399 objects between 19:00Z and 20:00Z, 0 rows). The code path from a per-identity 429 to the writer is direct (`app/server.py` lines 177 to 186 call `ratelimit.record_identity_refusal`, which writes ONE row per principal per 10 seconds, the FIRST refusal of a key always writing). So the 429 either did not come from this service's limiter, was folded by the per-key throttle, or this service answered it and its row failed to land. YOU DECIDE which, by a rule fixed here. You change NOTHING.

THE VERDICT RULE, fixed before you run anything (the check `ev12.AC1.sh` recomputes it from your numbers; read its header first), in this order:
- `THIS_SERVICE_WROTE_NOTHING` if the journal holds one or more `POST /mcp` lines answered 429 in the window and the lake holds 0 `gw_ratelimit` rows for 19:00Z to 20:00Z;
- `THROTTLED` else if the journal holds 429 lines and the lake holds at least one row but fewer than the 429 lines (the per-key fold explains the difference; record the `suppressed` sum of the rows);
- `OTHER_LAYER` else if the journal holds 0 `POST /mcp` 429 lines AND covers the 429's time (the first access line is at or before the start of the 429's time range and the journal window runs to its end): a 429 this service's access log never saw;
- `UNDETERMINED` otherwise (the journal does not cover the time, or the lake leg is unreadable).

DO, read-only, and write `W/ORGANIC_429.json` (exact shape in the header of `ev12.AC1.sh`):
1. THE JOURNAL. On the host, from `journalctl -u <the gateway unit>` from the first `POST /mcp` access line after the `OG-ap-44` restart (`2026-10-18T19:23:53Z`, the access log's return; read the real first line's timestamp into `first_access_line_ts`) to `2026-10-18T20:00:00Z` (`window_end`): count the access lines for `POST /mcp` answered 429 (`post_mcp_429_lines`), and the lines answered 429 on any other route (`other_429_lines`). Counts only; print no line that carries an address or an identity. Put the exact command in `source`. If the journal no longer reaches back to 19:23:53Z, say so: the first line you can read is the `first_access_line_ts` and the verdict follows the rule.
2. THE TIME OF THE 429. `organic_429_ts_range` = `{"from", "to"}`: the CTO's connection refused "at about 19:2xZ", so `from` `2026-10-18T19:20:00Z` and `to` `2026-10-18T19:29:59Z` unless the journal or the lake lets you narrow it (say how in `evidence`).
3. THE LAKE. In the audit lake (S3 bucket `opal-mcp-audit`, keys `audit/dt=<YYYY-MM-DD>/<ts>-<id>.jsonl`, one record per object) over `2026-10-18T19:00:00Z` to `2026-10-18T20:00:00Z`, count the records whose `event` is `gw_ratelimit` (`gw_ratelimit_rows`), the sum of their `suppressed` fields (`suppressed_sum`), and the objects listed (`denominator`, above 0; `read_errors` must be 0). Counts only; never print a principal.
4. THE RESPONSE SHAPE. Where you can read it read-only (the journal, the ALB or CloudFront access logs if the account keeps them and you can read them without a write, the gateway host's proxy logs), record what the 429 answer looked like: this service answers `{"error":"rate_limited","scope":"identity"}` with a `Retry-After` header (`app/server.py` lines 182 to 185); say whether that shape was seen (`guard_middleware_body_seen` true or false) or could not be read (`null`), and what you looked at, in `response_shape.evidence`.
5. THE THROTTLE RULE, AT A PINNED SHA. Pin `code_sha` = the live ref you read on the host (`/opt/opal-gateway/.deployed_commit`; expected `e09c30c3f064296ae7f8eb2c47b91bfec0be9b60`). Read `app/ratelimit.py` AT that sha (`git show <sha>:infra/aws/ec2/opal-gateway/app/ratelimit.py`), never at trunk, and record `throttle_rule` = `{"refusal_window_s": <the _REFUSAL_WINDOW_S value>, "first_refusal_writes": true, "source": "app/ratelimit.py:<line>"}`; the check reads the same constant at the same sha and requires equality.
6. `verdict` by the rule above and `evidence` (at least two strings, each one line: what you counted, where, and what it shows).

## 2. BOUNDS

- Only `W/` and the channel. No product file, no test, no release, no deploy, no S3 or SSM write, no Terraform, no restart, no request to the gateway.
- No principal, email address, account number, token or object content in any record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; run gateway code on the host without the hard guard (this cell runs none).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ev12.AC1.sh; echo "exit=$?"</invocation><expect>(?s)journal: 429 lines on POST /mcp \d+, on other routes \d+, first access line \S+, window end \S+: ok; lake 19:00Z to 20:00Z: gw_ratelimit rows \d+ \(suppressed \d+\) over \d+ objects, read errors 0: ok.*throttle rule at the pinned code sha: refusal window [0-9.]+ s \(the code at [0-9a-f]{10} reads [0-9.]+\): ok; the journal covers the organic 429's time (yes|no); verdict by the rule fixed before the run: (THIS_SERVICE_WROTE_NOTHING|OTHER_LAYER|THROTTLED|UNDETERMINED), the record says \2: consistent.*email-shaped strings 0 \(want 0\); digit runs of 9 or more 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the journal and lake counts are present and read without error, the throttle rule is read at the pinned sha and equals the record, the verdict equals what the rule returns from those counts, and the record holds no email, no principal and no long digit run.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-12.round-45-who-answered-the-organic-429.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>` (`python3`, not `python`: only `python3 -I` sees `jsonschema`, ruling msg 35901), and flip NOTHING (the `<status>` flip is mine). Report once: the commit hash, the journal 429 counts, the lake row count, the verdict, and the evidence in two lines.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 45, workstream ENRICH-R45-A, `<risk>LOCAL</risk>` (a read; no served data path is touched). Source: the CTO's round-44 analysis (`ledger/ROUND_ANALYSIS.round44.md` @ebefeda213, msg 35898), item 1: "the journal of 2026-10-18 from 19:24Z to 20:00Z for any 429 and its route; whether the answer's body and shape are `GuardMiddleware`'s own, or another layer's; the limiter's per-key throttle rule against a first refusal; output: a verdict `THIS_SERVICE_WROTE_NOTHING` / `OTHER_LAYER` / `THROTTLED` / `UNDETERMINED`, with its evidence. No change."
- READING DISCLOSED TO THE CTO: the four verdicts are given concrete rules (above). The access log returned at the `OG-ap-44` restart, `2026-10-18T19:23:53Z` by `OG-ev-10` STEP 1's read; if the CTO's 429 happened BEFORE that, the journal cannot show it and the rule returns `UNDETERMINED`, which is an honest answer; the lake leg (19:00Z to 20:00Z) is read either way. `THROTTLED` needs at least one lake row, so it cannot be the answer to "0 rows".
- Process-wide state (CVO verdict 35844): none (reads).
- Pre-cut: `AC1` base FAIL as expected (the record is absent). Synthetic arms fed to the check: journal not covering the time reads `UNDETERMINED` (PASS); covered with 0 lines reads `OTHER_LAYER` (PASS); 2 lines and 0 rows reads `THIS_SERVICE_WROTE_NOTHING` (PASS); 2 lines and 1 row reads `THROTTLED` (PASS); a verdict that contradicts the rule FAILS; a refusal window that differs from the code at the pinned sha FAILS.

<status>staged</status>
<status>complete</status>
<round>45</round>
<workstream>ENRICH-R45-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
