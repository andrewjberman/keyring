# TO NFRA_FIDUPL.TO-FR-s-2 -- the firm split of the staged raw day

<to_id>NFRA_FIDUPL.TO-FR-s-2</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~3</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>fidelity-perg</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FR-s-2` (`decompositions/NFRA_FIDUPL_DECOMP_R2.md` v1.0) | **outcome_ref:** FWD-9, C-BACKFILL |
**depends_on:** none (built against fakes; interfaces in worker reference section 11)

---

## WORKER FACE

### THE CELL

**FR-s-2** -- The firm split: from the staged raw day and the attribution, write each firm's lines byte-for-byte to `address('fidelity', <firm>, 'bronze', ...)`, once per firm; list conflicts, unplaced accounts, unmapped labels and firms without a scope row; one split record. Contract rows: C-TENANCY, FWD-9.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1 and 11 bind you; the rest is context) and the cell text above. Project NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning; round 2 splits it per firm by G number, backfills history per G number, and schedules it. You build against fakes; nothing here runs live.

### WHAT TO BUILD

Build `split.py` and `tests/test_split.py` to worker reference section 11 (the `split.py` bullet is your interface) and sections 5, 5a and 6 (handoff directory, landing addresses, the run-record home).

1. `split_day(handoff_dir, attribution, config, s3=None, now=None, dry_run=False)`. Read `listing.json` and the six files in `handoff_dir` (the same directory the lander read). Take the business date from the FIRST field of the FIRST row of each file, as the lander does (never from the file name or the run date).
2. Build account to firm: every account in `attribution["by_g"][G]["accounts"]` belongs to the firm whose `config["firm_labels"]` substring (upper case, first match) occurs in that G's upper-cased label. One account under several G numbers of ONE firm lands once for that firm. An account under G numbers of TWO firms goes to `conflicts` and is landed nowhere. An account under no G goes to `unplaced`. A label that matches no `firm_labels` entry goes to `unmapped_labels` (labels only) and its accounts to `unplaced`.
3. For each file, split its lines by the account number in the column `config["account_columns"][file name]`. Preserve every line's bytes exactly, including its line ending (split on the raw bytes, never decode and re-encode, never re-quote). Write each firm's lines with boto3 `put_object` (SSE AES256) to `opal_naming.address('fidelity', <firm>, 'bronze', <file stem>, <YYYYMMDD>, <file name>)`, called AT SPLIT TIME per firm and file. If `address()` refuses a firm (no registry scope row yet), add the firm to `firms_without_scope` and land nothing for it; never type a path. Nothing is written outside the `fidelity/` prefix.
4. The run record `split-<run_id>.json` goes to `address('fidelity','alongside','bronze','_runs', <YYYYMMDD>, 'split-<run_id>.json')` (not on a dry run) with counts per firm per file (rows in, rows written), `conflicts`, `unplaced`, `unmapped_labels`, `firms_without_scope`. A dry run writes nothing and prints one `DRYRUN dest=<address>` line per firm per file. Exit code 0 only when `conflicts` and `firms_without_scope` are empty and every written object's row count matches.
5. CLI `python split.py --handoff-dir DIR --attribution FILE --config FILE [--dry-run]`; it prints only counts.
6. Tests (a recording fake S3, synthetic attribution and six synthetic files with made-up account numbers): `test_rows_split_by_account_to_firm_addresses`, `test_account_under_two_g_of_one_firm_lands_once`, `test_account_under_two_firms_listed_not_landed`, `test_unplaced_accounts_listed`, `test_unregistered_firm_scope_listed_not_landed`, `test_raw_line_bytes_preserved` (include CRLF lines and a non-ASCII byte), `test_dry_run_writes_nothing`, `test_record_has_counts_and_lists`, `test_unmapped_label_listed_not_landed`.

### REPAIR (issuer, 2026-10-20 ~15:45Z; this order is REOPENED) -- your row W3-S5

Your split record carries ordinal ids and counts where the order asked for the account lists. The issuer rules: **the S3 run record `split-<run_id>.json` MUST hold the actual account-number strings in `unplaced` and `conflicts`** (the FWD-9 bar is that someone can see WHICH accounts could not be placed). It lives under `fidelity/alongside/bronze/_runs/`, the same staging prefix that already holds every account in the pull; that is not an output. What stays forbidden is any print, log line, exception message or CLI output carrying an account value or a G number: the CLI and the logs still print counts only. Change the record to carry the lists, keep the printed output counts-only, and add the test `test_record_lists_unplaced_and_conflict_accounts` to your `tests/test_split.py` (a recording fake S3 holding the record, with made-up account strings; assert the record contains them AND the captured stdout, stderr and logs do not). Your rows W3-S6, S7 and S8 are accepted as built (an account under one mapped and one unmapped G is unplaced; different bytes at a destination are refused; the stricter exit code). FR2-AC1 now needs ten. Refresh the proof instance and flip when it PASSES.

### ACCEPTANCE

<criterion id="FR2-AC1" cell_refs="FR-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr2</invocation><expect>R1-FR2-OK passed=\d+</expect></criterion>
`FR2-AC1` -- the ten named split tests (the nine and `test_record_lists_unplaced_and_conflict_accounts`) exist and pass.

<expected_criteria>FR2-AC1</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FR2-AC1` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Every test uses SYNTHETIC data and fakes; no network, no AWS, no live call. G numbers and account numbers in tests are made up and are never real ones.
- **No secret, no alert; no G number, account number or firm label in any output.** Counts and booleans only (reference section 11).
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, `<n>` your slot, `<k>` next unused across the investigation file) and stop that piece. A premise that fails is a row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `infra/aws/ec2/canonical-fidelity/land.py` (the lander: the content-date and address pattern to follow; read only)
- `lib/opal_naming.py`

<paths>
infra/aws/ec2/canonical-fidelity/split.py
infra/aws/ec2/canonical-fidelity/tests/test_split.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R2.md</decomp_doc> (round 2), cell `FR-s-2`.
<owned_cells>FR-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FR2-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~3/NFRA_FIDUPL.TO-FR-s-2.firm-split.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FR2-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build round on fakes; runs when the live round touches this surface.
lane: the paths block.
</preflight>

Source: CTO msg 8663 (PRD v0.4.5 @e4bb46835e); Andrew-direct @b329e1c5f3; decomposition round 2 cell FR-s-2; worker reference section 11.
