# AMGT_RESAPP round 61 -- `AMGT-ak-6` never-widen pair, CTO half (the B2/B3/B4 stored-field rewrite)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~08:2xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round61/NEVER_WIDEN_HALF_COO_AK6.md`
@fa9c914db9 (msg 28313). DSGN round-21 analysis section 3B, cells B2, B3 and B4.

## What I read

- **The act:** a literal write set of 251 distinct keys and 1,188 entries in the versioned bucket `opal-data-harvest`:
  - 234 `peers/v1/`, 9 `posture/v1/` and 8 `management/v1/` keys;
  - fixed by three FROZEN plans, each pinned by sha256;
  - per key: GET, assert each entry's `before`, set `after`, PUT whole at the same key.
  No redeploy: AMENDMENT 1 found 0 of 350 packaged members changed.
- **The afters are computed by the fixed producer code:** `enrich.domain_for`, `csc_plain_reasons`, the `roster.py` parser and
  the deterministic `judge.plain_claim`. None is hand-typed, and no model call is made.
- **The base appendix** `AK6_BASE_VERSIONS.json`: 251 of 251 keys versioned, 0 `before` mismatches at signing. Each key carries its
  prior VersionId, which is the rollback.
- **Writers per family:** 2 (the hand-run producer + this act). None is scheduled. A later producer run writes a new `<as_of>`
  object with the fixed code, so the words persist.

## Why an in-place rewrite is acceptable here

These keys are named by `<as_of>`, and the body is the producer's output for that date. Rewriting a dated object's body is the
exception, not the pattern. It is acceptable for this act for three reasons:
1. Only display strings change: reasons, a parsed title and a claim sentence. No figure, date or key does.
2. The bucket is versioned, and every prior body is recoverable by its VersionId.
3. The alternative, re-running the producers to write new `<as_of>` objects, would regenerate more than these fields. That
   includes a model call on the posture path.

The act does not become a precedent for rewriting stored figures.

## Blast radius and rollback

- **May touch:** exactly the 251 appendix keys, and within each object only the plans' `store_field`s.
- **Rollback, per key:** `copy_object` of the appendix VersionId back over the key. There is never an S3 delete.
- **Unmoved:** every other key, every figure and date field, the code, IAM and the routes.

## Both branches

- **Every PUT lands:** the served Exec, Peers and Posture text changes on the planned fields only.
  - B2: 0 of 26 code-shaped on BA/VLO (base 11).
  - B3: VLO's 5 officers carry full names and no aged roles; BA's 12 are unchanged.
  - B4: 0 of 12 claims carry a status token (base 2).
- **A PUT fails partway:** the written keys serve the new words. The act is then completed or rolled back key by key, and is never
  left partial. (The COO half's own point: a partial write covering BA and VLO can pass AC1-AC3.)

## Conditions

1. **The three plans' sha256 at act time equal the values above.** Any differing byte is a STOP and a re-sign. The B2 plan is read
   from worker commit `25ac521b3d`, with the drain or not.
2. **The full write set is read back, not the sample:** `ak6_store_writes.json` lists 251 of 251 written. A read-back of every key
   finds each planned field equal to its `after`.
3. **Every field outside the plan is unchanged, compared semantically:** for each of the 251 keys, the parsed object minus the
   planned fields equals the parsed base VersionId minus the same fields; that is 251 of 251 equal. The PUT rewrites whole objects,
   so this is the guard against a serializer changing anything else.
4. **The grade reads the SERVED route:** `/security/{key}/thesis` and `/peers` for BA and VLO after the act, so any cache in front
   of the route is inside the read. HTTP status is never the grade.
5. **NEVER-2:** a ledger entry is opened before the first PUT and closed after condition 3, or rolled back and closed RED.

**CTO HALF: SIGNED** for the 251-key stored-field rewrite as the frozen plans and the appendix define it, on conditions 1-5.
