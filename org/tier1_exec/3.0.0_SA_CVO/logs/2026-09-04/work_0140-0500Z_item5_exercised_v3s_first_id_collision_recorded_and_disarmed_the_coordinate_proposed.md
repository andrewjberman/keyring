# 3.0.0_SA_CVO -- 2026-09-04 01:40Z to 05:00Z -- item 5 exercised (the adjudication document's first row); v3's first id collision found, recorded, surfaced and disarmed on the owner's limb; the allocator coordinate proposed with its Rule 24 record

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

Seat: 3.0.0_SA_CVO base, MAIN fabric, laptop, CLOUD, PID 24480. Continues `work_2117-0140Z_...md` @180b34e344.

## Summary

1. **Item 5 exercised @b50a124783** (CTO 93996 named the contract + gate halves @b4299fa5aa; MSTR's lane half
   @7668568ed6): `surprise-channel/adjudications/ADJUDICATION_v1.md` under NFRA_COMPEFFICACY, one row S34 adjudicating S29
   (DISMISSED_WITH_REASON on this seat's exercises at both grains), committed through the row gate (1 new row admitted
   under adjudications/), the tree check (0 violations) and lane TREE_CVO. The gate's census read S29 dispositioned from
   that document alone (34 items / 3 files / undispositioned 0); the rollup lagged (33 / open 1) until the CTO widened
   its glob @747da480bc, validated on this seat's own run (34 / 26 files / 1 adjudication row / open 0). Item 5 closed
   on both instruments (93998/93999, 94029 earlier close on the rollup).
2. **v3's first id collision.** The first spine-v3 worker `0.9.0_WK_NFRA_COMPEFFICACY~2` (TO-CE-G-2) appended S34, S35,
   S36 to the investigation document in worktree wk-CE-2 (commits e7dda3d93c, a4a517214e), merged by the COO's drain
   @46ff7f8c8a -- a plain git merge, no gate on the union -- so `NFRA_COMPEFFICACY-S34` named two rows. Measured: the
   gate had no cross-document uniqueness limb (comp-read: 1 COMMENT hit, no code, over 1,026 lines); the gate's census
   kept the worker's S34 open while the rollup resolved the id to this seat's adjudication and reported the worker's
   observation as DISMISSED, which nobody decided; the worker's two GIT_COMMIT_AUTHOR_OVERRIDE audit lines lived only in
   the worktree's gitignored copy of the log (.gitignore:68 `*.log`). Surfaced 94007-94009 within the hour; recorded as
   S37 @f357b84197 (ARMED, disarm owner 1.0.0_SA_CTO; DISMISSED_WITH_REASON as an outside-chain record); one addition
   94010-94012 (the census counted the CVO's rows as items). The CRO's own check-out (94015) corroborated every fact,
   ruled item 3 NOT PASSED on the lane limb, and tabled five new gaps for Andrew's scope call.
3. **The owners moved the same hour.** The COO accepted the verdict, preserved the worker's six audit lines before the
   teardown, and fixed its two drain-side steps @e6351512fe (the pre-spawn `<paths>` lane census; the pre-merge row-gate
   run on the merged index) -- validated here on the diff, procedure text binding by reading, the mechanical refuser still
   a build act (94019-94022). The CTO landed the uniqueness limb and the census fix @72d05b2642 (adjudication rows no
   longer items; a collided id resolves toward OPEN; an ambiguous adjudication refused). **Exercised at this seat on
   real bytes in an isolated scratch worktree:** a planted duplicate (S35) REFUSED rc 1 with the gate naming the sibling
   document and the plane; a planted fresh id (S99) ADMITTED rc 0; both censuses agree (36 items / open 3 / duplicate
   ids 1 / 2 CVO rows beside). **S37 DISARMED by S38 @3aa32a699e**, the citing successor annex section 6 names, which
   itself committed through the gate carrying the limb (94029/94030). The CRO checked out gaps 2 and 5 PASS (94027).
4. **The third remedy on the record @ddbbf3ce46:** `PROPOSAL_CHANNEL_ID_ALLOCATOR_COORDINATE_20260904.md` -- the grammar
   `<CODE>-(Z-)?(W<n>-)?S<k>`, an allocator coordinate that removes the race rather than detecting it; Rule 24's four
   postulates; the consumer census over 148,424 files (two schema patterns, this seat's; three regexes --
   surprise-row-gate.py:78, proof-of-spec-check.py:946, surprise-watch.sh:80 -- the CTO's and the intake's; the rollup
   resolves by string). PROPOSAL only; the CTO reports its regex half ready on Andrew's word via the CRO.
5. **L9 prepared for round 6c** (the G-2 instance re-run VALID at this seat, five commits authored under the worker
   serial): G2-AC1 is the first `judgment="true"` criterion seen, recorded UNVERIFIABLE-BY-INSTRUMENT with no verdict --
   graded PASS in the stamp notes (2 of 2 tools measured pre-fix, carriers at file:line); G2-AC3 PASS on its expect with
   S35 carrying the inert `--budget` flag; the worker's S34/S35/S36 dispositioned at L9 with the packet, S34 by id landing
   on the worker's item under the census fix.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `python .tools/surprise-row-gate.py --self-test` x4 | the live census across the window | 32 -> 42 arms, 0 failed; the live line quoted at each step | the L10 refuser's own read |
| `comp-surprise --project` / `--json` x5 | NFRA_COMPEFFICACY | 33/open 1 -> 34/open 0 -> 36/open 2 (false dismissal) -> 36/open 3 + duplicate_ids 1 | the rollup, before and after two fixes |
| `git log --merges`, `git worktree list`, `git log --format=%an` | the drain and the worker | 46ff7f8c8a plain merge; wk-CE-2; five commits authored 0.9.0_WK_NFRA_COMPEFFICACY~2 | how the collision reached CLOUD |
| python parse of both channel files | S34 x2 at HEAD | both present; id order and row counts | the collision measured, not inferred |
| scratch worktree + staged plant + the gate CLI | 72d05b2642's uniqueness limb | duplicate REFUSED rc 1 / fresh ADMITTED rc 0 | the disarm's evidence, a different instrument from the builder's harness |
| `.tools/proof-of-spec-check.py` | the G-2 instance | VALID rc 0; 7 rows; 3 surprises resolving | L9 prep |
| `comp-read --enumerate` | the gate (uniqueness), comp-heat, comp_similar.py, the G-2 face, the id-pattern consumers | the lines cited above and in the proposal | |
| `comp-find` (corpus=all) | the id-pattern consumers | 26 hits / 148,424 files; 3 DEF, 2 CONFIG | the proposal's census |

**What worked:** measuring both S34s and both instruments before saying "collision"; exercising the owner's limb on
planted bytes in an isolated worktree rather than accepting the 42-arm self-test; writing the proposal with its census
so it is a proposal. **What failed:** an early `tail` clipped the gate's refusal sentence (re-run to capture it); a
heartbeat re-surfaced already-acked queued copies four times (cosmetic). **Gaps found:** the gate had no uniqueness
limb and the drain ran no gate (both fixed); the override audit log is per-checkout and gitignored (gap 4, no owner
yet); no lane admits a worker serial (gap 1, the grantor's); the census had counted the CVO's rows as items (fixed).

## MCP traffic

Inbound 7, all READ-acked by id: 93996, 94000, 94015, 94018, 94023, 94027 (+ queued re-surfacings of already-acked
rows). Outbound 8 acts: 93998/93999 (item 5 exercised), 02:01Z (rollup close), 94007-94009 (the collision), 94010-94012
(S37 hash + the census addition), 94019-94022 (close on the COO's fixes + the proposal), 94029/94030 (close on the
limb + S38). Nothing to any Tier-2 seat or worker (a worker cannot be messaged).

## Surprise channel

Rows this window, all in adjudications/ADJUDICATION_v1.md: S34 @b50a124783 (adjudicates S29), S37 @f357b84197 (the
collision, ARMED -> disarmed), S38 @3aa32a699e (the disarm). Watermark at 05:00Z: COMPEFFICACY 36 worker rows / open 3
(the worker's S34, S35, S36 -- at L9 with the packet) / duplicate ids 1; CLDGRPH 29 / 5 (held on Andrew's word).

## Files Modified

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/adjudications/ADJUDICATION_v1.md` @b50a124783, @f357b84197,
@3aa32a699e · `org/tier1_exec/3.0.0_SA_CVO/deliverables/PROPOSAL_CHANNEL_ID_ALLOCATOR_COORDINATE_20260904.md` @ddbbf3ce46 ·
this log.

## Blockers

None BLOCKED. Everything below is EVENT-GATED.

## Current State

- origin/CLOUD @351f309e0a (the CTO's ls-remote 01:4xZ); this device far ahead; pushes on Andrew's word.
- Monitors: inbox bq0382tky; surprise intake b8kw389m0. Zero crons.
- NFRA_COMPEFFICACY: round 6 -- tranche 1 at L9 (S33), G-2 complete (round 6c), the packet awaited from 2.0.0_SA_COO;
  the stamp in v2.3 form in the turn that reads it (the grades and the worker rows prepared); the remediation schema's
  route fields retire in the commit after it.
- The eight carriers: this seat's done and checked out; item 3 NOT PASSED on the lane limb (MSTR's grant, on the word);
  the coordinate proposal at Andrew's scope call.
- NFRA_CLDGRPH: round 3 terminal at L7, L8-L10 unowned on his word.

## Next Steps

- [2.0.0_SA_COO] the round-6 packet (tranche 2 + G-2).
- [3.0.0_SA_CVO] on the packet: proof instances + AUTHOR, S31, T20-AC4 FAIL, G2-AC1 PASS, the worker's S34/S35/S36, the
  slug; then the route fields retire from the remediation schema; annex v3.2 with the coordinate if the word comes.
- [Andrew] the scope call on the five gaps and the coordinate; the CLDGRPH ownership word; the 26 estate days.

— 3.0.0_SA_CVO
