# AMGT_RESAPP round 61 -- AMGT-ak-2, the company-name redeploy (session 352b911c, first order)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, SCRIBE

## Window

Session start (startup 06:44Z) -> 08:25Z. Seated by `2.0.0_SA_COO~Z` for AMGT_RESAPP round 61.
2 commits authored by this lane, 3 inbound messages acted on and acked (28268 staged-order,
28272 GO, 28309 row-schema correction), 1 deploy, 1 surprise row.

## What I did

**Startup.** `/watcher` (lane `~A` was NOT REGISTERED; re-registered, Monitor armed), then
`org/XXX.md` 1b A-F and `/cloud-ops`. The watcher census read 0 script rows on the skill's own
regex and 1 on a looser one -- the skill's pattern assumes an unquoted script path and this
device's repo path contains a space, so the arm command quotes it. Already banked as
`watcher-census-regex-reads-zero-on-a-quoted-path-with-a-space`; re-confirmed, no new memory.

**The 15-PENDING read is rot, not work.** `to-check.py --all --assignee 0.7.0_AE_CloudOps~A`
reported 15 PENDING task orders for this lane. Reading the appended `<status>` tags in
`org/missions/D5/AMGT/AMGT_RESAPP/task-orders/` (denominator 288 order files, 23 naming this
lane): all 15 read `last=complete`, except `vv-4` which reads `withdrawn`. to-check parses the
FIRST tag; orders append their flips. Zero work was owed. `2.0.0_SA_COO~Z` confirmed the same
read independently (msg 28268).

**ak-2, read while `staged`, preconditions measured BEFORE the GO.** The order's own begin-gate
has three clauses, so I measured all three rather than waiting idle: base CodeSha256 UNMOVED at
`UnSqZgCD...` (no re-sign owed), rollback artifact VersionId `1DFcRU3x...` still current, and
the CTO never-widen half ABSENT on disk. Reported those to the issuer; the GO arrived 6 minutes
later naming build commit `63e78fe4f7`.

**The act.** One artifact build+upload from a worktree at the GO commit, one code-only
`safe-apply`, AC1 then AC2, entry closed. Full sequence below.

**The gap I had to close before the act.** The CTO half's condition 2 asks for the
previously-unnamed keys' `display_name` and `name_source` printed BESIDE their pre-act values.
AC1's C1/C3 grade only the POST population, and round 61's `--what pre` records ONLY
CodeSha256/LastModified (`b1_names.py:61-65`). Those pre-act labels therefore existed on no
artifact, and the apply destroys them. I captured them first with a per-key census on the
criterion's own plane (`ak2_name_census.py`, read-only, three GETs through the same
`capture_lib._invoke` AC1 uses). That capture doubled as an unplanned control on the issuer's
comp-adversary declaration: declared 24 of 94 / 24 of 94 / 25 of 95 at the base, measured the
same three.

## Deployment Sequence (AE role section)

| # | act | result |
|---|---|---|
| 1 | NEVER-2 entry opened, 4 legs, window 3.0h | `20261002T0724Z_amgt-resapp-r61-ak2-company-name-redeploy` |
| 2 | entry COMMITTED before any deploy act | `124f21e26f` (refused once on a peer `index.lock`, landed on retry) |
| 3 | `b1_names.py --what pre` | `ak2-pre.json`, exit=0 |
| 4 | per-key name census, pre-act | 24 of 94 / 24 of 94 / 25 of 95, base figures AGREE with the declaration |
| 5 | worktree at `63e78fe4f7` | `C:/tmp/ak2-build`, detached (removed at close) |
| 6 | base re-read + `--build-only` | guard CLEAR; `CONTENT-DIFF SUMMARY: files 350, IDENTICAL 347, CHANGED 3, ADDED 0, REMOVED 0` |
| 7 | independent content-diff grade | PASS, set equality both ways, fabricated-path control discriminates |
| 8 | base + prior-version guard, then build+upload | VersionId `1DFcRU3xDzUsi84yZnWv985DDF1MymMn` -> `YSqlUTOWHwV6H7LePjd1pr9DKomiDo5U` |
| 9 | `terraform plan -out` | `Plan: 0 to add, 1 to change, 0 to destroy` |
| 10 | `safe-apply` of the SAVED plan | `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` |
| 11 | AC1, AC2 | both PASS, exit=0 |
| 12 | per-key census post-act + delta | 24/24, 24/24, 25/25 moved; 0 already-named rows changed |
| 13 | 4 legs closed, entry CLOSED, sentinel removed | absent from `deploy_ledger.py check` |

## Verification (ACTUAL output)

Live state after the apply, read at 07:46:21Z -- not the apply's rc:

```
E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=   2026-10-02T07:45:38.000+0000   41117744
```

Equal to the uploaded artifact's `content-sha256` and `ContentLength`, so the deployed bytes
are the built bytes. Base was `UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo=` @
`2026-10-01T13:59:33.000+0000`.

```
PASS C1 trending/price names every row status 200 rows 94 unnamed 0 [] ticker-as-name 0
PASS C1 breakout/price names every row status 200 rows 94 unnamed 0 [] ticker-as-name 0
PASS C2 positive control RMS_FP_Equity is named name='HERMES INTERNATIONAL' name_source='model_block_header'
PASS C3 the chatter set names every row status 200 rows 95 ticker-named 0 []
PASS C4 the overlay serves the row's display_name overlay 'HERMES INTERNATIONAL' row 'HERMES INTERNATIONAL'
EVERY PRICE BAR AND BUBBLE CARRIES A COMPANY NAME: YES
exit=0
```

```
PASS C2 every overlay display_name equals its row's 0 of 94 differ: []
EVERY BAR OPENS ONTO ITS OWN NAME: YES
exit=0
```

Both criteria were run TWICE. The first run graded them; the second produced the evidence
artifact after I noticed I had graded without capturing to file. Identical output both times --
re-run for the artifact, not for a better answer, and leg L4 records the distinction.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `build-and-upload-scoped-amgt.sh --for "bucket and key"` | PASS | gave `opal-313476888478-lambda-artifacts` / `research/opal-amgt-scoped-api.zip` |
| `comp-read` | `b1_names.py --for "what does --what pre record"` | PASS | **load-bearing**: revealed `pre` holds only a sha, which is why the per-key census had to precede the act |
| `comp-read` | `surprise-row-gate.py --enumerate 'SCHEMA_PATH\|schema.json\|SURPRISE_ROW'` | PASS | located `org/surprise_channel/schemas/investigation_item.schema.json` |
| `comp-find` | `--files 'AMGT_RESAPP\.TO-AMGT-aj-2' --limit 20` | PASS | located the tree task-orders dir after the base-folder path returned a 0-of-0 |
| `comp-find` | `'disposition.*enum\|DISPOSITION_...' --band DEF` | FAIL | 120s timeout, backgrounded, 0 matches. Too broad a regex over a 104k-file corpus |
| `comp-iam` | not re-run -- issuer ran it at the cut, 0 new actions, declared BLIND | n/a | gating clause is the plan's no-IAM change, which holds |
| `comp-schedule` | not run -- order declares NOT-APPLICABLE | n/a | one redeploy by hand, no cron/alarm/monitor |
| `comp-pipescript` | not run | n/a | a Lambda redeploy, not a gold/silver/bronze script; BOUNDS 1 forbids any store write |

**What worked.** `comp-read --for` on the check script is the single highest-value call of the
session: it turned "the pre file exists, so the before-state is captured" into "the pre file
holds a sha and nothing else," which is the difference between satisfying the CTO's condition
and claiming to.

**What failed.** `comp-find` with an alternation of loose regexes (`disposition.*enum|...`)
timed out at 120s against the 104k-file corpus. Censusing the live enum values in the target
file with python took under a second and gave the real answer. A schema question is better
asked of the schema than of the whole estate.

**Gap found.** Nothing in the round-61 check tooling captures the pre-act value of the FIELD the
act moves -- only the deployed sha. Every round whose CTO condition asks for a before/after on
served fields will hit this. The durable fix belongs in the check script (`--what pre` should
snapshot the graded fields, not just the config), not in each executor's private script.

## Blockers

**None.** Nothing is owed by this seat. `ak-6` is STAGED for this lane and waits on three worker
plans (`ak-3`/`ak-4`/`ak-5`) freezing -- that is the issuer's gate, not a blocker on me.

## Current State

`opal-amgt-scoped-api` (us-east-1, python3.11, timeout 29s) runs CodeSha256
`E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=`, LastModified `2026-10-02T07:45:38Z`, CodeSize
41,117,744, from `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
VersionId `YSqlUTOWHwV6H7LePjd1pr9DKomiDo5U`, built at commit `63e78fe4f7` from a worktree.
Rollback remains one code-only `safe-apply` with VersionId
`1DFcRU3xDzUsi84yZnWv985DDF1MymMn`, which restores `UnSqZgCD...` -- a write, not a delete.

Served effect: every row of TRENDING/PRICE and BREAKOUT/PRICE (94 each) and every chatter row
(95) carries a company name; the 24 + 24 + 25 rows that previously showed a ticker now carry
`name_source: model_block_header`; the per-name overlay serves the row's own name. 0 rows that
were already named had their name or source change.

Committed: `124f21e26f` (entry opened) and `b8481055c0` (instance VALID rc=0, 4 legs closed,
evidence, three graders, surprise row). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ak-2.the-company-name-redeploy.proof_of_spec.json`.
NEVER-2 entry `20261002T0724Z_amgt-resapp-r61-ak2-company-name-redeploy` is CLOSED and does not
appear in `deploy_ledger.py check`. The `<status>` flip on the order is the issuer's, not mine.

**Push state: LOCAL.** `origin/CLOUD` is `1f2346734b1d` by `git ls-remote`; local `CLOUD` is far
ahead. The push is `0.0.0_AB_MSTR~Z`'s act on Andrew's word.

**Row `AMGT_RESAPP-Z-S334`** (OBSERVATION, INERT, DISMISSED_WITH_REASON, disarm_owner
`2.0.0_SA_COO~Z`): the GO required the worktree build because a HARVST drain changed
`transport.py` and `load_window_grade.py` "and a HEAD build may package them". Measured --
neither is in the packaged closure, and 0 of 350 packaged members differ between `63e78fe4f7`
and HEAD, so a HEAD build would have produced the same CHANGED 3. The discipline is right and
was followed; its stated reason is not what makes it right.

## Two self-corrections, both caught by instruments rather than by me

1. The row first went in WITHOUT `dismissal_reason`, which the schema requires for
   `DISMISSED_WITH_REASON`. While uncommitted it put the standing corpus pass into a NEW-failure
   state that **refuses every surprise-channel commit fabric-wide**; `2.0.0_SA_COO~Z` flagged it
   (msg 28309) within minutes of my own gate run finding it. Fixed before commit.
2. The fix itself re-serialised all 710 rows -- a 15931/15906 diff on an APPEND-ONLY channel with
   concurrent writers, which is exactly what that file's own header warns against. Rebuilt as a
   true text splice off `HEAD` (25 insertions, 0 deletions) before committing. Lesson for this
   seat: editing a row in a shared JSON channel is not the same operation as appending one, and
   `json.dumps` over the whole array quietly converts the first into the second.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Grade the 24 keys and RMS as the GO said it would; flip the `<status>`
   on `AMGT_RESAPP.TO-AMGT-ak-2`. The per-key table it needs is ledger leg L3 and
   `ak2-evidence/ak2_name_delta.txt`. Also holds `AMGT_RESAPP-Z-S334` as disarm owner.
2. **[`2.0.0_SA_COO~Z`]** `ak-6` (the B2-B4 stored-field rewrite + redeploy) is staged for this
   lane behind the three worker plans. This seat is IDLE and ready for it.
3. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. Everything from this seat is LOCAL.
