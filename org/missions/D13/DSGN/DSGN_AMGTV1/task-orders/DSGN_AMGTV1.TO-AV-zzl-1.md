# DSGN_AMGTV1 task order -- `AV-zzl-1` -- THE ROUND-59 REPAIRS, BATCHED, WITH THE BATTERY RE-ANCHORED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~130</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal 3ea5d0f9 (= origin DEV, round 59) -- r60.cjs 1 of 7 (arms 1-6 FAIL as expected, PLANTED passes); battery29 FAIL as expected: ALL BOUND 7 of 14 harnesses (red: tabs, shell, execFallback, execText, modelPattern 11 of 12, posturePattern, thesisLadder) and three checks red (round24 posturezero 1 of 3, round23 postureharness 2 of 3, round20 namecard 2 of 3); tsc and eslint rc=0.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzl-1` (round 60, decomposition v60; one batched repair cell; serves FWD-27 and the layout outcomes)

Round 59 redesigned /security-analysis from Andrew's walk (register `docs/briefs/dsgn-amgtv1-security-analysis-walk-findings-20261009.json`):
a News tab, one news surface, absences said once, the tabs in the first screen. This cell is its repair list
(`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round59.md` section 3). Paths are under `portal/src/pages/SecurityAnalysis/`. Do the items in this order.

1. **The spine's day detail drops collection bookkeeping** (`components/TimelinePanel.tsx`: the day-dialog search notes
   `searchedLine`/`foundLine` and the empty-day caption). Remove "Searched: ...", "Not searched on this day" and any "had no search run"
   wording. The day detail keeps the day's articles and events. An empty day says "No articles on this day" once.
2. **The News tab opens ten items at rest** (`components/HeaderBrief.tsx`): set `FEED_OPEN_AT_REST = 10` and stop capping it with
   `HEADER_FEED_VISIBLE_COUNT` (the rest stay behind "Expand (N more)").
3. **The description once, in the header.** In `components/SecurityOverlay.tsx`, the identity header draws ONE short description line
   (the served `top_band.description_line` if present, else the first sentence of the served description), on an element carrying
   `data-identity-description`. `components/HeaderBrief.tsx` stops drawing "About the company" (the News tab keeps no copy).
4. **The mixed-currency reason** (`tabs/PeersTab.tsx`): when the Average row's price cell is empty because the peers' currencies differ,
   one line inside the existing "What is not on file" fold (`data-absence-fold`) says so, on an element carrying `data-mixed-currency`.
5. **What changed in display units** (`components/model/WhatChangedPanel.tsx`): export `displayAmount(value: number, unit: string | null)`.
   It prints a value in display units; a value whose served unit is `millions` is multiplied by 1e6 first. `displayAmount(1060161.94,
   'millions')` reads `1.06T` and `displayAmount(12276538360, null)` reads `12.28B` (two decimals, `K`/`M`/`B`/`T`). Use it for every
   Before/After/Change amount, so no row prints raw millions such as `1,060,161.94`. Ratios and percentages keep today's form.
6. **One as-of per card** (`components/model/WhatChangedPanel.tsx`): the What-changed panel sits inside the Model card, which has its own
   footer. Remove the panel's own `CardFooter`.
7. **Re-anchor the battery** (LAST, on the final markup). Run battery29 (AC2). For each red harness or check, re-anchor the ONE assertion
   that reads markup round 59 or this cell moved, folded or removed. Point it at the same fact as the page now states it (the words, a data
   attribute, or the new location such as the News tab or a `data-absence-fold`). Keep its claim; never drop or weaken a check; keep each
   harness at or above its base check count. Record every re-anchor (file, old anchor -> new anchor) in the instance.
   Red at the base: `__harness__/` tabs, shell, execFallback, execText, modelPattern, posturePattern, thesisLadder; and the issuer checks
   `round24/checks/posturezero.cjs`, `round23/checks/postureharness.cjs`, `round20/checks/namecard.cjs` (under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/`).

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text.** `reasonWords.ts` is not yours. No non-ASCII characters (use `--`). Keep each file's
   line endings as you find them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/checks/posturezero.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/postureharness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round20/checks/namecard.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~130/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the register, `portal/src/pages/SecurityAnalysis/types.ts`, `portal/src/pages/SecurityAnalysis/topBandTypes.ts`, the other battery29 checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round60/checks/r60.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzl-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round60/checks/r60.cjs"; echo "exit=$?"</invocation><expect>ROUND 60 REPAIRS: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzl-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzl-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): the six page repairs read as section 1 says, and
no re-anchor weakened a claim.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~130/DSGN_AMGTV1.TO-AV-zzl-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-60 close walk"; the re-anchor table in it). **Flip this order's
`<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W130-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), every re-anchor, the output line of every criterion, the portal and outer commit
hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 60 = `ledger/ROUND_ANALYSIS.round59.md` @3ce363b8b2 section 3, items 1-7, batched as ONE repair cell (obligation
1: repairs batched). Item 2 ("one as-of per card") is read as no card carrying a second footer inside it: the What-changed panel in the
Model card. Rulings carried from the round-59 close: W126-S1 (the description line goes back to the header; the News tab keeps no copy)
and W128-S1 (the mixed-currency line goes in the Peers fold). Issuer checks granted for re-anchor: three of `2.0.0_SA_COO~D`'s round20-24
checks. This seat has been the project's issuer since the move; site Z's COO~D is stood down. Base portal 3ea5d0f9 (= origin DEV).

<status>pending</status>
<round>60</round>
<to_id>DSGN_AMGTV1.TO-AV-zzl-1</to_id>
<slot>~130</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
