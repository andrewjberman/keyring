# TO NFRA_GATSCP.TO-GS-f-5 -- round 3 GS-f-5: a read-only census of the seven commit-path gates that read the working tree or grade beyond the act

<to_id>NFRA_GATSCP.TO-GS-f-5</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~12</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-f-5` (`decompositions/NFRA_GATSCP_DECOMP.round3.md`) | **outcome_ref:** FWD-6 |
**rows:** D1-S7 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

Row D1-S7 named seven gates on the commit path that read the shared working tree or grade beyond the act. The CTO
ruled (R6): they do NOT join this project's scope wholesale; this round records, per gate, what it reads against the act's write
set and how many false refusals or audited overrides the logs show for it in the last seven days. Only a gate with a measured false
refusal is cut later. The gates: `.tools/commit_gate_runner.py`; `.tools/to-pipeline-gate.py`; `.tools/to-decomp-ref-lint.py`;
`.tools/git-hooks/owned-paths-check.sh` (reads `.owned-paths.yaml` from disk, :37); `.tools/git-hooks/mstr-ledger-check.sh`;
`.tools/git-hooks/pipescript-suite-check.sh`; `rcg/bin/manifest_check.py`. Logs: `org/to-pipeline-override-audit.log`
(`TS | author | path | reason`); `org/git-author-override-audit.log` (lines tagged PASS, BLOCK, OVERRIDE, SURPRISE-ROW-OVERRIDE,
FORCE-BYPASS, MERGE-REFUSED, with an ISO time first); `org/tier0/audit/ledger-hook-audit.log`; `org/pipescript-suite-gate-audit.log`
exists only under `org/audit/archive/**`; rcg has no log.

### THE CELL

`GS-f-5`. A read-only census of the seven commit-path gates that read the working tree or grade beyond the act.

**Build:**
Read the seven gates' code and the logs; write
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~12/GATE_CENSUS_round3.md` with ONE table, a row per gate, the
columns exactly `gate | reads | beyond the act | false refusals 7d | audited overrides 7d | log read`:
- `reads`: the files it reads, `index` / `disk` / `both`, with file:line;
- `beyond the act`: what it grades outside the commit's own paths, or `none`;
- the two 7-day columns: integers counted from the log lines dated within the seven days before your run (0 is a value). A "false
  refusal" is a BLOCK/refusal later passed by an audited override naming the same gate, or one the log's own reason calls not the
  act's; state the rule you applied under the table;
- `log read`: the log path, or `none: <why>`.
Then one line `CENSUS window=<from>..<to> logs=<n> lines_read=<n>` (UTC). Edit no code, no log, nothing outside your folder.

### ACCEPTANCE

<criterion id="GF5-AC1" cell_refs="GS-f-5"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/r3_census.py"</invocation><expect>GS-F5-CENSUS ok=True</expect></criterion>
`GF5-AC1` -- the report has a row for each of the seven gates with integer 7-day columns and a log named, and the CENSUS denominators line.

<expected_criteria>GF5-AC1</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~12/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W12-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round3.md</decomp_doc> (round 3), cell `GS-f-5`.
<owned_cells>GS-f-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GF5-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~12/NFRA_GATSCP.TO-GS-f-5.seven-gate-census.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-f-5`,
validated with `python .tools/proof-of-spec-check.py <instance> GF5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- each criterion carries its negative or control arm (decomposition round 3, battery); BLIND: a census's conclusions are the CTO's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @0ef2dc8325 (with ADDENDUM 1); CTO msg 2258 for D1-S5; decomposition round 3. Base dry-run: see the
issuance commit.
