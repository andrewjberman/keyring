# AMGT_RESAPP task order -- `AMGT-rk-97` -- the print route's render time: measure the phases live and locally, then raise `opal-amgt-scoped-api` memory 512 -> 1769 MB (one full vCPU; the render is CPU-bound) by ONE targeted apply, and prove every name under 10 s warm and a fresh container under 20 s by live invokes with CloudWatch REPORT durations

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-97</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~97</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- arms no cron, alarm, monitor or cadence; the one live act is a TARGETED
  apply of module.scoped_amgt_api.aws_lambda_function.this changing memory_size only; the deploy-ledger entry is
  opened before the apply and closed on the post-act read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, grant, layer, environment variable, timeout or code moves. The
  function's memory setting has ONE writer in the repo (scoped-amgt-api.tf:267, via the yang-lambda module's
  main.tf:29); 0 scripts call update-function-configuration on this function (census at the cut).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~97`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your
first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`, `.tools/`
and `infra/aws/terraform/harvest/scoped-amgt-api.tf` exist; if any is absent, STOP with a BLOCKING row. Every Bash call
begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~97;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check
out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-97` (round 24, row `AMGT_RESAPP-Z-S216`)

**The ruling of record, verbatim** (1.0.0_SA_CTO~Z msg 24168, 2026-09-22T08:50:19Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T085019Z_1.0.0_SA_CTO_Z_Re_rk-94_drain__Z-S216_PRE-RULED_for_rou.md`,
lines 8-12):

> Z-S216 (ARMED, mine): 15-17 s warm against a hard 29 s ceiling, with 29,000 ms REPORTs at 08:13Z and 08:14Z.
> PRE-RULED for round 24; the ruling is confirmed in my round-23 analysis:
> 1. MEASURE FIRST. Time the phases on the three validation names AND on BA and COST (fast, about 104 KB): import, the
> font cache or MPLCONFIGDIR, data load, render, PDF write. The BA/COST vs CAT/CSL/6861 gap is itself evidence: more
> fiscal-year rows or charts, or a first-render cost.
> 2. FIX THE DOMINANT TERM, preferring (a), a prebuilt font cache or packaged MPLCONFIGDIR, and/or (b), more memory for
> CPU (230/512 MB used today). Both change no data and no served path. Target: every name under 10 s warm, and a cold
> start under 20 s.
> 3. (c), a per-(key, model-block stamp) PDF cache in S3, ONLY if (a) and (b) cannot reach the target. It is a new
> stored served artifact, so it needs its own pair, its builder address, and an invalidation rule keyed on the
> model-block stamp.
> Every candidate is proved by a live invoke on all 5 names, repeated 3 times, with the CloudWatch REPORT Durations
> printed.

**THE ISSUER'S MEASUREMENT AT THE CUT (step 1, done read-only by `2.0.0_SA_COO~Z` at SITEZ `4ecff8064b`). You
re-measure it all in AC1/AC2; your numbers govern.**

- **Live config:** `opal-amgt-scoped-api` Timeout 29, MemorySize 512, EphemeralStorage 512, x86_64, Layers
  `opal-amgt-print-deps:1`, CodeSha256 `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` (rk-94's deploy, LastModified
  2026-09-22T08:12:12Z).
- **CloudWatch REPORT, 8 h window, all pages: 306 REPORT lines, 176 over 5,000 ms.** Warm print invokes sit at
  **8.6-13.6 s** with outliers to **18.6 s**; Max Memory Used **224-236 MB of 512**. The **first print on a fresh
  container** runs **22.8-23.9 s** (05:29:11Z, 08:14:54Z, 08:45:22Z), and **six invokes hit `Status: timeout` at
  29,000 ms** (08:13:32Z, 08:14:01Z, 08:14:30Z, 08:44:01Z, 08:44:30Z, 08:44:59Z), four of them carrying `Init Duration`.
  Init Duration itself is only 130-168 ms: the cold cost is paid INSIDE the first print, where the plotting stack is
  imported (function-scope import, `render_pack.py:85-110`).
- **Local phase split** (Windows, python 3.11.9, matplotlib 3.11.0 vs the layer's 3.11.2 -- a DIFFERENT CPU and build,
  so it measures the SPLIT, never the Lambda seconds). Import plus a cold font cache: **0.69-1.08 s**. Per name:

  | name | figures | data load | render + PDF write | pypdf text extract |
  |---|---|---|---|---|
  | CAT_US_Equity | 262 | 0.52 | **2.39** | 0.40 |
  | CSL_AU_Equity | 279 | 0.56 | **2.46** | 0.38 |
  | 6861_JP_Equity | 277 | 0.60 | **2.49** | 0.37 |
  | BA_US_Equity | 179 | 0.56 | **1.67** | 0.22 |
  | COST_US_Equity | 205 | 0.59 | **1.75** | 0.25 |

  Render + PDF write is **70-75 %** of the local total on every name, and it scales with the figure count (262-279 vs
  179-205), which is the BA/COST gap. The local-to-Lambda ratio is about **4.5-5x**, consistent with 512 MB buying
  about 0.29 of one vCPU. **So the dominant term is CPU-bound rendering (warm), and the cold term is the plotting
  stack's import and font cache, also CPU-bound.** Both scale with CPU.

**ISSUER RULING (L5): candidate (b), memory 512 -> 1769 MB, and ONLY (b) in this order.** 1769 MB is the point at which
Lambda allocates one full vCPU. The render is single-threaded, so memory above 1769 buys no more speed for it. Projected
from the measured seconds by the CPU ratio: warm 8.6-18.6 s -> about 2.5-5.4 s, and a fresh container's first print
22.8-23.9 s -> about 6.6-6.9 s. Both are inside the targets with margin. Candidate (a) (a packaged font cache or
MPLCONFIGDIR; also packaged bytecode, see the record face) is NOT built here. It is the named next candidate ONLY if
(b) misses a target, and it goes to the CTO as a row. Candidate (c) is out of scope.

**THE CHANGE, one file:** `infra/aws/terraform/harvest/scoped-amgt-api.tf`.
- Line 267: `memory_size = 512` becomes `memory_size = 1769`.
- The rk-6 comment at `:271-273` ("TIMEOUT AND MEMORY ARE DELIBERATELY UNCHANGED ...") is replaced with an ASCII
  comment that says three things:
  - memory was raised to 1769 by AMGT-rk-97 under the never-widen pair `NEVER_WIDEN_ROUND24_RK97_*`, row Z-S216;
  - 1769 is one full vCPU and the print render is CPU-bound;
  - timeout stays 29, the HTTP API integration ceiling.
- Nothing else in the file moves.

## 2. WHERE THIS CAME FROM

**ROUND 24**, decomposition s.32 (cut by `2.0.0_SA_COO~Z`), on the CTO's msg 24168 and its round-23 analysis
(msg 24174, `ledger/ROUND_ANALYSIS.round23.md` @`1cb8c3cab3`), which AMENDS the acceptance, verbatim:

> (a) the FIRST read after the apply is a COLD invoke. The deploy forces a fresh environment; if anything has invoked
> the function since, force another with an env-var bump. Take it before anything warms the function. Target under
> 20 s on all 5 names.
> (b) Then 5 names x 3 warm repeats, target under 10 s.
> (c) Then a concurrency burst forcing parallel cold starts, with 0 Unhandled.

The env-var bump is NOT in this order (see the record face): the cold read is a 10-way concurrent coldphase, 2 per
name, taken with no invoke between the apply and it.
- Row `AMGT_RESAPP-Z-S216` (ARMED) was filed at rk-94's drain @`4ecff8064b`. After rk-94, print renders for all 5
  model-block names, but runs against the 29 s ceiling and has been cut off.
- Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~97/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-97.print-latency.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **Any surface NOT named in `<paths>` is a WALL** (reads need no grant).
  - In particular: `lib/research/print/render_pack.py`, `lib/research/api/scoped_amgt.py`, the print-deps layer
    (`print-deps-layer.tf`, `build_print_deps_layer.py`, `build-and-upload-print-deps-layer.sh`), both build scripts,
    the artifact key, every stored model block and every other S3 object.
  - Scratch is `<your worktree>/.scratch/r97/` only, and is never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~97 <0.9.0_WK_AMGT_RESAPP~97@opal.agent>" -F <msgfile> -- <paths>`.
  - The message file is written by the Write tool.
  - **Commit the `.tf` edit BEFORE the apply.** safe-apply does not check lanes; only the commit gate does, so the
    commit is the lane check.
  - Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**THE ACT is the only live write. It runs under the never-widen pair `ledger/NEVER_WIDEN_ROUND24_RK97_{COO,CTO}_HALF.md`;
both halves must be signed before you spawn (AC0 checks).**
- **The command:** ONE targeted apply,
  `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -target=module.scoped_amgt_api.aws_lambda_function.this`.
- **Its preconditions:**
  - AC3's plan reads `Plan: 0 to add, 1 to change, 0 to destroy.`
  - The ONLY changed attribute is `memory_size = 512 -> 1769`.
  - If the plan shows ANY other changed attribute (a `source_code_hash`, `layers`, `timeout`, `environment` or
    anything else), or any other resource: STOP, apply nothing, and file a BLOCKING row. That other change would
    ride this apply unnamed.
- **Init first:** a fresh worktree needs `terraform -chdir=infra/aws/terraform/harvest init -input=false` before the
  plan (row W94-S1). The init writes only the local `.terraform/` directory.
- **Deploy ledger:**
  - Open it AFTER AC3 passes and BEFORE the apply:
    `python .tools/deploy_ledger.py open --slug amgt-rk97-print-memory --title "<title>" --author "0.9.0_WK_AMGT_RESAPP~97" --lambda opal-amgt-scoped-api`.
    The tool takes `--slug --title --author` and `--leg` or `--lambda`; there is NO `--legs`.
  - Close it on the AC6 read, and report the entry's file path and its closed state.
- **KEEP OR ROLL BACK, decided on AC5/AC6. The pair covers both branches:**
  - **ROLLBACK (any one):**
    - post-act CodeSha256, Layers, Timeout or EphemeralStorage differs from AC0's read;
    - any print name's extracted text differs from the baseline;
    - any non-print route whose baseline status was 200 is no longer 200;
    - any name's post-act median print duration is NOT lower than its baseline median.
    - **Rollback = a NEW commit** setting `memory_size = 512` again (never a revert of history), then the same
      targeted apply, then `get-function-configuration` must print `MemorySize 512`. Close the ledger with the
      rollback read.
  - **KEEP, TARGET MET:** no rollback trigger fired, every warm print is under 10,000 ms, AND every fresh-container
    print is under 20,000 ms. AC5 passes.
  - **KEEP, TARGET MISSED:** no rollback trigger fired, but a target is missed. KEEP 1769 (it is strictly better and
    inside the pair). REFUSE AC5 with its measurement, and file a row naming the missed target and its durations. Per
    the CTO (msg 24174), a missed COLD target with nothing regressed sends the row Z-S217 layer rebuild (bytecode
    kept) to round 25. Never build (a) or (c) here.
- **No other live write:** no IAM change, no layer publish, no artifact upload, no S3 write, no S3 delete, no stored
  model block touched. PORTAL FROZEN. No alarm, monitor or schedule. No secrets needed.
- **Invokes:**
  - The measurement invokes are reads of the served route. Each run is 10 coldphase prints, 15 repeat prints,
    5 non-print invokes and a burst of 10 prints.
  - Run each measurement ONCE per criterion; never loop it.
  - Traffic from other clients may share the warm pool. Record, never retry, a run that another client perturbs.
- **Scripts and tests:**
  - **A script that carries an escape is a FILE** you write from this order's text verbatim (W84-S1). None of the
    scripts below carries one; write them as files anyway, byte-for-byte.
  - **Tests:** each test directory in its OWN pytest call.
- **THE REFUSAL CLAUSE:**
  - A criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row. It is never repaired,
    widened, or satisfied by a route this order did not name, and never by editing a WALL.
  - If a literal invocation fails on a tool-CLI mismatch, run the real one, grade the substance, and file a row
    naming the issuer-text defect.
- **SURPRISE ROWS:**
  - Ids are `AMGT_RESAPP-Z-W97-S<k>`, with `<k>` from 1. Each row carries `"project": "AMGT_RESAPP"` and
    `"fabric": "site-z"`.
  - Append by textual splice inside the one fenced JSON array. Never edit an existing row.
  - A worker never holds disarm duty: `disarm_owner` is `2.0.0_SA_COO~Z`. Row Z-S216 is NOT yours to resolve.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 600)

**Grading order:** AC0, AC1, AC2, then (edit, and commit the `.tf`), AC3, then (open the ledger), AC4, AC5, AC6, then (close the ledger), AC7, AC8.
AC5 runs IMMEDIATELY after AC4: nothing between them invokes the function (AC4's `cfg.py post` is a configuration
read, not an invoke).
Write each block below to the named file under `<your worktree>/.scratch/r97/`, byte-for-byte, and run it from the
worktree root.

`.scratch/r97/cfg.py` (the function's configuration; used pre-act by AC0 and post-act by AC4):
```
import boto3, sys
c = boto3.client("lambda", region_name="us-east-1").get_function_configuration(FunctionName="opal-amgt-scoped-api")
lay = [l["Arn"].split(":")[-2] + ":" + l["Arn"].split(":")[-1] for l in c.get("Layers", [])]
print(sys.argv[1], "MemorySize", c["MemorySize"], "Timeout", c["Timeout"], "EphemeralStorage", c["EphemeralStorage"]["Size"], "Layers", lay, "CodeSha256", c["CodeSha256"], "State", c["State"], "LastUpdateStatus", c["LastUpdateStatus"], "env_keys", sorted(c.get("Environment", {}).get("Variables", {})))
```

`.scratch/r97/measure.py` (the live proof the ruling names; `baseline` pre-act, `after` post-act):
```
import base64, boto3, hashlib, io, json, os, statistics, sys
from concurrent.futures import ThreadPoolExecutor
from botocore.config import Config
import pypdf
label = sys.argv[1]
lam = boto3.client("lambda", region_name="us-east-1", config=Config(read_timeout=70, retries={"max_attempts": 0}, max_pool_connections=16))
NAMES = ["CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity", "BA_US_Equity", "COST_US_Equity"]
def call(key, leaf):
    ev = {"rawPath": "/api/scoped/amgt/security/%s/%s" % (key, leaf), "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    r = lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode(), LogType="Tail")
    log = base64.b64decode(r.get("LogResult", "")).decode("utf-8", "replace")
    rep = log.split("REPORT RequestId")[-1] if "REPORT RequestId" in log else ""
    ms = float(rep.split("Duration: ")[1].split(" ms")[0]) if "Duration: " in rep else -1.0
    body = json.loads(r["Payload"].read() or b"{}")
    if r.get("FunctionError"):
        status = "timeout" if "timed out" in str(body.get("errorMessage", "")) else "error"
    else:
        status = body.get("statusCode")
    text = ""
    if status == 200 and leaf == "print":
        pdf = base64.b64decode(body["body"])
        txt = "".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(pdf)).pages)
        text = ("PDF:" if pdf[:4] == b"%PDF" else "NOTPDF:") + hashlib.sha256(txt.encode("utf-8")).hexdigest()[:16]
    return {"key": key, "leaf": leaf, "status": status, "ms": ms, "cold": "Init Duration" in rep, "report": rep.strip()[:240], "text": text}
out = {"label": label, "coldphase": [], "rows": [], "other": [], "burst": []}
PAIRS = [n for n in NAMES for _ in range(2)]
with ThreadPoolExecutor(len(PAIRS)) as ex:
    out["coldphase"] = list(ex.map(lambda n: call(n, "print"), PAIRS))
for row in out["coldphase"]:
    print(label, "coldphase", row)
for n in NAMES:
    for i in range(3):
        row = call(n, "print")
        out["rows"].append(row)
        print(label, n, i + 1, row)
for n in NAMES:
    row = call(n, "thesis")
    out["other"].append(row)
    print(label, "other", row)
with ThreadPoolExecutor(10) as ex:
    out["burst"] = list(ex.map(lambda _: call("CAT_US_Equity", "print"), range(10)))
for row in out["burst"]:
    print(label, "burst", row)
allrows = out["coldphase"] + out["rows"] + out["burst"]
cp_cold = [r for r in out["coldphase"] if r["cold"]]
cp_names = sorted({r["key"] for r in cp_cold})
warm = [r["ms"] for r in out["rows"] if not r["cold"]]
b_cold = [r["ms"] for r in out["burst"] if r["cold"]]
pdfs = sum(1 for r in out["rows"] if r["text"].startswith("PDF:"))
med = {n: round(statistics.median([r["ms"] for r in out["rows"] if r["key"] == n])) for n in NAMES}
texts = {n: sorted({r["text"] for r in out["rows"] + out["coldphase"] if r["key"] == n and r["text"]}) for n in NAMES}
print("SUMMARY", label, "coldphase_cold_names %d/5" % len(cp_names), "coldphase_cold_max %.0f" % max([r["ms"] for r in cp_cold] or [-1]), "pdf_ok %d/15" % pdfs, "warm_n", len(warm), "warm_max %.0f" % max(warm or [-1]), "burst_cold_n", len(b_cold), "burst_max %.0f" % max([r["ms"] for r in out["burst"]] or [-1]), "unhandled", sum(1 for r in allrows if r["status"] in ("timeout", "error")), "other_status", [r["status"] for r in out["other"]])
print("MEDIANS", label, med)
print("TEXTS", label, texts)
os.makedirs(".scratch/r97", exist_ok=True)
json.dump(out, open(".scratch/r97/%s.json" % label, "w"), indent=1)
```

`.scratch/r97/phase.py` (the local phase split; a DIFFERENT instrument from the live REPORT, which is why it is here):
```
import os, sys, time, tempfile, shutil
cfg = tempfile.mkdtemp(prefix="mplcold_")
os.environ["MPLCONFIGDIR"] = cfg
sys.path.insert(0, ".")
t = time.perf_counter
t0 = t()
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
t1 = t()
print("local matplotlib", matplotlib.__version__, "import_plus_cold_font_cache_s %.2f" % (t1 - t0), "cache_files", os.listdir(cfg))
from lib.research.api import scoped_amgt as sa
import lib.research.print.render_pack as rp
import pypdf
real = pypdf.PdfReader
for name in ["CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity", "BA_US_Equity", "COST_US_Equity"]:
    ident = sa.resolve_identity(name)
    a = t()
    block = sa.read_model_block(ident["security_key"])
    b = t()
    box = {}
    def timed(*aa, **kk):
        box["r0"] = t()
        return real(*aa, **kk)
    pypdf.PdfReader = timed
    c = t()
    pdf, txt = rp.build_pack(block["security"], block, out_dir=tempfile.mkdtemp())
    d = t()
    pypdf.PdfReader = real
    terms = {"data_load": b - a, "render_pdf": box["r0"] - c, "pypdf_extract": d - box["r0"]}
    print(name, "figures", len(block.get("figures", [])), " ".join("%s_s %.2f" % kv for kv in terms.items()), "largest", max(terms, key=terms.get))
shutil.rmtree(cfg, ignore_errors=True)
```

`.scratch/r97/plan_read.py <planfile>` (reads a saved plan; AC3 pre-act, AC7 post-act):
```
import sys
lines = open(sys.argv[1], encoding="utf-8", errors="replace").read().splitlines()
print("plan_line", [l.strip() for l in lines if l.strip().startswith("Plan:") or "No changes." in l])
print("resources", [l.strip() for l in lines if l.strip().startswith("# ") and "will be" in l])
print("changed_attrs", [l.strip() for l in lines if " -> " in l])
```

`.scratch/r97/compare.py` (AC6: served content and non-print routes invariant; median per name moved down):
```
import json, statistics
b = json.load(open(".scratch/r97/baseline.json"))
a = json.load(open(".scratch/r97/after.json"))
NAMES = ["CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity", "BA_US_Equity", "COST_US_Equity"]
def texts(d, n):
    return sorted({r["text"] for r in d["rows"] if r["key"] == n and r["text"]})
same = [n for n in NAMES if len(texts(b, n)) == 1 and texts(a, n) == texts(b, n)]
print("text_identical", len(same), "of", len(NAMES), "differ", [n for n in NAMES if n not in same])
bo = {r["key"]: r["status"] for r in b["other"]}
ao = {r["key"]: r["status"] for r in a["other"]}
print("other_route_equal", sum(1 for n in bo if bo[n] == ao.get(n)), "of", len(bo), "regressed", [n for n in bo if bo[n] == 200 and ao.get(n) != 200])
slower = []
for n in NAMES:
    mb = statistics.median([r["ms"] for r in b["rows"] if r["key"] == n])
    ma = statistics.median([r["ms"] for r in a["rows"] if r["key"] == n])
    print("median_ms", n, round(mb), "->", round(ma))
    if not ma < mb:
        slower.append(n)
print("medians_not_lower", slower)
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND24_RK97_COO_HALF.md && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND24_RK97_CTO_HALF.md && sed -n '267p' infra/aws/terraform/harvest/scoped-amgt-api.tf && python .scratch/r97/cfg.py pre</invocation><expect>BEFORE any edit: both pair halves present (read BOTH, signed); line 267 prints "  memory_size = 512"; then "pre MemorySize 512 Timeout 29 EphemeralStorage 512 Layers ['opal-amgt-print-deps:1'] CodeSha256 r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w= State Active LastUpdateStatus Successful env_keys ['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']" (measured at the cut). A differing CodeSha256 or Layers means another act moved the function: the values you read ARE the rollback targets, and the difference is a row. A MemorySize other than 512 is a STOP</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r97/measure.py baseline</invocation><expect>LIVE, pre-act, the baseline this order is graded against. The expected values were measured from CloudWatch at the cut; your run governs:
- a SUMMARY line with pdf_ok 15/15 (or each non-PDF row recorded with its status: timeout or error);
- warm durations in the 8,600-18,600 ms band;
- the coldphase (10 concurrent prints, 2 per name) and the burst (10 concurrent CAT prints) recorded as they fall. At 512 MB a cold print runs at or above about 22,800 ms or times out at 29,000, and unhandled may be non-zero (the CVO measured 3 of 5 names Unhandled in one sweep). That is the defect being fixed, recorded, NOT a stop;
- other_status for thesis on the 5 names recorded (the non-print baseline);
- TEXTS with exactly ONE text hash per name across its 3 repeats. Two hashes for one name means the extracted text is not stable; that is a STOP and a row, since AC6's invariance arm would then have no baseline;
- baseline.json written.</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r97/phase.py</invocation><expect>LOCAL, read-only, a different instrument from AC1:
- an import-plus-cold-font-cache time;
- for each of the 5 names, its figure count and the three terms, with "largest render_pdf" on 5 of 5 (measured at the cut: render 1.67-2.49 s against data load 0.52-0.60 and extract 0.22-0.40).
If render_pdf is NOT the largest term on every name, STOP before any edit and file a BLOCKING row: the choice of (b) rests on a CPU-bound render dominating.</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && terraform -chdir=infra/aws/terraform/harvest init -input=false -no-color > .scratch/r97/init.txt 2>&1; terraform -chdir=infra/aws/terraform/harvest plan -no-color -input=false -target=module.scoped_amgt_api.aws_lambda_function.this > .scratch/r97/plan_pre.txt 2>&1; python .scratch/r97/plan_read.py .scratch/r97/plan_pre.txt</invocation><expect>AFTER the .tf edit is COMMITTED:
- plan_line contains "Plan: 0 to add, 1 to change, 0 to destroy.";
- resources names exactly one resource, module.scoped_amgt_api.aws_lambda_function.this, updated in-place;
- changed_attrs is exactly ONE line, "~ memory_size = 512 -> 1769".
Anything else is a STOP: apply nothing, and file a BLOCKING row quoting the extra lines.</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -target=module.scoped_amgt_api.aws_lambda_function.this 2>&1 | tail -3; python .scratch/r97/cfg.py post</invocation><expect>Ledger entry OPENED before this call.
- The apply prints "Apply complete! Resources: 0 added, 1 changed, 0 destroyed.".
- Then "post MemorySize 1769 Timeout 29 EphemeralStorage 512 Layers ['opal-amgt-print-deps:1'] CodeSha256" followed by a value EQUAL to AC0's, and "State Active LastUpdateStatus Successful", with env_keys equal to AC0's.
- A moved CodeSha256, Layers, Timeout or EphemeralStorage is a ROLLBACK per section 4.</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r97/measure.py after</invocation><expect>LIVE, post-act, COLD FIRST (the CTO's round-23 acceptance, msg 24174). Run it IMMEDIATELY after AC4, with NO invoke of the function between the apply and this call (the apply recycles every environment, so the coldphase is the first read on fresh containers):
- (a) "coldphase_cold_names 5/5" -- at least one coldphase row per name carries "Init Duration" in its REPORT -- and coldphase_cold_max under 20000;
- (b) "pdf_ok 15/15" and warm_max under 10000 over the 5 names x 3 repeats;
- (c) burst_cold_n at least 1 (the 10-way burst forced parallel cold starts) and "unhandled 0" across every row of the run;
- every row's report string shows "Memory Size: 1769 MB".
If the coldphase reads fewer than 5 cold names (another client warmed the pool first), that arm is REFUSED with its rows and a row naming the perturbation; never re-run to get a colder draw.
A missed target with no rollback trigger is the KEEP-TARGET-MISSED branch of section 4: REFUSE this criterion with its numbers and a row; never re-run it to get a better draw.</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r97/compare.py</invocation><expect>"text_identical 5 of 5 differ []" -- the served pack text is unchanged on every name (memory changes no data and no served path); "other_route_equal 5 of 5 regressed []"; five median_ms lines, each strictly lower after; "medians_not_lower []". Any non-empty list is a ROLLBACK per section 4. Close the deploy-ledger entry on this read</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && terraform -chdir=infra/aws/terraform/harvest plan -no-color -input=false -target=module.scoped_amgt_api.aws_lambda_function.this > .scratch/r97/plan_post.txt 2>&1; python .scratch/r97/plan_read.py .scratch/r97/plan_post.txt && git diff --name-only 4ecff8064b HEAD -- infra/aws/terraform/harvest lib/research/print lib/research/api infra/aws/lambda/research</invocation><expect>
- plan_line contains "No changes.", resources is [] and changed_attrs is [] (state equals the declared 1769);
- the diff lists EXACTLY infra/aws/terraform/harvest/scoped-amgt-api.tf, with no other file under the adapter's roots. Read that file's bytes and record: non-ASCII bytes 0, CRLF 0, and line 267 "  memory_size = 1769".
On the ROLLBACK branch, the plan must also read "No changes." at 512.</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-97"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"N passed", 0 failed, where N equals the count you re-measure at spawn BEFORE the edit (record both). test_scoped_amgt_mount.py diffs the route table against this .tf, so the edit must leave it green</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~97/AMGT_RESAPP.TO-AMGT-rk-97.print-latency.proof_of_spec.json`
   per `org/standards/PROOF_OF_SPEC.schema.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8`;
   rc 0 is the verdict.
3. Flip the order's status (on the record face) to `complete` only if every criterion PASSES. Commit with
   `--only -- <paths>`.
4. Report ONCE, naming:
   - the pre and post config lines;
   - AC1's and AC5's SUMMARY and MEDIANS lines, and every cold row's REPORT;
   - AC2's five phase lines;
   - the plan lines, pre and post;
   - which section-4 branch fired (keep and target met, keep and target missed, or rollback);
   - the ledger entry's path and its open and close.

**MUTATION DISCIPLINE:** snapshot the `.tf` WORKING-TREE BYTES to `.scratch/r97/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**
1. **(b) ALONE, AT 1769 MB.** The ruling prefers "(a) and/or (b)".
   - The measurement says the dominant WARM term is a CPU-bound render. No font cache touches that term; only CPU
     does. So (b) is the candidate that addresses it.
   - 1769 MB is chosen as the single-vCPU point. 1024 MB (0.58 vCPU) would project to about 9.3 s on the worst
     observed warm (18.6 s), too close to the 10 s bar.
   - Above 1769 MB the single-threaded render gains nothing.
2. **(a) IS NOT BUILT, BUT IT HAS A SECOND MEMBER THE RULING DID NOT NAME: packaged BYTECODE.**
   `build_print_deps_layer.py` drops every `.pyc` and `__pycache__` (its `DROP_DIR_PARTS` / `DROP_SUFFIXES`), and
   `/opt` is read-only at runtime. So every fresh container compiles matplotlib, numpy, pillow and fonttools from
   source and can never cache the result.
   - Measured locally: the plotting-stack import takes 0.70 s with cached bytecode, and 1.77-2.13 s without it
     (`PYTHONPYCACHEPREFIX` set to an empty directory, plus `-B`).
   - At about 4.5-5x on Lambda, that is roughly 5-6 s of the ~10 s cold term, larger than the font cache
     (0.69-1.08 s locally).
   - If (b) misses the cold target, the next candidate is a layer rebuild that KEEPS bytecode (compiled for 3.11),
     together with a packaged font list. That is a layer publish, so it needs its own pair.
3. **The pypdf text extraction (`render_pack.py:322-326`) is WASTED on the print route.** `_print_pack` returns only
   the PDF bytes, yet every print pays the extraction: 0.22-0.40 s locally, about 10-15 % of the total.
   - It is a code change, outside the ruling's (a), (b) and (c).
   - It is NOT in this order. It is named here as a candidate for the CTO's round-24 analysis if the margin is ever
     needed.
4. **Cost:** memory x3.45 per ms. Over the last 8 h the function served 306 invokes; at an upper bound of about 5 s
   each at 1769 MB, that is about 2,700 GB-s, well under $0.05. Non-print routes (100-700 ms, I/O-bound) pay the
   higher per-ms price with little speed-up. That is immaterial at this volume and is recorded, not assumed.
5. **Pins:**
   - AC7's diff is pinned to `4ecff8064b` (Z-S193 discipline) and scoped to the adapter's roots. round-24 siblings
     (rk-96 in `lib/research/harvest`, and rk-95 in `.tools`) sit outside those roots.
   - Re-pin to the issuance commit if s.32 moves anything under those roots.
7. **THE CTO's ENV-VAR BUMP IS REPLACED, flagged at issuance (msg 24174 item 1a).** A bump is a second
   configuration write that changes `env_keys`, and it sits outside this pair's (B1)-(B4) and the one-line plan.
   The cold read is instead a 10-way concurrent coldphase, 2 prints per name, taken with no invoke between the apply
   and it. The apply recycles every environment; one stray client invoke warms at most one environment, so each name
   still gets a cold row from its pair. `coldphase_cold_names 5/5` proves it per name from the REPORT's
   `Init Duration`. If the read comes up short, AC5 refuses, and the bump goes to the CTO as its own paired act.
6. **The perturbation note:** CloudWatch shows a steady print stream roughly every 13 s from 05:57Z to 08:31Z, from
   another client. The warm pool is shared, so AC1/AC5 record rather than retry.

<status>complete</status>
<round>24</round>
<slot>~97</slot>
<fabric>site-z</fabric>
