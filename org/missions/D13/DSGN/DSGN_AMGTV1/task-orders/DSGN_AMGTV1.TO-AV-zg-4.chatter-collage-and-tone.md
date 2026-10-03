# DSGN_AMGTV1 task order -- `AV-zg-4` -- THE CHATTER FACE IS ONE PACKED COLLAGE, FILLED BY ITS SERVED TONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zg-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~83</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from captured and planted fixtures.
comp-adversary: RUN by the issuer at the cut on portal dcdc89b1 (= DEV ec65c5d6 for src/pages/SecurityAnalysis) -- collage.cjs 2 of 4, tone.cjs 2 of 4 (FAIL as expected; each check's CONTROL and PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zg-4` (round 29, decomposition v29; serves FWD-21 v0.10, its layout and fill limbs)

PRD `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` FWD-21 (lines ~291-315) and register rows SAUX-16, 17, 18
(`docs/briefs/amgt-security-analysis-ui-findings-20261002.json`). CTO fold ruling 2: one bubble per security, a collage with the largest
at the centre, a deterministic spiral placement with NO new dependency, and the fill is the served tone through ONE shared sentiment
module. Ruling 4: the diverging Topic Cloud ramp applies to sentiment fills, with a legend. The rolling windows are NOT this cell: the
month cursor stays.

Build (the checks grade exactly this):
1. **`portal/src/lib/sentimentColor.ts` (new).** `export function getSentimentColor(sentiment: number): string`, copied BYTE FOR BYTE from
   base `portal/src/components/market-performance/TopicCloud.tsx` lines 44-90. Only `export ` is added. The doc comment at lines 33-43
   may move with it.
2. **`TopicCloud.tsx`.** Remove that function (lines 44-90, or 33-90 with its comment). Add exactly one line:
   `import { getSentimentColor } from '@/lib/sentimentColor'`. Nothing else changes, and its render stays byte-equal. Its readers are
   the Market page's Topic Cloud; `KeywordSentimentModal.tsx:40` and `ExecutiveSummary.tsx:693` keep their own private copies, untouched.
3. **`portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx`.** Import `getSentimentColor` the same way; the file defines no ramp
   of its own. Extend the row type locally: `CollectedChatterRow & { tone?: number | null; voters?: number | null; articles_total?: number | null }`
   (`types.ts` is owned by no cell this round). These are RESAPP FWD-36 fields, not served yet; the page reads them the day they are.
   - **The svg.** One `<svg viewBox="minX minY W H">` holds every bubble. The viewBox is a constant, the same at 17 and at 95 names. The svg
     carries a numeric `height` attribute, or an inline style `height`/`max-height` in px, of 520 or less. No `transform` attribute or
     style on anything inside it.
   - **Each bubble.** `<circle data-bubble="<security_key>" cx cy r fill>` with absolute numbers; `motion.circle` is fine. It keeps its
     round-27 `<title>` hover. `r = k * sqrt(collected)`, with one k per render, area within 2% of proportional, and no minimum clamp.
   - **Placement.** A pure function: no `Math.random`, `Date.now`, `performance.now`, `new Date` or `crypto`. Sort by collected, largest
     first, ties by key. The largest bubble contains the box centre. No two circles overlap, and every circle sits inside the viewBox.
     The Spearman rho of radius against `hypot(dx/(W/2), dy/(H/2))` is -0.5 or lower (smaller outward).
   - **Labels.** Exactly one `<text data-bubble-label="<key>" x y font-size text-anchor>` per bubble; optional `<tspan x y dy>` lines.
     The text is the full served `display_name`, or a leading part of at least 3 characters ending in `...` with the full name in the
     hover. Every `<text>` must fit the box model: 0.6 x font-size wide per character, 1.2 x font-size tall. Bands: default baseline
     `[y-0.9fs, y+0.3fs]`; `middle`/`central` `[y-0.6fs, y+0.6fs]`; `hanging` `[y, y+1.2fs]`. No line leaves the box or overlaps
     another, and `font-size` is a numeric attribute.
   - **Fill.** A finite tone gives `fill={getSentimentColor(tone)}`. A null or absent tone gets ONE constant fill that is not a ramp
     colour; its hover includes "no clear tone", and a toned hover never does.
   - **Legend.** One `data-tone-legend` element. Its markup includes `#f5365c`, `#eab308`, `#2dce89` and the no-tone fill, and its
     text includes "no clear tone".
   - **Ink.** The Lead Panel becomes a WHITE hairline panel this round (cell `AV-zg-3`), so every text and stroke ChatterBubbles draws
     (the labels, the legend, the month cursor, the denominator line; today band ink at ~lines 133, 138, 164, 203, 212, 220, 223) uses
     navy ink (`--palette-navy`), never white or band-light ink. Graded at the PNG read.
   - **Keep as is.** The face text says "collected" and never "market chatter". `stepMonth` stays exported and clamped, and
     `[data-chatter-cursor]` still renders when `onMonthChange` is given. The props are unchanged, `package.json` is unchanged, and the
     only bare imports are `react` and `motion/react`.

**Contracts:** C-PRESENTATION-ONLY (no tone, window or count is computed); C-FRIDAY (the served unit as served). Design law: a code may
sit in a data attribute, never in visible or hover text. A served display name prints as served.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/lib/sentimentColor.ts
portal/src/components/market-performance/TopicCloud.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~83/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zg-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/collage/collage.cjs"; echo "exit=$?"</invocation><expect>THE CHATTER FACE IS ONE PACKED COLLAGE WITH CLEAR LABELS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zg-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/collage/tone.cjs"; echo "exit=$?"</invocation><expect>EVERY BUBBLE IS FILLED BY ITS SERVED TONE THROUGH THE ONE SHARED RAMP: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zg-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~83/DSGN_AMGTV1.TO-AV-zg-4.chatter-collage-and-tone.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W83-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Not graded by the checks (left to the PNG read at L9): whether the collage really fits 1440x900 with no scroll (the
check grades a 520px proxy), legibility and ink contrast on each fill, real browser text widths (0.6em/char is a model), a label over
another bubble, the legend's wording and placement, how Topic-Cloud-like the packing reads, and the month-step animation. Surprise:
tone is per window, so under the month cursor every month shows the same colour until RESAPP FWD-36 serves `?days=`.

<status>complete</status>
<round>29</round>
<slot>~83</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
