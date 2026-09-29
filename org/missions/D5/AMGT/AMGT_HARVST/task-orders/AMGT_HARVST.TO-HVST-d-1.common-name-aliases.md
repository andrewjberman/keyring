# AMGT_HARVST task order -- `HVST-d-1` -- ROUND 15 cell 1 of 2: COMMON-NAME ALIASES -- the census, the rule, and the rebuild proved in memory

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-d-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~41</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on universe_securities.py; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- S3 GET on the universe pool, silver article parts and the newest gold snapshots (mention, daily, event). NO PUT.
comp-adversary: RUN at L5 -- the adversary is a looser alias that buys the AMZN title hits with false hits on other companies' articles, or a new alias that the one-story rule's name detection then strips (row AMGT_HARVST-Z-W40-S1). AC2 prints both.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL.** This cell changes the alias rule and proves the rebuild IN MEMORY. The served
   rebuild is `HVST-d-2`, under its own never-widen pair.
2. **READ ROW `AMGT_HARVST-Z-W40-S1` FIRST** (`org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md`):
   the one-story rule's name-detection step strips a security's own recurring words, and "Amazon" is exactly such a word.
3. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/` -- **never `.scratch/`.**
4. **THE INPUT IS PINNED to what built the SERVED snapshots.** The served mention (`date=2026-09-24/part-20260924T105025Z`,
   263 rows, 55 securities) and daily (`part-20260924T105051Z`, 50,997 rows = 191 x 267 days) were built by
   `lib.research.harvest.universe_securities.build()` over the POOL universe `universe/v1/2026-09-16.json` (250 names ->
   191 securities), with NO sa join -- NOT from `deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json` (6 securities; the
   event build reads it only for its summary). Build with the same call: no `--research-universe` / `--sa-symbols`.
   Write the NEW-alias securities file with the module's own CLI to
   `.../deliverables/0.9.0_WK_AMGT_HARVST~41/securities.universe.json`; `HVST-d-2` builds from exactly that file.
5. **SEPARATE THE ALIAS CHANGE FROM INPUT DRIFT.** Silver has grown since 09-24 (the CTO read 120 articles; the 09-24
   build read 118), and a daily rebuild extends its day range to the new `--as-of`. AC2 therefore builds TWICE in memory
   over today's silver -- OLD aliases and NEW aliases -- and attributes every moved row to ALIAS (new vs old) or DRIFT
   (old vs served).
6. INSTANCE NAMED EXACTLY
   `.../deliverables/0.9.0_WK_AMGT_HARVST~41/AMGT_HARVST.TO-HVST-d-1.common-name-aliases.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-d-1.common-name-aliases`.

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round14.md` @`f00c9a0c43`, s.2-3; read it at the bytes)

**Measured by `1.0.0_SA_CTO~Z`:** AMZN's alias set is `['Amazon.com', 'Amazon.com Inc']`. A headline says "Amazon", and the
word-bounded matcher never finds "Amazon.com" in it; the body says "Amazon.com Inc.", so the LEAD hits and the TITLE never
does. **Tier A (title AND lead) is unreachable for Amazon on any headline using its common name, at any burst size.** The
crash articles (bbg 09-06 "Amazon Cargo Plane Overshoots Runway in Miami, Killing Five"; 09-07; 09-10; a wsj and a barrons
piece) are tier B or C today. `universe_securities.securities_from_universe` (~:169) builds aliases from the name plus
`suffix_forms` (~:105, corporate suffixes such as "Inc"); nothing strips a `.com` tail; `_usable_alias` (~:121) guards.

**RULED:** the alias floor adds the common name a registered name implies -- at minimum a `.com` tail stripped
(`Amazon.com` -> `Amazon`) -- and the cell FIRST censuses the whole universe for other non-suffix tails headlines drop,
printing its denominator (names scanned, aliases added per rule). `_usable_alias` still applies. The tier rule stays as
written.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-d-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/ac1_alias_census.py</invocation><expect>THE UNIVERSE CENSUS, THEN THE RULE: over the live universe build (securities_from_universe), print the names scanned (denominator), every name carrying a non-suffix tail a headline would drop (".com" and any other the census finds, each tail with its count), the aliases each rule ADDS per security, and the aliases _usable_alias REFUSES. PASS only if AMZN gains "Amazon" and the added-alias count per rule is printed with its denominator. At the base AMZN has no "Amazon" alias and this FAILS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-d-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~41/scripts/ac2_rebuild_in_memory.py</invocation><expect>THE REBUILD, IN MEMORY, OVER THE LANDED SILVER, built twice (OLD aliases, NEW aliases from securities.universe.json) and set beside the SERVED newest snapshots, every moved row attributed ALIAS or DRIFT: (a) article_security_mention -- rows served/old/new, every security whose rows move with its row delta, and every NEW (article, security) match printed with its headline (the false-hit sample source); (b) the AMZN crash articles' title/lead flags and tiers before/after; (c) chatter_daily -- the (security, day) cells whose counts move; (d) chatter_event -- every event before/after: the 7 served events each KEPT with the same span and lead unless a named alias change moves it, and every NEW event (expected: AMZN's crash burst) with span, days, articles, tier-A publishers, lead and every headline. (e) Z-W40-S1: print, for AMZN, the tokens the name-detection step strips and whether the crash burst survives it. PASS only if (a)-(e) all print, every served event's fate is named, and every event_id is unique. At the base (d) shows no AMZN event and this FAILS</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-d-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with the new alias tests NAMED in the -rA output (the ".com" strip; any other census-justified tail; _usable_alias still refusing an unusable alias); the pass count BEFORE and AFTER printed (base: 154 passed) and the collected count not falling</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No gold write, no tier-rule change, no one-story-rule change (if `Z-W40-S1` loses the AMZN burst, that is a BLOCKING row,
not a fix here), no vendor call. It does not grade FWD-6.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Split from the rebuild for the NEVER-1 reason of rounds 12-13:** the pair reads the expected outcome from the merged
   rule at signing.
2. **AC2 carries chatter_daily, which the analysis did not name.** `build_daily` reads the newest mention snapshot
   (`publication_gold.py:693`) and the deployed `/timeline` range route serves its series; rebuilding mentions and events
   without it would serve daily counts inconsistent with the events above them. `d-2`'s pair cards the widening for the CTO
   to accept or narrow.
3. **Base: AC1 and AC2 FAIL at the base by construction** (no "Amazon" alias; no AMZN event). Measured by the issuer at
   the cut (CLOUD `b907d17f1c`): `build()` = 250 names, 191 securities, 162 suffix aliases, 11 dropped, pool
   `universe/v1/2026-09-16.json`, sa join off; aliases with a dot tail: 1 of 191 (AMZN: `Amazon.com Inc`, `Amazon.com`).
   The served mention/daily builder was `2.0.0_SA_COO~Y`'s 09-24 QA build (log
   `org/tier1_exec/2.0.0_SA_COO/logs/2026-09-24/harvst_y_2b_graded_chatter_daily_1005-1100Z.md`), found at this cut. AC3 base: 154 passed (the b-1
   AMENDMENT 1 drain). Scripts are worker-written as in every round of this project.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~41</slot>
<fabric>site-z</fabric>
