# The source map now describes the build that is running — 0.7.0_AE_CloudOps~TV2

**archetype:** SCRIBE

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-RECORD-R3-sm1.ticket-api-deploy-record-dell2 (read at `11c612ede3`)
**Status:** COMPLETE — AC1 `SM1-RECORD-OK`; a git record only, no AWS write

---

## Objective

Make `lambda-source-map.json`'s `opal-ticket-api` entry describe the live build, by running the
repository's own recorder scoped to that one function. Cell `R3-sm-1` — the record the round-2 applies
never wrote, and the answer to my own row S25.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| record-terraform-deploy.sh | `ticket-center --function opal-ticket-api --author …` | PASS | read first, then run unmodified; `stamped 1 of 1 rows`, never `--all` |
| comp-blast | on the map | WARN | `SUBJECT_ABSENT_FROM_CORPUS` over 29860 nodes — a NOT-FOUND, **not** a clear, in its own words |
| comp-pydeps | `consumers` on the map | PASS | comp-blast's own pointer; 1 code consumer over 1148 py files |
| comp-find | `lambda-source-map` SURFACED; `aws sns publish` on the recorder | PASS | named the tooling readers; pinned the SNS site at `:871` |
| AC1 checker | before **and** after | PASS | `SM1-RECORD-FAIL map=ywAvsfx/ live=t1EoiJRZ` → `SM1-RECORD-OK` |
| safe-commit.sh | invoked by the recorder with my author forwarded | PASS | commit `6a5bee406c`, exactly its declared pathspec |

**What worked:** reading the recorder's code before running it — the order required it, and it is the only
reason I knew in advance that the script can publish to SNS. A 923-line script that "just stamps a
commit" does five things.

**What failed:** nothing. Four gates WARNed that they checked nothing or could not decide, and those are
recorded as WARNs rather than cited as validation — see Verification.

**Gap found:** one, S36.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | READ the recorder (header, `:60-120`, `:499-550`, `:843-880`, `:885-923`) | `--function` scopes via `record-deploy-scope.py`, which is forced to python and **refuses rc=2** rather than falling back to the pipeline-wide sweep; `last_deployed_commit` = last commit touching `source_dir`, **not HEAD**; reconcile sets `artifact_sha256` to the *deployed* CodeSha256, settle-aware 45s, audited; pathspec = map + CHANGELOG if written + audit log only if this run changed it |
| 2 | `comp-blast` on the map | not a graph node; readers named via `comp-pydeps` and the rail; none changed |
| 3 | BEFORE + dirt check | `ywAvsfx/…` / `da431554…` / `2026-10-07T19:37:43Z`; live `t1EoiJRZ…`; **0 dirty rows** on both paths, so the worktree branch did not fire |
| 4 | Run the recorder, one function | `+ opal-ticket-api da43155418 -> 861c9bba65`; `stamped 1 of 1`; CHANGELOG `untagged-0a8d4b56`; reconcile OK; commit `6a5bee406c` |
| 5 | Four after-reads | all pass — see Verification |
| 6 | Report once | the before/after triples, (a)–(d), the commit, push state |

## Verification

```
(a) entry artifact_sha256      t1EoiJRZWXBsSc0HPw+61IP+zdQxyYGfWEi+8L6lej4=
    live   CodeSha256          t1EoiJRZWXBsSc0HPw+61IP+zdQxyYGfWEi+8L6lej4=   -> equal
    AC1 before: SM1-RECORD-FAIL map=ywAvsfx/ live=t1EoiJRZ
    AC1 after : SM1-RECORD-OK

(b) stamped last_deployed_commit 861c9bba65eaf10b123698f8662f340297bc0967
    its lambda_function.py       cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74
    deployed file (required)     cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74
    -> EQUAL, so no finding is owed. 861c9bba65 is the R2-pk-1 AMENDMENT 1 worker commit
       (handler +2 lines, four test files) -- the last commit touching source_dir. I
       deployed from the drain merge be67d1fd38, a different commit with the same handler
       bytes, so the recorder's source_dir rule and the deployed bytes agree BY CONTENT.

(c) commit 6a5bee406c, three files and no others:
      lambda-source-map.json              6 lines
      source-map-reconcile-audit.jsonl    1 line
      ticket-center/CHANGELOG.json      132 lines
    map entries before 235 | after 235 | added 0 | removed 0
    CHANGED ENTRIES: 1  ['opal-ticket-api']   <- counted, not read off the diff shape
      artifact_sha256      ywAvsfx/... -> t1EoiJRZ...
      last_deployed_at     2026-10-07T19:37:43Z -> 2026-10-11T10:18:21Z
      last_deployed_commit da431554...          -> 861c9bba65...

(d) live CodeSha256 unchanged; LastModified still 2026-10-11T09:47:09Z (the R2-pk-2 apply)
    -> this act wrote nothing to AWS

gate output, recorded as WARNs and NOT cited as validation:
  commit-gate     checked 0 of 3 files (no .py/.sh/.tf in the set)
  risk-reflex     PARTIAL_OR_BLIND, danger map 97.9h STALE -- "could not check is not checked clean"
  client-data     hashed account-id list ABSENT -> commit NOT checked for client account ids
  one-writer      the reconcile audit log is the laptop's unsuffixed file, written from dell2
                  ("WARN until C-QUEUE") -- owned, pre-existing
  naming-gate     PASS 0 graded over a 2-path domain
```

---

## Decisions Made

1. **Said where the code disagrees with the order, as step 1 required.** The order's objective and bounds
   both say "no AWS write". The recorder carries an `aws sns publish` to `opal-infrastructure-alerts` at
   `:871`, in the else branch of the reconcile. It did **not** fire — the reconcile took its OK branch
   because the R2-pk-2 apply fully landed — so no AWS write occurred. But the bound held because of the
   world's state, not because the act cannot write. Row S36.
2. **Did not treat `comp-blast`'s empty answer as "nothing reads this".** It returned
   `SUBJECT_ABSENT_FROM_CORPUS` and says in its own output that this is a NOT-FOUND, not a clear. I
   followed its pointer to `comp-pydeps` and the rail instead, and named the readers properly —
   `deploy_ledger.py` among them, the tool I have used all session.
3. **Ran AC1 before as well as after.** A criterion that only ever passes proves little; the base reading
   `SM1-RECORD-FAIL map=ywAvsfx/ live=t1EoiJRZ` matches the issuer's dry-run exactly, so the check
   discriminates.
4. **Counted the scope rather than eyeballing the diff.** "Only one entry moved" is a comparison of the
   full 235-entry set across the commit, not a reading of the diff's shape.
5. **Computed the surprise id at write time, inside the appending script.** Earlier today a peer took the
   id between my read and my append and I had to re-identify my own row. Doing both in one script closes
   that race.
6. **Did not tag or push.** The recorder's closing "Next steps" suggests both; neither is in this order's
   GO or `<paths>`, and the version label is a default placeholder rather than a chosen tag.

---

## Files Modified

| File | Commit |
|------|--------|
| `lambda-source-map.json`, `ticket-center/CHANGELOG.json`, `source-map-reconcile-audit.jsonl` | `6a5bee406c` (by the recorder) |
| `TCKT_VNEXT.TO-RECORD-R3-sm1…proof_of_spec.json`, this log, row S36, TO status | this commit |

No AWS resource was touched, and (d) is the evidence.

---

## Blockers

None. Row S36 is an observation for the issuer and the CTO, not a block: either the "no AWS write" bound
gets restated to admit the one best-effort publish, or the recorder's alert limb becomes conditional.

---

## Current State

`opal-ticket-api`'s entry is accurate for the first time since 2026-10-07: it names the live artifact
hash, a stamped commit whose handler is byte-identical to the deployed file, and today's timestamp. Row
S25 — my own finding from this morning, that the entry was three deploys behind — is answered.

The next cell's precheck can read this entry instead of a hand-typed list of builds, which is the
standing fix for row S28.

---

## Next Steps

1. S36 to the issuer and the CTO.
2. The round-3 cell that reads this entry in place of `TICKET_OK`'s hand list (S28's remedy).
