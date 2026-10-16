# NFRA_OPLGTW task order -- `OG-rr-3` -- apply the CRO's 110 ruling_refs to the legacy name_rulings.json rows (CRO file msg 34909; CTO msg 34913)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rr-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rr-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~117</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a registry data file; no schedule, trigger or deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's instruction (msg 34913: "110 of 111 rows resolved by CRO~Z (@61a1df5f8d); cut the backfill ... Backfill the 110, re-run the full-add gate (0 moved), then OG-rr-2 as ruled") applying the CRO's ruling list, which is the CRO's act and not a decision of this cell.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-rr-3` (decomposition addendum R3-T.92, workstream RULING-REF-CRO, FWD-22)

STATE. `infra/logic/registry/name_rulings.json` (JSON object with `_about` and `name_rulings`, a list of 136 rows) has a `ruling_ref` (`<repo-relative path>@<40-hex commit>`) on 25 rows since `OG-rr-1` (`ecd2aad5d0`). The other 111 are legacy rows. The CRO resolved them: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/NAME_RULINGS_BACKFILL_RULING_REFS_20261016.json` is `{"_about": ..., "rows": [{"name", "type", "disposition", "ruling_ref"} x111]}`: 110 rows carry a `ruling_ref`, one (`opal-data-ycharts`, type `S3_BUCKET`) has `ruling_ref: null` and `disposition: "NOT RULED"`.

DO. For each CRO row with a non-null `ruling_ref`, set that string, verbatim, as the `ruling_ref` of the registry row with the same `(name, type)`: add it as the LAST key of the row (the same form `OG-rr-1` used on its 25 rows; read one). Do not edit, shorten, "fix" or re-resolve a ref: it is the CRO's ruling. Before writing, verify each of the 110 with `git cat-file -e <commit>:<path>` (split at the LAST `@`) and print the count; if one does not resolve, do NOT write it: list it in `W/RR3_UNRESOLVED.json` = `{"unresolved": [{"name": ..., "type": ..., "ruling_ref": "<the CRO's string>", "why": "<one line>"}]}` and file a BLOCKING row. The row `opal-data-ycharts` stays without a `ruling_ref` (the CRO's null row; its grade is unchanged). A registry row with a `(name, type)` that has no CRO row and no existing ref stays as it is and is named in the report.
Change NOTHING else: no other field of any row, no existing `ruling_ref`, no row moved, added or removed, `_about` untouched; keep the file's formatting and key order (`git diff` should show added lines and the trailing-comma change on the previous line only). Do it with a short python script of your own that prints the denominators (CRO rows with a ref: 110; applied: n; unresolved: n; rows still without a ref: n) and READ its output before you write the file.

## 2. BOUNDS

- `infra/logic/registry/name_rulings.json` and the files under `W/` only. Not the naming gate, not the CRO file, not any other record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; invent or alter a ref; print an account number or a person's name (a few row names carry an AWS account id: copy them as the file has them and do not echo them in your report).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/logic/registry/name_rulings.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~117/`. Rows: id `NFRA_OPLGTW-Z-W117-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rr3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings: rows 136; carrying a ruling_ref 135, unresolved 0 \(want 0\); CRO refs applied equal 110 of 110, differing 0 \(want 0\); rows without a ref 1 \(CRO null rows 1\); ref where the CRO file has none 0 \(want 0\); rows neither in the CRO file nor carrying a ref 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rr3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings vs ecd2aad5d0: rows 136 to 136; rows moved 0 \(want 0\); rows with another field changed 0 \(want 0\); existing ruling_ref changed 0 \(want 0\); keys added other than ruling_ref 0 \(want 0\); _about equal True; ruling_ref newly added on 110 rows.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the CRO's 110 refs are on the registry rows exactly and all 135 refs in the file resolve; the one null row stays without one. `AC2`: nothing else in the file changed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rr-3.apply-cro-ruling-refs.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the two AC lines, applied and unresolved counts, any registry row with no CRO row).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RULING-REF-CRO (decomposition addendum R3-T.92; a separate workstream because the L6 gate keys one issuer to a round and workstream). The refs are the CRO's rulings (27 cite R9, 4 a CTO ruling, 79 the CRO's record `@61a1df5f8d`); the CVO reads whether a record the CRO wrote today is a sound `ruling_ref` for rows it rules retroactively: that is a CVO judgment, not this cell's.
- Sequence per the CTO: this backfill merges FIRST, then `OG-rr-2` (the gate check; worker `~116` is building it in parallel, its drain waits on this merge), and the full-add re-grade (0 moved) is `OG-rr-2`'s AC2.
- Pre-cut: rr3.AC1 base FAIL as expected (0 of 110 applied); rr3.AC2 base PASS as expected (a bound: nothing has changed yet). All 110 CRO refs resolve in the issuer's main tree today (issuer read).

<status>staged</status>
<round>37</round>
<workstream>RULING-REF-CRO</workstream>
<slot>~117</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
