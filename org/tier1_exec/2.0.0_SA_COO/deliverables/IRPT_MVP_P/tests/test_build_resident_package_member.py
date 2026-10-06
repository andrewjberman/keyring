"""IRPT_YCDGEN R15: the resident package carries one repository file at a packaged path (`--member PACKAGED=REPO`).

The case: the Opal producer imports `etf_classifications_dynamodb`, which lives in the portal Lambda's shared folder and
in no packaged directory. `--member ycharts/research/etf_classifications_dynamodb.py=<that file>` packages it where the
research directory (on sys.path once `load_opal_producer()` runs) finds it. Every build here reads real commits of this
repository (`git show <pin>:<path>`), reads the core state from a fixture file (`--state-json`), and writes only under the
test's temp directory. No AWS call, no network.
"""
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
BUILDER = HERE.parent / "build_resident_package.py"
GATE = HERE.parent.parent / "IRPT_MVP_Y" / "live_walk" / "resident_package_gate.py"
ROOT = Path(__file__).resolve().parents[6]
IR = "infra/aws/lambda/investor-reporting"
BASE = "3f29017cfc"
OVERLAY = "d2b625e697"
M6_BUILDER_COMMIT = "2b5f4f00e1"  # the builder as cell m-6 left it (before --member)
MAP_PATH = "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json"
CLASSIFIER_REPO = "infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py"
CLASSIFIER_PACKAGED = "ycharts/research/etf_classifications_dynamodb.py"
MEMBER_ARG = "%s=%s" % (CLASSIFIER_PACKAGED, CLASSIFIER_REPO)
SECOND_PACKAGED = "ycharts/research/second_member_templates.json"
SECOND_REPO = IR + "/ycharts/generate/templates.json"
STATE = {"serial": 7, "outputs": {
    "queues": {"value": {"generation": {"url": "https://sqs.example.invalid/000000000000/fixture-generation"}}},
    "tables": {"value": {"jobs": "fixture-jobs", "requests": "fixture-requests"}}}}


def load_builder(source=None):
    spec = importlib.util.spec_from_file_location("build_resident_package_member_under_test", BUILDER)
    module = importlib.util.module_from_spec(spec)
    if source is None:
        spec.loader.exec_module(module)
    else:
        module.__file__ = str(BUILDER)
        exec(compile(source, str(BUILDER), "exec"), module.__dict__)
    return module


def git_show(pin, path):
    out = subprocess.run(["git", "show", "%s:%s" % (pin, path)], cwd=ROOT, capture_output=True, check=True)
    return out.stdout


def sums_of(package):
    rows = {}
    for line in (Path(package) / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        rows[name] = digest
    return rows


def bindings_of(package):
    return json.loads((Path(package) / "reports/resident_bindings.json").read_text(encoding="utf-8"))


def _argv(out, state, flags):
    return ["--enrolled-user-id", "1", "--out", str(out), "--state-json", str(state)] + list(flags)


def build(out, *flags, module=None):
    builder = module or load_builder()
    state = out.parent / "state.json"
    state.write_text(json.dumps(STATE), encoding="utf-8")
    return builder.main(_argv(out, state, flags))


@pytest.fixture(scope="module")
def state_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("irpt_r15")


@pytest.fixture(scope="module")
def state_file(state_dir):
    path = state_dir / "state_fixture.json"
    path.write_text(json.dumps(STATE), encoding="utf-8")
    return path


@pytest.fixture(scope="module")
def base_package(state_dir):
    out = state_dir / "base" / "pkg"
    out.parent.mkdir()
    assert build(out, "--pin", BASE) == 0
    return out


@pytest.fixture(scope="module")
def whole_tree_member_package(state_dir):
    out = state_dir / "whole" / "pkg"
    out.parent.mkdir()
    assert build(out, "--pin", OVERLAY, "--member", MEMBER_ARG) == 0
    return out


@pytest.fixture(scope="module")
def research_member_package(state_dir):
    out = state_dir / "research" / "pkg"
    out.parent.mkdir()
    assert build(out, "--pin", OVERLAY, "--research", "--opal-map", MAP_PATH, "--member", MEMBER_ARG) == 0
    return out


def test_member_flag_packages_and_records(state_dir, whole_tree_member_package, base_package, capsys):
    package = whole_tree_member_package
    expected = git_show(OVERLAY, CLASSIFIER_REPO)
    digest = hashlib.sha256(expected).hexdigest()
    # packaged at the named path, byte for byte the repository file at --pin, and in the manifest
    assert (package / CLASSIFIER_PACKAGED).read_bytes() == expected
    assert sums_of(package)[CLASSIFIER_PACKAGED] == digest
    provenance = bindings_of(package)["provenance"]
    assert provenance["members_added"] == [{"packaged": CLASSIFIER_PACKAGED, "repo_path": CLASSIFIER_REPO, "sha256": digest}]
    # it is the only difference in membership from the same pin built without the flag
    plain = state_dir / "plain_overlay" / "pkg"
    plain.parent.mkdir()
    capsys.readouterr()
    assert build(plain, "--pin", OVERLAY) == 0
    capsys.readouterr()
    assert set(sums_of(package)) - set(sums_of(plain)) == {CLASSIFIER_PACKAGED}
    assert set(sums_of(plain)) - set(sums_of(package)) == set()
    # the printed report lists the members, repeatable, and the member needs no --files-from entry under --base-pin
    listing = state_dir / "list.txt"
    listing.write_text(IR + "/ycharts/generate/entry.py\n", encoding="utf-8", newline="\n")
    state = state_dir / "state_report.json"
    state.write_text(json.dumps(STATE), encoding="utf-8")
    pkg2 = state_dir / "second" / "pkg"
    pkg2.parent.mkdir()
    assert load_builder().main(_argv(pkg2, state, ["--pin", OVERLAY, "--base-pin", BASE, "--files-from", str(listing),
                                                  "--member", MEMBER_ARG,
                                                  "--member", "%s=%s" % (SECOND_PACKAGED, SECOND_REPO)])) == 0
    report = json.loads(capsys.readouterr().out)
    assert [row["packaged"] for row in report["members_added"]] == [CLASSIFIER_PACKAGED, SECOND_PACKAGED]
    assert report["members_added"][1]["repo_path"] == SECOND_REPO
    assert report["members_added"][1]["sha256"] == hashlib.sha256(git_show(OVERLAY, SECOND_REPO)).hexdigest()
    assert (pkg2 / CLASSIFIER_PACKAGED).read_bytes() == expected
    assert (pkg2 / SECOND_PACKAGED).read_bytes() == git_show(OVERLAY, SECOND_REPO)
    assert bindings_of(pkg2)["provenance"]["members_added"] == report["members_added"]
    assert SECOND_REPO not in listing.read_text(encoding="utf-8") and CLASSIFIER_REPO not in listing.read_text(encoding="utf-8")
    print("members_added %s" % [row["packaged"] for row in report["members_added"]])


def _refused(state_file, *flags):
    with pytest.raises(SystemExit) as exc:
        load_builder().main(["--pin", OVERLAY, "--enrolled-user-id", "1", "--out", str(state_file.parent / "never"),
                             "--dry-run", "--state-json", str(state_file)] + list(flags))
    return str(exc.value)


def test_member_flag_refusals(state_file, state_dir):
    classifier = CLASSIFIER_REPO
    assert "absolute" in _refused(state_file, "--member", "/etc/x.py=" + classifier)
    assert "absolute" in _refused(state_file, "--member", "C:/x.py=" + classifier)
    assert "absolute" in _refused(state_file, "--member", "\\x.py=" + classifier)
    assert "'..'" in _refused(state_file, "--member", "../x.py=" + classifier)
    assert "'..'" in _refused(state_file, "--member", "ycharts/../x.py=" + classifier)
    # already a member of the package (a source-tree member, a census member, an earlier --member)
    assert "already a member" in _refused(state_file, "--member", "reports/resident_installed.py=" + classifier)
    assert "already a member" in _refused(state_file, "--member", "ycharts-host/ycharts_session.js=" + classifier)
    assert "already a member" in _refused(state_file, "--member", CLASSIFIER_PACKAGED + "=" + classifier,
                                          "--member", CLASSIFIER_PACKAGED + "=" + classifier)
    # a repository file that does not exist at --pin
    message = _refused(state_file, "--member", "ycharts/research/nothing.py=infra/aws/lambda/v2_portal/_shared/no_such_file.py")
    assert "does not exist at --pin" in message and "no_such_file.py" in message
    assert "not PACKAGED_PATH=REPO_PATH" in _refused(state_file, "--member", "no-equals-sign")
    # the refusal is a nonzero exit with the named message on stderr from the command line, and nothing is written
    out = state_dir / "refused_out"
    run = subprocess.run([sys.executable, str(BUILDER), "--pin", OVERLAY, "--enrolled-user-id", "1", "--out", str(out),
                          "--state-json", str(state_file), "--member", "/abs.py=" + classifier],
                         cwd=ROOT, capture_output=True, text=True, timeout=120)
    assert run.returncode != 0 and "absolute" in run.stderr
    assert not out.exists()


def _running_tar(base_package, target):
    with tarfile.open(target, "w:gz") as tar:
        data = (base_package / "SHA256SUMS").read_bytes()
        info = tarfile.TarInfo(name="./SHA256SUMS")
        info.size = len(data)
        tar.addfile(info, io.BytesIO(data))
    return target


def _run_gate(package, pin, tar, out):
    argv = [sys.executable, str(GATE), str(package), pin, str(tar), "newroot", "oldroot", "slug", str(out)]
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=300)


def test_gate_checks_added_members(base_package, whole_tree_member_package, state_dir):
    package = whole_tree_member_package
    tar = _running_tar(base_package, state_dir / "running.tar.gz")
    good = _run_gate(package, OVERLAY, tar, state_dir / "gate_ok")
    print(good.stdout)
    assert good.returncode == 0, good.stdout + good.stderr
    assert "G2 added members: 1 of 1 members_added equal" in good.stdout
    assert "DIFFERS" not in good.stdout and "GATE PASS" in good.stdout
    census = json.loads((state_dir / "gate_ok" / "newroot.census.json").read_text(encoding="utf-8"))
    assert CLASSIFIER_PACKAGED in census["added"] and census["gates"]["G2"] is True
    # an added member whose bytes differ from the repository file at the pin (manifest line kept honest, so G1 holds)
    bad_dir = state_dir / "tampered" / "pkg"
    bad_dir.parent.mkdir()
    shutil.copytree(package, bad_dir)
    tampered = git_show(OVERLAY, CLASSIFIER_REPO) + b"\n# not the repository file\n"
    (bad_dir / CLASSIFIER_PACKAGED).write_bytes(tampered)
    lines = []
    for line in (bad_dir / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if name == CLASSIFIER_PACKAGED:
            digest = hashlib.sha256(tampered).hexdigest()
        lines.append("%s  %s" % (digest, name))
    (bad_dir / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    bad = _run_gate(bad_dir, OVERLAY, tar, state_dir / "gate_bad")
    print(bad.stdout)
    assert bad.returncode == 1
    assert "G1 manifest" in bad.stdout and "DIFFERS: " + CLASSIFIER_PACKAGED in bad.stdout
    assert "1 of 1 members_added" not in bad.stdout and "G2 added members: 0 of 1" in bad.stdout
    assert "GATE FAIL" in bad.stdout
    # without the mapping the same member is not found at the pin under its packaged name: G2 would fail (the mapping is the fix)
    stripped = state_dir / "stripped" / "pkg"
    stripped.parent.mkdir()
    shutil.copytree(package, stripped)
    doc = bindings_of(stripped)
    doc["provenance"].pop("members_added")
    (stripped / "reports/resident_bindings.json").write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = []
    for line in (stripped / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if name == "reports/resident_bindings.json":
            digest = hashlib.sha256((stripped / name).read_bytes()).hexdigest()
        lines.append("%s  %s" % (digest, name))
    (stripped / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    refused = _run_gate(stripped, OVERLAY, tar, state_dir / "gate_stripped")
    assert refused.returncode == 1 and "DIFFERS: " + CLASSIFIER_PACKAGED in refused.stdout, refused.stdout


_SMOKE = r'''
import json, os, sys
from pathlib import Path
root = sys.argv[1]
sys.path.insert(0, root)
for rel in ("intake", "ops", "reports", "_keys", "_authz", "_gate", "ycharts/session", "ycharts/extract"):
    p = Path(root) / rel
    if p.is_dir():
        sys.path.insert(0, str(p))
sys.path.insert(0, str(Path(root) / "ycharts/generate"))
import resident_installed as ri
import resident_worker
resident_worker.load_opal_producer()
import layout_overview
result = {"v2_portal_on_path": [p for p in sys.path if "v2_portal" in p.replace("\\", "/")],
          "region": os.environ.get("AWS_DEFAULT_REGION")}
try:
    client = layout_overview._default_classifier()
    mod = sys.modules[type(client).__module__]
    result.update({"type": type(client).__name__, "table": client.table_name, "file": getattr(mod, "__file__", None)})
except layout_overview.LayoutRefused as exc:
    result.update({"refused": str(exc)})
print(json.dumps(result))
'''


def _smoke(package, cwd):
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP")}
    env["AWS_DEFAULT_REGION"] = "us-east-1"
    run = subprocess.run([sys.executable, "-I", "-c", _SMOKE, str(package)], cwd=str(cwd), env=env,
                         capture_output=True, text=True, timeout=120)
    assert run.returncode == 0, run.stderr[-1500:]
    return json.loads(run.stdout.strip().splitlines()[-1])


def test_packaged_classifier_import_smoke(research_member_package, state_dir):
    package = research_member_package
    result = _smoke(package, package.parent)
    print(result)
    assert result["region"] == "us-east-1" and result["v2_portal_on_path"] == []
    assert result.get("type") == "ETFClassifier", result
    assert Path(result["file"]).resolve() == (package / CLASSIFIER_PACKAGED).resolve()
    assert not any(part == "v2_portal" for p in package.rglob("*") if p.is_dir() for part in p.parts[len(package.parts):])
    # negative arm: the same package without the member refuses by the module's own named reason
    without = state_dir / "smoke_without" / "pkg"
    without.parent.mkdir()
    shutil.copytree(package, without)
    (without / CLASSIFIER_PACKAGED).unlink()
    refused = _smoke(without, without.parent)
    assert refused["v2_portal_on_path"] == [] and "classification client" in refused.get("refused", ""), refused


def test_default_build_has_no_members_added(base_package, state_dir):
    """A build with none of the new flags equals the m-6 builder's build, member for member, and carries no members_added."""
    bindings = bindings_of(base_package)
    assert "members_added" not in bindings["provenance"] and "members_added" not in bindings
    assert set(bindings["provenance"]) == {"package_pin", "member_overrides", "census_pin", "core_state_serial", "generated_at",
                                          "generated_by"}
    old_source = subprocess.run(["git", "show", "%s:org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py"
                                 % M6_BUILDER_COMMIT], cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8")
    assert "--member" not in old_source
    old = state_dir / "m6" / "pkg"
    old.parent.mkdir()
    assert build(old, "--pin", BASE, module=load_builder(old_source)) == 0
    old_files = sorted(p.relative_to(old).as_posix() for p in old.rglob("*") if p.is_file())
    new_files = sorted(p.relative_to(base_package).as_posix() for p in base_package.rglob("*") if p.is_file())
    assert old_files == new_files and len(new_files) > 200
    for name in new_files:
        if name in ("SHA256SUMS", "reports/resident_bindings.json"):
            continue
        assert (old / name).read_bytes() == (base_package / name).read_bytes(), name
    old_doc, new_doc = bindings_of(old), bindings
    for doc in (old_doc, new_doc):
        doc["provenance"].pop("generated_at")
    assert old_doc == new_doc
    assert sums_of(old).keys() == sums_of(base_package).keys()
    assert not [m for m in new_files if m == CLASSIFIER_PACKAGED]
