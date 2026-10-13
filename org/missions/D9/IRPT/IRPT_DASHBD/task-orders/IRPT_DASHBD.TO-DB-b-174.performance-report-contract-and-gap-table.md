# TO IRPT_DASHBD.TO-DB-b-174 -- the default performance report's Opal Shape as ONE vendor-free contract: a member for every baseline table, column, row, chart, cover field and convention, each naming its Opal gold source or ABSENT with its reason, and a gap table that counts them

<to_id>IRPT_DASHBD.TO-DB-b-174</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~140</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7181 and 7192, ROUND-94 ANALYSIS item 1 (PRD v0.14 @6d694ed9a5, FWD-21) | **Rows:** NONE | **Decomp cell:** `DB-b-174` (decomposition section 96) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-140` (branch `wk-IRPT_DASHBD-140`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~140/`.

**Why.** Andrew wants one default performance report for any client at any firm, on the Performance tab and as the export, in ONE "Opal Shape" (Andrew ~18:2xZ: vendors are data providers only; we own the serving process through our shapes; the gold layer is where vendor data becomes the shape). His baseline is a Black Diamond 49 Financial Performance Report (32 pages, one household of 11 accounts). Its STRUCTURE, read by the CTO, is the file
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md` (read it in full first). The PDF is client data and is NOT in the repo: you do not need it and you do not look for it. This cell writes the contract that the sample builder, the tab and the export will all share.

**The cell (`DB-b-174`).** A document, no code in the product.
1. **Read first.** The baseline schema above; the PRD's FWD-21 and its neighbours (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, search `FWD-21`, `FWD-20`, `FWD-8`); and the existing gold contracts in `org/standards/`, which are your SOURCES: `IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`, `IRPT_DASHBD_ACCOUNT_ACTIVITY_DAILY_CONTRACT.json`, `IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`,
   `IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json`, `IRPT_DASHBD_ACCOUNT_LOT_UNREALIZED_DAILY_CONTRACT.json`, `IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json`, `IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json`, `IRPT_DASHBD_SERIES_CONTRACT.json` (read their `summary`, `window_status`, field lists and `read_rule`). Also look for the FWD-20 figure map (`comp-find --files 'FWD-20' org/missions` and the IRPT_CUSTDY and IRPT_YCDGEN trees): if it exists, fold it in and set `fwd20_map_folded` true; if it does not, say so and set it false.
2. **Write ONE contract** `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, in the style of its siblings (`contract_version`, `project` "IRPT_DASHBD", `prd`, `prd_contracts`, `writer`, `reader`, `authored_by`, `siblings`, `change_rule`, `read_rule`) plus:
   - `sections`: exactly eight entries `{id, title, grain}` in this order: `cover`, `portfolio_overview`, `summary_of_portfolio_accounts`, `holdings_overview`, `taxable_realized_gain_loss_ytd`, `account_overview`, `gain_loss_review_by_account`, `disclosure` (the baseline's order; `disclosure` is the page the baseline export does not include).
   - `document`: how a FILLED report is laid out, for the sample builder to write and the tab and the export to read. It has a non-empty `shape` string (for example: values keyed by member id; each value is a number, a text, or `{"absent": "<reason in words>"}`; variable rows listed under `rows`), a `row_dimensions` object that holds at least `account` (one row per account of the household) and `class_hierarchy` (class then sub-class), the `windows` (quarter to date, year to date, last 12 months, month to date, since inception, each with its start date stated in the document), and how an "inception per household and per account" and a "not held for the entire period" footnote are carried.
   - `members`: a list with ONE member for each id printed by `python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . --ids` (117 ids, no more, no fewer; run it and keep its output as your checklist). Each member: `id`, `section` (one of the eight), `baseline` (the baseline's own place for it: section number, table, column, row, in words), `label` (the display words), `unit` ("dollars", "percent", "text" or "series"), and EITHER `source` = `{"contract": "org/standards/<one of the sibling files>", "field": "<a field name that really occurs in that file>"}` OR `source` = `"ABSENT"` with a `reason` in words (what Opal does not hold yet, and where it would come from). An ABSENT member carries no value and no default: ABSENT is never zero.
   - **Vendor-agnostic:** nothing in the file names a vendor or a custodian (no Black Diamond, Orion, Schwab, Commonwealth, Bloomberg, YCharts). Say "the baseline" where you mean it. A member's label never reads like a vendor's field name.
   - **Honest sources.** Map a member to a sibling's field only if that field really carries that figure at that grain and window (read the sibling's text). The four "Opal model benchmark" return rows, the month-to-date window, the household-level cost-basis columns and anything the siblings do not carry are ABSENT unless you find the field; say what is missing. Net gain: Opal's served return is total return BEFORE advisory fees (FWD-8) while the baseline's "Net Gain" includes fees: the member `convention.fee_basis_label` carries the label words, and the contract states where the two differ; never silently match them.
3. **Write the gap table** `GAP_TABLE.json` in your folder, with exactly these keys: `contract_sha256` (of the contract file's bytes as you leave it); `totals` {`members`, `sourced`, `absent`}; `by_section` (an object keyed by the eight section ids, each {`members`, `sourced`, `absent`}); `vendor_free` true; `baseline_cells_required` (equal to `totals.members`); `fwd20_map_folded` (bool); `sibling_contracts_read` (a list of at least three existing contract files you read); `reads` {`vendor_calls` 0, `s3_reads` 0, `s3_writes` 0, `secret_reads` 0}; `served_values_changed` false. Counts only; no run of eight or more digits.
4. A line in your final report: how many of the 117 members have an Opal source and how many are ABSENT, by section.

<criterion id="DB94-1-AC1" cell_refs="DB-b-174"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-1-AC1</invocation><expect>DB94-1-AC1 PASS</expect></criterion>
`DB94-1-AC1` -- the contract has the eight sections in the baseline's order, a `document` layout and exactly the 117 baseline members, each with a section and either a source whose contract exists and whose field really occurs in it, or ABSENT with a reason and no value; no vendor or custodian is named anywhere in it; the gap table is bound to the contract's bytes and its totals and per-section counts equal what the contract says; no S3, no vendor call; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB94-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every existing file in `org/standards/`.
- **No S3, no vendor call, no secret read, no deploy, no push, no portal.** You read repo files only.
- **No client data.** The PDF is not in the repo and you do not look for it. Nothing in the contract or the gap table names a client, a household or an account.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W140-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content. Commit with `.tools/safe-commit.sh` as your definition says; ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~140/
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-174.performance-report-contract-and-gap-table.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 96 (round 94), cell `DB-b-174`.
<owned_cells>DB-b-174</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB94-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~140/IRPT_DASHBD.TO-DB-b-174.performance-report-contract-and-gap-table.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB94-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the sourced and ABSENT counts by section; which sibling contracts carry which of the report's figures; whether the FWD-20 map was found; the fee-basis wording you chose; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a contract document and a counts-only gap table; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no contract) and its structure is derived from the baseline by the checker (60 synthetic arms dry-run).
lane: the <paths> block IS the grant.
</preflight>
