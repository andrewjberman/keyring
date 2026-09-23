"""Independent offline review of one immutable Git candidate; no cloud clients."""
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone

PIN = "70598ece96498d639b0fb12104ffe9fd4b0d5718"
ROOT = Path(__file__).resolve().parents[5]
SOURCE = "infra/aws/lambda/investor-reporting/reports/repository.py"
TEST = "infra/aws/lambda/investor-reporting/reports/tests/test_repository.py"
SCHEMA = "docs/contracts/investor-reporting/v1/AnalysisReport.schema.json"


def main():
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-70598-review-"))
    hashes = {}
    for name in (SOURCE, TEST, SCHEMA):
        data = subprocess.check_output(["git", "show", PIN + ":" + name], cwd=ROOT)
        target = snapshot / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    spec = importlib.util.spec_from_file_location("candidate_tests", snapshot / TEST)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = io.StringIO()
    result = unittest.TextTestRunner(stream=output, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromModule(module))
    observations = []

    def case(name, fn):
        try:
            detail = fn()
            observations.append({"case": name, **detail})
        except Exception as exc:
            observations.append({"case": name, "grade": "ERROR", "error": repr(exc)})

    def fresh():
        fixture = module.RepositoryTests()
        fixture.setUp()
        return fixture

    def exact_subset():
        f = fresh()
        ref = f.persist()
        f.allowed.remove("A-two")  # unselected permission loss must not deny A-one
        loaded = f.repository.get(f.principal, ref["report_id"], ref["revision"])
        assert loaded["report"] == module.report()
        f.allowed.clear()
        try:
            f.repository.get(f.principal, ref["report_id"], ref["revision"])
        except module.repo.ReportDenied:
            return {"grade": "PASS", "detail": "Unselected revocation permits exact selected report; selected revocation denies."}
        raise AssertionError("selected revocation accepted")

    def reordered_owner():
        f = fresh()
        one = f.persist(owner={**f.owner, "account_ids": ["A-two", "A-one"]})
        two = f.persist(owner={**f.owner, "account_ids": ["A-one", "A-two"]})
        assert one == two and f.s3.put_count == 1
        return {"grade": "PASS", "detail": "Selected-set ordering preserves identity and one blob."}

    def alias_report():
        f = fresh()
        ref = f.persist()
        row = copy.deepcopy(next(iter(f.table.rows.values())))
        alias = "RPT-" + "f" * 32
        assert alias != ref["report_id"]
        row["request_revision"] = module.repo._key(alias, ref["revision"])
        row["ref"]["report_id"] = alias
        f.table.rows[(f.principal["firm_id"], row["request_revision"])] = row
        try:
            loaded = f.repository.get(f.principal, alias, ref["revision"])
        except module.repo.ReportRefused:
            return {"grade": "PASS", "detail": "Corrupted index alias refused."}
        assert loaded["report"] == module.report()
        return {"grade": "FAIL", "detail": "Index alias with rewritten ref.report_id is accepted against unchanged original bytes/request; deterministic report ID not rebound on retrieval.", "original_ref": ref, "accepted_ref": loaded["ref"]}

    def alias_artifact_control():
        f = module.ArtifactTests()
        f.setUp()
        ref = f.put()
        row = copy.deepcopy(next(iter(f.table.rows.values())))
        alias = "ART-" + "f" * 64
        assert alias != ref["artifact_id"]
        row["request_revision"] = "ARTIFACT#" + alias
        row["ref"]["artifact_id"] = alias
        f.table.rows[(f.principal["firm_id"], row["request_revision"])] = row
        try:
            f.artifacts.get(f.principal, alias)
        except module.repo.ReportRefused:
            return {"grade": "PASS", "detail": "Equivalent artifact index alias refused by recomputed identity binding."}
        raise AssertionError("artifact alias accepted")

    def publication_revocation():
        f = fresh()
        f.s3.on_get = f.allowed.clear
        try:
            f.persist()
        except module.repo.ReportDenied:
            assert not f.table.rows
            return {"grade": "PASS", "detail": "Revocation during prepublication blob verification leaves no published index row."}
        raise AssertionError("revoked publication accepted")

    for name, fn in (("exact_subset_revocation", exact_subset),
                     ("selected_order_idempotency", reordered_owner),
                     ("report_index_alias_integrity", alias_report),
                     ("artifact_alias_negative_control", alias_artifact_control),
                     ("revocation_before_publication", publication_revocation)):
        case(name, fn)
    record = {"seat": "3.0.0_SA_CVO~P", "timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "candidate": PIN, "snapshot": str(snapshot), "sha256": hashes,
              "environment": "Offline actual candidate module; synthetic AWS adapters/authorization; no network, browser, IAM or deployed evidence",
              "implementer_suite": {"ran": result.testsRun, "failures": len(result.failures), "errors": len(result.errors), "output": output.getvalue()},
              "independent_cases": observations,
              "limits": "Corruption case assumes a misbound index row; no unprivileged ability to write the index is claimed. Full P/S acceptance NOT_EVALUATED."}
    Path(__file__).with_suffix(".json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 0 if result.wasSuccessful() and all(x["grade"] == "PASS" for x in observations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
