# TO MDPF_SECCLASS.TO-SC-e23 -- round 8 SC-e-23: the portal's class lists, legends, colours and layouts lose multi_asset; the two reader tests assert six classes

<to_id>MDPF_SECCLASS.TO-SC-e23</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~22</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** placement DELL1 (the project row's `fabric` still reads laptop) | **Decomp cell:** `SC-e-23`
(`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) | **outcome_ref:** FWD-2, FWD-16, C-SERVER | **depends_on:** none. `SC-e-22`
(the `HoldingsSnapshot` schema enum, dell2) depends on THIS cell: the page drops the value before the published contract does
(PRD addendum v0.7, "the contract changes with its consumer first").

---

## WORKER FACE

### THE CELL

`SC-e-23`. "The portal's class lists, legends, colours and layouts lose `multi_asset`; the two reader tests that assert it are
rewritten to assert six classes" (R8).

**Andrew-direct 2026-10-07:** "there should be no multi-asset class. There are 6 classes: cash, fixed income, equity,
structured, alternatives, commodities." The live table `etf-classifications` holds 0 `multi_asset` rows since the rule-B
remap (issuer's consistent full scan, 3,507 rows, 2026-10-07). No served artifact built after that scan can carry the value.
The portal's lists for it are now dead code that must go.

**Two repos, one worktree pair.** `<WS>` is your workspace worktree, given in your identity line. `<WS>/portal` is a worktree
of the SEPARATE portal git repo, based on portal DEV `8ddfe409948cc79bb45e5ac27a8136264ce8c9d4` (measured 2026-10-07) on its
own branch.
- A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd
  `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`.
- Workspace records (your proof instance, a surprise row) commit from cwd `<WS>` with workspace-relative paths.
- Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Toolchain.** bun: `command -v bun`, else `~/.bun/bin/bun`. Tests: from `<WS>/portal`, `bun test <file>`. If
  `<WS>/portal/node_modules` is absent, stop with a BLOCKING row; never run `bun install` yourself. Typecheck and lint are the
  issuer's drain checks, not yours.

**The files, measured at portal DEV 8ddfe40994 with the AC1 census** (22 files; R8 counted 17 + 6):
- 17 carry the token `multi_asset`: `src/lib/chartColors.ts`;
  `src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/multi-asset.readers.test.ts`;
  `src/pages/AdvisorIntelligence/_partners/{49financial,cottonwood,demo,inflection}/layout.ts`;
  `src/pages/AdvisorIntelligence/_shared/components/{AdvisorAnalytics,PartnerAnalytics}.tsx`;
  `src/pages/AdvisorIntelligence/_shared/lib/composition.ts`; `src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`;
  `src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts`;
  `src/pages/InvestorReporting/__tests__/dsgn-irptv1/{iv-e-12.cash-green.test.ts,iv-e-148.multi-asset-class-readers.test.ts}`;
  `src/pages/InvestorReporting/contracts/{adapt.ts,index.ts}`; `src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts`;
  `src/pages/InvestorReporting/tabs/holdings/assetClass.ts`.
- 5 carry the class as `multiAsset` or the label `'Multi-Asset'`: `src/components/holdings/HoldingsTreemapChart.tsx`;
  `src/pages/InvestorReporting/tabs/holdings/{HoldingsTreemap.tsx,SecurityList.tsx}`;
  `src/pages/InvestorReporting/__tests__/dsgn-irptv1/{iv-e-114.securities-map-walk.test.tsx,iv-e-115.order-and-disclosure.test.tsx}`.
- NOT a security class, so NOT in this cell, and excluded by the census by path: the Market Performance page's Multi-Asset tab
  (all of `src/pages/MarketPerformance/`, 6 files that match; R8 named 3) and
  `src/components/market-performance/MarketRegimeIndicator.tsx` (its "Multi-Asset Momentum" gauge, a market view; R8 listed
  it for triage, and the issuer triaged it OUT).

**Build:**
1. Remove the seventh class everywhere above: the registry colour (`ASSET_CLASS.multiAsset`, its `MIX_PIE` key), the
   adapter's `multi_asset -> multiAsset` mapping, the Holdings label, rank and legend extras, each partner layout's class
   entry, the Advisor Intelligence composition list and the `TenantLayoutConfig` type member.
   - The wire type `contracts/wire/HoldingsSnapshot.ts` drops `multi_asset` from its three enums (nodes,
     security_aggregates, class_totals). This is a hand edit: the published schema changes later under `SC-e-22`.
   - An unknown served token still reads `unclassified` (keep that control arm).
   - The order the six are shown in is unchanged: Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, then
     Other and Unclassified.
2. Rewrite the two reader tests:
   - `src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-148.multi-asset-class-readers.test.ts`
   - `src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/multi-asset.readers.test.ts`
   Each must assert six classes. EVERY test in both files carries `six_class` in its name (AC2 filters on it). Arms:
   - the adapter maps a served `multi_asset` token to `unclassified`, never to a class;
   - the Holdings class list, its order and the legend extras carry exactly the six plus Other and Unclassified;
   - the colour registry and `MIX_PIE` have no seventh class key;
   - the Advisor Intelligence partner layouts list no `multi_asset`.
   Keep each file's name. Edit `iv-e-12`, `iv-e-114` and `iv-e-115` only where they name the seventh class.
3. Delete nothing else, and add no new class.

**Hazard, not your act:** a portal change lands on portal DEV only by the issuer after the drain, and VALGATE runs on that
push. PROD is gated. You push nothing.

### ACCEPTANCE

<criterion id="SC8-e23-AC1" cell_refs="SC-e-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/portal_six_class_census.py</invocation><expect>PORTAL-SIX-CLASS ok=True</expect></criterion>
`SC8-e23-AC1` -- across `<WS>/portal/src` (`.ts/.tsx/.js/.jsx`, market-view files excluded by path and printed), no file carries `multi_asset`, `multiAsset`, `MultiAsset` or the label `'Multi-Asset'`; an empty walk fails.

<criterion id="SC8-e23-AC2" cell_refs="SC-e-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/portal_reader_tests.py</invocation><expect>PORTAL-READERS ok=True</expect></criterion>
`SC8-e23-AC2` -- `bun test` on the two rewritten reader files, filtered to `six_class`, exits 0 with at least one pass and zero fail.

<expected_criteria>SC8-e23-AC1,SC8-e23-AC2</expected_criteria>

Dry-run at the base 2026-10-07, against portal DEV 8ddfe40994: AC1 FAIL as expected
(`PORTAL-SIX-CLASS ok=False scanned=1070 excluded=6 files=22`); AC2 FAIL as expected (`pass=0 fail=2`; the base also lacked
`node_modules` on this box, so the fail is not only the missing `six_class` names). Both checks are the issuer's judges: you
READ them and never edit them.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted. Out of the grant: `src/pages/MarketPerformance/**`, `src/components/market-performance/**`, and every other file.
- **No deploy, no push, no `bun install`.**
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W22-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
portal/src/lib/chartColors.ts
portal/src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/multi-asset.readers.test.ts
portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts
portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts
portal/src/pages/AdvisorIntelligence/_partners/demo/layout.ts
portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts
portal/src/pages/AdvisorIntelligence/_shared/components/AdvisorAnalytics.tsx
portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx
portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts
portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx
portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-12.cash-green.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-148.multi-asset-class-readers.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-114.securities-map-walk.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-115.order-and-disclosure.test.tsx
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts
portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/components/holdings/HoldingsTreemapChart.tsx
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (22 portal files plus the channel).

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-23`.
<owned_cells>SC-e-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e23-AC1, SC8-e23-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~22/MDPF_SECCLASS.TO-SC-e23.portal-six-class-lists.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e23-AC1,SC8-e23-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** per file, what was removed; both checks' output; the portal commit hash(es) and the workspace commit hash(es).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery 2026-10-07 ~07:3xZ: no gate names the portal class lists.
comp-iam: RUN -- R8 battery: not applicable to a portal source edit (no AWS surface).
comp-adversary: RUN -- R8 battery on the decomposition. Cell-specific reads by the issuer at portal DEV 8ddfe40994: strict census 17 files (equals R8); loose census 30 files (R8 said 26: Market Performance carries 6 matching files, not 3, and index.ts/types.ts/tabs/index.ts were uncounted); MarketRegimeIndicator triaged out (a market gauge's label). BLIND: whether a served artifact built before the remap still carries multi_asset in a cache the page reads (the adapter's unclassified arm covers it).
lane: the <paths> block IS the grant.
portal_ref: 8ddfe409948cc79bb45e5ac27a8136264ce8c9d4 (portal origin/DEV at the cut; the workspace gitlink a3ab197ffd is behind it). Provision with `.tools/wk-provision.sh provision MDPF_SECCLASS 22 --path <abs> --portal-ref 8ddfe409948cc79bb45e5ac27a8136264ce8c9d4 --node-modules install` (dell1's main portal has no node_modules, so link would leave the worker without bun deps).
</preflight>

Source: DECOMP_R8 @495efa3c32 (origin 1640a0e86e); PRD v0.12 @87ad6d2e4c.
