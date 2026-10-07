# TO MDPF_SECCLASS.TO-SC-e59 -- round 10 SC-e-59: the fix of the BD thread's first failing hop that SC-e-58 names

<to_id>MDPF_SECCLASS.TO-SC-e59</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~41</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-59` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-1 | **depends_on:** TO-SC-e58 (slot ~41 queue: after TO-SC-e58)

---

## WORKER FACE

### THE CELL

`SC-e-59`. CTO round-9 analysis section 3 item 1: "the BD pages thread trace, then the fix of its failing hop."

Your input is your own SC-e-58 record, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_PAGES_THREAD_TRACE_20261007.json`:
its `first_failing_hop`, `fix_file` and `fix_line`.

**Build -- only when `fix_file` is one of these three:**
- `data/black_diamond/scripts/gold/lib/etf_classifier.py`
- `data/black_diamond/scripts/silver/build_bd_assets_dim.py`
- `data/black_diamond/scripts/gold/D_03.composition_artifacts.py`

Change that hop so it carries the canonical class and sub-class from `etf-classifications`, through the one client, with no fold. GLD and
PHYS then read commodities and VXX reads hedge at that hop. Write `data/black_diamond/scripts/gold/tests/test_thread_hop_fix.py`. It feeds
the hop a canonical fixture holding GLD, PHYS and VXX and asserts the three classes out. As the difference control, a ticker the fixture
does not hold reads as the hop's declared miss value, not a guess.

**Otherwise:**
- If `fix_file` is `D_04.client_portal_summary.py`, the fix is the next order's (TO-SC-e60).
- If `first_failing_hop` is `NONE`, or the hop is the page, the API, the canonical source or a platinum key with no code fix in these
  files, write NO code. File a surprise row naming the hop and its evidence, and report it; the issuer recuts.

### ACCEPTANCE

<criterion id="SC10-e59-AC1" cell_refs="SC-e-59"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests/test_thread_hop_fix.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e59-AC1` -- the fixed hop maps GLD/PHYS to commodities and VXX to hedge from the canonical fixture, with the miss control.

<criterion id="SC10-e59-AC2" cell_refs="SC-e-59"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e59-AC2` -- the BD gold suite still passes (control: 76 passed at the base).

<expected_criteria>SC10-e59-AC1,SC10-e59-AC2</expected_criteria>

Dry-run at the base (277fc76bc2, 2026-10-07): SC10-e59-AC1 FAIL as expected (rc=4, no such test file); SC10-e59-AC2 PASS as expected (control, 76 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- No upload, no S3 write, no deploy: these are shipped BD gold/silver files, so the branch is held off CLOUD until its half signs. Never
  push.
- Edit only the ONE file `fix_file` names, plus the new test.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W41-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/silver/build_bd_assets_dim.py
data/black_diamond/scripts/gold/D_03.composition_artifacts.py
data/black_diamond/scripts/gold/tests/test_thread_hop_fix.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-59`.
<owned_cells>SC-e-59</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e59-AC1, SC10-e59-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~41/MDPF_SECCLASS.TO-SC-e59.bd-thread-failing-hop-fix.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e59-AC1,SC10-e59-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the hop fixed (file:line before and after), or the row filed instead; AC1/AC2 outputs; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the BD chain's schedule is unchanged; the fix rides its next deploy, an issuer act under a pair.
comp-iam: DECLARED-NOT-APPLICABLE the BD host role already reads etf-classifications (TO-DEPLOY-e42 preflight); no grant changes.
comp-adversary: RUN -- a fix in a hop the trace did not name (one fix_file only); a fold left in place (the test's three tickers); BLIND: the served page after the deploy (the issuer's real run).
lane: the <paths> block IS the grant.
</preflight>

Source: round-9 analysis @9b6348f15e section 2.1, section 3 item 1; PRD v0.14 (ADMITTED); DECOMP_R10.
