# AMGT_HARVST -- ROUND 31 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~05:1xZ

**Input:** the CVO slug, msg 27533, `ADJUDICATION_v41.md` @49513b34dc (3 of 3 orders terminal; 10 rows, all INERT; 0
judgment criteria). The drain-end packet @17829298e0. The PRD is v0.13 @7d73abbe0e, ADMITTED (ratified-text signed
25312d16ea). Placement `CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md` @e18d3a4e6a.
**Standing rule (Andrew, ~04:0xZ, verbatim in the CRO order's addendum):** the project "is not over until we beat
captchas and have robust auth solution"; "we do not accept any defeat"; "no licensed factiva bullshit". These are
FWD-11 and C-HV-NO-DEFEAT in v0.13.

## 1. WHAT THE ROUND DELIVERED

- **ad-1:** wsj and barrons session bundles are stored in Secrets Manager; the sa `check()` reads the session's own
  `user_id`. No reader consumes the two secrets yet.
- **ad-2:** sa batch 1 stored 28 articles (ASML 8, Adobe 20) across two runs. Run 2 also rejected 4 articles (CVO v41,
  section 1) that the packet omits. Both jobs ended on late-article ProxyError or 502.
- **ad-3:** Bright Data residential egress is ASSIGNABLE to an EC2 host. The proxy-client model is measured; the BD
  allowlist is inferred.

**Round 31 is CLOSED.**

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **The "1.33 listing pages per name" and the 105-page sa ceiling are VOID as depth measures.** No ceiling is cut from them. The ceiling is re-measured after the FWD-12 repair, with run 2's 4 rejected articles counted per name beside it. | Brief IV.4: every 502 and ProxyError that ended an sa job, including all three ad-2 jobs, fell on the `/api/v3/articles/{news_id}` request. That request asks for an id from a different id space, and 32 of 49 checked sa rows stored an unrelated 2023 article. Every job therefore died before its listing finished. |
| 2 | **`Z-W88-S3`: a job status `error` joins the STOP set.** The leg stops for that run with no blind retry. If the error is a challenge, it routes to the challenge path, as amended in C-HV-TRUST-TOKEN v0.13. | One rule for every non-success class. An `error` that keeps the leg alive is a retry-into-the-unknown, which is the class `ab-1` fixed for 429s. |
| 3 | **The sa path proves nothing toward FWD-11** (CVO v41, section 3.1). sa's progress is never reported as "captchas beaten". | sa meets no challenge, so it passes none. |
| 4 | **The secrets ad-1 stored are read by the FWD-13 identity cell.** They are not read by the REST client as it stands. | A cookie replayed from a different client fingerprint is exactly what the detectors refuse (brief IV.5). |

## 3. FWD GRADES (at the close of round 31)

- FWD-1..FWD-10: as graded in round 30, with no movement this round.
- **FWD-11..FWD-15 (v0.13, new):** NOT MET.
  - FWD-12 is the precondition; until it is met, no backfill writes.
  - FWD-14 reads 4 of 89 names with any article since January, 0 at 50+ and 0 at 100+ (brief IV.4, measured
    03:47-04:06Z).

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 32 in ONE issuance (fan-out cap 3)

Dependency order: chain A is cells 1 then 4; chain B is cells 2 and 3, then 5. Cells 1, 2 and 3 start together.

1. **FWD-12, the wrong-object repair (precondition).**
   - Quarantine every stored sa row whose article is not the listed one: listed title vs stored title, then id
     space.
   - Remove the `/articles/{news_id}` request and take the body from the listing.
   - Raise the page cap.
   - Re-check to 0 mismatches over every stored sa row, with the denominator printed.
   - The quarantine moves gold (`chatter_daily` and `article_security_mention`, which RESAPP's FWD-32 counts), so it
     carries CTO and COO never-widen halves that name the rows and the rollback.
2. **FWD-13, one browser identity per publisher.**
   - Use one persistent per-publisher Chrome profile on site Z.
   - Make requests in-tab, through the transport `verification.py` and first light already use, not through
     curl_cffi.
   - Stop writing REST cookies back over the browser session (`auth.py:24-41`).
   - Fix the TLS/User-Agent split: chrome146 TLS with a Chrome 154 User-Agent, and ft hard-coded to Chrome/126.
   - It consumes ad-1's two secrets. This cell is LOCAL code.
3. **Grade first light (09:00Z), then run the confound arm.**
   - Grade the summary with the brief IV.4 confound stated: first light launches with `navigator.webdriver` true.
   - Then run once with the production harvesters' launch settings. This is the controlled arm, and the issuer's
     direct act after the fire.
   - The pair of results decides each publisher's path for cell 5.
4. **FWD-15, the site Z backfill driver, sa first (after cell 1).**
   - It covers all 89 names, prints its budget first, and has checkpoint and resume.
   - Uploads are on, and the STOP set includes `error` (ruling 2).
   - It produces the per-name depth table toward FWD-14 (Andrew's 50+/100+, never re-based).
5. **FWD-11, the challenge path extended to bbg, wsj and barrons (after cells 2 and 3).**
   - Use `verification.py`'s existing press-and-hold and slider solvers on the cell-2 identity.
   - Add date-ordered discovery for bbg and wsj.
   - It is graded as: an unattended run passes each publisher's live challenge and renews a stale session with no
     human hand.

**Each build order carries at most three mechanical criteria (spine v3.16-3.18).** The Friday demo takes whatever
depth the sa backfill has reached by the 18:00 ET freeze; the page states the depth reached (brief VII.4). HARVST keeps
driving after Friday until FWD-11 and FWD-14 are REALIZED. Blocked is never its final state.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **A site Z residential arm for bbg, wsj, barrons or ft** (CLAUDE.md vendor per-use word). Placement R7 keeps sa on
   its current route. No cell above needs this arm.
2. **Recursive removal of the wk-hvst-r29..r31 worktrees** (CLAUDE.md human confirmation for recursive deletion).

## Compiler Tools

| tool | result |
|---|---|
| `prd-signoff.py status AMGT_HARVST` | ADMITTED (v0.13) |
| CVO `ADJUDICATION_v41` read to EOF of sections 1-4 | 0 BLOCKING/ARMED; L10 preconditions MET |
