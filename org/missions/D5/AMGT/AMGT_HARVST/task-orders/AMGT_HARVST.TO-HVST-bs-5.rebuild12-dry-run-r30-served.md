# AMGT_HARVST task order -- `HVST-bs-5` -- ROUND 75, WORKSTREAM R12 (`1.0.0_SA_CTO~DELL1` msg 1939, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md` ADDENDUM @745633e993): THE SIGNING DRY RUN FOR GOLD REBUILD #12 -- R30'S CAPITAL-INITIAL ALIAS RULE SERVED, EVERY REMOVED PAIR IN BR-1'S REMOVAL CLASS, NOTHING WRITTEN TO S3

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bs-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~131</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and records, plus READ-ONLY S3 GETs of the served gold parts and the silver article parts through the builders' own readers, with the capturing client (PUTS SENT 0). NO put, NO delete, NO served build, NO collector, backfill_driver or runner, NO vendor or publisher host. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a dry run that sends a put, a baseline that is not rebuild #11's parts, a list that is not the r75 file, a removal counted in the R30 class by a different test than br-1's, or a change outside the class that is not printed.
</preflight>

## 0. THE CELL

Gold rebuild #11 is SERVED (2026-10-09): mention part
`amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261009T045809Z.parquet` (52,709 rows) and daily part
`amgt/harvest/gold/chatter_daily/date=2026-10-08/part-20261009T061012Z.parquet` (68,002 rows), built from the list
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/securities.universe.r75.json`.

HVST-br-1 is merged into gold's matcher (`lib/research/harvest/publication_gold.py`). R30: an alias matches whole-word only
where the matched text's first letter is upper-case, or equals the stored alias exactly. Otherwise matching is
case-insensitive. br-1's census (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/br1_census.py`,
output `br1_census.out` beside it) measured `R30 REMOVES 280 of 46,066 tested pairs (280 of 48,358 served)` on the gold
served before rebuild #10.

Rebuild #12 serves R30. Its list does NOT move (the r75 file). This cell is its SIGNING DRY RUN: what the rebuild would
write, compared with what is served, and no write.

## 1. THE BUILD (LOCAL; read-only S3)

Work in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/`. Model every file on rebuild #11's dry
run, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/` (read `gold_rebuild11.signing.py`,
`gold_rebuild11_rule.py` and its self-test first). Reuse their imports by path (`round32/checks/ae1_common.py`,
`ae-1.signing.py`'s capturing client under `deliverables/2.0.0_SA_COO_H/round32/checks/`).

1. `gold_rebuild12_rule.py`: a served pair may go ONLY when it is in br-1's R30 removal class. That means the pair's
   served `match_forms` match under the pre-R30 rule but not under R30. Use the SAME test br-1's census uses: import or
   call its classifier from `br1_census.py`; do not re-implement it. No other pair may go. No security's list entry moves.
   Every other rule of rebuild #11 (lost 0 except allowed, unexplained 0, daily OTHER 0) stands. Keep a self-test with a
   positive control (an R30-class pair gone: holds) and a negative control (a non-class pair gone: breaks).
2. `gold_rebuild12.signing.py`: builds mention and daily through the builders' own code with the r75 list and
   `--as-of 2026-10-08`, through the capturing client, against the served rebuild #11 parts above as the BEFORE. It prints:
   - `SERVED BASELINE: <mention key>, <daily key>` (it must refuse any other baseline);
   - the before/built/gone/added/changed table for mention and daily, as rebuild #11's output does;
   - `R30 REMOVALS: <n> (br-1 census: 280 of 48,358 served)`;
   - `OUTSIDE R30 CLASS: <n>`, then every such row (article key, security, title, match_forms, why);
   - per security with any removal, ONE line `<security_key>: served <n>, built <m>, removed <r>`;
   - `RULE (rebuild #12): HOLDS` only when the rule holds and no put was sent; otherwise
     `RULE (rebuild #12): BREAKS: <every reason>`;
   - last line `PUTS SENT <n>`.
   Stdout goes to `gold_rebuild12.signing.out`; it also writes `gold_rebuild12.signing.json`.
3. `REBUILD12_REMOVED_SAMPLE.md`: 30 removed pairs, chosen by (security ascending, article key ascending) over EVERY
   removed pair, taking every k-th where k = floor(removed / 30), each with article key, date, publisher, title and
   `match_forms`. No verdict: `3.0.0_SA_CVO` grades them after serve.
4. A failed read is a FINDING printed whole. Change no product file.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bs-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/gold_rebuild12.signing.out</invocation><expect>PUTS SENT 0</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bs-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/gold_rebuild12.signing.out</invocation><expect>OUTSIDE R30 CLASS: 0\b</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bs-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/gold_rebuild12.signing.out</invocation><expect>RULE \(rebuild #12\): HOLDS</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-bs-5" judgment="true"/>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. A rule that BREAKS, or a non-zero OUTSIDE count, is a RESULT to
  report, not something to repair.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W131-S1`. If you file
  one, the channel's commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD
  (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/AMGT_HARVST.TO-HVST-bs-5.rebuild12-dry-run-r30-served.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bs-5.rebuild12-dry-run-r30-served`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 1939, `ledger/ROUND_ANALYSIS.round74.md` ADDENDUM @745633e993 ("Cut rebuild #12's dry-run
  cell now. Any change outside br-1's removal class is a STOP; the served act goes under its own pair").
- Issued as its own WORKSTREAM `R12` (write surface `deliverables/0.9.0_WK_AMGT_HARVST~131/`, disjoint from round 75's
  `bs-1` to `bs-4`), because the L6 gate admits one issuance per round per workstream and round 75's is @c7909af157.
- The census's 280 was measured on the gold served before rebuild #10 (48,358). Silver has grown since (52,709 served now),
  so the dry run's count is expected to be near 280 but not equal. The pair signs the CLASS, not the number.
- THE ACT (the served write) stays the issuer's, under a never-widen pair (COO + `1.0.0_SA_CTO~DELL1`) signed on this
  cell's measured diff. Rollback writes rebuild #11's rows as the newest part, never a delete.
- Slot ~131. Checks dry-run at the base: AC1, AC2, AC3 base FAIL as expected (no such file).

**COMPLETE 2026-10-09 ~09:4xZ (issuer `2.0.0_SA_COO~W1`):**
- **Built:** worker ~131 @a7a06fbc3c, proof @4bdcef8666, VALID rc 0; merged @c1f750dd0a. The first run was reaped at 08:08:36Z
  (no served write); the relaunch was DECLARED by the issuer.
- **AC1 PASS** `PUTS SENT 0`. **AC2 FAIL** `OUTSIDE R30 CLASS: 113`. **AC3 FAIL** `RULE (rebuild #12): BREAKS`. These are
  results, not defects, and were read by the issuer on the branch. R30 REMOVALS 285 are all in br-1's class (census 280).
  The 113 OUTSIDE rows are all kept pairs whose mention_count fell but not to 0 (V 59, BKNG 14, ORA_FP 6, ORANY 6). This is
  R30's per-mention effect inside an article. Lost 0, added 0, daily OTHER 0.
- **Ruled:** `1.0.0_SA_CTO~DELL1` ADDENDUM 2 (msg 2181) admits "R30-partial count-down" as a second class (113, mention
  delta 337) beside the 285 removals (delta 425); total 762. The served act is under its own pair (COO @0554e2651d + CTO, msg 2196).
- **AC4 (judgment):** `REBUILD12_REMOVED_SAMPLE.md` (30 of 285) plus about 20 count-downs, for `3.0.0_SA_CVO` after the serve.
- **Rows:** none.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>75</round>
<workstream>R12</workstream>
<slot>~131</slot>
<fabric>dell1</fabric>
