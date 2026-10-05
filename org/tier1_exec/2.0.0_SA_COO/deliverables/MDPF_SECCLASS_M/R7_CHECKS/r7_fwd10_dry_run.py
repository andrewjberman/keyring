#!/usr/bin/env python3
"""
r7_fwd10_dry_run.py -- the FWD-10 producer's dry run against the live inputs (MDPF_SECCLASS, cell SC-e-19).

READS ONLY. It takes the latest canonical_shape day that has a previous day, runs the new-security-classifier handler
in its default dry run for that day, and prints:

    FWD10-DRY-RUN day=<d> previous=<d> sources=<n> new_stocks=<n> planned_writes=<n> present=<n> unresolved=<n>

With --packaged it first assembles the files the Lambda would ship (the handler plus every `_shared` module it imports,
transitively, found by reading its import statements) into a temp directory, and imports the handler from THAT layout
with the repo's `_shared` directory off sys.path (DECISION 103371's deployed-layout import). A shared module the handler
needs and the package lacks therefore fails here, as it would in the Lambda. The temp directory holds nothing else.

Every location comes from lib/opal_naming.py address() (the canonical_shape tier and the new-stock list); the Opal
silver holdings are the legacy etfs-netassets location (not builder-addressable; it is the order's named input).
The S3 client and the table are wrapped so a put, update or delete raises: this check cannot write.

Usage: python r7_fwd10_dry_run.py [--packaged] [--date YYYY-MM-DD] [--quiet]
"""
from __future__ import annotations

import argparse
import ast
import importlib.util
import os
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]  # R7_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
HANDLER_DIR = ROOT / "infra" / "aws" / "lambda" / "mdpf-secclass" / "new-security-classifier"
SHARED_DIR = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
REGION = "us-east-1"
PROBE = "date=0000-00-00"
# The Opal ETFs' silver holdings: etfs-netassets-daily writes <SILVER_ROOT>silver/holdings/{run_date}.parquet
# (infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:1501-1508). A legacy location with no builder home.
SILVER_BUCKET = "opal-data-etfs"
SILVER_PREFIX = "silver/holdings/"


def _load_naming():
    spec = importlib.util.spec_from_file_location("opal_naming_for_fwd10", ROOT / "lib" / "opal_naming.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def builder_env():
    """The handler's six environment variables, from address() (the bucket is the builder's)."""
    naming = _load_naming()

    def split(uri, probe=True):
        bucket, _, key = uri[len("s3://"):].partition("/")
        if probe:
            assert key.endswith(PROBE), key
            key = key[: -len(PROBE)]
        return bucket, key

    c_bucket, c_prefix = split(naming.address("rivalfunds", "etfs", "gold", "canonical_shape", PROBE))
    o_bucket, o_prefix = split(naming.address("mdpf", "etfs", "gold", "new_securities", PROBE))
    return {"CANONICAL_BUCKET": c_bucket, "CANONICAL_PREFIX": c_prefix,
            "SILVER_BUCKET": SILVER_BUCKET, "SILVER_PREFIX": SILVER_PREFIX,
            "OUTPUT_BUCKET": o_bucket, "OUTPUT_PREFIX": o_prefix}


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
    """Copy the handler and its shared closure flat into `dest`; return the file names."""
    shutil.copy2(HANDLER_DIR / "lambda_function.py", dest / "lambda_function.py")
    names = shared_closure(HANDLER_DIR / "lambda_function.py")
    for n in names:
        shutil.copy2(SHARED_DIR / (n + ".py"), dest / (n + ".py"))
    return ["lambda_function"] + names


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
            raise RuntimeError("REFUSED: the dry run attempted %s" % name)
        return getattr(self._inner, name)


def latest_day_with_previous(s3, bucket, prefix):
    days = []
    kw = dict(Bucket=bucket, Prefix=prefix, Delimiter="/")
    while True:
        resp = s3.list_objects_v2(**kw)
        days += [cp["Prefix"].rstrip("/").rsplit("=", 1)[-1] for cp in resp.get("CommonPrefixes", [])]
        if not resp.get("IsTruncated"):
            break
        kw["ContinuationToken"] = resp["NextContinuationToken"]
    days = sorted(days)
    if len(days) < 2:
        raise SystemExit("BLOCKED: fewer than two canonical_shape days under s3://%s/%s" % (bucket, prefix))
    return days[-1], len(days)


def main(argv=None):
    parser = argparse.ArgumentParser(description="FWD-10 producer dry run (reads only)")
    parser.add_argument("--packaged", action="store_true", help="import the handler from the assembled package layout")
    parser.add_argument("--date", default=None, help="run day (default: the latest canonical_shape day)")
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
        tmp = Path(tempfile.mkdtemp(prefix="fwd10-package-"))
        files = assemble(tmp)
        print("FWD10-PACKAGE dir=%s files=%s" % (tmp.name, ",".join(f + ".py" for f in files)))
        handler = import_packaged(tmp)
        loaded = {n: getattr(sys.modules.get(n), "__file__", None) for n in files if n in sys.modules}
        outside = [n for n, f in loaded.items() if f and Path(f).resolve().parent != tmp.resolve()]
        if outside:
            raise SystemExit("REFUSED: modules imported from outside the package: %s" % outside)
        print("FWD10-IMPORT all %d modules loaded from the package dir" % len(loaded))
    else:
        sys.path.insert(0, str(HANDLER_DIR))
        import lambda_function as handler  # noqa: E402

    try:
        day, ndays = latest_day_with_previous(s3, env["CANONICAL_BUCKET"], env["CANONICAL_PREFIX"])
        run_date = args.date or day
        table = boto3.resource("dynamodb", region_name=REGION, config=cfg).Table(handler.TABLE_NAME)
        result = handler.lambda_handler({"date": run_date}, None, s3=ReadOnly(s3), table=ReadOnly(table))
    finally:
        if tmp is not None:
            shutil.rmtree(tmp, ignore_errors=True)

    c, o = result["canonical_shape"], result["opal_silver"]
    print("FWD10-SPLIT canonical_shape funds=%s" % ",".join(c["funds"]))
    print("FWD10-SPLIT opal silver funds=%s; silver read for=%s (the Opal funds the canonical_shape lacks)"
          % (",".join(o["opal_funds"]), ",".join(o["funds_read"]) or "none"))
    print("FWD10-DAYS canonical_shape day=%s previous=%s stocks=%d; opal_silver day=%s previous=%s stocks=%d ignored_rows=%d"
          % (c["day"], c["previous"], c["stocks"], o["day"], o["previous"], o["stocks"], o["ignored_rows"]))
    if not args.quiet:
        for it in result["items"]:
            print("FWD10-NEW %s | %s | %s | %s | %s" % (it["key"], it["source"], it["fund"],
                                                        it["security_bloomberg"] or it["ticker"], it["state"]))
    n = result["counts"]
    print("FWD10-WOULD-WRITE s3://%s/%s" % (result["output"]["bucket"], result["output"]["key"]))
    print("FWD10-DRY-RUN day=%s previous=%s sources=%d new_stocks=%d planned_writes=%d present=%d unresolved=%d"
          % (c["day"], c["previous"], result["sources"], n["new_stocks"], n["planned_writes"], n["present"],
             n["unresolved"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
