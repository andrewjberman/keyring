# work session — 0.4.2_RD_AdvisorIntelligence — 2026-06-03 ~1400Z–1716Z

Andrew-direct FE session. Cleared the whole Advisor-Intelligence FE refinement queue, shipped two
Andrew-live data-label fixes, completed a cold-start correctness fix, and built the FIX2 keep-warm
mechanism (FE + coordinated backend) end-to-end. Headline = **keep-warm** (the one Andrew flagged
"important").

---

## 1. ADVI_FEREFI.W1 items 1-5 (Andrew-direct FE refinements) — SHIPPED PROD v2.1.113

TO: `org/projects/task_orders/ADVI_FEREFI.W1.rd-ai-fe-items-1-5.md`. Commit **b5d3e923** (portal DEV).

- **Item 1** — PartnerAnalytics Assets Overview defaults → Year + 3Y (`granularity 'quarterly'→'annually'`, `timeWindow '1Y'→'3Y'`).
- **Item 2** — removed 4 user-visible "(pseudonymized)" spans (ClientDetailPage:99; DistributionTab ×3). Masking LOGIC byte-unchanged. Removing the spans orphaned `canSeeCleartext` (their only consumer) in both files → removed the orphaned `useAuth` destructures + imports for eslint-clean. Server-side display_name masking untouched — only the annotation label is gone.
- **Item 3** — removed Segment-Analytics category search bar (both Inflection + 49F blocks) + dead `categorySearch` state/resets + now-orphaned `Search` lucide import (`X` kept).
- **Item 4** — AdvisorAnalytics Lifetime Activity defaults → Max + Year (`interval 'quarterly'→'yearly'`, `window '1Y'→'max'`).
- **Item 5** — AdvisorAnalytics AUM-mode tooltip (`AuaClientsChart`): added period-over-period **$ change + % change** rows, reusing the NNA prev-period pattern; base = `total_aua` (reconciles with Total). First period omits, `prev===0` → "—" for %, green/red signed via `ChartTooltipRow.signedValue`. The AUA-mix + NNA tooltips left byte-unchanged (the duplicate Mix tooltip at L663 deliberately untouched).

tsc + eslint clean. RAVC2 → COO ACCEPTED. **Shipped to PROD in v2.1.113** (PROD=9f890e0f).

**Item #6 (drop synthetic "approx")** — see §5. Resolved to verify-only, no code.

## 2. AUA → AUM (Andrew live) — NO-OP, already correct

Andrew: "we call it aua on the backend, change to aum on frontend." Investigated the whole AdvisorIntelligence FE: all user-visible labels ALREADY say AUM (mode toggles, "Total AUM", "AUM by Tax Status", "Assets under Management"). Remaining "AUA" tokens are non-rendered (data keys `ptAny['Total AUA']`/`total_aua`, var names, comments). Andrew clarified: **AUA stays for Opal/aggregate views, AUM for partner views** — exactly what `src/lib/assetsLabel.ts` (ADVI_INFOTD.W1) already does (`FIRM_SCOPED=AUM` / `AGGREGATE=AUA="Assets under Advisory"`). No change.

## 3. Cold-start false-empty FIX 1 (AE-handed brief) — SHIPPED PROD v2.1.113

Brief: `docs/briefs/advi-books-publicprofile-coldstart-false-empty-fe-brief-20260603.md` (AE 0.7.0, b5af4ccc2). Commit **21be552d** (portal DEV), AE RAVC-validate PASS.

Root cause: deep L3/L4 drilldown queries override the global smart-retry with `retry: false`, so a cold `opal-partners-data` 503/abort renders a false "no data" (no retry, no cache fallback). `retry: false` is NOT a PII control (`gcTime:0` is) and defeats the backend's deliberate 503-for-retry contract.

Fix: removed `retry: false` (KEPT `gcTime:0`) on AdvisorBookView.tsx L3/L4/timeseries/rfs-fan-out + AdvisorPublicProfile.tsx drilldown-summary. **Left exec-summary `:303` as-is** (404→empty by design). Added regression-guard comments citing the brief so nobody re-adds `retry:false` as a phantom PII control. Pure FE correctness, no backend dep.

## 4. INFDEMO.001 closure + F3b emit-gap FINDING

`ADVI_INFDEMO.001` was a stale `in_progress` (IWM demo 5/28, code live on PROD since `f61cb40b`+`4bdb844e`, only a CTO visual-confirm dangling). Surfaced to COO → disposition (a) flip COMPLETE (commit **64a8edbf8**, CLOUD). 

**F3b PHASE-1 emit-status finding** (reported separately to COO + CTO per carve-out): the Peter-Lee "ACTIVE SINCE Unknown / NO ROLE DATA" was a **genuine upstream data-emit gap** — Inflection advisor records emit neither `active_since` nor `role_breakdown` (49F emits both), NOT a FE bug. FE posture already resolved (Andrew Q3 graceful-hide, shipped 4bdb844e). Captured as a **parked DS backlog item** (CTO+COO): if Inflection advisor identity/role should ever surface, it needs an upstream DS emit. Same "Inflection-emits-less-than-49F" family as the fee lineage (F11→#6), distinct field set.

## 5. FEREFI #6 (drop synthetic "approx") — VERIFY-ONLY disposition (prevented a bad strip)

COO initially framed #6 as "dead-code cleanup: remove the synthetic branch + retire `computeSyntheticFeeRatio` once INF (W2) + 49F (W2b) serve real fee-splits." While pre-staging I found this was **wrong/dangerous**:

- `hasFeeSplitSeries` (AdvisorAnalytics.tsx:235) is **per-advisor data-driven** (true iff that advisor's served timeseries carries `*_fee_paying` sub-streams) — NOT a per-firm static flag.
- `computeSyntheticFeeRatio` is not just the "approx" label — it **scales** the actual AUM/NNA/inflows/outflows series (`:258/266/274/282`) for any advisor lacking sub-streams. The "approx" caption is the honest caveat **coupled** to that scaling (scale-synthetically + disclose-approx = one mechanism).
- ⇒ "fully unused fabric-wide" requires EVERY advisor across ALL firms (incl. demo + edge/pre-attribution) on the real path. INF+49F serving doesn't guarantee that. Removing the branch/label while scaling can still fire for any data-less advisor = the exact misleading state (scaled-as-if-real, no caveat) we're avoiding.

Surfaced to COO → COO accepted: **#6 = VERIFY-ONLY, KEEP the self-deactivating fallback, no code removal.** Andrew's "we have the data, don't approximate" is satisfied by SERVING the data — those advisors auto-take the real path; the fallback correctly remains where data is genuinely absent. Demo status = informational, not gating. **Saved us from stripping a live honest mechanism.**

## 6. ModelPortfolios Data Source panel — Inflection=Orion not SmartX (Andrew live) — DEV-ahead v2.1.114

Andrew flagged the Model Portfolios "Data Source" panel read "SmartX Connected / from SmartX Analytics / − SmartX Model AUM" for Inflection — should be Orion. A prior fix (548c9d7d) had firm-scoped the PanelFooter line but MISSED this panel + the Non-Model footnote (different render strings). Commit **858bd374** (portal DEV).

Completed it: added `modelSourceName` (Orion|SmartX) + `modelSourceFullName` (Orion Portfolio Solutions|SmartX Analytics) keyed off `effectiveFirmId==='inflection'`; applied to all 3 hardcoded sites (panel :1779, footnotes :1785 + :1042). 49F + global keep SmartX (historical default, consistent with the existing ternary). **ADVI checked (Andrew's request): already correct** — `_partners/inflection/index.tsx:299` renders "Orion Connected" (ADVI panels are per-firm-dir). Remaining "SmartX" in ModelPortfolios.tsx are comments only.

## 7. TaxCostBasis "Realized" → "Realized (YTD)" (Andrew live, label-only) — DEV-ahead v2.1.114

COO-queued after keep-warm. Commit **f2f62b17**. `TaxCostBasisPanel.tsx:151` bubble label only; DS-confirmed YTD semantics, no data change. "Unrealized" left as-is (point-in-time, unambiguous). Only rendered "Realized" label (rest comments).

## 8. ★ FIX2 keep-warm — FE hook + coordinated backend, END-TO-END

The important one. Andrew's question (via the cold-start companion brief `docs/briefs/fe-driven-lambda-keep-warm-feasibility-20260603.md`, AE 91df57398): *"How can we subtly ping relevant Lambdas while a user is active to keep them warm?"* Answer: FE-driven presence-gated warm-ping, ~150x cheaper than provisioned concurrency (~$0.15/mo vs ~$27/mo), follows the user, costs nothing idle.

**Coordination:** COO GO'd (Andrew decision-a) → I sent AE a `[CONTRACT-ASK]` for the exact warm-route, built the hook in parallel against the brief, AE replied with the contract, I matched it exactly, AE deployed the backend, I refined + RAVC2'd. Clean parallel build.

**FE (commits ed16010c + refine 90f67b5e):**
- `api-client.ts` `warmLambda(endpoint)` — fire-and-forget GET reusing the authed path (Bearer + 401 refresh-retry), 9s AbortController timeout, **all errors swallowed** (best-effort; warming must never touch the UI).
- `hooks/useLambdaKeepWarm.ts` — **presence-gated** (`visibilitychange` + `document.visibilityState==='visible'`), **view-targeted** (`/advisor-intelligence` + `/portfolios` only; S3-backed views skipped), **~4min jittered heartbeat** + **60s debounce**. Warms on route-into-view + tab-refocus + heartbeat; stops on hide / navigate-away / unmount. **Per-ping `&_=<ts>` cache-buster** so each ping provably reaches the Lambda (a cached warm response would silently defeat warming).
- `App.tsx` — mounted in `DashboardLayout` (authed-only, inside Router, persists across dashboard nav), firmId threaded from JWT claims.

**Backend (AE 0.7.0, partners-api-v1.16.3 + market-overview-v1.11.1, LIVE):** `?warm=1` early-return BEFORE any DynamoDB/S3 I/O, behind edge auth, returns `200 {"warm":true}` with `Cache-Control: no-store`. Still pays the module-level `import awswrangler` init on a cold env — which is exactly what warms the container.

**Warm route (matched exactly):** `GET /api/scoped/advisor-intelligence/filters?warm=1&firmId={firmId}` (cheapest stable opal-partners-data route; short-circuits at entry). Kept as a single `buildWarmEndpoint()` so any future path pin is a 1-line change (none needed — my path matched AE's final contract byte-for-byte).

**Verification:** backend = AE direct-invoke verified; FE hook = code + tsc + eslint clean + URL byte-match. **In-app NETWORK smoke** (warm-pings fire on Advisor-Intel/Portfolios, 200s in Network tab, stop on tab-hide) is **auth-gated → Andrew's gate at promote** (localhost dev requires login). `data-proxy` 2nd target left unwired (922ms minor vs partners-data's 5.4s; deferred).

---

## Net state at session end

- **PROD v2.1.113 (live):** ADVI_FEREFI.W1 items 1-5 (b5d3e923), cold-start FIX 1 (21be552d).
- **DEV-ahead for v2.1.114 (5 commits, CTO-tracked):** 858bd374 (Orion Data Source) · 3e0ce8d0 (xlsx, not mine) · ed16010c (keep-warm hook) · f2f62b17 (Realized-YTD) · 90f67b5e (keep-warm cache-buster).
- **CLOUD:** INFDEMO.001 closure (64a8edbf8).
- **Dispositioned:** AUA→AUM (no-op), FEREFI #6 (verify-only, no code), F3b emit-gap (parked DS backlog).
- **Gated / standing by:** (1) Andrew in-app network smoke for keep-warm at promote; (2) 49F W2b verify on 0.6.0's publish → #6 visual-verify; (3) CTO/Andrew v2.1.114 promote GO.
- Rule 19 honored throughout (portal main tree on DEV, no promotes). All commits via safe-commit under the RD serial; tsc+eslint clean on every change.

## Reusable takeaways

- **keep-warm is a reusable pattern** — presence-gated FE warm-ping + backend no-op `?warm=1` early-return. Cheap, follows the user, idle-free. Future Lambda cold-start problems can reuse `useLambdaKeepWarm` + the `?warm=1` branch shape (the brief's cost analysis generalizes).
- **A "dead-code cleanup" framing is a trap when the code is a per-entity self-deactivating fallback** (#6). Check whether the mechanism still does real work for ANY entity (not just the firms in question) before stripping; a coupled honest-caveat must not outlive its scaling.
- **Committed ≠ deployed ≠ rendered** kept biting adjacent work (INFDEMO closed-on-commit, 548c9d7d footnote-fix missed sibling render strings). Grep wide for ALL render strings of a token; visual gate is Andrew's where auth blocks localhost.
