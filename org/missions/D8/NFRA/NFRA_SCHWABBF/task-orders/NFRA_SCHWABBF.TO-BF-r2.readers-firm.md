# TO NFRA_SCHWABBF.TO-BF-r2 -- thread hop 3b: the readers that parse the old grammar by hand follow the shared function, FIRM form

<to_id>NFRA_SCHWABBF.TO-BF-r2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-4, FWD-5 | **depends_on:** `TO-BF-k2` (earlier in your queue, already on your branch)

---

## WORKER FACE

### THE CELL

`BF-r-2`, PRD contract C-READERS at v0.5: "Every reader and writer of the old form changes in the same release as the move." A reader that parses the old grammar by hand and is missed reads an empty prefix and reports "nothing to do". FWD-5 ACCEPT: "nobody can find a holdings, balance or activity figure for an already stored day that differs from the day before."
The firm form puts three masters in ONE partition folder (`schwab/49financial/bronze/{feed}/date=YYYY-MM-DD/`, files told apart by the name prefix `{master}.`), so a reader that lists the folder without filtering by master SUMS 0824 and 0833, which the purpose law forbids.

**What exists.** Two readers build the old layout themselves instead of calling the shared function (the issuer's census, `decompositions/NFRA_SCHWABBF_DECOMP.md`); every other reader follows the shared function with no edit. At the cut, after `TO-BF-z2`, your worktree holds them at their ORIGINAL bytes:
- `data/canonical/schwab/build_canonical_daily.py`: line 63 `MONOLITH_FEED_PREFIX = f"schwab/{CANON_MASTER}/bronze/{CANON_FEED}/"`; line ~141 lists "8-digit partition DIRECTORY names (YYYYMMDD)" under that prefix; the comment near line 186 about files "unreadable via monolith_bronze_key".
- `data/canonical/schwab/silver/build_fact_tax_1099div.py`: line 74 `prefix = f"schwab/{MASTER}/bronze/tnn/"` and the date parsing after it; line 87 already calls `monolith_bronze_key`.
- `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`: describes the old layout (lines ~10, 119, 203).
- A master-form edit of these three files is in git history for REFERENCE (`git show 293346aff1:<path>`); the grammar there is wrong now, the structure and the test names are reusable (`tnn_listing`, `old_form_only`).
- The shared function is `TO-BF-k2`'s, in `data/canonical/schwab/silver/_canonical_silver_lib.py`: `list_bronze_dates` / `latest_bronze_date` return compact `YYYYMMDD` strings for ONE master from the firm-form folder, filtering by the file-name prefix; they ignore old-form keys when any firm-form key exists for that master; they RAISE with an old-form count and "not moved" when only old-form keys exist. If a name you need is private, say so in your report; do not edit that file.

**Build.**
1. `build_canonical_daily.py`: replace the hand-built prefix and the 8-digit directory parse with the shared listing (import from `_canonical_silver_lib` as its neighbours do). For the same set of days the output and the "latest" selection are unchanged.
2. `build_fact_tax_1099div.py`: replace the hand-built `bronze/tnn/` listing and its date parse the same way; the written silver is unchanged. A positive `min_size` argument that the old listing honored must still work or be refused loudly (state which in your report; the round-1 reader refused it).
3. `test_canonical_daily_date_axis.py`: the fixture listing is the FIRM layout (`schwab/49financial/bronze/{feed}/date=YYYY-MM-DD/{master}.CRS...`) with TWO masters' files in the same partitions (the stub has different dates per master) and the existing date assertions hold per master. Keep a test whose name contains `tnn_listing` (the 1099 reader returns the master's own dates from the firm layout) and one whose name contains `old_form_only` (a listing with ONLY old-form keys makes the daily reader RAISE the "not moved" message instead of returning no dates).
4. If either file's header names a deploy target, state it in your report; deployment is the issuer's release act.

### ACCEPTANCE

<criterion id="BF2-r2-AC1" cell_refs="BF-r-2"><invocation>python -m pytest data/canonical/schwab/tests/test_canonical_daily_date_axis.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-r2-AC1` -- the daily builder's date axis on the firm layout with two masters in one folder, including the old-form-only refusal; report the skipped count.

<criterion id="BF2-r2-AC2" cell_refs="BF-r-2"><invocation>python -m pytest data/canonical/schwab/tests/test_canonical_daily_date_axis.py -q -p no:cacheprovider --color=no -k tnn_listing</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF2-r2-AC2` -- the 1099 reader's listing on the firm layout, master-filtered.

<expected_criteria>BF2-r2-AC1,BF2-r2-AC2</expected_criteria>

Dry-run at the base: at the restored original bytes AC1 reads `16 passed` (PASS, a control that the file runs against the OLD layout) and AC2 reads `16 deselected` (rc 5) -- FAIL as expected. AC1 must stay green after you move the fixture to the firm layout; if it is still green while the fixture still holds the old layout, you have not moved the file.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (notably `_canonical_silver_lib.py`, which is `TO-BF-k2`'s).
- **LOCAL.** No S3, no deploy, no network; listings are stubbed. If a reader needs a function the shared contract lacks, stop and file a surprise row.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/build_canonical_daily.py
data/canonical/schwab/silver/build_fact_tax_1099div.py
data/canonical/schwab/tests/test_canonical_daily_date_axis.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-r-2`.
<owned_cells>BF-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-r2-AC1, BF2-r2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-r2.readers-firm.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-r2-AC1,BF2-r2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the two reader diffs in one sentence each, the pytest summary lines, the deploy targets the headers name (if any), the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- readers and tests.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM and the readers keep their identities; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 1 (a lister that does not filter by master sums 0824 and 0833) is the two-masters-one-folder fixture above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-READERS; decomposition round 2 cell BF-r-2; round-1 reference `293346aff1`.
