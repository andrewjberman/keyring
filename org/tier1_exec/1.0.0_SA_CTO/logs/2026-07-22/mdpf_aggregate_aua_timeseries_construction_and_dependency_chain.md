# 1.0.0_SA_CTO — `aggregate-aua-timeseries.json`: construction, upstream production, downstream chain

**archetype:** TRACE
**secondary_archetypes:** EXPLORE
**Window:** 2026-07-22 ~1545Z | **Serial:** 1.0.0_SA_CTO
**Andrew-direct ~1544Z:** *"write a /log about it, specifically how it is constructed and its dependency chain
downstream as well as its upstream production."*
**Scope:** read-only trace. Every claim is `file:line` at working-tree HEAD; nothing from recall.

---

## 1. WHAT THE ARTIFACT IS

`s3://opal-data-portal-v2/json/mdpf/{firm_id}/aggregate-aua-timeseries.json`

The per-firm AUA time-series the Model Portfolios page renders. `firm_id` ∈ `global`, `49financial`,
`inflection`. **Two spellings of the same content exist and the difference is load-bearing:**

| path | separator | role |
|---|---|---|
| `platinum/mdpf/{firm_id}/aggregate_aua_timeseries.json` | **underscore** | build-tier PRIMARY |
| `json/mdpf/{firm_id}/aggregate-aua-timeseries.json` | **hyphen** | CF-canonical SERVED mirror |

Reason (`build_aggregate_aua_timeseries.py:84-88`): the CloudFront public-data-router rewrites
`/api/general/*` → `/json/*` on S3, so the portal's fetch of
`/api/general/mdpf/{firm_id}/aggregate-aua-timeseries.json` resolves to the **hyphenated `json/`** key.

---

## 2. UPSTREAM PRODUCTION

**Source partitions** → `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`, one per date
(`:77` `PLATINUM_PREFIX`), enumerated by paginator at `:253-254`.

**Producer** → `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py`
Reads every `{date}.json` partition, rolls them into a time-series, and slices per firm —
`firm_ids = "global" + every key in artifact["partners"]` (`:80-81`).

**Two writes per firm, and they are NOT equivalent:**
1. **PRIMARY** — `platinum/mdpf/{firm_id}/aggregate_aua_timeseries.json` (`:645-648`).
2. **MIRROR** — `json/mdpf/{firm_id}/aggregate-aua-timeseries.json` (`:651-653`), described in-source as a
   *"CF-canonical dual-write … ADDITIVE FE mirror; graceful-degrade."*

> ### ⚠ THE MIRROR IS GRACEFUL-DEGRADE, AND THAT IS THE STRUCTURAL WEAK POINT
> `:654-661` — the mirror write is wrapped in `try/except`. **On failure it logs a WARN and CONTINUES.**
> Its own warning text names the likely cause: *"runner `json/mdpf/*` grant?"*
> **So the build can succeed, the primary can be current, and the SERVED artifact can silently stay stale —
> the failure is a WARN in a log, not a non-zero exit.** Every consumer in §3 reads the mirror, not the
> primary. **This is the single-point-of-silent-staleness in the chain.**

---

## 3. DOWNSTREAM DEPENDENCY CHAIN

**Serving path:** S3 `json/mdpf/…` → CloudFront public-data-router (`/api/general/*` → `/json/*`) → portal.

**Consumers, all grounded:**

| # | Consumer | Site | Reads |
|---|---|---|---|
| C1 | **Portal FE** — Model Portfolios | `portal/src/pages/ModelPortfolios.tsx:370` via `getMdpfAggregateAUATimeSeriesByFirm` | the rendered trend |
| C2 | **THE REVAMP PRODUCER** | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:476-500`, called `:628` | `by_model[].account_count` |
| C3 | **SmartX metrics** | `data/smartx/scripts/generate_smartx_timeseries_and_metrics.py:481` | `json/mdpf/global/…` |
| C4 | **Per-firm account distribution** | `data/smartx/scripts/compute_per_firm_account_distribution.py:22` | prefix alignment |
| C5 | **Count-source audit** | `data/mdpf/scripts/gold/mdpf_revamp_count_source_audit.py:54` | `SERVED_KEY` |
| C6 | **Freshness monitoring** | `data/served_freshness_config.yaml:28` | staleness |

### C2 is the one that matters — and it is the 14:25 guard's subject
`load_served_account_count()` (`:476-500`) does a **date-joined import of the served
`by_model[].account_count`** into the revamp's own output. Its docstring states the rationale: the count is
*"a real daily-snapshot NOT recomputable from `opened_ts` alone,"* so it is **IMPORTED to tie served EXACTLY
at COMMON dates.**

**ONE live call site remains: `:628`, `FIRM_49F` only.** (`:809` records the import being **DROPPED** on the
other path — that is today's count-axis fix, which moved inflection and global to deriving count and value
from the *same* eclipse snapshot. **49F could not follow: no per-date 49F account-count source exists
anywhere.**)

**Failure mode on absence** (`:485-487`): a bare `except` → logs a WARN → **returns `{}` → all-None counts.**
**So deleting or freezing the served 49F artifact does not raise. It silently empties the count axis** — and
a frozen count is indistinguishable from a stable roster. **That is precisely what the delete-guard exists to
prevent.**

---

## 4. THE CIRCULARITY, STATED PLAINLY

`load_served_account_count`'s own docstring (`:483-484`):
> *"Read from the served path (pre-cutover = legacy; post-cutover `json/mdpf` IS the revamp → a stable
> rolling carry, never a runaway)."*

**Pre-cutover the revamp reads the LEGACY artifact. Post-cutover it reads ITS OWN PRIOR OUTPUT.** The design
calls this a *stable rolling carry*, and the argument is sound for a value that only ever carries forward.
**But it means the artifact becomes self-referential at cutover, and the 49F count axis has no external
anchor on either side of the line** — before cutover its anchor is a legacy series whose date axis we proved
today is not a trading-day axis; after cutover its anchor is itself.

**Consequence chain, all established today:** no per-date 49F source → count imported from the served
artifact → the served artifact's date axis is defective → **49F's count axis is structurally implicated and
unmeasurable by artifact comparison**, with one measured disagreement (2026-07-17, −10 accounts, mechanism
UNDETERMINED). **The only remedy is a per-date 49F roster history that does not currently exist.**

---

## 5. WHAT DEPENDS ON WHAT — one line

```
platinum/mdpf/aggregate_aua/{date}.json          (source partitions)
        └─ build_aggregate_aua_timeseries.py     (rollup + per-firm slice)
              ├─ platinum/mdpf/{firm}/aggregate_aua_timeseries.json   PRIMARY
              └─ json/mdpf/{firm}/aggregate-aua-timeseries.json       MIRROR  ← graceful-degrade
                       ├─ CloudFront /api/general/* → /json/*  →  ModelPortfolios.tsx:370      [C1]
                       ├─ dim_mdpf_aggregate_aua_timeseries.py:628  (49F account_count import) [C2]
                       ├─ generate_smartx_timeseries_and_metrics.py:481                        [C3]
                       ├─ mdpf_revamp_count_source_audit.py:54                                 [C5]
                       └─ served_freshness_config.yaml:28                                      [C6]
```

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` | routed | near-tie between `comp-pipescript io` and `pipescript --resource`; read the descriptions rather than taking rank order |
| `pipescript --resource "json/mdpf/49financial/aggregate-aua-timeseries.json"` | **no thread references it** | a real answer, not a failure: the artifact is not carried by any named thread — worth noting, since it means the estate's thread traversal does not reach the object six consumers depend on |
| `comp-grep "aggregate-aua-timeseries"` | 30+ hits across data/, docs/, portal | the on-rails search that produced the consumer census |
| `sed`/`grep` at `file:line` | PASS | every claim above pinned to a line at working-tree HEAD |

**What worked:** the `comp-grep` sweep surfaced consumers no single lane would have listed — C3/C4 are SmartX
scripts, outside the MDPF tree entirely. **What failed:** `pipescript --resource` returned nothing for a
six-consumer artifact; the named-thread graph does not model it. **Gap found:** the `json/` mirror's
graceful-degrade `try/except` (`:654-661`) means a failed FE-mirror write is a WARN, not a failure — no gate
distinguishes *"the build succeeded and the served copy is current"* from *"the build succeeded and the
served copy is eight days old."*

## Blockers
None. Read-only trace under the MDPF hold (carve-out 3: analysis is not initiation).

## Next Steps
- [1.0.0_SA_CTO] Carry the graceful-degrade mirror finding into Andrew's advisory as a named residual — it is
  the same *silent-staleness* family as the 49F count import, one layer up, and it is currently ungated.
- [ANDREW] the 14:25 delete-guard GO, still open (its subject is C2's dependency, documented above).
