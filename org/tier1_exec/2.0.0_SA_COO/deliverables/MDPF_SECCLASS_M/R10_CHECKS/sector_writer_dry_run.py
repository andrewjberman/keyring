#!/usr/bin/env python3
"""
sector_writer_dry_run.py -- the FWD-12 sector writer's dry run against the live inputs (MDPF_SECCLASS, cell SC-e-28).

READS ONLY. It runs the sector-writer handler in its default dry run against the newest real characteristics partition
and the live `etf-classifications` table, and prints:

    SECTOR-WRITER-DRY-RUN partition=<d> securities=<n> planned=<n> present=<n> no_row=<n> out_of_list=<n> seed_wins=<n> no_value=<n>

With --packaged it first assembles the files the Lambda would ship (the handler, the contract file it reads, and every
`_shared` module it imports, transitively, found by reading its import statements) into a temp directory, and imports
the handler from THAT layout with the repo's `_shared` directory off sys.path (DECISION 103371's deployed-layout
import). A shared module or the contract the package lacks therefore fails here, as it would in the Lambda.

Locations: the run list's address is lib/opal_naming.py address() output; the table name is the DYNAMODB_TABLE row of
infra/logic/registry/resources.json; the characteristics home `opal-data-etfs/bbg/` is the legacy ETF producer's
(etf_positioning_gold.py BBG_ROOT = "bbg"), not builder-addressable (row MDPF_SECCLASS-W24-S3).
The S3 client and the table are wrapped so a put, update or delete raises: this check cannot write.

Usage: python sector_writer_dry_run.py [--packaged] [--date YYYY-MM-DD] [--quiet]
"""
from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]  # R10_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
HANDLER_DIR = ROOT / "infra" / "aws" / "lambda" / "mdpf-secclass" / "sector-writer"
SHARED_DIR = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
CONTRACT = ROOT / "org" / "standards" / "MDPF_SECCLASS_CONTRACT.json"
REGISTRY = ROOT / "infra" / "logic" / "registry" / "resources.json"
REGION = "us-east-1"
PROBE = "date=0000-00-00"
BBG_BUCKET = "opal-data-etfs"
BBG_PREFIX = "bbg/"


def _load_naming():
    spec = importlib.util.spec_from_file_location("opal_naming_for_sector_writer", ROOT / "lib" / "opal_naming.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def table_name():
    """The classification table's name, read from its registry row (never typed)."""
    with open(REGISTRY, encoding="utf-8") as fh:
        rows = [r for r in json.load(fh)["resources"] if r.get("type") == "DYNAMODB_TABLE" and r.get("name") == "etf-classifications"]
    if len(rows) != 1:
        raise SystemExit(f"BLOCKED: expected one etf-classifications DYNAMODB_TABLE row, found {len(rows)}")
    return rows[0]["name"]


def builder_env():
    """The handler's five environment variables; the run list's bucket and prefix are address() output."""
    naming = _load_naming()
    uri = naming.address("mdpf", "etfs", "gold", "sector_writer_runs", PROBE)
    bucket, _, key = uri[len("s3://"):].partition("/")
    assert key.endswith(PROBE), key
    return {"BBG_BUCKET": BBG_BUCKET, "BBG_PREFIX": BBG_PREFIX, "OUTPUT_BUCKET": bucket,
            "OUTPUT_PREFIX": key[: -len(PROBE)], "TABLE_NAME": table_name()}


def shared_closure(handler_file):
    """Names of the `_shared` modules the handler imports, transitively, read from the import statements."""
    available = {p.stem for p in SHARED_DIR.glob("*.py")}
    todo, seen = [handler_file], set()
    while todo:
        tree = ast.parse(todo.pop().read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names = [node.module.split(".")[0]]
            for n in names:
                if n in available and n not in seen:
                    seen.add(n)
                    todo.append(SHARED_DIR / (n + ".py"))
    return sorted(seen)


def assemble(dest):
    """Copy the handler, the contract and the shared closure flat into `dest`; return the file names."""
    shutil.copy2(HANDLER_DIR / "lambda_function.py", dest / "lambda_function.py")
    shutil.copy2(CONTRACT, dest / CONTRACT.name)
    names = shared_closure(HANDLER_DIR / "lambda_function.py")
    for n in names:
        shutil.copy2(SHARED_DIR / (n + ".py"), dest / (n + ".py"))
    return ["lambda_function.py", CONTRACT.name] + [n + ".py" for n in names], names


def import_packaged(dest):
    """Import lambda_function from `dest` with the repo's _shared directory off sys.path and out of sys.modules."""
    sys.path[:] = [p for p in sys.path if Path(p or ".").resolve() != SHARED_DIR]
    for n in list(sys.modules):
        if n == "lambda_function" or (SHARED_DIR / (n + ".py")).exists():
            del sys.modules[n]
    sys.path.insert(0, str(dest))
    spec = importlib.util.spec_from_file_location("lambda_function", dest / "lambda_function.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["lambda_function"] = mod
    spec.loader.exec_module(mod)
    return mod


class ReadOnly:
    """Delegates every read to the wrapped client and refuses every write."""

    BLOCKED = ("put_object", "put_item", "update_item", "delete_item", "delete_object", "batch_write_item", "copy_object")

    def __init__(self, inner):
        self._inner = inner

    def __getattr__(self, name):
        if name in self.BLOCKED:
            raise RuntimeError(f"REFUSED: the dry run attempted {name}")
        return getattr(self._inner, name)


def main(argv=None):
    parser = argparse.ArgumentParser(description="FWD-12 sector writer dry run (reads only)")
    parser.add_argument("--packaged", action="store_true", help="import the handler from the assembled package layout")
    parser.add_argument("--date", default=None, help="bound the newest partition (default: today, UTC)")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    import boto3
    from botocore.config import Config

    env = builder_env()
    os.environ.update(env)
    cfg = Config(retries={"max_attempts": 10, "mode": "standard"}, read_timeout=120, connect_timeout=30)
    s3 = boto3.client("s3", region_name=REGION, config=cfg)

    tmp = None
    if args.packaged:
        tmp = Path(tempfile.mkdtemp(prefix="sector-writer-package-"))
        files, modules = assemble(tmp)
        print("SECTOR-WRITER-PACKAGE dir={} files={}".format(tmp.name, ",".join(files)))
        handler = import_packaged(tmp)
        loaded = {n: getattr(sys.modules.get(n), "__file__", None) for n in ["lambda_function"] + modules if n in sys.modules}
        outside = [n for n, f in loaded.items() if f and Path(f).resolve().parent != tmp.resolve()]
        if outside:
            raise SystemExit(f"REFUSED: modules imported from outside the package: {outside}")
        print(f"SECTOR-WRITER-IMPORT all {len(loaded)} modules loaded from the package dir")
    else:
        sys.path.insert(0, str(HANDLER_DIR))
        import lambda_function as handler

    try:
        event = {"date": args.date} if args.date else {}
        table = boto3.resource("dynamodb", region_name=REGION, config=cfg).Table(env["TABLE_NAME"])
        result = handler.lambda_handler(event, None, s3=ReadOnly(s3), table=ReadOnly(table))
    finally:
        if tmp is not None:
            shutil.rmtree(tmp, ignore_errors=True)

    if not result["partition"]:
        raise SystemExit("BLOCKED: no partition under s3://{}/{} holds both run_manifest.json and characteristics.parquet".format(env["BBG_BUCKET"], env["BBG_PREFIX"]))
    n = result["counts"]
    print("SECTOR-WRITER-CONTRACT version={}".format(result["contract_version"]))
    if not args.quiet:
        for it in result["items"]:
            detail = it.get("planned") or it.get("out_of_list") or it.get("reason") or ""
            print("SECTOR-WRITER-ITEM {} | {} | {} | {}".format(it["key"], it["security"], it["state"], json.dumps(detail, sort_keys=True)))
    print("SECTOR-WRITER-WOULD-WRITE-LIST s3://{}/{} (only under {{\"write\": true}}; none written here)".format(result["output"]["bucket"], result["output"]["key"]))
    print(f"SECTOR-WRITER-DRY-RUN partition={result['partition']} securities={n['securities']} planned={n['PLANNED']} "
          f"present={n['PRESENT']} no_row={n['NO-ROW']} out_of_list={n['OUT-OF-LIST']} seed_wins={n['SEED-WINS']} "
          f"no_value={n['NO-VALUE']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
