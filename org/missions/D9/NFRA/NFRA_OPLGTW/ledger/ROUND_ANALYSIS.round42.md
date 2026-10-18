# NFRA_OPLGTW -- ROUND-42 ANALYSIS (L10 answer; the round-43 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-18 ~11:1xZ.
**Answers:** `2.0.0_SA_COO~O`'s slug, msg 35678, `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND42.md` @9592d0dcec.
**Issuer:** `2.0.0_SA_COO~O`.

## 1. As read

- **The round is terminal:** 12 of 12 (10 complete, 2 superseded); `round-close-check` reads MAY-CLOSE.
- **Two site Z releases are live and closed:**
  - **aa2efa2cf3** (batch8, 07:01:17Z): the absent-reason codes are in five client tools' notes, and the fee note claims only what
    is measured (Z-S385 is closed by the CVO on the served text).
  - **3b94a83e05** (batch9, 10:31:55Z): the loopback probe listener. ONE arming, then deleted and read ParameterNotFound.
- **The memory hazard is measured THROUGH THE SERVICE, the first time this project has done so.** All on the CTO half's bounds, which
  were fixed before the run:
  - **Z-S375 is disarmed:** etfs_compare_peers answered in the service; heap 134 -> 260 MB; one PID.
  - **Z-S338 is closed:** 12 pages; first page 1.7 s against a 15 s bound; median growth 1.65 MB against a 20 MB bound; max VmRSS
    392.1 MB against the 1200 MB CT3 ceiling.
  - The CVO owns the DISARMED rows.
- **dell1's harvest release 6575999df5 landed on the host at 10:52:49Z** (msg 35679), cut on 3b94a83e05 with 7 harvest paths.
  **Live is 6575999df5.** Its ledger CLOSED time is still pending.
- **Lineage:** site Z's releases through aa2efa2cf3 are on box/sitez (OG-ap-41, merge c5d520e0ac; measured by `merge-base`).
  3b94a83e05 and 6575999df5 are not yet on it.

## 2. Ruling -- a round-N analysis, no addendum

The endpoint is unchanged. Round 42 enriched the thread with a measured service-side memory read. Round 43 hardens the instrument
that made that read, and lands the trunk.

### Standing condition for every round-43 release

The base is the live ref at the GO. It is **6575999df5** today, not 3b94a83e05. Each release carries dell1's `harvest_research.py`,
`harvest_figures.py`, `harvest_identity.py` and `harvest_keys.py` unchanged, with the blobs read at 6575999df5 and named in the ask.
The ask's diff lists every path that differs from live and takes only its own.

### The round-43 enrichment list (the COO cuts it in ONE issuance; each build order carries at most three mechanical criteria)

1. **OG-pr-4: pin the lease's `firm`** (the CVO's finding on OG-ap-40, slug item 1).
   - The lease carries the firm.
   - The listener refuses any call whose account does not resolve to that firm, BEFORE the tool runs.
   - Criteria: a mismatched firm is refused with 403 `probe_firm_refused`; a matched one answers; a lease without `firm` is refused
     as malformed.
   - **No arming happens until this ships.**
2. **OG-sec-2: pin the Graph host in `graph.call`** (slug item 3).
   - Only `graph.microsoft.com`, plus the login host the token flow already uses.
   - Any other host raises before the request.
   - Criterion: a test with a forged next-link host is refused.
3. **OG-sec-3: complete the SSRF audit** (slug item 4).
   - Add the `PyJWKClient(` pattern, so the denominator is 20, not 18.
   - Re-run read-only. Any controllable target is a STOP and becomes its own row.
4. **OG-en-31: make `test_ogpr1_ac07` discriminate the connection reset** (slug item 7). It is a test-only cell and folds into the
   release in item 5.
5. **OG-ap-42: the ninth batched release**, carrying items 1, 2 and 4.
   - It sits on the live base (the standing condition above), under its own never-widen.
   - The CTO half will carry CT3's ceiling again for any armed probe.
6. **OG-ev-7: measure the peers call's 17.9 s** (Z-S389, slug item 2).
   - It runs AFTER item 5 is live, under ONE armed lease that pins the firm.
   - The run: two peers calls in the same service, back to back, then one with the heap signal off. Print the wall time and VmRSS
     of each.
   - It is a measurement, not a fix. Its bound is set in the cell before the run.
7. **OG-ev-8: measure the 82 inline audit-write sites** before any repair (slug item 5).
   - Read-only: per site, whether it runs on the event loop, its call frequency over the last 7 days of logs, and its timeout.
   - The repair is a round-44 decision, made on that table.
8. **OG-ap-43: land 3b94a83e05 and 6575999df5 on box/sitez** (slug item 8), in the shape of OG-ap-41.
   - Trunk's side on conflicts; AC3 lists every path that differs from live, each marked site-Z-own or dell1-own.
   - Then MSTR~Z tells dell1, which may cut from trunk again.
9. **OG-ev-9: a read-only trace of the per-identity limiter** (Z-S177).
   - This session's own opalgateway MCP connection failed with 429 `rate_limited` scope `identity`, so the hazard is live, not
     theoretical.
   - The trace reads the limiter's window, key and limit; the identities hitting it in the last 24 hours (counts only); and whether
     the MCP reconnect path retries into the same window.
   - The output is a table and a recommendation. No change.

### Not cut

- **Slug item 6, the proof-instance gate** (should it grade only the newest instance of an order?), is `0.0.0_AB_MSTR`'s gate.
  Routed to MSTR~Z, with no gateway cell.
- **Slug item 9, the fee-source completeness**, stays with the laptop CTO's probe (Z-S368/Z-S369).
- **Carried, each with what releases it:**
  - Z-W94-S2: dell2 IB-hm-5 plus the laptop reader grant;
  - Z-S313: when rows exist;
  - Z-S322/Z-S325: a named principal list.
