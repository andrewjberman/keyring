#!/usr/bin/env python3
"""Round-21 check-step device key (NFRA_CTLPLN CT-ak-1, FWD-19 and FWD-15 laptop arm).

--device  the check step (org/devices/intake/intake_check.py) run on a tiny synthetic wheel in a temporary intake folder.
          The fetch-shaped record that the check module writes for that wheel (its write_fetch_record, the one place the
          check module writes an intake-fetch/1 record) must carry device=laptop (from AGENTBUS_DEVICE). The downloads
          reader (org/devices/intake/intake_request.py downloads) counts that record for laptop and never for dell1, with
          unattributed=0. A box that cannot be named writes device null, and the reader counts that record as unattributed.
          No network: the holding, records, site, signer and Security Center stand-in are all temporary folders and files.

Last line: CHECK-DEVICE arms=<k>/<n> ok=<True|False>
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
INTAKE = os.path.join(REPO, "org", "devices", "intake")
CHECK = os.path.join(INTAKE, "intake_check.py")
REQUEST = os.path.join(INTAKE, "intake_request.py")
sys.path.insert(0, INTAKE)
import intake_check as ic  # noqa: E402  (stdlib-only module beside this file; imported for its fixture writer)

SERIAL = "0.9.0_WK_NFRA_CTLPLN~116"
DEVICE = "laptop"
OTHER = "dell1"
BATCH = "rt21-a"
NO_DEVICE_BATCH = "rt21-b"
NO_SUCH_REG_KEY = "HKCU\\Software\\OpalRound21NoSuchKey"
GOOD_AV = [{"displayName": "Synthetic Antivirus (stand-in)", "productState": 266240}]
APPROVED_LINE = "%s==%s" % (ic.SYN_NAME, ic.SYN_VERSION)
SIGNER_TEXT = "I have read checks 1 to 7 for batch %s and sign file %s\n\nCHECK 8 SIGNED -- round-21 test signer\n"


def last_line(text):
    lines = [x for x in text.splitlines() if x.strip()]
    return lines[-1] if lines else ""


def read_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_or_none(path):
    try:
        return read_json(path)
    except (OSError, ValueError):
        return None


class World:
    """A temporary intake world: root/holding, records, an empty site folder, a stand-in AV answer, a signer folder."""

    def __init__(self, tmp):
        self.tmp = tmp
        self.root = os.path.join(tmp, "root")
        self.intake = os.path.join(tmp, "intake")
        self.records = os.path.join(self.intake, "records")
        self.site = os.path.join(tmp, "site")
        self.signer = os.path.join(tmp, "signer")
        for d in (self.root, self.records, self.site, self.signer):
            os.makedirs(d)
        self.av = os.path.join(tmp, "av.json")
        with open(self.av, "w", encoding="ascii") as fh:
            json.dump(GOOD_AV, fh)
        self.approved = os.path.join(tmp, "approved.txt")
        with open(self.approved, "w", encoding="ascii") as fh:
            fh.write(APPROVED_LINE + "\n")

    def cfg(self):
        return ic.Cfg(root=self.root, records=self.records, av_json=self.av, sites=[self.site], signer_dir=self.signer)

    def env(self, device):
        e = dict(os.environ)
        e.update({"OPAL_INTAKE_ROOT": self.root, "OPAL_INTAKE_RECORDS": self.records, "OPAL_INTAKE_AV_JSON": self.av,
                  "OPAL_INTAKE_SITE": self.site, "OPAL_INTAKE_SIGNER_DIR": self.signer, "OPAL_AGENT_SERIAL": SERIAL,
                  "AGENTBUS_DEVICE": device})
        return e

    def make_wheel(self, batch):
        hold = os.path.join(self.root, "holding", batch)
        os.makedirs(hold)
        path = os.path.join(hold, ic.syn_file_name())
        ic.build_synthetic_wheel(path)
        return path

    def signature(self, batch, file_name):
        p = os.path.join(self.signer, "signature_%s_%s.txt" % (batch, file_name))
        with open(p, "w", encoding="ascii") as fh:
            fh.write(SIGNER_TEXT % (batch, file_name))
        return p


def run_check(world, batch, file_name, device):
    cmd = [sys.executable, CHECK, "check", "--batch", batch, "--file", file_name, "--approved-by", world.approved,
           "--signed-by", world.signature(batch, file_name), "--scan-wait-seconds", "0"]
    p = subprocess.run(cmd, capture_output=True, text=True, env=world.env(device), timeout=200, stdin=subprocess.DEVNULL)
    return p.returncode, p.stdout


def run_downloads(world, device, day):
    cmd = [sys.executable, REQUEST, "downloads", "--device", device, "--day", day, "--root", world.intake]
    p = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ), timeout=120, stdin=subprocess.DEVNULL)
    return p.returncode, last_line(p.stdout)


def device_arms():
    tmp = tempfile.mkdtemp(prefix="round21_check_device_")
    results = []
    saved = {k: os.environ.get(k) for k in ("AGENTBUS_DEVICE", "AGENTBUS_REG_KEY")}

    def arm(label, ok):
        results.append(bool(ok))
        print("ARM %-2d %s %s" % (len(results), "PASS" if ok else "FAIL", label))

    try:
        world = World(tmp)
        os.environ["AGENTBUS_DEVICE"] = DEVICE
        os.environ.pop("AGENTBUS_REG_KEY", None)
        wheel = world.make_wheel(BATCH)
        file_name = os.path.basename(wheel)
        fetched = ic.write_fetch_record(world.cfg(), BATCH, wheel)
        day = fetched["at"][:10].replace("-", "")
        rec_path = os.path.join(world.records, BATCH, file_name + ".fetch.json")
        disk = load_or_none(rec_path)

        rc, out = run_check(world, BATCH, file_name, DEVICE)
        arm("the check step (intake_check.py check) on the synthetic wheel reads verdict=checked",
            rc == 0 and last_line(out).endswith("verdict=checked"))
        arm("the fetch-shaped record the check module writes carries device=%s and keeps schema intake-fetch/1" % DEVICE,
            disk is not None and disk.get("device") == DEVICE and disk.get("schema") == "intake-fetch/1")

        rc_l, line_l = run_downloads(world, DEVICE, day)
        arm("downloads %s %s: the record counted (files=1), unattributed=0" % (DEVICE, day),
            rc_l == 0 and line_l == "DOWNLOADS-TODAY device=%s day=%s requests=0 files=1 unattributed=0" % (DEVICE, day))
        rc_o, line_o = run_downloads(world, OTHER, day)
        arm("downloads %s %s: the record is not counted for another box (files=0)" % (OTHER, day),
            rc_o == 0 and line_o == "DOWNLOADS-TODAY device=%s day=%s requests=0 files=0 unattributed=0" % (OTHER, day))

        # a box that cannot be named: the check module's fetch-shaped record carries device null, never a guessed box
        os.environ["AGENTBUS_DEVICE"] = ""
        os.environ["AGENTBUS_REG_KEY"] = NO_SUCH_REG_KEY
        wheel2 = world.make_wheel(NO_DEVICE_BATCH)
        ic.write_fetch_record(world.cfg(), NO_DEVICE_BATCH, wheel2)
        disk2 = load_or_none(os.path.join(world.records, NO_DEVICE_BATCH, file_name + ".fetch.json"))
        arm("a fetch-shaped record written on an unnamed box carries device null",
            disk2 is not None and "device" in disk2 and disk2["device"] is None)
        rc_3, line_3 = run_downloads(world, DEVICE, day)
        arm("downloads %s %s after the unnamed record: files=1 still, unattributed=1" % (DEVICE, day),
            rc_3 == 0 and line_3 == "DOWNLOADS-TODAY device=%s day=%s requests=0 files=1 unattributed=1" % (DEVICE, day))
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(tmp, ignore_errors=True)
    k, n = sum(results), len(results)
    return k, n, k == n


def main(argv):
    if "--device" in argv:
        k, n, ok = device_arms()
        print("CHECK-DEVICE arms=%d/%d ok=%s" % (k, n, ok))
        return 0 if ok else 1
    print("usage: test_round21_check_device.py --device", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
