"""The CRO's refusal arm for the cross-viewer title binding, on a served generate zip.

Usage: python title_binding_refusal_arm.py --zip <generate.zip> --composition <composition.json>

Loads the zip's own request_composition.py (extracted fresh) and grades one captured composition twice:
- as captured: validate_bindings must pass (the positive control);
- with the maintained recipe TITLE source re-bound to another principal: it must refuse SOURCE_OWNER_BINDING.
A local read; no AWS and no vendor.
"""
import argparse
import copy
import json
import os
import sys
import tempfile
import zipfile


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--composition", required=True)
    a = ap.parse_args()
    root = tempfile.mkdtemp(prefix="irpt-title-arm-")
    zipfile.ZipFile(a.zip).extractall(root)
    sys.path.insert(0, root)
    import request_composition as rc
    if not os.path.samefile(os.path.dirname(rc.__file__), root):
        raise SystemExit("ERROR: request_composition loaded from %s, not the zip" % rc.__file__)
    document = json.load(open(a.composition, encoding="utf-8"))
    resolved = document["resolved"]
    title_id = resolved["profile_provenance"]["report_title"]["source_id"]
    title = resolved["source_descriptors"][title_id]
    print("title source %r kind %s bound to %s" % (title_id, title["source_kind"], title["binding"].get("principal_id")))
    rc.validate_bindings(document)
    print("CONTROL: the captured composition validates")
    mutant = copy.deepcopy(document)
    binding = mutant["resolved"]["source_descriptors"][title_id]["binding"]
    binding["principal_id"] = "someone-else@opal.test"
    try:
        rc.validate_bindings(mutant)
    except rc.CompositionRefused as refusal:
        print("ARM 3: the title re-bound to another principal is REFUSED", refusal)
        return 0 if str(refusal) == "SOURCE_OWNER_BINDING" else 1
    print("ARM 3: FAIL -- the re-bound title was accepted")
    return 1


if __name__ == "__main__":
    sys.exit(main())
