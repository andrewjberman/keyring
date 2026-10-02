# AMGT_RESAPP round 61 -- AMGT-ak-6, the 251-key stored-field rewrite (session 352b911c, second order)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, SCRIBE

## Window

08:23Z (ak-6 GO) -> 08:50Z. 2 commits by this lane, 3 inbound messages acted on and acked
(28316 GO, 28320 the ackable carrier, plus the ak-2 acceptance), 1 served-data act, 0 deploys.

## What I did

Act (A) only, per AMENDMENT 1: rewrote the stored display-text fields named by three FROZEN plans
across 251 distinct keys in the versioned bucket `opal-data-harvest` -- 8 `management/v1/`, 234
`peers/v1/`, 9 `posture/v1/`, 1,188 entries. No build, no upload, no apply.

**The GO's own basis was my own prior measurement.** AMENDMENT 1 removed act (B), the redeploy,
citing 0 of 350 packaged members changed between the deployed ak-2 build and the merged round-61
tree. That is the measurement this seat filed during ak-2 as row `AMGT_RESAPP-Z-S334`. A redeploy
would have rebuilt identical code.

**The GO arrived twice, and the second one is why it is ackable.** The 08:23:36Z file reached
`read/` with no `Msg-ID` -- its broker leg errored -- so the issuer sent msg 28320 as an ackable
carrier for the same GO. The file is authoritative; 28320 is what I acked. A file with no Msg-ID
cannot be acked, and an unacked GO leaves the READ clock untouched.

## Deployment Sequence (AE role section)

| # | act | result |
|---|---|---|
| 1 | condition 1: re-hash the three plans | B2 `d373d061..c4`, B3 `11518fd5..24`, B4 `0e77bc0c..84` -- all MATCH |
| 2 | B2 plan read from worker commit `25ac521b3d` | `git show` rc=0, 588,353 B; bogus-path positive control fails loudly |
| 3 | reconcile against the halves | 1,188 entries / 251 keys / prefix census 8+234+9; every key present in the base appendix |
| 4 | NEVER-2 entry opened, 5 legs | `20261002T0829Z_amgt-resapp-r61-ak6-stored-field-rewrite` |
| 5 | entry COMMITTED before the first PUT | `872b21a` |
| 6 | `b1_names.py --what pre` | `ak6-pre.json`, exit=0 |
| 7 | phase 1 DRY RUN: assert everything, write nothing | 1,188 of 1,188 befores match; 0 pin drift; 0 missing |
| 8 | phase 2: one whole-object PUT per key | 251 of 251 written, 1,188 of 1,188 entries, 0 failures, 251 of 251 moved |
| 9 | `ak6_verify.py` (CTO conditions 1-3 + C4) | AK6 READ-BACK CLEAN: YES |
| 10 | AC1 / AC2 / AC3 on the served routes | all PASS, exit=0 |
| 11 | per-entry served-equals-after (not a criterion) | 14 of 14 for BA and VLO |
| 12 | 5 legs closed, entry CLOSED, sentinel removed | absent from `deploy_ledger.py list` |

## Verification (ACTUAL output)

```
PASS C1 the plans are the frozen bytes [...three sha256 in order...]
PASS C2 every planned field reads the plan's after 1188 of 1188 fields; bad []
PASS C3 every object minus its planned fields equals its base version 251 of 251 keys; differing []; missing base []
PASS C4 every key moved off its base VersionId 251 of 251; unmoved []
AK6 READ-BACK CLEAN: YES
exit=0
```

```
PASS C1 no served reason carries a code-shaped token 0 of 26 strings: []
B2 EVERY SERVED REASON IS WORDS: YES
PASS C1 VLO officers carry person names, none a bare title 5 officers; title-as-name []
PASS C2 VLO roles carry no trailing age 0 of 5: []
PASS C3 BA officers unchanged in count 12 (cut 12)
B3 EVERY OFFICER CARRIES A FULL TITLE AND NO AGE: YES
PASS C1 no posture claim carries a status token 0 of 12 claims: []
B4 EVERY POSTURE CLAIM STATES A MISSING SCORE IN WORDS: YES
```

VLO's served officers, the row the earlier investigation named:
`'Harminder S. "Homer" Bhullar'` / `'Senior Vice President and Chief Financial Officer'` -- an
embedded quoted nickname and a title that had previously absorbed a trailing age, now both whole.

## Three things I did that no clause asked for

1. **Two-phase write.** The order and both halves say a differing `before` is "a STOP for the whole
   act, with nothing more written." Asserting key-by-key satisfies *nothing MORE* while leaving a
   partial act standing -- and the COO half itself warns a partial write covering BA and VLO can
   still pass AC1-AC3, because those grade 2 names out of 251. So phase 1 GET all 251 keys and
   asserted all 1,188 `before` values with zero writes; only a clean phase 1 unlocked phase 2. A
   mismatch anywhere would have meant zero objects touched.
2. **Rollback-pin drift check.** Both halves name the appendix VersionId as the rollback, written at
   signing. Phase 1 compared each key's LIVE VersionId to it: 0 drift. Had one moved since signing,
   copying that version back would have reverted a third party's write along with mine, so drift was
   treated as a STOP rather than a warning.
3. **Per-entry served-equals-after.** `ak6_verify` C2 proves the STORED field equals `after`;
   AC1-AC3 prove no bad *pattern* is served. Nothing proved the object I wrote is the text the route
   returns, per entry. `ak6_served_after.py` closes it: 14 of 14, with its denominator printed as
   **14 of 1,188** and explicitly silent about the other 1,174.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `ak6_verify.py --for "what C2/C3 compare"` | PASS | established that C3 compares PARSED objects, which is what makes the ASCII re-emit safe |
| `comp-read` | `b_served_text.py --for "where it looks for plan files"` | PASS | **load-bearing**: explained `plan entries 0 from 0 file(s)` and showed C0 is *skipped*, not vacuously passed |
| `comp-read` | `surprise-row-gate.py --enumerate 'SCHEMA_PATH\|...'` | PASS | found the schema whose required-field error the row had hit (carried over from ak-2) |
| `commit-gate.sh` | both new `.py` files | PASS | py_compile + ds-precommit + ruff clean, 2 of 2 |
| `comp-iam` | not re-run -- issuer ran it at the halves | n/a | 251 of 251 PUTs returned a VersionId, so the write grant is exercised, not assumed |
| `comp-schedule` | not run -- declared NOT-APPLICABLE | n/a | corroborated by the COO half's writers table: no scheduled writer on any of the three families |
| `comp-pipescript` | not run | n/a | no gold/silver/bronze script; a direct S3 rewrite under a never-widen pair |

**What worked.** `comp-read` on the grader before trusting its output. The printed line
`plan entries 0 from 0 file(s); stale or unlocatable 0 []` appears in all three AC runs and reads
like a measurement. It is the C0 clause skipped by its own `if a.plan:` guard -- no C0 verdict is
emitted at all -- and `--plan` is the grader's *pre-act* simulation path, which asserts `before`
then patches the body in memory. Run post-act with `--plan` it would correctly FAIL. I first read
that zero as a vacuous pass and corrected myself from the source.

**What failed.** Leg L1's proof text rode a Bash argument to
`deploy_ledger.py close-leg --proof "<4KB>"`. The text quoted the order's own wording --
"a differing \`before\` is a STOP" -- and bash command-substituted every backticked word away. The
leg closed rc=0 with the stored proof reading "a differing  is" and "all 1,188  values": the gate
satisfied, the evidence stripped of the exact nouns it existed to name. Repaired by a non-shell
writer; L2-L5 were then closed through a list-argv `subprocess.run([...])`, no shell in the path.

**Gap found.** `deploy_ledger.py close-leg` accepts only `--proof`, with no file form, so
CLAUDE.md's "use `-F`, authored by a non-shell writer" has no analogue for ledger evidence. The
durable fix is a `--proof-file` on that tool, owned by its own seat -- `deploy_ledger.py` is outside
this order's `<paths>` and I did not touch it. The incident is in git (leg L1 and commit
`4d12c64f00`). I attempted to bank it as a memory entry and the memory hook correctly refused:
seats do not write lessons to memory (Andrew-direct 2026-09-24); a lesson becomes a gate, field or
skill fix by its owning seat, and an incident stays in git history.

## Blockers

**None.** No open orders held by this seat.

## Current State

251 keys in `s3://opal-data-harvest` now serve the producers' words instead of code-shaped tokens:
8 under `management/v1/`, 234 under `peers/v1/`, 9 under `posture/v1/`. Per-key prior and new
VersionId are in
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ak6_store_writes.json`.
Rollback is per key: `copy_object` of the recorded `prior_version_id` back over the key, never an S3
delete; phase 1 confirmed all 251 keys sat on their appendix version at act time, so the documented
rollback is exact.

`opal-amgt-scoped-api` is UNCHANGED by this order and still runs ak-2's
`E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=` from 07:45:38Z -- act (B) was removed by AMENDMENT 1.

Serialization note: bodies were re-emitted with `ensure_ascii=True` so stored objects stay pure
ASCII. Measured after the fact: **0 of 251 prior bodies held any non-ASCII**, so no non-planned
field's bytes actually changed -- the precaution cost nothing and the receipt records
`prior_nonascii` per key either way.

Committed `872b21a` (entry opened) and `4d12c64f00` (instance VALID rc=0, 5 legs, evidence, two new
graders). NEVER-2 entry CLOSED. The `<status>` flip is the issuer's.

**Push state: LOCAL.** `origin/CLOUD` is `1f2346734b1d` by `git ls-remote`; local HEAD `4d12c64f00`.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Flip `<status>` on `AMGT_RESAPP.TO-AMGT-ak-6` and grade. Note AC1-AC3
   cover 2 names of 251 keys by construction; the full-population evidence is ledger leg L2 and
   `ak6_store_writes.json`, not the criteria.
2. **[`1.0.0_SA_CTO~Z`]** Optional, and not filed as a row: a `--proof-file` on
   `.tools/deploy_ledger.py` would close the class of defect recorded under "What failed" for every
   seat, not just this one.
3. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. Everything from this seat is LOCAL.
