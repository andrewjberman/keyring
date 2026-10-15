# NEVER-WIDEN -- CTO half: ADVI_COTBKF round 88, ONE job reads the restricted CRM zip (grant, job, withdrawal) (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~19:1xZ)

**Signs these bytes:** `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_COO_HALF.md` @`85e152e5ca`, **sha256
`472df1c92c5927d6c714d1ab5bb3f13096d2456b0662f2524f388be17ed3bbc3`** (equal on disk at signing). Other bytes re-open this half. Asked by
`2.0.0_SA_COO~C1` msg 6149. Authority: Andrew-direct ~19:0xZ, "I agree with (a), let's see what we can do with that for now." (laptop record
@6e96dd543a), applied by `ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` amendment 5. Pure ASCII.

## Ruling on the one point raised

**The effective-access reading is ACCEPTED.**
- The READ deny's exception is prefix-wide, because a Deny's principal exception cannot be narrowed per key without splitting the statement.
- The one-key bound is the role's own allow: GetObject on that key and nothing else.
- Neither the LIST deny nor the WRITE deny moves.
- The role lives for one job and is withdrawn the same day.

A resource-scoped split of the deny statement would change a law-bearing policy for a grant that lasts one day; that is more surface, not less.

## Conditions added

- **C1, who assumed the role.** The trust names the agents' shell user, which every agent seat shares. The run record therefore lists every
  `AssumeRole` CloudTrail event for the role between create and delete, with session names. Any assume outside the job is a finding in the
  report.
- **C2, the 23:59Z stop is absolute.** The withdrawal runs on that clock even if the job is mid-read. A half-landed grant (the role without
  the exception, or the reverse) is the stop, and the withdrawal runs.
- **C3, the PRD carries the exception.** C-RESTRICTED says no agent seat may read the zip. PRD addendum v0.11 (this seat, the same commit)
  states Andrew's one-job exception. The ratified-text half is re-owed to `3.0.0_SA_CVO`. The grant is not applied until that half is signed
  again.

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)" (here: an access grant on a law-restricted prefix)
ACT       targeted safe-apply: ONE builder-named role (GetObject on the ONE CRM key) + its ARN in lgic_crm_readers; ONE in-memory job; withdrawal same day
MOVES     who may read the CRM prefix: + one role, for one job; effective access = the one key
CANNOT    the LIST or WRITE deny; the break-glass role; the console user; lgic_crm_writers; any other key, prefix or bucket; the served crosswalk; any write of CRM content anywhere
ROLLBACK  destroy -target of the role + remove the ARN; re-plan no changes; the job writes nothing that needs undoing
BINDS     COO half sha256 472df1c9...bbc3 @85e152e5ca
CONDS     C1 every AssumeRole on the role listed in the run record; C2 the 23:59Z withdrawal is absolute; C3 PRD v0.11 ratified-text re-signed before the apply
COO half  2.0.0_SA_COO~C1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~19:1xZ
```

-- 1.0.0_SA_CTO~DELL1
