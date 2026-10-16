# L4-R re-review -- SOC2_MSLOGS PRD v0.2 @5df576eada, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-16 ~16:4xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 6878 and 6879, answering this seat's refusal
`L4R_REVIEW_SOC2_MSLOGS_v0.1_RATIFIED_TEXT_20261016.md` @a1dd5533bf.
**Graded:** the whole diff bedd22acc3 -> 5df576eada. ENDPOINT is unchanged and is still verbatim against @b8c7dd61e8. Three CONTRACTS rows
moved (C-ACCESS, C-READS, C-RESIDUAL), and a CHANGE LOG was added outside the half.

## Verdict: SIGN

| Change | Read |
|---|---|
| C-ACCESS | The members' free `put` is gone. "A member's only write is `recollect`: the door itself re-fetches a window still inside the API's 7 days and lands what Microsoft serves into `audit_records`. A member never supplies record bytes." It also says "Bronze keys are write-once: the door refuses to write a key that exists, so no principal can replace a stored record through it." This closes the ground. C-RAW's byte-for-byte property and FWD-8 now hold against a stolen member login, and the write targets `audit_records` only, so C-SWITCH's freeze of `audit_events` holds by construction. Write-once binds the collector's own `put` too ("no principal"). |
| C-READS | `baseline` (FWD-5) and `outside_baseline` (FWD-6) are named ops, so every FWD read has a door op. |
| C-RESIDUAL (4) | "no member can write, replace or delete a bronze record, because bronze keys are write-once and a member never supplies record bytes". Andrew's statement is now complete on the point that decides whether the record can be trusted. |

## Nits (not grounds; fix at the next edit)

1. **The "raw" wording now contradicts itself.** C-READS says the reads return "query results, never raw records". C-RESIDUAL (4) says a
   member "can read every Opal account's raw records". The substance is clear: the door returns query results with full field values, one
   account and window per call, and never a stored object. But the two sentences now say opposite things. Suggested wording:
   - C-READS: "never a stored bronze object";
   - C-RESIDUAL (4): "can read every Opal account's records in full, one account and window per call".
2. **Annotations inside CONTRACTS.** C-ACCESS carries "(v0.2, on the CVO's L4-R refusal)" and two sentences of rationale ("Andrew's 15:3xZ
   ... A free `put` would let ..."). These belong in the CHANGE LOG, which already says them.

## Carried for the build, not this half

- **The write-once test:** the round-1 access cell's proof should include a refused second write to an existing bronze key (a negative arm),
  not only the admin `GetObject` refusal.
- **What `recollect` is allowed to do:** a `recollect` of a window whose blobs are already stored lands nothing new (the keys exist). The cell
  should show that this reads as "already stored", not as an error or a gap in coverage.

-- 3.0.0_SA_CVO
