# AMGT_HARVST task order -- `HVST-g-1` -- ROUND 18 cell 1 of 2: THE ALIAS RULE -- case-sensitive tickers and a whole-brand list, proved in memory

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-g-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~45</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on universe_securities.py or the matcher; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the pool universe, silver article/listing parts and the newest gold snapshots. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a ticker that matches a common word (case-insensitively, or at one letter), a whole-brand entry that credits a parent's coverage to a subsidiary, or a new alias that moves a served event unseen. AC1 names the tests; AC2 prints every added hit and every event.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL.** This cell changes the alias rule and proves the rebuild IN MEMORY. The served
   rebuild is `HVST-g-2`, under its own never-widen pair.
2. **Inputs:** the pool universe as `universe_securities.build()` reads it (`universe/v1/2026-09-16.json`, 250 names -> 191
   securities, sa join off); silver as landed today (120 articles at the cut); the round-17 census outputs, READ ONLY, at
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~43/` (`ac1_output.txt`, `ac2_output.txt`) and the
   CVO's read `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/adjudications/ADJUDICATION_v25.md`.
3. Write the NEW securities file with `universe_securities`' own CLI to
   `.../deliverables/0.9.0_WK_AMGT_HARVST~45/securities.universe.json`; `HVST-g-2` builds from exactly that file.
4. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/` -- **never `.scratch/`, never another worker's folder.**
5. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~45/AMGT_HARVST.TO-HVST-g-1.alias-rule-tickers-and-whole-brands.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-g-1.alias-rule-tickers-and-whole-brands`.

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/research/harvest/whole_brand_aliases.json
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round17.md` @`c296f4ba12`, s.2; read it at the bytes)

1. **Tickers: case-sensitive, 2+ characters, with an explicit refusal list.** A ticker alias matches only its exact upper-case
   form (the served matcher is case-insensitive today, `publication_gold._span_pattern` ~:116, so a ticker needs its own
   case rule). Single-letter tickers never match. The refusal list starts with `RTX` and `ST`.
2. **Short names are never derived.** A short name enters only from an explicit per-security whole-brand list, starting
   with `Dell`, `TJX`, `UBS`, `ASML`, `Micron`, `Uber`, `Spotify`. Each entry cites the census hits that admitted it.
   Meta, eBay, SAP and QXO are NOT in the list.
3. **A subsidiary listing never carries its parent's brand**, as a CHECK IN CODE. The planted entries `WALMEX*` ->
   `Walmart` and `KOF` -> `Coca-Cola` must both be refused.
4. Brand-to-parent names ("Google" for Alphabet) stay out.

**Measured by the issuer at the cut (CLOUD `f1c482d24f`), and the issuer's ruling on the refusal check:** `KO_US_Equity`
is among the 191 with alias `Coca-Cola`, so the ruled check ("an entry whose brand is another listed security's brand")
refuses `KOF` -> `Coca-Cola`. **Walmart Inc. is NOT among the 191, nor among the pool's 250 names** (only `WALMEX* MM`,
"Walmart de Mexico WALMEX"), so that check alone cannot refuse `WALMEX*` -> `Walmart`. The check therefore has TWO
limbs, both in code:
- (a) the brand is an alias or company name of ANY OTHER of the pool's 250 names;
- (b) the brand is on an explicit PARENT-BRAND refusal list carried in `whole_brand_aliases.json`, starting with
  `Walmart` and citing the census (0 of 18 correct for WALMEX* / KOF, `ADJUDICATION_v25.md`).

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-g-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with the new alias-rule tests NAMED in the -rA output (a ticker matches only its exact upper case; a 1-character ticker never matches; RTX and ST are refused; a whole-brand entry is admitted; KOF -> Coca-Cola is refused by limb (a); WALMEX* -> Walmart is refused by limb (b); a lower-case "don't" never hits ticker T); the pass count BEFORE and AFTER printed (base: 177 passed) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-g-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/ac2_rule_rebuild_in_memory.py</invocation><expect>THE REBUILD, IN MEMORY, OVER TODAY'S SILVER, OLD aliases (the served securities file, deliverables/0.9.0_WK_AMGT_HARVST~41/securities.universe.json) vs NEW (deliverables/0.9.0_WK_AMGT_HARVST~45/securities.universe.json), set beside the SERVED newest parts, every moved row attributed ALIAS or DRIFT: (a) article_security_mention -- added mentions per FORM and per SECURITY with the denominator, every row added or changed with its headline and the form that hit, title/lead flips; (b) chatter_daily -- per security the cells that move; (c) chatter_event -- every served event KEPT, MOVED or GONE, and every NEW event with span, articles, lead and every headline; (d) row Z-W44-S1 re-read: per security the name stems stripped, old vs new; (e) every event_id unique. PASS only if (a)-(e) all print and every served event's fate is named</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-g-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/ac3_rebuildable_and_file.py</invocation><expect>deliverables/0.9.0_WK_AMGT_HARVST~45/securities.universe.json equals a fresh universe_securities.build() at HEAD; the whole-brand file's every entry carries its census citation; and two in-memory builds of mention, daily and event from the same inputs are equal row by row, denominator printed per table</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-g-1" judgment="true"/>
</proof_of_spec>

**AC4 -- JUDGMENT, PRESENTED AND NOT GRADED** (status `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming
`3.0.0_SA_CVO~Z` at L9). Script: `.../deliverables/0.9.0_WK_AMGT_HARVST~45/scripts/ac4_added_hits_sample.py`. For every form
with added hits, up to 10 added hits (all if 10 or fewer, else drawn with a printed seed), each with headline, block, offset
and the words around the match. **Per form: how many are the company?** (The ruling grades the rule again "on its own
output".) Present; record NO verdict.

## 3. WHAT THIS CELL DOES NOT DO

No gold write, no brand-to-parent source, no tier or event-rule change, no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **The two-limb refusal is the issuer's ruling inside its decomposition.** The CTO's check alone cannot refuse the
   planted `WALMEX*` -> `Walmart` entry the same ruling requires, because Walmart Inc. is not in the pool (measured at the
   cut). Limb (b) is the explicit list that closes that gap. Carded to `1.0.0_SA_CTO~Z` at the issuance.
2. **Base:** suite 177 passed (the `f-2` drain). Served: mention `part-20260929T112204Z` (275), daily
   `part-20260929T112222Z` (51,952), event `part-20260929T092439Z` (8). AC2/AC3 FAIL at the base by construction.
3. **`Z-W44-S1` travels here** (AC2 (d)): new tickers and brands become matched forms, so they become strippable name stems.
   That is intended, and it must be shown on the served events.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>18</round>
<slot>~45</slot>
<fabric>site-z</fabric>
