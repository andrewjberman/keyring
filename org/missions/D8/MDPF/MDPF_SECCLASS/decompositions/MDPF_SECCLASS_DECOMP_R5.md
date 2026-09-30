# MDPF_SECCLASS decomposition -- ROUND 5 (2026-09-30, issuer 2.0.0_SA_COO~M, on the CTO rounds 2-3 analysis @0a8deabc8e)

**Cut on:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND2_3_ANALYSIS_MDPF_SECCLASS_20260930.md` @0a8deabc8e section 4
(the round-5 enrichment list, four items) and section 2 (the row rulings on S3, W6-S2, W5-S2). Round 4 (SC-e-10) is
drained @999c35109f and its packet is `deliverables/2.0.0_SA_COO~M/DRAIN_END_R4_20260930.md`; the CTO's analysis reads
"Round 4 stands", so round 5 does not reopen it. PRD v0.2 @301332beb4 (RATIFIED; the addendum is contract wording, no
endpoint change, so no half re-signs: analysis section 1).

Rule 24: the domain is the CTO's four enrichment items. Two are ISSUER ACTS and are carried as such, not as cells,
because a worker cell for either would be a WAIT or a hand-off: item 1 (the signed acts in sequence) and item 4 (one
real scheduled fire of FWD-7's classifier, read from the log). Item 2 (W5-S2) is drain hygiene by the CTO's own ruling
("a hygiene cell at the next drain, not a round cell"). Item 3 (W6-S2) is a cell. The CVO's adopted question (CUSIP rows
landing before `seed_bd_securities.py` is guarded would add 349 rows the fork never had) is the CTO's precondition for
signing the CUSIP_ROWS half, so it is the round's build cell. Two cells, no remainder, same grain (one act each), one
intent each.

## The cells

| cell | item | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-11` | The CUSIP guard: `data/black_diamond/scripts/classification/seed_bd_securities.py` never copies a `CUSIP:`-prefixed etf-classifications row into `bd-securities`; a dry-run against the LIVE tables prints the bd-securities delta from CUSIP keys as 0 with its denominator; a test pins the guard; the CUSIP_ROWS half gains the guard section the CTO's analysis names as its signing precondition | FWD-4, FWD-5 (the fork's reader risk), the CUSIP_ROWS release | NOT-EVALUATED | laptop | WORLD | A, `0.9.0_WK_MDPF_SECCLASS~9` |
| `SC-e-12` | W6-S2: narrow `infra/aws/terraform/shared-infra/main.tf` `aws_iam_policy.bd_securities_access` (unconditional Scan/GetItem/PutItem/UpdateItem/BatchWriteItem on BOTH `bd-securities` and `etf-classifications`, attached to `bd-exporter-ec2-role` AND `partners-lambda-role`). Criterion 1 is the CONSUMER CENSUS of `partners-lambda-role` (N consumers = N rules read, N printed) before any edit; the plan covers both branches; apply under its own halves | FWD-5 (IAM read reports zero writers) | NOT-EVALUATED | laptop | WORLD | B, `0.7.0_AE_CloudOps` -- PARKED: the seat is dark (not relaunched by the 13:0xZ word); the order un-parks on that seat's registration, read by this issuer's drive tick |

**Slot.** MDPF_SECCLASS worker slots used to date: ~1..~8 (authors, issued_to and branches); S197 gives 1 + 8 = 9.

**Write sets are disjoint.** SC-e-11 writes the BD classification seeder, its test, an R5 check and the CUSIP_ROWS half.
SC-e-12 writes shared-infra `main.tf` and an evidence JSON. Neither touches the other's files, the contract, or any
round-1..4 product file.

## Issuer acts carried in this round (item 1 and item 4 of the enrichment list; not cells)

In the CTO's sequence:
1. FWD3 seed with `--accept-module-truth` -- RUN 13:48:39Z, VNQI 1 of 138, ledger `secclass-fwd3-vnqi-seed-m-20260930`
   CLOSED @044157b073.
2. E18_IAM step 1 (applied 13:56:26Z, builder name `mdpf-secclass-scheduled-put-policy`, @1554e7c8c8) then step 2
   (BD E_18 deployed and verified 14:1xZ); ledger `secclass-e18-iam-and-deploy-m-20260930` OPEN on leg A1 = item 4,
   the first ordinary 04:00Z scheduled fire of 2026-10-01 read from the log (written, refused, denominator; no
   AccessDenied; no bd-securities call).
3. CUSIP rows under the section-2 guard -- after SC-e-11's packet; the CTO signs the CUSIP_ROWS half on it.
4. MODEL rows after SC-e-10's census -- the MODEL_ROWS half (260 conditional rows, 130 flagged) waits for both
   signatures after the CVO's round-4 compile.
5. BD_THREAD_R2 with IRPT_BCKEND IB-mr-291 in ONE window under one ledger entry (analysis section 2, row S3). The
   packet naming IB-mr-291's commit is the CTO's precondition; IB-mr-291 is built and committed on
   `wk-IRPT_BCKEND-93` (c5f8b8ddd5 build, df71fb818c complete) and drains to CLOUD as soon as the shared index clears.

## Drain hygiene (item 2, W5-S2)

At this round's drain the issuer adds the citation the CTO's ruling names: the contract's enum is canonical and the
second schema's copy cites it and carries no value of its own. One commit, no worker.

## Chains

- A = `SC-e-11`, slot `~9`, worktree `../wk_mdpf_secclass_9`, branch `wk-MDPF_SECCLASS-9`. Spawned at issuance.
- B = `SC-e-12`, lane `0.7.0_AE_CloudOps`. PARKED at issuance (no worktree, no spawn). Un-park condition: the AE seat
  registers LIVE on the broker; the issuer then delivers the order's path by one message.

`fanout: 1` (one worker slot live; the parked order holds no slot).

## Ruling after issuance (1.0.0_SA_CTO 103327, 2026-09-30 ~16:5xZ)

Round 5 CLOSES on chain A (SC-e-11, drained @716f6f883a). SC-e-12 leaves this rectangle: parked on its own carrier (the
order file, `<status>parked</status>`), owner `0.7.0_AE_CloudOps`, un-park condition "the CloudOps seat is live on the
broker"; it re-enters the open round when the seat returns, without a new ruling. Round 6 is cut from the CTO's round-5
analysis after the CVO's slug and carries the two reader guards (CUSIP_ROWS CTO half condition 5) and SC-e-12 by reference.
