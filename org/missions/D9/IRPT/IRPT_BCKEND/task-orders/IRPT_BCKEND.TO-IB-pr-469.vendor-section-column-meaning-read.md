# TO IRPT_BCKEND.TO-IB-pr-469 -- READ ONLY: what a column of a vendor section IS -- where the producer could know it, one stored report's section ids by code, every consumer of the id's shape

<to_id>IRPT_BCKEND.TO-IB-pr-469</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~324</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>163</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6379 | **Decomp cell:** `IB-pr-469` (decomposition section 155) | **outcome_ref:** FWD-5

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-324/` (bash `/c/dev/wk-irpt-bckend-324`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no fix or member shape.

**Why.** A finished vendor report is served as sections. Each section's id is `<code>.<field slug>.c<column>`
(`infra/aws/lambda/investor-reporting/ycharts/extract/extract.py`, about lines 700-707), and the column is only the ORDINAL of a
value on the located row (about lines 556-606). So two cards of one field share a name, and nothing on the wire says what a
column is: a compared security (codes S01, S03, S18) or a period (S14, S15, S16). The CTO will write a member into the
contract (a column's entity or period, with its claim) and needs three facts first. Start from another project's read:
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~67/SHARED_TITLE_46.json` (code and census only; it derives
36 cards for S18 and could not explain a walked report's 46).

**HARD BOUNDS.** READ ONLY. No Lambda is invoked, no route is called, nobody signs in, no Secrets Manager read, nothing is
written to AWS, no vendor is called. NO figure of a report is written (no `value`), NO account id, NO client or security
name taken from a stored report: section CODES, field SLUGS, column ORDINALS and COUNTS only.

**Read 1 -- where the producer could know what a column is** (`column_label_by_section_code`, one entry for each of `S01`,
`S03`, `S18`, `S14`, `S15`, `S16`). Read `extract.py` whole, its callers in `ycharts/` (the generate and publication modules),
the census `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`, and the synthetic fixtures under
`ycharts/extract/fixtures/`. For each code say `column_is` (`ENTITY`, `PERIOD` or `OTHER`) and ONE `verdict`:
- `READ_AND_DROPPED`: the code reads the label (a header token, an entity name, a period heading) and does not carry it out;
- `ON_THE_PAGE_NEVER_READ`: the label is on the rendered page (shown by a fixture or the census) and no code reads it;
- `HELD_ELSEWHERE_BY_THE_PRODUCER`: the producer holds it outside the page (the request's compared securities, in their
  order; a period list) and the extraction does not join it;
- `NOT_ON_THE_PAGE`; or `NOT_ESTABLISHED`.
Each with `cites` (a list of `path:line`, repo-relative) and `in_words`. Say separately (`column_order_claim`) whether the
ordinal's ORDER is guaranteed to follow the request's security order or the page's left-to-right order, with the line.

**Read 2 -- one stored report** (`stored_report`). Find from the code where a finished vendor report's sections are stored
(the repository or publication module's own address builder; state `address_rule_in_words` with file:line). List that
prefix, take the MOST RECENT stored report that carries S18 sections, get it once, and count its section ids:
`sections_total`; `sections_by_code` (code -> count, summing to the total); for S18 `s18: {stored, predicted_by_the_rule: 36,
distinct_slugs, by_column: {"c0": n, ...}, slugs_with_more_than_two_columns, slugs_absent_from_the_census,
difference_in_words}`; and the same by-column counts for S01, S03, S14, S15, S16 (`other_codes`). State which report by its
stored date only (`report_stored_date`), never by an id that names a person or a firm. Set `read: true`. If the list or
the get is refused, or no stored report carries S18: set `read: false`, state `refusal_in_words` and `address_tried_shape`
(the address with ids replaced by `<...>`), file a row, and go on; try no other identity and no other path.

**Read 3 -- every consumer of the section id's shape** (`consumers_of_the_section_id_shape`). A consumer is any code that
builds, splits, parses, pattern-matches or compares a vendor `section_id`, in the service
(`infra/aws/lambda/investor-reporting/`), the contracts (`docs/contracts/investor-reporting/`), the tests, and the portal
checkout if your worktree has one (`portal/src/pages/InvestorReporting/`; say if absent). Use the native Grep tool. Each:
`{cite: "path:line", reads_the_shape_how: SPLITS_OR_PARSES | COMPARES_WHOLE | BUILDS_IT | DISPLAYS_ONLY, in_words}`. Give the
denominator: `consumer_census: {pattern, files_searched, files_with_a_hit}`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~324/`: `IB163-1_column_meaning.json` with
the keys above plus `base_commit`, `column_order_claim`, `not_established` (a list), and `functions_invoked`,
`sign_ins_made`, `aws_writes_made`, `accounts_written`, `figures_written`, `product_files_edited` each 0; and a one-page
`IB163-1_COLUMN_MEANING_READ.md` leading with the three answers.

<criterion id="IB163-1-AC1" cell_refs="IB-pr-469"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r163/p163_cells.py" . IB163-1-AC1</invocation><expect>IB163-1-AC1 PASS</expect></criterion>
<criterion id="IB163-1-AC2" cell_refs="IB-pr-469"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r163/p163_cells.py" . IB163-1-AC2</invocation><expect>IB163-1-AC2 PASS</expect></criterion>
<criterion id="IB163-1-AC3" cell_refs="IB-pr-469"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r163/p163_cells.py" . IB163-1-AC3</invocation><expect>IB163-1-AC3 PASS</expect></criterion>

<expected_criteria>IB163-1-AC1, IB163-1-AC2, IB163-1-AC3</expected_criteria>

The checks grade the form, the sums and that each cite exists. Every verdict and count is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** an AWS read refused, or a criterion that cannot be met as written: file a row and report. Never weaken
  a check; do not edit `p163_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W324-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~324" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~324@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~324 <0.9.0_WK_IRPT_BCKEND~324@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~324/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-469.vendor-section-column-meaning-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 155 (round 163, workstream ~P), cell `IB-pr-469`.
<owned_cells>IB-pr-469</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB163-1-AC1, IB163-1-AC2, IB163-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~324/IRPT_BCKEND.TO-IB-pr-469.vendor-section-column-meaning-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; per section code what the column is and the verdict with its line; the column
order claim; whether a stored report was read, its counts by code and the S18 difference in words (or the refusal); every
consumer with how it reads the shape, and the census denominator; what is not established; each criterion's last line; the
proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; one list and one get of a stored report by the box's own identity, a refusal being a stated result.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p163_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~03:0xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The CTO's three questions (msg 6379) are the three reads. The vendor path stays stopped: no vendor call, no sign-in. A stored report is read for section ids only; AC2 admits a stated refusal so that a denied read is a result and not a reason to try another identity.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
