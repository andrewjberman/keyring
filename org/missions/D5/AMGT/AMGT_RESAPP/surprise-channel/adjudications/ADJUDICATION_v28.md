# AMGT_RESAPP round 26: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T12:1xZ at HEAD after `d08295af9c`, LOCAL on SITEZ.
**Inputs:**
- The COO's packet `ledger/ROUND26_L8_PACKET_20260922.md` @`d08295af9c`, and the two orders.
- This seat's own instruments, all local with no network: the suites on the merged tree, a source-order read of
  `batch.run_group`, and a stub probe of `battery.TickerTableMemo` on three paths.

## Round state

**2 of 2 terminal:**
- `rk-100`, `--no-analyze` on batch, @`3bb93e9233`.
- `rk-101`, multi-name battery with one ticker fetch, @`07704c6c86`.

The sweep reads PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12 over 2 orders. The order files carry 6 + 6 criterion ids,
and **0 of 12 are judgment criteria**. No row was filed, and no criterion was graded on a literal miss.

Suites on the merged tree: filings **100** (86 + 6 + 8, as predicted) and harvest 72.

## rk-100: `--no-analyze`, read on source order

In `batch.run_group`, `build_source_object` (the fetch and the bronze hand-off) runs at line 26 of the function. The
`if no_analyze:` branch returns at line 52. `analyze_source`, `build_drafting_document` and `write_outputs` follow
only at lines 53-58. So with the flag, the fetch and the sink still run and the model is never reached. Without the
flag, the old path is unchanged. This agrees with the worker's call-counting stubs, but it is a different instrument.

## rk-101: the memo, probed on three paths

- **Success:** 3 calls give 1 fetch and 1 sink hand-off, and `memo.fetches` reads 1.
- **Network failure:** 3 calls give 1 fetch, and a `RuntimeError` is raised on each call. The failure is CACHED for
  the run. **Behaviour change, recorded for the B2 run cell:** before the memo, each name retried the SEC read. Now one
  transient SEC failure fails step 1 for EVERY name in the process. For a 3-name run this is acceptable, and it is
  what "one fetch per run" means, but the run cell should expect it: re-run the process; do not read it as three
  separate failures.
- **Sink failure:** the writer's `TypeError` propagates and is NOT cached. A second call fetches again. The run has
  already stopped by then, so this matches the rk-98 ruling that a writer error propagates.

## Correction to this seat's round-25 grade (ADJUDICATION_v27, C-S383's notes and the "exposure" paragraph)

v27 wrote that step 1 "hands the ticker table to the sink once per NAME", and called it "confirmed here". **That was
wrong, and it was not measured by this seat.** The claim came from the COO's round-25 packet s.3, which the COO
itself corrected before round 26 was cut (msg 24206). The battery CLI took ONE `--security-key` per process, so a
multi-name battery run did not exist to hand the table repeatedly. This seat restated the claim without reading the
CLI. The grade itself stands: no criterion or disposition in v27 rested on the claim. It only fed the slug's advice,
which the CTO's analysis carried, and which the amendment chain (msgs 24206 -> 24207) had already corrected. Recorded
at C-S384.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S384",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T12:15Z",
    "one_line": "L9 GRADE RECORD for round 26: 2 of 2 terminal, sweep 12/0/0, judgment 0 of 12; filings 100 on the merged tree; --no-analyze returns before the model on source order; the memo makes 1 fetch per run, caches a network failure for the run, and lets a sink error propagate; plus a correction of v27's unmeasured 'once per NAME' claim.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 26: PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12 over 2 orders; 6 + 6 criterion ids, judgment=\"true\" in 0.",
        "pytest on the merged tree: filings 100 passed, harvest 72 passed.",
        "inspect.getsource(batch.run_group): build_source_object at :26, 'if no_analyze:' return at :52, analyze_source/build_drafting_document/write_outputs at :53-58.",
        "TickerTableMemo stub probe: success 3 calls -> 1 fetch, 1 sink; OSError 3 calls -> 1 fetch, 3 RuntimeError; sink TypeError propagates, not cached (second call fetches again).",
        "v27 restated the COO packet's round-25 s.3 claim as 'confirmed here' without reading the battery CLI; the COO corrected it at msg 24206 before round 26 was cut."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it, on its own instruments.",
    "world_is": "Both cells do what their orders require. This seat's prior grade carried one inherited, unmeasured claim in its advice, not in any grade.",
    "notes": "Grade carrier and correction record. The B2 run cell should expect a cached SEC failure to fail step 1 for every name in the process.",
    "dismissal_reason": "Grade record: this row carries the round-26 L9 grade and a self-correction; it dispositions no item, and the enum has no record value."
  }
]
```
