# NFRA_OPLGTW task order -- `OG-ev-10` -- MEASURE: is the per-identity refusal's audit write failing? (round 44; row `Z-W155-S1`, ARMED; round-43 analysis item 1; plus the CTO's `OG-ev-7` CT3 service limb)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-10</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-10</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform, no SSM write. Every AWS and host call in STEP 1 is a read-only `get`/`list`/`describe`/`journalctl`.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-43 analysis (item 1): "read the in-process refusal counter if the running service exposes it; if not, ONE controlled identity refusal with a test principal against the existing limiter (no code or config change), then read the lake for its row within 2 minutes".
EGRESS CLASS, declared: Opal's own AWS and the gateway host only. STEP 2 (only if STEP 1 cannot decide) makes at most the number of requests its ask names to the gateway's own /mcp endpoint with a test principal.
</preflight>

## 1. THE CELL -- `OG-ev-10` (decomposition addendum R3-T.121, round 44, workstream ENRICH-R44-A)

WHY. `ratelimit.record_identity_refusal` (`infra/aws/ec2/opal-gateway/app/ratelimit.py`, lines 218 to 248) writes ONE `gw_ratelimit` audit row per identity per 10 seconds on a per-identity 429, and SWALLOWS every failure of that write: it adds 1 to a module counter (`audit_failure_count()`, line 202) and prints one line to stderr, `SCTY_PREMCP ratelimit-audit WARN: refusal row not recorded (<error>) -- the 429 is unchanged`. `OG-ev-9` (round 43) found ONE `gw_ratelimit` row in the lake in 24 hours (2026-10-17T17:21:43Z) and none for a per-identity 429 that this seat's own gateway connection received on 2026-10-18 (row `Z-W155-S1`, ARMED). The counter `audit_failure_count()` has no caller outside `tests/test_og_en10.py` (the issuer's grep at the cut), so no route reads it. Since the `OG-ap-44` deploy (ledger `batch11` CLOSED 2026-10-18T20:01:40Z) the service's own access log is back, so a `POST /mcp` answered 429 now leaves a journal line. YOU DECIDE which of three verdicts is true, by a rule fixed here, and change NOTHING in the product.

THE VERDICT RULE, fixed before you run anything (the check `ev10.AC1.sh` recomputes it from your numbers; read its header first), in this order:
- `FAILS` if the journal holds one or more lines containing `ratelimit-audit WARN: refusal row not recorded`;
- `FAILS` else if a controlled refusal was seen and no `gw_ratelimit` lake row followed within 120 seconds;
- `FAILS` else if the journal holds one or more `POST /mcp` lines answered 429 and the lake holds 0 `gw_ratelimit` rows for the window;
- `WRITES` else if the journal holds 429 lines and the lake holds one or more rows, or a controlled refusal was seen with its lake row within 120 seconds;
- `NOT_EXPOSED` otherwise (no refusal was observed and no route exposes the counter).

### STEP 1 (on the issuer's GO; READ-ONLY; no ask, no halves)

Write `W/AUDIT_REFUSAL_WRITE.json` (exact shape in the header of `ev10.AC1.sh`), `controlled_refusal` `null`:
1. THE JOURNAL. On the host, from `journalctl -u <the gateway unit>` over the whole retained window since the first access line after the `OG-ap-44` restart (read the first `POST /mcp` access line's timestamp into `first_access_line_ts`; `last_line_ts` is the last line you read): count the access lines for `POST /mcp` answered 429 (`post_mcp_429_lines`, an integer), and the lines containing `ratelimit-audit WARN: refusal row not recorded` (`ratelimit_audit_warn_lines`). Put the exact command in `source`. Print no log line that carries an address or an identity; counts only.
2. THE LAKE. In the audit lake (S3 bucket `opal-mcp-audit`, keys `audit/dt=<YYYY-MM-DD>/<ts>-<id>.jsonl`, one record per object), over the same window (`window_start` = `first_access_line_ts`, `window_end` = now), count the records whose `event` is `gw_ratelimit` (`gw_ratelimit_rows`) and the objects listed (`denominator`, must be above 0; `read_errors` must be 0). READ-ONLY, counts only, and never print a principal.
3. THE COUNTER. Read `infra/aws/ec2/opal-gateway/app/` for any route, health answer or status page that returns `audit_failure_count()`; record `counter_exposed` (true or false) and `counter_evidence` (file:line strings, or the grep you ran and its empty answer).
4. THE `OG-ev-7` SERVICE LIMB (the CTO's CT3 limb). `W/PEERS_MEASURE.json` (your own record of `OG-ev-7`) gives the lake window 21:08:03Z to 21:08:59Z on 2026-10-18 with 15 objects, of which 3 are labelled `probe:OG-ev-7` and 2 `probe:unarmed`. In the same lake read, for the OTHER 10 records of that window print, as counts only, the pairs (label, tool or event name) with their numbers: `ev7_unlabelled` = `{"window_start": "2026-10-18T21:08:03Z", "window_end": "2026-10-18T21:08:59Z", "records": 10, "pairs": [{"label": "<label or none>", "tool": "<tool or event name>", "n": n}], "source": "<how read>"}`; the pair numbers sum to `records`. (The CTO's question: journal `POST /mcp` was 0 in that window while the lake held these 10 records not labelled probe. The access log was silent until the `OG-ap-44` deploy, so the answer is expected to be ordinary traffic; the pairs show it.)
5. `verdict` and a one-line `reason`, by the rule above.
If STEP 1 returns `FAILS` or `WRITES`, STOP there: commit, run AC1, report. If it returns `NOT_EXPOSED` (no 429 in the journal window), report that and WAIT for my reply; do NOT start STEP 2 on your own.

### STEP 2 (only if STEP 1 reads `NOT_EXPOSED`, and only on the issuer's GO that names THREE signed halves)

ONE controlled identity refusal with a TEST PRINCIPAL against the existing limiter (120 requests per 60 seconds per validated principal key): no code change, no config change, no environment change, no SSM write. First write the ask `W/NEVER_WIDEN_ASK_OG-ev-10.md` for three halves (each under a heading containing its word `CTO`, `COO`, `CVO`) and STOP for the halves: the `principal` (masked `****xxxx`; WHICH identity and how its bearer is obtained, never the token), the exact `requests` (121 to 130 within one 30-second span of the cheapest authenticated `/mcp` call, for example `tools/list`), the expected answer (the 121st and later requests answer 429, `rate_limited`, scope `identity`), the lake read (a `gw_ratelimit` row for the principal within 120 seconds), `process-wide state this change touches: none, read` (it sends requests only; you opened `ratelimit.py` and `server.py` to say so), `rollback` (none needed: the sliding window clears in 60 seconds and no state is written outside the audit lake), `triggers` (any 5xx on a request, host memory above 85 percent, `NRestarts` above 0, the principal receiving a 429 outside the planned span), and the gate lines. If no test principal exists that is not a real person's identity, write that in the ask and say `NOT_EXPOSED stands`; do NOT use a person's identity. After the halves and my GO: make the refusal ONCE, read the lake within 2 minutes, fill `controlled_refusal` = `{"principal_ref": "****xxxx", "requests_made": n, "refusals_seen": n, "lake_row_within_120s": true|false, "halves": "<path of the ask>"}`, recompute the verdict, commit, run AC1, report.

### AMENDMENT A1 (issuer, 2026-10-19 ~03:4xZ, on the CTO's ruling msg 35872 and your STEP 2 ask msg 35869): STEP 2 is the WRITER TEST (your option (b)), not the controlled refusal

Your finding stands: no non-person `/mcp` principal exists, so the controlled refusal cannot run. The CTO ruled (a) AND (b) IN, bounded: (a) you re-run `ev10_step1.py` read-only after real use whenever I ask; (b) ONE writer test, under three halves on its own ask `W/NEVER_WIDEN_ASK_OG-ev-10.md` (amend your ask to name these bounds and carry the three headed halves):
- ONE lake object only; the key is unmistakably synthetic (`key_label` contains `OG-ev-10`, no real principal) and the object's lake key is PRINTED in the record so any consumer can exclude it;
- a guarded fresh process on the host calls `ratelimit.record_identity_refusal` with the synthetic key under the SERVICE'S OWN INSTANCE ROLE (so the IAM of the put is tested too), `process-wide state this change touches: none, read` (it opens `ratelimit.py` and `audit.py`), no code, config or environment change;
- the object is READ BACK and NEVER DELETED (an audit-lake delete is not ours);
- the verdict rule gains two lines (`ev10.AC1.sh`, amended): `FAILS` if the writer test's object was not written or not read back; `WRITES` if it was written and read back. Record it as `writer_test` = `{"key_label", "lake_key", "written", "read_back", "instance_role": true, "halves"}` in `AUDIT_REFUSAL_WRITE.json`; `controlled_refusal` stays `null`.
After the halves and my GO, run it ONCE, record it, run AC1, validate the proof, report. The `<status>` flip stays mine.

## 2. BOUNDS

- Only `W/`, the ask, and the channel. No product file, no test, no release, no deploy, no S3 write (the lake is read only), no SSM write, no Terraform, no restart of the service.
- No principal, email address, account number, token or object content in any record (`****xxxx` form only; label and tool names are not identities).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; run gateway code on the host without the hard guard; use a person's identity as the test principal.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/ev10.AC1.sh; echo "exit=$?"</invocation><expect>(?s)journal: 429 lines \d+, writer WARN lines \d+ .*: ok; lake: gw_ratelimit rows \d+ over \d+ objects, read errors 0: ok.*verdict by the rule fixed before the run: (WRITES|FAILS|NOT_EXPOSED), the record says \1: consistent.*OG-ev-7 window records not labelled probe: 10 \(PEERS_MEASURE\.json gives 10\); pairs sum 10: ok; email-shaped strings 0 \(want 0\); digit runs of 9 or more 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the journal and lake counts are present and read without error, the verdict equals what the rule returns from those counts, the 10 records of `OG-ev-7`'s window not labelled probe are accounted for by (label, tool) pairs that sum to 10, and the record holds no email, no principal and no long digit run.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-10.round-44-is-the-audit-refusal-write-failing.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, and flip NOTHING (the `<status>` flip is mine). Report once per step: the commit hash, the journal 429 and WARN counts, the lake row count, the verdict, the 10 records' pairs in one line, and for STEP 2 the requests made, refusals seen and the lake row time.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 44, workstream ENRICH-R44-A, `<risk>SERVED</risk>` (the CTO's class). Source: the CTO's round-43 analysis (`ledger/ROUND_ANALYSIS.round43.md` @d35c913755, msg 35841), item 1, and section 1: "CT3's service limb is UNGRADED: over 21:08:03Z-21:08:59Z the lake holds 10 records not labelled probe, against journal `POST /mcp` 0. Carried as cell 1."
- READING DISCLOSED TO THE CTO: the refusal writer prints a WARN line to stderr on every failed write, so STEP 1 can decide `FAILS` from the journal without any refusal being made; and the restored access log lets an ORGANIC 429 be matched against the lake. Only if the retained journal holds no 429 does the controlled refusal of STEP 2 become necessary, and then under three halves.
- Process-wide state (CVO verdict 35844): STEP 1 touches none (reads). STEP 2 touches none (requests only), as its ask must say.
- Pre-cut: `AC1` base FAIL as expected (the record is absent). Synthetic arms: a `NOT_EXPOSED` record with a matching 10-record account passes; a wrong verdict, a record count of 9, and a `FAILS` record are each judged against the rule.

<status>staged</status>
<round>44</round>
<workstream>ENRICH-R44-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
