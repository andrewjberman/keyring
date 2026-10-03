# DSGN_AMGTV1 task order -- `AV-zg-5` -- WHAT CHANGED LEADS THE MODEL TAB, IN ET AND IN READER WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zg-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~84</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from the portal's captured served fixtures.
comp-adversary: RUN by the issuer at the cut on portal dcdc89b1 (= DEV ec65c5d6 for src/pages/SecurityAnalysis) -- whatchanged.cjs 1 of 4, etwords.cjs 1 of 4 (FAIL as expected; PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zg-5` (round 29, decomposition v29; serves FWD-25 and FWD-27 on the Model tab)

PRD `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` FWD-25 (lines ~363-373) and FWD-27 (~387-402); register rows SAUX-23, 24,
26 and 34 (the Model's market cap) in `docs/briefs/amgt-security-analysis-ui-findings-20261002.json`. Today "WHAT MOVED BETWEEN TWO
VERSIONS" sits at the BOTTOM of the Model tab under a plain list of version timestamps, the times print in UTC, and four system
sentences print at rest. Read `tabs/ModelTab.tsx` (its versions/compare section ~680-900) and the served fixture
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/fixtures/model/served.BA_US_Equity.json`.

Build (the checks grade exactly this):
1. **The panel.** Exactly one `[data-what-changed]` element, ABOVE `table[data-model-sheet]` and above `[data-model-currency]`. It carries
   `data-what-changed-from` and `data-what-changed-to`, the served compact stamps of the pair shown.
   - **Header:** `[data-what-changed-header]`, with text containing "What changed".
   - **Count tiles:** `[data-what-changed-count="added"]` and `[data-what-changed-count="changed"]`. Each prints the served
     `denominators.added` / `denominators.changed` number and the word "added" / "changed".
   - **Table:** `[data-what-changed-table]`, with one row `[data-what-changed-row="<served compared.changed[].figure>"]` per changed figure.
   - **Cells:** `[data-what-changed-cell="before"|"after"|"change"|"pct"]`. Before and after each hold a figure. Change starts with
     its sign (`+` up, `-` or U+2212 down); a currency code may sit beside the sign. Pct is exactly `<sign><n>%`, equal to
     (to - from) / |from| x 100 at the precision shown.
   - **Per-line detail:** exactly one `[data-what-changed-detail]` per row, either a `<details>` with no `open` attribute or a
     `<button aria-expanded="false">`.
2. **Market cap (SAUX-34).** The `CUR_MKT_CAP` row's before and after both contain "USD", and the ET day of each version prints in that row
   or in the table's `<thead>`. No `$` anywhere in the panel.
3. **No codes at rest.** No `UPPER_SNAKE`, `snake_case` or `_Equity` token. The panel carries none of `data-model-sheet`, `-cell`, `-row`,
   `-refused`, `-absent-footnote` or `-fiscal-cells`: `ui-measure` reads the first `table[data-model-sheet]`, and `tabs.harness` counts
   `data-model-cell`.
4. **Default pair.** The later version is the newest served stamp. The earlier is the newest earlier stamp whose compare against it serves
   any added, removed or changed figure; walk back through every version with no cap. The static render resolves the pair in ONE pass,
   with no `useEffect`/`setState` stepping; a chain of probe components each calling `useModelCompare` once works.
5. **Picker.** `<select>` elements in the panel offer one `<option value="<served stamp>">` per version, and the pair shown is the selected
   options. No version time other than the pair's prints outside the selects or a closed `<details>`, so the version list collapses into
   the picker.
6. **ET (SAUX-24; issuer ruling b).** `dateWords.ts` exports `etStamp`, which maps `"20261002T154900Z"` to `"October 2nd, 2026, 11:49a ET"`
   and `"20260929T024521Z"` to `"September 28th, 2026, 10:45p ET"`. The existing `longDate`, `longStamp` and `chartTick` return exactly
   what they return today.
   - **On the tab:** every version option label is in that ET form, and every clock reads `h:mm[:ss]a|p ET`. No "UTC" and no raw
     stamp prints. The "Updated" day in `[data-model-panel-header]` and the ledger's "last ran" day are the ET day.
   - `[data-input-ledger]` stays in the HTML, at rest or inside a `<details>`.
   - `ModelTab.tsx` and `components/model/**` (comments excluded) contain no `UTC`, `toISOString`, `getUTC*`, `Intl.DateTimeFormat`,
     `toLocaleDateString`, `toLocaleTimeString` or `timeZone`. Times are formatted only in `dateWords.ts`.
   - This replaces the round-12 ruling (24-hour UTC labels) with PRD v0.10 FWD-27's one zone, ET.
7. **System sentences (SAUX-26).** None of these is at rest; text in an `sr-only` span or an open `<details>` counts as at rest:
   - "Showing <n> fiscal figures from the model block"
   - "No year-on-year growth rows: the model block serves none and this page computes none"
   - "<n> versions have landed; a refresh adds a version and never overwrites an earlier one"
   - "Re-running one input on its own is not available on this page yet"
   None appears word for word even behind a toggle; any you keep goes behind a details toggle in reader words. Keep
   `data-model-fiscal-cells=<history count>`, which `tabs.harness` reads.
8. **Imports, so the battery keeps passing.** Data comes only from `useThesisBundle`, `useModelVersions`, `useModelCompare` and
   `useInputLedger`. Use relative imports with full file paths and no index barrels. No `@/` import other than `@/ui/components/panels`,
   `@/lib/utils` and `@/components/DataTooltip`. `FigureTooltip`, `formatStatValue` and `figureTooltipRows` stay imported from
   `components/StatTile.tsx`, which another cell owns and must not re-sign; do not edit it.

**Contracts:** C-PRESENTATION-ONLY. The percent is the one figure computed, from the two served values, as FWD-25 asks. The page computes
no version, no window and no growth.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/dateWords.ts
portal/src/pages/SecurityAnalysis/components/model/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~84/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zg-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/model/whatchanged.cjs"; echo "exit=$?"</invocation><expect>WHAT CHANGED LEADS THE MODEL TAB: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zg-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/model/etwords.cjs"; echo "exit=$?"</invocation><expect>THE MODEL TAB READS IN ET AND IN READER WORDS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zg-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~84/DSGN_AMGTV1.TO-AV-zg-5.what-changed-leads-the-model-tab.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W84-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Not graded by the checks (L9 PNG read): the panel's look and wording; the readability of before/after/change (only the
sign and the percent are graded); the opened detail's content; behaviour after a user picks another pair; the no-differing-pair state;
the no-model state. Fixture is older than the walk (16 versions, 137 figures vs 19 / 147): no effect on the checks.

<status>complete</status>
<round>29</round>
<slot>~84</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
