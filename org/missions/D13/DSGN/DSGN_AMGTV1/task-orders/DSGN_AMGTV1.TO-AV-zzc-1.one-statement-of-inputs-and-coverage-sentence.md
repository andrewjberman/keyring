# DSGN_AMGTV1 task order -- `AV-zzc-1` -- ONE STATEMENT OF INPUTS; THE SERVED COVERAGE SENTENCE IS DRAWN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~113</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, rendered offline by the check.
comp-adversary: RUN by the issuer at the cut on portal DEV d1b21c97 -- r51a.cjs 1 of 4 (arms 1, 2, 3 FAIL: the filings row prints only "Worked"; the block is fed from the overlay and the Model tab draws a ledger; no CoverageNote.tsx; PLANTED passes). On a scratch reference edit arm 1 passes and arm 3's four renders pass; arm 2 and arm 3's mount line are source reads and were not exercised green. battery29.sh at the base: ALL PASS (0 skipped). The tree was restored after, 0 changes.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzc-1` (round 51, decomposition v51; two page repairs in files that touch each other)

All paths below are under `portal/src/pages/SecurityAnalysis/`.

### 1a. ONE statement of where the page's data comes from (PRD row SAUX-37)

**Today** the page states its inputs in two places and they disagree:
- `SecurityAnalysis.tsx` (about line 121) draws `<InputProvenance entries={top?.input_provenance} />` above the tabs. `top` is the
  `/overlay` read, which serves four rows and no filings row.
- `tabs/ModelTab.tsx` draws a second list, "Where each input came from" (the `InputLedger` component, about lines 665-760, mounted
  about line 824), from a different read.

**The function now serves ONE statement on the `/thesis` read**: `input_provenance`, five rows in this order: `bloomberg`,
`seekingalpha`, `serp`, `filings`, `pack`. The `filings` row has the same five fields as the others (`input`, `source`, `last_run`,
`outcome`, `reason`) plus three more: `form` (for example `"10-K"`), `filing_date` (`"2026-01-30"`) and `used_for` (a list of plain
phrases, for example `["the filing passages", "the written sections", "the officer list"]`). When no filing was read its `outcome`
is `"never read"`, `last_run`, `form` and `filing_date` are null, `used_for` is empty and `reason` is a plain sentence.

**Make it:**
1. `SecurityAnalysis.tsx`: feed the block from the thesis read. Call `useThesisBundle(state.selectedSecurityKey)` (from
   `hooks/useLeadPanelApi`; the tabs already call it, so it is the same cached read) and pass its `data?.input_provenance` to
   `<InputProvenance>`. Do not read `top?.input_provenance` any more. The block is still mounted exactly once.
2. `types.ts` / `topBandTypes.ts`: add the three optional fields to `InputProvenanceEntry` and an optional
   `input_provenance` on the thesis bundle type, so no cast is needed.
3. `components/InputProvenance.tsx`: a `filings` row whose `outcome` is `"landed"` and whose `used_for` has at least one item
   reads: the served `source`, then the served `form`, the words "filed" and the `filing_date` in words (use `longDate` from
   `dateWords.ts`: "January 30th, 2026"), then "used for" and every `used_for` item. Never print the raw `2026-01-30`, and do not
   print that row's served `reason` (it carries the raw date). Every other row, and a never-read filings row, is drawn exactly as
   today (a never-read row already prints its served `reason`). Update the file's header comment to say the block reads `/thesis`
   and has five rows.
4. `tabs/ModelTab.tsx`: remove the second statement. Delete the `InputLedger` component, its mount, and the constants and
   helpers only it uses (`LEDGER_CLASS_WORDS`, `LEDGER_SOURCE_WORDS`, `LEDGER_OUTCOME_WORDS`, `LEDGER_HEAD`, `ledgerSourceWords`,
   `ledgerRunWords`) and the `useInputLedger` import. Leave the hook itself in `hooks/useLeadPanelApi.ts` alone. Nothing else
   on the Model tab changes.

### 1b. The served "we do not cover this company" sentence is drawn (PRD row SAUX-39)

The `/overlay` read now serves `research_coverage`: `{ status, covered, sentence, covered_names }`. `status` is `"covered"`
(then `sentence` is null), `"outside_coverage"` or `"not_known"` (then `sentence` is a plain sentence). Today the page draws it nowhere.

**Make it:**
1. New file `components/CoverageNote.tsx` exporting `CoverageNote`, with one prop `coverage` (the served object, or
   null/undefined). When `coverage.sentence` is a non-empty string, draw ONE element carrying the attribute
   `data-research-coverage` set to the served `status`, whose text is the served sentence, verbatim, once. Use black ink at the
   page's body size (`text-[14px] text-black`). In every other case draw nothing at all.
2. `topBandTypes.ts`: add optional `research_coverage` to `OverlayTopFields`.
3. `SecurityAnalysis.tsx`: mount `<CoverageNote coverage={top?.research_coverage} />` exactly once, in Security mode only,
   directly under the identity header and above the top band.
4. The rule reads the served shape only. Do not match on the sentence's words and do not add a sentence of your own.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no registry-reaching command, no push, no deploy. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY (Write for the one new file); keep each file's line endings (`tabs/ModelTab.tsx` is CRLF).
5. If a page harness in the battery asserts the Model tab's input ledger or the overlay-fed block, update ONLY that assertion,
   inside the harness file that asserts it, to the new behaviour, and name it in your report.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx
portal/src/pages/SecurityAnalysis/components/CoverageNote.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/topBandTypes.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~113/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round51/checks/r51a/r51a.cjs"; echo "exit=$?"</invocation><expect>ONE STATEMENT OF INPUTS AND THE SERVED COVERAGE SENTENCE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~113/DSGN_AMGTV1.TO-AV-zzc-1.one-statement-of-inputs-and-coverage-sentence.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W113-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** PRD v0.18 @9a07662460 rows SAUX-37 (FWD-12) and SAUX-39 (FWD-27); CTO msg 31675 ("take rows 37 to 40 into the next
  issuance"); AMGT_RESAPP `ledger/ROUND_ANALYSIS.round78.md` @1a67e26433 R3; rows AMGT_RESAPP-Z-W303-S1 and the round-78 walk's
  COVERAGE section.
- **Served, read by content at the deployed pin fbb643923e:** `lib/research/api/inputs_statement.py` (the `/thesis` statement with
  its filings row) and `lib/research/api/coverage_marker.py` (`research_coverage` on `/overlay` and `/thesis`). The round-78 walk's
  capture `overlay_MSFT.json` carries the marker live. The `/thesis` statement on the live function was NOT read by this seat; the
  close walk reads it.
- **L5 decision (SAUX-37):** the ONE statement is the block above the tabs, fed from `/thesis`; the Model tab's ledger is the second
  statement and is removed. `round47/checks/r47/r47.cjs` (the ledger's wording) is superseded by this cell and is not a criterion.
- **Two cells, one shared directory:** `AV-zzc-2` may also touch `__harness__/`; the drain merges the two portal branches in order.

<status>complete</status>
<round>51</round>
<to_id>DSGN_AMGTV1.TO-AV-zzc-1</to_id>
<slot>~113</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
