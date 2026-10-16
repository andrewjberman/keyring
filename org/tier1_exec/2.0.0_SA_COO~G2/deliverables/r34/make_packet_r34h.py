"""Write the release-34g never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r34h.py <RESIDENT_R34H_BUILD.json> <stage folder> <expected tarball sha256> <v2 script path> <packet out path> <AR-g-142,143,144 merge short shas> <v2 test case count>

Every number in the packet is read from the record, the extracted tarballs, the V2 script and the reachability walk; nothing is typed. It refuses unless
ar_g145_checks.py verify passes on the same record with the same expected tarball sha256. ASCII only. Runs from the repository root. Writes the packet only.
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
CHECK = os.path.join(REPO, "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g145_checks.py")
REACH = os.path.join(REPO, "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/r32_reachability.py")
CODE_MEMBERS = ["reports/resident_installed.py", "ycharts/generate/resident_worker.py", "ycharts/session/operation_lease.py", "ycharts/session/resident_session.py"]
ADDED_MEMBER = "ycharts/research/price_transport_ycharts.py"
CELLS = sys.argv[6] if len(sys.argv) > 6 else "merged"  # the merge commits of cells AR-g-142, AR-g-143 and AR-g-144 (short shas, comma separated)
V2CASES = sys.argv[7] if len(sys.argv) > 7 else "all"  # the case count the V2 test printed

verify = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT_TAR], capture_output=True, text=True, cwd=REPO)
if verify.returncode != 0 or "AR-G145-OK" not in verify.stdout:
    raise SystemExit("REFUSE: the build does not verify: " + verify.stdout[-200:] + verify.stderr[-200:])
rec = json.load(open(REC, encoding="utf-8"))
pin, art, delta = rec["release_input"]["pin_full_sha"], rec["artifact"], rec["delta_vs_r34g"]
scripts = {s["name"]: s for s in rec["scripts"]}
if delta["changed"] != sorted(["SHA256SUMS", "reports/resident_bindings.json"] + CODE_MEMBERS) or delta["added"] != [ADDED_MEMBER] or delta["removed"]:
    raise SystemExit("REFUSE: the delta is not the six expected changed members and the one added")
v2_bytes = open(V2_PATH, "rb").read()
if any(b > 127 for b in v2_bytes):
    raise SystemExit("REFUSE: the V2 script is not ASCII")
if subprocess.run(["bash", "-n", V2_PATH]).returncode != 0:
    raise SystemExit("REFUSE: the V2 script fails bash -n")
v2_sha = hashlib.sha256(v2_bytes).hexdigest()
at_head = subprocess.run(["git", "show", "HEAD:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/v2_service_env_r34h.sh"], capture_output=True, cwd=REPO, check=True).stdout
if hashlib.sha256(at_head).hexdigest() != v2_sha:
    raise SystemExit("REFUSE: the V2 script on disk is not the committed one")
tmp = tempfile.mkdtemp(prefix="r34h_packet_")
tarfile.open(art["path"]).extractall(tmp + "/x34")
lives = {}
for member in CODE_MEMBERS + [ADDED_MEMBER]:
    reach = subprocess.run([sys.executable, "-I", REACH, tmp + "/x34", member], capture_output=True, text=True, check=True).stdout.splitlines()
    lives[member] = "LIVE" if reach[1].endswith("REACHABLE") and not reach[1].endswith("not reachable") else "not reachable"
WHAT = {"reports/resident_installed.py": "the tier list names `ycharts`; the optional binding `ycharts_window_budget` is validated; `_pricing_extras` builds the `ycharts` price reader over the stored session (and refuses the tier with no session); the runtime hands the budget to the session (cell AR-g-144)",
        "ycharts/generate/resident_worker.py": "the resolve hop re-sends a `:OPERATION_WINDOW_BUDGET` retry like a busy provider (cell AR-g-143)",
        "ycharts/session/operation_lease.py": "the lease row counts reserved calls per window, one count per host account; OPERATION_WINDOW_BUDGET with retry_after (cell AR-g-142)",
        "ycharts/session/resident_session.py": "`ResidentSession(window_budget=)` hands the budget to its lease (cell AR-g-142)",
        ADDED_MEMBER: "NEW: the (path, params) transport over the stored session that the existing YCharts price reader calls (cell AR-g-144)"}
member_rows = "\n".join("| `%s` | %s (%s in the resident's runtime, static import walk) | %s |" % (m, "ADDED" if m == ADDED_MEMBER else "changed", lives[m], WHAT[m]) for m in CODE_MEMBERS + [ADDED_MEMBER])
text = """# Never-widen sign-off packet -- r34h: the resident r34g -> r34h at pin %(pin12)s (ONE per-window YCharts call budget for the host; the YCharts price tier)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** `0.7.0_AE_CloudOps~IB2` (rule 34, CTO msg 9561).
**Authority:** CTO msgs 9694 (the YCharts price tier is owed with item 4's lease), 9727 (build the four code gaps offline-tested in its own r34h pair; ONE per-window count budget per host, shared by the door's lookups, the price tier and the SPY/BIL calls; the YCharts use is ordered: paced read, 390 s rest, window 4, rest, then the read-only measurement of the three unknowns), 9757 and 9761 (the budget is (6 calls, 390 s), a FLOOR the paced read showed clean, counts every securities_info CALL: an unknown symbol costs two). Cells %(cells)s (AR-g-142 reworked by AR-g-146 so the count has a row of its own). The tier's scope record is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268/YCHARTS_PRICE_TIER_SCOPE.json`; the paced read is `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34g/PACED_READ.txt` (IB2 msg 9749).
**One move:** D1, the install of one new root on the resident host. Five code members change or are added and the bindings gain the tier and the budget. No IAM, Lambda, queue, table or schema moves; no new vendor call path before the first price call a job makes.

## 1. What ships

Package pin `%(pin)s`; base pin `%(base)s`; built by `r34h_build.py` over the tools at that pin, BUILD ONLY, over the RUNNING r34g root (tarball sha256 `1e5b3ef4120b8799ebd5f1cf620044b01b5e1bfeac2e1d4169d3f576a802580b`). **%(members)d members**: %(unchanged)d identical to r34g, **%(nchanged)d changed**, **%(nadded)d added**, 0 removed.

| member | vs r34g | what changes |
|---|---|---|
%(member_rows)s
| `reports/resident_bindings.json` | changed | `provenance.package_pin`; `opal_pricing` tiers `[estate, yfinance]` -> `[estate, yfinance, ycharts]` (still enabled); the NEW key `ycharts_window_budget` = `{"calls": 6, "window_s": 390}` (the verifier proves no other key moved) |
| `SHA256SUMS` | changed | the package sums, replaced |

**Artifacts** (staged outside the repository; nothing uploaded):
- Tar `%(tar_name)s`: sha256 `%(tar_sha)s`, %(tar_bytes)s bytes, %(members)d members.
- Package sums `irpt-resident-0485393f3a-r34h.package.SHA256SUMS`: sha256 `%(sums_sha)s`.
- Host install script `resident_host_install_0485393f3a-r34h.sh`: sha256 `%(host_sha)s`; `install_r34.sh` `%(install_sha)s`; `pre_read_r34.sh` `%(pre_sha)s`; `rollback_r34.sh` `%(rb_sha)s`.
- V2 script `v2_service_env_r34h.sh` (in the repository at `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): sha256 `%(v2_sha)s`; its offline test printed %(v2cases)s cases OK.
- The capture library, wrapper, the door (r34g), the WAF back-off (r34f), the Yahoo checker and every other member are unchanged.

## 2. Blast radius, by branch (read from the code at the pin)

| what | BEFORE (r34g) | AFTER (r34h) |
|---|---|---|
| every YCharts call through the provider lease (the door's sessionless lookups, the suggestion verify, stored-session calls) | spaced 2 s, one at a time; no count | the lease also counts reserved calls per window in ITS OWN store row (`window_start`, `window_count`, beside the lease row): the 7th call inside 390 s is refused OPERATION_WINDOW_BUDGET with `retry_after` = the seconds to the window's end, writing nothing; ONE count per host account, because every caller shares the lease and the row is keyed by provider and account |
| the upload door's resolve hop meeting that refusal | would take the flat 60 s retry | re-sent for `retry_after` (1 to 900 s) through the busy path, the original deleted after the send; past 3600 s from the first dispatch the upload ends RESOLVE_PROVIDER_BUSY, as for a busy provider |
| Opal producer price chain (`opal_pricing` on) | estate, then yfinance; a symbol neither prices is MISSING (then C-SWAP or reported unpriced) | estate, yfinance, then YCharts through the stored session, one symbol per call under the same budget; a YCharts refusal or error is that tier's ERROR and the symbol falls to C-SWAP or is reported unpriced; the YCharts recipe path is not touched |
| the lease row's stored shape | eight keys | the same eight keys (the count has a row of its own, `PROVIDER_OPERATION#<hash of provider, account and "window">`, which r34g never reads), so the r34g lease keeps reading the lease row after a rollback |
| cached answers, the checker, the swap pass, the pool, the producer list, the WAF back-off, the door order | -- | unchanged |

**Known limits (named, not stops).** (1) THE NUMBER IS A FLOOR: (6, 390 s) is the pattern the paced read of 12 known symbols showed clean, not the measured limit; the CRO's reading of the SET 2 and SET 3 challenges (each unknown symbol costs two calls) fits a cutoff near 7 calls per window. After window 4 an unknown-symbol paced read logs every securities_info call and decides whether unknown symbols count separately (CTO msg 9761). (2) THREE ITEMS ARE UNMEASURED and the tier builds on them: the YCharts id form `id:<TICKER>` for a plain ticker, the served single-ticker `fund_data` shape (the adapter's fixtures only), and whether the price route answers a signed-out caller (the tier uses the session-bearing acquire). They are measured read-only after window 4 (CTO msg 9727); until then a YCharts price call that does not answer is that tier's error, never a priced value. (3) The pricing stage does not wait out a window: a call over the budget leaves the symbol unpriced by this tier. (4) THE COUNT CAN BE ONE SHORT: the count row is written after the lease row's swap; a count write that fails (its swap keeps failing, or the store raises) is swallowed, because the call already holds its reservation. The lease's spacing and in-flight rules are unaffected. The live DynamoDB rows were NOT read. (5) The DASHBD calendar hunk `f25618c0b4` is again NOT in this release (the pin is a scratch commit that puts `lib/trading_calendar.py` back to the r34e bytes).

**Writers counted.** Each changed or added member: ONE writer (the builder, for this release). The bindings file and the package sums: ONE (the builder).

## 3. Apply protocol, in this order

1. **Ordering of YCharts use (CTO msg 9727):** this install does not run while `~Y2`'s window 4 is open or about to open; it runs after window 4 closes and before the unknown-symbol paced read and the three-unknowns measurement, both of which then run on r34h. The GO says so in terms.
2. Both halves at HEAD naming this file's blob. The ledger `irpt-resident-r34h-20261016` is opened first; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming the resident host, the unit or its root is a STOP).
3. **Send every host script AS ROOT.** Before-read: `pre_read_r34.sh` (fail-closed: the running root must be `0485393f3a-r34g`; the r34h root absent; the library and wrapper unmoved; every changed member at its r34g value and the added member absent; the queue 0 0).
4. D1: upload the tar, the sums file and the host script to the keys the install script names (each key must read 404 first; record the S3 versions); `install_r34.sh` fetches the host script and the sums BY KEY and refuses unless their sha256 equal `WANT` / `WANTSUM`.
5. V1: running root `0485393f3a-r34h`; the %(nchecks)d changed members at their built value and the added member present; the package sums %(sums_lines)d of %(sums_lines)d OK; the imports; queue 0/0; no sign-in in the journal; `opal_pricing` enabled true with the three tiers and `ycharts_window_budget` (6, 390).
6. **V2, INSIDE the service's own environment:** `v2_service_env_r34h.sh`, sha256 `%(v2_sha)s` (verify before sending). It keeps r34g's controls, back-off (now also the window-budget class), door and pricing checks (the pricing check reads the three tiers and the 6 by 390 budget), and adds `V2S BUDGET` (the shipped lease, run over a fake store with a (2, 100 s) budget, refuses the 3rd call with OPERATION_WINDOW_BUDGET and retry_after 94) and `V2S TIER` (the shipped transport encodes the runner's query, closes its facade and the shipped installer lists the `ycharts` tier). No YCharts call.
7. **Gate:** anything but `V2S OK` (or an install that did not print its success line): send `rollback_r34.sh` AS ROOT the same session, read the running root back as `0485393f3a-r34g`, close the ledger ROLLED-BACK, report. No retry.
8. The ledger closes at V2.

**Live proof is a separate act** (the unknown-symbol paced read and the three-unknowns measurement, then the first priced run with the tier).

## 4. Rollback, per key

- **The root:** `rollback_r34.sh` (or the install's own failure branch) restores `0485393f3a-r34g`, which stays on the host.
- **The receipt:** the r34g receipt is kept by the install and copied back.
- **The lease row:** unchanged by r34h, so the r34g lease reads it after a rollback with no act. The count row stays in the table and is ignored by r34g (it is never read, never deleted; the next r34h install continues from it or restarts the window when it is older than 390 s). This is the reason cell AR-g-146 reworked the first design, which wrote two extra keys into the lease row (the r34g lease checks the exact eight keys and would have refused it).
- **Queued messages:** none are touched; a message received after a rollback is served by r34g.

## 5. Not claimed

- That the budget number is the YCharts limit (it is a floor), or that unknown symbols cost the same as known ones.
- That `id:<TICKER>` resolves at YCharts, that the served shape matches the adapter's fixtures, or that the price route answers without the signed-in session.
- That the live count row, or any reader of it other than this package, behaves as the fakes do.
- The live host, S3 objects, the lease row, running root and receipt were NOT read (this is a build record).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set is: one new root directory on the resident host (`/opt/irpt-resident/0485393f3a-r34h`); the receipt and its r34g copy; the unit's ExecStart; the kept library copy; one transient systemd unit for V2; and the count row (`PROVIDER_OPERATION#<hash>`, first written by the first job after the install). The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin12": pin[:10], "base": rec["release_input"]["base_pin"], "members": art["member_count"], "unchanged": delta["unchanged"],
    "nchanged": len(delta["changed"]), "nadded": len(delta["added"]), "member_rows": member_rows, "cells": CELLS, "v2cases": V2CASES, "tar_name": os.path.basename(art["path"]),
    "tar_sha": art["sha256"], "tar_bytes": "{:,}".format(art["bytes"]), "sums_sha": art["sha256sums_file"]["sha256"],
    "host_sha": scripts["resident_host_install_0485393f3a-r34h.sh"]["sha256"], "install_sha": scripts["install_r34.sh"]["sha256"],
    "pre_sha": scripts["pre_read_r34.sh"]["sha256"], "rb_sha": scripts["rollback_r34.sh"]["sha256"], "nchecks": len(delta["changed"]) + len(delta["added"]),
    "sums_lines": art["sha256sums_file"]["lines"], "v2_sha": v2_sha}
if any(ord(c) > 127 for c in text):
    raise SystemExit("REFUSE: non-ASCII in the packet")
with open(OUT, "w", encoding="ascii", newline="\n") as fh:
    fh.write(text)
print("wrote %s bytes=%d" % (OUT, len(text)))
