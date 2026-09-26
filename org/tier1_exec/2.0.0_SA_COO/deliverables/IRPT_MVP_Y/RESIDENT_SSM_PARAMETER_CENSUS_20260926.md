# The resident's SSM parameter reads -- census from code (CTO 101348, the resident list)

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~17:1xZ. For `2.0.0_SA_COO~P`'s explicit Deny on `irpt-ycharts-runner-role`
(ssm:GetParameter, GetParameters, GetParametersByPath, GetParameterHistory, with NotResource = `/irpt/render-token/*` plus
the names the host truly reads).

## Result: the resident reads ZERO SSM parameters

**Source.** The deployed package is `/opt/irpt-resident/f624e8a72f`. The unit reads, over SSM at 16:0xZ:
- `ExecStart=/usr/bin/python3.12 .../ycharts/generate/resident_main.py --factory resident_installed:build_resident_runtime`;
- `Environment=PYTHONPATH=...` and `PYTHONUNBUFFERED=1`; no parameter is named.

Its first-party source is `git archive f624e8a72f infra/aws/lambda/investor-reporting`.

**Two scans:**

1. **An SDK-call census of the resident's import closure** from `resident_main` + `resident_installed`: 52 modules,
   51 call sites. There are 0 `get_parameter`, `get_parameters` or `get_parameters_by_path` calls, and no
   `boto3.client("ssm")`. The clients are dynamodb, s3, secretsmanager and sqs (`resident_installed.py:206-210`).
2. **A text scan of the WHOLE first-party tree**, 362 files (.py, .sh, .json, .service, config), for an SSM client, a
   get_parameter call, `GetParameter`, `ssm get-parameter`, or a `{{ssm:...}}` reference. There are 6 hits, and none is
   the resident's:
   - `directory/refresh.py:655, :669, :699`: SSM Run Command (send_command, get_command_invocation,
     describe_instance_information), in the directory-refresh Lambda, not a parameter read.
   - `export/dispatch.py:70`: the export Lambda's ssm client, which is P's render-token path.
   - `_scope/global.py:139-140`: `_ssm_reader(name)`, the Opal roster read. `global` is a keyword, so it can only be
     imported dynamically. The only dynamic importer in the tree is `_scope/tests/test_global.py:28`, a test (scan over
     265 .py files). No non-test module loads it, so the resident does not reach it.

**The resident's contribution to NotResource: none.** The Deny needs only P's host-script names, such as
`/irpt/render-token/*`.

## What this census cannot see

- **The SSM Agent's own calls** (AmazonSSMManagedInstanceCore). It is AWS's binary, not IRPT code. Y's journal reads use
  the `AWS-RunShellScript` document, which references no parameter.
- **Third-party packages in the resident's site-packages** (boto3, botocore, pdfplumber and others). None is configured
  to read a parameter by the resident's code.

## Post-apply controls Y will run

1. Re-run the 40 resident pairs (`iam_hop3_pairs.py simulate irpt-ycharts-runner-role`, @2789ac3bbd): all 40 must still be
   met.
2. One `AWS-RunShellScript` journal read (`live_walk/resident_journal.py`): it must still return the resident's
   `IRPT_RESIDENT_POLL` lines, proving Run Command on this host survives the Deny.
