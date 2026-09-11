# Holes Scan — AMGT_RESAPP, Tick 3 (20260911 ~09:5xZ)

**Author:** 4.0.0_SA_CRO~Z · **For:** 1.0.0_SA_CTO~Z to fold in
**Builds on:** tick 2 (`f15af4dd7e`) — round-2b's five cells have now run; this tick reports what
they actually found, not a restatement of what was expected.

---

## 1. Round-2b results — 2 clean, 1 pending CVO judgment, 2 correctly left OPEN (not new problems)

**rb-1** PASS (AC1-4, complete). **rb-12** PASS (doc-only identity-note correction, fallback still
intentionally uncoded pending Andrew, as previously scoped — not a regression). **rb-10** mechanically
PASS (4/4), AC5 judgment pending CVO.

**rb-2 and rb-15 are OPEN, and both are the fabric behaving correctly, not new defects to chase:**
both workers refused to fake a green rather than game their own acceptance criteria — worth stating
plainly so neither reads as a failure of this seat's own tick-2 recommendation (both cells exist
BECAUSE that recommendation was adopted).

### rb-2 (this seat's tick-2 recommendation, in its first real test) — BLOCKED on lane ownership, and it surfaced a real, measured data discrepancy

The worker named the exact fix (switch `lib/research/print/render_pack.py` and
`lib/research/provenance/render_print.py` from the uncorrected `model_block` lane to `AMGT-r-1`'s
corrected `model_block_fye` lane) and MEASURED the actual gap it would close: **BABA US Equity FY2025
— the currently-stored reference model-block reads PX_LAST 146.58 (calendar-year-end snapshot); the
fiscal-year-correct price is 132.23 (gap_days 0 at the actual period end).** An ~11% difference on a
stored figure other proof-of-spec instances measure against.

**Why it's OPEN, correctly:** the task order's `<paths>` grant doesn't include either file the fix
needs to touch. The worker did not route around this (no shadow consumer, no out-of-scope overwrite
— both would have been HARD-STOP violations in their own right) — it filed a BLOCKING surprise row,
**`AMGT_RESAPP-Z-W1-S6`, disarm_owner `2.0.0_SA_COO~ZZZ`**, asking for re-issuance with the two
correct paths added. This is the discipline working as intended.

**Worth a direct question to you, not assumed either way:** `AMGT-s-3` and `AMGT-s-5`'s own
proof-of-spec instances are named as reading this SAME stored `model_block_BABA_US_Equity.json`
reference artifact. Were those already-closed instances validated against the 146.58 figure? If so,
that's not a new defect in this round — it's an open question about whether two ALREADY-CLOSED
cells' evidence rests on a since-corrected number. Not asserting a problem, flagging it as a question
this seat cannot answer from the commit trail alone.

### rb-15 (this seat's tick-2 negative-control recommendation, implemented) — AC3 fails on a test-scope defect, not the code

The fix itself is solid: AC1/AC2/AC4 all met, including the two must-fail controls this seat
recommended. **AC3 fails because the criterion's own invocation sweeps the whole
`lib/research/lists/` directory**, netting a SIBLING module (`rot.py`, from a different task
`AMGT-s-15`) that makes an already-reviewed, already-cleared (under a separate governance tag) DNS
lookup unrelated to this cell's actual change. The worker correctly refused to edit `rot.py` just to
force the criterion green — that file is outside this cell's own scope. Filed
**`AMGT_RESAPP-Z-W5-S2`**. This is a criterion-design defect (too broad a sweep), not a code defect,
worth naming as such so round-2c's fix is "narrow the sweep," not "touch code that already works."

---

## 2. Bucket/pipeline infra — unchanged, confirmed not assumed (same as tick 2)

No new AMGT-scoped Terraform this tick. Correct sequencing, still gated on your DESIGN_SPEC approval
for round 3.

## 3. Nothing new stale against an Andrew ruling this tick

No new design rulings arrived since tick 2 to check prior briefs against.
