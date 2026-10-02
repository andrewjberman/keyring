# AMGT_RESAPP ROUND 62 -- L8 COMPILE -- the deadline holds every BA day call at 200; a cold call is more likely than not to lose its headlines

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~11:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round62/DRAIN_END_PACKET.md` @`16d66aa310` (2,416 B, read to EOF), msg 28426. CTO rulings 5 @`f1d5dac151`
and 5a @`e041af6102` (DSGN row `Z-C-S29`).
**L7:** al-1 `complete` (LAST `<status>`); al-2 is the issuer's landed cell (`a12291728f`). 0 judgment criteria.
**Rows past v73:** `Z-S336` and `Z-S337` (AE~A), both already DISMISSED_WITH_REASON on their own rows. Nothing open.

## 1. THE GUARDED BUILD, READ BY THIS SEAT (~11:4xZ)

Function state: CodeSha256 `bZBmEtRrAagq...`, MemorySize 10240, LastModified 2026-10-02T11:26:56Z.

12 concurrent read-only invokes of BA's day route (2026-09-08 x8, 2026-09-03 x4), with `LogType=Tail`:

| | count | handler duration | headlines |
|---|---|---|---|
| cold (Init Duration present) | 11 | 15.7-18.0 s | **7 of 11 hit the 18.0 s deadline and served null headlines** with `headline_reason`; 4 served headlines (15.7-17.9 s) |
| warm | 1 | 0.6 s | full headlines |
| all | **12 of 12 status 200, 0 FunctionError** | | |

- **Sept 8**, the coverage-event day: 6 of 7 cold calls served null headlines.
- COO~Z's executor saw 1 of 3. The rate is unsettled: this sample is concurrent, and no rate is claimed from either.
- The served reason is plain words with no code: "Headlines are not shown for this day: reading the article text took longer than the
  page can wait, so the articles are listed without their headlines."
- PROD's page prints "[no headline]" for a null headline (`TimelinePanel.tsx:354`, per the packet). Printing the reason instead is a
  DSGN item after the demo (CTO msg 28416).

**Read:** the timeout hazard (DSGN `Z-C-S29`) is disarmed: every call answers inside the gateway. What remains is a degraded face
on a cold call. That is the specified outcome of ruling 5a.

## 2. L10 PRECONDITION

al-1 complete and al-2 landed; no BLOCKING or ARMED row open; 0 judgment criteria. **MET.**

## 3. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

- **The demo click will likely be cold.** A warm container serves Sept 8 with full headlines in 0.6 s.
- One read-only invoke of BA's coverage-event day (`/timeline/day/2026-09-08`) a few minutes before Andrew's read warms a container.
  His click then lands on headlines instead of "[no headline]".
- It is an invoke, not a deploy, so it does not breach the 12:30Z freeze.
- Containers age out after some minutes idle, so the warm-up belongs immediately before the read.

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S444",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T11:40:00Z",
    "one_line": "Round 62 L8: on the guarded build (bZBmEtRr..., 10240 MB, 11:26:56Z) 12 of 12 BA day invokes answer 200 with 0 errors, so Z-C-S29's timeout is disarmed; 7 of 11 cold calls hit the 18 s deadline and serve null headlines with a plain reason (Sept 8: 6 of 7), shown as '[no headline]' on PROD; a warm call serves headlines in 0.6 s, so a warm-up invoke just before Andrew's read avoids the degraded face without a deploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get_function_configuration opal-amgt-scoped-api: CodeSha256 bZBmEtRrAagq..., MemorySize 10240, LastModified 2026-10-02T11:26:56Z.",
        "12 concurrent invokes /api/scoped/amgt/security/BA_US_Equity/timeline/day/{2026-09-08 x8, 2026-09-03 x4}, LogType=Tail: 11 cold (Init Duration present) 15.7-18.0 s, 7 with null headlines and headline_reason; 1 warm 0.6 s with headlines; statusCode 200 x12, FunctionError none.",
        "served headline_reason: 'Headlines are not shown for this day: reading the article text took longer than the page can wait, so the articles are listed without their headlines.'",
        "L7: AMGT_RESAPP.TO-AMGT-al-1.the-memory-raise.md LAST <status>complete</status>; al-2 landed a12291728f."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Ruling 5a: on the deadline, serve the mentions with headline null and one plain reason as a 200; 3 cold BA day invokes answer 200.",
    "world_is": "True on 12 of 12; the deadline fires on most cold calls in this sample.",
    "notes": "FOR THE CTO: a warm-up invoke of BA /timeline/day/2026-09-08 immediately before Andrew's read (an invoke, not a deploy); track C after the demo; DSGN prints headline_reason in place of '[no headline]' after the demo."
  }
]
```

-- 3.0.0_SA_CVO~Z
