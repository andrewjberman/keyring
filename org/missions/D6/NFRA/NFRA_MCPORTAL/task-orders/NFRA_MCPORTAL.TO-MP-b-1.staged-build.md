# NFRA_MCPORTAL task order -- `MP-b-1` -- ROUND 2, E2: the grant writer becomes a package that runs from its own zip

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-b-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build cell; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM statement changes in this cell; nothing is applied.
comp-adversary: DECLARED-NOT-APPLICABLE -- enrichment round of a thread; the round-1 CVO findings are the input.
EGRESS CLASS, declared: NONE. The layer's wheels are NOT fetched here (MP-a-1 builds the layer).
</preflight>

## 1. THE CELL -- `MP-b-1` (round 2, decomposition section R2.1)

The grant writer is the AWS Lambda `mcportal-grant-writer-lambda`, built in round 1 at
`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`. It cannot run as packaged:
- `:42` computes `Path(__file__).resolve().parents[5]`, and `:43-48` add the gateway tree to `sys.path` and import
  `app.access_state` and `ops.schwab_entitlement_admin` from `infra/aws/ec2/opal-gateway/`;
- the Terraform `archive_file` (`infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:25-30`) zips only this
  function's own directory, with the handler `lambda_function.lambda_handler` at the zip root (`:85`). At `/var/task`,
  `parents[5]` raises IndexError and the gateway modules are absent.

Build:
1. **`build_package.py`** (new, in the function's directory, stdlib only). The command
   `python infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py --out <zip>` does four things:
   - writes a zip holding `lambda_function.py` at its root;
   - adds every module of the IMPORT CLOSURE of `app.access_state` and `ops.schwab_entitlement_admin` within the
     gateway tree, copied byte-for-byte at its REPO-RELATIVE path (e.g. `infra/aws/ec2/opal-gateway/app/access_state.py`,
     `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`) -- derive the closure by reading their imports,
     never by a hand-kept list;
   - adds any data file those modules load, also at its repo-relative path (e.g.
     `org/standards/NFRA_OPLGTW_CONTRACT.json`);
   - exits 0.
   The package MIRRORS the repository layout because `ops/schwab_entitlement_admin.py:49` climbs `parents[5]` to the
   repo root at import time. At Lambda's `/var/task` a zip-root copy has too few parents and raises IndexError (row
   NFRA_MCPORTAL-Z-W1-S3). `ops/` is NFRA_OPLGTW's and is never edited. Mirrored, `parents[5]` lands on the package's
   own root. A zero-byte `__init__.py` may be added where the source tree has none. The package is an artifact of the
   source, never a second copy that can drift.
2. **`lambda_function.py`**: sits at the zip root (the handler), never climbs `parents[N]`, and puts the package's
   mirrored gateway directory (`infra/aws/ec2/opal-gateway`, joined to its OWN directory) first on `sys.path` before
   importing `app` and `ops`. In the source tree, the tests' `conftest.py` puts the gateway tree on the path as today.
3. **`tests/conftest.py`**: also put `infra/aws/ec2/opal-gateway/` on `sys.path`, resolved from the repo root through
   `git rev-parse --show-toplevel` or the file's own location; never a hard-coded drive path. The existing
   `tests/test_grant_writer.py` stays green.
4. **`mcportal_grant_writer.tf`**: the function's code comes from the staged package, so the zip Terraform uploads is the
   one `build_package.py` makes (a `null_resource`/`local-exec` that runs it, or an `archive_file` over a staged
   directory it writes; say which), and the function names a layer for PyJWT + cryptography
   (`aws_lambda_layer_version`, filename from the layer build MP-a-1 runs). Nothing is applied.
5. **The layer's SPEC:** a row in `infra/aws/lambda/ci/lambda-layer-map.json` for `mcportal-grant-writer-deps`, in that
   file's own grammar (read its managed rows, e.g. `irpt-common`), and
   `infra/aws/lambda/layers/mcportal-grant-writer-deps/requirements.txt`. That file pins PyJWT and cryptography plus
   their full transitive closure, EXACT versions, for `manylinux2014_x86_64` / cp312, following the `irpt-common`
   header's discipline. Do NOT download anything.

## 2. BOUNDS

1. No egress: the wheels are MP-a-1's, on Andrew's word. Your proofs need none: the local interpreter supplies PyJWT for
   the import, and the refusal AC2 runs returns before any JWT decode.
2. The owner-key and record changes are the NEXT cell's (MP-b-2). Do not change `_verify_owner_header`, the env names
   or the store calls here.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/conftest.py
infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf
infra/aws/lambda/ci/lambda-layer-map.json
infra/aws/lambda/layers/mcportal-grant-writer-deps/requirements.txt
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/opal-gateway/app/`, `infra/aws/ec2/opal-gateway/ops/`,
`infra/aws/lambda/layers/irpt-common/requirements.txt`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPORTAL-Z-W1-S<k>` (next free k for W1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-b-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b1.AC1.sh; echo "exit=$?"</invocation><expect>build rc=0 built zip=yes; extracted at Lambda depth; lambda_handler callable=yes; app and ops resolved inside the package 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-b-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b1.AC2.sh; echo "exit=$?"</invocation><expect>build rc=0; in-package lambda_handler (Lambda depth) with no owner header -> verdict=REFUSED NO-OWNER-HEADER -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-b-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b1.AC3.sh; echo "exit=$?"</invocation><expect>zip members byte-equal to their repo path at HEAD k of k (k>=2, required members present 2 of 2); parents[ in lambda_function.py=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-b-1.staged-build.proof_of_spec.json`.
Report once:
- what you changed and where, and the commit hash;
- the import closure the build derived, listed;
- how the Terraform now takes the staged zip;
- the pinned layer versions;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E2, rulings R-1 and R-3 (@667f442b8a). Chain A's root. The slot continues with MP-b-2, then MP-a-1.

<status>pending</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
