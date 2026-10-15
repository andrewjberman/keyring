# IRPT_DASHBD: CVO adjudication, round 144 (workstream B-49F, ~D2): the disclosure-page placeholder (portal candidate)

<sweep_watermark>2026-10-15T23:08Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T23:08Z, on msg 8737 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND142_144_B49F_DRAIN_END_20261015.md` @162f5530dc, blob f1f543cacc; one packet covers rounds 142 and 144, adjudicated as v113 and v114). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-277 (LOCAL; worker ~224; workspace merge @52ad065fa3; portal candidate wk-IRPT_DASHBD-224-portal @af8ca0ba, LOCAL, never pushed: no origin ref carries it). No judgment criterion: the order holds three mechanical criteria and no render criterion. Re-run: DB144-1-AC1..AC3 FAIL on the landed tree by construction (the portal code is only on the candidate branch). On a scratch root holding a detached portal worktree at af8ca0ba, with the workspace org/ and lib/ linked, they all PASS: 3 of 3, the bun tests under TZ=UTC and TZ=America/Los_Angeles included. The scratch root was removed afterwards. No dev server was started. ROUND 143 EXISTS: issued @ddaafb7971 as the one order TO-DB-b-276 (the chain-cap code-update apply) to 0.7.0_AE_CloudOps~DB2. It is `pending`, so no packet is owed yet. The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S51",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T23:08:00Z",
  "one_line": "Round 144 B-49F: the 49 Financial disclosure page as a visible placeholder, on Andrew's word via the CTO (a252: placeholder for now). THE CODE SHOWS NO CLAIM AND NO FIGURE. Diff c81d54ff..af8ca0ba, 7 files: the product files add ONE text constant, DISCLOSURE_PLACEHOLDER = 'Disclosure page pending' (render/disclosurePlaceholder.ts), and a sheet title 'Disclosures'. Every other added literal is a CSS value, a data attribute or a slot state. No disclosure language, figure, date or firm statement is authored. Supplied disclosure text would print verbatim, one paragraph each, and nothing supplies any today. Both render paths (the custody ClientReportDocument's two status pages, and the performance report's new last sheet) import the one constant. The pointer line is unchanged and not printed on the page it points to. A RENDER IS NOT PROVEN: no criterion renders the PDF. Grading how the page looks needs a print or render of the 49 Financial report from this candidate. That means a portal dev or preview build on its own port (not the shared 5174), or the render host, plus a page read of the last sheet. It is the CTO's next render check, as the packet states. CLIENT-FACING: the candidate is unpushed and unregistered, so it reaches no client; its PROD path waits on Andrew. Rows: D2-W224-S1 (the checker pinned a trailing period on the pointer), S2 (the authored-language scan fired on the existing label 'Billed advisory fee:') and S3 ('every member exactly once' false of the render) are resolved by D2-W224-S7 (Amendment 1). Grounded, with ONE NOTE on S2: dropping 'advisory fee' from the scan narrows the guard, so a future authored disclosure using that phrase would pass it. An exemption for the one existing label would be tighter. S4, S5 and S6 (three pinned assertions edited for the new last sheet: the section-order filter, the last section, and the pointer count = sheets minus one) are each consistent with the stated rule that the pointer is not printed on the disclosure sheet itself. Accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W224-S1",
   "IRPT_DASHBD-D2-W224-S2",
   "IRPT_DASHBD-D2-W224-S3",
   "IRPT_DASHBD-D2-W224-S4",
   "IRPT_DASHBD-D2-W224-S5",
   "IRPT_DASHBD-D2-W224-S6",
   "IRPT_DASHBD-D2-W224-S7"
  ],
  "spec_asserts": "Andrew's word (a252: placeholder for now) relayed by the CTO; a renderer authors no disclosure language; a client-facing page reaches PROD only on Andrew's word; spine L9: a criterion is re-run.",
  "world_is": "A visible placeholder replaces an empty disclosure slot in an unpushed portal candidate. No client sees it, and its rendered look is unproven.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T23:0xZ: DB144-1-AC1..AC3 FAIL on the landed tree; PASS on a scratch root with a detached portal worktree at af8ca0ba (since removed)",
    "git -C portal diff c81d54ff af8ca0ba (7 files); src/pages/InvestorReporting/render/disclosurePlaceholder.ts; ClientReportDocument.tsx and PerformanceReportDocument.tsx added lines",
    "git -C portal ls-remote origin: no ref for wk-IRPT_DASHBD-224",
    "investigation rows D2-W224-S1..S7",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND142_144_B49F_DRAIN_END_20261015.md blob f1f543cacc (msg 8737)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three BLOCKING checker and face defects resolved by the issuer's amendment and green here, and three pinned-assertion edits consistent with the stated rule. The narrowed language scan and the unproven render are named."
 }
]
```
