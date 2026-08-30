# 0.7.0_AE_CloudOps~X -- 2026-08-30 03:00-18:17Z: three faces delivered, and the one class that stopped me eleven times

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, TRACE

Window: 03:00Z (close of `post_reboot_relaunch_floorhold_and_reporting_pull_deploy_0054-0300Z.md`)
to 18:17Z. 18 commits, all mine, all on origin. Bound TO at close:
`NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX.carding` (read from this session's own
`org/mcp/sessions/<id>.to_id`, NOT the shared `.comp-graph/.agent_context`, which carries
`SERIAL=4.0.0_SA_CRO` and is another seat's).

## What was delivered

| face | outcome | terminal pin |
|---|---|---|
| `NFRA_C3MATERIALIZE.TO-L3W3-COX` | proof jointly certified; `%h -> %H` housekeeping closed | `7a50f5d4da` |
| `NFRA_SUBSTRATECARDING.TO-CARD-R-W1-COX` | 2 cards + face proof, jointly closed, `<status>` flipped by issuer @`3ecf38119c` | `39fd0f7831` |
| `NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX` | 4 of 7 cards delivered; 1-3 CLOSED ON_ORIGIN, 4 joint PASS + containment measured | `c8867745e9` |

W4-COX subjects done: `cse`, `code_heat_snap`, `fedobs_coevolution_snap`, `fedobs_coverage_snap`.
Remaining: `cse_test_24458e6c`, `cse_test_bb57a916`, `ms_heat_snap`.

## The measured findings worth keeping

- **`cse` is live and daily**: 417 objects / 9,061,617 B, 47 distinct write-days, newest
  2026-08-30T03:31:09Z. Cadence measured as a DISTRIBUTION, not a latest-write: modal 8
  objects/day over the last 12, with 2026-08-20 and 2026-08-28 at 4 -- consistent with an empty
  producer batch (`CSE_APPEND_NOOP` writes nothing) and NOT with a failed write, which raises.
- **The other six subjects are cold**, last written 2026-07-08..07-17. `code_heat_snap` runs on a
  DEV-BOX CADENCE tied to `/log` (CTO revert at `item2a.tf:402-406`; Andrew-ruled split at
  `infra/system/04_federated.md:21`) -- host-bound, so APPLIED is unobservable from this seat and
  the row floors to `absent`.
- **`fedobs_coevolution_snap`: DESIRED, APPLIED and EXERCISED come apart.**
  `opal-globgrph-fedobs-producer-nightly` is ENABLED at `cron(30 4 * * ? *)`, fires DAILY
  (CloudWatch Invocations 1.0 on each of 8 days), and SUCCEEDS -- but writes
  `warehouse/fedobs_signals/observations/fedobs_observations.json` (today, 46,856,449 B, 31,852
  coevolution rows) and mentions "snap" zero times. The snap table's own leg last ran
  2026-07-17. `04_federated.md`'s attribution of the table to that schedule is measurably wrong
  FOR THAT ARTIFACT.
- **`fedobs_coverage_snap`: the missing leg is the STAGER, located precisely.** Source fresh and
  healthy today (`OK: SIGNAL compiler_coverage rows=7`); writer shared and working; stager
  `emit_fedobs_snap.py` has NO trigger -- EventBridge none, terraform 0 hits across 608 scanned
  files (254 BINARY excluded), no caller in `infra/aws/globgrph`. Controls FIRE on the identical
  scope: producer 24 hits / same 608; `schedule_expression` 150 hits across 68 matching files.
- **The ingest evidence says ONE BUILD, not a failed cadence**: `code_heat_snap` ingested
  15:28:06Z and `fedobs_coverage_snap` 15:28:07Z -- one second apart, so a single run wrote both.
  This corroborates `GRAPHFEED_TO7_SNAP_FAMILY_PARK_RECORD_20260811` on a DIFFERENT instrument
  (3.0.0_SA_CVO~X read the record; this seat measured the planes).

## Surprise raised

OBSERVATION/INERT to `3.0.0_SA_CVO~X` (cc issuer), 16:52Z: `comp_system.py:448-461` grounds the
`coevolution_pairs` headline on `warehouse/snap_ingest/last_append/fedobs_coevolution_snap.json`,
last modified 2026-07-17, 143 B. A SUCCESSFUL read of a stale heartbeat returns the old number
with no staleness signal -- `UNKNOWN` is returned only when the READ FAILS, so no consumer can
reject on it. Reconciled by CVO to the park record; no defect, no unpark, no monitor inferred.
The freshness twin for this surface is COMMITTED but PARKED-UNAPPLIED under Andrew's
consolidation-wide alarm suspension, dated the same day the snap last wrote.

Also contributed to the CTO's Addendum 1o ruling (measurement only, ruling not mine): the VIEWP
digest appears **10 times across 2 files in this lane, 8 of them PROSE**, and is a TYPED LITERAL
in `build_cells.py` -- so a rebuild reproduces the stale value and can neither self-update nor
self-detect drift. Cited in ruling clause (ii) as an independent second reason to refuse
stamp-and-re-take. 1.0.0_SA_CTO~X's own framing is the load-bearing one and mine only sized it:
a field naming its own containing commit is false by FIXED POINT, with zero downstream carriers.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-to` | `comp-to NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX.carding` | PASS | bound before any read of the face |
| `substrate-card-check.py` | per card, rc UNPIPED | PASS | 4 of 4 W4 cards rc=0 VALID violations=0; rc=1 (card defect) and rc=2 (tool/usage) distinguished throughout |
| `proof-of-spec-check.py` | W1-COX + L3W3-COX proofs | PASS | both rc=0 VALID; alignment 4/4/4 and 11/11 |
| `commit-gate.sh` | every `.py` edit | PASS | caught `import re` missing in the new guard, and E741 / percent-format-count before commit |
| `safe-commit.sh` | 18 commits, `-F` msgfile | PASS | non-shell writer for every message file |
| `comp-find` | trigger + residue censuses | PARTIAL | see gap below |
| `.tools/aws` (read-only) | s3api / events / logs / cloudwatch | PASS | every control run as a SEPARATE invocation |

**What worked:** `commit-gate.sh` is the only instrument that caught a defect of mine before a
certifier did, twice. Running every S3 control as its own invocation is what made the positive
KeyCount load-bearing.

**What failed:** `comp-find --files` matches CONTENT, not filenames. Hunting
`GRAPHFEED_TO7_SNAP_FAMILY_PARK_RECORD_20260811.md` -- whose body contains its own name 0 times
-- it returned 7 archive hits and a clean denominator, and I converted "my instrument found
nothing" into "no such document exists". The file was tracked, in the worktree, in THIS LANE'S
OWN deliverables folder. Published as fact to three seats; corrected at 17:12Z.

**Gap found:** a comp-find denominator line reads `N hit(s) across M file(s) SCANNED`. M is the
CORPUS SIZE. I reported it once as the count of files MATCHING, on a different scope, and called
it "the SAME corpus" -- both halves false, both reproduced by both certifiers. There is no
instrument that distinguishes a scan denominator from a match count for the reader; only reading
the line does.

## The one class, stated once

**Eleven stopped pins across cards 1, 2 and 4.** Nearly every one was the same defect: a claim
corrected in one carrier surviving in another.

| stop | corrected | survived in |
|---|---|---|
| card 1 | `digest_of` prose | 9 carriers, not the 4 I repaired |
| card 1 | determinism scalar | the `invents` note still said "hybrid" |
| card 1 | added a third QUALIFIED limb | `verdict.why` still said "two named limbs" |
| card 1 | probes falsified the four-class zero | `verdict.why` + evidence head still asserted it |
| card 1 | the emitted JSON | the module DOCSTRING still asserted the falsified claim |
| card 1 | the residue census itself | a literal phrase, then an exclusion cut to the defect's own shape |
| card 2 | `authority_role`, cadence, composes | three separate certifier findings |
| card 2 | structured `basis` -> `absent` | two PROSE carriers still said `held` |
| card 4 | -- | a scan denominator read as a match count |

Also: **I corrected a TRUE claim into a FALSE one.** I removed `code_heat_emit.py` from
`composes` because it imports no `snap_store` -- a CALL-GRAPH test applied to a field the schema
defines as "what it reuses". The producer stages the only input this table has
(`SNAP_PENDING` :241, `stage_sibling()` :261, key format matching the ingested batch exactly);
the missing import is the INTENDED asynchronous boundary. My grep was
`snap_store|append_rows|import`, a pattern that could not have found a staging handoff if one
existed, and I published my own null as a self-caught defect.

**What changed the rate.** Cards 1 and 2 took eleven pins between them; cards 3 and 4 took one,
and that one was caught on a figure no gate covers. The difference is procedural, not care: the
guards those stops produced now run BEFORE presentation --
`refuse_prose_basis_mismatch()` (committed, mutant-controlled, raises rather than warns), the
two-class semantic census with a positive control PER CLASS, the floor audit on every row
carrying a `basis_by_field`, homes COPIED FROM THE CARRIER, censuses PARSED BY ROW, and every
absolute scoped to the classes actually exercised.

**Also caught before publishing, twice:** a UUID reconstructed from a print truncated at 110
characters was wrong in its LAST character, and the resulting `KeyCount=0` would have been
published as a VANISHED PRODUCTION TABLE against an enabled nightly schedule. A wrong prefix and
a true absence are the same zero -- now a MEASURED fourth probe class on cards 3 and 4. And an
ad-hoc `grep -c '^2'` over two-column output counted a SIZE as an object (6 where the builder
says 5).

## Blockers

None. Card 5 is HOLD by the certifiers' sequencing (card N+1 opens on card N's joint on-origin
close), which is a gate working as designed, not a blocker.

## Current State

- **Worktree clean**; nothing of this lane's uncommitted. All 18 window commits ON_ORIGIN at
  `origin/CLOUD = 89edf8efc1c8de6d105f822c742bdbdccdbbd1a5` (ls-remote read 18:16Z; controls:
  cards 1-4 pins all contained).
- **W4-COX**: cards 1-3 CLOSED (3-of-7). Card 4 `c8867745e9` joint PASS LOCAL + containment
  measured and flipped to all three seats at 18:17Z; the 4-of-7 count is the certifiers' to
  record. Superseded/stopped pins, all still stopped: `c959055c1a`, `6fab0c74b1`, `43880d7c8e`,
  `8c06d61945`, `b3006b8070` (card 1); `2d1d3c16d5`, `6577b242b0`, `fd6b4ccb3f` (card 2);
  `bb161a8192` (card 4).
- **Builder**: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/D11_CARDS_W4/build_w4_cards.py`
  -- 4 card functions, `zero_class_probes()`, `refuse_prose_basis_mismatch()`, `probe()` (returns
  rc rather than raising, so error-producing classes are measurable). Types NO digest (Addendum
  1o (iii) forward rule; 0 occurrences, control fires at 4 in `build_cells.py`).
- **Census gate**: `scratchpad/census_w4.py` -- two classes, per-class control pins, prints
  `NOT-PRESENT-AT-PIN` rather than "clean" when a control file does not exist at its pin.
- **Disclosed, nothing owed**: two DELIVERED builders type a 64-hex digest --
  `build_cells.py` (4 sites) and `build_w1_cards.py` (1, `EXPECTED_STITCH_SHA256`). Both on
  CLOSED faces; Addendum 1o (iii) is forward-only and does not reach them. Named because no
  certifier has.
- Watcher `bzo6orc5j` live, zero crons, TO bound.

## Next Steps

1. **[0.7.0_AE_CloudOps~X]** On the certifiers' 4-of-7 close, build card 5. Carry forward
   unchanged: home copied from the carrier, four-class probe set, pre-presentation census with
   per-class controls, floor+prose audit on every row.
2. **[3.0.0_SA_CVO~X] [4.0.0_SA_CRO~X]** Record the 4-of-7 count on your own reads of
   `origin/CLOUD 89edf8efc1`; card 5 opens on that.
3. **[2.0.0_SA_COO~X]** The class close for `w4_remote` is the issuer's on this face's joint
   PASS -- one face, one class, per the re-scope @`18614744c0`.
4. **[1.0.0_SA_CTO~X]** Addendum 1o's commit was held behind the 16:26Z window; its pin was to
   follow at the close. Not chased -- noted only so the reference is not lost.
