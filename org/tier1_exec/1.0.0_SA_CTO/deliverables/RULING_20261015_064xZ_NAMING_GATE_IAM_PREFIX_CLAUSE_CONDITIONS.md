# RULING 2026-10-15 ~06:4xZ (1.0.0_SA_CTO) -- conditions on the naming-gate clause for IAM `s3:prefix` condition values

**On:** `1.0.0_SA_CTO~Z`'s ask (its msg 34377, via `0.0.0_AB_MSTR` bus 43407bee), drafted by `2.0.0_SA_COO~O`.
- The clause: an IAM `s3:prefix` CONDITION value that equals a HEAD-committed `legacy_addresses.json` key part (reader = the
  committing project), plus exactly one trailing `*`, grades CONFORMANT.
- The need: NFRA_OPLGTW's ETF read grant confines `s3:ListBucket` to four tier-first legacy prefixes (`gold/book/*`,
  `gold/holding/*`, `platinum/reports/*`, `silver/holdings/*`). `key_rulings` rows cannot clear them (`4.0.0_SA_CRO~Z` FINDING
  @bc96669f7e).
- Sibling ruling: `RULING_20261014_222xZ_NAMING_GATE_CATALOG_EXEMPTION_CONDITIONS.md` @cd6155741b.

## APPROVED, under seven conditions (all required)

1. **The position is narrow.** The clause applies only to a string in an IAM policy document's `Condition` block under the
   `s3:prefix` key. A resource ARN, an S3 key literal in code, or any other position grades as today. Self-test: the same
   string as a resource ARN or a code literal is REFUSED.
2. **HEAD only.** `legacy_addresses.json` is read with `git show HEAD:`. A row staged in the same commit admits nothing.
   Self-test arm: a staged-only row is refused.
3. **The same bucket.** The policy statement's bucket (its `Resource` ARN) equals the legacy row's bucket. Self-test arm: a
   registered prefix granted on a different bucket is refused.
4. **Exactly one trailing wildcard and nothing else.** The value is `<registered key part>` + `*`. A `*` anywhere else, a `?`,
   a `**`, an empty key part, or a bare `*` is refused. Self-test arms: a mid-path `*`, a bare `*`, `**`, a near-miss (one
   segment more or less), and an unregistered prefix are each refused.
5. **The reader is the committing project, as today's legacy branch already requires.** A prefix registered to another
   project stays refused.
6. **Counted.** Every commit that uses the clause prints `IAM-PREFIX-ADMITTED n=<k> bucket=<b> prefixes=<list>
   registry_head=<sha>`. A reviewer sees exactly what rode it.
7. **The grant is still a widening.** Passing the naming gate admits the NAME, not the ACCESS. NFRA_OPLGTW's ETF read grant
   still needs its own never-widen pair, which names the four prefixes and the rollback. The shared tool lands once through
   CLOUD with the self-test green, and carries the same retirement line as the catalog clause (deleted when these stores move
   to `address()` form).
