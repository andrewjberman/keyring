# NFRA_CLDGRPH -- L8 PACKET, ROUND 7, **FINAL** (4 of 4 orders drained) -- compiled by `2.0.0_SA_COO~A` 2026-09-10 06:2xZ, for `3.0.0_SA_CVO` at L9

Supplements `L8_PACKET.round7.partial.md` (3 orders, READ 05:31Z), which stands as filed. This packet carries **TO-CG-G-2**, the last order, and closes round 7's compile. **Grade against PRD v0.14.**

## 1. Round 7, all four

| order | cell | drained at | mechanical | judgment for L9 |
|---|---|---|---|---|
| TO-CG-G-1 | CG-s-32 the boundary-edge class census | @`15bfeb3a62` | 4 of 4 PASS (see the partial) | **G1-AC5** |
| TO-CG-G-3 | CG-s-34 the archive-read substrate card | @`91654ab3c6` | 4 of 4 PASS, one on a substituted instrument (row W2-S73, my defect, acked S107) | **G3-AC5**, premise REFUTED |
| TO-CG-G-4 | CG-s-35 the portal layer's vintage | @`67d7453815` | 4 of 4 PASS | **G4-AC5** |
| **TO-CG-G-2** | **CG-s-33 the bucket identity made one** | **@`e0255e47db`** (acts d4b17b4f6f, instance baf9e4c839, flip 7a3eaeb135) | **4 of 4 PASS**: AC1 `FIXTURE_ARMS=6 of 6` with `NEGATIVE_CONTROL=FIRED` over 4 fixture graphs and a mutant run; AC2 `STORED_IN 137 of 137` and `SERVED_FROM 27 of 27` onto `S3_BUCKET`, `ON_S3_BUCKET_POLICY=0 across both families`, `DERIVES_FROM 216 of 216`, over 59,887 resolved edges on `snapshots/20260910`; AC3 `RECONCILED 1790 = 1790 lost 0`, `GRAIN-SENTINEL: PASS` with its own 35-of-59 coverage qualifier CARRIED, `MAGNITUDES_UNCHANGED=5 of 5`; AC4 all five held acts at zero with `EGRESS_PROBE_CONTROL=FIRED` and 5 of 5 planted acts caught | **G2-AC5** -- what a LOCAL fold can and cannot prove about the served plane, what the served re-take will need, and whether normalizing at admission risks anything for a producer already emitting arns |

**Four of four terminal, four of four drained, all four verified in their worktrees before the merge. All four worktrees and branches removed; no `wk-cldgrph-7-*` remains.** No `org/modules/graph` path in any of the four merges, so no comp-system pass was owed in this round.

## 2. The round's substance: the seam was found, understood, and fixed on the plane the hold allows

**THE MECHANISM, and it is not what either the ruling or my cut named.** `kuzu_nessie_load.py:204` keys a served node `arn or node_id` and matches edge endpoints **RAW** against that key space. A bucket's served key is its ARN. An `S3_BUCKET_POLICY` carries the bucket **NAME** in its own `arn` column, so the policy node's served key IS the bucket name. **Therefore an edge built on the bucket's name never dangled -- it LANDED, on the policy, and every dangling check this project has ever run read clean.** That is the whole explanation for 135 wrong-class landings surviving every integrity control, and it is a discrimination failure of exactly the kind Rule 22 names: the instrument could not have told the two apart.

**BOTH PLANES MOVED IN ONE ACT**, as 94872 requires. The producer emitting canonically ALONE would have reproduced round 6's `0 of 955`; the fold's widened admission is what prevents that, exercised as fixture arm 6 (`admitted=1 of 1` against a pre-fix id set that admits `0 of 1`). **And `resolvable_before=64078 -> after=64080`: the widened admission RECOVERED round 6's two unresolved edges**, so 137 is a recovery and not a fan-out.

**NOTHING IS DEPLOYED AND THAT IS DELIBERATE.** Both producer files read `COMMITTED-NOT-DEPLOY-SCOPE`. Deploying one is a CodeBuild start; deploying the other is an image build plus an ECS derive. All three are held by the standing exclusion of ALL EGRESS OFF OPAL INFRASTRUCTURE from agent autonomy while the SMS card is RESERVED FOR ANDREW. Every number above is a local fold over real bytes; **none is a served claim**, and the served re-take stays bound to the deferred pass that already owes `F11-AC3`'s.

## 3. THE RETIREMENT DID NOT HAPPEN, and its own conditions are why

Ruled by the CTO at 94872: retire `STORED_IN`, re-point `SERVED_FROM`. **Both of the retirement's binding conditions failed on measurement, and the first failed in a way that is the round's most valuable finding.**

1. **CONDITION 1's CENSUS, RUN AS SPECIFIED, AUTHORIZES A BREAKING RETIREMENT.** `MANIFEST_TOOLS_TOUCHING_STORED_IN=0 of 78` over the declared denominator. The unscoped sweep of 31,293 tracked files finds **FIVE** consumers outside it. The remedy written to prevent a scoped-domain error specified a scoped domain, because **a manifest is a DECLARATION of consumers and not a census of them**. Row W1-S38, acked and carried at S110. Two of the five are the `tsgraph_spike` pair row W2-S25 declared harmless for a different question one round ago.
2. **CONDITION 2 IS BLOCKED BY MEASUREMENT.** `OWNED_BY` is consumed as a CONTAINMENT seam by `cse_schema.py:323`, `comp_marker_read.py:121` and `comp_coverage_check.py:523`, so widening its stated intent to absorb location changes what three readers mean. By the condition's own terms, a retirement whose surviving term cannot absorb the retired one's intent is a DELETION. Row W1-S37, open, disposition the CVO's.

**AND ONE HALF OF WHY THIS TOOK A RULING IS MINE:** the retirement arrived as a ruling's condition on a face whose accepts are `G2-AC1..AC5`. **I wrote a ruling onto a face without cutting a criterion to grade it**, so the order could not tell its assignee whether the retirement was inside what it accepts. The worker held `<status>` pending on condition 1's STOP instruction -- correct, and the refusal clause working -- and I ruled flip-and-stop @`86adc0280a`. **The retirement becomes its own cell with its own accepts in round 8, where it can be graded rather than merely required.** The state left behind is the safe one: the family is live and now correctly pointed, so the retirement's argument is stronger and its urgency lower, and nothing is half-landed.

## 4. Carried to round 8, each with an owner

| item | rows | owner |
|---|---|---|
| The retirement, as its own cell with its own accepts; reader denominator = the REPOSITORY, not the manifest | W1-S37, W1-S38, S110 | `2.0.0_SA_COO~A` to cut; `0.8.0_AE_CloudComp` for the producer half |
| The served re-take of `F11-AC3` and `G2-AC2`, one pass, when the hold lifts | S102, S104 | Andrew's answer gates it |
| The NODES carrier's missing drop-on-read | W2-S74/S75, S103 | `0.8.0_AE_CloudComp` |
| The portal vintage's four-hop feed, hop 1 with no committed producer | W3-S17, S108 | `0.7.0_AE_CloudOps` hops 1-2, the engine hops 3-4 |
| The 124-edge silent loss, bounded but unexplained | W1-S39, S111 | open; the question is what republished the projection |
| Two scorers declaring different canonical shapes for one edge, one with the wrong class baked into a scored artifact | the census record | outside this plane, placed |

## 5. Five rows against this seat's own cut, in one round

W2-S73 (a validator path and card-schema version that do not exist), W3-S17 (a premise labelled MEASURED taken from a contract document; the header prints 3 of 7 keys and drops 4 silently), W1-S36 (a count carried from an earlier vintage), W1-S35 (a comparator force-fitted into a population it sits outside), and the ruling-without-a-criterion above. **One shape: a name, a contract or a declaration written into a face as if it were a census or a run.** Every one was surfaced by the ASSIGNEE and none by me, and every one came back through the refusal clause -- which is now spine v3.11 L6 and was cut from this lane's own generalisation.

## 6. What the L9 is asked for

1. **Four judgment criteria:** G1-AC5, G3-AC5 (premise refuted -- grade on what the worker found), G4-AC5, G2-AC5.
2. **The disposition of W1-S37** (the retirement's blocker) and of the two carried ARMED rows W1-S38 and W1-S39.
3. Nothing else. No sign is outstanding in this round.

**Push state:** LOCAL at this compile; `origin/CLOUD` @`c6bcb7b12b` (the CTO's `ls-remote` 04:44Z, not re-read here; local reported 390 ahead at 06:1xZ). Andrew holds the push.
