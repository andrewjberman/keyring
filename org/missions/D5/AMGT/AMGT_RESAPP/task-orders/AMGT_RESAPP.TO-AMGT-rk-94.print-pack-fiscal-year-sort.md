# AMGT_RESAPP task order -- `AMGT-rk-94` -- the PRINT PACK sorts model-block fiscal years on a NORMALISED key, so the print route stops serving a 500 for the three validation names whose blocks carry mixed str/int fiscal years; the adapter redeploys under a never-widen pair, gated by the pre-deploy closure check

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-94</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~94</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- arms no cron, alarm, monitor or cadence; the one live act is a TARGETED
  redeploy of module.scoped_amgt_api.aws_lambda_function.this (no other resource); the deploy-ledger entry is opened
  before the first live write and closed on the post-act read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, grant, layer, environment variable, timeout or memory moves;
  the code change is pure rendering (a sort key) inside a module the function already packages. Coverage: the scoped
  role's inline policy is READ pre and post (4 statements, compact-separator sha 42d6bd14a35e1718 at the cut) and must
  be equal.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~94`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your
first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~94;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-94` (row `AMGT_RESAPP-Z-S215`, step 1)

**The ruling, verbatim (1.0.0_SA_CTO~Z msg 24146, 2026-09-22T05:52:53Z):**
> - Z-S215 (ARMED, mine), PRE-RULED for round 23, confirmed in my round-22 analysis after the CVO's slug (LD-0521):
>   (1) FIRST CELL: render_pack sorts on a normalised key, the adapter redeploys under a pair, and the binding AC7 closure check applies. Add a regression arm with the mixed {'str','int'} keys, and an invoke of /security/{key}/print for all 5 names expecting 200.
>   (2) CHAIN G: the producer writes forecast fiscal years as str, and model_block's re-homing re-derives them.
>   This matters more than its size suggests. The print pack is the managers' deliverable, and it 500s on all three validation names, so Andrew's PROD look can hit it.

This cell is step (1) ONLY. Step (2) -- changing the PRODUCER or any stored model block -- is NOT this cell (chain G).

**The defect, measured at the cut (SITEZ `218ff3c994`, read-only):**
- `lib/research/print/render_pack.py` (337 lines) groups non-header figures by `f.get("fiscal_year", "?")` into
  `by_fy` (`:240-242`) and renders `for fy in sorted(by_fy.keys())` (`:264`), heading `"Fiscal year {0}".format(fy)`
  (`:265`). A block whose keys mix `str` and `int` raises `TypeError: '<' not supported between instances of 'int' and
  'str'` there; `scoped_amgt._print_pack` (function-scope `from lib.research.print.render_pack import build_pack`,
  `scoped_amgt.py:3953`, called at `:3971`) lets it escape as the handler's generic 500.
- **Sort/compare census of render_pack.py, by AST (denominator: every `sorted`/`.sort`/`min`/`max` call and every
  ordering comparison in the file):** 1 sort call (`:264`, over the fiscal-year keys) + 1 ordering compare (`:182`,
  `self._y - n_lines * LINE_HEIGHT < BOTTOM_Y`, page layout, NOT fiscal years). So exactly ONE site sorts fiscal years.
  The text output (`txt_path`, `:302`) is built from the same page lines, so it has no second sort.
- **Live key population, every served name's LATEST model block** (`derived/model_block/<key>/<stamp>/model_block.json`,
  37 security keys, 122 objects): 34 keys carry ONLY `str` fiscal years; 3 carry MIXED -- `CAT_US_Equity` (230 str + 15
  int; int years 2026, 2027, 2028), `CSL_AU_Equity` (247 str + 15 int; 2027, 2028, 2029), `6861_JP_Equity` (247 str +
  15 int; 2027, 2028, 2029). The 15 int figures per name are source `BBG`. **Non-4-digit labels: NONE** in the live
  data; **years present as BOTH str and int in one block: NONE** (so today no two groups would print the same year).
  The `"?"` default for a figure with no `fiscal_year` is the only non-numeric label the CODE can produce.
- **Live served state at the cut:** a print sweep over all 37 model-block keys returns 200 for 33, 500 for CAT, CSL and
  6861, and 404 for NVDA_US_Equity (not covered by the crosswalk -- pre-existing, out of scope); the other 12 GET routes
  return 200 for CAT with real parameters (full per-route and per-key baseline re-read by AC3).
- **render_pack.py IS in the adapter's artifact:** the build script's transitive import closure (derived at HEAD:
  58 inputs) contains `lib/research/print/__init__.py` and `lib/research/print/render_pack.py`. Any byte change here
  changes the zip, so this cell redeploys `opal-amgt-scoped-api`. The plotting library is NOT in the zip: it is the
  attached layer `opal-amgt-print-deps:1` (Linux wheels) and is imported at CALL time by `_plotting()` (`:85-111`).

**RULED, what you build:**
1. In `render_pack.py`, ONE module-level helper `_fiscal_year_sort_key(fy)` that returns `(0, int(str(fy)))` when
   `str(fy)` is exactly 4 digits and `(1, str(fy))` otherwise (so `"?"` and any future non-numeric label sort AFTER
   every numeric year, deterministically). The grouping key becomes `str(f.get("fiscal_year", "?"))` so a year stored
   once as `"2026"` and once as `2026` can never produce two headings; the render loop becomes
   `for fy in sorted(by_fy, key=_fiscal_year_sort_key)`. The heading text is unchanged in form (`"Fiscal year 2026"`
   whether the stored value was `"2026"` or `2026`) -- for every one of the 34 all-str names the rendered pack is
   byte-identical in its text lines. No other line of render_pack.py changes (the one other ordering compare is layout).
2. NEW test file `lib/research/api/tests/test_print_fiscal_year_sort.py`, offline, no plotting library needed for the
   pure arms, EXACTLY these 5 arms (names must match AC1):
   - `test_sort_key_orders_mixed_str_and_int_years` -- `sorted(["2025", 2027, "2016", 2026, "?"],
     key=render_pack._fiscal_year_sort_key)` == `["2016", "2025", 2026, 2027, "?"]`.
   - `test_grouping_key_merges_str_and_int_of_one_year` -- a block with a `"2026"` figure and a `2026` figure groups
     into ONE key `"2026"` (call the grouping exactly as `build_pack` does: factor it as `_group_by_fiscal_year(figures)`
     if you need a callable; if you add it, it is the ONE grouping path `build_pack` uses).
   - `test_all_str_years_order_unchanged` -- for `["2016", ..., "2025"]` the new key orders exactly as plain `sorted()`.
   - `test_head_copy_raises_on_mixed_keys` -- the DISCRIMINATING arm: load render_pack.py's bytes at the PINNED commit
     `218ff3c994` via `git show 218ff3c994:lib/research/print/render_pack.py` into a temp module and show its
     `sorted(by_fy.keys())` shape raises `TypeError` on `{"2025": [], 2026: []}` while the new module's path does not
     (pin by hash, never HEAD or merge-base -- row Z-S193).
   - `test_patched_render_pack_is_the_one_print_pack_reaches` -- the IDENTITY arm (W85-S1): import
     `lib.research.print.render_pack` by its QUALIFIED name, monkeypatch its `build_pack` with a recorder, call
     `lib.research.api.scoped_amgt._print_pack` with a stubbed model-block read, and assert the recorder was called
     (the function-scope import reaches the SAME module object: `sys.modules["lib.research.print.render_pack"] is
     render_pack`).
3. Redeploy the adapter (THE ACT, section 4) only after AC7 passes.

**Tests that pin the changed behaviour (census, CTO msgs 24100/24133 -- WHOLE repo):** the tracked tests that
reference `render_pack` / `build_pack` / `by_fy` are exactly 3, all under `integrations/bloomberg/research/tests/`:
`test_consumer_wiring.py`, `test_unresolved_overlay_renders_marked.py`, `test_vintage_derivation_identity.py`. Each
imports `load_model_block` (the reader), none asserts fiscal-year ORDER or calls `build_pack`'s render loop, so none
pins the changed line. Two of them fail to COLLECT at the cut (pre-existing, `2 errors during collection`) and are
NOT a bar for this cell. If your own re-census finds a test that asserts the old order or the old grouping, and it is
OUTSIDE `<paths>`: STOP before any live act, file a BLOCKING row, report -- the issuer widens.

## 2. WHERE THIS CAME FROM

Round 23, decomposition s.31 (cut by `2.0.0_SA_COO~Z`) on the CTO's round-22 analysis. Row `AMGT_RESAPP-Z-S215`
(ARMED, disarm_owner `1.0.0_SA_CTO~Z`) was filed by this seat at M3's drain after its own 13-route census with real
parameters; reproduced box-side on pre-M3 code (`a74268ba4d`), so it predates round 22. The binding closure check is
CTO msg 24137 as clarified at msg 24141 (the isolated interpreter carries EXACTLY the python3.11 Lambda runtime set;
isolation is proven by `lib` resolving inside the artifact and repo-only modules being unimportable).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/print/render_pack.py
lib/research/api/tests/test_print_fiscal_year_sort.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~94/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- A surface NOT in `<paths>` is a WALL (read freely). In particular `lib/research/api/scoped_amgt.py`, the build script,
  `_harvest_prefixes.py`, every producer of model blocks and every stored object are WALLS.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~94 <0.9.0_WK_AMGT_RESAPP~94@opal.agent>"
  -F <msgfile> -- <paths>` (message file written by the Write tool). Commit the CODE before any live act.

## 4. BOUNDS

**THE ACT (the only live write), under the never-widen pair `ledger/NEVER_WIDEN_ROUND23_RK94_{COO,CTO}_HALF.md`
(both halves signed before you spawn -- AC0 checks):** one or more builds of the ONE artifact key
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` by
`infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`, each version recorded; then
`terraform -chdir=infra/aws/terraform/harvest plan -target=module.scoped_amgt_api.aws_lambda_function.this` (must read
`0 to add, 1 to change, 0 to destroy`) and `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply
-target=module.scoped_amgt_api.aws_lambda_function.this` (safe-apply takes `[-chdir=DIR] apply [args]` exactly as
terraform does, and refuses every subcommand but `apply`). One or more targeted applies allowed, each recorded.
- **Deploy ledger:** `python .tools/deploy_ledger.py open --slug amgt-rk94-print-pack-fy-sort --title "<title>" --author
  "0.9.0_WK_AMGT_RESAPP~94" --lambda opal-amgt-scoped-api` (the tool takes `--slug --title --author` and `--leg` or
  `--lambda`; there is NO `--legs`) BEFORE the first upload; close it on the AC6 read.
- **AC7 BEFORE ANY DEPLOY:** an ImportError / ModuleNotFoundError, or any failing control, is a STOP -- deploy nothing,
  file a BLOCKING row. Never "fix" a closure failure by importing the naming module or the harvest store into adapter
  code, and never edit a WALL to make AC7 pass.
- **Rollback trigger (any one):** post-act CodeSha256 not equal to the uploaded sha; any of the 12 non-print GET routes
  whose AC3 status was 200 no longer 200; any print key whose AC3 status was 200 no longer 200; the scoped policy sha
  moved. Rollback = `aws s3api copy-object` the artifact from the AC3 VersionId (`3SfOfR7Pr3dGvmyY.dKr4doXcNWQnOuF` at the
  cut -- your AC3 read is the target), then the same targeted apply, then read CodeSha256 back equal to AC3's
  (`cRT7dOyfg8dNA2cjv4fz+i5fw9OursxqNyKfXh17jyQ=` at the cut). No artifact version is ever deleted.
- **No IAM change, no S3 write outside the one artifact key, no S3 delete, no stored model block touched.** PORTAL
  FROZEN. No alarm, monitor or schedule. No secrets needed.
- **Policy sha formula (the rk-90 W90-S6 trap):** `sha256(json.dumps(doc, sort_keys=True, separators=(",", ":")))`.
- **Tests:** each test directory in its OWN pytest call.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy as written is REFUSED with its measurement and a row; if a
  literal invocation fails on a tool-CLI or formula mismatch, run the real one, grade the substance, and file a row naming
  the issuer-text defect -- never report a false drift.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W94-S<k>`; textual splice inside the one fenced JSON array; never edit a row; a
  worker never holds disarm duty (disarm_owner `2.0.0_SA_COO~Z`); a pure disarm sets `DISMISSED_WITH_REASON`.

## 5. PROOF OF SPEC -- one clause per criterion

Every script below is written by you to the named file FROM THIS TEXT VERBATIM and run from the file (W84-S1: no
escape sequences inline). Grading order: AC0, AC1, AC2, AC3, AC4, AC7, AC5, AC6, AC8.

`.scratch/r94/ac3.py` (pre-act baseline: rollback targets + the per-route and per-key status baseline rk-92 lacked):
```
import boto3, hashlib, json, os, sys, urllib.parse
sys.path.insert(0, ".")
from lib.research.api import scoped_amgt as sa
lam = boto3.client("lambda", region_name="us-east-1"); s3 = boto3.client("s3", region_name="us-east-1"); iam = boto3.client("iam")
c = lam.get_function_configuration(FunctionName="opal-amgt-scoped-api")
h = s3.head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip")
d = iam.get_role_policy(RoleName="opal-amgt-scoped-api-role", PolicyName="opal-amgt-scoped-api-grants")["PolicyDocument"]
psha = hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("CodeSha256", c["CodeSha256"], "ArtifactVersionId", h.get("VersionId"), "policy_sha", psha[:16], "statements", len(d["Statement"]))
def inv(path, qs=None):
    ev = {"rawPath": path, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    if qs:
        ev["queryStringParameters"] = qs
    return json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read()).get("statusCode")
routes = [x.split()[1] for x in sa.scoped_amgt_route_table() if x.startswith("GET")]
route_status = {}
for r in routes:
    p = r.replace("{security_key}", "CAT_US_Equity").replace("{movement}", "trending").replace("{subject}", "chatter")
    route_status[r] = inv(p, {"tickers": "CAT US"} if "timeseries" in p else None)
print("routes", len(routes), "status", sorted(set(route_status.values())), "non200", [r for r, s in route_status.items() if s != 200])
keys = sorted({o["Key"][len("derived/model_block/"):].rsplit("/", 2)[0] for p in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="derived/model_block/") for o in p.get("Contents", []) if o["Key"].endswith("model_block.json")})
print_status = {k: inv("/api/scoped/amgt/security/%s/print" % urllib.parse.quote(k, safe="")) for k in keys}
print("print_keys", len(keys), "print_200", sum(1 for s in print_status.values() if s == 200), "print_non200", sorted((k, s) for k, s in print_status.items() if s != 200))
os.makedirs(".scratch/r94", exist_ok=True)
json.dump({"CodeSha256": c["CodeSha256"], "ArtifactVersionId": h.get("VersionId"), "policy_sha": psha, "routes": route_status, "print": print_status}, open(".scratch/r94/pre.json", "w"), indent=1)
```

`.scratch/r94/ac7.py` (the closure check: identical to AMGT-rk-92's AC7 outer script except the paths `r92` -> `r94`
and the zip name `m3_build.zip` -> `rk94_build.zip`; the Lambda runtime set is copied to
`.scratch/r94/lambda_runtime_pkgs` and passed as `LAMBDA_RUNTIME_PKGS`):
```
import os, shutil, subprocess, sys, zipfile
import importlib.util as _u
zp = os.path.abspath(".scratch/r94/rk94_build.zip")
root = os.path.abspath(".scratch/r94/zipcheck")
shutil.rmtree(root, ignore_errors=True)
with zipfile.ZipFile(zp) as zf:
    zf.extractall(root)
    names = zf.namelist()
    print("unzipped", len(names), "entries; render_pack in zip", "lib/research/print/render_pack.py" in names)
venv = os.path.abspath(".scratch/r94/venv")
if not os.path.isdir(venv):
    subprocess.run([sys.executable, "-m", "venv", "--without-pip", venv], check=True)
vpy = os.path.join(venv, "Scripts", "python.exe") if os.name == "nt" else os.path.join(venv, "bin", "python")
probe = subprocess.run([vpy, "-I", "-c", "import sys; sys.path.insert(0, sys.argv[1]); import rpds", root], capture_output=True)
if probe.returncode != 0:
    pin = [ln for ln in open("infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh", encoding="utf-8").read().splitlines() if ln.startswith("RPDS_PIN=")][0].split("=", 1)[1].strip().strip(chr(34))
    wd = os.path.abspath(".scratch/r94/local_wheels")
    subprocess.run([sys.executable, "-m", "pip", "download", "--quiet", "--disable-pip-version-check", "--no-deps", "--only-binary=:all:", "-d", wd, pin], check=True)
    placed = []
    for wn in sorted(os.listdir(wd)):
        with zipfile.ZipFile(os.path.join(wd, wn)) as wz:
            for n in wz.namelist():
                if n.startswith("rpds/") and n.endswith((".pyd", ".so")) and not os.path.exists(os.path.join(root, n)):
                    wz.extract(n, root)
                    placed.append(n)
    print("overlay (scratch root ONLY, not the zip):", placed)
rt = os.path.abspath(".scratch/r94/lambda_runtime_pkgs")
if os.path.isdir(rt):
    shutil.rmtree(rt)
os.makedirs(rt)
for pkg in ("boto3", "botocore", "s3transfer", "jmespath", "dateutil", "urllib3", "six"):
    spec = _u.find_spec(pkg)
    src = os.path.dirname(spec.origin) if spec.submodule_search_locations else spec.origin
    (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(rt, os.path.basename(src)))
print("lambda runtime set (python3.11 provides these; the build never vendors them):", sorted(os.listdir(rt)))
env = dict(os.environ, LAMBDA_RUNTIME_PKGS=rt)
r = subprocess.run([vpy, "-I", os.path.abspath(".scratch/r94/ac7_inner.py"), root], env=env)
sys.exit(r.returncode)
```

`.scratch/r94/ac7_inner.py` (runs INSIDE the fresh venv, `-I`; the three isolation controls are rk-92's, unchanged):
```
import json, os, sys, importlib.util
root = sys.argv[1]
runtime = os.environ["LAMBDA_RUNTIME_PKGS"]
sys.path[:] = [root, runtime] + [p for p in sys.path if "site-packages" not in p and p != ""]
os.chdir(root)
import lib
if not os.path.abspath(lib.__path__[0]).startswith(os.path.abspath(root)):
    print("FAIL: lib resolves outside the artifact --", lib.__path__[0])
    sys.exit(2)
print("control: lib resolves inside the artifact")
for repo_only in ("lib.opal_naming", "lib.research.harvest.store", "pyarrow"):
    try:
        spec = importlib.util.find_spec(repo_only)
    except ImportError:
        spec = None
    if spec is not None:
        print("FAIL: repo-only module importable --", repo_only)
        sys.exit(2)
print("control: lib.opal_naming, lib.research.harvest.store, pyarrow NOT importable (isolated)")
import boto3
print("control: boto3 importable from the Lambda runtime set only --", os.path.abspath(boto3.__file__).startswith(os.path.abspath(runtime)))
results = []
def arm(name, fn):
    try:
        out = fn()
        print("ARM", name, "OK", str(out)[:160])
        results.append("OK")
    except ImportError as exc:
        print("ARM", name, "IMPORT-FAIL", type(exc).__name__, exc)
        results.append("IMPORT")
    except Exception as exc:
        print("ARM", name, "OTHER-FAIL", type(exc).__name__, str(exc)[:200])
        results.append("OTHER")
arm("import_handler", lambda: __import__("lambda_function").__name__)
arm("import_scoped_amgt", lambda: __import__("lib.research.api.scoped_amgt", fromlist=["x"]).__name__)
def sort_arm():
    from lib.research.print import render_pack as rp
    got = sorted(["2025", 2027, "2016", 2026, "?"], key=rp._fiscal_year_sort_key)
    assert got == ["2016", "2025", 2026, 2027, "?"], got
    assert os.path.abspath(rp.__file__).startswith(os.path.abspath(root)), rp.__file__
    return got
arm("render_pack_sort_from_zip", sort_arm)
print("RESULT arms", len(results), "ok", results.count("OK"), "import_fail", results.count("IMPORT"), "other_fail", results.count("OTHER"))
sys.exit(0 if results.count("OK") == len(results) else 1)
```

The plotting path itself is NOT exercised in AC7: the plotting library lives in the attached layer
`opal-amgt-print-deps:1` as Linux wheels, which cannot load on this box. The full print path is proven LIVE by AC6's
five named invokes and the whole-population sweep. `ac5.py` and `ac6.py` are written by you from section 4 and the
AC5/AC6 expectations; record each file's bytes in the deliverable.

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND23_RK94_COO_HALF.md && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND23_RK94_CTO_HALF.md && grep -c "^<""status>complete</""status>$" org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-92.sa-raw-move.md</invocation><expect>both pair halves present (read BOTH, signed) and "1" -- rk-92 (M3) complete at HEAD; anything else STOPS the order before any edit</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests/test_print_fiscal_year_sort.py -v -p no:cacheprovider</invocation><expect>"5 passed", 0 failed, the PASSED lines naming test_sort_key_orders_mixed_str_and_int_years, test_grouping_key_merges_str_and_int_of_one_year, test_all_str_years_order_unchanged, test_head_copy_raises_on_mixed_keys (pinned to 218ff3c994) and test_patched_render_pack_is_the_one_print_pack_reaches</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests -q -p no:cacheprovider</invocation><expect>"204 passed", 0 failed -- the 199 measured at the cut plus this cell's 5 (re-measure the baseline at spawn; the bar is baseline plus 5, failures 0)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r94/ac3.py</invocation><expect>CodeSha256 cRT7dOyfg8dNA2cjv4fz+i5fw9OursxqNyKfXh17jyQ= ArtifactVersionId 3SfOfR7Pr3dGvmyY.dKr4doXcNWQnOuF policy_sha 42d6bd14a35e1718 statements 4 (the rollback targets; if they differ, the values read ARE the rollback targets and the difference is a row, since another act moved the adapter); routes 13 with exactly one non-200, /api/scoped/amgt/security/{security_key}/print (500 for CAT); print_keys 37 print_200 33 with print_non200 naming exactly [('6861_JP_Equity', 500), ('CAT_US_Equity', 500), ('CSL_AU_Equity', 500), ('NVDA_US_Equity', 404)] -- NVDA's 404 is pre-existing (not covered by the crosswalk) and not this cell's; measured at the cut; pre.json written</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && git log --format="%h %an %s" 33ea2e4e00..HEAD -- lib/research lib/opal_data_harvest infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest</invocation><expect>the carry-along since the SERVED source (33ea2e4e00, M3's drain, which built cRT7dOyf...) on every root the adapter's closure draws from: ONLY this cell's own commit(s) by 0.9.0_WK_AMGT_RESAPP~94 (0 at the cut). Any other commit is a STOP with a BLOCKING row -- it would ride this redeploy unnamed</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only .scratch/r94/rk94_build.zip 2>&1 | tail -3 && python .scratch/r94/ac7.py</invocation><expect>RUN BEFORE AC5 (CTO msgs 24137/24141): the build prints "BUILD-ONLY: copied to .scratch/r94/rk94_build.zip -- NOT uploaded" after its own generated-prefix drift check; "render_pack in zip True"; the three controls ("lib resolves inside the artifact", "lib.opal_naming, lib.research.harvest.store, pyarrow NOT importable (isolated)", "boto3 importable from the Lambda runtime set only -- True"); ARM import_handler OK, ARM import_scoped_amgt OK, ARM render_pack_sort_from_zip OK ['2016', '2025', 2026, 2027, '?']; "RESULT arms 3 ok 3 import_fail 0 other_fail 0". Any IMPORT-FAIL or failing control = STOP, deploy nothing</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r94/ac5.py</invocation><expect>the deploy-ledger entry OPENED before the first upload; the build uploads (each artifact VersionId printed); `terraform -chdir=infra/aws/terraform/harvest plan -target=module.scoped_amgt_api.aws_lambda_function.this` prints "Plan: 0 to add, 1 to change, 0 to destroy."; `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -target=module.scoped_amgt_api.aws_lambda_function.this` prints "Apply complete! Resources: 0 added, 1 changed, 0 destroyed."; post CodeSha256 moved from AC3's and equal to the uploaded artifact's sha, State Active, LastUpdateStatus Successful</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r94/ac6.py</invocation><expect>live, against pre.json: the print route returns 200 for EACH of CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity, BA_US_Equity and COST_US_Equity (5 of 5); the whole-population sweep prints print_keys 37 print_200 36 with print_non200 exactly [('NVDA_US_Equity', 404)] -- the 3 fixed, NVDA's pre-existing 404 unchanged, 0 regressed (every key 200 in AC3 is still 200); the 12 non-print GET routes each equal to their AC3 status (200); the scoped policy sha equal to AC3's (42d6bd14a35e1718 at the cut), statements 4; a targeted `terraform plan` reads "No changes."; the deploy-ledger entry CLOSED with this read as proof. Any regression = rollback per section 4</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-94"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only 218ff3c994 HEAD -- lib/research/print/render_pack.py lib/research/api/tests/test_print_fiscal_year_sort.py</invocation><expect>exactly the two files, each ASCII-only with 0 CRLF (read their bytes: the non-ASCII byte count and the CRLF count are both 0, equal to render_pack.py's pre-edit figures of 0 and 0)</expect></criterion>
</proof_of_spec>

No judgment criterion.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~94/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.proof_of_spec.json`,
grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC7,AC5,AC6,AC8`
(rc 0), flip the status to complete, commit, and report once: the diff of render_pack.py, AC7's controls and arms,
CodeSha256 and every artifact VersionId pre/post, the print status pre/post for all 37 keys, the 12 other routes pre/post,
the policy sha pre/post, rollback fired or not, the ledger entry open/close.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES.** (1) Step (2) of the ruling (the producer writing int forecast years; the model_block re-derivation)
is chain G's, recorded in decomposition s.30b beside model_block's re-homing. (2) AC7 cannot exercise the plotting
path (the layer is Linux wheels); the live AC6 invokes are its proof. (3) The regression's discriminating arm is pinned
to `218ff3c994` (Z-S193). (4) Grouping is normalised as well as sorting so that a year stored as both `"2026"` and
`2026` never renders two headings; measured 0 such collisions in the live data today, so the pack text is unchanged
for every currently-rendering name.

<status>pending</status>
<round>23</round>
<slot>~94</slot>
<fabric>site-z</fabric>
