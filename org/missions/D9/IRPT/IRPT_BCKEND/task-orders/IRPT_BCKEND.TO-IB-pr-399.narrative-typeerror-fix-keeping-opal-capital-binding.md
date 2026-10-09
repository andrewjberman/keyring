# TO IRPT_BCKEND.TO-IB-pr-399 -- irpt-narrative: fix the TypeError while a no-row internal caller stays bound to opal-capital (no widening); release packet

<to_id>IRPT_BCKEND.TO-IB-pr-399</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~264</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>102</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO half @7f294053f0 (msg 2765) on row D2-W262-S1 | **Decomp cell:** `IB-pr-399` (decomposition section 95) | **outcome_ref:** FWD-2 (the narrative census row reads ONE; gates IRPT_ANLREQ FWD-1's seat run)

---

## WORKER FACE

**The gap (row IRPT_BCKEND-D2-W262-S1).** IB-pr-394 fixed narrative's TypeError by restaging `errors.py` and `served.py` to
`74a62fb46c`. That rebuild honours `selected_tenant`, so a NO-ROW Opal internal caller selecting inflection is admitted. Live
narrative binds every internal caller to `opal-capital` and ignores the selection, so the rebuild WIDENS reach. The CTO held it.

**Your cell** (worktree `C:/dev/wk-irpt-bckend-264`; keep scratch outside it):
1. **Fix the TypeError** with the IB-pr-394 approach, read in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~262/` and `infra/aws/lambda/ci/lambda-source-map.json`.
2. **Keep narrative's existing binding:** a NO-ROW internal caller is bound to `opal-capital` whatever it selects. Do it in
   narrative's own code (`infra/aws/lambda/investor-reporting/narrative/`), never by changing shared `served.py` for other
   hosts. A caller with a profile row is narrowed as the other hosts do.
3. **Tests** in narrative's tests, names containing `opal_capital_binding`, at least 2:
   - a no-row internal caller selecting inflection is bound to opal-capital;
   - a row-listed caller is narrowed.
   The `served_error_path` tests and the narrative suite still pass.
4. **Release packet:**
   - census and BUILD_ONLY (twice, clean tree) at the real map;
   - a replay with an arm named `no_row_internal_selects_other_firm` that reads IDENTICAL live versus built, plus a negative
     control;
   - the packet, with Branch A/B.
   Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~264/IB102-3_release_census.json` (`{pin, artifacts:[{name,built_sha256,live_before,changed_members}], build_only:{rc,tree_clean}}`),
   `IB102-3_release_replay.json` (`{arms:[{name,verdict,negative_control}]}`) and `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-399.md`.

<criterion id="IB102-3-AC1" cell_refs="IB-pr-399"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r102/p102_cells.py" . IB102-3-AC1</invocation><expect>IB102-3-AC1 PASS</expect></criterion>
<criterion id="IB102-3-AC2" cell_refs="IB-pr-399"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r102/p102_cells.py" . IB102-3-AC2</invocation><expect>IB102-3-AC2 PASS</expect></criterion>

<expected_criteria>IB102-3-AC1, IB102-3-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests, source-map restage, BUILD_ONLY and offline replays only; no upload, apply or
  deploy. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W264-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~264" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~264@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~264 <0.9.0_WK_IRPT_BCKEND~264@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/narrative/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~264/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-399.narrative-typeerror-fix-keeping-opal-capital-binding.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 95 (round 102, workstream ~P), cell `IB-pr-399`.
<owned_cells>IB-pr-399</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB102-3-AC1, IB102-3-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~264/IRPT_BCKEND.TO-IB-pr-399.narrative-typeerror-fix-keeping-opal-capital-binding.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the fix, the pin, the built sha256 and live_before, the replay verdicts, the commit hashes, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- irpt-narrative only; its TypeError (row W201-S6) plus the opal-capital binding live holds (row W262-S1); no other host moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p102_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~07:2xZ: AC1 FAIL (-k opal_capital_binding selects 0 of 44), AC2 FAIL (no census); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's narrative code (CTO half @7f294053f0).
</preflight>
