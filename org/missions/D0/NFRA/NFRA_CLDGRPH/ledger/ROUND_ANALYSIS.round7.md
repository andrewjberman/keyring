# ROUND 7 ANALYSIS -- NFRA_CLDGRPH

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-10 ~12:2xZ
**On the slug:** `3.0.0_SA_CVO` msg 95073, L9 committed @`2f86c28558` (rows C-S64..C-S66)
**Packet graded:** `ledger/L8_PACKET.round7.final.md` @`7c2bc76e39`, sha256
`147377ec13e1aa09ac027da6c5c34b929412c9f38881a1ecccf7d46fd541b51c` over 7,938 bytes --
**re-hashed at this seat over the blob at the issuer's own commit**, equal to the CVO's figure and
to the prefix the packet published. Three seats, one object.
**Graded against:** PRD **v0.14**

**A NOTE ON THIS ANALYSIS'S OWN LATENCY, because it is part of the record.** The slug was offered at
06:33:58Z. This device rebooted twice at 06:35Z and 06:44Z (RMM, then a TrustedInstaller OS upgrade),
killing every seat on it at 06:43:35Z, and the slug was never opened. All 20 messages to this serial
since 05:00Z read `OFFER-EXHAUSTED`, 0 READ. The L10 is late by a device event and by nothing else;
no limb of it was blocked.

---

## 1. The coverage read

**4 of 4 orders terminal and drained; all four worktrees and branches removed, no `wk-cldgrph-7-*`
remains.** All four judgment criteria graded (G1-AC5, G3-AC5, G4-AC5 at C-S62 on the partial; G2-AC5 in
the slug). **10 of 10 round-7 items dispositioned, 0 remaining.** No `org/modules/graph` path in any of
the four merges, so no comp-system pass was owed.

**Every endpoint outcome is served by a cell and no outcome went unserved, so there is no PRD addendum
this round -- the answer is this analysis**, as it was in round 6.

## 2. The grades: seven REALIZED, one NOT_REALIZED, and NOTHING MOVED

| | round 6 | round 7 |
|---|---|---|
| FWD-1, FWD-2, FWD-3, FWD-4, FWD-5, FWD-6, FWD-8 | REALIZED | **REALIZED, unmoved** |
| FWD-7 | NOT_REALIZED at `state_observed: APPLIED` | **NOT_REALIZED at APPLIED, unmoved** |

**Round 7 was not built to move a grade and did not move one.** Its four cells are the correctness and
substrate items round 6 handed forward in its own section 6 -- the boundary-edge class census, the bucket
identity, the archive-read carrier card, the portal layer's vintage. **Nothing in the round is deployed.**
Both producer files read `COMMITTED-NOT-DEPLOY-SCOPE`; deploying one is a CodeBuild start and the other an
image build plus an ECS derive, and all of it sits under the standing exclusion of all egress off Opal
infrastructure from agent autonomy. Every number in the packet is a LOCAL fold over real bytes. **None is
a served claim, and I grade none of them as one.**

**FWD-7's remaining limb is unchanged and is still an ACT, not a wait:** the PERSON half (row S22) -- a
site-Z seat and a laptop seat asking D-8's fixed question at the same moment through the public gateway,
byte-identical under one vintage. It gates on Andrew's allocation of a site-Z seat and, practically, on the
push he holds. That is a named person's named decision, which is the expressly-qualified exception the L2
law provides for, and this sentence is that qualification.

## 3. THE QUESTION THIS ROUND ACTUALLY PUT TO ME, and it is not one the packet asked

Round 7 found that **135 wrong-class facts survived every integrity control this project has ever run.**
The obligation that creates for an L10 is not to admire the finding. It is to ask: **did any grade I have
already called REALIZED rest on evidence this seam contaminated?**

**It did not, and the reason is worth naming because it is the only thing standing between here and a
retraction.** Round 6's grain baseline -- the signature seven REALIZED grades lean on -- **fenced itself in
its own text.** At `ROUND_ANALYSIS.round6.md:55` @`b831616961`, verbatim: *"The signature states what it
does NOT certify: not the `STORED_IN` endpoints, not any class outside the nine, not the artifact's
internal counts."* The contaminated objects are `STORED_IN` and `SERVED_FROM` **edges**; the baseline
certifies **node** classes at their magnitudes. The one object round 7 proved wrong is the one object round
6's signature explicitly declined to vouch for.

**So a disclosure written a round early is what makes tonight a finding rather than a retraction.** The CVO
raised the mirror-image hazard in the same slug -- a disclosed substitution that travels without its
disclosure becomes a silent one at the second hop -- and this is the same mechanism paying out in the other
direction. **I am recording it because the next reader will inherit the numbers and not the fence.**

## 4. The mechanism, and why no control could have caught it

`kuzu_nessie_load.py:204` keys a served node `arn or node_id` and matches edge endpoints RAW against that
key space. A bucket's served key is its ARN; an `S3_BUCKET_POLICY` carries the bucket NAME in its own `arn`
column, so the policy node's served key IS the bucket name. `:249-251` count `skipped` only for endpoints
ABSENT from that key space. **Therefore an edge built on a bucket's name never dangled. It LANDED, on the
policy node, and every dangling check read clean.**

This is Rule 22's shared-dependency limb exactly: every per-family integrity check passed **because they all
consulted the same key space**, and a check scoped to the members cannot see a defect in what the members
share. The reading proves a JOIN RULE rather than an edge-builder bug, and the CVO verified its central
claim at HEAD with an instrument the worker did not use -- `git show` of the blob, never the worktree.

**The strongest number in the answer is one the report does not flag as such:** `by_edge_type={"STORED_IN":
137}` carries **no** `SERVED_FROM`. Had the producer half not landed, its 27 endpoints would have needed the
fold's rewrite and would appear in that dict. They do not. **An absence from a dict that would have carried
it** is what evidences "producer and fold each did their own half", and it makes the 27 of 27 emission at
source rather than rescue at admission.

**One caution attached to a number and not to a grade, restated here so it travels:** the BEFORE half of the
before/after table is NOT re-derived by this run. `162 -> 0` reads as one movement while being two readings
of different planes at different vintages. The capture discloses it in its own words at line 7. Anyone
quoting the pair quotes the disclosure with it.

## 5. The retirement did not happen, and its failure bought a law

Both binding conditions of the `STORED_IN` retirement I ruled at 94872 failed **on measurement**, which is
the outcome a condition exists to produce.

1. **Condition 1's census, run exactly as I specified, AUTHORIZES A BREAKING RETIREMENT.**
   `MANIFEST_TOOLS_TOUCHING_STORED_IN = 0 of 78` over the declared manifest -- and that zero is honest for
   that domain, since 78 of 78 names resolved to a file under `.tools/`, so the arm separating a true zero
   from a resolution failure was present and passed. The unscoped sweep of 31,293 tracked files finds
   **FIVE** consumers outside it. **The remedy I wrote to prevent a scoped-domain error specified a scoped
   domain**, because a manifest is a DECLARATION of consumers and not a census of them.
2. **Condition 2 is blocked by measurement.** `OWNED_BY` is consumed as a CONTAINMENT seam by
   `cse_schema.py:323`, `comp_marker_read.py:121` and `comp_coverage_check.py:523`. Widening its stated
   intent to absorb location changes what three readers mean, and by the condition's own terms a retirement
   whose surviving term cannot absorb the retired one's intent is a DELETION.

**THE LAW EDIT IS LANDED AND BROADCAST, not deferred to this document.** The CVO raised the amendment and
assigned it here because the rule it sharpens is this seat's own and its one send was spent on the slug.
Rule 24(i) now carries: **a subtraction's DOMAIN must be the claim's POPULATION; choosing the domain is
itself a claim, falsified BEFORE the subtraction runs by one unscoped read with its denominator printed; a
member the domain does not hold VOIDS the subtraction; a denominator certifies the SWEEP, never the SET.**
Committed @`b3bc1d7511`; broadcast the same turn to the four seats measured live (95086-95089). The failure
mode is a GREEN -- a wrong domain returning non-empty gets argued with, returning empty it gets acted on --
and here the empty set WAS the authorizing branch.

**And half of why this needed a ruling at all is mine at the cut, not the assignee's:** the retirement
arrived as a ruling's condition on a face whose accepts are `G2-AC1..AC5`. **A ruling was written onto a face
with no criterion to grade it**, so the order could not tell its assignee whether the retirement was inside
what it accepts. The worker held `<status>` pending on condition 1's STOP instruction -- correct, and the
refusal clause working as designed. The state left behind is the safe one: the family is live and now
correctly pointed, so the retirement's argument is stronger and its urgency lower, and nothing is
half-landed.

## 6. What round 8 inherits -- the recut, ONE issuance, each cell with an owner

`2.0.0_SA_COO~A` cuts these. **The retirement becomes its own cell with its own accepts, where it can be
graded rather than merely required.**

| # | cell | rows | owner |
|---|---|---|---|
| 1 | **The retirement, as its own cell.** Reader denominator is **the REPOSITORY, not the manifest** -- this is the new Rule 24(i) clause binding at the cut, not advice | W1-S37, W1-S38, S110 | `2.0.0_SA_COO~A` to cut; `0.8.0_AE_CloudComp` the producer half |
| 2 | **The NODES carrier's missing drop-on-read** | W2-S74/S75, S103 | `0.8.0_AE_CloudComp` |
| 3 | **The portal vintage's four-hop feed**, hop 1 with no committed producer | W3-S17, S108 | `0.7.0_AE_CloudOps` hops 1-2, the engine hops 3-4 |
| 4 | **The 124-edge silent loss, bounded but unexplained.** The question is what republished the projection | W1-S39, S111 | open -- name an owner at the cut |
| 5 | **Two scorers declaring different canonical shapes for one edge**, one with the wrong class baked into a scored artifact | the census record | outside this plane, PLACED |
| -- | **The served re-take of `F11-AC3` and `G2-AC2`** -- ONE pass, when the hold lifts | S102, S104 | **Andrew's answer gates it. NOT cuttable now** |

**THE SERVED RE-TAKE CARRIES FOUR REQUIREMENTS AND THEY ARE PLACED HERE, NOT CHASED,** because the deferred
pass is not round 8's to cut. I adopt the CVO's reasoning as binding on whoever eventually cuts it: a served
re-take that reads LOW cannot separate *"the fix did not reach the served plane"* from *"the projection
dropped the family again"* -- and the second branch is measured, bounded to one drop, and **unexplained**.
**So the re-take would fail in the shape of a failed fix.** Before it reads a count it must carry: the
producer's own emission figure for the NAMED run; the projection manifest id and served vintage printed
beside the count; `OWNED_BY` read in the SAME tick as the negative control that moved zero; and **its QUERY
FORM stated**.

**That is my own condition 4 -- an absence must be ATTRIBUTABLE -- arriving one step EARLIER than I placed
it.** I put it on the proof of the removal. It belongs on the re-take of the FIX, because an unexplained
mover on a plane makes every reading of that plane non-attributable IN BOTH DIRECTIONS. **Adopted as
written.**

## 7. Five rows against the cut, in one round, and one shape

W2-S73 (a validator path and card-schema version that do not exist), W3-S17 (a premise labelled MEASURED
taken from a contract document whose header prints 3 of 7 keys and drops 4 silently), W1-S36 (a count
carried from an earlier vintage), W1-S35 (a comparator force-fitted into a population it sits outside), and
the ruling-without-a-criterion above.

**One shape: a name, a contract or a declaration written into a face as if it were a census or a run.** It is
the same shape as condition 1's manifest, one grain up -- which is why the law edit in section 5 is the
round's product and not a footnote to it.

**Every one was surfaced by the ASSIGNEE, and every one came back through the refusal clause.** So did all
six graduated items: the assignee ran the unscoped sweep nobody asked for, the issuer took the third served
read nobody asked for. **Not one came from a control, a gate or a census.** That is a fact about where this
estate's defects are actually found, and it should inform what we spend on controls next.

## 8. Where this leaves the project

`dep_stage` stays **EXECUTING**. Seven of eight outcomes hold; the eighth is one allocation away and has
been since round 6. Round 7 bought correctness beneath the seven, not progress toward the eighth --
which is the right trade when the eighth is gated on a person and the correctness was silently wrong.

**FOR ANDREW, one line, and it is the same line as last round:** FWD-7's last limb needs a site-Z seat
allocated, and site Z cannot read what rounds 6 and 7 built until the push. Everything else here is
moving without you.

## Push state
**MEASURED this turn, not carried forward:** local `CLOUD` @`b3bc1d7511`; `origin/CLOUD`
@`c6bcb7b12b0d0134274f689f470a91252d100546` by `git ls-remote` at this seat. `b3bc1d7511` reads **LOCAL**
by `merge-base --is-ancestor`; positive control `32ae4ede66` reads ON-BRANCH with the same instrument, so
the LOCAL verdict is a verdict and not a broken comparison. The two have diverged because the `~Z` fabric
worked through this device's reboot. **Publication is the integrator's act, and this claim ages the moment
one runs.**
