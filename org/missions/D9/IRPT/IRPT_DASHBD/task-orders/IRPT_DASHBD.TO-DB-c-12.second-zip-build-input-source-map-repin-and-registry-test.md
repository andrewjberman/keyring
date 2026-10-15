# TO IRPT_DASHBD.TO-DB-c-12 -- the BUILD INPUT for the second shared zip: the SOURCE-MAP RE-PIN of `scopes.json` (the `pin` and `sha256` of one entry in two function entries, nothing else) and the BUILD-TIME TEST that the staged registry resolves the 49 Financial, Inflection and `z09` keys, with a planted negative control; repo files only; nothing is built, uploaded, planned or applied

<to_id>IRPT_DASHBD.TO-DB-c-12</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~407</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's conditions on the addendum (msg 8055: "Re-pin scopes.json to HEAD's registry, the build input, not a hand edit. Add a build-time test that the zip's scopes.json resolves each function's registry key (49F, INF, z09); one test, no monitor."), the read `deliverables/0.9.0_WK_IRPT_DASHBD~406/SCOPES_PIN_READ_R118.json` and the unsigned addendum `deliverables/0.9.0_WK_IRPT_DASHBD~406/NEVER_WIDEN_ADDENDUM_DB-c-11_R118.md` | **Rows:** IRPT_DASHBD-D2-W407-S<k> | **Decomp cell:** `DB-c-12` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 6) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** none (`DB-c-11` is merged).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-407`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~407/`. Never push. No client data is read or written. No AWS call is needed or allowed.

**Why.** The shared holdings-performance zip is built from `infra/aws/lambda/ci/lambda-source-map.json`. Its `scopes.json` member is staged at a pin (`14b52ca13a...`) that has no `z09` row, so the Cottonwood function cannot resolve its firm. Round 118 proved that re-pinning `scopes.json` alone, to `69679b90e3dc52b670d33fddd96d06be1deaac90` (sha256 `6ce64167c26588521fded21330dc59e0109450e9a01c92e0f6ca9aa90b53cfae`), makes `z09` resolve to `cottonwood` and leaves every value the 49 Financial and Inflection channels derive identical. The CTO ordered the fix as a committed change to the build input, plus one build-time test, so this class of gap fails at build and not at the first live invoke.

**The cell (`DB-c-12`).**
1. **The re-pin.** In `infra/aws/lambda/ci/lambda-source-map.json`, in `functions["irpt-holdings-performance-lambda"].staged_from` and `functions["irpt-inf-holdings-performance-lambda"].staged_from`, the entry whose `repo_path` is `infra/logic/registry/scopes.json`: set `pin` to `69679b90e3dc52b670d33fddd96d06be1deaac90` and `sha256` to `6ce64167c26588521fded21330dc59e0109450e9a01c92e0f6ca9aa90b53cfae`. Verify first that `git show 69679b90e3dc52b670d33fddd96d06be1deaac90:infra/logic/registry/scopes.json | sha256sum` equals that sha256, else STOP. Change NOTHING else in the file: not another member, not another function's entry, not a note or a field. Keep the file's formatting byte-for-byte except those four values (edit with a text replacement of the old pin and old sha256 inside those two entries only, or with a script that rewrites only those lines and preserves the rest exactly; check `git diff --numstat` reads `4 4` for the file).
2. **The build-time test** `infra/aws/lambda/investor-reporting/holdings-performance/tests/test_zip_registry_resolves.py` with `def test_staged_registry_resolves_each_function_key` (and helpers): it reads the source map's `irpt-holdings-performance-lambda.staged_from`, materializes EACH staged member at its pin into a scratch tree under `tmp_path` in the zip's layout (`packaged_as` path; content from `git show <pin>:<repo_path>`, verified against the entry's `sha256`; a hash mismatch fails the test), adds `handler.py` unneeded, then, in a fresh `python -I` process with the scratch tree as the root on `sys.path` (and `data/assets/scripts/gold/irpt_holdings_performance` and `data/assets/scripts/lib` under it), calls the producer's own `holdings_performance.firm_scope(src)` for each channel entry of the staged `sources.json` (`schwab_08335338`, `orion`, `blackdiamond_z09`) and asserts the results are `49financial`, `inflection` and `cottonwood`. The environment variable `HP_REGISTRY_SCOPES_PIN`, when set, overrides the pin used for `infra/logic/registry/scopes.json` (the content is fetched at that commit and the sha256 check for that member is skipped), so the planted negative control can be run. An optional environment variable `HP_ZIP_PATH`, when set to a path of a built zip, extracts that zip into the scratch tree INSTEAD of materializing from pins (so the applier can run the same test against the actual built zip before upload). The test makes no network or AWS call.
3. **The planted negative control** (record it in your report): run the test with `HP_REGISTRY_SCOPES_PIN=14b52ca13a467e4be0e47231fb6840611bbb134a`; it MUST fail (z09 refused). Run it without the variable; it MUST pass.
4. **Do NOT**: build, zip or upload anything; run `build-and-upload.sh`; call AWS; run Terraform; edit any other function's source-map entry, any Terraform file, the producer, the declaration or the registry; edit the existing tests.

<criterion id="DBC119-1-AC1" cell_refs="DB-c-12"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r119/p119_bcw.py" . DBC119-1-AC1</invocation><expect>DBC119-1-AC1 PASS</expect></criterion>
`DBC119-1-AC1` -- the source map equals the base (the commit this round was issued at) in everything except the `scopes.json` entry's `pin` and `sha256` in the two holdings-performance function entries, which are the new pin and sha256; the file's diff is exactly one pin line and one sha256 line per function; no file outside the source map and the test changed under `infra/aws`, `infra/logic` or the producer's folder. Base: FAIL.

<criterion id="DBC119-2-AC1" cell_refs="DB-c-12"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r119/p119_bcw.py" . DBC119-2-AC1</invocation><expect>DBC119-2-AC1 PASS</expect></criterion>
`DBC119-2-AC1` -- the test file exists with a `test_` function; pytest passes on it with the staged pins; with `HP_REGISTRY_SCOPES_PIN` set to the old commit pytest FAILS. Base: FAIL (no test).

<expected_criteria>DBC119-1-AC1, DBC119-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, every Terraform file, the registry, the producer and every contract.
- **Reads and writes.** Reads: repo files and `git show`. Writes: the files in `<paths>`, your folder and scratch in your private folder. No AWS call, no upload, no Terraform, no invoke, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A source-map shape you cannot edit by value replacement alone is a row and a report, never a reformat.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W407-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~407/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-12.second-zip-build-input-source-map-repin-and-registry-test.md
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/holdings-performance/tests/test_zip_registry_resolves.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 6, cell `DB-c-12`.
<owned_cells>DB-c-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC119-1-AC1, DBC119-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~407/IRPT_DASHBD.TO-DB-c-12.second-zip-build-input-source-map-repin-and-registry-test.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC119-1-AC1 DBC119-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the source map's `git diff --numstat`; the negative control's outcome (old pin: fail; staged pin: pass); the test's file; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: repo files only; nothing is built, uploaded, planned or applied. The later act's blast (one zip upload, a code update on three functions, then the catch-up) is bounded in the addendum for the CTO's half.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed; the Cottonwood schedule stays DISABLED.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; both criteria FAIL at base and DBC119-2-AC1 runs the planted negative control itself.
</preflight>
