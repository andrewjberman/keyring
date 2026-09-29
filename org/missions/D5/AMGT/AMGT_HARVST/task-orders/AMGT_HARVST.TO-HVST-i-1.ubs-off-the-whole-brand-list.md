# AMGT_HARVST task order -- `HVST-i-1` -- ROUND 19 chain 1 of 1, cell 1 of 4: THE WHOLE-BRAND LIST AGREES WITH ITS REFUSAL LIMB -- `UBS` leaves the list, proved in memory

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-i-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~46</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on whole_brand_aliases.json, universe_securities.py or the harvest gold prefixes; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 -- no new boto3 call; the cell reads S3 (pool universe, silver articles and listing parts, the three newest gold parts) with GET/LIST only. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a list edit that silently moves a served row: `UBS` is also an alias that feeds the publisher-coverage identifiers (round 18 row Z-W45-S2 showed aliases reach data_status), so AC2 rebuilds ALL THREE tables in memory, not mention alone, and requires 0 ALIAS moves.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** This cell edits the whole-brand list and proves in memory that
   nothing served moves. There is no served act in this cell.
2. **Inputs:** the pool universe as `universe_securities.build()` reads it (`universe/v1/2026-09-16.json`, 250 names ->
   191 securities, sa join off); silver as landed today; the SERVED newest gold parts, read from S3.
3. Write the NEW securities file with `universe_securities`' own CLI to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json`. The later cells
   of this round build from exactly that file. The previous file (round 18) is
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/securities.universe.json`; READ ONLY.
4. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/`; outputs named
   `i1_*` -- **never `.scratch/`, never another worker's folder.**
5. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/AMGT_HARVST.TO-HVST-i-1.ubs-off-the-whole-brand-list.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-i-1.ubs-off-the-whole-brand-list`.

<paths>
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round18.md` @`d11fd4d089`, s.2 ruling 2 and s.4 item 2)

1. **`UBS` leaves the whole-brand list** (`lib/research/harvest/whole_brand_aliases.json`). The exact-case ticker `UBS`
   already carries all 7 of its hits, and all 7 are the bank. The whole-brand entry adds nothing and contradicts the
   list's own refusal limb (a): "the brand is an alias or company name of ANY OTHER of the pool's 250 names" refuses
   `UBS` (round 18 row `Z-W45-S1`: a keyless coverage row).
2. **The check becomes a test:** no whole-brand entry is one that limb (a) refuses. The test runs the REAL list through
   the REAL refusal code (`universe_securities`' brand refusal, limbs (a) and (b)), over a pool of names that includes
   the one that refuses `UBS`. State in the test's docstring where its pool comes from; a fixture is admissible only if
   it carries the refusing name verbatim from the pool file.
3. **The rest of the rule is unchanged:** exact-case tickers, the refusal list (`RTX`, `ST`), the other whole-brand
   entries, the parent-brand list (`Walmart`).

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-i-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with two new tests NAMED in the -rA output: (i) no entry of the real whole_brand_aliases.json is refused by limb (a) or limb (b) of the real refusal code; (ii) UBS is not a whole-brand entry and remains an exact-case ticker of UBS_US_Equity; the pass count BEFORE and AFTER printed (base: 194 passed) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-i-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/i1_ac2_nothing_served_moves.py</invocation><expect>deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json equals a fresh universe_securities.build() at HEAD; UBS_US_Equity's aliases and ticker_aliases printed OLD (~45 file) vs NEW; the in-memory rebuild of article_security_mention, chatter_daily and chatter_event from the NEW file, set beside the SERVED newest parts row by row, with every moved row attributed ALIAS or DRIFT and ALIAS = 0 on all three tables (denominators printed per table: served 304 / 51,952 / 8 at the cut); UBS_US_Equity's mention hits printed per form, 7 of 7 carried by the ticker form UBS, unchanged from the served rows</expect></criterion>
</proof_of_spec>

A DRIFT row (silver grown since the served build) is printed and attributed, never counted as an ALIAS move. The
cell's claim is ALIAS = 0.

## 3. WHAT THIS CELL DOES NOT DO

No gold write, no code change outside the list and the tests, no change to any other whole-brand entry, no tier or
event-rule change, no vendor call, no deploy.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Base at the cut (CLOUD after `d11fd4d089`):** suite 194 passed (the `g-1` drain, re-run on trunk after `g-2`).
   Served newest parts: mention `part-20260929T192610Z` (304), daily `part-20260929T192649Z` (51,952), event
   `part-20260929T192706Z` (8). AC1's two named tests FAIL at the base by construction (UBS is on the list); AC2 FAILS
   at the base (no `~46` securities file).
2. **Why all three tables in AC2:** round 18 row `Z-W45-S2` measured that `aliases` feed
   `publication_gold._listing_hit_query_identifiers`, so a list edit can move `data_status` and `publishers_covered`
   without moving a mention. The analysis names "mention rows unchanged (304) with 0 moved"; the issuer widens the
   in-memory read to daily and event inside its own decomposition, at no served cost.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>19</round>
<slot>~46</slot>
<fabric>site-z</fabric>
