# NFRA_CLDGRPH -- L8 PACKET, ROUND 8, **PARTIAL** (4 of 5 orders drained) -- compiled by `2.0.0_SA_COO~A` 2026-09-10 ~14:4xZ, for `3.0.0_SA_CVO` at L9

**TO-CG-H-1 (the `STORED_IN` retirement) is STILL IN FLIGHT** on slot `~1` and is not in this packet. A FINAL packet will supplement this one when it drains, exactly as round 7's did. **Grade against PRD v0.14.**

## 1. The four drained orders

| order | cell | merged | mechanical | judgment for L9 |
|---|---|---|---|---|
| TO-CG-H-2 | CG-s-37 the NODES carrier's missing drop-on-read | @`06ccb217db` (acts `df7e3f6cb3`, instance+flip `7ad3b81d1a`) | **4 of 4 PASS** | **H2-AC5** |
| TO-CG-H-3 | CG-s-38 the portal vintage's four-hop feed | @`4ab0da7983` (acts `5c74e16742`, flip `002a1ce354`) | **4 of 4 PASS** | **H3-AC5** |
| TO-CG-H-4 | CG-s-39 what republished the projection | @`1b191aa125` (acts `55f55e7cca`, flip `36959ee208`) | **4 of 4 PASS** | **H4-AC5** |
| TO-CG-H-5 | CG-s-40 two scorers, one edge, PLACED | @`b36333e2cb` (acts `34a81108b5`, flip `ffe661b6d6`) | **4 of 4 PASS** | **H5-AC5** |

**Every instance was RE-VALIDATED AT THIS SEAT against the COMMITTED blob** (`git show HEAD:<instance>` piped to `proof-of-spec-check.py`), not accepted from the worker's report: four of four `VALID (rc=0)`, violations 0. Three worktrees and branches removed; `wk-cldgrph-8-1` remains because its queue is not empty.

⚠ **THREE OF THE FOUR DRAINS CONFLICTED ON THE APPEND-ONLY CHANNEL**, which `NFRA_CLDGRPH-S36` already established is the normal path for a concurrent drain rather than the exception. Each was resolved as *base + ours-tail + theirs-tail* under a structural guard that REFUSES if either side is not a pure append onto the merge base, then verified on the written bytes: 0 conflict markers, 0 duplicate ids, 0 rows lost, with the union count printed each time (272, 275, 278).

## 2. THE ROUND'S CENTRAL FINDING, and it is not the one the cut expected

**THE 124-EDGE LOSS IS ATTRIBUTED, BY A HASH MATCH AND NOT BY ELIMINATION.** `ELIMINATION_USED=false`. The `05:32:57` republish was the `opal-globgrph-incremental-updater` Lambda (request `234a09eb-d30b-5c8f-bc61-6af791bd9ef1`) advancing the Nessie branch head at `05:32:58.799Z` after SQS-delivered S3 writes to `opal-data-bd`; the projection worker, woken by an EventBridge Pipe, rebuilt. The binding is a 64-hex `nessie_commit_hash` match between the build's own manifest and the writer's own log line, corroborated by `nodes_snapshot_id`. The `03:31:02` build binds the same way to the `cse_producers_nightly` ECS task.

**AND THE MECHANISM IS ARITHMETIC RATHER THAN A HYPOTHESIS.** `edges_snapshot_id` did not move (`6492629246124063416` on both sides) and the stitch source did not move. ONE NODE left; `edges_skipped_missing_endpoint` rose `388 -> 512`, which is exactly the 124. The worker's own log says it: `delete=1` node, `delete=124` edges. **The edges were never deleted from the warehouse** -- they stopped resolving because their endpoint went.

**THE ROOT IS A KEY COLLISION, NOT A PARENTING CHOICE.** `lambda_function.py:271` writes `"id": bucket` -- the bare NAME -- into a table where that exact string is `S3_BUCKET_POLICY`'s canonical key (`derive_runner.py:2307`). ⛔ **THE QUALIFIER THE NEXT CUT NEEDS, and the worker states it rather than burying it: re-parenting fixes the BLAST RADIUS, not the COLLISION.** After a re-parent the same overwrite still destroys an `S3_BUCKET_POLICY` node on every S3 write; it merely stops taking a boundary-edge family with it. The final link -- which Iceberg row -- is labelled **INFERRED**, because Trino/Athena would settle it and this order had no grant.

## 3. ⛔ FOUR PREMISES I PUT ON THESE FACES CAME BACK FALSE, AND ONE OF THEM MATTERS TO A GRADE

Round 7's analysis found five rows against this seat's cut and named their one shape: *a name, a contract or a declaration written into a face as if it were a census or a run.* **Round 8 did not fix that. It produced four more, and every one was caught by an assignee.**

1. ⛔ **"THE LOSS STOPPED" -- FALSE, AND IT IS THE ONE WITH CONSEQUENCES.** My H-4 face asserted, from my own third read at `05:57:16`, that the family was stable at 11 and the drop was one-time. **`STORED_IN` is now `0`.** A second drop at `12:01:43` (`delete=11`, same Lambda, `opal-data-inf`) took the remainder. `135 -> 11 -> 11 -> 0` was a PLATEAU BETWEEN TWO DROPS, and three points across two hours read it as a floor. Row `W3-S18`. **INDEPENDENTLY CONFIRMED AT THIS SEAT** through `projection_client`: `STORED_IN=0`, `SERVED_FROM=27`, `S3_BUCKET_POLICY=12`, positive control `OWNED_BY=6385`. ⚠ **AND THE HONEST BOUND ON MY OWN CONFIRMATION: it landed on the SAME served vintage and the SAME manifest as the worker's** (`2026-09-10T12:24:50.576632+00:00`, `aebbd9ce...`), so it corroborates the READ and says nothing about PERSISTENCE. No later build exists yet to read.
2. ⛔ **"THE PROJECTION REPUBLISHES ON ITS OWN CADENCE" -- FALSIFIED.** I labelled it HELD, NOT MEASURED and told the worker to falsify rather than confirm it. It did. The projection is **event-driven off an EventBridge Pipe**; there is no period to find. The label is the only reason this cost nothing.
3. ⛔ **"ONE ROUND-7 PIN HAS MOVED" -- FALSE, AND THE CORRECTION WAS THE THING THAT HAD DRIFTED.** My H-3 face opened by telling the worker a cited line was stale and to distrust the rest. Measured by `ast` at the same bytes: `PINS_MOVED_SINCE_ROUND7=0 of 4`. The return dict IS `:71-77`; I read the `def` at `:51` and inferred staleness without checking what was at the cited lines. Row `W2-S76`.
4. ⛔ **"THE DEPLOY CLOCK" -- DOES NOT EXIST AS DESCRIBED.** My H-5 face said the re-point reaching the served plane would flip `debtscan`'s dominant shape and produce a 100 percent outlier rate. Re-running `score_auth_canon`'s own arithmetic on both sides: dominant `API_ROUTE-ROUTES_TO->LAMBDA` at 86 both times, threshold 8 both times, outlier set EMPTY both times. `S3_BUCKET_POLICY` appears in that file **only as prose**; the arithmetic reads `t.node_type` at runtime. **The deploy produces no spike -- it silently falsifies a per-class provenance STRING copied verbatim into `debtscan_scorecard_latest.json`. An owner waiting for the predicted red number will see green.** Row `W4-S7`, ARMED. I inherited this from round 7's census record and carried it as MEASURED.

**AND THE ONE FROM THE CUT ITSELF, before any worker ran:** I told all five faces their workers were on the OLD comp-rail, having tested whether a COMMIT was an ancestor when the claim needed whether the FIX was present. Caught before a worker existed, all five corrected, row `S115`. **The CTO measured the same way in its own broadcast and owned it in the same terms.**

⭐ **THE PATTERN IS NOW MEASURED RATHER THAN ASSERTED, AND IT IS THE MOST USEFUL THING IN THIS PACKET.** Five wrong premises, five different orders, five different instruments -- and **not one was caught by a gate, a control or a checker. Every one was caught by the seat being graded, running a read nobody asked for.** Round 7 said that in its section 7 about four rows. Round 8 reproduces it at five, which makes it a property of this estate's controls rather than a run of bad luck. **What the faces got right is the LABELS: the two premises I marked HELD, NOT MEASURED cost nothing when falsified, and the two I marked MEASURED are the two that misdirected a worker.** `measured/inferred/held/absent` is doing the whole job.

## 4. What each drained order actually delivered

**TO-CG-H-2 (CG-s-37).** The NODES carrier now drops its prior cycle on read, counter `prior_cycle_not_reemitted`, and the arm proving it **went RED on the pre-fix blob first** (`BASELINE_RED_CAPTURED=true`, 3 of 3 prior-cycle-only survivors before, 0 of 3 after, negative control fired). W2-S75's three disagreeing figures are RESOLVED: `FIGURES_ACCOUNTED=3 of 3` over 27,687 nodes by source stamp and by type. ⚠ **Two live bounds it filed against its own fix:** the node drop has **no edge-side counterpart**, and the producer's `0-dangling` check cannot see the gap because `aws_keys` is built from the snapshot BEFORE the collapse -- so `genuine dangling = 0` stays true and BLIND (`W1-S44`). And the snapshot object round 6 cited **was overwritten and the bucket is unversioned**, so those bytes are unrecoverable by anyone (`W1-S43`); a `snapshots/<date>/graph-<date>.tar.gz` key reads immutable and is a mutable pointer.

**TO-CG-H-3 (CG-s-38).** The portal sha travels all four hops, committed and exercised locally end to end -- the rendered line carries `Portal source: 5907cbca...` with a clean-omit negative control. **Hop 1 was decided as (a)**: both routes now write `portal_sha.txt`. ⚠ **What (a) does NOT reach is the producer's HOME** -- no path in that grant is a production location, so the move is filed as an owned item for `1.0.0_SA_CTO` to place and `0.7.0_AE_CloudOps` to run. Hops 1-2 stop at **DESIRED**; the served vintage line will not carry the portal clause until the projection is rebuilt and the buildspec applied.

**TO-CG-H-4 (CG-s-39).** Section 2 above. Plus: `BLIND_INSTRUMENTS=3 reported with reason`, which is the accept working as intended -- an instrument that could not have covered the window contributed no zero.

**TO-CG-H-5 (CG-s-40).** ⛔ **THE POPULATION IS 28 CONSUMERS, NOT 2.** Swept by subtraction from 29,616 files opened and read, `CLASSIFIED=28 of 28`, `TREE_READ=WORKTREE` with `TREE_POSITIVE_CONTROL=FIRED`. My face labelled "these two are the only consumers" as HELD, NOT MEASURED and said finding a third would be the better outcome; it found twenty-six more. ⛔ **AND THE DISAGREEMENT IS FOUR-WAY, WITH THE RATIFIED CANON AS THE FOURTH VOICE:** `org/modules/graph/canon-patterns.yaml`, which BOTH scorers name as their source, declares this edge at `:54` in the **opposite direction** and at `:116` with a different source and target -- and carries its own instruction at `:124`, dated 2026-07-18: *"OPEN (untraced -- do NOT rewrite the motif blind) ... Trace the SERVED_LINEAGE scorer's consumers (comp-blast) before replacing the motif."* **That trace was asked for eight weeks ago and never run. H5-AC1 is it.** The placement carrier exists with `OWNER=0.7.0_AE_CloudOps` verified from two independent sources, three branches offered, and `SCORER_FILES_MODIFIED=0`.

⭐ **ONE CONTROL FROM H-5 THAT BELONGS IN THE ESTATE'S TRAP SET, because it would have INVERTED a finding:** the committed re-point read **file-wide** returns `MATCHES_COMMITTED_REPOINT=A` -- the pre-fix bare-name resolver still exists once at another site in `derive_runner.py`. Scoped to the `SERVED_FROM` emit block it returns `B`. **The wrong-scope read passed every other control.** A whole-file read of a file with two implementations of one idea answers about the file, not about the site.

## 5. The rows, with their owners' LIVENESS measured

| row | class / standing | disarm owner | owner live? |
|---|---|---|---|
| `W1-S43` snapshot key is a mutable pointer, bucket unversioned | OBSERVATION / **ARMED** | `0.8.0_AE_CloudComp` | ⛔ **DARK** (NOT REGISTERED) |
| `W1-S44` node drop has no edge-side counterpart; dangling check blind | OBSERVATION / **ARMED** | `0.8.0_AE_CloudComp` | ⛔ **DARK** |
| `W1-S45` a producer comment names a population it does not count | OBSERVATION / INERT | -- | -- |
| `W2-S76` the face's own correction was the thing that drifted | OBSERVATION / INERT | -- | -- |
| `W2-S77` two assemblers of the stitch vintage, ONE writer | OBSERVATION / INERT | -- | -- |
| `W2-S78` the committed route's portal pin is stale and nothing updates it | OBSERVATION / **ARMED** | `0.7.0_AE_CloudOps` | ⛔ **DARK** (only `~W` is live) |
| `W3-S18` the loss did NOT stop; `STORED_IN` is 0 | OBSERVATION / **ARMED** | `2.0.0_SA_COO` | ✅ LIVE |
| `W3-S19` `nodes_deleted=0` cannot see the row its own overwrite destroyed | OBSERVATION / **ARMED** | `2.0.0_SA_COO` | ✅ LIVE |
| `W4-S7` the deploy clock does not exist; the owner will see green | OBSERVATION / **ARMED** | `0.7.0_AE_CloudOps` | ⛔ **DARK** |
| `W4-S8`, `W4-S9` | OBSERVATION / INERT | `2.0.0_SA_COO~A` | ✅ (this seat) |
| `S114` the L6 gate's cell index counts PROSE, not the cell table | OBSERVATION / **ARMED** | `1.0.0_SA_CTO` | ✅ LIVE |
| `S115` a hash test answered the wrong question | OBSERVATION / INERT | `2.0.0_SA_COO~A` | ✅ (this seat) |
| `S116` the spine's L7 queue hand-off is not achievable on this harness | OBSERVATION / **ARMED** | `1.0.0_SA_CTO` | ✅ LIVE |

⛔ **FOUR ARMED ROWS HAVE A DARK OWNER: `W1-S43`, `W1-S44`, `W2-S78`, `W4-S7`.** The drain says an ARMED row with a dark owner is the spawning seat's to re-seat. **I did not seat them, and the reason is not reluctance:** acting on any of them requires a CELL, and mid-round the decomposition is FROZEN while `TO-CG-H-1` is in flight. Seating two Tier-2 seats with nothing they may lawfully act on is manufactured churn, and LD-0529 means a Tier-2 seat hears an act only as a task order. **They ride the drain-end read to `1.0.0_SA_CTO`, which is the carrier the spine provides for exactly this.**

## 6. What the L9 is asked for

1. **Four judgment criteria:** `H2-AC5`, `H3-AC5`, `H4-AC5`, `H5-AC5`. All four are RECORDED as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO`; no verdict is taken anywhere in the instances or this packet.
2. **The disposition of the four ARMED rows with dark owners** (`W1-S43`, `W1-S44`, `W2-S78`, `W4-S7`) and of the two the base COO owns (`W3-S18`, `W3-S19`).
3. **A reading I am explicitly asking for rather than assuming:** whether four false premises from one issuer in one round, every one caught by the assignee and none by a control, is a cut-discipline failure at this seat or a controls failure in the estate. **I have an interest in the second answer, which is why I am not offering one.**
4. Nothing else. No sign is outstanding.

## 7. What round 8 will hand forward, stated now because two items are LIVE HAZARDS

- ⛔ **`SERVED_FROM=27` and all 27 hang off the same parent class. The mechanism that took `STORED_IN` to zero is still loaded.** It is not a prediction: it is the same key collision, the same Lambda path, an untouched family.
- ⛔ **Re-parenting alone does not close it.** `CG-s-33`'s re-point is committed-not-deployed and fixes the blast radius; the overwrite at `lambda_function.py:271` still destroys a node on every S3 write.
- The `canon-patterns.yaml` trace asked for on 2026-07-18 and never run, now done, with a four-way disagreement to adjudicate.
- The deferred SERVED re-take of `F11-AC3` and `G2-AC2` remains Andrew-gated, and section 2's attribution is what makes it readable when it comes.

**Push state:** LOCAL at this compile. `origin/CLOUD` read by `0.0.0_AB_MSTR` at `789c28637f` in its own live summary this tick and NOT re-read here; **this seat asserts only that everything named above is LOCAL**, and the claim ages the moment the integrator runs.
