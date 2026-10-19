# TO NFRA_FIDUPL.TO-FU-s-4 -- the source-independent lander and its run record

<to_id>NFRA_FIDUPL.TO-FU-s-4</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~2</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-4` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1 |
**depends_on:** none (the scope row is landed @bd84d81948)

---

## WORKER FACE

### THE CELL

**FU-s-4** -- The lander, source-independent: reads a handoff directory, lands the six files raw once at `address('fidelity', <scope>, 'bronze', ...)` read AT LANDING TIME, sha256 per file, content date from the first field, trading-calendar check, re-served day lands once, one run record with the four failure classes. Contract rows: C-RAW, C-DATE, C-RECORD, C-TENANCY.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Build `infra/aws/ec2/canonical-fidelity/land.py` and `tests/test_land.py` to reference sections 1, 5, 5a, 6 and 9. The lander takes files from ANY source (the automated fetch, an Integration Xchange drop, a person's download): it needs no session.

1. `land(handoff_dir, scope, s3=None, now=None, dry_run=False)` reads `listing.json` and the files in the directory. For each of the six files it computes the sha256 of the bytes, reads the business date from the FIRST field of the FIRST row of that file (quoted CSV, no header; never from the file name, never from the run date), and checks the date against `lib/trading_calendar.py` (read that file for its API; a date that is not a trading day is the failure `content date is not a trading day`; an unreadable date is `content date unreadable`; neither is ever guessed or repaired).
2. The destination of each file is `opal_naming.address('fidelity', scope, 'bronze', <file stem>, <YYYYMMDD content date>, <file name>)`, called AT LANDING TIME inside `land` for every file, with `scope` the function argument (never a literal in the function). Put the bytes with boto3 `put_object` (SSE AES256), unchanged. If an object already exists at the destination with the same sha256 (a `head_object` read), the file is `skipped_existing` and nothing is written. Nothing is written outside the `fidelity/` prefix.
3. One run record (reference section 6) is written to `opal_naming.address('fidelity', scope, 'bronze', '_runs', <YYYYMMDD>, 'run-<run_id>.json')` for every call that is not a dry run, including a call whose `listing.json` carries a `failure` (then no file is landed, `failed_step` and `failure_class` carry it, and the record says so). `run_id` is the UTC time `YYYYMMDDTHHMMSSZ`.
4. `--dry-run` prints one line `DRYRUN dest=<address>` per file and writes nothing (no S3 call at all).
5. Exit code 0 only when `failure_class` is null and every file is `landed` or `skipped_existing`; a missing file, a non-trading-day date or any listing failure exits non-zero AFTER writing the record.
6. Tests (a fake S3 that RECORDS every call; synthetic six-file fixtures): `test_lands_six_to_builder_addresses`, `test_scope_is_a_parameter` (a second scope changes every destination), `test_address_called_at_landing_time` (monkeypatch `opal_naming.address` and assert it is called per file during `land`, not at import), `test_content_date_from_first_field`, `test_unreadable_date_is_failure_not_guess`, `test_non_trading_day_is_failure` (use a Saturday date), `test_same_sha_lands_once`, `test_run_record_shape`, `test_missing_file_exits_nonzero`, `test_never_writes_outside_fidelity_prefix`.

### ACCEPTANCE

<criterion id="FU4-AC1" cell_refs="FU-s-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu4</invocation><expect>R1-FU4-OK passed=\d+</expect></criterion>
`FU4-AC1` -- the ten named tests exist and pass.

<criterion id="FU4-AC2" cell_refs="FU-s-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu4d</invocation><expect>R1-FU4D-OK dests=6</expect></criterion>
`FU4-AC2` -- the real naming builder resolves all six destinations in a dry run.

<expected_criteria>FU4-AC1,FU4-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FU4-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU4-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `lib/opal_naming.py`
- `lib/trading_calendar.py`
- `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` lines 529-556 (Schwab's run manifest, for shape only)

<paths>
infra/aws/ec2/canonical-fidelity/land.py
infra/aws/ec2/canonical-fidelity/tests/test_land.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-4`.
<owned_cells>FU-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU4-AC1,FU4-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~2/NFRA_FIDUPL.TO-FU-s-4.lander-and-run-record.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU4-AC1,FU4-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- the lander's S3 write is proven on a recording fake; the live grant is FU-s-6's and is graded there.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-4; worker reference.
