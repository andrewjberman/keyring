# TO IRPT_DASHBD.TO-DB-b-185 -- CASH_USD to CASH, cell A (local): the gold ETF classifier's synthetic sweep-cash ticker serves the cash class, in classify and in classify_with_identity; tests updated and a mutant; the count of served positions and the consumers that change; no deploy, no write

<to_id>IRPT_DASHBD.TO-DB-b-185</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~150</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>99</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7401 ("write the CASH_USD packet: every synthetic sweep-cash position that moves, counted, under the same one rule") on the CVO's row IRPT_DASHBD-D2-W147-S3 | **Rows:** IRPT_DASHBD-D2-W150-S<k> | **Decomp cell:** `DB-b-185` (decomposition section 101) | **outcome_ref:** FWD-8 class label, FWD-21 | **depends_on:** none (the round-96 rule is committed at `e340e07f4e`).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-150` (branch `wk-IRPT_DASHBD-150`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~150/`.

**Why.** Andrew's smoke: cash should show as a CASH tagged asset, not Fixed Income. Round 96 made a canonical row typed Cash (by `sub_asset_class`) serve the class `cash` (`_row_class`, commit `e340e07f4e`). One special case is left: `ETFClassifier.classify` (about line 150) and `classify_with_identity` (about line 231) in `data/black_diamond/scripts/gold/lib/etf_classifier.py` answer the synthetic Black Diamond sweep-cash ticker `CASH_USD` with `fixed_income` BEFORE any row is read. So a synthetic cash position still serves fixed_income while a cash-typed fund serves cash. This cell makes the special case serve the same cash class, and counts what changes. It is a LOCAL code change plus a read-only count: nothing is deployed, nothing is written. The class value is `ETFClassifier.CASH_ASSET_CLASS` (`'cash'`; use the constant, not a second literal).

**The cell (`DB-b-185`).**
1. **Read first.** The classifier file in full, and the four classifier test files plus every test file that names `CASH_USD` (find them with `comp-find 'CASH_USD' data/black_diamond/scripts/gold/tests/` and `comp-find --files 'etf_classifier' --limit 20`). Run those tests under `python -I -m pytest` from files BEFORE you edit and record the base pass count (`tests.base_passed`).
2. **The change.** In `classify` and in `classify_with_identity`, the `CASH_USD` special case returns `CASH_ASSET_CLASS` instead of `fixed_income` (the identity version keeps its other three tuple members as they are). It still answers BEFORE the table is read. Change no other line of behaviour; the whole diff against `e340e07f4e` stays under 24 changed lines (the checker counts them). Update the comments that say "kept exactly as it was".
3. **The tests.** Every existing test that pins `CASH_USD` as `fixed_income` is updated to `cash` (name each file in `tests.updated_files`; the composition and advisor-positions tests assert the coarse class of `CASH_USD`: read what each asserts and change only the class). Add ONE new test file next to them with a stub client (no AWS): `CASH_USD` serves cash from `classify` and from `classify_with_identity` in upper and lower case; the client is never asked about it; a row typed Cash, an ordinary `fixed_income` row and an `equity` row are unchanged. ONE temporary mutant (restore `fixed_income` at one site) that a test catches, then reverted (`tests.mutant_failed` true). Run `bash .tools/commit-gate.sh <file>` on every `.py` you touch. Record `tests` {`new_file`, `updated_files`, `passed` (the new file), `failed` 0, `mutant_failed`, `base_passed`, `suite_passed`, `suite_failed` 0} where the suite is the four classifier test files, the new file, and every test file that names `CASH_USD`.
4. **Who assumes the old class (the part the pair will rest on).** Read every consumer of the classifier's class (`comp-pipescript io <script>`; D_03, D_04, C_06, E_25 and the silver asset dim named in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_FDRXX_CASH_CLASSIFIER.md` section 3) and name in `consumers_checked` each one you read (3 or more). Then list in `consumers_assuming_fixed_income` every place that treats a `CASH_USD` position as fixed income on purpose (a sum of fixed-income weight that includes sweep cash, a bucket list, a hard-coded class for the ticker): each `{file, line, what}`. An empty list is a finding too, only if you can say what you searched. Also list in `other_cash_usd_literals` every OTHER place the ticker is hard-coded under `data/black_diamond/scripts/gold/` and `infra/aws/lambda/` (`{file, line}`; you do not change them).
5. **The count.** Read, by S3 GET and LIST only (enumerate what the graph holds with `comp-pipescript io` before you list; the same stores round 96's count read: see `deliverables/0.9.0_WK_IRPT_DASHBD~147/FDRXX_CASH_CHANGE.json`, `served_holdings.stores_read`), the positions whose ticker is `CASH_USD` and whose served `asset_class` is not the cash class today: `served_holdings` {`stores_read`, `positions_scanned`, `positions_that_move`, `positions_already_cash`, `per_firm` (firm -> count, summing to `positions_that_move`), `accounts_with_a_moving_position`}. State in `limits` what the count does not see (partitions or positions beyond the files' top-N, firms not read).
6. **Record** `CASH_USD_CASH_CHANGE.json` in your folder with exactly: `pin` ("e340e07f4e"); `code` {`file`: "data/black_diamond/scripts/gold/lib/etf_classifier.py", `sha256` (of the committed file), `tracked` true}; `tests`; `served_holdings`; `limits`; `consumers_checked`; `consumers_assuming_fixed_income`; `other_cash_usd_literals`; `reads` {`dynamodb_writes` 0, `s3_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `deployed` false; `pushed` false; `served_values_changed` false. Counts and words only: no ticker other than the synthetic `CASH_USD`, no account id, no name, no run of eight or more digits.

<criterion id="DB99-1-AC1" cell_refs="DB-b-185"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r99/p99_round99.py" . DB99-1-AC1</invocation><expect>DB99-1-AC1 PASS</expect></criterion>
`DB99-1-AC1` -- the classifier differs from the round-96 pin by under 24 lines, is tracked and hashes to the stated sha256; run by the checker with a stub client, `CASH_USD` serves cash in both methods (any case) without a table read while a Cash-typed row, a fixed_income row and an equity row are unchanged; tests pass (3 or more new, the suite 37 or more, none failing) with a failing mutant; the served count names its stores, sums per firm and counts accounts; 3 or more consumers are named and the assuming list and literal list are present; no write, deploy or push; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB99-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No write of any kind to AWS** (no DynamoDB, S3, Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: S3 GET/LIST of served holdings stores, repo files. A denial is recorded verbatim, not retried by another route.
- **This change moves served classes once deployed**, which is a later WORLD order under its own never-widen pair; you do not deploy, upload or run the gold job. The file you edit is also the file the FDRXX release ships from the round-96 pin; do not alter lines outside the two special-case sites.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A consumer that depends on `CASH_USD` being fixed_income is a FINDING to list, not something to patch. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W150-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~150/
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-185.cash-usd-serves-cash-cell-a.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 101 (round 99), cell `DB-b-185`.
<owned_cells>DB-b-185</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB99-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~150/IRPT_DASHBD.TO-DB-b-185.cash-usd-serves-cash-cell-a.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB99-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the lines changed against the pin; the tests (base, new, updated files, suite, mutant); the count (positions, per firm, accounts, already cash); the consumers that assume fixed_income (each in one line) and the other literals; what the count does not see; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the change is local and undeployed; the blast radius of the later apply is what the count measures, and its pair will name it.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GET/LIST with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; nothing is released.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
