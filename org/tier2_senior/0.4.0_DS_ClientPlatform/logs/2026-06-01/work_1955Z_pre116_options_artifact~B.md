# work_1955Z — pre-1/16 disposition options artifact (DS~B)

## Tick class: SUBSTANTIVE (respawn recovery + deliverable authored)

## Session-start (respawn)
Prior ~B session dead ~67min (broker phantom-LIVE PID 4812 = pinned to broker-daemon). MSTR [STUCK] respawn.
- /watcher self-heal: re-registered LIVE PID 3916 (was phantom 4812); killed prior-session orphan watcher (504456 -> auto-respawn 519785), launched tracked watcher task `bf1vjk1jr`.
- INBOX RECOVERY: both ws COO dispatches had been swallowed into `~B/read/` by the dead session's orphan watcher (top-level + check-inbox empty; found via grep). Recovered: (1) 192710Z pre-1/16 options artifact [DRIVE-NUDGE], (2) 192102Z TO-B durable producer fix [SEQUENCED], + (context) 192803Z DE TO-A grain-finding.
- Confirmed pickup + ETA ~30min to COO (195409Z).

## Dispatch #1 DONE: pre-1/16 disposition OPTIONS artifact
`docs/briefs/mdpf-49f-pre-1-16-disposition-options-20260601.md` — 3 options (A back-cast estimate / B flag-at-1/16 / C start-at-1/16), each with what-Andrew-sees + honesty posture + data implications + AC6-dates handling + recommendation.

**Decisive empirical finding (pulled served `49financial/aggregate-aua-timeseries.json`):** the 1/16 boundary is ALREADY numerically continuous — 1/15 $1,409.3M -> 1/16 $1,412.9M (+$3.6M, no cliff). The $143M full-book->Schwab correction the re-derive removed was concentrated April->5/17; pre-1/16 the legacy bandaid basis was already ~= Schwab. Reframes the options:
- A: back-cast produces a line ~identical to today's (legacy ~= Schwab pre-April) while adding a widening error band + presenting modeled as measured -> cost for no visible gain, weakens honesty gate.
- C: discards real continuous growth history (Nov'24 ~$776M -> Jan'26 ~$1.4B) for no honesty gain (line already numerically honest).
- B (RECOMMENDED): keep history, numerically continuous, honest via explicit per-date legacy provenance flag + 1/16 boundary annotation. Lowest effort, re-rulable.

**AC6 pre-1/16 dates (12/30,12/31,1/2):** confirmed MISSING in served (jumps 12/29 -> 1/5; 1/1 holiday correct). Ride the option: A/B backfill on period basis + flag; C moot. Fold into whichever retains pre-1/16; harden producer date-selection to trading-calendar.

## Dispatch #2 (TO-B) — SEQUENCED AFTER #1, not started
Durable producer fix: emit per-firm ACCOUNTS-grain excluded-unfunded count directly in INF_09.generate_partner_analytics + 09.generate_partner_analytics (off positions cube). DE TO-A grain-confirm already landed (6639 = global-metrics 7039 - inflection-dist 400; no per-firm accounts-grain count exists in served feeds -> PRD option b necessary). RD~B stopgap (9b2fed2c) live -> not time-critical. Write-partition: do NOT parallel-write pre-1/16 producers; sequence after Andrew #3 ruling lands / pre-1/16 emit settles.

## Next
- RAVC2 the artifact to COO + CTO (-> COO routes Andrew #3).
- On Andrew ruling: execute B (or A/C) — full Rule 13 + ds-commit-gate + DE/CVO verify.
- TO-B when pre-1/16 producer-write window clears.
- /work 20m cron for queue triage.
