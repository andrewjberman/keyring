"""D0_TIGHTENING TO-1 -- T1-3 EXERCISE: the listener survives its parent seat's death.

Exercised, never reasoned about. A simulated "seat" process launches the broker, then the
seat is killed with the SAME recursive-ParentProcessId tree kill that .tools/kill-agent.ps1
uses (Stop-ProcessTree, :126-133). The broker must still answer /health afterwards.

MUTANT CONTROL: the identical scenario with the PRE-FIX spawn (plain Popen +
DETACHED_PROCESS) must KILL the broker. Without that leg, a green result here would be
consistent with a kill that simply never worked.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

WS = Path(__file__).resolve().parents[2]  # org/mcp/X.py -> workspace root
BROKER = WS / "org" / "mcp" / "broker.py"
RESULTS: list[tuple[str, str, str]] = []

CNPG = 0x00000200
DETACHED = 0x00000008


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def health(port, timeout=20.0):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.25)
    return False


def alive(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as r:
            return r.status == 200
    except Exception:
        return False


def tree_kill(pid):
    """Byte-for-byte the recursive ParentProcessId descent kill-agent.ps1 performs."""
    ps = (
        "function Stop-ProcessTree { param([int]$RootPid)"
        " $children=@(Get-CimInstance Win32_Process -Filter \"ParentProcessId=$RootPid\""
        " -ErrorAction SilentlyContinue);"
        " foreach($c in $children){ Stop-ProcessTree -RootPid $c.ProcessId };"
        " Stop-Process -Id $RootPid -Force -ErrorAction SilentlyContinue }"
        f" Stop-ProcessTree -RootPid {pid}"
    )
    subprocess.run(["powershell.exe", "-NoProfile", "-Command", ps],
                   capture_output=True, text=True)


def run_case(label, seat_code, port, db, expect_survive):
    env = dict(os.environ)
    env["OPAL_BROKER_PORT"] = str(port)
    env["OPAL_BROKER_DB"] = str(db)
    seat = subprocess.Popen([sys.executable, "-c", seat_code], env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not health(port):
        seat.kill()
        rec(label, False, f"broker never came up on {port} -- case INCONCLUSIVE, not a result")
        return
    print(f"    ({label}) broker up on {port}; seat pid={seat.pid}. Tree-killing the seat...")
    tree_kill(seat.pid)
    time.sleep(3.0)
    survived = alive(port)
    ok = (survived == expect_survive)
    rec(label, ok,
        f"after the seat tree-kill the broker is {'ALIVE' if survived else 'DEAD'} "
        f"(expected {'ALIVE' if expect_survive else 'DEAD'})")
    # cleanup
    if survived:
        # Reap the surviving scratch broker by PORT OWNER. It deliberately has no live
        # parent link now (that is the property under test), so a tree walk cannot find
        # it -- the port is the only handle left, which is the point.
        subprocess.run(["powershell.exe", "-NoProfile", "-Command",
                        f"$c=Get-NetTCPConnection -LocalPort {port} -State Listen "
                        f"-ErrorAction SilentlyContinue; if($c){{ Stop-Process -Id "
                        f"$c.OwningProcess -Force -ErrorAction SilentlyContinue }}"],
                       capture_output=True)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="t1listen_"))
    print("=" * 78)
    print("T1-3 EXERCISE -- listener survives parent seat death")
    print("=" * 78)

    # --- CASE 1: the FIXED spawn (double-spawn; intermediate exits) ---
    launcher = (
        "import subprocess,sys;"
        "subprocess.Popen([sys.executable, {brk!r}],"
        "creationflags=0x00000200|0x00000008,"
        "stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)"
    ).format(brk=str(BROKER))
    seat_fixed = (
        "import subprocess,sys,time;"
        f"m=subprocess.Popen([sys.executable,'-c',{launcher!r}],"
        "creationflags=0x00000200|0x00000008,"
        "stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL);"
        "m.wait(timeout=15);"
        "time.sleep(300)"
    )
    print("\n-- CASE 1: FIXED spawn (double-spawn, the T1-3 build) --")
    run_case("T1-3-FIXED", seat_fixed, 7921, tmp / "f.db", expect_survive=True)

    # --- CASE 2: MUTANT CONTROL -- the pre-fix spawn ---
    seat_old = (
        "import subprocess,sys,time;"
        f"subprocess.Popen([sys.executable,{str(BROKER)!r}],"
        "creationflags=0x00000200|0x00000008,"
        "stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL);"
        "time.sleep(300)"
    )
    print("\n-- CASE 2: MUTANT CONTROL -- pre-fix spawn (Popen + DETACHED_PROCESS) --")
    run_case("T1-3-MUTANT", seat_old, 7922, tmp / "o.db", expect_survive=False)

    print("\n" + "=" * 78)
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print(f"T1-3 BATTERY: {n}/{len(RESULTS)} PASS (denominator {len(RESULTS)})")
    print("  T1-3-FIXED  = the listener survives the seat kill (the acceptance leg)")
    print("  T1-3-MUTANT = the OLD spawn DIES to the same kill; without this the")
    print("                FIXED result would be consistent with a kill that never worked")
    print("=" * 78)
    return 0 if n == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
