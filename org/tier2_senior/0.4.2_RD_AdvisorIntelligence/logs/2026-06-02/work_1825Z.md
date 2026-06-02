# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~1825Z

## TO: ADVI_INFPRM.W1 — firmId-scoped layout resolution (FE-only) — IMPL-COMPLETE, RAVC2-pending

**Trigger:** Andrew-direct parallel-velocity dispatch; ~C spawned as 2nd RD-FE lane (parallel to RD~B INFOTD/INFNNA). Consumed W1 (dispatch_held=false, READY-TO-DISPATCH) off RD~B's P0 finding c35e3cd40.

### Root cause (P0-confirmed)
`firmOverride = internal ? FIRM_ID : undefined` (inflection/index.tsx:154). External partner users → firmOverride=undefined → the 3 data+role sites calling `useTenantLayout(firmOverride)` resolved to `DEFAULT_LAYOUT` (49F-ish) instead of their firm layout. Symptoms: S1 Role Composition wrongly rendered for Inflection; S3 Book view routed to the Lambda path ("Could not load book data") instead of the static adapter.

### Fix shipped (durable SHARED.006)
Two-param `useTenantLayout(firmId, firmOverride?)` — strictly additive:
- firmId-scoped fields (identity / tabs / panels / roles / routes) ← `firmId`
- data-path fields (dataSources / features / assetClasses.includesCash) ← `firmOverride ?? firmId`
- Fast path: when both scopes resolve to the same layout object (every single-param caller + internal admins whose firmOverride matches the partner route), the firmId layout is returned by reference unchanged → zero behavior change for existing callers.

3 sites repointed: `AdvisorPublicProfile.tsx:1155`, `AdvisorBookView.tsx:143`, `ClientsTab.tsx:150` (BooksTab).
firmId threaded into `AdvisorPublicProfile` + `AdvisorBookView` props and all 5 render sites: inflection/demo/49financial index NonAdminProfileTab (inflection's lacked firmId — added), ClientsTab x3, AdvisorsTab x1.

### Regression matrix (logic-verified — visual = Andrew/CTO, headless fabric-down)
| Context | roles.composition | dataSources handler | includesCash | verdict |
|---|---|---|---|---|
| Inflection ext (firmOverride=undefined) | inflection→**false** (S1 FIXED) | inflection→**static** (S3 FIXED) | true | **FIXED** |
| 49F ext | 49F→true (=DEFAULT) | 'lambda'→usesStatic=false (=DEFAULT undefined→false) | false | identical |
| demo ext | demo→true | 'lambda'→false | false | identical |
| internal admin (firmOverride defined) | firmId==partner==override | dataFirm=override (pre-W1 path) | per override | identical |

Key non-regression lever: `usesStaticClientDetail === 'static'` makes DEFAULT's `undefined` and 49F/demo's `'lambda'` both `false`; `composition.enabled=true` for DEFAULT + 49F + demo alike. Data fetchers still receive `firmOverride` unchanged (W1 changes handler-CHOICE + panel gating only; the getClientsTab backend leg is W2/AE).

### Evidence
- portal DEV commit **3d5d05b8** (8 files, 89+/13−), pushed `80f285c8..3d5d05b8` VALGATE-PASS.
- Scoped commit: RD~B's concurrent uncommitted `types.ts` + `DistributionTab.tsx` correctly EXCLUDED (safe-commit.sh --only pathspec).
- `tsc -b --noEmit` clean; `eslint` 0 errors (1 pre-existing unrelated react-hooks/exhaustive-deps warning at AdvisorPublicProfile:330).

### Open / handoff
- CVO: verify cross-tenant regression matrix (asymmetric-bug bar) on served DEV.
- Andrew/CTO: rendered-pixel visual smoke all 4 contexts.
- ws-repo `portal` gitlink bump → coordinated promote (RD~B concurrent on same portal tree; INFPRM = 2nd PROD promotion, separate from INFOTD bundle).
- W2 (AE, getClientsTab backend) independent + parallel.

RAVC2'd: 1.0.0_SA_CTO + 2.0.0_SA_COO + 3.0.0_SA_CVO.
