# ADVI_BDPRCE task order -- `BP-b-4` -- THE TRACE INSTRUMENT READS WHAT THE SERVED LOT READS (WITH A NEGATIVE ARM)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~8</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a new read-only script; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the script reads S3 (`get_object`, `list_objects_v2`, `list_object_versions` through boto3). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the script and the probe do not exist (AC1, AC2 FAIL); AC2's grader rejects a trace that does not follow the served value and a followed source off {canonical, daily} (33-arm self-test OK). Blindness: AC2 proves shape and that the followed value equals the served one, not that the recompute is right; AC1's arms prove the logic on planted frames.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-4` (round 2; a new read-only instrument, a v2 of round 1's)

Round 1's instrument `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py` (read it and its `TRACE_README.md`) takes the DAILY price row on a same-date tie, while the served lot
reads the CANONICAL row, so on such an asset it reports a false mismatch (round-1 row `ADVI_BDPRCE-D1-W4-S6`; the proof of it is `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/trace_canonical_only.py`
and `TRACE_2026-10-09.json`-style outputs in that folder). A trace that does not follow what is served cannot answer "where did this price come from?". You build v2, which follows the served row.

### 1a. What the served lot reads

- A served lot (`entities/clients/<key>/detail.json`, `tax.open_lots[]`, fields `asset_name`, `current_price`) was priced by `data/black_diamond/scripts/gold/B_01.holdings_lots.py:319-361` (`load_latest_prices`):
  it reads every `silver/prices/*.parquet` (the daily files AND `canonical_prices.parquet`), concatenates, sorts by `date` descending (unstable) and keeps the first row per `asset_name`.
  A same-date tie between a daily row and the canonical row is therefore settled by sort order, not by rank.
- So "what the served lot reads" is not decided by a rule the instrument can assume: it is decided by comparing the lot's own `current_price` with the candidate rows.

### 1b. The instrument: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/trace_price_v2.py` (stdlib, pandas, pyarrow, boto3 only)

```
python trace_price_v2.py --asset "<asset_name>" --date YYYY-MM-DD --served-price <value> [--bucket opal-data-bd] [--out <file.json>]
python trace_price_v2.py --lot-object <bucket>/<key>@<VersionId> --asset "<asset_name>" [--out <file.json>]
python trace_price_v2.py --self-test
```
Behavior: gather the candidate rows for the (asset, date): the row in `silver/prices/<date>.parquet` and the row in `canonical_prices.parquet`. The FOLLOWED row is the candidate whose `price` equals the served price
(within `1e-6 * max(1, |served|)`); if both equal it, follow canonical and say both; if neither equals it, report `follows_served: false` and say so (never pick one silently). Then trace the followed row exactly as
round 1's instrument does for its source (rule by `source`, trade ids from the day's `silver/transactions/<date>.parquet` for `transaction_observed`, recompute, match). Output keys (all required):
`asset_name`, `date`, `served_price`, `followed_source` (`canonical` or `daily`), `followed_price`, `follows_served` (boolean), `rule`, `trade_ids` (list), `recomputed_price`, `match` (boolean),
`daily_row` and `canonical_row` (each `{price, source, version_id}` or null), `claim` (`measured`).
Reuse round 1's functions by import or copy; do not weaken them. The instrument keeps today's rule as its recompute (the "as built" rule), and adds a field `r1_price` only if
`data/black_diamond/scripts/silver/bd_price_rule.py` exists in your tree (it is built by a parallel cell and may be absent; never block on it).

`--self-test` runs offline on planted frames and prints one last line `TRACE2 SELFTEST: OK <n> arms` (exit 0), at least: (1) daily and canonical both present and equal -> follows canonical, `follows_served` true;
(2) **negative arm:** daily 162.155 `carry_forward` and canonical 168.94 `transaction_observed`, served 168.94 -> `followed_source` canonical, the daily row is reported but not followed, `follows_served` true;
(3) the same frames with served 162.155 -> `followed_source` daily; (4) served matches neither -> `follows_served` false; (5) a repeated `transaction_id` is listed with repeats kept, as in round 1. Any failing arm prints `TRACE2 SELFTEST: FAIL <arm>`, exit 1.

### 1c. The probe: `.../deliverables/0.9.0_WK_ADVI_BDPRCE~8/TRACE2_PROBE.json`

Against the real objects: asset `EXXONMOBIL HOLDINGS CORP COM SHS`, date 2026-10-09, served price 168.94 (the round-1 thread lot: object
`opal-data-49financial/advi/49financial/platinum/entities/clients/z08334146/detail.json`, VersionId `ZCjWpzPR1n2uZl849onevhS.pIvSQhVA`; confirm the served price by reading the object). Expected: followed canonical,
daily row 162.155 reported, `trade_ids` of length at least 1, `match` true, with NO helper script. Also write `TRACE2_README.md` (half a page: how to run it, what it does not do).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited; the script writes only the `--out` file. Downloaded files go to `C:/dev/wk-bdprce-r2-8-data/` (outside the checkout).
2. No client name, account number or advisor name is printed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-4 instrument needs the key listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/ADVI_BDPRCE.TO-BP-b-4.trace-follows-served.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-4"><invocation>cd /c/dev/wk-bdprce-r2-8 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/trace_price_v2.py --self-test</invocation><expect>^TRACE2 SELFTEST: OK [0-9]+ arms$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-4"><invocation>cd /c/dev/wk-bdprce-r2-8 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py trace2 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/TRACE2_PROBE.json</invocation><expect>^TRACE2 record ok followed=canonical trades=[1-9][0-9]* match=true follows_served=true$</expect></criterion>
  <criterion id="AC3" cell_refs="BP-b-4"><invocation>cd /c/dev/wk-bdprce-r2-8 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-8 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (five planted arms, the negative arm among them); AC2 is the seam probe against the real served lot; AC3 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged).

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `trace_price_v2.py`, `TRACE2_PROBE.json` and `TRACE2_README.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W8-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the probe asset, date, served price, followed source, daily value, trade count, match; AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 4; closes `W4-S6`. FWD-3's grade (DEC-10) must trace what is served. Class LOCAL: a new script under `deliverables/`, reads only.

<status>pending</status>
<round>2</round>
<workstream>TRACE2</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-4</to_id>
<slot>~8</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
