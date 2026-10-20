# NFRA_SCHWABBF -- ROUND-2 ANALYSIS (1.0.0_SA_CTO, 2026-10-20 ~16:2xZ)

**On:** the issuer's L10 slug `deliverables/2.0.0_SA_COO~SB/ROUND2_L10_SLUG_TO_CTO.md` @7217fdaefc (laptop msg 109920). Round 2 is terminal: 8 of 8
orders merged and 8 of 8 proofs valid. Nothing was deployed or moved. The two ARMED rows (W5-S2, W5-S3) were disarmed the same turn. The
release plan on the firm form has its COO half signed. **PRD:** v0.6.

## Rulings

1. **The 1,245 unprefixed 0824 objects: option A, with one change.** They move UNCHANGED into the firm folder. Their master is recorded in
   the move's committed attribution manifest (old key, new key, source folder `08242234`) and is never inferred from the missing prefix.
   - Why not B: it keeps a second form alive for one master, against FWD-4.
   - Why not C: it rewrites names to look like vendor files they are not.
   - Why the manifest and not a standing rule: a rule that "unprefixed means 0824" is a default every future reader would have to know.
     The manifest keeps the attestation that the folder gave, at the moment of the move.
   - These files include days before Schwab's 2023-10-17 floor, so they cannot be re-pulled. The copy is verified by sha before anything
     old is touched.
2. **Round 3 as proposed:**
   - R3-1: this ruling (tool flag and the manifest);
   - R3-2: the `modules/opal_name` regeneration and the `secret_name` output, in their own Terraform cell;
   - R3-3: retire-banners on the three dormant old-form writers;
   - R3-4: FWD-2 (full backfill) and FWD-3 (held-days record) once the cutover is through;
   - then the release acts.
3. **The release waits on two things:** the ratified-text re-sign of v0.6 (C-KEYFORM changed), and Andrew's answer on silver, meta and
   `_ops` scope, which decides whether the cutover carries silver too. Bronze-only release acts may proceed if Andrew answers "bronze only".
   If he answers "all tiers", round 3 adds the silver move and the silver readers to the same cutover.

-- 1.0.0_SA_CTO
