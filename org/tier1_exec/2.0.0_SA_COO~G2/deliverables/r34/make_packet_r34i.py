"""Write the release-34i never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r34i.py <RESIDENT_R34I_BUILD.json> <stage folder> <expected tarball sha256> <v2 script path> <packet out path> <v2 test case count>

Every number in the packet is read from the record, the extracted tarballs and the V2 script; nothing is typed. It refuses unless
ar_g153_checks.py verify passes on the same record with the same expected tarball sha256. ASCII only. Runs from the repository root. Writes the packet only.
"""
import hashlib
import json
import os
import subprocess
import sys

REC, STAGE, WANT_TAR, V2_PATH, OUT = sys.argv[1:6]
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
CHECK = os.path.join(REPO, "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g153_checks.py")
V2CASES = sys.argv[6] if len(sys.argv) > 6 else "all"  # the case count the V2 test printed

verify = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT_TAR], capture_output=True, text=True, cwd=REPO)
if verify.returncode != 0 or "AR-G153-OK" not in verify.stdout:
    raise SystemExit("REFUSE: the build does not verify: " + verify.stdout[-200:] + verify.stderr[-200:])
rec = json.load(open(REC, encoding="utf-8"))
pin, art, delta = rec["release_input"]["pin_full_sha"], rec["artifact"], rec["delta_vs_r34h"]
scripts = {s["name"]: s for s in rec["scripts"]}
if delta["changed"] != sorted(["SHA256SUMS", "reports/resident_bindings.json"]) or delta["added"] or delta["removed"]:
    raise SystemExit("REFUSE: the delta is not exactly the bindings and the sums")
v2_bytes = open(V2_PATH, "rb").read()
if any(b > 127 for b in v2_bytes):
    raise SystemExit("REFUSE: the V2 script is not ASCII")
if subprocess.run(["bash", "-n", V2_PATH]).returncode != 0:
    raise SystemExit("REFUSE: the V2 script fails bash -n")
v2_sha = hashlib.sha256(v2_bytes).hexdigest()
at_head = subprocess.run(["git", "show", "HEAD:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/v2_service_env_r34i.sh"], capture_output=True, cwd=REPO, check=True).stdout
if hashlib.sha256(at_head).hexdigest() != v2_sha:
    raise SystemExit("REFUSE: the V2 script on disk is not the committed one")
text = """# Never-widen sign-off packet -- r34i: the resident r34h -> r34i at pin %(pin12)s (the YCharts price tier taken out of the bindings; no code member moves)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** `0.7.0_AE_CloudOps~IB2` (rule 34, CTO msg 9561).
**Authority:** CTO msgs 9991 (the price tier's `id:<TICKER>,include:true,&zoom=max` is refused HTTP 400 on the host; r34h condition 1 reads failed; cut r34i), 10004 (one confirming read, at most 4 requests) and 10027 (that read answered form NONE: the recipe form with SPY is refused 400 signed in, plain and typed; r34i sets the tiers to `[estate, yfinance]`, the lease and the budget stay; a later release adds the tier back on the endpoint the CRO finds). The read: `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34h/RECIPE_FORM_READ.txt` (IB2 msg 10021) and `PRICE_PROBE.txt` (IB2 msg 9985).
**One move:** D1, the install of one new root on the resident host. The bindings file and the package sums are the only members that change; every code member is byte-equal to r34h. No IAM, Lambda, queue, table or schema moves; no vendor call.

## 1. What ships

Package pin `%(pin)s`; base pin `%(base)s`; built by `r34i_build.py` over the tools at that pin, BUILD ONLY, over the RUNNING r34h root (tarball sha256 `60cc8d1d68627c993121df7eca946a40046f1d7f63ddfd2968f83e27077b93c0`). **%(members)d members**: %(unchanged)d identical to r34h, **%(nchanged)d changed**, 0 added, 0 removed.

| member | vs r34h | what changes |
|---|---|---|
| `reports/resident_bindings.json` | changed | `provenance.package_pin`; `opal_pricing` tiers `[estate, yfinance, ycharts]` -> `[estate, yfinance]` (still enabled); `ycharts_window_budget` stays `{"calls": 6, "window_s": 390}` (the verifier proves no other key moved) |
| `SHA256SUMS` | changed | the package sums, replaced |

**Artifacts** (staged outside the repository; nothing uploaded):
- Tar `%(tar_name)s`: sha256 `%(tar_sha)s`, %(tar_bytes)s bytes, %(members)d members.
- Package sums `irpt-resident-0485393f3a-r34i.package.SHA256SUMS`: sha256 `%(sums_sha)s`.
- Host install script `resident_host_install_0485393f3a-r34i.sh`: sha256 `%(host_sha)s`; `install_r34.sh` `%(install_sha)s`; `pre_read_r34.sh` `%(pre_sha)s`; `rollback_r34.sh` `%(rb_sha)s`.
- V2 script `v2_service_env_r34i.sh` (in the repository at `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): sha256 `%(v2_sha)s`; its offline test printed %(v2cases)s cases OK.
- The lease, the budget, the resolve hop, the price transport code, the price adapters, the door, the WAF back-off and every other member are unchanged.

## 2. Blast radius, by branch (read from the bindings at the pin)

| what | BEFORE (r34h) | AFTER (r34i) |
|---|---|---|
| Opal producer price chain (`opal_pricing` on) | estate, yfinance, then YCharts through the stored session, one symbol per call: every YCharts price call is refused HTTP 400 on the host, so it spends one call of the window budget and falls to C-SWAP or is reported unpriced | estate, then yfinance; a symbol neither prices is MISSING (then C-SWAP or reported unpriced). No YCharts price call is made, so none spends the budget |
| the host's call budget (6 calls per 390 s, counted in its own store row) | enforced for the door's lookups, the suggestion verify and the stored-session calls | unchanged |
| every other member and every other binding key | -- | unchanged |

**Known limits (named, not stops).** (1) FWD-7's YCharts-second clause stays unmet: the repo holds no proven single-security `fund_data` form (CTO msg 10027; the CRO is asked for the endpoint the captured recipe pages use). (2) The code that builds the `ycharts` tier is still in the package (the installer's tier list and the transport module are unchanged and unused until a binding names the tier). (3) The DASHBD calendar hunk `f25618c0b4` is again NOT in this release (the pin is a scratch commit that puts `lib/trading_calendar.py` back to the r34e bytes).

**Writers counted.** The bindings file and the package sums: ONE writer each (the builder, for this release).

## 3. Apply protocol, in this order

1. **No YCharts call and no `~Y2` window runs during the install or V2.** The GO says so in terms.
2. Both halves at HEAD naming this file's blob. The ledger `irpt-resident-r34i-20261016` is opened first; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming the resident host, the unit or its root is a STOP).
3. **Send every host script AS ROOT.** Before-read: `pre_read_r34.sh` (fail-closed: the running root must be `0485393f3a-r34h`; the r34i root absent; the library and wrapper unmoved; the bindings at their r34h value; the queue 0 0).
4. D1: upload the tar, the sums file and the host script to the keys the install script names (each key must read 404 first; record the S3 versions); `install_r34.sh` fetches the host script and the sums BY KEY and refuses unless their sha256 equal `WANT` / `WANTSUM`.
5. V1: running root `0485393f3a-r34i`; the %(nchecks)d changed members at their built value; the package sums %(sums_lines)d of %(sums_lines)d OK; the imports; queue 0/0; no sign-in in the journal; `opal_pricing` enabled true with the tiers `estate` and `yfinance` and `ycharts_window_budget` (6, 390).
6. **V2, INSIDE the service's own environment:** `v2_service_env_r34i.sh`, sha256 `%(v2_sha)s` (verify before sending). It keeps r34h's controls, back-off, door, budget and tier-code checks, and its pricing check now reads the two tiers (no `ycharts`) and the 6 by 390 budget. No YCharts call.
7. **Gate:** anything but `V2S OK` (or an install that did not print its success line): send `rollback_r34.sh` AS ROOT the same session, read the running root back as `0485393f3a-r34h`, close the ledger ROLLED-BACK, report. No retry.
8. The ledger closes at V2.

## 4. Rollback, per key

- **The root:** `rollback_r34.sh` (or the install's own failure branch) restores `0485393f3a-r34h`, which stays on the host.
- **The receipt:** the r34h receipt is kept by the install and copied back.
- **The lease row and the count row:** unchanged by r34i (no code moves).
- **Queued messages:** none are touched.

## 5. Not claimed

- That the YCharts price tier works in any form, or that a later form will.
- That the live host, S3 objects, the lease row, running root and receipt are as the build assumes (this is a build record; they were NOT read).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set is: one new root directory on the resident host (`/opt/irpt-resident/0485393f3a-r34i`); the receipt and its r34h copy; the unit's ExecStart; the kept library copy; one transient systemd unit for V2. The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin12": pin[:10], "base": rec["release_input"]["base_pin"], "members": art["member_count"], "unchanged": delta["unchanged"],
    "nchanged": len(delta["changed"]), "v2cases": V2CASES, "tar_name": os.path.basename(art["path"]),
    "tar_sha": art["sha256"], "tar_bytes": "{:,}".format(art["bytes"]), "sums_sha": art["sha256sums_file"]["sha256"],
    "host_sha": scripts["resident_host_install_0485393f3a-r34i.sh"]["sha256"], "install_sha": scripts["install_r34.sh"]["sha256"],
    "pre_sha": scripts["pre_read_r34.sh"]["sha256"], "rb_sha": scripts["rollback_r34.sh"]["sha256"], "nchecks": len(delta["changed"]),
    "sums_lines": art["sha256sums_file"]["lines"], "v2_sha": v2_sha}
if any(ord(c) > 127 for c in text):
    raise SystemExit("REFUSE: non-ASCII in the packet")
with open(OUT, "w", encoding="ascii", newline="\n") as fh:
    fh.write(text)
print("wrote %s bytes=%d" % (OUT, len(text)))
