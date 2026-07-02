# DRAFT: ADVI_ETLFIX WS-4 — Predictable Portal Refresh (freshness-SLA-as-GATE + single-writer/no-clobber + re-publish path)

**Status:** DRAFT design brief — **ARCH-GATE RULED 2026-07-02** (CTO ruled BOTH core calls YES; COO+CVO accepted; the 6 ADs are working defaults, CTO arch-reviews them on the firmed WS-4 TO). **Author:** 0.4.0_DE_ClientPlatform · 2026-07-02
**For:** 1.0.0_SA_CTO (arch-gate) · CC 2.0.0_SA_COO (drive) · 3.0.0_SA_CVO (freshness verification)

**Arch-gate ruling (2026-07-02) + folded refinements:**
- CTO RULED YES on (1) content-`data_as_of` oracle (not mtime) + (2) outcome-keyed alarm (served-advanced-to-today, not chain-success) — "content-keyed (can't be fooled by mtime) AND outcome-keyed (can't be silenced by a degrade)". CTO added REQUIREMENT R1 (below). Two distinct gates: `ChainStepDegraded` = the DEGRADE signal; the outcome-keyed served-advance = the STALE-SERVED signal (this one is the load-bearing anti-silent-freeze gate).
- CVO added load-bearing refinement C1 (per-dimension outcome-key — below).
- COO: aligns exactly with CTO GATE-4; WS-4 is durable Phase-1 (not firefight-urgent).
**PRD:** docs/architecture/ADVI_ETLFIX_PRD.md §5 WS-4 / §4 invariant-1&4 / §6 arch-gate-4. **COO decomp:** org/tier1_exec/2.0.0_SA_COO/briefs/ADVI_ETLFIX_decomposition_20260702.md WS-4.
**Not implement — SHAPE for RAVC.** Preemptible: the moment an upstream leg un-freezes, the Phase-0 post-fix re-publish preempts this.

## 0. Load-bearing input (from the 2026-07-02 P0 serving-side ground-truth)
The serving layer is CLEAN (no dead-path / CF-cache / routing fault); all 3 freezes were ETL-production content-staleness. **The design-critical finding: a freshness SLA keyed on S3 mtime FALSE-GREENS.** bd 49F served `dashboard.json` was mtime-fresh (@07-02, the platinum-emit ran) but content-stale (`data_as_of=2026-06-29`, upstream frozen). **So the WS-4 SLA oracle MUST read the served artifact's CONTENT vintage (`data_as_of`), not `LastModified`.** This is the single most important WS-4 design constraint.

## 1. The served surface WS-4 must cover (endpoint -> artifact map, per partner)
| Partner | Served key(s) | Read path | Content-vintage field |
|---|---|---|---|
| 49F (bd) | `opal-data-bd/platinum/firm/{dashboard,header_metrics,partner_analytics_{monthly,quarterly,annual},leaderboard,cumulative_chart,timeseries_overview,advisor_nna_canonical,fee_efficiency}.json` | `/api/scoped/advisor-intelligence/platinum/firm/*.json` -> S3 (shared-advisor-router L@E, firm-suffix) | `data_as_of` (dashboard/header) |
| Inflection (inf) | `opal-data-inf/platinum/firm/*.json` (same set) | same, firm=inflection | `data_as_of` |
| MDPF (aggregate AUA) | SERVED `opal-data-portal-v2/json/mdpf/aggregate-aua-timeseries.json` (published from build-tier `platinum/mdpf/aggregate_aua_timeseries.json`) | `/api/general/mdpf/aggregate-aua-timeseries.json` -> portal_data_proxy Lambda | `generated_at` + max timeseries date |
| (generalize) | any partner's `platinum/firm/*.json` | parameterized | declared per-partner |

Note the MDPF two-tier split (build `platinum/mdpf/` -> published `portal-v2/json/mdpf/`): the SLA must watch the SERVED (published) tier, and the re-publish path (SS4) covers the build->served publish step.

## 2. WS-4 limb (a) — per-partner freshness-SLA-as-GATE (the SS4 invariant + arch-gate-4)
**Design principle (the anti-silent-degrade core):** the alarm monitors the OUTCOME (did partner P's SERVED content advance to the current business date?), NOT the PROCESS (chain rc / a sentinel a degrade can green). A positive-signal/heartbeat model: "served `data_as_of` for P == expected business date by the SLA deadline" — if not, the per-partner alarm fires, regardless of what the chain reported. This is precisely why the inf firefight's degrade could have greened the `inf-gold-chain-failed` alarm (SS1.2) — WS-4 keys on the served content, so a degrade CANNOT silence it.

Per-partner SLA record (proposed schema):
```yaml
- partner: 49financial
  served_key: opal-data-bd/platinum/firm/dashboard.json
  vintage_field: data_as_of          # CONTENT date, NOT mtime
  vintage_extractor: json:$.data_as_of
  cadence: business_daily             # skips weekends/holidays
  sla_deadline_et: "09:30"            # served must reflect prior business close by this time
  warn_lag_bdays: 1
  fail_lag_bdays: 2                   # >= this many business days stale -> LOUD per-partner alarm
  severity: ERROR
  alarm_scope: partner:49financial   # per-partner, NOT a generic chain alarm
```
- **Oracle = comp-freshness + a CONTENT-vintage dimension** (the enhancement I flagged in the P0 RAVC): comp-freshness today reads S3 mtime; WS-4 adds a mode that fetches the served JSON and reads `vintage_field`, comparing to the business-date frontier. `comp-freshness` stays the queryable oracle; the alarm is the GATE wired off it.
  - **CTO ruling (2026-07-02): BUILD this content-vintage dimension INSIDE WS-4 — do NOT fork a separate tooling TO** (a fork creates a blocking cross-dependency: WS-4's oracle would wait on it). BUT design it as a REUSABLE, GENERAL comp-freshness capability (a content-vintage read parameterized by the served-key's vintage field — NOT WS-4-specific) so the whole freshness-gate ecosystem + WS-5 all-partners inherit it free; and FLAG it on the tooling/COMPLEARN worklist as a landed capability so the reuse is discoverable. Net: built-in-WS-4 (no blocking fork) + reusable-by-design + worklist-surfaced.
- **Fail-LOUD, per-partner:** each partner gets its own alarm (bd-stale, inf-stale, mdpf-stale are distinct). A miss pages; a degrade elsewhere cannot green it (outcome-keyed).
- **R1 (CTO REQUIREMENT — the oracle's dependency):** every served-key-under-SLA MUST carry a reliable, standardized content-vintage field (`data_as_of` / `as_of` / data-`generated_at`). If a served artifact lacks one, the oracle can't key on content and FALLS BACK to mtime = the trap. So WS-4 has a PRE-REQ: audit the served-key set for a content-vintage field, and standardize/add it where missing. Per-surface field map (heterogeneous — CVO+CTO): bd=`data_as_of`, inf=`data_as_of` (header_metrics), MDPF=`as_of_last` (+ max-timeseries-date). The vintage-extractor config (AD-2) encodes this map; the audit confirms coverage.
- **C1 (CVO refinement — per-feeder/per-DIMENSION outcome-key, load-bearing):** the outcome-key must be PER-DIMENSION content-advance, NOT just the top-level served `data_as_of`. Why: a chain can COMPLETE GREEN via a DEFER-guard that ROLLS FORWARD one stale dimension (e.g. txn stale, other dims fresh) — the AGGREGATE served `as_of` still looks advanced, so an aggregate-keyed alarm slips it through. The SLA must therefore assert per-contributing-dimension freshness where the served artifact exposes per-dimension vintage (or the emit stamps a per-dimension `as_of` map). Pair with the staleness-CEILING (CTO robustness limb-3): a rolled-forward dimension escalates warn->high-sev/hard past N trading days so a persistent degrade can't roll forward indefinitely behind a low-sev warn.

## 3. WS-4 limb (b) — single-writer + no-clobber, uniform across served keys
Anchored on the ADVI_BREAKS inf stub-clobber: `INF_D_00:885-898` emitted a minimal 728B header stub that raced `orion-gold-dispatch.sh` (D_00-before-D_04) and became last-writer, collapsing the mature header on the shared served key.
- **Single-writer:** a registry `served_key -> sole intended producer`; detect violations via S3 `list-object-versions` (multiple distinct writers/night = a race). Coordinate with the LIVE `opal-globgrph-freeze-monitor` (cross-firm READ-ONLY served-layer) + the in-flight `ADVI_BREAKS.TO-6b` content-keyed etag-skip — do NOT duplicate; WS-4 is the uniform-across-all-served-keys generalization.
- **No-clobber:** a write that would REPLACE a mature artifact with a minimal stub is REFUSED. Guard = a per-key byte-size / shape FLOOR: the writer compares the incoming payload size/shape to the existing object before PUT and refuses a suspicious shrink (e.g. header_metrics dropping ~1600B -> ~300/728B). Detection backstop = the freeze-monitor's size/shape forensic.

## 4. WS-4 limb (c) — post-fix re-publish / cache-invalidate + optional served-staleness UI
- **Re-publish path (the DE Phase-0 on-call, formalized):** when an upstream leg un-freezes and the platinum-emit re-runs, per surface: (i) verify the emit wrote a fresh `data_as_of` (not just a new mtime — the P0 lesson); (ii) for MDPF, if the SERVED (published portal-v2/json) tier lags the BUILD (platinum/mdpf) tier, run the publish step; (iii) if the CloudFront cache-control TTL would hold stale, invalidate the specific served keys. comp-routes confirms the served paths carry an `origin-response: cache-control-injector` — the TTL it injects governs whether a CF invalidation is even needed (open decision AD-4).
- **Served-staleness UI (optional / defense-in-depth):** a small shared Portal component reads the served `data_as_of` and renders a "data as of {date}" badge, escalating to a staleness banner when `data_as_of` lags the business frontier by > N bdays. Makes staleness visible to the user + us BEFORE the alarm. Recommend DEFER to a fast-follow (alarm is the primary gate).

## 5. Open arch-decisions (for the CTO gate)
- **AD-1 — where the SLA-gate lives:** (a) comp-freshness content-dimension + a CW alarm wiring, (b) a dedicated served-freshness Lambda/EventBridge emitting per-partner CW metrics, or (c) extend the LIVE `opal-globgrph-freeze-monitor` (already cross-firm served-layer read-only). **DE lean: (c)+(a)** — build on the existing freeze-monitor + a comp-freshness content dimension = least new infra, reuses a proven served-layer reader.
- **AD-2 — the vintage-extractor spec:** the content-date field is heterogeneous (`data_as_of` ADVI, `generated_at`+max-timeseries MDPF). Needs a per-served-key extractor config (which field/JSONPath per key). DE can author this config (I have the artifact shapes from the P0 map).
- **AD-3 — no-clobber enforcement point:** writer-side size/shape floor (each emitter guards before PUT) vs a served-layer S3-event validator that quarantines a suspicious shrink vs bucket-versioning+rollback. **DE lean: writer-side floor + freeze-monitor as the detection backstop.** (Writer-side = AE/DS emitter lane; DE consumes.)
- **AD-4 — cache-invalidate ownership + necessity:** is the CF invalidation needed at all (depends on the cache-control-injector TTL — needs the actual max-age value), and is it a DE step or AE-infra (CloudFront invalidation = infra/aws = AE lane)? **DE lean:** DE verifies + triggers; AE executes the CF invalidation; the platinum-emit re-publish (S3 write) is AE/DS. DE role = verify-served-freshness + signal, not the infra action.
- **AD-5 — served-staleness UI:** build now or defer. **DE lean: defer** (fast-follow; alarm is primary).
- **AD-6 — alarm severity/routing:** per-partner SNS topic vs one ADVI_ETLFIX topic + who's paged; coordinate with the existing AE alarm infra + the `inf-gold-chain-failed`-class alarms (WS-1). AE-owned.

## 6. Owners / lanes (WS-4)
- **0.4.0_DE (me):** the vintage-extractor config (AD-2), the served endpoint->artifact map (done, SS1), the re-publish-VERIFY procedure (SS4), the optional UI (AD-5), consuming the single-writer/no-clobber guarantees.
- **AE (alarm infra):** the per-partner CW metric/alarm + SNS wiring (AD-1/AD-6), the CF invalidation (AD-4), the writer-side no-clobber floor in the emitters (AD-3, AE/DS emitter lane).
- **CVO:** freshness verification (the alarm actually fires on a real content-stale; the no-clobber actually blocks a stub).
- **CTO:** arch-gate — the SLA-as-GATE design (esp. the content-vs-mtime oracle + the outcome-keyed anti-silent-degrade model).

## 7. Machine-checkable ACs (WS-4, from PRD AC#4)
1. Every anchor-partner served artifact (bd/inf/MDPF) has a declared daily freshness SLA record with a CONTENT-vintage field (not mtime). **(R1 pre-req)** The served-key set is AUDITED for a content-vintage field; every SLA'd key has one (standardized/added where missing) — no key silently falls back to mtime.
2. A per-partner fail-loud alarm fires when served content lags the business frontier past `fail_lag_bdays` — DEMONSTRATED by TWO adversarial cases: (i) a simulated content-stale (hold a served key at yesterday's `data_as_of`) fires the partner alarm while an unrelated green chain does NOT silence it; **(ii, C1)** a chain that COMPLETES GREEN via a DEFER-guard-rolled-forward stale DIMENSION (one dim stale, aggregate `as_of` still looks advanced) ALSO fires the partner alarm — the per-dimension outcome-key catches it. Past N trading days the alarm escalates to high-sev/hard (staleness-ceiling).
3. Single-writer verified per served key (S3 version-history: one writer/night); no-clobber DEMONSTRATED (a minimal-stub PUT against a mature key is refused/blocked).
4. The DE re-publish path is proven on >=1 real un-freeze (served `data_as_of` advances to current post-upstream-fix; CF serves the fresh content).
5. The SLA + no-clobber config is PARAMETERIZED per partner (feeds WS-5 generalization).

## 8. Sequencing / dependency
WS-4 durable stand-up rides AFTER the pipelines are daily-reliable (WS-1 inf + WS-2 bd/Schwab un-freeze), per the COO sequencing. BUT the re-publish-verify path (SS4) + the mtime-vs-content oracle finding are usable in Phase 0 NOW (the on-call re-publish). Recommend: land the vintage-extractor config + the SLA schema in Phase 1 early (cheap, DE-authorable), so the alarm layer is ready the moment the pipelines stabilize.
