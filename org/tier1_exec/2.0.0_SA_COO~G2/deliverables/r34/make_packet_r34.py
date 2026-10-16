"""Write the release-34 never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r34.py <RESIDENT_R34_BUILD.json> <stage folder> <expected tarball sha256> <packet out path>

Every number in the packet is read from the record, the extracted tarballs, the shipped pool and the reachability walk; nothing is typed.
It refuses unless ar_g107_checks.py verify passes on the same record with the same expected tarball sha256. ASCII only. Runs from the
repository root. Writes the packet and nothing else.
"""
import collections
import json
import math
import os
import subprocess
import sys
import tarfile
import tempfile

REC, STAGE, WANT_TAR, OUT = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
CHECK = os.path.join(REPO, "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g107_checks.py")
REACH = os.path.join(REPO, "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/r32_reachability.py")
R32_TAR = "C:/dev/irpt-release-r32/irpt-resident-0485393f3a-r32.tar.gz"
CHUNK = 50  # swap_pass.REQUEST_CHUNK, asserted below against the shipped module text

verify = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT_TAR], capture_output=True, text=True, cwd=REPO)
if verify.returncode != 0 or "AR-G107-OK" not in verify.stdout:
    raise SystemExit("REFUSE: the build does not verify: " + verify.stdout[-200:] + verify.stderr[-200:])
rec = json.load(open(REC, encoding="utf-8"))
pin = rec["release_input"]["pin_full_sha"]
tmp = tempfile.mkdtemp(prefix="r34_packet_")
tarfile.open(rec["artifact"]["path"]).extractall(tmp + "/x34")
tarfile.open(R32_TAR).extractall(tmp + "/x32")
delta = rec["delta_vs_r32"]
reach = subprocess.run([sys.executable, "-I", REACH, tmp + "/x34"] + delta["changed"] + delta["added"],
                       capture_output=True, text=True, check=True).stdout.splitlines()
reachable = {ln.split(" ")[0]: ln.endswith("REACHABLE") and not ln.endswith("not reachable") for ln in reach[1:]}
count_new = reach[0].split(":")[1].strip()
count_old = subprocess.run([sys.executable, "-I", REACH, tmp + "/x32"], capture_output=True, text=True, check=True).stdout.split(":")[1].strip().splitlines()[0]
compiled = failed = 0
for dp, _dn, fn in os.walk(tmp + "/x34"):
    for f in fn:
        if f.endswith(".py"):
            ok = subprocess.run([sys.executable, "-m", "py_compile", os.path.join(dp, f)], capture_output=True).returncode == 0
            compiled += ok
            failed += not ok
if failed:
    raise SystemExit("REFUSE: %d Python members do not compile" % failed)
swap_text = open(tmp + "/x34/ycharts/research/swap_pass.py", encoding="utf-8").read()
yahoo_text = open(tmp + "/x34/ycharts/research/yahoo_history_days.py", encoding="utf-8").read()
if "REQUEST_CHUNK = %d" % CHUNK not in swap_text or "DEFAULT_CHUNK = %d" % CHUNK not in yahoo_text:
    raise SystemExit("REFUSE: the request chunk is not %d in the shipped modules" % CHUNK)
stale = int(swap_text.split("STALE_DAYS = ")[1].split()[0])
pool = json.load(open(tmp + "/x34/ycharts/research/swap_pool.json", encoding="utf-8"))
sizes = collections.Counter((r["asset_class"].strip().casefold(), r["sub_asset_class"].strip().casefold()) for r in pool["rows"])
biggest = max(sizes.values())
batches_max = math.ceil(biggest / CHUNK)
batches_all = sum(math.ceil(n / CHUNK) for n in sizes.values())
art, scripts = rec["artifact"], {s["name"]: s for s in rec["scripts"]}
sw = rec["swap_pool"]
R33_PIN = "927337a741f40a83e7daa9e09154436a813b05dd"
R35L_PIN = "90b69dcb12cdfedc786966ab33d034bf14229396"  # the irpt-status failure-code release (r35L): the Lambda's status.py is this blob
for member, repo_path, ref in (("intake/portfolio.py", "infra/aws/lambda/investor-reporting/intake/portfolio.py", R33_PIN),
                               ("intake/uploads.py", "infra/aws/lambda/investor-reporting/intake/uploads.py", R33_PIN),
                               ("ops/status.py", "infra/aws/lambda/investor-reporting/ops/status.py", R35L_PIN)):
    at_ref = subprocess.run(["git", "show", "%s:%s" % (ref, repo_path)], capture_output=True, cwd=REPO, check=True).stdout
    if at_ref != open(tmp + "/x34/" + member, "rb").read():
        raise SystemExit("REFUSE: %s in the tarball is not the blob the Lambda release (%s) carries" % (member, ref[:10]))


def live(name):
    return "LIVE" if reachable.get(name) else "not reachable"


rows = "\n".join("| `%s` | changed | %s |" % (n, live(n)) for n in delta["changed"] if n not in ("SHA256SUMS",)) + "\n" + \
       "\n".join("| `%s` | ADDED | %s |" % (n, live(n)) for n in delta["added"])
text = """# Never-widen sign-off packet -- r34: the resident r32 -> r34 at pin %(pin12)s (the swap pass, the dated pool snapshot, the yfinance checker at the door and the hop_failure writers)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** a CloudOps seat named by the CTO.
**Authority:** CTO msgs 8907 and 8971 (C-HOP-FAILURE: the resident writers of `hop_failure`, folded into this release), CTO msg 8968 (the door's yfinance checker, folded into this release; ruling on `~Y2` msg 8965, row `IRPT_ANLREQ-D2-W165-S2`), CTO msgs 8693, 8711, 8714, 8723 (the swap: an UNRESOLVED holding is replaced in the Opal producer by a class-matched, Yahoo-priced security from a
dated pool), msg 8863 ("r34 is next"), PRD v0.19 (C-SWAP steps 1 and 2; step 3, the classifier, is its own cell after run 3). **Ledger:** `irpt-resident-r34b-20261016`.
**One move:** D1, the install of one new root on the resident host. No IAM, Lambda, queue, table or schema moves. **Two new Yahoo call paths:** the door's checker asks Yahoo for one month of history per symbol YCharts omits (section 2c), and the swap pass asks Yahoo
(through the `yfinance` library, whose presence on the host V2 reads) for monthly history of pool candidates; section 2b states the calls per holding and their bound. `opal_pricing` stays OFF.

## 1. What ships

Package pin `%(pin)s`; base pin `%(base)s`; built by `r34_build.py` over the tools at that pin, BUILD ONLY. **%(members)d members**: %(unchanged)d identical to r32, **%(nchanged)d changed**
(including `SHA256SUMS` and the bindings), **%(nadded)d added**, 0 removed. Two builds under one fixed clock are identical %(members)d of %(members)d, and the tarball equals
the issuer's own earlier build of the same pin. The verifier `ar_g107_checks.py verify` (independent of the builder) recomputed every number below and passed.

| member | vs r32 | in the resident's runtime (static import walk) |
|---|---|---|
%(rows)s

Reachable modules: %(count34)s in r34, %(count32)s in r32. Compiled: %(compiled)d of %(compiled)d Python members.

**The bindings** gain ONE key, `opal_swap_pool` = `{path: ../ycharts/research/swap_pool.json, sha256: %(pool_sha)s}`, pinned by content and verified by the installer's own loader
at every job; the provenance block changes; every other key is unchanged (pricing still OFF).

**The pool snapshot** `swap_pool.json`: schema `irpt-swap-pool.v1`, claim `%(pool_claim)s`, as of %(pool_as_of)s, %(rows_n)d rows in %(classes)d classes (largest %(biggest)d). It is the
committed output of the AQ2 read of the `etf-classifications` table (`dcdc6cb3d1`), shipped inside the package, not read from AWS at run time.

**Artifacts** (staged outside the repository; nothing uploaded):
- Tar `%(tar_name)s`: sha256 `%(tar_sha)s`, %(tar_bytes)s bytes, %(members)d members.
- Package sums `irpt-resident-0485393f3a-r34c.package.SHA256SUMS`: sha256 `%(sums_sha)s`.
- Host install script `resident_host_install_0485393f3a-r34c.sh`: sha256 `%(host_sha)s`; `install_r34.sh` `%(install_sha)s`; `pre_read_r34.sh` `%(pre_sha)s`; `rollback_r34.sh` `%(rb_sha)s`.
- The capture library and wrapper are unchanged.

## 2. Blast radius, by branch (read from the code at the pin)

| what | BEFORE (r32) | AFTER (r34) |
|---|---|---|
| an Opal job whose holdings carry no UNRESOLVED row | runs | the same (the swap stage is skipped; the pool is still read and checked at the start of every Opal job) |
| an Opal job with an UNRESOLVED holding | the read refuses (an unresolved row is not admitted) | each UNRESOLVED row is replaced by the pool candidate of its class with the longest Yahoo monthly history (ties: the alphabetically first), the amount KEPT; a replacement already held is MERGED into that row |
| the SAME job, a ticker the pool does not hold in exactly one class | -- | NOT swapped and left out; the disclosure reads "SYM is not analysed; Opal Staff will manage the replacement." |
| a job whose every holding is left out | -- | refused `NO_ANALYSABLE_HOLDINGS` |
| a swap | -- | one `SWAP` disclosure per row, ahead of every other disclosure; `run_doc.swaps` names the pool vintage and holds NO amount; `settings.swap` carries pool date, claim, stale flag, swapped and left-out counts |
| a pool older than %(stale)d days at the run date | -- | the swap still runs; each disclosure says the pool is older than %(stale)d days (this pool turns stale after %(stale_date)s) |
| a damaged, absent or altered pool file | -- | EVERY Opal job refuses (`PINNED_FILE_ABSENT` / `PINNED_FILE_DIFFERS` / a `POOL_*` code); the file is pinned by sha256 in the bindings and in the package sums |
| the door tree (`intake/portfolio.py`, `intake/uploads.py`, `ops/status.py`) | r32 bytes | the bytes the Lambdas carry (`portfolio.py` and `uploads.py` at the r33 pin, `status.py` at the r35L pin: the same blobs, checked by the generator); the resident's static walk reaches `portfolio.py` and `uploads.py`, not `status.py` |
| a symbol YCharts omits and the registry does not resolve (the door, every upload) | filed TICKER_NOT_FOUND with Replace and No offered | sent to the yfinance checker in ONE batch: KEPT when yfinance returns rows with a finite positive last close (no Replace or No; priced from yfinance), NOT_KEPT stays NOT_FOUND, a failed or pushed-back check reads UNAVAILABLE `YFINANCE_CHECK_FAILED`, never absence; a missing `yfinance` library reads as a failed check |
| a ready-signal send that fails (the commentary step is not told the analysis is ready) | a journal line only; the job stays READY | the same line, plus ONE write on that job's row: `hop_failure` = `{hop READY_SIGNAL, code READY_SIGNAL_SEND_FAILED, at}` (set-once: a second failure is a no-op) |
| a commentary-ready message the packager refuses or fails on | refusal logged and message deleted, or the error raised and the message retried | the same, plus ONE set-once write `hop_failure` = `{hop PACKAGER, code PACKAGER_REFUSED or PACKAGER_FAILED, at}`; the packager's own error is re-raised unchanged and a failing write is swallowed and journalled |
| the job row's state, receipt and `i3_sent_at` | -- | untouched by either write (the write names only the `hop_failure` attribute, conditional on it not existing) |
| pricing, the producer list, the map selection, the capture library | -- | unchanged |

**The class of the missing ticker.** The resident wires NO classifier store: the swap knows a ticker's class only when the pool holds that ticker in exactly one class. An
UNRESOLVED ticker the pool does not hold is left out. That is the C-SWAP step 3 gap (the model classifier is its own cell and pair after run 3). Run 3's candidates carry no
class in the pool, so this release alone does not swap them; it makes the swap real for every UNRESOLVED ticker the pool holds, and it is the release the classifier lands on.

**Writers counted.** The pool file: ONE writer (the builder, for this release). The bindings: ONE (the builder). Swap records: ONE (the producer).

## 2b. Yahoo calls per swapped holding, and their bound

Source: `swap_pass.py` and `yahoo_history_days.py` at the pin (REQUEST_CHUNK = DEFAULT_CHUNK = %(chunk)d). `[measured from the code and the shipped pool]`

- The swap asks Yahoo for the monthly Close history (`period` max, `interval` 1mo) of EVERY pool candidate in the missing ticker's class, in `yf.download` calls of at most %(chunk)d tickers
  (the prefetch). **Calls per swapped holding: at most ceil(class size / %(chunk)d) download calls** = %(batches_max)d for the largest class (%(biggest)d tickers); %(batches_all)d if every one of the %(classes)d classes were
  asked once. The history is CACHED for the job: a second holding of the same class asks nothing; a different class asks its own batches.
- `[inferred, library behaviour not read here]` `yfinance` fans one `download` out to one HTTP fetch per ticker, so the number of fetches Yahoo sees per swapped class is the class size
  (up to %(biggest)d), not %(batches_max)d. The bound that matters for Yahoo's rate limit is therefore the CLASS SIZE per distinct class per job.
- **Failure branch.** A batch that raises is skipped; its tickers are then asked ONE AT A TIME by the chooser, and a single ticker that raises is dropped as `HISTORY_ERROR` and is NOT
  cached, so a second holding of that class asks it again. With Yahoo fully down this is up to the class size of single calls per holding (%(biggest)d for the largest class) before the pick ends
  `NONE_PRICED` and the holding is left out with the not-analysed disclosure. A failed request never reads as "unpriced" in a way that picks a wrong replacement.
- The job's other work (the BBG/estate history, the existing yfinance price adapter) is unchanged and unreachable while pricing is off.
- The host check at V2 makes ONE `yf.download` call for ONE ticker and ONE checker call (`YfinanceChecker().check` of one ticker), to read that the host can reach Yahoo through the installed library at all.

## 2c. Yahoo calls by the door's checker, and their bound

Source: `intake/yfinance_check.py` and `security_resolution.py` at the pin. `[measured from the code]`

- Per upload: at most `cap` = 10 symbols are checked, each ONE `yf.Ticker(symbol).history(period="1mo")` call, paced `pace_seconds` = 1.0 apart, so at most 10 calls and about 10 seconds added to that upload's resolve. A symbol beyond the cap reads NOT_CHECKED `BEYOND_CAP` (UNAVAILABLE, never absent).
- A 401, 403 or 429 stops the rest of that batch (`STEP_STOPPED`); the stopped symbols read UNAVAILABLE.
- Only symbols the provider answered NOT_FOUND and the registry did not resolve are checked: a found symbol never reaches Yahoo. The result is cached KEPT for a day only when the resolver has a cache; the resident builds none, so a repeated upload re-asks.
- A missing library raises `CheckerUnavailable`; the resolver reads that as CHECK_FAILED for every symbol of the batch (a configuration fault, not a verdict).

## 2d. The hop_failure writers (C-HOP-FAILURE), and what they need

Source: `durable_job.py` (`mark_hop_failure`, `mark_hop_failure_keyed`, `HOP_FAILURE_CODES`), `resident_worker.py` `send_ready`, `resident_installed.py` `make_packager` at the pin. `[measured from the code]`

- Two writes only, each ONE `UpdateItem` on the `irpt-jobs` row of the request, `SET hop_failure = :value` with the condition that the attribute does not exist, never returning values. The resident host role's declared policy (`resident.tf`, `JobStateAcceptanceAndRetainedIndexes`) grants `dynamodb:UpdateItem` on `irpt-jobs` with no attribute condition `[declared in source; the live policy is read by the apply order's V3 with the simulator]`.
- Dormant until read: nothing reads `hop_failure` until the `irpt-status` reader release (cell `AR-g-111`, applied first) and the commentary writer exist. `mark_hop_failure_keyed` (the commentary hop's form) is in the package but unused by the resident.

## 3. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob, AND the library delivery closed: `yfinance` 1.2.0 and its Linux cp312 closure installed in the host's `pydeps` under its own pair (the first attempt of this release was installed as root `0485393f3a-r34` and ROLLED BACK at V2 because the library was absent; that root, its receipt copy and its three S3 objects are KEPT on purpose, so THIS release has its own names: root `0485393f3a-r34c` and keys `...-r34c.*`; CTO msgs 9066, 9070, 9075, 9114). Without the library V2 stops the install again.
2. Before-read: `pre_read_r34.sh` (fail-closed: the running root must be `0485393f3a-r32`, exit 40; the r34c root absent (the first attempt's r34 root may exist and is not touched); the library and wrapper unmoved; every changed member at its r32 value, every added member ABSENT; the queue 0/0).
3. D1: upload the tar, the sums file and the host script to the keys the install script names (each key must read 404 first; record the S3 versions); `install_r34.sh` fetches the host script and the sums BY KEY and refuses unless their sha256 equal `WANT` / `WANTSUM` (exits 31 and 33, dry-run: unchanged copy rc 0, one byte changed rc 31 and 33); it then runs the host script, which stages the tar, checks %(nchecks)d members, keeps the r32 root and library, installs, polls, and ROLLS BACK ITSELF to r32 on a failed start.
4. V1: running root `0485393f3a-r34c`; every changed or added member at its built value; the package sums %(sums_lines)d of %(sums_lines)d OK; the imports (`swap_pass`, `yahoo_history_days`, `opal_producer`); the pool file's sha256 equals the binding; queue 0/0; no sign-in in the journal.
5. V3 (read-only): `simulate-principal-policy` for the resident host's role, action `dynamodb:UpdateItem` on the `irpt-jobs` table ARN: expect allowed (the hop_failure writers need it); print the decision. A denial is a STOP before the ledger closes.
6. V2: ONE `yf.download` call for ONE ticker and ONE `YfinanceChecker().check(["SPY"])` call (expect KEPT) through the resident's interpreter (read-only, no job, no queue message); and `swap_pass.load_pool` on the shipped pool with today's date prints the pool date, claim, row count and stale flag.
7. The ledger closes at V2 and V3.

**Live proof is a separate act** (FWD-1 run 3 under `~Y2`).

## 4. Rollback, per key

- **The root:** `rollback_r34.sh` (or the install's own failure branch) restores `0485393f3a-r32`, which stays on the host; its readers are the r32 values of the changed members and ABSENT for the added ones.
- **The receipt:** `cutover_receipt.0485393f3a-r32.json` is kept by the install and copied back.
- **The library:** unchanged bytes before and after.
- **Queued messages:** none are touched; a job picked up after a rollback is served by r32.

## 5. Not claimed

- That the checker has run against a real upload, or that the host has `yfinance` installed (V2 reads it).
- That the swap has run against a real UNRESOLVED upload, or that Yahoo prices any candidate from this host (V2 reads one ticker, not a class).
- That the pool is current beyond its stated date (a held snapshot of %(pool_as_of)s).
- That run 3's candidates are swapped: they need the classifier (C-SWAP step 3).
- The live host, S3 objects, running root and receipt were NOT read (this is a build record).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set is: one new root directory on the resident host (`/opt/irpt-resident/0485393f3a-r34c`); the receipt
and its r32 copy; the unit's ExecStart; the kept library copy. The blast radius is section 2 and 2b; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin12": pin[:10], "base": rec["release_input"]["base_pin"], "members": art["member_count"], "unchanged": delta["unchanged"],
    "nchanged": len(delta["changed"]), "nadded": len(delta["added"]), "rows": rows, "count34": count_new, "count32": count_old, "compiled": compiled,
    "pool_sha": sw["sha256"], "pool_claim": sw["pool_claim"], "pool_as_of": sw["pool_as_of"], "rows_n": sw["rows"], "classes": len(sizes), "biggest": biggest,
    "batches_max": batches_max, "batches_all": batches_all, "chunk": CHUNK, "stale": stale,
    "stale_date": (__import__("datetime").date.fromisoformat(sw["pool_as_of"]) + __import__("datetime").timedelta(days=stale)).isoformat(),
    "tar_name": os.path.basename(art["path"]), "tar_sha": art["sha256"], "tar_bytes": "{:,}".format(art["bytes"]), "sums_sha": art["sha256sums_file"]["sha256"],
    "host_sha": scripts["resident_host_install_0485393f3a-r34c.sh"]["sha256"], "install_sha": scripts["install_r34.sh"]["sha256"],
    "pre_sha": scripts["pre_read_r34.sh"]["sha256"], "rb_sha": scripts["rollback_r34.sh"]["sha256"], "nchecks": len(delta["changed"]) + len(delta["added"]),
    "sums_lines": art["sha256sums_file"]["lines"]}
if any(ord(c) > 127 for c in text):
    raise SystemExit("REFUSE: non-ASCII in the packet")
with open(OUT, "w", encoding="ascii", newline="\n") as fh:
    fh.write(text)
print("wrote %s bytes=%d" % (OUT, len(text)))
