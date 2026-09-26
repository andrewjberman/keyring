# TO DSGN_IRPTV1.TO-IV-e-33 -- FWD-19 R1: the client is the page unit -- one selection, one shared snapshot, one account list; "Client" everywhere; clear empties the card

<to_id>DSGN_IRPTV1.TO-IV-e-33</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~22</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>6</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.11 @e13fed2413 | **Decomp cell:** `IV-e-33` (decomp v6) | **outcome_ref:** FWD-19, FWD-1, FWD-2 | **depends_on:** -- (chain 1, position 1) | **slot:** ~22, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-33` -- C25 part 1 (PRD v0.12 @0953f5b5d9, ENRICHMENT BACKLOG item 23, CELL CANDIDATE C25): routes R0 and R1 and rules C1, C2 and
"one account list" (proposal sections 2-5).

**Build:**
(a) **R1 holds the client.** A pick sets R1 (the client entry, its `clientSetId`, the ONE shared `GET /holdings/{clientSetId}` snapshot, and
`accountList` = the snapshot's level-0 ACCOUNT nodes `{accountId via drill_refs, label = display.label, value}`). `POST /selections` is sent
ONCE with the ENTRY'S OWN `permitted_scope` (unchanged from today). R1 is cleared only by a clear or a firm switch; no tab control changes it.
(b) **One account list.** `accountList` feeds the identity card's "over what", and is published (through `header/HeaderSelectionContext.ts`)
for the Holdings filter, the Performance chooser and Analysis's included accounts. `IdentityCard.fetchIdentityCardData`'s directory
account-name search is REMOVED; the card's snapshot fetch becomes R1's one shared fetch (`index.tsx:145-188` `select` sets R1 only;
`selectedScopeRef` splits into the client ref and each tab's account ref -- export the tab-account ref type for IV-e-34).
(c) **C1, "Client".** Every search option, the browse drawer row and the identity card say "Client" (`IdentityCard.tsx:145-156`,
`BrowseDrawer.tsx:272`, `ScopeSummary.tsx:81-82`); the entry's scope kind is carried, never shown.
(d) **Clear.** Clearing the client clears the card in the SAME render (no previous client's value beside "No client selected").
IV-e-34 (next on this slot) builds the tab-local account focus on (b); this cell leaves Performance and Holdings consuming the client ref
as today.

**The spec is the CRO's route proposal, AT ITS PIN:** read it with `git -C <WS> show 713a49f7b8:org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_ROUTE_STRUCTURE_PROPOSAL_20260926.md` (the working copy has moved since; the PRD adopts the pinned text). Sections 2 (the routes R0-R4), 3 (each route's exact calls), 4 (the six rules, each a test) and 5 (the code each retires) are binding; the PRD's ROUTE STRUCTURE section (`org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md`) carries the CTO's rulings: Call 1 (b) the client's LARGEST account by the snapshot's value is preselected on Performance (the first in snapshot order on a tie) with the chooser always visible; Call 2 (a) route state only, in-page -- no client or account id ever goes into the URL.

**Rulings since the PRD (binding):** each level-0 ACCOUNT node's `display.label` carries that account's own masked tail and type (e.g. "****4304 / IRA"; 2.0.0_SA_COO~M serves it) -- the page READS the label and never derives a mask from an id (CTO 101303); accounts are keyed by the snapshot's account id (via `drill_refs`), NEVER by label (CTO 101340; `tabs/holdings/DrillTree.tsx:312-333` keys category children by label today -- do not copy that); EVERY account-list surface -- the identity card's "over what", the Holdings filter, the Performance chooser, Analysis's included accounts -- shows each account's label AND its value, keyed by account id (proposal rule 4 at @713a49f7b8; PRD v0.12, CTO 101447).

**The rules:** the FE derives nothing; ids never print (not in the body, not in the URL); "not supplied", never zero; a refusal reads in advisor words with its code one click away; colour is keyed by served code or class.

**Environment:** the portal worktree is based on DEV `1e02be40` (= origin DEV = PROD 36a37afc plus site-Z work outside InvestorReporting). Each criterion's test file does not exist at the base: write it from the criterion's text against fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-21.*` and `iv-e-26.*`); it prints the VERDICT only when every arm holds. Do not start any server (dev builds run on port 5174 only, serving the main checkout). The live walk on DEV is the issuer's, after the drain.

### ACCEPTANCE

<criterion id="IVE33-AC1" cell_refs="IV-e-33"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-22/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~22; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-33.client-context.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: CLIENT-CONTEXT-OK</expect></criterion>
`IVE33-AC1` -- with a stubbed api and a multi-account client fixture, picking the client issues exactly ONE POST /selections carrying the entry's own scope and exactly ONE GET /holdings/{clientSetId}; the published account list equals the snapshot's level-0 ACCOUNT nodes, keyed by their drill_refs account id (two accounts sharing a label stay two entries), each carrying its display.label and value; zero directory account-name search calls are made. It prints `VERDICT: CLIENT-CONTEXT-OK` only when every arm holds.

<criterion id="IVE33-AC2" cell_refs="IV-e-33"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-22/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~22; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-33.client-words.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: CLIENT-WORDS-OK</expect></criterion>
`IVE33-AC2` -- rendered search options, the browse drawer row and the identity card use the kind word "Client" and never "Relationship" or "Account" as the kind; clearing the client empties the identity card in the same render (no dollar value beside "No client selected"); no client or account id appears in the markup or in `window.location`. It prints `VERDICT: CLIENT-WORDS-OK` only when every arm holds.

<criterion id="IVE33-AC3" cell_refs="IV-e-33" judgment="true"/>
`IVE33-AC3` -- graded by `2.0.0_SA_COO~D` on the live walk on portal DEV (the C25 walk): an advisor searches by client, sees the client's accounts listed by name and masked tail with their values, and clearing empties the card (FWD-19, FWD-2 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE33-AC1, IVE33-AC2, IVE33-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `api/**` and every other page
  are OUT; `src/lib/**` is read, never edited. The backend and its one-account rule (`performance/retained.py:77-80`) are taken as they are.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/header/ScopeSummary.tsx
portal/src/pages/InvestorReporting/header/HeaderSelectionContext.ts
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/search.ts
portal/src/pages/InvestorReporting/header/selectionRequest.ts
portal/src/pages/InvestorReporting/state/selection.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v6, cell `IV-e-33`.
<owned_cells>IV-e-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE33-AC1, IVE33-AC2, IVE33-AC3. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~22/DSGN_IRPTV1.TO-IV-e-33.client-context-r1.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE33-AC1,IVE33-AC2,IVE33-AC3` BEFORE the flip. `IVE33-AC3` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s live walk on portal DEV.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W22-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v6 -- the write paths are the proposal's section 5 at its pin 713a49f7b8, measured at portal DEV 1e02be40 (IdentityCard.fetchIdentityCardData :118, narrowToOneAccount :234).
lane: the <paths> block IS the grant; one chain, IV-e-34 consumes IV-e-33's account list on the same worktree.
</preflight>

Seating: slot ~22, queue position 1 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 22 --portal-ref 1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`.
