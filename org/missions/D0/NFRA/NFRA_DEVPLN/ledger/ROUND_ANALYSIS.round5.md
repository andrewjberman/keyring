# NFRA_DEVPLN -- ROUND-5 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~01:2xZ)

**On:** the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND5_DRAIN_END_20261014.md` (2 of 2 orders,
MAY-CLOSE; no SERVED or WORLD order, so no CVO packet). **PRD:** v0.3, unchanged. **Next:** round 6 in ONE issuance on section 3.

## 1. What round 5 moved

- **DP-f-1:** the DEV push payload limb (`.tools/portal-hooks/dev_push_payload_gate.py`, called from `.tools/portal-hooks/pre-push`),
  19 cases.

  The three demonstrations this seat required were run through the REAL hook script:
  - an unapproved commit onto DEV is REFUSED with exit 1;
  - an approved merge is admitted;
  - a PROD-into-DEV back-merge is admitted on real history.

  A new ref named DEV is refused, and a non-DEV ref is untouched.
- **DP-f-2:** one test seam variable, and exit checks on the self-test fixtures, with a negative control.
- **A second organic run of the route:** dell1's Opal-internal Security Analysis feature reached DEV as `5e40e541` with both trailers,
  approved by `1.0.0_SA_CTO~DELL1`, and read from the laptop. It is the route's first non-laptop feature; it is not the client-facing
  case.

## 2. Rulings

- **Who installs the limb, and where first: each box's manager, laptop first.** `.tools/portal-hooks/install.sh` is a per-box,
  run-once install from the workspace root. That is a box infrastructure act, so it belongs to the managers, not a worker cell.
  - `0.0.0_AB_MSTR` installs on the laptop now. The read-back is `cmp` of the installed `portal/.git/hooks/pre-push` against the
    canonical source, plus demonstration 1 re-run through the INSTALLED hook (exit 1).
  - Then `0.0.0_AB_MSTR~DELL1`, `~DELL2` and `~Z` each install after the box-sync carries `367ce6ff40`, with the same two reads,
    reported back. dell2 goes before the others, because its client-facing features are next through the route.
  - Until a box has installed it, that box's scripted direct DEV push is gated only by `never-rules-gate.sh` for typed commands.
- **W1-S15 (a live FAST lease against the structural refusals): the STRICTER reading stands.** A lease admits its own commits through
  the walk, and the structural refusals still apply first: a new DEV ref, and a non-fast-forward. That matches the CLAUDE.md FAST
  line, which lands the lease's product changes on DEV and grants no right to recreate or force the branch.
- **W2-S12 (the seam needs a guard): YES**, as one small repair. The seam is honoured only when the variable is set in a test, so a
  production tool that sets `OPAL_STATE_ROOT` can never read fixture refs.

## 3. ENRICHMENT LIST for round 6

1. **After Andrew rules the dell2 rows** (`3635`, `8500`, `7b45`, `fde0`, and `7773` the partner-firm filing): A14, the integrator's
   merge-forward of each approved feature, then the DT's chosen-set promote naming only those. This is FWD-1's client-facing close
   (SERVED, with the L8 packet). No order is cut before he rules.
2. **The install read-backs** from all four managers, folded into the round's record. This is not a worker cell.
3. **One small repair:** the W2-S12 guard.
