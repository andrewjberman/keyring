# 0.7.0_AE_CloudOps~Z -- session close: the edge link + Andrew's verification + stand-down

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, COORDINATE
**Window:** 2026-08-07 ~03:55Z -> ~04:15Z (delta since the cutover-close addendum @ the same
session's main log). The cutover itself (legs 1-4, 12/12 emission, 14/14 projection) is recorded
in `session_0000Z_lane_Z_reset_startup_p21_landed.md` addenda 1-3 -- this log covers only the
final link and the close of the night.

## What happened

1. **COO edge-link request (040513Z):** CTO found the last unvalidated hop -- the MDPF publisher
   does not invalidate CloudFront (INF sibling does, positive-controlled), so "Andrew SEES the
   newest data" had an unmeasured edge-cache variable. One-request test prescribed with two
   branches; the test returned a THIRD:
   - Raw `/platinum/...` via opalinvest.dev (EVTSA9VEHNZVH, resolved live as the distribution
     fronting opal-data-portal-v2): **403, X-Cache "Error from cloudfront"** (unauthenticated).
   - **FE route measured at source, not assumed:** `portal/src/api/portal-proxy.ts:513-525`
     fetches `/api/general/mdpf/{firmId}/aggregate-aua-timeseries.json`; `:516` declares it
     serves from `platinum/mdpf/{firmId}/...` -- **the FE flip to platinum is LANDED** (the
     publisher docstring's "no reader until WO-3" was stale; ModelPortfolios.tsx:238/:966 agree).
   - FE route unauthenticated: **401, X-Cache "LambdaGeneratedResponse"** -- JWT-gated at
     viewer-request, BEFORE cache; no anonymous payload read exists (measured, not assumed).
   - Therefore the cache variable was removed outright per COO's branch-(b) pre-authorization:
     **CloudFront invalidation IED4JJNDKL8CX6O94D0K952VKK** on `/platinum/mdpf/*` +
     `/api/general/mdpf/*` -- polled to **Completed**. Any authed client's next request
     necessarily fetches the 03:52Z origin set (as_of_last 2026-08-05, ruled union).
   - Side measurement filed to the register: BOTH legacy `json/mdpf/global/...` surfaces
     (opal-data-assets + opal-data-portal-v2) still carry **as_of_last 2026-07-22** (the
     P0-deny-frozen restoration) -- consistent with the FE no longer reading them; relevant to
     R11/R12 retirement sequencing later.
2. **Andrew verified on his own screen** and ruled the night closed -- verbatim relayed by COO
   041448Z: *"well done"*, *"Portal is showing correct data for the first time in a week"* --
   and directly at this terminal: *"portal looks right, well done. keep the morning clocks as
   planned."* COO stand-down: drive loop cut; Andrew is the oracle on the 09:00 ET unattended
   cycle (NO watcher armed against it -- moratorium + his explicit word); clocked TOs stand.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| comp-routes trace --json /platinum/... | resolve the client path | PARTIAL | CATCHALL_DEFAULT (correctly refused to call a default a resolution); pointed at the SPA distribution, so the data distribution was resolved on the live primitive instead |
| comp-grep "aggregate-aua-timeseries" portal/src | which URL the FE fetches | PASS | found portal-proxy.ts:513-525 + ModelPortfolios.tsx corroboration -- the load-bearing measurement of the night's last hop |
| Raw aws (rail-checked): cloudfront list-distributions / create-invalidation / get-invalidation; curl edge fetches; s3 body reads | live-primitive edge test + operational invalidation | PASS | invalidation is a write act, not an inspection; fetches measured 403/401 with X-Cache discriminators |

What worked: comp-grep found the proxy contract in one call; the trace tool's honest
CATCHALL_DEFAULT enum prevented a false resolution. Gap: none new (comp-routes' SPA-distribution
scope is a documented blind spot, not a surprise).

## MCP traffic (window)

4 significant: COO edge-link request (040513Z) -> my measured close (040929Z, third-branch chain
+ invalidation evidence) -> COO/Andrew stand-down relay (041448Z) -> heartbeats. No unhandled
messages; broker re-surfaces of already-executed items not counted.

## Blockers

NONE. The one unobservable (the authed payload pixel) is Andrew's own screen and he has
verified it.

## Current State (zero-prior-context handoff)

- **Portal serves the canonical platinum surface, Andrew-verified.** Origin:
  `s3://opal-data-portal-v2/platinum/mdpf/{scope}/{type}.json`, 14/14 written 03:52:48-50Z,
  global as_of_last 2026-08-05, gap rendered carried(07-28..30)/measured(07-31,08-03). FE reads
  it via `/api/general/mdpf/{firmId}/aggregate-aua-timeseries.json` (JWT-gated). Edge flushed
  (invalidation IED4JJNDKL8CX6O94D0K952VKK, Completed).
- **mdpf-gold-lambda** live at pin 0bc739e7d514e5040d5a51c31dac9089b0cba321 (CodeSha256
  XuLlClWT... == artifact 5ee2e50a...), scheduled: `mdpf-scheduled-floor` cron(0 9 * * ? *)
  America/New_York ENABLED targeting it directly (old chain's target removed atomically).
  **09:00 ET today = first UNATTENDED scheduled cycle = rubric adjudication event; ANDREW is
  its oracle -- do not arm anything against it.**
- **opal-assets-mdpf-portal-publisher** live at c0902245b07438eb0be65cf5e28241d4be56aa38
  (D5 unchanged-no-rewrite via `platinum/mdpf/_manifests/latest.json` pointer; D7 immutable
  manifests; D8 bidirectional roster completeness; roster = build-copy, no S3 leg). Its 09:50 ET
  scheduler stands. NEXT run is the first D5 zero-write proof if sources are unchanged.
- **Deploy ledger** `org/critical_paths/change_management/20260807_mdpf_canplat_cutover_bundle_AE_Z.md`
  CLOSED (all legs, zero rollbacks). Tags `mdpf-pipeline-v2.3.0` + `opal-assets-mdpf-publisher-v2.0.0`
  await MSTR~Z's integration push.
- **Clocked TOs STANDING (dispatched task orders, not loop artifacts):** wake Monitor `bylqhag3z`
  fires 12:05Z -> **P0-2R** Orion probe STRICTLY inside 08:05-08:40 ET (ground the floor on the
  live cron, cite s3api +00:00; SmartX = S3-side fallback, word never named SmartX) -> **P0-7R**
  enumeration riding the 09:00 ET cycle (S3-pull pattern, hashes + denominators, snapshot
  snap-0fa2186f01fbc3785 cited not re-minted, cycle-no-fire = NOT-RUN).
- **Morning register (remediation pass, NOT tonight):** publisher adopts the INF sibling's
  create_invalidation pattern; stale "no reader until WO-3" docstring line in the publisher
  header; legacy json/mdpf surfaces frozen at 07-22 (R11/R12 sequencing input).

## Next Steps

1. [0.7.0_AE_CloudOps~Z] 12:05Z wake -> P0-2R probe window -> same-morning evidence to
   [2.0.0_SA_COO~Z] + [1.0.0_SA_CTO~Z].
2. [0.7.0_AE_CloudOps~Z] P0-7R enumeration during the 09:00 ET production cycle -> evidence to
   [2.0.0_SA_COO~Z].
3. [0.7.0_AE_CloudOps~Z] morning remediation pass items (register above) on COO routing.
4. [3.0.0_SA_CVO~Z] continues the battery against the live emission + the 09:00 ET cycle
   (their lane; artifacts already handed off).
