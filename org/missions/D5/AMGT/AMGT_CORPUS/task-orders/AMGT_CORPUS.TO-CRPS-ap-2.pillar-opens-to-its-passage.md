# AMGT_CORPUS task order -- `CRPS-ap-2` -- ROUND 40: FWD-10 -- a team pillar opens to the report and the passage it came from

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check renders one component on a hand-built dossier.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV ba391aff -- page_check ap2 build 0/1 control 1/1. Blind spot: static markup only; the reading on the page is AC2.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 40.

**Your portal.** The nested `portal/` repository in your worktree, on its own portal branch based on origin/DEV `ba391aff`. Portal files commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit the portal gitlink. `portal/node_modules` is a LINK to a tree that already holds the dependencies: NEVER run `bun install` (site rule: a registry fetch is egress). If `bun run typecheck` cannot run because the link is missing, say so in your report and go on; the issuer typechecks at the drain. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas and white panels; reuse the classes already in the file.

## 1. THE CELL -- `CRPS-ap-2`

Outcome FWD-10: an analyst reads the TEAM'S OWN thesis pillars on the Thesis tab, "each openable to the report and the passage it
came from, and each marked as the team's rather than generated".

`portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx`, `ResearchTeamPillars` (about lines 111-175), renders each served pillar as
a bold lead, its paragraph, a "Terms:" line and a "Source: <report file name>" line. The served pillar already carries its
citation (`DossierPillar.citation`, `../types.ts`: `report_key`, `report_id`, `locator`, `passage`), but the page puts `report_key`
and `locator` in data attributes only and never shows the passage. Nothing on the page opens a pillar.

**Build, in `ThesisTab.tsx` only:**
1. Inside each pillar's `<li data-dossier-pillar>`, when its citation carries a `passage`, add a native `<details
   data-pillar-open>` (closed at rest, no JS state). Its summary is plain words (for example "Where this comes from"). Opened, it
   shows: the report's file name (as now, never the `s3://` key in visible text); an element with `data-pillar-locator` reading the
   locator in words (a number from a docx is a paragraph, from a pdf a page; if you cannot tell, say "location <n>"); and a
   `<blockquote data-pillar-passage>` with the served passage, exactly as served. `components/ThesisCards.tsx` (`TeamCaseBlock`,
   about 134-161) is the page's existing pattern for a cited team passage: match its look.
2. A pillar whose citation has no passage gets NO `<details data-pillar-open>`; it keeps the Source line and carries one element
   with `data-pillar-passage="NOT_SERVED"` reading, in plain words, that the passage is not in this security's data.
3. Everything the section renders today stays: `data-dossier-pillars`, the heading, the lead, the paragraph, the Terms line, the
   Source line, the two existing data attributes, and the three not-served branches.

## 2. BOUNDS

1. Do NOT arm the walker or run `.claude/skills/ui-walk/walk.mjs`. You MAY render with `portal/scripts/ui-smoke.mjs` (auth-stubbed) to look at your change.
2. No new served field, no new route, no edit to `types.ts`, and no edit to any `__harness__/` file.
3. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
4. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
5. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
6. Rows are `AMGT_CORPUS-Z-W4-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-ap-2.pillar-opens-to-its-passage.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-2.pillar-opens-to-its-passage.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx` and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs" ap2 portal</invocation><expect>(?m)^ap2 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-2" judgment="true"/>
</proof_of_spec>

- AC1 (the real `ResearchTeamPillars`, rendered to static markup on two hand-built pillars): build -- the pillar with a passage
  carries the opener with its passage and locator, the pillar without one carries no opener and the NOT_SERVED mark; control --
  the section, both pillars' lead and text, the Terms line and the not-carried branch are unchanged.
- AC2 (JUDGMENT, graded by the CVO at L9 on the issuer's real walk of IMB LN): a reader can tell the pillar is the team's and can
  reach the sentence it came from.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck` (clean) if the link allows it, and `node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs`;
   report each one's last line. If a harness line that passed before your change now fails, fix your change, not the harness.
2. Write the instance at the proof path, with its mutant control from the start. Record the judgment criterion as
   `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict. Then run `python
   .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change and why, AC1's output lines, the typecheck and harness lines, your portal and outer commit hashes, the
   portal branch name, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 7 + s.4 item 2. Base portal origin/DEV `ba391aff`: ap2 build 0/1 control 1/1. No control opens the report DOCUMENT (no route by report key exists); the cell shows the passage and names the report. Candidate to the CTO's render review.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~4</slot>
<fabric>site-z</fabric>
