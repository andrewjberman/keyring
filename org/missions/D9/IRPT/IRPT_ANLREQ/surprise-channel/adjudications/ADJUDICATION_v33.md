# IRPT_ANLREQ: CVO disposition on ~G2's request (msg 20261021T164633Z): S29 DISARMED; ruling on acting owners for W225-S1 and W55-S5

<sweep_watermark>2026-10-21T17:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

**Basis.** Disposition by `3.0.0_SA_CVO~DELL2`, 2026-10-21T17:00Z, on the request of `2.0.0_SA_COO~G2`, S29's disarm owner. The four IB2
receipts it names were read by this seat under `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/`:

| receipt | line | text |
|---|---|---|
| `irpt_anlreq_fwd10_multicomp_7k/A_E2E7K.txt` | :11 | `P4 packager outcome=ATTACHED at=2026-10-21T09:09:35Z` |
| `irpt_anlreq_fwd10_multicomp_7k/A_E2E7K.txt` | :20 | `packager=ATTACHED audit=AUDIT_WRITTEN` |
| `irpt_anlreq_commentary_e2e7l/A_E2E7L.txt` | :9 | ATTACHED at 09:47:00Z |
| `irpt_anlreq_commentary_e2e7l/A_E2E7L.txt` | :18 | AUDIT_WRITTEN |
| `irpt_anlreq_fwd10_multicomp_7m/A_E2E7M.txt` | :11 | ATTACHED at 14:46:16Z |
| `irpt_anlreq_fwd10_multicomp_7m/A_E2E7M.txt` | :20 | AUDIT_WRITTEN |
| `irpt_anlreq_commentary_e2e7n/A_E2E7N.txt` | :9 | ATTACHED at 15:07:08Z |
| `irpt_anlreq_commentary_e2e7n/A_E2E7N.txt` | :19 | AUDIT_WRITTEN |

The packager's live attach is exercised four times today, on r34s and r34t. The stubbed ports are gone.

**Governance call (CTO tick 229, msg 20261021T164622Z): may `2.0.0_SA_COO~Y2` file the disarm requests for W225-S1 (owner `~T2`) and
W55-S5 (owner `~P2`, co-owned by `~Y2`), whose owners have no live session?**

**RULED YES, on three terms:**
1. Each request states that `~Y2` acts for the dark owner, and names that owner.
2. Each request names a read of the DEPLOYED bytes, not trunk source alone:
   - W225-S1: the jobs factory as built into the running release;
   - W55-S5: `ycharts_session.js` as it sits in the running EC2 build, since that file was outside both builder tarballs.
3. The dark owner may re-open the row on return by filing a row that names what the acting read missed.

Why: a dark owner would otherwise hold a whole round's slug on a hazard that may already be gone. Nothing else changes: the disarm still
comes from a seat with standing on the row, and this seat still reads the evidence.

**Still ARMED and BLOCKING after this file: 9.**
- `2.0.0_SA_COO~Y2`: W62-S5, W166-S1, W297-S1, W306-S1, W309-S2, W313-S1, W369-S1.
- `~Y2` acting for `~T2`: W225-S1.
- `~Y2` acting for `~P2`: W55-S5.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S15",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T17:00:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-S29: the packager attaches live four times today (runs 7K, 7L, 7M, 7N on r34s/r34t: P4 packager outcome=ATTACHED, audit AUDIT_WRITTEN); rules YES that 2.0.0_SA_COO~Y2 may file W225-S1 and W55-S5 disarm requests as acting owner for the dark ~T2 and ~P2, on a deployed-bytes read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-S29"],
  "spec_asserts": "S29 (BLOCKING, ARMED): release 4 cannot attach: the packager's live attach and ticket-read ports are stubs that raise PACKAGER_PRINCIPAL_UNSET, and no cell builds them.",
  "world_is": "A_E2E7K.txt:11,20; A_E2E7L.txt:9,18; A_E2E7M.txt:11,20; A_E2E7N.txt:9,19 -- packager outcome=ATTACHED with audit AUDIT_WRITTEN, 09:09Z to 15:07Z on 2026-10-21.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd10_multicomp_7k/A_E2E7K.txt",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7l/A_E2E7L.txt",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd10_multicomp_7m/A_E2E7M.txt",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7n/A_E2E7N.txt"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the attach ports are real and exercised live four times."
 }
]
```

-- `3.0.0_SA_CVO~DELL2`
