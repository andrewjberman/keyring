"""Reader proof for the device register (NFRA_CTLPLN FWD-2, contract C-REGISTRY).

Run: python org/devices/test_readers.py   (exit 0 = every check passed)

A box is added ONCE, to a fixture copy of org/devices/DEVICES.json (OPAL_DEVICE_REGISTER points every reader at it), and
every re-pointed reader must know it with no script edit: .tools/agentbus-sqs.sh (devices, device), .tools/remote-job.py
(parse_device) and .tools/sequence-check.py (Reader.box_fabric). NEGATIVE CONTROL: against the real register the same
box is refused by each reader, so a PASS cannot come from a reader that admits anything.
.tools/hooks/presence-stamp.sh is not run here (it writes the main checkout's presence stamp); it consumes only
`agentbus-sqs.sh device`, which is exercised below.
"""
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TOOLS = ROOT / ".tools"
NEW = "dell9"
NEW_QUEUE = "agentbus-ajbdev-fixture-to-dell9.fifo"


def load_tool(name, filename):
    spec = importlib.util.spec_from_file_location(name, str(TOOLS / filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def bash(args, env):
    sys.path.insert(0, str(TOOLS))
    import git_bash_resolver  # the estate's canonical Git Bash, never a bare `bash`
    r = subprocess.run(git_bash_resolver.bash_argv(str(TOOLS / "agentbus-sqs.sh"), *args), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=env, timeout=120)
    return r.returncode, r.stdout + r.stderr


def readers(register, results, expect_known):
    """Run every reader with OPAL_DEVICE_REGISTER=register; expect_known says whether NEW must be admitted."""
    env = dict(os.environ, OPAL_DEVICE_REGISTER=str(register))
    env.pop("AGENTBUS_DEVICE", None)
    tag = "fixture" if expect_known else "CONTROL real register"

    rc, out = bash(["devices"], env)
    listed = ("  %-8s -> " % NEW) in out and NEW_QUEUE in out
    results.append(("%s: agentbus-sqs.sh devices lists %s" % (tag, NEW), listed == expect_known, out[-300:]))

    rc, out = bash(["device"], dict(env, AGENTBUS_DEVICE=NEW))
    ok = (rc == 0 and ("device: %s" % NEW) in out and NEW_QUEUE in out) if expect_known else rc != 0
    results.append(("%s: agentbus-sqs.sh device with AGENTBUS_DEVICE=%s" % (tag, NEW), ok, "rc=%s %s" % (rc, out[-300:])))

    saved = os.environ.get("OPAL_DEVICE_REGISTER")
    os.environ["OPAL_DEVICE_REGISTER"] = str(register)
    try:
        rj = load_tool("remote_job_under_test", "remote-job.py")
        try:
            got = rj.parse_device("device: %s\n" % NEW, 0)
            ok = got == NEW
        except SystemExit:
            ok = False
        results.append(("%s: remote-job.py parse_device admits %s" % (tag, NEW), ok == expect_known, ""))

        os.environ["AGENTBUS_DEVICE"] = NEW
        sc = load_tool("sequence_check_under_test", "sequence-check.py")
        box, basis = sc.Reader(str(ROOT)).box_fabric()
        results.append(("%s: sequence-check.py box_fabric reads %s" % (tag, NEW), (box == NEW) == expect_known,
                        "%s (%s)" % (box, basis)))
    finally:
        os.environ.pop("AGENTBUS_DEVICE", None)
        if saved is None:
            os.environ.pop("OPAL_DEVICE_REGISTER", None)
        else:
            os.environ["OPAL_DEVICE_REGISTER"] = saved


def main():
    real = ROOT / "org" / "devices" / "DEVICES.json"
    reg = json.loads(real.read_text(encoding="utf-8"))
    reg["devices"].append({
        "name": NEW, "aliases": [], "role": "execution", "role_claim": "held", "inbound_queue": NEW_QUEUE,
        "inbound_queue_claim": "held", "seat_limit": {"execution_lanes": 1}, "seat_limit_claim": "held",
        "lane_letters": ["Q"], "lane_letters_default": False, "lane_letters_claim": "held"})
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        fixture = pathlib.Path(tmp) / "DEVICES.json"
        fixture.write_text(json.dumps(reg, indent=2), encoding="utf-8")
        readers(fixture, results, expect_known=True)
    readers(real, results, expect_known=False)
    fails = 0
    for name, ok, detail in results:
        print("%s: %s" % ("PASS" if ok else "FAIL", name))
        if not ok:
            fails += 1
            print("      " + detail.replace("\n", "\n      "))
    print("RESULT: %d passed, %d failed (of %d)" % (len(results) - fails, fails, len(results)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
