# NFRA_OPLGTW task order -- `OG-rr-2` -- the commit-time naming gate checks `name_rulings.json` rows' `ruling_ref` (CTO ruling @8b9adcbd8d section 3 cell 2; CTO msg 34906; CVO verdict 6495)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rr-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rr-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~116</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a commit-time gate script and its test; no schedule, trigger or deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (@8b9adcbd8d section 3 cell 2: "naming-gate.py refuses a row whose ruling_ref does not resolve. Its selftest gains a planted unresolved row (REFUSE) and a resolved one (RULED). Before cell 2 merges, re-run the full-add gate over the repo, and print the number of names whose grade moved (expected 0)") as scoped by the CTO's msg 34906 ("OG-rr-2 refuses (a) a present ruling_ref that does not resolve, and (b) a row added after ecd2aad5d0 with no ruling_ref. The 111 legacy rows keep today's grade (moved 0)"), on the CVO's verdict 6495: "A free-text field that only gets printed becomes a lift by assertion."
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-rr-2` (decomposition addendum R3-T.90, workstream RULING-REF-GATE, FWD-22)

STATE. `OG-rr-1` merged at `ecd2aad5d0`: `infra/logic/registry/name_rulings.json` (136 rows) now has a `ruling_ref` string (`<repo-relative path>@<40-hex commit>`) on 25 rows; the other 111 are LEGACY rows with no `ruling_ref` (listed in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~115/RULING_REF_UNRESOLVED.json`; the CRO is finding their rulings). `.tools/naming-gate.py` (the commit-time gate; ENFORCE is on) already reads the rows through `ruling_amend` and the lazy `_rootcheck().load_name_rulings()` (cell `OG-ng-2`, `b7cbb3e93f`; read it first, and the existing test `.tools/tests/test_naming_gate_rulings.py` as the model).

THE RULING (verbatim scope). Add exactly two refusals, nothing else:
(a) A `ruling_ref` that is PRESENT on a row must RESOLVE: `git cat-file -e <commit>:<path>` succeeds for `path@commit` (split at the LAST `@`). A present ref that is not a `path@commit` string, or does not resolve, makes the gate REFUSE, naming the row `(name, type)` and the ref, in ENFORCE exit non-zero.
(b) A row that is ADDED by the commit being graded (present in the staged `name_rulings.json`, absent from the same file at `HEAD`, keyed `(name, type)`) must carry a `ruling_ref` that resolves; without one the gate REFUSES, naming the row. A row that is present at `HEAD` with no `ruling_ref` (a legacy row) is NOT refused and its grade is UNCHANGED. A row modified at HEAD-present keys (a legacy row gaining a ref) is graded under (a).

WHEN THE LIMB RUNS. Only when `infra/logic/registry/name_rulings.json` is among the staged paths the gate is graded on (read how the gate receives `--staged-paths` / the staged set, and how its other registry limbs scope themselves; copy that form). Read the staged bytes (the index), and the HEAD bytes with `git show HEAD:<path>`; never the working-tree copy. If the file cannot be read or parsed, print one notice line in the file's existing style and grade as today (no new refusal on an unreadable file; an unparseable staged file is already someone else's refusal).

BUILD in `.tools/naming-gate.py` only (a small new function plus one call site and the output line in the file's existing verdict style, e.g. `NAMING REFUSE name_rulings.json (<name>, <type>) ruling_ref <ref> does not resolve`), and four self-test arms in the existing `--self-test` set, each printing a line in the file's arm style `SELF-TEST arm <description>: ok`, with exactly these arm descriptions:
1. `ruling-ref refuse-unresolved: a planted row whose ruling_ref names a path@commit that does not exist -> REFUSE`
2. `ruling-ref admit-resolved: a planted row whose ruling_ref resolves -> admitted`
3. `ruling-ref refuse-new-row-no-ref: a planted row added with no ruling_ref -> REFUSE`
4. `ruling-ref legacy-row-unchanged: a planted row present at HEAD with no ruling_ref -> not refused, grade unchanged`
The arms inject small dicts / planted staged content; they NEVER write the real `name_rulings.json`. The self-test stays green with every existing arm. Optionally extend `.tools/tests/test_naming_gate_rulings.py` with the same four cases (pytest).

MEASURE. `rr2.AC2.sh` runs the full-add gate over the 17 release modules with the pinned pre-cell gate and with yours and compares the verdict lines: names whose grade moved must be 0. Keep its output as `W/RR2_FULLADD.txt` and print the number.

If any of the four arms cannot be written as described, do NOT bend the semantics: file a BLOCKING row and keep the rest.

## 2. BOUNDS

- Writes: `.tools/naming-gate.py`, `.tools/tests/test_naming_gate_rulings.py`, the files under `W/` and the investigation file (append rows only). Nothing else: not `infra/logic/registry/name_rulings.json`, not `naming-apply-gate.py`, not `lib/`, not a hook.
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
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~116/`. You WRITE only the first two files, the files under `W/` and the investigation file; the rest you only READ. Rows: id `NFRA_OPLGTW-Z-W116-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rr2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)gate self-test: rc=0; PASS lines 1 \(want 1\); ruling-ref arms refuse-unresolved [1-9]\d*, admit-resolved [1-9]\d*, refuse-new-row-no-ref [1-9]\d*, legacy-row-unchanged [1-9]\d* \(want 1 or more each\); failing arms 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rr2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)full-add re-grade over 17 release modules: old gate rc=0, new gate rc=0; verdict lines old \d+, new \d+; verdict lines that differ \(names whose grade moved\) 0 \(want 0\); new-gate REFUSE verdicts 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the self-test is green and carries the four ruling_ref arms. `AC2`: the gate with the new limb grades every name of the 17 release modules exactly as the gate before it did (0 moved) and prints no REFUSE.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rr-2.gate-checks-ruling-ref.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the number of names whose grade moved, the four arm lines).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RULING-REF-GATE (decomposition addendum R3-T.90; a second workstream of the project: the L6 gate keys one issuer to the round and workstream). Cut on the CTO's ruling msg 34906 (yes to REC: refuse a present unresolved ref and a new row with none; the 111 legacy rows keep today's grade and go to `4.0.0_SA_CRO~Z` to resolve). The "row added" test is per commit (staged vs HEAD), so it needs no list file and a legacy row that gains a ref becomes graded under (a).
- Pre-cut: rr2.AC1 base FAIL as expected (0 of the four arms present, self-test green otherwise); rr2.AC2 base PASS as expected (a control: the pinned gate and the unchanged gate agree, 0 moved; 11 verdict lines).
- A weakness stated: the PASS arm of rr2.AC1 and the "moved 0" arm are both exercised only by the worker's run; the issuer re-runs both in the main tree at the drain, and plants one row of each kind in a throwaway staged commit if the self-test arms leave doubt.

<status>complete</status>
<round>37</round>
<workstream>RULING-REF-GATE</workstream>
<slot>~116</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
