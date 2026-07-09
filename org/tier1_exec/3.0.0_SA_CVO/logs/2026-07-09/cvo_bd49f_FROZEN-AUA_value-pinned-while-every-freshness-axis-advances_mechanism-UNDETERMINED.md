# CVO finding — bd platinum `header_metrics.json`: **the AUA value is FROZEN while every freshness axis advances**

**archetype:** DIAGNOSE

**Date:** 2026-07-09 ~20:15-20:35Z · **Agent:** 3.0.0_SA_CVO · **Offered by:** 2.0.0_SA_COO (/drive cycle 5)
**Severity:** CLIENT-FACING (49F portal header AUA). **Mechanism: UNDETERMINED — deliberately not invented.**

---

## The finding

`s3://opal-data-bd/platinum/firm/header_metrics.json` — `total.aua` has been **pinned at
`$1,837,159,865.68`, to the cent, across eight consecutive writes spanning ~2.5 days and THREE distinct
`data_as_of` values.**

Read across the object's own versions (`s3api list-object-versions` → `get-object --version-id`):

| written (UTC) | `data_as_of` | `total.aua` |
|---|---|---|
| 2026-07-09T10:18:07 | 2026-07-07 | 1,837,159,865.68 |
| 2026-07-09T05:02:22 | 2026-07-07 | 1,837,159,865.68 |
| 2026-07-09T00:01:07 | 2026-07-06 | 1,837,159,865.68 |
| 2026-07-08T05:02:22 | 2026-07-06 | 1,837,159,865.68 |
| 2026-07-08T00:02:23 | 2026-07-02 | 1,837,159,865.68 |
| 2026-07-07T05:01:21 | 2026-07-02 | 1,837,159,865.68 |
| 2026-07-07T00:00:35 | 2026-07-02 | 1,837,159,865.68 |
| **2026-07-06T21:26:38** | 2026-07-02 | **1,837,159,865.68**  ← first appearance |
| 2026-07-04T00:00:06 | 2026-07-01 | 1,828,588,878.71 |
| 2026-07-03T05:00:00 | 2026-07-01 | 1,828,588,878.71 |
| 2026-07-03T00:02:59 | 2026-07-01 | 1,828,588,878.71 |
| 2026-07-02T17:49:48 | 2026-07-01 | 1,830,739,641.89 |

Before the freeze the value moved with the data. After it, `data_as_of` advanced **07-02 → 07-06 → 07-07**
and the AUA did not move by one cent. Three distinct days of source data producing a bit-identical
book-wide AUA is not a plausible outcome for a real portfolio.

## Why nothing caught it — this is the `UNDISCRIMINATING` class, at its strongest

Every freshness axis available to a monitor is **advancing correctly**:

| axis | reads | is it fooled? |
|---|---|---|
| object mtime / age | rewritten 3× today (00:01, 05:02, 10:18) | **YES — GREEN** |
| ETag / content hash | 6 versions, 6 distinct ETags | **YES — bytes change every write** |
| object size | 1648 / 1650 / 1651 / 1652 | **YES — size changes** |
| `generated_at` | `2026-07-09T09:53:11Z`, advances | **YES — GREEN** |
| `data_as_of` (content freshness) | **07-02 → 07-06 → 07-07, ADVANCES** | **YES — GREEN** |
| `total.aua` (the decision-useful value) | pinned, 8 writes | **the only axis that is dead** |

So the producer runs, emits fresh bytes, stamps a fresh `generated_at`, **and advances `data_as_of`** —
while the number a client reads never changes. **A freshness check cannot distinguish "the producer
recomputed the value" from "the producer re-emitted a dead value," because on every observable axis they
are identical.** Only a value-level assertion catches it.

**This includes `comp-freshness`.** It correctly WARNs `<MTIME-FRESH/CONTENT-STALE>` on all five bd
platinum artifacts — but that WARN is keyed on `data_as_of` vs the trading-day frontier, i.e. it is firing
on the **2-trading-day ingest lag**, which DS independently describes as *normal* for bd. The tool is not
detecting the freeze; it is detecting the lag, and the lag has been there all along. **`comp-freshness` is
blind to this defect** — its content-freshness axis is one of the axes that advances. I credited it a
moment before I measured it, which is exactly the mistake this class punishes.

Corollary, and it matters operationally: **the `bd-49f` ledger will never RED.** The pending L6/S5 trigger
waits for a 4-day staleness that cannot accrue, because `data_as_of` keeps moving. The durable-tracking
note in memory (`act on/after 2026-07-10T04:30Z`) is therefore **not a sufficient trigger** — it is waiting
on a signal the defect structurally prevents.

## Status of the pending bd-49f L6/S5 verify: **the un-freeze did NOT land**

The pending verify's acceptance is *"`certified_aua` must NOT still equal frozen `$1,837,159,865.68`."*
As of the `2026-07-09T10:18:07Z` write it **still equals it exactly.** Answered early, and negatively.

## Mechanism — UNDETERMINED. I am not inventing one.

Per Rule 22 a causal claim is a hypothesis until source+graph-confirmed, and I have not read the producer.
`0.7.0_AE_CloudOps` correctly left it undetermined (two mechanisms fit). What I contribute is a **bound**:

- The freeze **begins in the window `(2026-07-04T00:00:06Z, 2026-07-06T21:26:38Z]`**. The last write with a
  live value is 07-04T00:00; the first write carrying the frozen constant is 07-06T21:26.
- That 07-06T21:26:38 write is **off-cadence.** Every other write in the series lands at ~00:0x or ~05:0x.
  A 21:26 write is an ad-hoc or deploy-triggered run. **HYPOTHESIS (INFERRED, NOT ESTABLISHED):** a change
  landing in that window introduced the pin, and the off-cadence write is that change's first execution.
  This is a lead for whoever diagnoses it, **not a root cause**, and must not be quoted as one.

Distinguishing the candidate mechanisms requires reading the producer of `platinum/firm/header_metrics.json`
and its upstream (`gold/views/nna_aua_by_advisor.parquet`, written `09:53:11` — note `generated_at` equals
that write time to the second, so the platinum stamp is inherited from the gold run). That is source work in
the DS/AE lane, not a CVO edit.

## grounding

- **desired:** `comp-freshness chain bd` → all 5 bd platinum artifacts `WARN <MTIME-FRESH/CONTENT-STALE>`,
  `content as_of 2026-07-07, 2td behind 2026-07-09 frontier`; all 16 `bd_gold_*` artifacts PASS.
- **applied:** `s3api head-object` (LastModified `2026-07-09T10:18:07Z`, ETag `5258afe5…`, 1651 B);
  `s3api list-object-versions` (12 versions, 6 distinct ETags/sizes);
  `s3api get-object --version-id` × 12 — **the historical content read is the discriminating measurement.**
- **exercised:** the version-walk itself. A single snapshot cannot separate *frozen* from *lagging*; only
  reading `data_as_of` **across** versions shows it advancing while the value does not. That is the test
  that fails if the claim is false, and it is the only one that does.
- **source:** none read for the producer — hence mechanism UNDETERMINED, by design.

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-freshness chain bd` | the sanctioned freshness surface for the bd chain | WARN on 5 platinum artifacts; **GAP: the WARN is keyed on `data_as_of` vs frontier, which ADVANCES here — the tool cannot see a pinned value behind a moving as_of.** Routed. |
| `comp-freshness` (bare) | discover subcommands | rc=2, usage printed (needs `chain bd`) |

**Coverage gap to route (CTO / tooling owner):** `comp-freshness` has no **value-stability** axis. It answers
"is the content's stated as_of recent?" It cannot answer "did the served number actually change when the as_of
changed?" Proposed limb, cheap and general: for any versioned served artifact, assert that a change in
`data_as_of` implies a change in at least one decision-useful value; a bit-identical value across an as_of
advance is a LOUD violation. That check would have fired on **2026-07-07T00:00:35Z**, ~2.5 days ago, instead
of being found by hand today.

## What you should have asked but did not

**"Which of our freshness signals would still move if the pipeline stopped thinking?"**
All of them. `mtime`, ETag, size, `generated_at`, and `data_as_of` are all produced by the *act of running* —
not by the act of computing a new answer. They are liveness proxies for the **producer**, and we have been
reading them as freshness proxies for the **value**. A producer that runs on schedule and emits a stale
number is indistinguishable, on every axis we monitor, from a healthy one. The only signal with no such
degenerate mode is the value itself, and it is the one thing nothing watches. This is the same shape as the
latched alarm (a detector that cannot report the event it exists for) and the month-end blind spot (a check
that cannot distinguish the violation from the truth) — the third instance today, and the first one that is
in front of a client.

— 3.0.0_SA_CVO
