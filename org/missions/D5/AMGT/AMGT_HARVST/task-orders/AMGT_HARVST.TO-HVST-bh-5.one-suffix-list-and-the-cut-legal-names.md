# AMGT_HARVST task order -- `HVST-bh-5` -- ROUND 61 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): A LEGAL NAME CUT OFF INSIDE A CORPORATE SUFFIX LOSES THE FRAGMENT -- ONE SUFFIX LIST, EVERY CHANGED NAME PRINTED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~110</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a changed output for a security the rule does not name, a test with no negative control, a rule loosened to meet the census, a second list where the cell says one, or a gold build.
</preflight>

## 0. THE CELL

You are the second order of this slot's queue: `HVST-bh-4` (names from the identity registry) is merged into your base.

The collector's identity record cuts some company names at 30 characters (`LEGAL_NAME_EXACT_LENGTH` in
`lib/research/harvest/universe_securities.py`; reported, never altered today). Ten of its 234 names are exactly 30 long and
five are visibly cut: `AIG_US_Equity` "American International Group I", `KCDMY_US_Equity` "Kimberly-Clark de Mexico SAB d",
`ICT_US_Equity` "International Container Termin", `OMAB_US_Equity` and `OMAB_MM_Equity` "Grupo Aeroportuario del C...". A cut
name is an alias no article carries.

The module's suffix words live in `CORPORATE_SUFFIXES` (ordered longest first). `_FORM_WORDS` is derived from it.

The rule this cell lands: **a legal name is cut at a suffix on that ONE list and nowhere else.**

## 1. THE BUILD (LOCAL)

1. **The fragment rule** (`universe_securities.py`), applied to a name taken from the identity map ONLY, after
   `clean_legal_name`, and only when the ORIGINAL map value is exactly `LEGAL_NAME_EXACT_LENGTH` characters:
   - the name ENDS IN A SUFFIX FRAGMENT when, for some suffix S in `CORPORATE_SUFFIXES` (tried in the tuple's order), the name
     ends with a space followed by a PROPER, non-empty prefix of S, compared case-sensitively, and the name does not already
     end in a whole listed suffix at that place ("Group I" is a fragment of "Group Inc"; "SAB d" of "SAB de CV"; a name ending
     " Co" ends in a whole suffix and is NOT a fragment);
   - the fragment and the space before it are dropped, and the shortened name is the company name from there on
     ("American International Group", "Kimberly-Clark de Mexico"); it then takes the usual alias path;
   - a 30-character name that ends in no fragment is left exactly as it is ("International Container Termin") and is listed.
2. **One list.** The rule reads `CORPORATE_SUFFIXES` and nothing else. Add no second tuple, set or regex of suffix words; if
   you find one in this module that is not derived from `CORPORATE_SUFFIXES`, do not change it: name it in your report.
3. The summary gains `legal_names_cut_in_suffix` (`{security_key, original, fragment, name}` per changed name) and
   `legal_names_exact_length_unchanged` (`{security_key, original}`).
4. A security whose map value is not exactly 30 characters returns a dict byte-equal to today's.
5. **Plants** `lib/research/harvest/tests/test_bh5_cut_legal_names.py` (no network), on fixture maps:
   - (i) "American International Group I" gives company "American International Group";
   - (ii) "Kimberly-Clark de Mexico SAB d" gives "Kimberly-Clark de Mexico";
   - (iii) THE NEGATIVE CONTROL: "International Container Termin" is unchanged and listed as unchanged;
   - (iv) a 30-character name ending in a WHOLE suffix (build one, e.g. ending " Holdings Inc") is not treated as a fragment;
   - (v) a 29-character and a 31-character name ending " I" are unchanged (the rule keys on the exact length);
   - (vi) a pool name of 30 characters ending " I" is unchanged (map names only);
   - (vii) the mutant: with the exact-length condition removed, (v) changes -- assert that, so the control is shown to bite.
6. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh5_census.py`: BEFORE = `build()` with the fragment rule off (stated
   in the file how); AFTER = as you leave it. Over every latest silver article with the real `pg._security_mentions`:
   - `DENOMINATOR: identity records <R>, names of exactly 30 characters <n>, securities <S>, silver articles <N>`;
   - per 30-character name: `<security_key> original=<...> -> name=<...> | UNCHANGED`, with its aliases before and after;
   - `CHANGED: <k> of <n>`; per changed security `pairs before <p0> after <p1>; mention_count before <m0> after <m1>`;
   - `OTHER SECURITIES CHANGED: <c> of <S>`;
   - last line `CENSUS OK` only if N > 0, n > 0, the AIG and KCDMY names read as in plants (i) and (ii) when those keys are on
     the list (print `NOT ON THE LIST` for one that is not), no changed security lost a pair, and OTHER SECURITIES CHANGED
     is 0; otherwise `CENSUS FAIL` and the failing line. Write the output as `bh5_census.out`.
7. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold. The collector
   (`lib/opal_data_harvest`) is not changed: two legs are running from it.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/opal_data_harvest/config.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-5"><invocation>python -m pytest lib/research/harvest/tests/test_bh5_cut_legal_names.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh5_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bh-5"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W110-S2`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/AMGT_HARVST.TO-HVST-bh-5.one-suffix-list-and-the-cut-legal-names.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-5.one-suffix-list-and-the-cut-legal-names`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 75.
- R5: "One cell, one suffix list: a legal name is cut at a suffix on that list and nowhere else; the cell prints every name it
  changes." Row AMGT_HARVST-Z-S96.
- **Issuer rulings inside the decomposition** (no gate limb graded them): the rule drops the FRAGMENT and completes nothing (an
  "I" could be Inc, Inc. or Incorporated); it keys on the record's exact cut length, so an uncut name ending in a short word is
  not touched; the one list is the gold module's `CORPORATE_SUFFIXES`; the collector's own slug word list is left alone this
  round because two legs run from that package.
- Slot ~110's queue, second. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as
  expected (no such file); AC3 base PASS as expected (419 passed).

**COMPLETE 2026-10-08 ~01:5xZ (issuer):**
- **Built:** worker ~110 (re-seated) @2b22e36e05; merged @92c37b7e31 (6 paths, index check 0 of 6 differ).
- **AC1 PASS:** 8 of 8. **AC2 PASS:** CENSUS OK (234 identity records, 10 names of exactly 30 characters, 19,043 articles):
  changed 2 of 10 -- AIG "American International Group" (fragment `I`), KCDMY "Kimberly-Clark de Mexico" (fragment `SAB d`);
  8 unchanged, ICT's cut name among them; AIG pairs 16 to 16, mention count 23 to 35; other securities changed 0 of 242.
  **AC3 PASS:** 435 on the branch.
- **Issuer ruling on row Z-W110-S3 (no gate limb graded it):** where several suffixes offer a fragment the SHORTEST is dropped, so
  "Group" stays; that is the reading plant (i) fixes and the face's "tried in the tuple's order" was loose.
- **Row Z-W110-S2:** the face named the two OMAB names as visibly cut; "Grupo Aeroportuario del Centro" is a whole 30-character
  name and is left alone. Visibly cut are 3 (AIG, KCDMY, ICT), not 5; row Z-S96's count is corrected by this.
- **Reported, not changed:** `_FORM_WORDS` adds SPA, SE, LP, LLC beside the list; the fragment rule does not read them.
- **Existing assertion changed:** none.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>61</round>
<slot>~110</slot>
<fabric>site-z</fabric>
