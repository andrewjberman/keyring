# AMGT_HARVST task order -- `HVST-bq-2` -- ROUND 73 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): A FETCHED ARTICLE IS ACCEPTED ON THE STRINGS THE COLLECTOR SEARCHED WITH, NOT ON THE FULL STORED NAME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bq-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~125</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, tests and one table. NO S3 call, NO job, NO collector, backfill_driver or emitter run, NO vendor or publisher call. `lib/opal_data_harvest/config.json` and the identity files are NOT changed. Collection legs are LIVE from the shared tree; this branch is NOT merged while any leg runs.
comp-adversary: RUN at L5 -- the adversary is an acceptance that drops an article today's rule accepts, a form matched inside a longer word, a change to what is SEARCHED, an alias edited to make a test pass, or a job run to see what happens.
</preflight>

## 0. THE CELL

Your branch is CLOUD with `wk-AMGT_HARVST-123-r71` @537ac56e9b merged in. That branch is NOT on CLOUD yet; it carries
cells `HVST-bo-1` and `HVST-bp-1`: `publishers._query_override`, `slug_queries` returning a stored override when the
security carries `query_override`, `listing_label`, and the worker's `QueryOverrideMalformed` handling. Read them first.

The fault (row AMGT_HARVST-Z-S104). The collector SEARCHES a publisher with `slug_queries(security)`: the company string
and each alias with trailing legal-form words dropped ("Bloom Energy Corp" -> "Bloom Energy"). It then ACCEPTS a fetched
body only if some stored alias appears whole in the title plus text (`lib/opal_data_harvest/publishers.py`, the block that
appends `company_not_mentioned`, about line 145): `aliases = security.get("aliases") or [security["company"]]`, each
matched with `(?<!\w)` + alias + `(?!\w)`, case-insensitive. For 149 of the 242 covered names every alias ends in a
legal-form word, so an article headed "Bloom Energy Raises Outlook" is fetched and rejected. Over four days of job files
the Wall Street Journal kept 152 such articles and rejected 1,807 for that reason alone.

## 1. THE RULE (`1.0.0_SA_CTO~Z` R25 as amended by R27)

**Acceptance uses the strings `slug_queries(security)` returns, each matched whole-word and CASE-INSENSITIVELY, in the title
plus text.** Not the aliases. Case-insensitive because nine names are stored in capitals (NVIDIA, QUALCOMM, CATERPILLAR)
and a body says "Nvidia". Acceptance is the recall stage: the body is already fetched, and the gold matcher decides the
pair later.

## 2. THE BUILD (LOCAL; on your branch, which is not merged while a leg runs)

1. In `publishers.py`, one small helper returns the acceptance strings of a security: `slug_queries(security)`, and when
   that is empty the old strings (`security.get("aliases") or [security["company"]]`) so a security is never accepted on
   nothing. The `company_not_mentioned` block uses it. Nothing else in that function changes: the other issues
   (`publisher_did_not_unlock_body`, `short_or_partial_body`, and the rest) are untouched, and so is every caller.
   A malformed override must not raise from here in a way `bp-1` did not already contain: say in your report which path a
   malformed override takes through acceptance, and show it by one plant.
2. `lib/opal_data_harvest/test_bq2_acceptance_forms.py`, no network, using the fixtures the package's tests use:
   (i) alias "Bloom Energy Corp", body says "Bloom Energy" and never "Corp": ACCEPTED (no `company_not_mentioned`);
   (ii) THE NEGATIVE CONTROL: the same security, a body of the same length that never names the company: REJECTED with
   `company_not_mentioned`; (iii) stored company "NVIDIA", body says "Nvidia": accepted; (iv) whole word: company
   "Target Corp", body says only "targeted" and "retargeting": rejected; (v) a security carrying a well-formed
   `query_override`: accepted on the override's string, and NOT accepted on the derived string the override replaced;
   (vi) the mutant: with the helper returning the old strings, (i) fails.
3. THE PROOF TABLE, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~125/bq2_acceptance_table.py` writing `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~125/bq2_acceptance_table.out`, over every security
   `lib.opal_data_harvest.__main__.universe(load_config())` yields on your branch (242): the OLD acceptance strings and the
   NEW ones, side by side. For each security, check that EVERY old string contains, whole-word and case-insensitively, at
   least one new string: when that holds for all, every body the old rule accepted is accepted by the new one, by
   construction. The last lines of the output, exactly in this shape:
   `CHANGED <n> of 242`, `SUPERSET <m> of 242`, then `ONE-WORD FORMS <k>:` followed by every new string that is a single
   word, with its security key, sorted. If SUPERSET is not 242 of 242, list each failing security with both string sets
   and STOP there: do not weaken the check, file a row.
4. Do not change `_LEGAL_SUFFIX`, `slug_query`, `slug_queries`, `discovery._matches`, `config.json`, any identity file or
   any alias. Run no job.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~125/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bq-2"><invocation>python -m pytest lib/opal_data_harvest/test_bq2_acceptance_forms.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bq-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~125/bq2_acceptance_table.out</invocation><expect>SUPERSET 242 of 242</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bq-2"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W125-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~125/AMGT_HARVST.TO-HVST-bq-2.acceptance-on-the-searched-strings.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bq-2.acceptance-on-the-searched-strings`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.


## AMENDMENT 1 (2026-10-08 ~18:1xZ, the issuer `2.0.0_SA_COO~H`, inside its own decomposition; no gate limb graded it)

The first build reported `SUPERSET 225 of 242`: `slug_query` keeps only letters and digits, so for 17 names the stripped
string is not inside the stored alias ("Johnson & Johnson" -> "Johnson Johnson", "AT&T Inc" -> "AT T", "Coca-Cola Co/The"
-> "Coca Cola Co The"), and an article the old rule accepted is rejected. Row AMGT_HARVST-Z-W125-S1 is DISARMED by this
amendment. The rule is now:

1. **The acceptance strings of a security are the UNION of `slug_queries(security)` and the old strings
   (`security.get("aliases") or [security["company"]]`), in that order, without repeats; each matched whole-word and
   case-insensitively.** Every body the old rule accepted is then accepted by construction, which is the property
   `1.0.0_SA_CTO~Z` R27 names. `slug_query`, `slug_queries`, the aliases and `_LEGAL_SUFFIX` stay untouched.
2. The proof table's superset check is unchanged and must now read `SUPERSET 242 of 242`; then print the `ONE-WORD FORMS`
   block as item 3 of section 2 says (new strings only, those not among the old). Plant (vi), the mutant, now returns
   the old strings alone and shows (i) failing.
3. Add one plant: (vii) "Johnson & Johnson" in a body, for a security whose alias is "Johnson & Johnson": accepted.
4. **The four failing package tests (row W125-S3).** Three of them were fixed on CLOUD at 4feb748dba (the issuer's own
   miss after the pointer moved). Merge CLOUD into your branch first (`git merge CLOUD`; resolve the surprise channel as a
   union of rows if it conflicts). The fourth, `test_bo1_query_override.py` `test_vi`, exists only on your branch (cell
   `bo-1`); if it still asserts the 234-name pointer, update that one assertion to the moved pointer with a comment citing
   Andrew-direct 2026-10-08 ~13:1xZ, and list it in your report.
5. **Row W125-S2 is ruled:** acceptance runs in every publisher's `normalize`, so a malformed override can now end a job on
   any leg. That is accepted: the `bp-1` handler in `Worker.run_job` contains it on every leg (one job, a named status, no
   cooldown). Show it once on a non-sitemap publisher (Seeking Alpha or Barron's) with the package's fakes.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 86.
- `1.0.0_SA_CTO~Z` R25 (msg 31831): "repair the ACCEPTANCE CHECK, not the aliases ... acceptance uses what slug_queries
  returned for that security"; proof before any merge: the acceptance strings for all 242 before and after, every article
  accepted today still accepted, and the one-common-word names listed. R27 (msg 31867): "case-sensitive" is WITHDRAWN;
  whole-word, case-insensitive; a superset of today's rule by construction. R26: no list of company names is kept.
- **Issuer ruling inside the decomposition** (no gate limb graded it): where `slug_queries` is empty the old strings stand.
- **Stacked on the unmerged query-override branch** (537ac56e9b), because acceptance must honour a stored override. The
  signed pair for that branch's merge names 537ac56e9b; this cell's commits sit on top and need their own pair, or one new
  pair covering all three cells. The merge is HELD while any collection leg runs. Nothing is re-collected on this cell:
  re-collection is Andrew's word.
- <risk> SERVED. Chain of one, slot ~125. **Checks dry-run at the base (CLOUD + 537ac56e9b):** AC1 base FAIL as expected
  (the test is absent); AC2 base FAIL as expected (no such file); AC3 base PASS as expected (787 passed, 3 skipped on
  537ac56e9b, the bp-1 worker's run).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>

COMPLETE 2026-10-08 ~22:5xZ (issuer 2.0.0_SA_COO~H): worker ~125 reseated 21:2xZ after the issuer's session ended; @80a9b98fc0 (AMENDMENT 1 build) and @09642610bd (proof), on wk-AMGT_HARVST-125-r73. Re-run by the issuer from the worktree: AC1 12 passed; AC2 'CHANGED 158 of 242', 'SUPERSET 242 of 242', 'ONE-WORD FORMS 67:'. Worker's AC3 799 passed, 3 skipped. Rows Z-W125-S4 (DISMISSED by the worker: AMENDMENT 1 closes S1-S3) and Z-W125-S5 (test_vi's second assertion now names AIG, the one security bo-1 gave an override: RULED correct by the issuer). NOT MERGED: the branch carries bo-1 and bp-1 (537ac56e9b) and changes what the collector accepts; per section 86 it merges after gold (R26/R30) under its own pair, and not while a leg runs from the shared tree.
<status>complete</status>
<round>73</round>
<slot>~125</slot>
<fabric>site-z</fabric>
