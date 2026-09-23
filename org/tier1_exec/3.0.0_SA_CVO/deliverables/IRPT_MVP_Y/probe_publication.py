"""Pinned actual-PDF certifier and retained-extraction coverage review, offline."""
import argparse
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import zipfile


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="bcfbd380a12e88d06f2c26f7ad48f0ddc4feb212")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(["git", "rev-parse", "--verify", args.pin + "^{commit}"],
                                  cwd=root, text=True).strip()
    snapshot = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/publication-review" / pin
    snapshot.mkdir(parents=True, exist_ok=True)
    source_root = "infra/aws/lambda/investor-reporting/ycharts/extract"
    census_file = "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json"
    archive = subprocess.check_output(["git", "archive", "--format=zip", pin, source_root,
        "docs/contracts/investor-reporting/v1/AnalysisReport.schema.json", census_file], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            path = (snapshot / member.filename).resolve()
            if not path.is_relative_to(snapshot.resolve()):
                raise ValueError("snapshot path escape")
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
                continue
            data = bundle.read(member)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            hashes[member.filename] = hashlib.sha256(data).hexdigest()
    suite = subprocess.run([sys.executable, "-m", "pytest", source_root + "/tests/test_publication.py",
                            "-q"], cwd=snapshot, capture_output=True, text=True, check=False)
    subject = load("publication_review_tests", snapshot / source_root / "tests/test_publication.py")
    census = json.loads((snapshot / census_file).read_text(encoding="utf-8"))
    pdf = (snapshot / source_root / "fixtures/synthetic_pdf/overview.pdf").read_bytes()
    extracted = subject.extract.extract(pdf, census, specimen_label="synthetic", specimen_id="overview")
    row = next(row for row in extracted["sections"] if row["section_id"] == "S01.advisory_fee.c0")
    mutant = copy.deepcopy(row)
    mutant["value"] = 123.3
    baseline_pin = subprocess.check_output(["git", "rev-parse", "2d2c774452"], cwd=root, text=True).strip()
    baseline_bytes = subprocess.check_output(["git", "show", baseline_pin + ":" + source_root + "/certify.py"], cwd=root)
    baseline_path = snapshot / "baseline_certify.py"
    baseline_path.write_bytes(baseline_bytes)
    dependency_equal = {}
    for name in ("extract.py", "fonts.py"):
        old = subprocess.check_output(["git", "show", baseline_pin + ":" + source_root + "/" + name], cwd=root)
        dependency_equal[name] = old == (snapshot / source_root / name).read_bytes()
    if not all(dependency_equal.values()):
        raise ValueError("baseline certifier dependencies differ; cannot share candidate imports")
    old_certifier = load("baseline_certifier_review", baseline_path)
    numeric = {"section_id": row["section_id"], "original_value": row["value"],
               "mutant_value": mutant["value"], "unchanged_token": row.get("_token"),
               "unchanged_page_bbox": [row["page"], row["bbox"]],
               "baseline_pin": baseline_pin, "baseline_dependency_equal": dependency_equal,
               "baseline_certifier_sha256": hashlib.sha256(baseline_bytes).hexdigest(),
               "baseline_mutant": old_certifier.certify([mutant], pdf, census=census),
               "candidate_original": subject.certify.certify([row], pdf, census=census),
               "candidate_mutant": subject.certify.certify([mutant], pdf, census=census)}
    variants = {}
    for variant in ("overview", "comparison", "multicomp"):
        data = (snapshot / source_root / "fixtures/synthetic_pdf" / (variant + ".pdf")).read_bytes()
        result = subject.publication.build_publication(data, census, specimen_label="synthetic", specimen_id=variant)
        variants[variant] = result["fragment"]["extraction_coverage"]
    synthetic_pdf, synthetic_census = subject.pdf(), subject.census()
    retained = subject.extracted(synthetic_pdf)
    positive = subject.publication.verify_extraction(synthetic_pdf, synthetic_census, retained)
    omitted = copy.deepcopy(retained)
    omitted["charts"] = []
    omitted["disclosures"] = []
    try:
        omission = subject.publication.verify_extraction(synthetic_pdf, synthetic_census, omitted)
        omission_control = {
            "coverage": omission["fragment"]["extraction_coverage"],
            "disclosures": omission["fragment"]["disclosures"],
            "complete_despite_omission": omission["fragment"]["extraction_coverage"]["status"]
                == "COMPLETE_FOR_CENSUS"}
    except subject.publication.PublicationRefused as exc:
        omission_control = {"refused": str(exc), "complete_despite_omission": False}
    omission_control["expected"] = "Refuse retained census mismatch or expose missing chart/disclosure gaps"
    absent_text = copy.deepcopy(retained)
    absent_text["disclosures"][0]["text"] = "This sentence does not occur in the source PDF."
    try:
        absent = subject.publication.verify_extraction(synthetic_pdf, synthetic_census, absent_text)
        absent_control = absent["fragment"]["extraction_coverage"]
    except subject.publication.PublicationRefused as exc:
        absent_control = {"refused": str(exc)}
    changed_source = subject.pdf(token="99.99%")
    try:
        subject.publication.verify_extraction(changed_source, synthetic_census, retained)
        changed_source_outcome = "RETURNED"
    except subject.publication.PublicationRefused as exc:
        changed_source_outcome = str(exc)
    controls = {"positive_coverage": positive["fragment"]["extraction_coverage"],
                "omitted_chart_and_disclosure": omission_control,
                "absent_disclosure_text": absent_control,
                "changed_source_pdf": changed_source_outcome}
    evidence = {"candidate_pin": pin, "file_sha256": hashes,
                "supplied_suite": {"exit_code": suite.returncode, "stdout": suite.stdout, "stderr": suite.stderr},
                "original_numeric_failure_control": numeric, "variant_coverage": variants,
                "independent_source_coverage_controls": controls,
                "limits": ["Actual PDF bytes, extractor, certifier and fragment boundary",
                           "Synthetic PDFs only; no vendor or cloud calls",
                           "No repository publication, report READY or full Y5/E2E proof"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_pin": pin, "supplied_suite": evidence["supplied_suite"],
                      "controls": controls, "evidence_path": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
