"""Exercise check_file's emitted authority using the actual pinned exception rows."""

import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[4]


def main():
    spec = importlib.util.spec_from_file_location(
        "gate", ROOT / ".tools/surprise-row-gate.py"
    )
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    actual_blob = g._blob
    latest = g._latest_dispositions(str(ROOT), "POSN_ASTTAX")
    assert not latest[1] and not latest[3]
    results = []
    for number, pin, path, expected, excluded in (
        (
            3,
            g.POSN_R3_EXCEPTION_PIN,
            g.POSN_R3_EXCEPTION_PATH,
            "LD-0562 / COO 22245 / fa2b1764c4",
            "CTO 21533",
        ),
        (
            2,
            g.POSN_R2_EXCEPTION_PIN,
            g.POSN_R2_EXCEPTION_PATH,
            "Andrew call 1 YES / CTO 21533 / 10ceba8c43",
            "LD-0562",
        ),
    ):
        state, text = actual_blob(str(ROOT), pin, path)
        assert state == "OK"
        record = json.loads(text)
        entry = next(r for r in record["rows"] if "/adjudications/" in r["path"])
        rel = entry["path"]
        state, text = actual_blob(str(ROOT), "HEAD", rel)
        assert state == "OK"
        candidates, malformed = g._rows(text, False)
        assert not malformed
        row = next(r for r in candidates if r["id"] == entry["id"])
        assert g._canon_hash(row) == entry["sha256"]
        staged = "```json\n" + json.dumps([row]) + "\n```\n"
        orders = (
            [o["open_label"] for o in record["orders"]],
            record["expected_total_orders"],
            "",
        )

        def isolate_file(root, revision, file_path):
            if file_path == rel and revision == "HEAD":
                return "ABSENT", None
            if file_path == rel and revision == "":
                return "OK", staged
            return actual_blob(root, revision, file_path)

        # Isolate the note from the already-tested whole-channel census. The real
        # exception predicate still reads the actual immutable record and order bytes.
        with (
            patch.object(g, "_blob", isolate_file),
            patch.object(g, "_latest_dispositions", return_value=latest),
            patch.object(g, "_open_tos_for_project", return_value=orders),
        ):
            violations, notes = g.check_file(str(ROOT), rel)
        assert not violations, violations
        audit = [n for n in notes if "L10 NAMED EXCEPTION" in n]
        assert len(audit) == 1 and expected in audit[0] and excluded not in audit[0], (
            audit
        )
        results.append(
            {"round": number, "pass": True, "actual_check_file_note": audit[0]}
        )
    output = (
        ROOT
        / "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_EXCEPTION_AUDIT_20260913_Z.json"
    )
    output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
