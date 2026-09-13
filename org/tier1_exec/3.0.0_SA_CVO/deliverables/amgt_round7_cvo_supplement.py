"""Bounded read-only governance and portal evidence; no source mutation or checkout."""

import datetime
import importlib.util
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = "org/missions/D5/AMGT/AMGT_RESAPP"


def run(args):
    p = subprocess.run(
        args,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    return {"rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def rows(path):
    result = []
    for block in re.findall(
        r"```json\s*(.*?)```", path.read_text(encoding="utf-8"), re.S
    ):
        value = json.loads(block)
        result.extend(value if isinstance(value, list) else [value])
    return result


def main():
    intake = json.loads(
        (HOME / "AMGT_RESAPP_ROUND7_CVO_INTAKE_20260912_Z.json").read_text()
    )
    gate = module("gate7", ".tools/surprise-row-gate.py")
    toc = module("toc7", ".tools/to-check.py")
    result = {
        "utc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "head": run(["git", "rev-parse", "HEAD"]),
        "to_parser": {},
        "portal_sources": {},
    }
    for path in intake["task_orders"]:
        text = (ROOT / path).read_text(encoding="utf-8")
        raw = toc._extract_tag(text, "status")
        exact = re.findall(r"^\s*<status>([^<\r\n]+)</status>\s*$", text, re.M)
        result["to_parser"][path] = {
            "parser_status": raw,
            "classification": toc._classify_status(raw),
            "record_status": exact,
        }
    result["authoritative_orders"] = gate._open_tos_for_project(
        str(ROOT), "AMGT_RESAPP"
    )
    for path in [
        "src/pages/SecurityAnalysis/components/RankedChart.tsx",
        "src/pages/SecurityAnalysis/components/LeadPanel.tsx",
        "src/pages/SecurityAnalysis/tabs/ThesisTab.tsx",
        "src/pages/SecurityAnalysis/types.ts",
        "src/api/endpoints/amgt-lead-panel.ts",
    ]:
        result["portal_sources"][path] = run(
            ["git", "-C", "portal", "show", "83cc87f2:" + path]
        )
    result["portal_live_refs"] = run(
        [
            "git",
            "-C",
            "portal",
            "ls-remote",
            "origin",
            "refs/heads/DEV",
            "refs/heads/PROD",
        ]
    )
    result["portal_hygiene_descends_parent"] = run(
        ["git", "-C", "portal", "merge-base", "--is-ancestor", "c67281460a", "83cc87f2"]
    )
    result["round_drains_portal"] = run(
        [
            "git",
            "log",
            "--format=%H %s",
            "--raw",
            intake["pin"] + "^",
            "-20",
            "--",
            "portal",
        ]
    )
    result["prior_remedies"] = {
        p.relative_to(ROOT).as_posix(): rows(p)
        for p in (ROOT / PROJECT / "surprise-channel/remediations").glob(
            "REMEDIATION_v*.md"
        )
    }
    result["stamps"] = {
        p.name: json.loads(p.read_text())
        for p in (ROOT / PROJECT / "prd/stamps").glob("L*.r6.json")
    }
    result["prd_paths"] = run(
        ["git", "ls-tree", "-r", "--name-only", intake["pin"], "--", PROJECT + "/prd"]
    )
    target = HOME / "AMGT_RESAPP_ROUND7_CVO_SUPPLEMENT_20260912_Z.json"
    target.write_text(
        json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "path": str(target),
                "to_status": {
                    k: {
                        "classification": v["classification"],
                        "record_status": v["record_status"],
                    }
                    for k, v in result["to_parser"].items()
                },
                "orders": result["authoritative_orders"],
                "live_refs": result["portal_live_refs"],
                "stamps": result["stamps"],
                "prd_paths": result["prd_paths"],
            }
        )
    )
    for path, rr in result["prior_remedies"].items():
        for r in rr:
            if not r.get("closed"):
                print(
                    json.dumps(
                        {
                            "file": path,
                            "id": r["id"],
                            "owner": r.get("owner"),
                            "remedy": r.get("remedy"),
                        }
                    )
                )


if __name__ == "__main__":
    main()
