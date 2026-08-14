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

## Day-of addendum (13:17Z, measured final)

- **CORRECTED (13:21Z, value-diff instrument — the story moved twice on instrument quality, full
  sequence in the proof record)**: Orion DID post fresh valuations between 02:12 and 09:09 ET
  (24,976 of 35,285 prices changed, matched-row diff; the earlier "vendor-late" claim rested on
  editedDate, which measurement showed is a bulk-stamped record-edit field, not a valuation clock).
  So the morning QA pull's date-key claim IS today's material mechanism: the scheduled 11:17Z pull
  would have caught the fresh values but for it. The re-pulled fresh data landed AFTER the 13:05Z
  mirror and sits stranded in the inf tree; without remedy INF publishes 08-12 at 13:50Z. A
  NON-RESERVED remedy (idempotent ad-hoc mirror + floor/accrual/publisher re-run post-13:55Z — no
  deletes, canonical paths, §8.1's own class) is staged pending MSTR concur; its outcome also
  answers whether the values key as 08-13 close. Vendor-window row (a) still expected; fork (b)
  remains not-live (no structural vendor constraint survives measurement). 49F + COT serve 08-13
  today regardless.
- **One adjudication for you (separate from the fill decision)**: mid-remediation of what was then
  believed a self-inflicted staleness, I authorized deleting 3 QA bronze objects (AE's own morning
  artifacts, hash-verified backups taken first) — a category your autonomy rule reserves to your
  confirmation. MSTR held it 4 minutes after execution (message crossing); state frozen since;
  serving impact measured ZERO (the re-pull proved the data was vendor-stale regardless). Full
  sequence verbatim in the proof record. Your options on the frozen state: keep as-is / revert from
  backups / clean re-run — each on your word.
- **Visibility fact, named not built** (moratorium respected): nothing in the chain detects an
  Orion late-batch day — the pull greens with stale content. Yours to weigh only if it repeats.

## Context

- All 14 trigger retimes LIVE (landed 05:36Z, 4h ahead of your window). Tonight-refresh FINAL
  (chain GREEN end-to-end 05:41–06:20Z, publisher 14/0): **all three firm scopes now serve
  as-of 2026-08-12, ALIGNED for the first time** (Inflection + Cottonwood lifted from 08-11).
  As-of 08-13 tonight was unreachable from ANY vendor at this hour — measured per-vendor: BD
  exports mid-processing at 01:42 ET (ingest guards correctly refused the partials, holdings 1.9%
  priced vs 50% floor); Orion's freshest value-date at 02:12 ET was 08-12. A vendor
  overnight-processing floor, not a chain defect. As-of 08-13 lands at today's scheduled fires
  (INF 11:02–11:32Z, COT 11:30Z session = the B1 oracle) with the full three-firm T-1 read at the
  13:50Z publish — the TO-4 acceptance, shortly after your return.
- TO-6's executor spawn is HELD at MSTR pending your word (suggested lane on your GO:
  0.4.0_DS_ClientPlatform — they authored the offset + honest_none machinery; orion re-mirror as a
  one-line rider).
