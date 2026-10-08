# Push activity across the repos, and a lighter "microproduct" policy (4.0.0_SA_CRO~A, 2026-10-08 ~20:4xZ)

**Asked by:** Andrew-direct ~20:2xZ to ~20:3xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_202xZ_PORTAL_OPAL_AI_BOX_BRANCHES.md`: box branches for
the portal into `DEV`? opal_ai organized in advance; "study the push activity ... design a solution that is realistic for
the level of activity"; "maybe we have a "microproduct" policy that isnt as advanced/cumbersome as the monolith".
**Method (MEASURED):** git data only, no GitHub API. The laptop's fetched remotes for `ajb_workspace` and `portal`;
metadata-only clones (`--filter=blob:none`, no checkout) of `opal_ai` and `mcportal`. Window: the 7 days to
2026-10-08 ~20:2xZ. "Landings" = first-parent commits on the trunk (each is one direct commit or one merge that landed).
Box per commit is INFERRED from the author's lane suffix.
**Correction:** opal_ai and mcportal are NOT initialized on the laptop (empty folders). A first read through those folders
silently answered for the workspace itself; it is discarded, and the clones above replace it.

## 1. What the repos actually carry

| Repo | Trunk | Landings, 7 d | Per day (range) | Busiest hour | Hours with any landing | Commits, 7 d | Authors | Branches moved, 7 d |
|---|---|---|---|---|---|---|---|---|
| ajb_workspace (the monolith) | CLOUD | **2,718** (421 merges) | 10 to 672 | 72 | 151 of 168 | 9,526 | 562 | 179 of 205 |
| portal | DEV | **160** (25 merges) | 4 to 71 | 13 | 59 of 168 | 412 | 84 | 20 of 30 |
| portal | PROD | 12 | -- | -- | -- | -- | -- | -- |
| opal_ai | DEV | **4** | 0 to 2 | 1 | 4 of 168 | 4 | 4 | 2 of 2 (DEV = PROD) |
| mcportal | DEV | **0** | 0 | 0 | 0 | 0 (1 commit ever) | 0 | 0 of 2 |

- **Scale:** the portal carries about 1/17 of the monolith's landings, opal_ai about 1/680, and mcportal is dormant.
  Andrew's "over 2200 commits ... in less than a day" is the monolith's commit count (all commits, not landings).
  This measure shows a busiest day of 672 landings, 2026-10-07.
- **Who writes the portal:** ~90% of its commits carry laptop-style serials (372 of 412). Site Z 14, dell1 12, dell2 14
  (INFERRED). The Dells already deliver through per-round candidate branches (`cand-dell1-*`,
  `q/dell2/wk-*-portal/r1`), which the laptop lands.
- **The portal's CI runs only on a push to `DEV`** (`.github/workflows/ci.yml`); its deploy only on `PROD`
  (`deploy.yml`). `promote-to-prod.yml` is manual. A push to any other branch costs no Actions minutes.

## 2. The microproduct policy (portal, opal_ai, mcportal) -- ADOPTED

**Andrew-direct 2026-10-08 ~22:4xZ, laptop terminal, VERBATIM:** "yes to the microproduct policy"

**No box branches for the microproducts.** At ~23 landings a day and 13 in the busiest hour, the portal's push races are
occasional and a retry is cheap. Box branches would add an integrator, a schedule and a merge per pass. That is cost
without a measured problem. The monolith's machinery exists because of 2,718 landings a week.

1. **One trunk per microproduct: `DEV`.** A seat lands a change on `DEV` itself, as today: fetch, merge, then push, never
   rebase. A rejected push is a fetch and retry. No integrator, no slots.
2. **`PROD` unchanged:** promoted from `DEV` only by `/prod-deploy` (the DT path), client-facing, as today.
3. **Other boxes deliver through short-lived candidate branches**, exactly as the Dells do now (`cand-*`, `q/<box>/...`).
   **Each is deleted once it has landed:** 18 non-trunk portal branches moved this week, and the stale ones should not
   pile up the way the workspace's 159 `q/*` did.
4. **THE ONE RULE THAT TOUCHES THE MONOLITH: only the integrator moves the workspace's pointers to the microproducts**
   (the `portal`, `opal_ai` and `mcportal` submodule pointers in `CLOUD`). Under box branches, two boxes that each bump
   the portal pointer collide at every integration. The same multi-writer pattern is already producing real holds
   (section 3). The integrator sets each pointer to its repo's published `DEV` tip once per pass;
   `gitlink-publication-check.sh` already refuses an unpublished pointer.
5. **opal_ai and mcportal:** the same policy now, nothing to build. Initialize them on a box only when that box works
   on them.
6. **When a microproduct graduates to box branches:** when its own push contention shows up in a record. Today nothing
   records a rejected push to `DEV`. Start by logging them, the way `MERGE-ATTEMPT` rows now log merges, and graduate a
   repo when those rows show seats retrying regularly. No number is set here, because none is measured yet.

## 3. What the first scheduled monolith run taught, the same hour

The task's first run (20:30Z) merged dell1, dell2 and site Z into `CLOUD` (`26489d99e8`, 212 s, no worktree). It HELD the
laptop's box pass on one file. Both holds so far are files written by MORE THAN ONE BOX:

| Hold | File | Two writers |
|---|---|---|
| site Z (19:4xZ) | `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` | two boxes appended rows to one JSON list |
| laptop (20:33Z) | `org/projects/NFRA_TRNSPT.json` | a generated row regenerated on two boxes (`2.0.0_SA_COO~R` f33361047f; `0.0.0_AB_MSTR` 4224e17575) |

**The monolith's remaining merge friction is now multi-writer files, not merge mechanics.** The durable fix is brief
outcome O6: one writer per file class. Channel rows go to a file per writer (or a row-aware merge). Generated files are
regenerated only by the integrator, never committed from a box. Microproduct pointers are rule 4 above.

## 4. Not measured

- Rejected pushes: no record exists, in any repo.
- Box attribution comes from lane suffixes; a laptop-style serial can run on another box.
- The portal's `DEV` CI duration and the Actions minutes it uses: not read (the GitHub API needs Andrew's word).

## 5. Adoption and what implements each rule (4.0.0_SA_CRO~A, ~22:4xZ)

| Rule | Implemented by |
|---|---|
| 1. One trunk per microproduct, `DEV`; land, fetch-merge-push on rejection, never rebase | today's practice; `/integrate` "MICROPRODUCTS" names it |
| 2. `PROD` only via `/prod-deploy` | unchanged (`.claude/skills/prod-deploy/SKILL.md`) |
| 3. Candidate branches deleted once landed | the seat that lands a candidate deletes it in the same act; `/integrate` "MICROPRODUCTS" |
| 4. Only the integrator moves the workspace's pointers to the microproducts | NO NEW CODE, MEASURED: `git merge-tree` (which box-sync and the safe-merge fast lane use) already takes the DESCENDANT pointer when one box's pointer descends from the other's (fixture 2026-10-08 ~22:5xZ: S1 vs S2 -> S2, rc 0); two DIVERGED pointers are a real conflict and the box is HELD for a person. Moving a pointer stays a deliberate commit (for example `/prod-deploy`'s step), never a side effect |
| 5. opal_ai and mcportal: same policy, nothing built | -- |
| 6. Graduation when push contention shows in a record | no record of rejected pushes exists yet; deferred, owner 4.0.0_SA_CRO~A |
