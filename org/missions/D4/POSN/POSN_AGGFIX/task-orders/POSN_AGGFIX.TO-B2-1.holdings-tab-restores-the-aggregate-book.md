# TO POSN_AGGFIX.TO-B2-1 -- THE HOLDINGS TAB RESTORES THE AGGREGATE BOOK FOR OPAL VIEWERS: Aggregate first in the Models selector, both panels on the aggregate, the five per-model columns back in the layout the removal took out and legible on today's canvas, and the landing on the aggregate unless another book is remembered -- proved by page renders as Opal staff, an advisor and a client (AF1-s-14; FWD-1, FWD-3, FWD-9, FWD-2)

<to_id>POSN_AGGFIX.TO-B2-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-PRIOR-LAYOUT, C-DEFAULT-UNLESS-REMEMBERED, C-EXISTING-PREDICATE, C-FIVE-BOOKS-UNCHANGED, C-PORTAL-PROMOTE) - **Decomp
cell:** `AF1-s-14` - **Issuance:** round 1, slot `~3`, SECOND in this slot's queue. **Handed to you only after TO-B1-1 drained.** COMMIT
YES, PROMOTE NO.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~3;`. Workspace worktree
`/c/tmp/wk-aggfix-1-3` (branch `wk-posn_aggfix-1-3`); portal worktree `/c/tmp/wk-aggfix-1-3/portal` on YOUR branch `wk-aggfix-1-3-portal`,
continuing from TO-B1-1's commits (verify `git -C /c/tmp/wk-aggfix-1-3/portal merge-base --is-ancestor edf85ce503 HEAD`). First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; bring SITEZ into the workspace branch if it is not an
ancestor (`git merge-base --is-ancestor SITEZ HEAD || git merge --no-edit SITEZ`). Workspace commits via `bash .tools/safe-commit.sh
--author "0.9.0_WK_POSN_AGGFIX~3 <0.9.0_WK_POSN_AGGFIX~3@opal.agent>" -F <msgfile> -- <paths>`; portal commits via
`git -C /c/tmp/wk-aggfix-1-3/portal commit --author "0.9.0_WK_POSN_AGGFIX~3 <0.9.0_WK_POSN_AGGFIX~3@opal.agent>" -F <msgfile> -- <paths>`
(msgfiles by the Write tool, PURE ASCII). Never push, merge in the portal, rebase, `checkout --`, `clean`; never `git add portal`. Append
PORTAL_REFS at your first portal commit of this order. Every portal bar is anchored on `edf85ce503`. Scratch in
`/c/tmp/wk-aggfix-1-3/.scratch/` only.

## THE CELL (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-14` -- the selector entry, both panels, the per-model columns and the landing (S14, C-PRIOR-LAYOUT, C-DEFAULT-UNLESS-REMEMBERED).**
`portal/src/pages/Positioning/tabs/HoldingsTab.tsx`: for an internal viewer with the merged block present, `Aggregate` is the FIRST book in
the Models-mode selector (the removed `AGG_PORTFOLIO` shape, `d53049a0`); Portfolio Composition (:1105) and Holdings Breakdown (:1197) render
`current_holdings.AGG` through the existing path; the Model Breakdown group (UST, ST, INT, LT, ULT from `model_breakdown`) returns in the
position and order the removal took out, labelled as all of Opal, re-authored in today's light-canvas tokens (no `text-white`,
`text-orange-300`, `bg-white/10`, `bg-orange-500/5`); the first-render landing (:841) lands an internal viewer with no remembered choice on
the aggregate, and a remembered choice wins. Advisor and client see no change.

**The prior layout, MEASURED by the issuer from `git -C <portal> show d53049a0 -- src/pages/Positioning/tabs/HoldingsTab.tsx` -- read it
whole, never trust this summary:** `const AGG_PORTFOLIO = { id: 'AGG', name: 'Aggregate', color: PALETTE.opalIndigo }` (removed at diff line
98) prepended to the named books (:161 `return aggregate ? [AGG_PORTFOLIO, ...named] : named`); the default `useState(caps.aggregate ? 'AGG'
: '')` (:178) and the landing `if (caps.aggregate) return 'AGG'` (:286); the Model Breakdown header group rendered only when
`selectedPortfolio === 'AGG'`, placed FIRST among the column groups (":505 Model Breakdown - Orange (only for AGG) - NOW FIRST"), its cells
`holding.model_breakdown?.<CODE> ? (holding.model_breakdown.<CODE> * 100).toFixed(1) : '-'` for UST, ST, INT, LT, ULT (:537-557); the
client-side `aggregateWeighting` and the `/api/general/portfolios/aum-metrics.json` fetch (:101-123, :196-232) were DEAD code and are NOT
restored. **The canvas law:** `portal/CLAUDE.md` and `DESIGN.md` C3/C5 -- the canvas is light; ink on white panels; the removed
orange-on-dark classes render near-invisible today.

**Your inputs from TO-B1-1 (at your branch):** the merge helper and the viewer-scoped book set in `shared/bookSet.ts`; the page-level fetch and merge in `Positioning.tsx`
(NOT the hand-over to the `HoldingsTab` mount -- row W3-S1; this order lands it); `B_DOM_BEFORE.json` in `deliverables/0.9.0_WK_POSN_AGGFIX~3/`; the render harness `<FIVE_BOOKS_DOM_B>`, the unit
runner and the typecheck runner.

**AMENDED BEFORE HAND-OFF (issuer, ~20:3xZ, on row `POSN_AGGFIX-Z-W3-S1`):** TO-B1-1 measured that the hand-over to the tab could not land
in its grant. In Models mode `HoldingsTab` renders its OWN `getPositioningData()` result (`HoldingsTab.tsx:727-737` @`edf85ce503`), not the
page's object, so the page-level merge reaches only `PositioningSummary`; and passing `internal` at the mount fails the typecheck (TS2322)
until `HoldingsTab` declares the prop. **This order now owns both halves of that hand-over, in ONE commit that typechecks:** `Positioning.tsx`
passes `internal` and the Opal-only payload the page already fetched to the `HoldingsTab` mount (`:642`), and `HoldingsTab` declares both
props and merges the aggregate into its own Models-mode data through TO-B1-1's pure helper. **No second request for the Opal-only file**
(B2-AC11). `Positioning.tsx` is added to `<paths>` for exactly that mount change.

## YOUR ACT

1. `HoldingsTab.tsx` and the `HoldingsTab` mount in `Positioning.tsx` (the two props, nothing else in that file): the Aggregate entry first for an internal viewer whose resolved book set holds it; both panels on the aggregate
   through the existing `current_holdings[selectedPortfolio]` path; the Model Breakdown group restored in the prior position and order with
   an "All of Opal" label, in current tokens; the landing on the aggregate for an internal viewer with no remembered choice. Nothing else.
2. `<AGG_DOM_B2>`: extend the render harness with the aggregate fixture (the 1.1 payload, status OK) and an UNAVAILABLE fixture; screenshots
   saved as PNGs in your deliverables.
3. Commit, append PORTAL_REFS, record every criterion.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W3-S<k>` continuing your sequence, in
`org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="B2-AC1" cell_refs="AF1-s-14"><invocation>timeout 120 python <PRIOR_LAYOUT_MAP_B2></invocation><expect>each element d53049a0 removed from HoldingsTab.tsx (the AGG_PORTFOLIO entry, the prepend, the default and the landing, the Model Breakdown header group and its five cells) printed beside its restored counterpart at your HEAD with line numbers, `RESTORED <n> of <n>` for the elements that are not dead code, and the forbidden classes text-white, text-orange-300, bg-white/10, bg-orange-500/5 counted in the restored hunks as 0.</expect></criterion> `B2-AC1` -- THE PRIOR LAYOUT, ELEMENT BY ELEMENT.

<criterion id="B2-AC2" cell_refs="AF1-s-14"><invocation>timeout 900 node <AGG_DOM_B2> --viewer opal-staff --remembered none</invocation><expect>the page lands on Aggregate (the selected book label printed); the selector's FIRST entry reads Aggregate; the Portfolio Composition entries and the Holdings Breakdown rows each count equal to the fixture's AGG holdings; the Model Breakdown group shows five columns UST ST INT LT ULT placed first among the column groups, with the cell text for three sampled tickers equal to model_breakdown x 100 at one decimal (or '-'); an "All of Opal" label present; a screenshot saved.</expect></criterion> `B2-AC2` -- OPAL STAFF, FRESH, LANDS ON THE AGGREGATE.

<criterion id="B2-AC3" cell_refs="AF1-s-14"><invocation>timeout 900 node <AGG_DOM_B2> --viewer opal-staff --remembered ST</invocation><expect>the page lands on ST (the selected label printed); selecting Aggregate then renders both panels on the aggregate (row count printed equal to the fixture's).</expect></criterion> `B2-AC3` -- A REMEMBERED CHOICE WINS.

<criterion id="B2-AC4" cell_refs="AF1-s-14"><invocation>timeout 900 node <AGG_DOM_B2> --viewer advisor-and-client --remembered AGG</invocation><expect>for an advisor and for a client, each with 'AGG' hand-set as the remembered book before load: no Aggregate entry in the selector (entries printed), the landing on the ordinary default model (printed), 0 requests to opal_aggregate.json, and no Model Breakdown group in the DOM.</expect></criterion> `B2-AC4` -- NOBODY OUTSIDE OPAL FINDS IT, EVEN REMEMBERED.

<criterion id="B2-AC5" cell_refs="AF1-s-14"><invocation>timeout 900 node <FIVE_BOOKS_DOM_B> --compare-before org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/B_DOM_BEFORE.json</invocation><expect>on your HEAD with the same fixtures, the 10 advisor and client captures IDENTICAL to B_DOM_BEFORE.json (`IDENTICAL 10 of 10`), and the mutated-weight control reported as a difference.</expect></criterion> `B2-AC5` -- WHAT ADVISORS AND CLIENTS SEE HAS STILL NOT MOVED.

<criterion id="B2-AC6" cell_refs="AF1-s-14"><invocation>timeout 900 node <AGG_DOM_B2> --viewer opal-staff --legibility</invocation><expect>for the five Model Breakdown header cells and one body cell per column: the computed text colour and the computed background of its nearest opaque ancestor printed with their WCAG contrast ratio, every ratio at least 4.5; the same measurement on one existing column beside them printed as the reference.</expect></criterion> `B2-AC6` -- AS EASY TO READ AS THE COLUMNS BESIDE IT, MEASURED.

<criterion id="B2-AC7" cell_refs="AF1-s-14"><invocation>timeout 900 node <AGG_DOM_B2> --viewer opal-staff --aggregate-fixture unavailable</invocation><expect>with the UNAVAILABLE payload: no Aggregate entry, the landing on the ordinary default model, no Model Breakdown group, no page error.</expect></criterion> `B2-AC7` -- AN UNAVAILABLE AGGREGATE IS NEVER OFFERED.

<criterion id="B2-AC8" cell_refs="AF1-s-14"><invocation>timeout 900 bash <TYPECHECK_RUN_B></invocation><expect>the portal's typecheck at your HEAD exits 0 with 0 errors, and the deliberate-error scratch copy exits non-zero.</expect></criterion> `B2-AC8` -- THE TYPECHECK, SHOWN ABLE TO FAIL.

<criterion id="B2-AC9" cell_refs="AF1-s-14"><invocation>timeout 60 git -C /c/tmp/wk-aggfix-1-3/portal diff --stat edf85ce503 HEAD -- src</invocation><expect>exactly four files: src/api/portal-proxy.ts, src/pages/Positioning/Positioning.tsx, src/pages/Positioning/shared/bookSet.ts (TO-B1-1) and src/pages/Positioning/tabs/HoldingsTab.tsx (this order); README.md under src/pages/Positioning is a permitted fifth.</expect></criterion> `B2-AC9` -- THE PORTAL WRITE SURFACE, WHOLE.

<criterion id="B2-AC11" cell_refs="AF1-s-14"><invocation>timeout 900 node <FIVE_BOOKS_DOM_B> --network-arms</invocation><expect>at your HEAD, the page opened in Models mode as Opal staff, as an advisor and as a client with every request URL recorded: requests to opal_aggregate.json per page load -- Opal staff exactly 1, advisor 0, client 0; and in ETFs mode 0, 0, 0 (the same table TO-B1-1's B1-AC5 printed, unchanged by the hand-over).</expect></criterion> `B2-AC11` -- THE HAND-OVER ADDS NO SECOND REQUEST.

<criterion id="B2-AC10" cell_refs="AF1-s-14" judgment="true"/> `B2-AC10` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** whether the restored selector entry and Model Breakdown group read as "how it was before" (Andrew c) on today's canvas, judged from the screenshots beside the removal diff, and whether the "All of Opal" label keeps an Opal user from reading the aggregate as an advisor's own book. Record the readings and offer NO verdict.

<expected_criteria>B2-AC1, B2-AC2, B2-AC3, B2-AC4, B2-AC5, B2-AC6, B2-AC7, B2-AC8, B2-AC9, B2-AC10, B2-AC11</expected_criteria>

<placeholders>PRIOR_LAYOUT_MAP_B2, AGG_DOM_B2, FIVE_BOOKS_DOM_B, TYPECHECK_RUN_B</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-B2-1.holdings-tab-restores-the-aggregate-book.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_AGGFIX/ledger/PORTAL_REFS.md
portal/src/pages/Positioning/tabs/HoldingsTab.tsx
portal/src/pages/Positioning/Positioning.tsx
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-14</owned_cells>
Read-dependencies, NOT claimed: `AF1-s-13`, `AF1-s-15` (TO-B1-1's helpers and mount), `AF1-s-3` (the predicate). DOWNSTREAM: `AF1-s-16`
(TO-B3-1) renders your HEAD on live bytes.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; no deploy, promote or push in this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or cloud write.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the tokens that replace the removed classes are not chosen by the issuer; B2-AC6 measures legibility rather than naming a token; (2) the first-render landing block at :841 was re-shaped after the removal (its comment says so), so restoring the old landing line verbatim is not assumed to work; (3) whether the Composition treemap handles 30 holdings without layout changes is unread.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/POSN_AGGFIX.TO-B2-1.holdings-tab-restores-the-aggregate-book.proof_of_spec.json
</proof_of_spec>
