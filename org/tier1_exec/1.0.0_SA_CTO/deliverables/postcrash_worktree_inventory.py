"""Post-crash worktree inventory: one row per linked worktree, measured, no disposition."""
import json
import subprocess
import sys

ROOT = r"C:\Users\Opal Bloomberg\Desktop\ajb_workspace"
TRUNK = "CLOUD"


def git(*args, cwd=ROOT):
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, p.stdout.strip(), p.stderr.strip()


rc, out, err = git("worktree", "list", "--porcelain")
if rc != 0:
    sys.exit("ERROR: worktree list rc=%d %s" % (rc, err))

trees, cur = [], {}
for line in out.splitlines() + [""]:
    if not line:
        if cur:
            trees.append(cur)
        cur = {}
        continue
    k, _, v = line.partition(" ")
    cur[k] = v or True

rows = []
for t in trees:
    path = t["worktree"]
    if path.replace("\\", "/").rstrip("/").lower() == ROOT.replace("\\", "/").lower():
        continue
    branch = t.get("branch", "").replace("refs/heads/", "") or "(detached)"
    head = t.get("HEAD", "")
    rc, st, _ = git("status", "--porcelain", "--untracked-files=normal", cwd=path)
    status_ok = rc == 0
    lines = [ln for ln in st.splitlines() if ln and not ln.endswith(" portal") and ln[3:] != "portal"]
    tracked_dirty = [ln for ln in lines if not ln.startswith("??")]
    untracked = [ln for ln in lines if ln.startswith("??")]
    # commits on HEAD not reachable from trunk, and of those, patch-unique ones
    _, ahead, _ = git("rev-list", "--count", "%s..%s" % (TRUNK, head))
    _, cherry, _ = git("cherry", TRUNK, head)
    unique = sum(1 for ln in cherry.splitlines() if ln.startswith("+"))
    _, last, _ = git("log", "-1", "--format=%ad|%an", "--date=format-local:%m-%d %H:%M", head)
    rows.append({
        "path": path, "branch": branch, "head": head[:10],
        "last_commit": last.split("|")[0], "last_author": last.split("|")[-1],
        "ahead_of_trunk": int(ahead or 0), "patch_unique": unique,
        "tracked_dirty": len(tracked_dirty), "untracked": len(untracked),
        "status_readable": status_ok, "prunable": bool(t.get("prunable")),
        "dirty_sample": (tracked_dirty + untracked)[:4],
    })

rows.sort(key=lambda r: (r["patch_unique"] == 0 and r["tracked_dirty"] == 0, r["path"]))
print(json.dumps({"trunk": TRUNK, "denominator": len(rows), "rows": rows}, indent=1))
