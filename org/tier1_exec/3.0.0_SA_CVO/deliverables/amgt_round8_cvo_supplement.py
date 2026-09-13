"""Bounded source/remote controls for the round-8 clock advances."""

import datetime
import hashlib
import json
from amgt_round8_cvo_intake import ROOT, HOME, PROJECT, records, run

evidence = json.loads(
    (HOME / "AMGT_RESAPP_ROUND8_CVO_EVIDENCE_20260913_Z.json").read_text()
)
pin = run(["git", "rev-parse", "HEAD"])["stdout"].strip()
out = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "pin": pin}
out["portal_remote_ancestry"] = {}
for line in evidence["portal"]["remote_heads"]["stdout"].splitlines():
    sha, ref = line.split()
    out["portal_remote_ancestry"][ref] = {
        "sha": sha,
        "rc": run(
            ["git", "-C", "portal", "merge-base", "--is-ancestor", "a845a8be75", sha]
        )["rc"],
    }
out["portal_anchors"] = run(
    [
        "git",
        "-C",
        "portal",
        "for-each-ref",
        "--contains=a845a8be75",
        "--format=%(refname)",
    ]
)
source_paths = [
    PROJECT + "/decompositions/AMGT_RESAPP_DECOMP.md",
    ".claude/skills/canonical-flow/SKILL.md",
    "infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf",
    "org/tier1_exec/4.0.0_SA_CRO/deliverables/HARVEST_CONSUMER_CHECK_MAP_20260913_Z.md",
]
out["sources"] = {
    p: {
        "sha256": hashlib.sha256((ROOT / p).read_bytes()).hexdigest(),
        "text": (ROOT / p).read_text(encoding="utf-8"),
    }
    for p in source_paths
}
out["preserved_worktrees"] = {}
for name in ["wk-amgt-8-1", "wk-amgt-8-2", "wk-amgt-7-2"]:
    path = "C:/tmp/" + name
    out["preserved_worktrees"][path] = {
        "exists": __import__("pathlib").Path(path).is_dir(),
        "top_level": run(["git", "-C", path, "rev-parse", "--show-toplevel"]),
    }
out["all_originals"] = [
    dict(r, source=PROJECT + "/surprise-channel/investigations/INVESTIGATION_v1.md")
    for r in records(
        (
            ROOT / PROJECT / "surprise-channel/investigations/INVESTIGATION_v1.md"
        ).read_text(encoding="utf-8")
    )
]
out["limits"] = (
    "No owner stand-down or termination. No worker worktree edits. Nine remote heads listed at evidence read; ancestry rc1 means not contained, rc128 would mean unknown. Source map coverage does not establish applied resources or zero estate-wide executable checks."
)
(HOME / "AMGT_RESAPP_ROUND8_CVO_SUPPLEMENT_20260913_Z.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8"
)
print(
    json.dumps(
        {
            "remote": out["portal_remote_ancestry"],
            "anchors": out["portal_anchors"]["stdout"],
            "original_count": len(out["all_originals"]),
            "worktrees": {
                p: v["exists"] for p, v in out["preserved_worktrees"].items()
            },
        }
    )
)
