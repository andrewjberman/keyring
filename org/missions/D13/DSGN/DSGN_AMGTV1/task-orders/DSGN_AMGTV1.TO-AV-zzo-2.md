# DSGN_AMGTV1 task order -- `AV-zzo-2` -- THE SPINE'S EVENT LABELS NEVER COLLIDE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzo-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~136</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal ce3b0cc4 (= origin DEV, round 62) -- r63c.cjs 1 of 4 (arms 1-3 FAIL as expected; PLANTED passes); battery29 ALL PASS at the base (round-62 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzo-2` (round 63, decomposition v63; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round62.md` section 2 first. Do the items in this order.

`components/TimelinePanel.tsx` `makeMarkerShape` draws each event marker's title in a fixed-width box (`EVENT_LABEL_W`) on one of two
rows picked by `markerIndex % 2`. On NVDA, markers close together draw their titles over each other. The titles are also 10px, under
the 11px floor.

1. **A pure layout** (NEW file `components/timelineLabels.ts`, which imports nothing from the page or the app):
   `export function layoutEventLabels(items, labelWidth, rows)`.
   - `items` are `{ x, alignEnd }` in pixels, in day order.
   - A label spans `[x - 6, x - 6 + labelWidth]`, or `[x + 6 - labelWidth, x + 6]` when `alignEnd`, matching today's
     `foreignObject` placement.
   - It returns one entry per item: a row in `[0, rows)` where no two labels on that row overlap, or `null` when no row is free.
   - Greedy left to right: the lowest free row first. Same length and order as `items`.
2. **Use it** (`TimelinePanel.tsx`):
   - Lay the event labels out with `layoutEventLabels`, using the chart's plotted pixel positions. The plot width can come from
     `ResponsiveContainer`'s `onResize` or a measured ref.
   - Use three rows, and stop choosing the row by `markerIndex % 2`.
   - A label whose row is `null` draws no title text; its marker and the marker's `<title>` tooltip stay.
3. **Readable:** the event label text is `text-[11px]` (it was `text-[10px]`).
4. **One band (AMENDMENT 1, after the close walk).** The rows are assigned, but each label is still drawn at
   `y={cy - 22 - level * 14}`. That is relative to its own marker's bar top, so labels on different rows land at the same height and
   still collide (NVDA, walk at 11:15Z: "Global funds lead..." over "SPAC effect...", and "Nvidia Partner Hon Hai's Sale..." over
   "China May Let Alibaba...").
   - Draw every event label in ONE band at the top of the plot: the label's `y` is a fixed band top plus `row * 14`, and never reads
     `cy`. Make the chart's top margin hold three rows.
   - The marker stays at its data point. A thin vertical tick from the label down to its marker is allowed, in the axis-text colour,
     1px.
   - Keep items 1-3.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/timelineLabels.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~136/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/timelinePrices.ts`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/checks/r63c.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzo-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/checks/r63c.cjs"; echo "exit=$?"</invocation><expect>ROUND 63 EVENT LABELS: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzo-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzo-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): NVDA's spine shows no two event titles drawn over each other.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~136/DSGN_AMGTV1.TO-AV-zzo-2.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-63 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W136-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**REOPENED (AMENDMENT 1, 2.0.0_SA_COO~D1, 2026-10-09 ~11:2xZ):** AC3 missed on the close walk (`tmp/ui-walk/20261009T111310Z` shot 032): labels laid out by row but drawn relative to each marker's own cy, so they still collide. Item 4 added; r63c gains arm ONE BAND (5 arms). The first build @2f97a04cc8 stays merged; the fix lands as a second commit on top of candidate f8eee17d. Graded by no gate limb at cut (a modification; GATE viii does not apply, `<placeholders>` NONE).

**ISSUER NOTES:** round 63 = `ledger/ROUND_ANALYSIS.round62.md` @4b7ce964a2 section 2, five items in three cells by file surface
(decomposition v63). Prep: `round63/PREP.md`. Base portal ce3b0cc4 (= origin DEV). LF only (ruling R2, row D1-S1).

<status>complete</status>
<round>63</round>
<to_id>DSGN_AMGTV1.TO-AV-zzo-2</to_id>
<slot>~136</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
