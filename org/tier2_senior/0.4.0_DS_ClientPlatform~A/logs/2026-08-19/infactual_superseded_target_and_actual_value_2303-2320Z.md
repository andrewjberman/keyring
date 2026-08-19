# 0.4.0_DS_ClientPlatform~A — MDPF_INFACTUAL.001 (inflection ETF actual holdings) — 2026-08-19 23:03–23:20Z

**Archetype:** MEASURE-AND-ROUTE (the build was ruled off; the measurement is the deliverable)
**TO:** `MDPF_INFACTUAL.001` — issued 2026-07-29, flipped to GO 2026-08-19 ~23:03Z, **HELD** on CTO ruling
**Commit:** `600c5e0a33` (measurement deliverable)

---

## How it started

COO ran a `[DRIVE]` pass, saw a pending TO beside an idle seat, classified it STARVED and flipped it to GO —
explicitly inviting me to say so if the face carried something they had not seen. It did.

## What I found, in order

**The mandated Phase-1 gate could not answer its own question.** `comp-pipescript io mdpf_aggregate_aua.py`
returned `READS: (none detected) / WRITES: (none detected)` with a WARN that manual review was required. The
TO encodes that tool's silence as a **STOP trigger**. I did not fire it: *an instrument that detects nothing
at all — including reads that certainly exist — has not made a negative finding.* Checked the premise at
source instead; the override path is intact and firm-agnostic (`:177`, `:459-461`, `:1141-1150`).

**Both source caveats resolved by enumeration.** The TO warned explicitly not to construct paths.
`eclipse/inflection/silver/` carries model composition only; `orion/` carries custody ⇒ orion. `fact_assets`
vs `fact_positions` is **moot** — both carry every needed column and return byte-identical sums (though they
are near-duplicate tables, which is its own smell).

**The measurement.** $50,615,505 actual vs a $58,266,276 estimate — **−13.13%**, against a TO acceptance bar
of "~1–3% down, PFOE most", **with DIVZ moving UP**.

**So I tested the join instead of shipping it,** because acceptance #2 says a move of the wrong magnitude
means the join is wrong: 0 duplicate `(account, ticker)` rows of 2,330; `currentValue == shares × price` on
2,330 of 2,330. **The join is sound — the bar is stale.** The time series shows why: the ETFs are mid-ramp
into these accounts ($293k Jan → $12.1mm May → $52.3mm today), so the estimate measures *intent* against a
book still transitioning toward it, and DIVZ — ramped furthest — sits nearest target.

**Then the finding that ended the build.** The TO's target prefix `platinum/mdpf/aggregate_aua/` holds
**zero objects**. Not deleted — archived 2026-08-06T21:42:09Z, last data 08-05, with a live per-firm
successor carrying no ETF decomposition at all. I did **not** conclude absence from one key (the firm-scope
error I nearly made earlier tonight): swept all 484 objects under `platinum/mdpf/`, of which **40 live
non-archive JSON, 0 containing any of the four tickers / `attribution_basis` / `target_weight`, 0 read
failures** — with a **positive control** proving the same scanner finds all six tokens in the archived key.

**The defect was retired by supersession, not by fix.** Building the feeder would have landed correct code on
a consumerless path.

## What I did not do

Did not build. Did not close the TO. Did not re-point it. Those last two are the same line held all night:
surfacing is mandatory, adjudicating scope is not mine. CTO ruled do-not-build (231610Z) and recommended
closing OVERTAKEN with this measurement as the deliverable; COO confirmed the stop and owned the flip.

## The thing worth keeping

Both defects tonight in this TO — the stale acceptance bar and the superseded target — are **one class: a
fact that was true when written and was never re-tested.** COO named it in their own miss (treating "pending,
no gate" as evidence of readiness rather than as an unread question). The TO's §2 even documents a third
instance: a materiality threshold that "was reasonable when set and silently expired as the exposure grew."
Three instances of the same shape in one document.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-pipescript io` | `mdpf_aggregate_aua.py --pipeline mdpf` | **`(none detected)` for both reads and writes** — undiscriminating, not a negative finding. Routed by CTO to the instrument-repair queue with this file as the fixture. |
| `comp-find` | `"partner_held_etf"` | 383 hits / **27,060 files scanned**; located the 49F feeder + the aggregator consumer, and surfaced its **two independently-editable homes** |
| `comp-find` | `"aggregate-aua-timeseries"` | 1,506 hits / 27,069 files; identified `dim_mdpf_aggregate_aua_timeseries.py` as the live successor producer |
| `safe-commit.sh` | measurement deliverable | `600c5e0a33` |

*(Raw `aws` calls carried inline `# rail-checked:` markers — partition/prefix enumeration and S3
`LastModified`, none of which a comp-tool covers.)*

## Banked, no action taken

- `wsd_partner_held_etf.py` in **two independently-editable homes** — Rule 22a's one-producer-two-homes shape.
  CTO routed it as instance #3 of the night to the 0.8.0 T4 census.
- `mdpf-feeder-accelerator` carries `ScheduleExpression: None`.
- `fact_assets` / `fact_positions`: two near-duplicate silver tables, same grain, identical content.
