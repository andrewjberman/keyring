"""Replay a captured frozen composition through the RESIDENT's own admission, then stop before the vendor.

    python resident_admission_replay.py --root <investor-reporting dir of the resident package> --schemas <v1 dir>
        --composition <composition.json> [--overlay <dir>]

This is what FrozenCompositionWorker does before any vendor call:
- CompositionAdmission(schema_directory).validate(frozen), which is the closed schema plus submission.compose_frozen_request
  plus request_composition.validate_bindings plus portfolio.verify_frozen_portfolio;
- recipe_snapshot.consume_configuration over the prepared recipe and settings.

Both use the package's own modules, from a copy of --root. --overlay replaces same-named modules in that copy (the fix
under test). No AWS, queue or vendor call: the next act after this in the resident is the vendor session.
"""
import argparse
import json
import os
import shutil
import sys
import tempfile


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--schemas", required=True)
    ap.add_argument("--composition", required=True)
    ap.add_argument("--overlay")
    a = ap.parse_args(argv)
    work = os.path.join(tempfile.mkdtemp(prefix="irpt-resident-replay-"), "investor-reporting")
    shutil.copytree(a.root, work)
    overlaid = []
    if a.overlay:
        for name in sorted(os.listdir(a.overlay)):
            src = os.path.join(a.overlay, name)
            if not os.path.isfile(src):
                continue
            for dp, _, fn in os.walk(work):
                if name in fn and "tests" not in dp.split(os.sep):
                    shutil.copyfile(src, os.path.join(dp, name))
                    overlaid.append(os.path.relpath(os.path.join(dp, name), work))
    for rel in ("ycharts/generate", "reports", "intake", "_scope", "_authz", "_ids", "_keys", "ops"):
        sys.path.insert(0, os.path.join(work, rel))
    print("resident copy", work, "| overlay", overlaid or "none")
    frozen = json.load(open(a.composition, encoding="utf-8"))
    from composition_admission import CompositionAdmission
    import recipe_snapshot
    admission = CompositionAdmission(a.schemas)
    stages = []
    try:
        admission.validate(frozen)
        stages.append("admission.validate (schema + compose_frozen_request + validate_bindings + verify_frozen_portfolio)")
        resolved = frozen["resolved"]
        prepared = {"source_descriptors": resolved["source_descriptors"], "recipe_source_id": resolved["recipe_source_id"],
                    "settings_source_id": resolved["settings_source_id"], "recipe_version": frozen["recipe_version"],
                    "settings": frozen["settings"], "comparisons": list(resolved.get("comparison_catalog") or {})}
        configuration = recipe_snapshot.consume_configuration(prepared)
        stages.append("recipe_snapshot.consume_configuration -> template %s (%s)" % (
            configuration["template"]["template_id"], configuration["template"]["variant"]))
        profile = resolved["profile"]
        stages.append("profile ready: report_title=%r prepared_for=%r" % (profile["report_title"], profile["prepared_for"]))
        rows = resolved["document"]["holdings"]["rows"]
        stages.append("frozen holdings for the vendor upload: %s (total %s)" % (
            ", ".join("%s %s" % (r["security_id"], r["dollars"]) for r in rows), resolved["document"]["holdings"]["total_dollars"]))
    except Exception as exc:
        cause = exc.__cause__
        print("REFUSED at stage %d: %s %s | cause %s %s" % (len(stages) + 1, type(exc).__name__, exc,
              type(cause).__name__ if cause else None, str(cause)[:300] if cause else ""))
        for s in stages:
            print("  reached:", s)
        return 1
    for s in stages:
        print("  reached:", s)
    print("RESULT: ADMITTED -- the resident's next act is the vendor session (identity/template reads, then holdings_upload)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
