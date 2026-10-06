#!/usr/bin/env python3
"""Gate a BUILT resident package before it is uploaded or installed, and write its tarball and install script.

    python resident_package_gate.py <package-dir> <pin> <running-tar.gz> <new-root-name> <old-root-name> \
        <ledger-slug> <out-dir> [--base-pin P --files-from LIST]

`<package-dir>` is the output of IRPT_MVP_P/build_resident_package.py at `<pin>`. `<running-tar.gz>` is the package
the host runs now (downloaded by its S3 version). No AWS call is made here. Checks, each with its denominator:

  G1  every member named in SHA256SUMS hashes to its line (the manifest describes the bytes);
  G2  every member except the generated bindings is byte-identical to `git show <pin>:<repo path>` (nothing in the
      package is older or newer than the pin: the whole-tree rule);
  G3  every .py member compiles; non-ASCII character count over all text members is printed;
  G4  the route table and the installed boundary agree (every operation `entry.ROUTES` names is served by
      reports/generate_installed.py), the pair whose mismatch raises at Entry construction;
  G5  the member census against the running package: added, removed, changed, identical.

With `--base-pin P --files-from LIST` (IRPT_YCDGEN R13, the builder's named-list build) G2 expects each member whose repo
path is named in LIST to equal `git show <pin>:<path>` and every other member to equal `git show P:<path>`; the
opal_map member is read from the bindings' `provenance.opal_map_source` at the pin. A member that differs fails G2 with
the count printed. Without the flags G2 is the whole-tree-at-the-pin rule above.

IRPT_YCDGEN R15: the gate reads `provenance.members_added` from the package's own `reports/resident_bindings.json` (the
builder's `--member PACKAGED=REPO` records). G2 expects each added member equal to `git show <pin>:<repo_path>` (and its
recorded sha256 equal to its SHA256SUMS line), with or without the named-list flags; a member that differs fails G2 with the
count printed. G5 counts each added member as added against a running package that lacks it.

Then it writes `<out-dir>/<new-root-name>.tar.gz` (members in sorted order, mtime 0), its sha256, the census JSON,
and the host install script with member pins read from THIS package. Exit 0 only when G1-G4 hold. ASCII only.
"""
import hashlib
import io
import json
import os
import py_compile
import re
import subprocess
import sys
import tarfile
import tempfile

IR = "infra/aws/lambda/investor-reporting/"
PINNED = ["ycharts/generate/resident_main.py", "ycharts/generate/resident_worker.py",
          "ycharts/generate/current_authority.py", "ycharts/generate/recipe.py", "ycharts/generate/job.py",
          "ycharts/generate/transport.py", "ycharts/generate/publisher.py", "ycharts/generate/templates.json",
          "ycharts/extract/extract.py", "ycharts/extract/publication.py", "ycharts/extract/certify.py",
          "ycharts/session/broker.py", "ycharts/session/host_capture.py", "_scope/canonical_profile_reads.py",
          "_scope/maintained_sources.py", "reports/resident_installed.py"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def parse_sums(text):
    rows = {}
    for line in text.splitlines():
        if line.strip():
            digest, path = line.split("  ", 1)
            rows[path.lstrip("./")] = digest
    return rows


def repo_path(member):
    """The repository path a package member was read from (the builder's own mapping, inverted)."""
    if member.startswith("ycharts-host/"):
        return "infra/aws/ec2/investor-reporting-ycharts/" + member.split("/", 1)[1]
    if member.startswith("census/"):
        return None  # pinned by its own sha at its own commit; checked by the builder
    if member.startswith(("lib/", "data/", "org/", "infra/", "docs/")):
        return member
    return IR + member


def split_flags(argv):
    """(positionals, base_pin, files_from) -- the two optional flags may sit anywhere after the program name."""
    rest, flags, i = [], {}, 1
    while i < len(argv):
        if argv[i] in ("--base-pin", "--files-from"):
            if i + 1 >= len(argv):
                raise SystemExit("%s needs a value" % argv[i])
            flags[argv[i]] = argv[i + 1]
            i += 2
        else:
            rest.append(argv[i])
            i += 1
    if ("--base-pin" in flags) != ("--files-from" in flags):
        raise SystemExit("--base-pin and --files-from go together")
    return rest, flags.get("--base-pin"), flags.get("--files-from")


def main(argv):
    rest, base_pin, files_from = split_flags(argv)
    pkg, pin, running_tar, new_root, old_root, slug, out_dir = rest[:7]
    listed = set()
    if files_from:
        listed = {line.strip() for line in open(files_from, encoding="utf-8").read().splitlines() if line.strip()}
    os.makedirs(out_dir, exist_ok=True)
    sums = parse_sums(open(os.path.join(pkg, "SHA256SUMS"), encoding="utf-8").read())
    ok = True

    bad = [m for m, d in sums.items() if sha(open(os.path.join(pkg, m), "rb").read()) != d]
    print("G1 manifest: %d of %d members hash to their SHA256SUMS line" % (len(sums) - len(bad), len(sums)))
    ok &= not bad

    opal_source = None
    bindings_path = os.path.join(pkg, "reports/resident_bindings.json")
    bindings = json.load(open(bindings_path, encoding="utf-8")) if os.path.isfile(bindings_path) else {}
    provenance = bindings.get("provenance", {})
    opal_source = provenance.get("opal_map_source") if base_pin else None
    added_members = {row["packaged"]: row for row in provenance.get("members_added", [])}
    differ, checked, skipped, from_list, from_added = [], 0, [], 0, 0
    for member in sorted(sums):
        path = repo_path(member)
        if member == "reports/resident_bindings.json" or path is None:
            skipped.append(member)
            continue
        expect_pin = pin
        if member in added_members:
            path = added_members[member]["repo_path"]
            from_added += 1
        elif base_pin:
            if member == "ycharts/research/overview_map.json" and opal_source:
                path, expect_pin = opal_source, pin
            elif path in listed:
                from_list += 1
            else:
                expect_pin = base_pin
        blob = subprocess.run(["git", "show", "%s:%s" % (expect_pin, path)], capture_output=True)
        checked += 1
        if blob.returncode != 0 or sha(blob.stdout) != sums[member]:
            differ.append(member)
        elif member in added_members and added_members[member].get("sha256") != sums[member]:
            differ.append(member)
    if base_pin:
        print("G2 named list: %d of %d members equal their expected blob (%d listed members from `git show %s:<path>`, "
              "the rest from `git show %s:<path>`); not compared %d (%s); %d member(s) differ"
              % (checked - len(differ), checked, from_list, pin[:10], base_pin[:10], len(skipped),
                 ", ".join(skipped), len(differ)))
    else:
        print("G2 whole tree at the pin: %d of %d members equal `git show %s:<path>`; not compared %d (%s)"
              % (checked - len(differ), checked, pin[:10], len(skipped), ", ".join(skipped)))
    for member in differ:
        print("   DIFFERS:", member)
    if added_members:
        absent = sorted(m for m in added_members if m not in sums)
        bad_added = sorted(set(m for m in added_members if m in differ) | set(absent))
        print("G2 added members: %d of %d members_added equal `git show %s:<repo_path>`; %d differ or are absent %s"
              % (len(added_members) - len(bad_added), len(added_members), pin[:10], len(bad_added), bad_added or ""))
        differ.extend(absent)
    if base_pin:
        unpackaged = sorted(path for path in listed if (path[len(IR):] if path.startswith(IR) else path) not in sums)
        print("G2 named list: %d listed path(s), %d not in the package %s" % (len(listed), len(unpackaged), unpackaged or ""))
        differ.extend(unpackaged)
    ok &= not differ

    failed, nonascii, pys = [], 0, 0
    with tempfile.TemporaryDirectory() as tmp:
        for member in sorted(sums):
            data = open(os.path.join(pkg, member), "rb").read()
            if member.endswith((".py", ".json", ".sh", ".md", ".js")):
                nonascii += sum(1 for ch in data.decode("utf-8", "replace") if ord(ch) > 127)
            if member.endswith(".py"):
                pys += 1
                try:
                    py_compile.compile(os.path.join(pkg, member), cfile=os.path.join(tmp, "x.pyc"), doraise=True)
                except py_compile.PyCompileError as exc:
                    failed.append((member, str(exc)[:120]))
    print("G3 compile: %d of %d .py members compile; non-ASCII characters in text members: %d"
          % (pys - len(failed), pys, nonascii))
    ok &= not failed

    entry = open(os.path.join(pkg, "ycharts/generate/entry.py"), encoding="utf-8").read()
    installed = open(os.path.join(pkg, "reports/generate_installed.py"), encoding="utf-8").read()
    names = set(re.findall(r"^([A-Z_]*OPERATION)\s*=", entry, re.MULTILINE))
    unserved = sorted(n for n in names if ("generate_entry." + n) not in installed)
    print("G4 route and boundary pair: %d operation constant(s) in entry.py, %d not served by generate_installed.py %s"
          % (len(names), len(unserved), unserved or ""))
    ok &= not unserved

    with tarfile.open(running_tar) as tar:
        name = [n for n in tar.getnames() if n.split("/")[-1] == "SHA256SUMS"][0]
        old = parse_sums(tar.extractfile(name).read().decode())
    added = sorted(set(sums) - set(old))
    removed = sorted(set(old) - set(sums))
    changed = sorted(k for k in sums if k in old and old[k] != sums[k])
    print("G5 census against the running package: added %d, removed %d, changed %d, identical %d (running %d, new %d)"
          % (len(added), len(removed), len(changed), len(sums) - len(added) - len(changed), len(old), len(sums)))

    tar_path = os.path.join(out_dir, new_root + ".tar.gz")
    with tarfile.open(tar_path, "w:gz") as tar:
        for member in ["SHA256SUMS"] + sorted(sums):
            data = open(os.path.join(pkg, member), "rb").read()
            info = tarfile.TarInfo(name="./" + member)
            info.size, info.mode, info.mtime = len(data), 0o644, 0
            tar.addfile(info, io.BytesIO(data))
    tar_sha = sha(open(tar_path, "rb").read())
    pins = {m: sums[m] for m in PINNED}
    library = sums["ycharts-host/ycharts_session.js"]
    wrapper = sums["ycharts-host/run-ycharts-session.sh"]
    census = {"pin": pin, "new_root": new_root, "old_root": old_root, "members": len(sums), "tar_sha256": tar_sha,
              "tar_bytes": os.path.getsize(tar_path), "added": added, "removed": removed, "changed": changed,
              "pinned_members": pins, "library_sha256": library, "wrapper_sha256": wrapper,
              "gates": {"G1": not bad, "G2": not differ, "G3": not failed, "G4": not unserved}}
    json.dump(census, open(os.path.join(out_dir, new_root + ".census.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    script = INSTALL.replace("@NEW@", new_root).replace("@OLD@", old_root).replace("@SLUG@", slug) \
        .replace("@TAR_SHA@", tar_sha).replace("@LIBRARY@", library).replace("@WRAPPER@", wrapper) \
        .replace("@PIN@", pin[:10]) \
        .replace("@PINS@", "\n".join('check "%s" %s' % (m, d) for m, d in pins.items()))
    script_path = os.path.join(out_dir, "resident_host_install_%s.sh" % new_root)
    open(script_path, "w", encoding="utf-8", newline="\n").write(script)
    print("tar %s sha256 %s bytes %d" % (os.path.basename(tar_path), tar_sha, os.path.getsize(tar_path)))
    print("install script %s sha256 %s" % (os.path.basename(script_path), sha(open(script_path, "rb").read())))
    print("GATE %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


INSTALL = r'''set -uo pipefail
# Ledger @SLUG@: resident root @OLD@ -> @NEW@ (the whole tree at CLOUD @PIN@, no member override), and the host capture
# library moved to the same pin because the package's bindings pin its sha256. The @OLD@ root and the old library stay
# on the host for rollback. Written by resident_package_gate.py from the BUILT package; operator 2.0.0_SA_COO~Y.
NEW=@NEW@
OLD=@OLD@
R=/opt/irpt-resident
H=/opt/investor-reporting-ycharts
ROOT=$R/$NEW
UNIT=irpt-analysis-resident.service
Q=https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation
KEY=ec2/investor-reporting-ycharts/resident/irpt-resident-$NEW.tar.gz
WANT_TAR=@TAR_SHA@
WANT_LIBRARY=@LIBRARY@
WANT_WRAPPER=@WRAPPER@
check() { [ "$(sha256sum "$ROOT/$1" | cut -d' ' -f1)" = "$2" ] || { echo "ERROR: $1 is not the built member"; exit 17; }; }
echo "before: active=$(systemctl is-active $UNIT) root=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1) library=$(sha256sum $H/ycharts_session.js | cut -c1-16)"
test -d $R/$OLD || { echo "ERROR: rollback root $OLD absent"; exit 10; }
[ "$(sha256sum $H/run-ycharts-session.sh | cut -d' ' -f1)" = "$WANT_WRAPPER" ] || { echo "ERROR: the host wrapper is not the package's wrapper; this script moves the library only"; exit 18; }
rm -rf "$ROOT"; mkdir -p "$ROOT"
aws s3 cp "s3://opal-313476888478-lambda-artifacts/$KEY" /tmp/irpt-resident-$NEW.tar.gz --only-show-errors --region us-east-1 || exit 11
[ "$(sha256sum /tmp/irpt-resident-$NEW.tar.gz | cut -d' ' -f1)" = "$WANT_TAR" ] || { echo "ERROR: tar is not the built bytes"; exit 16; }
tar -xzf /tmp/irpt-resident-$NEW.tar.gz -C "$ROOT" || exit 12
cd "$ROOT" || exit 13
sha256sum -c SHA256SUMS --quiet && echo "package SHA256SUMS OK ($(wc -l < SHA256SUMS) members)" || exit 14
@PINS@
check ycharts-host/ycharts_session.js $WANT_LIBRARY
node --check "$ROOT/ycharts-host/ycharts_session.js" || { echo "ERROR: the new capture library does not parse"; exit 19; }
cp -a $H/pydeps/. "$ROOT/"
rm -rf "$ROOT/bin"
chown -R ec2-user:ec2-user "$ROOT"
python3.12 - <<'PY'
import hashlib, os
rows = []
for dp, dn, fn in os.walk('.'):
    for f in fn:
        p = os.path.join(dp, f)
        if p == './SHA256SUMS':
            continue
        rows.append(hashlib.sha256(open(p, 'rb').read()).hexdigest() + '  ' + p)
rows.sort(key=lambda r: r.split('  ', 1)[1])
open('SHA256SUMS', 'w').write('\n'.join(rows) + '\n')
PY
MAN=$(sha256sum SHA256SUMS | cut -d' ' -f1)
echo "host members $(wc -l < SHA256SUMS) manifest_sha $MAN"
cp -p $R/cutover_receipt.json $R/cutover_receipt.$OLD.json
python3.12 - "$MAN" "$ROOT" <<'PY'
import json, sys, time
path = "/opt/irpt-resident/cutover_receipt.json"
r = json.load(open(path))
r.update({"package_manifest_sha256": sys.argv[1], "package_root": sys.argv[2], "written_by": "2.0.0_SA_COO~Y",
          "written_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ledger": "@SLUG@"})
open(path, "w").write(json.dumps(r, indent=2) + "\n")
PY
chown ec2-user:ec2-user SHA256SUMS $R/cutover_receipt.json
restore_receipt() { cp -p $R/cutover_receipt.$OLD.json $R/cutover_receipt.json; }
queue_depth() { aws sqs get-queue-attributes --queue-url $Q --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s ' \t' ' '; }
# The library moves BEFORE the factory check: the factory refuses PINNED_FILE_DIFFERS:library unless the host file is
# the one the bindings pin. The running unit pins the OLD library, so between this swap and the stop below a capture
# would refuse; the queue is read empty first, and again before the stop.
DEPTH0=$(queue_depth)
echo "queue visible/in-flight before the library swap: $DEPTH0"
if [ "$DEPTH0" != "0 0" ]; then restore_receipt; echo "BLOCKED: queue not empty; receipt restored, nothing moved"; exit 20; fi
cp -p $H/ycharts_session.js $H/ycharts_session.js.before-$NEW
install -m 0644 -o root -g root "$ROOT/ycharts-host/ycharts_session.js" $H/ycharts_session.js
restore_library() { install -m 0644 -o root -g root $H/ycharts_session.js.before-$NEW $H/ycharts_session.js; }
[ "$(sha256sum $H/ycharts_session.js | cut -d' ' -f1)" = "$WANT_LIBRARY" ] || { restore_library; restore_receipt; echo "BLOCKED: library install did not land; restored"; exit 21; }
sudo -u ec2-user PYTHONPATH="$ROOT" /usr/bin/python3.12 - "$ROOT" <<'PY'
import sys
for rel in ('intake', 'ops', 'reports', '_keys', '_authz', '_gate', 'ycharts/session', 'ycharts/extract'):
    sys.path.insert(0, sys.argv[1] + '/' + rel)
import resident_installed as ri
rt = ri.build_resident_runtime()
print('factory OK:', sorted(rt), 'enrolled', rt['assembly'].session.broker.enrolled_user_id)
PY
if [ $? -ne 0 ]; then restore_library; restore_receipt; echo "BLOCKED: factory failed; library and receipt restored, unit untouched"; exit 15; fi
DEPTH=$(queue_depth)
echo "queue visible/in-flight: $DEPTH"
if [ "$DEPTH" != "0 0" ]; then restore_library; restore_receipt; echo "BLOCKED: queue not empty; library and receipt restored, unit untouched"; exit 20; fi
systemctl stop $UNIT
install_root() {
  PYTHONPATH="$R/$1" bash "$R/$1/ycharts/generate/install-resident.sh" "$R/$1" /usr/bin/python3.12 resident_installed:build_resident_runtime ec2-user $R/cutover_receipt.json
}
install_root $NEW
RC=$?
echo "install $NEW rc=$RC"
sleep 25
ACTIVE=$(systemctl is-active $UNIT)
POLLS=$(journalctl -u $UNIT --since "-30 s" --no-pager | grep -c "IRPT_RESIDENT_POLL")
TRACE=$(journalctl -u $UNIT --since "-30 s" --no-pager | grep -c "Traceback")
echo "active=$ACTIVE polls_30s=$POLLS tracebacks_30s=$TRACE"
if [ $RC -ne 0 ] || [ "$ACTIVE" != active ] || [ "$POLLS" -lt 1 ] || [ "$TRACE" -ne 0 ]; then
  echo "ROLLBACK to $OLD"
  systemctl stop $UNIT
  restore_library
  restore_receipt
  install_root $OLD
  echo "rollback install rc=$?"
  sleep 20
fi
echo "final active: $(systemctl is-active $UNIT)"
systemctl show $UNIT -p MainPID -p ActiveEnterTimestamp -p NRestarts -p ExecStart | cut -c1-200
journalctl -u $UNIT --since "-1 min" --no-pager -o short-iso | cut -c1-200 | tail -6
RUN=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)
echo "running root $RUN"
echo "running current_authority $(sha256sum $RUN/ycharts/generate/current_authority.py | cut -d' ' -f1) allowedFirmIds mentions $(grep -c allowedFirmIds $RUN/ycharts/generate/current_authority.py)"
echo "running worker $(sha256sum $RUN/ycharts/generate/resident_worker.py | cut -d' ' -f1) PERMANENT_AUTHORITY_REFUSALS mentions $(grep -c PERMANENT_AUTHORITY_REFUSALS $RUN/ycharts/generate/resident_worker.py)"
echo "running reader $(sha256sum $RUN/_scope/canonical_profile_reads.py | cut -d' ' -f1) host library $(sha256sum $H/ycharts_session.js | cut -d' ' -f1)"
'''


if __name__ == "__main__":
    sys.exit(main(sys.argv))
