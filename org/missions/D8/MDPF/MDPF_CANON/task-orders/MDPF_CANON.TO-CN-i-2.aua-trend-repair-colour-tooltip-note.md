# MDPF_CANON task order -- `CN-i-2` -- THE AUA TREND REPAIR: CLIENT UNSUPERVISED LEAVES THE LOCKED ORANGE, THE TOOLTIP DRAWS NO ROW FOR AN ABSENT SERIES, THE PAGE STATES WHERE PER-MODEL DETAIL BEGINS (FWD-9; PORTAL CANDIDATE REPAIR)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-i-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~24</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one colour entry, two pure functions, one type field and three page lines.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS write; the `data` arm reads one served object (read-only gets).
comp-adversary: RUN by the issuer's fork (2.0.0_SA_COO~D1) on DELL1 -- `r8_cn_i_2.py build` reads 3 of 13 at base (C1, C4 and N4 are controls that hold) and 13 of 13 on a scratch reference patch; six mutants (the colour left orange, a tooltip filter that drops a measured zero, a note that shows on an equal date, a band added to the mount list, the note not wired, the meta type not added) turn C2/C3, T2, N2, N4, N3 and N1 red; `regress` reads 2 of 2 (the CN-i-1 module 9 and page 8 arms) at base and on the reference; `data` reads 3 of 3 on the served object by design (it grades the SERVED inputs and the classifier, and is not a build test); `selftest` prints OK, with the classifier failing three planted defects (a model line before the boundary, a stack above the Total, a Total that is not the sum of its parts) that the CN-i-1 data arm D1 accepted.
EGRESS CLASS, declared: READ-ONLY S3 gets by the `data` arm (bucket opal-data-assets, prefix portal/gold/mdpf/global/aggregate-aua-timeseries/); no write.
</preflight>

**Your worktree:** the spawn names it (outer branch `wk-MDPF_CANON-24`, cut from the issuance commit). The portal is a NESTED repository at `<worktree>/portal`, provisioned on its own
branch `wk-MDPF_CANON-24-portal` cut from the CANDIDATE branch `cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` (head 34cd12d2, NOT from DEV: the repair builds on that work) with `node_modules` linked.
Start every shell call with `cd` into the outer worktree path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout. The existing files use CRLF line
endings: keep them, and confirm with `git -C portal diff --stat` that the diff is about 45 lines over four files.

## 1. THE ACT -- `CN-i-2` (the repair of the AUA Trend candidate)

THE REQUIREMENT. The CVO graded the candidate NOT MET against PRD FWD-9 (3) and (4) and DESIGN.md (row D1-C-S73): (1) `Client Unsupervised` is drawn in the locked Ultra-Short Term orange (#f97316, CIEDE2000 0.0
against it); (2) the tooltip prints a `$0` row for a series that is null on the hovered date; (3) the stack does not sum to the Total on 383 dates and the page says nothing about it. The CTO ruled the third (PRD v2.18,
FWD-9 clause (2)): on every date before `per_model_detail_begins` (2026-05-15) the FWD-3 fold suppresses EVERY model line, so the stack is below the Total by the whole model AUA; that is exception (ii); it is NOT drawn as a band
(a band would draw what FWD-3 forbids); the page STATES it: "per-model detail begins <date>; earlier model assets are in the Total and are not broken out". You make exactly these three repairs and nothing else.

### 1a. `portal/src/components/CategoryViewTree.tsx` -- one colour entry

In the exported `L1_COLOR` table, the line `  'Client - Opal Unsupervised': PALETTE.orange500,` becomes these three lines (the comment lines are part of the edit):

```
  // CN-i-2 (D1-W18-S7): lime500, not orange500 -- orange500 is the locked Ultra-Short Term hex (CIEDE2000 0.0 on the Trend);
  // lime500 is dE00 20.6 or more from every other Trend colour and 19.9 from every other row of this table.
  'Client - Opal Unsupervised': PALETTE.lime500,
```

`PALETTE.lime500` exists in `src/lib/chartColors.ts` (#84cc16): add no token and edit no other line. `L1_COLOR` is shared with the Total Assets breakdown, so its Client Unsupervised bar and dot repaint too: that is
intended (the Trend takes the Total Assets colours, FWD-9's title) and the issuer names it in the approval row. Do NOT add a Trend-local colour override.

### 1b. `portal/src/lib/trendGrouping.ts` -- two pure exports appended at the end of the file

```ts
/**
 * CN-i-2 (PRD v2.18): the Trend tooltip lists a series only where it HAS a value on the hovered date. ABSENT IS NOT ZERO:
 * null, undefined, '' and a non-finite value drop; a measured 0 (number or numeric string) and a negative stay.
 * Returns a new array in the input order and never mutates the input.
 */
export function presentTrendEntries<T extends { value?: unknown }>(entries: ReadonlyArray<T>): T[] {
  return entries.filter((e) => {
    const v = e.value
    if (v === null || v === undefined || v === '') return false
    return Number.isFinite(Number(v))
  })
}

const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/

/**
 * CN-i-2 (PRD v2.18, FWD-9 clause (2)): the sentence the Trend states when it draws dates before the served object's
 * meta.by_model_fold.per_model_detail_begins. Null unless both dates are ISO and the first drawn period is BEFORE the boundary.
 */
export function trendDetailNote(begins: string | null | undefined, firstPeriod: string | null | undefined): string | null {
  if (typeof begins !== 'string' || typeof firstPeriod !== 'string') return null
  if (!ISO_DATE.test(begins) || !ISO_DATE.test(firstPeriod)) return null
  if (!(firstPeriod < begins)) return null
  const shown = new Date(begins + 'T12:00:00').toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })
  return `Per-model detail begins ${shown}; earlier model assets are in the Total and are not broken out.`
}
```

The module imports nothing and keeps its header law. Touch no existing function.

### 1c. `portal/src/api/portal-proxy.ts` -- one optional type field (type only, no runtime change)

In `export interface MdpfPerFirmTimeSeries`, inside its `meta: { ... }` block, add before the `honest_none?` comment (`// MDPF_REVAMP.S5: producer-DECLARED honest-None days ...`):

```
    // CN-i-2 (PRD v2.18): the Global fold's boundary, served in meta.by_model_fold.
    by_model_fold?: { min_firms?: number; per_model_detail_begins?: string; statement?: string }
```

The served Global object already carries `meta.by_model_fold` (`min_firms`, `per_model_detail_begins`, `statement`); today the type hides it. Add no fetch.

### 1d. `portal/src/pages/ModelPortfolios.tsx` -- three edits

(i) The import `import { groupCustomModelsSeries, etfStrategiesAua, otherAua, clientChipAt } from '@/lib/trendGrouping'` gains `presentTrendEntries, trendDetailNote`.

(ii) In `renderTrendTooltip`, the line `const buckets = payload.filter((entry) => entry.dataKey !== 'interp_total')` becomes
`const buckets = presentTrendEntries(payload.filter((entry) => entry.dataKey !== 'interp_total'))`. Nothing else in the function moves (the total, the sort and the row map read `buckets` as before).

(iii) In the Trend body, right after the line `const endDateDisplay = latestTransactionDate.toLocaleDateString(...)`, add
```
          const detailNote = isGlobalSI
            ? trendDetailNote(globalMdpfData?.meta?.by_model_fold?.per_model_detail_begins, earliestPeriodStr)
            : null
```
and right after the closing `</p>` of the window paragraph (the one whose last line is `: \`Rolling 1-year ${assetLbl.short} growth from ${startDateDisplay} to ${endDateDisplay}.\`}`), add
```
              {detailNote && (
                <p data-trend-detail-note="true" className="-mt-3 mb-4 text-xs text-white/60">{detailNote}</p>
              )}
```
The note shows at Global only, and only when the Trend draws a date before the served boundary. `STACK_SERIES` does not change: there is NO band for the suppressed dates, no series, no label, no colour.

LAWS THAT BIND THIS EDIT. (i) No band, no series and no number is drawn for the suppressed model assets (PRD v2.18: it would draw what FWD-3 forbids); the gap is printed by the issuer's readback, never by the page. (ii) Absent is not zero. (iii) No new served key,
no served-object change, no second fetch, no new dependency. (iv) The locked model colours (the five Opal models), Custom, ETF, Client Supervised and ALT (vermilion500, pinned by `ModelPortfolios.taxsma-color.test.ts`) do not change. (v) The provenance read guard stays
green (`node scripts/provenance-read-guard.mjs` in the portal prints `OK:`). (vi) The CN-i-1 arms (`r7_cn_i_1.py module` 9 of 9 and `page` 8 of 8) stay green: the `regress` arm reads them.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ`. Row id form `MDPF_CANON-D1-W24-S<k>`, `disarm_owner` `2.0.0_SA_COO~D1`. If you meet a resolved colour equal to another series' colour, file an OBSERVATION row naming both hex values.

## 2. BOUNDS

1. Portal repository only, on branch `wk-MDPF_CANON-24-portal`; never push; never touch `DEV` or `PROD`; no merge.
2. Edit only the files in section 3 (plus your deliverables and the surprise channel). No token change, no new dependency, no new component, no new file.
3. No AWS write of any kind, no deploy, no store write. The `data` arm's read-only gets are the only AWS contact. No `bun install` (the modules are linked). No browser launch.
4. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file; the arms print firm-level aggregates and counts only.
5. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF in the existing files.
6. If an item cannot be met inside your paths, file a row and stop on that criterion: the issuer rules it.
7. Do not edit the issuer's checks, `ModelPortfolios.taxsma-color.test.ts`, `chartColors.ts`, `modelPortfolioColors.ts` or `STACK_SERIES`.

## 3. SURFACES

<paths>
portal/src/components/CategoryViewTree.tsx
portal/src/lib/trendGrouping.ts
portal/src/api/portal-proxy.ts
portal/src/pages/ModelPortfolios.tsx
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~24/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, `portal/src/lib/chartColors.ts`, `portal/src/lib/modelPortfolioColors.ts` and the issuer's checks
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_2.py` and `r7_cn_i_1.py` (never edit them; read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_2.py" build; echo "exit=$?"</invocation><expect>ROUND 8 CN-I-2 BUILD: 13 of 13 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_2.py" data; echo "exit=$?"</invocation><expect>ROUND 8 CN-I-2 DATA: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_2.py" regress; echo "exit=$?"</invocation><expect>ROUND 8 CN-I-2 REGRESS: 2 of 2 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-i-2" judgment="true"/>
</proof_of_spec>

AC2 reads the served Global object (read-only gets) and prints the per-class counts of the stack against the Total: it is the issuer's readback of the gap the page now states, and it must still read 3 of 3 after your edit (it grades the served data, not your files).

AC4 is JUDGMENT, graded at the round close (never self-graded): the issuer renders the Global AUA Trend at a STATED portal commit and the CVO reads it against PRD FWD-9 (3), (4) and (2) as ruled in v2.18: the five canonical series unchanged; "Client Unsupervised" no
longer in the Ultra-Short Term orange, distinct from every other series in the legend and the stack; hovering dates C and D prints no Client row and no `$0` row; the note "Per-model detail begins May 15, 2026; earlier model assets are in the Total and are not broken out." is
on the face above the charts; no band for the earlier dates. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the four portal files INSIDE the nested repo: `git -C "<worktree>/portal" add -- src/components/CategoryViewTree.tsx src/lib/trendGrouping.ts src/api/portal-proxy.ts src/pages/ModelPortfolios.tsx` then
   `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~24 <0.9.0_WK_MDPF_CANON~24@opal.agent>" -F <msgfile>` (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~24/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.proof_of_spec.json`, AC4 UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round close".
   **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when AC1, AC2 and AC3 all pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~24 <0.9.0_WK_MDPF_CANON~24@opal.agent>" -F <msgfile> -- <paths>` (outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once: the portal branch and commit hash, the diff (one line per file), the output line of AC1-AC3 (the AC2 line carries the class counts), the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the repair of the AUA Trend candidate (`cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` @34cd12d2; DEV already carries it as `9e637fe51e`, landed 2026-10-14 ~18:4xZ before the CTO's "do not promote", msg 5705; DEV is not PROD). Inputs: the CVO's L9 (`ADJUDICATION_v10.md` rows
D1-C-S73, D1-C-S74), the CTO's ruling (msg 5719, PRD v2.18 @0736ed5c23: exception (ii) covers the dates before `per_model_detail_begins`, NO band), `round7/STACK_SUM_MEASURE_20261014.md` @caec08b05f. Cut only after the CVO signs v2.18's ratified-text half; the round number is the issuer's at the recut (round 8).
DRAIN CHECKS (the issuer's, not criteria): `bun run typecheck` and `node scripts/provenance-read-guard.mjs` in the portal worktree, once, after the commit; the real run is `/ui-walk` on `bun run dev:live --port 5174` with the portal commit stated beside the screenshots (`git -C portal rev-parse HEAD` in the worker's portal
worktree: the CVO asked for the stamp) and a HOVER on dates A, C, D and E.

**RISK CLASS:** `LOCAL` for this cell (portal/src is the LOCAL floor, GATE xii). `worker` (not light): four files and a colour contract, about 45 lines. LANDING (CLAUDE.md Portal, fcdfc34843): DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row, never by this order; the client-facing candidate's approver is Andrew; PROD only by a chosen-set promote.
The repair becomes a NEW candidate branch cut by the issuer from the worker's portal branch, and its approval row is a FRESH client-facing row that names exactly what changed from the head Andrew approved (34cd12d2): (1) the Client Unsupervised colour, which also repaints the Total Assets breakdown's Client Unsupervised bar and dot (orange500 to lime500);
(2) the tooltip lists no row for an absent series; (3) one sentence of text at Global; (4) one optional type field. Nothing served changes. The CVO's grade of CN-i-1 AC4 stays NOT MET until the repaired head is read.

**FOR THE ISSUER (measured, not decided here):**
1. **The colour choice and what it costs.** Measured with the CVO's own CIEDE2000 (this check's implementation reproduces his five published pairs to 0.05): no gold-family token clears 10 (yellow500 3.5 from Client Supervised, amber600 7.9 and orange400 7.7 from Ultra-Short Term), because the warm region is held by Ultra-Short orange, Short amber, Client Supervised amber400 and ALT vermilion. The
   best legible token is `lime500` #84cc16: minimum 20.59 from the Trend colours (Intermediate-Term green #10b981) and 19.94 from every row of the Total Assets table (ALT green400 #34d399). It leaves the Client gold family (Supervised stays amber400). Alternatives: pink400 16.4 (vs Custom), cyan600 18.2 (vs Long). Whether a green-family Unsupervised is acceptable is Andrew's design call; the rule is the CVO's instrument.
2. **The colour lives in a SHARED table.** Changing `L1_COLOR` repaints the Total Assets breakdown too (client-facing). The alternative is a Trend-local override like ALT's, which breaks FWD-9's "the colors the Total Assets breakdown already uses" and needs a PRD note. REC: the shared change (one place; the precedent is IV-e-70, which moved the Alternatives asset-class token off orange500 for the same collision).
3. **The gap, measured now on the served 2026-10-13 object** (487 valued dates of 496; boundary 2026-05-15 = the first date with any model line): BEFORE-DETAIL 383 (gap equals the whole model AUA, $436,842,747.89 to $1,349,270,858.88, to the cent); EXACT 49; FOLD-OR-OTHER 55 (stack below the Total, $26,130,760.13 to $58,576,784.27, dates 2026-05-15 to 2026-09-09); FAIL 0;
   identity breaks 0. The 55 are CONSISTENT WITH the fold's suppressed Other Models line and NOT ESTABLISHED as it: the object carries no per-date fold record (a producer matter, outside this cell). The CN-i-1 data arm D1 stays vacuous in `round7/checks/r7_cn_i_1.py` (its rounding-gap branch accepts every date); this cell's `data` arm replaces it, and the issuer patches or retires D1 at issuance.
4. **Per-firm scopes** carry no `meta.by_model_fold` (the fold is Global's), so the note shows at Global only; the per-firm series are unmeasured for a boundary.
5. **TypeScript is unverified for the reference patch** (the arms read it as source; the scratch tree is not a project): the drain's `bun run typecheck` is the compile proof.
6. **The helper formats the boundary date with `toLocaleDateString('en-US', long)`**, the format the page's own window sentence uses ("May 15, 2026").
7. **Not in this cell:** the history-leaf failure surfacing (CN-j-2), the Other Models "as of" text (CN-l-2, merged outer, same candidate), any change to the stack or its mount list, any served-object change.

**Fanout:** 1 of 1 chains; no shared file with any other open cell (CN-j-2 owns the publisher). `portal_ref:` the candidate branch `cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` (34cd12d2d0), passed as `--portal-ref` to `wk-provision.sh`, not portal DEV.

<status>complete</status>
<round>8</round>
<to_id>MDPF_CANON.TO-CN-i-2</to_id>
<slot>~24</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
