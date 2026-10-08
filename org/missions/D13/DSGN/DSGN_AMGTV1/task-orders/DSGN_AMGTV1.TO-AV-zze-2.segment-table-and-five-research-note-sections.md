# DSGN_AMGTV1 task order -- `AV-zze-2` -- THE SEGMENT TABLE AND THE FIVE RESEARCH-NOTE SECTIONS ON THE THESIS TAB

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zze-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~116</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, rendered offline by the check against bodies the issuer captured.
comp-adversary: RUN by the issuer at the cut on portal DEV 38cc0ecf -- r53b.cjs 1 of 4 (arms 1 and 2 FAIL: no SegmentTable.tsx, no DossierSections.tsx; arm 3 FAIL: the Thesis tab renders for all five live bodies and draws neither place; arm 4 PLANTED passes). On scratch reference components loaded through CHECK_SRC_OVERRIDE, 4 of 4. The tree was not edited.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zze-2` (round 53, decomposition v53; PRD rows SAUX-43 and SAUX-42, FWD-4)

All product paths below are under `portal/src/pages/SecurityAnalysis/`. The `/thesis` read (`useThesisBundle`, type `ThesisBundle` in
`types.ts` at about line 1200) now serves two blocks the page draws nowhere. Real served bodies for five names are in
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/served/thesis_<name>.json` (AMD_US_Equity, ASML_NA_Equity,
NU_US_Equity, 8766_JP_Equity, HD_US_Equity). Read them before you write a line.

### 2a. `segment_table` -- the Bloomberg segment table (SAUX-43)

Shape: `{ status, reason, source, currency, units, currency_note, period_note, periods, rows, operating_income_rows }`.
- `status` is `"served"` or `"none"`. With `"none"`, `rows` and `periods` are empty and `reason` is a plain sentence (HD: "No Bloomberg
  segment table has been stored for this name yet.").
- `periods`: in served order, each `{ period, label, fiscal_year, note, top_level_sum }`. `label` is what a column is called ("Fiscal year
  2025", or "Period 2" when the column ties to no year); `note` is null or a plain sentence saying why a column has no year.
- `rows` (revenue) and `operating_income_rows`: in served order, each `{ segment, level, values }`, `values` one number or null per period.
- `source`: `{ label, vendor, pulled_at, company, object }`, e.g. label "Bloomberg product segments", pulled_at "2026-10-07T11:51:13Z".
  `object` is a storage path and is never printed.

**Make it:** new file `components/SegmentTable.tsx` exporting `SegmentTable`, one prop `table` (the served block, or null/undefined).
1. No block: draw nothing at all.
2. `status` not `"served"`: draw ONE `<section data-segment-table="none">` holding the served `reason`, verbatim, once. No table.
3. `status` `"served"`: draw ONE `<section data-segment-table="served">` holding, in this order:
   - a heading "Revenue by segment" and a `<table data-segment-table-revenue>`: a `<thead>` row whose first `<th>` is "Segment" and then
     one `<th>` per served period carrying its `label` verbatim, in served order; a `<tbody>` with one `<tr>` per served row in served
     order: a first `<td>` with the `segment`, then one `<td>` per value. A number prints with
     `new Intl.NumberFormat('en-US', { maximumFractionDigits: 1 })` (16635 reads "16,635", -4007 reads "-4,007"); a null value is an
     EMPTY `<td>` (no text at all). A row whose `level` is above 1 is indented (`pl-4` per level above 1);
   - when `operating_income_rows` is not empty: a heading "Operating income by segment" and a second table, `<table
     data-segment-table-operating>`, with the same head and the same cell rules;
   - the served `currency_note` once and the served `period_note` once (each only when served);
   - each DISTINCT non-null period `note` once, prefixed by the labels of the columns it applies to, joined with ", " (AMD: "Period 2,
     Period 3, Period 4, Period 5: The rows of this column do not add up ...");
   - ONE element carrying `data-segment-table-source` whose text is "Source: " + the served `source.label` + ", pulled " + the pull day
     in words with `longDate` from `../dateWords` ("October 7th, 2026"). Never print a raw ISO date or the `object` path.
4. Styling: the table `w-full text-sm tabular-nums`; head cells bold navy (`text-[hsl(var(--palette-navy))]`); rows separated by the
   hairline (`border-t border-[hsl(var(--hairline))]`); numbers right-aligned; notes and the source line
   `text-xs text-[hsl(var(--palette-darkGray))]`. White surface only; no purple fill, no light text.

### 2b. `dossier_sections` -- the five research-note sections (SAUX-42)

Shape: a list of five, always in this order of `field`: `company_description`, `why_we_own`, `positives`, `negatives`,
`special_items`. Each `{ field, heading, status, text, reason, citation }`. `status` is `"served"` (then `text` is the stored text and
`citation` is `{ report_key, report_id, locator, passage }`) or `"absent"` (then `text` and `citation` are null and `reason` is a plain
sentence, e.g. "No research report we hold for this company has a \"Company description\" section."). On the live bodies ASML serves
5 of 5, NU 3 of 5, 8766 1 of 5, AMD and HD 0 of 5.

**Make it:** new file `components/DossierSections.tsx` exporting `DossierSections`, one prop `sections` (the served list, or
null/undefined).
1. Not a list, or an empty list: draw nothing at all.
2. Otherwise ONE `<section data-dossier-sections="">` with the heading "The research team's notes" (same heading class as the pillars:
   `text-[0.8125rem] font-bold uppercase tracking-wide text-[hsl(var(--palette-navy))]`), then one element per served entry, in served
   order, carrying `data-dossier-section="<field>"` and `data-dossier-section-state="<status>"`, holding its served `heading` (bold).
3. A served entry: its `text`, verbatim, once (`whitespace-pre-wrap`); a line "Source: <report name>" named the way the Thesis tab's
   pillars name it (`dossierReportName` in `tabs/ThesisTab.tsx`: the last segment of `report_key` without its extension; when there is
   none, "Source: the report is not named in this security's data"); and ONE closed `<details data-dossier-section-open="">` built like
   the pillars' opener (`tabs/ThesisTab.tsx` about lines 170-193: summary "Where this comes from", then the locator in words from
   `dossierLocatorWords(report_key, locator)` in `../reasonWords`, then the served `passage` in a `<blockquote>`). Never `open` by default.
4. An absent entry: its served `reason`, verbatim, once. No opener.
5. Never print `report_key`, `report_id` or any storage path.

### 2c. Mount both on the Thesis tab, and type them

1. `tabs/ThesisTab.tsx`: mount `<DossierSections sections={data.dossier_sections} />` exactly once, directly under
   `<ResearchTeamPillars ... />`, and `<SegmentTable table={data.segment_table} />` exactly once, directly above `<SegmentBreakdown ... />`.
   Both under the same `!isLoading && !isError && data` guard as their neighbours, so both draw whatever the drafting state is (never
   inside the `served &&` block).
2. `types.ts`: export `SegmentTablePeriod`, `SegmentTableRow`, `SegmentTableBlock` and `DossierSection` matching the shapes above, and add
   `segment_table?: SegmentTableBlock | null` and `dossier_sections?: DossierSection[] | null` to `ThesisBundle`. Do not touch the existing
   `segment_table?: string` inside `DriverChart` (a different field). The two components import their prop types from `../types`.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy. REFUSE, do
   not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). The page draws what is served: no sentence of
   your own except the four fixed words named above ("Revenue by segment", "Operating income by segment", "Source: ... pulled ...",
   "The research team's notes", "Where this comes from").
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY (Write for the two new files); keep each file's line endings (`tabs/ThesisTab.tsx` and `types.ts` are CRLF; write the
   new files CRLF too).
5. If a page harness in `__harness__/` asserts the Thesis tab's exact markup and breaks on the two new places, update ONLY that assertion,
   inside the harness file, to the new behaviour, and name it in your report.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/SegmentTable.tsx
portal/src/pages/SecurityAnalysis/components/DossierSections.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~116/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zze-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/checks/r53b.cjs"; echo "exit=$?"</invocation><expect>THE SEGMENT TABLE AND THE FIVE RESEARCH-NOTE SECTIONS ARE DRAWN: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zze-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~116/DSGN_AMGTV1.TO-AV-zze-2.segment-table-and-five-research-note-sections.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes.
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W116-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** PRD v0.18 @9a07662460 rows SAUX-42 and SAUX-43 (FWD-4): each "after COO~Z serves it (AMGT_RESAPP round 79)"; SAUX-43
  added under v0.18 at ~11:5xZ, no ENDPOINT change.
- **The dependency is met, measured by this seat:** `r79_deployed.py` "R79 DEPLOYED: YES 1 of 1" (~21:1xZ, cc-7 @42700562a4); the five
  live bodies captured by `round53/capture_served.py` (thesis http 200 each).
- **L5 decision (SAUX-42, "where each sits is this project's L5 decision"):** the five sections sit together on the Thesis tab, directly
  under the research team's pillars, as one block "The research team's notes", each under its served heading with the pillars' opener.
- **L5 decision (SAUX-43):** the table sits on the Thesis tab directly above the filing's segment prose (`SegmentBreakdown`), the place
  where AMD read a reason before. Both draw whatever the drafting state is.
- **One cell, not two:** both rows write `tabs/ThesisTab.tsx` and `types.ts`; cut by write set they are one cell.

<status>pending</status>
<round>53</round>
<to_id>DSGN_AMGTV1.TO-AV-zze-2</to_id>
<slot>~116</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
