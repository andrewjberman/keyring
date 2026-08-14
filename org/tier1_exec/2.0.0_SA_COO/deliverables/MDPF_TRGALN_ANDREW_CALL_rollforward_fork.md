# SOVEREIGN CALL — MDPF_TRGALN: Inflection empty-date fill (roll-forward fork)

**PARKED for your ~07:00 ET return — not time-critical tonight (all 14 retimes are live and today's
cycle is unaffected). Grounded on VALIDATED proof_TO-5.json @98dbaf099a (14/14 claims PASS).**
**CC: MSTR, CTO.** Per PRD §8.2: roll-forward requires your explicit word.

---

## THE CALL (one decision)

The 7 empty Inflection stacked-bar dates are all MISSING data (none is true history), and the
missing eclipse model-leg data is **permanently unfillable** — source-confirmed three ways: the
eclipse API is current-state-only (`--date` is a label, not a query; docstring @b0cad1965), the
only date-parameterized path (auditlog reconstruction) was exercised 2026-07-16 and returned empty
(18 files, 2 bytes each), and no rawer copy exists in either bronze home. Surgical backfill is
honored where possible (below). For the unfillable model leg, pick the fill scope:

**(A) ONE-SHOT** labeled fill of exactly the 7 adjudicated dates — smallest change; the next
eclipse absence makes a new hole needing a new ruling.
**(B) STANDING** labeled carry-forward rule in the builder for absent-eclipse run-dates — no future
holes; standing behavior.

**Load-bearing fact:** the absences are RECURRING, not a closed incident — five distinct episodes
across 2.5 months (run-dates 05-21, 06-01, 07-01, 07-13/14/15, 08-06 — the last on the platinum-
cutover night). A one-shot fix leaves the next episode to re-manufacture this exact hole.

---

## COO RECOMMENDATION

**(B) STANDING labeled carry-forward**, because the absence cause is measured-recurring (5 episodes)
and every fill carries its provenance marker in the artifact — the honest_none machinery that let
tonight's truth-pass agree 7/7 with an independent census is exactly what keeps a standing fill
auditable. Plus the surgical component either way: the orion custody leg of 08-05 is recoverable
IN-ESTATE with zero vendor egress (the 08-06 pull's parquet exists at
`opal-data-inf/bronze/positions/2026-08-06.parquet`, 1.23MB — only the mirror leg missed it) and
gets re-mirrored, not rolled.

## Implementation is pre-framed (CTO arch pre-ruling 054404Z — you rule the WHAT, the HOW is set)

Either scope lives BUILDER-SIDE as an extension of the carry-forward union you ruled at the 08-05
cutover — never publisher-side (platinum stays serving-only, one-producer-by-construction). Every
filled date carries a provenance marker IN the gold artifact (`model_leg_filled_from: <date>`) — a
silent fill is a falsified series. Fills are LEG-SCOPED: only the unfillable eclipse/model leg
rolls; the orion 08-05 custody leg is surgically re-mirrored. Note: reverting the RP-W1 label
offset is NOT a remedy — the truth-pass confirmed the pre-offset "full" values were D-1 closes
mislabeled (the offset fixed a real defect; these holes are the honest view of missing data).

## The adjudicated table (validated proof_TO-5.json @98dbaf099a; full table TO-5_INFLECTION_TRUTH_TABLE.md)

| Served date | Verdict | Missing run-date | Fillable? |
|---|---|---|---|
| 2026-05-20 | MISSING (eclipse model leg) | eclipse 05-21 | NO — roll-forward only |
| 2026-05-29 | MISSING (eclipse model leg) | eclipse 06-01 | NO |
| 2026-06-30 | MISSING (eclipse model leg) | eclipse 07-01 | NO |
| 2026-07-10 | MISSING (eclipse model leg) | eclipse 07-13 | NO |
| 2026-07-13 | MISSING (eclipse model leg) | eclipse 07-14 | NO |
| 2026-07-14 | MISSING (eclipse model leg) | eclipse 07-15 | NO |
| 2026-08-05 | MISSING (eclipse model + orion custody) | both 08-06 (cutover night) | custody YES (in-estate re-mirror, zero egress); model NO |

The other 383 zero-model dates are ALL TRUE-ZERO (pre-launch history; model era = exactly 53
nonzero + 7 null of 60 trading days since 2026-05-15) — untouched under any option.

## Context

- All 14 trigger retimes LIVE (landed 05:36Z, 4h ahead of your window); tonight-refresh was running
  at package time — per-firm as-of readback rides the TO-3/TO-4 close reports. The retime program
  is independent of this fork.
- TO-6's executor spawn is HELD at MSTR pending your word (suggested lane on your GO:
  0.4.0_DS_ClientPlatform — they authored the offset + honest_none machinery; orion re-mirror as a
  one-line rider).
