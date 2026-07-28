# 2026-07-28 — Session 1343-2015Z: MDPF P0 render verification -> the $1.92B mechanism, the 0824 basis trace, and two Andrew-directed route/architecture traces

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, VALIDATE, COORDINATE

Spawned for ONE task — verify the portal renders $1.95b Global on deployed PROD after CTO's serve
restore. It did not. Reproducing WHY produced the session: a cross-basis sum in the renderer, an
Andrew-direct canonical basis ruling, a producer trace, a route-canonicality census, the DEBT.FRONTEND
brief, and two Andrew-directed architecture traces. **Zero writes to served output. Zero deploys. Zero
promotes.** One CloudFront invalidation, explicitly GO'd by CTO.

---

## The through-line

**Andrew sees $1.92B; CTO's restored bytes say $1,951,676,164.42.** Reproduced the rendered figure to
the cent from the served artifacts:

```
ModelPortfolios.tsx:1168-1172 (global branch)
  totalAUM = trendLastPoint.aum + getNonModelAumForDate(nonModelData.time_series, period)

  1,676,493,815.11   FRESH model    <- json/mdpf/global/...      restored 13:41:05Z
+   247,692,229.36   STALE non-model<- json/portfolios/non_model_assets.json  07-27T15:10:07Z
= 1,924,186,044.47   -> renders $1.92B    == what Andrew sees
  1,951,676,164.42   -> $1.95B            == the coherent figure inside the REVAMP artifact alone
```

**The headline sums a model leg from one basis with a non-model leg from another.** That claim survived
Andrew's challenge; my first framing ("the legacy file is stale, so $1.95b is right") did not, and I
withdrew it — staler does not mean wrong, and I had not established which producer was authoritative.

---

## Hypotheses killed on evidence (the useful part)

| hypothesis | verdict | how |
|---|---|---|
| Stale CloudFront edge cache | **DEAD** | scoped invalidation `I7XEJLFTYGIUEDR4J97XNW091Z` Completed 13:58:24Z; number did not move. Recorded dead, not unproven-but-likely. |
| Position-vs-date axis offset (COO's 18-slot) | **FALSIFIED for the headline** | `getNonModelAumForDate:363-381` is a DATE-keyed roll-forward, not positional. Segment/trend paths NOT cleared. |
| F7 blend roll-up broken (CTO's) | **NOT THE DEFECT** | `rollBlendsIntoArchetypeModels:208` exists, invoked on Global at `:724`, operates on already-canonicalised names (`:688`), targets all resolve. Both failure modes ruled out. |
| Mixed scope in Global artifact (MINE) | **RETRACTED** | measured `398,074,961.68` was exact and aimed at the wrong object — Andrew: *"global is scoped correctly, i am reffering to 49 here"*. Saved only by labelling it a BASIS question I was not entitled to answer. |
| `$0` on my own render | **NOT A PORTAL STATE** | 13/13 requests 401'd at `auth-validator-edge`; the $0 was my stub token. Nearly a false P0. |

---

## Andrew-direct rulings received + recorded (verbatim, broadcast same turn per XXX.md)

1. **~1427Z canonical basis** — *"0824 schwab total value minus 49F smartx model aggregation, that is
   canonical balance"* → `13fbdea6d`, broadcast CTO+COO+MSTR.
2. **~1443Z scope** — *"global is scoped correctly, i am reffering to 49 here"* → killed my mixed-scope
   finding; folded into `f68266a2d`.
3. **~1830Z canonical routes** — `/api/general/` + `/api/scoped/` only → census `3370c546f`.
4. **~1845Z DEBT.FRONTEND** — investigation, **LOW PRIORITY**, *"generated != displayed"* → `c034fee55`.
5. **~1915Z (via CTO) two traces** — logic not inventory → `ef18a5fac` + `1a60b0542`.

**Trace result on (1):** REVAMP satisfies the formula **EXACTLY, 3/3 firms** (`custody_total - model_aua`,
to the cent); LEGACY does not. Source-confirmed at `build_aggregate_aua_timeseries.py:430`. **Single date
tested (2026-07-22) — disclosed unprompted; 446 dates untested.**

---

## Findings raised

- **AGG weighting defect [LIVE, client-facing, DE's lane].** `codeMap` in `SelectionTab.tsx:92` /
  `HoldingsTab.tsx:567` hits **1 of 7** served model names (hyphen vs space) → AGG weights Intermediate
  100%, other four 0% on Attribution + Positioning. **The equal-weight fallback is DISARMED by the single
  partial hit** (`hasAUM = totalAUM > 0`). NOT rendered — no visual claim made.
- **`/json-tiered/*` serves 200 UNAUTHENTICATED** where its canonical twin is 401, same S3 origin, zero
  portal clients. **BOUNDED:** mdpf/portfolios keys 403 — no client data reachable.
- **`/api/private/` is NOT dead** — self-correction; 14 live call sites, 11 Portfolio Management.
- **Write-side gap**, raised 3x: AE's deny covers 2 of 4 legacy keys; `aum-metrics.json` +
  `account-distribution.json` unprotected. COO dispositioned and kept it open on its own axis.
- **Namespace sprawl reproducing in the consolidation bucket** — `opal-data-assets/portal/{gold,
  model-portfolios,portfolios}/`. COO escalated on cost-of-delay.
- **Vocabulary contract** (Andrew-directed to CTO): consumers join on `by_model` MACHINE KEYS;
  `display_name` is presentation-only; `cohort_class` is served, do not re-implement. **FOUR competing
  display vocabularies measured** — and the consolidated one has already renamed
  `Long-Term Conservative` -> `Long Term`, so a point fix re-breaks at cutover.

---

## Deployment Sequence + Verification (DT role requirement)

**NO deploy, NO promote, NO Terraform, NO Lambda change this session.** One infra action:

```
CloudFront invalidation (CTO GO 135654Z, scoped as ordered — NOT /*)
  ID      I7XEJLFTYGIUEDR4J97XNW091Z
  PATHS   /json/mdpf/*   /api/general/mdpf/*
  STATUS  Completed
  CREATED 2026-07-28T13:58:24.762Z
```
**Outcome reported as it happened: the invalidation completed and the number did NOT change.** That was
the informative result — it killed the cache hypothesis.

Evidence pulls (read-only): `get-distribution-config` (24 behaviors), `list-invalidations`,
`get-cache-policy` (`Managed-CachingOptimized`, DefaultTTL 86400), `list-object-versions`,
`head-object`/`get-object` on 6 served artifacts, `cloudtrail describe-trails`/`get-event-selectors`,
6 unauthenticated route probes.

---

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| `comp-which` | yes (x2) | PARTIAL — routed to `comp-routes`/`comp-transform` on near-ties; correctly declined to guess. Did not have a route for "which fetched data is never rendered". |
| `comp-routes behaviors` | yes | PASS — gave the full CF behavior/auth map incl. behavior 18 and the `[AUTH]`/`[ROUTER]` annotations that made the `/json-tiered/*` auth split legible. Correctly disclosed DESIRED-plane. |
| `comp-grep` | yes (x6) | PASS — found the producers (`build_aggregate_aua_timeseries.py:430`, `build_legacy_compat_emit.py:615`), the `/api/private/` census, and the `json/latest/` writer. |
| `comp-cache map` / `key` | yes | PASS — 105 of 105 `useQuery` sites, 0 unparseable. Confirmed Andrew's generated!=displayed hypothesis (`getAUMFlows` zero consumers). |
| `pipescript --resource` | yes (x2) | PARTIAL — snapshot 43d stale, and `non_model_assets` returned "no thread references". Used for localisation only. |
| `comp-iam` | no | No IAM change made; the deny work was AE's lane and I grounded on CTO's applied-plane report. |

**What worked:** the **two-method enumeration with different blind spots** — runtime capture + source
trace, denominators reported separately. It is the only reason the sixth namespace surfaced. And
**positive-controlling my own retrieval**: `aws s3 cp --quiet` produced no file and no error, caught only
because I checked the destination.

**What failed:** (a) `aws s3 cp --quiet` silent no-op — the objects=0-on-unwritable-path class;
(b) `git log --since "13:00"` read LOCAL time and **silently dropped 2 of my 6 commits** while building
this log — verification-law-11, caught by a count that looked wrong; (c) my ui-smoke tab selector matched
the CSS-uppercased label, not DOM text, leaving the lazy tabs unexercised for hours.

**Gap found:** **no comp-tool routes "which fetched data is never rendered."** `comp-cache` audits
`useQuery` ONLY — and **both live consumers I found this session are direct `await`s, invisible to it**.
`comp-transform schema-check`'s UNUSED axis is the nearest instrument but is component-scoped, not
route-scoped. Recorded in the DEBT.FRONTEND brief §7 so the next agent does not inherit a false
denominator.

---

## Current State

- **Deployed PROD unchanged:** portal head `17256834` (v2.1.148). Main tree on DEV. **I made no portal
  commit, no merge, no promote.**
- **Served MDPF bytes:** `json/mdpf/global/aggregate-aua-timeseries.json` ETag `5f758b47`, 254,419 B,
  LastModified 2026-07-28T13:41:05Z (CTO's restore) — re-verified by me independently.
- **Rendered Global headline: $1.92B**, mechanism source-confirmed at `ModelPortfolios.tsx:1168-1172`.
  **NOT FIXED — no GO held.**
- **AE deny** `P0DenyJsonMdpfClobber20260728` covers `json/mdpf/*` (applied + exercised per CTO) and TWO
  literal `json/portfolios/` keys; `aum-metrics.json` + `account-distribution.json` remain unprotected.
- **Deliverables committed:** `13fbdea6d` (basis ruling) · `f68266a2d` (producer trace) · `3370c546f`
  (route census) · `c034fee55` (DEBT.FRONTEND brief) · `ef18a5fac` + `1a60b0542` (Traces 1+2 + residuals).
- **RAVC:** CTO closed the traces 201205Z, VALIDATED, no rework. COO's enumeration DELIVERED — I corrected
  both CTO and COO who had it as open.
- **Watcher:** Monitor task `b05v8mo07` live all session; zero crons armed.

## Next Steps

- **[0.4.0_DE_ClientPlatform]** AGG weighting defect (`codeMap` 1-of-7). **Design against the
  consolidation vocabulary (machine keys), not a string patch** — a patch to today's literals re-breaks at
  cutover.
- **[1.0.0_SA_CTO]** owns: publisher sequencing + the fix-shape call (FE re-point vs producer re-point —
  **`comp-blast` first, other consumers of `json/portfolios/aum-metrics.json` NOT enumerated**);
  Benchmark/Peers partner-selector semantics; portal-v2 write attribution; the `/json-tiered/*` auth split.
- **[2.0.0_SA_COO]** DEBTCLEAN decomposition — has the 23-key derived set + the vocabulary contract line.
- **[0.7.0_AE_CloudOps]** deny extension to the two unprotected legacy keys (authorised per CTO 1445Z; I
  have not seen it read as applied).
- **[me]** IDLE, available. DEBT.FRONTEND stays LOW PRIORITY / unstaffed per Andrew.

## Blockers

**None.** Nothing I own is blocked; every open item is dispositioned to a named owner above.
