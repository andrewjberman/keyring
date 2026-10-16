# TO ADVI_COTBKF.TO-CB-cy-1.bloomberg-history-coverage -- round 103 CB-cy-1: find where returned Bloomberg price history lives for Cottonwood, count what is in it, and measure which of the 3,059 listed securities came back priced and how many of the 15,973,399 UNPRICED holding-days those closes cover; read-only, no Bloomberg call, counts only

<to_id>ADVI_COTBKF.TO-CB-cy-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~192</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cy-1` (`decompositions/ADVI_COTBKF_DECOMP.round103.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** 98.3% of the served daily returns that are blank are blank because a holding has no close price (UNPRICED): 15,973,399 holding-days over 4,371 securities, 3,791 of them never priced anywhere in the served table. A Bloomberg price history could fill them only if it covers those securities on those days. Cottonwood's Bloomberg history requests are listed in committed records (3,059 distinct securities: 2,354 never-priced and 515 gap-priced among them, per round 102), but no committed record says which of them came back priced. The CTO's question: "which of the 3,059 listed securities came back priced from Bloomberg history, and how many of the 15,973,399 UNPRICED holding-days those closes cover." If any, the next round rebuilds under a pair. You find where returned history lives, count what is there, and measure the coverage. **You read what is already in Opal's own store. You make NO Bloomberg call, pull nothing, write nothing to S3, serve nothing, change no code and fill no blank.**

**Read first.** (1) `integrations/bloomberg/READ_HERE.md` (the house rules for anything Bloomberg: a pull goes only through the queue and only on Andrew's word; you pull nothing). (2) Round 102's record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~191/BLANK_CENSUS_RECORD.json` (`unpriced_breakdown`, item (d): the committed request lists it counted and the note that `BBG_ACTUALS.jsonl` holds 5 job rows with cell counts only). (3) The projects that run the queue and the series: `org/missions/D8/MDPF/MDPF_DEMQUE/` (ledger, deliverables, round analyses) and `org/missions/D8/MDPF/MDPF_SECHIST/` (the series writer `data/mdpf/scripts/silver/security_series_writer.py`, `lib/opal_naming.py`'s `address()` for its home) and any record that names an S3 prefix where returned Bloomberg history lands. Use the native Grep and Glob tools, not `find`.

**Your items.**

1. **Find where it lives.** From those records, name every S3 location (bucket and prefix) where returned Bloomberg daily price history for Cottonwood securities could be, and for each, list the objects with the metadata-only `list_objects_v2` (count, total bytes; never read a body in this step). Include the series writer's home (the SECHIST `security_series` prefix, built with `opal_naming.address()`), the queue's results prefix if a record names one, and any prefix named `bloomberg`/`bbg` in the records. For each location: objects, bytes, and whether it holds closes by security and date (read ONE object's schema footer to learn the column names; counts and names only).
2. **Pick the primary location and name its columns.** The primary is the location that holds Bloomberg daily closes by security and date. Record its `bucket`, `prefix` and the three column names that hold the security id, the date and the close (`cusip`, `date`, `close` in the issuer's script's vocabulary). If NO location holds any such closes, the primary is the SECHIST series prefix with `objects` = 0 and the coverage is 0: that is a valid, clean answer, stated plainly. If two locations hold closes, record the one with the most securities as primary and list the other under `other_locations` with its counts.
3. **Count and cover.** Run the issuer's script on your record to learn what it measures: `python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cy1_bbg_coverage_check.py <your record.json>` (about a minute). From the primary location, over positive finite closes: `bloomberg.objects`, `bloomberg.points` (distinct (security, date) pairs with a close) and the securities they cover. Then the coverage of the served UNPRICED holding-days (the served `account_day_value` rows with a null close and a null blank_reason, 15,973,399): `coverage.securities_covered` (distinct securities with at least one covered holding-day), `coverage.holding_days_covered` (holding-days whose (security, date) has a Bloomberg close) and the shares of 4,371 securities and 15,973,399 holding-days.
4. **Which of the 3,059 came back.** From the committed request lists (named in round 102's record), the number of listed securities with at least one Bloomberg close in the primary location (`listed_came_back_priced`), of the 3,059 (`listed`), split into never-priced and gap-priced securities of the served table, counts only. If the lists cannot be read as sets of securities, say so and give what can be counted. Never print or copy a security id.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~192/BBG_COVERAGE_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `locations` (`[{"bucket","prefix","objects","bytes","holds_closes","columns"}]`), `bloomberg` (`{"bucket","prefix","columns":{"cusip","date","close"},"objects","points"}`), `other_locations`, `coverage` (`{"securities_covered","holding_days_covered","securities_share","holding_days_share","unpriced_holding_days","unpriced_securities"}`), `listed` (`{"listed","came_back_priced","never_priced_listed_came_back","gap_listed_came_back","source_lists":[paths]}`), `what_this_shows` (two sentences in counts), `not_established`; and a short `.md` beside it. `bloomberg.objects`, `bloomberg.points`, `coverage.securities_covered` and `coverage.holding_days_covered` must equal the issuer's script. No account id, security id, ticker, name or dollar value in either file.

### ACCEPTANCE

<criterion id="CB103cy1-AC1" cell_refs="CB-cy-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~192/BBG_COVERAGE_RECORD.json',encoding='utf-8'));m=d['measured'];print('BBG-COVERAGE-RECORD measured=%s' % m + ((' objects=%d points=%d securities_covered=%d holding_days_covered=%d listed=%d came_back=%d' % (d['bloomberg']['objects'],d['bloomberg']['points'],d['coverage']['securities_covered'],d['coverage']['holding_days_covered'],d['listed']['listed'],d['listed']['came_back_priced'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^BBG-COVERAGE-RECORD measured=(True objects=\d+ points=\d+ securities_covered=\d+ holding_days_covered=\d+ listed=\d+ came_back=\d+|False reason=.+)$</expect></criterion>
`CB103cy1-AC1` -- the record states the Bloomberg objects and points in Opal's store, the unpriced securities and holding-days they cover, and how many of the listed securities came back priced, or states plainly why nothing could be measured.

<criterion id="CB103cy1-AC2" cell_refs="CB-cy-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cy1_bbg_coverage_check.py org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~192/BBG_COVERAGE_RECORD.json</invocation><expect>^BBG-COVERAGE objects=\d+ bbg_points=\d+ bbg_cusips=\d+ unpriced_cusips_covered=\d+ unpriced_rows_covered=\d+ unpriced_rows=15973399 objects_equal=True points_equal=True cusips_covered_equal=True rows_covered_equal=True$</expect></criterion>
`CB103cy1-AC2` -- the issuer's script independently lists the primary location, reads only its three named columns, joins to the served unpriced holding-days and prints the same objects, points, securities covered and holding-days covered as the record (and the 15,973,399 unpriced holding-days of round 102).

<criterion id="CB103cy1-AC3" cell_refs="CB-cy-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py</invocation><expect>^SERVED-UNCHANGED versions_equal=3 of 3$</expect></criterion>
`CB103cy1-AC3` -- the cell wrote nothing: the three served keys still carry the VersionIds the round-98 apply left.

<expected_criteria>CB103cy1-AC1,CB103cy1-AC2,CB103cy1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder, your own NEW channel row, and this order's own file (for the one `<status>` flip). You change no code, test or other committed file. Scratch, if any, stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r103a/` (gitignored, never committed). Your instance rows for artifacts that already exist in a commit are pinned to that commit's FULL hash (never `PENDING-THIS-COMMIT` for a file an earlier commit carried).
- **AWS: READ-ONLY** (`list_objects_v2`, `head_object`, `get_object` of parquet footers and of the named columns of objects in Opal's own buckets, and the served `account_day_value` at its pinned VersionId `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a`). **NO Bloomberg call, no queue draw, no vendor API, no Yahoo call; no write.** A firm-restricted bucket or prefix that refuses a read is reported as refused and not worked around. You do not contact Cottonwood or Commonwealth.
- **No account id, security id (CUSIP or ticker), name or dollar value** in the record, the report or any message: the request lists and the history hold identifiers; read them for counts and never copy one.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never fill, estimate or repair a blank; never mint `data/bloomberg/`; never grade FWD-3 yourself.
- **Time.** Listing and reading a few prefixes takes seconds to minutes; run anything over 100 seconds in the background under `timeout 2400` and read its log.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W192-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only. A difference between your counts and the issuer's script is a finding to report, not to adjust: AC2 then reads False and you stop.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cy-1.bloomberg-history-coverage.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one write to this order is the `<status>` flip.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round103.md</decomp_doc> (round 103), cell `CB-cy-1`.
<owned_cells>CB-cy-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB103cy1-AC1, CB103cy1-AC2, CB103cy1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~192/ADVI_COTBKF.TO-CB-cy-1.bloomberg-history-coverage.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB103cy1-AC1,CB103cy1-AC2,CB103cy1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix; AC2's evidence is the script's two lines joined by a newline); put any note in `denominator`. All three criteria are mechanical. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the order file is in your `<paths>` for this flip).
</proof_of_spec>

**REPORT:** FIRST the `BBG-COVERAGE-RECORD` line. Then: every location examined with its objects and bytes and whether it holds closes; the primary and why; the Bloomberg objects and points; the unpriced securities and holding-days covered and their shares; how many of the 3,059 listed securities came back priced; any location that refused a read; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account id or security id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a listing, a read of named columns and a count; nothing is scheduled, served, pulled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE list, head and get of objects in Opal's own buckets and of one served object at a pinned version under the existing role; no new permission; no Bloomberg or other vendor access.
comp-adversary: RUN -- the headline counts (objects, points, securities and holding-days covered) are recomputed by an issuer script from the primary location the record names, and the record must equal it (AC2); BLIND: the issuer's script trusts the record's choice of location and columns, so a Bloomberg history that lives elsewhere would not be seen by it (the worker's survey of locations is stated and the issuer spot-reads it), and a prefix that holds closes in a shape other than three columns per row (wide or nested) is not read by it; `listed.came_back_priced` depends on reading the committed request lists as sets and is not mechanically graded; the join is on (security id, calendar date) exactly as the served table carries them, so a date or id convention difference would show as a low coverage and is named in `not_established` if suspected.
lane: the <paths> block IS the grant (worker RULING 1), and names the order file for the status flip.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6633 (item 1). The issuer ran its script against an empty prefix as a control: objects 0, 0 covered of 15,973,399, the four `_equal` fields all True, so a zero is a clean answer. No positive control exists yet (no known Bloomberg object in the store to run it on); the join is a plain set intersection on (id, date). Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL as expected; AC3 PASSES (served versions unchanged).
