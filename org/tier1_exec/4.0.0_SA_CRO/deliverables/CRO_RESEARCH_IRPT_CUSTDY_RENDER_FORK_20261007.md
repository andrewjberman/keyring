# IRPT_CUSTDY hop 5: render the client report through irpt-export-render (a), or through its own renderer (b)?

**Author:** `4.0.0_SA_CRO~DELL2`. **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 199 (research ask 2). **Mode:** read-only. No
AWS call, no host start, no edit outside this file. **Measured at:** workspace HEAD `dd3f44e69e`, portal `DEV` `8ddfe409`,
2026-10-07 08:54Z.

## The fork, answered

### 1. What the render path is, measured

- **The engine is the portal, not a template library.** `irpt-export-render` freezes a bundle to S3. It then dispatches by
  SSM to a host that opens the portal's print route (`/investor-reporting/print?bundle=<id>&kind=...&renderToken=...`) in
  headless Chromium and calls `page.pdf()` (`infra/aws/ec2/investor-reporting-export/render_export.cjs:180-306`). The
  layout lives in the portal's versioned render package (`portal/src/pages/InvestorReporting/render/manifest.ts`,
  `PrintEntry.tsx`). A "template" is a React document chosen by `reportKind`.
- **The host is `irpt-ycharts-runner` (`i-0167fd745ad906a66`).** It is held STOPPED by Terraform, and it carries the only
  Chromium and playwright on the estate. Andrew's word lets it start only "for the export render"
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_145xZ_YCHARTS_RUNNER_MAY_BE_STARTED_FOR_THE_EXPORT_RENDER.md`,
  "WHAT IT DOES NOT SETTLE: Any other start of that host, for any other purpose").
- **A Lambda cannot render.** A browser in Lambda means fetching one off Opal infrastructure, which was refused at IB-s-8
  (rows IRPT_BCKEND-W3-S1/S2; `render_export.cjs:4-10`). Any renderer, (a) or (b), therefore runs on that host.
- **The contract is closed and extended by kind.** The submit-export body carries report refs, sections, versions and
  options, and no document (W4-S1, `submit-export.request.json`). The print package refuses any bundle whose schemaVersion
  it does not list (`manifest.ts:357`, `assertSupported`). It knows two kinds, mapped by `templateFor`
  (`manifest.ts:400-401`).
- **Precedent for a new kind:** ANALYSIS was added as a second kind in three IRPT_BCKEND cells on 2026-10-02:
  - IB-pr-281 @429f938bee: resolve, grant pins and print query take the kind;
  - IB-pr-291 @23d839c618: a prospect scope for the render grant;
  - IB-pr-296 @acce364286: the installed render ports and the print query's resolved kind.

  Performance exports were unchanged throughout.
- **Owner:** the export path is IRPT_BCKEND's export lane (`2.0.0_SA_COO~P2`, per IRPT_CUSTDY-S2). Under the writer split of
  2026-09-23 (RULINGS.md:296), P owns the public schema, wire, display, export integration and runtime installation.
  IRPT_CUSTDY's PRD (C-PROGRAMME, PRD:111) owns templates.

### 2. Option (a): extend the export contract with a client-report kind

**What changes, by surface:**

| # | Surface | Change | Owner |
|---|---|---|---|
| a1 | submit-export request and resolve (`export/retained_export.py`, 439 lines) | accept a client-report document reference; resolve, grant and freeze it into the bundle, as IB-pr-281 did for ANALYSIS | IRPT_BCKEND ~P2 |
| a2 | export role IAM (`export/b1_submit.tf`, `b1_report_prefixes`) | read grant on the client-report document's address under the firm's own prefix (an LGIC builder address; none exists yet, PRD S06) | IRPT_BCKEND, CTO plan review |
| a3 | render host (`render_export.cjs:240`) | a third kind. **Today any template name not starting with "analysis" renders as PERFORMANCE**, so a client-report name sent before this edit would be silently mis-rendered, not refused | IRPT_BCKEND |
| a4 | portal render package (`manifest.ts`, `PrintEntry.tsx`) | a `client-report` kind and its supported schemaVersion; `PrintEntry` dispatches it | P (package) |
| a5 | the template itself | a `ClientReportDocument` per firm (49 Financial first) | IRPT_CUSTDY (C-TEMPLATE) |

- **Cost:** about the ANALYSIS precedent (three backend cells), one host line, and the portal kind. IRPT_CUSTDY builds only
  the template (a5).
- **Blast radius:** the served `irpt-export-render` Lambda, the render host script and the portal print package, all shared
  with the live Performance and Analysis exports. That risk is bounded by the precedent: the kind is additive and refused per
  schemaVersion. Each regression is caught by the existing export tests (`export/tests/`, 8 files) if a4 and a3 land together.
- **Rollback per surface:**
  - a1, a3, a4: revert the additive kind; the old kinds are untouched.
  - a2: delete the one policy statement.
- **Schedule cost:** IRPT_CUSTDY hop 5 waits on IRPT_BCKEND's export lane to cut and release a1 to a4.

### 3. Option (b): IRPT_CUSTDY's own renderer on the same engine

**What it must stand up:**

| # | Need | Why |
|---|---|---|
| b1 | its own dispatch (a Lambda or script) and its own SSM command document | the export function is not used |
| b2 | its own render authorization: token minting, SSM carriage, the IAM fence | `b2_render.tf` is the export's; its fence (`render_host_parameter_fence`) admits only `/irpt/render-token/*` |
| b3 | a host start for a NEW purpose | Andrew's word covers only "the export render"; a start for anything else needs his word or a CVO classification |
| b4 | a print route or HTML template the host can open | either a second portal print entry (the same package, so the same owner as a4), or `page.setContent` of the local HTML `report_render_request.py` already builds (`render_export.cjs` only does `page.goto`, so this means a second host script) |
| b5 | LGIC names and addresses for every new resource | CLAUDE.md rule 30: a new pipeline is built to LGIC |

- **Cost:** greater than (a). It duplicates the security-bearing half of the export path (b2), adds a second host script
  (b4), and needs a sovereign word (b3).
- **Blast radius:** new surfaces only, so the live exports are untouched. But it is a second PDF render path for IRPT reports
  on the same host. That reads close to the standing veto on a duplicate output path (CLAUDE.md section 5, "NEVER stand up
  a shadow/build-alongside pipeline, duplicate output path"). Whether a different report kind is "duplicate" is a ruling,
  not this brief's call. Two render-token carriers on one host also widen the host's SSM fence.
- **Rollback:** delete the new resources. Nothing shared moves.

### 4. Recommendation

**(a), with the writer split as the PRD already draws it.** IRPT_BCKEND carries the pipe (a1 to a4); IRPT_CUSTDY writes only
the template (a5).

Reasons:
1. The PRD already names the export path for hop 5 (PRD:143-144).
2. (a) has a three-cell precedent.
3. (b) needs a new Andrew word for the host, duplicates the render authorization, and sits near the duplicate-path veto.

Until a1 to a4 land, hop 5's look stays the local HTML (W4-S1 "world_is") and the advisor read (S08) can be held on that
HTML. That last point is a suggestion for the decomposition; it is not adjudicated here.

**Two hazards to carry whichever is chosen:**
1. `render_export.cjs:240` maps every unknown template to PERFORMANCE. Make it refuse an unknown template.
2. The render host is the YCharts runner. IRPT_YCDGEN FWD-11 / S28 removes the "YCharts producer". The PRD does not say
   whether the host or its node_modules survive. If they go, every export render goes with them.

### 5. Not checked

- The served state of `irpt-export-render` and the host: no AWS read was made, by design.
- Whether the client-report document's address and size fit the bundle freeze's limits.
- Whether `PrintEntry`'s render grant model fits a per-client batch: one export per client means N host cycles per advisor.
  Batch cost is the open question for hop 5 under either option.
