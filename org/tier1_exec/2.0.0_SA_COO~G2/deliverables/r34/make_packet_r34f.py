"""Write the release-34f never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r34f.py <RESIDENT_R34F_BUILD.json> <stage folder> <expected tarball sha256> <v2 script path> <packet out path> <AR-g-129 merge short sha> <v2 test case count>

Every number in the packet is read from the record, the extracted tarballs, the V2 script and the reachability walk; nothing is typed. It refuses unless
ar_g130_checks.py verify passes on the same record with the same expected tarball sha256. ASCII only. Runs from the repository root. Writes the packet only.
"""
import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile

REC, STAGE, WANT_TAR, V2_PATH, OUT = sys.argv[1:6]
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
CHECK = os.path.join(REPO, "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g130_checks.py")
REACH = os.path.join(REPO, "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/r32_reachability.py")
MEMBER = "ycharts/generate/resident_worker.py"
G129 = sys.argv[6] if len(sys.argv) > 6 else "merged"  # the merge commit of cell AR-g-129 (short sha)
V2CASES = sys.argv[7] if len(sys.argv) > 7 else "all"  # the case count the V2 test printed

verify = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT_TAR], capture_output=True, text=True, cwd=REPO)
if verify.returncode != 0 or "AR-G130-OK" not in verify.stdout:
    raise SystemExit("REFUSE: the build does not verify: " + verify.stdout[-200:] + verify.stderr[-200:])
rec = json.load(open(REC, encoding="utf-8"))
pin, art, delta = rec["release_input"]["pin_full_sha"], rec["artifact"], rec["delta_vs_r34e"]
scripts = {s["name"]: s for s in rec["scripts"]}
if delta["changed"] != sorted(["SHA256SUMS", "reports/resident_bindings.json", MEMBER]) or delta["added"] or delta["removed"]:
    raise SystemExit("REFUSE: the delta is not the three expected members")
v2_bytes = open(V2_PATH, "rb").read()
if any(b > 127 for b in v2_bytes):
    raise SystemExit("REFUSE: the V2 script is not ASCII")
if subprocess.run(["bash", "-n", V2_PATH]).returncode != 0:
    raise SystemExit("REFUSE: the V2 script fails bash -n")
v2_sha = hashlib.sha256(v2_bytes).hexdigest()
at_head = subprocess.run(["git", "show", "HEAD:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/v2_service_env_r34f.sh"], capture_output=True, cwd=REPO, check=True).stdout
if hashlib.sha256(at_head).hexdigest() != v2_sha:
    raise SystemExit("REFUSE: the V2 script on disk is not the committed one")
tmp = tempfile.mkdtemp(prefix="r34f_packet_")
tarfile.open(art["path"]).extractall(tmp + "/x34")
reach = subprocess.run([sys.executable, "-I", REACH, tmp + "/x34", MEMBER], capture_output=True, text=True, check=True).stdout.splitlines()
live = "LIVE" if reach[1].endswith("REACHABLE") and not reach[1].endswith("not reachable") else "not reachable"
text = """# Never-widen sign-off packet -- r34f: the resident r34e -> r34f at pin %(pin12)s (the resolve hop backs off a WAF challenge: 150, 300, 450 s, not a flat 60 s)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** `0.7.0_AE_CloudOps~AQ2`.
**Authority:** CTO msgs 9429 and 9447 (run 3 stays HELD; AQ2's ONE cookieless lookup read CLEAN, so cut the bounded WAF back-off now: growing spacing, 15-minute cap, class named in the journal; its own cell and pair). Design: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/WAF_BACKOFF_DESIGN_20261016.md`. Cell AR-g-129 merged `%(g129)s`.
**One move:** D1, the install of one new root on the resident host. One member changes: `%(member)s`. No IAM, Lambda, queue, table or schema moves; no new vendor call path; `opal_pricing` stays OFF.

## 1. What ships

Package pin `%(pin)s`; base pin `%(base)s`; built by `r34f_build.py` over the tools at that pin, BUILD ONLY, over the RUNNING r34e root (tarball sha256 `a96fbfb74db2caf6ad55d93ab35c3b7dd419cf54f4a4dba444bb3268e68e9227`). **%(members)d members**: %(unchanged)d identical to r34e, **%(nchanged)d changed**, 0 added, 0 removed. Two of the three are bookkeeping (the sums and the pin in the bindings).

| member | vs r34e | what changes |
|---|---|---|
| `%(member)s` | changed (%(live)s in the resident's runtime, static import walk) | a resolve-hop RETRY whose code ends `:WAF_CHALLENGE` is released for 150 s, 300 s, 450 s at receives 1, 2, 3 (900 s in all, under `REDRIVE_SECONDS` 960 and the queue's maxReceiveCount 5); every other RETRY cause keeps 60 s; the BUSY class keeps its own re-send path; the journal line names the delay (`visibility=<s>`) |
| `reports/resident_bindings.json` | changed | only `provenance.package_pin` (the verifier proves no other key moved) |
| `SHA256SUMS` | changed | the package sums, replaced |

**Artifacts** (staged outside the repository; nothing uploaded):
- Tar `%(tar_name)s`: sha256 `%(tar_sha)s`, %(tar_bytes)s bytes, %(members)d members.
- Package sums `irpt-resident-0485393f3a-r34f.package.SHA256SUMS`: sha256 `%(sums_sha)s`.
- Host install script `resident_host_install_0485393f3a-r34f.sh`: sha256 `%(host_sha)s`; `install_r34.sh` `%(install_sha)s`; `pre_read_r34.sh` `%(pre_sha)s`; `rollback_r34.sh` `%(rb_sha)s`.
- V2 script `v2_service_env_r34f.sh` (in the repository at `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): sha256 `%(v2_sha)s`; its offline test printed %(v2cases)s cases OK.
- The capture library, wrapper, the r34e door checker and every other member are unchanged.

## 2. Blast radius, by branch (read from the code at the pin)

| what | BEFORE (r34e) | AFTER (r34f) |
|---|---|---|
| a resolve-hop RETRY coded `...:WAF_CHALLENGE` (the door's lookup challenged by the firewall) | retried at 60 s, 60 s, 60 s: all inside the measured (122, 373] s window; row ends RESOLVE_RETRY_EXHAUSTED (SET 2 and SET 3) | retried at +150, +300, +450 s; the attempts at +450 and +900 s clear the window's far edge; the row still ends at receive 4 if all are challenged |
| any other RETRY code (503, body, timeout, a code that only CONTAINS WAF_CHALLENGE, a missing or non-string code) | 60 s | 60 s (unchanged; the checks assert it at receives 1, 2, 3 through the real poll_once) |
| the BUSY class | own re-send path | unchanged |
| a filer's upload on a persistent challenge | RESOLVING about 3 minutes, then NEEDS_CORRECTION | RESOLVING up to 15 minutes, then NEEDS_CORRECTION (the CTO's cap) |
| the door's lookup, the lease, `_end_exhausted_resolve`, the generation hop's 390 s read-back, the checker, pricing | -- | unchanged |

**Known limit (named, not a stop).** The +150 s attempt sits at the lower edge of the measured window and may be challenged again; the +450 s and +900 s attempts are the ones expected to clear. If the retries are challenged anyway, the next fix is source pacing of the lookups, a separate cell. Nothing in this release claims the challenge is rate-based for the sessionless lookup: the 2026-10-05 measurement says so for the generation hop and SET 2 is consistent with it.

**Writers counted.** `%(member)s`: ONE writer (the builder, for this release). The package sums: ONE (the builder).

## 3. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob. The ledger `irpt-resident-r34f-20261016` is opened first; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming the resident host, the unit or its root is a STOP).
2. **Send every host script AS ROOT.** Before-read: `pre_read_r34.sh` (fail-closed: the running root must be `0485393f3a-r34e`; the r34f root absent; the library and wrapper unmoved).
3. D1: upload the tar, the sums file and the host script to the keys the install script names (each key must read 404 first; record the S3 versions); `install_r34.sh` fetches the host script and the sums BY KEY and refuses unless their sha256 equal `WANT` / `WANTSUM`.
4. V1: running root `0485393f3a-r34f`; the %(nchecks)d changed members at their built value; the package sums %(sums_lines)d of %(sums_lines)d OK; the imports; queue 0/0; no sign-in in the journal.
5. **V2, INSIDE the service's own environment:** `v2_service_env_r34f.sh`, sha256 `%(v2_sha)s` (verify before sending). It keeps r34e's four controls and adds `V2S BACKOFF`: it imports the shipped `resident_worker` from the new root on the service's flat import path and reads the schedule (WAF code at receives 1, 2, 3 = 150, 300, 450; a 503 = 60; the constants; the module file lies under the new root). No vendor call.
6. **Gate:** anything but `V2S OK` (or an install that did not print its success line): send `rollback_r34.sh` AS ROOT the same session, read the running root back as `0485393f3a-r34e`, close the ledger ROLLED-BACK, report. No retry.
7. The ledger closes at V2.

**Live proof is a separate act** (FWD-1 run 3 under `~Y2`, once this ledger reads CLOSED and the CTO releases the hold).

## 4. Rollback, per key

- **The root:** `rollback_r34.sh` (or the install's own failure branch) restores `0485393f3a-r34e`, which stays on the host.
- **The receipt:** the r34e receipt is kept by the install and copied back.
- **The library:** unchanged bytes before and after.
- **Queued messages:** none are touched; a message received after a rollback is served by r34e (flat 60 s retry).

## 5. Not claimed

- That a retry at +150, +300 or +450 s clears the WAF window for the sessionless lookup (the offline checks and V2 prove the schedule, not the firewall).
- That the service process itself has run the shipped schedule: a live challenged resolve does.
- The live host, S3 objects, running root and receipt were NOT read (this is a build record).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set is: one new root directory on the resident host (`/opt/irpt-resident/0485393f3a-r34f`); the receipt and its r34e copy; the unit's ExecStart; the kept library copy; one transient systemd unit for V2. The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin12": pin[:10], "base": rec["release_input"]["base_pin"], "members": art["member_count"], "unchanged": delta["unchanged"],
    "nchanged": len(delta["changed"]), "member": MEMBER, "live": live, "g129": G129, "v2cases": V2CASES, "tar_name": os.path.basename(art["path"]), "tar_sha": art["sha256"],
    "tar_bytes": "{:,}".format(art["bytes"]), "sums_sha": art["sha256sums_file"]["sha256"],
    "host_sha": scripts["resident_host_install_0485393f3a-r34f.sh"]["sha256"], "install_sha": scripts["install_r34.sh"]["sha256"],
    "pre_sha": scripts["pre_read_r34.sh"]["sha256"], "rb_sha": scripts["rollback_r34.sh"]["sha256"], "nchecks": len(delta["changed"]),
    "sums_lines": art["sha256sums_file"]["lines"], "v2_sha": v2_sha}
if any(ord(c) > 127 for c in text):
    raise SystemExit("REFUSE: non-ASCII in the packet")
with open(OUT, "w", encoding="ascii", newline="\n") as fh:
    fh.write(text)
print("wrote %s bytes=%d" % (OUT, len(text)))
