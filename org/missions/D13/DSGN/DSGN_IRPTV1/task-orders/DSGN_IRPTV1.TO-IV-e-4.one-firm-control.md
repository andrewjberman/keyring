# TO DSGN_IRPTV1.TO-IV-e-4 -- FWD-4: one firm control, whoever the viewer is

<to_id>DSGN_IRPTV1.TO-IV-e-4</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~4</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-4` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-4 | **depends_on:** IV-e-3 (same slot) | **slot:** ~4, queue position 2 of 3

---

## WORKER FACE

### THE CELL

`IV-e-4` -- FWD-4 ONE FIRM CONTROL (PRD candidate C2; ROUND_ANALYSIS item 4). Today `portal/src/pages/InvestorReporting/index.tsx`'s `actions=` ternary (the block from the line containing `actions={partnerContext ? <label` through the line containing `}} />}`; at 895752676a lines 156-166 -- print the span you found) renders TWO controls for one job: a raw `<select aria-label="Select Firm">` listing tenant tokens for internal users, and `<FirmDropdown/>` (the shared `PageSurfaceControl`, the same one Model Portfolios uses) for firm users (CONCEPTS H2).

**What changes.** (1) `portal/src/pages/InvestorReporting/header/FirmDropdown.tsx` is EXTENDED additively (CTO ruled touch T2): a new optional prop `catalogue?: { internal: boolean; firms: readonly { id: string; name: string }[] }` -- when present and `internal`, the options are "Global (All)" (`value: 'global'`) followed by each firm by DISPLAY NAME (never the tenant token), the current `value` respected, `onChange` unchanged; when absent the component behaves exactly as today (firm users keep their validated single-firm path through `useFirmContext`). (2) `index.tsx` -- that whole `actions=` ternary block collapses to ONE `<FirmDropdown scope={resolved} value={firmId} onChange={...same handler...} catalogue={partnerContext ? { internal: partnerContext.internal, firms: <display names from globalContext.firms> } : undefined} />` element; the display names come from `globalContext.firms[].scope?.verifiedRequestFirm?.displayName` with the tenant token as the honest fallback label only when no display name exists (print which in the result file). No other line of `index.tsx` changes; no new import.

**Prior art (read, never edit):** `portal/src/pages/ModelPortfolios.tsx:1265` (the "Select Partner:" control), `components/ui/PageSurfaceControl.tsx`, `header/firm.ts`, `global/useFirmContext.ts`, `global/firms.ts`.

### ACCEPTANCE

<criterion id="IVE4-AC1" cell_refs="IV-e-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-4.one-control.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ONE-CONTROL</expect></criterion>
`IVE4-AC1` -- the built behaviour as a DIFFERENCE CONTROL: rendering `FirmDropdown` with `catalogue.internal = true` yields ONE `PageSurfaceControl` dropdown whose first option is "Global (All)" and whose other options are the display names (print `OPTIONS: n of n names, 0 tokens`); with `catalogue.internal = false` (a firm user) the markup carries NO "Global (All)" option and behaves as the round-1 path (the existing `fe-s-2`-era behaviour); the raw `<select aria-label="Select Firm">` no longer exists in `index.tsx` (a source read). `VERDICT: ONE-CONTROL` only when all three hold.

<criterion id="IVE4-AC2" cell_refs="IV-e-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 300 python -c "import subprocess,re,os;B='C:/Users/AndrewBerman/.bun/bin/bun.exe';S=['src/pages/InvestorReporting/__tests__/fe-s-2/','src/pages/InvestorReporting/__tests__/fe-s-10/'];A=re.compile(r'\x1b\[[0-9;]*m');f=lambda d:(lambda o:(sorted(set(re.sub(r' \[[0-9.]+ms\]','',l[2:]).strip() for l in o.splitlines() if l.startswith('\u2717 '))),(lambda m:m.group(1) if m else '?')(re.search(r'Ran (\d+) tests',o))))((lambda r:A.sub('',r.stdout+r.stderr))(subprocess.run([B,'test']+S,cwd=d,capture_output=True,text=True,encoding='utf-8',errors='replace')));bd='C:/tmp/dsgn-irptv1-base';ok=os.path.isdir(bd);t,tn=f('.');b,bn=f(bd) if ok else ([],'ABSENT');print('BASE 895752676a:',len(b),'of',bn,'fail',b);print('TIP:',len(t),'of',tn,'fail',t);print('NEW-AT-TIP:',[x for x in t if x not in b]);print('VERDICT:','NO-NEW-FAILURES' if ok and t==b and tn==bn else ('BASE-CHECKOUT-ABSENT' if not ok else 'NEW-FAILURES'))"</invocation><expect>VERDICT: NO-NEW-FAILURES</expect></criterion>
`IVE4-AC2` -- AMENDED by the issuer on 1.0.0_SA_CTO 100553 (the original "0 fail" premise was false at the base -- 5 of 48 tests fail at 895752676a, the same five at the candidate without this cell, row W4-S2): the seam as a DIFFERENCE control -- the failure SET (test names) of the fe-s-2/ + fe-s-10/ suites at your tip equals the set at portal 895752676a, measured in the issuer's detached checkout `C:/tmp/dsgn-irptv1-base` (read only; if that path is absent the invocation prints `BASE-CHECKOUT-ABSENT` and the criterion is REFUSED, never satisfied by another base), both sets printed with their denominators (`N of 48`), `VERDICT: NO-NEW-FAILURES` only when the sets and the counts are equal. The five base failures pre-exist on DEV, are NOT this cell's, and go on the round-2 enrichment list for the suites' owner.

<criterion id="IVE4-AC3" cell_refs="IV-e-4"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~4; timeout 120 python -c "import subprocess,re;b='895752676a45e83dc252d4253aebc5fa316a229e';f='src/pages/InvestorReporting/index.tsx';base=subprocess.run(['git','show',b+':'+f],capture_output=True,text=True).stdout.splitlines();s=next(i+1 for i,l in enumerate(base) if 'actions={partnerContext ? <label' in l);e=next(i+1 for i,l in enumerate(base) if i+1>s and '}} />}' in l);ic=next(i+1 for i,l in enumerate(base) if '<IdentityCard' in l);d=subprocess.run(['git','diff','-U0',b,'--',f],capture_output=True,text=True).stdout;rem=[x for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))? ',d,re.M) for x in range(int(m.group(1)),int(m.group(1))+(int(m.group(2)) if m.group(2) is not None else 1))];add=[l[1:] for l in d.splitlines() if l.startswith('+') and not l.startswith('+++')];badrem=[x for x in rem if not (s<=x<=e or x==ic)];adds=[a for a in add if 'IdentityCard' not in a];starts=[a for a in adds if re.search(r'<[A-Za-z]',a)];n=subprocess.run(['git','diff','--numstat',b,'--','src/pages/InvestorReporting/header/FirmDropdown.tsx'],capture_output=True,text=True).stdout.strip().split();print('TERNARY-SPAN',s,e,'IDENTITY-LINE',ic,'REMOVED',rem,'BAD-REMOVED',badrem,'ADDED-NON-MOUNT',len(adds),'ELEMENT-STARTS',starts,'FIRMDROPDOWN-NUMSTAT',n[:2]);ok=(not badrem and len(starts)==1 and '<FirmDropdown' in starts[0] and len(n)>=2 and n[1]=='0');print('VERDICT:','ACTIONS-BLOCK-ONLY' if ok else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: ACTIONS-BLOCK-ONLY</expect></criterion>
`IVE4-AC3` -- the ruled touch T2, bound by ELEMENT (CTO 100522): the span is located at the base by its text (the `actions={partnerContext ? <label` line through the `}} />}` line, printed); every REMOVED line of `index.tsx` lies inside that span (or is IV-e-3's `<IdentityCard` line, already on this branch); the ADDED lines outside the IdentityCard line form exactly ONE element start, `<FirmDropdown`; `FirmDropdown.tsx`'s numstat has 0 removed (additive). Nothing else in `index.tsx`.

<criterion id="IVE4-AC4" cell_refs="IV-e-4" judgment="true"/>
`IVE4-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the static markup of the header for an internal viewer and for a firm viewer (`iv-e-4.header-internal.html`, `iv-e-4.header-firm.html`): the same control both times, C8 (no second accent), C1/C11 weight and radius. RECORD; NO VERDICT.

<expected_criteria>IVE4-AC1, IVE4-AC2, IVE4-AC3, IVE4-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `header/firm.ts`, `global/*`, `components/ui/PageSurfaceControl.tsx` (DSGN_REBRND's), `api/**`, `contracts/**` are OUT (read them).
- **Two repos, one worktree pair** (same pair as IV-e-3). Same commit discipline. Never push, merge, rebase, `checkout --`, `clean`.
- **The rules:** a firm user never sees "Global (All)"; the validated-selection path (`useFirmContext`) is not bypassed; a display name, never a tenant token, on the control.
- **Refusal clause.** As every order. **Your queue.** IV-e-8 follows.

<paths>
portal/src/pages/InvestorReporting/header/FirmDropdown.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-4`.
<owned_cells>IV-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE4-AC1` .. `IVE4-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~4/DSGN_IRPTV1.TO-IV-e-4.one-firm-control.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE4-AC1,IVE4-AC2,IVE4-AC3,IVE4-AC4` BEFORE the flip. `IVE4-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `one-firm-control.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W4-S<k>`, continuing).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register; none owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. FirmDropdown.tsx (P-written) admitted additively and index.tsx for the actions block :151-161 (CTO touch T2).
</preflight>

Seating: slot ~4, queue position 2 (after IV-e-3, before IV-e-8), same worktree pair.
