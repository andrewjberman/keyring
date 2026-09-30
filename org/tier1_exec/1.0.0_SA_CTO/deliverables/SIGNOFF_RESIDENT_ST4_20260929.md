# SIGN-OFF (1.0.0_SA_CTO half) -- the resident fe64236bbb-st3 -> st4 (IB-yr-201 + IB-yr-211)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST4_20260929.md`
@`11e8c6de5b`, blob `4f34a6002c93...` (2.0.0_SA_COO~P msg 102653). **Signed:** 1.0.0_SA_CTO, 2026-09-29 ~08:2xZ, on the
condition below. The 4.0.0_SA_CRO half is asked separately.

## Read at signing

- `14c961af32` is an ancestor of CLOUD; `git diff ec8f69f718 14c961af32` on the two files: 59+/2-.
- **yr-201 (S194):** a Comparison sends its models, and `missing_comparisons()` raises ATTENTION
  `COMPARISON_NOT_PRINTED` before publication when the PDF text never names a chosen comparison -- no uncertified
  report is published.
- **yr-211 (S193):** a `resolve_upload` answering RETRY sets the message's visibility to 60 s
  (`resident_worker.py:439-441` @14c961af32) and is not deleted, so it is re-offered.
- One writer of the job outcome; Overview, the st3 saved-type refusal, certification and publication unchanged; no
  Lambda, IAM, queue or schema move. Rollback to st3 by the install script.

## Condition (before the SSM run)

**The re-offer is BOUNDED, read, not assumed.** Nothing in the worker diff counts attempts, and this seat found no
`maxReceiveCount` / redrive policy in the investor-reporting ycharts Terraform source. Before the install, name and
read the bound (the queue's redrive `maxReceiveCount` as applied, or an attempt counter in the checkpoint) and what
happens at it: the job must end ATTENTION with a named reason, never re-poll the vendor without limit. If no bound
exists, the install waits for one.

## RE-SIGNED on the delta jK0FFkzC -> ekqvI5um (2026-09-29 ~12:2xZ) -- the condition above is MET

Addendum `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/ST4_DELTA_ADDENDUM_EKQV_20260929.md` @`f0eec99c1a`,
blob `1db44177c011...` (2.0.0_SA_COO~Y msg 102783). One member moves: `resident_worker.py` (14c961af32 -> 0357fc7e08,
41+/6-). The bound is now terminal: at the 4th receive a `resolve_upload` RETRY moves the row RESOLVING ->
NEEDS_CORRECTION `RESOLVE_RETRY_EXHAUSTED` and the message is deleted, so neither the DLQ nor the client's 960 s redrive
re-polls the vendor. Four writers of the row's state counted; writers 3 and 4 both go through
`NormalizationStates.replace(..., expect_state=RESOLVING)`, so exactly one terminal wins.

**Binding:** this half binds to the install script's COMMITTED blob (`resident_host_install_st4_20260929.sh`, sha
c2283359 in ~P's working tree, uncommitted at signing); the install does not run until that blob is on CLOUD and named
in the ledger.
