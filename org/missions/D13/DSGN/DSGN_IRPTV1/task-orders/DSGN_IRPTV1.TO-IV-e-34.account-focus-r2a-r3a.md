# TO DSGN_IRPTV1.TO-IV-e-34 -- FWD-19 R2a/R3a: account focus is tab-local -- Performance is always one account (largest preselected, chooser always shown); Holdings focus; refusals in words; export follows the focused account

<to_id>DSGN_IRPTV1.TO-IV-e-34</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~22</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>complete</status>
<round>6</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.11 @e13fed2413 | **Decomp cell:** `IV-e-34` (decomp v6) | **outcome_ref:** FWD-19, FWD-1, FWD-5, FWD-9 | **depends_on:** IV-e-33 (chain 1, position 2: consumes R1's account list) | **slot:** ~22, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-34` -- C25 part 2: routes R2a and R3a and rules C3, 5 and 6 (proposal sections 2-5), on IV-e-33's R1 (already on this
worktree: read its commits first, `git -C <WS>/portal log --oneline 1e02be40..HEAD`).

**Build:**
(a) **R3/R3a, Performance is per account.** Every `GET /performance/{id}` pairs with a one-account `POST /selections {scope_kind: ACCOUNT,
scope_ids: [accountId]}` (cached per account and directory revision; idempotent -- the same set gives the same `sel_`). The client set is
NEVER sent to `/performance` (`ReportingTab.tsx:171-193` requests with the TAB's account set, not `scopeRef.accountSetId`). At rest the
client's LARGEST account by the snapshot value is preselected (first in snapshot order on a tie); a one-account client opens R3a directly.
The account chooser (each account's label and value) renders ABOVE the answer gate in EVERY state (`ReportingTab.tsx:245-249` moves it out
of the `answer && report` branch). Switching accounts never changes R1: not the identity card, not the holdings total.
(b) **R2a, Holdings focus.** `AccountFilter.tsx` and `IdentityCard.tsx:234-277` (`narrowToOneAccount`, `restoreFullSelection`, chip click) become
TAB-LOCAL account focus: a one-account `POST /selections` + `GET /holdings/{accountSetId}` for the focused view; they stop calling the
page's `select`; R2 (no focus) reads R1's snapshot with no second fetch.
(c) **Rule 6, refusals in words.** A one-account refusal (`OBJECT_NOT_COVERED`, `DEPENDENCY_UNAVAILABLE`) renders in advisor words on the
body with the code one click away (a disclosure); no raw reason code prints on the body.
(d) **Rule 5, export follows the tab.** On Performance the page Export targets R3a's account set and its report revision, never the
client set (`export/ExportButton.tsx`, `export/resolveBundle.ts`); Holdings has no export kind today, unchanged.
(e) **Presets end on the data's as-of date** (amendment 1, issuer 2026-09-26 ~18:3xZ, CTO 101422 accepting ~D's window-4 finding): every
period preset (YTD, 1Y, 3Y, Since inception) ENDS on the data's as-of (business) date taken from the served response or R1's snapshot, never on
the browser's calendar date (`tabs/reporting/period.ts` `dateWindowForPreset` today uses `new Date()`; the T-1 trading-calendar rule). Before
the as-of date is known, no Performance request is sent. A Custom range is the advisor's own and is unchanged.
(f) **Disarm rows W22-S1..S3** (amendment 2, issuer 2026-09-26 ~19:1xZ): IV-e-33's spec-mandated changes (the directory-search
retirement in `fetchIdentityCardData`; rule C1's kind word "Client") break three sibling tests inside this order's grant:
`__tests__/dsgn-irptv1/iv-e-3.card-fed.test.ts` (runtime AND `bun run typecheck`), `iv-e-23.identity-firm.test.ts` (kind-word assertion) and
`iv-e-8.browse-drawer.test.ts` (per-row kind-word assertion). Re-scope each to the R1 spec (class R: retired by FWD-19, PRD v0.12 ROUTE
STRUCTURE / proposal @713a49f7b8 section 5 and rule C1), naming the retiring FWD and version in the test's header comment; never weaken what
the current ENDPOINT still requires. `bun run typecheck` must read 0 errors on your branch. These are graded at the drain (typecheck and the
suite), not as a criterion here.

**The spec is the CRO's route proposal, AT ITS PIN:** read it with `git -C <WS> show 713a49f7b8:org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_ROUTE_STRUCTURE_PROPOSAL_20260926.md` (the working copy has moved since; the PRD adopts the pinned text). Sections 2 (the routes R0-R4), 3 (each route's exact calls), 4 (the six rules, each a test) and 5 (the code each retires) are binding; the PRD's ROUTE STRUCTURE section (`org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md`) carries the CTO's rulings: Call 1 (b) the client's LARGEST account by the snapshot's value is preselected on Performance (the first in snapshot order on a tie) with the chooser always visible; Call 2 (a) route state only, in-page -- no client or account id ever goes into the URL.

**Rulings since the PRD (binding):** each level-0 ACCOUNT node's `display.label` carries that account's own masked tail and type (e.g. "****4304 / IRA"; 2.0.0_SA_COO~M serves it) -- the page READS the label and never derives a mask from an id (CTO 101303); accounts are keyed by the snapshot's account id (via `drill_refs`), NEVER by label (CTO 101340; `tabs/holdings/DrillTree.tsx:312-333` keys category children by label today -- do not copy that); EVERY account-list surface -- the identity card's "over what", the Holdings filter, the Performance chooser, Analysis's included accounts -- shows each account's label AND its value, keyed by account id (proposal rule 4 at @713a49f7b8; PRD v0.12, CTO 101447).

**The rules:** the FE derives nothing; ids never print (not in the body, not in the URL); "not supplied", never zero; a refusal reads in advisor words with its code one click away; colour is keyed by served code or class.

**Environment:** the portal worktree is based on DEV `1e02be40` (= origin DEV = PROD 36a37afc plus site-Z work outside InvestorReporting). Each criterion's test file does not exist at the base: write it from the criterion's text against fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-21.*` and `iv-e-26.*`); it prints the VERDICT only when every arm holds. Do not start any server (dev builds run on port 5174 only, serving the main checkout). The live walk on DEV is the issuer's, after the drain.

### ACCEPTANCE

<criterion id="IVE34-AC1" cell_refs="IV-e-34"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-22/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~22; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-34.per-account-performance.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: PER-ACCOUNT-PERF-OK</expect></criterion>
`IVE34-AC1` -- with a stubbed api and a 3-account client in R1: opening Performance preselects the largest account by snapshot value (a tie takes the first in snapshot order) and issues one one-account POST /selections then one GET /performance for THAT account set; zero GET /performance carry the client set; the chooser renders above the answer gate in the loading, refused and answered states; choosing another account issues one one-account selection (a repeat choice reuses the cached set) and one GET; across switches the identity card text and the holdings total are unchanged. It prints `VERDICT: PER-ACCOUNT-PERF-OK` only when every arm holds.

<criterion id="IVE34-AC2" cell_refs="IV-e-34"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-22/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~22; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-34.focus-refusal-export.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: FOCUS-REFUSAL-EXPORT-OK</expect></criterion>
`IVE34-AC2` -- a one-account OBJECT_NOT_COVERED answer renders in advisor words with its code only inside a closed disclosure (the code string is absent from the visible body); the Performance export submission carries the focused account's set and report revision, never the client set; focusing one account on Holdings issues a one-account selection and a holdings GET for that set while R1 (client, card, total) is unchanged. It prints `VERDICT: FOCUS-REFUSAL-EXPORT-OK` only when every arm holds.

<criterion id="IVE34-AC4" cell_refs="IV-e-34"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-22/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~22; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-34.preset-asof.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PRESET-ASOF-OK</expect></criterion>
`IVE34-AC4` -- with the browser clock set to 2026-09-26 and a served as-of date of 2026-09-22, the YTD preset requests start 2026-01-01 and end 2026-09-22 (and 1Y / 3Y / Since inception end on 2026-09-22 too); with no as-of date known yet, no Performance request is sent; a Custom range is sent exactly as chosen (the difference-control arm). It prints `VERDICT: PRESET-ASOF-OK` only when every arm holds.

<criterion id="IVE34-AC3" cell_refs="IV-e-34" judgment="true"/>
`IVE34-AC3` -- graded by `2.0.0_SA_COO~D` on the live walk on portal DEV (the C25 walk): a 49F 3-account client -> Performance opens on its largest account with a computed figure -> a second account -> Holdings shows the client total unchanged -> clear empties the card; a COT 2-account client renders each account, a refusal in words; the HAR shows every /performance GET paired with a one-account /selections and 0 carrying the client set (FWD-19, FWD-1 ACCEPT; proposal section 7). RECORD; never self-graded.

<expected_criteria>IVE34-AC1, IVE34-AC2, IVE34-AC4, IVE34-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `api/**` and every other page
  are OUT; `src/lib/**` is read, never edited. The backend and its one-account rule (`performance/retained.py:77-80`) are taken as they are.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/header/HeaderSelectionContext.ts
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/resolveBundle.ts
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v6, cell `IV-e-34`.
<owned_cells>IV-e-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE34-AC1, IVE34-AC2, IVE34-AC4, IVE34-AC3. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~22/DSGN_IRPTV1.TO-IV-e-34.account-focus-r2a-r3a.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE34-AC1,IVE34-AC2,IVE34-AC4,IVE34-AC3` BEFORE the flip. `IVE34-AC3` recorded
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

Seating: slot ~22, queue position 2 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 22 --portal-ref 1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`.
