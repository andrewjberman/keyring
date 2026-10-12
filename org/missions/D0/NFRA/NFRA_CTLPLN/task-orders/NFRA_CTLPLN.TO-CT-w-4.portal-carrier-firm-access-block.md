# TO NFRA_CTLPLN.TO-CT-w-4 -- round 8 CT-w-4: the portal's firm-access matrix becomes a generated block of the same registry file (FWD-28, step 8)

<to_id>NFRA_CTLPLN.TO-CT-w-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~65</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-4` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`) | **outcome_ref:** FWD-28 |
**depends_on:** `CT-w-1` (same worker's queue, after `CT-w-2`; staged until the issuer hands it over)

---

## WORKER FACE

### THE CELL

After `CT-w-1` the registry file `infra/logic/registry/firm_pages.json` is the single source of which firm may read which portal page. The portal's own matrix, `portal/src/lib/firmAccess.ts` (`FIRM_ALLOWED_PATHS`), is still hand-kept. CTO point 4 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_CTLPLN_CT_V2_FIRM_ACCESS_REGISTRY_FIVE_POINTS_20261012.md`): the portal carrier is a second order, DEV first with a drift test, the gitlink after; `firmAccess.ts` is a product file on partner-facing pages, so its PROD push waits on Andrew's word. You PREPARE the carrier; you land NOTHING in the portal's DEV or PROD and you do not move the gitlink. Plan of record: `PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md` (`deliverables/0.9.0_WK_NFRA_CTLPLN~64/`) sections 1 (one-writer consequence) and 3 (the portal target).

### BUILD

1. **The builder edit to `lib/opal_naming.py`, its OWN commit through `.tools/commit-gate.sh`**: a second VIEWS target `("portal/src/lib/firmAccess.ts", "mjs", ("FIRM_ALLOWED_PATHS",))` with the entries it needs in `TARGET_REGISTRY_KEYS` (reads `firm_pages`), BLOCKS and a renderer `_blk_firm_allowed_paths`. It is NOT a whole-file target: the hand-kept header, `INTERNAL_FIRM_ID`, `FIRM_EXEMPT_PATHS` and the functions stay hand-kept. The existing `_mjs_span` ends a block at a line `});` (about lines 1398-1406) and `FIRM_ALLOWED_PATHS` closes with a line `}`, so write a NEW span rule for this block (a block that ends at the first line that is exactly `}` after its open). The generated block must reproduce the object literal's shape (`'<firm>': new Set([ '<path>', ... ]),`) so that the portal's code reads it unchanged.
2. **Regenerate into the portal checkout of YOUR worktree**: `python -I lib/opal_naming.py generate --out . --target portal/src/lib/firmAccess.ts` (the nested portal worktree is on branch `wk-NFRA_CTLPLN-65-portal`). The first generate inserts the block over the existing object; show the portal diff: every firm and every path of the hand-kept matrix must appear in the generated block exactly (the new block's content must equal the old object's content set-for-set; DELTA = 0 in meaning). If it does not, STOP and file a BLOCKING row: the registry rows or the renderer are wrong. Commit the portal change ONLY on the portal worktree's own branch (`git -C portal ...`); never on DEV, never on PROD, never push.
3. **Tests** in a new `lib/tests/test_opal_naming_firm_access_ts.py` (workspace side): T1 the generated block in the portal file equals a fresh render; T2 everything OUTSIDE the block (the hand-kept lines) is byte-identical to the file at the portal's DEV commit you branched from; T3 set equality of firm -> paths between the generated block and the hand-kept object at that commit (read from `git -C portal show <commit>:src/lib/firmAccess.ts`, parsed by a small regex in the test); T4 the mark names `firm_pages.json`. The test names no firm itself.
4. **Say in your report** what the PORTAL-side drift test must be (a one-paragraph spec for the portal repository's CI: it fails if a hand edit changes the block) without writing it: the portal repo's test tooling needs `node_modules`, which this worktree does not have. The CTO rules the portal-side test.

### RULES FOR THIS CELL

Your write surface is the `<paths>` below. You land nothing in the portal's DEV or PROD, push nothing, and do not commit the workspace's `portal` gitlink. You run no terraform and no aws and no portal build. Use `.tools/safe-commit.sh` for workspace commits and plain `git -C portal commit` with author `0.9.0_WK_NFRA_CTLPLN~65 <0.9.0_WK_NFRA_CTLPLN~65@opal.agent>` for the portal worktree's branch. If the naming gate REFUSES a commit, STOP and file a BLOCKING row. No non-ASCII added. The law files CLAUDE.md and org/XXX.md are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W65-S<k>`, continuing your numbering) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw4-AC1" cell_refs="CT-w-4"><invocation>python -m pytest -q lib/tests/test_opal_naming_firm_access_ts.py</invocation><expect>passed</expect></criterion>
`CTw4-AC1` -- T1-T4 pass, set equality included.

<criterion id="CTw4-AC2" cell_refs="CT-w-4"><invocation>python -I lib/opal_naming.py targets</invocation><expect>firmAccess.ts</expect></criterion>
`CTw4-AC2` -- the target list names the portal file (the line says it ships through portal CI).
</proof_of_spec>

<expected_criteria>CTw4-AC1,CTw4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~65/NFRA_CTLPLN.TO-CT-w-4.portal-carrier-firm-access-block.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTw4-AC1,CTw4-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-4</owned_cells>
</decomp_ref>

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming_firm_access_ts.py
portal/src/lib/firmAccess.ts
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a generated block that differs in meaning from the hand-kept matrix and changes what a partner firm sees (T3 set equality; STOP if not equal); a hand edit inside the portal checkout the workspace gate cannot see (the portal-side drift test, specified for the CTO); the portal file landed on DEV or PROD by the worker (forbidden; only the worktree branch is written); the gitlink moved (forbidden); BLIND: the portal repository's CI and typecheck, which need node_modules.
risk: WORLD is declared because the L6 gate derives a floor from the lib and portal paths; this cell lands nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ROUND_ANALYSIS.round7.md` section 3 (E10 b), CTO ruling msg 108481 point 4, the proposal sections 1 and 3.
