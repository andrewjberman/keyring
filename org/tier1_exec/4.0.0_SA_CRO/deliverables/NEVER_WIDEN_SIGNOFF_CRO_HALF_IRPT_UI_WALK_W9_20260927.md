# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 9: ~D's read-only round-7 walk

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W9_20260927.md`
blob `6dd81fbfd697ce119c629bb370bd199dcc23ade5` @`a35b555f2e`. The blob is the same at HEAD and on disk (read
2026-09-27 ~05:3xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101814. This seat is not in the act.

## VERDICT: SIGNED on blob 6dd81fbf, with one condition

- **Window 5's shape, fewer powers.**
  - The keys are K1, K1-CRED, K2, K3 and K9 (the retained 49F reports, as window 5).
  - There is no upload, submission or export.
  - No vendor call is reachable: the adapter holds no plan (`approved_performance_plan = null` since 04:34:55Z) and
    no vendor-session grant. So a fresh COT or INF read is refused with 0 vendor calls.
  - K1-CRED is deleted at login, the walk is capped at 60 minutes, and the window at 90 minutes.
- **The adapter bOefL9nx deploy holds as DELTA=0 on what is reachable today.** COT's actual_start becomes the
  account's first series point. Its ledger
  (`20260927T0509Z_irpt-cot-actual-window-20260927_deploy_completion.md`, read here) grades DELTA=0 on every reachable
  surface:
  - 49F arms and reopens are unchanged;
  - COT and INF fresh reads are refused with no plan;
  - retained reports are immutable.

  The new disclosure (07-21..09-22) appears only at the next armed COT compute, and it corrects a false start date,
  so it narrows the claim to the truth.
- **This walk is the round's verification artifact** (the CVO grades on it). The condition below exists so the grade
  attaches to the code it names.

## CONDITION -- the walk log proves which bytes it ran

The packet names the build as "a LOCAL portal build of DEV `200d257a`". A dev server serves the working tree, not a
commit. Read here at ~05:3xZ:
- the portal working tree is on `DEV` @`200d257a`, with **0 modified tracked files**;
- it has 40 untracked entries, including `src/org/`, `src/pages/AdvisorIntelligence/org/` and **`public/__mockcot`**.
  The dev server serves `public/` as static files.

So the walk log records, at walk start and at walk end:
1. `git -C portal rev-parse HEAD`, which must be `200d257a`;
2. `git -C portal status --porcelain --untracked-files=no`, which must be empty;
3. from the HAR, the count of requests to `/__mockcot/`, which must be 0.

If any of these fails, the walk grades "200d257a plus the named difference", not "200d257a", and the CVO's grade
says so.

## Carried

- **Named item 1:** this seat does not arm the ui-walker from the window's create through its audit close.
- **K9:** the 49F REPORT# pre-read before ~D's first request, and the HAR-traced re-read at the audit.

Not measured by this seat: the served pins in W9-3 (the packet's, re-read at create).
