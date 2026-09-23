from pathlib import Path
import json
import re
import subprocess

root = Path(__file__).resolve().parent
repo = root.parents[4]
order = "org/tier1_exec/4.0.0_SA_CRO/task_orders/IRPT-X10_REGISTRY_REVIEW_20260922.md"
report = "org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/REVIEW.md"
pin = subprocess.check_output(
    ["git", "log", "-1", "--format=%H", "--", report], cwd=repo, text=True
).strip()
assert pin
assert (
    "Bounded owner verdict: PASS"
    in subprocess.check_output(["git", "show", pin + ":" + report], cwd=repo).decode()
)
criteria = dict(
    re.findall(
        r'<criterion id="([^"]+)">(.*?)</criterion>',
        (repo / order).read_text(encoding="utf-8"),
        re.S,
    )
)
receipts = root / "review_notice_receipts.txt"
sent = (
    receipts.exists()
    and receipts.read_text(encoding="utf-8-sig").count("Message delivered to ") == 3
)
evidence = {
    "C1": "Exact pins in input_manifest.json; candidate parent equals baseline 78a48596640f32d908955941a2c52dbb713235c6. Consumed CTO grant blobs/author match original grant; canonical X10 705dae3202 and ruling resolve exactly. Fresh shared comparison at 45b0908ccc595bf72dc3cbfdf74f94d8d7272526 matches incumbent scopes and library. semantic_checks.json: 34 checks, 34 true, zero failures.",
    "C2": "Bounded owner PASS only for PENDING_ENFORCEMENT candidate 587e782bc6. Exact 12 families/3 firms/10 state/2 platinum and all family retention metadata match X10; enforcement_ref null, disposal OPEN. 36/36 writers refuse, 36/36 previews private/nonwritable, seven negatives refuse, nine default firm homes unchanged. REVIEW.md condition matrix distinguishes metadata and current refusals from unproven authorization, retention/dependency/race, IAM, byte secrecy, immutable storage and activation controls.",
    "C3": "20/20 generated output hashes reproduced by independent baseline/candidate runs. Nine stamp-only deltas; five Python ASTs equal; Terraform adds exactly four IRPT maps. Baseline harvest/stamp/whitespace drift independently reproduced without IRPT. Ten source carriers unchanged; non-IRPT scopes and five incumbent registry blobs equal. Targeted tests 60 PASS; canonical validate rc0/33 warnings. CRO core naming suite both 80 PASS/same 5 FAIL/8 deselected; CVO full-suite evidence eb00a0c6b2 reports 88 PASS/same 5 FAIL, separately attributed. No uncovered full-suite result represented as CRO PASS.",
    "C4": receipts.read_text(encoding="utf-8-sig")
    if sent
    else "Report and evidence committed at "
    + pin
    + "; three report-pin delivery receipts pending.",
}
acceptance = []
for key in ["C1", "C2", "C3", "C4"]:
    row = {
        "criterion_id": key,
        "criterion_verbatim": criteria[key],
        "method": "manual_read_with_citation" if key == "C2" else "command",
        "invocation": "python -B org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/semantic_checks.py"
        if key != "C4"
        else 'org/mcp/codex-send.ps1 -To <each of COO~M, CTO, CVO~M> -Subject "IRPT X10 owner verdict PASS for pending candidate" -BodyFile org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/review_notice.md',
        "output_evidence": evidence[key],
        "denominator": {
            "C1": "7 primary pins, 34 semantic/provenance checks",
            "C2": "12 families, 3 firms, 36 writer/preview pairs, 7 negative inputs, 9 default homes",
            "C3": "10 carriers, 20 output hashes, 5 Python ASTs, 60 targeted tests, 85/93 CRO naming cases",
            "C4": "3 required recipient seats; 1 report and 1 proof",
        }[key],
        "status": "PASS",
    }
    if key == "C4" and not sent:
        row.update(
            status="UNCOMPUTABLE-BY-CONSTRUCTION",
            status_reason="Finalize after canonical report-pin notices, then commit this proof and return its pin.",
        )
    acceptance.append(row)
proof = {
    "schema_version": "1.0",
    "to_id": "IRPT-X10_REGISTRY_REVIEW_20260922",
    "phase": "NON-BUILD-OTHER",
    "spec_ref": {
        "doc": order,
        "group": "OTHER",
        "vintage_commit": "8529764a5d3a5bf924237328a4af87c6243ed07e",
    },
    "assignee": "4.0.0_SA_CRO",
    "artifacts_produced": [
        {
            "path_or_key": report,
            "kind": "doc",
            "commit_or_etag": pin,
            "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE",
            "deploy_evidence": "Read-only owner review; no source, carrier, runtime or deployment changes.",
            "introduces": ["# IRPT X10 registry-owner review"],
            "artifact_covered_by": ["C1", "C2", "C3", "C4"],
        }
    ],
    "acceptance": acceptance,
    "controls": {
        "mutant": {
            "description": "The documentary owner-review order names no mutant; existing targeted negative controls and independent refusal probes were exercised.",
            "expected": "N/A: no new mutation requirement in this order.",
            "observed": "36 writer refusals and seven independent invalid-input refusals; 60 producer tests independently rerun.",
            "status": "N/A-SPEC-NAMES-NONE",
        },
        "determinism": {
            "method": "N/A: documentary review; baseline and candidate are distinct pinned inputs, not misrepresented as repeated same-input runs.",
            "observed": "All 20 hashes independently match producer baseline/candidate inventory; no runtime determinism claim.",
            "status": "N/A-WITH-REASON",
        },
    },
    "declared_exclusions": [
        {
            "item": "Runtime enforcement, ACTIVE policy, source/carrier integration, provisioning, deployment and product acceptance",
            "reason": "Explicitly outside review authority; X10 conditions remain pending and disposal OPEN.",
        },
        {
            "item": "Eight deployment/plane-dependent cases in the 93-case naming suite",
            "reason": "CRO extracted snapshots lack full tracked source-map/Terraform fixtures. Ran 85 core cases at both pins and separately cited CVO full-suite evidence; initial harness failures are retained and not attributed to candidate.",
        },
        {
            "item": "Consumer R-P07 expiry-crossing finding",
            "reason": "Reported in independent CVO review; not rerun in registry-owner scope and not cleared by this verdict.",
        },
    ],
    "surprises": [],
    "session_log": report,
    "compiler_tools": [
        {
            "tool": "comp-which",
            "invocation": 'comp-which "Read IRPT-X10_REGISTRY_REVIEW_20260922 order and pinned candidate evidence for registry owner review"',
            "result": "No curated match; selected comp-read by document concern.",
        },
        {
            "tool": "comp-read",
            "invocation": "comp-read "
            + order
            + ' --for "criteria paths proof baseline review" --top 10',
            "result": "Read order shape followed by exact committed full bytes.",
        },
        {
            "tool": "opal_naming.py validate/generate",
            "invocation": "python -B org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/review_checks.py",
            "result": "Exact baseline/candidate generation reproduced 20 hashes; candidate validate rc0 with 33 warnings. Final core-suite invocation explicitly excludes eight out-of-snapshot fixtures.",
        },
    ],
}
(root / "IRPT-X10_REGISTRY_REVIEW_20260922.proof_of_spec.json").write_text(
    json.dumps(proof, indent=2) + "\n", encoding="utf-8"
)
notice = f"""Bounded CRO owner verdict: PASS for the exact pending registry candidate 587e782bc6 and generated evidence 3c14153eeb only.
Committed immutable report/evidence pin: {pin}
Report: {report}

Independently verified 12 families/3 private firms/10 state + 2 platinum, exact retention metadata, 36 writer refusals/36 private nonwritable previews, 7 negatives, 9 unchanged default homes, 34 semantic/provenance checks. Targeted suite 60 passed; registry validate rc0 with 33 inherited warnings. Non-IRPT scope fields and five incumbent registry blobs unchanged; fresh shared-source comparison pinned in report.
Ten generated carriers independently regenerated at both pins: 20/20 inventory hashes match; nine stamp-only candidate deltas, five Python ASTs equal, exactly four IRPT Terraform mappings. Harvest/formatting drift independently reproduced from unchanged baseline; no carrier overwritten. Naming owner must disposition inherited drift separately and reconcile fresh shared state before integration.
CRO core naming suite: both 80 passed/same 5 failed/8 deselected (85/93 cases). Full 93-case 88/5 result is separately cited CVO evidence eb00a0c6b2, not claimed as CRO full-suite execution. Initial incomplete snapshot/temporary-directory harness errors are retained and explained, not candidate defects.

Report contains the full recorded-versus-enforced condition matrix. ACTIVE reference checking is syntactic, not proof of accepted enforcement. Pending remains non-writable; runtime authorization, source secrecy/versioning, retention/dependency/clock races, IAM, physical disposal and full S7 remain unproven. CVO-reported P-lane R-P07 remains open; this owner PASS does not clear it. No source repair, integration, deployment or product PASS.
Proof path: org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/IRPT-X10_REGISTRY_REVIEW_20260922.proof_of_spec.json. Final delivery receipts, bound validation and proof commit are being completed after these three report notices; final proof pin follows.
"""
(root / "review_notice.md").write_text(notice, encoding="utf-8")
print(json.dumps({"report_pin": pin, "notices_complete": sent}))
