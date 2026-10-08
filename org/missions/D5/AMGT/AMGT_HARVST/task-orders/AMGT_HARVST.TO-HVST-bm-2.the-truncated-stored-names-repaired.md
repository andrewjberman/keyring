# AMGT_HARVST task order -- `HVST-bm-2` -- ROUND 68 (`1.0.0_SA_CTO~Z` msg 31637 (R19, R20), on `4.0.0_SA_CRO~Z`'s research `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_STANDING_COLLECTION_AND_DAILY_SWEEP_RESEARCH_20261008.md` @2394cfc3d8): AIG'S TRUNCATED STORED NAME REPAIRED IN THE NEW IDENTITY FILE, AND EVERY OTHER NAME CUT THE SAME WAY PRINTED -- NOTHING FETCHED, NO CONFIG CHANGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~120</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL files and scripts, plus READ-ONLY reads (S3 GET of the pool universe and the crosswalk object). NO put, NO delete, NO job, NO collector, backfill_driver or emitter run, NO vendor, publisher or Bloomberg call. `lib/opal_data_harvest/config.json` is NOT changed: one collection leg is LIVE and reads the two round-47 files it names. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a round-47 file edited in place, a config pointer moved, a name completed by guessing, a record added from a source that does not carry it, or a job run to test the result.
</preflight>

## 0. THE CELL

You are the second order of this slot's queue: `HVST-bm-1` is built on your branch. Its new files
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/rank_universe_20261008.json` and `rank_universe_identity_20261008.json` are the ones you edit. The round-47 files
and `lib/opal_data_harvest/config.json` stay untouched.

The collector's identity record stores `AIG_US_Equity`'s company as "American International Group I": 30 characters, cut
inside the word "Inc". No headline carries that string, and AIG's six collection jobs returned nothing. Ten of the 234
stored names are exactly 30 characters long. The gold side already repairs this for its own list
(`lib/research/harvest/universe_securities.py`, `HVST-bh-5`: `suffix_fragment`, `cut_legal_name_fragment`,
`CORPORATE_SUFFIXES`, `LEGAL_NAME_EXACT_LENGTH`); read it. The collector reads the stored name itself: see
`lib/opal_data_harvest/publishers.py` (`slug_query`, `slug_queries`) and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/build_rank_identity.py`.

## 1. THE BUILD (LOCAL)

1. **Every name cut the same way, printed first.** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/bm2_truncated_names.py` prints
   `DENOMINATOR: identity records <n>, company values of exactly 30 characters <k>` and, for each of the k: security_key,
   the stored value, whether it is CUT (ends in a fragment of a corporate suffix by the gold side's own function, imported
   and called, not copied), CUT WITH NO SUFFIX FRAGMENT (a 30-character value that is visibly not a whole name; say what
   makes it so, or `WHOLE` when it is a complete name), and the full name a STORED source gives for that key if one does
   (the pool record's name, `lib/research/identity/registrations.json` `identity.name`), with that source named.
2. **The repair, in your two new files only.** For a record whose stored company is CUT:
   - where a stored source carries the full name for that exact key, the record takes it, with the field's status and
     evidence saying where it came from;
   - else, where the value ends in a suffix fragment, the fragment is dropped (the gold side's rule) and the status says so;
   - else the value is left as it is and listed as `CUT, NOT REPAIRED`.
   The record's search forms (aliases, slug words) are rebuilt from the repaired name by the builder's own rules. Nothing
   is completed by guessing.
3. Print `REPAIRED: <r>` with before and after for each (company, aliases, and what `publishers.slug_query` or the function
   the collector uses returns for the old and the new string, called locally); `CUT, NOT REPAIRED: <u>` with each;
   `OTHER RECORDS CHANGED: <c>` (must be 0).
4. **Plants** in `lib/opal_data_harvest/test_bm2_truncated_names.py` (no network): (i) the new file's `AIG_US_Equity` company
   is not the 30-character cut string and its slug words are words a headline about AIG could carry (assert the exact
   strings you produce); (ii) THE NEGATIVE CONTROL: the round-47 file still holds "American International Group I";
   (iii) a 30-character WHOLE name ("Mitsubishi UFJ Financial Group") is unchanged; (iv) a cut value with no stored full
   name and no suffix fragment is unchanged and is in the not-repaired list; (v) the collector's loader accepts the file.
5. Last line: `REPAIR OK` only if k > 0, `AIG_US_Equity` is among REPAIRED, and OTHER RECORDS CHANGED is 0. Otherwise
   `REPAIR FAIL` and the failing line. Write the output as `bm2_truncated_names.out`.
6. Run no job to see whether the repaired name finds articles: that is a call on a publisher and waits on Andrew's word.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/
lib/research/identity/
lib/research/harvest/universe_securities.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bm-2"><invocation>python -m pytest lib/opal_data_harvest/test_bm2_truncated_names.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bm-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/bm2_truncated_names.out</invocation><expect>REPAIR OK</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W120-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/AMGT_HARVST.TO-HVST-bm-2.the-truncated-stored-names-repaired.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bm-2.the-truncated-stored-names-repaired`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31637 (R19, R20), on `4.0.0_SA_CRO~Z`'s research `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_STANDING_COLLECTION_AND_DAILY_SWEEP_RESEARCH_20261008.md` @2394cfc3d8. Decomposition section 82.
- R20 (b): "repair AIG's truncated stored name and print every other name cut the same way. A run for any of them waits on
  Andrew's per-use word."
- The repair lands in the NEW dated identity file of `bm-1`, not in the file the live leg reads (the issuer's ruling recorded on
  `bm-1`). What AIG's six jobs asked for (the withdrawn `bl-2`) is answered here in part: item 3 prints the query the collector
  derives from the old string and from the new one.
- Slot ~120's queue, second. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as
  expected (no such file).

**COMPLETE 2026-10-08 ~09:3xZ (issuer):**
- **Built:** worker ~120 (re-seated) @6c9eb0eab5; merged with `bm-1` @1b2e841422.
- **AC1 PASS:** 6 of 6. **AC2 PASS:** REPAIR OK. Package suite on the branch: 756 passed, 3 skipped.
- **The ten 30-character stored names:** 5 WHOLE (AEP, BBSEY, BIPC, JBHT, 8306 JP); 2 CUT in a suffix fragment and REPAIRED in
  the new identity file -- AIG "American International Group I" to "American International Group", KCDMY "Kimberly-Clark de
  Mexico SAB d" to "Kimberly-Clark de Mexico"; 3 CUT, NOT REPAIRED -- `ICT_US_Equity` "International Container Termin" and
  the two OMAB lines "Grupo Aeroportuario del Centro" (no stored source carries a fuller name and there is no suffix
  fragment to drop). OTHER RECORDS CHANGED: 0.
- **What AIG's jobs asked for (the withdrawn `bl-2`'s question):** the collector derived its query from the stored string, so
  it asked for "American International Group I". From the repaired name it derives "American International".
- **Stated, not fixed:** "American International" is a two-word query that could return other companies; no job has been run
  with it. "Centro" is a real word, so OMAB's cut is the rule's reading, not proof.
- **Existing assertion changed (1):** `test_bm1_identity_records.py` test i now excepts the two repaired records.
- **Row Z-W120-S3 (ARMED, this seat's):** re-running `bm1_three_universes.py` rebuilds the identity file and would revert both
  repairs while still printing RECONCILE OK. **Issuer ruling, the disarm:** `bm1_three_universes.py` is NOT re-run; the
  order of acts is bm1 then bm2, once, and it is done. The next cell that touches these files folds the repair into the
  builder so one script yields the repaired file; until then the row stays open for `3.0.0_SA_CVO~Z`'s remediation record.
- **Not done, by ruling:** the config pointer is not moved to the new files, and no job is run for any added or repaired name;
  a run waits on Andrew's per-use word.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>68</round>
<slot>~120</slot>
<fabric>site-z</fabric>
