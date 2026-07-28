# Deploy: emitter-wo4c-cadence-acceptance

**Opened:** 2026-07-28T23:38Z by 0.7.0_AE_CloudOps · **Authority:** MDPF_RESET WO-4c as ruled by
CTO 223619Z (accept latest ≤ run_date per roster-declared cadence + 1 td slip, identity stamped;
never same-day from a T-1 feed; never re-phase to D+1).

Pre-deploy live smoke (read-only, 23:31Z): c2_custody(07-28) → $1,684,259,082.58 @07-27 lag 1
`at_declared_cadence` (was ABSENT); inf_models → $141.88mm @07-27; inf_total → @07-28 lag 0;
smartx settled_max_day 07-27 (was T-2 via the max-day drop); cot_models honest-absent (pair
series ends 07-22, 4 td > D+2+1 window — the bounded refusal working as the outage signal).

VENDORED ROSTER: cadences read from packaged `partner_roster.json` (verbatim copy of the one
repo authority; AE-base re-vendors on change — same ownership as the runner S3 copy).
Disclosed design residual: `vintage_state` stays derived from raw as_of (rolled_forward at T-1)
to keep the G6 alarm/staleness contract in sync; the cadence fields
(`cadence_state`/`cadence_normalized_lag_td`) carry the PIN-3 "T-1 IS fresh" judgment. Flipping
the enum itself couples to the G6 checker and is flagged to CTO, not done unilaterally.

## Completion

(open)
