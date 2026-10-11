# TO ADVI_COTBKF.TO-CB-bn-2.scan-declared-cusips -- round 66 CB-bn-2: the account-id scan tells a declared security identifier from an account id; the suite returns to green

<to_id>ADVI_COTBKF.TO-CB-bn-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~98</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>66</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bn-2` (`decompositions/ADVI_COTBKF_DECOMP.round66.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** row ADVI_COTBKF-D2-S113 in the channel; `data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py` in full;
`data/assets/scripts/silver/tests/_cotbkf_acct_check.py` in full (`shape_patterns`, `scan_text`, `check_exceptions`,
`load_account_set`).

**The problem.** The silver suite is RED at the base on one test: `test_no_account_ids_in_cotbkf_tracked_files` reports
`76 shape hits and 0 account-set hits in 2 files`. The two files are security lists this project committed in round 65:
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~95/PRICE_REQUEST_YAHOO.csv` (68 hits) and
`PRICE_REQUEST_BLOOMBERG.csv` (8). Each has a `cusip` column; 76 of the 4,408 nine-character CUSIPs have the same SHAPE as a client
account id. None IS one: the set limb, which compares against the real ids, reads 0.

**Your item. The scan must stay as strict as it is everywhere else.**

1. Teach the scan ONE narrow thing: in a tracked CSV that DECLARES itself a security list (its header row has a column named exactly
   `cusip`), a token that sits in that file's `cusip` or `identifier` column is a declared security identifier, and its SHAPE hit is
   not counted, PROVIDED the token is not in the account set. The SET limb is never relaxed: a real account id in that column still
   fails the test. A shape hit in any other column of such a file, or anywhere in a file that is not such a CSV, counts as before.
2. Put the rule in `_cotbkf_acct_check.py` (a named function) and use it from the test; print in the test's DENOMINATOR line how many
   shape hits were set aside as declared security identifiers and in how many files, so the exemption is visible every run.
3. Do NOT add the 76 CUSIPs to `CUSIP_EXCEPTIONS`, do not exclude the two files or their folder by path, and do not loosen a shape
   pattern.
4. Tests for the rule itself (synthetic values only, never a real account id): a shape-matching token in the `cusip` column of a
   declared list is set aside; the same token in another column counts; the same token in a CSV with no `cusip` header counts; a token
   that IS in the (synthetic) account set counts even in the `cusip` column; a non-CSV file is unchanged.
5. Run the suite. It must return to green.

### ACCEPTANCE

<criterion id="CB66bn2-AC1" cell_refs="CB-bn-2"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB66bn2-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB66bn2-AC2" cell_refs="CB-bn-2"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s</invocation><expect>DENOMINATOR:</expect></criterion>
`CB66bn2-AC2` -- the scan's own line prints its denominator with the count of shape hits set aside as declared security identifiers
(76 in 2 files at this base) and 0 account-set hits.

<expected_criteria>CB66bn2-AC1,CB66bn2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** the two CSV files, any other deliverable, or any product script.
- **Never print a real account id.** The account set is loaded by the test's own loader; do not print its members.
- **No AWS call. No push. No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W98-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file (open it
  in append mode; `git diff --numstat` must show added lines only).

<paths>
data/assets/scripts/silver/tests/_cotbkf_acct_check.py
data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round66.md</decomp_doc> (round 66), cell `CB-bn-2`.
<owned_cells>CB-bn-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB66bn2-AC1, CB66bn2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~98/ADVI_COTBKF.TO-CB-bn-2.scan-declared-cusips.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB66bn2-AC1,CB66bn2-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the pytest line before and after; the scan's DENOMINATOR line after; the rule in one sentence and its function name; tests added, by name; the diff of the two files; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one test helper and its tests.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the set limb is never relaxed and a test asserts a real (synthetic) id in the cusip column still fails; the exemption is keyed on the file declaring a cusip column AND the token sitting in it, and is printed in the denominator every run; path exclusion and a 76-name exception list are barred; BLIND: an account id absent from the pinned set that sits in a cusip column would pass, as it would have under any exception.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4734 (2026-10-11), items 2 and 3, and msg 4772; round-65 packet @66db401fb2; rows ADVI_COTBKF-D2-S111 and D2-S113.
