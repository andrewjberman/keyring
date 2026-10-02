# AMGT_HARVST task order -- `HVST-aj-7` -- ROUND 37 CELL 7 (CTO track-C ruling msg 28509): `title` (VERBATIM) AND `published_precision` JOIN THE GOLD MENTION ROWS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants; no S3 write (served gold moves only at the issuer's rebuild #5 under its own never-widen pair); AC2 reads live silver read-only through a capturing client that sends no put.
comp-adversary: RUN at L5 -- the adversary is a title that is NOT verbatim (stripped, case-folded, unicode-normalised, truncated, or "" where silver has none), a published_precision taken from the wrong field, or a change that moves any pre-existing gold field (tier, counts, co-mentions) -- which would turn an additive change into a served-output change. Plants pin verbatim title (incl. a title with leading/trailing spaces, curly quotes and an em dash), null-not-empty, and every pre-existing field byte-identical on a fixture.
</preflight>

## 0. THE CELL

`lib/research/harvest/publication_gold.py` builds the gold mention rows: `GOLD_MENTION_SCHEMA` (around line 64) and
`build_mention` (around line 1026), with each row assembled around lines 280-300 from a silver article row that carries
`title` and `published_precision` (see `_TIMELINE_SILVER_COLUMNS` around line 926). The timeline day route
(AMGT_RESAPP) today reads those two fields from SILVER at request time. The CTO ruled they join the gold mention rows,
so the day route reads gold only.

## 1. THE BUILD (LOCAL)

1. Add `("title", pa.string())` and `("published_precision", pa.string())` to `GOLD_MENTION_SCHEMA`, as nullable
   fields appended after the existing ones. If silver types `published_precision` differently, use the silver type
   and say so in your report.
2. In `build_mention`, every mention row carries:
   - `title` = the silver article's `title` VERBATIM (no strip, no case change, no unicode normalisation, no
     truncation), or null when silver has none, never "";
   - `published_precision` = the silver article's `published_precision`.
   Nothing else in the row, the tiering or the co-mention logic changes. Optional: if `build_event` makes a second
   whole-silver title scan that the gold title now makes redundant, drop it. Change no output of `build_event` or
   `build_daily`.
3. Plants in `lib/research/harvest/test_aj7_gold_title_precision.py` (no network; fixture silver rows):
   - (i) a title with leading and trailing spaces, curly quotes, an em dash and non-ASCII letters comes through
     byte-identical;
   - (ii) a silver row with no title gives a null `title`, never "";
   - (iii) `published_precision` equals silver's for each value present in the fixture;
   - (iv) on the same fixture, every pre-existing field of every row is byte-identical to the builder's output before
     this change (a mutant that alters a tier or a count fails);
   - (v) the written parquet's schema carries both new fields.
4. The research suites that cover `publication_gold` stay green. Run `python -m pytest lib/research/harvest -q` and
   report the before and after counts.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r37e`, sparse cone per decomposition
section 50 (it includes `lib`). Do not touch any `.runtime` directory.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/test_aj7_gold_title_precision.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-7"><invocation>python -m pytest lib/research/harvest/test_aj7_gold_title_precision.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-7"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-7.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 runs the real builder over 5 securities against live silver through a capturing client, so nothing is sent. It
  needs the repo's AWS read path. Run it from your worktree; if it cannot read silver there, mark it "issuer re-runs
  at the base after merge".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-aj-7.title-precision-into-gold-mention.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-7.title-precision-into-gold-mention`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 28509 (track C = A; step 1 is HARVST's). Workstream goldheadline. Served gold moves only at
rebuild #5, an issuer act under a NEW never-widen pair: the COO half by this seat after a round-37 signing dry run
whose rule permits only the two added fields to differ, and the CTO half owed. RESAPP round 63 (step 2) follows the
rebuild.

**COMPLETE 2026-10-02 ~14:5xZ (issuer).** AC1 PASS: 6 passed. Merged @385f4a76cc. Its AC2 first FAILED on the barrons dict
titles (row Z-W90-S17; the base builder failed identically). After aj-8 and the re-derivation, AC2 PASSES at the base
(`deliverables/2.0.0_SA_COO_H/round37/aj-7.AC2.issuer_grade.txt`): 713 rows over 5 securities, title mismatches 0,
precision mismatches 0, PUTS SENT 0. `published_precision` is a string (silver values instant / second / minute).
Served gold moves at rebuild #5, under the new never-widen pair.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>37</round>
<workstream>goldheadline</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
