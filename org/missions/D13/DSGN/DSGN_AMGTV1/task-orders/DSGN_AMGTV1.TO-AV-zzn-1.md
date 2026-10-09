# DSGN_AMGTV1 task order -- `AV-zzn-1` -- THE PRICE LINE READS AS ONE LINE AND SAYS SO; THE NEWS TYPES MOVE TO THE CURRENT CONTRACT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~134</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal 9b06f6ed (= origin DEV, round 61) -- r62.cjs 2 of 6 (arms 1, 3, 4 and 5 FAIL as expected; NOTHING INVENTED holds as the guard; PLANTED passes); battery29 ALL PASS at the base (round-61 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzn-1` (round 62, decomposition v62; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round61.md` section 3 first. Do the items in this order.

Round 61 drew the served closing prices on the News tab's timeline spine (`components/TimelinePanel.tsx`) as a line on a right-hand
axis. The spine has a day for every calendar day, and prices exist only on trading days, so with `connectNulls={false}` the line breaks
at every weekend and holiday and reads as dashes.

1. **One line** (`components/TimelinePanel.tsx`, the price `Line` with `yAxisId="price"`): set `connectNulls` so the line joins across
   days with no close. Do not change `components/timelinePrices.ts`: a day with no served close stays `null`, and the chart draws the join.
2. **The axis says what it is** (the price `YAxis`, `yAxisId="price"`): add a label, in the same style as the left axis's
   `Articles per day` label, that names the closing price, e.g. `Closing price` (angle 90, on the right). No currency is served on the
   series, so the label names none.
3. **The join is stated** (the legend's price item, `data-timeline-legend-price`): its words become
   `Closing price, joined across days with no close`, replacing `Price`. Nothing else about prices is printed.
4. **The news types move to the current contract:** in `types.ts`, `CoverageItem.url` becomes `url: string | null` (the served feed
   carries null); in `constants.ts`, remove `HEADER_FEED_VISIBLE_COUNT`, which nothing reads (the News tab opens `FEED_OPEN_AT_REST = 10`
   in `components/HeaderBrief.tsx`). Fix any type error this makes in `components/HeaderBrief.tsx` without changing behaviour; its
   `feedRow` already guards the url at runtime.

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
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~134/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/timelinePrices.ts`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round62/checks/r62.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzn-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round62/checks/r62.cjs"; echo "exit=$?"</invocation><expect>ROUND 62 PRICE LINE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzn-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzn-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): the spine's price line reads as one line across weekends with its axis and legend saying what it is, and a name with no stored prices says so once.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~134/DSGN_AMGTV1.TO-AV-zzn-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-62 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W134-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 62 = `ledger/ROUND_ANALYSIS.round61.md` @3e33baad5b section 3. Items 1 and 3 (the price line, row Z-W87-S1)
are repairs batched into this one cell. Item 2 is the issuer's close walk (NVDA US, no stored prices). Item 4: Z-S21 is ruled no cell
(served case lines are not drawn since FWD-12 amended), and Z-W97-S1 is re-measured at the close (ChatterBubbles MIN_FS = 11 at
9b06f6ed). Base portal 9b06f6ed (= origin DEV). The order is LF only (ruling R2, row D1-S1).

<status>complete</status>
<round>62</round>
<to_id>DSGN_AMGTV1.TO-AV-zzn-1</to_id>
<slot>~134</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
