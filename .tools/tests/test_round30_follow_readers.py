#!/usr/bin/env python3
"""test_round30_follow_readers.py -- the follow-on readers of the retired Lambda map (NFRA_CTLPLN TO-CT-cg-1, round 30).

Standard library only, ASCII only, offline (no network, no aws). Every planted case is built in a temporary folder from
.tools/tests/fixtures/function_map_base_5.json (5 entries). Readers under test (the six files of the cell):
  1 org/modules/graph/comp_closure.py          load_function_map (the module's alias of load_all)
  2 org/modules/graph/extract_lambda_routes.py _load_source_map
  3 rcg/bin/lexicon.py                         channel_lambdas
  4 rcg/bin/mark.py                            build_root_set
  5 infra/aws/ec2/estate-report-runner/estate_report_runner.py  load_attribution_maps (its lambda hop)
  6 org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py  (--selftest and the file text)

Arms:
  a-literal  (1-6) no line of the file names the retired map (the name is built by parts here, so this file is not a reader)
  a-loader   (1-6) the file loads lib/opal_lambda_map.py or the function-map folder
  fixture    the fixture holds exactly 5 entries
  b          (1-5) the reader, called on a fixture folder, returns what the same 5 entries give (expected derived from the entries)
  c          (1-5) an EMPTY folder and a MISSING folder each make the reader raise (never an empty result)
  d          p137_repin.py --selftest ends in a pass line
  e          a mutant that restores a read of the retired name in reader 2 is flagged by arm a-literal
  ascii      this file is ASCII

Usage: python .tools/tests/test_round30_follow_readers.py
Last line: FOLLOW-READERS arms=<k>/<n> ok=<True|False>
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import types
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "lib"))
sys.path.insert(0, REPO)  # org.modules.graph is a package: extract_lambda_routes uses a relative import

RETIRED = "lambda-" + "source-map"  # the retired map's name, built by parts so this test is not a reader
FIXTURE = os.path.join(HERE, "fixtures", "function_map_base_5.json")
FOLDER_REL = os.path.join("infra", "aws", "lambda", "ci", "function-map")
FILES = {
    "comp_closure": "org/modules/graph/comp_closure.py",
    "extract_lambda_routes": "org/modules/graph/extract_lambda_routes.py",
    "lexicon": "rcg/bin/lexicon.py",
    "mark": "rcg/bin/mark.py",
    "estate_report_runner": "infra/aws/ec2/estate-report-runner/estate_report_runner.py",
    "p137_repin": "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_repin.py",
}
P137 = os.path.join(REPO, FILES["p137_repin"])

ARMS = []


def arm(name, cond, detail=""):
    ARMS.append((name, bool(cond)))
    print("%s %s %s" % ("PASS" if cond else "FAIL", name, detail))


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
        return f.read()


def literal_ok(text):
    """True when no line of the text names the retired map."""
    return RETIRED not in text


def fixture_entries():
    with open(FIXTURE, encoding="ascii") as f:
        return json.load(f)["functions"]


def plant(root, entries, charters=True):
    """A temporary repository root: the function-map folder holds one <name>.json per entry; rcg/charters.yaml is empty."""
    folder = os.path.join(root, FOLDER_REL)
    os.makedirs(folder)
    for name, entry in entries.items():
        with open(os.path.join(folder, name + ".json"), "w", encoding="ascii", newline="") as f:
            f.write(json.dumps(entry, indent=2, sort_keys=False, ensure_ascii=True) + "\n")
    if charters:
        os.makedirs(os.path.join(root, "rcg"))
        with open(os.path.join(root, "rcg", "charters.yaml"), "w", encoding="ascii") as f:
            f.write("root_set: []\n")
    return root


def new_root():
    return tempfile.mkdtemp(prefix="fr30-root-")


def load_module(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def raised(fn, kinds):
    """(True, detail) when fn raises one of kinds; (False, detail) otherwise."""
    try:
        fn()
    except kinds as e:
        return True, "%s" % type(e).__name__
    except Exception as e:  # noqa: BLE001
        return False, "raised the wrong %s" % type(e).__name__
    return False, "returned without raising"


def expected_prefixes(entries):
    """What the runner's prefixes() gave for these entries: name order, then longest source_dir first (stable)."""
    items = [(e["source_dir"].rstrip("/"), n) for n, e in sorted(entries.items())]
    return sorted(items, key=lambda kv: -len(kv[0]))


def make_clone(files, branch="CLOUD"):
    """A temporary git repository whose branch holds the given {relative path: bytes}; the runner's clone stands in."""
    d = tempfile.mkdtemp(prefix="fr30-clone-")
    subprocess.run(["git", "init", "-q", d], check=True, capture_output=True)
    subprocess.run(["git", "-C", d, "symbolic-ref", "HEAD", "refs/heads/" + branch], check=True, capture_output=True)
    for rel, data in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(data)
    subprocess.run(["git", "-C", d, "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", d, "-c", "user.name=fr30", "-c", "user.email=fr30@test", "commit", "-q", "-m", "fx"],
                   check=True, capture_output=True)
    return d


def main():
    # arms a: the six readers do not name the retired map and do load the folder
    for key, rel in FILES.items():
        text = read(rel)
        arm("a-literal %s" % key, literal_ok(text), "file=%s" % rel)
        arm("a-loader %s" % key, ("opal_lambda_map" in text) or ("function-map" in text), "file=%s" % rel)

    entries = fixture_entries()
    arm("fixture 5 entries", len(entries) == 5, "count=%d" % len(entries))

    # arms b: each reader, on a fixture folder, gives what the same entries give
    comp = load_module("comp_closure_t", FILES["comp_closure"])
    sys.path.insert(0, REPO)
    from org.modules.graph import extract_lambda_routes as extract  # noqa: E402
    lex = load_module("lexicon_t", FILES["lexicon"])
    mark = load_module("mark_t", FILES["mark"])
    if "boto3" not in sys.modules:
        try:
            import boto3  # noqa: F401
        except ImportError:
            sys.modules["boto3"] = types.SimpleNamespace(client=lambda *a, **k: None, resource=lambda *a, **k: None)
    for var in ("ESTATE_REPORT_BUCKET", "ESTATE_GITHUB_SECRET_ID", "ESTATE_KIMI_SECRET_ID", "ESTATE_KIMI_URL",
                "ESTATE_KIMI_MODEL", "ESTATE_REPO_URL"):
        os.environ.setdefault(var, "fr30-test")
    runner = load_module("estate_report_runner_t", FILES["estate_report_runner"])

    root = plant(new_root(), entries)
    got = extract._load_source_map(Path(root))
    arm("b extract_lambda_routes", got == entries, "entries=%d" % len(got))
    got = comp.load_function_map(root)
    arm("b comp_closure", got == entries, "entries=%d" % len(got))

    lex.WS = Path(root)
    toks = lex.channel_lambdas()
    want = [{"token": n, "kind": "lambda", "status": "LIVE", "source": "function-map/%s.json" % n} for n in sorted(entries)]
    arm("b lexicon", toks == want, "tokens=%d" % len(toks))

    mark.WS = Path(root)
    dirs = {e["source_dir"].strip("/") for e in entries.values()}
    population = {"%s/handler.py" % sorted(dirs)[0], "%s/lib/x.py" % sorted(dirs)[-1], "org/unrelated/x.py"}
    want_roots = {p for p in population if any(p.startswith(d + "/") for d in dirs)}
    roots, why = mark.build_root_set(population)
    arm("b mark", set(roots) == want_roots and all(why[p] == "root:function-map" for p in roots),
        "roots=%d want=%d" % (len(roots), len(want_roots)))

    clone = make_clone({FOLDER_REL.replace(os.sep, "/") + "/%s.json" % n: json.dumps(e).encode("ascii")
                        for n, e in entries.items()} | {"lib/opal_lambda_map.py": open(os.path.join(REPO, "lib", "opal_lambda_map.py"), "rb").read()})
    m = runner.load_attribution_maps(clone)
    arm("b estate_report_runner", m["lambda_prefixes"] == expected_prefixes(entries),
        "prefixes=%d" % len(m["lambda_prefixes"]))

    # arms c: an empty folder and a missing folder each raise (fail loud)
    empty = plant(new_root(), {})
    os.makedirs(os.path.join(empty, FOLDER_REL), exist_ok=True)
    with open(os.path.join(empty, FOLDER_REL, "README.md"), "w", encoding="ascii") as f:
        f.write("no function file here\n")
    missing = new_root()
    os.makedirs(os.path.join(missing, "rcg"))
    with open(os.path.join(missing, "rcg", "charters.yaml"), "w", encoding="ascii") as f:
        f.write("root_set: []\n")

    def set_lex(r):
        lex.WS = Path(r)
        return lambda: lex.channel_lambdas()

    def set_mark(r):
        mark.WS = Path(r)
        return lambda: mark.build_root_set({"org/unrelated/x.py"})

    cases = [
        ("c extract_lambda_routes", lambda r: (lambda: extract._load_source_map(Path(r)))),
        ("c comp_closure", lambda r: (lambda: comp.load_function_map(r))),
        ("c lexicon", set_lex),
        ("c mark", set_mark),
    ]
    for name, mk in cases:
        ok_e, d_e = raised(mk(empty), (ValueError,))
        arm("%s empty-folder" % name, ok_e, d_e)
        ok_m, d_m = raised(mk(missing), (FileNotFoundError,))
        arm("%s missing-folder" % name, ok_m, d_m)

    bare = make_clone({"lib/opal_lambda_map.py": open(os.path.join(REPO, "lib", "opal_lambda_map.py"), "rb").read()})
    ok_r, d_r = raised(lambda: runner.load_attribution_maps(bare), (subprocess.CalledProcessError,))
    arm("c estate_report_runner missing-folder", ok_r, d_r)
    empty_clone = make_clone({FOLDER_REL.replace(os.sep, "/") + "/README.md": b"no function file here\n",
                              "lib/opal_lambda_map.py": open(os.path.join(REPO, "lib", "opal_lambda_map.py"), "rb").read()})
    ok_r2, d_r2 = raised(lambda: runner.load_attribution_maps(empty_clone), (ValueError,))
    arm("c estate_report_runner empty-folder", ok_r2, d_r2)

    # arm d: p137 keeps its selftest pass line
    rr = subprocess.run([sys.executable, P137, "--selftest"], capture_output=True, timeout=120)
    last = rr.stdout.decode("utf-8", "replace").strip().splitlines()[-1:] or [""]
    arm("d p137 selftest", rr.returncode == 0 and last[0].startswith("selftest PASS"), "rc=%d last=%s" % (rr.returncode, last[0]))

    # arm e: a mutant that restores a read of the retired name is flagged
    mutant = read(FILES["extract_lambda_routes"]) + "\n_PROBE = 'infra/aws/lambda/ci/%s.json'\n" % RETIRED
    print("MUTANT extract_lambda_routes+retired-read literal_ok=%s" % literal_ok(mutant))
    arm("e mutant flagged", literal_ok(mutant) is False)

    raw = open(os.path.abspath(__file__), "rb").read()
    arm("ascii this file", all(b < 128 for b in raw))

    for d in (empty, missing, bare, empty_clone, clone, root):
        shutil.rmtree(d, ignore_errors=True)
    k = sum(1 for _n, ok in ARMS if ok)
    n = len(ARMS)
    print("FOLLOW-READERS arms=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
