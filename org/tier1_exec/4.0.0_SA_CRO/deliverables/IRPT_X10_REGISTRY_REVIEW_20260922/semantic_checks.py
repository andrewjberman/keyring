from pathlib import Path
import json
import re
import hashlib
import importlib.util
import sys
import subprocess
import ast

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
src = Path(r"C:\Users\AndrewBerman\Desktop\ajb_irpt_m")
shared = Path(r"C:\Users\AndrewBerman\Desktop\ajb_workspace")


def git(*args, repo=src):
    return subprocess.check_output(["git", "-C", str(repo), *args])


pins = json.loads((ROOT / "evidence/input_manifest.json").read_text())["pins"]
spec = importlib.util.spec_from_file_location(
    "cro_pinned_candidate", ROOT / "snapshots/candidate/lib/opal_naming.py"
)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
p = m.reporting_policy("irpt-x10-v1")
expected = {
    "ORIGINAL_CSV",
    "NORMALIZED_PORTFOLIO",
    "REQUEST_COMPOSITION",
    "ORIGINAL_VENDOR_PDF",
    "EXTRACTION_EVIDENCE",
    "PERFORMANCE",
    "ANALYSIS",
    "EXPORT_BUNDLE",
    "EXPORT_PDF",
    "EXPORT_RECEIPT",
    "SELECTED_ACCOUNTS",
    "PERFORMANCE_SOURCE_EVIDENCE",
}
checks = {}
checks["exact_12_families"] = set(p["families"]) == expected
checks["exact_3_private_firms"] = p["firms"] == [
    "49financial",
    "cottonwood",
    "inflection",
]
checks["ten_state_two_platinum"] = sum(
    x["tier"] == "state" for x in p["families"].values()
) == 10 and {k for k, v in p["families"].items() if v["tier"] == "platinum"} == {
    "PERFORMANCE",
    "ANALYSIS",
}
checks["x10_reference_exact"] = (
    p["register_commit"] == pins["x10"]
    and p["register_path"] == "infra/logic/06_CONFORMANCE_LEDGER.md"
    and p["register_id"] == "X10"
)
checks["ruling_reference_resolves_exact"] = (
    git("rev-parse", p["ruling_commit"] + "^{commit}").decode().strip()
    == pins["ruling"]
)
checks["source_and_product_irpt"] = p["source"] == p["product_scope"] == "irpt"
checks["pending_null_enforcement_open_disposal"] = (
    p["state"] == "PENDING_ENFORCEMENT"
    and p["enforcement_ref"] is None
    and p["physical_disposal"] == "OPEN"
)
checks["retention_id_exact"] = p["retention_policy_id"] == "irpt-retention-v1"
for family, v in p["families"].items():
    draft = (
        None
        if family in {"PERFORMANCE", "ANALYSIS"}
        else 7
        if family.startswith("EXPORT_")
        else 30
    )
    checks["retention_" + family] = v["unreferenced_days"] == draft and v[
        "accepted_ceiling_days"
    ] == (30 if family == "SELECTED_ACCOUNTS" else 2555)
checks["source_evidence_request_state"] = (
    p["families"]["PERFORMANCE_SOURCE_EVIDENCE"]["table"]
    == "performance_source_evidence"
    and p["families"]["PERFORMANCE_SOURCE_EVIDENCE"]["tier"] == "state"
)
row = next(s for s in m.load_registry()["scopes"]["scopes"] if s["key"] == "irpt")
checks["unprovisioned_product_scope"] = (
    row["class"] == row["tenancy"] == "PRODUCT"
    and row["bucket"] == "opal-data-irpt"
    and row["bucket_provisioned"] is False
    and row["aliases"] == []
)
refusals = []
previews = []
for firm in p["firms"]:
    for family in sorted(expected):
        args = (firm, family, "ART-" + "a" * 64, "b" * 64)
        view = m.preview_reporting_destination(*args, policy_revision="irpt-x10-v1")
        previews.append(
            view["writable"] is False
            and view["key"].startswith("irpt/" + firm + "/")
            and view["bucket"] == "opal-data-irpt"
            and view["policy_sha256"] == p["policy_sha256"]
        )
        try:
            m.reporting_destination(*args, policy_revision="irpt-x10-v1")
            refusals.append(False)
        except ValueError as e:
            refusals.append("not writable" in str(e))
checks["all36_pending_writers_refuse"] = len(refusals) == 36 and all(refusals)
checks["all36_private_previews_nonwritable"] = len(previews) == 36 and all(previews)
negative = []
for firm, family, aid, digest, rev in [
    ("global", "PERFORMANCE", "ART-" + "a" * 64, "b" * 64, "irpt-x10-v1"),
    ("49f", "PERFORMANCE", "ART-" + "a" * 64, "b" * 64, "irpt-x10-v1"),
    ("demo", "PERFORMANCE", "ART-" + "a" * 64, "b" * 64, "irpt-x10-v1"),
    ("49financial", "NOT_ALLOWED", "ART-" + "a" * 64, "b" * 64, "irpt-x10-v1"),
    ("49financial", "PERFORMANCE", "../x", "b" * 64, "irpt-x10-v1"),
    ("49financial", "PERFORMANCE", "ART-" + "a" * 64, "..", "irpt-x10-v1"),
    ("49financial", "PERFORMANCE", "ART-" + "a" * 64, "b" * 64, "not-registered"),
]:
    try:
        m.preview_reporting_destination(firm, family, aid, digest, policy_revision=rev)
        negative.append(False)
    except ValueError:
        negative.append(True)
checks["seven_input_negatives_refuse"] = len(negative) == 7 and all(negative)
checks["nine_default_firm_homes_unchanged"] = all(
    m.address("irpt", f, t, "holdings", "2026-09-22").startswith(
        "s3://opal-data-" + f + "/"
    )
    for f in p["firms"]
    for t in ["gold", "platinum", "state"]
)


def unstamped(s):
    return re.sub(r"registry@[0-9a-f]{16}", "registry@STAMP", s)


gen = json.loads((ROOT / "evidence/reproduction.json").read_text())[
    "generated_carriers"
]
asts = {}
for item in gen:
    path = item["path"]
    b = (ROOT / "generated/baseline" / path).read_text()
    c = (ROOT / "generated/candidate" / path).read_text()
    if path.endswith(".py"):
        asts[path] = ast.dump(ast.parse(b)) == ast.dump(ast.parse(c))
    if path.endswith("generated_locals.tf"):
        source = (ROOT / "snapshots/baseline" / path).read_text()
        irpt = [x.strip() for x in c.splitlines() if re.match(r'\s*"irpt"\s*=', x)]
        clean_c = (
            "\n".join(x for x in c.splitlines() if not re.match(r'\s*"irpt"\s*=', x))
            + "\n"
        )
        checks["terraform_exact_four_irpt_mappings"] = len(irpt) == 4 and unstamped(
            clean_c
        ) == unstamped(b)
        noharvest = "\n".join(
            x for x in b.splitlines() if not re.match(r'\s*"harvest"\s*=', x)
        )
        checks["baseline_harvest_stamp_whitespace_only"] = re.sub(
            r"\s+", "", unstamped(source)
        ) == re.sub(r"\s+", "", unstamped(noharvest))
checks["five_python_generated_asts_equal"] = len(asts) == 5 and all(asts.values())
sharedpin = git("rev-parse", "HEAD", repo=shared).decode().strip()
scopefile = "infra/logic/registry/scopes.json"
c = json.loads(git("show", pins["candidate"] + ":" + scopefile))
c["scopes"] = [s for s in c["scopes"] if s["key"] != "irpt"]
checks["non_irpt_scopes_match_fresh_shared"] = c == json.loads(
    git("show", sharedpin + ":" + scopefile, repo=shared)
)
checks["shared_library_matches_baseline"] = git(
    "show", sharedpin + ":lib/opal_naming.py", repo=shared
) == git("show", pins["baseline"] + ":lib/opal_naming.py")
checks["candidate_direct_parent_baseline"] = (
    git("rev-parse", pins["candidate"] + "^").decode().strip() == pins["baseline"]
)
grantpaths = (
    git("diff-tree", "--no-commit-id", "--name-only", "-r", pins["grant"])
    .decode()
    .splitlines()
)
checks["consumed_grant_blobs_equal"] = all(
    git("show", pins["grant"] + ":" + path)
    == git("show", pins["baseline"] + ":" + path)
    for path in grantpaths
)
checks["consumed_grant_author_equal"] = git(
    "show", "-s", "--format=%an <%ae>", pins["grant"]
) == git("show", "-s", "--format=%an <%ae>", pins["baseline"])
peerpin = git("rev-parse", "eb00a0c6b2^{commit}").decode().strip()
peer = git(
    "show",
    peerpin
    + ":org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/REGISTRY_REVIEW_587E.md",
)
(ROOT / "evidence/peer_CVO_REVIEW.md").write_bytes(peer)
result = {
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "failures": [k for k, v in checks.items() if not v],
    "writer_refusals": sum(refusals),
    "private_previews": sum(previews),
    "negative_refusals": sum(negative),
    "generated_python_asts": asts,
    "terraform_irpt_mappings": irpt,
    "policy_sha256": p["policy_sha256"],
    "policy_file_sha256": hashlib.sha256(
        (
            ROOT / "snapshots/candidate/infra/logic/registry/reporting_policies.json"
        ).read_bytes()
    ).hexdigest(),
    "fresh_shared_pin": sharedpin,
    "peer_pin": peerpin,
    "grant_paths": grantpaths,
    "runtime_controls": "Recorded via X10/ruling; enforcement excluded while pending. ACTIVE enforcement_ref is syntactically checked only; fabricated hash in producer test is not runtime acceptance.",
}
(ROOT / "evidence/semantic_checks.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
raise SystemExit(bool(result["failures"]))
