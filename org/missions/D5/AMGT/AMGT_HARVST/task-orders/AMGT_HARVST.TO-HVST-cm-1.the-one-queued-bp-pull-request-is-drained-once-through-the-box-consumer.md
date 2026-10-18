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

- (a) (AMENDED) The never-widen pair is SIGNED at the current bytes AND its COO addendum 1 (the site Z route) is countersigned by the CTO: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round98/NEVER_WIDEN_HALF_COO_CM1_DRAIN_THE_QUEUED_BP_PULL.md` (the issuer prints its sha256 in the GO) and the CTO half named in the GO. Read both; their conditions bind you. The order is STAGED until the issuer sends GO.
- (b) You have read `integrations/bloomberg/READ_HERE.md` (sections 1 to 3) and `integrations/bloomberg/research/pull_consumer.py` in full.
- (c) (AMENDED) Your ledger `harvst-cm1-drain-queued-bp-pull` was opened for a deploy that did not occur here: CLOSE it as a STOP with nothing written (NEVER-2); the after-reads need no ledger.

## 2. THE ACT (AMENDED: the drain runs at SITE Z; you READ the result)

**AMENDMENT 1 (the CTO's ruling, msg 8152; COO addendum `deliverables/2.0.0_SA_COO_W1/round98/NEVER_WIDEN_ADDENDUM_COO_CM1_SITE_Z_ROUTE.md`).** You STOPPED correctly at step 0: this box has no `PY_AWS`, no `blpapi` and no Terminal; site Z keeps the Bloomberg jobs. **dell1 does not order a site Z seat: MSTR asks site Z, MSTR to MSTR, to drain the one queued message on its Terminal box with `pull_consumer.py --once`, as site Z's own order on its own rules, with the pair's terms as our conditions (a health read first; no consumer start on an unhealthy Terminal; exactly one message; nothing under a raw prefix; the result reported back). Site Z decides.** **You do NOT run the consumer, do NOT sign in, and make NO Bloomberg call.** Your remaining part of this cell is READ-ONLY:
0. **Before-state (done):** `cm1_before.out` (your read 16:46Z to 16:51Z) stands as the BEFORE record, with `status_before.json`. Close your ledger `harvst-cm1-drain-queued-bp-pull` as a STOP with nothing written (say so), if you have not already.
1. **Wait for the issuer's message** that site Z has reported (the drain done, declined or blocked). Do nothing before it; the issuer sends the site Z report and says GO for the after-reads.
2. **The after-reads, READ-ONLY (`cm1_after.out`), after that message:** (i) the queue counts (expect 0 and 0 if drained); (ii) the whole status body (expect `LANDED` with `raw_stamp`, `derived_stamp`, `ref_key`, `hist_key`, `derived_key`, or `FAILED` with its reason, or still `REQUESTED` if site Z declined or was blocked); (iii) the newest keys, with sizes and times, under the five prefixes of `cm1_before.out` (`bloomberg/harvest/bronze/refdata/`, `.../histdata/`, `.../bestdata/`, `amgt/harvest/state/pull_log/`, `derived/model_block/BP-SLASH-_LN_Equity/`): which are NEW against the before-keys and which stamp; (iv) that NOTHING sits under any raw-spelling prefix that is newer than the before-state (`security_key=BP/_LN_Equity/`, `derived/model_block/BP/_LN_Equity/`, `packs/BP/_LN_Equity/status.json`); (v) through the gateway, `harvest_get_fundamentals` kind `model` for `BP/_LN_Equity` (narrow it: `mnemonics` `["PX_LAST","CUR_MKT_CAP"]`) names the new model-block stamp. DO NOT call `etfs_compare_peers`.
3. **The cause (`cm1_cause.out`):** copy site Z's reported cause (why the request sat) and the evidence you read at step 0: the consumer is a person-started poller that exists only on the Terminal box at site Z, so a request queued from dell1 drains only when site Z runs it (the CTO's round-99 rows). A cause that is not the Terminal and not that is a surprise row.
4. **Write `cm1_served.out`** ending with exactly these lines: `QUEUE_DRAINED_ONCE=PASS|FAIL|DECLINED_BY_SITE_Z`, `STATUS_LANDED_CANONICAL=PASS|FAIL|BLOCKED_TERMINAL|DECLINED_BY_SITE_Z`, `NOTHING_UNDER_RAW_PREFIX=PASS|FAIL`, `CAUSE_NAMED=PASS|FAIL`. A `DECLINED_BY_SITE_Z` or `BLOCKED_TERMINAL` is accepted by the CTO's ruling ("if it declines, the request stays queued and that is recorded") and the issuer regrades it in the close.
5. Tell the issuer when `cm1_served.out` is written. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>` (read the channel's tail first), then keep working.

## 3. STOPS AND EXPECTED QUESTIONS (AMENDED: for YOU only the stops that concern a read apply; the stops that name a consumer run, a sign-in or a second drained message are the CONDITIONS site Z was asked to keep, and you check them in the after-reads)

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

- **AMENDMENT 1 (issuer, 2026-10-18 ~17:0xZ; the CTO's msg 8152; SC1's STOP message of 16:52Z):** SC1 stopped at step 0 because this box has no `PY_AWS`, no `blpapi` and no Terminal (`cm1_before.out`); the executor of the drain becomes SITE Z, by MSTR's request on site Z's own order, and the seat's part becomes the READ-ONLY after-reads; steps 1 to 3 and the sign-in were removed from the seat's part; the proof criteria and the four lines are unchanged (two lines gained the value `DECLINED_BY_SITE_Z`). My COO half assumed dell1 ran the consumer: MY ERROR, named in the COO addendum. Gate limb: GATE (viii) grades this modification (the order declares `<placeholders>NONE</placeholders>`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>98</round>
<workstream>PULL-DRAIN</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
