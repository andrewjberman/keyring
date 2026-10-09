# DSGN_AMGTV1 task order -- `AV-zzm-2` -- THE SPINE DRAWS THE SERVED PRICE LINE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~132</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal e6fb269c (= origin DEV, round 60) -- r61b.cjs 1 of 3 (arms 1-2 FAIL as expected, PLANTED passes; a clean timelinePrices.ts passes arm 1, the positive control); battery29 ALL PASS at the base (round-60 close).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzm-2` (round 61, decomposition v61; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round60.md` section 3 first. Do the items in this order.

The timeline range route (`/security/<key>/timeline`, read by `components/TimelinePanel.tsx`) now serves three more fields (AMGT_RESAPP
round 82, live): `price_series`, a date-ascending list of `{date, close}` points inside the served window; `price_series_source`, one
string naming the stored objects read; and, only when `price_series` is empty, `price_series_reason`, a plain sentence. An older payload
carries none of them.

1. **The type** (`components/TimelinePanel.tsx`, `TimelineRangeResponse`): add the three as optional fields
   (`price_series?: Array<{ date: string; close: number }> | null`, `price_series_source?: string | null`,
   `price_series_reason?: string | null`).
2. **A pure placing function** in a NEW file `components/timelinePrices.ts` that imports nothing from the page or the app:
   `export function withPrices(series, priceSeries)`. It returns the spine's own day entries, in their order, each with `close` = the
   served close for that exact date, or `null`. It adds no day, drops no day, and computes nothing (no fill, no average). With no served
   series every `close` is `null`. TimelinePanel imports it.
3. **The line** (`components/TimelinePanel.tsx`): when the served `price_series` has points, draw the closes as one line over the
   article bars, on its own right-hand axis, on the chart data from `withPrices`; a day with no close leaves a gap (never joined across).
   Mark the line's element with `data-timeline-price-line` (on the Line, or on a wrapper the panel renders only when the line is drawn).
   Keep the bars, markers, day dialog and legend as they are; add "Price" to the legend in the same style. Recharts `ComposedChart`
   with `Bar` + `Line` + a second `YAxis` is already installed.
4. **Said once when there is none:** when the served series is absent or empty, draw no line, and draw ONE short line under the chart on
   an element carrying `data-timeline-price-absent`: `No price line: ` followed by the served `price_series_reason` when one is served,
   else `No price line for this window.` Nothing else about prices is printed.

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
portal/src/pages/SecurityAnalysis/components/timelinePrices.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~132/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/harvest/timeline_api.py` (the producer, ~:300-380), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round61/checks/r61b.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzm-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round61/checks/r61b.cjs"; echo "exit=$?"</invocation><expect>ROUND 61 SPINE PRICE LINE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzm-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzm-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): AMD's spine shows the price line over the article bars, and a name with no stored prices says so once.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~132/DSGN_AMGTV1.TO-AV-zzm-2.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-61 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W132-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 61 = `ledger/ROUND_ANALYSIS.round60.md` @0b03adc339 section 3 (four items; items 1-2 are repairs, batched into
`AV-zzm-1`; items 3 and 4 are build cells `AV-zzm-2` and `AV-zzm-3`). Requested on UB-20261009T091009Z-b711 act 1. Base portal
e6fb269c (= origin DEV). The three cells' write surfaces are disjoint; only `AV-zzm-1` holds `__harness__/`.

<status>pending</status>
<round>61</round>
<to_id>DSGN_AMGTV1.TO-AV-zzm-2</to_id>
<slot>~132</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
