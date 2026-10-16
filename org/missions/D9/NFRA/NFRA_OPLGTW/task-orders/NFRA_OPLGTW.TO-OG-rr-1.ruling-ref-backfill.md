# NFRA_OPLGTW task order -- `OG-rr-1` -- every name_rulings.json row carries a `ruling_ref` (path@commit) that resolves, or is listed unresolved (CTO ruling @8b9adcbd8d section 3 cell 1; CVO verdict 6495)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rr-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rr-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~115</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a registry data file; no schedule, trigger or deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (@8b9adcbd8d section 3 cell 1) on the CVO's verdict 6495: "the gate should check that ruling_ref names a record that exists at a commit, and refuse the row if it does not, not just print the field. A free-text field that only gets printed becomes a lift by assertion." This cell adds the field; the gate check is the later cell `OG-rr-2`.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-rr-1` (decomposition addendum R3-T.89, workstream RULING-REF, FWD-22)

`infra/logic/registry/name_rulings.json` is a JSON object with a key `_about` and a key `name_rulings`: a list of 136 rows. Each row has `name`, `type`, `evidence`, `owner`, and exactly one of `canonical` (60 rows) or `none_owed` (76 rows). No row has a `ruling_ref` yet.

1. Add `ruling_ref` to EVERY row for which a ruling record can be found: a string `<repo-relative path>@<full 40-hex commit sha>` such that `git cat-file -e <commit>:<path>` succeeds. The record is the committed file the row's own `evidence` text cites (a ruling file, a task order, a surprise-channel row file, an adjudication file). Read the row's `evidence`; find the file it names; resolve the commit with `git log -1 --format=%H -- <path>` (the latest commit that carries the file) and use that full sha. Rows from the CTO ruling @d97ea3ae82 cite `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md`.
2. A row whose ruling cannot be found in this repository (its evidence cites nothing, cites only a message id, or cites a record not present locally) gets NO `ruling_ref` and NO invented one. List it in `W/RULING_REF_UNRESOLVED.json` = `{"unresolved": [{"name": "<name>", "type": "<type>", "evidence_cites": "<what the evidence cites>", "why": "<one line>"}]}`, so the CRO can rule it. Every row is in exactly one place: it carries a resolving `ruling_ref`, or it is listed unresolved.
3. Change NOTHING else: no other field of any row, no row moved, added or removed, `_about` untouched. Keep the file's existing formatting and key order (add `ruling_ref` as the last key of each row; `git diff` should show only added lines and the trailing-comma change on the previous line).
4. Method note: this is 136 small lookups, so do it with a short python script of your own (in your scratchpad or under `W/`) that prints, per row, the cited path candidates and the resolved commit, and READ the output before writing the file; never write a ref you have not verified with `git cat-file -e`. Print the denominator (rows resolved, rows unresolved, total 136).

## 2. BOUNDS

- `infra/logic/registry/name_rulings.json` and the files under `W/` only. The naming gate (`.tools/naming-gate.py`) is NOT touched in this cell.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a check; invent a ref; print an account number or a person's name; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/logic/registry/name_rulings.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~115/`. Rows: id `NFRA_OPLGTW-Z-W115-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rr1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings: rows 136; ruling_ref resolves \d+; listed unresolved \d+; neither \(defect\) 0 \(want 0\); in both 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rr1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings vs a9dd9aff6c: rows 136 to 136; rows moved 0 \(want 0\); rows with another field changed 0 \(want 0\); keys added other than ruling_ref 0 \(want 0\); _about equal True; rows carrying ruling_ref \d+.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every row either has a `ruling_ref` that resolves in git or is listed unresolved, and none is in both or neither. `AC2`: nothing in the file changed except the added `ruling_ref` keys.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rr-1.ruling-ref-backfill.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the two AC lines, resolved and unresolved counts, and the unresolved list by `(name, type)`).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RULING-REF (decomposition addendum R3-T.89). Held since ~07:0xZ until `OG-ap-23` released (cutting earlier would have changed `name_rulings.json` under the release's commit); `OG-ap-23` closed 20261016T092154Z, so it is cut now. Slot `~115` (a finished worker cannot be resumed; the worker that landed the rows was `~111`).
- Pre-cut: rr1.AC1 base FAIL as expected (`RULING_REF_UNRESOLVED.json` absent); rr1.AC2 base PASS as expected (a bound check: nothing has changed yet). The AC1 PASS arm was not exercised before the cut (the check reads fixed repo paths); the worker's run is its first PASS-arm run, and the issuer re-runs it in the main tree at the drain (a sparse tree has misled a gate-reading check once today).
- `OG-rr-2` (the gate refuses a row whose `ruling_ref` does not resolve; planted rows; full-add re-grade moves 0) is cut only after this merges.

<status>complete</status>
<round>37</round>
<workstream>RULING-REF</workstream>
<slot>~115</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
