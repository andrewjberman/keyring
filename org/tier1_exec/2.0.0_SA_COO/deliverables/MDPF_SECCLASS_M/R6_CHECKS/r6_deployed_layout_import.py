"""Round 6 (~M) check SC6-e13-AC2: the BD thread modules import from an EXACT EXTRACT of what the deploy tool
ships, laid out the way the runner lays out code/gold/, with NO repo path on sys.path (1.0.0_SA_CTO DECISION 103371).

How it is built (nothing hand-listed):
  1. The deploy tool (.tools/safe_deploy_core.py) is asked for the exact upload plan of the five gold thread files:
     upload_plan() returns (repo_path, bucket, s3_key) for each file's own target PLUS the declared shipped artifacts.
  2. The gold layer's flatten rule is read from the runner's own script (gold_dispatch.sh sync_scripts:
     `aws s3 sync s3://$BD_S3_BUCKET/code/gold/ $SCRIPTS/`, SCRIPTS=/tmp/gold_layer_scripts) and must equal the
     tool's own layer prefix; the destination of every file is its key minus that prefix.
  3. The files the act does NOT upload but the modules import (the rest of code/gold/, already on S3) come from the
     same tool mapping over the repo's gold tree; each is printed as a BASE-DEP only if a module actually loaded it.
  4. Every import runs in a FRESH interpreter (`python -I`, cwd = the temp root, sys.path = that root + the
     interpreter's own stdlib/site-packages) and the child REFUSES to run if any sys.path entry is inside the repo.
  5. The silver builder is checked against the layout MEASURED from its runner's bootstrap document
     (infra/aws/ssm/opal-bd-asset-dim-download.json: the `aws s3 cp ... "$RUNROOT/..."` lines), parsed, not retyped.
Prints `OK <module> client=<resolved path>` per module and, when all five import from the extract,
`DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=<n>`; the silver layout gets its own lines. Exit 0 only when the five
gold modules import AND each resolved its client from inside the extract. Nothing is uploaded or run anywhere.
Run from any directory:  python <this file>
"""
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()


def _repo_root() -> Path:
    for anc in HERE.parents:
        if (anc / ".tools" / "safe_deploy_core.py").is_file():
            return anc
    raise SystemExit("ERROR: repo root (a directory holding .tools/safe_deploy_core.py) not found above %s" % HERE)


REPO = _repo_root()
GOLD_HOME = "data/black_diamond/scripts/gold"
# The five thread modules, as (module name, repo path). lib.etf_classifier is imported as a package member; the
# other four carry a dot in their file name and are loaded by location, exactly as `python3 <file>` runs them.
THREAD = [
    ("C_06.client_mix_timeseries", GOLD_HOME + "/C_06.client_mix_timeseries.py"),
    ("D_03.composition_artifacts", GOLD_HOME + "/D_03.composition_artifacts.py"),
    ("D_04.client_portal_summary", GOLD_HOME + "/D_04.client_portal_summary.py"),
    ("E_18.detect_new_securities", GOLD_HOME + "/E_18.detect_new_securities.py"),
    ("lib.etf_classifier", GOLD_HOME + "/lib/etf_classifier.py"),
]
SILVER_BUILDER = "data/black_diamond/scripts/silver/build_bd_assets_dim.py"
SSM_DOC = "infra/aws/ssm/opal-bd-asset-dim-download.json"
GOLD_DISPATCH = GOLD_HOME + "/gold_dispatch.sh"

_CHILD = r'''
import importlib.util, json, sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
repo = Path(sys.argv[2]).resolve()
kind, name, rel = sys.argv[3], sys.argv[4], sys.argv[5]
extra_path = sys.argv[6:]
for p in extra_path[::-1]:
    sys.path.insert(0, p)
sys.path.insert(0, str(root))
bad = []
for p in sys.path:
    try:
        rp = Path(p or ".").resolve()
    except OSError:
        continue
    if rp == repo or repo in rp.parents:
        bad.append(p)
out = {"module": name, "sys_path": len(sys.path), "repo_on_path": bad, "ok": False}
try:
    if bad:
        raise RuntimeError("repo path on sys.path: %r" % bad)
    if kind == "package":
        importlib.import_module(name)
    else:
        spec = importlib.util.spec_from_file_location(name, str(root / rel))
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    out["imported"] = True
    # resolve the client the way each module's own code does
    try:
        if name.startswith("E_18"):
            if mod._require_shared() is None:
                raise RuntimeError("E_18 could not resolve its shared dir")
            import etf_classification_scheduled as sched
            out["scheduled"] = sched.__file__
            client_file = sys.modules["etf_classifications_dynamodb"].__file__
        else:
            cls = sys.modules["lib.etf_classifier"]._load_shared_classifier_cls()
            client_file = sys.modules[cls.__module__].__file__
        out["client"] = str(Path(client_file).resolve())
        out["ok"] = True
    except BaseException as exc:  # noqa: BLE001
        out["client_error"] = "%s: %s" % (type(exc).__name__, str(exc)[:300])
except BaseException as exc:  # noqa: BLE001 -- the check reports every failure verbatim
    out["error"] = "%s: %s" % (type(exc).__name__, str(exc)[:400])
out["loaded_from_root"] = sorted(
    str(Path(m.__file__).resolve().relative_to(root)).replace("\\", "/")
    for m in list(sys.modules.values())
    if getattr(m, "__file__", None) and root in Path(m.__file__).resolve().parents)
print("CHILD-JSON " + json.dumps(out))
'''


def _load_core():
    spec = importlib.util.spec_from_file_location("safe_deploy_core", str(REPO / ".tools" / "safe_deploy_core.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["safe_deploy_core"] = mod
    spec.loader.exec_module(mod)
    return mod


def _runner_flatten_prefix(core) -> tuple[str, str]:
    """(prefix, evidence): the S3 prefix the gold runner syncs, read from its own script and required to equal
    the deploy tool's gold-layer prefix."""
    text = (REPO / GOLD_DISPATCH).read_text(encoding="utf-8", errors="replace")
    m = re.search(r'aws s3 sync "s3://\$BD_S3_BUCKET/([^"]+)" "\$SCRIPTS/"', text)
    d = re.search(r'^SCRIPTS="([^"]+)"', text, re.MULTILINE)
    if not m or not d:
        raise SystemExit("ERROR: could not read the runner's sync line / SCRIPTS from %s" % GOLD_DISPATCH)
    tool_prefix = core.tree_layers("black_diamond")["gold"][1]
    if m.group(1) != tool_prefix:
        raise SystemExit("ERROR: runner syncs %r but the deploy tool's gold prefix is %r" % (m.group(1), tool_prefix))
    return tool_prefix, "%s: sync s3://<bd bucket>/%s -> %s/ (flat, recursive, no infra/ tree)" % (
        GOLD_DISPATCH, m.group(1), d.group(1))


def _copy(src_rel: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REPO / src_rel, dest)


def _child(root: Path, kind: str, name: str, rel: str, extra: list[str] | None = None) -> dict:
    r = subprocess.run([sys.executable, "-I", "-c", _CHILD, str(root), str(REPO), kind, name, rel] + (extra or []),
                       cwd=str(root), capture_output=True, text=True, timeout=110)
    for line in r.stdout.splitlines():
        if line.startswith("CHILD-JSON "):
            return json.loads(line[len("CHILD-JSON "):])
    return {"module": name, "ok": False, "error": "no result from child rc=%s stderr=%s" % (r.returncode, r.stderr[-300:])}


def _inside(path: str, root: Path) -> bool:
    return root.resolve() in Path(path).resolve().parents


def gold_section(core, work: Path) -> bool:
    prefix, evidence = _runner_flatten_prefix(core)
    print("GOLD-LAYOUT measured from " + evidence)
    thread_paths = [p for _n, p in THREAD]
    plan = core.upload_plan(thread_paths)
    print("UPLOAD-PLAN files=%d (safe_deploy_core.upload_plan of the five gold thread files)" % len(plan))
    for repo_path, bucket, key in plan:
        print("  %s -> s3://%s/%s" % (repo_path, bucket, key))
    root = work / "gold_layer_scripts"
    in_plan = set()
    for repo_path, _bucket, key in plan:
        if not key.startswith(prefix):
            raise SystemExit("ERROR: plan key %r is outside the synced prefix %r" % (key, prefix))
        _copy(repo_path, root / key[len(prefix):])
        in_plan.add(key[len(prefix):])
    # BASE: the rest of code/gold/, mapped by the same tool; copied only where the plan did not already place a file
    base = []
    for p in sorted((REPO / GOLD_HOME).rglob("*.py")):
        rel = p.relative_to(REPO).as_posix()
        if "/tests/" in rel:
            continue
        tgt = core.file_to_s3_target(rel)
        if tgt is None or not tgt[1].startswith(prefix):
            continue
        flat = tgt[1][len(prefix):]
        if flat in in_plan:
            continue
        _copy(rel, root / flat)
        base.append(flat)
    print("EXTRACT root=<temp>/gold_layer_scripts uploaded_by_act=%d base_already_on_s3=%d" % (len(in_plan), len(base)))
    results = []
    base_used = set()
    for name, rel in THREAD:
        kind = "package" if name.startswith("lib.") else "file"
        flat = rel[len(GOLD_HOME) + 1:]
        res = _child(root, kind, name, flat)
        ok = res.get("ok") and _inside(res["client"], root)
        if res.get("ok") and not ok:
            res["ok"], res["error"] = False, "client resolved OUTSIDE the extract: %s" % res["client"]
        results.append(res)
        if res["ok"]:
            print("OK %s client=%s (sys.path entries=%d, inside repo=%d)" % (
                name, res["client"], res["sys_path"], len(res["repo_on_path"])))
            for f in res.get("loaded_from_root", []):
                if f not in in_plan and f in base:
                    base_used.add(f)
            if name.startswith("E_18"):
                print("   E_18 scheduled module=%s" % res["scheduled"])
        else:
            print("FAIL %s %s (sys.path entries=%s repo_on_path=%s)" % (
                name, res.get("error") or res.get("client_error"), res.get("sys_path"), res.get("repo_on_path")))
    print("BASE-DEPS loaded from the rest of code/gold/ (on S3 already, not uploaded by this act): %s"
          % (", ".join(sorted(base_used)) or "none"))
    n_ok = sum(1 for r in results if r["ok"])
    if n_ok == len(THREAD):
        print("DEPLOYED-LAYOUT-IMPORT modules=%d of %d files=%d" % (n_ok, len(THREAD), len(plan)))
        return True
    print("DEPLOYED-LAYOUT-IMPORT-FAILED modules=%d of %d files=%d" % (n_ok, len(THREAD), len(plan)))
    return False


def _silver_stage(core, work: Path, label: str, add_shipped: bool) -> tuple[Path, list[str], list[str]]:
    """Stage the silver runner's tree from the SSM document's own `aws s3 cp` lines; map each key back to its
    repo source through the deploy tool (code/lib/ keys are the separately-deployed fabric lib, source lib/)."""
    doc = json.loads((REPO / SSM_DOC).read_text(encoding="utf-8"))
    lines = doc["mainSteps"][0]["inputs"]["runCommand"]
    key_to_repo = {}
    for p in sorted((REPO / "data/black_diamond/scripts").rglob("*.py")):
        rel = p.relative_to(REPO).as_posix()
        tgt = core.file_to_s3_target(rel)
        if tgt is not None:
            key_to_repo[tgt[1]] = rel
    root = work / label
    staged, skipped = [], []
    for ln in lines:
        m = re.search(r'aws s3 cp s3://[\w.-]+/(\S+)\s+"\$RUNROOT/([^"]*)"', ln)
        if not m:
            continue
        key, dest = m.group(1), m.group(2)
        src = key_to_repo.get(key)
        if src is None and key.startswith("code/lib/"):
            src = "lib/" + key.rsplit("/", 1)[-1]
        if src is None or not (REPO / src).is_file():
            skipped.append(key)
            continue
        target = root / dest / key.rsplit("/", 1)[-1] if dest.endswith("/") else root / dest
        _copy(src, target)
        staged.append("%s -> %s" % (key, (dest + key.rsplit('/', 1)[-1]) if dest.endswith("/") else dest))
    if add_shipped:
        gold_lib = root / "data/black_diamond/scripts/gold/lib"
        for repo_path, _b, key in core.shipped_artifacts_for([GOLD_HOME + "/lib/etf_classifier.py"]):
            _copy(repo_path, gold_lib / "_shared" / key.rsplit("/", 1)[-1])
            staged.append("%s -> data/black_diamond/scripts/gold/lib/_shared/ (ADDED; not in the document today)" % key)
    return root, staged, skipped


def silver_section(core, work: Path) -> None:
    print("SILVER-LAYOUT measured from %s: a repo-shaped RUNROOT holding silver/build_bd_assets_dim.py, "
          "gold/lib/{etf_classifier,__init__}.py (two cp lines) and lib/{silver_ids,trading_calendar}.py; the script "
          "runs as `cd $RUNROOT && python3 data/black_diamond/scripts/silver/build_bd_assets_dim.py`; "
          "gold/ is reached through the builder's own ../gold sys.path insert" % SSM_DOC)
    for label, add in (("silver_as_staged_today", False), ("silver_with_shipped_artifacts", True)):
        root, staged, skipped = _silver_stage(core, work, label, add)
        res = _child(root, "file", "build_bd_assets_dim", SILVER_BUILDER,
                     [str(root / "data/black_diamond/scripts/silver")])
        tag = "SILVER-LAYOUT-AS-STAGED-TODAY" if not add else "SILVER-LAYOUT-WITH-SHIPPED-ARTIFACTS"
        print("%s files_staged=%d (document keys with no repo source, not staged: %d)" % (tag, len(staged), len(skipped)))
        for s in staged:
            print("  " + s)
        if res.get("ok") and _inside(res["client"], root):
            print("%s OK build_bd_assets_dim import=OK client=%s" % (tag, res["client"]))
        elif res.get("imported"):
            print("%s REFUSED build_bd_assets_dim import=OK client=UNRESOLVED %s" % (tag, res.get("client_error")))
        else:
            print("%s NOT-IMPORTED build_bd_assets_dim %s" % (tag, res.get("error")))


def main() -> int:
    core = _load_core()
    work = Path(tempfile.mkdtemp(prefix="r6_layout_"))
    try:
        gold_ok = gold_section(core, work)
        silver_section(core, work)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return 0 if gold_ok else 1


if __name__ == "__main__":
    sys.exit(main())
