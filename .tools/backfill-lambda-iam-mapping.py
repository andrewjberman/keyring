#!/usr/bin/env python3
"""ADHC_COMPIL_V4.022 Cat 6.1: backfill `iam_role` field in lambda-source-map.json.

Parses each pipeline's `lambdas.tf` to extract module->role mapping, then for
each Lambda function (matching by `function_name` value or by module name
to entry's `tf_resource`), writes `iam_role` into lambda-source-map.json.

Roles can be expressed three ways in TF:
  module "X" { role_arn = aws_iam_role.foo.arn }       -> role 'foo'
  module "X" { role = aws_iam_role.bar.arn }            -> role 'bar'
  module "X" { role_arn = local.NAME_ARN }              -> resolve local def

Where local is defined as: locals { NAME_ARN = aws_iam_role.X.arn }

Run: python .tools/backfill-lambda-iam-mapping.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
SOURCE_MAP_PATH = WORKSPACE / "infra" / "aws" / "lambda" / "ci" / "lambda-source-map.json"


# Match `aws_iam_role "X" { name = "actual-role-name" }`
_TF_ROLE_DEF = re.compile(
    r'resource\s+"aws_iam_role"\s+"(\w+)"\s*\{[^}]*?name\s*=\s*"([^"]+)"',
    re.DOTALL,
)

# Match `local.SOMETHING_ARN = aws_iam_role.X.arn`
_TF_LOCAL_ROLE = re.compile(
    r'(\w+)\s*=\s*aws_iam_role\.(\w+)\.arn',
)

# Match `module "X" { ... }` OR `resource "aws_lambda_function" "X" { ... }` block boundaries
_TF_MODULE = re.compile(
    r'module\s+"(\w+)"\s*\{(.*?)^\}',
    re.MULTILINE | re.DOTALL,
)
_TF_AWS_LAMBDA_FUNCTION = re.compile(
    r'resource\s+"aws_lambda_function"\s+"(\w+)"\s*\{(.*?)^\}',
    re.MULTILINE | re.DOTALL,
)

# Within a module/resource block, find role_arn / role assignment
_MODULE_ROLE_DIRECT = re.compile(
    r'(?:role_arn|role)\s*=\s*aws_iam_role\.(\w+)\.arn',
)
_MODULE_ROLE_LOCAL = re.compile(
    r'(?:role_arn|role)\s*=\s*local\.(\w+)',
)
# Inline string-ARN: `role_arn = "arn:aws:iam::...:role/causality-ai-query-handler-role"`
_MODULE_ROLE_INLINE_ARN = re.compile(
    r'(?:role_arn|role)\s*=\s*"arn:aws:iam[^"]*role/([^"]+)"',
)
# Variable reference: `role = var.shared_lambda_execution_role_arn` -> "lambda-execution-role"
# Known shared-var convention; cross-pipeline shared role.
_MODULE_ROLE_SHARED_VAR = re.compile(
    r'(?:role_arn|role)\s*=\s*var\.shared_lambda_execution_role_arn',
)
# Local-scoped string role-arn: `BD_EXEC_ROLE = "arn:aws:iam::...:role/lambda-execution-role"`
_TF_LOCAL_ROLE_STRING = re.compile(
    r'(\w+)\s*=\s*"arn:aws:iam[^"]*role/([^"]+)"',
)
# function_name within module/resource block
_MODULE_FN_NAME = re.compile(
    r'function_name\s*=\s*"([^"]+)"',
)


def parse_tf_role_map(tf_path: Path, locals_role_map: dict[str, str] = None,
                     locals_role_string: dict[str, str] = None) -> dict[str, str]:
    """Return dict: lambda_function_name -> role_resource_name (from TF resource block).
    Empty values mean role wasn't resolvable (e.g. shared lambda-execution-role).

    locals_role_map / locals_role_string can be passed pre-built from a
    pipeline-wide scan (locals may live in a different .tf file than the
    Lambda definitions, e.g. yang-pipeline main.tf vs lambdas.tf).
    """
    if not tf_path.exists():
        return {}

    try:
        content = tf_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}

    # Merge in this file's locals on top of pipeline-wide locals (if passed)
    locals_role_map = dict(locals_role_map or {})
    locals_role_string = dict(locals_role_string or {})
    locals_section_m = re.search(r'locals\s*\{(.*?)^\}', content, re.MULTILINE | re.DOTALL)
    if locals_section_m:
        body = locals_section_m.group(1)
        for m in _TF_LOCAL_ROLE.finditer(body):
            locals_role_map[m.group(1)] = m.group(2)
        for m in _TF_LOCAL_ROLE_STRING.finditer(body):
            locals_role_string[m.group(1)] = m.group(2)

    fn_to_role: dict[str, str] = {}

    def _scan_block(body: str):
        fn_name_m = _MODULE_FN_NAME.search(body)
        if not fn_name_m:
            return
        fn_name = fn_name_m.group(1)
        role_resource = None
        role_direct_name = None  # already-resolved role name (no TF lookup needed)

        # Priority: aws_iam_role.X.arn > local.NAME > inline string-arn
        direct_m = _MODULE_ROLE_DIRECT.search(body)
        if direct_m:
            role_resource = direct_m.group(1)
        else:
            local_m = _MODULE_ROLE_LOCAL.search(body)
            if local_m:
                local_name = local_m.group(1)
                if local_name in locals_role_map:
                    role_resource = locals_role_map[local_name]
                elif local_name in locals_role_string:
                    role_direct_name = locals_role_string[local_name]
            else:
                inline_arn_m = _MODULE_ROLE_INLINE_ARN.search(body)
                if inline_arn_m:
                    role_direct_name = inline_arn_m.group(1)
                elif _MODULE_ROLE_SHARED_VAR.search(body):
                    role_direct_name = "lambda-execution-role"

        if role_resource:
            fn_to_role[fn_name] = role_resource
        elif role_direct_name:
            # Use prefix marker so caller knows to skip role-name lookup
            fn_to_role[fn_name] = f"__direct__::{role_direct_name}"

    for m in _TF_MODULE.finditer(content):
        _scan_block(m.group(2))
    for m in _TF_AWS_LAMBDA_FUNCTION.finditer(content):
        _scan_block(m.group(2))

    return fn_to_role


def parse_iam_tf_role_names(iam_tf_dir: Path) -> dict[str, str]:
    """Return dict: tf_resource_name -> actual_role_name (from `aws_iam_role` resource blocks).
    Scans all *.tf files in pipeline dir.
    """
    role_names: dict[str, str] = {}
    for tf_file in sorted(iam_tf_dir.glob("*.tf")):
        try:
            content = tf_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in _TF_ROLE_DEF.finditer(content):
            tf_resource = m.group(1)
            actual_name = m.group(2)
            role_names[tf_resource] = actual_name
    return role_names


def main() -> int:
    if not SOURCE_MAP_PATH.exists():
        print(f"ERROR: source map not found: {SOURCE_MAP_PATH}")
        return 1

    sm = json.loads(SOURCE_MAP_PATH.read_text(encoding="utf-8"))
    fns = sm.get("functions", {})

    # Build cross-pipeline role map: pipeline_dir -> {fn_name: role_resource}
    # Also build pipeline_dir -> {role_resource: actual_role_name}
    # Scan ALL .tf files in each pipeline dir (not just lambdas.tf — causality
    # uses main.tf, and other pipelines split into multiple files).
    tf_root = WORKSPACE / "infra" / "aws" / "terraform"
    pipeline_dirs = [d for d in tf_root.iterdir() if d.is_dir()]

    pipeline_fn_role: dict[Path, dict[str, str]] = {}
    pipeline_role_names: dict[Path, dict[str, str]] = {}

    for pd in pipeline_dirs:
        # Pre-scan all .tf files for pipeline-wide locals (locals may live in
        # main.tf while Lambdas live in lambdas.tf — yang/market-overview pattern).
        pipeline_locals_map: dict[str, str] = {}
        pipeline_locals_string: dict[str, str] = {}
        for tf_file in sorted(pd.glob("*.tf")):
            try:
                tf_content = tf_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            ls_m = re.search(r'locals\s*\{(.*?)^\}', tf_content, re.MULTILINE | re.DOTALL)
            if ls_m:
                ls_body = ls_m.group(1)
                for m in _TF_LOCAL_ROLE.finditer(ls_body):
                    pipeline_locals_map[m.group(1)] = m.group(2)
                for m in _TF_LOCAL_ROLE_STRING.finditer(ls_body):
                    pipeline_locals_string[m.group(1)] = m.group(2)

        # Merge fn_role mappings from all *.tf files in the pipeline dir
        merged_fn_role: dict[str, str] = {}
        for tf_file in sorted(pd.glob("*.tf")):
            merged_fn_role.update(parse_tf_role_map(
                tf_file,
                locals_role_map=pipeline_locals_map,
                locals_role_string=pipeline_locals_string,
            ))
        pipeline_fn_role[pd] = merged_fn_role
        pipeline_role_names[pd] = parse_iam_tf_role_names(pd)

    # Build a global fn -> (pipeline_dir, role_resource) lookup for entries
    # that lack tf_file (legacy source-map entries).
    global_fn_to_pipeline: dict[str, Path] = {}
    for pd, fn_role_map in pipeline_fn_role.items():
        for fn_name in fn_role_map:
            global_fn_to_pipeline[fn_name] = pd

    populated = 0
    skipped_existing = 0
    unresolved: list[str] = []

    for fn_name, entry in fns.items():
        if not isinstance(entry, dict):
            continue

        if entry.get("iam_role"):
            skipped_existing += 1
            continue

        # Find which pipeline this Lambda belongs to via tf_file, fall through
        # to global function-name lookup when tf_file missing.
        tf_file = entry.get("tf_file", "")
        if tf_file:
            tf_file_path = WORKSPACE / tf_file
            pipeline_dir = tf_file_path.parent
        else:
            pipeline_dir = global_fn_to_pipeline.get(fn_name)
            if pipeline_dir is None:
                unresolved.append(fn_name)
                continue

        fn_role_map = pipeline_fn_role.get(pipeline_dir, {})
        role_names = pipeline_role_names.get(pipeline_dir, {})

        # Lookup by fn_name
        role_resource = fn_role_map.get(fn_name)
        if not role_resource:
            unresolved.append(fn_name)
            continue

        # Direct-resolved (e.g. shared lambda-execution-role from string-arn local)
        if role_resource.startswith("__direct__::"):
            actual_role_name = role_resource.split("::", 1)[1]
        else:
            actual_role_name = role_names.get(role_resource, role_resource)
        entry["iam_role"] = actual_role_name
        populated += 1

    # Write back
    SOURCE_MAP_PATH.write_text(
        json.dumps(sm, indent=2) + "\n",
        encoding="utf-8",
    )

    print("BACKFILL COMPLETE")
    print(f"  Total functions:    {len(fns)}")
    print(f"  Newly populated:    {populated}")
    print(f"  Already had role:   {skipped_existing}")
    print(f"  Unresolved:         {len(unresolved)}")
    if unresolved:
        print(f"  First 20 unresolved: {unresolved[:20]}")
    print("  Shared lambda-execution-role fallback: NOT applied (kept unresolved for explicit triage)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
