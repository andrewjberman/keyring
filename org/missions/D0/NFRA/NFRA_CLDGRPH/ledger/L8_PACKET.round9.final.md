# NFRA_CLDGRPH -- L8 PACKET, ROUND 9, **FINAL** (5 of 5 orders drained) -- compiled by `2.0.0_SA_COO~A` 2026-09-10 ~20:0xZ, for `3.0.0_SA_CVO` at L9

**SUPPLEMENTS `L8_PACKET.round9.partial.md` @`d1f3fc09d7` (12,968 bytes, sha256 prefix `551035e5026092ca`),
which stands unamended.** That packet carries `TO-CG-I-1/-2/-4/-5`; this one adds `TO-CG-I-3` and the
round's totals. **Grade against PRD v0.14.**

**THE ROUND IS COMPLETE AT L7: 5 of 5 orders terminal and drained, 49 of 49 PROJECT-WIDE, zero worktrees
left.** Both denominators are printed on purpose -- see s.4.

## 1. The fifth order

| order | cell | merged | mechanical | judgment for L9 |
|---|---|---|---|---|
| TO-CG-I-3 | CG-s-42 the fold's LICENCE moved, or the remedy re-cut | @`e2bc841263` (acts `4846d3a734`, harness fixes `d68175f26f`, instance+flip `72e68ae40b`) | **4 of 4 PASS** | **I3-AC5** |

Instance re-validated at this seat IN TREE against the COMMITTED blob: `VALID (rc=0)`, 0 violations,
8 artifacts resolved at pin. Worktree and branch removed.

## 2. `OWNED_BY`'S OTHER WRITER HAS A NAME, AND THE WAY IT HID IS THE FINDING

**`graphuni-storage`.** `org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1-A.storage_producer.json` (169 edges)
plus `...storage_producer_phaseB.json` (63) = **232** -- **the exact integer round 8 measured on the served
plane**, arrived at from the repository side by a different instrument. Served from
`s3://opal-313476888478-globgrph/producers/graphuni/` and re-read on EVERY derive by
`derive_runner.ingest_graphuni_producers`.

⛔ **AND IT WAS NEVER HIDDEN -- IT WAS RECORDED IN A FORM NO CENSUS COULD SEE.** The string
`"Producer=graphuni-storage (~A)"` sits at `.tools/tool_index.py:4378-4381`, in the repository, the whole
time. **An emission-shaped census looks for code that WRITES an edge; this writer declares its edges as
DATA in a JSON payload and is named in PROSE.** Round 8 established by subtraction that the writer existed;
naming it took an instrument that reads what a producer DECLARES, not only what code EMITS.

⚠ **TWO THINGS ABOUT IT THAT BELONG IN THE NEXT READING, neither of which this cell was cut to fix:** its
materializer `org/projects/NFRA_GRAPHUNI/storage_producer.py` is **UNTRACKED**, and the payloads have not
been regenerated since **2026-07-01**. A live production input whose generator is not in the repository is
its own question, and it is not this round's.

## 3. THE BRANCH TAKEN, AND WHAT IT REFUSES BY CONSTRUCTION

**`BRANCH=LICENCE_MOVED`.** The drop's licence was a COMMENT asserting *"STORED_IN is this producer's OWN
edge type"*; it is now `SOLE_WRITTEN_EDGE_TYPES` plus a `SOLE_WRITERSHIP_EVIDENCE` table carrying each
member's claim kind, instrument and vintage, and a function that **REFUSES an unlicensed type** and drops
only the INTERSECTION of what the caller requests and what the licence permits. Proven on a 5-edge fixture,
`FIXTURE_ARMS=6 of 6`: a multi-writer term SURVIVES the fold, a sole-written term is still DROPPED,
negative control fired. The `OWNED_BY` fixture edges are copied VERBATIM from `graphuni-storage`'s payload.

⭐ **THE COMMENT ABOVE THE TABLE STATES ITS OWN EXPIRY, WHICH IS THE PART WORTH KEEPING:** *sole-writership
is a fact about today, not a property of the type* -- a new producer can falsify a member without touching
that file, so the census is a re-runnable falsifier rather than a one-time sign-off. **The CTO's withdrawn
remedy is now refused BY CONSTRUCTION rather than by memory:** adding `OWNED_BY` to that table is the act
the withdrawal refused, and the table makes the assertion explicit and testable instead of implicit.

## 4. ⛔ THE RETIREMENT AS RULED IS A TWO-EDIT ACT AND ONLY ONE EDIT HAS EVER BEEN SCORED

**Row `W2-S80`.** `derive_runner.py:2276` carries `STITCH_EDGE_TYPES = frozenset({"ROUTES_TO", "WRITES",
"READS", "DERIVES_FROM", "STORED_IN"})` -- an ALLOW-LIST that does not contain `OWNED_BY`. So the 94872
remedy, had it survived, needed a second edit in a second file that no cell in any round has named. **Every
round since has scored the producer's side and none has scored the consumer's allow-list.** `derive_runner.py`
was not in that order's `<paths>`, so it is a ROW and not an act -- which is the grant rule working exactly
as written.

## 5. Round 9 in totals

| measure | value |
|---|---|
| orders issued / terminal / drained | 5 / 5 / 5 |
| criteria graded mechanically | **20 of 20 PASS** |
| judgment criteria for `3.0.0_SA_CVO` at L9 | **5** -- `I1-AC5`, `I2-AC5`, `I3-AC5`, `I4-AC5`, `I5-AC5` |
| instances re-validated at this seat, in tree, against the committed blob | **5 of 5 VALID (rc=0)** |
| worktrees and branches left | **0** |
| rows minted by workers | 7 (`W1-S49/S50/S51`, `W2-S79/S80`, `W3-S20`, `W4-S10`) |
| rows minted by the issuer | 2 (`S118` cross-round blindness, `S119` the dark READ clock) |
| task orders open PROJECT-WIDE at close | **0 of 49** |

⭐ **THE LAST ROW IS `S118`'S REMEDY, LANDED.** Rounds 7 and 8 both reported `task_orders_drained_open: 0`,
both TRUE and both scoped to their own round's order set, while a round-6 order sat open through both.
**This packet and this round's completion report print the PROJECT-WIDE denominator beside the round one**,
so a gap between them is visible instead of invisible. It needed no code and no gate.

## 6. WHAT THIS ROUND DID NOT DO, stated so no reader infers otherwise

- **NOTHING WAS DEPLOYED.** Five of five orders proved a zero-count egress arm with a firing probe control:
  no `ecs run-task`, no CodeBuild start, no image push, no `terraform apply`, no S3 write.
- **THE RETIREMENT WAS NOT PERFORMED.** `RETIREMENT_PERFORMED=false`, and `CG-s-42` makes it AVAILABLE
  rather than taken -- performing it is an act on a decision nobody has made, and s.4 now shows it was
  always a two-file act.
- **`FWD-7`'s PERSON half is untouched.** Andrew ALLOCATED the site-Z seat; an allocation is not a session.
- ⚠ **`W1-S51` REMAINS ARMED AND IS THE ISSUER'S.** The corrected source sits beside a TRACKED deploy
  artifact carrying its own stale copy of the pre-fix code. No cell in this round covers rebuilding a
  deployment artifact, and inventing one mid-round is the spec-freeze violation the channel exists to
  prevent. **It is the first named item for the round-10 cut, or for the CTO's analysis to place.**

## 7. Three self-caught instrument defects, all from the seats being graded

1. **A harness that was re-runnable only BEFORE its own evidence was committed** -- a name-list
   classification broke once its files became tracked. Caught by running each criterion TWICE at HEAD
   instead of trusting pre-commit captures.
2. ⛔ **A diff-against-the-index that reads 0 bytes once the acts land, silently shrinking the scanned
   surface while still printing five clean zeros** -- an egress arm that would have passed by measuring
   nothing. Both fixed in `d68175f26f` and recorded rather than quietly repaired.
3. **A repo root resolved by counting `..` landed on a directory that STILL EXISTED**, so a status read on
   an absent path returned empty and printed CLEAN on a file that was not there (`TO-CG-I-5`).

**Push state, measured at compile rather than carried:** every hash named here is LOCAL. Andrew holds the
push and this line ages the moment an integrator runs.
