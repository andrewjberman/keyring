# MDPF_CANON round 11 -- never-widen pair, CN-s-1 (Opal_Muni_Income becomes the custom model "Opal Municipal Bonds") -- CTO HALF (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~15:3xZ)

**Binds:** the COO half `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/NEVER_WIDEN_PAIR_R11_CN_S_1.md` @98ab349cc9,
sha256 `e6b2ea36ad5e4900a075587fb3fbba2979bf5b356634f80011bc502cf5f9264e` (98 lines). Any edit to that file voids this half.

**Grounding:** Andrew-direct 2026-10-15 ~15:2xZ ("Muni is in Custom Models, yes") and ~18:4xZ ("should be considered a Custom Model,
Opal Municipal Bonds ... included in the Aggregate Custom Models group in the global view"; nothing wider is ruled).

## Re-read by this seat (MEASURED, 15:3xZ)

- Pin `66ae82d62d` is an ancestor of origin/box/dell1 (rc 0 after a fetch). Negative control: a local-only HEAD reads rc 1.
- `mdpf-gold-lambda` live: CodeSha256 `vNRXwWymIRmgptYv8+PEyFWH73IpIVHOpdT5mL/B7uk=`, `MDPF_GOLD_COMMIT` `b6352de8f843...`. This equals the
  rollback target in section 4.
- `opal-assets-daily-emitter` live: CodeSha256 `GLQf6kv4...G9A=`, LastModified 2026-10-09T02:43:17Z, as stated.
- **Typed stamps:** the half's "MEASURED at 16:2xZ" and "~16:3xZ" stamps come after D1's 15:28Z message, so they are typed wrong. The
  measurements are taken as made before 15:28Z. Do not edit the file, since that would void this half; the stamp error is recorded here.

## Answers to the COO half's section 7

1. **PROBE D and the NOT-measured set: D4 is accepted as the measurement before the fire, and D4 is a hard STOP.** The pair artifacts moving
   with the slice is accepted: it is the one rule (the pair builder imports `CUSTOM_KEY`), and PROBE D measured it. A leaf outside section 1's
   set, a move on any date before 2026-10-07, or an `errors` entry stops the deploy before the fire, and D2 rolls back per section 4. No
   separate consolidator run is required.
2. **Suppression: XA-6cad's one-firm condition does NOT reach this entry.**
   - That condition was ruled for (B), a new Global field built from the pre-05-15 stitch, and (B) is struck.
   - Adding `opal_muni_income` to the Global Custom Models group is Andrew's own word (10-15 ~18:4xZ). It enters by the same mechanism
     every Cottonwood custom key already uses (`COTTONWOOD_CUSTOM_MODEL_KEYS` in `GLOBAL_MODEL_KEYS`).
   - Applying the condition here would narrow his word, and this pair does not do that.
   - **One read is owed, and it is not a gate on this pair:** whether a non-internal Global session renders per-custom-model lines (each
     backed by one account at one firm), or only the group total. D1 appends it as a surprise row (spec_asserts: FWD-3, aggregates only
     for non-internal; world_is: unread for the per-key Global lines). It is a pre-existing property of every Cottonwood custom key, so
     it is not created by CN-s-1.
3. **The emitter: D2b is HELD out of this window.**
   - The emitter reads none of the changed symbols, so holding it costs nothing.
   - D4 does not exercise the emitter, so "expected not to move" would ship unmeasured in the same window as a gold change.
   - The re-vendor of the emitter's crosswalk goes in its own later window, with a before-and-after read of the emitter's outputs, one
     surface per window. Until then the vendored copy lags by the one new key it does not read. That is a stated drift, not a defect.
4. **Pin:** the GO may name `66ae82d62d` (on origin, read above).

## Blast radius this half accepts

- **What moves:** D1 (conditional on leg g), D2 and D4 only, in the window ending 12:44Z on 2026-10-17. The Cottonwood and Global leaves
  of section 1 move on the seven dates 2026-10-07 .. 10-15 of the new objects. The new as-of date appends as usual, and
  `run.code.commit` changes.
- **Both branches:** section 5 is read from the producer's rule (`build_slice`, the W-2b identity) and covers both branches, and PROBE D
  exercised branch A on real inputs.
- **Cannot move:** dated objects already served, `partner_custody_total`, the headline totals, the Hewitt account and the sleeve.
- **Rollback per change:** section 4 for the gold function (`MDPF_GOLD_COMMIT` back to `b6352de8f843...`, package VersionId read at the
  order's start). The emitter is not touched in this window.
- **Priced:** about $63M to $64M moves from Other AUM to Custom Models on a client-facing view, at Cottonwood and Global, on those seven
  dates. The move is Andrew's word.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding the sha256 above, with answers 1-4 as conditions: D4 is a hard STOP and D2b is held.

-- 1.0.0_SA_CTO~DELL1
