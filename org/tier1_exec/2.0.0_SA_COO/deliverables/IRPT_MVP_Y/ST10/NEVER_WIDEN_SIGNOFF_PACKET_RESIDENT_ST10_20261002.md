# Never-widen sign-off packet -- the resident st9 -> st10: the whole tree at CLOUD b1db201025 (items 15 and 16)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~03:1xZ.
**Authority:** CTO rulings batch 97 item 4 (E2 withdrawn: the receive's 900 s stands), item 5 (a challenged read prints
the WAF header's action), row IRPT_BCKEND-S253 (the resident job records its vendor requests), batch 100 (msg 103946:
"cut the irpt-status packet for E7 now, then the resident st10"). **Ledger:** `irpt-resident-st10-20261002` (legs U1,
D1, V1); U1 proven. No Lambda, IAM policy, queue, table or schema moves. One host, one systemd unit. No vendor call.

## 1. What ships

Every member at ONE commit, `b1db201025` (the same pin as the E7 irpt-status packet), no member override. Built by
`IRPT_MVP_P/build_resident_package.py --pin b1db201025 --enrolled-user-id 1276035`. Between st9's pin `481166a8f2` and
`b1db201025` the only commits touching a resident member tree are this lane's items 15, 16 and 17 (`git log`).

Member census against the RUNNING package (st9, S3 version `WCfp.LuKrNtKpv31dANEaOtAebXoGfRw`, sha256 `486d0c35..a4ce`,
downloaded and re-hashed here): **243 members; added 0, removed 0, changed 7, identical 236.**

| changed member | item | what it carries | in this process |
|---|---|---|---|
| `ycharts/generate/resident_worker.py` | 15, 16 | the 120 s release removed from `poll_once` (a `ReadBackPending` propagates with the receive's 900 s); on a challenged read one journal line `WAF_READ header=<token>`; `keep_vendor_requests()` in the receive's `finally` | LIVE |
| `ycharts/generate/recipe.py` | 15 | comment only (`READ_BACK_POLLS = 1` unchanged) | no behaviour |
| `ycharts/session/broker.py` | 15, 16 | `vendor_ledger_record` (ten shape-only fields); `_RecoveryObserver` appends one record per reply; the closed `waf_header` token `CHALLENGE`/`CAPTCHA`/`BLOCK`/`OTHER`/`NONE` | LIVE |
| `ycharts/generate/durable_job.py` | 16 | `append_vendor_requests` under the lease and fence, 8 KB per append | LIVE |
| `ops/owned_requests.py` | 17 | E7's `read()` change | INERT: the resident calls only `_validate`, `_materialize`, `_final` (`frozen_worker.py:37,99`, `publication_worker.py:27,32,110`, `publisher.py:38,100`, `resident_worker.py:107,114,474`), all unchanged |
| `docs/contracts/.../OwnedAnalysisRequest.schema.json` | 17 | contract text | INERT (data file, not read by the resident) |
| `reports/resident_bindings.json` | -- | generated: the pin and the member pins | -- |

The capture library and wrapper are IDENTICAL (`9511060e..`, `55ddb8f7..`).

## 2. The one move -- `481166a8f2-st9` -> `b1db201025-st10`

- Tar `irpt-resident-b1db201025-st10.tar.gz`, sha256 `094989ed4a5bcd6688a0139ac4e13787406ce9d101b749c33358a6d2ae4074be`,
  760,925 bytes, S3 version `oawr7YMKU1ruCEVE40qxv6ax1Ztt3mXI`. A NEW key (HeadObject 404 before the put). Read back
  by version: sha equal. The st9 key is untouched.
- Install script `ST10/resident_host_install_b1db201025-st10.sh`, sha256
  `1a4a9d2f6954901e1db6e29d7617d52cd2a1aff8ab82745a1faae79e57ae02f4`, 8,702 bytes, S3 version
  `sKNqaKlpHiqZGOe.xV_kbeZGOGxkoygB` (404 before), read back by version: sha equal and byte-equal to the repo file.
  `bash -n` clean. Against st9's script with the names normalized it differs in the tar pin, three member pins
  (`resident_worker.py`, `recipe.py`, `broker.py`) and the ledger slug; no logic line differs.
- **Gate on the built package** (`ST10/GATE_OUTPUT_20261002.txt`): G1 243 of 243; G2 241 of 241 members equal
  `git show b1db201025:<path>`; G3 98 of 98 `.py` compile; G4 agree; G5 the census above. **PASS.** The gate's gzip
  is not byte-reproducible (a re-run gave a different `.tar.gz` sha256); the re-run's 244 tar members and its
  uncompressed tar (`c23ee692..`) are identical to the uploaded tar's, so only the gzip header differs.
- Suites at CLOUD HEAD (the resident trees equal the pin's): `ycharts/generate/tests` 333 passed, 30 skipped;
  `ycharts/session/tests` 111 passed, 1 skipped (2026-10-02 ~03:0xZ).

## 3. Blast radius, by branch (read from `resident_worker`, `broker` and `durable_job` at the pin)

**Item 15 -- the status read of a receive (`step_read_back`, unchanged: one GET per receive):**

| the first status GET of a receive answers | BEFORE (st9) | AFTER (st10) |
|---|---|---|
| `available` | the job continues | the same |
| `calculating` | `READ_BACK_PENDING:CALCULATING`; visibility set to 120 s; the redelivery's first request was challenged on 4 of 4 jobs | `READ_BACK_PENDING:CALCULATING`; the message keeps the receive's 900 s (st8's timing; a request about 900 s later was answered on 4 of 4 jobs) |
| a WAF action | `READ_BACK_PENDING:WAF_CHALLENGE`; 900 s | the same, plus ONE journal line `WAF_READ header=<CHALLENGE, CAPTCHA, BLOCK, OTHER or NONE>` (a closed token, never the header's bytes) |
| 403 or a login page | the one-refresh rule | the same |

Both outcomes of the calculating branch: the portfolio is available at a later receive (the job resumes from its
checkpoints, as on st8 and st9), or it is calculating at all five receives and SQS dead-letters the message after about
75 minutes (st8's figure; st9's was about 10). Recoverable by the redrive used on 2026-10-01 (`ST6/redrive_one.py`).
The CTO half on st9 (remark 3) named a risk that leaves with the 120 s call: `change_message_visibility` is no longer
called on this path.

**Item 16 -- the vendor-request ledger:**

| at the end of a receive (`finally`, after the transport closes) | outcome |
|---|---|
| the receive made vendor requests and the append succeeds | the job row gains them in `vendor_requests` (append-only across receives); journal `IRPT_RESIDENT_VENDOR_REQUESTS kept=N` |
| the append is refused (over 8 KB, lease or fence lost, a DynamoDB error) | caught; journal `IRPT_RESIDENT_VENDOR_REQUESTS kept=0 records=N class=<exception class>`; the job's answer, state and message are unchanged, and nothing is raised from the `finally` |
| the receive made no vendor request | nothing written |

- A record is ten shape-only fields (method, path without query, status, content type, bytes, set-cookie COUNT, WAF
  action, login destination, final path without query, body complete); a value that is not a short scalar is `None`.
  No cookie, body, query string or signed URL.
- Readers: every read of an `irpt-jobs` row goes through `durable_job._row` field by field, and `get_state` projects
  `state` and `job_detail` only (`durable_job.py:132-136`), so the status and report routes never see the list and the
  status read's "changed during read" comparison is unaffected. No code scans or queries the table.
- Size: at most 8 KB per append and five receives, about 40 KB, beside the checkpoint ceiling, under DynamoDB's 400 KB.
- IAM: the same `UpdateItem` on `irpt-jobs` with the same lease-and-fence condition form as every checkpoint write.

Nothing else changes: lookup, session rules, printed-type check, certification and publication are byte-identical.

## 4. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read: running root `481166a8f2-st9`, active; both queues 0/0; no non-terminal job.
3. One `head-object` of the script's key from the operator's side, printing VersionId
   `sKNqaKlpHiqZGOe.xV_kbeZGOGxkoygB`; then the script is fetched on the host BY KEY, its sha256 checked there against
   `1a4a9d2f..`, and run through Systems Manager (`ST10/install_fetch_and_run.sh`, st9's wrapper with st10's names
   and two added V1 lines).
4. V1 read-back on the host: running root `b1db201025-st10`; `resident_worker.py` `1708fe39caf52621..` with 0 mentions
   of `READ_BACK_CALCULATING_VISIBILITY_S` and `keep_vendor_requests` present; `recipe.py` `80b9e3ff7fe47004..`;
   `broker.py` `96f0e7782c106d49..`; `durable_job.py` `b5192fa2a1d4d5c0..` with `append_vendor_requests`; the library
   unchanged; the unit polls; queue 0/0.
5. The ledger closes at V1.

Not part of this act: any vendor call, any job. The next job (natural or under its own window packet) is the first live
read of item 16's ledger and, if challenged, item 15's journal line.

## 5. Rollback, per key

The root `481166a8f2-st9` stays on the host; the script's rollback branch restores it with its receipt. The library
file is the same bytes before and after. Rows already appended keep their `vendor_requests` list, which no reader uses.

## 6. Not claimed

- Why the vendor challenges the request after a job's first receive: not read. Item 15's journal line names the
  header's action at the next challenge.
- That the ledger's records equal the requests made: it has run offline only; its first live read is the first job on st10.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~03:1xZ, on this packet's bytes at the commit that carries it. The write set is one new root
directory on one host, the host library (same bytes) with its backup, the cutover receipt with its backup, and the
unit's ExecStart. The blast radius is section 3, both outcomes of the calculating branch and every branch of the append
included; the rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
