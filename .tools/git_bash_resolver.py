"""
Canonical python->bash resolver for the Windows fabric. Import this; never invoke bare `bash`.

THE CLASS this closes (CLAUDE.md git-section "a python/powershell-spawned bash inherits the wrong
resolution"): a python (or PowerShell) subprocess invoking bare `bash` / `/bin/bash` gets WINDOWS PATH
resolution, which finds the System32 WSL stub (C:\\Windows\\System32\\bash.exe) BEFORE Git Bash. WSL isn't
configured on this host, so it fails -- `execvpe(/bin/bash) failed: No such file or directory` -- silently,
from python. (From a Git Bash SHELL, /bin/bash IS Git Bash and works; the bug only bites a
python/powershell-spawned bash, which is why it hides from interactive testing.)

FIX: resolve the ABSOLUTE Git-for-Windows bash.exe and pass it to subprocess. An absolute path launches
that exe directly, bypassing PATH resolution -- context-independent (python / PowerShell / anywhere).
Precedent: .tools/aws exists for the analogous MSYS path-mangling class.

Usage:
    from git_bash_resolver import git_bash
    bash = git_bash()
    if bash:
        subprocess.run([bash, "some-script.sh", ...])   # NOT ["bash", ...] and NOT ["/bin/bash", ...]
    # else: no Git Bash found -- fail loudly; do NOT fall back to bare 'bash'.

Self-test: `python .tools/git_bash_resolver.py` -> resolves + runs `bash -c 'echo ok'`.

First caught + fixed 2026-07-19 (CTO exec-exercise of audit-archive-invoker: python->safe-commit.sh hit
the WSL stub, execvpe(/bin/bash) failed). Extracted from the invoker to close the class estate-wide
(CTO-authorized follow-on). Owner: 0.7.0_AE_CloudOps. CLAUDE.md git-section pointer: CTO's gate.
"""
from __future__ import annotations

import shutil
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def git_bash() -> str | None:
    """Absolute path to the Git-for-Windows bash.exe, or None if not found. NEVER returns bare 'bash'
    (that Windows-resolves to the System32 WSL stub). Prefers known install locations; falls back to
    deriving from the git executable on PATH (e.g. <root>\\mingw64\\bin\\git.exe -> <root>\\usr\\bin\\bash.exe)."""
    for c in (r"C:\Program Files\Git\usr\bin\bash.exe",
              r"C:\Program Files\Git\bin\bash.exe",
              r"C:\Program Files (x86)\Git\usr\bin\bash.exe"):
        if Path(c).is_file():
            return c
    git = shutil.which("git")
    if git:
        for anc in Path(git).resolve().parents:
            for rel in ("usr/bin/bash.exe", "bin/bash.exe"):
                b = anc / rel
                if b.is_file():
                    return str(b)
    return None


def bash_argv(script: str, *args: str) -> list[str]:
    """Convenience: [git_bash(), script, *args] for subprocess.run. Raises if no Git Bash is found --
    fail loudly rather than let a caller degrade to bare 'bash' (the WSL-stub trap)."""
    bash = git_bash()
    if not bash:
        raise RuntimeError("no Git Bash found; refusing to fall back to bare 'bash' (WSL-stub trap)")
    return [bash, script, *args]


if __name__ == "__main__":
    import subprocess
    import sys
    b = git_bash()
    if not b:
        print("git_bash: NOT FOUND (bare 'bash' would resolve to the System32 WSL stub)", file=sys.stderr)
        sys.exit(1)
    r = subprocess.run([b, "-c", "echo ok"], capture_output=True, text=True)
    ok = r.returncode == 0 and "ok" in r.stdout
    print(f"git_bash -> {b}")
    print(f"self-test: {'PASS' if ok else 'FAIL'} {(r.stderr or '').strip()}")
    sys.exit(0 if ok else 1)
