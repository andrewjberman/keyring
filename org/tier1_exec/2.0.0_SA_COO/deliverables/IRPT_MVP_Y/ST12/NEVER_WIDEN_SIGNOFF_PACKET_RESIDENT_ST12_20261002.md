# Never-widen sign-off packet -- st12: the resident st11 -> st12 at CLOUD cf3ae52aee (a cookie the vendor rotates is written back to the stored session at once)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~09:0xZ.
**Authority:** CTO rulings batch 127 ("persist the rotated cookie as st12 ... write a rotated session cookie back to the
secret at once, under the bundle's lease and fence, only when it changed, names only in logs; PutSecretValue on that one
secret ARN ...; the probe uses the same transport; offline rotation test; live proof after Andrew's sign-in"). The read
behind it: `HOP3_PROOF/PROBE_ROTATION_READ_20261002.md`. **Ledger:** `irpt-resident-st12-20261002` (U1 proven; D1, V1).
**One move:** D1, the install. No IAM, Lambda, queue, table or schema moves. No vendor call.

## 1. What ships

**Code** (commit `9718ac5c87`, merged `cf3ae52aee`):
- `ycharts/session/operation_lease.py`: `OperationTransport.request`, after the lease completes a request, calls
  `_keep_rotation()`. When a cookie changed, it writes through the existing `persist()`, which checks lease ownership and
  the fence immediately before and after the write. It journals `IRPT_SESSION_ROTATION kept=1|0 names=<names> ...`,
  with names only. A failed write does not fail the request; the next request tries it again.
  `SessionlessTransport._keep_rotation` writes nothing.
- `ycharts/generate/transport.py`: `rotated_cookies()` writes the jar over the stored list. It replaces or adds a
  cookie and never removes one: the never-sent `aws-waf-token` record and any cookie the vendor removed stay as stored.
  Expiry is compared as the jar holds it. `Transport.persist()` uses it, and the bundle it wrote becomes the new baseline.
- Both a job and leg P's probe take `session.acquire()`, so both go through this one transport.

**IAM: none.** The write is `secretsmanager:PutSecretValue` on `ycharts/session/current-*`. That grant is already
declared (`infra/aws/terraform/investor-reporting/ycharts/iam.tf:104-107`, sid `WriteFreshSessionOnly`, policy
`irpt-ycharts-runner`). It reads back applied on `irpt-ycharts-runner-role`, the role of the resident host's instance
profile (`irpt-ycharts-runner-profile` on `i-0167fd745ad906a66`), read at 09:0xZ. The capture's own sign-in writes
use the same grant (INFERRED: the same host and role; CloudTrail not read).

**The package.** Every member is at ONE commit, `cf3ae52aee`, with no member override. Gate (`ST12/GATE_OUTPUT_20261002.txt`):
- G1: 244 of 244 members match `SHA256SUMS`.
- G2: 242 of 242 members equal `git show cf3ae52aee:<path>`.
- G3: 99 of 99 Python members compile.
- G4: the route table and the installed boundary agree.
- G5, against the RUNNING st11 package (S3 version `iifNrF9a..`, sha256 `27d8107f..`, re-hashed): **added 1, removed 0,
  changed 8, identical 235.**

Reachability is a static import graph from `resident_main` and `resident_installed` (`ST12/resident_reachability.py`).
It finds 57 modules; the same walk over st11's package finds 56, matching the st11 packet.

| member | from | in the resident's runtime |
|---|---|---|
| `ycharts/session/operation_lease.py` | st12 `9718ac5c87` | LIVE: `_keep_rotation` runs after every session request |
| `ycharts/generate/transport.py` | st12 | LIVE: `rotated_cookies`, `Transport.persist` |
| `ops/owned_requests.py` | E6 `4c23ef5d98`, item 22 `f27418381d` | reachable. `_final` now runs inside `_fresh_reads`, which is a no-op here because the resident builds no `ReadMemo` (only `reports/status_installed.py` builds one, and it is not reachable). `history(client_id=)` is called only by `ops/entry.py`, which is not reachable |
| `ops/read_memo.py` (ADDED) | E6 | reachable only through `owned_requests`' lazy import; `fresh_reads` returns `nullcontext()` |
| `ops/entry.py`, `ops/owned_report.py`, `ops/prospect_dates.py`, `reports/status_installed.py` | E6, item 22 | NOT reachable |
| `reports/resident_bindings.json` | generated | the pin |

The E6 and item-22 members ride along only because of the whole-tree rule. They serve on `irpt-status` through their own
packets, behind E7.

**Artifacts:**
- Tar `irpt-resident-cf3ae52aee-st12.tar.gz`: sha256 `1d1ca78273d1ae9301bd547bdf8e827865ae07dc12240f8dd41b12a8d4877de1`,
  765,913 bytes, S3 version `dL3uvbQqOjO6W0AyUDiT0Nxwbba_eEvw`. The key read 404 before the upload; read back by
  version, the sha256 is equal.
- Install script `ST12/resident_host_install_cf3ae52aee-st12.sh`: sha256
  `9c2b2be6be7f239de2b8a123d2f0260f232d32ff8bed7fd7eaaadd48513e95aa`, S3 version `tYs77bo4wZIwujZzpMNR0wiOakEFBQqp`.
  The key read 404 before the upload; read back, it is byte-equal to the repo file. Against st11's script, with root
  names normalized, it differs only in the tar pin, the `transport.py` member pin and the ledger slug.
- The capture library and wrapper are unchanged.

**Suites at the pin:** session 118 passed, 1 skipped; generate 338 passed, 30 skipped; ops 203 passed, 22 skipped; intake
253 passed, 1 skipped; generate offline suite rc 0. The new `session/tests/test_session_rotation.py` holds 7 tests, with a
negative control: without the write, the next operation sends the stale cookie, the shape of the 2026-10-02 probe.

## 2. Blast radius, by branch (read from `OperationTransport.request` at the pin)

| a session request's reply | BEFORE (st11) | AFTER (st12) |
|---|---|---|
| sets no cookie, or re-sets one to the same value and expiry | nothing written | the same: no changed name, no write, no journal line |
| rotates or adds a cookie (value or expiry) | the new cookie lives only in that process's jar; the stored secret stays stale and the next operation starts from it (measured: the probe at 06:24:58Z drew one `Set-Cookie`, and the job 71 s later was refused 403) | ONE `PutSecretValue`: the stored bundle with the changed cookies written over it, the SAME `fence` and `generation`, plus `transport_updated_at`. It runs after the lease completed the request, with lease ownership and the fence rechecked immediately before and after. Journal: `IRPT_SESSION_ROTATION kept=1 names=<names> version=<8 chars>` |
| only removes a cookie | nothing written | nothing written: a write never removes a cookie, so it cannot sign the stored session out |
| a newer sign-in was published during the request (fence moved) | the request is refused `OPERATION_SESSION_CHANGED` | the same, and nothing is written (tested) |
| the write fails (throttle, denial) | -- | the request's answer stands. Journal: `kept=0 names=... class=<class> code=<closed code or ->`. The next request of the same operation writes again; with none, the next operation starts stale, as st11 does |
| the sessionless ticker lookup | no session | unchanged: never writes (tested) |
| a sign-in (capture) | unchanged | unchanged |

**Why a rotation write cannot pose as a sign-in.** It keeps the bundle's `fence` and `generation`. `broker.current()`
classifies it exactly as before, and the worker's one refresh still demands a STRICTLY higher fence
(`resident_worker.refresh_session`, `transport.bundle["fence"] <= prior_fence` refuses).

**Concurrency.** The resident's own sign-in (`HostCapture`) takes the same provider operation lease
(`host_capture.py:161`), so it cannot run between the recheck and the write. RESIDUAL: Secrets Manager has no
conditional put. A publication from OUTSIDE the provider lease that lands within one Secrets Manager round trip of the
recheck would be overwritten by a bundle carrying the older fence.

**Churn.** One version per rotation. The only measured rotation rate is 1 `Set-Cookie` across 5 probes over about
22 hours.

**What a reader sees:** the secret's version list and the journal line. No cookie value enters a log, a record or this
packet.

## 3. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read:
   - running root `4f68a17d3a-st11`, active;
   - the generation queue 0/0;
   - no non-terminal job (the restart would cut one);
   - `WriteFreshSessionOnly` present on `irpt-ycharts-runner`.
3. D1:
   - one `head-object` of the script's key, printing `tYs77bo4..`;
   - the script fetched on the host BY KEY, its sha256 checked against `9c2b2be6..`;
   - run through Systems Manager (`ST12/install_fetch_and_run.sh`).
4. V1 on the host:
   - running root `cf3ae52aee-st12`;
   - `operation_lease.py` `2519834356b2d7a4` (`_keep_rotation` 3 mentions);
   - `transport.py` `d8cdbf3907a7d149` (`rotated_cookies` present);
   - `owned_requests.py` `1815caf24afdcf72`;
   - `read_memo.py` `c23cccb4f488e785`;
   - `resident_worker.py` `93e50f0f148960ed` and `broker.py` `96f0e7782c106d49`, both unchanged;
   - the host library unchanged;
   - the unit active and polling;
   - queue 0/0;
   - 0 `IRPT_SESSION_ROTATION` lines.
5. The ledger closes at V1.

**Live proof: a separate act, after Andrew's sign-in** (the stored session is dead, and only Andrew can sign in through
the CAPTCHA). It is the first jobs after the sign-in:
- when the vendor rotates, the journal carries `IRPT_SESSION_ROTATION kept=1`;
- `ycharts/session/current` shows a new version at that time, with the fence unchanged;
- the operation after it is not evicted.

Until st12 serves, no probe precedes a job (batch 127).

## 4. Rollback, per key

- **D1:** root `4f68a17d3a-st11` stays on the host, and the script's rollback branch restores it.
- **A secret version written by st12:** it is a valid bundle (same fence and generation, newer cookies) that st11 reads
  as `OK`, so nothing needs undoing. If one were wrong, `AWSPREVIOUS` holds the prior version (a stage move, outside
  this act).

## 5. Not claimed

- That the vendor rotates on any particular request. That the 2026-10-02 eviction was caused by the rotation (INFERRED;
  see the read).
- That keeping the rotated cookie keeps the session alive indefinitely: the vendor may evict on other grounds.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~09:0xZ, on this packet's bytes at the commit that carries it. The write set is:
- one new root directory on one host;
- the cutover receipt with its backup, and the unit's ExecStart;
- from then on, a new version of `ycharts/session/current` only when the vendor rotates a cookie, under the lease and
  the fence.

The blast radius is section 2, every branch of a session reply. The rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
