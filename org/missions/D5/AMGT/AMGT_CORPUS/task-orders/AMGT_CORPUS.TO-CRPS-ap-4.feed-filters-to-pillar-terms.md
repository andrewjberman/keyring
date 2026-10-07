# AMGT_CORPUS task order -- `CRPS-ap-4` -- ROUND 40: FWD-18 -- the header feed filters to a pillar's terms

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check renders one component on a hand-built feed.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV ba391aff -- page_check ap4 build 0/1 control 1/1. Blind spot: static markup only; the reading on the page is AC2.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`**, slot `~5` of round 40, continuing in the same worktree and on the same portal branch after `CRPS-ap-3`.

**Your portal.** The nested `portal/` repository in your worktree, on its own portal branch based on origin/DEV `ba391aff`. Portal files commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit the portal gitlink. `portal/node_modules` is a LINK to a tree that already holds the dependencies: NEVER run `bun install` (site rule: a registry fetch is egress). If `bun run typecheck` cannot run because the link is missing, say so in your report and go on; the issuer typechecks at the drain. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas and white panels; reuse the classes already in the file.

## 1. THE CELL -- `CRPS-ap-4`

Outcome FWD-18: "a pillar's terms are readable on the page and the feed filters to them for at least one name."

The terms are already readable: each team pillar on the Thesis tab prints "Terms: ..." from the served `DossierPillar.terms`. The
feed does not filter. `portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx`, `FeedList` (about lines 106-152), lists the
served news items (`CoverageItem`: `article_key`, `title`, `url`, `publisher`, `published_at`), one open at rest and the rest
under a native `<details data-feed-expand>`. A feed item carries no term field, so the filter matches on the item's TITLE.

**Build:**
1. `FeedList` takes an optional `terms?: string[]`. For each distinct non-empty term, in the order given, it renders after the
   list a native `<details data-feed-term="<term>" data-feed-term-count="<k>">` (closed at rest, no JS state). k is the number of
   feed items whose `title` contains the term, case-insensitively. Its summary reads the term and the count in plain words (for
   example `pricing power -- 2 of 4 headlines`). Opened, it lists exactly those items through the existing `FeedItemRow`. A term
   that matches nothing reads count 0, lists nothing, and says in words that no headline in the window names it.
2. Put the terms under one small heading that says whose they are (the research team's thesis terms) so the reader knows the
   filter is by the team's own words.
3. With no `terms` (undefined or empty) `FeedList` renders exactly what it renders today, byte for byte.
4. `HeaderBrief` takes an optional `pillarTerms?: string[]` and hands it to `FeedList`. In
   `components/SecurityOverlay.tsx`, the ONE mount line (`<HeaderBrief bundle={bundle} />`, about line 460) passes the distinct
   terms of the served pillars: `thesis.data?.dossier_fields?.thesis_pillars` (each `terms`), already read in that component
   through `useThesisBundle`. Change nothing else in that file.

## 2. BOUNDS

1. Do NOT arm the walker or run `.claude/skills/ui-walk/walk.mjs`. You MAY render with `portal/scripts/ui-smoke.mjs` (auth-stubbed).
2. No new served field, no new route, no edit to `types.ts`, `TimelinePanel.tsx`, `TimelineWordCloud.tsx` or any `__harness__/` file. The Chatter axis half of the outcome is not in this cell.
3. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
4. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
5. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
6. Rows are `AMGT_CORPUS-Z-W5-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-ap-4.feed-filters-to-pillar-terms.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-4.feed-filters-to-pillar-terms.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md` and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs` with `ap4_base_snapshot.json` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs" ap4 portal</invocation><expect>(?m)^ap4 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs" ap3 portal</invocation><expect>(?m)^ap3 build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ap-4" judgment="true"/>
</proof_of_spec>

- AC1 (the real `FeedList`, rendered to static markup on four hand-built headlines and three terms): build -- one term block per
  term with its count and exactly its matching items; control -- with no terms the markup is byte-equal to the base snapshot.
- AC2 (control on the file you share with `CRPS-ap-3`): the header dossier line and the machine's posture line still read as ap-3
  left them.
- AC3 (JUDGMENT, graded by the CVO at L9 on the issuer's real walk of one name with pillar terms): a theme the team named is
  followable into the news.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck` (clean) if the link allows it, and `node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs`;
   report each one's last line. If a harness line that passed before your change now fails, fix your change, not the harness.
2. Write the instance at the proof path, with its mutant control from the start. Record the judgment criterion as
   `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict. Then run `python
   .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change and why, AC1's output lines, the typecheck and harness lines, your portal and outer commit hashes, the
   portal branch name, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 7 + s.4 item 2. Base portal origin/DEV `ba391aff`: ap4 build 0/1 control 1/1. Queued behind ap-3 on slot ~5 (the mount line is in ap-3's file). Title match only: a feed item serves no term field. The Chatter axis half of FWD-18 is named NOT COVERED in the packet. Candidate to the CTO's render review.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~5</slot>
<fabric>site-z</fabric>
