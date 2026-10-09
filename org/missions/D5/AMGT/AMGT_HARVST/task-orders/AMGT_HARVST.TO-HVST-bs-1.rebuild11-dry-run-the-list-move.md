# AMGT_HARVST task order -- `HVST-bs-1` -- ROUND 75 (`1.0.0_SA_CTO~DELL1` msg 1410, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md` @fdce9f9c38, enrichment item 1; R28): THE SIGNING DRY RUN FOR GOLD REBUILD #11 -- THE AIG AND OMAB LIST MOVE, PAIRS MOVED PER SECURITY, TEN TITLES EACH, NOTHING WRITTEN TO S3

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bs-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~129</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and records, plus READ-ONLY S3 GETs of the served gold parts and the silver article parts through the builders' own readers, with the capturing client (PUTS SENT 0). NO put, NO delete, NO served build, NO collector, backfill_driver or runner, NO vendor or publisher host. `lib/opal_data_harvest/config.json` is not changed. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a dry run that sends a put, a list file that is not `universe_securities.build()` at HEAD, a served baseline that is not rebuild #10's parts, a rule that passes because a pair loss was counted under a list-moved security it does not belong to, or ten titles chosen to look good rather than the first ten by a stated order.
</preflight>

## 0. THE CELL

Gold rebuild #10 is SERVED (2026-10-08 23:40:30Z): mention part
`amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261008T225527Z.parquet` and daily part
`amgt/harvest/gold/chatter_daily/date=2026-10-08/part-20261008T232700Z.parquet`, built from the FROZEN list
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round72/securities.universe.r72.json` (242 securities).

`lib/research/harvest/universe_securities.build()` at HEAD returns 242 securities and differs from that list in exactly three:
`AIG_US_Equity` (company and aliases now `AMERICAN INTERNATIONAL GROUP, INC.`, `AMERICAN INTERNATIONAL GROUP`,
`AMERICAN INTERNATIONAL`, `AMERICAN INTERNATIONAL GROUP, INC`; was `American International Group`, `American International`),
`OMAB_MM_Equity` (aliases now `Grupo Aeroportuario del Centro Norte`, `Grupo Aeroportuario del Centro`) and `OMAB_US_Equity`
(alias now `Grupo Aeroportuario del Centro Norte` only). Rebuild #11 serves that list move and nothing else. This cell is its
SIGNING DRY RUN: what the rebuild would write, compared with what is served, and no write.

## 1. THE BUILD (LOCAL; read-only S3)

Work in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/`. Model every file on rebuild #10's, in
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round72/`: read `gold_rebuild10.signing.py`,
`gold_rebuild10_rule.py` (run its self-test) and `REBUILD10_NAMED_REMOVALS.json` first, and reuse their imports
(`round32/checks/ae1_common.py`, `ae-1.signing.py`'s capturing client) by path; do not copy those two.

1. `securities.universe.r75.json`: written once from `universe_securities.build()` at HEAD (same JSON form as the r72 file).
2. `gold_rebuild11_rule.py`: rebuild #10's rule with the served list = the r72 file and the proposed list = the r75 file. A
   served pair may go only when its security is list-moved (the three above) or fallback, or it is named by key in
   `REBUILD11_NAMED_REMOVALS.json` (write it; it starts EMPTY, and you add nothing to it). Keep the self-test and add one
   negative control: a pair lost on an UNCHANGED security breaks the rule.
3. `gold_rebuild11.signing.py`: builds mention and daily through the builders' own code with the r75 list and
   `--as-of 2026-10-08`, through the capturing client, against the served rebuild #10 parts above as the BEFORE. It prints:
   - `SERVED BASELINE: <mention key>, <daily key>` and `LIST FILE EQUAL TO build() AT HEAD: True|False`;
   - `LIST MOVED: <the securities whose entries differ, comma-separated>`;
   - the before/built/gone/added/changed table for mention and daily, as rebuild #10's signing output does;
   - per list-moved security ONE line `<security_key>: pairs served <n>, built <m>, gone <g>, added <a>`;
   - `RULE (rebuild #11): HOLDS` only when the rule holds, the list check passes and no put was sent; otherwise
     `RULE (rebuild #11): BREAKS: <every reason>`;
   - last line `PUTS SENT <n>`.
   Its stdout goes to `gold_rebuild11.signing.out`, and it writes `gold_rebuild11.signing.json`.
4. `REBUILD11_TITLES.md`: for each of the three list-moved securities, the FIRST TEN gone pairs and the FIRST TEN added pairs
   by (published date descending, article key ascending), each with article key, date, publisher, title and `match_forms`.
   If fewer than ten exist, all of them and the count. No verdict, no grade: `3.0.0_SA_CVO~Z` grades the titles.
5. A failed read is a FINDING printed whole; do not replace a builder's read with a direct table read. Change no product file.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bs-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/gold_rebuild11.signing.out</invocation><expect>PUTS SENT 0</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bs-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/gold_rebuild11.signing.out</invocation><expect>LIST MOVED: AIG_US_Equity, OMAB_MM_Equity, OMAB_US_Equity</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bs-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/gold_rebuild11.signing.out</invocation><expect>RULE \(rebuild #11\): HOLDS</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-bs-1" judgment="true"/>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression (row AMGT_HARVST-Z-W128-S1); AC3 escapes its parentheses for that reason.
- If the rule BREAKS, AC3 fails and that is a RESULT, not something to repair: print every reason and report it.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-D1-W129-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~129/AMGT_HARVST.TO-HVST-bs-1.rebuild11-dry-run-the-list-move.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bs-1.rebuild11-dry-run-the-list-move`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 1410, `ledger/ROUND_ANALYSIS.round74.md` @fdce9f9c38, enrichment item 1 and placement 3
  (rebuild #11 first). R28 (`1.0.0_SA_CTO~Z` msg 31945, ADDENDUM 4 of the round-60 analysis): the AIG/OMAB list move is rebuild
  #11 under its own pair; its dry run prints the pairs moved per security, ten titles each, graded by `3.0.0_SA_CVO~Z`.
- The three-security diff was read by the issuer at box/dell1 HEAD 2026-10-09 ~02:0xZ (r72 file against `build()`: 242 and 242,
  3 changed, 0 added, 0 removed).
- Rebuilds #9 and #10 ran their dry runs as the issuer's own act. Under FULL this issuer cuts and spawns and does not build,
  so the dry run is a worker cell. THE ACT (the served write) stays the issuer's, under a never-widen pair that reads this
  cell's output; it is not an order.
- Slot ~129. Checks dry-run at the base: see decomposition section 88.

**COMPLETE 2026-10-09 ~03:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Built:** worker ~129 @52be31ddc2 (dry run), proof @2ba8e449f5, VALID rc 0; merged @ff5e34ab44. Re-read by the issuer on the
  branch: output, proof, and the rule self-test (holds on a list-moved loss; negative controls break it).
- **AC1 PASS** `PUTS SENT 0` (2 puts captured, 0 sent). **AC2 PASS** `LIST MOVED: AIG_US_Equity, OMAB_MM_Equity, OMAB_US_Equity`.
  **AC3 PASS** `RULE (rebuild #11): HOLDS`.
- **The finding:** the list move gains and loses 0 pairs on all three securities (AIG 16 served, 16 built; OMAB_MM 5 and 5;
  OMAB_US 5 and 5). It shows only as 22 changes to those securities' own fields (class g: AIG 12, OMAB_MM 5, OMAB_US 5).
  The rest of the build is silver growth since rebuild #10: mention +427 (418 on unchanged securities, 9 on fallback
  GSK_LN), daily 1,690 changed (a 847, d 840, b 3), lost 0, unexplained 0, OTHER 0. `OMAB_US_Equity` lost a served alias,
  and no mention count went down.
- **AC4 (judgment):** `REBUILD11_TITLES.md` is empty by construction (no pair moved). R28's ten titles each cannot be graded.
  Routed to `1.0.0_SA_CTO~DELL1` with the serve act's pair. Row `AMGT_HARVST-D1-W129-S1`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>75</round>
<slot>~129</slot>
<fabric>dell1</fabric>
