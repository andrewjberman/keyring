"""Write the release-34k never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r34k.py <RESIDENT_R34K_BUILD.json> <stage folder> <expected tarball sha256> <v2 script path> <packet out path> <merge short shas of AR-g-155,157,159> <V2_OFFLINE_TEST_R34K.txt record>

Every number in the packet is read from the record, the extracted tarballs, the V2 script and the reachability walk; nothing is typed. It refuses unless
ar_g160_checks.py verify passes on the same record with the same expected tarball sha256. ASCII only. Runs from the repository root. Writes the packet only.
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
CHECK = os.path.join(REPO, "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g160_checks.py")
REACH = os.path.join(REPO, "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/r32_reachability.py")
CODE_MEMBERS = ["intake/yfinance_check.py", "ycharts/research/price_adapter_ycharts.py", "ycharts/generate/resident_main.py"]
ADDED = ["ycharts/research/price_form_ycharts.py", "ycharts/research/ycharts_client.py"]
CLIENT_SRC = "infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py"
CELLS = sys.argv[6] if len(sys.argv) > 6 else "merged"
V2REC = open(sys.argv[7], encoding="ascii").read().split()
V2HEAD = [t.split("=", 1)[1] for t in V2REC if t.startswith("head=")][0]
V2CASES = [t.split("=", 1)[1] for t in V2REC if t.startswith("cases=")][0]

verify = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT_TAR], capture_output=True, text=True, cwd=REPO)
if verify.returncode != 0 or "AR-G160-OK" not in verify.stdout:
    raise SystemExit("REFUSE: the build does not verify: " + verify.stdout[-200:] + verify.stderr[-200:])
rec = json.load(open(REC, encoding="utf-8"))
pin, art, delta = rec["release_input"]["pin_full_sha"], rec["artifact"], rec["delta_vs_r34h"]
scripts = {s["name"]: s for s in rec["scripts"]}
if delta["changed"] != sorted(["SHA256SUMS", "reports/resident_bindings.json"] + CODE_MEMBERS) or delta["added"] != sorted(ADDED) or delta["removed"]:
    raise SystemExit("REFUSE: the delta is not the four expected changed members and the two added")
v2_bytes = open(V2_PATH, "rb").read()
if any(b > 127 for b in v2_bytes):
    raise SystemExit("REFUSE: the V2 script is not ASCII")
if subprocess.run(["bash", "-n", V2_PATH]).returncode != 0:
    raise SystemExit("REFUSE: the V2 script fails bash -n")
v2_sha = hashlib.sha256(v2_bytes).hexdigest()
at_head = subprocess.run(["git", "show", "HEAD:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/v2_service_env_r34k.sh"], capture_output=True, cwd=REPO, check=True).stdout
if hashlib.sha256(at_head).hexdigest() != v2_sha:
    raise SystemExit("REFUSE: the V2 script on disk is not the committed one")
client_blob = subprocess.run(["git", "rev-parse", "%s:%s" % (pin, CLIENT_SRC)], capture_output=True, text=True, cwd=REPO, check=True).stdout.strip()
tmp = tempfile.mkdtemp(prefix="r34k_packet_")
tarfile.open(art["path"]).extractall(tmp + "/x34")
client_sha = hashlib.sha256(open(tmp + "/x34/ycharts/research/ycharts_client.py", "rb").read()).hexdigest()
pin_parent = subprocess.run(["git", "rev-parse", pin + "^"], capture_output=True, text=True, cwd=REPO, check=True).stdout.strip()
if V2HEAD != pin_parent:
    raise SystemExit("REFUSE: the V2 offline test record was made on %s, not on the pin's parent %s (the merged tree)" % (V2HEAD, pin_parent))
smoke_lines = rec.get("import_smoke") or []
if not smoke_lines or " fail=0 " not in smoke_lines[0] + " ":
    raise SystemExit("REFUSE: the record carries no clean import smoke")
lives = {}
for member in CODE_MEMBERS + ADDED:
    reach = subprocess.run([sys.executable, "-I", REACH, tmp + "/x34", member], capture_output=True, text=True, check=True).stdout.splitlines()
    lives[member] = "LIVE" if reach[1].endswith("REACHABLE") and not reach[1].endswith("not reachable") else "not reachable"
WHAT = {"ycharts/generate/resident_main.py": "the resident's entry module puts lib on sys.path with the other package directories, so intake/yfinance_check.py can import lib/trading_calendar.py in the service (cell AR-g-159; r34j's V2 failed because lib was not on the path)",
        "intake/yfinance_check.py": "the door's checker judges a symbol by its last FINITE close at or before the T-1 trading-day frontier of lib/trading_calendar.py (`now=` injectable): a null newest row, a Saturday's Friday row and the run's own day are no longer the answer (cell AR-g-157)",
        "ycharts/research/price_adapter_ycharts.py": "the YCharts price reader asks for the path price_form_ycharts builds and sends it with no params (cell AR-g-155)",
        "ycharts/research/price_form_ycharts.py": "NEW: calls the estate client's own fund_data(symbol, calc) on a subclass that reads no secret and sends nothing, and returns the path and query (calc price; level for a ^ index) (cell AR-g-155)",
        "ycharts/research/ycharts_client.py": "NEW: the estate client infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py at its pinned blob, unedited; only its fund_data builder is called, never its sending (CTO msg 10079)"}
member_rows = "\n".join("| `%s` | %s (%s in the resident's runtime, static import walk) | %s |" % (m, "ADDED" if m in ADDED else "changed", lives[m], WHAT[m]) for m in CODE_MEMBERS + ADDED)
text = """# Never-widen sign-off packet -- r34k: the resident r34h -> r34k at pin %(pin12)s (the YCharts price tier on the estate client's working form; the door's checker reads the last finite close at the T-1 frontier)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-17. **Applier:** `0.7.0_AE_CloudOps~IB2` (rule 34, CTO msg 9561).
**Authority:** CTO msgs 10166 and 10172 (r34j was rolled back at V2: the door's checker imports lib/trading_calendar.py and lib was not on the service's sys.path; r34k puts lib on the path ONCE in resident_main.py, adds a package-layout import smoke over the BUILT tree, runs the V2 offline test on the merged tree at the pin and records the order, and has V2 print the exception class; no retry-once), 10040 (r34k re-adds the tier by CALLING the estate builder), 10079 (option C accepted with two pinning tests: the SPY path byte-equal to IB2's HTTP 200 request; a signature pin on fund_data and _request; `ycharts_client.py` enters the package at its pinned blob, the pin printed here), 10112 and 10122 (the door's checker is the defect behind r34i's V2 failure; fix it in r34k with tests for a null newest row, a Saturday and a holiday; the pricing `as_of` alignment is a separate pair). The reads: `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34h/PRICE_FORM_READ.txt` (IB2 msg 10066: SPY, the estate form, HTTP 200, 1,256 points) and `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34i/A_AFTER_R34I.txt` (r34i rolled back, V2S FAIL SPY LAST_CLOSE_NOT_FINITE). Cells %(cells)s. The CRO's research: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261016_YCHARTS_SINGLE_TICKER_PRICE_SERIES_FORM.md` @c9f3005376.
**One move:** D1, the install of one new root on the resident host. Three code members change, two are added and the bindings' provenance changes; the tiers (`estate, yfinance, ycharts`) and the budget (6 calls, 390 s) are r34h's. No IAM, Lambda, queue, table or schema moves; no new vendor call path before the first price call a job makes.

## 1. What ships

Package pin `%(pin)s`; base pin `%(base)s`; built by `r34k_build.py` over the tools at that pin, BUILD ONLY, over the RUNNING r34h root (tarball sha256 `60cc8d1d68627c993121df7eca946a40046f1d7f63ddfd2968f83e27077b93c0`). **%(members)d members**: %(unchanged)d identical to r34h, **%(nchanged)d changed**, **%(nadded)d added**, 0 removed.

| member | vs r34h | what changes |
|---|---|---|
%(member_rows)s
| `reports/resident_bindings.json` | changed | `provenance.package_pin`, and the files-from list's count and sha256 (it grew by one line, `price_form_ycharts.py`); the verifier proves no other key moved |
| `SHA256SUMS` | changed | the package sums, replaced |

**The estate client's pin.** `%(client_src)s` enters the package as `ycharts/research/ycharts_client.py` from the pin: git blob `%(client_blob)s`, sha256 `%(client_sha)s`. It is not edited. The module calls only `YChartsClient.fund_data`; the client's own sending (its credentials secret, cookie header, `urllib`) is never reached, because the subclass skips `__init__` and replaces `_request`. A test pins the signatures of `fund_data` and `_request`: a change to either fails the suite.

**Verification before this packet (CTO msg 10172).** (a) THE IMPORT SMOKE over the built tree, `python -I`, `sys.path` set from the built `resident_main.py`'s own tuple, every module the static walk marks LIVE imported: %(smoke)s. The verifier re-ran it. At r34j the same smoke read `live=82 imported=80 fail=2` (lib/opal_naming.py and lib/trading_calendar.py: ModuleNotFoundError). (b) THE V2 OFFLINE TEST, %(v2cases)s cases, was run on HEAD `%(v2head)s`, which is the pin's parent, AFTER `AR-g-155`, `AR-g-157` and `AR-g-159` merged (record `V2_OFFLINE_TEST_R34K.txt` in this folder; at r34j the test was run before AR-g-157 merged and not after). It runs with PYTHONPATH removed and a copy of the real `resident_main.py` and `lib/trading_calendar.py` in the fake root, and holds a case that fails V2 with the first-ask exception class when `lib` is off the tuple.

**Artifacts** (staged outside the repository; nothing uploaded):
- Tar `%(tar_name)s`: sha256 `%(tar_sha)s`, %(tar_bytes)s bytes, %(members)d members.
- Package sums `irpt-resident-0485393f3a-r34k.package.SHA256SUMS`: sha256 `%(sums_sha)s`.
- Host install script `resident_host_install_0485393f3a-r34k.sh`: sha256 `%(host_sha)s`; `install_r34.sh` `%(install_sha)s`; `pre_read_r34.sh` `%(pre_sha)s`; `rollback_r34.sh` `%(rb_sha)s`.
- V2 script `v2_service_env_r34k.sh` (in the repository at `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): sha256 `%(v2_sha)s`; its offline test printed %(v2cases)s cases OK (see above); on a first failure it prints `V2S FIRST-ASK EXCEPTION <class>`.
- The lease, the budget, the resolve hop, the price transport, the door's resolver and every other member are unchanged.

## 2. Blast radius, by branch (read from the code at the pin)

| what | BEFORE (r34h) | AFTER (r34k) |
|---|---|---|
| the door's check of a held symbol (`intake/yfinance_check.py`) | the NEWEST Yahoo row decides: a null close reads NOT_KEPT (r34i's V2 hit it at 00:50Z on a Saturday), and a row dated after T-1 is read as the answer | the last FINITE close dated at or before `prev_trading_day(expected_last_trading_day(now))`; rows after that day are ignored; an only-non-finite history is still NOT_KEPT `LAST_CLOSE_NOT_FINITE`, a last finite close of zero or less NOT_POSITIVE, rows only after the frontier NOT_KEPT `NO_ROWS`; a calendar error is CHECK_FAILED, never NOT_KEPT |
| the YCharts price tier's request | `/charts/fund_data.json?securities=id:SPY,include:true,&zoom=max`, refused HTTP 400 (IB2 PRICE_PROBE), so each price call that reached the tier spent one call of the window budget for nothing | the estate client's own 41-parameter quote-page request, calc price (level for a `^` index): 760 characters for SPY, byte-equal to the request that answered HTTP 200 (IB2 PRICE_FORM_READ); still one symbol per call under the same lease and budget |
| a symbol YCharts prices | -- | the served levels are PRICE levels, so the chained series is a price return, not a total return |
| the host's call budget, the lease row, the count row, the resolve hop, the tiers list | 6 calls per 390 s | unchanged |

**Known limits (named, not stops).** (1) ONE SAMPLE: the estate form was read once, for SPY, signed in (and 67 of 67 in May for the estate client's pull); other symbols, the signed-out call and ETFs other than SPY are unmeasured. (2) PRICE, NOT TOTAL RETURN: whether a report line must carry that basis next to `source: ycharts` is a PRD question (C-PRICES names the source only). (3) THE CALENDAR'S FALLBACK covers 2010 to 2027 (`pandas_market_calendars` is absent on the host): a date outside it raises, which the checker reads as CHECK_FAILED; regenerate with `lib/tests/gen_nyse_closures.py --write` before 2028. (4) THE PRICING `as_of` is still the weekday rule (`resident_installed.py:379-385`: Saturday gives Friday, the calendar gives Thursday); it moves report as-of dates and is its own pair (CTO msg 10122, row IRPT_ANLREQ-D2-S163). (5) The DASHBD calendar hunk `f25618c0b4` is again NOT in this release (the pin is a scratch commit that puts `lib/trading_calendar.py` back to the r34e bytes; `prev_trading_day` and `expected_last_trading_day` exist in those bytes).

**Writers counted.** Each changed or added member: ONE writer (the builder, for this release). The bindings file and the package sums: ONE (the builder).

## 3. Apply protocol, in this order

1. **No YCharts call and no `~Y2` window runs during the install or V2.** The GO says so in terms.
2. Both halves at HEAD naming this file's blob. The ledger `irpt-resident-r34k-20261017` is opened first; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming the resident host, the unit or its root is a STOP).
3. **Send every host script AS ROOT.** Before-read: `pre_read_r34.sh` (fail-closed: the running root must be `0485393f3a-r34h`; the r34k root absent; the library and wrapper unmoved; every changed member at its r34h value and the added members absent; the queue 0 0).
4. D1: upload the tar, the sums file and the host script to the keys the install script names (each key must read 404 first; record the S3 versions); `install_r34.sh` fetches the host script and the sums BY KEY and refuses unless their sha256 equal `WANT` / `WANTSUM`.
5. V1: running root `0485393f3a-r34k`; the %(nchecks)d changed or added members at their built value; the package sums %(sums_lines)d of %(sums_lines)d OK; the imports (including `price_form_ycharts` and `ycharts_client`); queue 0/0; no sign-in in the journal; `opal_pricing` enabled true with the tiers `estate, yfinance, ycharts` and `ycharts_window_budget` (6, 390).
6. **V2, INSIDE the service's own environment:** `v2_service_env_r34k.sh`, sha256 `%(v2_sha)s` (verify before sending). It keeps r34h's controls, back-off, door, pricing and budget checks, and its TIER check now reads the estate-form SPY path (760 characters, sha256 `96a5d1b9...e383d`, built by the shipped modules from the shipped estate client, no network). The SPY and ZQXWVK reads use the shipped checker, so they follow the T-1 rule. No YCharts call.
7. **Gate:** anything but `V2S OK` (or an install that did not print its success line): send `rollback_r34.sh` AS ROOT the same session, read the running root back as `0485393f3a-r34h`, close the ledger ROLLED-BACK, report. No retry.
8. The ledger closes at V2.

**Live proof is a separate act:** one priced request that reaches the YCharts tier (a symbol neither the estate nor Yahoo prices), read for its status, its rows and its source field.

## 4. Rollback, per key

- **The root:** `rollback_r34.sh` (or the install's own failure branch) restores `0485393f3a-r34h`, which stays on the host.
- **The receipt:** the r34h receipt is kept by the install and copied back.
- **The lease row and the count row:** unchanged by r34k (no lease code moves).
- **Queued messages:** none are touched; a message received after a rollback is served by r34h.

## 5. Not claimed

- That the YCharts price tier answers for any symbol but SPY, or without the signed-in session, or that it keeps answering.
- That a price return is what a report should print where a total return is expected.
- That the live host, S3 objects, the lease row, running root and receipt are as the build assumes (this is a build record; they were NOT read).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-17, on this packet's bytes at the commit that carries it. The write set is: one new root directory on the resident host (`/opt/irpt-resident/0485393f3a-r34k`); the receipt and its r34h copy; the unit's ExecStart; the kept library copy; one transient systemd unit for V2. The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin12": pin[:10], "base": rec["release_input"]["base_pin"], "members": art["member_count"], "unchanged": delta["unchanged"],
    "nchanged": len(delta["changed"]), "nadded": len(delta["added"]), "member_rows": member_rows, "cells": CELLS, "v2cases": V2CASES, "v2head": V2HEAD[:10], "smoke": "; ".join(smoke_lines), "tar_name": os.path.basename(art["path"]),
    "tar_sha": art["sha256"], "tar_bytes": "{:,}".format(art["bytes"]), "sums_sha": art["sha256sums_file"]["sha256"],
    "host_sha": scripts["resident_host_install_0485393f3a-r34k.sh"]["sha256"], "install_sha": scripts["install_r34.sh"]["sha256"],
    "pre_sha": scripts["pre_read_r34.sh"]["sha256"], "rb_sha": scripts["rollback_r34.sh"]["sha256"], "nchecks": len(delta["changed"]) + len(delta["added"]),
    "sums_lines": art["sha256sums_file"]["lines"], "v2_sha": v2_sha, "client_src": CLIENT_SRC, "client_blob": client_blob, "client_sha": client_sha}
if any(ord(c) > 127 for c in text):
    raise SystemExit("REFUSE: non-ASCII in the packet")
with open(OUT, "w", encoding="ascii", newline="\n") as fh:
    fh.write(text)
print("wrote %s bytes=%d" % (OUT, len(text)))
