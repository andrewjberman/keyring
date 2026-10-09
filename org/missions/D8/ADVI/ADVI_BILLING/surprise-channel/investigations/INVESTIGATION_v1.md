# ADVI_BILLING -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; rows are validated by `.tools/surprise-row-gate.py`. A seat's row is `ADVI_BILLING-S<k>`; a worker's is `ADVI_BILLING-W<n>-S<k>`. **Append-only during the round.**

## ADVI_BILLING-D2-W2-S1 -- The order says call the fee-quarter route with the same apiRequest as getPlatinumClientSum

```json
{
  "id": "ADVI_BILLING-D2-W2-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:42Z",
  "one_line": "The order says call the fee-quarter route with the same apiRequest as getPlatinumClientSummary, but that apiRequest is module-private, so advi-billing.ts carries its own minimal copy.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/api/endpoints/advisor-intelligence.ts@2d42e9b7 line 232: 'async function apiRequest<T>' with no export; grep of the file for 'export.*apiRequest' returned nothing",
      "the same file is outside this cell's <paths> (read-only), so exporting it is not mine to do"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "getFeeQuarter calls its route 'exactly as getPlatinumClientSummary calls its route (same apiRequest, same firmId rule)'.",
  "world_is": "apiRequest is not exported and advisor-intelligence.ts is not in the grant. advi-billing.ts holds a local apiRequest with the same GET, bearer token, 30 s abort and the same ?firmId= rule, but without the NaN/Infinity strip and the chain-timestamp cache interceptor. If the issuer wants the shared helper, exporting it from advisor-intelligence.ts and swapping the import is a two-line change at the merge."
}
```

## ADVI_BILLING-D2-W2-S2 -- The order says use formatCurrency, which rounds to 3 significant digits ($4,360.54 prints 

```json
{
  "id": "ADVI_BILLING-D2-W2-S2",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:42Z",
  "one_line": "The order says use formatCurrency, which rounds to 3 significant digits ($4,360.54 prints as $4.36K), so the panel formats money to the cent with Intl instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun run on portal/src/lib/universalNumberFormatter.ts@2d42e9b7: formatCurrency(1234.56)='$1.23K', formatCurrency(1250000.45)='$1.25M', formatCurrency(612345.67)='$612K'",
      "a $2.50 platform-fee difference in the fixture cannot be shown if both sides render as '$471'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "'Use the page's own kit: Panel, PanelHeader, PanelContent from @/ui/components/panels, formatCurrency from @/lib/universalNumberFormatter, HelperTip'.",
  "world_is": "Panel, PanelHeader, PanelContent and HelperTip are used. formatCurrency is not: AdvisorBookFeePanel.tsx formats every dollar value with a local Intl.NumberFormat (two decimals) because the panel's job is a cent-level reconciliation. Swapping to formatCurrency is a one-function change if the issuer prefers the compact form."
}
```

## ADVI_BILLING-D2-W2-S3 -- The contract gives components[].rate no unit and the flow entries no shape; the panel assu

```json
{
  "id": "ADVI_BILLING-D2-W2-S3",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:42Z",
  "one_line": "The contract gives components[].rate no unit and the flow entries no shape; the panel assumes rate is an annual decimal fraction (0.0085 = 85 bps) and reads flows as {date, amount, note}.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B2: before the merge, confirm against org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json (or the AB-t-1 object) that components[].rate is a decimal fraction; if it is already in bps the panel shows 100x too many bps",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "the order's contract block lists 'rate' and 'flows_in_period[]' with no unit or element fields; schedule carries a separate 'basis_points' field, which suggests rate is not in bps",
      "org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json was not present in the worktree at HEAD 57dd6256e1 (ls org/standards | grep ADVI_BILL returned nothing)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The panel shows 'the schedule (rate as bps)' and 'flow adjustment ... when non-zero' from fields the contract lists by name only.",
  "world_is": "Unit of components[].rate and the element shape of flows_in_period are unstated here. The panel multiplies rate by 10000 for display and renders each flow as 'date - signed amount - note', skipping missing keys, so a different shape degrades to fewer words rather than failing. The fixture uses the same assumption, so AB1-3-AC2 does not test it."
}
```

## ADVI_BILLING-D2-W2-S4 -- The commit-time naming gate refused the literal '49financial' in the fixture's firm field,

```json
{
  "id": "ADVI_BILLING-D2-W2-S4",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:55Z",
  "one_line": "The commit-time naming gate refused the literal '49financial' in the fixture's firm field, so the fixture carries firm 'example-firm' instead of the contract's example value.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit in the portal worktree, 2026-10-09: 'NAMING REFUSE src/pages/AdvisorIntelligence/_shared/__fixtures__/adviBillingFeeQuarter.json:3 49financial -> lookup(...)  why: NEW hand-kept carrier (context rule)'",
      "after the change the same commit passed: 'NAMING-GATE: PASS 0 graded'; the AB1-3-AC2 validator checks only that the key 'firm' is present, so it still passes on the fixture",
      "the portal worktree repo also has no committer identity configured (fatal: unable to auto-detect email address); the commit used GIT_COMMITTER_NAME and GIT_COMMITTER_EMAIL set for that call only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The contract lists firm (\"49financial\") and the fixture is 'an example object of the contract'.",
  "world_is": "A hand-typed '49financial' in a new portal file is refused by the naming limb (LGIC_ENFORCE). The fixture's firm value is 'example-firm'; nothing in the panel reads it. The real object from AB-t-1 carries the registered value."
}
```
