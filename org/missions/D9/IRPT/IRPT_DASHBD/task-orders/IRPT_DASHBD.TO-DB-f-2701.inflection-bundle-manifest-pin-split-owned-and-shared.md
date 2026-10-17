# TO IRPT_DASHBD.TO-DB-f-2701 -- the INFLECTION BUNDLE MANIFEST'S PIN SPLIT, ONE cell: the manifest `INF_G_01.bundle.json` marks its 14 shared registry members `shared` with no cut pin (the 5 owned members keep theirs); `build_bundle` compares a shared member against a RECEIPT pin only; the runtime verifies the zip against the receipt beside it; the launcher test file reads green; the CTO's round-138 analysis ruling 4

<to_id>IRPT_DASHBD.TO-DB-f-2701</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2701</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>139</round>
<workstream>F2SPLIT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2SPLIT (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-138 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_138_20261017.md` @aace591b52, msg 10373) ruling 4: "a cell splits the manifest's members into two kinds: owned members, pinned at cut as now; shared registry members (lib/opal_naming.py, exemptions.json, the registry and contract files other lanes write), listed without a cut pin. For a shared member, the release-day cell records the pin in the receipt, and build_bundle compares against that receipt pin, not a cut pin. The cell's criteria: the nine tests read green at HEAD; a planted edit to an owned member still refuses; a planted edit to a shared member does not refuse until a receipt pin exists." | **Decomp cell:** `DB-f-2701` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none.

**Risk class LOCAL:** repo text and offline tests in a branch. No AWS call, no Terraform, no upload, no push. The release-day receipt is the applier's later act, not yours.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2701` (branch `wk-IRPT_DASHBD-2701`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2701/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS: make no AWS call.** No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The launcher's bundle manifest pins the sha256 of all 19 members, 14 of which are files other lanes edit (the registry, `lib/opal_naming.py`, `lib/trading_calendar.py`, the naming schema). Two have drifted, so `build_bundle` REFUSES on the trunk and the launcher test file reads 2 failed, 7 errors, 59 passed. A red baseline hides the next real failure.

**The cell (`DB-f-2701`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_split.py` (your three criteria; `OWNED`, `SHARED`, `manifest_problems`, `scratch_repo`, `try_build` and the AC bodies are the exact spec; it has a `--selftest`), the launcher `data/inf/scripts/gold/INF_G_01.account_transaction_gold.py` (whole: `build_bundle`, `bootstrap`, `EXPECTED_BUNDLE_SHA256`, `manifest_path`), the manifest `data/inf/scripts/gold/INF_G_01.bundle.json`, and the test file `data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py` (its bundle tests, the `built_zip` fixture and `flat_run`).
2. **The manifest:** for each of the 14 SHARED members of the checker's list, remove `sha256` and add `"shared": true`; the 5 OWNED members keep their `sha256` unchanged. Nothing else in the manifest changes (the member list, order and other keys stay).
3. **The launcher:**
   - `build_bundle(root, out_path, receipt=None)`: owned members compared with the manifest's sha256 as now (REFUSED naming the path on a difference); a shared member is compared only with `receipt["shared_pins"][path]` when `receipt` carries one for it (REFUSED naming the path on a difference), else it is packaged as it is. The zip stays deterministic (sorted, fixed stamps and attributes) and the function still returns the zip's sha256.
   - a function `make_receipt(root, zip_path)` returning `{"bundle_sha256": <sha256 of the zip>, "shared_pins": {<each shared member path>: <its sha256>}}` (the applier writes it as JSON on the release day).
   - REMOVE the constant `EXPECTED_BUNDLE_SHA256`. `bootstrap()` reads the expected bundle sha256 from the file `INF_G_01.bundle.receipt.json` BESIDE the zip (the same folder as the zip, whether the zip is `INF_G_01.bundle.zip` beside the launcher or the one named by `INF_IRPT_BUNDLE_LOCAL`), REFUSES naming the receipt when it is absent or lacks `bundle_sha256`, and REFUSES naming the sha256 on a zip that differs from it. The extraction into the temporary repo layout is unchanged.
   - Nothing else in the launcher changes (the window, the plan, the S6 report, `main`).
4. **The tests:** the launcher test file is brought to the new mechanism so that it reads GREEN (0 failed, 0 errors): the nine currently red tests are the bundle tests that build the zip against the manifest; make them build with the manifest as split and, where a test needs the zip verified at run time, write the receipt beside it with `make_receipt` in the fixture. Replace the test of the old constant (`test_bundle_pin_equals_the_built_sha256`) with tests of the new rule. Add at least: a planted edit to an OWNED member refuses naming it; a planted edit to a SHARED member builds with no receipt; the same edit refuses against a receipt pin it differs from and builds against a pin equal to it; `bootstrap` refuses a zip with no receipt beside it, refuses a zip that differs from its receipt, and accepts a zip equal to it; `make_receipt` pins exactly the 14 shared members. Keep every other test as it is.
5. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_split.py" . DBF139-1-AC1`, then `AC2`, then `AC3`. Write `RD_BUNDLE_SPLIT_FACTS_R139.json` in your folder: `claim` ("measured"), `owned` (5), `shared` (14), `tests_before` ({passed, failed, errors}: 59, 2, 7), `tests_after`, `tests_added`, `files_touched` (3).
6. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2701 <0.9.0_WK_IRPT_DASHBD~2701@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): the manifest, the launcher and the test file in one commit, the record and the proof in a second.

<criterion id="DBF139-1-AC1" cell_refs="DB-f-2701" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_split.py" . DBF139-1-AC1</invocation><expect>DBF139-1-AC1 PASS</expect></criterion>
`DBF139-1-AC1` -- the launcher test file reads green at HEAD: no failed and no erroring test (the nine that are red on the trunk read green). Base: FAIL (2 failed, 7 errors).
<criterion id="DBF139-1-AC2" cell_refs="DB-f-2701" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_split.py" . DBF139-1-AC2</invocation><expect>DBF139-1-AC2 PASS</expect></criterion>
`DBF139-1-AC2` -- the manifest is split exactly (5 owned with a sha256, 14 shared flagged with none), the unedited tree builds, and a planted edit to an OWNED member still refuses naming it. Base: FAIL (the manifest is not split).
<criterion id="DBF139-1-AC3" cell_refs="DB-f-2701" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_split.py" . DBF139-1-AC3</invocation><expect>DBF139-1-AC3 PASS</expect></criterion>
`DBF139-1-AC3` -- a planted edit to a SHARED member does not refuse while no receipt pin exists; against a receipt pin it differs from the build refuses naming the member; against a pin equal to the edited file it builds. Base: FAIL (the tree refuses on the already-drifted members).

<expected_criteria>DBF139-1-AC1, DBF139-1-AC2, DBF139-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer modules, the contract, the dispatch script, the registry and lib files, the checker.
- **AWS: none; no Terraform; no upload; no push.** No change to the dispatch script or to any bundle member's bytes.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker or an order sentence is wrong, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2701-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2701/
data/inf/scripts/gold/INF_G_01.account_transaction_gold.py
data/inf/scripts/gold/INF_G_01.bundle.json
data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2701.inflection-bundle-manifest-pin-split-owned-and-shared.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md</decomp_doc> round 139, workstream F2SPLIT (F-SHIP), cell `DB-f-2701`.
<owned_cells>DB-f-2701</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF139-1-AC1, DBF139-1-AC2, DBF139-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2701/IRPT_DASHBD.TO-DB-f-2701.inflection-bundle-manifest-pin-split-owned-and-shared.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2603/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF139-1-AC1,DBF139-1-AC2,DBF139-1-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the pytest line before and after; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the edit is the launcher's bundle build and bootstrap, its manifest and its tests; the launcher's callers are the dispatch script's best-effort block and by-hand release runs (read in round 135), nothing is deployed in this order, and the flat sync's carrying of a receipt file beside the zip is a release-day fact the applier lists.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed; nothing is deployed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF139-1-AC1 to AC3 FAIL at base, a reference manifest and build_bundle(receipt) put into the tree by the issuer made AC2 and AC3 PASS and were restored, and the checker's pure helpers are exercised by its selftest (8 arms).
lane: the <paths> block IS the grant.
</preflight>
