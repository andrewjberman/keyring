"""AC2 (HVST-v-1): THE POSITIVE CONTROL -- nothing else moved.

ARM A: wsj's HELD listing payload produces a BYTE-IDENTICAL row set and an IDENTICAL arrow schema
before and after the change. "Before" is the pre-change code path RUN, not quoted: HEAD's bytes of
`silver_from_bronze.py`, exec'd as a package member (same loader as ac1.py). Byte-identity is
measured on a canonical serialisation of the whole row set (sorted keys, repr of non-JSON scalars)
digested with sha256, and corroborated by direct `==`. The schemas are printed in full, both arms.

ARM B: a POPULATED mapping is still a struct with its child -- built through the real
`listing_hit_rows`, its arrow type printed, and written to parquet. Includes the harder case: an
empty mapping NESTED inside a populated one, where the populated parent must stay a struct and only
the empty child is nulled.

Write path = `pa.Table.from_pylist` + `pq.write_table` into an in-memory buffer, verbatim from
`lib/research/harvest/store.py` `silver_append` (:348, READ ONLY). NO S3, no network, no vendor call.
"""
import hashlib
import io
import json
import subprocess
import sys
import types
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           check=True).stdout.decode().strip())
sys.path.insert(0, str(REPO))

MAIN_TREE = Path("C:/Users/Opal Bloomberg/Desktop/ajb_workspace")
HELD = MAIN_TREE / ".runtime/opal-data-harvest/harvest_listing"
WSJ_PAGES = [("wsj_p1_45058f937f5eff24.html", 1), ("wsj_p2_bfec5a47fe3ed50b.html", 2)]

TARGET = "lib/opal_data_harvest/silver_from_bronze.py"
QUERY = "berkshire hathaway"
FETCHED_AT = "2026-09-22T20:32:00Z"
RUN_STAMP = "20260922T203200Z"
FIX_MARKER = "_null_empty_mappings"


def load_head_module():
    import lib.opal_data_harvest  # noqa: F401

    src = subprocess.run(["git", "show", "HEAD:" + TARGET], cwd=str(REPO),
                         capture_output=True, check=True).stdout.decode("utf-8")
    name = "lib.opal_data_harvest._ac2_head_silver_from_bronze"
    mod = types.ModuleType(name)
    mod.__package__ = "lib.opal_data_harvest"
    mod.__file__ = "<git show HEAD:%s>" % TARGET
    sys.modules[name] = mod
    exec(compile(src, mod.__file__, "exec"), mod.__dict__)
    return mod, src


def canonical(rows):
    """A canonical BYTE serialisation of a row set: key order removed, every non-JSON scalar
    rendered by repr (so a datetime/date difference cannot hide inside str())."""
    return json.dumps(rows, sort_keys=True, default=repr, ensure_ascii=False).encode("utf-8")


def schema_of(rows):
    table = pa.Table.from_pylist(rows)
    pq.write_table(table, io.BytesIO())
    return table


def main():
    head_mod, head_src = load_head_module()
    from lib.opal_data_harvest import silver_from_bronze as now_mod
    now_src = (REPO / TARGET).read_text(encoding="utf-8")

    print("AC2 -- HVST-v-1 POSITIVE CONTROL: wsj unchanged, populated mapping still a struct")
    print("pyarrow %s | BEFORE = git show HEAD:%s (carries fix: %s) | AFTER = worktree (carries fix: %s)"
          % (pa.__version__, TARGET, FIX_MARKER in head_src, FIX_MARKER in now_src))
    print("")

    checks = []

    # ================= ARM A: wsj held payloads, before vs after =================
    print("=" * 78)
    print("ARM A -- wsj HELD listing payloads: byte-identical rows AND identical arrow schema")
    print("=" * 78)
    total_rows = 0
    for name, page in WSJ_PAGES:
        path = HELD / name
        body = path.read_bytes()
        args = ("wsj", body, QUERY, page, "wsj/harvest/bronze/news_listing/%s" % name,
                FETCHED_AT, "live", RUN_STAMP)
        before_rows = head_mod.listing_hit_rows(*args)
        after_rows = now_mod.listing_hit_rows(*args)
        total_rows += len(after_rows)

        before_bytes, after_bytes = canonical(before_rows), canonical(after_rows)
        before_sha = hashlib.sha256(before_bytes).hexdigest()
        after_sha = hashlib.sha256(after_bytes).hexdigest()

        print("")
        print("-- %s (%d bytes held)  rows BEFORE = %d  rows AFTER = %d"
              % (name, len(body), len(before_rows), len(after_rows)))
        print("   canonical row-set sha256 BEFORE = %s (%d bytes)" % (before_sha, len(before_bytes)))
        print("   canonical row-set sha256 AFTER  = %s (%d bytes)" % (after_sha, len(after_bytes)))
        print("   ROW SET VERDICT: %s" % ("BYTE-IDENTICAL" if before_bytes == after_bytes
                                          else "*** DIFFERENT ***"))
        print("   direct equality (before_rows == after_rows): %s" % (before_rows == after_rows))

        if before_rows:
            before_table = schema_of(before_rows)
            after_table = schema_of(after_rows)
            print("   arrow schema BEFORE (%d fields):" % len(before_table.schema))
            for field in before_table.schema:
                print("      %s: %s" % (field.name, field.type))
            print("   arrow schema AFTER  (%d fields):" % len(after_table.schema))
            for field in after_table.schema:
                print("      %s: %s" % (field.name, field.type))
            same_schema = before_table.schema.equals(after_table.schema)
            print("   SCHEMA VERDICT: %s" % ("IDENTICAL" if same_schema else "*** CHANGED ***"))
            print("   parquet row count BEFORE = %d  AFTER = %d"
                  % (before_table.num_rows, after_table.num_rows))
            print("   table data equality: %s" % before_table.equals(after_table))
            checks.append(("%s arrow schema identical" % name, same_schema))
            checks.append(("%s arrow table data identical" % name, before_table.equals(after_table)))
            checks.append(("%s parquet row count unchanged" % name,
                           before_table.num_rows == after_table.num_rows))
        else:
            print("   0 rows on this held page -- no schema to compare (searchResults is an empty"
                  " list in the captured bytes); row-set identity still measured above")
        checks.append(("%s row set byte-identical" % name, before_bytes == after_bytes))
        checks.append(("%s row count unchanged" % name, len(before_rows) == len(after_rows)))

    print("")
    print("ARM A row denominator: %d wsj listing rows compared across %d held pages"
          % (total_rows, len(WSJ_PAGES)))

    # ================= ARM B: a populated mapping is still a struct =================
    print("")
    print("=" * 78)
    print("ARM B -- a POPULATED mapping still writes AS A STRUCT (and a nested empty one is nulled)")
    print("=" * 78)
    # Built through the real row builder: an sa listing page whose `themes` mapping HAS a key, and
    # whose `links` mapping holds a populated child next to an EMPTY grandchild.
    payload = {"data": [{
        "id": "901",
        "attributes": {
            "title": "Populated mapping control",
            "publishOn": "2026-09-22T00:00:00Z",
            "themes": {"berkshire": "primary"},
            "nested": {"kept": {"inner": 7}, "dropped": {}},
        },
        "links": {"self": "/news/901-populated"},
    }]}
    rows = now_mod.listing_hit_rows("sa", json.dumps(payload).encode("utf-8"), QUERY, 1,
                                    "seeking-alpha/harvest/bronze/news_listing/ac2-populated.json",
                                    FETCHED_AT, "live", RUN_STAMP)
    print("rows built = %d of 1 expected" % len(rows))
    print("themes value  = %r" % (rows[0]["themes"],))
    print("nested value  = %r" % (rows[0]["nested"],))
    print("links value   = %r" % (rows[0]["links"],))
    table = pa.Table.from_pylist(rows)
    buf = io.BytesIO()
    pq.write_table(table, buf)
    themes_type = table.schema.field("themes").type
    nested_type = table.schema.field("nested").type
    links_type = table.schema.field("links").type
    print("arrow type of themes = %s" % themes_type)
    print("arrow type of nested = %s" % nested_type)
    print("arrow type of links  = %s" % links_type)
    print("WRITE: SUCCEEDED -- parquet bytes = %d, rows = %d" % (len(buf.getvalue()), table.num_rows))
    read_back = pq.read_table(io.BytesIO(buf.getvalue()))
    print("read back from the parquet bytes: themes = %r" % (read_back.column("themes")[0].as_py(),))
    print("read back from the parquet bytes: nested = %r" % (read_back.column("nested")[0].as_py(),))

    checks.append(("populated themes is a struct with its child",
                   pa.types.is_struct(themes_type) and themes_type.num_fields == 1
                   and themes_type.field(0).name == "berkshire"))
    checks.append(("populated themes value preserved", rows[0]["themes"] == {"berkshire": "primary"}))
    checks.append(("populated parent stays a struct with an empty child nulled",
                   pa.types.is_struct(nested_type)
                   and rows[0]["nested"] == {"kept": {"inner": 7}, "dropped": None}))
    checks.append(("populated links unchanged", rows[0]["links"] == {"self": "/news/901-populated"}))
    checks.append(("populated-mapping row writes to parquet", table.num_rows == 1))
    checks.append(("populated themes survives the parquet round trip",
                   read_back.column("themes")[0].as_py() == {"berkshire": "primary"}))

    # ================= verdict =================
    print("")
    for label, ok in checks:
        print("  %-58s %s" % (label, "PASS" if ok else "FAIL"))
    passed = sum(1 for _, ok in checks if ok)
    print("")
    print("AC2 denominator: %d of %d checks PASS (wsj rows compared: %d)"
          % (passed, len(checks), total_rows))
    print("AC2: %s" % ("PASS -- wsj row set and schema unmoved; a populated mapping is still a struct"
                       if passed == len(checks) else "FAIL"))
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
