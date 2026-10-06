# IRPT_YCDGEN PRD v0.2 -- ratified-text half review (3.0.0_SA_CVO, 2026-10-05 ~20:5xZ)

Delivered by `1.0.0_SA_CTO` msgs 105361 and 105362. PRD `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md`
@4635d40c62 (prd_version v0.2), half hash c27c89297ee8. The brief half is admitted (the CRO wrote the briefs).

**Verdict: REFUSE, on three lines. Each is a one-line fix; nothing else in the half is in question.**

## The three lines

1. **An annotation sits inside the ENDPOINT block.** PRD line 45: "(the second outcome of v0.1 was retired 2026-10-05 on
   Andrew's word, call 3; its number stays vacant)". It carries a date, a history and a source, and the hash binds it. The
   PROVENANCE section already says the same thing (line 168). The endpoint record @0bb26ab898 has no such line. Fix: drop
   it from the block, or reduce it to a bare vacant marker.
2. **FWD-16's ACCEPT holds a clause that is not in Andrew's word.** "Nothing is changed until the person accepts it."
   His ~20:4xZ word (the 204xZ record, verbatim) says an AI pipeline is to "handle typos and swaps", that the given
   security is classified "in the ETFClassifier row shape", and that swaps go "to comparable securities", ETFs first.
   It does not say whether a correction or swap waits for a person. The clause is today's behaviour of the intake gate
   and C-RESOLVE item (4) already carries it as such. Inside the ratified section it reads as his ruling. Fix: remove the
   sentence from ACCEPT and leave it in C-RESOLVE, or have him read it back. The PRD header itself says FWD-15's and
   FWD-16's lines "have not been read back by him".
3. **C-PRICES has no carrier for the cross-firm rule.** The contract makes the price history "the existing
   `silver/historical_prices.parquet` pull" with its ticker list "extended by the C-MART universe", and the thread's hop 5
   has the producer read it. That object lives in `opal-data-bd`
   (`data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py:43,47`: `S3_BUCKET` default `opal-data-bd`).
   So as written a Cottonwood report reads the bd bucket, and a `data/black_diamond/` script takes a ticker list built from
   other firms' client holdings. CLAUDE.md section 5 forbids referencing another firm's data from a pipeline tree, by
   bucket or key prefix, and `.tools/ds-precommit-check.py:69-72` blocks a `data/black_diamond/` script that names
   `opal-data-cottonwood`. The PRD does not name the bucket, does not say where the universe object lives or how the pull
   reads it, and names no acknowledged departure. C-FIRM's "the shared market-data tables carry no client fact" covers
   the two new `marketdata` tables, not this one. Fix: state the bucket, the universe object's builder address, and
   either the rule that makes the read lawful or the departure Andrew acknowledges.

## The checks

| check | this seat's read | result |
|---|---|---|
| ENDPOINT against the endpoint record | PRD lines 34-164 against `ENDPOINT_FORWARD_IRPT_YCDGEN_INHOUSE_GENERATION_20261005.md` @0bb26ab898, block by block, whitespace normalized. FWD-1, 5, 6, 8 to 14: outcome, DONE WHEN and ACCEPT identical (10 of 10); only SOURCE lines are reworded. FWD-3, 4, 7: the record says "unchanged from v0.1" and the PRD's text equals v0.1 @8b364d6d94 (3 of 3). FWD-2 dropped, as call 3 says | PASS |
| the pin is ratified | The record is PROPOSED and "replaces the ENDPOINT section ... when Andrew confirms it". The 202xZ record holds his answers to the three calls the record put to him ("Call 1 yes ... Call 3 Yes, approved") and the 195xZ record his "all recs approved". No record holds a confirmation of the fourteen outcomes as written; the three calls were all the record asked of him | PASS, as read (note 1) |
| FWD-15 against his word | Outcome and ACCEPT follow the 202xZ verbatim: classification "passes through that table", "new rows are added for unrecognized securities", "cleaned up and proper capitalized" | PASS |
| FWD-16 against his word | Follows the 204xZ verbatim except the one clause in line 2 above | FAIL (line 2) |
| no annotation, history or seat name inside the section | 0 seat serials; one annotation line (line 1 above). FWD-14's SOURCE "(approved, not started: Bloomberg quota)" extends the record's "(approved, not started)" | FAIL (line 1) |
| every operative constraint present | One producer per request and no standing comparator (C-SCOPE, C-COMPARE); scheduled production (C-SCHEDULE); no alerts (C-MORATORIUM); vendor egress on his word (C-VENDOR); builders and registry rows (C-STORE, C-REGISTER); never-widen on the price table and the served worker (C-PRICES, S13). The cross-firm rule has no carrier (line 3 above) | FAIL (line 3) |
| CONTRACTS agree with the counterpart PRDs | IRPT_BCKEND v0.26 `AnalysisReport` (B9/B10, PRD lines 138-159) requires a vendor artifact hash; C-REPORT says so and makes the addendum this project's first dependency (S20 before S13). MDPF_SECCLASS v0.3 names new entries for Rival Funds' stocks and ETF trading (FWD-9, FWD-10) and no request path for a security a client upload names; C-CLASSIFY says the mechanism is MDPF_SECCLASS's and adds no second writer | PASS (note 2) |
| C-STORE and C-REGISTER builder output | re-run here through `lib/opal_naming.py`: both `marketdata/global/silver` addresses, the `ycharts_runs` address and the lambda name reproduce byte for byte; `address('yahoo', ...)` and `name(..., 'schedule')` refuse with the reasons the PRD quotes | PASS |
| cited code | the price pull, the classification client, the three intake files, `held_data.py` and `integrations/bloomberg/READ_HERE.md` all exist at HEAD | PASS |

## Notes (not conditions)

1. A one-line read-back from Andrew of the fourteen carried outcomes would make the pin ratified by his word and not by
   this seat's reading of what the three calls covered.
2. C-CLASSIFY depends on a mechanism MDPF_SECCLASS does not yet state for this universe. An MDPF_SECCLASS addendum naming
   the request path would make the agreement two-sided before FWD-15 is cut.
3. PROVENANCE line 168 says "FWD-8 to FWD-15 added"; the block holds FWD-16 as well. It is outside the hashed section.
4. FWD-16's ACCEPT gives the accepted security a row; his word names "the given security", and C-RESOLVE item (3) covers
   both.
5. Row `IRPT_YCDGEN-W2-S10` is answered by C-COVERAGE and RULINGS batch 267 (the 0.95 floor binds every aggregate). The
   row closes at the next compile on the layout test that pins it.

-- 3.0.0_SA_CVO

## Addendum ~20:4xZ -- v0.3 @cf8c4759e7 (msg 105366, half hash 076dba7b81d7): REFUSE, the same three lines

v0.3 was committed at 20:37:33Z, before this seat's refusal of v0.2 was read (sent 20:37:18Z). Its diff against v0.2
@4635d40c62 changes the version, one header sentence, C-CLASSIFY and C-REPORT; the ENDPOINT block and C-PRICES are
byte-equal. So lines 1, 2 and 3 above stand as written; the annotation is now PRD line 47 and the FWD-16 clause line 163.

Read of the two changed contracts, neither a refusal ground:
- C-CLASSIFY now states the table as 2.0.0_SA_COO~M measured it: no separate sector field, and no model in the path
  that adds an unknown security's row. That agrees with note 2 above, and it means FWD-15 and FWD-16 rest on a classifier
  MDPF_SECCLASS has yet to build on Andrew's word. The contract says so. This seat did not re-measure the table.
- C-REPORT points at a design file and lands the contract row in IRPT_BCKEND's PRD at that project's next round
  boundary. The design file was not graded here.

-- 3.0.0_SA_CVO

## Addendum ~20:4xZ -- v0.4 @6f8b8b9591 (msgs 105367, 105368, half hash 6f5ccc54b568): SIGN

The v0.3 half was never stamped: the tool refused while v0.4 was an uncommitted edit. v0.4's diff against v0.3
@cf8c4759e7 was read whole.

| refusal line | v0.4 at HEAD | result |
|---|---|---|
| 1. annotation inside the ENDPOINT block | the line is gone; the block (PRD lines 36-167) holds no "retired", "vacant" or seat serial; PROVENANCE keeps the retirement | FIXED |
| 2. FWD-16 clause not in Andrew's word | the sentence is out of ACCEPT; C-RESOLVE item (4) keeps it as today's behaviour. The other ENDPOINT bytes are unchanged from the v0.2 read (10 of 10 identical to the endpoint record, 3 of 3 carried from v0.1, FWD-15 on his 202xZ word) | FIXED |
| 3. no carrier for the cross-firm rule in C-PRICES | rewritten: the bd-bucket table is named as 49financial's and is not read, modified or extended; the report reads one new table and the universe has its own address, both builder output; a ticker reaches the universe only by a firm's own push; the gate's foreign-bucket limb is named | FIXED |

Builder output re-run here: `security_total_return_prices` and `security_universe` reproduce byte for byte at
`s3://opal-data-assets/marketdata/global/silver/...`.

**Notes (not conditions).**
6. C-PRICES now builds a second Yahoo price pull beside the 49financial one, where v0.2's ruling 6.3 said "no second price
   pull". The contract gives the reason (the cross-firm rule) and names the consolidation as its own migration. The
   standing veto on build-alongside pipelines is Andrew's; his acknowledgement of this one is not on record.
7. Counts left from v0.3: C-REGISTER item (2), manifest S21 and the write surface (PRD lines 191, 308, 266) say "two"
   tables; the project now writes four `marketdata` tables. C-MART's owner cell (line 188) still says "the existing Yahoo
   price pull (extended)".
8. The gate's foreign-bucket limb keys on `data/black_diamond/` and `data/cot/` paths
   (`.tools/ds-precommit-check.py:69-72`). A refresh or producer under `infra/aws/lambda/` is outside that enumeration,
   so "grades the refresh and the producer like any pipeline tree" is DESIRED until the enumeration gains those homes.
9. Notes 1 to 5 above stand.

-- 3.0.0_SA_CVO
