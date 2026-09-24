#!/usr/bin/env python3
"""drive-mode -- the MODE LEASE: which driver runs a project right now (report 2 C1, Andrew-approved 2026-09-24).

FAST = Andrew is present; the project's seat builds directly under /closer-drive.
FULL = the default; /canonical-drive runs. HOLD = both drivers pause.
A lease is a device-local marker, org/mcp/drive_mode/<CODE>.json, in the MAIN worktree. It FAILS CLOSED TO FULL:
absent, expired or unreadable reads FULL, so a forgotten FAST lapses by itself. Every arm, end, hold and lapse
appends one line to org/mcp/drive-mode.log (committed with the seat's record batch; that line is the record).

Presence: a live lease extends to 30 minutes past the newest stamp in org/mcp/presence/*.last (epoch seconds, written
by a UserPromptSubmit hook when installed). Without the hook the lease runs its stated length.
Rail (call 6): `read` run BY THE LEASE'S SEAT mirrors a live FAST lease into that session's /freeform marker
(org/mcp/sessions/<sid>.freeform, expiry = the lease's), so the comp-tool rail stands down for the lease's life.
The one refusal: `arm` refuses a surface that overlaps another live FAST lease or another project's open task
order `<paths>` (a project under HOLD excluded). Resolve by `hold` on the other, or a narrower --surface.

  drive-mode.py arm <CODE> --surface <dir> [--surface <dir>...] [--hours 2] [--seat <serial>] [--by <who>]
  drive-mode.py full <CODE> | hold <CODE> [--hours 2] | read <CODE> | status | --self-test
"""
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys

TERMINAL = {"complete", "superseded", "cancelled", "canceled", "withdrawn", "retired", "closed"}
PRESENCE_GRACE = 30 * 60
PATH_LINE = re.compile(r"^[A-Za-z0-9_.][A-Za-z0-9_./*?\-~{},\[\]]*$")  # a path or glob; prose never matches


def main_root():
    try:
        common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                capture_output=True, text=True, check=True).stdout.strip()
        return os.path.dirname(common)
    except Exception:  # noqa: BLE001
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ROOT = main_root()
LEASES = os.path.join(ROOT, "org", "mcp", "drive_mode")
LOG = os.path.join(ROOT, "org", "mcp", "drive-mode.log")
PRESENCE = os.path.join(ROOT, "org", "mcp", "presence")
SESSIONS = os.path.join(ROOT, "org", "mcp", "sessions")


def now():
    return int(dt.datetime.now(dt.timezone.utc).timestamp())


def iso(epoch):
    return dt.datetime.fromtimestamp(epoch, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(line):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write("%s %s\n" % (iso(now()), line))


def lease_path(code):
    return os.path.join(LEASES, "%s.json" % code)


def presence_last():
    """Newest epoch-seconds stamp; a value in the future (malformed, e.g. an ISO string read as digits) is skipped
    so one bad stamp cannot hold a lease open overnight (0.0.0_AB_MSTR msg 100756)."""
    best, ceiling = 0, now() + 300
    for f in glob.glob(os.path.join(PRESENCE, "*.last")):
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                raw = fh.read().strip()
            val = int(raw) if raw.isdigit() else 0
        except Exception:  # noqa: BLE001
            continue
        if val <= ceiling:
            best = max(best, val)
    return best


def load(code, t=None):
    """The live lease, extended by presence and persisted; None (= FULL) when absent, unreadable or lapsed."""
    t = now() if t is None else t
    p = lease_path(code)
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            lease = json.load(fh)
        exp = int(lease["expires_epoch"])
    except FileNotFoundError:
        return None
    except Exception:  # noqa: BLE001
        return None  # unreadable reads FULL
    ext = max(exp, presence_last() + PRESENCE_GRACE)
    if ext <= t:
        os.remove(p)
        log("LAPSE %s mode=%s seat=%s (expired %s)" % (code, lease.get("mode"), lease.get("seat"), iso(ext)))
        return None
    if ext != exp:
        lease["expires_epoch"], lease["expires_at"] = ext, iso(ext)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(lease, fh, indent=1)
    return lease


def all_live():
    out = []
    for f in sorted(glob.glob(os.path.join(LEASES, "*.json"))):
        lease = load(os.path.basename(f)[:-5])
        if lease:
            out.append(lease)
    return out


def _prefix(path):
    p = path.strip().replace("\\", "/")
    p = re.split(r"[*?\[]", p, maxsplit=1)[0]
    return p.rstrip("/")


def overlaps(a, b):
    a, b = _prefix(a), _prefix(b)
    if not a or not b:
        return True
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def project_home(code):
    hits = glob.glob(os.path.join(ROOT, "org", "missions", "D*", "*", code))
    return hits[0] if hits else None


def open_orders(skip_codes):
    """(code, order file, [paths]) for every non-terminal task order, projects in skip_codes excluded."""
    out = []
    for f in glob.glob(os.path.join(ROOT, "org", "missions", "D*", "*", "*", "task-orders", "*.md")):
        code = os.path.basename(os.path.dirname(os.path.dirname(f)))
        if code in skip_codes:
            continue
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except Exception:  # noqa: BLE001
            continue
        st = re.search(r"<status>\s*([A-Za-z_-]+)", text)
        if st and st.group(1).lower() in TERMINAL:
            continue
        blk = re.search(r"^<paths>\s*$(.*?)^</paths>", text, re.M | re.S)
        lines = [ln.strip().lstrip("-").strip().strip("`") for ln in blk.group(1).splitlines()] if blk else []
        paths = [ln for ln in lines if PATH_LINE.match(ln)]
        out.append((code, os.path.relpath(f, ROOT).replace("\\", "/"), paths))
    return out


def conflicts(code, surfaces, live=None, orders=None):
    live = all_live() if live is None else live
    held = {x["code"] for x in live if x.get("mode") == "HOLD"}
    hits = []
    for x in live:
        if x["code"] != code and x.get("mode") == "FAST":
            for s in surfaces:
                for o in x.get("surface", []):
                    if overlaps(s, o):
                        hits.append("live FAST lease %s (seat %s) surface %s" % (x["code"], x.get("seat"), o))
    orders = open_orders(held | {code}) if orders is None else orders
    for ocode, f, paths in orders:
        for s in surfaces:
            for p in paths:
                if overlaps(s, p):
                    hits.append("open order %s <paths> %s" % (f, p))
    return sorted(set(hits))


def caller_serial():
    s = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    if not s and sid:
        try:
            with open(os.path.join(SESSIONS, sid + ".serial"), encoding="utf-8", errors="replace") as fh:
                s = fh.read().strip()
        except Exception:  # noqa: BLE001
            pass
    return s, sid


def sync_rail(lease):
    """Mirror a live FAST lease into THIS session's freeform marker when the caller IS the lease's seat."""
    serial, sid = caller_serial()
    if not (lease and lease.get("mode") == "FAST" and sid and serial == lease.get("seat")):
        return None
    ff = os.path.join(SESSIONS, sid + ".freeform")
    exp = int(lease["expires_epoch"])
    try:
        with open(ff, encoding="utf-8", errors="replace") as fh:
            cur = int(re.sub(r"\D", "", fh.read()) or 0)
    except Exception:  # noqa: BLE001
        cur = 0
    if abs(cur - exp) > 60:
        os.makedirs(SESSIONS, exist_ok=True)
        with open(ff, "w", encoding="utf-8") as fh:
            fh.write("%d\n" % exp)
        with open(os.path.join(ROOT, "org", "mcp", "comp-tool-hud.log"), "a", encoding="utf-8") as fh:
            fh.write("%s  FREEFORM-ARM  sid=%s  FAST lease %s  expires=%d\n" % (iso(now()), sid, lease["code"], exp))
    return exp


def claims(lease):
    p = os.path.join(ROOT, lease.get("status_path", ""))
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except Exception:  # noqa: BLE001
        return "(no STATUS.md at %s)" % lease.get("status_path")
    m = re.search(r"^## (?:Write claims|Claims)\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return (m.group(1).strip() if m else "(no claims section)")[:600]


def arm(code, mode, surfaces, hours, seat, by):
    if mode == "FAST":
        if not surfaces:
            print("drive-mode: REFUSED -- a FAST lease names its surface (--surface <dir>)", file=sys.stderr)
            return 2
        if not seat:
            print("drive-mode: REFUSED -- no seat (--seat <serial>, or OPAL_AGENT_SERIAL)", file=sys.stderr)
            return 2
        hits = conflicts(code, surfaces)
        if hits:
            print("drive-mode: REFUSED -- %s surface already has a driver:" % code, file=sys.stderr)
            for h in hits:
                print("  " + h, file=sys.stderr)
            print("  resolve: `drive-mode.py hold <OTHER>` or a narrower --surface", file=sys.stderr)
            return 1
    home = project_home(code)
    t = now()
    exp = t + int(hours * 3600)
    lease = {"code": code, "mode": mode, "seat": seat, "surface": surfaces, "armed_by": by,
             "armed_at": iso(t), "expires_at": iso(exp), "expires_epoch": exp,
             "status_path": os.path.relpath(os.path.join(home, "STATUS.md"), ROOT).replace("\\", "/") if home else ""}
    os.makedirs(LEASES, exist_ok=True)
    with open(lease_path(code), "w", encoding="utf-8") as fh:
        json.dump(lease, fh, indent=1)
    log("%s %s seat=%s surface=%s expires=%s by=%s" % ("ARM" if mode == "FAST" else "HOLD", code, seat,
                                                      ",".join(surfaces) or "-", iso(exp), by))
    print("%s %s: seat %s, surface %s, until %s" % (mode, code, seat, ",".join(surfaces) or "-", iso(exp)))
    return 0


def end(code, by):
    lease = load(code)
    if not lease:
        print("FULL %s (no live lease)" % code)
        return 0
    os.remove(lease_path(code))
    for sf in glob.glob(os.path.join(SESSIONS, "*.freeform")):
        try:
            with open(sf, encoding="utf-8", errors="replace") as fh:
                val = int(re.sub(r"\D", "", fh.read()) or 0)
            if val == int(lease["expires_epoch"]):
                os.remove(sf)  # only markers this lease wrote (same expiry); an Andrew /freeform survives
        except Exception:  # noqa: BLE001
            continue
    log("END %s mode=%s seat=%s by=%s" % (code, lease.get("mode"), lease.get("seat"), by))
    print("FULL %s (ended %s lease)" % (code, lease.get("mode")))
    return 0


def status():
    live = all_live()
    print("DRIVE-MODE STATUS %s | live leases: %d (absent = FULL)" % (iso(now()), len(live)))
    for x in live:
        print("  %s %s seat=%s surface=%s until %s" % (x["mode"], x["code"], x.get("seat"),
                                                       ",".join(x.get("surface", [])) or "-", x["expires_at"]))
        if x["mode"] == "FAST":
            print("    claims: " + claims(x).replace("\n", "\n            "))
            for h in conflicts(x["code"], x.get("surface", []), live):
                print("    OVERLAP: " + h)
    return 0


def self_test():
    global ROOT, LEASES, LOG, PRESENCE, SESSIONS
    import tempfile
    ok = True

    def check(name, cond):
        nonlocal ok
        ok = ok and bool(cond)
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    with tempfile.TemporaryDirectory() as tmp:
        ROOT = tmp
        LEASES, LOG = os.path.join(tmp, "org/mcp/drive_mode"), os.path.join(tmp, "org/mcp/drive-mode.log")
        PRESENCE, SESSIONS = os.path.join(tmp, "org/mcp/presence"), os.path.join(tmp, "org/mcp/sessions")
        tod = os.path.join(tmp, "org/missions/D9/M/OTHER_P/task-orders")
        os.makedirs(tod)
        with open(os.path.join(tod, "OTHER_P.TO-1.x.md"), "w") as fh:
            fh.write("<status>pending</status>\n<paths>\nportal/src/pages/Other/a.tsx\n</paths>\n")
        with open(os.path.join(tod, "OTHER_P.TO-2.x.md"), "w") as fh:
            fh.write("<status>complete</status>\n<paths>\nportal/src/pages/Done/\n</paths>\n")
        check("absent lease reads FULL", load("A_X") is None)
        check("arm FAST on a free surface", arm("A_X", "FAST", ["portal/src/pages/Mine"], 2, "S~1", "t") == 0)
        check("live lease reads FAST", (load("A_X") or {}).get("mode") == "FAST")
        check("second FAST on an overlapping surface REFUSED",
              arm("B_X", "FAST", ["portal/src/pages/Mine/tabs"], 2, "S~2", "t") == 1)
        check("FAST over another project's OPEN order REFUSED",
              arm("C_X", "FAST", ["portal/src/pages/Other"], 2, "S~3", "t") == 1)
        check("FAST over a COMPLETE order admitted", arm("D_X", "FAST", ["portal/src/pages/Done"], 2, "S~4", "t") == 0)
        check("HOLD on the other project releases its orders",
              arm("OTHER_P", "HOLD", [], 2, "-", "t") == 0 and not conflicts("C_X", ["portal/src/pages/Other"]))
        check("prefix is component-bounded (mine vs mine-too)", not overlaps("portal/src/mine", "portal/src/mine-too"))
        with open(lease_path("A_X")) as fh:
            lz = json.load(fh)
        lz["expires_epoch"] = now() - 5
        with open(lease_path("A_X"), "w") as fh:
            json.dump(lz, fh)
        check("expired lease LAPSES to FULL and logs it",
              load("A_X") is None and "LAPSE A_X" in open(LOG, encoding="utf-8", errors="replace").read())
        with open(lease_path("D_X")) as fh:
            lz = json.load(fh)
        lz["expires_epoch"] = now() - 5
        with open(lease_path("D_X"), "w") as fh:
            json.dump(lz, fh)
        os.makedirs(PRESENCE)
        with open(os.path.join(PRESENCE, "dev.last"), "w") as fh:
            fh.write(str(now() - 60))
        with open(os.path.join(PRESENCE, "bad.last"), "w") as fh:
            fh.write("2026-09-24T15:46:19Z")
        with open(os.path.join(PRESENCE, "future.last"), "w") as fh:
            fh.write(str(now() + 86400))
        check("an ISO or future stamp is skipped (MSTR 100756)", abs(presence_last() - (now() - 60)) <= 2)
        got = load("D_X")
        check("fresh presence EXTENDS an expired-by-clock lease", got and got["expires_epoch"] >= now() + 1700)
        with open(lease_path("C_X"), "w") as fh:
            fh.write("{not json")
        check("unreadable lease reads FULL (fail-closed)", load("C_X") is None)
        os.environ["OPAL_AGENT_SERIAL"], os.environ["CLAUDE_CODE_SESSION_ID"] = "S~4", "sid-test"
        exp = sync_rail(load("D_X"))
        ff = os.path.join(SESSIONS, "sid-test.freeform")
        check("the lease's own seat gets its freeform marker", exp and open(ff).read().strip() == str(exp))
        os.environ["OPAL_AGENT_SERIAL"] = "S~9"
        check("another seat gets NO marker", sync_rail(load("D_X")) is None)
        end("D_X", "t")
        check("END removes the lease and the marker it wrote", load("D_X") is None and not os.path.exists(ff))
    print("SELF-TEST: %s" % ("ALL HOLD" if ok else "BROKEN"))
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--self-test":
        return self_test()
    cmd = argv[0]
    if cmd == "status":
        return status()
    if len(argv) < 2:
        print(__doc__)
        return 2
    code, rest = argv[1], argv[2:]
    surfaces, hours, seat, by = [], 2.0, caller_serial()[0], caller_serial()[0] or "operator"
    i = 0
    while i < len(rest):
        k = rest[i]
        v = rest[i + 1] if i + 1 < len(rest) else ""
        if k == "--surface":
            surfaces.append(v.rstrip("/"))
        elif k == "--hours":
            hours = float(v)
        elif k == "--seat":
            seat = v
        elif k == "--by":
            by = v
        else:
            print("drive-mode: unknown argument %s" % k, file=sys.stderr)
            return 2
        i += 2
    if cmd in ("arm", "fast"):
        return arm(code, "FAST", surfaces, hours, seat, by)
    if cmd == "hold":
        return arm(code, "HOLD", surfaces, hours, seat or "-", by)
    if cmd in ("full", "end"):
        return end(code, by)
    if cmd == "read":
        lease = load(code)
        mode = lease["mode"] if lease else "FULL"
        rail = sync_rail(lease)
        print("%s %s%s%s" % (mode, code, " until %s" % lease["expires_at"] if lease else "",
                             " (rail stood down for this session)" if rail else ""))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
