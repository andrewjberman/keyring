# NFRA_OPLGTW -- the disarm clock for Z-S312, and the slug debts the row gate names (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v39. Fabric: site-z. Recorded: 2026-10-17 ~05:0xZ.

**Input:** `2.0.0_SA_COO~O` msg 35372 (acked). It carries the disarm owner's word for `NFRA_OPLGTW-Z-S312`, the owner's ruling row
`Z-S351`, and the record `org/tier1_exec/2.0.0_SA_COO~MP/deliverables/ANDREW_DIRECT_20261017_044xZ_THREE_ROUTES_CLEAR_GO_MP_V_2.md`.
Andrew's answer there is verbatim: "they are all clear + go". The CVO writes the clock (R-15).

**What the word covers, stated as recorded, neither wider nor narrower:**
- Andrew opened `/sprint`, `/rivalfunds` and `/yearinreview` on his own account and answered "clear", without per-route codes.
- `/login`, the fourth route of Z-S312, was not named. Reaching the three pages signed in passes through it.
- The second owner principal in Z-S312 (the Opal Bloomberg identity) was not browser-run. Its `email_deny` record was deleted by
  OG-ap-30, read by this seat in v36 (`email_deny` total 1).
- The owner disarms on this word. That call is the owner's, and this seat does not adjudicate it narrower. The unexercised arms
  are recorded so a later reader does not count them as exercised.

The v20 row `NFRA_OPLGTW-Z-S312` is superseded in place (DISARMED, REMEDIATED, closed).

**Slug debts in the same commit:** two BLOCKING ARMED items, Z-S336 and Z-S338, are dispositioned GRADUATED by
`adjudications/ADJUDICATION_v39.Z.md` (Z-C-S88). Their remediation rows are below; each stays ARMED with its owner's clock.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S87",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S312 (the owners refused on the email-only browser routes by C2's email_deny) was held ARMED by its owner until Andrew's own browser run; the run reads clear.",
    "evidence": [
      "2.0.0_SA_COO~O msg 35372 (the disarm owner's word)",
      "investigations/INVESTIGATION_v1.md row NFRA_OPLGTW-Z-S351 (the owner's ruling)",
      "org/tier1_exec/2.0.0_SA_COO~MP/deliverables/ANDREW_DIRECT_20261017_044xZ_THREE_ROUTES_CLEAR_GO_MP_V_2.md (verbatim: they are all clear + go)",
      "adjudications/ADJUDICATION_v36.Z.md (OG-ap-30: the two owner records deleted) and ADJUDICATION_v37.Z.md (OG-ap-31 e4)"
    ],
    "remedy": "OG-ap-30 deleted the two owner email_deny records; OG-ap-31 shipped the route-class exemption; Andrew's browser run reads clear on /sprint, /rivalfunds and /yearinreview. Not exercised: /login by name, and the Opal Bloomberg identity in a browser.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v39",
    "disarms": [
      "NFRA_OPLGTW-Z-S312"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-17T04:49:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v39"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S336",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Another seat's release (319c9413a2, three harvest files) moved the live gateway ref between OG-ap-32's Phase A reads; a release cut on the older ref would have reverted those files on deploy.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S336 and the owner's ruling row Z-S337 (option B)",
      "deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-ap-34.md section 1 (sha256 bdccc464670ea801): the three harvest files are live and equal to trunk's"
    ],
    "remedy": "Option B cut OG-ap-32 on the declared live base with the three files taken from trunk; the wrapper's stale-base guard refuses a moved ref; OG-ap-34 is cut on the live ref d3ae88be46. Disarm on the owner's word.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v39",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-17T07:57:24Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v39"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S338",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "OG-ap-32's paged read retained 110 to 165 MB per page (host 87.1 percent at page 4); the cause is glibc per-thread arenas under the per-page thread pool (OG-ev-4, ruled in Z-S343).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S338, Z-S342, Z-S343",
      "deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-ap-34.md section 2 (MEM_GATE.json: median page growth -10.4 MB over pages 2 to 4, fresh process)",
      "deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-34_20261017.md (signed; Amendment 1)"
    ],
    "remedy": "OG-en-20 (mallopt M_ARENA_MAX 2, 8 read workers) in release 9d5b712557 (OG-ap-34, all three halves signed). Disarm when OG-ap-34 Phase B holds memory inside CT1 (a): the 12-page fresh-process chain and the 30-minute service read-back. A zero window-call read-back leaves the service-process claim ABSENT.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v39",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-18T10:53:32Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v39"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
