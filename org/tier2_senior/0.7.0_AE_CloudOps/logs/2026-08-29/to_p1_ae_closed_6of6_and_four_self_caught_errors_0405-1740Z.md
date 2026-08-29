# 0.7.0_AE_CloudOps~Z -- 0405-1740Z: TO-P1-AE closed at 6 of 6, and four errors caught by instruments rather than by me

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, SCRIBE

## Window

0405Z -> 1740Z. Prior log: `reland_complete_and_relayed_authorisation_refused_0300-0405Z.md` @`c4d7e4ac42`.

## Outcome

`D1_CATVIEWS.TO-P1-AE` is CLOSED at 6 of 6 by `2.0.0_SA_COO~Z`, accepted 6/6 by
`3.0.0_SA_CVO~Z`. The proof-of-spec instance is filed and VALID.

```
  TP1AE-AC1  PASS  live_read                 4 of 4 scopes on the SCHEDULED fire
  TP1AE-AC2  PASS  command                   D1-inv-2   4/4, every delta +0.00
  TP1AE-AC3  PASS  command                   D1-inv-4   16/16, 8 VACUOUS excluded
  TP1AE-AC4  PASS  command                   D1-inv-3   5 of 5 byte-unchanged
  TP1AE-AC5  PASS  manual_read_with_citation 4/4 arms on the DEPLOYED bytes
  TP1AE-AC6  PASS  diff                      re-cut pin BY CONTENT + negative control
  proof-of-spec-check.py -> VALID, rc=0. Alignment 6/6 fwd-1, 3/3 fwd-2, 3/3 backward.
```

## THE FOUR ERRORS, because they are the useful part of this window

Every one was caught by an instrument or a peer, none by my own review of my own work.

**1. `find org -name "*TP1AE*" | head -8` -- I HEADED A CENSUS.** The 8 inbox hits filled
the window and I concluded my own AC4 baseline artifacts did not exist. They did, committed,
in my own lane. The banked rule is "never `head` ANY census" and I broke it while looking
for my own work.

**2. The AC4 scorer REFUSED on my own deploy artifact.** `_code/mdpf-gold-lambda.zip`
rewritten 804455 -> 834732 -- my rebuilds #2/#3. A TRUE observation against the WRONG
invariant: `gold-lambda.tf:116` declares that key as the lambda's `s3_key`, so rewriting it
IS the deploy mechanism. My LEG3 swept the deploy plane into a data invariant. Narrowed to
exclude REWRITE failures ONLY; deletion still fails; the key is still PRINTED.

**3. The proof-of-spec checker caught me citing the WRONG DECOMP.** I named
`20260828T2130Z`, copied from the TO-R1-AE sibling's instance, where this face names
`20260824T195537Z`. Plus six invented enum values and a string where an array is required.
`org/standards/PROOF_OF_SPEC.schema.json` existed the whole time; I wrote first and read it
after being refused.

> **AND THE CHECKER'S OWN WARNING IS THE THING TO KEEP: the alignment figures printed on my
> INVALID draft were IDENTICAL to the valid one's -- 6/6, 3/3, 3/3. "They are NOT evidence
> of validity. Do not quote them without the verdict."** A wrong-decomp instance produces
> perfect-looking alignment arithmetic about the wrong id space.

**4. I walked into the hazard I had warned five seats about.** At 0308Z I told the fabric
that `deploy_ledger` removes the sentinel at CLOSE, leaving the markdown as the only carrier,
untracked on a shared checkout. I then closed two ledgers and left exactly that for an hour.
The sentinel DELETIONS mattered as much as the edits: uncommitted, they resurrect on another
checkout and re-alarm a deploy that is closed on proof.

**The shape common to 1, 3 and 4: knowing a rule and applying it to my own work are
different acts, and the second is the one that keeps failing.**

## Deployment / verification work

- **Both D1_CATVIEWS ledgers CLOSED on proof and the closures COMMITTED** (`1694968163`).
  `catvp-c-publisher-derived-type-axis` L2 closed on the 13:50Z SCHEDULED publisher fire,
  manifest `20260829T135046Z-0ae2ff1b`.
- **The L2 discriminator went through three forms and only the last is sound.** My first was
  a TWO-key id list -- and a THIRD ad-hoc manifest existed (`20260829T035610Z-c9e85dd4`) that
  I had missed by reading my chain's return value instead of listing the prefix. Anyone using
  my list would have closed L2 on my own ad-hoc run. Replaced by a temporal floor; hardened by
  `3.0.0_SA_CVO~Z` to the FILENAME stamp (dodging the `s3 ls` local vs `s3api` UTC trap); and
  the final check is better than all three: **`trigger.source` is empty on the scheduled run
  while this seat's ad-hoc runs carry `source=adhoc, run_class=adhoc-qa`.** The artifact
  identifies its own plane and nobody has to remember anything.
- **Two advi-49f ledgers dispositioned** (`920facba7c`). Entry A CLOSED on measured git
  evidence; entry B's L3 closed and **L4 deliberately NOT fired** -- it requires SSM sends with
  a parameter omitted to rule out a halt-trap, so if the hypothesis is wrong the exercise stops
  the host. An exercise whose FAILURE MODE is a reserved act inherits that reservation.
- **`0.0.0_AB_MSTR~Z`'s three SmartX SFTP drafts preserved** (`10c3477b99`) -- sole copies,
  untracked ~10h, `infra/**` is this lane and not theirs. Read all three first: 12 secret-pattern
  hits, every one a HARDENING line.
- **Build sidecar committed with this log** -- `mdpf-gold-lambda.BUILD_MANIFEST.json` had been
  uncommitted ~15h. Verified against live before committing: pin and zip sha256 both match the
  deployed function exactly.

## Blockers

**Rebuild #4 HELD for leg C**, which is blocked at ANDREW on the 0833 scope grant. The hold is
cost-free in both branches: measured by `0.4.0_DS_ClientPlatform~Z` that zero `by_model` keys
resolve to an additive member, so `73c2dea263` and `b6e97e9685` produce byte-identical output
until a `tax` key exists, and `tax` cannot exist until leg C.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| proof-of-spec-check.py | on the TO-P1-AE instance, 3 runs | PASS (3rd) | caught the wrong-decomp citation, 6 enum errors, 1 type error |
| commit-gate.sh | on 2 new scorers | PASS | clean 1/1 each |
| deploy_ledger.py | close-leg / close / check | PASS | 2 ledgers closed, sentinels removed AND the removals committed |
| TP1AE-AC4 scorer | `--self-test` then live, x2 | PASS | self-test caught my own incomplete edit (2 unpack sites) |
| TP1AE-AC2/AC3 scorer | `--self-test` then live | PASS | authored this window; 2-arm gated before use |
| mdpf-gold-packaged-check.py | on producer commits vs the deployed pin | PASS | 2 members stale, unchanged all window |

**What worked:** self-test gating on both scorers. Each one caught something before it could
reach a record -- the AC4 self-test refused after my incomplete edit, and the AC2/AC3 self-test
proved the vacuous detector fires before I trusted its 16/16.
**What failed:** `python .tools/mdpf-gold-packaged-check.py ... | tail` -- `$?` captured *tail's*
rc, so a WARN with rc=1 printed as rc=0. My own banked "a pipe resets `$?`" trap, walked into
while using my own instrument.
**Gap found:** `deploy_ledger.py` still has no `close-leg` path for an unindexed (hand-authored)
record. The tool DETECTS that class and cannot remediate it -- which is why the two advi-49f
entries alarmed for 31.7h and why both had to be dispositioned by hand-editing the status line.

## Current State

- `D1_CATVIEWS.TO-P1-AE` CLOSED 6/6; instance at
  `org/tier2_senior/0.7.0_AE_CloudOps~Z/deliverables/D1_CATVIEWS.TO-P1-AE_PROOF_OF_SPEC.json` @`d18fb1e846`.
- `mdpf-gold-lambda` runs pin `73c2dea263`, CodeSha256 `U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=`,
  `MDPF_GOLD_COMMIT` == in-zip vintage, 22/22 modules verified. Rebuild #4 owed and held.
- Served plane: 4 scopes, publisher run `20260829T135046Z-0ae2ff1b`. **TWO `as_of` dates live
  at once** -- cottonwood 2026-08-28, the other three 2026-08-27.
- Deploy-ledger sweep clean of this seat's work. Estate-wide: `freshguard-leg4` HELD on Andrew's
  alarm moratorium, `advi-49f-ssm-date-param` correctly open on its one un-fired exercise.
- THREE open calls at Andrew, one BLOCKING (0833 scope grant).

## Next Steps

- [ANDREW] The three open calls. Only the 0833 grant blocks anything.
- [0.7.0_AE_CloudOps~Z] Rebuild #4 at one pin once leg C lands -- build, upload, `safe-apply`,
  22-of-22 audit on the DOWNLOADED package. ~12 minutes.
- [ETFS_INGEST instance, when spawned] Z-S31 (replay remedy PRESENT but INERT --
  `ETFS_REPLAY_FROM_BRONZE` absent from the live env), Z-S16, Z-S22.
- [unowned] `deploy_ledger.py` has no close path for unindexed records; the next hand-authored
  ledger lands in the same hole.
