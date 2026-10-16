# NFRA_OPLGTW task order -- `OG-cl-10` -- the etfs name_rulings.json row cites the CTO ruling it rests on (CTO msg 34732)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-10</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-10</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one registry data field; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's instruction (msg 34732): "Put my ruling path in its evidence field, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md, so the row names the ruling it rests on."
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cl-10` (decomposition addendum R3-T.82, workstream G2-CONFORM-4, FWD-22)

In `infra/logic/registry/name_rulings.json`, the row you added in OG-cl-9 (`name` `etfs`, `type` `hand-kept carrier`) must name the ruling it rests on. Append ONE sentence to that row's `evidence` string, after its final full stop and one space: "The row rests on the CTO's ruling org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md (section 1: one none_owed row per refused (name, type), no new class, no override) and the CTO's instruction msg 34709." Change nothing else: not the other fields, not any other row, not the file's formatting. Do NOT touch the four Black Diamond rows.

## 2. BOUNDS

- One field of one registry row. No code, no other file, no override.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/logic/registry/name_rulings.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE only `name_rulings.json`, the files under `W/` and the investigation file (append rows, only if you hit a surprise). `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/`. Rows: id `NFRA_OPLGTW-Z-W111-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl10.AC1.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings: etfs row 1 of 1 True; evidence cites the CTO ruling file True; row otherwise kept True; black diamond rows kept 4 of 4; unique per \(name, type\) True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the one `etfs` row cites the ruling file in its evidence and is otherwise kept; the four Black Diamond rows are kept.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-10.etfs-row-cites-ruling.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSES, and report once (commit hash, the AC1 line).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-CONFORM-4 (decomposition addendum R3-T.82). The issuer cannot commit `infra/logic/registry/` (lane PLATFORM_LOGIC_DOCS); the lane that admitted the four rows is a worker order that names the path (CTO msg 34732: "land it through the lane that admitted the four rows, with no new override"). dell1's after-the-fact review ACCEPTED the gate fix and put a lane finding (no ruling_ref on the file) with the CVO; nothing is held on it.
- Pre-cut: cl10.AC1 base FAIL as expected (the row's evidence does not cite the ruling).

<status>pending</status>
<round>37</round>
<workstream>G2-CONFORM-4</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
