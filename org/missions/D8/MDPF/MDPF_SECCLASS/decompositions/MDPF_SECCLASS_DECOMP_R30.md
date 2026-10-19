# MDPF_SECCLASS decomposition -- ROUND 30 (2.0.0_SA_COO~M1, dell1, 2026-10-19 ~15:0xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers two cells: one build and one read. The served acts of the round are the issuer's own and are stated below, each under its own pair and one per fire.

**Cut on:** the CTO round-29 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_29_20261019.md` @c6cb70fed9, `1.0.0_SA_CTO~DELL1` msg 8326, answering the CVO's slug msg 8325 and this seat's packet `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R29_20261019.md` @26ee88136c). The CTO's list, one served change per fire, in this order:
1. S55: the 14 held-out tickers enter candidacy through the classifier's normal path, each written row carrying `resolved_via = april_table`, under its own pair; blast radius the 14 tickers and nothing else; proof is the next fire's E_18 line (the 14 read as written or refused-with-reason, and 0 held out).
2. S53: a read cell, no writes: the step and the dates behind the $32k Monday-to-Thursday gap, read against `lib/trading_calendar.py` and the producer's own rule.
3. TO-DEPLOY-e57e61: closed, or its wait named.
4. Carried: the partners-data repoint (W104-S2 inlined), waiting on Andrew's word for the client-facing apply; then FWD-12; then D_03 / C_06.

## What is a cell and what is the issuer's own act

- **Item 1 is cell `SC-e-117`:** E_18 stops skipping a real ticker that the April table resolves but the canonical table lacks; it sends the pair to the scheduled classifier's own plan (`plan_rows`, the same refusal rule) and tags each such row `resolved_via = april_table`; its output replaces the held-out list with one outcome line per pair (written, refused with its reason, unresolved, seed_pending, or planned in a dry run). The shared module `etf_classification_scheduled.py` gains the one column name in `_WRITE_FIELDS` (precedent: `identifier_namespace`). A build whose `<paths>` reach a lambda-deployable shared module, so its class is WORLD; its ship is a later order to a CloudOps seat under a never-widen pair. **Not in the cell:** the contract entry for `resolved_via` (`org/standards/MDPF_SECCLASS_CONTRACT.json`, C-FIELD) is the CTO's; asked in msg after this issuance. The ship needs it.
- **Item 2 is cell `SC-e-118`:** `S53_CAUSE.json`: per date, the residue split by class, the producer step (file, line, quote) that leaves the gap, the calendar function it is read against; graded by `R30_CHECKS/check_r30_reads.py s53-cause`.
- **Item 3 is NOT a cell; it is a disposition recorded here (measured 2026-10-19 ~15:0xZ).** `TO-DEPLOY-e57e61` (`org/tier2_senior/0.7.0_AE_CloudOps~SD/task_orders/MDPF_SECCLASS.TO-DEPLOY-e57e61.fwd10-producer-apply-laptop.md`, `<status>pending</status>`, ledger `secclass-e57e61-fwd10-apply-s-20261007` HELD-SOVEREIGN-GATED, verify leg L3 open). Its gate is the first scheduled `mdpf-secclass-new-security-lambda` run whose plan lists US stocks (US planned > 0), graded by `org/tier2_senior/0.7.0_AE_CloudOps~SD/deliverables/e57e61_verify_read.py <run_date>`. I ran that script for every date 2026-10-09 to 2026-10-19: runs with an output object on 10-09, 10-12, 10-13, 10-14, 10-15, 10-16 and 10-19, each `PASS (no US row needed writing: US planned == 0, so acceptance 2 does not arm)`; no output object on 10-10, 10-11, 10-17, 10-18 (Saturdays and Sundays). So the gate has not armed in 7 graded runs; the rollback condition (US planned > 0 and US written == 0) has not occurred. **It waits on that run, an external event no seat can cause on demand without a write invoke; it is not Andrew's word.** It stays open and named; the verify script is the one read that closes it. (10-14 shows `written 1` with US planned 0: by the verifier's own rule that is a non-US row; not read further.)
- **Item 4:** the partners-data repoint, FWD-12 and D_03 / C_06 are not cut: the repoint's apply is Andrew's; its build is sequenced behind his word by the CTO's list; FWD-12 follows it; D_03 / C_06 wait on `lib/supervised_scope.py` (still on no branch).
- **The issuer's served acts, each under its own pair, one per fire, in this order:** (1) the S55 ship (E_18 and `lib/_shared/etf_classification_scheduled.py` to `code/gold/`, CloudOps) after `SC-e-117` drains and the contract entry exists; (2) nothing else is cut for a fire.

## Rule 24 record

- **Domain:** the CTO's four items; two cells; the issuer's acts.
- **(ii) Same grain:** the read cell ends in one JSON file graded by one mode of one committed script; the build cell is one code change, one one-word column list entry and one test file.
- **(iii) Intent coherence:** `s53-cause` checks the residue against `S48_RANGE_RECON.json`, the class numbers against their sum, the quoted step against the repo file and the calendar function against `lib/trading_calendar.py`; it does not recompute class numbers from S3 (the issuer recomputes one Monday at the drain).
- **(iv) State coherence:** the read writes nothing to AWS. SC-e-117 deploys nothing; its ship is an order to CloudOps under a pair.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-117` | E_18 admits the April-resolved real tickers to candidacy, tagged `resolved_via = april_table`; `_WRITE_FIELDS` gains the name; 7 new test cases; r29 display test trimmed to the 2 cases that stay true | S55 | WORLD (the gate's floor for a `_shared` lambda module path; nothing deploys in the cell) | none (as a build) |
| `SC-e-118` | `S53_CAUSE.json`: class split, step, calendar function, for the Monday-to-Thursday residue | S53, FWD-1 | LOCAL, direct act | none |

## Write sets (disjoint)

- **SC-e-117:** `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`, `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`, `data/black_diamond/scripts/gold/tests/test_e18_april_candidacy_r30.py` (new), `data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py`.
- **SC-e-118:** `.../deliverables/0.9.0_WK_MDPF_SECCLASS~106/S53_CAUSE.json`.
- Both also append to the project's surprise channel (byte-mode appends).

## Chains

Two cells, no edge: two chains. Fan-out 2 of 2, cap 8. Slots ~106 (SC-e-118) and ~107 (SC-e-117), `worker`, haiku (treatment box, MP-20261010).
