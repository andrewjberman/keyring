# TO NFRA_SCHWABBF.TO-BF-r1 -- thread hop 3b: the readers that parse the old grammar by hand follow the shared function

<to_id>NFRA_SCHWABBF.TO-BF-r1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-1` (`decompositions/NFRA_SCHWABBF_DECOMP.md`) |
**outcome_ref:** FWD-4, FWD-5 | **depends_on:** `TO-BF-k1` (merged in your worktree before this order starts; it is earlier in your queue)

---

## WORKER FACE

### THE CELL

`BF-r-1`, PRD contract C-READERS: "Every reader and writer of the old form changes in the same release as the move." A reader that parses the old grammar by hand and is missed reads an empty prefix and reports
"nothing to do". FWD-5 ACCEPT: "nobody can find a holdings, balance or activity figure for an already stored day that differs from the day before."

**What exists (read it).** The issuer's census of the old grammar (31 files, native Grep, decomposition file) found two readers that build the old layout themselves instead of calling the shared function; every other reader follows `TO-BF-k1`'s function with no edit.
- `data/canonical/schwab/build_canonical_daily.py`: line 63 `MONOLITH_FEED_PREFIX = f"schwab/{CANON_MASTER}/bronze/{CANON_FEED}/"`; line 141 and nearby list "8-digit partition DIRECTORY names (YYYYMMDD)" under that prefix; the comment near line 186 about files "unreadable via monolith_bronze_key".
- `data/canonical/schwab/silver/build_fact_tax_1099div.py`: line 74 `prefix = f"schwab/{MASTER}/bronze/tnn/"` and the date parsing that follows it; line 87 already calls `monolith_bronze_key`.
- `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`: its fixture and assertions describe the old layout (lines ~10, 119, 203).
- The shared function and listers are `TO-BF-k1`'s, in `data/canonical/schwab/silver/_canonical_silver_lib.py`: `list_bronze_dates` / `latest_bronze_date` return compact `YYYYMMDD` strings from the NEW form `date=YYYY-MM-DD`, ignore old-form tokens when any new-form token exists, and RAISE when only old-form tokens exist.

**Build.**
1. `build_canonical_daily.py`: replace the hand-built prefix and the 8-digit directory parse with the shared listing (import from `_canonical_silver_lib` the way the file's neighbours do). Output and behavior for the same set of days are unchanged: same dates, same order, same selection of "latest".
2. `build_fact_tax_1099div.py`: replace the hand-built `bronze/tnn/` listing and its date parse the same way; the written silver is unchanged.
3. `test_canonical_daily_date_axis.py`: the fixture listing is the NEW layout (`date=YYYY-MM-DD` partitions) and the existing assertions about dates still hold. Add a test whose name contains `tnn_listing` that stubs the S3 listing for the 1099 reader and asserts it returns the same dates from the new layout; and a test (name contains `old_form_only`) that a listing holding ONLY old-form tokens makes the daily reader RAISE with the "not moved" message rather than return no dates.
4. If either file's header names a deploy target (a box path or `s3://opal-data-bd/code/...`), state it in your report; deployment is the issuer's release act R5.

### ACCEPTANCE

<criterion id="BF1-r1-AC1" cell_refs="BF-r-1"><invocation>python -m pytest data/canonical/schwab/tests/test_canonical_daily_date_axis.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-r1-AC1` -- the daily builder's date axis on the new layout, including the old-form-only refusal; every test in the file passes (no skip hides a failure: report the skipped count).

<criterion id="BF1-r1-AC2" cell_refs="BF-r-1"><invocation>python -m pytest data/canonical/schwab/tests/test_canonical_daily_date_axis.py -q -p no:cacheprovider --color=no -k tnn_listing</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF1-r1-AC2` -- the 1099 reader's listing on the new layout (the second hand-parser).

<expected_criteria>BF1-r1-AC1,BF1-r1-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 "16 passed" (PASS as expected: a control that the file runs against the OLD layout) and AC2 "16 deselected" (rc 5, no `1 passed`) -- FAIL as expected.
AC1 must stay green AFTER you move the fixture to the new layout; if it is still green after your reader edits but the fixture still holds the old layout, you have not moved the file: rewrite the fixture first.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (notably `_canonical_silver_lib.py`, which is `TO-BF-k1`'s).
- **LOCAL.** No S3, no deploy, no network; all listings are stubbed. If a reader needs a function the shared contract lacks, stop and file a surprise row; do not add it to a file you do not own.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/build_canonical_daily.py
data/canonical/schwab/silver/build_fact_tax_1099div.py
data/canonical/schwab/tests/test_canonical_daily_date_axis.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP.md</decomp_doc> (round 1), cell `BF-r-1`.
<owned_cells>BF-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-r1-AC1, BF1-r1-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-r1.readers.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-r1-AC1,BF1-r1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two reader diffs in one sentence each, the pytest summary lines, the deploy targets the headers name (if any), the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM and the readers keep their existing identities; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the "empty prefix reads as nothing to do" hazard (PRD C-READERS) is the old_form_only test above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-READERS; decomposition round 1 cell BF-r-1 and its census section.
