# ANDREW-DIRECT (verbatim) — 2026-07-14 ~07:2xZ, Claude Code session direct to 0.5.0_AE_OpalETL

**Channel:** mid-turn user message in 0.5.0_AE_OpalETL's Claude Code session.
**Received by:** 0.5.0_AE_OpalETL. **Recorded same turn; broadcast to COO + CTO + MSTR same turn.**
**Context he was responding to:** my claim commit `eab9c6693` had restored the SmartX client's default
rate limit to 17/min pending CTO ratification of the crashed session's unreproducible re-measure.

## Verbatim

> no requests per minutes should be like significantly higher, we got away with 35 per second when
> we did the backfill, dont waste time with 17 requests per minute are you serious? be for real

## Scope note (SURFACE, NOT ADJUDICATED)

- Settles the SmartX rate-limit question by sovereign word: the 17/min inherited "vendor ceiling"
  is dead; the rate is to be significantly higher.
- **Corroborates the crashed session's measurement**: "we got away with 35 per second when we did
  the backfill" — 35/s == 2,100/min, consistent with the session's claimed x32 probe (2,357/min).
  Andrew's word is the grounding the crash-lost probe artifact couldn't carry.
- **Reveals the backfill already RAN** at that rate — the C5 "remaining: backfill orchestration"
  picture is stale; live S3 denominators to be re-read before the data-shape plan states coverage.
- Applied: `smartx_client.py` default = 600/min (10/s; ~3.5x under the demonstrated 2,100/min),
  env-overridable for backfill pushes; 429 retry/backoff stays armed. `backfill.py` docstring's
  17/min CTO-attribution updated to cite this ruling.
- Supersedence chain on this constraint: D4 §8.7 inherited ceiling → CTO Q6 ruling (premised on
  that ceiling being a vendor fact) → **this Andrew-direct ruling (governing)**.

## Clarification (same channel, minutes later, verbatim) — GOVERNING FORM OF THE RULING

> I don't think you really get it, we're not rate limited so stop saying we are. The limit was
> more likely i/o to s3

- **There is NO vendor rate limit.** The "rate limit" framing itself is dead, not just the number.
  The observed throughput ceiling (269/min sequential → 2,357/min at x32; ~35/s on the real
  backfill) is most likely **our own S3 write I/O**, not SmartX.
- Applied (supersedes the 600/min default from the first message): `smartx_client.py` pacing
  **DISABLED by default** (`SMARTX_RATE_PER_MIN=0` = unpaced; the TokenBucket short-circuits).
  The env knob stays as a dormant safety valve only; `SMARTX_MAX_WORKERS` is the throughput
  lever; 429 remains in the ordinary retry set as client hygiene, not as "the vendor limit."
