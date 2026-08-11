# 49F canonical window backfill — one-time historical fill (OPEN 2026-08-11T17:50Z)

**Owner:** 0.4.0_DS_ClientPlatform
**Authorization:** COO GO 20260811T174515Z (bounded one-time historical fill; explicitly NOT P2 —
"a historical fill of gold window partitions is not a schedule change; it is completing P1's
outputs"). Standing behind it: Andrew ~1742Z VERBATIM "Recs approved" (@745ca6d78f) — Schwab-08335338
canonical AUTHORITATIVE for 49F; the $122.5M DIVERGE-SOVEREIGN RULED-ACCEPTED. Cost basis:
the COO-authorized 20-date timing sample (59/59 rc=0; ~15 min warm extrapolation, stated as an
extrapolation with uniform-cost assumption).

## Scope (the GO'd act, nothing more)
Three chained per-date fills using EXISTING P1 code (no new code beyond the driver loop):
- B_00 canonical_valuation x every silver dim_balance date partition (526 expected)
- C_00 flow_ledger x every silver fact_trn date partition (525 expected)
- C_02 twr_engine x every date whose D-1 valuation exists post-fill (per A_04 calendar prev map)
Writes: `s3://opal-data-assets/schwab/08335338/gold/canonical/{canonical_valuation,flow_ledger,twr_daily}/date=*/`
(B_00/C_00 via runner emit --upload with read-back verify; C_02 table per its emitter).

## Bounds (COO 174515Z, verbatim adopted)
- ONE-TIME. NOTHING STANDING: no trigger, no schedule, no comparator, no shadow path. The
  go-forward path remains the SCHEDULED run; production numbers come from it.
- ZERO served surfaces: no repoint, no publisher change, no platinum write. Serving cutover is
  P3/P4 and carries never-widen (CTO+COO).
- B_01 x 525 NOT run (explicitly excluded — not required for the gated families).

## Declarations
- BOUNDARY RETRO-APPLICATION: historical partitions carry the 2026-08-07 A_02 boundary artifact
  (one full-history-predicate artifact), boundary_version stamped per-row — the declared choice
  from the 163847Z scope, now exercised under the GO.
- IDEMPOTENCY: overwrite-all. The 40 QA partitions from the timing sample (2025-05-05..2025-06-02,
  B_00+C_00) are overwritten for a uniform fill vintage; content identical by construction modulo
  provenance timestamps.
- LOCAL DIM FAN-OUT: boundary/ref artifacts are staged locally per-date for the runners'
  --*-local paths (the A-group dims are not yet uploaded to S3 gold — reported 171054Z surprise (a);
  the dims-upload leg is a separate act, not smuggled into this one).

## ROLLBACK (stated before the first write)
Prefix delete of the written date partitions:
`aws s3 rm --recursive` over `schwab/08335338/gold/canonical/canonical_valuation/`,
`.../flow_ledger/`, `.../twr_daily/` (each partition self-contained with manifest beside it;
zero consumers exist today — the platinum publishers are P4 scope and nothing reads these keys).
S3 object deletion requires human confirmation per Agent Autonomy — rollback is therefore
DECLARED-AND-ESCALATED (COO fires it or confirms it) rather than unilaterally executed.

## Verification plan (verify on the RE-READ, never the write rc)
- Per-chain partition counts with denominators (written / expected).
- Re-read sample: N random partitions per chain re-downloaded and row-counted vs manifest.
- C_02 REFUSED-NO-BMV census: only the earliest date (no D-1 in domain) may refuse.

## Carried obligations (CVO, recorded now per COO 174515Z)
(a) RE-PIN AT THE SERVING CUTOVER: today's pins verify new-vs-OLD-BD-serve deltas ($122.5M
    class). At P3/P4 cutover to Schwab-canonical the pins re-base to ~0 — a stale pin must
    fail LOUD so the cutover cannot drift silently. (The pinned-delta design already fails
    loud on stale pins; this line makes the re-base act explicit cutover scope.)
(b) The per-account migration control stays current per vintage (962 legacy out / 1,687
    Schwab-only in, identity -$0.00) so no account silently drops on cutover.

## Status
- OPENED 17:50Z, fill driver launched (background). CLOSE requires: counts + re-read verify
  printed below, zero unexplained refusals, evidence tee'd to scratchpad xwalk/.. timing/..
  fill logs.

## FILL-1 COMPLETE (~18:12Z) — INTERIM; ledger stays OPEN through fill-2 (COO ruling 175737Z)
- B_00: 526/526 rc=0 (478s) | C_00: 526/526 rc=0 (512s) | C_02: 525/525 rc=0 (82s process-grade)
- RE-READ VERIFY: canonical_valuation 526 S3 partitions, 3/3 sampled re-reads TIE rows==manifest;
  flow_ledger 526 partitions, 3/3 sampled re-reads content-coherent (identity_in_eq_out True).
- ⚠ C_02 CONTENT FINDING (process count != content count): its main is still the single-partition
  exercise — the D-1 wiring "arrives with Group W" LITERALLY; all 525 runs emitted REFUSED-NO-BMV
  refusal records (LOCAL only; C_02 has no S3 leg). The 525/525 is process truth, not TWR content.
  Remedy folded into fill-2: build the D-1 loading path (P1 output completion, same class).
- SURVIVORSHIP MEASURED (reported 175426Z): day-one 867/4,075 (~21%) excluded by the retro boundary.
  COO RULED 175737Z: re-fill on CONTEMPORANEOUS A_02-per-date boundaries, OVERWRITING; no second
  standing artifact; positive control = the runner's 'rows==boundary NO -- investigate' marker
  GOING QUIET on historical dates.
## FILL-2 SCOPE (same bounds; rollback unchanged)
- A_02 per-date boundary build (truncated leg sweep: legs <= D — a --truncate flag on a02, no
  future information in a historical boundary), locals only (dims-upload stays a separate act).
- B_00 + C_00 re-fill overwriting (declared idempotency); C_02 re-fill WITH the D-1 wiring.
