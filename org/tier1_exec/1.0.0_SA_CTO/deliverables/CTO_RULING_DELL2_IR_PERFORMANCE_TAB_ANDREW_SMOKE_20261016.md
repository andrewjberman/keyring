# CTO RULING -- Investor Reporting Performance tab, from Andrew's smoke on localhost:5174 (2026-10-16 ~18:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Binds:** `2.0.0_SA_COO~C2` (page files) and `2.0.0_SA_COO~D2` (DB-b-307, the template).
**Andrew's words, verbatim (four screenshots, 14:22-14:23 ET):** *"I have not seen a change on this page in days."* (1) A Cottonwood client
(Thiessen, Anna) has never shown performance, though Holdings displays. (2) A 49 Financial client (ANNA BEYER, ****9943) shows no
performance, "object not covered". (3) An Inflection client (Andersen) shows performance, but *"as usual, always displaying this useless
header 'The firm selected in the header does not match this client's firm', which will always be the case because we are looking from Global
view ... for advisors viewing their own firm clients, the thing should always match (it should not even be possible on the frontend for
Advisor from Firm A to select between Firm A B C)."* (4) *"we're not seeing any of the sector radial charts and other visually enticing
breakdowns which were presented in the 49 Financial reporting template. We need to get more visuals together for this view ... using
techniques we already have and components we already have all over this page."*

## What was measured (code at `cand/dell2/irpt-49f-performance-template-mount` @49381cb5, served on 5174)

- **One cause behind (1), (2) and (3).** The served performance reads (the published series for 49 Financial and Cottonwood, the client
  summary, and the template's filled report) are firm-bound. The service refuses them unless the request names a firm
  (`ReportingTab.tsx:450-452`: "the service refuses every reporting read by design at Global", `IRPT_BCKEND _authz/served.py`). The service
  already admits an internal caller choosing a firm per request through `selected_tenant` (`served.py:535`; the export path already sends
  it, `export/submit.ts`). The page sends none at Global. So at Global, every published series is refused. Cottonwood and 49 Financial have
  no other source and show nothing. Inflection shows the holdings-based calculation (PATH A) with the firm banner above it.
- **The template (4) is mounted but silent.** `PerformanceTemplateView` (`ReportingTab.tsx:963`) reads the served filled report. At Global
  that read is refused, the state stays `none`, and it renders nothing, not even the dev SYNTHETIC PREVIEW. A silent component is a defect in
  itself.

## RULED

1. **Global resolves per client.** When the header reads Global (All), every client-scoped read sends `selected_tenant` = the CLIENT's own
   firm, from the resolved scope or the identity card. That covers the dashboard series and manifest, the client summary, the per-account
   YTD, the template's filled report, and the export. Global staff then see each client as that client's firm. No backend change unless the
   measured read below shows the service refusing a staff `selected_tenant`.
2. **The firm-mismatch banner is removed.** At Global it can no longer arise (ruling 1). A firm-bound advisor is never offered another firm:
   the header's Firm control shows only the caller's own firm for any non-global login. If that is not already enforced, it is enforced in
   the same cell, and a test proves an advisor cannot select a second firm.
3. **No silent panel.** The template view shows its served report, or (dev server only) the SYNTHETIC PREVIEW, or a worded state. It never
   renders nothing.
4. **Proof on the three named clients,** read on localhost:5174 at Global under a staff login. Thiessen, Anna (Cottonwood), ANNA BEYER
   ****9943 (49 Financial) and Andersen (Inflection) each show performance, with no firm banner. Any client still empty gets its own traced
   cause (for example an account absent from the 6,949 or 939 published series), never a generic message.
5. **Visuals (his point 4), a second cell, plan first.** Bring the 49 Financial template's sector and asset-class radial charts and its
   allocation and attribution breakdowns onto the Performance tab for all three firms. Reuse components already on the page (the Holdings
   donuts, the dashboard class breakdown, ReportChart) and the PerformanceReport pieces; build nothing new where one exists. `~D2` and `~C2`
   send this seat a one-page panel list first (each panel, its data source per firm, and the component reused), then build.
6. **Order and approval.** Rulings 1 to 4 are ONE cell, cut on top of DB-b-307's branch, so Andrew smokes one branch. This seat serves it on
   5174 the moment it builds. It is client-facing: DEV and PROD wait on Andrew's approval after his smoke.

-- 1.0.0_SA_CTO~DELL2
