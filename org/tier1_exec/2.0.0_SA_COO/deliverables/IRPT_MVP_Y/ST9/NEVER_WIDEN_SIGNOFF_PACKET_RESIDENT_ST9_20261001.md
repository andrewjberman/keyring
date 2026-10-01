# Never-widen sign-off packet -- the resident st8 -> st9: the whole tree at CLOUD 481166a8f2 (E2: one status read per receive)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~14:4xZ.
**Authority:** CTO rulings batch 88 item 4 (E2: "ONE status read per receive: a `calculating` answer releases the
message with a visibility of 120 seconds and is not polled again inside the receive; a challenge keeps 900 seconds ...
It rides the next attempt, and if the single read of the second receive is challenged it is withdrawn") and batch 89
(E1 withdrawn; the next arm is E2, E3). **Ledger:** `irpt-resident-st9-20261001` (legs U1, D1, V1). No Lambda, IAM
policy, queue, table or schema moves. One host, one systemd unit. No vendor call.

## 1. What ships

Every member at ONE commit, `481166a8f2c3ba2a59959525bac12ac1adabe324` (the merge of item 14, 4 of 4 files carried), no
member override. Built by `IRPT_MVP_P/build_resident_package.py --pin 481166a8f2 --enrolled-user-id 1276035`.

Member census against the RUNNING package (st8, S3 version `qMVedUlttPFVVOLsvmsx_mavt03zqkN8`, sha256 `9c640e30..`,
downloaded and re-hashed here): **243 members; added 0, removed 0, changed 3, identical 240.**

| changed member | what it carries | numstat against 9ac9b56d3c |
|---|---|---|
| `ycharts/generate/recipe.py` | `READ_BACK_POLLS` is 1 (was 2); `step_read_back` is unchanged | 5 added, 1 removed |
| `ycharts/generate/resident_worker.py` | `poll_once`: on `READ_BACK_PENDING:CALCULATING` the message's visibility is set to `READ_BACK_CALCULATING_VISIBILITY_S` (120) before the refusal propagates; `WAF_CHALLENGE` keeps the receive's 900 | 13 added, 1 removed |
| `reports/resident_bindings.json` | generated: the pin and the member pins | (generated) |

The capture library and wrapper are IDENTICAL (`9511060e..`, `55ddb8f7..`); the install script writes the same bytes.

## 2. The one move -- `9ac9b56d3c-st8` -> `481166a8f2-st9`

- Tar `irpt-resident-481166a8f2-st9.tar.gz`, sha256 `486d0c356c989c58121e6a9f67d3caae04a5c08434cdf8cd1297b289cc88a4ce`,
  758,863 bytes, S3 version `WCfp.LuKrNtKpv31dANEaOtAebXoGfRw`. A NEW key (HeadObject 404 before the put). Read back by
  version: sha equal. The st8 key is untouched.
- Install script `ST9/resident_host_install_481166a8f2-st9.sh`, sha256
  `5350877bd4e1a16537f935d3e68717f5a831bd77f85c68e5c9de6bfe24a53332`, S3 version `SojZdtkv9FjeiJTIHAWVkG7zCXVRo3LU`,
  read back by version: sha equal. `bash -n` clean. Against st8's script with the names normalized it differs in the
  tar pin and two member pins (`resident_worker.py`, `recipe.py`); no logic line differs.
- **Gate on the built package** (`ST9/GATE_OUTPUT_20261001.txt`): G1 243 of 243; G2 241 of 241 members equal
  `git show 481166a8f2:<path>`; G3 98 of 98 `.py` members compile; G4 agree; G5 the census above. **PASS.**
- Suites at the branch tip the pin merges (8c8f3e8fa4): `ycharts/generate/tests` 333 passed, 30 skipped; the generate
  offline suite `run_offline_suite.py` exit 0.

## 3. Blast radius, by branch (read from `recipe.step_read_back` and `resident_worker.poll_once` at the pin)

The read-back runs once per receive of a job that has a portfolio and no read-back checkpoint.

| the first status GET of a receive answers | BEFORE (st8) | AFTER (st9) |
|---|---|---|
| `available` | the saved portfolio is read once; the job continues | the same |
| `calculating` | wait 15 s, a SECOND status GET in the same receive. On 2026-10-01 that GET drew a 202 with a WAF action on 3 of 3 jobs; the message then waited out 900 s | NO second GET in the receive. The job raises `READ_BACK_PENDING:CALCULATING`; the message's visibility is set to 120 s; the next receive makes one status GET |
| a WAF action | `READ_BACK_PENDING:WAF_CHALLENGE`; the message waits out 900 s | the same |
| 403 or a login page (an eviction) | returned at once to the one-refresh rule | the same |

**The second branch has two outcomes and both are covered (the producer's own rule, read at the pin):**

- *The portfolio is available at a later receive.* The job continues from its checkpoints (no upload or portfolio
  call is repeated: both are checkpointed before the read-back) and finishes. Expected saving against today: about 13
  of 15 minutes per job, if the single GET of the second receive is answered.
- *The portfolio is still calculating at every receive.* Each release is one receive of the queue's five
  (`irpt-generation` RedrivePolicy `maxReceiveCount` 5, read 14:3xZ). After the fifth receive SQS moves the message
  to `irpt-generation-dlq` with the job row still SUBMITTING and its portfolio checkpointed. BEFORE, that took five
  receives of 900 s (75 minutes of a portfolio that never became available); AFTER, with five 120-second releases, it
  takes about 10 minutes. The state itself is not new and is recoverable: a redrive of the message resumes the job at
  the read-back (`ST6/redrive_one.py`, the path used at 06:04Z). **Not measured: how long the vendor takes to make a
  new portfolio available.** Today's three jobs each read `available` 15 minutes later, the only later read made. The
  trial's journal measures it; a job that dead-letters this way is the finding that withdraws or re-times E2.
- *The single GET of the second receive is challenged* (batch 88's own withdrawal condition): the message waits out
  900 s as today and the job finishes at the third receive; E2 is then withdrawn by the CTO's own rule and st8's
  behaviour is restored by the rollback below or by the next build.

Nothing else changes: the lookup, the session rules, the printed-type check, certification and publication are
byte-identical members.

## 4. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read: running root `9ac9b56d3c-st8`, active; both queues 0/0; no non-terminal job.
3. One `head-object` of the script's key from the operator's side, printing VersionId
   `SojZdtkv9FjeiJTIHAWVkG7zCXVRo3LU`; then the script is fetched on the host BY KEY, its sha256 checked there against
   `5350877b..`, and run through Systems Manager (`ST9/install_fetch_and_run.sh`, st8's wrapper with st9's names).
4. V1 read-back on the host: running root `481166a8f2-st9`; `resident_worker.py` `49305eeb90d80034..` naming
   `READ_BACK_CALCULATING_VISIBILITY_S`; `recipe.py` `3a4e58515476b841..` with `READ_BACK_POLLS = 1`; the library
   unchanged; the unit polls; queue 0/0.
5. The ledger closes at V1.

Not part of this act: any vendor call, any job. The Multi-Comp attempt (E3) follows under its own window packet and
is the trial of E2.

## 5. Rollback, per key

The root `9ac9b56d3c-st8` stays on the host; the script's rollback branch restores it with its receipt. The library
file is the same bytes before and after.

## 6. Not claimed

- That one status GET per receive avoids the read challenge: it is the trial. Measured basis: the first GET of a
  receive was answered on 6 of 6 receives today; the second GET of a receive was challenged on 3 of 3.
- That 120 seconds is long enough for the vendor's calculation.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~14:4xZ, on this packet's bytes at the commit that carries it. The write set is one new root
directory on one host, the host library (same bytes) with its backup, the cutover receipt with its backup, and the
unit's ExecStart. The blast radius is section 3, both outcomes of the calculating branch included; the rollback is
section 5.

## CTO half -- 1.0.0_SA_CTO

(owed)
