"""AC1 (HVST-v-1): the defect REPRODUCED and then GONE, both arms in one output, on the REAL held
seeking-alpha listing payload.

The BEFORE arm RUNS the pre-change code path -- the bytes of `silver_from_bronze.py` at
`git show HEAD:...`, exec'd as a module inside the `lib.opal_data_harvest` package so its relative
imports resolve. It is never a quotation of the task order. A positive/negative control prints
whether each arm's source carries the fix, so "before" cannot silently be the after-bytes.

The write is the REAL silver write path, lifted verbatim from `lib/research/harvest/store.py`
`silver_append` (:348, READ ONLY here): `pa.Table.from_pylist(rows)` then `pq.write_table(table,
io.BytesIO())`. NO S3 CLIENT, no network, no vendor call -- the buffer is in memory.
"""
import io
import subprocess
import sys
import traceback
import types
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           check=True).stdout.decode().strip())
sys.path.insert(0, str(REPO))

MAIN_TREE = Path("C:/Users/Opal Bloomberg/Desktop/ajb_workspace")
SA_PAYLOAD = MAIN_TREE / ".runtime/opal-data-harvest/harvest_listing/sa_p1_990943eddbd5a172.json"

TARGET = "lib/opal_data_harvest/silver_from_bronze.py"
QUERY = "berkshire hathaway"
PAGE = 1
BRONZE_KEY = "seeking-alpha/harvest/bronze/news_listing/ac1-held-page.json"
FETCHED_AT = "2026-09-25T22:18:00Z"
RUN_STAMP = "20260925T221800Z"
FIX_MARKER = "_null_empty_mappings"


def load_head_module():
    """The PRE-CHANGE module: HEAD's bytes of the target file, exec'd as a package member."""
    import lib.opal_data_harvest  # noqa: F401  (the package must exist for relative imports)

    src = subprocess.run(["git", "show", "HEAD:" + TARGET], cwd=str(REPO),
                         capture_output=True, check=True).stdout.decode("utf-8")
    name = "lib.opal_data_harvest._ac1_head_silver_from_bronze"
    mod = types.ModuleType(name)
    mod.__package__ = "lib.opal_data_harvest"
    mod.__file__ = "<git show HEAD:%s>" % TARGET
    sys.modules[name] = mod
    exec(compile(src, mod.__file__, "exec"), mod.__dict__)
    return mod, src


def build_and_write(module, body):
    """Build the listing rows and drive them through the real parquet write. Returns
    (rows, table, error) -- error is the exception the write raised, or None."""
    rows = module.listing_hit_rows("sa", body, QUERY, PAGE, BRONZE_KEY, FETCHED_AT, "live", RUN_STAMP)
    try:
        table = pa.Table.from_pylist(rows)
        pq.write_table(table, io.BytesIO())
        return rows, table, None
    except Exception as exc:  # noqa: BLE001 -- the arm under measurement IS the exception
        return rows, None, exc


def main():
    body = SA_PAYLOAD.read_bytes()
    print("AC1 -- HVST-v-1: empty mapping in a listing row, BEFORE and AFTER, one held sa payload")
    print("held payload: %s (%d bytes)" % (SA_PAYLOAD, len(body)))
    print("pyarrow %s | write path = pa.Table.from_pylist + pq.write_table (store.py:348 verbatim,"
          " in-memory buffer, NO S3)" % pa.__version__)
    print("")

    head_mod, head_src = load_head_module()
    from lib.opal_data_harvest import silver_from_bronze as now_mod
    now_src = (REPO / TARGET).read_text(encoding="utf-8")

    print("ARM PROVENANCE (the control that the BEFORE arm is really pre-change bytes)")
    print("  BEFORE source = %s  carries %r: %s"
          % (head_mod.__file__, FIX_MARKER, FIX_MARKER in head_src))
    print("  AFTER  source = %s  carries %r: %s"
          % (TARGET + " (worktree)", FIX_MARKER, FIX_MARKER in now_src))
    print("")

    # ---------------- BEFORE ----------------
    before_rows, before_table, before_err = build_and_write(head_mod, body)
    empty_before = sum(1 for r in before_rows
                       for v in r.values() if isinstance(v, dict) and not v)
    print("BEFORE (HEAD bytes): rows built = %d of 20 expected; empty-mapping field values = %d"
          % (len(before_rows), empty_before))
    print("  themes on row[0] = %r   (type %s)"
          % (before_rows[0].get("themes"), type(before_rows[0].get("themes")).__name__))
    if before_err is None:
        print("  WRITE: SUCCEEDED -- the defect did NOT reproduce")
    else:
        print("  WRITE RAISED: %s: %s" % (type(before_err).__name__, before_err))
        print("  raised at: %s" % traceback.format_exception_only(type(before_err), before_err)[-1].strip())
    print("")

    # ---------------- AFTER ----------------
    after_rows, after_table, after_err = build_and_write(now_mod, body)
    empty_after = sum(1 for r in after_rows
                      for v in r.values() if isinstance(v, dict) and not v)
    print("AFTER (worktree bytes): rows built = %d of 20 expected; empty-mapping field values = %d"
          % (len(after_rows), empty_after))
    print("  themes on row[0] = %r   (type %s)"
          % (after_rows[0].get("themes"), type(after_rows[0].get("themes")).__name__))
    if after_err is None:
        print("  WRITE: SUCCEEDED -- parquet row count written = %d of 20 expected" % after_table.num_rows)
        print("  arrow type of themes AFTER = %s" % after_table.schema.field("themes").type)
        print("  columns = %d" % after_table.num_columns)
    else:
        print("  WRITE RAISED: %s: %s" % (type(after_err).__name__, after_err))
    print("")

    # ---------------- the verdict, as a conjunction of measured facts ----------------
    is_arrow_not_impl = type(before_err).__name__ == "ArrowNotImplementedError"
    names_struct = before_err is not None and "no child field" in str(before_err)
    checks = [
        ("BEFORE arm ran pre-change bytes (no fix marker)", FIX_MARKER not in head_src),
        ("AFTER arm ran post-change bytes (fix marker present)", FIX_MARKER in now_src),
        ("BEFORE write raised ArrowNotImplementedError", is_arrow_not_impl),
        ("BEFORE error names a struct with no child field", names_struct),
        ("AFTER write succeeded", after_err is None),
        ("AFTER parquet row count == 20", after_table is not None and after_table.num_rows == 20),
        ("AFTER rows carry no empty mapping", empty_after == 0),
        ("BEFORE rows carried 20 empty mappings", empty_before == 20),
    ]
    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print("  %-52s %s" % (label, "PASS" if ok else "FAIL"))
    print("")
    print("AC1 denominator: %d of %d checks PASS" % (passed, len(checks)))
    print("AC1: %s" % ("PASS -- defect reproduced on pre-change bytes and gone on post-change bytes"
                       if passed == len(checks) else "FAIL"))
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
