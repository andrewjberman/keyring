# NFRA_OPLGTW task order -- `OG-gt-5` -- `harvest_get_published_analysis` (invokes `opal-amgt-scoped-api`), its grant file and its own never-widen ask

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-5</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~76</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-5` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

`harvest_get_published_analysis` (invokes `opal-amgt-scoped-api`) with its read-grant file and its own never-widen ask; ships only when that ask is signed.

### The base you build on (cell OG-gt-0, ALREADY ON YOUR HEAD): `app/harvest_typed.py`, exactly this surface

- `admit_typed(tool, ref, *extra) -> Optional[dict]`: the refusal dict, else `None`. It wraps `harvest_read.admit` (principal
  present, Opal user, served prefix; one audited refusal). Call it FIRST, before any S3 call.
- `audit_ok(tool, ref, nbytes) -> None`: the one audit row of a served call.
- `refusal(message, code) -> dict`: `{"error", "code", "guard_denied": True}`.
- `envelope(body, *, as_of, source_keys, denominator, absent_reason=None) -> dict`: returns
  `{"as_of", "source_keys", "denominator", "absent_reason", **body}`, projected to 50 KB.
- `project(out, limit=51200) -> dict`: when the JSON size exceeds `limit`, pops items off the end of the largest list
  field until it fits, sets `"truncated": True` and `"projected_to_bytes"`.
- `list_keys(prefix) -> list[{"key", "size", "last_modified"}]`: every page, no Delimiter, auto-paginated.
- `newest_part(prefix) -> Optional[str]`: for a prefix laid out `<prefix>date=YYYY-MM-DD/part-<stamp>.parquet`, the key
  with the greatest `(date partition, part file name)`; `None` when there is no `.parquet`.
- `read_parquet(key, columns=None, filters=None) -> (rows, total_rows, nbytes)`: columns projected at read; `filters` is
  a list of `(column, op, value)` with op in `=`, `<`, `>`, `in` (a string value is coerced to the column's date type).
- `read_json(key) -> (obj, nbytes)`: `.json` and `.json.gz`, capped.
- `TYPED_MAX_BYTES` (64 MiB): the cap on one object read; over it, `harvest_over_cap`.

**Rules of the seam.** A tool module NEVER imports `get_current_principal` or boto3: it reaches S3 and the principal only
through `harvest_typed`, so one probe patch point (`app.harvest_read.get_current_principal`) governs every tool. Each tool
is a TOP-LEVEL function in your module with exactly the tool's name and the inputs below, returns a dict, and every success
carries `as_of`, `source_keys`, `denominator` and `absent_reason` through `envelope(...)`. A key you were asked about that is
absent returns an empty body with `absent_reason` set (a string naming WHY), never an error and never silence.

### The tool (G1 section 3, lines 75-86 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`) and its own never-widen ask. PHASE A ONLY: build, grant file, ask. NO apply, NO deploy.

Module `infra/aws/ec2/opal-gateway/app/harvest_published.py`.

1. **`harvest_get_published_analysis(security_key: str, sections: str = "overlay")`**. `sections` is one of `overlay | thesis |
   peers | ledger | versions | timeline` (else `harvest_bad_argument`). Returns the published (portal) body per section,
   projected to 50 KB: header figures, posture, price movement and rank, chatter standing, peers, model cases with
   formula, dossier and drafted section titles, versions. It reads by INVOKING the Lambda `opal-amgt-scoped-api` (the live
   published layer; no second reader). Read the published-layer routes in
   `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md` (section naming the routes)
   and the Lambda's handler source (find it with `comp-find 'opal-amgt-scoped-api' --files`; read, do not run) to build the
   invoke payload and to see which credentials the handler needs. The Lambda is invoked through ONE injectable function
   `_invoke(function_name, payload) -> dict` (module scope, boto3 created inside it, so a test replaces it and `comp-iam`
   resolves the call). `admit_typed` runs FIRST; a refusal makes ZERO invokes. The function name comes from the naming
   builder output, never typed from memory (`python -c "import sys; sys.path.insert(0,'lib'); import opal_naming"`; name the
   call you used in a comment).
   **Ruling A1 (issuer, on your rows S2 and S5):** the live function is `opal-amgt-scoped-api`, which the builder does not produce, and the naming gate refuses it as a NEW
   literal in code (no override). So the module NEVER holds the function name: it reads it from the environment key `AMGT_SCOPED_API_FUNCTION` at call time (`os.environ.get`); unset
   returns the error dict `harvest_published_unavailable` with zero invokes. The value is written by the gateway deploy script: add the line for that key (value `opal-amgt-scoped-api`) to the `printf`
   that writes `.env` in `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (a shell file the gate does not grade). The ask names the new `.env` key as one of its triggers and as part of the diff; the tests set
   the env key. Your row S1 (a security key refused as not served): the ref you pass to `admit_typed` must start with a served prefix; pass `amgt/security/<key>` with a `<key>` that has no `..`.
2. **The grant file**, `infra/aws/terraform/opal-gateway/harvest_published_invoke_iam.tf`: ONE `aws_iam_role_policy`
   named by the builder, `lambda:InvokeFunction` on the ONE function ARN of `opal-amgt-scoped-api` (no wildcard, no
   `lambda:*`, no other action), attached to the role whose credentials `_invoke` uses: the gateway instance role
   `aws_iam_role.gw` unless you find that `_invoke` is to run under `aws_iam_role.int_reader`, in which case that role.
   Say which and why in the ask. Run a targeted plan through `safe-apply` plan mode (never bare `terraform`) and record it:
   1 to add, 0 to change, 0 to destroy.
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-gt-5.md`, for the three halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`). It
   names SEVEN items, each under a heading containing its word: (1) the `diff` by file; (2) the `tool`, its inputs, and its
   `refused` arms (non-Opal, bad section, over-projection); (3) the `widening`, stated plainly: the gateway's reach grows to
   INVOKE one named Lambda, for Opal principals only; (4) the `grant` (the one policy, its builder name, the action, the one
   ARN, the plan line); (5) `both branches` of a call (refused: zero invokes; admitted: one invoke); (6) the order of acts and
   the `rollback` (redeploy the prior release; destroy the one policy); (7) the `triggers` that prove it (tools +1 on the
   live census, no `.env` key change, the invoke succeeds under an Opal stand-in principal).
4. **Tests,** `infra/aws/ec2/opal-gateway/tests/test_og_gt5.py`, `_invoke` replaced by a recorder:
   - `test_oggt5_ac01`: an Opal principal's call invokes the function once with the payload for the section and returns the
     published body, projected to 50 KB with the four envelope keys.
   - `test_oggt5_ac02`: a non-Opal and an absent principal are refused with ZERO invokes; a bad `sections` value is refused
     `harvest_bad_argument` with zero invokes.
   - `test_oggt5_ac03`: a Lambda error (a `FunctionError` payload or an exception from `_invoke`) returns an error dict with
     code `harvest_published_unavailable` and writes one audit record; the exception text never reaches the caller.
   - `test_oggt5_ac04`: the module imports no boto3 at module scope and never imports `get_current_principal`.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_published.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt5.py
infra/aws/terraform/opal-gateway/harvest_published_invoke_iam.tf
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~76/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~76/`. Rows: id `NFRA_OPLGTW-Z-W76-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt5.AC2.sh; echo "exit=$?"</invocation><expect>(?s)grant: policies 1 \(want 1\); actions \['lambda:InvokeFunction'\] \(want only lambda:InvokeFunction\); function ARNs 1 \(want 1\); wildcard actions 0 \(want 0\).*ask sections: 7 of 7.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tool invokes once for an Opal principal and never for a refused one.
- `AC2`: the grant file is one policy with one action on one function ARN, and the ask names its seven items.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-5.published-analysis-tool.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The release this cell rides: `NFRA_OPLGTW.TO-OG-ap-18`; its grant is `NFRA_OPLGTW.TO-OG-hv-2` (A5).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).
- Queue: staged until OG-gt-0 merges; the spawn is the GO.
- Phase A only: the ask rides to the three halves; the apply and the deploy are a later order.

- A1 (issuer, 2026-10-14 ~15:4xZ, workers' rows S2 and S5): the function name comes from the env key `AMGT_SCOPED_API_FUNCTION` written by `deploy-to-ec2.sh`; `deploy-to-ec2.sh` added to `<paths>`; no literal in code.
  The worker is re-seated on its uncommitted module with this amendment. No criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>G1-TYPED</workstream>
<slot>~76</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
