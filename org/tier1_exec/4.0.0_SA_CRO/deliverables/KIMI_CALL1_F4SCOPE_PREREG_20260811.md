# CALL #1 -- F4 FILE-SCOPING FIRE: PRE-REGISTERED QUALITY DELTA (before the read)

**Author:** `4.0.0_SA_CRO~B`. Adopts CVO rider. Timestamped before the fire.
**Change vs the F2-direction fire:** F4 replaced estate-wide agent-type matrix with per-vertical
file-scoped attribution -- mdpf: 38 files / 170 touches / DS 88.8% (AE 12, SA 5, AB 2); 3 cross-type
seam files (mdpf_aggregate_aua.py AE5/DS4, build_aggregate_aua_timeseries.py, build_legacy_compat_emit.py).
F2 stays wired (DIVERGING); F1/F3 still UNMEASURED.

## Ground truth F4 now says
mdpf is a CONCENTRATED single-owner (DS ~89%) vertical; the only cross-type coupling is localized to
the AE<->DS aggregate-AUA seam. Read WITH F2 (hot/heating): a single team is actively building this
vertical out -- low cross-type contention, coupling localized to a named handoff.

## NEW pass criterion (the point of this fire):
- **The model now USES F4 as an mdpf-SPECIFIC signal** -- reads the concentrated DS ownership and/or the
  AE-DS seam, and does NOT repeat "F4 is estate-wide context, cannot attribute to mdpf." Confidence may
  rise (F2 AND F4 are now mdpf-scoped -> 2 of 4 mdpf-specific).

## HARD FAILS specific to this fire:
- Still calls F4 estate-wide / non-mdpf (ignores the new grain -- the wiring bought nothing).
- Misreads 88.8% single-owner as ABANDONED/dead (concentration != death; F2 says hot -- the boundary_declaration warns this explicitly).
- Reads single-owner as HIGH contention (inverts the signal).

## RETAINED (must still hold):
- Direction still DIVERGING/heating from F2 (the F4 change must not regress the F2 read).
- F1 + F3 still named blind, not read as calm.
- No lifecycle value, no proposed change, no invented axis.
- GOOD (not required): connects F4 concentration + F2 heat into "one team actively building it out," and/or names the AE-DS seam as the coupling point.
