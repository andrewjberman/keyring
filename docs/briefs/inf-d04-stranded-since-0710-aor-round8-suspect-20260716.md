# BRIEF — INF_D_04 stranded since 2026-07-10: the Jul-9 header on PartnerAnalytics

**Author:** 0.6.2_AE_PartnerETL · **Date:** 2026-07-16 ~16:5xZ · **To:** 1.0.0_SA_CTO
**Requested by:** Andrew-direct at my terminal (~16:2xZ): *"we need to do pipescript on D_04, trace its
dependencies, and figure out where the issue is... write a brief on the subject and give it to CTO. I am
fairly sure the issue stems from our work on the AoR logic."*
**Trigger:** Andrew, screenshot: the Assets Overview header in `PartnerAnalytics.tsx` reads **"as of Jul 9,
2026"** (EXISTING CLIENTS $191M) — a week stale.
**Grade:** scope ESTABLISHED on served artifacts + source. **Mechanism NOT established — see §5.**
**Lane note:** INF is not my lane. I was Andrew-directed. Nothing was run, nothing written, no ad-hoc gold
run (NEVER#4). Every read below is a listing/GET on a served artifact or a source line.

---

## 1. It is not a cache, and it is not a display bug

The portal renders exactly what is in S3. The artifacts are stale **at source**:

```
platinum/firm/header_metrics.json         written 2026-07-10T14:51:11Z   data_as_of 2026-07-09
platinum/firm/partner_analytics_monthly   written 2026-07-10T14:51:14Z   data_as_of 2026-07-09
platinum/firm/partner_analytics_quarterly written 2026-07-10T14:51:16Z   data_as_of 2026-07-09
platinum/firm/partner_analytics_annual    written 2026-07-10T14:51:18Z   data_as_of 2026-07-09
platinum/firm/timeseries_chart.json       written 2026-07-10T14:51:24Z
```
`as_of_by_dim` on each: `{"aua":"2026-07-09","nna":"2026-07-08"}`. The `comp-platinum` trace shows the
rendered field is `data.data_as_of` via the `auaDonutSegments` transform — the header is faithfully
printing the artifact. **There is no cache to bust.**

## 2. Scope: ONE script, not the D group — and the mapping is 1:1

`comp-pipescript io INF_D_04.client_portal_summary.py` declares **11 WRITES**. The platinum/firm
write-date census returns **exactly 11 stranded artifacts**, and they are the same 11:

```
STRANDED (11, all written 2026-07-10 14:50:56 -> 14:51:39Z — ONE contiguous ~43-second run, then never again)
  header_metrics · dashboard · fee_efficiency · timeseries_chart · timeseries_overview
  partner_analytics{,_monthly,_quarterly,_annual} · clients-tab-slim · client_directory
  (+ its advisor-tier writes: platinum/advisors/{*}/{book,summary,nna_clients}.json)

FRESH TODAY (18, written 2026-07-16 14:57:48 -> 15:00:47Z)
  INF_D_00c -> leaderboard | INF_D_00 -> clients_tab | INF_D_02b -> top_holdings
  + activity_scan_* · cash_drag_* · firm_concentrations · concentration_risk · cumulative_chart
    · firm_composition · mix_summary · nmec_nmnc_nna · advisor_nna_canonical
```

**The D group is healthy.** `D_00`, `D_00b`, `D_00c`, `D_00d`, `D_02b`, `D_03` all wrote today. The runner
is alive. **`INF_D_04` alone has not written since 2026-07-10T14:51Z = 4 trading days** (07-13/14/15/16;
trading-calendar-resolved, not wall-clock — this is not a weekend artifact). Its `data_as_of 2026-07-09` is
5 trading days stale.

**The atomicity is diagnostic:** all 11 outputs are missing *together*, none partial, none stale-but-newer.
That is the signature of a script that **dies before its first write**, not one that degrades.

## 3. It is NOT input starvation — every dependency is fresh

All of D_04's gold/platinum inputs were written **today**, upstream of its slot:

```
gold/dimensions/accounts_dimension_latest.parquet  2026-07-16 14:08:51Z   <- INF_A_00 (the AoR-touched dim)
gold/timeseries/account_performance.parquet        2026-07-16 14:55:50Z   <- INF_C_03
gold/timeseries/client_performance.parquet         2026-07-16 14:55:57Z   <- INF_C_02
gold/views/account_team.parquet                    2026-07-16 14:55:52Z
gold/artifacts/advisor_fee_efficiency.json         2026-07-16 14:56:10Z   <- INF_C_08
gold/artifacts/timeseries_chart.json               2026-07-16 14:57:57Z   <- INF_D_00b
gold/artifacts/firm_mix_views.json                 2026-07-16 14:59:39Z   <- INF_D_03
platinum/firm/clients_tab.json                     2026-07-16 14:57:48Z   <- INF_D_00
platinum/firm/cumulative_chart.json                2026-07-16 14:58:06Z   <- INF_D_00d
```
**The chain ran and fed D_04. D_04 did not write.** Note especially: `accounts_dimension_latest.parquet` —
the dimension the AoR work rebuilt — is **fresh**. So "AoR broke the accounts dimension" is NOT supported.

## 4. THE PRIME SUSPECT — and Andrew's hypothesis is pointed at the right work, one layer over

`INF_D_04.client_portal_summary.py:60-62`, verbatim:
```python
# Round-8 (LD-0277): the per-view household resolve is RETIRED -- inherit C_07's stamped headline.
from aor_resolution import household_headline_map  # noqa: E402
```
**D_04 was edited BY the AoR work** (Round-8 / LD-0277) — the per-view household resolve was retired and
replaced with an inherited C_07 stamped headline. And the imported symbol carries a raise-on-empty guard:
```python
# data/inf/scripts/gold/lib/aor_resolution.py:955
def household_headline_map(account_team, expect_nonempty: bool, ...)
```
`expect_nonempty` is an **assertion parameter**. If D_04 passes `expect_nonempty=True` and the map resolves
empty, it raises — D_04 dies at that call, before any of its 11 writes. **That mechanism would produce
exactly the observed signature: 11 outputs stranded atomically, siblings unaffected, inputs fresh.**

Ruled out at source: module exists (`data/inf/scripts/gold/lib/aor_resolution.py`),
`household_headline_map` is defined, and `py_compile` on D_04 passes — **so it is not a missing module and
not a syntax error.** Any failure is at import-time-side-effect or runtime.

## 5. WHAT I HAVE NOT ESTABLISHED — and will not assert (Rule 22)

**§4 is a HYPOTHESIS, not a root cause.** I have not seen D_04 fail. The claim "the AoR Round-8 edit raises
and kills D_04" rests on shape-matching (atomicity + the edit's presence + a raise-capable guard), **not on
an observed exception**. A hypothesis cannot authorize a fix.

**The one artifact that would settle it: D_04's invocation result / CloudWatch log from today's 13:47Z
supervised nightly.** That names the exception or shows it was never dispatched. Two candidates remain live
and are DIFFERENT fixes:
- **(a) it runs and raises** — likely at the Round-8 `household_headline_map(expect_nonempty=...)` call.
- **(b) it is never dispatched** — absent from the restored run set (AMEND 62's "Restore daily dispatch"),
  in which case there is no exception at all and §4 is a red herring.
**(a) and (b) are indistinguishable from the S3 evidence alone** — both produce zero writes. Whoever holds
the run log can separate them in one read; I cannot, and I will not run D_04 to find out (NEVER#4: validate
on the scheduled run's artifacts, never one manufactured to validate against).

## 6. Falsified along the way (recorded so nobody re-walks them)

- **"The group D pipeline is broken"** (the starting hypothesis) — **FALSE.** Six D scripts wrote today.
  It is one script.
- **"Starved by missing bronze orion-api inputs"** — **FALSE, and it was mine.** `comp-pipescript io`
  reports D_04 reads `bronze/orion-api/{activity,household,performance}/latest.csv`, and all three ARE
  absent from the bucket (whose real grammar is `bronze/orion-api/{date|latest}/{file}`). I nearly called
  that the cause. **The source says they are tier-2 fallbacks:** *"Source priority (silver-first,
  bronze-fallback): 1. silver/api_dims/... 2. bronze/orion-api/.../latest.csv 3. empty DataFrame."*
  A missing bronze CSV cannot crash D_04 — it falls through to empty. **The tool's READS list is not a
  requirements list, and I read it as one.** (Worth a note for the next reader of any `comp-pipescript io`
  output: it enumerates referenced keys, not mandatory ones.)
- **"AoR broke the accounts dimension"** — **NOT SUPPORTED.** `accounts_dimension_latest.parquet` is fresh
  today (14:08:51Z).

## 7. Blast radius (why this is worth your slot today)

`platinum/firm/header_metrics.json` → **PartnerAnalytics + ClientsTab**;
`partner_analytics_{*}.json` → **PartnerAnalytics, DistributionTab, + 4 index routes**;
`dashboard.json` → **ClientsTab**; `platinum/advisors/{*}/nna_clients.json` → **DistributionTab**.
So a client-facing header has been serving a 5-trading-day-stale AUA since the chain came back, and every
*other* number on the same page is current — **the page is internally inconsistent, which is worse than
uniformly stale**: it looks live. Nothing alarmed.

**Recommended next step (yours):** read D_04's result from the 13:47Z nightly → separate (a) from (b) →
route to the AoR/Round-8 owner if (a), or to the dispatch set if (b). I hold no verb here and am not
proposing a fix to code I did not write.
