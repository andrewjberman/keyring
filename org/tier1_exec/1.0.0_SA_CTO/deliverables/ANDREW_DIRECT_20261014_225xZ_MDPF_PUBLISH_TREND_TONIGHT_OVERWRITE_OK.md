# Andrew-direct 2026-10-14 ~22:5xZ (dell1, `1.0.0_SA_CTO~DELL1` terminal) -- publish the MDPF Trend groups tonight, overwriting the as-of 2026-10-13 objects

## VERBATIM (in order)

> "No I need that mdpf rerun now, i need to smoke that now"

The CTO answered: a rerun cannot publish tonight, because the as-of 2026-10-13 keys are write-once and already written. A local 5174 render with
the real numbers is under way. "If you'd rather have it truly published tonight, the only way is to overwrite today's already-written production
files. That needs your explicit OK."

> "do it"

## What it decides (verbatim scope)

- **His explicit OK to publish tonight:** deploy CN-p-1 now, then ONE on-demand production run of `mdpf-gold-lambda` that re-writes the as-of
  2026-10-13 served MDPF objects, overwriting the keys the 13:31Z fire wrote. Bucket versioning keeps every prior version, and the prior VersionIds
  are recorded (pair section 6).
- It goes under the CN-p-1 never-widen pair plus an ADDENDUM for the manual overwrite path (CLAUDE.md NEVER-1: a manual path off the producer's
  clock is a new reachable state, and the sign-off must cover it). Rollback is per key: copy each prior VersionId back as the current version, never
  a delete.
- The local 5174 render continues in parallel. Whichever is ready first goes to Andrew.

-- 1.0.0_SA_CTO~DELL1
