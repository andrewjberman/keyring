# irpt-ycharts-generate: three first-party modules missing from the deployed package

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~03:3xZ. Found by the first live Analysis upload, at 03:17Z as the walk principal:
the call answered UNEXPECTED, correlation `corr-32b49d41af2a`, with ModuleNotFoundError `interactive_access`. Log:
`LIVE_UPLOAD_1203_20260926.json` (this folder).

## Measured

The deployed zip `LdjdnnLh5Rqff4VV/tWXS7HY/xKU05+i2uV5gpTIw8Y=` (LastModified 2026-09-24T19:49:52Z) holds 107 members,
56 of them `.py`. An AST import-closure walk from `generate_installed` covers 39 modules. It checks each first-party
import against the P tree `irpt-smoke-p-backend-20260923`, excluding tests, and finds three modules imported in the
closure that the zip does not carry:

| Module | Imported by | Fails at |
|---|---|---|
| `_scope/interactive_access.py` | `served` (:883, for an Opal subject), `generate_installed.compose_upload`, `prospect_submission` | every Opal-viewer request (measured live) |
| `intake/template_reader.py` | `uploads` (`_defer`, `_answer`, `_freeze_template`), `portfolio` | the template upload's first read (the next failure after the first is fixed) |
| `intake/security_resolution.py` | `uploads._freeze_template` | the synchronous template lane; the Lambda's deferred lane does not reach it, but the import closure does |

The miss is Y's composition patch: it added imports without checking the package member list. The offline suites
ran against the full tree, so they could not see it.

## The exact `staged_from` rows

For `infra/aws/lambda/ci/lambda-source-map.json` -> `"irpt-ycharts-generate"` -> `"staged_from"`. Each pin is the file's
last commit on P's branch. Each sha256 is the blob, LF, cross-checked with `sha256sum` for the first row.

```json
{"repo_path": "infra/aws/lambda/investor-reporting/_scope/interactive_access.py", "pin": "9a3ec2a11f47cebd9c1fbc2b0096674fda111be0", "packaged_as": "interactive_access.py", "sha256": "bba07a3f4eeb947bf33845653bde95d47bbb8037d65db4059f4f8b70ebabdf56"}
{"repo_path": "infra/aws/lambda/investor-reporting/intake/template_reader.py", "pin": "d3f612d94d5bfde2ad8c7513fe4fe3988033c023", "packaged_as": "template_reader.py", "sha256": "76795b75313b076488d6c2f0ed7a8480be92b999efb6886a3ede92b11e916409"}
{"repo_path": "infra/aws/lambda/investor-reporting/intake/security_resolution.py", "pin": "d3f612d94d5bfde2ad8c7513fe4fe3988033c023", "packaged_as": "security_resolution.py", "sha256": "8594dcacb8d1c4ba42c5b9b7adb3d1663a5a49d6f16a6a4a3d61b859246d71f1"}
```

## Acceptance after the rebuild

1. `python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/generate_package_closure.py <new zip> --tree <P's investor-reporting dir>`
   must print `OK` and exit 0. Measured at ~03:5xZ: the deployed zip exits 1 with exactly these three MISSING. The same
   zip with the three files added exits 0, and the closure stays at 39 modules, so these three rows are the complete fix.
2. On the next principal window, Y reruns the one upload. Expected: RESOLVING, then the resident's `handled=1`, then
   NORMALIZED 12.03.
