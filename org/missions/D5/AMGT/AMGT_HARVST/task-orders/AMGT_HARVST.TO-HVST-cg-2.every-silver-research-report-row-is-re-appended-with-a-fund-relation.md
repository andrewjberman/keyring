# AMGT_HARVST task order -- `HVST-cg-2` -- ROUND 92, workstream SILVER-REWRITE: EVERY SILVER `research-report` ROW IS RE-APPENDED WITH A `fund_relation` (STAGED behind a signed never-widen pair and the host owner's notice) (row D1-S46; CTO round-91 analysis item 1)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cg-2.every-silver-research-report-row-is-re-appended-with-a-fund-relation</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cg-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs `typed.main` or the induction against the bucket in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; a PutObject on `amgt/harvest/silver/research-report/` is the only write. The BLAST RADIUS is three new parquet objects, named in the never-widen pair with their rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree that is not `a9aecdd593`'s `lib/research` (a stale classifier fixed into 353 rows), a row dropped or a misfiled KMB row re-appended by hand, a part that wins the newest-part rule with a wrong relation, a retry loop that writes a second part, a detached process whose buffered output hides a gap (`D1-S44`), and a half-landed write (NEVER-2).
</preflight>

## 0. THE CELL

Round 92 adds a key `fund_relation` to the silver `research-report` row (`HVST-cg-1` `ad116e0037`, `HVST-cg-5` `a9aecdd593`). The rows already stored have none. This cell re-appends every stored report's newest row with the key, as NEW parquet parts (the silver writer never overwrites), so the served silver carries the relation. **State plainly in `cg2_before.out`:** nothing served changes until the gateway release `HVST-cg-3`; the proof of this cell is the read-back of the written parts and the equality of two gateway reads before and after.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cg-5` is `<status>complete</status>` and merged (`a9aecdd593`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round92/NEVER_WIDEN_HALF_COO_CG2_SILVER_FUND_RELATION.md` (sha256 `11cf6bd0e637fd440b89881ecd9357c0a10d9c942644f57a3193a7fd287b9158`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CG2_SILVER_FUND_RELATION_CTO_HALF.md`. Read both; their conditions C-1 to C-9 bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cg2-silver-fund-relation-rewrite.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. Work in a worktree of your own at `a9aecdd593` (print `git diff a9aecdd593 HEAD -- lib/research`: empty).
0. **Before-state, read only (`cg2_before.out`):** (i) run `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163/cg5_census.py` in the FOREGROUND with `python -u` and print it: its last two lines must equal `CENSUS-FUND-RELATION rows=355 reports=353 securities=94 holding=121 candidate=14 initiate=2 interest=2 template=1 unclassified=0 none=213 gets=6 bytes=133462` (gets and bytes may differ by the parts present) and the six-name `PROOF-NAMES` line of the COO half; (ii) run `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~161/cg1_rebuild_plan.py` (the dry run: a recording client, nothing put) and print it: `REBUILD-PLAN rows=353 skipped_unchanged=0 new_parts=3 dates=3 puts_recorded=3 puts_performed=0` and the three `WOULD_PUT` row counts 121 (`2026-09-23`), 148 (`2026-09-24`), 84 (`2026-09-25`); any difference: STOP and file a row; (iii) read the scheduled-task list and print that no task runs `typed.main` or the induction against the bucket in the window; (iv) the BEFORE gateway reads (C-7 of the COO half): `harvest_get_research` for `UNH_US_Equity` and `CPA_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of`, `source_keys` and the `research_reports[]` entries. DO NOT call `etfs_compare_peers`.
1. **Write the driver** `cg2_run.py` in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/` from `cg1_rebuild_plan.py`: the same row selection and the same `silver_append` call, with (1) the real client, (2) a `--date YYYY-MM-DD` argument restricting the rows to that `fetched_at` date, (3) a printed manifest line per part written, and (4) the read-back of C-3 and the Branch A checks of the COO half run after the write, printing `READBACK date=<d> rows=<n> equal=PASS|FAIL`. It has NO loop, NO retry and NO background mode.
2. **Write, one date per command, in this order** (C-5): `python -u cg2_run.py --date 2026-09-25` (the canary, 84 rows), then `--date 2026-09-23` (121), then `--date 2026-09-24` (148). After each: append the output to `cg2_run.log`, read the manifest `cg2_written.out` and confirm the part is present, confirm `READBACK ... equal=PASS`; only then the next date. A missing part, a FAIL, an error or silence is a STOP with the exact text.
3. **After the last date (C-6 and C-7):** apply the gateway's newest-part rule to the bucket and print, for all 353 reports, that the newest row carries `fund_relation`, with the per-relation counts (they must equal the census line) and the six `PROOF-NAMES`; then the same gateway reads as step 0 (iv), verbatim; every returned field entry and key equal to the before reads.
4. **Write `cg2_served.out`** ending with exactly these lines: `PARTS_WRITTEN_AND_READ_BACK=PASS|FAIL` (the manifest holds `WRITTEN parts=3 rows=353` and all three read-backs passed), `NEWEST_PER_REPORT_EQUALS_CENSUS=PASS|FAIL`, `GATEWAY_READS_UNCHANGED=PASS|FAIL`. A FAIL stays `pending`; the repair is a still NEWER part decided by the issuer and the CTO, never an overwrite and never a delete by you.
5. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the first date (the canary) is written and read back, and when `cg2_served.out` is written. Commit the ledger close WITH the manifest.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cg2-silver-fund-relation-rewrite.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cg-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg2_served.out</invocation><expect>(?m)^PARTS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cg-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg2_served.out</invocation><expect>(?m)^NEWEST_PER_REPORT_EQUALS_CENSUS=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cg-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg2_served.out</invocation><expect>(?m)^GATEWAY_READS_UNCHANGED=PASS$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cg-2.every-silver-research-report-row-is-re-appended-with-a-fund-relation.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cg-2.every-silver-research-report-row-is-re-appended-with-a-fund-relation` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cg-2.every-silver-research-report-row-is-re-appended-with-a-fund-relation.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** every command in this order is foreground and unbuffered; if you start any process that outlives a tool call, start it unbuffered with its stdout and exit status logged to a file, and read that file; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.
- The hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the bucket and prefix are AMGT's own).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **AMENDMENT 1 (issuer, 2026-10-18 00:1xZ; CTO half SIGNED @b4aac7476a, msg 7791, binding the COO half at sha256 `11cf6bd0...9158` unchanged):** the CTO half is `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CG2_SILVER_FUND_RELATION_CTO_HALF.md`; C-1 to C-9 of the COO half bind you. **Where the two halves differ, the COO half governs:** the CTO half lists the row counts in size order (84, 121, 148) against the dates; the pairing is `2026-09-23` 121 rows, `2026-09-24` 148 rows, `2026-09-25` 84 rows (the dry run, `deliverables/2.0.0_SA_COO_W1/round92/cg2_dryrun_at_a9aecdd593.out`). **C-9, site Z is told first:** the issuer has asked `0.0.0_AB_MSTR~DELL1` to tell site Z the window (2026-10-18 00:30Z to 02:30Z); you may do step 0 (all read only) and write the driver `cg2_run.py` now, but you write NOTHING to the bucket until the issuer sends GO with site Z's answer. The ledger close is COMMITTED with the manifest. If the run passes 02:30Z, stop at a date boundary and tell the issuer.
- **STAGED, not sent.** It waits on the CTO half of the pair, site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`), and the issuer's GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-91 analysis item 1 and msgs 7771, 7775, 7782, 7784. Sequence (CTO msg 7775): this cell, then `HVST-cg-3` (the gateway release), then the proof read through the gateway; `HVST-cf-3` and `-5` follow this cell.
- **Why three commands, smallest date first:** `silver_append` writes one part per date partition in one call; the three calls bound the first exposure to the 84-row partition, and each part is read back before the next. Nothing served changes in the meantime.
- **AMENDMENT 2 (issuer, 2026-10-18 01:1xZ; SC1 msg 7809): A RULING ON C-7, AND AN ERROR OF THE ISSUER'S HALF.** C-7 of the COO half (sha256 `11cf6bd0...9158`, signed, not edited) says `content_sha256`, `source_keys` and the `research_reports[]` entries are equal before and after. That sentence is WRONG about two things, and the issuer wrote it: the gateway lists in `source_keys` the silver parts it read, and names in each `research_reports[].part` the part that won the newest-part rule (`harvest_research.py` lines 270-293); after an add-only rewrite whose new parts win, both change. SC1 found it, read it, and refused to self-grade. **Ruling: this is the EXPECTED consequence of the act, not a failure.** The criterion `GATEWAY_READS_UNCHANGED` is read as: every served VALUE equal (every gold field entry, both gold keys, `content_sha256`, `as_of`, every `research_reports[]` attribute other than `part`, the report set and its order, `omitted_items`), with exactly two named differences: (1) `research_reports[].part` names the new part; (2) `source_keys` lists the three new parts (`date=2026-09-23/part-20261018T010056Z`, `date=2026-09-24/part-20261018T010114Z`, `date=2026-09-25/part-20261018T010034Z`) in addition to the old ones. SC1 writes `GATEWAY_READS_UNCHANGED=PASS` and cites this amendment and msg 7809 in `cg2_served.out`, with the two differences listed. No criterion text changed. Told to the CTO (the co-signed half's condition is read the same way).
- **Own workstream** `SILVER-REWRITE` (each issuance of a round holds its own workstream).
- **Not covered, named:** the gateway release, the `fund_form` rebuild, gold, the shared classifier (row `D1-S49`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>92</round>
<workstream>SILVER-REWRITE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
