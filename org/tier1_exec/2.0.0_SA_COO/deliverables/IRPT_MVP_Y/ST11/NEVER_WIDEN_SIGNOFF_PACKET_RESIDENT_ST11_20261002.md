# Never-widen sign-off packet -- st11: the resident st10 -> st11 at CLOUD 4f68a17d3a (a BUSY resolve no longer spends itself) and the resident role's sqs:SendMessage

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~07:2xZ.
**Authority:** CTO rulings batch 120 items 1-4 (option (a) with a fresh delayed re-send, the 60-minute deadline, a busy
code with a retry action, "a new resident packet (st11) with both halves"), batch 121 (exactly `sqs:SendMessage` on
`irpt-generation` to `irpt-ycharts-runner-role` in `ycharts/resident.tf`; applied only under this packet by a targeted plan;
"show the self-send cannot loop"). **Ledger:** `irpt-resident-st11-20261002` (U1 proven; I1, D1, V1). **Two moves, in order:**
I1 the IAM line, then D1 the install. No Lambda, queue, table or schema moves. No vendor call.

## 1. What ships

**I1 -- IAM.** `aws_iam_role_policy.runner_resident`, sid `ConsumeTheGenerationQueue`: the four actions it holds plus
`sqs:SendMessage`, on the same one resource (`irpt-generation`'s ARN). Targeted plan (`ST11/plan_iam_targeted.txt`): 1 to
change, the one added action, nothing else; the full plan of the root reads the same single change (07:1xZ).

**D1 -- the resident.** Every member at ONE commit `4f68a17d3a`, no member override. Gate on the built package
(`ST11/GATE_OUTPUT_20261002.txt`): G1 243 of 243; G2 241 of 241 equal `git show 4f68a17d3a:<path>`; G3 98 of 98 compile;
G4 agree; G5 against the RUNNING st10 package (S3 version `oawr7YMK..`, sha256 `094989ed..`, downloaded and re-hashed):
**added 0, removed 0, changed 8, identical 235.**

| changed member | from | in the resident's runtime (static import graph from `resident_main` + `resident_installed`, 56 modules) |
|---|---|---|
| `ycharts/generate/resident_worker.py` | item 19 `951afdf4e6` | LIVE: the BUSY branch of `poll_once` and `_end_busy_resolve` |
| `intake/resolution_broker.py` | item 19 | LIVE: keeps the lease refusal's `retry_after` beside its class |
| `intake/uploads.py` | item 19 | reachable; the change is the `RESOLVE_PROVIDER_BUSY` words, read only when an upload answer is SERVED (generate's route), never by the resident |
| `ops/status.py` | item 19 | NOT reachable (the same words, irpt-status's copy) |
| `ycharts/generate/comparison_catalogue.py` | item 18 | NOT reachable (imported only by `generate_installed` and generate's `entry`, neither loaded by the resident) |
| `infra/logic/registry/reporting_policies.json` | `11bf813387` | read by `opal_naming`: the package's own `reporting_policy("irpt-x10-v1")` validates and returns digest `e0046398e2395145`, equal to the live registry's |
| `org/standards/NAMING_SCHEMA.json` | `aa2b5a42ff` | read by `opal_naming`: one cadence token added |
| `reports/resident_bindings.json` | generated | the pin and member pins |

Tar `irpt-resident-4f68a17d3a-st11.tar.gz`, sha256 `27d8107f585d998be269c165587e61f866d899699ec3717ad333aa5cead0e7be`,
762,644 bytes, S3 version `iifNrF9aaIxbauvQAWUBqui7BpLHfGq2` (404 before; read back by version, sha equal). Install script
`ST11/resident_host_install_4f68a17d3a-st11.sh`, sha256 `51a21c45ea57203256f6c2c444c06d99064230eb0ad489c74e9aa7ee649c9b78`,
S3 version `Of7y6LTygJwlezKP0MuY3TBi5rmRM8XB` (404 before; byte-equal to the repo file). Against st10's script with names
normalized it differs in the tar pin, the `resident_worker.py` member pin and the ledger slug. The capture library and
wrapper are unchanged. Suites at the pin: generate 338 passed, 30 skipped; intake 253 passed; ops 187 passed; session 111
passed; generate offline suite rc 0.

## 2. Blast radius, by branch (read from `poll_once` at the pin)

| a `resolve_upload` receive answers | BEFORE (st10) | AFTER (st11) |
|---|---|---|
| READY / ATTENTION | delete | the same |
| RETRY, class `OPERATION_BUSY`, before first dispatch + 3600 s | 60 s release; the 4th receive ends `RESOLVE_RETRY_EXHAUSTED` (`REPLACE_FILE` stored) | SEND the same body with `DelaySeconds` = the lease's retry-after clamped to 1..900, THEN delete the received message; the row stays RESOLVING; journal `... requeued delay=N` |
| RETRY, class `OPERATION_BUSY`, at or past first dispatch + 3600 s | as above | the row ends `NEEDS_CORRECTION RESOLVE_PROVIDER_BUSY`, finding action `CORRECT`; delete; no send |
| RETRY, any other class | 60 s release; 4th receive ends `RESOLVE_RETRY_EXHAUSTED` | the same |
| a generation message | unchanged | unchanged |

**Why the self-send cannot loop** (batch 121's ask): (1) the deadline anchors on the row's `requested_at`, written once at
the upload (`intake/uploads.py:305`) and moved by nothing (a client redrive moves `dispatched_at`, not `requested_at`); the
message carries no counter, so no re-send resets it. (2) Each BUSY receive sends ONE and deletes ONE, so a chain never
grows. (3) Past the deadline the row ends by name and the message is deleted with no send; a later copy finds the row
non-RESOLVING and is deleted as READY. (4) Proven offline with SQS's own count: `test_a_resolve_busy_for_its_whole_deadline_
never_reaches_the_dead_letter_queue` holds the lease busy past the deadline; 12 re-sends at 300 s, then the busy end, an
empty queue, nothing dead-lettered, no vendor call. Negative control: the 3 new tests fail on st10's worker.

**Send-before-delete:** a failed send raises and leaves the received message to return after its 900 s; a failed delete
after a send leaves two copies of one chain, both bounded by the same deadline. **Concurrent chains:** the page's redrive
(every >= 960 s while it polls) can add a chain; at most about four inside an hour, all ending at the same deadline.

**What the user reads:** the busy end's finding is `RESOLVE_PROVIDER_BUSY`, action `CORRECT`, never `REPLACE_FILE`. Its words
("The data provider was busy with another report while this file was being checked. Nothing is wrong with your file; submit
the request again.") are served once the generate and irpt-status bundles carry item 19; until then the served answer
shows the code with action `CORRECT` and no description (`_with_correction_words` leaves an unmapped code as written). The
page maps a finding's code through without a closed list (`adapt.ts:867-870`).

## 3. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read: running root `b1db201025-st10`, active; both queues 0/0; no non-terminal job; the role's applied policy lists
   the four actions.
3. I1: a fresh targeted plan of `aws_iam_role_policy.runner_resident` showing only `+ "sqs:SendMessage"`; ONE `safe-apply`;
   the applied policy read back lists five actions on the one ARN; a re-plan reads no changes.
4. D1: one `head-object` of the script's key printing `Of7y6LTy..`; the script fetched on the host BY KEY, its sha256
   checked against `51a21c45..`, run through Systems Manager (`ST11/install_fetch_and_run.sh`).
5. V1 on the host: running root `4f68a17d3a-st11`; `resident_worker.py` `93e50f0f148960ed..` with `RESOLVE_BUSY_DEADLINE_S`;
   `resolution_broker.py` `29c86578a4e20d95..` with `last_retry_after`; `uploads.py` `fe3f13a8336cd08c..`; the library
   unchanged; the unit polls; queue 0/0.
6. The ledger closes at V1.

Not part of this act: any vendor call or job. The live proof (an upload during another job's generation reads NORMALIZED
after it) needs a live YCharts session, which needs Andrew's own sign-in (batch 120 item 7).

## 4. Rollback, per key

I1: one targeted apply removing the action (the four-action statement as before). D1: root `b1db201025-st10` stays on the
host; the script's rollback branch restores it. A re-sent message under st10 is an ordinary resolve message.

## 5. Not claimed

- That the BUSY end is reached in practice: a generation usually ends within the hour and the re-sent resolve then runs.
- The served words: they ride the generate and irpt-status builds, not this act.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~07:2xZ, on this packet's bytes at the commit that carries it. The write set is one IAM action on one
role and resource, one new root directory on one host, the cutover receipt with its backup and the unit's ExecStart. The
blast radius is section 2, every branch of a resolve receive; why the self-send cannot loop is section 2's four points; the
rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
