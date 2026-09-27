# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the COT one-use arm (plan 22f0a988) and window-8 amendment K12

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_ARM_W8_K12_20260927.md`
blob `27434c70dbdb85c2f91b50a302a5c08e3c915e1c` @`d70974dc4a`. The blob is the same at HEAD and on disk (read
2026-09-27 ~04:2xZ).
**Authority:** Andrew-direct "yes to all three", call 3: "Re-arm ONE Cottonwood one-use Performance plan for one
signed-in COT run (sequenced after INF)".
**Asked by:** 2.0.0_SA_COO~P msg 101797. This seat is not in the act.

## VERDICT: SIGNED on blob 27434c70

- **It is inside Andrew's call 3.**
  - Andrew's unit is ONE plan use for ONE signed-in run. The packet states plainly that one use of the BD adapter is 2
    HTTP requests (`performancePeriod` + `performanceSeries`, `bd_selected.calculate`) under ONE claim
    `PERFORMANCE_USE#22f0a988..`.
  - Sequencing holds: INF's plan 7f64b166 was spent at 04:11:14Z, with one Orion call and RPT-df47a1fc (msg 101797).
- **The plan was built with no vendor call,** through the served path's own functions:
  - the account is the rule's median pick (82 eligible, 0 refused);
  - the end is READ from the served holdings answer (09-22), per the (a)/(b) direction CTO 101756 set for INF;
  - it expires at 18:00Z.
- **The arm-OFF pre-check follows this seat's window-8 condition:** account, start and end from the HAR must equal
  the plan; the adapter answers VendorEgressRefused with 0 vendor calls; both are recorded before the arm.
- **The arm is 1/1/1, and not env-only like INF's. This seat signs it knowingly.**
  - It adds `irpt-performance-approved-session-policy`: `secretsmanager:GetSecretValue` on the ONE COT session secret.
  - It changes the two env keys.
  - It destroys INF's session read.

  That is the designed per-firm switch (`retained.tf:161-172`). The live re-plan must read exactly 1/1/1, or it
  stops. The rollback (re-apply the spent 01209afb) reverses it.
- **Traceable writes.** Window 8's before-census (`UI_WALK_W8_CENSUS_BEFORE_20260927.json`, read here) reads the
  REPORT# counts per firm as **cottonwood 0**, inflection 0, 49financial 19. So a COT report after K12 is K12's own.

## Named items for the audit and the close

1. **Count BD requests, not GETs.** In the INF read, the page sent two identical GETs, and the gate's conditional
   claim let one through (msg 101797). The COT audit counts, from the adapter log, **exactly 2 BD requests under ONE
   claim**. A second claim, or a third BD request, is branch (d). COT REPORT# goes from 0 to at most 1, traced to
   K12's HAR.
2. **Recommendation to the CTO, not a condition:** after the claim, disarm to `approved_performance_plan = null`
   rather than leaving the spent plan armed. A spent plan's session grant (here, read access to the COT BD session
   secret) serves no call, and `null` removes it. This is the same question for INF's spent 01209afb, which holds
   INF's session read today. Leaving it is the existing, accepted pattern; this seat only names that it grants
   something no call uses.

Not measured by this seat: the plan receipt and its sha, the dry plan output, and `retained.tf` (the packet's).
