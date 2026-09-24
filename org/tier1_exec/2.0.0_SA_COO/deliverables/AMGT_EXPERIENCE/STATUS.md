# AMGT EXPERIENCE + SERVED RUNTIME

Seat `2.0.0_SA_COO~Z` (Claude session from 2026-09-24 04:38Z, successor of the 02:40Z session). Thread: Peers B04/P1,
mandate `AMGT_COMPLETION_20260923/COO_Z_PEERS.md` @`7b26e2ac1c`. Reviewer `3.0.0_SA_CVO~Z`. Andrew ~04:3xZ (CTO
record `HANDBACK_TO_CANONICAL_20260924.md` @`ad5c7a75c6`, msg 25253): AMGT_RESAPP returns to canonical rounds with
this seat named; the closer items in flight finish under their own spec (Rule 27) and are listed below.

## Pins and write claims

- Worktree `C:/tmp/closer-amgt-peers-z-20260924`, branch `closer/amgt-peers-z-20260924` off CLOUD `7b26e2ac1c`, NOT
  merged (MSTR's drain); portal nested worktree on the same branch name off DEV `c1ac41ec`. Trunk `CLOUD`; MSTR pushes.
- Source on this thread: `lib/research/identity/crosswalk.py` (+schema), `lib/research/peers/engine.py`,
  `lib/research/peers/universe.py`, two test files; portal `cscTable.ts`, `PeersTab.tsx`, `types.ts`, harnesses
  `__harness__/peersCarry.harness.cjs` and `__harness__/peersReadFailed.harness.cjs`. Identity + peers suites 109
  passed; both harnesses PASS.

## The four steps -- DONE, published 03:33Z, route/data layer graded PASS

1. **Live thread (E0) REACHED** 03:12Z on the served stack under Andrew's admin+Dev identity (no `/market` redirect).
   Evidence `PEERS_LIVE_TRACE_20260924T0320Z/` (before) and `_0335Z/` (after the act).
2. **One key space:** `universe/v1` is the second registration source; crosswalk MEASURED 36 -> 194; `resolve()` over
   the 191 prior pool keys = 191 MEASURED on the live object.
3. **Present columns carried:** producer copies `price`/`ev`/`ey`; frontend map + NTM-grain P/E. Offline harness PASS;
   the SERVED bundle still renders "1 column(s) carry" until portal `1ec5446c` deploys (MSTR merge + DEV/PROD).
4. **Owner + trigger:** batch 194 = crosswalk 194, derived 145 / absent 49; trigger stated; owner this seat.

**Act:** both never-widen halves (COO @`4c7d0b2e7c`, CTO @`429efcdf30`), `publish_peers_candidate.py` @`f12263b4e7`,
`UPLOADED 194 of 194 + 1 crosswalk, read-back 195 of 195`, receipt in `PEERS_CANDIDATE_20260924T0310Z/`.
**Grade:** CVO @`bb4d36e32c` route/data PASS (R-24); 992_HK member swap CLOSED not-a-defect on arithmetic (R-25).
**Struck, my error:** "cap vintage carried nowhere on R-1" -- it is `subject.cap_vintage` and it moved. Enrichment (b),
a member-set digest on R-1, stands. Control rule adopted (R-25b): an untouched case proves non-corruption, a
regenerated case free to differ proves fidelity; both arms are cited from now on.

## Closer items after the hand-back -- what the 04:38Z session measured

### Consumer 2 (Posture) -- EXERCISED on the served stack, every selection, 05:03Z
`PEERS_CONSUMER2_TRACE_20260924T0503Z/` (driver `peers_consumer2_trace.cjs`, trace.json with every `/api/scoped/amgt`
response body, run.log, 12 screenshots; token scan clean). Real signed-in session (claims `role=admin`,
`userType=Dev`), bundle `d2n2nzpeqf34ge`, 109 API responses, statuses {200, 404}; all 10 404s are the slash key.
Each case: the Peers tab, then the Posture tab, whose `usePeerSet` fires for the subject AND the comparable
(`PostureTab.tsx:339,347`; both calls observed in the trace):

| selection | Peers (consumer 1) | Posture (consumer 2) |
|---|---|---|
| `BA_US_Equity` | derived / 12 / SERVED; 17 columns, 1 carried (old bundle) | subject peers derived 12; comparable `DE_US_Equity` -> `/peers` 200 basis absent, rendered "identity UNRESOLVED ... it is NOT guessed" (R-23a fork, standing) |
| `992_HK_Equity` | derived / 12 / SERVED, FX caveat in reason | subject peers derived 12; posture object MACHINEABSENT, comparable none named |
| `ASML_US_Equity` | basis absent, reason shown, `(read SERVED)` | posture ABSENT (no O-1 object); subject peers read SERVED/absent |
| `CAT_US_Equity` | derived / 12 / SERVED | posture ABSENT (no O-1 object); subject peers derived 12 |
| `NOSUCHKEY_ZZ_Equity` | UNRESOLVED, raw string shown, no read | "ABSENT -- identity UNRESOLVED -- no posture was read" (negative control holds on consumer 2) |
| `BP/_LN_Equity` | "Loading..." -- every route 404 | "Loading..." -- every route 404 (failure case 3) |

### Failure case 1 -- expired session: EXERCISED on the served stack, BOTH arms
**Proactive arm (05:03Z, `PEERS_CONSUMER2_TRACE_20260924T0503Z/`):** the profile's bearer had expired at 03:35:43Z;
first navigation -> `/auth/refresh` 200 -> `/auth/me` 200 -> new bearer -> page landed, no `/login` bounce, no 401 in
109 responses (`ensureFreshToken` refreshes before the request when the in-memory marker reads old).
**Reactive arm (05:23Z, `PEERS_REACTIVE401_TRACE_20260924T0523Z/`, driver in the folder):** the expired bearer was
read out with scripts aborted, the app loaded and refreshed proactively, the expired bearer was swapped back into
localStorage without a reload (marker still fresh), then a client-side navigation fired the next requests with it:
`/security/BA_US_Equity/peers` **401** at 05:23:20.225Z -> console `[api-client] 401 received -- attempting token
refresh` -> `/auth/refresh` **200** at .378 -> the SAME URL retried **200** at .610; bearer rotated (new exp), page
stayed on `/security-analysis/CAT_US_Equity`, Peers panel rendered 17 rows. Edge 401 -> refresh -> retry, MET.
**LIMIT, named by the CTO (round-1 CORPUS analysis item 5, msg 25313 "routed call 2"):** the `pushState` + `popstate`
navigation did NOT re-drive the router -- the rendered Peers panel still read "BA US" and the 401 fired on
`BA_US_Equity/peers`, so the arm proved 401 -> refresh -> retry on the SAME URL, not on a different-security load. The
criterion is met (the edge 401 path is exercised); "the different-security case exercises what it appears to" is a
RE-RUN owed by this seat with the router driven through the app's own link or a full navigation with the marker held.
**Observation, explained, no row:** `/auth/refresh` + `/auth/me` fired on every navigation, 7 pairs 5 s apart, against
the 10-minute proactive threshold -- because `tokenIssuedAt` is an in-memory module variable (`api-client.ts:31-35`)
that resets to 0 on a FULL reload, and this driver hard-navigates per case. Client-side routing does not reset it.
Driver artefact, not an app defect.

### Failure case 2 -- READ_FAILED must not render as ABSENT: PASS as a TEST RUN
`portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs` (actual PeersTab + PostureTab, actual
react-dom/server): READ_FAILED renders "(read READ_FAILED)" with its incomplete-read reason, ABSENT renders "(read
ABSENT)", UNRESOLVED renders no read record; the three markups are pairwise different (531 vs 500 bytes); PostureTab
calls subject then comparable on both. LIMIT: a READ_FAILED cannot be induced on the served stack without breaking a
permission; whether the deployed route ever emits one is NOT MEASURED.

### Failure case 3 -- `BP/_LN_Equity` 404: LOCALISED to the API Gateway route table, with a discriminating pair
- The 404 body is `opal-portal-data-proxy`'s "Route not found" (its `/v1/*` list) with `path` already DECODED to
  `/api/scoped/amgt/security/BP/_LN_Equity/peers` -- the request never reached `opal-amgt-scoped-api`.
- Direct invoke of the DEPLOYED function (`CodeSha256 DEQQiCH+...`, LastModified 2026-09-23T22:02:35Z): rawPath
  `.../security/BP/_LN_Equity/peers` -> **200, derived, 12, SERVED**; rawPath `.../BP%2F_LN_Equity/peers` -> **200**;
  control `BA_US_Equity` -> 200. The handler's AMGT-rk-61 multi-segment branch is deployed and works.
- Live API `7k3ed8px20` (`opal-portal-data-proxy-api`): 103 routes, 16 scoped-amgt, all eight per-security keys
  single-segment `{security_key}`, zero greedy under `/api/scoped/amgt`, `$default -> opal-portal-data-proxy`. HTTP API
  decodes `%2F` before matching, a one-segment parameter cannot match two segments, the request falls to `$default`.
- **THIRD CLAUSE, R-30 amended by the CTO (msg 25290, 06:19Z):** a 404 on these routes today renders NO terminal state --
  three panels reading "Loading..." while the client retries (10 BP calls across ~6 s over three routes, the last 2.07 s
  after the trace's own `finished_at`). The slash-key repair removes today's TRIGGER and leaves that behaviour untested.
  So the act gains a clause graded INDEPENDENTLY of the route repair: **a 404 on a security route renders a TERMINAL
  state** (`PanelError` with its cause, C12), proven with the 404 still reachable (before the route lands) or with a
  fixture 404. Owner: this seat; un-parks with the route work.
- **Recommendation to `1.0.0_SA_CTO~Z` (infra, not this seat's file):** add ONE route
  `GET /api/scoped/amgt/security/{proxy+}` to `scoped_amgt_routes` in `scoped-amgt-api.tf` (precondition 16 -> 17;
  precedent `ANY /auth/{proxy+}` on the same API; a parameter segment beats greedy, so the eight existing keys keep
  matching slash-free keys) and the matching 17th entry in `scoped_amgt_route_table()` (this seat's file; the mount
  test diffs both directions). Zero client change; the `-SLASH-` token alternative is not needed because the handler
  was built for the literal form. rk-61's AC6 graded the two forms EQUAL-status -- a predicate two 404s satisfy.

## Dependencies

| Need | Owner | State |
|---|---|---|
| Live grading of consumer 2 + failure cases 1-2 from the 0503Z trace + harness | `3.0.0_SA_CVO~Z` | DUE: review handoff sent |
| Greedy route for the slash key (tf) + AE apply; py table entry from this seat in the same drain | `1.0.0_SA_CTO~Z` | OPEN CALL with recommendation |
| Portal deploy of `1ec5446c` (5 carried columns on the served bundle) | `0.0.0_AB_MSTR~Z` | OPEN: merge to DEV/PROD on Andrew's word |
| Posture comparable key space (`DE_US_Equity`, scanner members vs 194 subjects) | `4.0.0_SA_CRO~Z` research, CTO decides | OPEN (R-23a) |
| AMGT_RESAPP L4 addendum for the next round (CRO~Z surface walk -> CTO addendum -> this seat's L5/L6) | `1.0.0_SA_CTO~Z` | IN FLIGHT |

## Parked

- 60-name induction through `add_security`: per the hand-back §3(b) this is the AMGT_CORPUS round's (scripted,
  deterministic, R-21; V2 authorizes the calls, not a pick). NOT run here; `2.0.0_SA_COO~X`'s round owns it.
- Scanner-universe refresh (asOf 2026-08-06, writer unnamed); FX for the band; the 12 absent CSC columns: Andrew's
  data-source calls. B08/Price on `closer/amgt-experience-z-20260923` (MSTR's merge). No vendor call on this thread.

## Limits

No deploy, delete, schedule change, vendor call or shared push on this thread. The pool publication is the one write.
Offline PASSes bank no acceptance credit until graded on the served stack.
