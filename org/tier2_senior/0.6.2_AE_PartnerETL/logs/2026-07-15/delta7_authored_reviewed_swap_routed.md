# 0.6.2_AE_PartnerETL -- delta-7 (named-hole event SKIP) authored -> verified on the real incident key -> CTO+contract PASS -> swap routed; 0824 parity-certified, 0833 draining

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**Date:** 2026-07-15 | **Window:** ~12:5xZ -> ~13:1xZ | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Delta-7 -- the hole-skip fix for the seam the first live fire exposed -- went author -> verify -> review
-> swap-route in one window, CTO PASS zero changes.

- **What it fixes:** the S3 event fires on the `.zip` suffix for EVERY bronze type incl. the named holes
  (tcf/tcfx/tnn); pre-delta-7 a hole landing hit `feed_from_key`'s unrecognised-type raise -> failed ->
  retry x3 -> DLQ. tcf is a DAILY feeder (754 partitions), so it was recurring noise on the shared DLQ
  each morning. This morning's fire produced 12 such failures exactly as the finding predicted.
- **The fix (CTO ruling 20260714T215400Z; contract v1.2.4 @ de54d79a3):** `hole_from_key` derives from
  the ONE `conversion_manifest.NAMED_HOLES` constant (the same the sweep + manifest name holes from);
  `convert_object` returns `action='skipped-hole'` for a hole landing, checked BEFORE `feed_from_key` so
  no raise/retry/DLQ; `build_manifest` keeps `ok=true` for a hole-only batch and names it in a new
  `skipped_holes[]` field; a genuinely UNKNOWN type still hits the byte-identical `feed_from_key` raise.
- **Verification:** suite 176 passed + 7 skipped (+7 new). The standout (CTO-named): the collision guard
  proves `hole_from_key(RPS) is None` AND `hole_from_key(ZZZ) is None` -- closing the one real hazard of
  filename-token classification (a hole token silently skipping a convertible pipe = silent data loss),
  both directions, disjoint-by-construction. REAL-BYTES: the EXACT tnn key that DLQ'd this morning now
  skips clean (0 writes, manifest ok, hole named); the sec pipe control still converts 2,315 rows
  T1_RECONCILED. The incident is retired at source, not synthetically.
- **CTO's one confirm-in-passing (not a gate):** is tcfx intended reader-less? Answered from SOURCE
  (dictionary SS2c: tcfx = "3 header rows / 2 data sections, confirms-extended, reader variance -- convert
  later", same disposition as tcf, no ruled reader today). DS's v1.2.4 NAMED_HOLES correct; loop closed
  with DS.
- **Deploy:** committed @ 092d342c3, DEPLOY UNTOUCHED. Swap routed to 0.7.0 (artifact-hash-only, no TF
  config delta -- runtime/sizing unchanged from v0.13.0), plan-shape at CTO's gate.

## Parity state (Andrew's directive)

- **0824: PARITY-CERTIFIED** by CTO (RAVC-4 ACCEPTED 125927Z) -- the scheduled 12:15Z sweep's OWN manifest
  attests shortfall_post=0/surplus=0/collisions=0. The pipeline certifying itself clean = parity as a
  standing property.
- **0833: ~44% draining** (3,734/8,436) via the ad-hoc ratchet (timeout-kills nominal, landings durable);
  per-lane RAVC to CTO on its completing sweep manifest.
- **Morning fires (07-14 daily set):** first FULL daily delivery converting live under the complete family
  (0824 11 / 0833 13 files, pipe types clean e.g. fact_sec 2,151); event-trigger leg CONFIRMED ~10s
  landing-to-manifest; the 12 hole failures were the known delta-7 noise (now fixed).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| pytest x1 (full dir) | delta-7 gate | 176 passed + 7 skipped |
| ci/vendor-manifest.sh copy + --check | re-vendor the 2 changed modules | 10/10 |
| .tools/commit-gate.sh | Rule 14 on 7 files | clean |
| real-bytes HybridS3 exercise | delta-7 on the exact tnn incident key + sec pipe control | tnn skips clean / sec converts 2,315 |
| aws s3 (parity + fire manifests, footer reads) | 0824 sweep verdict, morning fires, S2 verify | 0824 shortfall_post=0; S2 15/15 TIE earlier |

**What worked:** the morning incident key was the acceptance test -- delta-7 validated against the exact
production failure, not a synthetic. **What failed/caught:** the real-bytes exercise first ModuleNotFound
on backfill_status (lib/ not on path) -- added the lib dir; a reminder the lambda's flat-vendored layout
differs from the repo's silver/ + lib/ split. **Gap:** none.

## Blockers

None. External gates: 0.7.0 delta-7 swap, DS delta-7 review (in flight), 0833 ratchet completion (running).

## Next Steps

- **[0.6.2 self]** On 0.7.0 swap-live: observe the next fire's hole landings return skipped-hole (ok=true,
  no DLQ). Then the box-guard upload (sequenced after delta-7-live, one-variable) -> its first guarded
  fire -> V2-2 RAVC-4. On 0833 completing sweep shortfall_post=0 -> per-lane parity RAVC to CTO.
- **[1.0.0_SA_CTO]** delta-7 swap plan-shape gate; folds the clean-by-construction event path into the cert.
- **[0.7.0]** delta-7 apply on CTO's plan gate.
- **[0.4.0_DS]** delta-7 same-day review (in flight).
