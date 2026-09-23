"""Exercise the issued suite filter against real bounded Bun runs, without portal edits."""

from pathlib import Path
import json
import subprocess

root = Path.cwd()
out = root / ".runtime/codex-seats/3.0.0_SA_CVO~F/r14-filter"
out.mkdir(parents=True, exist_ok=True)
tests = {
    "pass": "import {test,expect} from 'bun:test'; test('CVO positive',()=>expect(1).toBe(1));",
    "unexpected": "import {test,expect} from 'bun:test'; test('CVO unexpected',()=>expect(1).toBe(2));",
    "known": "import {test,expect} from 'bun:test'; test('F81-AC3/AC4 synthetic known',()=>expect(1).toBe(2));",
    "timeout": "import {test} from 'bun:test'; test('CVO incomplete',async()=>{await new Promise(r=>setTimeout(r,10000));},20000);",
}
rows = []
for name, body in tests.items():
    f = out / (name + ".test.ts")
    f.write_text(body, encoding="utf-8")
    # Exact filter from the amended orders. Save the otherwise-discarded producer exit code.
    script = """#!/usr/bin/env bash
NO_COLOR=1 timeout TIMEOUT /c/Users/AndrewBerman/.bun/bin/bun test TEST > LOG 2>&1
producer_rc=$?
sed -r 's/\\x1b\\[[0-9;]*m//g' LOG > CLEAN
UNEXPECTED=$(grep "^\u2717" CLEAN | grep -vc "F81-AC3/AC4")
echo "PRODUCER_RC=$producer_rc"
echo "UNEXPECTED-FAIL-COUNT=$UNEXPECTED"
"""
    for key, value in {
        "TIMEOUT": "1" if name == "timeout" else "30",
        "TEST": f.as_posix(),
        "LOG": (out / (name + ".raw.log")).as_posix(),
        "CLEAN": (out / (name + ".clean.log")).as_posix(),
    }.items():
        script = script.replace(key, "'" + value + "'")
    s = out / (name + ".sh")
    s.write_text(script, encoding="utf-8", newline="\n")
    p = subprocess.run(
        ["C:/Program Files/Git/bin/bash.exe", str(s)],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=40,
    )
    rows.append(
        {
            "case": name,
            "wrapperRC": p.returncode,
            "output": p.stdout,
            "stderr": p.stderr,
            "raw": (out / (name + ".raw.log")).read_text(
                encoding="utf-8", errors="replace"
            ),
        }
    )
(out / "result.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
print(json.dumps(rows, indent=2))
