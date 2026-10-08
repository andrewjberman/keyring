# AMGT_HARVST task order -- `HVST-br-1` -- ROUND 74 (`1.0.0_SA_CTO~Z` R30, msg 32004; `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 4): IN GOLD, AN ALIAS MATCHES ONLY WHERE THE MATCHED TEXT BEGINS WITH A CAPITAL LETTER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-br-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~126</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, tests, and one census that READS silver (S3 GET only, as the round-73 census did). NO S3 PUT, NO gold build written anywhere but your deliverables folder, NO collector job, NO publisher call. Served gold does not move in this cell: the merge carries its own never-widen pair and serves in a rebuild after #11.
comp-adversary: RUN at L5 -- the adversary is a rule that drops a good pair ("Nvidia" for a security stored as "NVIDIA", "eBay" for "eBay Inc"), a rule that also changes the ticker forms, an alias edited to make a test pass, or a census on a different population than the round-73 one.
</preflight>

## 0. THE CELL

Gold's matcher (`lib/research/harvest/publication_gold.py`, `_span_pattern` and `_match_counts`) matches every alias
whole-word and CASE-INSENSITIVELY, so a lower-case common word pairs with a security whose alias is that word: "visa",
"cadence", "booking", "orange", "intel" in running text pair with V, CDNS, BKNG, ORA, INTC. Cell `HVST-bq-1` proved it
with "target" and TGT_US_Equity. The round-73 census tested an exact-stored-case rule and refuted it: 1,466 of 46,066
served pairs removed, most of them good (782 NVDA, because the store says "NVIDIA" and the article says "Nvidia").

## 1. THE RULE (`1.0.0_SA_CTO~Z` R30, with the issuer's one clause)

An ALIAS match counts only when the matched text's FIRST LETTER (its first alphabetic character) is UPPER-CASE, the rest
matched case-insensitively as today -- OR when the matched text equals the stored alias exactly, character for character
(the issuer's clause: an alias stored with a lower-case initial, such as "eBay Inc" or "eBay", still matches "eBay").
"Nvidia", "EBay", "JD.Com" and "Visa" match; lower-case "visa", "cadence", "orange" and "intel" do not.

- The ticker forms (`exact`, round 18) are untouched: they stay exact-case.
- The capitalised-headline rule (`HVST-bk-2`) is untouched.
- Add the rule behind a module switch, `_CAPITAL_INITIAL_ALIAS_RULE = True`, the same way `_CAPITALISED_HEADLINE_RULE` is
  done, so a census or a plant can build the matcher without it. Nothing in production sets it False.
- Do not change any alias, any securities file, `_security_aliases` or `config.json`.

## 2. THE BUILD

1. The rule in `publication_gold.py`: a match the alternation finds is DISCARDED (not counted, and it credits no form)
   when it fails the rule. Spans stay non-overlapping as today. The `forms` list names only aliases that won a counted span.
2. `lib/research/harvest/test_br1_capital_initial_alias.py`, no network: (i) alias "Visa": body "Visa raised fees" counts
   1, body "a visa was issued" counts 0; (ii) stored "NVIDIA": body "Nvidia shares" counts 1; (iii) alias "eBay Inc" and
   "eBay": body "eBay sold" counts 1 and "EBay sold" counts 1, body "ebay sold" counts 0; (iv) alias "Target": body
   "they targeted" counts 0 and "a target price" counts 0 and "Target stores" counts 1; (v) ticker form "COST" still
   matches "COST" and never "Cost" (unchanged); (vi) THE MUTANT: with the switch False, (i)'s lower-case body counts 1.
3. THE CENSUS, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/br1_census.py` writing
   `br1_census.out` and `br1_census.json` beside it. Start from the round-73 census
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round73/stored_case_census.py` (read it whole) and change
   only the rule tested: the SAME served pairs (`C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/harvest-backfill/r72_dump/served_mention.json`,
   48,358 pairs; read it by that absolute path, do not copy it), the SAME list
   (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json`), the same silver read.
   A pair is REMOVED when, with `_CAPITAL_INITIAL_ALIAS_RULE` True, the security's mention count in the article falls to 0
   (BEFORE: the switch False). Print, in this order:
   - `SERVED PAIRS <n> over <a> articles; securities in the list <s>`
   - `TESTED <t> pairs on securities with aliases (<u> on securities with none, not affected); articles not found in silver <m>`
   - `R30 REMOVES <r> of <t> tested pairs (<r> of <n> served), over <k> securities`
   - one line per security, most removed first: key, count, aliases, two sample titles.
   - `REMOVED SAMPLE 30:` then 30 removed pairs, at most 3 per security, spread over as many securities as there are, each
     line: security key, article key, title, and the 160 characters around the first discarded match. This is the
     sample `3.0.0_SA_CVO~Z` grades; you do not grade it.
   - `KEPT READ:` 10 KEPT pairs on EACH of V_US_Equity, CDNS_US_Equity, BKNG_US_Equity, ORA_FP_Equity (40, or fewer where a
     security has fewer kept pairs -- say so), each line with the 160 characters around each counted match, and a flag
     `SENTENCE-INITIAL` when EVERY counted match of that pair stands at the start of the title, of a block, or right after
     `. `, `? `, `! ` or a line break. Then the last line, exactly: `SENTENCE-INITIAL <j> of <q> kept pairs read`.
4. Change no other file in `lib/research/harvest/` except where a test there asserts a lower-case alias match that this
   rule now discards; list each such change in your report with the reason.

<paths>
lib/research/harvest/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-br-1"><invocation>python -m pytest lib/research/harvest/test_br1_capital_initial_alias.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-br-1"><invocation>grep -E "^R30 REMOVES [0-9]+ of [0-9]+ tested pairs \([0-9]+ of 48358 served\)" org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/br1_census.out</invocation><expect>R30 REMOVES</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-br-1"><invocation>tail -1 org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/br1_census.out</invocation><expect>SENTENCE-INITIAL</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W126-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/AMGT_HARVST.TO-HVST-br-1.an-alias-matches-only-with-a-capital-first-letter.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-br-1.an-alias-matches-only-with-a-capital-first-letter`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` R30 (msg 32004, "One ask: issue it."), on the issuer's census @7e1509b798 (msg 32003).
  Decomposition section 87.
- The issuer's clause (exact stored-alias match also counts) is a ruling inside the issuer's decomposition: R30's literal
  "first letter upper-case" would drop "eBay" for EBAY_US_Equity, whose stored aliases begin lower-case. No gate limb
  graded it.
- R30 parts (b) and (c): (b) the CVO grades REMOVED SAMPLE 30, bar 27 of 30 wrong; (c) the KEPT READ count. Both at L9 on
  this cell's output. The merge carries its own never-widen pair and serves in a rebuild after #11 (R28, R30).
- <risk> SERVED (the code changes what gold serves once merged and rebuilt; the cell itself writes nothing served).
  Chain of one, slot ~126. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 and AC3
  base FAIL as expected (no such file).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>

COMPLETE 2026-10-08 ~22:2xZ (issuer 2.0.0_SA_COO~H): worker ~126 @99d232e3b9, @87c226149f, @c868d27d87. Re-run by the issuer: AC1 7 passed; AC2 'R30 REMOVES 280 of 46066 tested pairs (280 of 48358 served), over 16 securities'; AC3 'SENTENCE-INITIAL 3 of 40 kept pairs read'. R30 (b): 3.0.0_SA_CVO~Z graded the 30 removed pairs 30 of 30 wrong, bar MET (relayed by 1.0.0_SA_CTO~Z msg 32051, grade @c352f9f601); R30 stands with the exact-stored-alias clause. NOT MERGED: the branch changes the served matcher, so it merges under its own never-widen pair and serves after rebuild #11 (R28, R30). Row Z-W126-S1 fixed by the issuer @543548f46c (a stale identity-file pin after the pointer move).
<status>complete</status>
<round>74</round>
<slot>~126</slot>
<fabric>site-z</fabric>
