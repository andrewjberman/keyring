# TO DSGN_IRPTV1.TO-IV-e-115 -- an opened vendor report names each section and states each unit: the page maps the section code to its census name and maps the producer's 12 unit tokens -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-115</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~63</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5664 (2026-10-11 ~19:31Z): "TITLE: the page. ... The page maps section_type to the census name: the 33 names COPIED from the pinned census file, its path, pin and sha256 recorded beside the copy, with a test that fails if the copy differs. A code not in the map prints the code. ... UNIT: the page. Map the 12 tokens the producer sends, in its own case; an unmapped token prints the token, never 'unknown'. Fix the fixtures to send real tokens." | **Rows:** DSGN_IRPTV1-D2-S21, DSGN_IRPTV1-D2-W62-S1 | **Decomp cell:** `IV-e-115` (decomposition v27) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** IV-e-113 (drained @7378d53be9: its record is this cell's evidence).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (the slot's worktree; branch `wk-dsgn-irptv1-r21-57`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~63/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the other slot's real install: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~63/`) is your base for `new_failing_ids`.

**What is wrong (row D2-S21, ruled).** On a served vendor report every card's title and Label read as a section code (`S03`) and every
card reads "Unit: unknown". IV-e-113 traced both (read its record first:
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/SECTION_TITLE_UNIT.json`): the vendor section carries no title member on the
wire, only `section_type` = the census code, and the page prints it (`contracts/adapt.ts` near lines 937 and 941); the producer sends 11
lower-case unit tokens plus `chart`, and the page's map `SECTION_UNIT_FOR_WIRE` (`adapt.ts` near 530-537) has six upper-case keys, so
0 of 12 match and the adapter falls to `'unknown'` (near line 944). The CTO ruled both are the PAGE's to fix now; served vendor reports
are immutable and carry only the code. No schema change. The census file is a workspace file you READ; it is not in your grant (AMENDMENT 1) and you do not edit it.

**The cell (`IV-e-115`).**
1. **The 33 names.** The pinned census is `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json` (its `sections` array: 33 entries, each `id` and
   `title`; this seat measured its sha256 as `44853788fa6d39c8b6011c2f86fc82ea6906c2e006935df549f153378c950905`, last changed at
   `45c8fc4eb4`: re-measure both). COPY the 33 (id -> title) into ONE new page module beside the adapter, with the census's path, pin
   and sha256 recorded in that module as constants. A test under `__tests__/dsgn-irptv1/` reads the census file from the workspace
   and FAILS if the copy differs in any id or title or if the census's sha256 is no longer the recorded one (so a census change is seen,
   not silently absorbed); one temporary mutant (a title altered in the copy) makes it fail. `names` {copied, copy_file, drift_test}.
2. **The card's title and Label** for a VENDOR section read the census name for its code; a code not in the map prints the code
   itself (`unmapped_code_prints_code`), and `source_chart_representation` and any other non-code `section_type` prints as it does
   today unless IV-e-113's record shows a census name for it: say what you did. An Opal report's sections are NOT touched: their names
   come from their own member; show with a test that an Opal section's title is unchanged.
3. **The 12 unit tokens.** Take the exact tokens from the producer's code IV-e-113 cites (`extract.py` near 709 and 777: count, date,
   enum, number, pct, price, ratio, score, text, usd_billions, years, and chart), in the producer's own case; map each to what the
   card prints (extend the page's existing unit vocabulary only as far as needed; say each mapping and why). The existing upper-case
   keys stay (an Opal report or an older fixture may send them): show nothing that passed before fails. An unmapped token prints the
   TOKEN, never "unknown" (`unmapped_token_prints_token`); the literal fallback `'unknown'` no longer reaches a card for a non-empty
   token. `units` {tokens, mapped, mapping {token: printed}}.
4. **Fixtures send real tokens.** The page's own vendor-report fixtures (under `fixtures/` and the tests) that send a unit token the
   producer never sends for a vendor report are changed to real tokens and real codes (`fixtures_changed`); the PRODUCER's contract
   fixtures in the workspace are read, never edited: if they too send a token the producer's code cannot, that is a row for
   IRPT_BCKEND, not an edit.
5. A rendered test (a vendor report with real codes and tokens: names and units on the cards; an unknown code and an unknown token
   print themselves; an Opal report unchanged). A screenshot of an opened vendor report from a build with a synthetic fixture, read
   by you. `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`, `portal_commit`. Record `SECTION_NAMES_UNITS.json`.
   Still open on the row and NOT yours: the validation line and the source line of a vendor report.

<criterion id="IV115-AC1" cell_refs="IV-e-115"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r27/p27_round27.py" . IV115-AC1</invocation><expect>IV115-AC1 PASS</expect></criterion>
`IV115-AC1` -- the 33 census names are copied with their source recorded and a test that fails when the copy differs, all 12 unit tokens the producer sends are mapped, an unmapped code or token prints itself, and a screenshot was read. Base: FAIL.

<expected_criteria>IV115-AC1</expected_criteria>

## AMENDMENT 1 (2.0.0_SA_COO~D2, 2026-10-11 ~19:5xZ) -- the census file is NOT in the grant

As issued @2ac7f5ec16 this order's `<paths>` block listed the pinned census file, which made it part of the worker's write surface while
the text said read-only. That was the issuer's error (a generator patch that failed). The file is removed from `<paths>`: reading a
workspace file needs no grant, and the census is never edited by this cell. Nothing else changes; no worker had been spawned. Gate limb
that graded this modification: none (a modification of an issued order; LIMB 6 fires on a newly added order only).

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Every portal commit is followed by `bun run lint` and `bun run typecheck`**; a lint ERROR is fixed before you report (the count goes in
  the record as `lint_errors`, and typecheck's as `typecheck_errors`).
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W63-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~63/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-115.vendor-section-names-and-unit-tokens.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v27 (round 27), cell `IV-e-115`.
<owned_cells>IV-e-115</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV115-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~63/DSGN_IRPTV1.TO-IV-e-115.vendor-section-names-and-unit-tokens.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV115-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the census path, pin and sha256 as you measured them; where the copy lives and the drift test with its mutant; what a card prints for a mapped code, an unmapped code and a chart row; the 12 tokens and what each prints; what an unmapped token prints; the fixtures changed; that an Opal report is unchanged and how shown; what the screenshot shows; `product_files_changed`; lint, typecheck and suite; the portal commit; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; names and unit words on a vendor report's cards, from a table copied from a pinned file with a drift test; no request, route or contract change. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
