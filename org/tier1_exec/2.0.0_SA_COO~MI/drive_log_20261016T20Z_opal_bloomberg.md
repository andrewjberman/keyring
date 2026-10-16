# Drive log -- 2.0.0_SA_COO~MI, NFRA_MCPINDEX, 2026-10-16 ~19:0xZ to ~21:0xZ (host opal_bloomberg)

Loop: `/canonical-drive NFRA_MCPINDEX 30m`, `/keep-driving` ON. Lease FULL.

## Substantive ticks

- **~19:0xZ to 20:0xZ, round 20 closed out.** MX-c-27 (regeneration loses no hand-set field and no registry row) complete @f3e0c03447 (merge f5e5872dd4, A1 0561aced58); MX-c-28 (measured depth claims are floors with `measured_at`) complete @8af05b0672 (merge 614a633c9a). Trial emit PASS, nothing landed. L8 packet `round20/L8_PACKET_ROUND20.md` @2ad9da384e to `3.0.0_SA_CVO~Z`. Disarm row Z-S132 (worker ~50's five rows).
- **~20:0xZ, CTO round-20 analysis @3f03a45f83 (msg 35237)** on the CVO slug ADJUDICATION_v16: R21-1 (a regeneration refuses to drop a registry row; 36 of 143 `catalog-*` rows dropped today) and R21-2 (two depth kinds, `latest` a floor, `series_start` a ceiling). The CVO caught that my MX-c-28 tagged all 39 claims `floor`, six of them series starts: my defect, owned in the message to the CTO. `round12/checks/c12_depth.py` made kind-aware (selftest 16 of 16).
- **~20:0xZ, round 21 issued** `158de6411b` (battery `ff13c436b1`; every check FAIL at the base in a sparse worktree): MX-c-29 (worker ~52) and MX-c-39 (worker ~53); fanout 2 of 2 chains, cap 8.
- **~20:1xZ, candidate gate for the trial emit** `d4a07e2923`: `round21/checks/r21_check.py`, `r21.AC1/AC2.sh`, `round21/emit_final.sh` (base r21.AC1 FAIL as expected).
- **~20:2xZ to 20:5xZ, round 21 drained.** ~53 MX-c-39 merged `8906f5fb80`, flip `0ed2c150b5`; trial emit r21.AC1, r21.AC2, c23.AC4, c21.AC2, r13.AC3 PASS (candidate md5 b014f6379707e9071cb73b3a94516182, not landed). ~52 MX-c-29 finished AC3 FAIL (2 of 60): the generator's integration tests run a 180-row fixture against a copy of the tracked registry and the new guard rightly refuses the 36 others. The face omitted the test file from `<paths>`: my defect. A1 `e48fe1117d` granted the file, the slot was re-seated, merged `28d19f4834`, flip `b03ffb960f`. Disarm rows Z-S133, Z-S134. `round-close-check.py --round 21` MAY-CLOSE (2 of 2). L8 packet `round21/L8_PACKET_ROUND21.md` @da5fcda084 to the CVO at 20:50Z (msg 35254).

## Lessons for the record

- Run the NEW guard against the sibling test files of the changed module in the sparse worktree BEFORE issuing; a guard that refuses a legitimate old fixture is found by the worker as a BLOCKING row otherwise (cost: one re-seat).
- The proof-of-spec checker must be run inside the worker tree; from the main tree it reads INVALID on a valid instance.
- A surprise row for a disarm needs `dismissal_reason` when `disposition` is DISMISSED_WITH_REASON.

## Standing clock

MX-s-19 acceptance 2026-10-20 ~03:10Z (`round7/checks/s19.AC2.sh`); from 2026-10-19 check `0.7.0_AE_CloudOps~NFRA1` is LIVE, message `0.0.0_AB_MSTR~Z` by 2026-10-20T02:30Z if not; ledger `nfra-mcpindex-r7-bd-doc-retire` open to 2026-10-21T06:02Z. MX-c-24 plus the kind-keyed catalog ride `2.0.0_SA_COO~O`'s next batched release; catalog emitted fresh at that cut.

Push state: LOCAL (ls-remote read at commit time).
