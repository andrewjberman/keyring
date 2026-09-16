---
name: outcome-check
description: Step-by-step OUTCOME REPORT of what a fabric actually delivered on one project over a time window, published as an Artifact page -- an honest headline, a timeline diagram, numbered outcomes with evidence, a standard-technical-English breakdown (before/after, still open, where the effort went) and the cloud resources touched. Every figure is measured at run time from git, live endpoint calls, AWS and CI, never taken from status prose. `/outcome-check <PROJECT_CODE>`; `--since <session|ISO time|commit>`; `--until <ISO time>`; `--update <artifact url>`. Read-only apart from the publish. Any Tier-1 seat or MSTR.
---

# /outcome-check -- what actually got delivered, measured, on one page

**Authority (Andrew-direct, 2026-09-16, at the `1.0.0_SA_CTO~Z` terminal, VERBATIM).** ~20:2xZ: *"I need to understand how much
your fabric has actually accomplished since the start of the session on the AMGT_RESAPP project. Please use /artifacts to
create a step by step sequence of outcomes with a high level headline, image/diagram block if possible, then two subsections
one providing Standard technical english breakdown of what was achieved, the other describing what resources in the cloud were
involved. if i like what I see, i will make this query/response form into a skill called /outcome-check."* Then, ~20:3xZ, after
seeing the page: *"need this as a skill"*. Typos are his. **The accepted first run** is
https://claude.ai/artifact/XejZL8TRwE2irTUHUCWmGP (AMGT_RESAPP, 9:33 AM to 4:16 PM ET); its HTML is `template.html` in this folder.

**The one question it answers:** *how much has actually been accomplished on this project in this window?* An OUTCOME is a
change in what the product does or where it lives, with the instrument that shows it. It is not a stage (`/exec-sum`), not a
PRD-coverage percentage (`/prd-delta`), and not commit activity (`/activity-check`). Records, logs, criteria repairs and merges
are the COST of outcomes; they appear in the effort mix and never as outcomes.

## Invocation

| form | behavior |
|---|---|
| `/outcome-check <CODE>` | window = this session (see Step 1), measure, write the page, publish, report |
| `/outcome-check <CODE> --since <ISO time or commit>` | explicit window start; `--until <ISO time>` bounds the end (default now) |
| `/outcome-check <CODE> --update <artifact url>` | same measurement, republished to that URL (read it first, per the Artifact tool) |

## Step 0 -- Load the page contract, then open the template

Load the `artifact-design` skill before writing. Then start from `template.html` in this folder and **keep its form**: tokens
(light and dark), IBM Plex type, section order, fact row, three-lane timeline, step list, tables, effort bars, method footer.
Replace every word and number; the template's AMGT_RESAPP content is an example, never a default. **Do not redesign per run --
the form is what Andrew approved.** Change the layout only when a block has no data (Step 3 says how each block degrades).

## Step 1 -- Resolve the project and the window

- **Project:** `org/missions/D*/*/<CODE>/project.json` (fabric, status, `dep_stage`). Not found -> print `NOT FOUND` and stop.
  Placed on the other fabric -> say so; measure git only and mark every live-plane block `not measured: other fabric`.
- **Window start:** `--since`, else `session` = this seat's own session start (its first registration or its relaunch record in
  this session). State on the page how the start was resolved. **End:** `--until`, else now.
- **Base commit:** `git rev-list -1 --before=<start> HEAD`. **Timezone:** every time on the page is US Eastern; the evidence
  packet may keep UTC.

## Step 2 -- Measure: the evidence packet

Collect all of it before writing a word. Keep the raw outputs in the scratchpad (`outcome-check_<CODE>_packet.txt`).

**2a. Git census.** `git log --since=<start> --until=<end> --format='%h|%cI|%an|%s'`. Count by author. Classify by subject
prefix: `drain` = branch merges; `fix(<CODE> round N, 2.0.0_SA_COO...)` = acceptance-test repairs; `L7(` / `prove(` /
`row+proof(` / worker `fix(` or `docs(` = worker builds and proofs; `log(` = session logs; `audit(` = product-existence audits;
`record(` `register(` `row(` `co-sign` `sign(` `surprise(` = rulings, sign-offs, records; `ledger(` `issue(` `chore(` = the rest.
**Code paths** = the union of the project's order `<paths>` minus `org/` and `docs/`: count commits touching them, run
`git diff --shortstat <base> HEAD -- <code paths>` and list the files. Portal code named by the orders is counted in the portal
repo on its branch, separately.

**2b. Work orders.** For every `<CODE>.TO-*.md`: status. For each `complete`, the flip commit
(`git log -S'<status>complete</status>' --format='%h %cI %an' -- <order>`) and the drain that landed it on the shared branch.
Completed-in-window vs before-window are separate counts. **The outcome sentence comes from the drain body and the proof
instance, quoted as measured -- never from the order's title.**

**2c. The served plane, live.** For each deployed function the project serves through (from the PRD surface manifest, the
orders, and the change records): `get_function_configuration` (code sha, size, LastModified, memory, timeout, layers, env
keys); `list_object_versions` on its artifact key, filtered to the window; its role's inline policy, counted per limb; **the
route table read from the source of truth (the adapter's own route-table function or the Terraform locals), never typed**;
then a GET-only invoke of every GET route with a real key, printing status, body bytes and the one field that shows real
content (for AMGT, `model_status` and `header_figures`). Data stores the orders write: object counts per prefix with
`LastModified >= start`, and generation markers where the project has them. Schedules are read by name; if the read does not
find one, the page cites who measured it instead.

**2d. Change records.** `org/critical_paths/change_management/` entries opened in the window: status and legs. **A route that
went from 200 to anything else inside the window is a STEP, with its duration.** So is its rollback, and so is its restore.

**2e. Pushes and CI.** `git ls-remote` for every branch the window moved (workspace and portal). `gh run list --branch <b>` for
each pushed head. **A red run is compared with the previous run on the same branch (failing step, and the error set by file)
BEFORE it is attributed to the window's work**; the page says `pre-existing, same N errors` or `new`.

**2f. Baseline (the Before column).** The earliest in-window measurement of each figure -- an audit, a tick log, a change
record's pre-census -- with its time and source named in the footer. A figure with no in-window baseline reads `not measured at
start`; it is never reconstructed from memory.

**2g. Decisions.** Andrew-direct records committed in the window (`deliverables/ANDREW_DIRECT_<date>_*`) are steps, quoted
briefly in plain words.

**2h. Still open.** Pending orders (in plain words, not slugs); approved-but-unrun acts; independent grading state (slug,
adjudication, completion report present or not); **user reachability -- is the surface on a plane a person can open, or only
on a branch or a CI-only DEV?**; red CI; unmerged branches and pending merges.

## Step 3 -- Write the page, block by block

1. **Eyebrow:** `Outcome check · <CODE> · <fabric>`.
2. **Headline (h1):** one or two sentences carrying **the biggest measured gain AND the biggest gap between the build and a
   user.** Never a stage label, never a count of commits.
3. **Lede:** the date, the window in ET, and that every figure was measured at the end time rather than taken from reports.
4. **Fact row, exactly four:** orders closed in the window (with the overall count); live reads answering normally (name the
   failing one); the headline product figure (with its before); code and data lines changed (with files). No section may
   contradict a fact.
5. **Timeline (inline SVG, in the overflow container, `min-width:700px`):** three lanes -- *Delivered* (green markers),
   *Live system* (red regression, amber rollback, green restore, and a translucent red band across any outage labelled with
   its duration), *Decisions and pushes* (accent). Markers carry the step numbers. Geometry: the axis runs from the hour
   boundary before the start to the one after the end; `x = x0 + minutes_since_axis_start * scale`; markers `r=8`; any two
   markers closer than 16 px stagger vertically by 9 px; hour gridlines; a start label and a dashed `measured <time>` line.
   **No deployed surface:** keep the lane and write `no deployed surface` in it.
6. **Sequence of outcomes:** numbered, chronological by the time each landed on the shared branch or the live system. Each
   step: time (ET), a badge coloured by kind, a plain-words title, one or two sentences carrying the measured figure, and an
   evidence line (order id, commit hashes, record ids, CI run id). Regressions, rollbacks and approvals are steps. **Work
   produced before the window and proved inside it says so** ("written before the reboot; this session re-proved it").
7. **What was achieved -- standard technical English.** Two or three paragraphs: the product gain, any setback and its
   recovery, then frontend, library and data. **No fabric vocabulary in this section**: no limb names, serials, criterion
   ids, cells, rows or order slugs -- say "work order", "acceptance test", "deploy", "rollback". Then three sub-blocks:
   *Before and after* (table, the Step 2f baseline), *Still open* (the 2h list), *Where the effort went* (commit-mix bars,
   one sentence stating `N of M commits changed application code; K repaired acceptance tests`, and the by-seat counts).
8. **Cloud resources involved:** table `Resource | Service | This session | State now`, pill per row (`changed N times`,
   `written`, `pushed`, `read only`). Every AWS and GitHub resource the window changed, wrote, read or pushed to, including CI.
   Then *Approved but not yet used* and *Referenced, unchanged*.
9. **Method footer:** the instruments, every denominator, the baseline's source, the timezone.

**A window with no commits** is a one-line page: the headline `Nothing landed on <CODE> between <start> and <end>`, the method
footer, nothing else.

## Step 4 -- Publish and report

- Write `outcome-check_<CODE>_<YYYYMMDD>.html` in the scratchpad. Publish with the Artifact tool: favicon `🧭` and icon `report`
  on a first publish, a one-sentence description naming the project, window and measurement. `--update <url>` republishes there.
- On this box the Playwright MCP blocks `file://`, so a local preview is not available; the published page is the review
  surface. Do not build a screenshot loop.
- **Terminal reply:** the URL, then three to five bullets -- the gain, the gap, the setback if any, and anything the measurement
  surfaced that no seat had reported. Nothing else.

## Rules

- **Measure, never recollect.** A figure without an instrument is not on the page.
- **Produced is not proved.** A write whose timestamp predates the window is not a window outcome; its acceptance is.
- **Nothing is smoothed.** A regression, a rollback and a red CI run are all on the page, each attributed only after comparison
  with the prior state.
- **Process is not product.** Logs, records, repairs and merges are counted in the effort mix, never listed as outcomes.
- **Read-only.** No commits, messages, deploys, pushes or task orders. The only writes are the scratchpad files and the publish.
- **COST:** roughly 15 to 25 tool calls. **NON-APPLICATION:** a project with no deployed surface keeps the Live-system lane and the
  cloud table and says so in them; it does not drop them.
