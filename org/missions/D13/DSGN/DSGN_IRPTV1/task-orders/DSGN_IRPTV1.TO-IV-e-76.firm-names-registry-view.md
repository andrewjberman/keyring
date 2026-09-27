# TO DSGN_IRPTV1.TO-IV-e-76 -- Firm display names from the registry generated view (W35-S1 ruling)

<to_id>DSGN_IRPTV1.TO-IV-e-76</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~40</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E10 | **Decomp cell:** `IV-e-76` (decomp v9) | **outcome_ref:** FWD-2, FWD-15 | **depends_on:** chains P, H, N and X drained (index.tsx, IdentityCard.tsx, FirmAttribution.tsx); the registry view target committed by 1.0.0_SA_CTO | **slot:** ~40, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-76` -- Rows (acceptance lines verbatim, PRD v0.18): UIR-04 "Every option shows the firm's display name (e.g. 'Cottonwood'), laid out the same on every row."; UIR-13 "The line reads the firm's display name with normal punctuation."; UIR-30 "The firm shows by display name, once."

CTO ruling W35-S1 (analysis section 2): firm names come from `infra/logic/registry/scopes.json` `tenant.display_name`, rendered by a DEC-5 generated view into a generated TS module the portal imports (see scopes.json `_about` and `lib/opal_naming.py`). `header/firmDisplay.ts`'s title-case transform is retired; no firm literal is typed in portal source. A shorter page label, if an acceptance line needs one, is a registry FIELD added by 1.0.0_SA_CTO before this cell seats, never a literal.

**Build:** Generate the module from the registry (commit the generator output, not hand edits), import it in firmDisplay.ts and its callers, and delete the title-case transform.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE76-AC1" cell_refs="IV-e-76"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-40/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-76.firm-registry.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: FIRM-NAMES-REGISTRY-VIEW-OK</expect></criterion>
`IVE76-AC1` -- the built behaviour: (a) every firm label equals the generated module's value for its tenant key; (b) a grep of portal/src for the firm display strings outside the generated module finds none; control: requests still carry the tenant key. Print `VERDICT: FIRM-NAMES-REGISTRY-VIEW-OK` only when every arm holds.
<criterion id="IVE76-AC2" cell_refs="IV-e-76" judgment="true"/>
`IVE76-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE76-AC1, IVE76-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/header/firmDisplay.ts
portal/src/pages/InvestorReporting/header/search.ts
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/global/FirmAttribution.tsx
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/generated/
lib/opal_naming.py
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-76.firm-registry.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-76`.
<owned_cells>IV-e-76</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE76-AC1, IVE76-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~40/DSGN_IRPTV1.TO-IV-e-76.firm-names-registry-view.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE76-AC1,IVE76-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W40-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~40, queue position 1 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 40 --path <abs> --portal-ref <DEV at seating>`.
