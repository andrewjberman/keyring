# TO DSGN_IRPTV1.TO-IV-t-3 -- the Holdings L0 hero, fed

<to_id>DSGN_IRPTV1.TO-IV-t-3</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~3</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>1</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_IRPTV1_PRD.md` v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-t-3` | **outcome_ref:** FWD-1 (hop 7), FWD-6, FWD-10 | **depends_on:** -- (chain C head) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`IV-t-3` -- the HOLDINGS L0 HERO, FED (PRD candidate C3). ONE function changes: `mdpfResultFromSnapshot(snapshot)` in `portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx`, lines 140-171 at portal `7c542fd23ec70c88bade4e3270f4c87f267a275a` (from `function mdpfResultFromSnapshot` to the line before `function Breadcrumbs`). The file is `2.0.0_SA_COO~M`'s to its labels pin and every OTHER line of it stays exactly as it is.

Today every top-level category becomes `{ aum, members: [], children: {} }` (line 151), so `CategoryViewTree`'s hover detail and "View breakdown" dialog are empty on this page while they are the hero on Model Portfolios. Fill them from the snapshot: for each L0 category node (the Models / SMAs / Client labels the producer carries; the label logic `displayLabelFor` stays as is), `children` = the nodes directly beneath it per the ruled tree (CTO 100332: strategy > constituent models + SMA + Client plug), each keyed by its label (`display.label` when present, else `displayName`) with `aum` = that node's own `amount`; and `members` = the leaf holdings beneath the category (kind `security`), each named from `display.label` when present else `displayName`, with its `amount`. The types are `MdpfCategoryNode` / `MdpfCategoryChildNode` / `MdpfCategoryMember` in `portal/src/api/endpoints/aum.ts:760-` (read them; fill only the fields the types require and leave optional ones out rather than inventing values). You SUM NOTHING: a category's `aum` stays the category node's own `amount`, exactly as today; unknown / null amounts stay null. `CategoryViewTree.tsx` is read, never edited (a change it would need is a BLOCKING row naming every other page that renders it). Add `export` to the function so your test can call it directly -- that keyword is inside the one function's span.

**Fixtures (adapted shape):** `portal/src/pages/InvestorReporting/fixtures/fe-s-7/holdings.cottonwood-target-blend.json`, `fixtures/fe-s-7/holdings.smartx-observed.json`, `fixtures/holdingsSnapshot.success.json`. Anna's real served node subtree (pre-adapter wire, a NAME reference only): `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/anna.holdings-nodes.dec293d6.json`.

### ACCEPTANCE

<criterion id="IV3-AC1" cell_refs="IV-t-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~3; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-3.hero-fed.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: HERO-FED</expect></criterion>
`IV3-AC1` -- the built behaviour: over each named fixture the result's `status` is `ok`; for every L0 category that has descendant nodes in the snapshot, its `children` is non-empty and its `members` lists the leaf holdings beneath it; every child's `aum` equals the corresponding node's `amount` (no sum); a member is named from `display.label` where the node carries `display`. Print `L0: <n> categories, <m> with children, <k> members; display-named: <d> of <k>` per fixture and `VERDICT: HERO-FED` only when every category with descendants is fed. **At issuance this reads 0 with children on every fixture -- the criterion detects the defect rather than confirming it.**

<criterion id="IV3-AC2" cell_refs="IV-t-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~3; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7/ 2>&1 | tail -8</invocation><expect> 0 fail</expect></criterion>
`IV3-AC2` -- the seam with the adapter's existing consumers, AMENDED by the issuer (the cut's own pathspec defect, found by the worker's refusal): the invocation now names the directory `__tests__/fe-s-7/` with its trailing slash -- the bare prefix `fe-s-7` also swept `fe-s-71`..`fe-s-78`, and `fe-s-78/cohort-chip.test.ts` fails at the base 7c542fd2 untouched by this cell (3 of 56, reproduced by the issuer on an independent worktree). The fe-s-7 Holdings suite (drill, slices, source bounds) still passes at your branch tip -- the fill must not move the L0 cards, the drill or the signed table. The runner's own summary line (`N pass / 0 fail`) is the output; denominator = its pass count. Re-run in place; the earlier FAIL row on the bare prefix stands as an honest measurement superseded by this re-run. (Stated as the seam arm because the real neighbour, the deployed holdings function, needs a login a worker does not hold; the live seam is the COO's drain trace.)

<criterion id="IV3-AC3" cell_refs="IV-t-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~3; timeout 120 python -c "import subprocess,re;d=subprocess.run(['git','diff','-U0','7c542fd23ec70c88bade4e3270f4c87f267a275a','--','src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx'],capture_output=True,text=True).stdout;hunks=[int(m.group(1)) for m in re.finditer(r'^@@ -(\d+)',d,re.M)];print('HUNKS at base lines:',hunks);ok=len(hunks)>0 and all(140<=h<=171 for h in hunks);print('VERDICT:','ONE-FUNCTION' if ok else 'TOUCH-OUTSIDE-FUNCTION')"</invocation><expect>VERDICT: ONE-FUNCTION</expect></criterion>
`IV3-AC3` -- the ruled touch (CTO 100332): every diff hunk against `7c542fd23ec70c88bade4e3270f4c87f267a275a` in `DrillTree.tsx` starts inside the `mdpfResultFromSnapshot` span (base lines 140-171). Hunk base lines printed beside the verdict. A helper you need lives INSIDE the function (a nested function), not beside it.

<criterion id="IV3-AC4" cell_refs="IV-t-3" judgment="true"/>
`IV3-AC4` -- graded at L9 by `3.0.0_SA_CVO` from your static markup of `DrillTree` over the Cottonwood fixture (`iv-t-3.hero.html` in your deliverables) and a PNG if `node scripts/ui-smoke.mjs investor-reporting <deliverables>/iv-t-3.png --port <PORT> --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json` runs for you: the hero reads as the Model Portfolios hero (pie, nested tiles, hover detail, breakdown) with the Models / SMAs / Client labels. RECORD; NO VERDICT.

<expected_criteria>IV3-AC1, IV3-AC2, IV3-AC3, IV3-AC4</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override. `components/CategoryViewTree.tsx`, `tabs/holdings/HoldingsTab.tsx` (IV-t-4's, your NEXT order), `slices.ts`, `SliceTable.tsx`, `HoldingsSummary.tsx`, `contracts/**`, `api/**` are OUT of this order's grant.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo, based on `7c542fd23ec70c88bade4e3270f4c87f267a275a` on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Toolchain.** `node_modules` is a junction; **do not run `bun install`**. bun is `/c/Users/AndrewBerman/.bun/bin/bun`. Tests: `bun test <file-or-dir>`. Typecheck is the COO's drain check, not yours.
- **The rules every cell obeys (PRD v0.5 CONTRACTS):** the FE derives nothing -- no sums, no percentages you compute; every amount is the node's own; the L0 taxonomy is the contract's (M's projection) and you re-attribute nothing.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is REFUSED and reported with your measurement -- never repaired, widened, or satisfied by a route this order did not name.
- **Your queue.** `DSGN_IRPTV1.TO-IV-t-4` follows in this same worktree pair once this order is terminal; the COO hands it to you by continuing this conversation.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v1 @1f24052b87, cell `IV-t-3`.
<owned_cells>IV-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IV3-AC1` .. `IV3-AC4`. Instance at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/DSGN_IRPTV1.TO-IV-t-3.holdings-hero.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> IV3-AC1,IV3-AC2,IV3-AC3,IV3-AC4` BEFORE the `complete` flip. `IV3-AC4` is recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO` -- a `PASS` or `FAIL` on a judgment row is INVALID. Result file `holdings-hero.result.md` beside it. Flip `complete` only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row in the investigation file above -- that file does NOT exist yet (the row gate refuses an empty channel file, so it is minted by its FIRST row): if it is absent when you need it, create it with the header line `# DSGN_IRPTV1 -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (.tools/surprise-row-gate.py validates every NEW row).` followed by a fenced ```json array holding your row as its first item (the DSGN_REBRND W1-S1 precedent); a sibling slot may create the same file in its own worktree and the COO reconciles by UNION of rows at the drain (id `DSGN_IRPTV1-W3-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at L5 (thread round; the lens runs on the enrichment round that touches its surface). The round's gates are sequencing inputs in the decomposition section 8; none is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: a word-boundary AWS-surface token sweep over the PRD at HEAD (v0.5, 26,070 bytes) returned 0 of 11 tokens; no cell writes an AWS surface.
comp-adversary: DECLARED-NOT-APPLICABLE at L5 (thread round); runs on the enrichment round against the PRD and these orders.
lane: the <paths> block IS the grant (RULING 1). Portal entries resolve to <WS>/portal/<rest> and commit in the portal repo. DrillTree.tsx is granted for the ONE function span 140-171 at 7c542fd23ec70c88bade4e3270f4c87f267a275a (CTO 100332); IV3-AC3 grades the bound.
</preflight>

Seating: slot ~3, queue position 1 (IV-t-4 is queue position 2 on this slot); fresh worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 3` off workspace `HEAD` and portal `7c542fd23ec70c88bade4e3270f4c87f267a275a` (e5dd8487 is-ancestor rc=0 at the cut -- this cell's base MUST carry M's labels pin).
