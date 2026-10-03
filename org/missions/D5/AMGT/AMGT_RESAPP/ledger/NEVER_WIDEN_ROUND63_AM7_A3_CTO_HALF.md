# AMGT_RESAPP round 63 -- `AMGT-am-7` AMENDMENT 3 never-widen pair, CTO half (three officer objects from Andrew's one Bloomberg pull)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~19:2xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM7_A3.md` @af927eee81 (msg 28688).
**Executor:** `0.7.0_AE_CloudOps~A`.
**Input:** am-2 AMENDMENT 2 @af6184d5b0: ONE `COMPANY_EXEC_OFFICERS` pull on Andrew's per-use word ~18:1xZ ("thee allow"; record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_181xZ_ALL_RECS_APPROVED_OPALAI_PUSH_BLOOMBERG_ALLOW_REMOVE_WORKTREE_CLOUD_PULL_PUSH.md`).
The pull is done. Bronze holds three versioned objects, with the VersionIds printed in the COO half.

## What I read

- **Three PUTs to three NEW keys,** `management/v1/{ASML_NA,6501_JP,2317_TT}_Equity/2026-10-02T1840Z.json`:
  - each key reads 404 before the act;
  - each file's sha256 is checked against plan `m1_fwd7_plan_a2.json` (ca25158b...);
  - a `head-object` follows each PUT.
- **The route's own rule:** `read_pool_object` serves the LAST key in key order, and `...T1840Z.json` sorts after `2026-10-02.json`.
  Each object therefore serves on the next request, with nothing overwritten.
- **Both branches, read through the same reader locally (3 of 3):**
  - C1: ASML_NA moves from ABSENT to SERVED, BLOOMBERG_FALLBACK, 7 officers;
  - C2: 6501_JP serves 37 officers and 2317_TT 8, each moving from a reason-only object to SERVED;
  - a sha256 mismatch is a STOP before writing;
  - a c2 miss is superseded forward.
- **Writers:** the management batch builds only `real_filing` names and never writes these three, so this act is the only writer.

## Named, and accepted with a condition

**The body's `as_of` is the date `2026-10-02` (the schema requires a date), while the KEY carries the time.** Two objects now share a
body `as_of` under each name. The route orders by KEY, so it serves correctly. Any other reader that orders by the body's `as_of`
would see a tie.

**Condition:** the leg-v read prints, for each name, the served object's KEY beside its `as_of`. The next schema touch on
`management/v1` (not this act) adds the source stamp to the body (for example the bronze object's timestamp or VersionId), so the
body says which object it is.

## Blast radius and rollback

- Three NEW keys. There is no overwrite and NO delete, ever.
- **Rollback is a forward supersede:** PUT the bytes of the object served before the act (`2026-09-18.json` for ASML; `2026-10-02.json`
  for the other two) under a newer as_of key, named at that time under a re-sign.

## Conditions

1. A sha256 mismatch before any PUT is a STOP, and `head-object` after each PUT prints the VersionId.
2. The post-act read is `r63_served.py --cell c2 --where deployed`. It prints C1 and C2 with officer counts 7 / 37 / 8, and the
   served key beside the `as_of`.
3. After this act, DSGN FWD-7 is re-gradeable on PROD for all three names. The grade request goes to `3.0.0_SA_CVO~Z`.

**CTO HALF: SIGNED** for am-7 AMENDMENT 3: three PUTs to the three named new keys, with the forward-supersede rollback and no delete.
