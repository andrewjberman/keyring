"""Independent bounded artifact reads. No network, deploy, or source mutation."""

import ast
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
P = ROOT / "org/missions/D5/AMGT/AMGT_RESAPP"
B = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W"
W17 = P / "deliverables/0.9.0_WK_AMGT_RESAPP~17"
W16 = P / "deliverables/0.9.0_WK_AMGT_RESAPP~16"
V = Path("C:/tmp/portal-resapp-view")


def git(*args):
    p = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return {"rc": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip()}


def payload(path):
    x = json.loads(path.read_text(encoding="utf-8-sig"))
    b = x.get("body", x)
    return x, json.loads(b) if isinstance(b, str) else b


def main():
    a = {
        "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "head": git("rev-parse", "HEAD"),
        "instrument": "Local source, saved response/log artifacts and a controlled actual-component render; no new live AWS or browser request.",
        "hashes": {},
    }
    files = (
        list(B.glob("ROUND10*"))
        + list(B.glob("adapter-local*.json"))
        + list(W17.glob("ri*"))
        + list(W16.glob("*.json"))
    )
    files += [
        ROOT / "infra/aws/terraform/harvest/s3.tf",
        ROOT / "lib/research/api/scoped_amgt.py",
        V / "src/pages/SecurityAnalysis/tabs/ThesisTab.tsx",
        V / "src/pages/SecurityAnalysis/components/RankedList.tsx",
    ]
    for p in files:
        if p.is_file():
            a["hashes"][str(p)] = {
                "bytes": p.stat().st_size,
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            }
    a["portal"] = {
        "head": git("-C", str(V), "rev-parse", "HEAD"),
        "status": git("-C", str(V), "status", "--porcelain"),
        "gitlink": git("ls-files", "-s", "portal"),
        "diff_from_round9": git(
            "-C", str(V), "diff", "--name-only", "a845a8be75", "HEAD", "--", "src/"
        ),
    }
    a["drain_ancestry"] = {
        pin: git("merge-base", "--is-ancestor", pin, "HEAD")
        for pin in ["672bca64fe", "5c95c00268", "50064d78f5", "8da6d27866"]
    }
    a["bucket"] = {
        "head": git("show", "HEAD:infra/aws/terraform/harvest/s3.tf"),
        "status": git(
            "status", "--porcelain", "--", "infra/aws/terraform/harvest/s3.tf"
        ),
        "commit": git(
            "log", "-1", "--format=%H %an", "--", "infra/aws/terraform/harvest/s3.tf"
        ),
    }
    before = set((W17 / "ri4.routes.before.txt").read_text().splitlines()) - {""}
    after = set((W17 / "ri4.routes.after.txt").read_text().splitlines()) - {""}
    a["routes"] = {
        "before": len(before),
        "after": len(after),
        "lost": sorted(before - after),
        "added": sorted(after - before),
        "amgt_after": sum("/api/scoped/amgt/" in x for x in after),
    }
    a["plans_and_applies"] = {}
    for name in ["ri2.plan.txt", "ri2.apply.txt", "ri4.plan.txt", "ri4.apply.txt"]:
        txt = (W17 / name).read_text(encoding="utf-8-sig")
        a["plans_and_applies"][name] = {
            "lines": len(txt.splitlines()),
            "summaries": re.findall(r"(?:Plan:|Apply complete!)[^\n]+", txt),
            "bucket_address_mentions": txt.count("aws_s3_bucket.harvest"),
            "create_addresses": re.findall(r"^\s*# (.*?) will be created", txt, re.M),
            "update_addresses": re.findall(
                r"^\s*# (.*?) will be updated in-place", txt, re.M
            ),
            "destroying": txt.count("Destroying..."),
            "destroyed": txt.count("Destruction complete"),
        }
    browser, local = payload(
        B / "adapter-local.rankings.trending.chatter.2026-09-12.json"
    )
    live, today = payload(W16 / "rankings.trending.chatter.response.2026-09-15.json")
    a["ranking_comparison"] = {
        "browser_day": local.get("as_of_date"),
        "deployed_day": today.get("as_of_date"),
        "same_payload": local == today,
        "browser_rows": len(local["rows"]),
        "deployed_rows": len(today["rows"]),
        "same_ticker_sequence": [r["ticker"] for r in local["rows"]]
        == [r["ticker"] for r in today["rows"]],
        "browser_rows_with_security_key": sum(
            "security_key" in r for r in local["rows"]
        ),
        "deployed_rows_with_security_key": sum(
            "security_key" in r for r in today["rows"]
        ),
        "same_axis": local["axis"] == today["axis"],
        "same_resolution": local["resolution"] == today["resolution"],
        "browser_computed_at": sorted(
            {r.get("computed_at", "") for r in local["rows"]}
        ),
        "deployed_computed_at": sorted(
            {r.get("computed_at", "") for r in today["rows"]}
        ),
    }
    a["saved_adapter_responses"] = {}
    for p in [
        B / "adapter-local.thesis.BABA_US.json",
        B / "adapter-local.thesis.BABA_US_Equity.json",
        W17 / "ri4.ev.out.json",
        W17 / "ri4.ev-nofirm.out.json",
    ]:
        env, b = payload(p)
        a["saved_adapter_responses"][p.name] = {
            "statusCode": env.get("statusCode"),
            "keys": list(b),
            "header_figures": len(b.get("header_figures", [])),
            "fiscal_figures": len(b.get("fiscal_year_figures", [])),
            "check_face": len(b.get("check_face", [])),
            "drafted_sections": len(b.get("drafted_sections", [])),
            "row_count": b.get("row_count"),
            "reason": b.get("reason"),
        }
    # Compute the declared source closure independently. Do not run the uploader.
    paths = {ROOT / "infra/aws/lambda/research/scoped_amgt_api/lambda_function.py"}
    for package in ["api", "metrics", "checkface", "rules", "watchlist"]:
        paths.update(
            p
            for p in (ROOT / "lib/research" / package).rglob("*.py")
            if not {"tests", "__pycache__"} & set(p.parts)
        )
    seed = set(paths)

    def resolve(module):
        stem = ROOT / Path(*module.split("."))
        for p in [stem.with_suffix(".py"), stem / "__init__.py"]:
            if p.exists():
                return p

    def required(ps):
        found = set()
        for p in ps:
            for node in ast.walk(ast.parse(p.read_text(encoding="utf-8-sig"))):
                names = []
                if isinstance(node, ast.Import):
                    names = [x.name for x in node.names]
                if isinstance(node, ast.ImportFrom):
                    if node.level:
                        package = list(p.parent.relative_to(ROOT).parts)
                        prefix = ".".join(package[: len(package) - node.level + 1])
                        module = prefix + ("." + node.module if node.module else "")
                    else:
                        module = node.module or ""
                    names = [module] + [module + "." + x.name for x in node.names]
                for name in names:
                    if name.startswith("lib.research"):
                        q = resolve(name)
                        if q:
                            found.add(q)
        return found

    while True:
        expanded = paths | required(paths)
        for p in list(expanded):
            for parent in p.parents:
                if parent == ROOT:
                    break
                init = parent / "__init__.py"
                if init.exists():
                    expanded.add(init)
        if expanded == paths:
            break
        paths = expanded
    a["source_closure"] = {
        "seed": len(seed),
        "closure": len(paths),
        "added": sorted(p.relative_to(ROOT).as_posix() for p in paths - seed),
        "required_modules": len(required(paths)),
        "missing": sorted(str(p) for p in required(paths) - paths),
        "seed_missing_control": sorted(
            p.relative_to(ROOT).as_posix() for p in required(seed) - seed
        ),
        "limit": "Source AST closure, not a fresh read of the deployed ZIP; dynamic imports and non-Python assets are outside this declared criterion.",
    }
    for name, cmd in [
        (
            "BOUNDARY",
            [
                "node",
                str(
                    V / "src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs"
                ),
            ],
        ),
        ("PROSE", ["node", str(HOME / "AMGT_RESAPP_ROUND10_CVO_PROSE_20260915_W.cjs")]),
    ]:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        suffix = "txt" if name == "BOUNDARY" else "json"
        (HOME / f"AMGT_RESAPP_ROUND10_CVO_{name}_20260915_W.{suffix}").write_text(
            p.stdout, encoding="utf-8"
        )
        a[name.lower()] = {"rc": p.returncode, "stderr": p.stderr}
    OUT = Path(__file__).with_suffix(".json")
    OUT.write_text(json.dumps(a, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {k: v for k, v in a.items() if k not in ["hashes", "bucket"]}, indent=2
        )
    )


if __name__ == "__main__":
    main()
