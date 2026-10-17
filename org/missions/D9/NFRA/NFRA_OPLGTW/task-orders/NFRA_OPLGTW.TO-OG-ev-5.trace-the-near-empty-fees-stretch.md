# NFRA_OPLGTW task order -- `OG-ev-5` -- TRACE (read only): is the near-empty fees stretch the source or the account? (round 41; CTO round-40 analysis item 4; row Z-S355)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-5</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only trace; no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The reads run on the gateway host in a scratch process under the dedicated role `gateway-49f-blackdiamond-live-read-role`, dispatched by SSM, as in `OG-ev-4`; a read denied is a STOP.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 analysis item 4 (`ledger/ROUND_ANALYSIS.round40.md` @66aeb73b0c: "a read-only trace of the near-empty fees stretch: whether the source or the account is the cause, before any tool change; no write, and no tool change in this round") on the CVO's row Z-S355 (one fees source stretch near-empty, 109 rows over 30 days).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ev-5` (decomposition addendum R3-T.111, round 41, workstream ENRICH-R41)

WHY. The CVO's chain on the live release read the test account's fees as 12 rows over 14 pages, with one stretch of about 30 days holding 109 rows (row `Z-S355`, `adjudications/ADJUDICATION_v40.Z.md`). Before anyone changes a tool, the world must say whether the SOURCE table is thin there (a producer gap) or the ACCOUNT simply has few fees there (nothing wrong).

DO (read only; counts, dates and fixed words only; never print, commit or message a client value, an account id, an amount or a name):
1. On the gateway host, in a scratch process under the gateway role through the installed adapter's read path (`ctx.read_rows` over the served `fees` prefix, the same column list `get_fees` uses; the code of release `9d5b712557` is live), read the fees partitions of the 13-month window and, for each dated partition, count (a) ALL rows of the partition and (b) the rows of the one test account you used for the `OG-ap-34` chains (resolve it in-process; never print it). Use the page-sized reads you already know are safe (one call at a time; stop at 75 percent host used; the whole window is 14 pages of about 30 partitions).
2. Identify the STRETCH: the 30 or more consecutive dates over which the test account's fee rows are fewest relative to the rest of the window (the CVO's stretch holds 109 rows over 30 days; use that stretch if your counts agree, and say so).
3. Write `W/FEES_TRACE.json` (`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`) = `{"body": {"read_at": "<iso>", "window": {"from": "<date>", "to": "<date>"}, "stretch": {"from": "<date>", "to": "<date>", "days": N}, "source": {"rows_in_stretch": n, "median_rows_per_day_outside": m, "partitions_in_stretch": k, "partitions_expected_in_stretch": k2}, "account": {"rows_in_stretch": n, "median_rows_per_day_outside": m}, "verdict": "source|account|neither|not_determined"}}`. `rows_in_stretch` is the sum over the stretch's dates; `median_rows_per_day_outside` is the median of the per-date counts OUTSIDE the stretch; `partitions_expected_in_stretch` is the number of trading days in the stretch by `lib/trading_calendar.py`. The verdict follows the rule in `ev5.AC1`: a table is near-empty when its stretch rows are below 25 percent of (its median per day outside x the stretch's days); `source` if the source is near-empty, else `account` if the account is, else `neither`; `not_determined` only when a median outside is 0.
4. Run `ev5.AC1`, write the proof instance, flip the status, REPORT once: the verdict, the two ratios, the missing partitions if any, and any surprise.

## 2. BOUNDS

- Read only: no write to any bucket or table, no deploy, no code change, no IAM change, no change to the gateway's service. One pass per table; stop at 75 percent host used. A read denied is a STOP and a BLOCKING row. No tool change in this round (the CTO's rule).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print or commit a client value, an account id, an amount or a name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ev5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)stretch: \d+ days \(want 30 or more\); source rows \d+, account rows \d+; partitions in the stretch (\d+) of \1 expected.*verdict (\w+) \(rule says \2\).*content hygiene: long digit runs 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record is complete and self-consistent: a stretch of 30 days or more, the source's partitions in it equal the expected, the verdict follows the stated 25 percent rule from the counts, and nothing but counts, dates and fixed words is in it.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-5.trace-the-near-empty-fees-stretch.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41 (decomposition addendum R3-T.111), cell 4 of the CTO's round-40 analysis. Risk SERVED (a read of served data; counts only). No tool change in this round whatever the verdict.
- The 25 percent line is the issuer's reading of "near-empty"; the numbers, not the verdict word, are the evidence, and the CTO reads the verdict at the round analysis.
- Pre-cut: `ev5.AC1` base FAIL as expected (record absent); PASS arms on synthetic records (account near-empty; source near-empty; neither; not_determined); controls FAIL (a verdict contradicting the counts three ways; a 20-day stretch; a missing partition; an e-mail in the record).

<status>complete</status>
<round>41</round>
<workstream>ENRICH-R41</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
