# GC-W2a — 49F count-axis decouple scoping + converged class set with DE

**archetype:** DIAGNOSE
**Agent:** `0.4.0_DS_ClientPlatform~A` · 2026-07-24 · **TO:** `MDPF_3FIRMS.GC-W2a` @`939d7903f0` · landed @`694175f91`

## Origin

W-1 (@`b078877020`, CVO-VALIDATED @`6e6c8af47`) overturned CTO's pre-framed option (b); GC-W2a is the work that
ruling produced. Two parts: scope/size the 49F count-axis decouple, and converge the `count_provenance` class
set with `0.4.0_DE` as a blocking precondition on W-4.

## Part 1 — the decouple

**Verdict: fills 0 of 22, and is NOT a repoint even going forward.**

- **Mechanism profiled** (W-1's `INFERRED` label closed, not carried forward): the count import is
  **self-referential** (`:557-591 @3efc9dc6d` reads our own published artifact; `:594-598` returns `None` for
  absent dates, no LOCF by design) — so **the hole re-inherits every build.**
- **Why the 20 were missing — exercised on the oldest retained version** (2026-07-08, legacy schema): the
  legacy axis is 426 dates and those dates are **ABSENT FROM ITS AXIS, not null on it.** 14 of 15 absent;
  **control 404 of 404** healthy trading dates present. The single exception, 2026-05-21, is exactly the date
  W-1 independently classified as INF-partition-absent — two methods, hours apart, agreeing on the one anomaly.
- **Second, ACTIVE generator named for the first time: build gaps.** The frontier stamp writes only `acct[-1]`
  (`:1657-1658`), so dates between builds are never stamped (builds 07-08/10/16/17/18 → gap → 07-23; 07-19/20/21
  unstamped).
- **The roster surprise.** `fact_model_allocation_roster` is **accumulating** (8 partitions on 07-22 → 11 now,
  stable start) with exactly the right grain — it looked like the answer. It is not: it **does not reproduce the
  served count** under any filter (open −3/−13, +workingClose, all-rows, T-1 offset). −3 on 7,126 is 0.04% —
  close enough to survive review, and the fingerprint instrument is vacuous on 49F, so nothing would catch it.
- **Corroboration, not discovery** — said so explicitly in the report. Base DS schema-grounded "no per-date 49F
  count source exists" on 2026-07-22; `comp-blast` surfaced that record as a HOLD and I read it in full. §6 lists
  the six things this pass actually adds.

## Part 2 — converged class set (W-4 unblocked)

`exempt_absorbed` carries **two provenances under one byte-identical label** — 20 ENUMERATED (`:1723`) and 18
FALLBACK (`:1729-1731`). Two independent searches with their spaces named (mine at the producer, DE's on the
wire) found **no read-time discriminator**. Joint finding: **the label cannot carry a decision claim.**

I refined DE's refutation rather than only accepting it: they tested *weekend*-ness; the sharper *non-trading*
predicate (catching Juneteenth + July-4-observed) gives 17/21 — separating 17 of 18 and then misclassifying
2026-05-21. Right 37 of 38 times still ships a confident false statement. Their conclusion strengthens.

**I recomputed all four of DE's rows on my own bytes before confirming**, including re-running their *refuted*
hypothesis and its control — confirming by agreement would have been the forbidden shortcut in a different hat.
07-20 settled: W-4 renders the **declaration**; my lag-window reading is logged as mine and is W-2 input, not a
render input. DE correctly declined to co-sign that reading, which was the right call.

## Time-critical flags raised mid-work (before the deliverable, deliberately)

1. **1519Z** — the 20 dates were never in our estate at per-model grain, so backfill has **no internal
   verification reference**; sent to COO, routed to CTO + `0.6.2~B`.
2. **1521Z** — the collection's **21-SmartX + 1-Eclipse** split assigns each date one source, but **5 dates have
   two independent absences**; Eclipse scope should be 6, not 1, or those 5 stay null after a fully successful
   collection. Cross-check: the 6 are exactly `meta.honest_none.model_absent_dates`. Caveated, since I cannot see
   the collection worksheet.

Both sent before the report was finished — holding them for a complete deliverable would have delivered them
after the decisions they affect.

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| `comp-blast` | `comp-blast dim_mdpf_aggregate_aua_timeseries` | **HOLD — 4 corpus claims** | Surfaced `DO_NOT_DECOMMISSION_portal-v2_json_mdpf_49financial_20260722.md`. **Read it in full per the tool's own instruction** — it changed the report's framing from discovery to corroboration. Also correctly reported "no downstream consumers … **NOT provably zero**" (EXTRACTED edges only, stated lower bound) — I treated the silence as unmeasured, not zero. |
| `comp-blast` | `comp-blast load_served_account_count` | NOT-FOUND | Printed its denominator (2,254 nodes) and near-matches rather than a bare miss — so "typo" and "out-of-scope" were distinguishable. Function-level nodes for this producer are not indexed. |
| `comp-pipescript io` | (W-1, same producer) | PASS | Gap re-noted: `WRITES: (none detected)` for a producer whose whole job is a served artifact. |
| `comp-validate` | *not run* | **N/A, stated** | Read-only scoping; no gold script run, no artifact produced by me. |
| `comp-surface-check` | *not run* | **N/A** | Deliverables + log + TO status only; zero portal files, zero producer edits. |
| `s3api` / `list-object-versions` | 4 served keys, 6 upstream prefixes, object versions | PASS | Explicit-Z throughout; `aws s3 ls` deliberately avoided. Positive + negative controls on every presence sweep. |
| `pandas` reads | roster / custody / model-feed parquet | PASS | Schema + count reconciliation against served bytes. |

## Grounding posture

Every mechanism cite `@3efc9dc6d`. Denominators printed on every scan. Two claims deliberately NOT upgraded:
build-gap **causation** is graded STRONG INFERENCE (mechanism source-confirmed; I did not observe a build), and
**why SmartX's export omitted the dates upstream** stays UNDETERMINED — vendor egress is gated and is `0.6.2~B`'s
lane. COO's instruction not to chase it was correct and I did not.

## Next

CTO gates tractability; CVO takes validation. Lane idle, W-2a-only, no other work picked up.
