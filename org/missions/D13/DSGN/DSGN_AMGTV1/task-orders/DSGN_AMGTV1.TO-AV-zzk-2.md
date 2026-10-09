# DSGN_AMGTV1 task order -- `AV-zzk-2` -- ONE NEWS SURFACE, EACH HEADLINE ONCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzk-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~125</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files only.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) at the cut on DELL1 against portal c0c6f570 (= origin DEV) -- r59.cjs B: every build arm FAILS at the base and the PLANTED arm PASSES (the graders refuse the base form and admit a clean form); hyg59.sh PASS (tsc rc=0, eslint rc=0).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzk-2` (round 59, decomposition v59; serves FWD-27 and the layout outcomes)

**Why.** Andrew walked /security-analysis on 2026-10-09 and called it ugly: the news spine "makes no sense", the news is "the worst part
... a shit ton of information laying around everywhere haphazardly", and the page is full of "verbose and redundant disclaimers". The
findings register is `docs/briefs/dsgn-amgtv1-security-analysis-walk-findings-20261009.json` (read your SAW ids there: `observed` and `acceptance`). The CTO's rulings
(`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round58.md`, R2-R5): say each thing once; move and fold, never reword served text.
Paths below are under `portal/src/pages/SecurityAnalysis/`.

Your findings: **SAW-05, SAW-07, SAW-09** (SAW-06's relevance ranking waits on a served field; not yours). Owned:
`components/HeaderBrief.tsx`, `components/TopBand.tsx`.

1. **One news surface.** `HeaderBrief.tsx` becomes THE news surface: its root carries `data-news-surface`. It takes the "In the news" items
   (the served `top_band.items`, which carry `mentions`; pass them in as a prop) and the feed items, and draws ONE list:
   - first the top-band items in descending served `mentions` (they are the day's most-mentioned stories), then the feed items in served
     order;
   - each headline ONCE: de-duplicate by `url`, else by `title` (a `Set` of seen keys);
   - "Mentioned N times" shows as a small count beside an item that has served `mentions`.
2. **The range matches the items.** The header range reads from the earliest to the latest `published` day of the items actually listed
   (house long dates), not the served window when they differ.
3. **TopBand.tsx stops drawing a news card.** Remove the "In the news on <day>" block, its item list and its "no social source is admitted yet"
   line from `TopBand.tsx` (leave `CompanyLine` exported; another cell decides its mount). The card's mount line in `SecurityAnalysis.tsx` is
   cell AV-zzk-3's.
4. No why-line or relevance ranking: those wait on served fields (RESAPP asks).
Export what the news tab will mount (cell AV-zzk-3 mounts `HeaderBrief` with the props it needs); name any new prop in your report.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Five sibling cells (A-F) edit other files of
   this page at the same time. Do not touch a file you do not own, even to fix an import; if you need a change outside your paths, file a
   row and stop on that criterion.
3. **Move and remove, never reword served text.** The page may stop printing a served sentence, print it once, or fold it into a
   `<details>`. It never rewrites the words of a served field. `reasonWords.ts` is not yours to edit.
4. Use the estate's own components (`PanelEmpty` and the others in `@/ui/components/states`, the page's `<details>` pattern), not new
   ones. No non-ASCII characters in code or text (use `--`, not a dash glyph). Keep each file's line endings exactly as you find them
   (read them first, e.g. `python -c "print(open(p,'rb').read().count(b'\r\n'))"`). Edit tool for existing files, Write for new ones.
5. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
6. The page's battery29 harnesses (`__harness__/`) are anchored on markup some cells remove. Their re-anchor is the round's batched repair
   cell, cut after A-F merge. Do not edit `__harness__/`, and do not run battery29 as a criterion.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/TopBand.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~125/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `docs/briefs/dsgn-amgtv1-security-analysis-walk-findings-20261009.json`, `portal/src/pages/SecurityAnalysis/types.ts`, `portal/src/pages/SecurityAnalysis/reasonWords.ts`, `portal/DESIGN.md`, and the issuer's
checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round59/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzk-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round59/checks/r59.cjs" B; echo "exit=$?"</invocation><expect>ROUND 59 CELL B: every arm PASS -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzk-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round59/checks/hyg59.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>HYG59: PASS -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzk-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round's close on the issuer's signed-in walk against the register (never self-graded): your SAW findings
read as their `acceptance` lines say.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~125/DSGN_AMGTV1.TO-AV-zzk-2.proof_of_spec.json`
(AC3 recorded as UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-59 close walk"). **Flip this order's `<status>` to `complete`
in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W125-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 59 = `ledger/ROUND_ANALYSIS.round58.md` @23fec8836a (cells A-F as the cut plan
`deliverables/2.0.0_SA_COO~D1/round59/ROUND59_CUT_PLAN.md` @f37fb3dc95, R2-R5 applied). This cell: SAW-05, 07, 09 (06 waits on a served relevance field). Base portal c0c6f570.
Check r59.cjs is a source-level floor; the round closes on a signed-in walk against the register (23 of 23 dispositioned).

<status>complete</status>
<round>59</round>
<to_id>DSGN_AMGTV1.TO-AV-zzk-2</to_id>
<slot>~125</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
