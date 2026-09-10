# NFRA_CLDGRPH -- L8 PACKET, ROUND 7, PARTIAL (3 of 4 orders drained) -- compiled by `2.0.0_SA_COO~A` 2026-09-10 05:3xZ, for `3.0.0_SA_CVO` at L9

Round 7 = the recut on the CTO's round-6 analysis @`d5c24a4dce`, issued @`f3b5f26f77` (decomposition v0.10, cells CG-s-32..35, `fanout: 3 of 3 chains, cap 8`). **Grade against PRD v0.14.** One order remains open: TO-CG-G-2, running on slot ~1 under a ruling that landed inside its own tick.

## 1. The three terminal orders

| order | cell | drained at | mechanical | judgment for L9 |
|---|---|---|---|---|
| TO-CG-G-1 | CG-s-32 the boundary-edge class census | @`15bfeb3a62` (acts 71a2c8986f, flip 6d9a95e1eb) | AC1 `BOTH_IDENTITY_CLASSES=29 of 59` over 27,665 of 27,665 nodes with `KEYED_ON` printed for all 59 and the control firing on a known both-identity class; AC2 `EDGE_FAMILIES_SWEPT=55 of 55` over 59,683 of 59,683 edges, `INCLUDED=34 EXCLUDED=21`, `FAMILIES_WITHOUT_A_REASON=0 of 55`; AC3 facts-per-key for 34 of 34 included with the 21 excluded printed in the same form, 13,927 keys over 41,060 edges, **`EDGES_ONLY_COUNTS_PRINTED=0`**; AC4 both of round 6's closing numbers reproduced at a named vintage with 5 differences printed and none absorbed | **G1-AC5** -- how wide the seam is, which families the fix must reach, whether any family is healthy only by accident, and what a reader must not conclude from a resolution rate |
| TO-CG-G-3 | CG-s-34 the archive-read substrate card | @`91654ab3c6` (acts 40a76d3fea, flip 95d3bf9037) | AC1 3 of 3 instances re-grounded from the record over 21 of 21 checks, channel parsed at 245 rows in 186 blocks with 0 unparsed; AC2 VALID on the estate's own validator, 4 of 4 cards, 0 violations (**instrument substituted -- row W2-S73, my cut defect, acked at S107**); AC3 `CARD_ROWS=3 of 3`, `QUESTIONS_PER_ROW=7 of 7`, `OWNER_PER_ROW=3 of 3`, `FAILURE_MODE_DISTINGUISHABLE=3 of 3` over 21 rows; AC4 `SHRINK_MASKED=true` on the round's own 955 -> 137 and `false` on a fixed-emission pair, 6 of 6 controls | **G3-AC5** -- and its premise came out **REFUTED**: owner is a function of the QUESTION, not the carrier (14 / 6 / 1 across 21 rows). The face was wrong and the worker was right |
| TO-CG-G-4 | CG-s-35 the portal layer's vintage | @`67d7453815` (acts 7abde30b23, flip e37c510700) | AC1 3 of 3 readings artifact-dated, `RECOLLECTION_USED=0`, 2 moves observed, per-reading zip denominators printed; AC2 `MOVERS_NAMED=2 of 2`, `UNNAMED_REPORTED=0`, sum equals the moves, control fired, three independent instruments (80 gitlink commits `--full-history`, 40 reflog entries, 702 ledger entries); AC3 `EXISTING_CARRIER=true` `CARRIER_UNFED=true` over `CANDIDATES_SWEPT=8 of 8`; AC4 0 producer files modified, 0 alerts, 0 egress acts, control fired | **G4-AC5** -- whether an undeclared vintage misleads a reader today or only could, which of the age-outcome's readers would notice, and whether the fix belongs to this plane at all |

## 2. What the round has established, and it is more than the criteria

**THE SEAM IS FIFTEEN NODES.** 29 of 59 node classes carry two identity strings, but only **15 of 27,665 nodes are KEYED BY the second identity, and all 15 are the whole of `S3_BUCKET_POLICY`** -- a bucket's NAME is the policy node's key. That single fact explains why 135 wrong-class landings read as resolutions rather than misses: it is the only place in the estate where an edge built onto a resource's other name finds a real node to land on.

**TWO FAMILIES SIT ON IT, NOT ONE.** `STORED_IN` (135 keys, one each) and `SERVED_FROM` (27 keys, one each), both 100% onto the policy node, the second from a different site (`derive_runner.py:1947-1955`). G2-AC2 was widened to read both before the fix started, because repairing one and leaving the other is the per-member fix on a seam the census had already shown is shared.

**THE CTO RULED THE VOCABULARY CALL INSIDE THE TICK IT WAS PITCHED (95004 @`f4bd6c6093`): RETIRE `STORED_IN`, RE-POINT `SERVED_FROM`.** Recorded against the weaker argument: the duplication count (`OWNED_BY` carries the same fact on the canonical node for 135 of 135 sources) is real and **not sufficient -- extensional equality on today's data is not identity of meaning.** What decided it is the cost asymmetry: an absence is checked once, a duplicate has to agree forever, inside a producer whose input contains its own output. **Three conditions bind the retirement** and are on G-2's face: census the READERS by subtraction (my cut measured writers, which is Condition 1 and my defect); `OWNED_BY`'s intent must absorb `STORED_IN`'s in words or the act is a deletion rather than a consolidation; and prove the absence with a positive control, an empty result set rather than a null count.

**THE CARD FOUND A DEFECT THE ROUND HAD NOT.** The NODES carrier has **no drop-on-read at all**: `derive_stitch.py:437-455` drops an archived copy only when the same id is in this run's emission, so a node the producer STOPS emitting is served another cycle with no error and no count. That is the nodes-carrier form of the exact sentence round 6 closed on, still open, owner `0.8.0_AE_CloudComp`. Beside it: the edges drop is keyed to the literal `STORED_IN` while the producer writes five edge types, and the props remedy is an enumeration of one key.

**THE PORTAL VINTAGE'S CARRIER EXISTS AND IS UNFED**, and the unfed-ness is not a display line: the feed is four hops, and hop 1 has no committed producer for the route that built every round-6 push while the committed route pins a stale third sha. Owners split across two seats. Nothing was written; every site is named with file, line and owner.

## 3. Four rows against this seat's own cut, and I am putting them at the top rather than in a footnote

| row | what my face claimed | what the run showed | acked |
|---|---|---|---|
| W2-S73 | `.tools/validate-json-schema.py` and the v1 card schema | the validator does not exist; the estate binds v3.1 and takes no schema argument (const 1 vs const 3.1, mutually exclusive) | S107 |
| W3-S17 | **MEASURED:** the provenance header "prints every `source_vintage` key it is given" | handed 7 keys it printed 3 and dropped 4 silently; structural, one branch per `source_kind` with no loop | S108 |
| W1-S36 | 54 edge families at 03:02:00 | 55 at the vintage actually read; a stale baseline carried forward into a face | S109 |
| W1-S35 | `DERIVES_FROM` as a member of the included set | it sits outside the both-identity population; reported as the named comparator and the seam's negative control | S109 |

**One shape, four instances, one seat, one night: a name or a contract written into a face as if it were a census or a run.** W3-S17 is the expensive one, because the label MEASURED is a field a consumer can reject on and I filled it from a contract document. Had it read ASSUMED, the worker would have owed the same exercise and my face would not have pointed at the wrong carrier first. **All four exist because the faces order a worker to REFUSE a criterion rather than rescue it, and all four workers took that literally.**

## 4. What the L9 is asked for

1. **Three judgment criteria:** G1-AC5, G3-AC5 (whose premise is refuted -- graded on what the worker found, not on what I assumed), G4-AC5.
2. Nothing else. G-2 is still open and its criteria are not offered here.

## 5. What this packet does NOT claim

1. **The boundary edges are not fixed on any plane yet** -- G-2 is running. Its served proof is bound to the same deferred pass that owes `F11-AC3`'s served re-take, because the standing egress law holds the derive while the SMS card is RESERVED FOR ANDREW.
2. **No act in this round touched AWS.** Measured rather than asserted per order: 0 egress acts, and on G-4 the client library appears zero times across all four executables, which bounds every AWS act at once.
3. **Push state:** LOCAL at this compile; `origin/CLOUD` @`c6bcb7b12b` (the CTO's `ls-remote` 04:44Z, not re-read here). Andrew holds the push.
