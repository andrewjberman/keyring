# INCIDENT REMEDIATION -- WHAT THE NO-SPAN GAP ADMITTED

**`3.0.0_SA_CVO~Z`, 2026-09-23 ~22:3xZ.** The **SECOND half of the double remedy**. C4 discharged the
first half -- the guard is built, deployed and exercised. This measures what the gap admitted while it
was open, which Rule 22's negative mirror requires of an **INCIDENT** and which a green deploy makes
easy to skip.

## HEADLINE

**The gap WAS exercised-against -- so `ADJUDICATION_v45`'s INCIDENT classification is CONFIRMED, not
downgraded. But the reach is FIVE served responses, on ONE security, to ONE distinct client IP** --
not 179 sentences across a broad served audience.

| | |
|---|---|
| Window measured | **2026-09-19T00:00Z -> 2026-09-23T21:58Z** (the rk-41 window, to the cutover) |
| Instrument | **CloudFront access logs**, `s3://opal-data-security/waf-logs/cloudfront-access/`, 664 hourly files |
| Parser positive control | **19,114 log rows parsed** -- non-zero, so a zero below is absence and not a broken parser |
| `/api/scoped/amgt*` requests | **521** -- **423 refused 401**, 98 served |
| Responses that could carry no-span prose | **5** |
| Distinct client IPs among them | **1** |

## 1. THE SERVED SURFACE, BY SUB-ROUTE

| sub-route | 401 (refused, served nothing) | 200 (served) |
|---|---|---|
| `/thesis` | 114 | **21** |
| `/overlay` | 78 | **17** |
| `/peers` | 16 | 6 |

⭐ **423 of 521 AMGT requests were refused 401 at the edge and served nothing at all.** The
`auth-validator-edge` gate did most of the work of containing this.

## 2. THE INTERSECTION THAT BOUNDS THE BLAST RADIUS

**A thesis or overlay response can only carry a no-span sentence if the security has drafted sections
at all** -- i.e. if it is one of the **12 objects under `drafting/v1/`** (the complete set, measured
during C4). Intersecting the served responses with that corpus:

| security served on `/thesis` | responses | in the drafting corpus? |
|---|---|---|
| `Lenovo` | 12 | **no** -- no drafted sections exist |
| `992_HK_Equity` | 4 | **no** |
| `BA_US_Equity` | **4** | ⛔ **YES** |
| `DE_US_Equity` | 1 | **no** |

**So 17 of the 21 served thesis responses carried NO drafted prose whatsoever** and could not have
served a no-span sentence. **Four could.** On `/overlay`, **1 of 17** served responses was on an
in-corpus security.

**THE FOUR THESIS RESPONSES, in full:**

```
2026-09-22 19:15:35  BA_US_Equity  108.242.96.89
2026-09-22 20:14:11  BA_US_Equity  108.242.96.89
2026-09-22 20:21:40  BA_US_Equity  108.242.96.89
2026-09-23 20:44:34  BA_US_Equity  108.242.96.89
```

**`BA_US_Equity` holds 21 no-span sentences on today's corpus** (measured in C4). So the gap admitted
**at most ~21 no-span sentences, repeated across 4 responses, to a single client**, plus one overlay
response whose drafted-prose path is the description fallback.

## 3. WHAT THIS DOES AND DOES NOT CHANGE ABOUT THE ADJUDICATION

- ⛔ **INCIDENT stands.** The guard was missing AND the gap was exercised. This is not re-classified to
  exposure, and the double remedy was correctly owed.
- ⚠ **`ADJUDICATION_v46`'s upward blast-radius amendment is NOT contradicted** -- the audience was a
  real authenticated browser session, served-class rather than engineering-class, exactly as v46 says.
  **What is now measured is the REACH, which v46 did not quantify: 5 responses, 1 security, 1 IP.**
- ⭐ **The figure "179 sentences served" describes the DEFECT'S CAPACITY, not its realised reach.** 179
  is what the corpus would have served had every security been requested; **only `BA_US_Equity` ever
  was.** Both numbers are true about different things, and a remediation that conflated them would
  re-open eleven securities' worth of work that nothing ever touched.

## 4. LIMITS, STATED RATHER THAN IMPLIED

- ⛔ **WINDOW: 2026-09-19 to the cutover ONLY.** The no-span defect existed in every build before the
  repair, and the artifact history reaches back to **2026-09-15** (30 versions). **Requests before
  09-19 are NOT measured here** -- and they ARE measurable by this same method, since the CloudFront
  logs run back to **2026-09-03**. Widening the window is one re-run, not new instrumentation.
- ⛔ **AN IP IS NOT AN IDENTITY.** One distinct client IP is reported. This seat does **not** name who
  it was, and the access log carries no firm id -- **the firm header is injected by
  `auth-validator-edge` downstream of the log**, so per-firm attribution is unavailable from this
  instrument and no other instrument in the estate carries it (API Gateway access logging is **not
  declared**; the Lambda log carries only `START`/`END`/`REPORT` plus 28 error lines, with **no route
  and no firm** on a successful request).
- ⚠ **RESPONSE BODIES WERE NOT CAPTURED.** "Could carry no-span prose" is inferred from **corpus
  membership today**; the drafting corpus on 2026-09-22 is not re-measurable, so the per-response
  sentence count is an upper bound rather than a reading.
- The overlay's drafted-prose path is the description fallback, which **reads `ABSENT` today**;
  what it returned on 09-21 is not recoverable.

## 5. WHAT THIS SEAT RECOMMENDS AS THE REMEDIATION ACT

**Given the measured reach, the proportionate remedy is small and this seat says so rather than
inflating it:**

1. **No re-processing of the eleven untouched securities.** Nothing ever served them. Re-opening them
   would be the "re-opening work nothing ever harmed" failure the negative-mirror rule names
   explicitly.
2. **`BA_US_Equity` is the only security with realised exposure**, across 4 responses in a ~25-hour
   span, to one client. **Whether that warrants a notification is ANDREW'S CALL, not this seat's** --
   it turns on who the client was, which this seat cannot determine and will not guess.
3. **If the window is to be widened past 09-19**, it is one re-run of this method over the earlier
   log files, and this seat will run it on request.

⛔ **THIS DOCUMENT CLOSES THE MEASUREMENT, NOT THE INCIDENT.** The incident closes when the remediation
act -- whatever Andrew decides it is -- is done and recorded. **Closing the guard and closing the
incident are two different facts, and only the first plus this measurement are now true.**

## 6. ONE THING FOUND OFF-TASK, FILED NOT CHASED

The Lambda log carries **28 unhandled exceptions** in the window -- `ModuleNotFoundError: No module
named 'lib.opal_naming'` and `TypeError: '<' not supported between instances of 'int' and ...` --
each returning a 500 with a fixed body. **This is unrelated to the no-span repair and is not chased
here**; it is filed as a surprise row per CLAUDE.md s.2.
