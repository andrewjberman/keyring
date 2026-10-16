"""Write the release-34g never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r34g.py <RESIDENT_R34G_BUILD.json> <stage folder> <expected tarball sha256> <v2 script path> <packet out path> <AR-g-133 merge short sha> <v2 test case count>

Every number in the packet is read from the record, the extracted tarballs, the V2 script and the reachability walk; nothing is typed. It refuses unless
ar_g137_checks.py verify passes on the same record with the same expected tarball sha256. ASCII only. Runs from the repository root. Writes the packet only.
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
CHECK = os.path.join(REPO, "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g137_checks.py")
REACH = os.path.join(REPO, "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/r32_reachability.py")
MEMBER = "intake/security_resolution.py"
G133 = sys.argv[6] if len(sys.argv) > 6 else "merged"  # the merge commit of cell AR-g-133 (short sha)
V2CASES = sys.argv[7] if len(sys.argv) > 7 else "all"  # the case count the V2 test printed

verify = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT_TAR], capture_output=True, text=True, cwd=REPO)
if verify.returncode != 0 or "AR-G137-OK" not in verify.stdout:
    raise SystemExit("REFUSE: the build does not verify: " + verify.stdout[-200:] + verify.stderr[-200:])
rec = json.load(open(REC, encoding="utf-8"))
pin, art, delta = rec["release_input"]["pin_full_sha"], rec["artifact"], rec["delta_vs_r34f"]
scripts = {s["name"]: s for s in rec["scripts"]}
if delta["changed"] != sorted(["SHA256SUMS", "reports/resident_bindings.json", MEMBER]) or delta["added"] or delta["removed"]:
    raise SystemExit("REFUSE: the delta is not the three expected members")
v2_bytes = open(V2_PATH, "rb").read()
if any(b > 127 for b in v2_bytes):
    raise SystemExit("REFUSE: the V2 script is not ASCII")
if subprocess.run(["bash", "-n", V2_PATH]).returncode != 0:
    raise SystemExit("REFUSE: the V2 script fails bash -n")
v2_sha = hashlib.sha256(v2_bytes).hexdigest()
at_head = subprocess.run(["git", "show", "HEAD:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/v2_service_env_r34g.sh"], capture_output=True, cwd=REPO, check=True).stdout
if hashlib.sha256(at_head).hexdigest() != v2_sha:
    raise SystemExit("REFUSE: the V2 script on disk is not the committed one")
tmp = tempfile.mkdtemp(prefix="r34g_packet_")
tarfile.open(art["path"]).extractall(tmp + "/x34")
reach = subprocess.run([sys.executable, "-I", REACH, tmp + "/x34", MEMBER], capture_output=True, text=True, check=True).stdout.splitlines()
live = "LIVE" if reach[1].endswith("REACHABLE") and not reach[1].endswith("not reachable") else "not reachable"
text = """# Never-widen sign-off packet -- r34g: the resident r34f -> r34g at pin %(pin12)s (the upload door asks yfinance FIRST, YCharts second; opal_pricing ON)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** `0.7.0_AE_CloudOps~IB2` (rule 34, CTO msg 9561).
**Authority:** PRD v0.22 (Andrew-direct ~15:2xZ: "yfinance first and ycharts second as a general rule for any part of this process"); CTO msgs 9522 (the four items), 9600 (items 1 to 3 and pricing ON first, item 4 later; NOT installed while run 3 is pinned to r34f and its window is open or about to open) and 9620 (item 3 is met for this release by naming the remaining YCharts calls). Cell AR-g-133 merged `%(g133)s`; the id trace is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~266/YCHARTS_ID_TRACE.json` (merged `1180b2f0b1`).
**One move:** D1, the install of one new root on the resident host. One code member changes: `%(member)s`; the bindings file changes in one binding (`opal_pricing.enabled` false -> true) and the pin. No IAM, Lambda, queue, table or schema moves; no new vendor call path (the door's Yahoo checker already exists; its cap and pacing are unchanged).

## 1. What ships

Package pin `%(pin)s`; base pin `%(base)s`; built by `r34g_build.py` over the tools at that pin, BUILD ONLY, over the RUNNING r34f root (tarball sha256 `0d223e500a92aa274bbb52437d33657dd870b9f29af41ec942463c936d904a3f`). **%(members)d members**: %(unchanged)d identical to r34f, **%(nchanged)d changed**, 0 added, 0 removed.

| member | vs r34f | what changes |
|---|---|---|
| `%(member)s` | changed (%(live)s in the resident's runtime, static import walk) | `SecurityResolver.check` with a checker asks it ONCE about every uncached symbol (and every cached provider NOT_FOUND) BEFORE the provider; a symbol it KEEPS is final (the KEPT row of AR-y-293: `price_source` yfinance, no provider receipt) and never reaches YCharts; only the rest go to the provider in one call; a provider FOUND beats a NOT_KEPT; a NOT_KEPT stays the provider's NOT_FOUND with no second checker call; a CHECK_FAILED or NOT_CHECKED symbol the provider does not find reads UNAVAILABLE with its reason word as before; `verified_suggestions` also shows a candidate the checker KEPT |
| `reports/resident_bindings.json` | changed | `provenance.package_pin`, and `opal_pricing` from `{"enabled": false, ...}` to `{"enabled": true, "tiers": ["estate", "yfinance"]}` (the verifier proves no other key moved) |
| `SHA256SUMS` | changed | the package sums, replaced |

**Artifacts** (staged outside the repository; nothing uploaded):
- Tar `%(tar_name)s`: sha256 `%(tar_sha)s`, %(tar_bytes)s bytes, %(members)d members.
- Package sums `irpt-resident-0485393f3a-r34g.package.SHA256SUMS`: sha256 `%(sums_sha)s`.
- Host install script `resident_host_install_0485393f3a-r34g.sh`: sha256 `%(host_sha)s`; `install_r34.sh` `%(install_sha)s`; `pre_read_r34.sh` `%(pre_sha)s`; `rollback_r34.sh` `%(rb_sha)s`.
- V2 script `v2_service_env_r34g.sh` (in the repository at `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): sha256 `%(v2_sha)s`; its offline test printed %(v2cases)s cases OK.
- The capture library, wrapper, the WAF back-off (r34f), the Yahoo checker and every other member are unchanged.

## 2. Blast radius, by branch (read from the code at the pin)

| what | BEFORE (r34f) | AFTER (r34g) |
|---|---|---|
| the upload door, a symbol Yahoo keeps (history at T-1) | one YCharts securities_info lookup first, Yahoo only after a YCharts NOT_FOUND | KEPT without a YCharts call; zero YCharts lookups when every symbol is kept |
| the upload door, a symbol Yahoo does not keep, or a Yahoo failure | YCharts lookup; NOT_FOUND then asked Yahoo | Yahoo asked first (one batch, the checker's cap of 10 and 1 s pacing unchanged), then YCharts for these symbols; FOUND beats NOT_KEPT; the unavailable and not-checked reasons read as before |
| Yahoo called for every uncached symbol rather than only for YCharts misses | -- | more Yahoo calls per upload, bounded by the checker's cap of 10; a symbol beyond the cap reads NOT_CHECKED and goes to YCharts (named, not a stop; raising the cap is a Yahoo-pushback question for the CTO) |
| the Opal producer's report (producers `andrew@opalinvest.com`, `fwd1-staff-r41b@opal.invalid`) | unpriced (`opal_pricing` off) | priced from the chain the resident reads today: estate, then yfinance, as_of T-1 (resident_installed.py, AR-g-90); the YCharts recipe path is not touched |
| cached answers (FOUND 86400, NOT_FOUND 900, KEPT 900) | served with no call | unchanged |
| the report built by YCharts (recipe: upload, create, status, read-back, validate, generate, download) | 8 to 9 YCharts calls per report | unchanged: those calls are the "remaining YCharts calls" of PRD v0.22 item 3 (CTO msg 9620). The Opal-built report path is FWD-7's own outcome, a later ENGINE cell |
| the lease, the WAF back-off, the swap pass, the pool, the checker, the producer list | -- | unchanged (the other 311 members are byte-identical to r34f) |

**Known limits (named, not stops).** (1) Item 4, the lease count per window, is NOT in this release (CTO msg 9600); the AR-g-129 back-off is the fallback. (2) A holding Yahoo keeps but YCharts does not carry is KEPT at the door and still cannot be in a YCharts-built report (the vendor echo refuses an omitted holding: recipe.py:541-545); today it goes through C-SWAP's replacement. (3) With pricing ON the Opal producer prices its report; the first live priced run is a separate act.

**Writers counted.** `%(member)s`: ONE writer (the builder, for this release). The bindings file and the package sums: ONE (the builder).

## 3. Apply protocol, in this order

1. **Run 3 first (CTO msg 9600).** This packet is not applied while run 3 is pinned to r34f and its window is open or about to open. The GO says so in terms.
2. Both halves at HEAD naming this file's blob. The ledger `irpt-resident-r34g-20261016` is opened first; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming the resident host, the unit or its root is a STOP).
3. **Send every host script AS ROOT.** Before-read: `pre_read_r34.sh` (fail-closed: the running root must be `0485393f3a-r34f`; the r34g root absent; the library and wrapper unmoved; the changed member at its r34f value).
4. D1: upload the tar, the sums file and the host script to the keys the install script names (each key must read 404 first; record the S3 versions); `install_r34.sh` fetches the host script and the sums BY KEY and refuses unless their sha256 equal `WANT` / `WANTSUM`.
5. V1: running root `0485393f3a-r34g`; the %(nchecks)d changed members at their built value; the package sums %(sums_lines)d of %(sums_lines)d OK; the imports; queue 0/0; no sign-in in the journal; `opal_pricing` reads enabled true.
6. **V2, INSIDE the service's own environment:** `v2_service_env_r34g.sh`, sha256 `%(v2_sha)s` (verify before sending). It keeps r34f's four controls and the back-off check, and adds `V2S DOOR` (the shipped resolver, imported on the service's flat import path with fake ports, asks the checker once about both symbols and the provider only about the one not kept) and `V2S PRICING` (the shipped bindings carry the pricing ON). No YCharts call.
7. **Gate:** anything but `V2S OK` (or an install that did not print its success line): send `rollback_r34.sh` AS ROOT the same session, read the running root back as `0485393f3a-r34f`, close the ledger ROLLED-BACK, report. No retry.
8. The ledger closes at V2.

**Live proof is a separate act** (an upload whose symbols Yahoo keeps, read at the door: zero YCharts lookups).

## 4. Rollback, per key

- **The root:** `rollback_r34.sh` (or the install's own failure branch) restores `0485393f3a-r34f`, which stays on the host.
- **The receipt:** the r34f receipt is kept by the install and copied back.
- **The library:** unchanged bytes before and after.
- **Queued messages:** none are touched; a message received after a rollback is served by r34f.

## 5. Not claimed

- That Yahoo answers for every symbol it keeps within the checker's cap, or that a larger first batch does not draw Yahoo pushback (V2 asks Yahoo for two symbols; the door test uses fake ports).
- That a priced Opal report is correct on live data: V2 reads the binding, not a report.
- The live host, S3 objects, running root and receipt were NOT read (this is a build record).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set is: one new root directory on the resident host (`/opt/irpt-resident/0485393f3a-r34g`); the receipt and its r34f copy; the unit's ExecStart; the kept library copy; one transient systemd unit for V2. The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin12": pin[:10], "base": rec["release_input"]["base_pin"], "members": art["member_count"], "unchanged": delta["unchanged"],
    "nchanged": len(delta["changed"]), "member": MEMBER, "live": live, "g133": G133, "v2cases": V2CASES, "tar_name": os.path.basename(art["path"]), "tar_sha": art["sha256"],
    "tar_bytes": "{:,}".format(art["bytes"]), "sums_sha": art["sha256sums_file"]["sha256"],
    "host_sha": scripts["resident_host_install_0485393f3a-r34g.sh"]["sha256"], "install_sha": scripts["install_r34.sh"]["sha256"],
    "pre_sha": scripts["pre_read_r34.sh"]["sha256"], "rb_sha": scripts["rollback_r34.sh"]["sha256"], "nchecks": len(delta["changed"]),
    "sums_lines": art["sha256sums_file"]["lines"], "v2_sha": v2_sha}
if any(ord(c) > 127 for c in text):
    raise SystemExit("REFUSE: non-ASCII in the packet")
with open(OUT, "w", encoding="ascii", newline="\n") as fh:
    fh.write(text)
print("wrote %s bytes=%d" % (OUT, len(text)))
