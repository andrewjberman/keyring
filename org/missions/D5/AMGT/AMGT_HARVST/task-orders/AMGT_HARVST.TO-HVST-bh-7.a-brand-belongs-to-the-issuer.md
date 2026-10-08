# AMGT_HARVST task order -- `HVST-bh-7` -- ROUND 62 (`1.0.0_SA_CTO~Z` msg 31493, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 1 @c75d056652): TWO LISTINGS OF ONE ISSUER MAY BOTH CARRY ITS BRAND -- THE BRAND REFUSAL HOLDS BETWEEN DIFFERENT COMPANIES ONLY; ASML IS THE CASE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-7</owned_cells>
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

You are the fourth order of this slot's queue: `HVST-bh-4`, `HVST-bh-5` and `HVST-bh-3` are merged into your base.

`lib/research/harvest/universe_securities.py` `brand_refusal(brand, owner_key, forms_by_key, rule)` limb (a) refuses a whole
brand for a security when ANY OTHER security already carries that word as its company name or an alias. That is right
between two companies. It is wrong between two listings of one company: `ASML_NA_Equity`'s company name is now `ASML`, so the
brand `ASML` is refused for `ASML_US_Equity` (company `ASML Holding NV`), and at the last gold rebuild the mention count fell
on 2 served rows of `ASML_US_Equity` (row AMGT_HARVST-Z-W107-S2).

The ruling: **a brand belongs to the ISSUER. The refusal that stops one brand matching two securities holds between
different companies only.**

Seven ticker roots have two listings on the 242-name list: ASML (NA, US), AZN (LN, US), GSK (LN, US), ICT (PM, US), OMAB (MM,
US), RIO (LN, US), TTE (FP, US).

## 1. THE BUILD (LOCAL)

1. **One issuer** (`universe_securities.py`, a pure function with a docstring). Two securities are listings of ONE ISSUER when:
   - (1) `lib/research/identity/registrations.json` gives both the same non-empty `identity.lei`; or
   - (2) they share a ticker root (the part of `security_key` before its first `_`) AND, casefolded, one's company name equals
     the other's company name or one of the other's `suffix_forms`.
   Nothing else groups two securities. A shared root alone does not.
2. **The refusal.** In limb (a), a security of the SAME ISSUER as the owner is skipped exactly as the owner is. Limb (b) and
   every other path are unchanged. The docstring's ASML sentence is corrected to say how it now holds.
3. The summary gains `issuer_groups` (each a list of security keys, with the limb that grouped them) and
   `listings_sharing_a_root_not_grouped` (the keys and both company names).
4. A security in no group returns a dict byte-equal to today's.
5. **Plants** `lib/research/harvest/tests/test_bh7_brand_belongs_to_the_issuer.py` (no network):
   - (i) two listings grouped by limb (2) (`ASML` and `ASML Holding NV`, root ASML) both carry the brand `ASML`;
   - (ii) THE NEGATIVE CONTROL: two DIFFERENT companies where one's name is the other's brand still refuse, as today;
   - (iii) two securities with a shared root and unrelated names are not grouped and still refuse;
   - (iv) two securities with the same registry `lei` and different roots are grouped by limb (1);
   - (v) an empty or missing `lei` groups nothing;
   - (vi) the mutant: with the grouping switched off, (i) refuses the brand for the second listing -- assert that.
6. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh7_census.py`: BEFORE = `build()` with the grouping off (stated in the
   file how); AFTER = as you leave it. Over every latest silver article with the real `pg._security_mentions`:
   - `DENOMINATOR: securities <S>, ticker roots with two or more listings <r>, silver articles <N>`;
   - per such root: the listings, both company names, `GROUPED by limb <1|2>` or `NOT GROUPED: <why>`;
   - `BRAND REFUSALS: before <b0> after <b1>` and each one that changed;
   - per security whose alias set changed: aliases before and after, `pairs before <p0> after <p1>`,
     `mention_count before <m0> after <m1>`;
   - `PAIRS LOST: <l>` over all securities; `SECURITIES CHANGED OUTSIDE A GROUP: <c>`;
   - last line `CENSUS OK` only if N > 0, the brand `ASML` is in `ASML_US_Equity`'s aliases after, PAIRS LOST is 0, and
     SECURITIES CHANGED OUTSIDE A GROUP is 0; otherwise `CENSUS FAIL` and the failing line. Write `bh7_census.out`.
7. If the S3 read is refused or returns 0 articles: BLOCKING row, stop on AC2. Build no gold.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/publication_gold.py
lib/research/harvest/whole_brand_aliases.json
lib/research/identity/registrations.json
lib/research/harvest/tests/
lib/opal_data_harvest/test_az1_alias_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-7"><invocation>python -m pytest lib/research/harvest/tests/test_bh7_brand_belongs_to_the_issuer.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh7_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bh-7"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W110-S4`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/AMGT_HARVST.TO-HVST-bh-7.a-brand-belongs-to-the-issuer.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-7.a-brand-belongs-to-the-issuer`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31493, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 1 @c75d056652. Decomposition section 76. Cut as round 62 because `.tools/to-pipeline-gate.py` admits one issuance per round and round 61's was committed (@fcf5542a36) minutes before the addendum; the analysis names these two as round 61's items 7 and 8.
- R8: "the builder groups listings by issuer before it applies that refusal; its check names ASML's two listings as the real case
  and prints every other pair of listings the change affects, with 0 pairs lost elsewhere. It disarms the row." Row
  AMGT_HARVST-Z-W107-S2 (ARMED, disarm_owner this seat): disarmed when this cell's change is in a served rebuild; the CVO's
  remediation row records it.
- **Issuer ruling inside the decomposition** (no gate limb graded it): one issuer is an equal registry LEI, or a shared ticker
  root with one company name equal to the other's name or suffix form. The registry carries 67 of the 242 securities and neither
  ASML listing, so limb (2) is what groups the real case; a shared root alone groups nothing (ICT PM and ICT US stay apart on
  their names as they stand).
- Slot ~110's queue, fourth. `whole_brand_aliases.json` is in `<paths>` to be read; this cell adds no entry to it.
- **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected (no such file);
  AC3 base PASS as expected (419 passed).

**COMPLETE 2026-10-08 ~03:0xZ (issuer):**
- **Built:** worker ~110 (re-seated) @6366640582; merged @7e75953bf3 (6 paths, index check 0 of 6 differ).
- **AC1 PASS:** 8 of 8. **AC2 PASS:** CENSUS OK over 19,049 articles: 7 roots with two listings, 5 grouped by limb 2 (ASML, AZN,
  GSK, OMAB, RIO), 2 not (ICT: 'International Container Terminals' against the cut 'International Container Termin'; TTE:
  'Total Energies' against 'TotalEnergies SE'); limb 1 grouped nothing (the registry holds one listing per root). Brand
  refusals 1 to 0: `ASML` is back on `ASML_US_Equity`, pairs 582 to 582, mention count 2820 to 2822. Pairs lost 0; securities
  changed outside a group 0 of 242. **AC3 PASS:** 468 on the branch; the issuer's drain check is in this close's commit message.
- **Row Z-W107-S2 (ARMED, this seat's to disarm):** the cause is removed in code; it is disarmed when this change is in a served
  rebuild, which the next never-widen pair carries. **Row Z-W110-S5** (ICT and TTE not grouped; nothing lost today).
- **Existing assertion changed:** none.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>62</round>
<slot>~110</slot>
<fabric>site-z</fabric>
