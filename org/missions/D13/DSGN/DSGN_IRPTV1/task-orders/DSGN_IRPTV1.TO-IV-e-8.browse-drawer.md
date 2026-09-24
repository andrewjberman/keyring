# TO DSGN_IRPTV1.TO-IV-e-8 -- FWD-3: the browse drawer; the paged combobox retired

<to_id>DSGN_IRPTV1.TO-IV-e-8</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~4</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-8` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-3 | **depends_on:** IV-e-4 (same slot) | **slot:** ~4, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-8` -- FWD-3 THE BROWSE DRAWER (PRD candidate C9; ROUND_ANALYSIS item 8; brief O2, card 1 ruled (a); CONCEPTS section 2.1 and the Advisor Intelligence L2 `ClientListPanel` as the reference). Today `portal/src/pages/InvestorReporting/header/ClientSearch.tsx` is a 288px combobox paging 25 rows with a "Load more clients" link (the `loadMore()` function and its button -- find them by text and print the lines) -- the ONLY way to reach a client.

**What changes.** (a) NEW `portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx`: a "Browse" trigger that opens a right-hand drawer (the portal's own drawer / dialog primitive if one exists under `ui/components`; else a `Panel`-styled aside with a close control -- say which in the result file) listing every client the viewer may reach: walk `directory-browse` pages TO COMPLETION for the current context (all `contexts` in the Global view, grouped by firm display name; the one firm otherwise), each row = display name, masked tail, kind in advisor words, active / terminated (from `terminatedMarker` / availability), account count; a filter box narrows the list client-side; selecting a row calls the SAME `onSelectionChange(narrowing, row)` path `ClientSearch` uses (build the `SearchOptionRow` + `Narrowing` exactly as `header/search.ts` does -- read it; do not fork its rules). (b) `header/ClientSearch.tsx` (CTO ruled touch T6): `loadMore()` and the "Load more clients" button are REMOVED; the type-ahead stays as it is for those who know the name; the Browse trigger renders beside the input (the drawer component itself lives in the new file; `ClientSearch` renders `<BrowseDrawer .../>` in its own row -- so `index.tsx` needs NO change; if a clean mount needs `index.tsx`'s search row (the `<ClientSearch` element through its closing `/>`), that is the alternative T6 form the CTO ruled and IVE8-AC3 admits it). Paging state (`cursors`) that only served "Load more" goes with it; a page-size constant used by the type-ahead query stays.

**Fixtures:** `fixtures/directory.*.json` (the named negatives incl. `directory.multiple-relationships.json`, `directory.terminated-entitled.json`), `contracts/directory-browse.ts` (`DirectoryBrowsePage`), `fixtures/smoke/fe-s-14-global.json` for the Global shape.

### ACCEPTANCE

<criterion id="IVE8-AC1" cell_refs="IV-e-8"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-8.browse-drawer.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: DRAWER-OK</expect></criterion>
`IVE8-AC1` -- the built behaviour with a stubbed api returning three browse pages: the drawer lists every entry across the pages (`ROWS: n of n across p pages`), grouped by firm in the Global shape (`GROUPS: g`), each row carrying name, masked tail, kind words, status, account count and NEVER an id (`IDS-PRINTED: 0`); the filter narrows to the matching rows; a terminated entry reads as terminated. `VERDICT: DRAWER-OK` only when all hold.

<criterion id="IVE8-AC2" cell_refs="IV-e-8"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-8.selection-path.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SAME-SELECTION-PATH</expect></criterion>
`IVE8-AC2` -- the seam as a DIFFERENCE CONTROL: selecting a drawer row calls `onSelectionChange` exactly once with a `Narrowing` + `SearchOptionRow` deep-equal to what `ClientSearch`'s own type-ahead selection produces for the same entry (build the expected pair with `header/search.ts`'s exported helpers); typing in the combobox still selects (the type-ahead arm unchanged); the string "Load more clients" no longer appears in `ClientSearch.tsx`'s source and the markup. `VERDICT: SAME-SELECTION-PATH` only when all hold.

<criterion id="IVE8-AC3" cell_refs="IV-e-8"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 python -c "import subprocess,re;b='895752676a45e83dc252d4253aebc5fa316a229e';idx='src/pages/InvestorReporting/index.tsx';base=subprocess.run(['git','show',b+':'+idx],capture_output=True,text=True).stdout.splitlines();imp=max(i+1 for i,l in enumerate(base) if l.startswith('import '));ts=next(i+1 for i,l in enumerate(base) if 'actions={partnerContext ? <label' in l);te=next(i+1 for i,l in enumerate(base) if i+1>ts and '}} />}' in l);ic=next(i+1 for i,l in enumerate(base) if '<IdentityCard' in l);cs=next(i+1 for i,l in enumerate(base) if '<ClientSearch' in l);ce=next(i+1 for i,l in enumerate(base) if i+1>=cs and l.strip()=='/>');d=subprocess.run(['git','diff','-U0',b,'--',idx],capture_output=True,text=True).stdout;h=[int(m.group(1)) for m in re.finditer(r'^@@ -(\d+)',d,re.M)];other=[x for x in h if not (x<=imp+1 or ts<=x<=te or x==ic or cs<=x<=ce+1)];n=subprocess.run(['git','diff','--numstat',b,'--','src/pages/InvestorReporting/header/search.ts','src/pages/InvestorReporting/header/selectionRequest.ts','src/pages/InvestorReporting/header/ScopeSummary.tsx'],capture_output=True,text=True).stdout.strip();cur=open('src/pages/InvestorReporting/header/ClientSearch.tsx',encoding='utf-8').read();keep=['const PAGE_LIMIT = 100','const MIN_QUERY_CHARS = 2','const generation = useRef(0)','++generation.current'];missing=[k for k in keep if k not in cur];gone=('Load more clients' not in cur) and ('function loadMore' not in cur);print('INDEX spans import<=',imp,'ternary',ts,te,'identity',ic,'search',cs,ce,'HUNKS',h,'OUTSIDE',other,'| UNTOUCHED-SET',repr(n),'| F5/F3 MISSING',missing,'| PAGING-GONE',gone);ok=n=='' and not other and not missing and gone;print('VERDICT:','DRAWER-IN-GRANT' if ok else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: DRAWER-IN-GRANT</expect></criterion>
`IVE8-AC3` -- the ruled touch T6, bound by ELEMENT (CTO 100522): `search.ts`, `selectionRequest.ts`, `ScopeSummary.tsx` untouched (empty diff); any `index.tsx` hunk lies in the import region, the `actions=` ternary (IV-e-4's, same branch), the `<IdentityCard` line (IV-e-3's) or the `<ClientSearch` element's span, all located by text; in `ClientSearch.tsx` the F5 / F3 constants and guard survive byte-for-byte (`const PAGE_LIMIT = 100`, `const MIN_QUERY_CHARS = 2`, `const generation = useRef(0)`, `++generation.current`) and `loadMore` + "Load more clients" are gone.

<criterion id="IVE8-AC4" cell_refs="IV-e-8" judgment="true"/>
`IVE8-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the static markup of the drawer open and closed (`iv-e-8.drawer.html`) and the smoke PNG if IV-e-2's fixture renders it: an advisor who does not know a client's spelling finds them in the drawer (brief O2); C3, C8 (the trigger is not a second accent), C10/C12. RECORD; NO VERDICT.

<expected_criteria>IVE8-AC1, IVE8-AC2, IVE8-AC3, IVE8-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `header/search.ts`, `header/selectionRequest.ts`, `header/ScopeSummary.tsx`, `header/IdentityCard.tsx`, `header/FirmDropdown.tsx`, `ui/components/**`, `contracts/**`, `api/**` are OUT (read them).
- **Two repos, one worktree pair** (same pair as IV-e-3/4; your branch carries their commits). Same commit discipline. Never push, merge, rebase, `checkout --`, `clean`.
- **The rules:** the selection stays server-accepted through the same request; the drawer changes PRESENTATION only; ids never print; the type-ahead is kept.
- **Refusal clause.** As every order. **Your queue:** this is your last order; then the pair ends.

<paths>
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-8`.
<owned_cells>IV-e-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE8-AC1` .. `IVE8-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~4/DSGN_IRPTV1.TO-IV-e-8.browse-drawer.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE8-AC1,IVE8-AC2,IVE8-AC3,IVE8-AC4` BEFORE the flip. `IVE8-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `browse-drawer.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (one block per order in this pair: IV-e-3, IV-e-4, IV-e-8); surprise rows in the investigation file (id `DSGN_IRPTV1-W4-S<k>`, continuing). Then `NEXT: queue empty`.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register; none owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. ClientSearch.tsx (P-written) admitted for the paging removal + the trigger; index.tsx for the search row 166-171 if needed (CTO touch T6).
</preflight>

Seating: slot ~4, queue position 3 (after IV-e-3 and IV-e-4), same worktree pair.
