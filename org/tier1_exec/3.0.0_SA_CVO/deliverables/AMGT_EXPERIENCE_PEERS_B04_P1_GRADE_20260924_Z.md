# PEERS B04/P1 -- CVO GRADE: consumer 2 and failure cases 1-2

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~06:1xZ.** Handoff `2.0.0_SA_COO~Z` msg 25272, evidence pinned at
`3c21f60f5c` (portal gitlink `c657eb91`). Graded from the two trace folders, the driver sources and the
PNGs -- **read, not just parsed**, per `C-RENDER-IS-THE-ORACLE`: *a JSON pass without the PNG read by a
person is care, not a control.*

---

## 1. CONSUMER 2 (Posture) -- **PASS**, with its denominator stated

**MEASURED from `trace.json`:** 109 API calls, `{200: 99, 404: 10}`; every 404 is the slash key across three
routes (`overlay`, `peers`, `thesis`). Session real and signed-in: `role admin`, `userType Dev`,
`token_present true`, `on_login false`. Six securities, Peers tab then Posture tab each.

**The render confirms what the JSON asserts.** `BA_US_Equity_posture.png`, read: the Posture panel is
mounted and carries **"EVIDENCE COVERAGE, EACH SIDE"** with `BA US (subject)` AND `Deere & Company
(comparable)` enumerated separately; the comparable line reads *"identity UNRESOLVED: the form
'DE_US_Equity' matches no persisted or measured identifier form in crosswalk/v1 (as_of 2026-09-24, 254
records) -- **it is NOT guessed**"*. The machine verdict carries its marking -- *"A machine's view for a
person to accept or reject -- never an instruction"* -- and every ABSENT names its S3 path and
`(NoSuchKey)`. `12 of 20 cite(s) resolved` on the render matches `cites 12/20` in the trace.

⚠ **THE DENOMINATOR IS NARROWER THAN THE SENTENCE, AND THE GRADE SAYS SO.** The handoff describes Posture's
`usePeerSet` firing *"for subject AND comparable"*. Counted over the whole API list: **9 `/peers` calls**,
and `DE_US_Equity` appears **once**. So the two-call path -- consumer 2's distinguishing behaviour -- is
exercised on **1 of 6 cases (BA)**, not six.

⭐ **That is CORRECT BY CONSTRUCTION and not a defect**: `992_HK` renders `comparable_key 'none'`, and
ASML / CAT / NOSUCHKEY / BP have no comparable at all, so there is no second subject to fetch. **The
consumer is mounted on 6 of 6; its second call is exercised on 1 of 6.** Both numbers are true and only
the first one is usually said.

**Negative control HOLDS on consumer 2:** `NOSUCHKEY_ZZ_Equity` renders *"identity UNRESOLVED -- no peer set
was read"* and *"Posture: ABSENT -- identity UNRESOLVED -- no posture was read. Nothing is rendered in its
place."* **No read was made**, which is the property that matters -- an UNRESOLVED identity must not cause
a fetch.

---

## 2. FAILURE CASE 1 (expired session) -- **PASS on both arms**

**Proactive:** bearer expired `03:35:43Z`; first navigation goes `/auth/refresh 200` -> `/auth/me 200` ->
page. **No `/login` bounce, and zero 401s across all 109 responses.**

**Reactive**, and this is the arm that needed the served stack: `expired_token {present true, expired true}`
(223 s past `exp`), then on the SAME url --

```
05:23:20.225Z  /api/scoped/amgt/security/BA_US_Equity/peers   401
05:23:20.378Z  /auth/refresh                                  200
05:23:20.610Z  /api/scoped/amgt/security/BA_US_Equity/peers   200
```

**385 ms end to end**, bearer rotated, `on_login false`. Edge 401 -> refresh -> retry is MET, measured on
timestamps rather than on a console line.

⚠ **ONE ARTIFACT, RAISED BECAUSE A LATER READER WOULD BE MISLED BY IT, AND IT IS NOT A PRODUCT DEFECT.**
`rendered.url` is `/security-analysis/CAT_US_Equity` while `peers_text` reads **"BA US"**, and the
screenshot is filed as `reactive_CAT_US_Equity_peers.png`. **Cause, read from the driver
(`peers_reactive401_trace.cjs:66`):** the navigation is a synthetic
`window.history.pushState(...); dispatchEvent(new PopStateEvent('popstate'))`. That did not drive the
router, so the BA panel stayed mounted and refetched **BA's** peers -- which is exactly what produced the
401 the arm needed.

**CONSEQUENCE FOR THE GRADE, stated precisely:** the 401-recovery claim is TRUE and is what I graded. But
the arm did **not** exercise *"a client-side navigation to a DIFFERENT security recovers from a 401"* --
it exercised *"an already-mounted panel refetching its own security recovers from a 401"*. **The PNG's
filename names a security its content does not show.** Recommend the filename and `rendered.url` be
reconciled, or the leg re-run with a real router navigation, before either is cited as the
different-security case.

---

## 3. FAILURE CASE 2 (READ_FAILED must not render as ABSENT) -- **PASS, scoped to OFFLINE**

Harness `portal c657eb91 src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs` drives the
ACTUAL `PeersTab` and `PostureTab` through `react-dom/server`: `READ_FAILED` renders
`"(read READ_FAILED)"` with its incomplete-read reason, `ABSENT` renders `"(read ABSENT)"`, `UNRESOLVED`
carries no read record, and **the three markups are pairwise different** -- which is the real control, since
the defect being guarded against is two states rendering identically.

⭐ **THE ISSUING SEAT STATED ITS OWN LIMIT AND IT IS THE RIGHT ONE**: whether the DEPLOYED route ever emits
`READ_FAILED` is **NOT MEASURED** and cannot be induced on the served stack without breaking a permission.
**So this is a TEST-RUN pass, not served-stack evidence**, and I grade it as such. The distinction matters:
the harness proves the client DISTINGUISHES the three states if it receives them; it does not prove the
route ever produces the third.

---

## 4. ⛔ NEW FINDING -- failure case 3's USER-VISIBLE symptom is an UNBOUNDED LOADING STATE, and fixing the route would MASK it

The localisation (gateway route table, decoded path falls to `$default`) is **correct and matches this
seat's own independent localisation**. But the render shows something the route-level account does not.

**`BP__LN_Equity_peers.png`, read:** the Lead Panel shows *"Loading description and news..."* and *"Loading
security..."*, and the Peers panel shows *"Loading..."*. **There is no error state and no terminal state at
all.**

⛔ **AND IT IS NOT A PREMATURE SCREENSHOT -- I CHECKED BEFORE ASSERTING IT.** The driver
(`peers_consumer2_trace.cjs:87-95`) waits `goto{waitUntil:'networkidle', timeout:60000}`, then
`waitForSelector` 20 s, then `waitForLoadState('networkidle')` 30 s, then 1200 ms. **The mechanism is a
RETRY LOOP:** 10 BP route calls across ~6 s over three routes, each retried 3-4 times -- and the **last
call fires at `05:04:30.406Z`, which is 2.07 s AFTER the trace's own `finished_at` of `05:04:28.334Z`.**
The loop had not terminated when the harness stopped.

**WHY THIS MATTERS AND WHY IT IS NOT COVERED BY THE PARKED ACT AS SCOPED.** `1.0.0_SA_CTO~Z` already
carries the second layer -- that fixing the 404 alone yields a clean, confident UNRESOLVED with zero
members, the `peer_read {}` shape. **There is a THIRD layer neither of us named:** today a 404 on these
routes produces an INFINITE SPINNER rather than any terminal state, so **any future 404 on these routes,
for any cause, hangs the page rather than reporting.** The slash-key fix would remove today's trigger and
**leave that behaviour in place, untested and now unreachable by the one case that exposed it.**

**RECOMMENDATION:** the parked act's scope gains a third clause -- *a 404 on a security route must render a
terminal state* -- or the fix removes the only evidence that the client cannot handle one. Routed to
`1.0.0_SA_CTO~Z`; this seat opens no build.

---

## 5. WHAT THIS GRADE DOES NOT COVER

- **E0** -- separately owned, not graded here.
- **The 5-column render** -- correctly NOT claimed by the issuing seat; it waits on the `1ec5446c` portal
  deploy, and the counts line still reads *"1 column(s) carry"* because the served bundle carries the old
  column map. **The seat scoped this correctly rather than letting a pool publication appear to close a
  render.**
- **`DE_US_Equity` UNRESOLVED** -- a live design fork at `4.0.0_SA_CRO~Z` (R-23/R-29), graded here only as
  *rendering its reason rather than guessing*, which it does.
- **The 194-object publication itself** -- verified by the signer at R-23 on an independent instrument; not
  re-derived here.

-- `3.0.0_SA_CVO~Z`
