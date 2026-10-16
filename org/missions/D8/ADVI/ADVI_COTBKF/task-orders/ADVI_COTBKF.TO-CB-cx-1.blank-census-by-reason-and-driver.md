# TO ADVI_COTBKF.TO-CB-cx-1.blank-census-by-reason-and-driver -- round 102 CB-cx-1: count the blank days and months of the served FWD-3 tables by reason, prove no blank lacks a reason, and name each reason's driver (above all UNPRICED) so the CTO can tell whether Bloomberg history would fill it; read-only, counts only

<to_id>ADVI_COTBKF.TO-CB-cx-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~191</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>102</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cx-1` (`decompositions/ADVI_COTBKF_DECOMP.round102.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** FWD-3 says: an analyst reads each Cottonwood account's return for any single day, and "a day that cannot be worked out says so and is never filled in". On the served tables 1,584,413 of 1,691,729 days carry no return (93.7%), and 78,622 of 82,593 months are UNGRADABLE. The CTO needs to know, for every blank, WHY it is blank (each blank must carry a reason) and what DRIVES each reason, so that it is clear whether Bloomberg history would fill it. You count, prove, and name drivers. **You read; you write nothing to S3, serve nothing, change no code, fill no blank and grade nothing (the CTO grades).**

**Inputs (READ-ONLY).** The served objects at the pinned VersionIds, one `get_object` each: `daily_returns` at `lNzQMjfx6uX2zdFdWKsDANboShtDUz2N`, `month_grades` at `nkTE.F82uFSboXr9PEamIENCwFL9cwcC`, `account_day_value` at `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a` (all `s3://opal-data-assets/commonwealth/cottonwood/silver/<table>/date=2026-06-23/part-00000.parquet`). Local run data already on this box (off git, gitignored; read-only; do not list or describe it beyond counts): the price stores' cache from round 99 at `C:/Dev/ajb_workspace/.scratch/cotbkf_r99/store_cache`, the transactions cache at `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache` (read with `dh.load_tx_pos` / `dv.universe_from_tx` for each security's `asset_type` and `symbols`), and the round-97 regrade's `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade/after/security_day_price.parquet`. Your worktree has no `.scratch`: pass absolute paths. The private sweeps config is not needed; do not look for it.

**Read first.** (1) The issuer's script `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cx1_blank_census.py` (in your worktree; read it, do not edit it): it prints the census your record must equal. (2) The reason codes and where code sets them: grep (native Grep) `data/assets/scripts/silver/commonwealth_daily_returns.py` (`UNPRICED`, `FIRST_DAY`, `NON_POSITIVE_BASE`, `FLOW_UNVALUED`), `data/assets/scripts/silver/commonwealth_daily_valuation.py` (`DVR_CLOSE_STEP`) and `data/assets/scripts/silver/commonwealth_fwd3_serve.py` (`HELD_SOURCE_UNDER_REVIEW`, `REGRESSED_UNDER_AS_TRADED`); for months, `data/assets/scripts/silver/commonwealth_monthly_grade.py` (`UNGRADABLE`, `DIFF`, its `reason` texts) and the builder's ABSENT rule. (3) Bloomberg: the project `org/missions/D8/MDPF/MDPF_DEMQUE/` holds the backfill queue's records for Cottonwood's requests; find, with Grep, whether a committed record lists the CUSIPs requested for Cottonwood and what came back; name it by path.

**Your items.**

1. **The census.** Run the issuer's script (no argument; about 12 seconds): `python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cx1_blank_census.py`. Record its three lines' numbers exactly as the record keys `days`, `months`, `unreasoned` and `unpriced` below. State in the record the CTO's criterion as met or not: the number of blank days with no reason, and of non-MATCH months with no reason (the script's `unreasoned`). If any is above 0, LIST those rows by counts per month or day-band (never an account id) and say so in `not_established`.
2. **The driver of each reason code.** For every reason code of the days (UNPRICED, NON_POSITIVE_BASE, FIRST_DAY, DVR_CLOSE_STEP, HELD_SOURCE_UNDER_REVIEW, REGRESSED_UNDER_AS_TRADED, FLOW_UNVALUED) and every month category (UNGRADABLE with its reason texts grouped by kind, DIFF, ABSENT, and the MATCH months for completeness), give: the number of days or months; `rule` = the code that sets it (file, line, one sentence of what the rule says, quoted from the code); `driver` = what in the data or the method makes the rule fire; and `bloomberg_fill` = one of `yes` (the driver is a missing price or missing history that a vendor history of the security's price would supply), `no` (the blank is a property of the method or the account: a first day has no prior value, a non-positive base, a held row under review, a regression recorded by design), or `not_established`, with `why` in one line. Do not claim `yes` without naming what would be fetched (for example "the daily close of the security on the unpriced days").
3. **UNPRICED, decomposed.** The 15,973,399 unpriced holding-days of `account_day_value` (close null and blank_reason null) over 4,371 securities: (a) split into NEVER-PRICED securities (no row of the table carries a close for it: 3,791) and GAP securities (580); for each group give securities and holding-days. (b) For the never-priced securities: counts by `asset_type` (from the universe), and the split into securities with no ticker symbol at all, securities with a ticker the price stores hold no row for, and securities with a ticker whose store rows exist but whose key is claimed by more than one security (`pc.symbol_claims`) or whose security-days were dropped as conflicting inside the winning store; counts only. (c) For the gap securities: split their unpriced holding-days into BEFORE the security's first priced day, AFTER its last priced day, and INTERIOR (between two priced days); rows and securities each. (d) Overlap with Bloomberg: the number of never-priced and gap securities that appear in the committed Bloomberg request record for Cottonwood found in item (3) above, and how many of those came back priced, if the record says; if no committed record carries the list, say `not_established` and name what record would. Never print a cusip, ticker, account or value.
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~191/BLANK_CENSUS_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `served` (`{"daily_returns_version","month_grades_version","account_day_value_version"}`), `days` (`{"total","with_return","blank","unreasoned","by_reason":{reason:count}}`), `months` (`{"total","not_match","unreasoned","by_verdict":{verdict:count}}`), `unreasoned` (`{"days","months"}`), `unpriced` (`{"rows","cusips","never_priced_cusips","never_priced_rows","gap_cusips","gap_rows"}`), `drivers` (one object per reason code and month category: `{"kind","code","count","rule":{"file","line","text"},"driver","bloomberg_fill","why"}`), `unpriced_breakdown` (items 3a to 3d as counts), `what_this_shows` (three sentences in counts: how many blanks have a reason, what drives most of them, what a vendor history could and could not fill), `not_established`; and a short `.md` beside it. `days`, `months`, `unreasoned` and `unpriced` must equal the issuer's script exactly. No account id, cusip, ticker, name or dollar value in either file.

### ACCEPTANCE

<criterion id="CB102cx1-AC1" cell_refs="CB-cx-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~191/BLANK_CENSUS_RECORD.json',encoding='utf-8'));m=d['measured'];print('BLANK-CENSUS measured=%s' % m + ((' days_blank=%d unreasoned_days=%d unreasoned_months=%d reasons=%d unpriced_cusips=%d' % (d['days']['blank'],d['unreasoned']['days'],d['unreasoned']['months'],len(d['days']['by_reason']),d['unpriced']['cusips'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^BLANK-CENSUS measured=(True days_blank=\d+ unreasoned_days=\d+ unreasoned_months=\d+ reasons=\d+ unpriced_cusips=\d+|False reason=.+)$</expect></criterion>
`CB102cx1-AC1` -- the record states the blank days, how many lack a reason (days and months), how many reason codes there are and how many securities are unpriced, or states plainly why nothing could be measured.

<criterion id="CB102cx1-AC2" cell_refs="CB-cx-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cx1_blank_census.py org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~191/BLANK_CENSUS_RECORD.json</invocation><expect>^CENSUS-CROSS days_equal=True months_equal=True unreasoned_equal=True unpriced_equal=True$</expect></criterion>
`CB102cx1-AC2` -- the issuer's script recomputes the census from the served objects and the record equals it on the days, the months, the unreasoned counts and the unpriced partition.

<criterion id="CB102cx1-AC3" cell_refs="CB-cx-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py</invocation><expect>^SERVED-UNCHANGED versions_equal=3 of 3$</expect></criterion>
`CB102cx1-AC3` -- the cell wrote nothing: the three served keys still carry the VersionIds the round-98 apply left (the issuer's script reads object metadata only).

<expected_criteria>CB102cx1-AC1,CB102cx1-AC2,CB102cx1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder, your own NEW channel row, and this order's own file (for the one `<status>` flip). You change no code, test or other committed file. Scratch stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r102/` (gitignored, never committed); the read script you write may be committed in your deliverables folder as evidence. Your instance rows for artifacts that already exist in a commit must be pinned to that commit's FULL hash (never `PENDING-THIS-COMMIT` for a file an earlier commit carried).
- **AWS: READ-ONLY** (`get_object` of the three served objects at the pinned VersionIds, `head_object` for AC3); no write, no `--apply`, no vendor call, no Bloomberg call, no Yahoo call. You do not contact Cottonwood or Commonwealth.
- **No account id, cusip, ticker, name or dollar value** in the record, the report or any message; the committed Bloomberg request record may hold identifiers: read it for counts and never copy one.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never fill, estimate or "repair" a blank; never grade FWD-3 yourself.
- **Timing.** The census script and the three reads take seconds; the decomposition of 16 million holding-days takes minutes: run anything over 100 seconds in the background under `timeout 2400` and read its log.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W191-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only. A difference between your counts and the issuer's script is a finding to report, not to adjust: AC2 then reads False and you stop.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cx-1.blank-census-by-reason-and-driver.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one write to this order is the `<status>` flip.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round102.md</decomp_doc> (round 102), cell `CB-cx-1`.
<owned_cells>CB-cx-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB102cx1-AC1, CB102cx1-AC2, CB102cx1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~191/ADVI_COTBKF.TO-CB-cx-1.blank-census-by-reason-and-driver.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB102cx1-AC1,CB102cx1-AC2,CB102cx1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the order file is in your `<paths>` for this flip).
</proof_of_spec>

**REPORT:** FIRST the `BLANK-CENSUS` line. Then: the census by reason (days and months); the unreasoned counts; per reason code its rule, driver and whether a vendor history would fill it; the UNPRICED decomposition (never priced vs gap, asset type, symbol, gap position, the Bloomberg overlap or why it is not established); what the data shows in three sentences; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account id, cusip, ticker or value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of three served objects and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE get_object of three objects at pinned versions under the existing role; no new permission.
comp-adversary: RUN -- the headline census and the unpriced partition are recomputed by an issuer script from the same served objects and the record must equal it (AC2); BLIND: the issuer's script and the worker read the same objects, so a defect in the served tables is not tested; the `driver` and `bloomberg_fill` entries are the worker's reading of the code and of committed records and are not mechanically graded (the issuer spot-reads them against the cited lines before they go on), and `bloomberg_fill: yes` is a claim about a vendor's coverage that no record here can prove.
lane: the <paths> block IS the grant (worker RULING 1), and names the order file for the status flip.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6622 (ROUND_ANALYSIS.round101). The CTO's criterion (blank with no reason = 0, or listed) already holds on the served tables by the issuer's count; the cell proves it again as a recorded count and adds the drivers. Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL as expected; AC3 PASSES (served versions unchanged).
