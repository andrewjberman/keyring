# ANDREW-DIRECT 2026-09-24 ~18:4xZ -- IRPT: the firm tab should filter for Opal staff; the $10K rounding is a mistake

**Channel:** Andrew at the `2.0.0_SA_COO~M` terminal, returning HAR `C:\Users\AndrewBerman\Downloads\bbbbbb.har`
(647 entries, 18:34:36-18:37:33Z). **Recorded by:** `2.0.0_SA_COO~M`, same turn.

## Verbatim

> C:\Users\AndrewBerman\Downloads\bbbbbb.har Interesting finding here, so i "can" view any user while on the global
> tab, but if i change the tab to a specific partner firm, i get blocked on "this firm is out of scope". I dont think
> that is the natural conclusion, in my opinion that should essentially function as a filter for opal employees if
> they select firm in dropdown. The only other thing i noticed immediately was that it appears like there is some
> rounding happening somewhere to the nearest 10k which I want to establish if thats server side (I suspect it is
> because I believe I added a function like that to model portfolios to make it appear prettier front end and that
> is a mistake).

## What the HAR and the source establish (read in place; no header or token left the file)

### 1. The firm tab block is a CLIENT id-space defect, not a scope rule

- **The pair of calls:**
  - 18:35:06Z `POST directory/resolve` with `selected_tenant=49financial` returns 200, firm `fir_c9fc...`, and the
    filter works.
  - 18:35:07Z the portal re-POSTs with `selected_tenant=fir_c9fc04650e2134d6ea033da2`, the OPAQUE id. The answer is
    `ok:false`, UNAVAILABLE / FIRM_BINDING.
  - Cottonwood repeats the pattern at 18:35:41Z.
- **The mechanism:**
  - The firm-specific resolution carries one catalogue entry.
  - `portal/src/pages/InvestorReporting/global/firms.ts:53` (`if (firms.length === 1) return firms[0].firmId`)
    returns its opaque `firmId`.
  - `global/useFirmContext.ts:91` writes that into the dropdown state.
  - `index.tsx:75` sends the state as `selectedTenant`, which the server reads as a registry tenant. The global
    catalogue (`index.tsx:68`) lists `firm.tenant`, so the two spaces meet only in the one-firm branch.
- **Andrew's reading is the design's intent:** the first call already filters.
- **The fix:** hold the registry tenant in the dropdown state, or map `firmId` to `tenant` before the resolve. Owner:
  the portal IRPT surface.

### 2. The $10K rounding is FRONT END, in the shared Model Portfolios component

- **The API carries cents:**
  - Holdings: 24 of 24 amounts carry cents; 0 are multiples of 10K. Examples: INF Greene SIMPLE 5,096.44; 49F Alison
    Horton IRA 49,610.75.
  - The directory calls return no dollar values at all.
- **The rounding lives in the portal:**
  - `portal/src/components/CategoryViewTree.tsx:353-368`: `ROUND_TO = 10_000`, `formatAmount`. Its comment cites
    Andrew-direct 2026-09-15 ~02:5xZ for the Model Portfolios view.
  - `pages/InvestorReporting/tabs/holdings/DrillTree.tsx:316` renders that component, so Holdings inherits the 10K
    grain.
- **Scope question for Andrew:**
  - Investor Reporting amounts must be exact.
  - Whether Model Portfolios also drops the 10K grain is his call: the 09-15 word asked for it; today's word calls
    the function a mistake.

## Journey evidence carried (goal criterion 1)

- **INF:** Greene ****1506 SIMPLE returns READY on d32e50c6. It is a Client-only account: 5 nodes, all labelled.
- **49F:** Alison Horton ****3941 IRA returns READY on 5a25ae76, 19 nodes. MODEL_LEAF "Opal Ultra Long Term" sits
  under the "Models" sleeve.
- **COT:** READY on dec293d6 in the 14:17Z HAR.
- **What this means:** the signed-in API journey is EXERCISED at all three firms. The screen fails SEMANTIC on the
  $10K grain until item 2 lands.
