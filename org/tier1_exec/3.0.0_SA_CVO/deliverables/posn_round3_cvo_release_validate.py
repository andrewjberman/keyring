"""Exercise the real LD-0562 gate branch and reject near misses without mutation."""

import copy
import datetime
import importlib.util
import json
from pathlib import Path
import subprocess
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[4]
PREFIX = "org/tier1_exec/3.0.0_SA_CVO/deliverables/"
PACKAGE = PREFIX + "POSN_ASTTAX_ROUND3_RELEASE_PACKAGE_20260913_Z.json"
OUT = PREFIX + "POSN_ASTTAX_ROUND3_RELEASE_VALIDATION_20260913_Z.json"


def main():
    spec = importlib.util.spec_from_file_location(
        "gate", ROOT / ".tools/surprise-row-gate.py"
    )
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    pin = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    package = json.loads((ROOT / PACKAGE).read_text(encoding="utf-8"))
    record_status, record_text = g._blob(
        str(ROOT), g.POSN_R3_EXCEPTION_PIN, g.POSN_R3_EXCEPTION_PATH
    )
    assert record_status == "OK"
    record = json.loads(record_text)
    census = g._open_tos_for_project(str(ROOT), "POSN_ASTTAX")
    assert len(census[0]) == 4 and census[1] == 15 and not census[2], census
    parsed = {}
    controls = []
    for path, body in package["files"].items():
        rows, bad = g._rows(body, False)
        assert not bad
        kind = "REMEDIATION" if "/remediations/" in path else "INVESTIGATION"
        for row in rows:
            assert not g._check_row(row, kind, g._schema(str(ROOT), kind)), row["id"]
        parsed[path] = rows
    matched = 0
    for item in record["rows"]:
        row = next(r for r in parsed[item["path"]] if r["id"] == item["id"])
        assert g._canon_hash(row) == item["sha256"]
        assert not g._route_precondition_violations(
            str(ROOT), item["path"], row, "POSN_ASTTAX", census
        )
        matched += 1
    controls.append(
        {
            "case": "all exact authorized rows accepted by actual route gate",
            "count": matched,
            "pass": True,
        }
    )
    entry = record["rows"][0]
    rel = entry["path"]
    row = next(r for r in parsed[rel] if r["id"] == entry["id"])

    def rejects(label, candidate=None, path=rel, code="POSN_ASTTAX", orders=census):
        result = g._route_precondition_violations(
            str(ROOT), path, candidate or row, code, orders
        )
        assert result, label
        controls.append({"case": label, "pass": True, "refusal": result})

    mutant = copy.deepcopy(row)
    mutant["notes"] += " unauthorized change"
    rejects("same ID but changed row bytes", mutant)
    mutant = copy.deepcopy(row)
    mutant["id"] = "POSN_ASTTAX-Z-C-S999"
    rejects("new unrecorded row ID", mutant)
    rejects("next round path", path=rel.replace("v5.md", "v6.md"))
    rejects("old round path", path=rel.replace("v5.md", "v3.md"))
    rejects("other project", code="AMGT_RESAPP")
    rejects("fifth open order", orders=(census[0] + ["extra [staged]"], 16, ""))
    rejects("changed total with same open set", orders=(census[0], 16, ""))
    rejects(
        "same count but different open identity",
        orders=(["extra [staged]"] + census[0][1:], 15, ""),
    )
    rejects("unreadable order census", orders=(None, 15, "control unreadable"))
    original_blob = g._blob

    def changed_order(root, revision, path):
        state, text = original_blob(root, revision, path)
        if revision == "HEAD" and path == record["orders"][0]["path"]:
            return state, text + "\nchanged control\n"
        return state, text

    with patch.object(g, "_blob", changed_order):
        rejects("same open status but changed order content")

    def missing_record(root, revision, path):
        if revision == g.POSN_R3_EXCEPTION_PIN and path == g.POSN_R3_EXCEPTION_PATH:
            return "MISSING", ""
        return original_blob(root, revision, path)

    with patch.object(g, "_blob", missing_record):
        rejects("missing immutable authority record")

    def corrupted_record(root, revision, path):
        if revision == g.POSN_R3_EXCEPTION_PIN and path == g.POSN_R3_EXCEPTION_PATH:
            return "OK", "not json"
        return original_blob(root, revision, path)

    with patch.object(g, "_blob", corrupted_record):
        rejects("malformed immutable authority record")
    latest, unknown, documents, note = g._latest_dispositions(str(ROOT), "POSN_ASTTAX")
    assert not unknown and not note
    files = []
    rem_ids = []
    for pattern in (
        g.INVESTIGATION_PATTERNS + g.ADJUDICATION_PATTERNS + g.REMEDIATION_PATTERNS
    ):
        paths, err = g._index_paths(str(ROOT), [pattern % "POSN_ASTTAX"])
        assert paths is not None, err
        for path in paths:
            if path in parsed:
                continue
            rows, bad = g._rows(
                (ROOT / path).read_text(encoding="utf-8"), path.endswith(".json")
            )
            assert not bad
            if g._kind(path) == "REMEDIATION":
                rem_ids.extend(r["id"] for r in rows)
            else:
                files.append((path, rows))
    for path, rows in parsed.items():
        if g._kind(path) == "REMEDIATION":
            rem_ids.extend(r["id"] for r in rows)
        else:
            files.append((path, rows))
    prospective, unknown = g._resolve_latest(files, rem_ids)
    pending = [k for k, v in prospective.items() if v == "UNDER_INVESTIGATION"]
    assert not pending and not unknown, (pending, unknown)
    rem_path = next(p for p in parsed if "/remediations/" in p)
    rem_row = parsed[rem_path][0]
    assert not g._investigations_precondition_violations(
        str(ROOT), rem_row, "POSN_ASTTAX", "control", (prospective, [], documents, "")
    )
    pending_mutant = dict(prospective)
    pending_mutant[next(iter(pending_mutant))] = "UNDER_INVESTIGATION"
    assert g._investigations_precondition_violations(
        str(ROOT),
        rem_row,
        "POSN_ASTTAX",
        "control",
        (pending_mutant, [], documents, ""),
    )
    controls.append(
        {
            "case": "investigation-completion limb still rejects a pending original",
            "pass": True,
        }
    )
    schema_mutant = dict(rem_row)
    schema_mutant.pop("remedy")
    assert g._check_row(
        schema_mutant, "REMEDIATION", g._schema(str(ROOT), "REMEDIATION")
    )
    controls.append({"case": "required-field schema limb still rejects", "pass": True})
    assert not g._posn_round2_terminal_exception(
        str(ROOT), rel, row, "POSN_ASTTAX", census[0], 15
    )
    controls.append({"case": "round-2 exception does not admit round 3", "pass": True})
    result = {
        "head": pin,
        "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "immutable_record_pin": g.POSN_R3_EXCEPTION_PIN,
        "controls": controls,
        "exact_authorized_rows": matched,
        "originals": len(prospective),
        "pending_after_proposed": pending,
        "unknown": unknown,
        "orders": census,
        "limits": "Read-only gate controls, in-process blob substitutions only. No order mutation, staging, override, network call or production act.",
    }
    (ROOT / OUT).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "controls": len(controls),
                "all_pass": True,
                "exact_rows": matched,
                "originals": len(prospective),
                "pending": pending,
                "output": OUT,
            }
        )
    )


if __name__ == "__main__":
    main()
