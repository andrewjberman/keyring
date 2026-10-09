# AMGT_HARVST task order -- `HVST-bt-1` -- ROUND 76 (`1.0.0_SA_CTO~DELL1` msg 2333, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md` ADDENDUM 3, R31): A COMMON-WORD ALIAS MATCHES ONLY WITH A SECOND ANCHOR IN THE SAME ARTICLE -- THE RULE, ITS TESTS, AND A MENTION-GRAIN CENSUS ON SERVED GOLD, NOTHING WRITTEN TO S3

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bt-1.a-common-word-alias-needs-a-second-anchor</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~132</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests, plus READ-ONLY S3 GETs of the served gold mention part and the silver article parts (the census), and ONE public HTTPS GET of a public-domain word list. NO put, NO delete, NO served build, NO collector, runner or backfill_driver, NO vendor API, NO Bloomberg. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a common-word list chosen by hand instead of measured, a second anchor that is the alias itself, a census counted at pair grain when R31 asks mention grain, or a switch that silently stays on in a test that claims to test it off.
</preflight>

## 0. THE CELL

Gold's matcher is `lib/research/harvest/publication_gold.py`. R30 is served (rebuild #12):
`_CAPITAL_INITIAL_ALIAS_RULE = True` (line ~154) discards an alias match whose first letter is lower-case. The CVO's grade
of rebuild #12 (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_REBUILD12_REMOVED_AND_COUNTDOWN_GRADE_20261009.md`)
found that 14 of 20 kept rows are still not about the company: 8 travel or immigration "Visa", 6 fruit or colour
"Orange". They survive on a capitalised word, for example in a headline.

R31 (ADDENDUM 3): an alias that is also an ordinary dictionary word matches only where the SAME article ALSO carries a
SECOND ANCHOR. The anchor is one of:
- the security's ticker;
- its full legal or company name;
- a company-specific term the alias row already holds, meaning another alias of the same security that is not itself a
  common word.

A distinctive alias (not a dictionary word) is unchanged.

## 1. THE BUILD (LOCAL; on your branch)

1. **The word list.** Fetch `https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt` once (public
   domain, about 370,000 lower-case words). Save it as
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~132/words_alpha.txt`, with
   `WORDLIST_SOURCE.json` beside it holding the URL, the fetch time (UTC), the byte size, the line count and the SHA-256.
   Do not hand-edit the list.
2. **The common-word alias set, MEASURED.** In `publication_gold.py`, a function returns, for a security, the aliases
   whose lower-cased whole text is ONE word in the list. A multi-word alias is common only when every word is in the list
   and the alias has one word; say how you decided this in a comment. The word list is loaded from a path set in one
   module constant, `_COMMON_WORD_LIST_PATH`, pointing at the vendored file. Its absence is a loud error, never a silent
   "no common words".
3. **The rule.** Behind a module switch `_COMMON_WORD_SECOND_ANCHOR_RULE = True`, done the same way as
   `_CAPITAL_INITIAL_ALIAS_RULE`: a counted span whose winning form is a COMMON-WORD alias of the security counts only
   when the article (title plus all blocks) also has a second anchor for that security. The ticker anchor uses the
   existing exact-case ticker forms. The full-name anchor uses the security's company string, whole-word,
   case-insensitive. The term anchor uses any other alias of the same security that is NOT common. The common alias itself
   never anchors itself. If no anchor exists, every span that alias won is discarded, as R30 does.
4. **Tests**, `lib/research/harvest/test_bt1_common_word_second_anchor.py`, no network. They use a tiny fixture word list
   in the test, with the constant patched, and assert:
   - (i) a "Visa" security: body "Visa raised fees" alone counts 0; the same body plus "V shares rose" (ticker) counts 1;
     plus "Visa Inc." (full name) counts 1.
   - (ii) an "Orange" security with alias "Orange" and the full name "Orange S.A.": "Orange juice prices" counts 0, and
     "Orange S.A. said ... Orange" counts 2.
   - (iii) a distinctive alias, "Nvidia": counts as today with no anchor.
   - (iv) THE MUTANT: with the switch False, (i)'s first body counts 1.
   - (v) a missing word-list path raises.
5. **THE CENSUS**, `deliverables/0.9.0_WK_AMGT_HARVST~132/bt1_census.py`, writing `bt1_census.out` and `.json`. Build
   from `deliverables/0.9.0_WK_AMGT_HARVST~126/br1_census.py` (read it whole) and change only the rule tested. The
   population is the SERVED gold mention part
   `amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261009T093755Z.parquet` (rebuild #12, 52,424 pairs)
   with silver read the same way. The list is `deliverables/0.9.0_WK_AMGT_HARVST~129/securities.universe.r75.json`.
   BEFORE has R31 off and R30 on; AFTER has both on. Print, in this order:
   - `WORD LIST: <lines> words, sha256 <hash>`
   - `COMMON-WORD ALIASES: <n> over <s> securities`, then every one as `<security_key>: <alias>`;
   - `R31 MENTIONS: before <b>, after <a>, removed <b-a>` (MENTION grain, summed mention_count over every tested pair);
   - `R31 PAIRS REMOVED: <p>` (pairs whose count falls to 0) and `R31 PAIRS COUNTED DOWN: <q>` (fell, not to 0);
   - `CVO ROWS: <x> of 14 removed`, where the 14 are the rows named in the CVO grade above;
   - `REMOVED SAMPLE 20:` 20 removed mentions spread over securities, each with article key, title and the 160 characters
     around the discarded match;
   - `KEPT SAMPLE 20:` 20 kept mentions on common-word securities, each with the anchor that kept it.
   No verdict: `3.0.0_SA_CVO` grades both samples.
6. Change no other file in `lib/research/harvest/` except a test that asserts a match this rule now discards. List each
   such change in your report.

## AMENDMENT 1 -- "common word" is measured from SILVER, not a dictionary (ADDENDUM 4, `1.0.0_SA_CTO~DELL1` msg 2353)

The first build's dictionary list (370,105 words) flagged 33 aliases, including Apple, Amazon, Meta, Roche, Boeing, Nike
and Intel. It removed 9,958 mentions, and the removed sample was mostly TRUE mentions. That definition is WITHDRAWN.
Continue on the same branch; its commits stay, and you change them forward.

1. **The common-word set is measured from silver.** For every alias of every security in the r75 list, count across all
   silver article titles and bodies (the same silver read the census uses):
   - LOWER: whole-word uses written all lower-case (`visa`, `orange`);
   - CAP_MID: whole-word uses with a capital first letter that stand MID-SENTENCE, meaning NOT the first word of a title
     or of a sentence. A sentence opens at the start of a block, or after `. `, `? `, `! ` or a line break.

   An alias is a COMMON WORD when LOWER > CAP_MID. Write `common_word_aliases.json` (security key, alias, LOWER, CAP_MID,
   articles scanned) into your deliverables folder. The matcher loads ONLY this file, by `_COMMON_WORD_LIST_PATH`. Remove
   the dictionary word list and its loader from the build: no file, no code path.
2. **Before the census, print `COMMON-WORD ALIASES (silver): <n> over <s> securities; articles scanned <a>`.** Then print
   every flagged alias with its LOWER and CAP_MID counts, and then the 10 nearest misses (the highest LOWER / CAP_MID
   ratio among those NOT flagged).
3. **The census as before**, at mention grain, plus these lines:
   - `CVO ROWS: <x> of 14 removed` -- it must read 14 of 14;
   - `BRAND CHECK:` -- every flagged alias that is also a company's ordinary trading name, printed for the CVO. It is not
     a verdict, and the CTO STOPs on a plainly-brand name.
4. Tests: replace the dictionary fixture with a fixture `common_word_aliases.json`; (i) through (iv) stand. Add (vi): an
   alias with LOWER <= CAP_MID is not common and counts with no anchor. (v) becomes: a missing list path raises.
5. The eight existing test files that set the switch False: keep that only where the fixture alias is flagged under the
   NEW definition. Otherwise remove it. List which you kept.

## AMENDMENT 2 -- flag at LOWER / CAP_MID >= 0.2 (ADDENDUM 5, `1.0.0_SA_CTO~DELL1` msg 2380)

AMENDMENT 1's strict test (LOWER > CAP_MID) flagged 0 of 413 aliases over 20,908 articles, so CVO ROWS read 0 of 14. That
test is replaced. Everything else in AMENDMENT 1 stands: the counts, the file, the loader, the tests and the census lines.

1. **An alias is a COMMON WORD when LOWER / CAP_MID >= 0.2**, with CAP_MID = 0 counting as flagged when LOWER > 0. Put the
   threshold in one module constant, `_COMMON_WORD_RATIO = 0.2`. The silver measure says this flags Booking, Cadence,
   Orange (both listings) and Visa: the break sits before Waste Management at 0.17. Print the flagged list with counts and
   ratio, plus the 10 nearest misses, exactly as before.
2. **The census** adds, for EACH flagged alias, `REMOVED SAMPLE <alias>: 10`: ten removed mentions chosen by (article
   key ascending, every k-th), each with article key, title and the 160 characters around the discarded match. This
   replaces the 20-row mixed sample. The CTO STOPs an alias whose removals are mostly true company mentions; look hardest
   at Booking and Cadence. No verdict from you.
3. **`CVO ROWS: <x> of 14 removed`** must read 14 of 14. If it does not, report it and do not tune the rule.
4. **Tests:** add (vii): an alias at ratio exactly 0.2 is flagged, and one at 0.19 is not, with the constant patched.
   Re-check the eight switch-False files under this definition (keep the switch-False fixture only where the fixture alias
   is now flagged), and list which you kept.

## AMENDMENT 3 -- the second anchor widens, with two guards (ADDENDUM 6, `1.0.0_SA_CTO~DELL1` msg 2405)

AMENDMENT 2 flagged 5 aliases and removed CVO 14 of 14, but its removed samples read 90-100% TRUE (Visa 10/10). The cause
is thin anchors (row D1-W132-S3). AMENDMENTS 1 and 2 stand, including the 0.2 ratio. Only the second anchor changes.

1. **A second anchor is ANY of:**
   - (A) the ticker from the security key (the symbol before the first `_`, e.g. `V` from `V_US_Equity`), and any stored
     ticker forms;
   - (B) the company string with its legal suffix stripped, using the same suffix list the collector uses
     (`publishers._LEGAL_SUFFIX`), e.g. "Booking Holdings";
   - (C) the full names held for the security in the identity file the collector reads (name the file and the field);
   - (D) the ticker of any sibling listing of the same issuer, by the existing issuer grouping, e.g. ORANY for ORA_FP;
   - (E) another alias of the same security that is not itself common (as before).
2. **Guard (a):** a ticker of ONE or TWO letters anchors only in a ticker form -- `(V)`, `( V )`, `NYSE: V`, `NASDAQ: V`,
   `OTC: V` or `$V` -- never as a bare word.
3. **Guard (b):** a stripped name or full name that EQUALS the common alias itself (Cadence) is not an anchor.
4. **The census:** re-run it exactly as AMENDMENT 2 specifies, adding per flagged alias `ANCHORS USED:` counts by kind
   (A to E) over its KEPT mentions. `CVO ROWS` must still read 14 of 14 -- if not, report it and do not tune. The four
   REMOVED SAMPLE blocks are re-drawn the same way.
5. **Tests:** add (viii) "Visa ( V ) rose" anchors via (A); (ix) the bare word "V" does not anchor; (x) "Booking
   Holdings said" anchors Booking via (B); (xi) a stripped name equal to the alias does not anchor; (xii) ORANY anchors
   ORA_FP via (D).

<paths>
lib/research/harvest/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~132/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bt-1"><invocation>python -m pytest lib/research/harvest/test_bt1_common_word_second_anchor.py -q</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bt-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~132/bt1_census.out</invocation><expect>R31 MENTIONS: before \d+, after \d+, removed \d+</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bt-1"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q</invocation><expect> passed</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-bt-1" judgment="true"/>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression.
- AC4 (CVO): both census samples graded; the common-word list read for words wrongly caught (a brand that is a word but
  should stay distinctive) or missed.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-D1-W132-S1`. Its commit
  needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310);
  this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~132/AMGT_HARVST.TO-HVST-bt-1.a-common-word-alias-needs-a-second-anchor.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bt-1.a-common-word-alias-needs-a-second-anchor`. Pin every artifact row to its commit.
- Run every command from the repo root of YOUR worktree, with `PYTHONPATH=.`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 2333, `ledger/ROUND_ANALYSIS.round74.md` ADDENDUM 3 (R31). "It is cut as an HARVST
  round-76 cell, with the dry run, then its own served-rebuild pair, the same ladder as br-1 and #12."
- The word list: there is none in the repo, in the stdlib, in any installed package (nltk, wordfreq, enchant,
  spellchecker are absent), or in Git Bash (`/usr/share/dict` is absent). So the cell vendors a public-domain list, with
  its hash recorded. Egress off Bloomberg is open (law edit 4d77a9c3ea).
- <risk> SERVED: the merge changes what gold serves once rebuilt; the cell writes nothing served. Its merge takes its own
  never-widen pair, and gold serves R31 only after rebuild #13.
- **AMENDMENT 1 (2026-10-09 ~11:4xZ, issuer):** the first build is on origin `wk-AMGT_HARVST-132-r76` @b6fff70840. Its
  census (9,958 mentions removed over 33 dictionary-flagged aliases, mostly true mentions) was STOPPED by the issuer
  (msg 2350). `1.0.0_SA_CTO~DELL1` ruled ADDENDUM 4 @9c0f0d882a (msg 2353): common word = LOWER > CAP_MID in silver. The
  issuer amends this order in place (a re-cut into the first issuance), with the same criteria. Gate limb that graded it:
  to-pipeline-gate GATE (viii), on a MODIFIED order. Do not merge bt-1 until the CTO reads the new census.
- Slot ~132. Checks dry-run at the base: AC1 FAIL as expected (the test is absent); AC2 FAIL as expected (no such file);
  AC3 PASS as expected (base suite, read at the cut).

**COMPLETE 2026-10-09 ~12:5xZ (issuer `2.0.0_SA_COO~W1`) -- R31 MEASURED AND RETIRED, NOT SERVED:**

Every census ran on served rebuild #12 (205,470 mentions). The issuer checked each on the branch before routing it.

| cut | branch head | flagged | mentions removed | CVO rows | removed sample | ruling |
|---|---|---|---|---|---|---|
| dictionary (words_alpha) | @b6fff70840 | 33 aliases | 9,958 | 14/14 | mostly true | issuer STOP, msg 2350 |
| AMENDMENT 1, LOWER > CAP_MID | @5086c69a0b | 0 | 0 | 0/14 | -- | msg 2378 |
| AMENDMENT 2, ratio >= 0.2 | @4898fd0c6e | 5 aliases | 2,716 | 14/14 | Visa 10/10, others 9/10 true | msg 2403 |
| AMENDMENT 3, anchors A-E + guards | @fa9135694e | 5 aliases | 908 | 14/14 | Orange 10/10, Cadence 9/10, Visa 7/10, Booking 4/6 true | msg 2435 |

- **Ruled:** `1.0.0_SA_CTO~DELL1` ADDENDUM 7 (msg 2438). R31 is retired, Visa-only is refused too, and bt-1 stays UNMERGED
  as the record (`wk-AMGT_HARVST-132-r76` @fa9135694e on origin). The records alone (deliverables and rows) were drained
  @43019e178e, with the R31 code reverted on the records branch @c95384c001. lib/ and tests/ moved 0 lines (msg 2449, form (a)).
- The 14 Visa and Orange rows are a stated known residual in the coverage figure. Row D1-W132-S1 is dispositioned by
  this ruling.
- A re-open needs a per-mention method whose removed sample reads mostly false.
- **Proof:** VALID rc 0 at each head; the final AC1 is 25 passed, AC3 543 passed. **Rows:** D1-W132-S1 to S5.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>76</round>
<slot>~132</slot>
<fabric>dell1</fabric>
