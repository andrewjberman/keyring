# DSGN_AMGTV1 -- round 63 L9 grades (dell1)

<sweep_watermark>2026-10-09T11:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T11:45:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 2358, org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/ROUND63_CLOSE.md @bedf70c4bd. zzo-1 AC3 NOT MET (no description printed under its label; the press not walked); zzo-2 AC3 MET; zzo-3 AC3 MET with the pick carried to the next walk.

```json
[
  {
    "id": "DSGN_AMGTV1-D1-C-S30",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T11:45:00Z",
    "one_line": "TO-AV-zzo-1 AC3 NOT MET. (1) ASML's Thesis window prints NO description: the heading 'COMPANY DESCRIPTION' sits directly over the machine-drafted Item 5 financial sentences ('In Logic, net sales increased by EUR 2.9 billion ...', ITEM 5 > PARAGRAPH 31), so the label now names filed financial detail as the company description -- the false 'No company description' line is gone, but the description it should be replaced by is not printed (the server sends company_description, served, 1,535 chars). (2) 'Pressing a figure moves to its passage' was not exercised: the walk has no press and no after-shot; the issuer's reading states the sentence is the press, from the build, not from the page. Re-grade on a walk that shows the description text under its label and one press with its result.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: JUDGMENT criteria are graded at L9 by a seat that did none of the work, never self-graded.",
    "world_is": "TO-AV-zzo-1 AC3 NOT MET. (1) ASML's Thesis window prints NO description: the heading 'COMPANY DESCRIPTION' sits directly over the machine-drafted Item 5 financial sentences ('In Logic, net sales increased by EUR 2.9 billion ...', ITEM 5 > PARAGRAPH 31), so the label now names filed financial detail as the company description -- the false 'No company description' line is gone, but the description it should be replaced by is not printed (the server sends company_description, served, 1,535 chars). (2) 'Pressing a figure moves to its passage' was not exercised: the walk has no press and no after-shot; the issuer's reading states the sentence is the press, from the build, not from the page. Re-grade on a walk that shows the description text under its label and one press with its result.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T113527Z/shots/008-ASML-NA-Equity-Thesis-open-INVESTMENT-THESIS-In-Apr.png: 'COMPANY DESCRIPTION' heading, then MACHINE sentences with Item 5 passages; no description prose",
        "AMGT_RESAPP WALK_ROUND83.md item 1: API dossier_sections company_description served, 1,535 chars",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/ROUND63_CLOSE.md @bedf70c4bd real-run row TO-AV-zzo-1 ('The whole sentence, including the figure, is the press to its passage')"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  },
  {
    "id": "DSGN_AMGTV1-D1-C-S31",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T11:45:00Z",
    "one_line": "TO-AV-zzo-2 AC3 MET: NVDA's spine draws the event titles in one band above the plot, in two rows, none drawn over another ('China Tells Alibaba, Tech Firm...', 'GTC effect...', 'Global funds lead biggest on...', 'Nvidia Introduces First PCs D...', 'Nokia, Nvidia Unveil AI-Powe...', 'Nvidia Partner Hon Hai's Sale...', 'China May Let Alibaba Buy N...'). Seen again, not of this criterion: a Price hover tooltip covers the name band in the capture.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: JUDGMENT criteria are graded at L9 by a seat that did none of the work, never self-graded.",
    "world_is": "TO-AV-zzo-2 AC3 MET: NVDA's spine draws the event titles in one band above the plot, in two rows, none drawn over another ('China Tells Alibaba, Tech Firm...', 'GTC effect...', 'Global funds lead biggest on...', 'Nvidia Introduces First PCs D...', 'Nokia, Nvidia Unveil AI-Powe...', 'Nvidia Partner Hon Hai's Sale...', 'China May Let Alibaba Buy N...'). Seen again, not of this criterion: a Price hover tooltip covers the name band in the capture.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T113121Z/shots/004-NVDA-overlay.png",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/ROUND63_CLOSE.md @bedf70c4bd real-run row TO-AV-zzo-2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  },
  {
    "id": "DSGN_AMGTV1-D1-C-S32",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T11:45:00Z",
    "one_line": "TO-AV-zzo-3 AC3 MET with a carried half: typing 'ASML' reads \"2 companies match 'ASML'; type the ticker.\" with two buttons, 'ASML Holding NV (ASML_US_Equity)' and 'ASML NA (ASML_NA_Equity)', plus 'Back to all names'. 'Picking one opens it' was not walked -- shots 050-056 all show the same choice page; the walker pressed neither button. The target page ASML_NA_Equity loads on the other walk (20261009T113527Z). Carry: the next walk presses one button and shows the page it opens.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: JUDGMENT criteria are graded at L9 by a seat that did none of the work, never self-graded.",
    "world_is": "TO-AV-zzo-3 AC3 MET with a carried half: typing 'ASML' reads \"2 companies match 'ASML'; type the ticker.\" with two buttons, 'ASML Holding NV (ASML_US_Equity)' and 'ASML NA (ASML_NA_Equity)', plus 'Back to all names'. 'Picking one opens it' was not walked -- shots 050-056 all show the same choice page; the walker pressed neither button. The target page ASML_NA_Equity loads on the other walk (20261009T113527Z). Carry: the next walk presses one button and shows the page it opens.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T111310Z/shots/050-ASML-overlay.png and 052-ASML-Thesis.png (same choice page)",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/ROUND63_CLOSE.md @bedf70c4bd real-run row TO-AV-zzo-3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  }
]
```
