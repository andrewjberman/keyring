# DEPLOY-COMPLETION LEDGER: Door-5 de-collide (opal-data-inf code/ prefixes)

**Opened:** 2026-07-15T22:53Z by 0.7.0_AE_CloudOps
**Status:** OPEN (closes in-session per NEVER#6 -- a begun deploy finishes or rolls back + escalates)

## Motion
Sovereign INF release window, step 2: de-collide the two basename collisions in
s3://opal-data-inf/code/ by re-deploying the canonical (silver, newer/load-bearing) bytes over the
gold prefix keys so all copies are byte-identical (the sync_scripts guard's own remedy line).
NOTHING deletes. Chain dispatch stays held by the inf-gold-trigger chokepoint until the CTO+COO
sentinel motion (separate, theirs).

## Authorization
- Andrew-direct GO, verbatim x2, recorded @ aab5f21d5 (22:42Z "GO NOW" + 22:43Z run-tonight).
- CTO gate confirmation + re-sequence + 3 design pins: 1.0.0_SA_CTO 224755Z.
- COO co-sign rides the sentinel motion (requested URGENT, in flight).
- Executor named by the hold doc: 0.7.0 opens Door 5, reversibly, revert pre-staged, never as cleanup.

## Legs
1. [DONE 22:51Z] Bank all 4 copies + md5-vs-ETag verify (4/4 match).
2. [DONE 22:53Z] MANIFEST.json + revert.sh written (full-state one-command restore) -- committed BEFORE the open.
3. [PENDING] Execute: cp silver bytes -> gold keys (both files).
4. [PENDING] Post-verify: ListObjectsV2 ETags -- gold keys carry silver MD5s; 4 keys byte-identical pairwise.
5. [PENDING] Evidence to DS~B (their two-stage run gates on this + the sentinel) + CTO/COO; ledger CLOSE.

## Rollback
`bash org/tier2_senior/0.7.0_AE_CloudOps/deliverables/door5_decollide_20260715/revert.sh`
restores the exact pre-motion state (ETags in the script header). If any leg fails mid-motion:
run revert.sh, verify ETags, escalate loud to COO -- do NOT leave a half-consolidated prefix pair.
