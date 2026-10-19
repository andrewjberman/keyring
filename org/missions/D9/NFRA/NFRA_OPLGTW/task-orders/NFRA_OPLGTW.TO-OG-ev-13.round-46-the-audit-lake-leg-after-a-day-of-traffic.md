# NFRA_OPLGTW task order -- `OG-ev-13` -- READ-ONLY: the audit lake leg after a FULL DAY of production traffic (round 46; round-45 analysis item 1; row `Z-S402`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-13</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-13</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform, no SSM write, no S3 write. Every AWS and host call is a read-only `get`/`list`/`describe`/`journalctl`.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-45 analysis, item 1 (the journal's WARN lines and the running count, the lake per hour against `POST /mcp` per hour, and the 2026-10-19 02:00Z hour; a verdict and its evidence; no change).
EGRESS CLASS, declared: Opal's own AWS and the gateway host only; COUNTS ONLY (no principal, email, account or object content is printed or kept).
</preflight>

## 1. THE CELL -- `OG-ev-13` (decomposition addendum R3-T.123, round 46, workstream ENRICH-R46-A)

⛔ **STAGED, WITH AN ESSENTIAL WAIT: THE GO COMES NO EARLIER THAN `2026-10-20T07:45:00Z`.** The outcome is "the lake leg holds under a day of real traffic" (the CTO's analysis, section 2). Only elapsed traffic produces that, and no act can manufacture production load honestly, so the wait is not a polling delay. START ONLY on the issuer's GO, which names `window_end` (the GO's time, at least 24 hours after the `OG-ap-48` close).

WHY. Round 45's `OG-pr-6` and `OG-ap-48` made the audit lake leg bounded and audible: a failed lake put is counted and writes ONE stderr line (the first failure, then at most one per 60 s) carrying the exception class name and the running count, and the audit client has a bounded botocore `Config`. The release's own 30-minute read-back read 0 such lines. This cell reads a FULL DAY (row `Z-S402`, still open until a window of production traffic is read) and also explains one odd hour: the lake holds about 2,896 objects for `2026-10-19T02:00Z` to `03:00Z`, about 7 times the baseline hour. YOU CHANGE NOTHING.

THE VERDICT RULE, fixed before you run anything (the check `ev13.AC1.sh` recomputes it from your numbers; read its header first), in this order:
- `FAILS_SEEN` if the journal holds one or more `audit-lake WARN` lines in the window (a failed lake put was reported; record the classes and the last `count=`);
- `HOLDS` else if EVERY hour that holds 20 or more `POST /mcp` lines also holds at least 0.5 times as many lake objects (the lake keeps pace with the traffic);
- `UNDETERMINED` otherwise (an hour where the lake lags the journal with no WARN line is unexplained; or the journal does not reach the window start).

DO, read-only, and write `W/AUDIT_LEG_24H.json` (exact shape in the header of `ev13.AC1.sh`):
1. THE WINDOW. `window_start` = `2026-10-19T07:44:53Z` (the `OG-ap-48` ledger CLOSED time); `window_end` = the GO's time (at least 24 hours later). Pin `code_sha` = the live ref you read on the host (`/opt/opal-gateway/.deployed_commit`; expected `6b1a9bd292855841826e194d0bddf9ac79bc8337`; if it is anything else, say so in `evidence`), and set `warn_every_s` to the value of `_LAKE_WARN_EVERY_S` in `app/audit.py` AT that sha (`git show <sha>:infra/aws/ec2/opal-gateway/app/audit.py`), never at trunk; the check reads the same constant at the same sha.
2. THE JOURNAL. On the host, from `journalctl -u <the gateway unit>` over the window: count the lines containing `audit-lake WARN: lake put failed` (`warn_lines`), the last `count=` those lines print (`last_count`, 0 with none), and the exception class names they print inside the parentheses (`classes`, distinct). Counts only; print no line that carries an address or an identity. Put the exact command in `source`; `first_line_ts` is the first journal line you can read (it must reach `window_start`, else the verdict follows the rule).
3. THE HOURS. For every WHOLE hour that touches the window (24 or 25 consecutive hours: a window that starts at :44 spans 25 buckets), `hours[]` = `{"hour_start": "<iso on the hour>", "lake_objects": n, "post_mcp_lines": n}`: the audit-lake objects whose KEY time falls in that hour (list `s3://opal-mcp-audit` keys `audit/dt=<YYYY-MM-DD>/<ts>-<id>.jsonl`; LIST only, no bodies; the key time is the `<ts>`), and the journal's `POST /mcp` lines in that hour, both over the whole hour.
4. THE ANOMALY HOUR. `anomaly_hour` for `2026-10-19T02:00:00Z` to `03:00:00Z`: `objects` = the lake's real count for that hour (about 2,896 was listed); read EVERY body (`read` equals `objects`; retry a failed get up to 3 times; `read_errors` must be 0) and record a histogram `tools` = `[{"tool": "<tool or event name field>", "n": n}]` (counts only: find the field from `app/audit.py` and two sample records' KEY NAMES only; never print a value that is a principal, email, account or token), then ONE line `explanation` from the histogram (for example one tool dominating, or one event class). Run the long read as a background script that writes progress to a scratch file and poll it; no single command may run over 120 seconds.
5. `verdict` by the rule above and `evidence` (at least two strings, each one line: what you counted, where, and what it shows).

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
  <criterion id="AC1" cell_refs="OG-ev-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/ev13.AC1.sh; echo "exit=$?"</invocation><expect>(?s)window \S+ to \S+ \(at least 24 hours, from the OG-ap-48 close\): ok; journal: audit-lake WARN lines \d+ \(last count \d+, classes \[.*?\]\): ok.*24 or 25 consecutive hourly rows ok, busy hours \(20 or more POST /mcp lines\) \d+, the lake keeps pace in every busy hour (yes|no); the throttle constant at the pinned sha reads [0-9.]+ and the record says [0-9.]+: ok.*anomaly hour 2026-10-19T02:00Z: \d+ objects, \d+ read, errors 0, tool rows \d+, histogram covers at least 95 percent of the bodies read: ok; verdict by the rule fixed before the run: (HOLDS|FAILS_SEEN|UNDETERMINED), the record says \2: consistent.*email-shaped strings 0 \(want 0\); digit runs of 9 or more 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the window runs at least 24 hours from the `OG-ap-48` close, the journal and the hourly lake counts are present and read without error, the anomaly hour's bodies are all read and its histogram accounts for them, the throttle constant is read at the pinned sha and equals the record, the verdict equals what the rule returns from those counts, and the record holds no email, no principal and no long digit run.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-13.round-46-the-audit-lake-leg-after-a-day-of-traffic.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>` (`python3`, not `python`: only `python3 -I` sees `jsonschema`, ruling msg 35901), and flip NOTHING (the `<status>` flip is mine). Report once: the commit hash, the WARN line count and classes, the busy-hour result, the verdict, and the anomaly hour's explanation in one line.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, workstream ENRICH-R46-A, `<risk>LOCAL</risk>` (a read; no served data path is touched). Source: the CTO's round-45 analysis (`ledger/ROUND_ANALYSIS.round45.md` @de11baa89b, msg 35919), list item 1. The wait is essential and its reason is the CTO's (above); the L2 endpoint rule's qualification is carried by his analysis.
- READINGS DISCLOSED TO THE CTO: (1) "lake/hour tracks POST/hour" is given a rule: in every hour with 20 or more `POST /mcp` lines the lake holds at least half as many objects (the two read-backs read 1.8 objects per line, so the floor is generous and flags only a real lag). (2) A window that starts at :44:53 spans 25 hourly buckets; the check accepts 24 or 25. (3) The anomaly hour is explained by reading ALL its bodies for a tool or event histogram (counts only), about 2,900 reads, in a background script.
- Process-wide state (CVO verdict 35844): none (reads).
- Pre-cut: `AC1` base FAIL as expected (the record is absent). Synthetic arms fed to the check: a clean day reads `HOLDS` (PASS); 3 WARN lines read `FAILS_SEEN` (PASS); a busy hour where the lake lags reads `UNDETERMINED` (PASS); a verdict that contradicts the rule FAILS; a window under 24 hours FAILS; an anomaly hour with only 100 of 2896 bodies read FAILS; a wrong throttle constant FAILS.

<status>staged</status>
<round>46</round>
<workstream>ENRICH-R46-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
