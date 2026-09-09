#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-4 battery: a `comp-heat federated` answer carries the catalogs it joined and
each one's ARTIFACT BUILD TIME -- never the query's clock.

Run at both required file grains:
  python .tools/tests/test_os4_federated_vintage.py
  python -m pytest -q .tools/tests/test_os4_federated_vintage.py

WARN: COST AND SAFETY, load-bearing for this file. `comp-heat federated` reaches a LIVE plane, so this
battery is built to touch it ONCE and to never dispatch a Trino query:
  - EIGHT of the nine arms run entirely OFFLINE against a FAKE object plane (no boto3 call at all),
    which is also what lets them exercise branches the live estate does not currently exhibit (a
    0-match convention join, an unregistered catalog, a spent budget).
  - ONE arm runs the real CLI at `--budget 120`, which is BELOW comp-heat's own
    FEDERATED_LIVE_FLOOR_S (200 s), so the tool's refuse-before-dispatch guard fires and the live
    Trino plane is NEVER reached. That arm asserts the refusal text is present, so "no query was
    dispatched" is a checked property of this battery and not an assumption about it.
  - No arm raises a budget to make anything pass.

THE FIXTURE'S TWO NUMBERS ARE THE POINT (arm B). The Glue catalog row for
`code_heat.globgrph.code_heat` reports UpdateTime 2026-06-29T20:34:47Z while the parquet under its
own StorageDescriptor.Location was last written 2026-07-16T03:40:46Z -- both measured live
2026-09-05. A vintage that read the catalog would be well-formed, plausible and seventeen days
wrong. The fake plane reproduces that disagreement so the arm can tell the two apart.
"""
from __future__ import annotations

import datetime as _dt
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "comp-heat"
ENGINE = ROOT / "org" / "modules" / "heatmap" / "federated_vintage.py"

UTC = _dt.timezone.utc
# The two fixture timestamps, both MEASURED on the live estate 2026-09-05 (see the module docstring).
GLUE_UPDATE_TIME = _dt.datetime(2026, 6, 29, 20, 34, 47, tzinfo=UTC)      # the CATALOG ROW's time
PARQUET_BUILD_TIME = _dt.datetime(2026, 7, 16, 3, 40, 46, tzinfo=UTC)     # the ARTIFACT's time

# The real child prefixes under the Nessie warehouse root, transcribed from a live
# `s3:ListObjectsV2(Prefix='warehouse/globgrph/', Delimiter='/')` on 2026-09-05. Arm C uses these to
# prove the `<table>_<uuid>/` convention join returns a NON-ZERO on a case known to exist -- the
# check a sibling cell (OS-s-8) found missing on a join that matched 0 of 1774 and said nothing.
REAL_WAREHOUSE_CHILDREN = [
    "warehouse/globgrph/code_heat_snap_8b0bca7a-9078-4b8e-8868-ef04062d9952/",
    "warehouse/globgrph/cse_b557721f-8b81-4ec2-9289-fe5f44c3f272/",
    "warehouse/globgrph/cse_test_24458e6c-667c-4e85-ba44-33751795e182/",
    "warehouse/globgrph/cse_test_bb57a916-76de-454d-a71e-932dc173620e/",
    "warehouse/globgrph/fedobs_coevolution_snap_499558ba-0181-42ab-a008-93a518692299/",
    "warehouse/globgrph/fedobs_coverage_snap_a9637eab-f8d2-4421-847c-4a2ca27cdc86/",
    "warehouse/globgrph/graph_contracts_bccbceec-941a-424e-be43-edd7d751a1cf/",
    "warehouse/globgrph/graph_edges_6629328d-a582-46d2-80bc-5059de1a77ce/",
    "warehouse/globgrph/graph_nodes_4c6c23bd-fffa-427e-9cd9-7a9deaa3426d/",
    "warehouse/globgrph/ms_heat_snap_a1875ebc-9d80-4078-b8e7-19e6455265bd/",
    "warehouse/globgrph/resource_summaries_b38ddc35-944f-4dd4-b801-120e96c6d4cd/",
]
ICEBERG_PREFIX = REAL_WAREHOUSE_CHILDREN[8]

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, ok, str(detail).replace("\n", " ")[:300]))


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FakePlane:
    """The object plane, stubbed. NOTHING here calls AWS -- which is what makes the offline arms
    both free and able to reach branches the live estate does not currently exhibit."""

    def __init__(self, glue_locations=None, children=None, objects=None, per_object_delay=0.0):
        self.glue_locations = glue_locations or {}
        self.children = children if children is not None else []
        self.objects = objects or {}
        self.per_object_delay = per_object_delay
        self.calls = []

    def glue_table_location(self, database, table):
        self.calls.append(("glue", database, table))
        loc = self.glue_locations.get((database, table))
        if loc is None:
            return None, f"glue:GetTable {database}.{table} failed: EntityNotFoundException"
        return loc, None

    def list_common_prefixes(self, bucket, prefix):
        self.calls.append(("prefixes", bucket, prefix))
        return [c for c in self.children if c.startswith(prefix)], None

    def iter_object_times(self, bucket, prefix):
        self.calls.append(("objects", bucket, prefix))
        for key, lm in self.objects.get(prefix, []):
            if self.per_object_delay:
                time.sleep(self.per_object_delay)
            yield key, lm


def _fv():
    return _load(ENGINE, "os4_fv_%s" % uuid.uuid4().hex)


def _run_cli(*args, timeout=115):
    return subprocess.run([sys.executable, str(TOOL), *args], cwd=str(ROOT), text=True,
                          capture_output=True, timeout=timeout)


def _run_battery() -> None:                                                # noqa: C901
    if RESULTS:
        return
    fv = _fv()
    sys.path.insert(0, str(ROOT / ".tools"))
    from _trino_fed import Q_CODE_BANDS                                    # noqa: E402

    # ---- ARM A: the table list is DERIVED from the SQL about to run, not recited ----
    default_tables = fv.tables_in_sql([Q_CODE_BANDS])
    custom = fv.tables_in_sql(["SELECT * FROM hive.other.thing t JOIN code_heat.globgrph.code_heat "
                               "c ON c.graph_path = t.p"])
    _record("A-TABLES-DERIVED-FROM-THE-SQL-NOT-RECITED",
            default_tables == [("iceberg", "globgrph", "graph_nodes"),
                               ("code_heat", "globgrph", "code_heat")]
            and custom == [("hive", "other", "thing"), ("code_heat", "globgrph", "code_heat")],
            "canonical SQL -> %r ; a DIFFERENT --sql -> %r (2 of 2 statements parsed)"
            % (default_tables, custom))

    # ---- ARM B: Glue is a LOCATION source, never a TIME source (a 17-day disagreement) ----
    plane_b = FakePlane(
        glue_locations={("globgrph", "code_heat"): "s3://bkt/warehouse/code_heat/"},
        objects={"warehouse/code_heat/": [
            ("warehouse/code_heat/repo=ajb_workspace/code_heat.parquet",
             PARQUET_BUILD_TIME - _dt.timedelta(seconds=1)),
            ("warehouse/code_heat/repo=portal/code_heat.parquet", PARQUET_BUILD_TIME)]})
    rows_b = fv.vintage_rows(["SELECT 1 FROM code_heat.globgrph.code_heat"], plane=plane_b)
    got_b = rows_b[0]["build_time"]
    _record("B-GLUE-IS-A-LOCATION-SOURCE-NOT-A-TIME-SOURCE",
            len(rows_b) == 1 and rows_b[0]["claim"] == "measured"
            and got_b == PARQUET_BUILD_TIME and got_b != GLUE_UPDATE_TIME,
            "reported build_time=%s (the ARTIFACT's); the catalog row's UpdateTime is %s and is "
            "NOT what was reported -- they disagree by %.1f days"
            % (got_b, GLUE_UPDATE_TIME,
               (PARQUET_BUILD_TIME - GLUE_UPDATE_TIME).total_seconds() / 86400.0))

    # ---- ARM C: the <table>_<uuid>/ convention join is NON-ZERO on a case known to exist ----
    plane_c = FakePlane(children=REAL_WAREHOUSE_CHILDREN,
                        objects={ICEBERG_PREFIX: [(ICEBERG_PREFIX + "metadata/x.metadata.json",
                                                   _dt.datetime(2026, 9, 5, 2, 11, 10, tzinfo=UTC))]})
    b_c, p_c, how_c, why_c = fv.resolve_location("iceberg", "globgrph", "graph_nodes", plane_c)
    # NEGATIVE CONTROL, in the same arm: a table with no directory must be UNREAD, never a guess.
    _b0, _p0, _how0, why0 = fv.resolve_location("iceberg", "globgrph", "no_such_table", plane_c)
    _record("C-CONVENTION-JOIN-NONZERO-ON-A-KNOWN-CASE-PLUS-ZERO-MATCH-CONTROL",
            p_c == ICEBERG_PREFIX and why_c is None and b_c
            and why0 is not None and "matched 0 directory" in why0,
            "graph_nodes -> 1 of %d child prefix(es) -> %s | NEGATIVE CONTROL no_such_table -> %s"
            % (len(REAL_WAREHOUSE_CHILDREN), p_c, (why0 or "")[:110]))

    # ---- ARM D: a TRUNCATED listing is UNREAD, never a max-over-a-partial-read ----
    many = [("warehouse/globgrph/big/k%05d" % i,
             _dt.datetime(2026, 1, 1, tzinfo=UTC) + _dt.timedelta(days=i)) for i in range(400)]
    plane_d = FakePlane(children=[ICEBERG_PREFIX], objects={ICEBERG_PREFIX: many},
                        per_object_delay=0.002)
    rows_d = fv.vintage_rows(["SELECT 1 FROM iceberg.globgrph.graph_nodes"], plane=plane_d,
                             table_ceiling_s=0.05)
    _record("D-TRUNCATED-LISTING-IS-UNREAD-NOT-A-PARTIAL-MAX",
            len(rows_d) == 1 and rows_d[0]["build_time"] is None
            and rows_d[0]["claim"] == "absent"
            and "lexicographically" in (rows_d[0]["reason"] or "")
            and 0 < rows_d[0]["scanned"] < len(many),
            "scanned %d of %d object(s) then stopped; build_time=%r claim=%s -- reason: %s"
            % (rows_d[0]["scanned"], len(many), rows_d[0]["build_time"], rows_d[0]["claim"],
               (rows_d[0]["reason"] or "")[:120]))

    # ---- ARM E: an UNREGISTERED catalog is UNREAD with a reason, never guessed ----
    rows_e = fv.vintage_rows(["SELECT 1 FROM hive.other.thing"], plane=FakePlane())
    _record("E-UNREGISTERED-CATALOG-IS-UNREAD-WITH-A-REASON",
            len(rows_e) == 1 and rows_e[0]["claim"] == "absent"
            and "not in this tool's vintage registry" in (rows_e[0]["reason"] or "")
            and rows_e[0]["build_time"] is None,
            (rows_e[0]["reason"] or "")[:180])

    # ---- ARM F: a spent budget is UNREAD with a reason, never a default timestamp ----
    rows_f = fv.vintage_rows([Q_CODE_BANDS], plane=FakePlane(), budget_remaining=0)
    _record("F-SPENT-BUDGET-IS-UNREAD-NOT-A-DEFAULT",
            len(rows_f) == 2 and all(r["claim"] == "absent" and r["build_time"] is None
                                     for r in rows_f)
            and all("budget was already spent" in (r["reason"] or "") for r in rows_f),
            "2 of 2 tables UNREAD with the budget reason; 0 fabricated timestamps")

    # ---- ARM G: RED MUTANT -- the build time replaced by the QUERY CLOCK ----
    needle = "    return _probe_prefix(plane, bucket, prefix, deadline, object_cap)"
    src = ENGINE.read_text(encoding="utf-8")
    if src.count(needle) != 1:
        raise AssertionError("mutation anchor count != 1: %d" % src.count(needle))
    tmp = tempfile.mkdtemp(prefix="os4-mutant-")
    try:
        mpath = Path(tmp) / "federated_vintage.py"
        mpath.write_text(
            src.replace(needle,
                        "    return _now_utc(), 1, False, None  # RED MUTANT: the QUERY CLOCK", 1),
            encoding="utf-8")
        mfv = _load(mpath, "os4_fv_mutant")
        rows_g = mfv.vintage_rows(["SELECT 1 FROM code_heat.globgrph.code_heat"], plane=FakePlane(
            glue_locations={("globgrph", "code_heat"): "s3://bkt/warehouse/code_heat/"},
            objects={"warehouse/code_heat/": [("k", PARQUET_BUILD_TIME)]}))
        mut_t = rows_g[0]["build_time"]
        now = _dt.datetime.now(UTC)
        drift = abs((mut_t - now).total_seconds()) if mut_t else -1
        _record("G-RED-MUTANT-PRINTS-THE-QUERY-CLOCK-AND-IS-CAUGHT",
                mut_t is not None and drift < 120 and mut_t != PARQUET_BUILD_TIME,
                "mutant build_time=%s is within %.1f s of the query clock instead of the "
                "artifact's %s (%.1f days apart) -- the exact substitution this cell exists to "
                "prevent" % (mut_t, drift, PARQUET_BUILD_TIME,
                             abs((now - PARQUET_BUILD_TIME).total_seconds()) / 86400.0))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    _record("H-MUTATION-ANCHOR-UNIQUE",
            ENGINE.read_text(encoding="utf-8").count(needle) == 1
            and ENGINE.read_text(encoding="utf-8").count("def _now_utc") == 1,
            "one occurrence of the mutated return and one _now_utc definition")

    # ---- ARM I: THE ONE LIVE ARM -- the real CLI, bounded, and it must NOT dispatch ----
    started = time.monotonic()
    live = _run_cli("federated", "--budget", "120", timeout=115)
    elapsed = time.monotonic() - started
    out = live.stdout
    vline = next((x for x in out.splitlines() if x.startswith("VINTAGE:")), "")
    ch = next((x for x in out.splitlines() if "code_heat.globgrph.code_heat" in x
               and "build_time=" in x), "")
    gn = next((x for x in out.splitlines() if "iceberg.globgrph.graph_nodes" in x
               and "build_time=" in x), "")
    stamp = ""
    if "build_time=" in ch:
        stamp = ch.split("build_time=", 1)[1].split()[0]
    # PARSED_OK IS SEPARATE FROM FRESH ON PURPOSE. If an unparseable stamp merely made `fresh`
    # False, "not fresh" would read as "not the query clock" and this arm would PASS on a broken
    # timestamp -- a confident green from a blind read, the failure mode this project keeps meeting.
    parsed_ok, fresh, age_days = False, True, None
    if stamp and stamp != "UNREAD":
        try:
            got = _dt.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
            parsed_ok = True
            delta = abs((got - _dt.datetime.now(UTC)).total_seconds())
            fresh, age_days = delta < 600, delta / 86400.0
        except ValueError:
            parsed_ok = False
    _record("I-LIVE-CLI-CARRIES-VINTAGE-AND-DID-NOT-DISPATCH",
            live.returncode == 0 and vline.startswith("VINTAGE:")
            and "refusing to dispatch to the LIVE Trino plane" in out
            and "claim=measured" in ch and parsed_ok and not fresh
            and "claim=absent" in gn and "reason:" in out,
            "rc=%d in %.1fs | %s | %s | stamp=%r parsed=%s age=%s d | not-the-query-clock=%s | "
            "refusal present=%s"
            % (live.returncode, elapsed, vline[:90], ch.strip()[:90], stamp, parsed_ok,
               ("%.1f" % age_days) if age_days is not None else "n/a", parsed_ok and not fresh,
               "refusing to dispatch to the LIVE Trino plane" in out))


def _report() -> int:
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    print("OS4-FEDERATED-VINTAGE BATTERY: %d/%d PASS (denominator %d; 8 offline, 1 live-bounded, "
          "0 Trino queries dispatched)"
          % (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    assert not failed, "comp-heat OS4 federated-vintage battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
