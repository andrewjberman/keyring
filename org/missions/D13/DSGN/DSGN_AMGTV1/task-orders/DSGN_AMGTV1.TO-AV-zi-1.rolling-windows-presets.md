# DSGN_AMGTV1 task order -- `AV-zi-1` -- ROLLING WINDOWS: A PM PICKS THE LAST 30, 90 OR 365 DAYS ON CHATTER AND PRICE, AND READS WHICH WINDOW IS SHOWN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zi-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~88</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from fixtures captured on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal 2defab11 (the round-30 candidate) -- presets.cjs 1 of 4, windowread.cjs 1 of 4 (FAIL as expected; PLANTED arms pass by design). The amended round-29 leadface.cjs reads 2 of 3 there (its cursor clause fails as expected).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zi-1` (round 31, decomposition v31; serves FWD-26, and FWD-21 / FWD-22 read through the window)

**The outcome (PRD FWD-26):** "Chatter and Price each offer 30D / 90D / 365D presets in the shared Segmented control, default 30D,
replacing 'Earlier month' / 'Later month'; each face's caption names its window ending at the served as-of date; where the store is
shorter than the window, the face states the served window start ('since <date>') and never extrapolates. Price's 90D/365D render
the served 'not produced yet' reason as a designed empty state."

**What the routes serve now** (deployed, captured in `round31/fixtures/windows.{chatter,price}.{30,90,365}.json` under
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace/org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/`):
- `GET .../lead-panel/timeseries/collected/chatter?days=N`. It serves `window_days` N, `window_start`, `window_end`
  (2026-10-02) and `window_start_requested`. At 365 it also serves `window_note`, because the store begins 2026-01-01, after the
  requested start. Every row carries `articles_total`, the count in the window (Boeing: 71 at 30 days, 143 at 90), plus `by_month`.
- `GET .../lead-panel/rankings/trending/price?days=N`. At 30 it serves 94 rows with `window_days` 30. At 90 and 365 it serves 0
  rows with `ranking_status` "ABSENT" and `window_reason` ("the 90- and 365-day price windows are not produced yet: ...").

Build:
1. **The route** (`portal/src/api/endpoints/amgt-lead-panel.ts`):
   - `getCollectedChatter(days?: number)` sends `?days=<days>`.
   - `getLeadPanelRankings(movement, subject, limit?, days?)` sends `days` beside `limit`.
   - With `days` omitted, each URL is byte-identical to today's.
2. **The reads** (`hooks/useLeadPanelApi.ts`, `constants.ts`):
   - `useCollectedChatter` and `useLeadPanelRankings` take the window and pass it through as `days`.
   - Their query keys (`AMGT_QUERY_KEYS`) carry the window, so 30, 90 and 365 are three cache entries.
   - The page always sends the window explicitly: 30 at rest.
3. **The presets** (`components/LeadPanel.tsx`):
   - ONE `Segmented` (from `@/ui/components/Controls`, `ground="band"` like its neighbours) with exactly three options, labelled
     `30D`, `90D` and `365D` (or `1Y`, the IndexPerformanceModal label), in that order. 30D is active at rest.
   - The window lives in `useState` inside the LeadPanel tree; nothing outside your files holds it.
   - Both faces read the same window. Chatter reads `getCollectedChatter(days)`; Price reads
     `getLeadPanelRankings(movement, 'PRICE', PRICE_BARS_READ_LIMIT, days)`.
   - Hand ChatterBubbles the served rows whole (`data.rows`, all of them; round-30 `universe.cjs` counts 95).
   - Hand it NO `month` and NO `onMonthChange`. The month cursor leaves the page.
4. **The Chatter face, at the window** (`components/ChatterBubbles.tsx`, `LeadPanel.tsx`):
   - When ChatterBubbles is not handed a `month`, each row's bubble is sized by its served `articles_total` (area proportional,
     the existing radius rule). A row with `articles_total` 0 or null draws no bubble.
   - The bubble's hover names "<n> article(s) collected" and the window, e.g. "71 articles collected in the last 30 days".
   - The face's caption reads "Articles collected over the last <N> days to <window_end in words>", using `longDate` from
     `../dateWords`.
   - When `window_start` differs from `window_start_requested`, the caption adds "since <window_start in words>", e.g. "since
     January 1st, 2026". It never claims days the store does not hold.
   - Neither face prints "Earlier month", "Later month", "partial month" or "per month". The footer's "Articles collected per
     month" goes.
   - **Keep month mode working** for a caller that hands `month` (and `onMonthChange`): the round-29 `collage.cjs` and `tone.cjs`
     checks and the round-30 `chrome.cjs` check render ChatterBubbles that way, so keep `stepMonth` exported and the cursor drawn
     when `onMonthChange` is given.
5. **The Price face, at the window** (`components/PriceBars.tsx`, `LeadPanel.tsx`):
   - At 30 days nothing changes: the served bars and the `[data-price-window]` caption "Change over the last 30 days to ...".
   - At 90 and 365 days the served list is empty with a `window_reason`. Print that reason as the designed empty state (fall back
     to `ranking_reason`). Draw no bar and no `[data-price-window]` caption, and no "30 days" and no "No price moves ranked yet"
     anywhere on the face.
   - The page computes no window and no return (C-PRESENTATION-ONLY).
6. **Types** (`types.ts`): add the served window fields as OPTIONAL properties only (`window_days`, `window_start`, `window_end`,
   `window_start_requested`, `window_note`, `window_reason`, `articles_total`). No existing property changes.
7. **Harnesses** (`__harness__/leadPanelPattern.harness.cjs`, `__harness__/errorEmpty.harness.cjs`): change them only to follow a
   new hook argument or export. No assertion is removed or weakened.

**Contracts:** C-PRESENTATION-ONLY (served counts, returns and reasons print as served). One purple action per view: the presets
are a `Segmented`, never a filled button.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. In `types.ts` and `constants.ts`, changes are additive or key-shape only.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. The base worktree's
   files may be CRLF; keep each file's existing line endings.

## 3. SURFACES

<paths>
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~88/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository. In particular, the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round31/`, `round30/` and `round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zi-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round31/checks/presets/presets.cjs"; echo "exit=$?"</invocation><expect>ROLLING WINDOWS, NAMED: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zi-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round31/checks/presets/windowread.cjs"; echo "exit=$?"</invocation><expect>EACH WINDOW IS ITS OWN READ: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zi-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC2's KEEP arm also runs, and needs each of these to exit 0: the round-29 collage, tone, pricemovers and leadface checks (leadface
as amended), and the round-30 universe, resolutionwords and chrome checks.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~88/DSGN_AMGTV1.TO-AV-zi-1.rolling-windows-presets.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W88-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded** (L9 PNG read at the close walk): how the presets sit beside Subject and Starred; whether 90D's bubble sizes read as a
  change; how the Price empty state looks; the 365 "since" clause's wording in place.
- **Check limits:** the click replay reaches state held in `useState`/`useReducer` in the LeadPanel tree only. The route arm reads
  the two endpoint functions only.
- **Issuer amendment landed with this issuance:** round29/checks/leadprice/leadface.cjs AMENDMENT 1 (no month cursor; reads the
  served 30-day window fixture).
- **Model:** this worker runs on the Sonnet override. The Opus subagent pool returned a weekly rate limit at ~02:2xZ.

<status>complete</status>
<round>31</round>
<slot>~88</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
