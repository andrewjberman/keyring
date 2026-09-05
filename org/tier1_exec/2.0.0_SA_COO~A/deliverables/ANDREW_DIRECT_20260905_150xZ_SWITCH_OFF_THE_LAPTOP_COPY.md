# ANDREW-DIRECT 2026-09-05 ~15:0xZ, at the `2.0.0_SA_COO~A` terminal -- VERBATIM

> "we can switch off laptop copy"

Given unprompted, in response to this seat's `/exec-sum`, whose single **WAITING ON YOU** line was
whether to delete the laptop's local copy of the graph. Recorded here at the moment it was given so it
does not decay into recollection between now and the act, which is several hours and one task order away.

## WHAT IT AUTHORIZES, MEASURED RATHER THAN DESCRIBED

The word covers the local Kuzu database under `infra/aws/globgrph/`, which at the time of writing is
**six entries, 56,548,885 bytes total**, all **gitignored** (`infra/aws/globgrph/.gitignore:3`) and
**untracked** (`git ls-files --error-unmatch` returns "Did you forget to 'git add'?"), so removing them
changes no commit and no history:

| entry | bytes | what it is |
|---|---|---|
| `kuzu_nessie_db` | 48,070,656 | the database itself |
| `kuzu_nessie_db._build_manifest.json` | 942 | its provenance stamp |
| `kuzu_nessie_db.fallback.jsonl` | 9,504 | the stale-serve sink CG-s-8 removes the writer for |
| `kuzu_nessie_db.rebuild.lock` | (dir) | the mkdir mutex, left from a rebuild at 2026-09-04 12:53 |
| `kuzu_nessie_db.rebuild.tmp` | 4,096 | an interrupted rebuild's temp DB |
| `kuzu_nessie_db.rebuild.tmp.wal` | 8,463,687 | its write-ahead log |

## WHEN IT FIRES, AND WHY NOT NOW

⛔ **NOT YET, and the reason is the order's own text, not this seat's preference.**
`NFRA_CLDGRPH.TO-CG-D-7` states it twice:

> *"The laptop's own copy ... is NOT in your worktree and is NOT yours to delete: **the issuer switches it
> off at the drain** after your branch merges (recorded in the round-4 step log)."* (`:34`)
> *"The laptop's own DB directory is the issuer's to delete at the drain, never yours."* (`:80`)

and the cell it serves fixes the sequence:

> *"S8 STARTS when a reader exists and CLOSES when CG-x-7 passes (two machines, same answer, local copy
> off). **Retiring earlier breaks the estate's only graph**; never retiring is the shadow pipeline."*

**The concrete hazard of acting early is measured, not theoretical:** TO-CG-D-7's own criteria run
`comp-find` and `comp-blast`, and those route through `_canonical.ensure_fresh`, which **rebuilds a
BEHIND local database by design** -- the finding recorded at row `NFRA_CLDGRPH-S12`. Deleting the copy
before D-7 has removed that seam would either recreate the file or break the criteria that prove the seam
is gone. The retirement order exists precisely to make the deletion safe.

**The gate, therefore:** the deletion fires at the **TO-CG-D-7 drain**, immediately after that branch
merges and before TO-CG-D-8 observes the absence (D8-AC3 expects `ls infra/aws/globgrph/ | grep -c
kuzu_nessie_db` to read `0`). D-7 is LAST by ruling R7 and is currently behind TO-CG-D-10, which is
running as this is written.

## HOW IT WILL BE DONE, AND WHAT WILL BE SAID AFTERWARDS

- All six entries removed together, by exact path, never by a wildcard that could reach wider.
- The byte counts above re-measured immediately before, so the record states what was actually removed
  rather than what was expected to be.
- A `ls` of `infra/aws/globgrph/` after, showing zero matches, quoted in the step log.
- ⛔ **No backup is taken and none is implied.** The whole point of FWD-7 is that the estate keeps ONE
  graph story; a preserved copy is the duplicate output path the standing rule forbids. The served cloud
  graph is the copy, and TO-CG-D-6 has already proved a machine that never held the local database can
  ask and be answered.
- Recorded in `STEP_LOG.2.0.0_SA_COO~A.round4.json` at that drain, citing this file.

## SCOPE, HELD NARROW

This word authorizes **the deletion of the laptop's local graph database and its five siblings, once, at
the D-7 drain.** It is not a general deletion permission, it does not extend to any other project's local
state, and it does not alter the standing push hold -- every commit of this run remains LOCAL until
`0.0.0_AB_MSTR`'s window on Andrew's separate word.
