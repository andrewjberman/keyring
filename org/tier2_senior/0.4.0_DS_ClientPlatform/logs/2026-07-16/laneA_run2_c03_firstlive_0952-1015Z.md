# Run 2 (a00/a01) + C_03 FIRST LIVE — event-fired on partition arrival; the incremental machinery works; two guards fired correctly on day one

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-16 09:52Z -> ~10:15Z
**Trigger:** partition watch v2 (ba5414y05) ALL-LANDED at 09:52Z (six minutes off the 09:46Z census ETA;
the watch exited clean by design after emitting all three landings).

## What landed

1. **A_00 run 2** (`dim_account/date=2026-07-15/`, ETag 8615e345..., listing + read-back verified):
   7,142 read == 7,142 converter-attested; **the incremental machinery's first real day**: prev_dim
   diffed -> new=7, closed=2, 4 absent-carries (7,146 rows), first_seen continuity held, jd1 stamp
   correctly reads the smartx prefix (2026-07-14), fam/slm 2026-07-15.
2. **A_01 run 2** (`dim_relationship/date=2026-07-15/`): 7,142 -> 3,476 relationships; ssn-absent
   read-back asserted.
3. **C_03 FIRST LIVE** (`gold/canonical/nna_atomic/date=2026-07-15/`, 328 accounts): census printed
   per the CTO evidence bar; **the zero-in-kind HOLD FIRED** and discharged BY INVESTIGATION (below);
   override reason audited in the manifest.

## Two guards fired correctly on day one — both were fixes-before-defects

- **SCD2 merge multiplication (a00 core bug, CAUGHT BY THE RUN, fixed at source + fixture-pinned):**
  the 07-15 jd2 carries 5,336 accounts x 2 SCD2 periods (10,672 rows — the snapshot-diff's first real
  day; the 07-14 all-open floor was single-row only by birth). The naive role merge multiplied dim rows
  and the snapshot-diff crashed on a duplicate index. Fix: merge CURRENT-period rows only (is_current,
  dictionary-pinned) + a dup-multiplying-merge-NEVER-ships assert + loud dedupe fallback. Fixture added
  (current-period-wins pinned); suite 43/43. Run 1 could not have seen this — the input shape did not
  exist yet. THE INCREMENTAL PATH'S FIRST EXERCISE IS EXACTLY WHERE THIS CLASS LIVES.
- **C_03 zero-in-kind HOLD (the instrument working as CTO specified 235953Z):** first live census read
  in_kind 0/1,166 -> HELD, not shipped. Investigation (both partitions, bytes): 07-15 carries 3 TA rows,
  ZERO with quantity — no security transfers in the delivery; 07-14 comparison: 349 TA / 336 in-kind.
  **The zero is the DAY, not the instrument** — discriminator verified on both shapes; shipped with the
  stated audited override. (Also banked: 07-14 was an ACAT-heavy day — 30% of legs were transfers;
  daily TA volume is bursty, so the hold rule will fire on quiet days routinely — a per-day-expected
  behavior worth a threshold discussion at the C_03 spec fold, NOT a defect.)

## Compiler Tools

commit-gate x2 (a00 core + wave2 fixtures) PASS; pytest 43/43; rail-marked listings for the
partition-shape investigation (Rule 22a bytes-grounding); postdeps unchanged from the wiring window.

## Next

- Evidence to CTO this window (sent with commit). Wave-3 TO cuts still awaited.
- C_03 day-2 rides tomorrow's partition (transfer-day expected to exercise the valuation path live).
- Watch v2 retired clean (ALL-LANDED); tomorrow's watch arms at need.
