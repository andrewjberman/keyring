#!/usr/bin/env python3
"""Battery for org/ref/SEAT_ROLES.json, lib/seat_roles.py and the launcher's hand-off (TO NFRA_CTLPLN.TO-CT-s-1).

WHAT IT PROVES
  1. validate passes on the real file, with every example serial below matching exactly ONE kind.
  2. kind_of resolves a serial of each kind, with and without a lane; unknown serials are UNKNOWN.
  3. For each of the eight kinds, `ajb <serial> -PrintPrompt` prints that kind's `is` sentence from the
     file character for character, between the watcher line and the existing role text.
  4. The old MSTR / COO / CRO "what I am" sentences are gone from the launcher text (no second statement).
  5. FALLBACK: in a SCRATCH COPY of lib/seat_roles.py + .tools/ajb.ps1 (the real files are never moved or
     edited) with the roles file absent, malformed, or carrying an unknown key, -PrintPrompt still prints
     the whole prompt plus the loud line `SEAT-ROLES: no statement for <serial> (...)`; a control copy WITH
     the file shows the statement, which proves the copy resolved its root to the scratch directory.
  6. -PrintPrompt launches nothing: a stub `claude.cmd` first on PATH leaves its marker file unwritten.

HOW THE LAUNCHER IS INVOKED: .tools/ajb.ps1 only DEFINES functions (it is dot-sourced from a profile), so
`powershell -File .tools/ajb.ps1 <serial> -PrintPrompt` would define and exit. The working invocation is
`powershell -NoProfile -ExecutionPolicy Bypass -File <driver.ps1>` where the driver sets OPAL_WS_ROOT, dot-sources
.tools/ajb.ps1 and calls `ajb <serial> -PrintPrompt`. One PowerShell process serves many serials.

Run: python .tools/tests/test_seat_roles_launcher.py     (exit 0 only when ok=True)
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.dont_write_bytecode = True

# one serial per kind for the launcher prompt check (lanes on purpose: '~' must survive the argument passing)
PROMPT_SERIALS = {
    "MSTR": "0.0.0_AB_MSTR~DELL1",
    "CTO": "1.0.0_SA_CTO",
    "COO": "2.0.0_SA_COO~C",
    "CVO": "3.0.0_SA_CVO~NFRA",
    "CRO": "4.0.0_SA_CRO",
    "CLOUDOPS": "0.7.0_AE_CloudOps~E",
    "TIER2": "0.4.0_DS_ClientPlatform~B",
    "WORKER": "0.9.0_WK_NFRA_CTLPLN~6",
}

# example serials, at least two per kind, with and without a lane
EXAMPLES = {
    "MSTR": ["0.0.0_AB_MSTR", "0.0.0_AB_MSTR~DELL1", "0.0.0_AB_MSTR~Z"],
    "CTO": ["1.0.0_SA_CTO", "1.0.0_SA_CTO~Z", "1.1.0_SA_CTO"],
    "COO": ["2.0.0_SA_COO", "2.0.0_SA_COO~C", "2.1.0_SA_COO"],
    "CVO": ["3.0.0_SA_CVO", "3.0.0_SA_CVO~NFRA", "3.1.0_SA_CVO"],
    "CRO": ["4.0.0_SA_CRO", "4.0.0_SA_CRO~B"],
    "CLOUDOPS": ["0.7.0_AE_CloudOps~E", "0.7.0_AE_CloudOps", "0.8.0_AE_CloudComp"],
    "TIER2": ["0.4.0_DS_ClientPlatform~B", "0.6.2_AE_PartnerETL~A", "0.5.0_DE_Foo", "0.3.0_DT_Bar",
              "0.2.0_RD_Baz", "0.7.0_AE_CloudOpsX", "0.9.0_AE_Cloud"],
    "WORKER": ["0.9.0_WK_NFRA_CTLPLN~6", "0.9.0_WK_NFRA_CTLPLN~1", "0.9.0_WK_LGIC_BLANKFIX~2"],
}
UNKNOWN_SERIALS = ["0.0.3_BG_BBGTerminal", "0.0.1_UA_Thing", "1.2.0_DS_CompLearns", "2.1.0_SC_CompLearns",
                   "FOO", "9.9.9_XX_YY"]


def _load_module(path):
    spec = importlib.util.spec_from_file_location("seat_roles_under_test", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _powershell():
    return shutil.which("powershell") or "powershell"


_DRIVER = (
    "param([string]$Root, [string]$SerialsCsv)\n"
    "$env:OPAL_WS_ROOT = $Root\n"
    ". (Join-Path $Root '.tools\\ajb.ps1')\n"
    "foreach ($s in ($SerialsCsv -split ',')) { Write-Output \"=====$s\"; ajb $s -PrintPrompt }\n"
)


def run_prompts(root, serials, work_dir, extra_path=None):
    """Run -PrintPrompt for each serial in ONE powershell process rooted at `root`. Returns {serial: text}."""
    driver = Path(work_dir) / "driver.ps1"
    driver.write_text(_DRIVER, encoding="ascii")
    env = dict(os.environ)
    env["OPAL_WS_ROOT"] = str(root)
    env.pop("WT_SESSION", None)
    if extra_path:
        env["PATH"] = str(extra_path) + os.pathsep + env.get("PATH", "")
    cmd = [_powershell(), "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(driver),
           "-Root", str(root), "-SerialsCsv", ",".join(serials)]
    proc = subprocess.run(cmd, capture_output=True, env=env, timeout=100)
    text = proc.stdout.decode("utf-8", "replace").replace("\r\n", "\n")
    out = {}
    for chunk in text.split("=====")[1:]:
        head, _, body = chunk.partition("\n")
        out[head.strip()] = body
    return out, proc.returncode


def main() -> int:
    mod = _load_module(ROOT / "lib" / "seat_roles.py")
    data = mod.load(ROOT / "org" / "ref" / "SEAT_ROLES.json")
    is_by_kind = {row["kind"]: row["is"] for row in data["kinds"]}
    notes = []

    # 1. validate, with every example serial checked against all patterns
    all_examples = [s for lst in EXAMPLES.values() for s in lst]
    problems, counts = mod.validate(all_examples, data=data)
    validate_ok = not problems and counts["kinds"] == 8
    notes.append("validate: kinds=%d examples=%d problems=%s" % (counts["kinds"], len(all_examples), problems))

    # 2. kind_of per kind, lane and no lane; unknowns; exclusivity fuzz on the AE namespace
    kinds_ok = set()
    for kind, serials in EXAMPLES.items():
        if all(mod.kind_of(s, data) == kind for s in serials):
            kinds_ok.add(kind)
        else:
            notes.append("kind_of FAIL for %s: %s" % (kind, [(s, mod.kind_of(s, data)) for s in serials]))
    unknown_ok = all(mod.kind_of(s, data) == mod.UNKNOWN for s in UNKNOWN_SERIALS)
    notes.append("unknown serials all UNKNOWN: %s" % unknown_ok)
    names = {"CloudOps", "CloudComp", "Cloud", "C", "", "CloudOpsX", "CloudCompX", "ClientPlatform"}
    for lit in ("CloudOps", "CloudComp"):
        for i in range(len(lit) + 1):
            names.add(lit[:i])
            for ch in "AXo":
                names.add(lit[:i] + ch + lit[i + 1:])
                names.add(lit[:i] + ch + lit[i:])
    fuzz_ok = True
    for name in sorted(names):
        serial = "0.7.0_AE_" + name
        got = mod.kind_of(serial, data)
        want = "CLOUDOPS" if name in ("CloudOps", "CloudComp") else "TIER2"
        if got != want:
            fuzz_ok = False
            notes.append("AE namespace fuzz FAIL: %s -> %s want %s" % (serial, got, want))
    notes.append("AE namespace fuzz (%d names, CLOUDOPS xor TIER2): %s" % (len(names), fuzz_ok))
    kinds_pass = len(kinds_ok) if (validate_ok and unknown_ok and fuzz_ok) else 0
    # the printed kinds count is the number of kinds whose examples all resolve, once validate also holds

    tmp_root = Path(tempfile.mkdtemp(prefix="seat_roles_test_"))
    try:
        # 3. the launcher prints each kind's `is` sentence, after the watcher line and before the role text
        prompts_ok = set()
        outs, rc = run_prompts(ROOT, list(PROMPT_SERIALS.values()), tmp_root)
        notes.append("real launcher -PrintPrompt rc=%s serials_printed=%d" % (rc, len(outs)))
        for kind, serial in PROMPT_SERIALS.items():
            text = outs.get(serial, "")
            i_watch = text.find("FIRST: run /watcher")
            i_stmt = text.find("SEAT STATEMENT [kind=%s]" % kind)
            i_is = text.find("Is: " + is_by_kind[kind])
            i_loop = text.find("Loop arming:")
            good = (rc == 0 and text.startswith(serial) and 0 <= i_watch < i_stmt < i_is < i_loop
                    and "SEAT-ROLES: no statement" not in text)
            if good:
                prompts_ok.add(kind)
            else:
                notes.append("prompt FAIL for %s (%s): positions watch=%d stmt=%d is=%d loop=%d"
                             % (kind, serial, i_watch, i_stmt, i_is, i_loop))

        # 4. the launcher no longer states what MSTR / the COO / the CRO is, a second time
        ajb_text = (ROOT / ".tools" / "ajb.ps1").read_text(encoding="utf-8")
        gone = ["device/fabric infra manager", "cross-device / cross-fabric comms", "coordinates and routes",
                "recon->specs"]
        still = [g for g in gone if g in ajb_text]
        gone_ok = not still
        notes.append("old role sentences gone from ajb.ps1: %s %s" % (gone_ok, still))

        # 5. fallback on a SCRATCH COPY of the three files; the real ones are not touched
        def build(name, with_file):
            base = tmp_root / name
            (base / ".tools").mkdir(parents=True)
            (base / "lib").mkdir()
            shutil.copy2(ROOT / ".tools" / "ajb.ps1", base / ".tools" / "ajb.ps1")
            shutil.copy2(ROOT / "lib" / "seat_roles.py", base / "lib" / "seat_roles.py")
            if with_file is not None:
                (base / "org" / "ref").mkdir(parents=True)
                (base / "org" / "ref" / "SEAT_ROLES.json").write_bytes(with_file)
            return base

        real_bytes = (ROOT / "org" / "ref" / "SEAT_ROLES.json").read_bytes()
        serial = PROMPT_SERIALS["MSTR"]
        control = build("control", real_bytes)
        c_out, _ = run_prompts(control, [serial], tmp_root)
        control_ok = "SEAT STATEMENT [kind=MSTR]" in c_out.get(serial, "")
        notes.append("fallback control (file present in scratch copy) shows statement: %s" % control_ok)
        fb_ok = control_ok
        variants = {
            "absent": None,
            "malformed": b"{ this is not json",
            "unknown_key": real_bytes.replace(b'"schema": "seat-roles/1",', b'"schema": "seat-roles/1", "extra": 1,'),
        }
        for name, content in variants.items():
            base = build("fb_" + name, content)
            f_out, f_rc = run_prompts(base, [serial], tmp_root)
            text = f_out.get(serial, "")
            loud = "SEAT-ROLES: no statement for %s (" % serial in text
            whole = (("\n" + serial + "\n") in ("\n" + text) and "FIRST: run /watcher" in text and "Loop arming:" in text
                     and "MSTR:" in text and "SEAT STATEMENT" not in text)
            this_ok = loud and whole and f_rc == 0
            fb_ok = fb_ok and this_ok
            reason = re.search(r"no statement for \S+ \((.*)\)", text)
            notes.append("fallback[%s]: loud=%s prompt_whole=%s rc=%s reason=%s"
                         % (name, loud, whole, f_rc, reason.group(1)[:80] if reason else None))
        if variants["unknown_key"] == real_bytes:
            fb_ok = False
            notes.append("fallback[unknown_key] variant was not built")

        # 6. -PrintPrompt launches nothing: stub claude first on PATH, marker must stay unwritten
        stub_dir = tmp_root / "stub"
        stub_dir.mkdir()
        marker = tmp_root / "claude_was_run.txt"
        (stub_dir / "claude.cmd").write_text("@echo off\r\necho run> \"%s\"\r\n" % marker, encoding="ascii")
        s_out, s_rc = run_prompts(ROOT, [PROMPT_SERIALS["WORKER"]], tmp_root, extra_path=stub_dir)
        nothing_ok = (not marker.exists()) and PROMPT_SERIALS["WORKER"] in s_out and s_rc == 0
        notes.append("-PrintPrompt with stub claude first on PATH: marker_written=%s rc=%s" % (marker.exists(), s_rc))
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)

    fb_final = bool(fb_ok)
    k_pass = kinds_pass
    p_pass = len(prompts_ok)
    ok = (k_pass == 8 and p_pass == 8 and fb_final and validate_ok and gone_ok and nothing_ok)
    for line in notes:
        print(line)
    print("SEAT-ROLES-TEST kinds=%d/8 prompts=%d/8 fallback_ok=%s ok=%s" % (k_pass, p_pass, fb_final, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
