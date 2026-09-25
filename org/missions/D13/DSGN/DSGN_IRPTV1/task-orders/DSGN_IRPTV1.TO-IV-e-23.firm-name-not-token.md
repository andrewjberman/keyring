# TO DSGN_IRPTV1.TO-IV-e-23 -- FWD-15: the firm chip and the identity card print the firm name; the token in a disclosure (IVE18 header half)

<to_id>DSGN_IRPTV1.TO-IV-e-23</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~14</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<round>4</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-23` (decomp v4 @d4add46f46) | **outcome_ref:** FWD-15, FWD-2 | **depends_on:** -- (chain 3) | **slot:** ~14, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-23` -- IVE18-AC4 FAILED (ADJUDICATION_v2 C-S15) on the firm token: the "F-CW" chip on Performance and Holdings, and
"F-CW -- Account" in the identity card. Ruling R6 (1.0.0_SA_CTO, RULINGS_IRPT_20260925.md @75156f2b18): a firm's NAME is client
language (FWD-2 puts the firm on the header) and stays visible; only a system token moves to a disclosure.

**(a)** `IR/global/FirmAttribution.tsx`: the chip prints the firm's display name (from the scope's catalogue /
`verifiedRequestFirm.displayName`); the firm token moves to the chip's disclosure (a `title` or popover). Where no display
name is served, the chip reads "not supplied", never the token. **(b)** `IR/header/IdentityCard.tsx`: the firm line under WHO
reads the firm's display name + the kind word, never the token. **(c)** `IR/__tests__/fe-s-10/parity.test.ts` is KEPT (R6)
and must stay green; do not edit it.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

**Environment (every cell):** the portal worktree is based on DEV `8242412d` (round 3 merged). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. The header's accepted selection reaches tab bodies through `IR/header/HeaderSelectionContext.ts` (wrap a render in `HeaderSelectionContext.Provider` to exercise it). Do not start any server: dev builds run on port 5174 only, and 5174 serves the main checkout, not your worktree.

### ACCEPTANCE

<criterion id="IVE23-AC1" cell_refs="IV-e-23"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~14; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.firm-chip.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: FIRM-CHIP-OK</expect></criterion>
`IVE23-AC1` -- FirmAttribution, given a scope whose firm has a display name and a token, renders the display name on the face and the token only inside its disclosure; given no display name, the face reads "not supplied" and never the token. The test prints `VERDICT: FIRM-CHIP-OK` only when every arm holds.

<criterion id="IVE23-AC2" cell_refs="IV-e-23"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~14; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.identity-firm.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: IDENTITY-FIRM-OK</expect></criterion>
`IVE23-AC2` -- IdentityCard's WHO block prints the firm display name with the kind word and never the firm token on the face (a planted token string is absent from the visible text). The test prints `VERDICT: IDENTITY-FIRM-OK` only when every arm holds.

<criterion id="IVE23-AC3" cell_refs="IV-e-23"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~14; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.parity-kept.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PARITY-KEPT-OK</expect></criterion>
`IVE23-AC3` -- runs `bun test src/pages/InvestorReporting/__tests__/fe-s-10/parity.test.ts` in a subprocess and asserts rc 0 with 0 fail, printing its pass count. The test prints `VERDICT: PARITY-KEPT-OK` only when every arm holds.

<criterion id="IVE23-AC4" cell_refs="IV-e-23" judgment="true"/>
`IVE23-AC4` -- graded at the round-4 drain by `2.0.0_SA_COO~D` on the signed-in trace (IRPT_BCKEND principal IB-rtf-3, else Andrew's walk on `localhost:5174`), per CTO 100991 -- never the CVO: an advisor reads the header and the tab bodies and sees firm names, never a firm code (FWD-15 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE23-AC1, IVE23-AC2, IVE23-AC3, IVE23-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `8242412dde9a3ef807e118f648242cf24ffe2981`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/global/FirmAttribution.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 @d4add46f46, cell `IV-e-23`.
<owned_cells>IV-e-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE23-AC1, IVE23-AC2, IVE23-AC3, IVE23-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~14/DSGN_IRPTV1.TO-IV-e-23.firm-name-not-token.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE23-AC1,IVE23-AC2,IVE23-AC3,IVE23-AC4` BEFORE the flip. `IVE23-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s drain trace (CTO 100991).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W14-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v4 section 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- every write path measured at portal DEV 8242412d at the cut (decomp v4 section 5).
lane: the <paths> block IS the grant; the write sets are pairwise disjoint (decomp v4 section 2).
</preflight>

Seating: slot ~14, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 14 --portal-ref 8242412dde9a3ef807e118f648242cf24ffe2981`.
