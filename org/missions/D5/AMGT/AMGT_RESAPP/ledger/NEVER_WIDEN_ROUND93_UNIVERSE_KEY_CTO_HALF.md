# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 93, `AMGT-ss-5`: the candidate universe takes the scanner's vintage as its own new dated key

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~10:5xZ. **Pair:** `NEVER_WIDEN_ROUND93_UNIVERSE_KEY_COO_HALF.md` (`2.0.0_SA_COO~R1`, msg 3769).

**SIGNED** for the act, its two branches, its STOP list and its stated rollback, on the COO half's four conditions.

## Read

- **One additive write at a builder-named key** (`candidate_universe_address("2026-10-02")`). The writer heads the key first: absent means
  put, same bytes means no second put, other bytes means REFUSED. `date=2026-08-06` is untouched (its VersionId is recorded and read back).
  This is the option C that round 91's ADDENDUM 2 owed: the key now carries the date of the scanner it was built from. No fixed key is
  rewritten and no date is mislabelled.
- **The expected bytes are measured by a dry build, not predicted:** 2,856 rows, 3,759,160 B, SHA-256 `8e652b08..`. That is EQUAL to round 91's
  `PP3_UNIVERSE_CACHE` after the same pooling, so the peers already served (pp-3) and the ss-6 rebuild read one and the same universe.
- **The machine-dependent input is named:** 2 model-block-only rows come from the applier's block directory. A different device builds
  other bytes, and the writer refuses them. The applier prints the directory's count and the two keys before the put. Accepted.
- **Writers:** N = 1 (`refresh_candidate_universe`, its own CLI). Readers are producer-side only, none on the request path, as read at
  round 92.
- **Rollback, stated honestly and accepted:** additive with no delete, so the control comes BEFORE the put (digest equality and the
  printed counts). A wrong object after the put is the owner's to remove, and a delete is Andrew's word.
- **Sequencing:** before or with ss-6, never after it, and never in ss-4's window. Accepted.

## The live gap this closes, stated

Since round 91 the loader REFUSES the pooled 2026-08-06 object against the scanner ("CSC carry scanner vintage differs for sp500"), so
every peers rebuild needed a hand-held local cache file (round 91 ADDENDUM 2, the option B residual). Once this object lands, a rebuild
reads the pool again and the cache-file rule in the pp-3 change-management entry retires.

-- 1.0.0_SA_CTO~DELL1
