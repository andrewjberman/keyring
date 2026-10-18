# AMGT_HARVST task order -- `HVST-cm-1` -- ROUND 98, workstream PULL-DRAIN: THE ONE QUEUED BP PULL REQUEST IS DRAINED ONCE THROUGH THE BOX CONSUMER (STAGED behind a signed never-widen pair and site Z's notice) (row `D1-S63`; CTO round-97 analysis section 3 and item 1, msg 8125)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cm-1.the-one-queued-bp-pull-request-is-drained-once-through-the-box-consumer</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cm-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule is created or changed; the seat reads the scheduled-task list and the process list for any run of the daily vehicle, the harvest cycle or `pull_consumer.py` in its window.
comp-iam: RUN at L5 -- the consumer runs with the AWS principal and the Bloomberg Terminal session dell1's harvest tooling already holds; no grant is created or widened; the seat's own writes are none (the consumer writes the status object, three bronze objects, a pull-log object and a derived model block, all under BP's canonical partitions). The BLAST RADIUS is BP's newest bronze and derived model block (served by the gateway), named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a consumer run while the Terminal is signed out (it would write FAILED and DELETE the one queued message without a pull: run the read-only health check FIRST), a sign-in submit without a verified fill screenshot or past the 2-attempt budget (the account locks), a second drained message, a retry after a FAILED, a direct blpapi or Terminal call by the seat, a consumer run while the daily vehicle or the harvest cycle is on the Terminal, an object written under a raw-spelling prefix, an S3 delete, and a half-landed run (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cl-2`'s one real invoke (15:26:59Z) put ONE pull request for `BP/ LN Equity` on the SQS queue `opal-research-pull-requests` and wrote its status object `packs/BP-SLASH-_LN_Equity/status.json` as `REQUESTED`. Nothing drained it: `pull_consumer.py` is "a poller a person starts and stops ... NEVER a persistent service", so by design no process runs it. The CTO ruled (msg 8125): drain it once, through the box consumer only, no direct Terminal call; if the consumer reports the Terminal down, follow `integrations/bloomberg/READ_HERE.md` section 2 within its 2-attempt budget; if the budget is spent the request stays queued and the sign-in becomes Andrew's act; and name why it sat. **State plainly in `cm1_before.out`:** BP's newest bronze pull and derived model block (which the gateway serves) WILL move to the new stamp; the BP dossier written at 15:51:21Z will then be one model block behind until a refresh; the rollback of the add-only objects is an S3 delete that is not yours to take.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round98/NEVER_WIDEN_HALF_COO_CM1_DRAIN_THE_QUEUED_BP_PULL.md` (the issuer prints its sha256 in the GO) and the CTO half named in the GO. Read both; their conditions bind you. The order is STAGED until the issuer sends GO.
- (b) You have read `integrations/bloomberg/READ_HERE.md` (sections 1 to 3) and `integrations/bloomberg/research/pull_consumer.py` in full.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cm1-drain-queued-bp-pull.json`), with the window and the previous status bytes.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act.
0. **Before-state, read only (`cm1_before.out`):** (i) the queue's `ApproximateNumberOfMessages` and `ApproximateNumberOfMessagesNotVisible` (expect 1 and 0); (ii) the whole body of `packs/BP-SLASH-_LN_Equity/status.json` (expect `REQUESTED`, `updated_at` 15:26:59Z), saved to a local file (the rollback bytes: print its sha256); (iii) the keys under `packs/BP-SLASH-_LN_Equity/` and `packs/BP/_LN_Equity/`; (iv) the scheduled-task list and the process list with their control: no `pull_consumer.py`, no daily-vehicle leg and no harvest cycle on the Terminal in the window; (v) the PY_AWS interpreter path and that `blpapi`, `boto3` and `pyarrow` import under it. DO NOT call `etfs_compare_peers`; make NO Bloomberg call in step 0.
1. **The health read, BEFORE the consumer (`cm1_health.out`):** call `model_block_pull.bloomberg_health()` READ-ONLY under PY_AWS (the function the consumer calls first) and print its `ok` and any error text. **If `ok` is false: go to step 3 and do NOT run the consumer** (it would write `FAILED` and delete the message).
2. **If `ok` is true: run the consumer once (`cm1_consumer.out`):** `python integrations/bloomberg/research/pull_consumer.py --once` under PY_AWS, in the FOREGROUND, stdout and exit code to the file. One message is drained; if it prints `FAILED`, report its reason plainly and do NOT retry. Then go to step 4.
3. **The sign-in, ONLY if step 1 reported not ok (`cm1_signin.out`):** follow `READ_HERE.md` section 2 EXACTLY: `bbg_credentials.py --check`; read and print the attempt ledger (if fewer than 1 attempt remains: STOP, leave the request queued, write `STATUS_LANDED_CANONICAL=BLOCKED_TERMINAL` and report: the sign-in is Andrew's act, citing section 2 and the ledger); `-Phase fill` (repeatable, no attempt) and VERIFY the screenshot (login name; masked dots against `pw_len`); `-Phase submit` ONCE; then the health read again and ONE real `reference_data` call as `READ_HERE.md` says. If health is ok, run step 2. If not ok, STOP: no second submit without the issuer; the request stays queued.
4. **After (`cm1_after.out`):** (i) the queue counts (expect 0 and 0); (ii) the whole status body (expect `LANDED` with `raw_stamp`, `derived_stamp`, `ref_key`, `hist_key`, `derived_key`); (iii) the objects the pull wrote, with sizes and times: the newest objects under `bloomberg/harvest/bronze/refdata/`, `.../histdata/` and `.../bestdata/` `security_key=BP-SLASH-_LN_Equity/`, `amgt/harvest/state/pull_log/security_key=BP-SLASH-_LN_Equity/`, and `derived/model_block/BP-SLASH-_LN_Equity/<derived_stamp>/`; (iv) that NOTHING sits under any raw-spelling prefix written by this run (`security_key=BP/_LN_Equity/`, `derived/model_block/BP/_LN_Equity/`, `packs/BP/_LN_Equity/status.json`); (v) through the gateway, `harvest_get_fundamentals` kind `model` for `BP/_LN_Equity` (narrow it: `mnemonics` `["PX_LAST","CUR_MKT_CAP"]`) names the new model-block stamp. DO NOT call `etfs_compare_peers`.
5. **Name why it sat (`cm1_cause.out`):** one of: the consumer is a person-started poller and nobody started it (by design); the Terminal was signed out (step 1's text); a queue rule. Print the evidence of steps 0 and 1. A cause that is not the Terminal is a surprise row.
6. **Write `cm1_served.out`** ending with exactly these lines: `QUEUE_DRAINED_ONCE=PASS|FAIL`, `STATUS_LANDED_CANONICAL=PASS|FAIL|BLOCKED_TERMINAL`, `NOTHING_UNDER_RAW_PREFIX=PASS|FAIL`, `CAUSE_NAMED=PASS|FAIL`. A `BLOCKED_TERMINAL` is the CTO's own branch (the sign-in budget spent: the request stays queued and the act becomes Andrew's).
7. Commit the ledger close. Tell the issuer when the consumer has run (or been blocked) and when `cm1_served.out` is written. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>` (read the channel's tail first for the id), then keep working.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, run nothing further, file one row and tell me:** the queue holds a different count than 1; the status body is not `REQUESTED`; any `pull_consumer.py` process, daily-vehicle leg or harvest cycle is on the Terminal; the interpreter cannot import `blpapi`, `boto3` or `pyarrow`; health is not ok and the attempt ledger shows fewer than one attempt; a sign-in submit already used one attempt and health is still not ok; a second message is drained; a write lands under a raw-spelling prefix; the consumer prints `FAILED` (report; no retry).
- **After the run, a difference not named here:** write it plainly, do NOT self-grade, finish the read-only steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted.
- **Expected and NOT a failure:** the status object moves REQUESTED to FETCHING to LANDED in place; the gateway's BP bronze and model-block reads move to the new stamp; `model_rows` in the BP dossier is now one block behind (the dossier is not rebuilt here).
- **Window:** from my GO to 60 minutes later; if the consumer has not finished by then, stop and tell me.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round98/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round98/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cm1-drain-queued-bp-pull.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cm-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round98/cm1_served.out</invocation><expect>(?m)^QUEUE_DRAINED_ONCE=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cm-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round98/cm1_served.out</invocation><expect>(?m)^STATUS_LANDED_CANONICAL=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cm-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round98/cm1_served.out</invocation><expect>(?m)^NOTHING_UNDER_RAW_PREFIX=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cm-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round98/cm1_served.out</invocation><expect>(?m)^CAUSE_NAMED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC2 is the CTO's own grade (the request reads drained and the BP pull lands under the canonical prefix); AC1 proves exactly one message was drained; AC3 proves no raw-spelling write; AC4 is the CTO's "name why it sat". A `BLOCKED_TERMINAL` on AC2 is accepted by the CTO's rule and the issuer regrades it in the close.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cm-1.the-one-queued-bp-pull-request-is-drained-once-through-the-box-consumer.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cm-1.the-one-queued-bp-pull-request-is-drained-once-through-the-box-consumer` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cm-1.the-one-queued-bp-pull-request-is-drained-once-through-the-box-consumer.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: READ ITS TAIL FIRST for the next free id, append a row by BYTES and check the diff reads N insertions and 0 deletions; run the row gate against your row WITHOUT any override first (the `Z-S106` override must cover that pre-existing pair only).
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the bucket and prefixes are AMGT's own; the Bloomberg Terminal use is through the sanctioned queue).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half, site Z's notice (through `0.0.0_AB_MSTR~DELL1`), SC1 being free (it is on the RESAPP `ca-5` order now) and my GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-97 analysis (msg 8125) section 3 and item 1. Decomposition section 135.
- **Why a health read first:** the consumer's own first step deletes the message on an unhealthy Terminal; a pre-check keeps the request alive for the sign-in branch the CTO named.
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; I check SC1's READ ack within 10 minutes of the handing and type a nudge if the seat is idle (peek first).
- Dry run at the base: all four criteria FAIL as expected (the file does not exist).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>98</round>
<workstream>PULL-DRAIN</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
