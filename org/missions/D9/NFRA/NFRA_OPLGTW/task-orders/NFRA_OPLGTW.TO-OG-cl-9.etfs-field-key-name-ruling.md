# NFRA_OPLGTW task order -- `OG-cl-9` -- one name_rulings.json row for `etfs`, the served etf_returns object's own key (CTO msg 34709)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-9</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-9</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one registry data row; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's instruction (msg 34709, "add the etfs name_rulings row now ... no override"), the same carrier and shape as your OG-cl-8 rows.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cl-9` (decomposition addendum R3-T.79, workstream G2-CONFORM-3, FWD-22)

The naming gate refuses the string `etfs` in `infra/aws/ec2/opal-gateway/app/portal_json_served.py` at lines 374 and 376 (worker row NFRA_OPLGTW-Z-W113-S1): it is the key of the portal's served `etf_returns` object (`json/benchmarks/etf_returns.json`), read exactly as the object publishes it. Do exactly what you did for the four Black Diamond identifiers in OG-cl-8, for this one name:

1. Add ONE row at the end of `infra/logic/registry/name_rulings.json` (the same row shape and indentation as your four rows): `name` = `etfs`; `type` = `hand-kept carrier`; `none_owed` = "the key of the portal's served etf_returns object (json/benchmarks/etf_returns.json), read exactly as the object publishes it; Opal mints no name here"; `evidence` = "naming-gate.py at the commit of infra/aws/ec2/opal-gateway/app/portal_json_served.py (worker 0.9.0_WK_NFRA_OPLGTW~113, row NFRA_OPLGTW-Z-W113-S1) graded NAMING REFUSE infra/aws/ec2/opal-gateway/app/portal_json_served.py:374 and :376 etfs as a hand-kept carrier; the string is the served object's own field key, measured at HEAD, not minted by the code."; `owner` = "the portal served etf_returns object schema". No `canonical`. No other row. Change nothing else in the file.
2. Confirm the line numbers 374 and 376 still hold the `etfs` string at your HEAD (`portal_json_served.py`); if they moved, write the true numbers in `evidence`.

## 2. BOUNDS

- One registry data row. No code, no rename, no `# naming-place-override`, no edit to `.tools/naming-gate.py`, no other file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/logic/registry/name_rulings.json
infra/aws/ec2/opal-gateway/app/portal_json_served.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE only `name_rulings.json`, the files under `W/` and the investigation file (append rows, only if you hit a surprise); you only READ `portal_json_served.py`. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/`. Rows: id `NFRA_OPLGTW-Z-W111-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl9.AC1.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings: etfs rows 1 of 1; unique per \(name, type\) True; black diamond rows kept 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the one `etfs` row exists, unique per (name, type), and the four Black Diamond rows are kept.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-9.etfs-field-key-name-ruling.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSES, and report once (commit hash, the AC1 line).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-CONFORM-3 (decomposition addendum R3-T.79). The issuer cannot commit `infra/logic/registry/` (lane PLATFORM_LOGIC_DOCS); a worker commits it under an order that names the path, as OG-cl-8 did.
- Whether the commit-time gate READS the row is the cross-adjudication XA-20261016T034740Z-28da; this cell lands the row regardless.
- Pre-cut: cl9.AC1 base FAIL as expected (0 etfs rows).

<status>pending</status>
<round>37</round>
<workstream>G2-CONFORM-3</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
