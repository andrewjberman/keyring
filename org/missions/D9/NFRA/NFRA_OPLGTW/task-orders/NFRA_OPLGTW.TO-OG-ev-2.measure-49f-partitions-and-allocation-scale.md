# NFRA_OPLGTW task order -- `OG-ev-2` -- MEASURE: are the 49F live transactions and fees partitions daily INCREMENTS or cumulative SNAPSHOTS, and is the live allocation weight a FRACTION or a PERCENT (round 39 E1 and E2; CVO v35 AC3 findings 5 and 1; PRD v3.6 item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-2</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only measurement; no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. You read `opal-data-bd/silver/{transactions,fees,allocations}/` under your OWN audited identity; the gateway roles are not used. If your identity is denied a read, STOP and report: do not widen anything.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-38 analysis (`ledger/ROUND_ANALYSIS.round38.md` @faa77bd49e, E1: "measure increment vs snapshot on the live tables before any tool spans dates") and the CVO's v35 finding that the allocation weights carry no unit.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ev-2` (decomposition addendum R3-T.99, round 39 cells E1 and E2, workstream ENRICH-R39-B)

WHY. The 49F live tools `client_get_transactions` and `client_get_fees` answer a 13-month window from ONE daily partition (`window_partial: true`), and the allocation weights carry no unit. Before any code spans partitions or names a unit, the world must be measured: if each daily partition holds only that day's new rows (INCREMENTS), the answer must read every partition in the window; if each holds the whole history to date (SNAPSHOTS), the newest partition already answers the window. For the allocation weights, whether a weight of 0.5 means half or half a percent is not stated anywhere in the repo.

DO (read-only; counts only; client data NEVER printed, committed or messaged):
1. **Partitions.** For each of `transactions` and `fees` under `s3://opal-data-bd/silver/<table>/` (flat dated files `<YYYY-MM-DD>.parquet`; list the prefix with the pagination counted client-side, print the denominator): count the partitions and record the first and last date. Take the NEWEST 6 partitions, the 5 consecutive pairs (A older, B newer). For each pair read only the natural key column (`transaction_id` for transactions; for fees name the column that identifies one fee row, by NAME) and compute `overlap = |keys(A) AND keys(B)| / |keys(B)|` (0 when B is empty). Record the overlap list (5 numbers, or fewer if fewer partitions exist; at least 3 pairs are required), and classify on the MEDIAN overlap: `<= 0.05` is `increment`, `>= 0.9` is `snapshot`, anything between is `mixed`.
2. **Allocation scale.** In the newest `silver/allocations/` partition, group by account (read the account id column and `account_allocation` and `cash_allocation` only), sum `account_allocation + cash_allocation` per account in memory, and count the accounts whose sum is within 0.05 of 1 (`near_1`), within 5 of 100 (`near_100`) or neither (`other`). `weight_scale` is `fraction` if `near_1` exceeds `near_100 + other`, `percent` if `near_100` exceeds `near_1 + other`, else `unclear`. At least 20 accounts must be sampled (all accounts if fewer than 20 exist: say so).
3. Write `W/E1_PARTITION_MEASURE.json` (W = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`) = `{"body": {"read_at": "<iso>", "live_commit": "<deployed_commit at HEAD>", "tables": {"transactions": {"partitions": N, "first": "<date>", "last": "<date>", "key_column": "<column name>", "pairs_checked": k, "overlap_ratios": [..], "classification": "increment|snapshot|mixed"}, "fees": {...same...}}, "allocations": {"accounts_sampled": n, "scale_counts": {"near_1": a, "near_100": b, "other": c}, "weight_scale": "fraction|percent|unclear"}}}`. Numbers and the fixed words only: no key value, no account id, no amount, no name; no digit run of 9 or more; no e-mail.
4. Run `ev2.AC1`, write the proof instance, flip the status, REPORT once: the two classifications, the scale, and any surprise (for example a partition that is empty, a missing key column, or ratios in the `mixed` band).

## 2. BOUNDS

- Read-only: no write to any bucket or table, no deploy, no code change, no IAM change. One read pass; do not loop. A read denied or a table missing is a STOP and a BLOCKING row, not a workaround.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print or commit a client key value, an account id, an amount or a name; send client data in any message.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` as above (the tree convention grants it; it needs no entry). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ev2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)transactions: partitions \d+, pairs checked [3-9]\d*, median overlap \S+, classification (\w+) \(rule says \1\).*fees: partitions \d+, pairs checked [3-9]\d*, median overlap \S+, classification (\w+) \(rule says \2\).*allocations: accounts sampled (?:[2-9]\d|[1-9]\d{2,}); near_1 \d+, near_100 \d+, other \d+; weight_scale (\w+) \(rule says \3\).*content hygiene: long digit runs 0 \(want 0\); e-mail addresses 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record is complete and self-consistent: both table classifications and the allocation scale follow their stated rules from the recorded numbers, and nothing but counts, ratios and the fixed words is in it.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-2.measure-49f-partitions-and-allocation-scale.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSes, and report once. Tell the issuer the three words (the two classifications and the scale): the code cells `OG-en-13` and `OG-en-15` are cut on them.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39, workstream ENRICH-R39-B (decomposition addendum R3-T.99). Second order to `0.7.0_AE_CloudOps~NFRA1` this tick; it can run beside `OG-ap-30` Phase A (read-only, different table), but `OG-ap-30` goes first if the lane has one keyboard.
- Risk SERVED (a read of served client data; counts only).
- Pre-cut: `ev2.AC1` base FAIL as expected (record absent); PASS arms on a synthetic record (increment plus fraction; snapshot plus percent); controls FAIL (a classification that contradicts its ratios; a scale that contradicts its counts; a 12-digit run; too few accounts sampled).

<status>staged</status>
<round>39</round>
<workstream>ENRICH-R39-B</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
