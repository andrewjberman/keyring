# Research: a live map of what every box is working on, and where two boxes are getting close

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07 ~21:5xZ. **For:** Andrew.
**Status:** research and a proposed shape. Nothing was built and nothing in the estate was changed.

## His words, VERBATIM AND ENTIRE (typed at the 4.0.0_SA_CRO terminal, ~21:3xZ; the first paragraph is text he pasted)

> "what im wondering, is how do we keep effectively a streaming map of what seats are doing which is like a risk map,
> where one box is coming too close to another box, e.g. two devices with a team on each that are working on opal_ai,
> and then all of a sudden both are working on opalgateway and terraform, and then all of a sudden they are both making
> edits to the tf? I'm wondering if there is a way to essentially keep an eye on these things so that control plane can
> step in if needed. Also this system would of course be inherently foundational in managing GitOps, as it would be
> able to tell when the optimal times would be for merges, pulls and pushes."

> "I want you to look into this mechanism and figure out how we would build something like this, and how we could
> abstract it in such a way that it could be a foundational tool for the control plane, maybe its a streaming service
> with some figures appearing per box and overlap danger and etc. I feel like a service like this could have all kinds
> of uses for us, many applications. I ask because we just did 2300 commits today and there is absolutely no way I can
> keep track of this as one person, so need to start thinking in greater aggregations."

**Reading, narrow:** an order to research the mechanism, how to build it, and how to abstract it. Not an order to build
it. A service that watches and lets the control plane step in is a monitor, and the standing rule bars building one
without his explicit word; this document ends with that word as a call.

---

## 1. Conclusion

1. **It can be built almost entirely from records the estate already writes.** No new sensing is needed for a first
   version: git, task orders, the deploy ledger and the device register already hold what each box intends, what it
   did, and what it has in flight.
2. **The right abstraction is one small record, "a box did a thing to a surface", and one question asked of it: which
   surfaces have two boxes on them.** Everything he lists (the overlap danger, the figures per box, the best time to
   merge) is a different read of that one table.
3. **Today's real overlap is small and is exactly the dangerous kind.** Of 3,672 files changed today, 64 were touched
   by two or more boxes. 44 of those are shared registers and logs that are meant to be shared. About 14 are code,
   tools or infrastructure, and one Terraform folder was edited by two boxes: the case in his example.
4. **Build it in three steps, cheapest first:** a read-only tool on the laptop that computes the map from git on
   demand; then each box reporting its own events as they happen; then a page. Step 1 is days of work and needs no new
   cloud resource.

---

## 2. What today looked like, measured

Read at 2026-10-07 21:4xZ from every branch the laptop can see (after one `git fetch`), commits since midnight Eastern.

| Measure | Value |
|---|---|
| Commits, not counting merges | 2,022 |
| Merges | 494 |
| Distinct authors (seats, lanes, workers) | 240 |
| Files changed | 3,672 |
| Commits by box | laptop 759, dell2 571, site Z 349, dell1 340, unplaced 3 |
| Files touched by two or more boxes | 64 (1.7%) |
| Files touched by three or more boxes | 3 |
| Terraform folders edited | 11 |
| Terraform folders edited by two boxes | 1: `shared-infra` (laptop 6 commits, dell2 1) |

What the 64 shared files are:

| Kind | Files | Is the sharing a problem? |
|---|---|---|
| Project records and registers (task orders, project rows, the directives register) | 36 | Mostly no: the laptop integrates and rules on other boxes' records by design |
| Append-only channels and logs | 8 | No: these are built to take two writers |
| Shared libraries, tools and skills | 7 | Yes, potentially |
| Pipeline and Lambda code | 3 | Yes, potentially |
| Terraform | 3 | Yes: his example |
| Registry or schema | 1 | Yes, potentially |
| Other | 6 | Not classified |

**Two limits on these numbers, and both are findings.**
- **A commit does not say which box made it.** The box was inferred from the author's serial (a lane ending in 1 or 2,
  or named DELL or Z) and, for the 576 worker commits, from where the worker's project is placed today. That is a
  guess a tool should not have to make. The committer field already reads `dell2` on 291 commits and the fabric
  manager's name on 583, so the information exists on some boxes and not others.
- **The laptop sees a box's work only after that box publishes a branch.** Work that is committed but unpublished, or
  not yet committed, is invisible from here.

Andrew's "2300" matches: 2,022 plus 494 merges is 2,516 objects, and the count moves by the minute.

---

## 3. The abstraction: one record, one question

**The record.** Every source below can be reduced to the same seven fields:

```
when | box | seat | project | surface | verb | evidence
```

- **surface** is the thing being touched, named at the coarsest level that still means something: a Terraform folder,
  a Lambda function, a bucket, a shared tool, a registry file, a portal area. A file path is a surface's address, not
  the surface. `infra/aws/terraform/shared-infra/s3-49financial.tf` and `.../s3-lgic-firm-buckets.tf` are one surface.
- **verb** is one of four, in order of how early they warn:

| Verb | Meaning | Already recorded in |
|---|---|---|
| DECLARES | a box has said it will write here | a live task order's `<paths>` block (mandatory, gated) and its `<risk>` class; a fast-drive lease's surface |
| EDITS | a box has committed a change here | git, on the trunk and on each box's published branches |
| HOLDS | a box has a deploy or apply in flight here | the change-management ledger's open entries (18 entry files on the laptop's tree at this read; other boxes' entries are on their own branches) |
| MERGED | the change reached the trunk | git |

**The question.** For each surface: how many boxes have a record on it inside a time window, with which verbs. One box
is normal. Two boxes is the event he is describing.

**The score.** A number per surface per pair of boxes, built from three things the estate already classifies:
- how strong the verbs are (two boxes DECLARING is a warning; two EDITING is a collision forming; one HOLDING a deploy
  while another EDITS is the dangerous case);
- how recent;
- how much the surface matters. This is already indexed: the commit-time danger map scores 1,662 files, every task
  order carries LOCAL, SERVED or WORLD, and shared channels are known to be safe for two writers. A shared log scores
  zero however many boxes write it. A Terraform folder with a live deploy scores at the top.

That is the whole mechanism. It is a join, not a model.

---

## 4. What reads of that table give him

| Use | The read | Who acts |
|---|---|---|
| **Overlap danger** (his example) | surfaces with two or more boxes, ranked by score | the laptop's CTO steps in on the top rows |
| **Figures per box** | per box: lanes live, commits in the last hour, surfaces held, deploys open | Andrew, at a glance |
| **When to merge, pull, push** | for each pair of unmerged branches, a trial merge that writes nothing (`git merge-tree`), giving the predicted conflicts; a window is good when that is zero and no deploy is open on a shared surface | the fabric manager |
| **"Touches only its own fabric"** | rule 32 lets a CTO rule a call that touches only its fabric; the map is what measures that | each box's CTO |
| **A deploy that could upset another box** | his word of ~19:0xZ today; the map says who else is on the folder or resource being deployed | the deploying seat, before it deploys |
| **Where new work should go** | load per box, for the bid that places an inbound job | the fabric manager |
| **His own day in aggregates** | the same records rolled up by directive and project instead of by commit: "D9 moved on three projects, two rounds closed, one deploy" | Andrew |

The last row is the answer to "2300 commits and one person". The unit he reads should be the surface and the project,
never the commit.

---

## 5. How it would be built, cheapest first

**Step 1. A read-only tool on the laptop, run on demand.** It fetches, reads the four sources in section 3, writes the
table, and prints the three reads that matter most: overlap, per-box figures, merge windows. No new cloud resource, no
standing process, nothing that notifies. It is "streaming" only in that it is cheap enough to run every few minutes.
Its blind spot is everything a box has not yet published. Two small changes make it trustworthy:
- every commit carries its box (one line added by the commit tool from the box's own name in the device register);
- a box publishes its work-in-progress branch more often than at cell close (the control-plane project already
  requires publishing at each cell close; this is the same rule, tighter).

**Step 2. Each box reports as it works.** The commit, apply and deploy tools on each box send one record per act to
the laptop over the message bus that already connects the boxes. The laptop keeps the table current to the second. This
removes the publishing blind spot for EDITS and HOLDS. It adds one thing the estate does not have today: a small store
for the records.

**Step 3. A page.** The same table served as a view: a row per box, a row per contested surface, a merge-window
indicator. This is where "figures appearing per box and overlap danger" lives.

**What stepping in would be.** The map does not stop anyone. It gives the laptop's CTO the pair of boxes and the
surface; the CTO rules who holds it, exactly as a cross-fabric call is ruled under rule 32. If Andrew wants the map to
refuse an act (a second box's deploy on a held folder), that is a gate, and a separate decision.

---

## 6. What already exists, so it is not bought twice

| Need | Already in the estate |
|---|---|
| The list of boxes and their names | `org/devices/DEVICES.json`, read through `lib/devices.py` |
| Declared write surfaces | every task order's `<paths>` and `<risk>`; refused when missing by `.tools/to-pipeline-gate.py`; a worker's surface is checked by `.tools/owned-paths-validate.py` |
| Which files are dangerous | the commit-time risk read (`comp-pulse diff`), 1,662 scored files |
| Deploys in flight | `org/critical_paths/.open_deploys/` |
| Which seats are live | `org/mcp/liveness.json` and 192 per-seat telemetry files, per box |
| A trial merge and a refusal on a bad one | `git merge-tree`; `.tools/safe-merge.sh` |
| Box-to-box messages | the agent bus, one queue per box |
| A daily roll-up for Andrew | the `/daily-sprint` skill, which already groups by directive |
| Load per box for placing work | `.tools/remote-job.py`'s bid |

What does NOT exist: the join of these across boxes; a surface vocabulary coarser than a file path; the box on every
commit; any place that holds another box's live state.

---

## 7. What it cannot see, however it is built

- **Edits not yet committed.** Two boxes can both have a file open. Only a declared task order warns of that.
- **Work with no task order.** A fast drive, a CTO's own act, a registry edit by this seat. These appear at EDITS, not
  at DECLARES, so the early warning is missing for them.
- **Cloud changes made outside Terraform.** The cloud graph sees them later; the map would not see them forming.
- **Two boxes meeting through a shared resource rather than a shared file.** One edits a Lambda's code, another its
  role in a different folder. Catching that needs the surface vocabulary to know both files are one resource, which
  the dependency graph can supply and a file comparison cannot.

---

## 8. Calls for Andrew

- **A. Build it?** REC: yes, step 1 now, as an addition to the control-plane project (NFRA_CTLPLN), through a brief.
  It serves rule 32 and his ~19:0xZ word directly, and step 1 costs days and no new infrastructure.
- **B. May it notify, or is it a board the CTO reads?** REC: a board first. His standing rule bars alerts unless he
  asks; a text when two boxes converge on a top-scored surface is worth asking for only after the scores have been
  watched for a week and are not noisy.
- **C. Every commit names its box?** REC: yes. One line from the commit tool. Without it every figure per box is a
  guess, as section 2 shows.
- **D. Should it ever refuse an act?** REC: not at first. A refusal of a second box's deploy on a folder another box
  holds is the one worth considering later; it is a gate and needs its own word.

---

## 9. Not measured

- Nothing on dell1, dell2 or site Z was read directly; all figures are from branches visible on the laptop.
- How stale a box's published branch is against its working tree.
- Whether the 14 code and infrastructure files touched by two boxes today produced a real conflict. The count is
  proximity, not harm.
- The box attribution in section 2 is inferred from serials and project placement; several projects changed box today.
- The message bus's capacity for a record per commit.
- Reproduce: `git log --all --since=2026-10-07T04:00:00Z --no-merges --name-only`, grouped by box and file.
