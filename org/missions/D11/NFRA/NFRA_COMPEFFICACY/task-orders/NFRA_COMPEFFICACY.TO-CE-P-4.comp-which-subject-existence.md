# TO NFRA_COMPEFFICACY.TO-CE-P-4 -- comp-which validates a subject's EXISTENCE, not only its shape: a non-existent gold id is refused with the authority named, a misspelled real id is offered candidates, a real subject routes exactly as before, and the verdict is told apart on the spilled rank file

<to_id>NFRA_COMPEFFICACY.TO-CE-P-4</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.9.0_WK_NFRA_COMPEFFICACY~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- issued as round 7's ONE cell on PRD v0.9 @`1feed4008e` (the manual-act addendum on Andrew's ~21:4xZ no-waiting word; row M-3's second limb: "one seat starting one piece of work from the ratified fourteen the same day, 2.0.0_SA_COO naming the seat"), the CVO's second-cut list v3 @`debf661cba` s.4 THE FIRST PIECE (P-4, comp-which F2); decomposition v0.3 s.6. The seat named is this worker slot. Nothing waits: the cut, the spawn and the work are tonight's.</status>

**Directive:** D11 | **Fabric:** laptop | **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.9 (s.9 row M-3; s.5 the marquis list; s.7 row T-3 comp-which's audit) | **Decomp cell:** `CE-p-4` (`../decompositions/NFRA_COMPEFFICACY_DECOMP.md` v0.3, s.6) | **outcome_ref:** FWD-8 (the short list USED: one piece of work started from the fourteen) | **verb:** fix | **depends_on:** none (T-3's audit and C-S46's regression set are on the record; this order changes the router)

---

## THE CELL

`CE-p-4` (the CVO's v3 second cut, s.4, on `comp-which`'s audit finding F2 -- *"the router validates a subject's SHAPE and never its EXISTENCE"*): `.tools/comp-which` matches a gold id by regex (`GOLD_ID = re.compile(r"(?<![\w])(INF_)?[A-DIS]_-?\d{1,2}[a-z]?(?![\w])")`, `:1279`; `gid = GOLD_ID.search(q)`, `:2236`) and routes a NON-EXISTENT gold id with a confident score -- a seat that mistypes a subject is handed a tool and a rank instead of a refusal, the wrong-object error one step before every downstream read. The fixer called it the most consequential finding across the three CE-t cells; the roll-up carried it to the CTO as the highest-value unfixed finding; it sits inside the router every other piece routes through. Andrew ratified the marquis fourteen on 09-04 (record `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260904_095xZ_MARQUIS_14_RATIFIED_COMP_DENYTEST_KEPT_COMP_HEAT_DEVELOP.md`); `comp-which` is number 3 on it, and this order is the first piece of work started from that list -- FWD-8's "the short list USED" reads on this face's record.

⛔ **THE SHAPE THE CVO SET, verbatim as the accept below carries it:** the instrument is `comp-which` itself; a PLANTED non-existent subject (a gold id no registry carries) returns a subject-unresolved verdict NAMING THE AUTHORITY CHECKED, with 0 ranked tool rows presented as a route for it; a real subject (positive control) still routes as before -- the four `when:` phrasings F-10 measured (C-S46) are the regression set, 0 change in their ranked lists; a real-but-misspelled subject (negative control) is NOT routed with confidence -- the nearest real ids are offered as CANDIDATES, marked as such; the spilled rank file carries `subject_resolved: true|false` and the authority consulted, so the verdict is told apart ON THE ARTIFACT; the change is population-side or router-side BY DECLARATION, and P-6's inheritance question (a ranker that never sees the subject check is the next false confidence) is answered in the deliverable.

⛔ **THE AUTHORITY IS FOUND, NOT INVENTED.** Before writing a line, measure where gold ids are registered in this estate (`comp-which "where are gold ids registered"` first; then `comp-find` for the `GOLD_ID` pattern's consumers and for the registry `comp-estate --definitions` names) and print the census: the authority file(s), their id count (the denominator), and a real id from each as the positive control. If more than one authority exists, the check consults ALL and names each; if none is machine-readable, that is a BLOCKING row (the fix cannot honestly claim "no registry carries it" against no registry).

⛔ **A REFUSAL IS NOT A CRASH.** The unresolved verdict is a first-class output in comp-which's own voice (its existing answer-state vocabulary; `comp-read` the tool's header for it), exit code unchanged from its refusal convention, the rank file still spilled with `subject_resolved: false`; the router keeps answering questions that carry no gold id at all exactly as before (the regression set proves it).

## DELIVERABLE

1. The change in `.tools/comp-which` (and, only if the subject check must live beside the ranker, in `.tools/comp-which-routing-test.py`'s fixtures), ASCII-only, `commit-gate` clean.
2. `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/test_cep4_subject_existence.py` -- the battery below -- and `comp-which-subject-existence.result.md`: the authority census, each criterion's invocation and output verbatim with rc and denominator, the before/after ranked lists for the four phrasings (byte-equal), the P-6 answer, any row filed.
3. The proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry** -- your own `deliverables/<serial>/` folder and THIS ORDER'S OWN FILE under `task-orders/` for the `<status>` flip -- and nothing else. A path you need that it does not name is a BLOCKING row, never an override.
- **NEVER widen `comp-which`'s scope**: no new tool routed, no ranking change beyond the subject check, no registry edited (the authority is READ). A registry that is wrong is a row, not an edit.
- **THE REGRESSION SET IS SACRED:** the four `when:` phrasings F-10 measured (C-S46 -- read the CVO's row in `org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/adjudications/` and the NFRA_CLDGRPH F-10 record for the exact strings) produce ranked lists BYTE-EQUAL before and after; capture BEFORE first, on the unpatched tool, into your deliverables folder.
- **`.py` edits pass `bash .tools/commit-gate.sh <file>`** (py_compile + ds-precommit + ruff) -- `.tools/comp-which` is a python script without the extension: run `python -m py_compile .tools/comp-which` and the routing test beside the gate.
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_COMPEFFICACY-W1-S<k>` (append; cite `path@commit`; never edit an existing row).
- **NEVER `git push`.** Report push state as MEASURED.

## ACCEPTANCE

<criterion id="P4-AC1" cell_refs="CE-p-4"><invocation>timeout 600 python org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/test_cep4_subject_existence.py</invocation><expect>CEP4-SUBJECT-EXISTENCE-ENFORCED</expect></criterion>
`P4-AC1` -- a battery you write, printing the token ONLY when every arm holds, each arm invoking the ESTATE'S OWN CLI (`comp-which "<question>"`, never an inner function): (a) THE AUTHORITY CENSUS printed first -- the registry file(s), the id count per file (denominator), one real id per file as the positive control; (b) PLANTED NON-EXISTENT: a question naming a gold id that no registry carries (e.g. `INF_D_99` -- verify it is absent from EVERY authority before planting) returns the subject-unresolved verdict NAMING the authority(ies) checked, with 0 ranked tool rows presented as a route (the ranked-row count printed = 0); (c) POSITIVE CONTROL: the four regression phrasings route with ranked lists BYTE-EQUAL to the captured BEFORE lists (diff empty, printed per phrasing); (d) NEGATIVE CONTROL: a real id misspelled by one character (e.g. a real `INF_D_02` written `INF_D_20` only if `INF_D_20` is absent -- verify) is NOT routed with confidence: the nearest real ids are offered as CANDIDATES and the output marks them as candidates, ranked rows 0; (e) THE ARTIFACT: the spilled rank file for (b), (c) and (d) carries `subject_resolved` as a THREE-value field -- (b) `false`, (c) `not-applicable` with `authority_consulted` EMPTY (0 of the four F-10 regression phrasings carries a gold id, row W1-S1, so nothing was looked up and the field may not say an authority was consulted), (d) `false` -- and a POSITIVE CONTROL question carrying a REAL id (`what does INF_D_02 write to s3`) reading `true` with `authority_consulted` populated; all four printed side by side (RE-CUT 00:1xZ on row W1-S1: the two-value form as first cut, `false`/`true`/`false`, would have asserted a consultation that never happened) and the authority consulted -- printed; (f) a question carrying NO gold id at all routes exactly as before (one of the four phrasings qualifies if it carries none; else a fifth captured BEFORE); (g) `timeout 600 python .tools/comp-which-routing-test.py --binary-ref WORKING --out org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_routing_test_report.json` passes after the change (its own token/rc printed, its header naming `WORKING-TREE` and the blob it scored) -- RE-CUT 00:1xZ on row W1-S3: the bare form as first cut scores the COMMITTED blob (`--binary-ref` defaults to `HEAD`, `:1134`), so it cannot fail on an uncommitted change, and its default `--out` is the CloudComp baseline outside this grant (`:1653`); the bare form's rc is recorded beside it as the harness's own defect, never as this arm's verdict. Denominators on every list.

<criterion id="P4-AC2" cell_refs="CE-p-4"><invocation>python -m py_compile .tools/comp-which; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`P4-AC2` -- the changed script compiles under the estate's Python 3.12; `bash .tools/commit-gate.sh` run beside it on every `.py` you touched, its `pre-commit gate clean` line recorded in the deliverable.

<criterion id="P4-AC3" cell_refs="CE-p-4" judgment="true"/>
`P4-AC3` -- graded by the CVO at L9: whether the check is population-side or router-side and why (declared, with the authority named); P-6's inheritance answer (does every ranker path see the subject check, or is there a path that never does); what a seat now sees on a mistyped subject and whether a person could act on it without a follow-up; and what this fix does NOT cover (a subject that exists in a registry but not in the served graph, say). Evidence with vintage. NO VERDICT.

AMENDMENT 2026-09-10 ~00:1xZ BY THE ISSUER on rows `NFRA_COMPEFFICACY-W1-S1`, `W1-S2`, `W1-S3` (worker branch `wk-nfra_compefficacy-7-1` @`e4c2d4a3e7`), under the standing re-cut authority @`9f4a57262f` / @`1ced87e810`, told to `1.0.0_SA_CTO` and `3.0.0_SA_CVO` the same tick. **W1-S1 (ruled):** clause (e) re-cut above to the three-value field the worker shipped -- the verdict-vocabulary rule (a field with no NOT-EVALUATED value encodes non-evaluation as a verdict) and Taxonomy Law (i)/(iv); the positive control with a real id supplies the `true` reading the two-value form could only have faked. Judged on EFFECT: HARDER. **W1-S3 (BLOCKING, ruled -- the criterion-text half):** arm (g) re-cut above to the parameterised harness form, the only form that can fail on this change; the harness's three defects (default `HEAD`, default `--out` on a committed baseline, non-termination on the unpatched tool at 580 s) are the harness lane's, `0.8.0_AE_CloudComp`, carried to `3.0.0_SA_CVO` for a remediation row. **W1-S2 (ruled, standing at the cut):** `~/bin/comp-which` is a bootstrap shim baked to the MAIN tree's `.tools/comp-which`, so a bare PATH invocation inside a linked worktree runs the file the worker did NOT change and passes GREEN; this face already orders `python .tools/comp-which` by explicit path from the worktree root and the battery prints the absolute path it ran -- every future cell that edits a `.tools/comp-*` binary carries the same clause at the cut; the shim's worktree-blindness is CloudComp's, carried with S3. No re-run is owed for these amendments where the battery already prints the re-cut readings; `<invocation>` and `<expect>` UNCHANGED.

<expected_criteria>P4-AC1, P4-AC2, P4-AC3</expected_criteria>

<paths>
.tools/comp-which
.tools/comp-which-routing-test.py
org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/
org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
The `<paths>` block IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. The registries the authority census finds are READ, never edited; `.tools/comp-estate`, `.tools/comp-find` and the population authority `comp-coverage-map.yaml` are instruments, not surfaces.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> v0.3, cell `CE-p-4`.
<owned_cells>CE-p-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_COMPEFFICACY, comp-which or the comp-tool registry (0 hits for those tokens across the ledger output). BLIND SPOT: none that bears -- a repo-only code cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud plane touched.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants; `.tools/comp-which`'s owning lane (CloudComp, T-3) is not a seat tonight -- the worker's grant is the paths, stated in the decomposition.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `P4-AC1`, `P4-AC2`, `P4-AC3`. Instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/NFRA_COMPEFFICACY.TO-CE-P-4.comp-which-subject-existence.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> P4-AC1,P4-AC2,P4-AC3` BEFORE the complete flip, which you commit yourself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
