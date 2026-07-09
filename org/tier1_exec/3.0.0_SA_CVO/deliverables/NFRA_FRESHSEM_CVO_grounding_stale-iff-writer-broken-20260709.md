# NFRA_FRESHSEM -- CVO grounding: "stale IFF a writer is broken" (the freshness-semantics footgun)

**Author:** 3.0.0_SA_CVO~B  ·  **Date:** 2026-07-09  ·  **Class:** grounding-finding (source-confirmed)
**Routes to:** 0.7.0_AE_CloudOps (builder -- owns needs_refresh debounce + incremental stitching), 1.0.0_SA_CTO (arch-gate), 2.0.0_SA_COO~B (coordination)
**Andrew's directive (this session, verbatim):** "stop footgunning and defining freshness as only when nessie resets in the early morning ... we should only refer to a head of kuzu as stale if the incremental writer is broken or if nessie fails to write with the early morning full reset." / "It's only stale if a writer is broken, yes." / "if incremental writes and full reset writes are working as designed, its not stale." / applies "at the cloud graph level nessie/iceberg as well as locally on the kuzu db projection."

## The thesis (Andrew), restated as an acceptance property

The graph -- at BOTH levels (cloud Nessie/Iceberg, local Kuzu projection) -- is STALE **iff a writer is broken**:
- the incremental writer (SQS -> `incremental_updater` Lambda) is down/erroring, OR
- the nightly full-reset/derive (`derive_runner`) failed to write.

**Corollary (the footgun):** a healthy incremental writer ADVANCING HEAD is the writer *doing its job*. The local projection being BEHIND that HEAD is a NORMAL, transient, self-healing lag -- **not** staleness. Calling it "stale" (or churning a rebuild on it) is the mis-definition.

## Grounded mechanism (source-confirmed -- file:line, not inference)

1. **The refresh trigger is whole-graph HEAD-POSITION, not writer-health.**
   `_canonical.needs_refresh` (`infra/aws/globgrph/_canonical.py:78-84`) returns `True` on
   `_nessie_head_status(...) == "behind"`. That status (`_provenance.py:133-154`) is defined as
   `pin graph_nodes snapshot_id != HEAD graph_nodes snapshot_id`. So the local canonical DB rebuilds
   on **any** pin!=HEAD -- i.e. on EVERY incremental-writer commit that advances the marker. The trigger
   never consults writer-health. This is the churn Andrew observed ("why are you constantly rebuilding
   nessie locally? third time I've seen a full derive").

2. **The human header WARNs off the SAME position signal.**
   `_provenance` header rendering (`_provenance.py:318-324`) emits `WARN: BEHIND Nessie HEAD` whenever
   `_nessie_head_status == "behind"`. So a healthy writer advancing HEAD surfaces to every agent as a
   staleness WARN -- the exact conflation the thesis forbids.

3. **The writer-health oracle ALREADY EXISTS -- but is display-only.**
   FRESHGUARD leg-4 (`_provenance.py:159-163`, `:239-250`, `:325-331`) stamps per-table
   `last_write_iso` into the branch-head marker (= the table's current-snapshot timestamp). This is the
   AUTHORITATIVE per-table freshness: a stalled SOLE-writer (a frozen `derive_runner` -> `graph_edges`)
   reads per-table STALE even under a fresh `committed_at` / advancing pin (a light cse/incremental
   writer "can't mask it"). **But `last_write_iso` is consumed ONLY by `_per_table_vintage_lines` for
   the human header** (`:330-331`) -- it is NOT fed into `needs_refresh` (the rebuild decision) NOR into
   the `WARN: BEHIND` label decision. The signal that would separate "healthy-lag" from "writer-broken"
   is computed and then discarded at the two points where the decision is actually made.

## The gap (what Andrew's thesis requires that the code does not yet do)

**Decouple REFRESH from STALE. They are triggered by one position signal today; the thesis needs two independent decisions:**

- **REFRESH (catch the local projection up):** on behind-HEAD is FINE and should be SILENT + CHEAP + NORMAL -- never a WARN. Already made cheap: DELTA-default-on is CERTED (Tier-1, `kuzu_incremental_refresh.py`; `_canonical.py` gating `!= "0"`), so catch-up is a delta-apply, not a ~6min full-derive; the incremental STITCHING 0.7.0 is building removes the on-query catch-up entirely (the local DB applies the same SQS writes continuously). Refresh is close to solved.

- **STALE (the alarm-worthy state):** must be gated on WRITER-HEALTH, not whole-graph pin-position:
  - **local:** the marker's per-table `last_write_iso` older than that writer's expected cadence (incremental: minutes; derive: ~24h) -- the signal that already exists, just not wired into the decision.
  - **cloud:** SQS DLQ depth > 0, `incremental_updater` Lambda error-rate > 0, or nightly `derive_runner` failure. (These monitors exist and were validated GREEN this session -- SQS 0/0 DLQ 0, Lambda 102inv/0err; the derive-non-delivery alarm was found flapping and routed to base COO. The cloud-level thesis maps onto these writer-health monitors, not onto a rebuild.)
  - **decision:** "behind HEAD but all writers fresh" => self-healing lag (refresh via stitch/delta, do NOT WARN, do NOT alarm). "per-table `last_write_iso` beyond cadence, OR DLQ>0, OR derive failed" => STALE (WARN + alarm). This is `needs_refresh` returning a THIRD state, or the header WARN keying off writer-health instead of pin-position.

## Already-done vs missing (so the builder isn't re-solving solved parts)

| Piece | State |
|---|---|
| Cheap catch-up (delta not full-derive) | DONE -- DELTA-default-on CERTED (Tier-1) |
| Continuous local currency (no on-query catch-up) | IN FLIGHT -- 0.7.0 incremental stitching |
| Per-table writer-health signal exists | DONE -- `last_write_iso` (FRESHGUARD leg-4) |
| Cloud writer-health monitors | EXIST + validated GREEN (SQS/Lambda/derive-alarm) |
| **Refresh trigger gated on writer-health (not pin-position)** | **MISSING -- the finding** |
| **Header "stale/WARN" gated on writer-health (not pin-position)** | **MISSING -- the finding** |
| needs_refresh debounce (don't churn a rebuild per advance) | 0.7.0 todo #14 (P3) -- this finding is its grounding |

## CVO disposition

- This is a **source-confirmed mechanism** (every claim cites file:line), so per Rule 22 it authorizes a finding + routing -- it is NOT an ungrounded hypothesis. It does **not** authorize a fix in this lane: the BUILD (wire `last_write_iso` + writer-health into the refresh/WARN decision; add the debounce) is 0.7.0_AE_CloudOps's, arch-gated by CTO.
- **CVO cert bar when it lands** (against Andrew's thesis, EXERCISED not config-read): (1) with all writers healthy, an advancing HEAD produces NO "stale/WARN" label and NO full-derive churn -- exercised by a real head-advance, header shows current/self-healing, not WARN; (2) a genuinely-broken writer (inject: a per-table `last_write_iso` beyond cadence / a non-empty DLQ / a derive-fail) DOES flip STALE+alarm -- exercised by the injected break, header REDS. Same discipline as the freshness Tier-1 cert: prove the signal BITES on the real degenerate case, and prove it does NOT false-fire on the healthy-lag case (the footgun).
- Ties to task #8 (freshness semantics + verify 0.7.0 stitching, both levels) and the Tier-2 reconcile-oracle wiring cert (pending 0.7.0 land).
