"""IRPT_YCDGEN R13: the resident package carries the producer, the map and a named file list; the gate understands the list.

Every build here reads real commits of this repository (`git show <pin>:<path>`), reads the core state from a fixture
file (`--state-json`), and writes only under the test's temp directory. No AWS call, no network.
Pins: BASE is the running package's pin, OVERLAY is the merge that holds the round-6 files.
"""
import hashlib
import importlib.util
import io
import json
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
OLD_BUILDER_COMMIT = "4d2331db75"
CENSUS_FILE = ROOT / "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/act/PACKAGE_CENSUS_3d705e700f-st22.json"
MAP_PATH = "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json"
STATE = {"serial": 7, "outputs": {
    "queues": {"value": {"generation": {"url": "https://sqs.example.invalid/000000000000/fixture-generation"}}},
    "tables": {"value": {"jobs": "fixture-jobs", "requests": "fixture-requests"}}}}


def load_builder(source=None):
    spec = importlib.util.spec_from_file_location("build_resident_package_under_test", BUILDER)
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


def git_ls(pin, prefix):
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", pin, "--", prefix], cwd=ROOT, capture_output=True, check=True)
    return [line for line in out.stdout.decode().splitlines() if line]


def sums_of(package):
    rows = {}
    for line in (Path(package) / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        rows[name] = digest
    return rows


def bindings_of(package):
    return json.loads((Path(package) / "reports/resident_bindings.json").read_text(encoding="utf-8"))


def build(out, *flags, module=None):
    builder = module or load_builder()
    state = out.parent / "state.json"
    state.write_text(json.dumps(STATE), encoding="utf-8")
    argv = ["--enrolled-user-id", "1", "--out", str(out), "--state-json", str(state)] + list(flags)
    return builder.main(argv)


def round6_list():
    census = json.loads(CENSUS_FILE.read_text(encoding="utf-8"))
    names = list(census["added"]) + [n for n in census["changed"] if n != "reports/resident_bindings.json"]
    return [n if n.startswith("infra/") else IR + "/" + n for n in names]


@pytest.fixture(scope="module")
def state_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("irpt_r13")


@pytest.fixture(scope="module")
def base_package(state_dir):
    out = state_dir / "base" / "pkg"
    out.parent.mkdir()
    assert build(out, "--pin", BASE) == 0
    return out


@pytest.fixture(scope="module")
def listed_package(state_dir):
    out = state_dir / "listed" / "pkg"
    out.parent.mkdir()
    listing = state_dir / "listed" / "list.txt"
    listing.write_text("\n".join(round6_list()) + "\n", encoding="utf-8", newline="\n")
    assert build(out, "--pin", OVERLAY, "--base-pin", BASE, "--files-from", str(listing)) == 0
    return out, listing


@pytest.fixture(scope="module")
def research_package(state_dir):
    out = state_dir / "research" / "pkg"
    out.parent.mkdir()
    assert build(out, "--pin", OVERLAY, "--research", "--opal-map", MAP_PATH) == 0
    return out


def test_research_dir_packaged(research_package):
    members = sums_of(research_package)
    expected = {p[len(IR) + 1:] for p in git_ls(OVERLAY, IR + "/ycharts/research")
                if p.endswith((".py", ".json", ".sh", ".md", ".cjs"))
                and "/tests/" not in p and "/fixtures/" not in p and "/__pycache__/" not in p}
    got = {m for m in members if m.startswith("ycharts/research/") and m != "ycharts/research/overview_map.json"}
    assert expected and got == expected, (sorted(expected - got), sorted(got - expected))
    for name in ("opal_producer.py", "layout_overview.py", "runner.py", "keeper.py", "held_data.py", "render_pdf.cjs"):
        assert "ycharts/research/" + name in got
    assert not [m for m in members if "/tests/" in m and m.startswith("ycharts/research/")]
    assert not [m for m in members if "/fixtures/" in m and m.startswith("ycharts/research/")]
    for name in sorted(got)[:3]:
        assert (research_package / name).read_bytes() == git_show(OVERLAY, IR + "/" + name)
    print("research members %d of %d tracked non-test files at %s" % (len(got), len(expected), OVERLAY))


def _loader_in_clean_interpreter(package, tag):
    code = r'''
import json, sys
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
bindings = json.loads((Path(root) / "reports/resident_bindings.json").read_text(encoding="utf-8"))
loaded = ri._opal_map_loader(bindings, Path(root) / "reports")()
producer = resident_worker.load_opal_producer()
mods = {name: getattr(sys.modules.get(name), "__file__", None) for name in
        ("opal_producer", "layout_overview", "runner", "keeper", "held_data")}
print(json.dumps({"map_type": type(loaded).__name__, "map_keys": len(loaded), "producer": producer.__name__,
                  "modules": mods}))
'''
    out = subprocess.run([sys.executable, "-I", "-c", code, str(package)], cwd=str(package.parent),
                         capture_output=True, text=True, timeout=120)
    assert out.returncode == 0, out.stderr[-1500:]
    return json.loads(out.stdout.strip().splitlines()[-1])


def test_opal_map_binding_pinned(research_package, base_package):
    bindings = bindings_of(research_package)
    packaged = research_package / "ycharts/research/overview_map.json"
    digest = hashlib.sha256(packaged.read_bytes()).hexdigest()
    assert packaged.read_bytes() == git_show(OVERLAY, MAP_PATH)
    assert bindings["opal_map"] == {"path": "../ycharts/research/overview_map.json", "sha256": digest}
    assert sums_of(research_package)["ycharts/research/overview_map.json"] == digest
    assert "opal_map" not in bindings_of(base_package)
    # the installer's loader reads the packaged map and returns it as a dict
    result = _loader_in_clean_interpreter(research_package, "opal_map")
    assert result["map_type"] == "dict" and result["map_keys"] > 0
    # a changed map is refused by the same pin
    tampered = research_package.parent / "tampered"
    tampered.mkdir()
    code = r'''
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
for rel in ("intake", "ops", "reports", "_keys", "_authz", "_gate", "ycharts/session", "ycharts/extract", "ycharts/generate"):
    sys.path.insert(0, str(root / rel))
import resident_installed as ri
bindings = json.loads((root / "reports/resident_bindings.json").read_text(encoding="utf-8"))
bindings["opal_map"]["sha256"] = "0" * 64
try:
    ri._opal_map_loader(bindings, root / "reports")()
except ri.ResidentInstallRefused as exc:
    print(str(exc))
'''
    out = subprocess.run([sys.executable, "-I", "-c", code, str(research_package)], cwd=str(tampered),
                         capture_output=True, text=True, timeout=120)
    assert out.stdout.strip() == "PINNED_FILE_DIFFERS:opal_map", (out.stdout, out.stderr[-500:])


def test_named_list_package_differs_only_by_the_list(base_package, listed_package, capsys):
    package, listing = listed_package
    names = round6_list()
    base, new = sums_of(base_package), sums_of(package)
    added = sorted(set(new) - set(base))
    removed = sorted(set(base) - set(new))
    changed = sorted(m for m in new if m in base and new[m] != base[m])
    print("added %d, removed %d, changed %d of %d" % (len(added), len(removed), len(changed), len(new)))
    assert (len(added), len(removed), len(changed)) == (5, 0, 10)
    listed_members = {n[len(IR) + 1:] if n.startswith(IR + "/") else n for n in names}
    assert set(added) | (set(changed) - {"reports/resident_bindings.json"}) == listed_members
    # unlisted members are the base package's bytes; listed members are the overlay's blobs
    for member in set(new) - listed_members - {"reports/resident_bindings.json"}:
        assert new[member] == base[member]
    for name in names:
        member = name[len(IR) + 1:] if name.startswith(IR + "/") else name
        assert new[member] == hashlib.sha256(git_show(OVERLAY, name)).hexdigest()
    # the round-6 build's own census recorded these member digests (pinned members that the build changed)
    census = json.loads(CENSUS_FILE.read_text(encoding="utf-8"))
    for member, digest in census["pinned_members"].items():
        assert new[member] == digest, member
    bindings = bindings_of(package)["provenance"]
    assert bindings["base_pin"] == subprocess.run(["git", "rev-parse", BASE], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    assert bindings["files_from_sha256"] == hashlib.sha256(listing.read_bytes()).hexdigest()
    assert bindings["files_from_count"] == len(names) == 14
    assert "opal_map" not in bindings_of(package)


def test_named_list_report_prints_the_list_and_count(state_dir, capsys):
    listing = state_dir / "report_list.txt"
    listing.write_text("\n".join(round6_list()[:2]) + "\n", encoding="utf-8", newline="\n")
    state = state_dir / "state.json"
    state.write_text(json.dumps(STATE), encoding="utf-8")
    capsys.readouterr()
    assert load_builder().main(["--pin", OVERLAY, "--enrolled-user-id", "1", "--out", str(state_dir / "x"), "--dry-run",
                                "--state-json", str(state), "--base-pin", BASE, "--files-from", str(listing)]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["files_from"] == round6_list()[:2] and report["files_from_count"] == 2
    # a listed file that does not exist at --pin is refused
    listing.write_text("infra/aws/lambda/investor-reporting/ops/not_a_file.py\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        load_builder().main(["--pin", OVERLAY, "--enrolled-user-id", "1", "--out", str(state_dir / "x"), "--dry-run",
                             "--state-json", str(state), "--base-pin", BASE, "--files-from", str(listing)])


def _running_tar(base_package, target):
    with tarfile.open(target, "w:gz") as tar:
        data = (base_package / "SHA256SUMS").read_bytes()
        info = tarfile.TarInfo(name="./SHA256SUMS")
        info.size = len(data)
        tar.addfile(info, io.BytesIO(data))
    return target


def _run_gate(package, pin, tar, out, listing=None, base=None):
    argv = [sys.executable, str(GATE), str(package), pin, str(tar), "newroot", "oldroot", "slug", str(out)]
    if listing:
        argv += ["--base-pin", base, "--files-from", str(listing)]
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=300)


def test_gate_accepts_listed_package_and_refuses_an_extra_member(base_package, listed_package, state_dir):
    package, listing = listed_package
    tar = _running_tar(base_package, state_dir / "running.tar.gz")
    good = _run_gate(package, OVERLAY, tar, state_dir / "gate_ok", listing, BASE)
    print(good.stdout)
    assert good.returncode == 0, good.stdout + good.stderr
    assert "G2 named list" in good.stdout and "0 member(s) differ" in good.stdout
    assert "GATE PASS" in good.stdout
    # an unlisted member that differs from the base pin's blob (here: the overlay's version of one more file)
    bad_dir = state_dir / "extra" / "pkg"
    bad_dir.parent.mkdir()
    extra = IR + "/ycharts/generate/entry.py"
    base_blob, over_blob = git_show(BASE, extra), git_show(OVERLAY, extra)
    if base_blob == over_blob:
        over_blob = base_blob + b"\n# extra\n"
    import shutil
    shutil.copytree(package, bad_dir)
    (bad_dir / "ycharts/generate/entry.py").write_bytes(over_blob)
    lines = []
    for line in (bad_dir / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if name == "ycharts/generate/entry.py":
            digest = hashlib.sha256(over_blob).hexdigest()
        lines.append("%s  %s" % (digest, name))
    (bad_dir / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    bad = _run_gate(bad_dir, OVERLAY, tar, state_dir / "gate_bad", listing, BASE)
    print(bad.stdout)
    assert bad.returncode == 1
    assert "DIFFERS: ycharts/generate/entry.py" in bad.stdout and "1 member(s) differ" in bad.stdout
    assert "GATE FAIL" in bad.stdout


def test_packaged_import_smoke(research_package):
    result = _loader_in_clean_interpreter(research_package, "smoke")
    assert result["producer"] == "opal_producer"
    for name in ("opal_producer", "layout_overview", "runner", "keeper", "held_data"):
        located = result["modules"][name]
        assert located and Path(located).resolve().parent == (research_package / "ycharts/research").resolve(), (name, located)
    assert result["map_type"] == "dict"


def test_default_build_unchanged(base_package, state_dir):
    """A build with none of the new flags equals the build of the commit before this change, member for member."""
    old_source = subprocess.run(["git", "show", "%s:org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py"
                                 % OLD_BUILDER_COMMIT], cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8")
    old = load_builder(old_source)
    old.core_outputs = lambda: (STATE["serial"], {k: v["value"] for k, v in STATE["outputs"].items()})
    out = state_dir / "old" / "pkg"
    out.parent.mkdir()
    assert old.main(["--pin", BASE, "--enrolled-user-id", "1", "--out", str(out)]) == 0
    old_files = sorted(p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file())
    new_files = sorted(p.relative_to(base_package).as_posix() for p in base_package.rglob("*") if p.is_file())
    assert old_files == new_files and len(new_files) > 200
    for name in new_files:
        if name in ("SHA256SUMS", "reports/resident_bindings.json"):
            continue
        assert (out / name).read_bytes() == (base_package / name).read_bytes(), name
    old_bindings, new_bindings = bindings_of(out), bindings_of(base_package)
    for doc in (old_bindings, new_bindings):
        doc["provenance"].pop("generated_at")
    assert old_bindings == new_bindings
    assert set(new_bindings) == set(old_bindings) and "opal_map" not in new_bindings
    assert set(new_bindings["provenance"]) == {"package_pin", "member_overrides", "census_pin", "core_state_serial", "generated_by"}
    assert not [m for m in new_files if m.startswith("ycharts/research/")]
