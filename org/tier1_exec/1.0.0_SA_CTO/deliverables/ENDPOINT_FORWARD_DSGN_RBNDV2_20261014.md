# ENDPOINT (step 2, /endpoint --forward) -- DSGN_RBNDV2, the surgical re-skin of the portal sidebar and default panel cards

**Author:** `1.0.0_SA_CTO`, 2026-10-14 ~20:4xZ. **Brief:** `docs/briefs/dsgn-rbndv2-sidebar-panel-reskin-brief-20261014.md`
(15,189 bytes, `4.0.0_SA_CRO~A`, commit 1e6d26b626). **Order:** Andrew-direct ~20:1xZ,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_201xZ_DSGN_RBNDV2_SURGICAL_SIDEBAR_AND_PANEL_RESKIN.md`.
**Status:** NOT YET LANDED in a PRD. Its home is the `ENDPOINT` section of
`org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md`, written at L4 once Andrew confirms the DONE WHEN lines below.

```
  FWD-1  Andrew opens Market Overview on the dev build, signed in with real data, and sees the new
         sidebar and the new default panels doing their job on a real page
         DONE WHEN  EXERCISED -- Andrew has looked at the page and said whether it reads as Opal's work
         ACCEPT     the page shows real figures, not sample ones; the new look arrived without anyone
                    rewriting that page; Andrew can say yes or no to how it looks
         SOURCE     brief Part I, "Candidate thread"

  FWD-2  The left navigation looks like Opal's own, not a template rail
         DONE WHEN  EXERCISED -- someone who knows opalinvest.com has compared the two
         ACCEPT     shown the portal beside opalinvest.com, a person says the navigation looks like the
                    same firm's work; shown it beside a stock admin dashboard, they say it does not
         SOURCE     brief O1; Part III "Recognisability"

  FWD-3  A panel looks like Opal's own, with the precision of an analytics tool, not a stock web card
         DONE WHEN  EXERCISED -- the same comparison has been made for a panel
         ACCEPT     a person says the panel looks like Opal's work; nobody says "this looks like Hex"; the
                    old look (stacked dark strips, a box inside a box, a shouting title with a help icon)
                    is gone
         SOURCE     brief O2; Part III "The Hex half is precision, not costume"

  FWD-4  The new look reaches every page that uses the standard sidebar and panels, through one change
         DONE WHEN  APPLIED -- the change is in place and every page using the standard pieces shows it
         ACCEPT     a reviewer reading the change finds only the sidebar, the shared panel pieces and the
                    shared colours and corners, and no individual page edited to get the new look
         SOURCE     brief O3; Part III "Surgical"

  FWD-5  The pages that did NOT get the new panel are named, not quietly left behind
         DONE WHEN  APPLIED -- the list exists and matches what a person sees
         ACCEPT     anyone can read which pages still draw their own old-style panels, open one, and
                    see that it is indeed still old-style
         SOURCE     brief O4

  FWD-6  Andrew sees old and new together and gives his word before any client does
         DONE WHEN  EXERCISED -- Andrew has compared them and answered
         ACCEPT     Andrew can look at the current and the new sidebar and panel on the same page, and
                    nothing of the new look reaches a page a client can open until he says so
         SOURCE     brief O5

  FWD-7  The next page anyone builds gets the new sidebar and panel without asking
         DONE WHEN  APPLIED -- the written design rules describe the new look and the design check uses them
         ACCEPT     a builder starting a new page finds the new sidebar and panel described in the design
                    rules, and the design check flags a panel built the old way
         SOURCE     brief O6

  Nothing regresses (a bar on FWD-2 to FWD-4, not an outcome of its own): panel titles still do not
  run into their buttons when zoomed in, keyboard focus stays visible, and text stays readable against
  its background (brief Part III "Nothing regresses").
```

**OPEN FOR ANDREW (scope, from brief Part II), with a recommendation for each:**
1. **Panel background colour:** today navy on most panels, white on some. The brief keeps SHAPE and FRAME in scope and
   COLOUR out, because of your 2026-10-06 hold that keeps the light Market page experiment off the main branch.
   **REC: leave colour out**; this project changes shape and frame only.
2. **Pages that draw their own panels instead of using the shared ones (FWD-5):** bringing them over means editing
   pages, which the surgical rule excludes by default. **REC: list them only**, and bring any over only on your word, page
   by page.
3. **DSGN_REBRND's held work:** nothing is reused unless you ask (brief Part II). **REC: start clean.**

**Placement:** dell1, on your word ("the design project can be handled on DELL1 box"). D13/DSGN. The L3 registration follows
your confirmation of the lines above.

**NOT READ:** the task-order register, any project JSON (none exists yet), the DSGN_REBRND worktrees, the Yang Liu Teams
thread (the brief marks it as an addendum owed once you sign in to the gateway), and brief Parts IV-VII beyond the outcome
territory, boundary and bar.

## ADDENDUM 1 (~03:2xZ 2026-10-15): Andrew's rulings at 4.0.0_SA_CRO~A, applied to the endpoint

Andrew, verbatim (~00:0xZ, `ANDREW_DIRECT_20261014_201xZ_..._PANEL_RESKIN.md` addendum @f4532f545c): "This whole light mode build
needs to stay on a feature tree on this box and is only pushed when i say so. also yes, i like EAEAF7"

- **Open item 1 is answered: background colour is IN scope.** The page and sidebar ground is `#EAEAF7`; panels are white with
  a 1px `#C4CBDB` border. FWD-2 and FWD-3 grade the light build with that ground.
- **FWD-4 and FWD-6 tighten.** The build lives on a laptop feature branch, and nothing is pushed (not DEV, not PROD) without
  his word. FWD-6's "before anything reaches a client" becomes "before anything leaves the laptop's feature branch".
  FWD-1's "dev build" is the LOCAL dev build (port 5174) of that branch.
- **Open item 2 (placement) is for him:** the first order placed DSGN_RBNDV2 on dell1; this one places the light-mode build on
  the laptop.
