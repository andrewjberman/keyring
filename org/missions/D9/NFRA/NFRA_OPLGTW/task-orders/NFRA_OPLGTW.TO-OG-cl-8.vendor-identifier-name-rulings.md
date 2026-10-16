# NFRA_OPLGTW task order -- `OG-cl-8` -- the naming gate admits the Black Diamond upstream identifiers through name_rulings.json; the unread orion/4698 alias goes (CTO ruling @d97ea3ae82 section 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-8</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-8</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a registry data row, one alias deletion and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @d97ea3ae82 section 1 (file `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md`, read it at that commit with `git show d97ea3ae82:<path>`), on your own rows Z-W111-S7 and Z-W111-S8.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cl-8` (decomposition addendum R3-T.78, workstream G2-CONFORM-2, FWD-22)

Your OG-cl-7 left the naming gate REFUSING eight strings in `app/client_adapter_bd49f.py` (your rows Z-W111-S7 and Z-W111-S8). The CTO ruled: neither a new registry class nor a departure. The estate already has the carrier, `infra/logic/registry/name_rulings.json` (read its `_about` block first: a row is `name`, `type`, EXACTLY ONE of `canonical` or `none_owed`, `evidence`, `owner`; unique per `(name, type)`).

1. **Rows.** Run the same full-add naming gate you ran for `W/CL7_AFTER.txt` (the construction in `deliverables/2.0.0_SA_COO~O/r37/checks/cl7.AC2.sh`, over every `app/client_*.py` added whole) and read the type word the gate prints for each refused string. For EACH distinct `(name, type)` among `bd_account_id`, `bd_account_number`, `fact_bd_allocation` and `market_value_profile`, add ONE row to `name_rulings.json` with `none_owed` = "a Black Diamond upstream identifier (column, table or response key) that the adapter reads exactly as the vendor publishes it; Opal mints no name here", `evidence` = the gate line and the `client_adapter_bd49f.py:<line>` (the text must contain that file:line), and `owner` = "the Black Diamond vendor schema". Do not add a `canonical`. Do not add any row for a name the gate does not refuse. Keep the file's JSON formatting (indent, key order) unchanged elsewhere.
2. **The alias.** Delete the unread `orion/4698` key from the firm alias map in `app/client_core.py` (the line `"aliases": {short49: k49, "orion/4698": kinf, "4698": kinf}`) and its mention in the module docstring (line 10). Add no registry row for it. Keep `4698`. Behaviour of every other alias is unchanged.
3. **If the gate does not consult `name_rulings.json` for a type** (a refusal that remains after the rows exist): do not rename, do not override. File a BLOCKING surprise row naming the (name, type) and the gate file/line that did not consult the file, and keep the rest.
4. Re-run the full-add gate (write `W/CL8_AFTER.txt`) and the client suites.

## 2. BOUNDS

- Code and one registry data file only. No release, no deploy, no placement override, no `# naming-place-override`, no rename of a vendor column, no edit to `.tools/naming-gate.py`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number or a person's name; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/logic/registry/name_rulings.json
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/tests/test_og_cl1.py
infra/aws/ec2/opal-gateway/tests/test_og_cl7.py
.tools/naming-gate.py
infra/logic/02_DOCTRINE.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/`. You WRITE only `name_rulings.json`, `client_core.py`, the investigation file (append rows), the files under `W/` and, if a test must follow the alias deletion, `tests/test_og_cl1.py` or `tests/test_og_cl7.py`. You only READ the rest. Rows: id `NFRA_OPLGTW-Z-W111-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)client suites: pytest rc=0; passed [0-9]+ \(want at least 49\); failed 0.*host-shaped import: client modules import without lib/opal_naming True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cl-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl7.AC2.sh; echo "exit=$?"</invocation><expect>(?s)naming gate over the client modules in ENFORCE: rc=0; REFUSE verdicts 0 \(want 0\); hand-kept firm literals 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-cl-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl8.AC3.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings: rows for the 4 identifiers 4 of 4 \(none_owed, evidence file:line\); unique per \(name, type\) True; orion/4698 alias gone True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the client suites still pass and the modules still import in the host shape. `AC2`: the full-add naming gate in ENFORCE prints no REFUSE. `AC3`: the four registry rows exist and the unread alias is gone.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-8.vendor-identifier-name-rulings.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the three result lines, the gate's type word per name).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-CONFORM-2 (decomposition addendum R3-T.78). The CTO named this cell as an OG-ap-23 batch cell (msg 34699); it merges before OG-ap-23's release cut. When it passes, the issuer closes `OG-cl-7` (its AC2 is the same check).
- Pre-cut: cl8.AC3 base FAIL as expected; cl7.AC2 base FAIL as expected (8 REFUSE); cl7.AC1 base PASS (the suites, unchanged by the cut).

<status>complete</status>
<status_reason>closed by the issuer 2026-10-16: the worker's AC2 FAIL was the commit-time naming gate not reading name_rulings.json; OG-ng-2 (merged f1b3aeb579, XA-20261016T034740Z-28da) fixed the gate and the issuer re-ran cl7.AC2 on trunk f1b3aeb579: rc=0, REFUSE 0, firm literals 0, PASS. AC1 PASS in the worker's instance and re-run.</status_reason>
<round>37</round>
<workstream>G2-CONFORM-2</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
