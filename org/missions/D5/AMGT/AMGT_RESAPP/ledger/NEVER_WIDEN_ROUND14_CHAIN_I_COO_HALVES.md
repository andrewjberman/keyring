# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain I (identity). One section per co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_I_CTO_HALVES.md` (DESIRED plane -- the source diff
and the producer's rule). **This plane:** APPLIED and EXERCISED -- what the act MAY touch, the writer census of every
named property, the per-key rollback from the LIVE PRE-ACT state the worker measures fresh, and both branches of every
expected outcome. Neither half stands alone; the worker reads BOTH files (their sha256 into its change-management entry)
before its first live act and STOPS with a BLOCKING row if either is absent (order section 1, bound (c)).

A half names the act's BLAST RADIUS, never the producer's decision (CLAUDE.md s.5 NEVER-1): every outcome below is read
from the producer's own rule as the order inlines it, and covers both branches.

## `AMGT-rk-31` -- add-a-security entry writes a NEW dated crosswalk object (R14-I1; FWD-2, V1; C-INSTANTIATION-ENTRY)

**THE ACT.** `python -m lib.research.identity.add_security --bloomberg "<id>" --as-of <today> --write-pool` for exactly
three names -- `CAT US`, `CSL AU`, `6861 JP` (C-VALIDATION-NAMES) -- and the corpus-folder form for the same three.
Each run lands ONE raw object and, at the end, the newest crosswalk object.

**BLAST RADIUS -- the keys the act MAY touch, and nothing else.**
- `s3://opal-data-harvest/crosswalk/v1/<today>.json` -- ONE NEW dated key. `crosswalk/v1/2026-09-15.json` (the population
  of record, MEASURED = 33, 89 records) is NEVER modified: `write_pool()` writes only the `<as_of>` key it is handed and
  its put is ETag-conditional (order section 1, bound (b)).
- `s3://opal-data-harvest/raw/bloomberg/<KEY>/<stamp>/identity.json` for the three keys -- put-if-absent, fresh stamps,
  the existing raw landing family; no existing raw object is overwritten.
- NO Lambda, NO Terraform, NO IAM, NO page. The Lambda `opal-amgt-scoped-api` is NOT redeployed by this cell.
- REACHABILITY, stated plainly: the adapter resolves every key through the NEWEST crosswalk object, so the new dated key
  is reachable by every served route the moment it lands. That is why this cell is co-signed although it moves no code.

**WRITER CENSUS of the named property (`crosswalk/v1/<newest>`): N = 2 writers at HEAD** -- `lib/research/identity/
crosswalk.py write_pool()` (called by the round-13 population producer, `--as-of` explicit) and, after this cell,
`add_security.py` calling the SAME `write_pool()`. Both write a dated key and neither rewrites an existing one; the property
"newest object" is moved by whichever wrote the later date. No scheduled producer writes this prefix (the round-13
analysis s.3 lists none; `comp-schedule` at the cut: 0 matches on `crosswalk`). Rule read for BOTH writers: a dated key
is appended, never replaced.

**EXPECTED OUTCOME -- both branches, read from `add_security.py`'s rule as the order inlines it (section 1, items 3-6).**
- Branch RESOLVED: the newest object reads MEASURED = 33 + k (k = names whose Bloomberg call resolved, at most 3), every
  base record byte-identical (AC6: `base_records_byte_identical_in_newest N of N`, N = 89), DELTA = 0 on the 33.
- Branch UNRESOLVED (a Bloomberg call fails, the terminal is signed out, or a name refuses the entity test): the name is
  written UNRESOLVED with its reason and COUNTED, never dropped; MEASURED still = 33 + (resolved count); base records
  still byte-identical. The act is covered on this branch too -- the rollback below applies unchanged.
- Branch NOT RUN (the pair absent at spawn, AC1-AC3 only): nothing lands; this half covers nothing because nothing moved.

**PER-KEY ROLLBACK, from the live pre-act state the worker measures FRESH.** Pre-act: `list_objects_v2 crosswalk/v1/`
(count and newest key -- expected 2026-09-15.json newest) and `head_object` on each of the three raw keys (expected 404),
all recorded in the change-management entry before the first `--write-pool`. Rollback = `delete_object` of the ONE new
crosswalk key (the newest then reverts to 2026-09-15.json by the adapter's own newest-key rule, with no redeploy) and
`delete_object` of the up-to-three new raw keys. No object is restored because no existing object is written.

**NOT COVERED by this half (a new act, a new pair):** any write to a crosswalk key other than `<today>`; any run on a
name outside the three; any `--write-pool` over the 33 covered names (Andrew, verbatim: *"I dont care about rerunning
until the process is completely validated end to end"*); any adapter redeploy.

**Change-management:** the worker opens the entry with `.tools/deploy_ledger.py open` (legs L1 git, L2 verify receipt,
L3 verify DELTA=0) BEFORE the first `--write-pool`, sentinel COMMITTED, and closes every leg with its proof.

**PRECISION added ~22:0xZ on `1.0.0_SA_CTO~Z`'s source read (msg 23819, `crosswalk.py:627-628`):** the sentence above,
"its put is ETag-conditional", is true but is NOT what protects `2026-09-15.json`. `write_pool()` refuses nothing: a new key
puts with `IfNoneMatch "*"`; an existing key with the same sha is skipped; an existing key with DIFFERENT bytes is
OVERWRITTEN under `IfMatch <ETag>`. The protection is the CALLER'S key argument, so this half binds (and the order's bound
(b) + AC8 now carry): `add_security.py` REFUSES any `--as-of` that is not today UTC when `--write-pool` is given, exercised
as a planted negative control on a past date (would rewrite the record) and a future date (would win `_read_pool_latest`'s
`sorted(keys)[-1]`, `:513-530`, and be served at once). The rollback stands as written for the same reason: the adapter
resolves through the sort, not a pointer, so deleting the new key restores the prior newest with no redeploy.

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut (the CTO's concurrence that this pair is OWED: @44702e4e90).
