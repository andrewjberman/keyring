# TO DSGN_IRPTV1.TO-IV-e-1 -- the round-2 REPAIR: Ticker honesty and the hero's L2 members

<to_id>DSGN_IRPTV1.TO-IV-e-1</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~5</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_IRPTV1_PRD.md` v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-1` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-6, FWD-11 | **rows:** C-S12 (ARMED, disarmed by this order's VALID instance), W3-S1 | **depends_on:** -- (chain B head) | **slot:** ~5, queue position 1 of 3 (then IV-e-2, IV-e-6)

---

## WORKER FACE

### THE CELL

`IV-e-1` -- the REPAIR the CTO placed first (ROUND_ANALYSIS.round1.md item 1): FWD-11 is BREACHED today by a derived value, and the hero's L2 is empty.

**(a) Ticker honesty -- `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx`, `tickerFor()` (find the function by its name and print the line; at 895752676a it starts at line 61).** Today it returns `display.symbol` when present, else the TAIL of `securityId` split on `:` or `-` -- on the fixtures that prints '1'..'4', on live data a CUSIP fragment: the FE derived a value the wire never stated and put an identifier fragment on the body (row C-S12). The fix is one branch: `display.symbol` (trimmed) when present, else exactly `NOT_SUPPLIED`; the id is NEVER split, NEVER printed, in whole or in part. The docstring above the function says the new rule. Nothing else in the file changes in THIS order (IV-e-2, your next order, restyles it).

**(b) The hero's L2 -- `portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx`, inside the ONE function `mdpfResultFromSnapshot` (from `export function mdpfResultFromSnapshot` to the line before `function Breadcrumbs`; base lines re-measured at `895752676a45e83dc252d4253aebc5fa316a229e` and printed by IV-e-1-AC3).** Today each L0 category's `children[label]` carries `{ aum }` only; `CategoryViewTree`'s L2 hover detail and "View breakdown" read `children[label].members`, which is never populated (row W3-S1). Fill it: for each direct child of a category, `children[label].members` = the leaf `security` nodes beneath THAT child (any depth), each `{ member_id: nodeRef, display_name: display.label else displayName, served: true, strategy_id: null, aum: the node's own amount }` -- the same shape `leafSecurityMembers` already builds for the category's top-level `members`, applied one level down. Reuse that nested helper; sum nothing; keep the top-level `members` fill. `CategoryViewTree.tsx` is read, never edited.

**Fixtures (adapted shape; discover the `fe-s-7/holdings.*.json` set from disk as round 1 did -- the naming gate refuses a firm token in a new file's text, CTO batch 36):** `portal/src/pages/InvestorReporting/fixtures/fe-s-7/`, `fixtures/holdingsSnapshot.success.json`. Reference: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/anna.holdings-nodes.dec293d6.json` (68 of 68 served securities carry `display.symbol`).

### ACCEPTANCE

<criterion id="IVE1-AC1" cell_refs="IV-e-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-1.ticker-honesty.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: TICKER-HONEST</expect></criterion>
`IVE1-AC1` -- the Ticker rule as a DIFFERENCE CONTROL with both arms in one file, over `securityRowsFrom` and the rendered table: (NEGATIVE arm) every fixture's security leaves with `display` absent -> every `ticker` is exactly "not supplied" and NO ticker cell text is a substring of that node's `securityId` (print `ABSENT-SYMBOL: n of n rows not supplied, 0 id fragments`); (POSITIVE control) the same fixture with `display = {label: 'X', symbol: 'PLNT'}` planted on one leaf in the test -> that row's ticker is exactly `PLNT` and appears in the rendered `data-slot="security-ticker"` cell (print `PLANTED: PLNT printed`). `VERDICT: TICKER-HONEST` only when both arms hold. **At issuance the negative arm reads FAIL ('1'..'4' printed) -- the criterion detects the defect.**

<criterion id="IVE1-AC2" cell_refs="IV-e-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-1.l2-members.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: L2-FED</expect></criterion>
`IVE1-AC2` -- the L2 fill: over each fixture, for every L0 category and every direct child of it that has leaf securities beneath, `children[label].members` is non-empty and equals (as a set of `member_id`) the test's own independent walk of leaf securities beneath that child; each member's `aum` equals the node's own `amount` and its `display_name` follows display.label-else-displayName; the top-level `members` fill of round 1 is unchanged (the round-1 suite `iv-t-3.hero-fed.test.ts` still passes -- run it in this file's `afterAll` or assert its VERDICT line). Print `L2: <c> children checked, <m> members, display-named <d> of <m>` per fixture; `VERDICT: L2-FED` only when every checked child is fed. **At issuance this reads 0 members on every child.**

<criterion id="IVE1-AC3" cell_refs="IV-e-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 python -c "import subprocess,re;b='895752676a45e83dc252d4253aebc5fa316a229e';src=subprocess.run(['git','show',b+':src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx'],capture_output=True,text=True).stdout.splitlines();s=next(i+1 for i,l in enumerate(src) if 'export function mdpfResultFromSnapshot' in l);e=next(i for i,l in enumerate(src) if l.startswith('function Breadcrumbs'));d=subprocess.run(['git','diff','-U0',b,'--','src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx'],capture_output=True,text=True).stdout;h=[int(m.group(1)) for m in re.finditer(r'^@@ -(\d+)',d,re.M)];n=subprocess.run(['git','diff','--numstat',b,'--','src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx'],capture_output=True,text=True).stdout.strip();print('SPAN',s,e,'HUNKS',h,'SECURITYLIST-NUMSTAT',n.split()[:2]);ok=len(h)>0 and all(s<=x<=e for x in h);print('VERDICT:','ONE-FUNCTION' if ok else 'TOUCH-OUTSIDE-FUNCTION')"</invocation><expect>VERDICT: ONE-FUNCTION</expect></criterion>
`IVE1-AC3` -- the ruled touch (CTO 100332 span, re-measured at the base): every `DrillTree.tsx` hunk against `895752676a45e83dc252d4253aebc5fa316a229e` starts inside `mdpfResultFromSnapshot`'s span (the span's base lines print), and `SecurityList.tsx`'s numstat prints beside it for the record (its bound is IV-e-2's, not this order's).

<criterion id="IVE1-AC4" cell_refs="IV-e-1" judgment="true"/>
`IVE1-AC4` -- graded at L9 by `3.0.0_SA_CVO` from your static markup of `SecurityList` over the Cottonwood fixture with one planted symbol (`iv-e-1.security-list.html`) and of `DrillTree` (`iv-e-1.hero.html`): the Ticker column reads "not supplied" everywhere the wire carries no symbol and the planted symbol where it does; no id fragment on the body; the L2 lists securities under each sleeve. RECORD; NO VERDICT.

<expected_criteria>IVE1-AC1, IVE1-AC2, IVE1-AC3, IVE1-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/<your serial>/` and this order's own file. Nothing else. `components/CategoryViewTree.tsx`, `tabs/holdings/HoldingsTab.tsx`, `SliceTable.tsx`, `slices.ts`, `contracts/**`, `api/**` are OUT. A path you need that is not named is a BLOCKING surprise row -- never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (identity line); `<WS>/portal` its portal worktree based on `895752676a45e83dc252d4253aebc5fa316a229e`. `portal/` entries commit in the portal repo (cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`); workspace records in `<WS>`. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean`.
- **Toolchain.** `node_modules` is a junction; never `bun install`; bun is `/c/Users/AndrewBerman/.bun/bin/bun`; tests `bun test <file>`. Typecheck is the COO's drain check.
- **The rules (PRD v0.5 CONTRACTS):** the FE derives nothing; "not supplied", never zero, never a derived fragment; every amount is the node's own.
- **Numbers.** No number here is an acceptance value except where a criterion prints one; `PLNT` is a test plant.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is REFUSED and reported with your measurement -- never repaired, widened, or satisfied by a route this order did not name.
- **Your queue.** IV-e-2 then IV-e-6 follow in this pair; the COO hands each by continuing this conversation.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-1`.
<owned_cells>IV-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE1-AC1` .. `IVE1-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~5/DSGN_IRPTV1.TO-IV-e-1.repair-ticker-and-l2.proof_of_spec.json` (phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with `python .tools/proof-of-spec-check.py <instance> IVE1-AC1,IVE1-AC2,IVE1-AC3,IVE1-AC4` BEFORE the `complete` flip. `IVE1-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `repair-ticker-and-l2.result.md` beside it. Flip `complete` only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row in the investigation file above (it exists at HEAD with 8 rows; append inside the fenced array; id `DSGN_IRPTV1-W5-S<k>`, your slot's own sequence starting at 1).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register (6 entries: the trace, hop 6's Performance path, IV-e-6's fee-basis parameter, the Analysis half of the sweep, the naming gate's JS/TS escape, comp-adversary's flagged path); none owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands (0 of 11 AWS-surface tokens over the PRD at HEAD); no cell writes an AWS surface.
comp-adversary: RUN at L5 v2 on the PRD: 9 of 9 cited commits verified; 6 paths, 5 stable, 1 flagged (read at the cut); T11 blindness stated by the tool.
lane: the <paths> block IS the grant (RULING 1). DrillTree.tsx admitted for the ONE function span (CTO 100332, re-measured at 895752676a45e83dc252d4253aebc5fa316a229e by IVE1-AC3); SecurityList.tsx is this project's round-1 file.
</preflight>

Seating: slot ~5, queue position 1 (IV-e-2 position 2, IV-e-6 position 3); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 5` off workspace `HEAD` and portal `895752676a45e83dc252d4253aebc5fa316a229e`.
