#!/usr/bin/env python3
"""test_wk_sparse_provision.py -- CT-ag-2: a worker worktree is a SPARSE checkout by default.

Arms (a)-(g) run .tools/wk-provision.sh on a temporary repository that mimics the layout
(.tools/, lib/, org/missions/D0/X/CODE/task-orders/, infra/, docs/, a root file and a nested
portal repository). Standard library only; no AWS, no network.

--real additionally provisions a REAL sparse worktree of THIS repository for the already-merged
order NFRA_CTLPLN.TO-CT-af-2 (--order that file), runs that cell's test inside it, prints the
SPARSE-REAL line and removes the worktree and its branches in a finally.

Usage: python .tools/tests/test_wk_sparse_provision.py [--real]
"""
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash` (the WSL stub)

SCRIPT = TOOLS / "wk-provision.sh"
CODE = "PROJX"
PROJ_DIR = "org/missions/D0/NFRA/PROJX"
REAL_CODE = "NFRA_CTLPLN"
REAL_ORDER = "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-af-2.round-close-check-decomp-round-scope.md"
REAL_CELL_TEST = ".tools/tests/test_round_close_decomp_round.py"
DISK_FLOOR_GB = 12

ORDER_B = """# TO PROJX.TO-b fixture
<paths>
infra/aws/x/main.tf
</paths>
"""
ORDER_E = """# TO PROJX.TO-e fixture
<paths>
infra/aws/nope/absent.tf
</paths>
"""


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def bash(cwd, *args):
    return subprocess.run(git_bash_resolver.bash_argv(str(SCRIPT), *args), cwd=str(cwd),
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def rm_tree(path):
    def _fix(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(str(path), onerror=_fix)


def build_repo(base):
    repo = Path(base) / "super"
    repo.mkdir(parents=True)
    git(repo, "init", "-q", "-b", "main")
    for key, val in (("user.email", "wk-sparse-test@invalid"), ("user.name", "wk-sparse-test"),
                     ("core.autocrlf", "false")):
        git(repo, "config", key, val)
    portal = repo / "portal"
    portal.mkdir()
    git(portal, "init", "-q", "-b", "main")
    for key, val in (("user.email", "wk-sparse-test@invalid"), ("user.name", "wk-sparse-test")):
        git(portal, "config", key, val)
    write(portal / "package.json", '{"name": "portal"}\n')
    git(portal, "add", "-A")
    git(portal, "commit", "-q", "-m", "portal init")
    write(repo / ".tools" / "marker.txt", "tools\n")
    write(repo / "lib" / "common.py", "X = 1\n")
    write(repo / "root.txt", "root\n")
    write(repo / PROJ_DIR / "task-orders" / "PROJX.TO-b.md", ORDER_B)
    write(repo / PROJ_DIR / "task-orders" / "PROJX.TO-e.md", ORDER_E)
    write(repo / "infra" / "aws" / "x" / "main.tf", "# tf\n")
    write(repo / "docs" / "readme.md", "docs\n")
    write(repo / "org" / "ref" / "SEAT_ROLES.json", "{}\n")  # the base set carries org/ref (W105-S2)
    git(repo, "add", "-A")  # git records the portal repository as a gitlink
    p = git(repo, "commit", "-q", "-m", "fixture init")
    if p.returncode != 0:
        raise RuntimeError("fixture commit failed: " + p.stderr)
    return repo


def check(name, ok, detail):
    print("%s  %s  (%s)" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def run_arms(base):
    repo = build_repo(base)
    arms = []
    wt = {k: Path(base) / ("wt-" + k) for k in "abcdefg"}
    o_b = repo / PROJ_DIR / "task-orders" / "PROJX.TO-b.md"
    o_e = repo / PROJ_DIR / "task-orders" / "PROJX.TO-e.md"

    # (a) default provision: base set only
    p = bash(repo, "provision", CODE, "a", "--path", str(wt["a"]))
    a_ok = (p.returncode == 0 and (wt["a"] / ".tools" / "marker.txt").is_file()
            and (wt["a"] / "lib" / "common.py").is_file()
            and (wt["a"] / PROJ_DIR / "task-orders" / "PROJX.TO-b.md").is_file()
            and (wt["a"] / "org" / "ref" / "SEAT_ROLES.json").is_file()
            and not (wt["a"] / "infra").exists() and not (wt["a"] / "docs").exists())
    arms.append(check("a default provision: .tools, lib, org/ref, project folder present; infra and docs absent", a_ok,
                      "rc=%d infra=%s docs=%s org_ref=%s" % (p.returncode, (wt["a"] / "infra").exists(),
                                                             (wt["a"] / "docs").exists(),
                                                             (wt["a"] / "org" / "ref" / "SEAT_ROLES.json").is_file())))

    # (b) --order naming a path under infra/aws/x/
    p = bash(repo, "provision", CODE, "b", "--path", str(wt["b"]), "--order", str(o_b))
    b_ok = (p.returncode == 0 and (wt["b"] / "infra" / "aws" / "x" / "main.tf").is_file()
            and not (wt["b"] / "docs").exists())
    arms.append(check("b --order infra/aws/x: that folder present, docs absent", b_ok,
                      "rc=%d main.tf=%s docs=%s" % (p.returncode,
                                                    (wt["b"] / "infra" / "aws" / "x" / "main.tf").is_file(),
                                                    (wt["b"] / "docs").exists())))

    # (c) --full "reason": everything checked out, reason printed
    p = bash(repo, "provision", CODE, "c", "--path", str(wt["c"]), "--full", "reason")
    c_ok = (p.returncode == 0 and (wt["c"] / "docs" / "readme.md").is_file()
            and (wt["c"] / "infra" / "aws" / "x" / "main.tf").is_file()
            and "mode=full reason=reason" in p.stdout)
    arms.append(check("c --full reason: all checked out, prints mode=full reason=reason", c_ok,
                      "rc=%d docs=%s line=%s" % (p.returncode, (wt["c"] / "docs").exists(),
                                                 [ln for ln in p.stdout.splitlines() if "PROVISIONED" in ln])))

    # (d) --full "" refused rc 2, nothing created
    p = bash(repo, "provision", CODE, "d", "--path", str(wt["d"]), "--full", "")
    branch_d = git(repo, "branch", "--list", "wk-%s-d" % CODE).stdout.strip()
    d_ok = p.returncode == 2 and not wt["d"].exists() and branch_d == ""
    arms.append(check("d --full empty refused rc 2 before anything is created", d_ok,
                      "rc=%d path_exists=%s branch=%r" % (p.returncode, wt["d"].exists(), branch_d)))

    # (e) --order path absent at HEAD: printed as skipped, no failure
    p = bash(repo, "provision", CODE, "e", "--path", str(wt["e"]), "--order", str(o_e))
    e_ok = (p.returncode == 0 and "SKIPPED" in p.stdout and "infra/aws/nope/absent.tf" in p.stdout
            and wt["e"].is_dir())
    arms.append(check("e --order path absent at HEAD printed as SKIPPED, does not fail", e_ok,
                      "rc=%d skipped_line=%s" % (p.returncode,
                                                 [ln for ln in p.stdout.splitlines() if "SKIPPED" in ln])))

    # (f) plain git commit inside the sparse worktree lands and moves the branch tip
    f_ok = False
    f_detail = "provision rc unknown"
    p = bash(repo, "provision", CODE, "f", "--path", str(wt["f"]))
    if p.returncode == 0:
        before = git(wt["f"], "rev-parse", "HEAD").stdout.strip()
        target = wt["f"] / PROJ_DIR / "task-orders" / "PROJX.TO-f-note.md"
        write(target, "sparse commit\n")
        g1 = git(wt["f"], "add", "--", PROJ_DIR + "/task-orders/PROJX.TO-f-note.md")
        g2 = git(wt["f"], "commit", "-q", "-m", "arm f: sparse commit")
        after = git(wt["f"], "rev-parse", "HEAD").stdout.strip()
        tip = git(repo, "rev-parse", "wk-%s-f" % CODE).stdout.strip()
        f_ok = (g1.returncode == 0 and g2.returncode == 0 and after != before and tip == after)
        f_detail = "add=%d commit=%d moved=%s tip=%s" % (g1.returncode, g2.returncode, after != before,
                                                         tip == after)
    arms.append(check("f plain git commit in the sparse worktree lands and moves the branch tip", f_ok, f_detail))

    # (g) remove still tears a sparse worktree down
    p = bash(repo, "provision", CODE, "g", "--path", str(wt["g"]))
    g_ok = False
    g_detail = "provision rc=%d" % p.returncode
    if p.returncode == 0:
        r = bash(repo, "remove", str(wt["g"]))
        listing = git(repo, "worktree", "list", "--porcelain").stdout
        gone = ("worktree %s" % wt["g"].as_posix()) not in listing.replace("\\", "/")
        g_ok = r.returncode == 0 and not wt["g"].exists() and gone
        g_detail = "remove rc=%d path_exists=%s registered=%s" % (r.returncode, wt["g"].exists(), not gone)
    arms.append(check("g remove <path> removes the sparse worktree and its registration", g_ok, g_detail))

    return arms


def ls_tree_blob_sizes(cwd):
    sizes = {}
    out = git(cwd, "ls-tree", "-r", "-l", "HEAD").stdout
    for line in out.splitlines():
        meta, _, path = line.partition("\t")
        fields = meta.split()
        if len(fields) >= 4 and fields[1] == "blob":
            sizes[path] = int(fields[3])
    return sizes


def checked_out_stats(wt):
    """(files, bytes) of the tracked files PRESENT in a worktree: ls-files H entries, sizes from HEAD's blobs."""
    sizes = ls_tree_blob_sizes(wt)
    present = [ln[2:] for ln in git(wt, "ls-files", "-t").stdout.splitlines() if ln.startswith("H ")]
    present = [p for p in present if p in sizes]
    return len(present), sum(sizes[p] for p in present)


def real_arm():
    """Provision a real sparse worktree of THIS repository; return the SPARSE-REAL line and green flag."""
    free_gb = shutil.disk_usage("C:/").free / (1024.0 ** 3)
    if free_gb < DISK_FLOOR_GB:
        print("SKIP --real: C: has %.1f GB free, below the %d GB floor" % (free_gb, DISK_FLOOR_GB))
        return None, False
    print("disk: C: %.1f GB free (floor %d GB)" % (free_gb, DISK_FLOOR_GB))
    main = git(REPO, "worktree", "list", "--porcelain").stdout.splitlines()[0].split(" ", 1)[1]
    tmp = tempfile.mkdtemp(prefix="wksparse-real-")
    wt = Path(tmp) / "sparse"
    n = "real-%d" % os.getpid()
    branch = "wk-%s-%s" % (REAL_CODE, n)
    line = "SPARSE-REAL tracked_bytes_sparse=0 tracked_bytes_full=0 ratio=0.00 du_sparse=n/a green=False"
    green = False
    try:
        p = bash(REPO, "provision", REAL_CODE, n, "--path", str(wt), "--order", str(REPO / REAL_ORDER))
        print(p.stdout.rstrip())
        if p.stderr.strip():
            print(p.stderr.rstrip())
        if p.returncode != 0 or not wt.is_dir():
            print("ERROR: real provision failed rc=%d" % p.returncode)
            return line, False
        t = subprocess.run([sys.executable, REAL_CELL_TEST], cwd=str(wt), capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        out_lines = [ln for ln in t.stdout.splitlines() if ln.strip()]
        last = out_lines[-1] if out_lines else ""
        print("CELL TEST rc=%d last=%s" % (t.returncode, last))
        green = bool(last) and last.split()[-1] == "ok=True"
        sparse_files, sparse_bytes = checked_out_stats(wt)
        full_sizes = ls_tree_blob_sizes(REPO)
        full_bytes = sum(full_sizes.values())
        ratio = (float(sparse_bytes) / float(full_bytes)) if full_bytes else 0.0
        du = subprocess.run([git_bash_resolver.git_bash(), "-c", "du -sh '%s'" % wt.as_posix()],
                            capture_output=True, text=True, encoding="utf-8", errors="replace")
        du_h = du.stdout.split()[0] if du.stdout.split() else "n/a"
        line = "SPARSE-REAL tracked_bytes_sparse=%d tracked_bytes_full=%d ratio=%.2f du_sparse=%s green=%s" % (
            sparse_bytes, full_bytes, ratio, du_h, green)
        print("sparse files=%d" % sparse_files)
        return line, green
    finally:
        if wt.exists():
            bash(REPO, "remove", str(wt))
        if wt.exists():
            git(REPO, "worktree", "remove", "--force", str(wt))
        git(REPO, "branch", "-D", branch)
        git(Path(main) / "portal", "branch", "-D", branch + "-portal")
        if Path(tmp).exists():
            rm_tree(tmp)


def main(argv):
    want_real = "--real" in argv
    base = tempfile.mkdtemp(prefix="wksparse-arms-")
    try:
        arms = run_arms(base)
    finally:
        rm_tree(base)
    k = sum(1 for ok in arms if ok)
    n = len(arms)
    arms_ok = k == n
    print("WK-SPARSE-PROVISION arms=%d/%d ok=%s" % (k, n, arms_ok))
    if not want_real:
        return 0 if arms_ok else 1
    line, green = real_arm()
    if line is not None:
        print(line)
    return 0 if (arms_ok and green) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
