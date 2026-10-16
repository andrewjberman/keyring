# NFRA_OPLGTW task order -- `OG-ng-2` -- the commit-time naming gate grades a name that has a name_rulings.json row from that row (XA-20261016T034740Z-28da, ruled (a))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ng-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ng-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~114</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a change to one local tool and its self-test; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the cross-adjudication XA-20261016T034740Z-28da, ruled (a) by the laptop cluster lead at 2026-10-16 03:53:14Z (`org/critical_paths/cross_adjudication/20261016T0353Z_XA-20261016T034740Z-28da.md` on box/laptop; its terms are in this order) and the CTO's submission `org/tier1_exec/1.0.0_SA_CTO/deliverables/XADJ_SUBMISSION_NAMING_GATE_READS_NAME_RULINGS_20261016_Z.md`.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ng-2` (decomposition addendum R3-T.80, workstream NAMING-GATE-RULINGS, FWD-22)

THE DEFECT. `.tools/naming-gate.py` (the commit-time gate; ENFORCE is on) never reads `infra/logic/registry/name_rulings.json`. Only `.tools/naming-apply-gate.py` does, through `ruling_amend(rulings, node_type, name, base, addition)` (line ~282; read its docstring and body) and `_rootcheck().load_name_rulings()`. So five rows of `name_rulings.json` (the four Black Diamond identifiers `bd_account_id`, `bd_account_number`, `fact_bd_allocation` (type `hand-kept carrier`), `market_value_profile` (type `INSTANCE_PROFILE`), and `etfs` (type `hand-kept carrier`)) change nothing, and the gate still REFUSES ten lines: eight in `infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py` and two in `infra/aws/ec2/opal-gateway/app/portal_json_served.py` (lines 374 and 376). A release commit that adds those files whole is refused.

THE RULING (verbatim terms). Reuse the `ruling_amend` (name, node type) lookup: a `canonical` row means the name must equal it; a `none_owed` row means RULED with the row cited; no row means the grade is UNCHANGED. The diff is limited to `.tools/naming-gate.py` and its self-test. No override, no rename.

BUILD. In `.tools/naming-gate.py`, in the function that grades one string literal (the one whose body holds the lines `carr = None if lit.built else nm.carrier(lit.value)` and the NEW-carrier branch that returns `"REFUSE", canon, "NEW hand-kept carrier (context rule)..."`, near line 2335 to 2375, and the typed branch after it that calls `nm.grade(typ, graded_as)`):
1. Load the rulings ONCE per run, lazily, through the file's own `_rootcheck()` (line ~2662) `.load_name_rulings()`. If it cannot be read, print one `NAMING RULINGS-NOTICE name_rulings.json could not be read (...); no name is graded from a row` note (as `naming-apply-gate.py` line ~475 does) and grade as today.
2. Where the gate is about to return a REFUSE (or a WARN/OUT-OF-PATTERN) for a literal, look up the row keyed `(name, type)`: the type is `hand-kept carrier` for the carrier branch, and the node type word the gate prints (for example `INSTANCE_PROFILE`) for the typed branch. Reuse `ruling_amend` itself: import it from `.tools/naming-apply-gate.py` with `importlib` (the file name has a hyphen), do NOT copy it. A `none_owed` row, or a `canonical` equal to the name, returns the verdict `RULED` which PASSES (exit 0 in ENFORCE) and prints `NAMING RULED <file>:<line> <string> -> <string>` plus a `why:` line citing the row; a `canonical` different from the name keeps today's REFUSE with the row's canonical named; no row leaves the grade exactly as today. The key is exact: the same string under ANOTHER type is not admitted.
3. The final summary line and the exit code must count `RULED` as a pass (read how the summary tallies verdicts; `NAMING-GATE: PASS <n> graded` for a diff whose only non-conformant strings are RULED).
4. Self-test: add exactly three arms to the existing `--self-test` set, each printing a line in the file's existing arm style `SELF-TEST arm <description>: ok`: (i) `SELF-TEST arm name-rulings admit: a none_owed row for (name, type) grades the planted NEW carrier RULED -> PASS: ok`; (ii) `SELF-TEST arm name-rulings control no-row: the same planted carrier with no row is REFUSE -> REFUSE: ok`; (iii) `SELF-TEST arm name-rulings control other-type: a row for (name, another type) does not admit it -> REFUSE: ok`. The arms inject a small rulings dict; they never write the real `name_rulings.json`. The self-test must stay green with every existing arm.
5. Optionally ONE new test file `.tools/tests/test_naming_gate_rulings.py` (pytest) covering the same three cases plus a `canonical` row that differs (REFUSE) and the unreadable-file notice.
6. Measure: run the gate over the full add of the client modules and `portal_json_served.py` (the construction in `deliverables/2.0.0_SA_COO~O/r37/checks/ng2.AC2.sh`) BEFORE and AFTER, and keep both outputs as `W/NG2_BEFORE.txt` and `W/NG2_AFTER.txt`. AFTER prints no REFUSE and ten RULED lines.

If a refused string has no row, or a row's type word does not match the gate's, do NOT edit `name_rulings.json` (not yours): file a BLOCKING surprise row naming the (name, type) and keep the rest.

## 2. BOUNDS

- The diff outside `org/` is `.tools/naming-gate.py` and at most the one new test file named above. Nothing else: not `naming-apply-gate.py`, not `lib/`, not the registry, not any client module, not a hook.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; set `NAMING_GATE_ENFORCE=0` or remove `org/mcp/naming-gate.enforce`; `# naming-place-override`; print an account number or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
.tools/naming-gate.py
.tools/tests/test_naming_gate_rulings.py
.tools/naming-apply-gate.py
lib/opal_naming.py
lib/opal_naming_rootcheck.py
infra/logic/registry/name_rulings.json
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/app/portal_json_served.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~114/`. You WRITE only `.tools/naming-gate.py`, `.tools/tests/test_naming_gate_rulings.py`, the files under `W/` and the investigation file (append rows only); the rest you only READ. Rows: id `NFRA_OPLGTW-Z-W114-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ng-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)gate self-test: rc=0; PASS lines 1 \(want 1\); name-rulings arms admit [1-9]\d*, no-row control [1-9]\d*, other-type control [1-9]\d* \(want 1 or more each\); failing arms 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ng-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)full-add naming gate over the client modules and portal_json_served in ENFORCE: rc=0; REFUSE verdicts 0 \(want 0\); RULED verdicts (?:1\d|[2-9]\d) \(want 10\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ng-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng2.AC3.sh; echo "exit=$?"</invocation><expect>(?s)outside the allowed two files: 0 \(want 0\); naming-gate.py changed: 1 \(want 1\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the self-test is green and carries the three arms. `AC2`: the ten refused lines are graded RULED and the full-add gate prints no REFUSE in ENFORCE. `AC3`: the diff outside `org/` is `naming-gate.py` and at most one new test file.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ng-2.gate-reads-name-rulings.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the three result lines, the exit code and summary line of the AFTER run).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream NAMING-GATE-RULINGS (decomposition addendum R3-T.80). Origin: worker rows Z-W111-S11..S14 and Z-W113-S1; CTO msgs 34707, 34709, 34713; XA-20261016T034740Z-28da ruled (a). Before merge the issuer re-runs the self-test, plants a name with no row (REFUSE) and a row that admits only its own pair, then re-grades the ten lines; the merge goes through `safe-merge.sh`; `0.0.0_AB_MSTR` announces it to all four boxes. No override.
- Depends on `OG-cl-9` (the `etfs` row) being merged: AC2 needs all five rows on the base.
- Pre-cut: ng2.AC1, ng2.AC2, ng2.AC3 base FAIL as expected (no arms; 10 REFUSE; naming-gate.py unchanged).

<status>complete</status>
<round>37</round>
<workstream>NAMING-GATE-RULINGS</workstream>
<slot>~114</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
