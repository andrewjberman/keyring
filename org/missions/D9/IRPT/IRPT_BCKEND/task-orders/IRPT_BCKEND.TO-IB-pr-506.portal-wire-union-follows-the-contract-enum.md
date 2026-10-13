# TO IRPT_BCKEND.TO-IB-pr-506 -- the portal's `HoldingsSnapshot` wire union and type follow the contract's `asset_class` enum, `multi_asset` included (row D2-S127; CTO round-174 analysis section 1)

<to_id>IRPT_BCKEND.TO-IB-pr-506</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~357</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>174</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-174 ANALYSIS (msg 6812) section 1 (row D2-S127) and section 2 item 2, and RE 6807/6809 | **Decomp cell:** `IB-pr-506` (decomposition section 166) | **outcome_ref:** FWD-3

---

## WORKER FACE

**AMENDMENT 2 (issuer, 2026-10-13T06:2xZ; supersedes the cell's direction and steps 1 to 3 where they differ; CTO RE 6818 and round-174 analysis section 3 @cbcc4a88b8):** the CTO WITHDREW the ruling that moved the wire to the contract's enum. Andrew-direct 2026-10-07 ("there should be no multi-asset class. There are 6 classes") stands: the portal test `iv-e-148` (`six_class (d)`: the wire type admits no retired token at any class enum) is NOT to be edited and must pass, and the contract keeps `multi_asset` only as a RETIRED member so its published bytes do not narrow. So: (1) the wire type keeps the SIX classes: change the wire GENERATOR (in `src/pages/InvestorReporting/__tests__/fe-s-13/`) to subtract a named RETIRED set, exactly `{multi_asset}` (a constant with a comment citing Andrew-direct 2026-10-07 and dell1 TO-SC-e100), from every `asset_class`-style enum it emits; regenerate; the generated files may then differ from HEAD by ONE thing only, the optional `account_id?: string` on the nodes block (granted in AMENDMENT 1); `contracts/wire/HoldingsSnapshot.ts` must contain no `multi_asset`. (2) edit `IVE48-AC1` arm 1 in `__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx` so it asserts the wire union EQUALS the contract's enum MINUS its retired members, the retired set named in the test as exactly `{multi_asset}` (so a new retired member, or a new active one, still fails it); change nothing else in that test. (3) the ADAPTER carries one runtime guard in `contracts/adapt.ts`: a served `multi_asset` value is shown as not classified (it folds to `unclassified` already: keep that) and is LOGGED (use the portal's existing logging convention; if it has none, one `console.warn` per adapted snapshot naming the token and no figure); it is never typed as a class. (4) the plain-fallback-label and colour work of step 2 is DROPPED (no change under `tabs/holdings/`). (5) your new test `ib-174-multi-asset-label.test.ts` has at least TWO arms naming `multi_asset`: the adapter shows a served `multi_asset` as unclassified AND records the log (spy on the logger); the generated wire file carries no `multi_asset`. The criteria are unchanged except AC1, which now also pins `iv-e-148` byte-for-byte (LF-normalised sha256) and requires IVE48 to name the retired set. Your uncommitted regenerated wire file in this worktree is from the old direction: restore it to HEAD first (`git -C portal checkout -- .`), then start from the generator.

**AMENDMENT 1 (issuer, 2026-10-13T06:0xZ; your refusal and row W357-S1 were right and the clause was my defect):** the regeneration also adds `account_id?: string` to the `nodes` block of `contracts/wire/HoldingsSnapshot.ts`, because the contract has carried the OPTIONAL `account_id` member since PRD v0.52 (the wire copy predates it). That change is EXPECTED and GRANTED: the contract is the truth the wire copy follows. The regeneration may therefore differ from HEAD by exactly two things in the generated files: the `multi_asset` member of the `asset_class` union, and the optional `account_id?: string` on the ACCOUNT node. Any OTHER difference in any generated file still means STOP and a row. Run `gen-all.ts` as you did, keep both changes, then do steps 2 to 5. For the typecheck use `bunx tsc --noEmit -p tsconfig.app.json` (your row S2: `-p .` checks nothing). If a portal test that passes at the base fails because the node type gained `account_id`, STOP and name it.

**Cell `IB-pr-506` (inlined):** the v1 contract `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` admits `multi_asset` in its `asset_class` enum again (restored by `7d49d6cc6d`; it is a retired, never-emitted member). The portal's generated wire copy `portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts` was generated while the enum lacked it, so its `asset_class` union lacks `multi_asset`, and the test `portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx` (test `IVE48-AC1`, arm 1: the wire union equals the contract's enum) now FAILS: `wire union [alternatives,cash,commodities,equity,fixed_income,other,structured,unclassified] != contract enum [... multi_asset ...]`. The CTO's ruling: **the wire union and type MOVE to the contract's enum; the test keeps asserting wire == contract (never the producer's six); `multi_asset` gets a plain fallback label.** You work in the PORTAL repo (your worktree's `portal/` directory, `node_modules` linked, `bun` on PATH). This is a portal candidate for the CTO's review lane, DEV only.

**Do:**
1. Regenerate the wire copy from the contract with the portal's own generator (`src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`; the test imports `schemaFilePath` from it; read it to find the command that rewrites `contracts/wire/HoldingsSnapshot.ts`). The expected change in the generated file is the `multi_asset` member of the `asset_class` union; if the regeneration changes anything else in any generated wire file, STOP and file a row (the contract may have moved for another reason).
2. Everything that is keyed or exhaustive over the `asset_class` union must now cover `multi_asset` (the type `HoldingAssetClass` and the colour map `ASSET_CLASS_COLOR` in `src/pages/InvestorReporting/tabs/holdings/assetClass.ts` or `.tsx`, and any label map or `switch` the TypeScript compiler or a test shows is exhaustive). `multi_asset` gets a PLAIN fallback label (a readable string such as `Multi-asset`, and the same neutral colour the file uses for its fallback/other class) and no new feature. Find the places by running `bunx tsc --noEmit -p .` from `portal/` ONCE after step 1 (record its error count before and after; if the typecheck cannot run in this worktree, say so and rely on the tests).
3. Add the worker test `src/pages/InvestorReporting/__tests__/dsgn-irptv1/ib-174-multi-asset-label.test.ts` with at least TWO arms naming `multi_asset`: (a) the label function (or map) the holdings tab uses returns the plain fallback label for `multi_asset`, and it is not the raw code and not empty; (b) `ASSET_CLASS_COLOR` (or the colour lookup) has an entry for `multi_asset`. Do not edit `iv-e-48.new-classes.test.tsx` or any other existing test.
4. Keep each file's EXISTING line endings (compare with `git diff --ignore-cr-at-eol`); do not mass-convert; do not hand-edit a generated file.
5. Commit the portal change per your definition (plain `git -C portal commit`).

**Criteria (run each under `timeout 120` from your WORKSPACE root, the parent of `portal/`, record the output and exit code verbatim):**

<criterion id="IB174-2-AC1" cell_refs="IB-pr-506"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py" . IB174-2-AC1</invocation><expect>IB174-2-AC1 PASS</expect></criterion>
<criterion id="IB174-2-AC2" cell_refs="IB-pr-506"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py" . IB174-2-AC2</invocation><expect>IB174-2-AC2 PASS</expect></criterion>
<criterion id="IB174-2-AC3" cell_refs="IB-pr-506"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py" . IB174-2-AC3</invocation><expect>IB174-2-AC3 PASS</expect></criterion>

<expected_criteria>IB174-2-AC1, IB174-2-AC2, IB174-2-AC3</expected_criteria>

What the checks grade: AC1 `IVE48-AC1` passes (`bun test` of its file); AC2 the whole `src/pages/InvestorReporting` folder reads at least 1214 pass and at most 4 fail (the base reads 1212 pass, 5 fail: the four pre-existing are IVE26-AC3, IVE98, producer fixtures, F14-AC3; AC2 takes about 75 seconds, so run nothing else beside it); AC3 your new test file exists, names `multi_asset`, and passes with at least 2 tests. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and nothing else. Portal repo: only the files named in `<paths>`. No `package.json` or lockfile; run no `bun install`; push nothing.
- **Refusal clause:** STOP, file a row, change nothing more, if the regeneration changes anything other than the `multi_asset` member and the optional `account_id` node member (AMENDMENT 1), if making a type exhaustive needs a file outside the paths (name it), or if a test other than `IVE48-AC1` that passes at the base fails after your change.
- **Commit** in BOTH repos per your definition: the workspace commit (order flip, proof, rows) with `.tools/safe-commit.sh`, and the portal commit with plain `git -C portal commit` (same author and committer values, message file from the Write tool outside the worktree); ASCII only; never stage the workspace's `portal` gitlink.
- **Row ids** are `IRPT_BCKEND-D2-W357-S<k>` (the next free `k`). Report once, under 150 words.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-13/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/ib-174-multi-asset-label.test.ts
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~357/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-506.portal-wire-union-follows-the-contract-enum.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 166 (round 174, workstream ~P), cell `IB-pr-506`.
<owned_cells>IB-pr-506</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB174-2-AC1, IB174-2-AC2, IB174-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~357/IRPT_BCKEND.TO-IB-pr-506.portal-wire-union-follows-the-contract-enum.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a generated wire type and the holdings tab's class map of one portal page; a product-file candidate for portal DEV through the CTO review lane (PROD rides the held promote `dell1-e7f2`); `multi_asset` is a retired, never-emitted member, so no client answer changes. No live DSGN_IRPTV1 order names these paths (the DSGN_IRPTV1 seat is parked on this project's account_id member).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p174_cells.py dry-run at base on dell2 2026-10-13 ~05:5xZ in the shared portal checkout: IB174-2 AC1 FAIL (IVE48-AC1 fails, the contract enum names multi_asset and the wire union lacks it), AC2 FAIL (1212 pass, 5 fail), AC3 FAIL (no test file).
lane: the paths block IS the grant; worker slot ~357 of IRPT_BCKEND, a portal worktree pair. Class LOCAL.
</preflight>
