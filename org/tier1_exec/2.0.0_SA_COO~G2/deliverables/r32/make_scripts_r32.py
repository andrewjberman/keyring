"""Derive the four release-32 host scripts from the release-31 set (the r31 method, shifted one release). Writes four files; runs nothing.

usage: python -I make_scripts_r32.py <r31 scripts dir> <dst dir> <extracted r32 root> <extracted r31 root> <r32 tarball> <r32 package SHA256SUMS file>

The r31 scripts are verified by sha256 first. The member sets are read from the two extracted trees (never typed): the members whose bytes
differ between release 31 and release 32, and the members release 32 adds, are the member checks. Every substitution names its exact text
and its count; any other count REFUSES. ASCII only. Nothing is uploaded, installed, applied or run.
"""
import hashlib
import os
import sys

SRC, DST, X32, X31, TAR, PKGSUMS = sys.argv[1:7]
SUMS = "SHA256SUMS"
BINDINGS = "reports/resident_bindings.json"
SRC_SHA = {
    "pre_read_r31.sh": "608ef22db839267e3e463ece83a9875f5063b536cb3fdb6e7b7f6aaf274442e0",
    "install_r31.sh": "855681b628cb88932c5340d9abb0beae5bf5f7646a27b9553142b2286bbd3d35",
    "rollback_r31.sh": "9c38440a3286b07ba30d111fec3ce8bee5f260d90384f31fcf69b740a2dbceab",
    "resident_host_install_0485393f3a-r31.sh": "6f5590899dc64b2371e7dd04a21de386e15e33ce955420ec4b0083c673611987",
}
LIB = "a1c2880169c5f7996cc7c5880e4fe36db90f0a2c1f5a1cd01e0d1d8153544841"
WRAP = "55ddb8f7947cba7cdca1b9139d4d0a1a3ad620e330c86ba3ab648d334763aff9"
R31_TAR = "22193944345ce2dd52d2b732ce0ac8d569aa2359958601686239b7e1da8e6021"


def sha_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def refuse(why):
    raise SystemExit("REFUSE: " + why)


def walk(root):
    names = []
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            names.append(os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/"))
    return sorted(names)


def load(name):
    with open(os.path.join(SRC, name), "rb") as fh:
        return fh.read().decode("ascii")


def write(name, text):
    if any(ord(c) > 127 for c in text):
        refuse("%s: non-ASCII" % name)
    if not text.endswith("\n"):
        text += "\n"
    path = os.path.join(DST, name)
    with open(path, "wb") as fh:
        fh.write(text.encode("ascii"))
    print("wrote %s bytes=%d sha256=%s" % (name, os.path.getsize(path), sha_file(path)))
    return path


def rep(text, old, new, count=1):
    got = text.count(old)
    if got != count:
        refuse("%d matches (want %d) for %r" % (got, count, old[:100]))
    return text.replace(old, new)


def rep_line(text, prefix, new_lines, count=1):
    """Replace every line that starts with `prefix` (exactly `count` of them) by `new_lines`."""
    lines = text.split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.startswith(prefix)]
    if len(hits) != count:
        refuse("%d lines start with %r, want %d" % (len(hits), prefix[:80], count))
    out = []
    for i, ln in enumerate(lines):
        out.extend(new_lines if i in hits else [ln])
    return "\n".join(out)


for _name, _want in SRC_SHA.items():
    if sha_file(os.path.join(SRC, _name)) != _want:
        refuse("source %s sha256 is not the release-31 script" % _name)
n32, n31 = walk(X32), walk(X31)
R32 = {n: sha_file(os.path.join(X32, *n.split("/"))) for n in n32}
R31 = {n: sha_file(os.path.join(X31, *n.split("/"))) for n in n31}
if sha_file(TAR) == R31_TAR:
    refuse("the tarball is the r31 tarball")
ONLY32 = sorted(set(n32) - set(n31))
ONLY31 = sorted(set(n31) - set(n32))
if ONLY31:
    refuse("members only in r31: %s" % ONLY31)
DIFF = sorted(n for n in n32 if n in R31 and R32[n] != R31[n])
for must in (SUMS, BINDINGS):
    if must not in DIFF:
        refuse("%s does not differ" % must)
PKG_DIFF = [n for n in DIFF if n not in (SUMS, BINDINGS)]
CHECKED = sorted(set(DIFF) | set(ONLY32))
TAR_SHA = sha_file(TAR)
SUMS_SHA = R32[SUMS]
if sha_file(PKGSUMS) != SUMS_SHA:
    refuse("the staged package sums file is not the tarball's SHA256SUMS member")
if R32["ycharts-host/ycharts_session.js"] != LIB or R32["ycharts-host/run-ycharts-session.sh"] != WRAP:
    refuse("the capture library or wrapper moved; this derivation assumes they did not")
PKG_COUNT = len(n32) - 1  # the package's own sums list every member but SHA256SUMS itself
WORKER = R32["ycharts/generate/resident_worker.py"]
WORKER31 = R31["ycharts/generate/resident_worker.py"]
LEDGER_OLD, LEDGER_NEW = "irpt-resident-r31-20261014", "irpt-resident-r32-20261015"
checks_lines = ['check "%s" %s' % (n, R32[n]) for n in CHECKED]


def entries(names, table, indent="  "):
    out = ["for ent in \\"]
    for i, n in enumerate(names):
        out.append('%s"%s %s"%s' % (indent, n, table[n], "; do" if i == len(names) - 1 else " \\"))
    return out


# ---------------------------------------------------------------- host script
host = load("resident_host_install_0485393f3a-r31.sh")
host = rep(host, "NEW=0485393f3a-r31\nOLD=0485393f3a-r29\n", "NEW=0485393f3a-r32\nOLD=0485393f3a-r31\n")
host = rep(host, "WANT_TAR=" + R31_TAR, "WANT_TAR=" + TAR_SHA)
host = rep(host, '"ledger": "' + LEDGER_OLD + '"', '"ledger": "' + LEDGER_NEW + '"')
lines = host.split("\n")
if lines[0] != "set -uo pipefail":
    refuse("host script first line")
first_check = next(i for i, ln in enumerate(lines) if ln.startswith('check "'))
last_check = max(i for i, ln in enumerate(lines) if ln.startswith('check "'))
if any(not lines[i].startswith('check "') for i in range(first_check, last_check + 1)):
    refuse("the member checks are not one block")
lines = lines[:first_check] + checks_lines + lines[last_check + 1:]
HOST_HEADER = [
    "# Ledger %s: resident root 0485393f3a-r31 -> 0485393f3a-r32 (the r31 member set with the trunk blobs of the %d package members that the merged cells of" % (LEDGER_NEW, len(PKG_DIFF)),
    "# IRPT_ANLREQ workstream ~G (AR-g-67, AR-g-68, AR-g-80 to AR-g-91 and AR-g-93) change, the %d members they add, the package sums and the bindings replaced; base pin 0485393f3a)," % len(ONLY32),
    "# and the 0485393f3a-r31 root and its library stay on the host for rollback.",
    "# Copy of the r31 script with NEW, OLD, WANT_TAR, the member checks (one per differing or added member, equal to the extracted r32 tarball), the ledger and this header changed;",
    "# written by 0.9.0_WK_IRPT_ANLREQ worker for 2.0.0_SA_COO~G2 (build only); operator a CloudOps seat under a signed pair. Authoring this script uploaded, installed and applied nothing.",
]
head_end = next(i for i, ln in enumerate(lines) if ln.startswith("NEW="))
host_text = "\n".join(["set -uo pipefail"] + HOST_HEADER + lines[head_end:])
HOST_NAME = "resident_host_install_0485393f3a-r32.sh"
host_path = write(HOST_NAME, host_text)
HOST_SHA = sha_file(host_path)
quoted = [ln for ln in host_text.split("\n") if ln.startswith('check "')]
if len(quoted) != len(CHECKED):
    refuse("quoted member checks %d, want %d" % (len(quoted), len(CHECKED)))

# ---------------------------------------------------------------- install
ins = load("install_r31.sh")
ins = rep(ins, "NEW=0485393f3a-r31\nOLD=0485393f3a-r29\n", "NEW=0485393f3a-r32\nOLD=0485393f3a-r31\n")
ins = rep_line(ins, "WANT=", ["WANT=" + HOST_SHA])
ins = rep_line(ins, "WANTSUM=", ["WANTSUM=" + SUMS_SHA])
ins = rep(ins, 'echo "R31 guard: running root', 'echo "R32 guard: running root')
ins = rep(ins, "V1 P2b release-31 members (each wanted value is the release-31 build record sha256 of the member):",
          "V1 P2b release-32 members (each wanted value is the release-32 build record sha256 of the member; an added member has no release-31 value):")
ilines = ins.split("\n")
start = next(i for i, ln in enumerate(ilines) if ln == "for ent in \\")
end = next(i for i in range(start, len(ilines)) if ilines[i].endswith("; do"))
PKG_ALL = sorted(set(PKG_DIFF) | set(ONLY32))
ilines = ilines[:start] + entries(PKG_ALL, R32) + ilines[end + 1:]
ins = "\n".join(ilines)
ins = rep(ins, "V1 P3 held members: the package's own sums (298 entries) checked against the running root:",
          "V1 P3 held members: the package's own sums (%d entries) checked against the running root:" % PKG_COUNT)
ins = rep(ins, "(want 0 of 298, the build record's sha256sums_check)", "(want 0 of %d, the build record's sha256sums_check)" % PKG_COUNT)
ins = rep(ins, "(the package's 298 plus the host's pydeps; the release-19 root had 4346; the build record carries no host count, printed for the record only)",
          "(the package's %d plus the host's pydeps; the release-19 root had 4346; the build record carries no host count, printed for the record only)" % PKG_COUNT)
ins = rep(ins, "import opal_producer  # noqa: F401\n",
          "import opal_producer  # noqa: F401\nimport portfolio_series  # noqa: F401\nimport price_source  # noqa: F401\nimport swap_replacement  # noqa: F401\n"
          "import tr_level  # noqa: F401\nimport price_adapter_bbg  # noqa: F401\nimport price_adapter_demque  # noqa: F401\nimport price_adapter_yfinance  # noqa: F401\n"
          "import price_adapter_ycharts  # noqa: F401\n")
ins = rep_line(ins, 'echo "V1 worker sha256 ', [
    'echo "V1 worker sha256 $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -d\' \' -f1) (want %s; release-31 %s)"' % (WORKER, WORKER31)])
ins = rep_line(ins, 'echo "V1 expected producer list ', [
    'echo "V1 expected producer list (release 32, two entries): andrew@opalinvest.com fwd1-staff-r41b@opal.invalid; running: $(grep -m1 \'^OPAL_PRODUCER_PRINCIPALS\' $RUN/ycharts/generate/resident_worker.py)"'])
if ins.count(LEDGER_OLD) != 2:  # the old header comment (dropped below) and the V1 receipt read-back
    refuse("ledger text count %d, want 2" % ins.count(LEDGER_OLD))
ins = ins.replace(LEDGER_OLD, LEDGER_NEW)
INS_HEADER = [
    "set -u",
    "# Ledger %s, legs D2 + V1: fetch the signed r32 install script BY KEY (the host role holds GetObject, not GetObjectVersion), verify its sha256" % LEDGER_NEW,
    "# (it binds the bytes), run it (it stages the tar, checks every changed or added member, reinstalls the library with the same bytes, keeps the r31 root and library for rollback and rolls both",
    "# back itself on a failed start), then read the running package back. Sent through Systems Manager. No vendor call.",
    "# Written for IRPT_ANLREQ round 20 (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it under a signed never-widen pair.",
    "# Derived from install_r31.sh by the r31 method. Changed: NEW, OLD, WANT, WANTSUM; the guard (the running root must be 0485393f3a-r31, exit 34); the release-32 member table;",
    "# the package sums count; the expected producer list; the imports of the price modules. Every fetch, sha256 and refusal guard of install_r31.sh is kept with its exit code.",
]
ibody_start = next(i for i, ln in enumerate(ins.split("\n")) if ln.startswith("NEW="))
ins_text = "\n".join(INS_HEADER + ins.split("\n")[ibody_start:])
write("install_r32.sh", ins_text)

# ---------------------------------------------------------------- pre-read
pre = load("pre_read_r31.sh")
pre = rep(pre, "OLD=0485393f3a-r29\nNEW=0485393f3a-r31\n", "OLD=0485393f3a-r31\nNEW=0485393f3a-r32\n")
pl = pre.split("\n")
s = next(i for i, ln in enumerate(pl) if ln.startswith('echo "P1 members that release 31 changes'))
e = next(i for i in range(s, len(pl)) if pl[i] == "done")
body = ['echo "P1 members that release 32 changes or adds, read at the running root (each wanted value is the release-31 sha256; an added member must be absent):"',
        "for ent in \\"]
for i, n in enumerate(PKG_ALL):
    want = R31.get(n, "ABSENT")
    body.append('  "%s %s"%s' % (n, want, "; do" if i == len(PKG_ALL) - 1 else " \\"))
body += ["  set -- $ent",
         "  if [ -f $RUN/$1 ]; then GOT=$(sha256sum $RUN/$1 | cut -d' ' -f1); else GOT=ABSENT; fi",
         '  echo "P1 member $1 sha256 $GOT (want $2) $([ "$GOT" = "$2" ] && echo MATCH || echo MISMATCH)"',
         "done"]
pl = pl[:s] + body + pl[e + 1:]
pre = "\n".join(pl)
pre = rep_line(pre, 'echo "P1 worker sha256 ', [
    'echo "P1 worker sha256 $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -d\' \' -f1) (want %s, the release-31 worker; release 32 moves the worker (its producer list))"' % WORKER31])
pre = rep(pre, "(want /opt/irpt-resident/$OLD and irpt-resident-r29-20261014)", "(want /opt/irpt-resident/$OLD and %s)" % LEDGER_OLD)
pre = rep(pre, "the release-29 library", "the release-31 library", count=pre.count("the release-29 library"))
pre = rep(pre, "the release-29 wrapper", "the release-31 wrapper", count=pre.count("the release-29 wrapper"))
pre = pre.replace("expected before the r31 installer runs", "expected before the r32 installer runs").replace("release-29 receipt", "release-31 receipt")
PRE_HEADER = [
    "set -u",
    "# Ledger %s, leg P1 (READ ONLY): the host state before the r32 install (expect the r31 root running, the library and wrapper unmoved, the r32 root absent). No write, no vendor call." % LEDGER_NEW,
    "# Written for IRPT_ANLREQ round 20 (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it under a later order.",
    "# Derived from pre_read_r31.sh by the r31 method, shifted one release. Changed: OLD, NEW, the fail-closed running-root read (STOP-READ-0, exit 40), the release-32 member read-back",
    "# (the members the release changes at their release-31 sha256, the members it adds as ABSENT), the worker read-back (release 31) and the receipt ledger (r31).",
]
pstart = next(i for i, ln in enumerate(pre.split("\n")) if ln.startswith("R=/opt/irpt-resident"))
write("pre_read_r32.sh", "\n".join(PRE_HEADER + pre.split("\n")[pstart:]))

# ---------------------------------------------------------------- rollback
rb = load("rollback_r31.sh")
rb = rep(rb, "NEW=0485393f3a-r31\nOLD=0485393f3a-r29\n", "NEW=0485393f3a-r32\nOLD=0485393f3a-r31\n")
rl = rb.split("\n")
s = next(i for i, ln in enumerate(rl) if ln.startswith('echo "X1 members that release 31 changes'))
e = next(i for i in range(s, len(rl)) if rl[i] == "done")
body = ['echo "X1 members that release 32 changes or adds, read at the running root (each wanted value is the release-31 sha256; an added member must be absent):"',
        "for ent in \\"]
for i, n in enumerate(PKG_ALL):
    want = R31.get(n, "ABSENT")
    body.append('  "%s %s"%s' % (n, want, "; do" if i == len(PKG_ALL) - 1 else " \\"))
body += ["  set -- $ent",
         "  if [ -f $RUN/$1 ]; then GOT=$(sha256sum $RUN/$1 | cut -d' ' -f1); else GOT=ABSENT; fi",
         '  echo "X1 member $1 sha256 $GOT (want $2) $([ "$GOT" = "$2" ] && echo MATCH || echo MISMATCH)"',
         "done"]
rl = rl[:s] + body + rl[e + 1:]
rb = "\n".join(rl)
rb = rep(rb, "(want /opt/irpt-resident/$OLD and irpt-resident-r29-20261014)", "(want /opt/irpt-resident/$OLD and %s)" % LEDGER_OLD)
rb = rb.replace("the host library is not the release-29 library", "the host library is not the release-31 library")
RB_HEADER = [
    "set -u",
    "# Ledger %s, leg X1 (NOT run unless the issuer orders it): put the resident back on the r31 root. The library bytes are the same before and after" % LEDGER_NEW,
    "# release 32 (a1c288, reinstalled by the r32 install from the package), so no library step is needed beyond the refusal check.",
    "# Written for IRPT_ANLREQ round 20 (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it only if the issuer orders it.",
    "# Derived from rollback_r31.sh by the r31 method. Changed: NEW, OLD, the member read-back (the members release 32 changes at their release-31 sha256, the members it adds as ABSENT:",
    "# the values the rollback target must hold) and the wording. Every refusal guard of rollback_r31.sh is kept with its exit code.",
]
rstart = next(i for i, ln in enumerate(rb.split("\n")) if ln.startswith("NEW="))
write("rollback_r32.sh", "\n".join(RB_HEADER + rb.split("\n")[rstart:]))

print("TAR_SHA %s" % TAR_SHA)
print("SUMS_SHA %s" % SUMS_SHA)
print("HOST_SHA %s" % HOST_SHA)
print("DIFF %s" % " ".join(DIFF))
print("ADDED %s" % " ".join(ONLY32))
print("CHECKED %d PKG_ALL %d PKG_COUNT %d" % (len(CHECKED), len(PKG_ALL), PKG_COUNT))
