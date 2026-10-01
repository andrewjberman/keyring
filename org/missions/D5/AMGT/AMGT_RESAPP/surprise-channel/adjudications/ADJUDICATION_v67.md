# AMGT_RESAPP ROUND 55 -- L8 COMPILE + L9 (the AMENDMENT 2 re-scope)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~06:2xZ
**Input:** `2.0.0_SA_COO~Z`'s `round55/DRAIN_END_PACKET.md` @`3bab99e4ae` (2,988 B, read to EOF), msg 27557.
**L7 re-measured:** `TO-AMGT-ae-1` and `TO-AMGT-ae-2` read `complete` on their LAST `<status>` tag.

---

## 1. L9 -- AMENDMENT 2 re-pointed AC1's served limb after a failure: **SOUND, with one bound**

**What changed** (`git diff 8e5e899de9 3bab99e4ae -- round55/checks/ae_1_posture.py`): only `serve()`. It read
`/security/{key}/posture` and now reads the `posture` field of `/security/{key}/overlay`, refusing a non-200. The comparison
(`/as_of`, `/verdict`, served against stored) and the AC1 expectation text are unchanged.

**Why it is sound:**
- **It is the page's carrier.** `portal/src/api/endpoints/amgt-lead-panel.ts:128` fetches `/security/{key}/overlay`; no
  `/posture` route exists. The original limb read a surface nobody serves.
- **Negative control (this seat, live):** `GET /api/scoped/amgt/security/KMB_US_Equity/posture` on the deployed function
  returns **404** `{"refused": true, "reason": "no /api/scoped/amgt route ..."}`. The original failure was the check, not the act.
- **Positive read (this seat, live):** the overlay's `posture` serves KMB `better` (the batch moved it from `hold`), BA `hold`
  and ASML `absent`, all status 200, matching the issuer's re-grade.
- **It is narrower in kind, not wider:** the new refusal on non-200 makes a transport failure a REFUSAL rather than a content
  mismatch. That is fail-closed.

**The bound.** The served `as_of` is the posture's evidence date. On KMB it reads 2026-09-16 both before and after the batch,
because the act rewrote the same key at a new VersionId. So the served comparison on (`as_of`, `verdict`) discriminates
"serves the new object" from "serves the old one" **only where the verdict moved: 1 of 12 targets (KMB)**. For the other 11, the
limb passes against a stale serve exactly as against a fresh one. That KMB served `better` evidences the read path (one function,
one carrier, one newest-object read for every key), which is a mechanism inference, not 12 measurements. This is the same gap
`Z-S324` names from the other side: nothing in AC1 reads a field the act always moves (`generated_at`, or the VersionId).

## 2. L8 -- the rest

- **ae-2 (LOCAL):** complete; `Z-S323` records that the drain's merge commit `52b8287a8b` is authored by `2.0.0_SA_COO~D`, not
  this round's issuer. Content is the issuer's; authorship is the peer's. INERT.
- **The vendor act:** Andrew's per-use word recorded @`17f29440e8`; 9 calls of 12 authorized (3 classed ABSENT make none),
  $0.9692.
- **NEVER-2 entry `20261001T0500Z` (AE~A):** L2 is left open pending the issuer's ACCEPT, which the packet gives; the entry closes
  at the executor's next act. Rollback (12 prior VersionIds) is in `ae1-pre/pre.json`. The open entry belongs to `0.7.0_AE_CloudOps~A`,
  not this seat.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S325` (ARMED: the served limb cannot pass; no `/posture` route) | **GRADUATED** | disarmed by `Z-S326`, and the disarm is verified: `/posture` 404, the overlay serves posture 200 with the moved verdict (section 1) |
| `Z-S326` (the disarm act) | **GRADUATED** | as above |
| `Z-S324` (AC1 never reads `generated_at`) | **CARRIED**, INERT | it is the section-1 bound; for the round-55 analysis |
| `Z-S323` (a peer committed this seat's drain merge) | **CARRIED**, INERT | authorship only |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S325` GRADUATED. **MET** (the NEVER-2 entry's L2 is open on its executor's
   act, not a channel row)
3. **Every judgment criterion graded:** the AMENDMENT 2 re-scope, SOUND with a bound. **MET**

## 5. FOR THE ROUND-55 ANALYSIS

A served limb that compares only fields the act may leave unchanged proves nothing on the names it does not move. A
served-read criterion should compare a field every write changes (a generation stamp or the object VersionId), with the pre-act
value printed beside it. That is the positive arm, and it also answers `Z-S324`.

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S437",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T06:20:00Z",
    "one_line": "L9 round 55: AMENDMENT 2's re-point of AC1's served limb (/posture non-route -> the overlay's posture field, the page's carrier) is SOUND -- live /posture 404, overlay 200 serving KMB 'better'; BOUND: the served compare (as_of, verdict) discriminates fresh from stale on 1 of 12 targets only (as_of is the evidence date, unchanged by the rewrite); Z-S325 disarm verified and graduated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AMGT-ae-1, ae-2 read 'complete' on their LAST <status> tag.",
        "git diff 8e5e899de9 3bab99e4ae -- round55/checks/ae_1_posture.py: only serve() changed (/posture -> /overlay .posture; non-200 raises REFUSED); compare fields /as_of, /verdict unchanged.",
        "portal/src/api/endpoints/amgt-lead-panel.ts:128 fetches ${BASE}/security/${key}/overlay.",
        "Live invoke opal-amgt-scoped-api via capture_lib: /security/KMB_US_Equity/posture -> 404 refused 'no /api/scoped/amgt route'; /security/{KMB,BA,ASML}/overlay -> 200, posture verdict better/hold/absent, KMB as_of 2026-09-16 (pre-batch as_of 2026-09-16 per ae1_AC1_regrade_amendment2.out object name)."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S325",
      "AMGT_RESAPP-Z-S326"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @3bab99e4ae asserts AMENDMENT 2 changes the carrier the limb reads and no expectation, and that the re-run against the deployed function reads YES with 12 of 12 moved.",
    "world_is": "True: the carrier is the page's and the expectation is unchanged; but the served limb's compare can tell a fresh serve from a stale one only on KMB, the one moved verdict.",
    "notes": "FOR THE ROUND-55 ANALYSIS: served-read criteria compare a field every write changes (generated_at or VersionId) with its pre-act value printed -- answers Z-S324."
  }
]
```
