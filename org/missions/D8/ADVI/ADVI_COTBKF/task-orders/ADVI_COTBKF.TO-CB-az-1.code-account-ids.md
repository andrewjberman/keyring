# TO ADVI_COTBKF.TO-CB-az-1.code-account-ids -- round 52 CB-az-1: no client account id in this project's code or its tracked manifest

<to_id>ADVI_COTBKF.TO-CB-az-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~79</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>52</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-az-1` (`decompositions/ADVI_COTBKF_DECOMP.round52.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** That includes
code, tests, fixtures, your report, commit messages and rows. Counts, sha256 and reason codes only.

The project's HEAD census (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACCOUNT_ID_CENSUS_HEAD_20261009.md`) finds
real Commonwealth/Cottonwood account numbers in 6 code files:
- `data/assets/scripts/silver/commonwealth_asf_source.py`
- `data/assets/scripts/silver/commonwealth_div_dating_trace.py`
- `data/assets/scripts/silver/commonwealth_scale_trace.py`
- `data/assets/scripts/silver/commonwealth_sweeps.py`
- `data/assets/scripts/silver/tests/test_commonwealth_asf.py`
- `data/assets/scripts/silver/tests/test_commonwealth_portfolio_files.py`

The shapes are `[A-Z0-9]{2}[A-Z]\d{6}`, `\d[A-Z]{2}\d{6}` and `[A-Z]{3}\d{6}`.

Separately, the adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` writes a build manifest whose
`sample_day_manifest.first_data_date` is a map keyed by account. The CTO removed one such tracked manifest, and the issuer two more.

**CTO ruling, item 3:**
- a real id in a TEST becomes a synthetic fixture;
- in a RUNTIME literal, it moves to a config read from outside the repo, or from the firm's served data.
- The CB-al-2 refusal adds: the tracked manifest carries day keys, hashes and counts only. The account map lives outside the repo,
  referenced by its sha256.

**Your item.** No S3 write and no deploy.

1. **Tests:** replace each real id with a synthetic one, e.g. `SYN_ACCT_01` (a form no account-id pattern matches), consistently within each test. The tests stay green.
2. **Trace scripts** (`*_div_dating_trace.py`, `*_scale_trace.py`): their accounts become CLI arguments, or are read from the order's
   own evidence outside the repo. They are never literals. Each script must still run, given the accounts.
3. **Runtime rule data** (`commonwealth_sweeps.py`, `commonwealth_asf_source.py`):
   - Move the account literals to a config file OUTSIDE the repo at
     `C:/dev/_cotbkf_private_evidence_20261009/config/<name>.json`.
   - The code loads it by a path from an environment variable, with that file as the default, and FAILS CLOSED (a named error) when it
     is absent.
   - The repo carries only the config's sha256, as a constant the loader checks.
   - **The chain output must be unchanged.** Run `python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1
     --after-list v1 --data-dir .scratch/advi_cotbkf/r28 --out <scratch>` before and after. The LAST line must be identical. Print
     both.
4. **The adapter's manifest:**
   - The tracked `ard_cottonwood_manifest.json` carries day keys, per-day hashes, counts and exception counts only.
   - Everything keyed by account (`first_data_date` and any sample manifest) goes to
     `C:/dev/_cotbkf_private_evidence_20261009/ard_private_manifest.json`. The tracked manifest names its sha256.
   - `--apply` already rebuilds `first_data_date` from the local day files. Keep that.
   - Regenerate a clean manifest from the EXISTING round-47 build (`.scratch/advi_cotbkf/ard_cottonwood_r47/`) without rebuilding the
     days, into your deliverables folder. Its per-day `sha256` / `content_sha256` must equal the round-47 values. Print the count
     equal.
5. **Test** `data/assets/scripts/silver/tests/test_cotbkf_code_no_account_ids.py`: it scans `data/assets/scripts/silver/commonwealth_*.py`,
   `data/assets/scripts/silver/tests/test_commonwealth*.py`, the cot gold files this project changed, AND the regenerated tracked
   manifest. It expects 0 hits and prints the denominator. Commit the test ALONE first; it must fail at the base.

**AMENDMENT 1 (issuer, 2026-10-09 ~17:0xZ; row W79-S1).** The grant adds `data/assets/scripts/silver/commonwealth_signs.py`.
- One client account id sits in a message string (around line 71). The HEAD census missed it because its scope did not include this
  file. Replace it with a synthetic, pattern-safe id. Nothing else in the file changes.
- Row W79-S2 is ACCEPTED: the shapes are bounded (no hit inside a longer capital/digit run), as stated in the test's docstring.

### ACCEPTANCE

<criterion id="CB52az1-AC1" cell_refs="CB-az-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_code_no_account_ids.py -q</invocation><expect>passed</expect></criterion>
`CB52az1-AC1` -- 0 account ids in this project's code and its tracked manifest. The test alone was committed first and failed at the
base.

<criterion id="CB52az1-AC2" cell_refs="CB-az-1" judgment="true"/>
`CB52az1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- the chain output is unchanged (the SWEEP-REGRADE line is identical before and after);
- the runtime config is fail-closed and sha-checked;
- the clean manifest's per-day hashes equal round 47's.

<expected_criteria>CB52az1-AC1,CB52az1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `C:/dev/_cotbkf_private_evidence_20261009/` (outside the repo), plus your deliverables
  folder and this order's file.
- **Do NOT touch** `data/cot/scripts/gold/` (round 50's ~77 is editing it). No S3 act. The silver suite stays green.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise
  row (id `ADVI_COTBKF-D2-W79-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_signs.py
data/assets/scripts/silver/commonwealth_asf_source.py
data/assets/scripts/silver/commonwealth_div_dating_trace.py
data/assets/scripts/silver/commonwealth_scale_trace.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/test_commonwealth_asf.py
data/assets/scripts/silver/tests/test_commonwealth_portfolio_files.py
data/assets/scripts/silver/tests/test_cotbkf_code_no_account_ids.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round52.md</decomp_doc> (round 52), cell `CB-az-1`.
<owned_cells>CB-az-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB52az1-AC1, CB52az1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ADVI_COTBKF.TO-CB-az-1.code-account-ids.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB52az1-AC1,CB52az1-AC2` BEFORE the flip. Mechanical: CB52az1-AC1. A judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT (counts only):**
- the pytest lines (the test and the silver suite);
- the SWEEP-REGRADE line before and after;
- the clean manifest's day count and hash-equality count;
- the outside-repo files with their sha256;
- commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE local code; the commonwealth chain is not deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first; the chain output proven unchanged; the config fail-closed and sha-checked; the manifest hashes equal round 47's; BLIND: another script reading the moved literals by import (the suite and the re-grade surface it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` containment ruling @0e8209c33c (item 3) and msg 3626 (CB-al-2 refusal).
