# TO IRPT_DASHBD.TO-DB-b-225 -- the ACCOUNT LABEL RULE: "ending" prints only before a real digit run of at least 4 digits from a field measured to be the custodian account number, otherwise the label is "Account <n> of <N>"; the Inflection sample relabelled (every value unchanged), the render rule and its test, every page read as an image; private folder only

<to_id>IRPT_DASHBD.TO-DB-b-225</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~180</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>111</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-111 ANALYSIS section 1 (row "The labels") and section 2 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_111_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W180-S<k> | **Decomp cell:** `DB-b-225` (decomposition section 113) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-180` (branch `wk-IRPT_DASHBD-180`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~180/`. `C:/dev/wk-irpt-dashbd-180/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-180-portal`), cut from `wk-IRPT_DASHBD-175-portal` (the branch that carries round 110's Inflection render). Do not amend or revert anything already committed there except where this order names it. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: any account, household or client id, any last four, any text fragment of an account field and any figure are never written in the repo, a row or your report (counts, hashes and words only).

**Why.** The CVO graded round 110's Inflection render FAIL on one count (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_110_L9_GRADE_20261014.md`): three labels read "Account ending 4INT", "Account ending tion (1 of 2)" and "Account ending tion (2 of 2)". "Account ending" promises the last characters of an account number, and these are fragments of a text field: a client cannot read them as an account and they show the shape of the platform's identifier. The CTO ruled: Inflection's `accountNumber` field carries text fragments, not a custodian number. "ending" prints ONLY before a real digit run of at least 4 digits from a field measured to be the custodian account number; otherwise the label is "Account <n> of <N>", with the registration or account name beside it when the source holds one (the sample shape holds none, so none prints). No Inflection field is measured to be that number yet (another cell reads it), so EVERY account of the Inflection sample takes the fallback this round. Everything else of round 110's render stands.

**The cell (`DB-b-225`).**
1. **Read first.** The issuer's check `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r111/p111_labels.py` (your criterion: read it fully, with `label_of`, `render_extras11` and `check_sample`), round 110's records `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/BUILD_R110.json` and `RENDER_R110.json` and harness `~175/render_sample.ts` (copy the harness into YOUR folder as `render_sample.ts`; edit your copy only: its sample path comes from your `BUILD_R111.json`, its output folder is `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r111/`), the round-110 sample the first record names (private client data, read-only), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.5.1) and the components `portal/src/pages/InvestorReporting/dashboard/report/` and `portal/src/pages/InvestorReporting/render/performance/report/` with their tests under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`. Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~180/`) as your base.
2. **Relabel the sample** into `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~180/HOUSEHOLD_SAMPLE.json` (a NEW file; the round-110 sample stays unchanged): the round-110 sample with ONE change, each account's `last4` set to JSON `null` (every value of `values`, the household ref, `as_of`, `first_data_date`, the accounts, their order, their `first_data_date` and `window_status` are byte-for-byte the same). A `last4` of null means: no field is measured to be the custodian account number for this account. Record `BUILD_R111.json` in your folder with exactly: `sample` {`path`, `sha256`, `contract_sha256`}, `accounts` (the integer count), `values_sha256_equal_to_r110` (true: you compared the canonical JSON of `values` of the two samples), `label_basis` (words: no field is measured to be the custodian account number, so every account takes the position label), `orion_guard` (copy `~175/BUILD_R110.json` `orion_guard`), `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Counts, hashes and words only.
3. **Render with no code change first** into `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r111/` (three outputs: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf`; run it in the background and wait for its summary) and read what the checker would find: the components must already cope with a null `last4` or they do not.
4. **The label rule, generic and keyed by the account entry, never by a firm.** One label function used by every place that prints an account label (headers, footers, tables, notes, the note keys' visible text): `Account ending NNNN` when the account entry's `last4` is a string of at least 4 characters that are ALL DIGITS; otherwise `Account <n> of <N>` where n is the account's 1-based position in the household's accounts in account_id order and N the count. Where two accounts that both qualify share a last four, each such label is still followed by ` (k of n)` (round 110's rule). No component derives any other label, and none prints "ending" before anything but a digit run of 4 or more.
5. **Tests and gates.** A new test file `report-render-r111.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/` pins the rule on a synthetic report: a null `last4` prints `Account <n> of <N>`; a fragment of letters (a word), a mix of letters and digits and a digit run under 4 each print `Account <n> of <N>` and the page never contains "ending" before them; a digit run of 4 prints `Account ending NNNN`; two qualifying accounts that share a last four print `(k of n)`; plus the minimum edits to existing assertions the new behaviour requires (round 110's tests asserted "Account ending" for alphanumeric last fours: name each edit; never weaken an assertion beyond the minimum). ONE temporary mutant (a fragment accepted as a number) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
6. **Re-render and read EVERY page.** Render again after your last portal commit into the same folder; the Read tool refuses a PDF: rasterise it with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs PDF> <abs NEW folder under fwd21_sample_r111/pages/> 70` and open EVERY `page_NN.png` with the Read tool (all of them). Look for any label that is not "Account <n> of <N>", a leftover "ending", a header, footer, table row or note that names an account differently from the others, and everything round 110's reading looked for (a figure called unavailable in one place and printed in another, a benchmark that cannot belong to its window, a doubled reason, clipped text). Fix and re-render until clean; record the final render only.
7. **Record** `RENDER_R111.json` in your folder with exactly the fields of round 110's record (`~175/RENDER_R110.json`) PLUS `labels` {`position_labels` (the number of accounts, each printed as "Account <n> of <N>"), `ending_labels` 0} and, inside `tests`, `fragment_test` (the test's name) and `fragment_cases` (a list of words naming the kinds of fragment the test feeds, for example "letters only", "letters and digits", "digit run under 4"). `portal.branch` is "wk-IRPT_DASHBD-180-portal". `sample_sha256` is the relabelled sample's. Counts, paths, hashes and words only.

<criterion id="DB111-2-AC1" cell_refs="DB-b-225"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r111/p111_labels.py" . DB111-2-AC1</invocation><expect>DB111-2-AC1 PASS</expect></criterion>
`DB111-2-AC1` -- the relabelled sample is bound to the contract bytes, passes the kind carrier, the whole-document rule and the equivalence rule, equals the round-110 sample in every value, date, window status and account order and holds a null `last4` for every account; the render clauses of round 109 and round 110 re-bound to your folder (the firm title, all member ids, percents, the dash only for an unheld class, the whole-document and note-level rules with their planted mutants, the account-return and lot sentences, the guard state, the portal commit, a failing mutant, lint 0, typecheck 0, no new failing test, no write, push or deploy); both HTMLs print the gain/loss Ending Value for every account, no "needs more history" for a not-spanned window and one reason per cell; no label reads "Account ending" and every account is labelled "Account <n> of <N>"; `labels` and the fragment test are recorded. Base: FAIL (no record).
<criterion id="DB111-2-J1" cell_refs="DB-b-225" judgment="true"/>
`DB111-2-J1` (JUDGMENT, the CVO's at L9, never the worker's or the issuer's) -- the label pages of the Inflection re-render only (the headers, tables, notes and footers that name an account): no label claims to be an account number that is not one, no label shows the shape of the platform's identifier, and the labels tell the accounts apart in the order of the household.

<expected_criteria>DB111-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the round-110 sample, the issuer's check files, `~175/render_sample.ts`, `firmDisplayNames.generated.ts` (generated) and every portal file outside the two component directories and the tests directory.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** The samples and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of them goes in the repo, a row, a message or your report: counts, hashes and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker's convention or formatting, not the render, is wrong, file a BLOCKING row naming the clause and stop on it. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W180-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~180/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-225.inflection-account-labels-ending-only-before-a-measured-digit-run.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 113 (round 111), cell `DB-b-225`.
<owned_cells>DB-b-225</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB111-2-AC1 (mechanical), DB111-2-J1 (judgment: the CVO's; leave it out of the instance, the validator refuses a judgment row). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~180/IRPT_DASHBD.TO-DB-b-225.inflection-account-labels-ending-only-before-a-measured-digit-run.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB111-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether the SAME components rendered the second firm without a firm-specific edit (and any edit you made, which and why); how every account is now labelled (words and the count); the checker's denominator (cells scanned, absent cells, notes, pointer notes) and that the planted mutants were reported; the PDF's page count and that you read every page (and any you found clipped, or none); lint, typecheck and the suite before and after; the existing assertions you edited. Counts, hashes and words only: no client or account id, no last four, no text fragment, no figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits on a local branch and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB111-2-AC1 FAILS at base (no record) and its label clauses are exercised by the checker's self-test; DB111-2-J1 is the CVO's.
lane: the <paths> block IS the grant.
</preflight>
