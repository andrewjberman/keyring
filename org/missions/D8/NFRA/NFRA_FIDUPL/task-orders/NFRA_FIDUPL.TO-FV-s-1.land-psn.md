# TO NFRA_FIDUPL.TO-FV-s-1 -- the lander learns the fixed-length positions-and-balances file (.psn)

<to_id>NFRA_FIDUPL.TO-FV-s-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~6</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-histwalk-build</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FV-s-1` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 15) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** none (land.py as merged)

---

## WORKER FACE

### THE CELL

**FV-s-1** -- Fidelity's Historical export in Standard Format A returns ONE fixed-length file `FI<MMDDYY>.psn` (positions as 156-character records, balances as 56-character records, CRLF). It has no comma columns, so `land.land` cannot read its date. Add to `infra/aws/ec2/canonical-fidelity/land.py` a landing function for this one file. The CSV landing of the six files is NOT changed.

**Read first:** `land.py` whole (especially `_content_date`, `landing_date`, `_entry`, `_fail`, `_examine`, `_head`, `_land_one`, `_public`, `land`, `exit_code`, `main`) and `tests/test_land.py` (its `FakeS3` is the pattern: copy it into your new test file).

### WHAT TO BUILD

In `land.py` (Python 3.9, ASCII):
1. Constants `PSN_NAME = "position_balance_fl.psn"` and `PSN_DATE_OFFSET = 17`, and `_psn_content_date(data)`: the first line of `data` (split on the first `\n`, strip a trailing `\r`), characters `[17:23]` decoded as latin-1; they must be six digits forming a valid `%m%d%y` date (the year is 2000 plus YY); return that `datetime.date`, else `None` (a short line, non-digits, an impossible month or day).
2. `land_psn(path, scope, s3=None, now=None, dry_run=False)`: read the file's bytes (a missing or unreadable file is a failed entry, step `read`, like `_examine`). Build the entry with `_entry(PSN_NAME)`, set `bytes` and `sha256`, take the as-of from `_psn_content_date` (None gives `_fail(entry, "date", CLASS_DATE_UNREADABLE, ...)`), set `content_as_of`, `trading_day` and `content_date` exactly as `_examine` does (`landing_date`, `CalendarCoverageError` fails closed with step `calendar`), then call `_land_one(entry, data, scope, dry_run, client)` unchanged (its stem comes from the entry name, so the key is `address("fidelity", scope, "bronze", "position_balance_fl", <content date>, "position_balance_fl.psn")`). Write ONE run record exactly as `land()` does (same keys; `files` holds the one public entry; `outcome` ALL_LANDED when the entry's action is in OK_ACTIONS, else FAILED; `business_date_in_content` the landing date; a dry run writes nothing). Return the record.
3. CLI: `main` accepts `--psn PATH` as an alternative to `--handoff-dir` (exactly one of the two is required; `--scope` and `--dry-run` as today) and prints the same `ERROR:` and summary lines as the handoff path. `--handoff-dir` behaviour is unchanged.
4. Tests in the NEW `tests/test_land_psn.py` (fakes only; the file bytes are synthetic: 156-character lines whose characters 17 to 22 read the MMDDYY, e.g. `("A" * 17) + "101526" + (" " * 133)` plus CRLF; no real data): `test_psn_date_is_read_from_offset_17_as_mmddyy`, `test_psn_lands_under_the_content_date_with_the_fixed_table_name` (the put key is `fidelity/alongside/bronze/position_balance_fl/20261015/position_balance_fl.psn` and the record has `outcome` ALL_LANDED and the run record put), `test_psn_unreadable_date_is_a_named_failure_and_lands_nothing` (no put of the file; failure class `content date unreadable`), `test_psn_existing_identical_is_skipped_and_different_is_not_overwritten` (`skipped_existing`; a different body at the key is a failed `land` step and no put), `test_psn_non_trading_asof_lands_under_the_prior_trading_day` (a Saturday as-of lands under the Friday and the entry keeps both dates).

### ACCEPTANCE

<criterion id="FV-s-1-AC1" cell_refs="FV-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv1</invocation><expect>R1-FV1-OK passed=\d+</expect></criterion>
`FV-s-1-AC1` -- the five named psn tests exist and pass.

<criterion id="FV-s-1-AC2" cell_refs="FV-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu4</invocation><expect>R1-FU4-OK passed=\d+</expect></criterion>
`FV-s-1-AC2` -- the lander's existing tests still pass (a regression guard: the CSV landing is unchanged).

<expected_criteria>FV-s-1-AC1,FV-s-1-AC2</expected_criteria>

Dry-run at the base: `FV-s-1-AC1` base: FAIL as expected; `FV-s-1-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fakes only.** No network, no AWS. No change to `land.land` behaviour or to the six-file landing.
- **Refusal clause.** A premise that fails is a surprise row (`NFRA_FIDUPL-D1-W6-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax.** The whole module suite must have no failure: its last line goes in your report.

<paths>
infra/aws/ec2/canonical-fidelity/land.py
infra/aws/ec2/canonical-fidelity/tests/test_land_psn.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 15 addendum), cell `FV-s-1`.
<owned_cells>FV-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FV-s-1-AC1, FV-s-1-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~6/NFRA_FIDUPL.TO-FV-s-1.land-psn.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FV-s-1-AC1,FV-s-1-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, the module suite's last line, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; the live walk is ordered separately (TO-FV-s-3) under the CTO's go (msg 9101).
lane: the paths block.
</preflight>

Source: CTO msg 9101; the issuer's live PBL read 2026-10-21 (decomposition section 15).
