# IRPT_ANLREQ -- decomposition, round 48, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the CTO's FWD-4 ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`, msg 8906), PRD v0.21 contract C-HOP-FAILURE (signed by `3.0.0_SA_CVO~DELL2`, msg 8924), and the narrow-grant ruling (A) (msg 8970). Owners: `2.0.0_SA_COO~T2` the commentary hop (`fail` op, its caller, its grant); `2.0.0_SA_COO~G2` `hop_failure` in `durable_job.py` and `resident_worker.py` plus the status code and words (TO-AR-g-109); `2.0.0_SA_COO~V2` the ticket page read. The one-drain rule: the contract and its first writer land in one merge, so this round's cells and G2's TO-AR-g-109 are drained together and released together.

**Round 45 measured:** 24 of 35 hops SILENT on the ticket; round 46's routes map (23 rows) showed no existing service route can carry a failure note; the CTO ruled the ticket reads the job row's failure instead.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tf-71` | FWD-4 | FWD-4 build: the draft store's `fail` op writes the commentary hop_failure | `commentary_draft_store.py`, `test_hop_failure_fail_op.py` | WORLD |
| `AR-tf-72` | FWD-4 | FWD-4 build: the commentary function reports its failed draft to the draft store's `fail` op | `lambda_handler.py`, `test_hop_failure_calls.py` | LOCAL |
| `AR-tf-73` | FWD-4 | FWD-4 build (Terraform source): a narrow UpdateItem grant for the draft store on irpt-jobs | `commentary_draft_store.tf`, `test_hop_failure_grant.py` | WORLD |

## Edges and chains

- Three chains (M = 3). AR-tf-72 calls the `fail` event AR-tf-71 serves; the event is fixed in the contract text of both orders, so no cell consumes another's output and no two write the same file. AR-tf-71 uses a fake `mark_hop_failure` until G2's TO-AR-g-109 merges; the integration check (the real writer behind the real op) is the issuer's at the drain, after G2's merge.
- The release is a later WORLD pair (not this round): the draft-store zip (its members must include `ycharts/generate/durable_job.py`), the commentary function's zip (the transcripts root ships ONE zip to three functions, row IRPT_ANLREQ-D2-S127: a surgical zip), and the Terraform apply of AR-tf-73 with an `iam simulate-custom-policy` battery.

fanout: 3 of 3 chains, cap 4, reason: the CTO keeps fan-out at 4 (dell2 CPU budget); three independent write sets
