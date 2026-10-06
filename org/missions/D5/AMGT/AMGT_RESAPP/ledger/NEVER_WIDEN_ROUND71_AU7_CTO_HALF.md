# AMGT_RESAPP round 71 -- AMGT-au-7 never-widen pair, CTO half (code-only redeploy at a53eaf74c5, carrying au-1..au-6)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~18:2xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round71/NEVER_WIDEN_HALF_COO_AU7.md`
@f850d9d1e6 (msg 29752), with AMENDMENT 1: the gold leg leaves au-7. HARVST is the gold table's one writer, and c35 is graded after
HARVST's next build. **Executor:** `0.7.0_AE_CloudOps~A`. Proof: DEPLOY genre.

## Read live at signing

- **Base:** CodeSha256 `GS//XHnVd4+bBIg1VU++r1fp9v495pi6jKFat9KbEYE=`, memory 1769. No NEVER-2 entry is open on the function.
- **The content diff (COO half):**
  - CHANGED: `scoped_amgt.py` and `publication_gold.py`;
  - ADDED: `lib/research/api/served_cache.py`;
  - 96.9% of the package ceiling, and no new S3 read path.
- **`served_cache.py`, read here:** a per-container memo for the Lead Panel's stored reads (au-6, Andrew's speed issue). Its rules:
  - **version-keyed** entries carry the stored object's identity (generation_id and row_count), so they never go stale and have no
    expiry;
  - **TTL** entries cover reads with no version: the generation pointer at `POINTER_TTL` 60 s, which bounds how late a newly committed
    generation can be seen, and classifications and names at `SLOW_TTL` 300 s;
  - values come back as deep copies, and a failed read is never stored.

  **This is sound.** The only staleness is bounded: 60 s for a new generation, 5 minutes for a classification or name edit.

## Conditions

1. **At build time,** the content diff against the deployed CodeSha256 (re-read then) is exactly CHANGED `scoped_amgt.py` and
   `publication_gold.py`, and ADDED `served_cache.py`. Anything else is a STOP. No gold or store write is part of this act.
2. **Graded on the DEPLOYED function:**
   - au-1..au-5's checks, and the full regression set (c14, c15 as amended, c23-c33);
   - c38's latency is reported, with no rollback, because no value changes (EQUAL 9 of 9).
3. **THE SPEED CLARITY ANDREW IS WAITING ON** (his ~15:5xZ word holds the DSGN PROD promote on it):
   - after the deploy, measure the Lead Panel routes' load time BEFORE (the base) and AFTER, both cold and warm, with the request count
     and segment times;
   - `2.0.0_SA_COO~Z` writes that as a short plain-words note for Andrew through `0.0.0_AB_MSTR~Z`: what was slow, what changed, the
     measured times, and what remains slow, if anything.
4. **One NEVER-2 entry,** in the DEPLOY genre, with base against new CodeSha256 as the discriminating control and the named rollback
   (the prior artifact VersionId).

**CTO HALF: SIGNED** for AMGT-au-7 under conditions 1-4.
