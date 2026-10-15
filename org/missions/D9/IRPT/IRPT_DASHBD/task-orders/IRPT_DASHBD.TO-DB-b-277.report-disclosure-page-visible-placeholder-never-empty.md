# TO IRPT_DASHBD.TO-DB-b-277 -- the 49 Financial DISCLOSURE PAGE as a visible placeholder (round 144, workstream B-49F): the default performance report document ends with a disclosure sheet whose slot reads "Disclosure page pending" while no text is supplied; the custody ClientReportDocument's unfilled disclosure slot reads it too; never empty, never invented text

<to_id>IRPT_DASHBD.TO-DB-b-277</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~224</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>144</round>
<workstream>B-49F</workstream>

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-15 ~22:4xZ, on worker rows IRPT_DASHBD-D2-W224-S1, S2 and S3; gate limb: an existing order modified, placeholders NONE unchanged, no criterion id, cell or path change):** three defects of MY order and checker, ruled here. (S1) The pointer constant `INCOMPLETE_WITHOUT_DISCLOSURE` reads `'This report is incomplete without the accompanying disclosure page'` WITHOUT a trailing period (the period in this order's text was Andrew's sentence, not the constant); wherever this order quotes the constant with a period, read it without. The constant stays exactly as it is. (S2) The checker's authored-language scan matched the pre-existing label "Billed advisory fee:"; the phrase `advisory fee` is removed from the scan (the other four stay). (S3) Step 5's "every contract member still appears exactly once" is false of the render (a member prints on several sheets); read it as: **the set of DISTINCT contract member ids the document prints is unchanged by the new sheet** (117 at the base; the new sheet adds none and loses none). Your test already asserts the 117 distinct ids; that satisfies the amended clause. Nothing else changes; `p144_placeholder.py` is updated (its ids and the three criteria are unchanged).

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 144 | **Ordered by:** Andrew, verbatim, via the CTO (org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_213xZ_90EF_PLACEHOLDER_2106_TO_LAPTOP_4608_STOP_J4_CHECKING.md @cf8764df23 (msg 8686)): "We will deal with this later, should just be placeholder for now." The CTO's act: render the `disclosure_text` slot as a VISIBLE placeholder ("Disclosure page pending"): never empty, never invented text; the disclosure composition is no longer gated on the file. | **Decomp cell:** `DB-b-277` (decomposition section 142).

**Risk class LOCAL**: portal files and tests on a portal branch only; no deploy, no push, no AWS call. Nothing here reaches a client: the report stays a release gate and every render stays in the private evidence folder.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-224` (branch `wk-IRPT_DASHBD-224`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~224/`. `C:/dev/wk-irpt-dashbd-224/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-224-portal`), cut from `wk-IRPT_DASHBD-180-portal` (commit `c81d54ff`, the head of the 49 Financial report render lineage; it is NOT merged to DEV). Do not amend or revert anything already committed there except where this order names it. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`; counts, hashes and words only anywhere else.

**Why.** The 49 Financial template Andrew named (a252) holds no disclosure page: its footers say "This report is incomplete without the accompanying disclosure page" and nothing else is prose. Andrew rules that the page is a placeholder for now. The renderer may not author disclosure language (a renderer that writes its own disclosure text is writing compliance copy), so the page reads a VISIBLE placeholder until the firm's own text is supplied: never an empty section, never invented words. Today the default performance report document (`render/performance/report/PerformanceReportDocument.tsx`) has NO disclosure page at all (its eight sections, each sheet closing with the pointer line), and the custody `ClientReportDocument`'s disclosure slot renders NOTHING when it is unfilled.

**The cell (`DB-b-277`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r144/p144_placeholder.py` (your three criteria); `portal/src/pages/InvestorReporting/render/performance/report/PerformanceReportDocument.tsx` and `documentSheets.ts` (the sheet list, `INCOMPLETE_WITHOUT_DISCLOSURE`, `Page n of N`); `render/clientreport/ClientReportDocument.tsx` (the `data-slot="disclosure"` sections of its two status pages); `render/performance/Disclosures.tsx` (read only: NOT edited); the existing tests under `__tests__/irpt-dashbd/` and `__tests__/clientreport/`.
2. **One shared constant.** A new file `portal/src/pages/InvestorReporting/render/disclosurePlaceholder.ts` exports ONE constant whose value is exactly `Disclosure page pending`. That string literal appears NOWHERE else in non-test product source (both renderers import the constant).
3. **The custody document.** In `ClientReportDocument.tsx`, BOTH status pages' disclosure slot (`data-slot="disclosure"`): when the disclosure text is empty or null the section prints one paragraph `<p className="ir-note" data-disclosure-placeholder="true">` holding the constant; `data-slot-state` stays `unfilled`; when text is supplied each paragraph prints verbatim exactly as today and no placeholder prints (`filled`).
4. **The performance report document.** `PerformanceReportDocument` takes two new OPTIONAL props, `disclosures?: readonly string[] | null` and `disclosureVersion?: string | null`, and `documentSheets` gains ONE new LAST sheet: id `disclosures`, titled "Disclosures", no contract member, numbered after the eight sections, so that EVERY sheet's `Page n of N` total counts it and `data-pages` includes it. The document renders it after the eight sections as a `<section data-section="disclosures">` holding one `div.ir-page` with `data-report-page="disclosures"` (header and footer as every other sheet; the footer shows its own `Page n of N`) whose body is `<div data-slot="disclosure" data-slot-state="unfilled|filled" data-disclosure-version="...">`: with no text it prints ONE visible `<p data-disclosure-placeholder="true">` holding the constant; with text each paragraph verbatim in order and no placeholder. **The pointer line stays exactly as it is** (`INCOMPLETE_WITHOUT_DISCLOSURE` = "This report is incomplete without the accompanying disclosure page" (no trailing period), printed on each of the eight sections' sheets); it is NOT printed on the disclosure sheet itself. Every contract member still appears exactly once; the new sheet adds none. **No other word is authored**: no sentence of disclosure, compliance or performance language beside the heading and the placeholder.
5. **Tests and gates.** A new test file `disclosure-placeholder.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/` holds the verdict line `VERDICT: DISCLOSURE-PLACEHOLDER-OK` (printed once, after the last case passes) and at least seven cases: the custody document with empty and with null disclosures prints the placeholder (`data-slot-state` `unfilled`) on both status pages; with text it prints the paragraphs verbatim, `filled`, no placeholder; the report document's LAST sheet is `disclosures` and reads the placeholder when no text is supplied; with text it prints each paragraph verbatim and no placeholder; every sheet's `Page n of N` has N equal to the number of sheets and the last sheet's n equals N; the pointer line prints on the eight sections' sheets and not on the disclosure sheet; every contract member still appears exactly once; the shared constant's value is exactly the words. Plus the MINIMUM edits to existing assertions that pinned the old sheet count, the old `data-pages` or an empty disclosure slot (name each in a row; never weaken an assertion beyond the minimum; at most 40 changed lines across all existing test files). ONE temporary mutant (the report document ignores the supplied text and always prints the placeholder, OR the placeholder branch prints nothing) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
6. **Record** `RD_DISCLOSURE_PLACEHOLDER_R144.json` in your folder with EXACTLY these fields: `claim` ("measured"); `portal` {`branch` "wk-IRPT_DASHBD-224-portal", `commit`, `files_changed` (each under `src/`)}; `constant` {`file` (the new file, under `src/`), `name`, `value` ("Disclosure page pending")}; `branches` exactly `{"client_unfilled": "placeholder", "client_filled": "verbatim paragraphs", "report_sheet": "last sheet, placeholder when no text is supplied", "pointer_line": "unchanged"}`; `tests` {`new_file`, `mutant_failed` true, `lint_errors` 0, `typecheck_errors` 0, `suite_base` and `suite_after` as {pass, skip, fail, new_failing_ids}}; `pushed` false; `deployed` false; `words` (one paragraph, 80 to 1800 characters: what the placeholder is and where it prints, that no disclosure language was authored, and what is NOT proven: how the page looks in a rendered PDF, which the CVO reads at its next render check). Counts, paths, hashes and words only.

<criterion id="DB144-1-AC1" cell_refs="DB-b-277"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r144/p144_placeholder.py" . DB144-1-AC1</invocation><expect>DB144-1-AC1 PASS</expect></criterion>
`DB144-1-AC1` -- the new test file exists, holds the verdict line and the required tokens (the placeholder words, `data-disclosure-placeholder`, the slot states, `disclosures`, the pointer constant, `Page `) and at least seven cases, and passes under two runtime zones (UTC and America/Los_Angeles).
<criterion id="DB144-1-AC2" cell_refs="DB-b-277"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r144/p144_placeholder.py" . DB144-1-AC2</invocation><expect>DB144-1-AC2 PASS</expect></criterion>
`DB144-1-AC2` -- the neighbour tests (every test file of `__tests__/irpt-dashbd/` and `__tests__/clientreport/`, plus the print-kind and custody-print tests; at least twelve) and the new test file pass together under `bun test`.
<criterion id="DB144-1-AC3" cell_refs="DB-b-277"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r144/p144_placeholder.py" . DB144-1-AC3</invocation><expect>DB144-1-AC3 PASS</expect></criterion>
`DB144-1-AC3` -- the words `Disclosure page pending` are ONE string literal in the non-test product source, in a file under `src/pages/InvestorReporting/`, imported by both renderers; ClientReportDocument's two status pages print the placeholder when unfilled and keep `data-slot-state` and the verbatim filled branch; PerformanceReportDocument holds a `disclosures` sheet whose slot carries `data-slot`, `data-slot-state` and the placeholder, takes the text as an optional `readonly string[]` prop, and keeps the pointer constant exactly and its printing; no authored disclosure language appears; the record is complete and bound to a portal commit descending from `c81d54ff`, with nothing pushed or deployed.

<expected_criteria>DB144-1-AC1,DB144-1-AC2,DB144-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `render/performance/Disclosures.tsx`, the contract, the issuer's check files, the generated firm-names file and every portal file outside the render directories, the new test and the neighbour tests named in step 5.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** None is read or recorded; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than the render, file a BLOCKING row naming the clause and stop on it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W224-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
portal/src/pages/InvestorReporting/render/disclosurePlaceholder.ts
portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
portal/src/pages/InvestorReporting/__tests__/clientreport/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~224/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-277.report-disclosure-page-visible-placeholder-never-empty.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 142 (round 144, workstream B-49F), cell `DB-b-277`.
<owned_cells>DB-b-277</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB144-1-AC1, DB144-1-AC2, DB144-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~224/IRPT_DASHBD.TO-DB-b-277.report-disclosure-page-visible-placeholder-never-empty.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB144-1-AC1,DB144-1-AC2,DB144-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; where the placeholder prints in one line; the test count; the mutant result; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: portal files and tests on a portal branch; nothing is pushed, built for production or served; no AWS is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were validated by the issuer's self-test (green and red arms) and its test runs read the neighbour tests at the base (all pass before the cell).
lane: the <paths> block IS the grant.
</preflight>
