# IRPT_ANLREQ: CVO adjudication, a correction -- the Investor Reporting page is Opal-internal

<sweep_watermark>2026-10-11T17:47Z</sweep_watermark>

By `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:47:44Z. Read: portal `src/App.tsx:462` on origin/PROD and origin/DEV.
This seat wrote "a page a firm login can open" and "a client-facing page" without reading the router. The route requires an admin,
an Opal-internal and a Dev user. Row D2-S56.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S10",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T17:47:44Z",
    "one_line": "This seat's correction row D2-S56 is dismissed as a correction record: the Investor Reporting page is Opal-internal by its route on portal PROD and DEV, so 'a page a firm login can open' in this seat's row D2-S48, and 'client-facing' in its round 4 read file and slug, were wrong. The hold it described is put to the CTO by message.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S56"
    ],
    "spec_asserts": "CLAUDE.md, Agent Autonomy: the push law's client-facing exception.",
    "world_is": "No remediation row is opened: the correction changes a hold, not a defect. Row D2-S51 stays ARMED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-S56",
        "this seat's read 2026-10-11T17:47:44Z of portal src/App.tsx on origin/PROD 37aa1247 and origin/DEV ca23f110: line 462 routes /investor-reporting through ProtectedRoute requireAdmin requireInternal requireDev; line 107 gives the nav entry the same three; lines 460-461 cite Andrew-direct 2026-09-22 ('marked in tsx for admin and isDev only'); line 614 gives the print view the same three plus a render claim. Found first by worker row DSGN_IRPTV1-D2-W59-S2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A correction of this seat's own wording, read on the router."
  }
]
```
