# self-drive AMGT_RESAPP -- ticks 71-73, `1.0.0_SA_CTO~Z`, 2026-09-24 ~22:4xZ

**Arming record:** `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`.
**state: ARMED.** Covers ticks 71-73; last log tick 70 @`de0b3144f2` (~21:2xZ), so this lands on the
one-hour floor. ASCII detector run in its own call before each commit.

## The block in one line

**Both owed CTO never-widen halves are SIGNED, so no AMGT act is blocked on this seat** -- and two of this
seat's own cards turned out to be mis-measured: one RETRACTED outright, one RE-SHAPED to name a movable
Andrew had already offered to move.

## Acts, with hashes

| act | hash |
|---|---|
| BOTH CTO never-widen halves SIGNED (re-mint + FWD-12 derive) | `35e4cb93ef` |
| `org/XXX.md` double-stop card RETRACTED | `054bad6cc7` |
| ruling to `2.0.0_SA_COO~Y`: the HARVST publisher card re-shaped | msg 22:42:30Z |
| release to `2.0.0_SA_COO~X`: msg 25790's ONE ASK answered | msg 22:27:46Z |

## THE TWO HALVES -- what each signature actually decided

**RE-MINT: signed on the shape, not on the reproduction.** I re-derived the issuer's preflight at HEAD on a
clean identity tree and it reproduced the COO half EXACTLY (`UNRESOLVED 4 -> 0`, folder-form coverage 41 of
41, VERDICT PASS). **That is weak evidence and the signature does not rest on it.** `Z-S25` recorded why: the
old synthetic-request preflight reproduced `UNRESOLVED 0` exactly *while being wrong about these same four
folders*. **Re-deriving an instrument confirms only that the instrument agrees with itself.** What earns the
citation is that the instrument CHANGED in the two ways `Z-S25` named -- it now models the request-side skip
through the producer's own `_find_existing` and censuses the folder form through `crosswalk.harvester_key`,
the ingest's own function, on committed bytes. What it still cannot do is RUN the ingest, so
`resolved_folders 94` is a PREDICTION and the re-ingest is the only thing that settles it. The act carries no
delete in any branch, the bucket is versioned, and the round-2 anchor is outside the write set.

**FWD-12 DERIVE: signed with the delete branch NARROWED.** The COO half disclosed, correctly, that for the 58
keys going absent-to-present "the only rollback is an S3 delete, which needs Andrew's confirmation". True as
written and WIDER than the act requires. `s3_put_if_absent` never overwrites and all four readers take the
NEWEST object, so **a WRONG VALUE on the 58 is corrected exactly as on the 31 -- a newer stamp, no delete, no
Andrew.** The only state a newer stamp cannot reach is one where the correct condition is ABSENT: a key that
should serve no block at all, or a block served under the wrong security's key. Signing it unnarrowed would
have handed a future reader a delete-gated rollback on 58 keys when the real exposure is a narrow, nameable
set.

**Vendor authority bound to the CONTRACT, not to a citation about it.** A grep for `C-SA-VENDOR-WORD` in the
CORPUS PRD read **0**, and I refused to call that an absence -- it is the exact inference that produced my
wrong R-21 hold. It was a WRONG-OBJECT read: the contract lives in `AMGT_RESAPP_PRD.md:1425-1440`, lifting SA
BY NAME for exactly two paths, one of them the `SA_FALLBACK` cells of `C-MODEL-FORECASTS`, terms cleared at
v0.13. **The lift reaches a CORPUS act because it names a PATH, not a project:** `C-MODEL-FORECASTS` is
written about this very producer and its sibling cites `model_block_pull.py:101` by path -- the module the act
runs. I also checked which way the bounded citations cut: the "3 or fewer tickers, runs 1" lines in the RESAPP
proof-of-spec files are a **pre-v0.12 EXPLORATION cell's criteria**, superseded by a lift scoped by path with
NO count ceiling, so 89 securities is inside it. Named explicitly because the next reader who greps the id
hits those bounded lines first, as I did.

## THE PRECONDITION I REFUSED TO CERTIFY -- a log that reads as a clean finish

The re-mint waits on the production sequence ending. I did not certify that it had. Measured 22:20:54Z:
`mtime 21:48:07Z` (33 min stale), **`bytes 65536` EXACTLY**, final line truncated mid-word
(`names 0 rebuilt 0 ex`). A 64KiB-exact size with a half-written last line is a **BUFFER BOUNDARY, not a
completion marker**, and a `tail` of it reads as an orderly finish -- equally consistent with a run still
buffering and one that died mid-step. A PID census does not rescue it: 35 live `python` processes, none at the
17:28 ET launch, no command lines. The runner reads the sequence's own terminal line or its final artifact and
states which. Free finding from that log: `folders_read 94 = resolved 73 + unresolved 21` -- `Z-S24` standing
on the served plane, and the exact before-figure the re-mint moves.

## TWO OF MY OWN CARDS WERE MIS-MEASURED

**1. `org/XXX.md` double-stop -- RETRACTED @`054bad6cc7`.** Local is **byte-identical to origin/CLOUD**
(`git diff --stat` empty), clean in the worktree, and carries exactly ONE stop heading (`:9`) with ONE
directive. The cited `:86-87` holds sections A.2 and A.3. **I asked Andrew to unlock a LAW FILE -- the most
expensive act the card could request -- to repair an artifact of a working-tree state since reverted, on a
citation pointing at unrelated lines.** Against DO NOT MANUFACTURE FRICTION, this card was friction I
generated. Keepable: **a defect claim about a SHARED file is measured on the SHARED plane** -- one
`git diff --stat origin/<branch> -- <path>` retires the class -- and **a line-number citation is verified by
PRINTING THE BYTES AT THE CITED LINE**, which CLAUDE.md already requires for quotations.

**2. The HARVST publisher card -- RE-SHAPED, and it had a movable in it.** I had been carrying "ft and
barrons, whose refusals authorization cannot reach". `AMGT_HARVST/project.json`'s blocking field
(COO~Y's re-measure ~20:3xZ, 2,086 chars) says **FOUR** publishers hold zero `listing_hit` rows -- barrons,
bbg, ft, sa; only wsj has any -- and `Z-S14` separates the KINDS. **bbg is the ONE MOVABLE of the three**, and
what makes it movable is Andrew's own sentence: *"If there is an issue with getting BBG access let me know and
we can troubleshoot that."* **That is an OFFER, not a grant, and nobody has taken it up.** A verification
challenge is exactly what a person clears and no seat can -- the same shape as the portal sign-in he cleared at
20:25:29Z. ft (403) and barrons (post-auth rejection) stay carded; authorization reaches neither. Ruled to
COO~Y at 22:42:30Z; round 6 stays PARTIAL-shaped per msg 25731.

## THE FWD-12 DERIVE RAN, FAILED, AND ROLLED BACK INSIDE THE PAIR -- the signature earned its keep

`Z-S26` @`c25c5207a8` (COO~X's incident, its own act). **The pull passed SECURITY KEYS
(`ADBE_US_Equity`) where the puller expects BLOOMBERG IDENTIFIERS (`ADBE US Equity`)**, so all 89 raw
responses came back empty and the derive minted empty blocks. The 31 keys that had served real blocks were
rolled back by copy-forward -- **inside the rule my pair specified** -- 31 of 31 in about 7 minutes.

**I verified it on the served reader rather than taking the self-report** (NEVER-trust-a-producer; a
CONFESSION is a claim and carries the same evidence burden). Recount from the before-file's own `per_key`:
`had_block=31 had_none=58 total=89`, matching its `with_block`/`keys` fields. Through
`scoped_amgt.read_model_block`, the consumer's own path: sample of the 31 reads **figures 205 / 203 / 228**;
sample of the 58 reads **figures=0, unresolved=51**. **Report CONFIRMED.**

**Section 3 of my half is what decided this incident, and it decided it correctly.** `figures=0` with 51
unresolved is an HONEST EMPTY BLOCK, not a false figure -- `stage_derive` refused to invent and recorded why,
which is its own rule working. So the remedy is a newer stamp, **not a delete**: had I signed the COO half's
delete-gated wording unnarrowed, 58 keys would have read as needing Andrew's confirmation to fix, and the
live remedy would have looked blocked. The delete branch arrives only if a corrected pull ALSO returns empty
for a key AND that key must return to ABSENT -- named in advance so nobody discovers it mid-incident.

**Ruled 22:50Z, three limbs.** (i) **R-21 COVERS one corrected re-pull**: same vendor, route, scripted
producer, population and mnemonics; the only delta is the identifier format, a defect fix and not a wider
reach. Refusing a standing word for not being phrased per-use is the over-restriction error I made this
morning and did not repeat. (ii) **The signed pair @`2a3319e5ae` COVERS the corrected derive, no new pair** --
its BEFORE-STATE is now false (31 restored, 58 serving empty), and the radius is unchanged or NARROWER,
because for the 58 a corrected derive is now a REPLACE rather than an absent-to-present ADD. Stated
explicitly because a reader comparing the half's before-state to the world would otherwise stall. (iii)
**The verify leg checks CONTENT** (FY rows above 0 per key). `89 of 89 keys landed raw` measured EXISTENCE --
**a failed retrieval returns a VALUE** -- and that missing discriminator, not a reporting lapse, is what let
an all-empty pull read as a success.

## Instrument notes from this block

- **A ROSTER SUMMARY AND ITS LIVENESS STAMP HAVE DIFFERENT VINTAGES, and the row prints only one.** COO~X read
  LIVE 5 s ago beside a summary saying "4 workers building" on round 3 -- whose five orders all read
  `complete` with a single tag each on the shared index. I doubted my own census on the strength of the
  summary; reading the PRIMARY artifact (the status tags) localised the fault to the summary. Two instruments
  disagreeing is symmetric evidence until one of them is the artifact.
- **`git ls-files` with a `**` pathspec returned `TOTAL=0`** for a directory holding 22 orders. A zero from a
  glob is OUT-OF-CORPUS, not absence; the tell was that my own tick-70 log recorded 22.
- **An aged citation is not a wrong one.** I carried `origin/CLOUD 8105cd4f0e` all session; it measures
  `5b3756fa16` now. `8105cd4f0e` (17:16 ET, CTO~O) *was* origin/CLOUD when reported and the integrator pushed
  again at 18:11 ET. Re-measured at send time, as the law requires, rather than corrected as an error.
- The author anchor `--author="<serial> <"` was used with a positive control (1,017 commits all time) before
  any ABSENT verdict about CVO~Z activity.

## Scope state, denominators printed

| project | orders | non-terminal | next |
|---|---|---|---|
| `AMGT_RESAPP` | 221 | 7 | `ro-1` running; `ro-7` (WORLD, half signed `94f72e3cd4`) starts when it lands; `0.7.0_AE_CloudOps~A` reading the order |
| `AMGT_CORPUS` | 22 | **0** | round-3 orders all terminal; the DRAIN acts (re-mint, FWD-12 derive) are what `35e4cb93ef` unblocked |
| `AMGT_HARVST` | 18 | 0 | `ROUND_CLOSE`; round 6 cuttable and PARTIAL-shaped; COO~Y idle |

Inbox 0 at 22:2xZ. Watcher re-armed (`bsa1av90e`) the turn the expiry notice landed -- a lapsed Monitor is a
seat that has stopped being reachable.

## COMPLETION TEST

**NOT DONE -- 0 of 3 projects `status: complete`.** Round 3's drain acts have not run; round 40 has `ro-1`
and `ro-7` live. **No AMGT act is blocked on this seat.**

## Cards at Andrew -- TWO, both re-stated this block

1. **bbg publisher access** -- he offered to troubleshoot it and the offer is untaken. This is the movable
   one, and taking it up is what moves `data_status` off PARTIAL.
2. **ft and barrons** -- a 403 and a post-auth rejection; authorization reaches neither, so `data_status
   COMPLETE` stays a later outcome.

(The `org/XXX.md` card is withdrawn and is no longer one of them.)

## Compiler Tools

`git log -- <file>` as the only commit oracle -- the character-count ASCII detector in its own call --
`git diff --stat origin/<branch>` as the shared-plane control -- `git show <ref>:<path>` with
`MSYS_NO_PATHCONV=1` and a line-count positive control -- last-tag `<status>` parse (flips append) --
`git worktree list --porcelain` + per-tree `ls-tree` for branch-resident state -- `ls-remote` at send time for
push state -- the PRD read at HEAD in place of the citations about it.
