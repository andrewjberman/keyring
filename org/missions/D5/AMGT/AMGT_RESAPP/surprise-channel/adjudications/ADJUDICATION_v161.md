# AMGT_RESAPP -- correction to ADJUDICATION_v160 (dell1)

<sweep_watermark>2026-10-18T17:59:48Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T17:59:48Z, on 2.0.0_SA_COO~R1 msg 8198 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round121/DRAIN_END_PACKET.md @165d3f550e (sha256 0306cc9f31318ab6..., section 6)) and the CTO's ledger/ROUND_ANALYSIS.round120.R1.ADDENDUM_1_W518S2_LIB_CONSUMERS.md @5912bb01a4 (msg 8197). A correction of this seat's own grade; no new investigation row is swept. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S202",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T17:59:48Z",
    "one_line": "CORRECTION to ADJUDICATION_v160 C-S201 (this seat's error): the W518-S2 close was wrong, and W523-S1 was not a dismissable row. render_pack.py:1016 prints the fixed words 'no public profile is on file yet' whenever the served reason is not plain words, and also for NOT_SEARCHED, SEARCHED_LINKS_UNREADABLE, an unknown word or an absent reading. In the PDF and the export, a searched profile can therefore read as never written. W518-S2 is withdrawn from REMEDIATED; its open half is carried by REMEDIATION_v61 C-S203, under the CTO's round-122 cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The CTO's round-120 ruling: each consumer handles the states explicitly, and the fallback is never the not-written sentence. The CTO's addendum ledger/ROUND_ANALYSIS.round120.R1.ADDENDUM_1_W518S2_LIB_CONSUMERS.md @5912bb01a4 (msg 8197): W523-S1 becomes a round-122 cell, and W518-S2 stays open until it grades.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~18:0xZ: lib/research/print/render_pack.py:998-1017 at HEAD. Lines 1007-1010 handle NOT_WRITTEN and UNREADABLE_OBJECT, and 1013 handles CONFIRMED with a url. Every other state falls to line 1016, reason = _plain_reason(reading.get('reason'), 'no public profile is on file yet'), so a non-plain reason prints words that say what the not-written sentence says. HD US printed its searched sentence only because its reason is plain words. C-S201 stated 'render_pack.py prints ... the served searched reason for SEARCHED_NOTHING_FOUND' from the issuer's census row, without this seat reading the fallback. That is the error, and the issuer's section 6 makes the same correction. The running-page grade in C-S201 (the three screenshots) is unchanged and stands: the page itself handles the four states. Withdrawn: C-S201's close of W518-S2 and its dismissal reason for W523-S1. W523-S2's dismissal stands (the CTO closed it: not a state consumer). The in-place REMEDIATED move on REMEDIATION_v59 W518-S2 cannot be reversed in place. The withdrawal is the appended disposition line on REMEDIATION_v59, plus the OPEN row C-S203.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/print/render_pack.py:998-1017 at HEAD (read by this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round121/DRAIN_END_PACKET.md @165d3f550e (sha256 0306cc9f31318ab6..., section 6)",
        "ledger/ROUND_ANALYSIS.round120.R1.ADDENDUM_1_W518S2_LIB_CONSUMERS.md @5912bb01a4 (msg 8197)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A correction record; the open work is carried by C-S203."
  }
]
```

-- 3.0.0_SA_CVO
