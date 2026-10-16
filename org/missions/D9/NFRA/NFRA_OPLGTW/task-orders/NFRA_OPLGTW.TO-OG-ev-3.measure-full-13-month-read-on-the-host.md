# NFRA_OPLGTW task order -- `OG-ev-3` -- MEASURE: the full 13-month read of the 49F transactions and fees windows on the host, at concurrency 16 (round 40 W1; CTO ruling @0a15d90223)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-3</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only measurement; no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The reads run on the gateway host under the INSTALLED code and its dedicated role `gateway-49f-blackdiamond-live-read-role` (live from `OG-ap-29`), by one SSM command per run set; your own identity only dispatches the SSM command. A read denied is a STOP.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 ruling W1 (`ledger/ROUND_ANALYSIS.round38.md` update ~22:4xZ @0a15d90223: "measure first, on the host: read the full 13-month window with bounded concurrency (16) through the live role; record p50 and p95 wall time and the bytes read").
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ev-3` (decomposition addendum R3-T.102, round 40 cell W1, workstream ENRICH-R40-W1)

WHY. `client_get_transactions` and `client_get_fees` answer a 13-month window from the newest 60 daily files (334 and 395 are in the window), so a year's request gets about two months (`window_partial: true`). Before any code changes, the world must be measured: can the whole window be read inside the gateway's request budget? The public endpoint sits behind a 60 s ALB idle timeout; the ISSUER's reading of "inside the request budget" is a worst p95 wall time of 30 s or less over the two tables (half the timeout, so the auth and answer build keep headroom). The CTO reads that threshold at the round analysis.

DO (read-only; counts, seconds and bytes only; no client value printed, committed or messaged):
1. On the gateway host, in the gateway's own Python venv, through the installed adapter's read path (`app/client_adapter_bd49f.py`: the same `ctx.read_rows(prefix, part, columns=...)` call and the same column lists `get_transactions` and `get_fees` use), read EVERY dated partition inside a 13-month window ending at the newest partition, for `transactions` (expected about 334 files) and `fees` (about 395), with a `ThreadPoolExecutor(16)`. The rows are read and counted, never printed. One SSM command per table per repetition, or one for all, as you prefer; print the denominator (partitions listed) beside each result.
2. Repeat the full read of each table 5 times (a cold first run counts; do not discard it). Record each run's wall seconds, the p50 and p95 of the 5 walls per table, and the bytes read (sum of the objects' sizes, or the bytes the reader fetched, say which).
3. Write `W/WINDOW_MEASURE.json` (W = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`) = `{"body": {"read_at": "<iso>", "live_commit": "<deployed_commit at HEAD>", "concurrency": 16, "tables": {"transactions": {"partitions": N, "files_read": N, "wall_seconds": [5 numbers], "p50": x, "p95": y, "bytes": B}, "fees": {...}}, "request_budget": {"alb_idle_timeout_seconds": 60, "inside_threshold_seconds": 30, "verdict": "inside|outside"}}}`. `verdict` is `inside` if and only if the worst p95 of the two tables is 30 or less. `files_read` must equal `partitions` (the whole window, not a sample). Numbers and the fixed words only: no key, no account id, no amount; no digit run of 9 or more; no e-mail.
4. Run `ev3.AC1`, write the proof instance, flip the status, REPORT once: the two p50/p95 pairs, the bytes, the verdict, and any surprise (a throttle, a slow cold run, an S3 error rate, memory growth on the host). Note the host's CPU and the gateway's memory before and after (names and percentages only), because the real change would run the reads inside a live request.

## 2. BOUNDS

- Read-only: no write to any bucket or table, no deploy, no code change, no IAM change, no change to the gateway's service. 5 repetitions per table and no more; do not loop. A read denied or a partition missing is a STOP and a BLOCKING row. Be aware the measurement shares the host with live traffic: if the host shows memory pressure (above 85 percent) stop and report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print or commit a client value, an account id, an amount or a name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ev3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)transactions: partitions \d+, files read \d+, runs [1-9], p50 \S+ s, p95 \S+ s, bytes \d+.*fees: partitions \d+, files read \d+, runs [1-9], p50 \S+ s, p95 \S+ s, bytes \d+.*budget: ALB idle timeout 60 s, threshold 30 s, worst p95 \S+ s, verdict (\w+) \(rule says \1\); concurrency 16 \(want 16\).*content hygiene: long digit runs 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record is complete and self-consistent: the whole window of each table was read at concurrency 16, five runs each, p50 at or below p95, the verdict follows the stated rule from the recorded p95s, and nothing but numbers and fixed words is in it.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-3.measure-full-13-month-read-on-the-host.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once. Tell the issuer the verdict word and the two p95s: the code cell `OG-en-17` is spawned on them.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-W1 (decomposition addendum R3-T.102). Risk SERVED (a read of served client data; numbers only). Third order to `0.7.0_AE_CloudOps~NFRA1` of the day; the lane is idle after the `OG-ap-31` bodies.
- The 30 s threshold is the issuer's reading of "inside the gateway's request budget" (half the 60 s ALB idle timeout); the CTO may move it. The CTO's rule: inside, raise the cap and read concurrently; outside, a continuation cursor; never a silent truncation, never a monthly source, never narrowing up front.
- Pre-cut: `ev3.AC1` base FAIL as expected (record absent); PASS arms on synthetic records (inside p95 12 s; outside p95 41 s); controls FAIL (a verdict contradicting its p95; 60 of 334 files read; concurrency 8; 3 runs; p95 below p50).

- A1 (issuer, 2026-10-16 ~23:3xZ, `~NFRA1`'s OG-ev-3 report and rows Z-S327 and Z-S328): the measurement read OUTSIDE by a wide margin (transactions: one complete full-window run of 239.9 s, 334 of 334 files, about 318 MB; fees: 396 of 396 files, five runs of 145.7 to 147.2 s, p95 147.2 s; threshold 30 s). The applier stopped further transactions runs at its own 80 percent memory guard (81.6 percent at 190 files, no swap), which is the right call on a shared host, and `ev3.AC1` as first written refused the record for two defects of MINE: it demanded five runs of every table (a further run could not change an outside verdict when the fastest run is 8 times the threshold), and its digit-run limb counted the legitimate nine-digit `bytes` integer as a leak. `ev3.AC1` is corrected, with the evidence: fewer than five runs (at least one) are accepted ONLY when the verdict is `outside` and the fastest recorded run is above 30 s; integer `bytes` values are excluded from the digit-run scan. Dry-run: the amended check passes the real record, and its controls (one run with the fastest below 30 s; an inside verdict on three runs; a nine-digit run outside `bytes`) fail. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-W1</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
