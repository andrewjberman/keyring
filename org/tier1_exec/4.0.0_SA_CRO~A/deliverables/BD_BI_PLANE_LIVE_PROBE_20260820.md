# BD BI plane -- LIVE probe results (under Andrew's ~0210Z egress extension)

**Seat:** `4.0.0_SA_CRO~A` | **2026-08-20 ~0225Z** | **Authority:** Andrew-direct verbatim
*"you have egress there too, go ahead"* (@8e37f53710). **Read-side only; every POST here is a query
verb that mutates nothing.**

## 1. THE PLANE IS LIVE-CALLABLE, AND THE TIE-OUT NOW HAS THREE INDEPENDENT LEGS

Bearer minted from **`bd3/auth/token`** (NOT `/datamining/auth/token` -- each sibling app mints its
own, per `AUTHENTICATION.md`). `POST /advisor/api/v1/Dashboard/data` -> **200, 791,931 B, 216 groups.**

| leg | Travis Penfield EMV | groups |
|---|---|---|
| my qt6 datamining probe (template 517678 / run 517753) | 456,773,323.40 | 216 |
| Andrew's HAR capture of his own dashboard session | 456,773,323.40 | 216 |
| **my LIVE call to `/advisor/api/v1/Dashboard/data`** | **456,773,323.40** | **216** |

**Delta 0.00 across three independent legs, two distinct API planes, and two distinct observers.**

## 2. `levelType` IS THE GRAIN CONTROL -- AND ACCOUNT GRAIN EXISTS

| levelType | status | bytes | rows |
|---|---|---|---|
| `PortfolioGroup` | 200 | 791,931 | **216** |
| `Account` | 200 | **26,782,154** | **7,625** |
| `Relationship` | 200 | 9,312,404 | **2,622** |
| `Portfolio` | 500 | 0 | -- |
| `zzzNegCtl9999` (NEG-CTL) | 500 | 0 | -- |

Invalid values 500, so the instrument discriminates. **`Portfolio` is NOT a valid levelType here**
(it 500s exactly like the invented one) -- worth knowing before anyone designs against it.

**7,625 account rows is BROADER than both comparison universes we hold** -- fam 7,202 and the
allocation export's 6,155 distinct accounts.

## 3. THE MULTI-MEMBERSHIP TELL

Account grain: **7,625 rows but only 5,361 distinct `accountNumber`** (and 5,619 distinct
`accountName`; `id` is unique 7,625/7,625). So accounts REPEAT -- consistent with DS~B's measured
90.6% multi-group membership, and it implies the rows are group-scoped internally.

## 4. ACCOUNT ROWS CARRY NO GROUP ATTRIBUTION -- and the supervision split DOES reach account grain

35 fields per account row. **Not one names a group**; the only group-ish field is `levelType`, whose
value is the constant `"Account"`. So a single call at account grain does **NOT** yield
account-to-group mapping.

**What it DOES newly carry, and this is the useful half:** `supervisedBmv` / `unsupervisedBmv` /
**`supervisedEmv` / `unsupervisedEmv` at ACCOUNT grain**, plus `walletSharePercentage`,
`contribution`, `netgain`, `fees` / `previousFees`, `relationshipCount`, and four
relationship-lifecycle sub-objects (`new` / `active` / `lost` / `existingAndNoRelationship`).
qt6 expresses none of this. The supervision-sleeve GRAIN convention (ADVI_49F PARITY ADDENDUM A6)
can be served from here at account grain.

## 5. ⛔ THE `values` FILTER IS NOT APPLIED AS CALLED -- CAUGHT BY A NEGATIVE CONTROL

| call | rows | distinct acctNum |
|---|---|---|
| `values: []` (unfiltered) | 7,625 | 5,361 |
| `values: [272271]` (Travis's real group id) | 7,625 | 5,361 |
| **`values: [999999999]` (CANNOT EXIST -- NEG-CTL)** | **7,625** | **5,361** |

**A nonexistent group id returns byte-identical results to a real one and to no filter at all.** So
`values` is inert in this call shape -- it needs a companion flag or a different `filterTypeId`
pairing I have not found.

> **Without that control I would have reported "Travis Penfield has 5,361 accounts / 2,001,567,789.82
> EMV."** That is the whole firm, presented as one advisor's book -- a wrong number that would have
> looked entirely plausible beside a real group id. **Fourth invented-input control of the session,
> fourth kill.**

`includeDirectAssign` True vs False is likewise **inert at both grains** (216 groups / Travis EMV
identical; 7,625 rows identical). It is not the primacy discriminator on this call shape.

## 6. THE MEMBERSHIP PRIMITIVES (all live, all 200)

```
GET  /advisor/api/v1/advisorview/groupingLevel?groupExternalId=z08362691
     -> ["Portfolio","Class","Segment","Asset","Account"]        (levels, not members)
POST /advisor/api/v1/advisorview/multiPortfolioGroups  {"searchString":"","selectedIds":[],"take":20}
     -> [{id, name, firmID, excludeFromBI, hasAllPortfolioAccess, overrideAdvisorReportsLimit}]
GET  /advisor/api/v1/Dashboard/groupingDetailSearch
     -> dimension objects; id 1140 "Portfolio Group", mappedColumn "portfolioGroup"
GET  /request/api/grouping?pageType=2
     -> groupings keyed by z-id, e.g. {"id":"z08362701","name":"Assets",
        "levels":["Portfolio","Asset","Account"], "_href": .../request/api/grouping/z08362701}
GET  /advisor/api/v1/zzz_negctl_9999   (NEG-CTL)  -> 404   [the plane discriminates]
```

`multiPortfolioGroups` exposes **`excludeFromBI`** per group -- the same concept as catalog dim 5150
"Exclude From BI", now at group grain and directly readable.

## 7. WHAT IS STILL NOT ANSWERED, STATED PRECISELY

**Account-to-group ATTRIBUTION, and therefore PRIMACY, is NOT yet obtained.** The rows are
group-scoped (the 7,625-vs-5,361 tell) but carry no group field, and the `values` filter is inert as
called. The untried lead is the **`advisorview` flow** -- `initial-load` -> `multiPortfolioGroups`
with `selectedIds` -> `result` -- which is the sequence Andrew's own session performed
(`selectedIds:[272271]` immediately after searching "travis"). `/request/api/grouping/{z-id}` is a
second untried lead with a self-declared `_href`.

**Not chased further tonight rather than half-chased into a claim.** Named as the next step with its
evidence, not as a finding.
