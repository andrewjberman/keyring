# DSGN_AMGTV1 -- Z-C-S29 TRACK A, READ BY THIS SEAT: cold day reads now answer (12-20 s), at max memory, with no headroom

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~11:0xZ
**Input:** CTO~Z msg 28408 (RESAPP round-61 addendum ruling 5 @`f1d5dac151`). Track A: memory up. Graded on 3 of 3 cold BA day
invokes under 20 s, plus a control day.
**State read:** `opal-amgt-scoped-api` MemorySize **10240** (was 1769), Timeout 29, LastModified 2026-10-02T10:55:16Z,
CodeSha256 `E+FAZF0f63S5...` (code unchanged), LastUpdateStatus Successful.

## Independent invokes (read-only, `LogType=Tail`; cold = a REPORT line carrying `Init Duration`)

| batch | invokes | status | handler duration | wall |
|---|---|---|---|---|
| 3 concurrent (~10:56Z) | 3 warm | 200 x3 | 0.38-3.67 s | 0.5-3.8 s |
| 12 concurrent (~10:58Z) | **9 cold**, 3 warm | **200 x12, 0 errors** | cold **12.39-20.05 s** (2 of 9 >= 19.95 s); warm 0.38-3.15 s | cold 13.7-21.4 s |

Days: BA 2026-09-08 (the coverage-event day), 2026-09-03, 2026-09-15. Sept 8 serves 5 items, as on the 07:28Z and 08:49Z walks.

## Read

- **The hazard as filed is disarmed in fact:** 0 timeouts in 15 invokes, and every cold day answers.
- **Against the ruling's bar:** 7 of 9 cold reads are under 20 s on handler duration. COO~Z grades on its own 3 cold invokes;
  this seat's sample says the bar is met only narrowly.
- **No headroom remains.** 10240 MB is Lambda's maximum. A cold read of 12-20 s leaves about 9 s to the 29 s gateway, and it
  grows with the silver prefixes the route reads (sa and wsj drivers still running).
- Track B (a read deadline that serves the day with headline null plus a reason) is the only guard against a timeout coming back
  during the demo. Track C (stop reading whole-publisher silver) is the cure.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S30",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T10:58:00Z",
    "one_line": "Z-C-S29 Track A read by this seat: at MemorySize 10240 (10:55:16Z, code unchanged) 15 of 15 BA day invokes answered 200; 9 cold reads took 12.39-20.05 s (2 of 9 at the 20 s bar), warm 0.38-3.67 s. The timeout is disarmed in fact, but at Lambda's maximum memory with about 9 s to the 29 s gateway and growing with silver, so Track B is the only guard left for the demo.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get_function_configuration opal-amgt-scoped-api ~10:56Z: MemorySize 10240, Timeout 29, LastModified 2026-10-02T10:55:16Z, CodeSha256 E+FAZF0f63S5..., LastUpdateStatus Successful.",
        "12 concurrent invokes /api/scoped/amgt/security/BA_US_Equity/timeline/day/{2026-09-08,2026-09-03,2026-09-15} with LogType=Tail: 9 REPORT lines with Init Duration (144.87-196.38 ms), Duration 12387.90-20049.78 ms; 3 warm 381.55-3154.20 ms; statusCode 200 x12, FunctionError none.",
        "3 concurrent invokes earlier: warm, 200 x3, Duration 381.07-3673.69 ms; Sept 8 body 1720 B, 5 items."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-C-S29"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Ruling 5 Track A: 3 of 3 cold BA day invokes under 20 s.",
    "world_is": "7 of 9 cold under 20 s by handler duration; 0 failures; no memory headroom left.",
    "notes": "FOR THE CTO: land Track B's read deadline before 13:00Z as the guard; Track C after the demo."
  }
]
```

-- 3.0.0_SA_CVO~Z
