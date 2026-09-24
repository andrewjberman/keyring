# TO DSGN_IRPTV1.TO-IV-e-3 -- FWD-2 complete: the identity card fed and its chips live

<to_id>DSGN_IRPTV1.TO-IV-e-3</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~4</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-3` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-2 | **rows:** W1-S3 | **depends_on:** -- (chain A head) | **slot:** ~4, queue position 1 of 3 (then IV-e-4, IV-e-8)

---

## WORKER FACE

### THE CELL

`IV-e-3` -- FWD-2 COMPLETE (ROUND_ANALYSIS item 3; PRD backlog item 1; row W1-S3). Today `portal/src/pages/InvestorReporting/header/IdentityCard.tsx` renders "Account details not supplied" chips except when the selection is one account, "value pending" for the total, and no toggle -- because the `<IdentityCard` mount line in `index.tsx` (find it by the element text; at 895752676a it is line 191 -- print the line you found) feeds only `scope` / `selection` / `row`.

**What changes.** (1) THE MOUNT LINE ONLY (CTO ruled touch T1, bound by ELEMENT never by line number): the `<IdentityCard` line in `index.tsx` becomes `<IdentityCard scope={selectedScope} selection={acceptedNarrowing} row={accepted ? row : null} api={api} scopeRef={selectedScopeRef} onNarrow={select} />` -- no other line of `index.tsx`, no new import (`api`, `selectedScopeRef` and `select` already exist in `SelectionWorkspace`). (2) THE CARD does the rest: with `api` and `scopeRef` in hand it requests the holdings snapshot for the accepted selection (the same `holdings-snapshot` operation `HoldingsTab` uses -- read `tabs/holdings/HoldingsTab.tsx` and `api/endpoints/investor-reporting.ts` for the exact call and the `irKey` cache key; reuse them, never a second client) and prints the unique custody total + business date from it ("value pending" while loading or absent); it requests one `DirectoryEntry` per permitted account (`scope.permittedAccountIds`) through `directory-search` / `directory-browse` on the accepted firm context, and renders each chip as `displayName` + masked tail -- NEVER an id; a chip click narrows the scope through `onNarrow` with the SAME `Narrowing` + `SearchOptionRow` shape `header/selectionRequest.ts` and `index.tsx`'s `select()` expect (the server accepts or refuses; you change presentation only). If the directory operations cannot return per-account entries for a relationship selection (a DECLARED assumption -- decomp v2 section 2), the chips keep the honest fallback and IVE3-AC2 is REFUSED with the measured response shape.

**Fixtures:** `fixtures/resolvedScope.success.json`, `fixtures/directoryEntry.success.json`, `fixtures/directory.multiple-relationships.json`, `fixtures/holdingsSnapshot.success.json` (adapted shape); wire shapes under `fixtures/wire/`.

### ACCEPTANCE

<criterion id="IVE3-AC1" cell_refs="IV-e-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-3.card-fed.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CARD-FED</expect></criterion>
`IVE3-AC1` -- the built behaviour with a stubbed api (a test double implementing the two operations from the fixtures): the total prints the snapshot's `custodyTotalAmount` formatted and the business date; one chip per permitted id with `displayName` + masked tail (`CHIPS: n of n named, 0 ids`); while the snapshot is pending the total reads "value pending". `VERDICT: CARD-FED` only when all hold.

<criterion id="IVE3-AC2" cell_refs="IV-e-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-3.chip-narrows.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CHIP-NARROWS</expect></criterion>
`IVE3-AC2` -- the toggle as a DIFFERENCE CONTROL: clicking one chip calls `onNarrow` exactly once with a `Narrowing` whose `scope.accountIds` is that one account and a row whose `entry.accountId` matches (print the call's arguments); clicking it again (or "all") restores the full permitted set; with `onNarrow` absent the chips render but no handler fires (the round-1 mount shape still works). `VERDICT: CHIP-NARROWS` only when both arms hold.

<criterion id="IVE3-AC3" cell_refs="IV-e-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 python -c "import subprocess;b='895752676a45e83dc252d4253aebc5fa316a229e';n=subprocess.run(['git','diff','--numstat',b,'--','src/pages/InvestorReporting/index.tsx','src/pages/InvestorReporting/header/ScopeSummary.tsx'],capture_output=True,text=True).stdout.strip().splitlines();d=subprocess.run(['git','diff','-U0',b,'--','src/pages/InvestorReporting/index.tsx'],capture_output=True,text=True).stdout;ch=[l for l in d.splitlines() if (l.startswith('+') or l.startswith('-')) and not l.startswith('+++') and not l.startswith('---')];other=[l for l in ch if 'IdentityCard' not in l];print('NUMSTAT:',n);print('CHANGED:',len(ch),'OUTSIDE-MOUNT:',other);ok=(len(n)==1 and n[0].split()[2].endswith('index.tsx') and n[0].split()[0]=='1' and n[0].split()[1]=='1' and not other);print('VERDICT:','ONE-LINE-MOUNT' if ok else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: ONE-LINE-MOUNT</expect></criterion>
`IVE3-AC3` -- the ruled touch T1: `index.tsx` differs from `895752676a45e83dc252d4253aebc5fa316a229e` by exactly the one mount line (1/1, both changed lines carry `IdentityCard`); `ScopeSummary.tsx` untouched.

<criterion id="IVE3-AC4" cell_refs="IV-e-3" judgment="true"/>
`IVE3-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the static markup (`iv-e-3.identity-card.html`) and the smoke PNG if IV-e-2's fixture renders it: the brief's bar "an advisor answers who / how much / over which accounts / as of when from the header alone", chips readable as names, the toggle discoverable. RECORD; NO VERDICT.

<expected_criteria>IVE3-AC1, IVE3-AC2, IVE3-AC3, IVE3-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `header/ScopeSummary.tsx`, `header/ClientSearch.tsx`, `header/FirmDropdown.tsx`, `header/search.ts`, `header/selectionRequest.ts`, `api/**`, `contracts/**` are OUT (read them; `index.tsx` is admitted for the ONE mount line only).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` based on `895752676a45e83dc252d4253aebc5fa316a229e`; the same commit discipline; never push, merge, rebase, `checkout --`, `clean`.
- **Toolchain.** As every order.
- **The rules:** the selection stays server-accepted (`POST selections`); you change presentation; ids never print; "value pending" / "not supplied", never zero.
- **Refusal clause.** As every order. **Your queue.** IV-e-4 then IV-e-8 follow in this pair.

<paths>
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-3`.
<owned_cells>IV-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE3-AC1` .. `IVE3-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~4/DSGN_IRPTV1.TO-IV-e-3.identity-complete.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE3-AC1,IVE3-AC2,IVE3-AC3,IVE3-AC4` BEFORE the flip. `IVE3-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `identity-complete.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W4-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register; none owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. index.tsx admitted for the ONE mount line (CTO touch T1).
</preflight>

Seating: slot ~4, queue position 1 (IV-e-4 position 2, IV-e-8 position 3); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 4`.
