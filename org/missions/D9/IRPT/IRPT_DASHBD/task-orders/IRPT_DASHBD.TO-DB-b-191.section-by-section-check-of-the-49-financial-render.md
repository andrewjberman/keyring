# TO IRPT_DASHBD.TO-DB-b-191 -- the SECTION-BY-SECTION CHECK: a seat other than the builders renders the filled 49 Financial sample through the fixed components and reads the eight sections against the baseline schema, PRESENT / PARTIAL / ABSENT with the reason for each

<to_id>IRPT_DASHBD.TO-DB-b-191</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~156</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7451, ENRICHMENT item 4 ("a seat other than the builder reads each of the renders against the baseline schema and prints, per section, PRESENT / PARTIAL / ABSENT with the reason. This is a JUDGMENT criterion, graded at L9.") narrowed to the one firm that has a render | **Rows:** IRPT_DASHBD-D2-W156-S<k> | **Decomp cell:** `DB-b-191` (decomposition section 103) | **outcome_ref:** FWD-21 | **depends_on:** `DB-b-187` (the fixed components and harness) and `DB-b-189` (the filled sample); this order is spawned after both drain.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-156` (branch `wk-IRPT_DASHBD-156`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~156/`. `C:/dev/wk-irpt-dashbd-156/portal` is a PORTAL worktree cut from the branch that carries the fixed components (`wk-IRPT_DASHBD-152-portal`); `node_modules` there is a LINK to the real install (no `bun install`, never delete it); resolve bun with `command -v bun`. You edit NO portal file and no component, harness or builder.

**Why.** FWD-21's done-when includes "checked section by section against the baseline by a seat". You are that seat: you did not build the sample, the components or the harness, so you read the render fresh. The baseline is the Black Diamond 49 Financial performance report; its structure (never its data) is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`. The contract is `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (117 members, each with a `section`; the eight sections in order are `cover`, `portfolio_overview`, `summary_of_portfolio_accounts`, `holdings_overview`, `taxable_realized_gain_loss_ytd`, `account_overview`, `gain_loss_review_by_account`, `disclosure`). Only 49 Financial has a render: Cottonwood and Inflection have no gold yet (round 101's `DB-b-190` reads why), so they are recorded as not built.

**The cell (`DB-b-191`).**
1. **Render the filled sample** with the fixed harness: the harness is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~152/render_sample.ts` (read its folder's record `RENDER_FIX.json` and, beside it, `~146/README.txt` for the run: from the portal, `bun <abs path to the harness> <abs path to the report JSON> <abs path to the output folder>`). The report JSON is the filled sample from round 101's builder cell: `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~154/HOUSEHOLD_SAMPLE.json` (client data; read-only). Write the outputs to the NEW private folder `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r101_final/` (three files: the tab HTML, the export HTML, the export PDF; the harness names them).
2. **Read the PDF as an image, page by page** with the Read tool (`pages` "1-5", "6-10", ...), and read the baseline schema beside it. Record one entry per page in `pdf_clipping` (`{page, clipped (bool), note (one short sentence; no figure, name or account number)}`).
3. **Tabulate each of the eight sections** in the baseline's order: `{section, members_total (the contract's count of members in the section), members_filled (the number of that section's members that hold a value, not the absent form, in the filled sample: count them from the sample), state, reason, seen_in_render}`. `state` is `PRESENT` when every member is filled, `ABSENT` when none is, else `PARTIAL` (the checker recomputes it). `reason` says in a sentence why the section is not fully present (which kinds of member are absent and why, using the absent reasons the render prints), or "all members filled". `seen_in_render` says in a sentence what you saw on the pages of that section in the PDF (its heading, its tables, its charts, its absent notes, its footer, and whether it matches the baseline's section as the schema describes it): that is the judgment this cell exists to give; be specific and plain; no figure, name or account number.
4. **Record** `SECTION_CHECK.json` in your folder with exactly: `checked_by` ("0.9.0_WK_IRPT_DASHBD~156"); `sample_sha256` (of the filled sample above); `outputs` {`tab_html`, `export_html`, `export_pdf`: each `{path, sha256, bytes}` of the file in the private folder}; `export_pdf_pages` and `pdf_pages_read` (both the PDF's page count); `pdf_clipping`; `firms_checked` (["49financial"]); `firms_not_built` (["cottonwood", "inflection"]); `sections` (eight entries in order); `baseline_schema_read` (the repo-relative path of the baseline schema file you read); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure, no run of eight or more digits (a path under a key named `path` is exempt).

<criterion id="DB101-5-AC1" cell_refs="DB-b-191"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r101/p101_round101.py" . DB101-5-AC1</invocation><expect>DB101-5-AC1 PASS</expect></criterion>
`DB101-5-AC1` -- the record is by a worker other than the builders, bound to the filled sample, with the three renders in the private folder (never the repo) hashing as recorded; the PDF's page count equals pages read with an entry per page; the eight sections appear in the baseline's order with the member counts and the filled counts the contract and the sample give and the state they imply, each with a reason and what was seen; only 49 Financial is checked and the other two firms are stated not built; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).
<criterion id="DB101-5-J1" cell_refs="DB-b-191" judgment="true"/>
`DB101-5-J1` (JUDGMENT, graded by the CVO at L9, never by the worker or the issuer) -- each section's `seen_in_render` is a faithful reading of the render against the baseline schema: the right section, the right members, the absent notes as printed, nothing claimed that the PDF does not show.

<expected_criteria>DB101-5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every portal file, the harness, the builder, the contract, the sample and the baseline.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`.
- **Client data.** The sample and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of them goes in the repo, a row, a message or your report: counts, hashes and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A defect you find in the render is a ROW (OBSERVATION) with the section and what you saw, never a fix. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W156-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~156/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-191.section-by-section-check-of-the-49-financial-render.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 103 (round 101), cell `DB-b-191`.
<owned_cells>DB-b-191</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB101-5-AC1 (mechanical), DB101-5-J1 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~156/IRPT_DASHBD.TO-DB-b-191.section-by-section-check-of-the-49-financial-render.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB101-5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per section the state and the filled count of the total, in one line each; the PDF's page count and the pages you found clipped (or none); the three defects you rank worst (words only); any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a local render and a read; nothing is changed, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB101-5-AC1 FAILS at base (no record) and is dry-run on 7 synthetic arms; DB101-5-J1 is a judgment criterion for the CVO.
lane: the <paths> block IS the grant.
</preflight>
