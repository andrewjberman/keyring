# TO SOC2_MSLOGS.TO-R2-n2 -- the door's bronze prefixes come from the naming builder

<to_id>SOC2_MSLOGS.TO-R2-n2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~9</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** WORLD only by the gate's path floor; the cell calls nothing live. `staged` until TO-R2-d2 is terminal (the issuer then flips it to `pending` and continues you on it); both orders write `handler.py`.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-n-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** rule 30 (CLAUDE.md), remediation `SOC2_MSLOGS-D1-W2-S3` | **depends_on:** TO-R2-d2 (same file)

---

## WORKER FACE

### THE CELL

`SM-n-2`. CLAUDE.md rule 30: every S3 address is `lib/opal_naming.py address()` output, never hand-typed. The door's `handler.py` types the bronze `audit_records` prefix twice (the constant `BRONZE_DAY` and the `bronze` key grammar in `_GRAMMAR`), and the commit-time naming gate
(`.tools/naming-gate.py`) REFUSES both lines. The Lambda cannot import `lib/` at run time (the zip carries only the door's own modules), so the names must reach the zip another way.

READ first: `infra/aws/lambda/globgrph-trino-access/handler.py` (`PREFIX`, `BRONZE_DAY`, `_GRAMMAR`, `key_ok`), `infra/aws/lambda/globgrph-trino-access/build.sh`, `lib/opal_naming.py` (`address`), and `.tools/naming-gate.py` (how a line is graded and what it admits). Run the gate on the handler as an all-added diff to see the lines:
`git diff --no-index -- /dev/null infra/aws/lambda/globgrph-trino-access/handler.py > <scratch>/h.diff` (a nonzero exit is normal for `--no-index`), then `python .tools/naming-gate.py --diff <scratch>/h.diff`.
The builder's output for the bronze day prefix: `address('m365-metadata','trino','bronze','audit_records','date=20261016', object='x')` -> `s3://opal-data-trino/m365-metadata/trino/bronze/audit_records/date=20261016/x`.

BUILD (the suggested design; any design that passes the check is acceptable):
- `handler.py` gets the bronze day prefix and the bronze key grammar's prefix from the builder: first `try: from names import ...` (a module the ZIP carries), `except ImportError:` from `lib.opal_naming import address` (the repository, where the tests and the check run with the repository root on `sys.path`).
  `BRONZE_DAY` keeps its value and its meaning: `BRONZE_DAY % "20261016"` is `m365-metadata/trino/bronze/audit_records/date=20261016/`. The `bronze` entry of `_GRAMMAR` is built from that prefix with `re.escape`, so `key_ok` admits exactly the keys it admits today.
- `build.sh` writes `names.py` into the package directory at build time by running `lib.opal_naming` (so the generated file is a build product, never committed), and packages EVERY top-level `*.py` of the door directory that is not a test, sorted, with the fixed timestamps it uses today. It asserts that `handler.py`, `silver_builder.py` and `names.py` are among them (the next
  cells add `exposure.py` to the directory, and the zip must carry it with no further edit). Run it once and read the zip's file list.
- Add tests to `tests/test_handler.py`: the prefix equals the builder's output; `key_ok` still admits a builder-shaped bronze key and refuses a key with a wrong date part, a wrong object name and a `..`.
- The gate also refuses lines for the `silver`, `state` and `gold` prefixes (the state/gold/silver key shapes are a HOLE: no registry module places them, which the gate assigns to `1.0.0_SA_CTO`). Leave those lines as they are and report the gate's exact lines for them. Do NOT hide them to quiet the gate.
- If `.tools/naming-gate.py` admits NO form for the bronze lines in the Lambda's source (read its rules before concluding), stop at that measurement: write the gate's rule and the output in your report and a surprise row, and leave the criterion FAIL. Do not weaken the check.

Hard limits: ASCII only; stdlib only in the handler; no AWS call, no network.

### ACCEPTANCE

<criterion id="R2-n2-AC1" cell_refs="SM-n-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py naming</invocation><expect>R2-NAMING-OK</expect></criterion>
`R2-n2-AC1` -- `handler.BRONZE_DAY` equals the builder's bronze day prefix, `key_ok` still admits a builder-shaped key, and the naming gate refuses no `audit_records` line in any top-level module of the door directory.

<expected_criteria>R2-n2-AC1</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-NAMING-REFUSED the naming gate still refuses 2 audit_records line(s)` -- FAIL as expected. Run it from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL work only; NOTHING is called live.** No AWS call, no network, no Terraform.
- `silver_builder.py`'s derive code and `access.tf` are not yours.
- **Refusal clause.** As above: stop, report, surprise row (id `SOC2_MSLOGS-D1-W9-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), never weaken a check.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~9 <0.9.0_WK_SOC2_MSLOGS~9@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/handler.py
infra/aws/lambda/globgrph-trino-access/build.sh
infra/aws/lambda/globgrph-trino-access/names.py
infra/aws/lambda/globgrph-trino-access/tests/test_handler.py
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-n-2`.
<owned_cells>SM-n-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: R2-n2-AC1. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~9/SOC2_MSLOGS.TO-R2-n2.door-naming.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-n2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the check line, the gate's remaining lines on the door directory (verbatim, they are the HOLE the CTO owns), the zip's file list from one `build.sh` run, the `pytest` summary line (`python -m pytest infra/aws/lambda/globgrph-trino-access/tests -q`), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a name-source change; key_ok's accepted and refused keys are graded by the check and the tests.
lane: the <paths> block IS the grant.
</preflight>

Source: the CVO's remediation `SOC2_MSLOGS-D1-W2-S3` (ARMED, owner this issuer, `surprise-channel/remediations/REMEDIATION_v1.md`) and the CTO's round-1 analysis section 3 item 5 (@843819d1ab). The row closes when the check passes and the issuer records it.
