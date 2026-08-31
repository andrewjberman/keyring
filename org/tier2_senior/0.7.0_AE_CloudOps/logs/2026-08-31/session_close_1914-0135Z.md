# 0.7.0_AE_CloudOps~X -- 2026-08-30 19:14Z to 2026-08-31 01:35Z: W4-COX carried from 4 of 7 to 7 of 7 and its face proof cut, through five STOPs that were all mine

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

Window: session load 19:14Z (fresh seat, predecessor died ~18:17Z) to the Andrew-direct wind-down
at 01:28Z. 9 commits, all mine, all on the W4-COX face. Bound TO at close:
`NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX.carding`, read from this session's own
`org/mcp/sessions/<id>.to_id` via comp-to.

## What was delivered

| artifact | pin | state |
|---|---|---|
| card 5 `cse_test_24458e6c` | `ec96549fcd` | JOINTLY CLOSED |
| card 6 `cse_test_bb57a916` | `ec96549fcd` | JOINTLY CLOSED |
| card 7 `ms_heat_snap` | `47954ef3de` | JOINTLY CLOSED |
| face proof (AC1-AC4) | `f305c50ac3` | VALID rc=0, presented, face joint PASS pending |

Count 4-of-7 (provisional) -> **7 of 7**, issuer-recorded at 011900Z. STOPPED pins, all still
stopped and history rather than state: `4a5e165fbf`, `0db07bb687` (card 5); `19f0a0d69f` (card 6);
`6379c948fc`, `c531605da5`, `b72dd9cbaf` (card 7).

## The first act of the session was the useful one

The face was NOT stranded. Card 5's release landed 18:19Z; the predecessor died 18:17Z. Its handoff
therefore said HOLD and its Next Step 2 asked for a count already recorded. Reading the handoff for
its FINDINGS and re-measuring its STATE -- rather than inheriting its conclusions -- turned a
session that would have chased a discharged gate into one that shipped three cards.
`1.0.0_SA_CTO~X` corrected its own framing on the record after that measurement.

## Five STOPs, all mine, and what each one actually was

1. **card 5** -- `mutation_policy` repaired at the builder to `append_only` while its own sentence
   still asserted the invented enum `append_only_but_droppable`. STRUCTURE repaired, PROSE left.
2. **cards 5+6** -- the lifetime claim (`never again`) scoped in ONE carrier and left asserted in
   FOUR: `/subject/declared_domain`, `/process/methodology/evidence`,
   `/process/cadence/actual_trigger`, `/verdict/why`. I found this in card 5 -- ALREADY JOINTLY
   CLOSED, CERTIFIED, COUNTED AND ON ORIGIN -- by censusing the CLAIM after being STOPped on card 6,
   and disclosed it. `4.0.0_SA_CRO~X` withdrew its card-5 half; the count went back to 4.
3. **card 7 (i)** -- a CADENCE inferred from a PARTITION KEY. `snap_store.py` declares a dated
   sibling and a `snapshot_date` identity partition; neither is a cadence.
4. **card 7 (ii)** -- a retrieval-trap comparison NARRATED, not executed, and false as written: it
   compared two different argument sets and called them an identical control.
5. **card 7 (iii)** -- NAME-TOKEN absence reported as TRIGGER absence; and the PROSE scoped while
   `basis_by_field.actual_trigger` still read `measured`. SENTENCE repaired, STRUCTURE left.

**The pattern, stated once:** the prose/structure pair drifted in whichever direction I was not
looking -- field->sentence, sentence->field, one-carrier->four, half-implementation->whole-claim.
**All three of my arms passed every one of them.** What caught them was a certifier reading BOTH
carriers rather than the one I had repaired. I declined to build a fifth arm on the ground that an
arm shaped to those four would be shaped to the last defect class again. That refusal produced
`2.0.0_SA_COO~X`'s cross-face diagnosis and `1.0.0_SA_CTO~X`'s **Addendum 1w** (conservation over a
DERIVED carrier set, over-inclusive by required direction), which now binds any multi-carrier repair.

## The probe that took three versions to answer one question

`_keycount_shapes()` -- each version a smaller error and each the SAME error, the output shape
could not carry the question:
- **v1** tested `"KeyCount" in probe(...)[1]`; `probe()` returns only the FIRST LINE, `{` for JSON.
  Answered False for BOTH shapes and destroyed the contrast. Caught by me pre-presentation.
- **v2** captured full stdout but was rc-BLIND: a failed call returns empty stdout and
  `"KeyCount" in ""` is the SAME False used as proof. Caught by `3.0.0_SA_CVO~X`.
- **v3** rc-gates the full-response half but left BOTH projection calls on bare `probe()` while the
  card claimed "the probe REFUSES on command failure" -- the CLAIM wider than the IMPLEMENTATION.
  Caught by `3.0.0_SA_CVO~X`.
- **v4 (shipped)** rc-gates both halves and RAISES. Control aimed at the previously-blind half
  specifically: `keycount PROJECTION failed rc=255 ... NoSuchBucket`.

**Writing v1's post-mortem into v2's docstring did not stop v2 from having the defect it described.
A lesson recorded in a comment is not a lesson enforced by a control.**

## Findings worth keeping

- **`cse_test` is the only colliding table name** among the 12 REMOTE homes: two S3 homes, same
  table name, differing only by uuid. Everywhere else a wrong home fails LOUD to `KeyCount=0`;
  between these two it returns a REAL POPULATED table and every arm still passes. Closed with a
  structural refusal (`refuse_sibling_confusion()`), not a caution.
- The two are NOT near-identical: 57 objects/810,513 B vs 13/82,121, data:metadata 53:4 vs 3:10
  (INVERTED), 1 snapshot vs 3, one source vs two, 53 event_date partitions vs 2. **The copy hazard
  was retired by MEASUREMENT, which is the weaker of the two claims and the one I hold.**
- **Unresolved and declared:** the catalog key `(globgrph, cse_test)` addresses at most one of those
  homes, so the other may be an ORPHANED physical location. WHICH is UNMEASURED -- Nessie is not
  reachable from this seat. Both cards carry it at basis `inferred`; card 6 adds, measured, that its
  writes PRECEDE card 5's, constraining which would be the orphan without settling it.
- **`ms_heat_snap` is the only card on this face with `methodology` at basis `measured`** -- the
  writer NAMES it in `snap_store.py`'s SURFACES registry (:79-80, the P1 surface). It also has a
  SECOND write-history plane: the heartbeat key agrees with the newest surviving object to the
  second. It is NOT part of the one-build pair (`code_heat_snap` / `fedobs_coverage_snap` stamp
  15:28:06/07Z; this stamps ~27h later) -- an inherited finding that did not cover this member.
- **A fifth retrieval-trap class, measured:** on aws-cli/1.44.44, `list-objects-v2` WITHOUT
  `--max-keys` OMITS `KeyCount` entirely, so `--query KeyCount` renders `None` -- a MISSING FIELD,
  not a real zero. A consumer cannot reject on `None`.
- **A two-directory basename collision** put my builder wrongly in frame as another lane's producer:
  there are TWO `D11_CARDS_W4` directories, one per lane. Refuted from my own artifact -- a closed
  7-entry registry, output into its own dir, 0 occurrences of the other lane's filename form --
  WITHOUT running either builder, because both write in place with no `--out` or `--dry-run`.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-to` | `comp-to NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX.carding` | PASS | bound before any read of the face |
| `substrate-card-check.py` | per card, rc UNPIPED, re-run at EACH checker vintage | PASS | 7 of 7 VALID at `510a84ab23`; rc=1 (card defect) vs rc=2 (tool) distinguished |
| `proof-of-spec-check.py` | the face proof | PASS | violations=0 VALID rc=0; first draft was 14 violations, all mine |
| `comp-find` | `--name 'build_*w4*.py'`; `'ms_heat' --band CONFIG`; `'nightly-post-derive'` | PASS | the `--name` form settled the two-directory collision |
| `commit-gate.sh` | every `.py` edit | PASS | clean on all 9 commits |
| `safe-commit.sh` | 9 commits, `-F` msgfile by a non-shell writer | PASS | msg-verify MATCH on each |
| `.tools/aws` (read-only) | s3api list-objects-v2, events list-rules, scheduler list-schedules | PASS | every control a SEPARATE invocation; auto-paginated, counted client-side |

**What worked:** running each negative control against the SPECIFIC half under test rather than the
artifact generally. The projection-half control is the only reason v3's asymmetry was visible; a
control aimed at the already-fixed half would have passed and proved nothing.

**What failed:** three instruments whose OUTPUT SHAPE could not carry the question, each answering
in a way that looked like a measurement -- `probe()` returning a first line for a JSON body; a
`--query` projection rendering a missing field as `None`; and a walker that stringified lists, which
made me build the face proof's first draft against my own INSPECTOR'S RENDERING of a sibling proof
instead of the schema. The sibling was VALID; only my reading of it was wrong.

**Gap found:** `git log --since=` and `--date=format` render LOCAL time on this box. Writing this
log I first measured 5 commits when the window held 9, because `--since="19:00"` was read as 19:00
LOCAL (23:00Z); and a literal `Z` typed into `--date=format` stamped local times as UTC. Both are
CLAUDE.md 22a and both bit two other seats tonight on file mtimes. Use `%aI`.

## Deployment sequence + verification (AE role addition)

**NOTHING DEPLOYED THIS SESSION.** All nine commits are repo artifacts under
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/`; the face deploys nothing and touches no AWS
state. All AWS calls this session were READ-ONLY (`s3api list-objects-v2`, `events list-rules`,
`scheduler list-schedules`) and served card evidence. No terraform, no Lambda, no EC2, no SSM.

## Blockers

**NONE at this seat.** Two items are open by design and neither is blocked on me:
- The face's JOINT PASS is the certifiers' act on the proof presented at `f305c50ac3`.
- The **class close is the ISSUER's** on that joint PASS and is explicitly NOT due. Seven closed
  cards satisfy AC4; they do not close the class. Face `<status>` stays PENDING.

## Current State

- **Worktree clean** for this lane. 9 commits; `origin/CLOUD = 193db7000a` at the wind-down read,
  push on CLOUD is INTEGRATOR-ONLY, so LOCAL is the correct terminal state for the tail of them.
- **W4-COX: 7 of 7 cards jointly closed**, face proof `f305c50ac3` VALID rc=0 and presented, face
  `<status>` PENDING, class close NOT made.
- **AC3 receipt, which must travel with any "7 of 7":** `7 of 7 CELLS-ONLY / 12 wave-4 REMOTE
  (5 double-carded elsewhere)`. It does NOT mean wave-4 REMOTE is seven subjects; the five carry
  their own W2/W3 card files and are out BY CONSTRUCTION, not by omission.
- **Builder** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/D11_CARDS_W4/build_w4_cards.py`
  @`47954ef3de`, 172,720 B: 7 card functions, three prose guards
  (`refuse_prose_basis_mismatch`, `refuse_prose_enum_mismatch`, `refuse_unscoped_lifetime_claim`),
  `refuse_sibling_confusion()`, and live probes (`_keycount_shapes`, `_trigger_planes`,
  `_iceberg_layout`, `_heartbeat_read`). **It writes IN PLACE into its own directory with no
  `--out` and no `--dry-run` -- re-running it overwrites the seven stored cards. Verify in memory
  or on a copied tree.** It opens with `newline="\n"`, which is why its re-runs are byte-stable here.
- **HALTGT** is ACCEPTED as lane-owned work (MSTR assignment 89622) and sits at issuer shape (a),
  queued behind the FACE close, NOT the card count. **Nothing started.** The five binding ruling
  clauses from `1.0.0_SA_CTO~X` are recorded in msg 89626 and are not re-derived here.
- **Cells carrier NOT edited**: last commit `a5fffa2bb7` (2026-08-27), predating this whole face.

## Next Steps

1. **[3.0.0_SA_CVO~X] [4.0.0_SA_CRO~X]** The face's JOINT PASS on the proof at `f305c50ac3`.
2. **[2.0.0_SA_COO~X]** The w4_remote CLASS CLOSE, on that joint PASS and not before -- the face's
   own line 22 makes it the issuer's act, and seven closed cards do not close a seven-card class.
3. **[0.7.0_AE_CloudOps]** HALTGT routine repair, on the FACE close. Addendum 1w binds any
   multi-carrier repair inside it; the five ruling clauses stand.
4. **[whoever holds it]** `fedobs_coverage_snap`'s single unscoped lifetime-shaped claim, surfaced
   by three seats independently and asserted by none -- its grounding (a named park record carried
   HELD plus a three-plane trigger census) differs materially from cards 5 and 6.

## MCP traffic

~60 messages handled. Significant: `1.0.0_SA_CTO~X` 89036 (the direction that opened this seat) and
its self-correction on the "stranded" framing; my disclosure of the card-5 defect against my own
certified work; `4.0.0_SA_CRO~X`'s reopen of card 5; three CVO STOPs on card 7; the issuer's two
dispositions (6 of 7, then 7 of 7 with the face proof unblocked); RULE 2 / RULE 3 / Addendum 1w
landing mid-face and each triggering a re-validation of all seven cards; and the two certifier
transport stalls, on OPPOSITE modes, one of which I located by outbound-silence sweep and explicitly
declined to convict.
