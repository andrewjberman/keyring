# TO IRPT_DASHBD.TO-DB-f-2705 -- the INFLECTION LAUNCHER ASSUMES THE TRANSACTION ROLE AND RUNS FROM A FLAT DIRECTORY, ONE cell: `assumed_s3_client` (fixed session name, builder-made role name, REFUSED naming the role), `main` uses it, and the naming registry is read through the verified bundle when the launcher is outside the repo layout; the CTO's route-B ruling, msg 10542

<to_id>IRPT_DASHBD.TO-DB-f-2705</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2705</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>139</round>
<workstream>F2INFASSUME</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2INFASSUME (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 10542 (route B): the launcher assumes the narrow account-transaction role for its reads and writes. The flat-directory defect is the issuer's measurement inside the same file. | **Decomp cell:** `DB-f-2705` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md`, amendment 3) | **outcome_ref:** FWD-5 | **depends_on:** `DB-f-2701` (merged).

**Risk class LOCAL:** repo text and offline tests in a branch. No AWS call, no Terraform, no upload, no push. The tests inject fake STS and S3 objects.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2705` (branch `wk-IRPT_DASHBD-2705`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2705/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS: make no AWS call** (the tests never reach boto3's network; STS and S3 are injected fakes). No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** (a) The runner role cannot write the Inflection gold bucket (its fence admits only `role/*-inf-*`); the policy now lives on a role the builder names, which the runner assumes (cell `DB-f-2704`), so the launcher must assume it. (b) Measured: from a flat directory (launcher, bundle zip and receipt only), `orion_prefix()` raises "REFUSED: the naming registry is read from the repo layout only", before the bundle is opened, so the release run cannot reach its first S3 call.

**The cell (`DB-f-2705`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_assume.py` (your three criteria; `FakeSts`, `arn_problems`, `ac1`, `ac2`, `ac3`, `FLAT_SCRIPT` are the exact spec; it has a `--selftest`), the launcher `data/inf/scripts/gold/INF_G_01.account_transaction_gold.py` (whole: `_firm_row`, `orion_prefix`, `bootstrap`, `_repo_root`, `_producers`, `main`), and the test file `data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py` (its `FakeS3`, `line`, `put_partition` helpers and the flat-directory test).
2. **The launcher (ONE file; no other file but its test file):**
   - a module constant `SESSION_NAME = "g01-account-transaction"`;
   - `_firm_row()`: when `_repo_root()` is None, take the root from `bootstrap()` (the verified bundle, extracted in the repo layout; it carries `lib/opal_naming.py` and the registry) instead of REFUSING. The repo-layout path is unchanged;
   - `role_name()`: the builder-made name, `opal_naming.name("orion", "inflection", "account-transaction", "role")`, obtained after `_firm_row()` has put the `lib` folder on `sys.path`; never typed;
   - `assumed_s3_client(sts=None, client_factory=None)`: `sts` defaults to `boto3.client("sts")` and `client_factory` to `boto3.client` (import boto3 inside the function); the account is `sts.get_caller_identity()["Account"]`; call `sts.assume_role(RoleArn="arn:aws:iam::<account>:role/<role_name()>", RoleSessionName=SESSION_NAME)` exactly once; build the client with `client_factory("s3", aws_access_key_id=..., aws_secret_access_key=..., aws_session_token=...)` from the returned credentials and return it. If the assume raises, `raise SystemExit("REFUSED: could not assume role <role> as session <SESSION_NAME> (<exception class name>)")`: the role is named, the account id and the exception text are not;
   - `main(argv, s3=None)`: when `s3` is None use `assumed_s3_client()` (no `boto3.client(` call remains in `main`) and print one line `INF_G_01 assumed role <role> session <SESSION_NAME>`; with an injected `s3` make no STS call and print no such line.
   - Nothing else changes (the window, the plan, the S6 report, the bundle build, the receipt).
3. **The tests:** in the test file add (keep every other test as it is, and the file GREEN: 0 failed, 0 errors): `assumed_s3_client` with a fake STS and factory (the ARN, the fixed session name, the credentials reach the factory, one assume call); a failing assume REFUSES naming the role and not the account id; `main` with no injected client calls `assumed_s3_client` once (monkeypatched) and with an injected client does not; and a FLAT-directory dry run through `main(--date ... --dry-run, s3=<FakeS3 holding one snapshot>)` from a copy of the launcher with the built zip and its receipt beside it, in a subprocess under `python -I`, printing the run and S6 lines and making no put (the shape of `FLAT_SCRIPT` in the checker).
4. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_assume.py" . DBF139-5-AC1`, then `AC2`, then `AC3`; then `python -m pytest data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py -q`. Write `RD_INF_LAUNCHER_ASSUME_FACTS_R139.json` in your folder: `claim` ("measured"), `tests_before` ({passed, failed, errors}), `tests_after`, `tests_added`, `files_touched` (2).
5. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2705 <0.9.0_WK_IRPT_DASHBD~2705@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): the launcher and the test file in one commit, the record and the proof in a second.

<criterion id="DBF139-5-AC1" cell_refs="DB-f-2705" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_assume.py" . DBF139-5-AC1</invocation><expect>DBF139-5-AC1 PASS</expect></criterion>
`DBF139-5-AC1` -- `assumed_s3_client` builds the role ARN from the caller account and the builder-made role name, assumes it once with the fixed session name, passes the temporary credentials to the S3 client factory, and a failed assume REFUSES naming the role and never the account. Base: FAIL (no `SESSION_NAME`, no `assumed_s3_client`).
<criterion id="DBF139-5-AC2" cell_refs="DB-f-2705" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_assume.py" . DBF139-5-AC2</invocation><expect>DBF139-5-AC2 PASS</expect></criterion>
`DBF139-5-AC2` -- `main` with no injected client uses `assumed_s3_client()` once and runs with its client; with an injected client it makes no STS call; no `boto3.client(` call remains in `main`. Base: FAIL (`main` builds a plain client).
<criterion id="DBF139-5-AC3" cell_refs="DB-f-2705" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_assume.py" . DBF139-5-AC3</invocation><expect>DBF139-5-AC3 PASS</expect></criterion>
`DBF139-5-AC3` -- a flat-directory dry run (launcher, zip, receipt only, under `python -I`) completes against a fake S3 holding one synthetic snapshot, prints the run and S6 lines and writes nothing. Base: FAIL (the naming refusal).

<expected_criteria>DBF139-5-AC1, DBF139-5-AC2, DBF139-5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer modules, the manifest, the dispatch script, the registry and lib files, the checker.
- **AWS: none; no Terraform; no upload; no push.** No change to any bundle member's bytes (the bundle's pins must still hold: the launcher is not a bundle member).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker or an order sentence is wrong, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2705-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2705/
data/inf/scripts/gold/INF_G_01.account_transaction_gold.py
data/inf/scripts/gold/tests/test_INF_G_01_account_transaction_gold.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2705.inflection-launcher-assumes-transaction-role-flat-directory-naming.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md</decomp_doc> round 139, workstream F2INFASSUME (F-SHIP), cell `DB-f-2705`.
<owned_cells>DB-f-2705</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF139-5-AC1, DBF139-5-AC2, DBF139-5-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2705/IRPT_DASHBD.TO-DB-f-2705.inflection-launcher-assumes-transaction-role-flat-directory-naming.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2701/IRPT_DASHBD.TO-DB-f-2701.inflection-bundle-manifest-pin-split-owned-and-shared.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF139-5-AC1,DBF139-5-AC2,DBF139-5-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the pytest line before and after; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the edit is the launcher's client construction and one naming read, plus its tests; the launcher's callers are the dispatch script's best-effort block and by-hand release runs, nothing is deployed in this order.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM object is changed (the role is cell DB-f-2704).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed; nothing is deployed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF139-5-AC1 to AC3 FAIL at base, a reference launcher put into the tree by the issuer made all three PASS and was restored with git checkout, and the checker's pure helpers are exercised by its selftest (8 arms).
lane: the <paths> block IS the grant.
</preflight>
