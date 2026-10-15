# TO IRPT_DASHBD.TO-DB-c-17 -- the Cottonwood `account_dim` PACKAGE: one new source-map entry (the function's members at pins, sha256-verified) and a build-time test that the staged package resolves the silver locations; repo files only; nothing is built, uploaded, planned or applied

<to_id>IRPT_DASHBD.TO-DB-c-17</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~410</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's decision C (msg 8167: its own package, a `*-cot-*` role, builder names) and the merged code of `DB-c-16` (`infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py`, drain `c4d2b97165`) | **Rows:** IRPT_DASHBD-D2-W410-S<k> | **Decomp cell:** `DB-c-17` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 10) | **outcome_ref:** FWD-2, FWD-11, FWD-15 | **depends_on:** none (`DB-c-16` is merged).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-410`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~410/`. Never push. No client data is read or written. No AWS call is needed or allowed.

**Why.** Lambda zips are built from `infra/aws/lambda/ci/lambda-source-map.json`: each function has an entry listing its `files` and, for every file not tracked under its `source_dir`, a `staged_from` row (the file at a commit `pin`, `packaged_as` its repo path, with its `sha256`). The Cottonwood `account_dim` function (`lambda_function.py` plus the `DB-c-16` adapter) has no entry. You add ONE entry, and one test that the staged package resolves its silver locations, so a missing member fails at build and not at the first invoke. Model the entry on the existing `irpt-holdings-performance-lambda` entry in the same file (read it first; it has the same 13 shared members).

**The cell (`DB-c-17`).**
1. **The entry.** Add to `functions` ONE new key, `irpt-cot-account-dim-lambda` (the builder's name: `lib/opal_naming.py name("irpt", "cottonwood", "account-dim", "lambda")`; run it and confirm it prints exactly that), with these fields and no other: `source_dir` = `infra/aws/lambda/investor-reporting/account-dim-cot`; `files` = exactly these 15: `lambda_function.py`, `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`, and the 13 members of the `irpt-holdings-performance-lambda` entry other than `handler.py` (the producer, its `sources.json`, `stream_parquet.py`, `opal_naming.py`, `trading_calendar.py`, `NAMING_SCHEMA.json` and the seven registry files); `staged_from` = a row for each of the 14 members other than `lambda_function.py` (which is tracked under `source_dir`): the 13 shared ones COPIED BYTE FOR BYTE (same `pin`, same `sha256`, same `packaged_as`) from the holdings entry, and the adapter with `pin` = the full 40-character hash printed by `git log -n1 --format=%H -- data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`, `packaged_as` = its repo path, and `sha256` = the SHA-256 of the file's bytes at that pin (`git show <pin>:<path> | sha256sum`; it must equal the working file's); `tf_file` = `infra/aws/terraform/investor-reporting/account-dim-cot/lambda.tf`; `tf_resource` = `module.irpt_account_dim_cot.aws_lambda_function.this`; `iam_role` = `irpt-cot-account-dim-role`; `pipeline` = `investor-reporting`; `artifact_s3_key` = `investor-reporting/irpt-cot-account-dim-lambda.zip`; plus a `_staged_from_note` and a `_build_note` of one or two sentences each saying what the function does and that its members are staged at their pins (copy the holdings entry's wording where it fits). Do NOT add `artifact_sha256`, `last_deployed_commit`, `last_deployed_at`, `recorded_by` or `deployed_code_sha256`: nothing is built. Add the entry at the end of `functions`, keep the file's formatting byte-for-byte elsewhere (insert only; `git diff --numstat` must show only added lines for the file, no removed line other than the one that gains a trailing comma), and change NO other function's entry.
2. **The test** `infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_package_resolves.py` with `def test_package_resolves_silver_locations_and_target_day` (and helpers). It reads the new entry; materializes EVERY staged member at its pin into a scratch tree under `tmp_path` at its `packaged_as` path (content from `git show <pin>:<repo_path>`, verified against the entry's `sha256`; a mismatch fails the test) and copies `lambda_function.py` from the working tree to the scratch root; then, in a fresh subprocess (`sys.executable -c`, `cwd` = the scratch root, NOT `-I`, because the trading calendar needs the user site packages), imports `lambda_function` from the scratch root and prints as JSON `silver_locations("2026-10-13")` and `target_day(datetime(2026, 10, 14, 12, 30, tzinfo=timezone.utc))`. The test asserts: two `(bucket, key)` pairs, one per silver table, with the same non-empty bucket and keys that end `date=2026-10-13/data.parquet` and differ only in the table segment; and the target day equals `2026-10-13`. The environment variable `ADCOT_SCOPES_PIN`, when set, overrides the pin used for `infra/logic/registry/scopes.json` (content fetched at that commit; the sha256 check of that one member skipped), so the planted control can run. The environment variable `ADCOT_ZIP_PATH`, when set to a built zip, extracts that zip into the scratch tree INSTEAD of materializing from pins, so the applier can run the same test on the real artifact. No network or AWS call.
3. **The planted control** (record it in your report): with `ADCOT_SCOPES_PIN=14b52ca13a467e4be0e47231fb6840611bbb134a` the test MUST fail (that scopes file has no row for the Black Diamond channel, so the producer's firm resolution refuses); without it the test MUST pass.
4. **Do NOT**: build, zip or upload anything; run `build-and-upload.sh`; call AWS; run Terraform; edit any other entry of the source map, any Terraform file, the Lambda, the adapter, the holdings-performance package, the registry or any existing test.

<criterion id="DBC123-1-AC1" cell_refs="DB-c-17"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r123/p123_bcw.py" . DBC123-1-AC1</invocation><expect>DBC123-1-AC1 PASS</expect></criterion>
`DBC123-1-AC1` -- the source map equals its base in every existing entry, gains exactly the one new function entry with exactly the 15 files and 14 staged rows, every pin resolves to its recorded sha256, the 13 shared members carry the holdings entry's pins, the adapter's pin is the working bytes, and no deploy field is present. Base: FAIL.

<criterion id="DBC123-1-AC2" cell_refs="DB-c-17"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r123/p123_bcw.py" . DBC123-1-AC2</invocation><expect>DBC123-1-AC2 PASS</expect></criterion>
`DBC123-1-AC2` -- the named test exists; pytest passes on it with the staged pins; with `ADCOT_SCOPES_PIN` set to the old commit pytest FAILS. Base: FAIL (no test).

<expected_criteria>DBC123-1-AC1, DBC123-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, every Terraform file, the registry, the Lambda, the adapter and every contract.
- **Reads and writes.** Reads: repo files and `git show`. Writes: the files in `<paths>`, your folder and scratch in your private folder. No AWS call, no upload, no Terraform, no invoke, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A source-map shape you cannot edit by insertion alone is a row and a report, never a reformat.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W410-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~410/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-17.cottonwood-account-dim-package-source-map-entry-and-package-test.md
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_package_resolves.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 10, cell `DB-c-17`.
<owned_cells>DB-c-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC123-1-AC1, DBC123-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~410/IRPT_DASHBD.TO-DB-c-17.cottonwood-account-dim-package-source-map-entry-and-package-test.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC123-1-AC1,DBC123-1-AC2` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the source map's `git diff --numstat`; the planted control's outcome (old pin: fail; staged pins: pass); the test's file; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: repo files only; nothing is built, uploaded, planned or applied. The later act's blast (a new function, role and schedule and one partition write) is bounded in the CTO pair packet.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant; the role is DB-c-18's.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed; the schedule is DB-c-18's and is created DISABLED.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC123-1-AC2 plants its own negative control.
</preflight>
