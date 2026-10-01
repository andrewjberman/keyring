# 2.0.0_SA_COO~H drive log -- 2026-09-30 09Z (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron bf9d159b). Lease: FULL.

## Round 27 closed

- **`q-1` reported (~09:0xZ).**
  - One run record was persisted.
  - bbg was `request_rejected`: the job's only live request re-fetched a rejected key, which drew a 403 and a failed
    press-and-hold repair (row `Z-S45`).
  - wsj had no `reached_span`, because it read cached listings.
  - `q-1` was withdrawn @`3849afe124`.
- **Drained:** `q-2` @`0e3952dcab`, `q-4` @`906dbe0658`, `q-5` @`c6ebfc8b7a`, `q-6` @`75db57b063`. The trunk runs 657 passed.
- **`q-7` withdrawn** per the CTO (msg 27057): 0 of 191 eligible, so a flip could only HOLD.
- **`q-3` @`a40b6d5493`:** ELIGIBLE 0 of 191 (NOT_SEARCHED 190, PARTIAL 1).
- **Close run:** 13 of 13 rc 0. Packet @`699fb78c93`.
- **Incident:** my post-merge channel-union step met a peer's open merge. It failed on read, wrote nothing and staged nothing.

## Round 28 issued

- **Round-27 analysis @`8c0b34526b`** (msg 27073). PRD v0.5: the declared set is derived from config.
- **Ruling 4's premise was carded:** `silver_latest` groups by `article_key`, so the tie-break cannot supersede the 11
  hash-keyed empty bbg rows (11 of 30 bbg keys are served empty).
- **ONE issuance @`ffbcfc8937`:** `aa-1`..`aa-5`. `aa-1`, `aa-4` and `aa-5` spawned.
  - `aa-2` waits on `aa-1` and a fresh UTC day.
  - `aa-3` waits on the CTO ruling for the 11 rows.
