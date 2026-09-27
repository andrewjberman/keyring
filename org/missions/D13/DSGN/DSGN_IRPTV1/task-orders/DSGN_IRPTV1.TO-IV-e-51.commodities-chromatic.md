# TO DSGN_IRPTV1.TO-IV-e-51 -- commodities takes a CHROMATIC palette token, picked mechanically (CTO 101681 ruling (b) on IV-e-49)

<to_id>DSGN_IRPTV1.TO-IV-e-51</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~30</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 (UIR-37, UIR-44, UIR-50) | **Decomp cell:** `IV-e-51` (decomp v7 addendum 6; workstream AI-TAGS) | **outcome_ref:** FWD-12/13 (O7) | **depends_on:** IV-e-49 (same slot, commit 888215a7) | **slot:** ~30, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-51` -- this slot's IV-e-49 (portal commit 888215a7) set `MIX_PIE.commodities` and `ASSET_CLASS.commodities` (in
`src/lib/chartColors.ts`) to `PALETTE.gray900`. 1.0.0_SA_CTO ruled (101681): **not gray900** -- `getAssetClassTextColor` uses gray900
as the dark text ink, so it would be one colour with two meanings (UIR-37: "No hue means both a model and an asset class"; O7 one
colour, one meaning).

**The pick is mechanical (the CTO's rule, verbatim in substance):** take the `PALETTE` token with the LARGEST minimum CIEDE2000 (dE00)
against every `MIX_PIE` colour, every `ASSET_CLASS` colour and every model primary (extended models included, discovered as IV-e-49's
test discovers them), subject to ALL of:
1. it is chromatic -- no gray, neutral, black or white token;
2. no text or ink role in `src/lib/chartColors.ts` (or the portal's text tokens) uses it;
3. its minimum dE00 is at least 20.
**Prefer the amber/gold family if any member clears 20** (then the largest-minimum member of that family); otherwise the global
largest-minimum token. Use it for BOTH `MIX_PIE.commodities` and `ASSET_CLASS.commodities`. The text drawn on it (white or dark,
whichever `getAssetClassTextColor` would give or you add for it) has contrast 4.5:1 or better. If NO chromatic token clears 20, change
nothing, say so, and name the best score (refusal clause).

Keep the >= 20 assertion in BOTH `iv-e-46.class-readers.test.ts` and `iv-e-49.commodities-distance.test.ts` (they currently expect
gray900's values; update them to the rule, never to a hard-coded pass), and print the chosen token and its minimum dE00.

**Environment:** this slot's portal worktree (IV-e-46 + IV-e-49 on DEV 6757223a). Reuse IV-e-49's dE00 implementation. Do not start any
server. The workspace `portal` gitlink is NOT yours: never stage or commit it.

### ACCEPTANCE

<criterion id="IVE51-AC1" cell_refs="IV-e-51"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-30/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/iv-e-51.commodities-chromatic.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COMMODITIES-CHROMATIC-OK</expect></criterion>
`IVE51-AC1` -- the built behaviour with its control: the test enumerates every `PALETTE` token, applies rules 1-3 and the amber/gold
preference itself, and asserts the chosen token equals `MIX_PIE.commodities` and `ASSET_CLASS.commodities`; it prints each candidate's
minimum dE00 and the winner; it asserts the text contrast on the winner is at least 4.5:1. Control arm: gray900 is rejected by rule 1 or
2. Prints `VERDICT: COMMODITIES-CHROMATIC-OK` only when every arm holds.

<criterion id="IVE51-AC2" cell_refs="IV-e-51"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-30/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts src/pages/AdvisorIntelligence/__tests__/iv-e-46.composition-tags.test.ts src/pages/AdvisorIntelligence/__tests__/iv-e-49.commodities-distance.test.ts src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-44.securities-map.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx 2>&1 | tail -25</invocation><expect>0 fail</expect></criterion>
`IVE51-AC2` -- no regression: IV-e-46's and IV-e-49's tests (updated to the rule), the IR securities map and the IR new-classes test pass
together.

<expected_criteria>IVE51-AC1, IVE51-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every other file is READ, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/lib/chartColors.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-49.commodities-distance.test.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-51.commodities-chromatic.test.ts
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 6, cell `IV-e-51`.
<owned_cells>IV-e-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE51-AC1, IVE51-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~30/DSGN_IRPTV1.TO-IV-e-51.commodities-chromatic.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE51-AC1,IVE51-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W30-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read on slot ~30 @888215a7: getAssetClassTextColor returns PALETTE.gray900 as the dark ink (chartColors.ts :374-379), the colour IV-e-49 chose for commodities.
lane: the <paths> block IS the grant; slot ~30 only.
</preflight>

Seating: slot ~30, queue position 3 of 3. Drain: with both checks PASS and contrast >= 4.5:1, GO to DEV with no second review (CTO 101681).
