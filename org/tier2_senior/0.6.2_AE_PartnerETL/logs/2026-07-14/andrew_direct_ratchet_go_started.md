# 0.6.2_AE_PartnerETL -- ANDREW-DIRECT ratchet GO (verbatim banked) + the ratchet STARTED

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, SCRIBE
**Date:** 2026-07-14 | **Window:** ~18:5xZ -> ~19:0xZ | **Serial:** 0.6.2_AE_PartnerETL

## THE SOVEREIGN INSTRUCTION (durable record per XXX.md -- verbatim, channel, time, scope)

Received via CTO relay (msg 20260714T185823Z; Andrew -> CTO, chat, 2026-07-14 ~18:5xZ), VERBATIM:

> "We are not waiting for the scheduled event, we need to proceed with a manual, ad hoc run of each
> silver converter to test outputs now and also reach parity between all completed bronze buckets and
> their corresponding silver buckets. I want to establish that we are completely clear on bronze full
> backfill and silver parity with that backfill. Once that is done, and bronze scheduled ingestion
> triggers and associated silver event-based triggers for the conversion to canonical form are
> confirmed, then we can proceed to devote full resources to Opal_RUNNERS."

SCOPE AS RELAYED: the after-orion-drain sequencing condition on MY schwab ratchet is LIFTED by his word
(shared-DLQ cross-attribution accepted + noted in manifests, not sequenced around). CTO's relay carries
the operational translation: ratified V2-9 mechanics, 0824-then-0833 (the runtime's own
DECLARED_SCHWAB_MASTERS order), one invoke in flight, RAVC per lane on completing manifest + listing vs
denominator. Broadcast duty: CTO (sender) holds it Tier-1 side; this log is my durable record; COO
notified same window. NOTE the wider scope signal: ad-hoc runs of EACH silver converter + parity on ALL
completed bronze buckets is FABRIC-wide (0.7.0/DS lanes for the mirror families) -- mine is the schwab
leg; I do not adjudicate the others.

## EXECUTION (started this window)

- Quiesce-first: converter last CW event 18:35:33Z (delta-5 smoke), 25 min quiet vs the 600s window --
  QUIESCED. Config verified live: py3.11 / 3008 / 600, LastModified 18:34:41Z (delta-5, v0.12.0).
- Driver LAUNCHED (Monitor b2tbxyvln, scratchpad/ratchet_driver.sh): sync RequestResponse, strictly
  sequential, AWS_MAX_ATTEMPTS=1, payload {"mode":"sweep"}; per-invoke listing deltas vs denominators
  (0824 -> 7,468 / 0833 -> 8,436 silver keys); terminal PARITY = a COMPLETED sweep whose OWN manifest
  reports shortfall_post==0 both lanes (manifest is the oracle, listings are the meter); WALL =
  timeout/error AND delta<=1 -> stop + sizing proposal; cap 80 invokes.
- Coexistence: tonight's 21:45/22:15Z fires idempotent per (feed, date); fire watch (bplnno19q)
  unchanged and doubles as the event-trigger confirmation leg of Andrew's condition.
- Expected per the expectation report S6: early invokes TIMEOUT-KILL mid-backlog (predicted-nominal),
  landings durable, killed runs write no manifest; with delta-5 live the rl* refusal class is ABSENT
  and the two 2025-01-09 shells convert 0-row T1_RECONCILED.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| aws lambda get-function-configuration | live config ground (not the map) | py3.11/3008/600 @ 18:34:41Z |
| aws logs describe-log-streams | quiesce check (last event) | 18:35:33Z -- quiet 25 min |
| ratchet driver (Monitor) | THE mechanism | running; per-invoke lines stream |

## Blockers

None. The ratchet self-reports; wall/parity terminals notify.

## Next Steps

- **[0.6.2 self]** Per-invoke lines monitored; on PARITY -> RAVC per lane to CTO (completing manifest +
  listing vs denominator) + report to Andrew's condition chain; on WALL -> sizing proposal to CTO.
  Fires 21:45/22:15Z verified against the S2 table regardless. Box-script upload stays morning-window.
- **[1.0.0_SA_CTO]** receives per-lane RAVC closes; parity certification is his to fold.
