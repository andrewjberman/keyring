# ADVI_FIRMBKTS task order -- `FB-f-2` -- THE TABLE REPAIR UNDER THE GRAIN RULING (mapping_v3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~12</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell writes a table and a view; no cron, rule or cadence is touched.
comp-iam: RUN by the issuer -- the identity lists and heads the three legacy buckets (round 2 did the same listing under the same identity); no grant is created.
comp-adversary: RUN by the issuer -- r3_mapping.py structure 0 of 5 and repair 0 of 5 at base (mapping_v3.json absent); 5 of 5 and 5 of 5 on a fixture derived from mapping_v2.json; mutants: a dropped collision entry 4 of 5, a rule-(a) row left FAULT 3 of 5, a disturbed round-2 address 3 of 5. Blindness: the fixture's counts are not the live listing; the live HEAD arm (T1) is the only arm that reads S3.
EGRESS CLASS, declared: NONE (S3 list and head inside the account).
</preflight>

## 1. THE CELL -- `FB-f-2` (round 3, enrichment item 3; PRD F2; closes D1-W4-S2..S6)

The round-2 table, `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json`, places 444 census classes and leaves
89 as FAULT rows, each owned by `1.0.0_SA_CTO~DELL1`. The CTO has ruled the grain for each shape of the 89
(`ledger/ROUND_ANALYSIS.round2.md` section 2 item 3, quoted below). You apply the ruling and write the next table. **You
decide nothing the ruling does not decide**: a class no rule places stays a FAULT row with a reason and the same owner.

### 1a. The ruling, verbatim

- (a) **A zero-byte object whose key equals its class prefix** (a folder placeholder) is RETIRE. It holds no data. This
  unblocks `bd gold/clients/` (2,949 objects), which stays FAULT today only because of such a marker (W4-S3).
- (b) **Completion markers (`state/complete` groups)** carry `kind: marker` in the table and map to the R21 `state/` home
  of the class they mark. They are never re-gridded beside data (W4-S2).
- (c) **Classes that interleave markers and data** are split by (b), then re-gridded PER DATE PARTITION with no child
  cap. The 25-child limit was a worker's choice, not a rule (W4-S5: 6 classes, 23,977 objects).
- (d) **A new class that collides with a round-1 placed class** follows round 1's collision rule: a deliberate merge with
  its reason, or a split, decided at a measured key overlap. The round-1 row is not displaced by default (W4-S4).
- (e) **Denominators:** the re-grid counts against the live listing; the census stays the census. Each table repair
  prints both and their difference (W4-S6).
- Close: the repair applies (a)-(d) and prints FAULT before and after, with an owner on every remaining class.

### 1b. The steps

0. Work in the worktree `/c/dev/wk-firmbkts-12`. Begin every shell call with `cd /c/dev/wk-firmbkts-12 &&`.
1. Read `mapping_v2.json` (keys: `census_listed_at`, `supersedes`, `rows`, `regrids`, `collisions`), `census.json` (the
   census; never edited) and `mapping.json` (round 1). Print the FAULT rows grouped by `reason`.
2. For every FAULT class you touch, take a LIVE listing (read-only `list_objects_v2` on the row's `bucket` and `prefix`,
   all pages) and record its `listed_at` and object count. A zero-byte object is a `ContentLength` of 0.
3. Apply the rules. Row and table shapes:
   - **(a)** the placeholder becomes a row `{bucket, prefix, disposition: "RETIRE", rule: "3a: zero-byte folder
     placeholder (ruling 3a)", placeholder_key: <the key, equal to prefix>, reason: "folder placeholder, zero bytes"}`.
     The class's other objects, if any, are re-gridded into children (a child's `prefix` starts with its `parent`; one
     `regrids` entry per parent) or stay FAULT.
   - **(b)** a completion marker row carries `kind: "marker"`, `disposition: "MOVE"` (or `HOME`) with `dest.tier:
     "state"`, `dest.table` the family it marks, and `address` / `dest_pattern` exactly as `lib/opal_naming.py address()`
     builds them (never typed). A re-grid's children are ALL markers or NONE.
   - **(c)** a `regrids` entry for an interleaved class carries `partition_rule: "per-date"` and NO `cap` key; its
     children are the class's date partitions (the directory names that carry a date), one child row per partition.
   - **(d)** `collisions[]`: one entry per destination table that two or more MOVE/HOME classes of one bucket share,
     `{bucket, source, scope, tier, table, classes, verdict: "merge"|"split", reason, overlap_keys}` where `overlap_keys`
     is the MEASURED number of destination keys both classes write (an integer from the two live listings). `merge`
     requires 0; `split` requires more than 0 and names the classes' children. A collision between two round-1 PLACED
     classes with overlap above 0 stays FAULT, owner `1.0.0_SA_CTO~DELL1` (a worker never chooses which class wins).
   - **(e)** every `regrids` entry carries `census_objects` (the parent's `objects` in `census.json`), `listed_objects`
     (the live count), `difference` (`listed_objects - census_objects`), `children_objects` (equal to `listed_objects`)
     and `listed_at`.
4. Write `deliverables/mapping_v3.json` with keys `census_listed_at` (equal to `census.json`'s `listed_at`),
   `live_listed_at` (the time of your listings), `supersedes: "mapping_v2.json"`, `rows`, `regrids`, `collisions`. Every
   v2 row that was not FAULT is copied unchanged. Every row carries `rule` (a string naming the rule that placed it).
5. Write `deliverables/MAPPING_TABLE_v3.md`: counts per disposition (MOVE, HOME, RETIRE, DECISION, FAULT) with the census
   class and object denominators (444 classes and the object total) and the live total, and two lines that read
   `FAULT before: 89` and `FAULT after: <n>`, then the remaining FAULT classes grouped by reason with their owner.
6. Run AC1 and AC2 (section 4). Repair only what they name.

## 2. BOUNDS

1. Read-only against S3: list and head calls only. No write, copy, delete or configuration change anywhere.
2. Never edit `mapping.json`, `mapping_v2.json`, `census.json` or any check. No table row is typed from memory: every
   address comes from `lib/opal_naming.py address()`.
3. A class the rules do not place is FAULT with a reason and owner `1.0.0_SA_CTO~DELL1`; you never create a DECISION row
   (FWD-7 and FWD-8 are the only two, already present).
4. Keys carry client ids in some classes: your report names counts and class prefixes, never an object key.
5. Only the files in section 3 change. No non-ASCII; LF line endings. If something cannot be met within your paths,
   file a surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE_v3.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `census.json`, `mapping.json`, `mapping_v2.json`, `lib/opal_naming.py`, the checks under
`deliverables/2.0.0_SA_COO~B1/round3/checks/`, `ledger/ROUND_ANALYSIS.round2.md`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~12/ADVI_FIRMBKTS.TO-FB-f-2.table-repair.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-2"><invocation>cd /c/dev/wk-firmbkts-12 &amp;&amp; timeout 110 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py --arms structure --root /c/dev/wk-firmbkts-12; echo "exit=$?"</invocation><expect>ROUND 3 MAPPING STRUCTURE: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-2"><invocation>cd /c/dev/wk-firmbkts-12 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py --arms repair --root /c/dev/wk-firmbkts-12; echo "exit=$?"</invocation><expect>ROUND 3 MAPPING REPAIR: 5 of 5 arms</expect></criterion>
</proof_of_spec>

AC1 includes its own difference control (S5: every class round 2 placed, retired or decided keeps its row). AC2's arm T1
makes live read-only HEAD calls on each placeholder key. Each invocation terminates inside the bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-2.table-repair.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~12`. **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance and the two deliverables**, only when AC1 and AC2 pass. A row id on this project carries
the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W12-S<k>`, `surfaced_at` from `date -u +%FT%TZ`. Report once: FAULT
before and after, the count per rule (a)-(d), the re-grids with their census, live and difference counts, the collision
entries by verdict, the output of AC1 and AC2 in full, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the repair is rule application, not judgment; the CVO's grade of FWD-2 is "the second person got the
same answer" (round 3's compare of two placers is not cut: the table has not stopped moving). Round-1 placements and
the CTO's `D1-W4-S1` ruling (`2ca0be7c81`) are untouched by design (S5). The check's T3 expects the five round-2
interleaved inf classes disposed under rule (c); if a class has no date partitions the worker files a row and the class is
the CTO's.

<status>pending</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-2</to_id>
<slot>~12</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
