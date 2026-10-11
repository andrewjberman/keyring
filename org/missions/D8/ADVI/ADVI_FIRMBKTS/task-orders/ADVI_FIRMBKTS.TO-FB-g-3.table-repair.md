# ADVI_FIRMBKTS task order -- `FB-g-3` -- THE TABLE REPAIR UNDER THE CTO'S EDGE RULINGS S2 TO S11 (mapping_v4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~26</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell writes a table and a view; no cron, rule or cadence is touched.
comp-iam: RUN by the issuer -- the identity lists and heads the three legacy buckets (rounds 2 and 3 did the same listing under the same identity); no grant is created.
comp-adversary: RUN by the issuer -- r4_mapping.py structure reads 0 of 5 and repair 0 of 5 at base (mapping_v4.json absent); structure reads 4 of 5 on a fixture (mapping_v3 copied as v4: the live-listing arm S2 fails on 5 re-grid parents that grew since the table's listing, which is the arm working); repair arms U1 to U5 are the rulings below read one per arm. Blindness: the fixture's counts are the v3 listing, not the live one; arm S2 and arm T1-style HEAD reads are the only arms that read S3.
EGRESS CLASS, declared: NONE (S3 list and head inside the account).
</preflight>

## 1. THE CELL -- `FB-g-3` (round 4, enrichment item 2; PRD F2; the round-3 analysis section 2)

The round-3 table, `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json`, places 3,265 classes and leaves 84 as FAULT rows. The CTO ruled each edge the
round-3 worker met (rows `D1-W12-S2` to `D1-W12-S11` in `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md`; read them first: each names its evidence). You apply the
rulings and write the next table. **You decide nothing a ruling does not decide**: a class no ruling places stays FAULT with
a reason and an owner serial.

### 1a. The rulings, verbatim (`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round3.md` section 2)

- **S2: an overlap-0 MERGE must name its destination table in the row.** A merge row with no destination is FAULT, with this
  ruling cited, until the repair writes the destination.
- **S3: rule (b) applies to UNPLACED classes only.** A round-1 placed row stays as placed (the copied-unchanged rule wins).
  No `kind` field is added to a placed row.
- **S5: state families are `<tier>_complete`** (`bronze_complete`, `silver_complete`, `gold_complete`), at `address()` output
  under the owning firm or vendor. A builder refusal is a registry row (CLAUDE.md 30).
- **S6: a QA-named feed is QA only if its WRITER is a QA tool**, read from the writer, not the name. A verified QA output
  gets the RB rule (no destination: RETIRE). Otherwise it is production bronze and goes `bronze/**` HOME. The table records
  which, with the writer named.
- **S7: `*_SKIP.json` (1,142 in the orion-api partitions) is a marker by literal tail**, under ADDENDUM 1's `marker_match`,
  and goes to the same `<tier>_complete` family as a `skip` kind. A skip record is state, not data.
- **S8 and S11: colliding marker keys are split by WRITER.** The state key carries the writing class as a segment
  (`<tier>_complete/<class>/<date>`), so the two eclipse bronze classes (66 keys) and the ten forward-fill `_complete/`
  groups stop colliding. A collision is then a FAULT only if one writer collides with itself.
- **S9: the table repair's sum check compares against the LIVE listing**, per round-2 ADDENDUM 1 (e): list each re-grid
  parent live and print both numbers.
- **S10: a class-grain row has no partition token.** Its address is the class prefix. A class that needs partitions is
  re-gridded, per date. (Exactly one row carries the token today: `opal-data-bd gold/clients/`.)
- Close: print FAULT before and after, with an owner on every remaining class.

### 1b. How each ruling is written (the shapes `r4_mapping.py` reads)

Write `mapping_v4.json` with keys `census_listed_at` (equal to `census.json`'s `listed_at`), `live_listed_at`,
`supersedes: "mapping_v3.json"`, `rows`, `regrids`, `collisions` and **`rulings_applied`**: an object with one key per
ruling id `S2 S3 S5 S6 S7 S8 S9 S10 S11` whose value is the number of rows (or entries) the ruling touched (0 is legal,
and say why in the table view). Every v3 row that is not FAULT is copied unchanged. Every row carries `rule`.

- **S2.** Each `collisions[]` entry with `verdict: "merge"` carries `destination_table` equal to its `table`. The seven
  overlap-0 FAULT classes of `D1-W12-S2` (no `dest`, no table in the row) become MOVE/HOME rows at the group's table
  where the rows name it, or stay FAULT citing S2.
- **S3.** `silver/_silver_complete/` (inf) and `gold/meta/pull-complete.json` (inf) stay as placed, with no `kind`.
- **S5, S7, S8, S11.** A marker row has `kind: "marker"`, `marker_kind: "complete"` or `"skip"`, `state_family` one of
  `bronze_complete` `silver_complete` `gold_complete`, `writer` (a non-empty string: the class or script that writes the
  marker, read from the code, never the object's name), `marker_match` (a non-empty list of literal key tails, no `*`,
  `?` or bracket; `_SKIP.json` for S7), `disposition` MOVE (or HOME), and `dest`: `tier: "state"`, `table` equal to
  `state_family`, `partition` the writing class as ONE token the builder accepts, `object: "{object}"`. `address` and
  `dest_pattern` are exactly `lib/opal_naming.py address()`'s output (never typed). A builder refusal is a missing
  registry row: file it in the report, leave the class FAULT with the reason. No two rows of one bucket carry the same
  (`dest.scope`, `dest.table`, `dest.partition`) with different writers.
- **S6.** Each class whose prefix names QA (`qa`, `diag`, `probe`, `test` as a path token) carries `qa_writer` (the
  script that writes it) and `qa_verdict`: `"qa-tool"` (disposition RETIRE, reason names the writer) or `"production"`
  (disposition HOME, bronze or silver in `opal-data-assets`, through `address()`).
- **S9.** Every `regrids` entry carries `census_objects`, `listed_objects` (a LIVE count taken now),
  `difference` (`listed_objects - census_objects`), `children_objects` (equal to `listed_objects`) and `listed_at`; a
  parent a producer is still writing carries `moving: true` and `moving_reason` (two listings minutes apart differ).
- **S10.** The one class-grain row with a `{partition}` token is re-written at class grain: `dest.partition` is `null`,
  its `address` is `address(source, scope, tier, table, "x")` with the trailing `x` removed (the prefix, ending in `/`,
  never a typed string), and `dest_pattern` ends at the table directory with `/`. Or, if its objects need partitions, it
  is re-gridded per date.

### 1c. Steps

0. Work in `/c/dev/wk-firmbkts-26`. Begin every shell call with `cd /c/dev/wk-firmbkts-26 &&`.
1. Read `mapping_v3.json`, `census.json`, `mapping.json` (round 1) and the channel rows named above. Print the FAULT rows
   grouped by `reason`.
2. For every class you touch, take a LIVE listing (read-only `list_objects_v2`, all pages) and record `listed_at` and
   the count. A QA writer is found by reading the pipeline code (`comp-find` the key prefix over the repository), never by
   guessing from a name.
3. Write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json` and `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE_v4.md`: counts per disposition with the class and object
   denominators (444 classes) and the live total; two lines that read `FAULT before: 84` and `FAULT after: <n>`; for each
   ruling its count and one example; each re-grid's live count (the number the check re-lists); the remaining FAULT
   classes grouped by reason with their owner.
4. Run AC1 and AC2. Repair only what they name.

## 2. BOUNDS

1. Read-only against S3: list and head calls only. No write, copy, delete or configuration change anywhere.
2. Never edit `mapping.json`, `mapping_v2.json`, `mapping_v3.json`, `census.json` or any check. No address is typed from
   memory.
3. A class the rulings do not place is FAULT with a reason and owner `1.0.0_SA_CTO~DELL1`; you never create a DECISION
   row (FWD-7 and FWD-8 are the only two). FAULT after must not exceed FAULT before.
4. Keys carry client ids in some classes: your report names counts and class prefixes, never an object key.
5. Only the files in section 3 change. ASCII only; LF endings. If something cannot be met within your paths, file a
   surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE_v4.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~26/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `census.json`, `mapping.json`, `mapping_v2.json`, `mapping_v3.json`, `lib/opal_naming.py`, the checks under
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`, `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round3.md`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~26/ADVI_FIRMBKTS.TO-FB-g-3.table-repair.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-3"><invocation>cd /c/dev/wk-firmbkts-26 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_mapping.py --arms structure --root /c/dev/wk-firmbkts-26; echo "exit=$?"</invocation><expect>ROUND 4 MAPPING STRUCTURE: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-3"><invocation>cd /c/dev/wk-firmbkts-26 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_mapping.py --arms repair --root /c/dev/wk-firmbkts-26; echo "exit=$?"</invocation><expect>ROUND 4 MAPPING REPAIR: 5 of 5 arms</expect></criterion>
</proof_of_spec>

AC1 includes the difference control (S5: every class the previous table placed, retired or decided keeps its row) and
lists each re-grid parent live (ruling S9). AC2 reads the rulings one per arm (U1 S2, U2 S3, U3 S5/S7/S8/S11, U4 S6,
U5 S9/S10 with the FAULT denominators). Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-3.table-repair.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~26`.
Commit the two deliverables and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer
drains it). Row ids: `ADVI_FIRMBKTS-D1-W26-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: FAULT
before and after, the count per ruling, the re-grids with census, live and difference counts, the output of AC1 and AC2
in full, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the repair is ruling application, not judgment. The field names the check reads (`rulings_applied`,
`state_family`, `writer`, `marker_kind`, `qa_writer`, `qa_verdict`, `destination_table`, `moving`) are the issuer's
shapes for the CTO's text; the CTO reads them at the round-4 analysis. Round-1 placements and the round-2 grain ruling are
untouched by design (S3, S5). The readers of FB-g-4 and FB-g-5 are cut from `mapping_v3.json`'s placed classes, so this
cell and they have no edge.

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the worker's report: rows D1-W26-S1 to S3):** three rulings by the issuer, inside this
decomposition. (S1) the CTO's S10 is the later and specific ruling: the one v3 row carrying a `{partition}` token
(`opal-data-bd gold/clients/`) is rewritten at class grain, and the S5 difference control no longer holds that row to its
token (`r4_mapping.py` S5 skips a v3 non-marker row whose address carries a token). (S2) the CTO's S7 stands: write ONE
skip marker row for `opal-data-inf bronze/orion-api/` (`kind: "marker"`, `marker_kind: "skip"`, `state_family`
`bronze_complete`, `marker_match: ["_SKIP.json"]`, `writer` the class that writes it, read from the writers the worker found
in `inf-performance-daily`), beside the class's existing `complete` marker row: the check's duplicate-key test now tells two
marker rows of one class apart by `marker_kind`. The re-grid entry's `marker_objects` and `data_objects` carry the
skip objects (1,142 at the worker's listing) and their sum still equals `listed_objects`. (S3) a QA-named class whose
writer the pipeline code does not carry is not guessed: it is a FAULT row with reason `S6: no writer found` (cite the
search), owner `1.0.0_SA_CTO~DELL1`, `qa_verdict: "unresolved"`; a row the previous table already placed or retired is copied
unchanged and not re-judged (S3, S5). Arm U3 now requires at least one skip marker row (S7). Gate limb: none grades a
criteria-text amendment here except GATE viii, which read `<placeholders>NONE</placeholders>` at HEAD and no token in the
invocations (unchanged).

<status>pending</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-3</to_id>
<slot>~26</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
