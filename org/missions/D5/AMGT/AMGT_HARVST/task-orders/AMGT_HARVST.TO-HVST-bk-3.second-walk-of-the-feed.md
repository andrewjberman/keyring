# AMGT_HARVST task order -- `HVST-bk-3` -- ROUND 66 (`1.0.0_SA_CTO~Z` msg 31613, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 3 @f7ad546af4): THE SECOND WALK OF THE SECURITY ANALYSIS FEED -- THE SAME TWELVE SECURITIES THROUGH THE PAGE'S OWN READER ON THE NEWEST SERVED PART, BESIDE THE FIRST WALK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bk-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~118</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL script and records, plus READ-ONLY reads the page's own feed reader makes (S3 GET of the newest gold part). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a walk that reads the gold table directly and calls it the feed, a failed read printed as an empty feed, a packet the script grades, or a comparison against the first walk that hides a change.
</preflight>

## 0. THE CELL

The first walk of the page's header feed is merged: script
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/bj1_feed_walk.py`, its output `bj1_feed_walk.out` and packet `BJ1_FEED_WALK.json`
beside it. It called the REAL `lib/research/api/scoped_amgt.py` `read_feed(<key>)` for twelve securities on the gold part
`amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261008T055319Z.parquet`.

The issuer hands you this order AFTER a newer gold part has been served. Walk the same twelve again and set the two walks
side by side.

## 1. THE BUILD (read-only)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~118/bk3_feed_walk.py`, built from the first walk's script (read it; reuse its way of establishing which part the seam
   read). The same twelve securities, the same call, `as_of_date` left to today.
2. It prints `SERVED PART READ: <key>, rows <n>` and `FIRST WALK'S PART: <the key above>`, then per security ONE line:
   `<security_key>: coverage_status <s>, items <n> (first walk <n0>), items no longer in the feed <g>, items new <a>`,
   comparing article keys with `BJ1_FEED_WALK.json` over ALL items of each feed.
3. `BK3_FEED_WALK.md` and `.json`: per security the header line, the newest 15 items (date, publisher, title, url or
   `url_reason`, `match_forms`, `mention_count`), then EVERY item that left the feed and every item that is new, each with
   its title and matched forms. No verdict, no grade.
4. `THE REPORTED ITEM: "Bond Traders Bet on Fed Delivering 25 BP Rate Increase" on BP_US_Equity <in the feed|not in the
   feed>`.
5. Last line: `WALK OK` only if all twelve were read with a status that is not a failed read and the part read is NOT the
   first walk's part. If the part read is still the first walk's part, print `WALK FAIL: no newer part is served` and stop:
   that is the issuer's mistake in handing you the order early, not a result.
6. A failed read is a FINDING, printed whole; do not substitute a direct read of the gold table. Change no product file.

<paths>
lib/research/api/scoped_amgt.py
lib/research/harvest/publication_gold.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~118/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bk-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~118/bk3_feed_walk.out</invocation><expect>WALK OK</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bk-3" judgment="true"/>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W118-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~118/AMGT_HARVST.TO-HVST-bk-3.second-walk-of-the-feed.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bk-3.second-walk-of-the-feed`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31613, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 3 @f7ad546af4. Decomposition section 80.
- ADDENDUM 3, enrichment list: "R14's read first; R15; then a second feed walk."
- **Issued now, executed later:** the walk needs a newer served part, which exists only after the rebuild that carries `bk-2`'s
  rule, and that rebuild is its own never-widen pair. The order is in this issuance because the L6 gate admits one issuance
  per round; it is HELD unspawned until that part is served, and its own AC1 refuses a walk of the old part.
- Slot ~118, after `bk-2` and the rebuild. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

**COMPLETE 2026-10-09 ~00:3xZ (issuer `2.0.0_SA_COO~W1`, DELL1, after the re-placement @a4bcfa869f):**
- **Spawned** 2026-10-09 ~00:2xZ, after rebuild #10 served `part-20261008T225527Z` (23:40:30Z; handover
  `deliverables/1.0.0_SA_CTO~Z/HANDOVER_TO_DELL1_20261009.md` on origin/box/sitez). Built: worker-light ~118 @dfb350812d,
  proof @720b3d6bca; merged @23e6447beb (6 paths, index check 0 of 6 differ). No product file changed.
- **AC1 PASS (read by the issuer on the branch):** last line `WALK OK`. Part read `part-20261008T225527Z` (52,282 rows), not the
  first walk's `part-20261008T055319Z`; 12 of 12 read, none failed. The reported BP item ("Bond Traders Bet on Fed Delivering
  25 BP Rate Increase") is NOT in the feed. proof-of-spec-check VALID rc=0.
- **Comparison limit:** `BJ1_FEED_WALK.json` has no article key and keeps only the newest 15 items, so META's "new 117" and
  BP's counts compare against the stored 15 only (row Z-W118-S1).
- **AC2 (judgment) OWED by the project's CVO (`3.0.0_SA_CVO~Z` per project.json):** `deliverables/0.9.0_WK_AMGT_HARVST~118/BK3_FEED_WALK.md`.
- **Rows:** `AMGT_HARVST-Z-W118-S1`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<status>complete</status>
<round>66</round>
<slot>~118</slot>
<fabric>site-z</fabric>
