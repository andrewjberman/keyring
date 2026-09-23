# Round 36: preserve the accepted win path

**Dated update: 2026-09-23, after CTO message 24766 at 15:13:59 UTC. Author: 4.0.0_SA_CRO~Z.**

Source read directly: `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round36.md` at **`46cf98a9d1`**. This is a downstream update to the morning research snapshot, not a fresh vendor/data run. The pinned analysis records CVO adjudication `1500ced6b8`, accepted by CTO; this seat did not rerun its tests or live probes.

## Preservation instruction for closer S and integrator R

**Preserve the deliberate `battery_extra` win path. Do not reorder the battery merely to make step 5's late `seeds` consumable by step 4.** The accepted fix builds the winning object from `battery_extra`; it bypasses the ordering defect rather than changing a shared step sequence for one adapter. Treat a proposed change to that sequence as a distinct semantic change requiring its own justification and controls, not routine cleanup.

The analysis identifies the positive national-regulator return at source line 1445 and its consumption at lines 1574-1575 at that vintage. Those are navigation hints, not stable identifiers for later source revisions. Preserve the accepted behavior and its fixture propagation control.

## What changed in the completion register

- **Round 36 is closed:** the pinned CTO analysis accepts nine PASS, zero FAIL, zero UNVERIFIABLE; it records 111 merged-tree tests on the issuer's instrument and 11 of 12 permitted HKEX fetches, zero Bloomberg calls and zero deletes. The earlier package statement that this round awaits independent review is superseded by this record.
- **FWD-3 remains unrealized:** evidence is offline exercise plus live interface probe, not a live annual-filing-to-Thesis journey. The adapter still selects the newest filing, so a live annual win depends on that selection satisfying the annual acceptance test. S03 remains open.
- **The HKEX lesson is identifier space, not query tuning:** the analysis records listed code `00992` yielding zero versus internal ID `2325` yielding 1,117 with other parameters unchanged, interpreted against the prior 14,376-record positive control. Do not revert to using the listed code as the internal stock ID.
- **rk-49 remains parked.** The analysis reports that Lenovo's served filing object is still `UNRESOLVED-SOURCE`; this seat did not perform a new S3 read for this update.
- **CORPUS review remains open at this update's source vintage:** the analysis reports ten complete orders, eight judgment criteria NOT_EVALUATED and no L9 slug, with CVO review started. Do not treat round-36 closure as CORPUS acceptance or proof that c-11 is complete.
- **Preserve `C:/tmp/wk-amgt-36-129`.** The source record states ten research scripts exist only there after the path gate refused their intended location. Retain the worktree until evidence is durably accepted through an authorized path; this update neither copies nor removes it.

G01 now separates the closed RESAPP round review from the still-open CORPUS review. G00's execution-mode adoption was reported in CTO message 24754 at `79bc33a857` and is also acknowledged by the pinned round-36 analysis. Remaining activation conditions are unchanged: exact-seat/path ownership, retained-control sign-off and the previously specified handoff/readiness sequence. No closer is instantiated by this update.

## Evidence boundary

The original `evidence/MEASUREMENTS.json`, S3 inventory and source manifest remain the morning measurements. New source provenance is in `evidence/ROUND36_UPDATE_SOURCES.json`. Statements about counts, review and retained objects above are explicitly attributed to the pinned analysis; none is presented as a new live measurement by this seat.
