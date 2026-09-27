# TO DSGN_IRPTV1.TO-IV-e-56 -- The firm shows by its display name, once, never its tenant key (UIR-04, UIR-13, UIR-30)

<to_id>DSGN_IRPTV1.TO-IV-e-56</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~35</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-56` (decomp v8) | **outcome_ref:** FWD-2, FWD-15 | **depends_on:** IV-e-54 (contracts/adapt.ts; drained to DEV before this chain seats) | **slot:** ~35, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-56` -- Rows (acceptance lines verbatim, PRD v0.16): UIR-04 "Every option shows the firm's display name (e.g. 'Cottonwood'), laid out the same on every row." UIR-13 "The line reads the firm's display name with normal punctuation." UIR-30 "The firm shows by display name, once."

The round-7 walk (window 9) shows `cottonwood` and `49financial` (the tenant key, lower case) in the search options and on the card.
Root cause: `contracts/adapt.ts` `firmFromWire` (:696-706) sets `displayName: firmId`, and `adaptResolvedScope` (:717) overwrites it
with `registry_tenant`; every screen reads that value. The key reaches the screen at: `header/search.ts` `firmNameFor` :99-102
(-> `header/ClientSearch.tsx` `toSearchSelectOption` tag :46; failure text :122/:128); `header/BrowseDrawer.tsx` `loadBrowseGroups`
:104 (group heading :245); `header/IdentityCard.tsx` :452 and :490 (`${firmName} (${kind})`); `index.tsx` :290 (FirmDropdown
catalogue) and :326 (unavailable firms); `global/FirmAttribution.tsx` :44-57. No shared name map exists: `src/pages/ModelPortfolios.tsx:244-249`
and `src/pages/AdvisorIntelligence/index.tsx:23-28` each carry their own; the page fixture `fixtures/fe-s-10/scope.two-firms.json:40,46`
carries display names.

**Build:** One page-local display-name source (a new `header/firmDisplay.ts`), keyed by tenant key, used by `firmFromWire` /
`adaptResolvedScope` for `displayName` and by every site above; a tenant with no entry shows a neutral title-cased form of its key,
never the raw lower-case key. The firm appears ONCE per line (UIR-30; no "firm (firm)" repetitions) with normal punctuation (UIR-13).
The tenant key stays the value every request and cache key uses; only what is SHOWN changes. Copy the names from the existing maps;
never type a client name.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt: `3f76cdb2` plus IV-e-54, merged before this chain seats. Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

**Amendment 1 (issuer, 2026-09-27 ~13:0xZ; CTO 101880, PRD v0.17 @fc21988bce, CRO walk docs/briefs/irpt-ui-review-verification-20260927.md):** this cell also carries UIW-0927-03 "While a client loads, the header shows a loading state, never words that read as missing data." (CRO walk: right after a client is picked the header reads 'value pending', 'not supplied', '0 accounts' until Holdings loads.) Build: while the client's snapshot is loading, `header/IdentityCard.tsx` shows one loading state (for example 'Loading client...') in place of those words; once loaded, or refused, it shows the answer or the refusal as today. AC1 gains the arm: a loading identity card carries none of 'value pending', 'not supplied', '0 accounts'.

### ACCEPTANCE

<criterion id="IVE56-AC1" cell_refs="IV-e-56"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-35/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-56.firm-display.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: FIRM-DISPLAY-OK</expect></criterion>
<criterion id="IVE56-AC2" cell_refs="IV-e-56" judgment="true"/>
`IVE56-AC2` -- judgment: UIR-04/13/30 read on the running page (round-8 walk), graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. AC1: render the search option, browse heading, identity card line and firm attribution from fixtures carrying two firms; each shows the display name, none shows a lower-case tenant key, the firm appears once per line; control: requests still carry the tenant key. The `__tests__/` grant is for re-goldening a pinned test that asserted the tenant key as a DISPLAY value, each re-golden naming UIR-04/13/30.

<expected_criteria>IVE56-AC1, IVE56-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/header/firmDisplay.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/header/search.ts
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/global/FirmAttribution.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-56.firm-display.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-56`.
<owned_cells>IV-e-56</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE56-AC1, IVE56-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~35/DSGN_IRPTV1.TO-IV-e-56.firm-display-names.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE56-AC1,IVE56-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W35-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~35, queue position 1 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 35 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).
