# ANDREW-DIRECT 2026-09-21 ~09:5xZ -- 2.0.0_SA_COO~T winds down its team; MDPF_TAXSMA position recorded

**Channel:** Andrew, typing at the `2.0.0_SA_COO~T` terminal, mid-turn.
**Verbatim:**

> take note of your position on TAXSMA and wind down your team at the next logical checkpoint.

**Recorded by:** `2.0.0_SA_COO~T` (holder of MDPF_TAXSMA round 1, L7).

## How it was applied

"The next logical checkpoint" was the TX-a-2 drain @`4e91f41768` (2026-09-21 ~09:5xZ). At that moment
**no worker was in flight**, so the wind-down took effect there and then:

- No new worker was spawned. TX-u-1, TX-k-1 and TX-i-3 were all dependency-ready and were
  deliberately NOT seated.
- The lane holds no cron and no loop. It stays reachable (inbox watcher) but idle.
- Scope was read exactly as written: "your team" means this lane's worker subagents. Nothing here
  asks any other seat to change its pacing.

## POSITION -- measured at HEAD 4e91f41768, 2026-09-21T09:56Z

**Round 1, L7: 12 of 27 complete, 13 pending, 2 staged.**
The count is the `<status>` of all 27 orders at HEAD. Every one of the 10 completions this session
was ALSO re-verified by the COO at its branch tip before its drain, so status and proof agree.

| cell | drained @ | COO drain verification |
|---|---|---|
| TX-p-1 | 3dcb249826 (prior session) | proof VALID; AC10 ruled by 1.0.0_SA_CTO (97296) |
| TX-v-1 | a481dfa6a1 (prior session) | proof VALID; AC4 judgment owed at L9 |
| TX-g-1 | e8f800e6a9 | 23/23 re-run; had been complete-but-UNDRAINED since 09-15 |
| TX-m-3 | c99159e2cd | 5/5 mech re-run; AC6 judgment for L9 |
| TX-b-1 | 5c80dc5d98 | 9/9 re-run; G-R EXERCISED with a negative control @2aa1e26cbf |
| TX-g-2 | 99e82c399f | 4/4 re-run; VERIFY-REUSE, 0 Gateway paths touched |
| TX-b-2 | fa353c4c29 | 11/11 re-run |
| TX-m-1 | c1555c428a | 23/23 re-run |
| TX-m-2 | 5cc9756554 | 14/14 re-run; 0008335338 / 0008242234 are data-contract constants |
| TX-m-4 | f8d419c9f0 | 21/21 re-run |
| TX-a-1 | fb5f7d6038 | 10/10 re-run; PROD gold script, gold suite 89/3 before = after |
| TX-a-2 | 4e91f41768 | 12/12 re-run; PROD consolidator, gold suite 89/3 unchanged |

On every drain above the COO ALSO ran a forge scrub (0 suspect), a grant check (0 out of grant) and
a long-digit privacy read.

### READY NOW (every dependency drained) -- the resume point, in this order

1. **TX-u-1** (slot ~3, publisher). This is the CRITICAL PATH (TX-u-1 -> TX-c-1 -> TX-c-2 ->
   TX-c-3 -> TX-v-3 -> TX-r-3). Its worker MUST emit contract fields only and MUST NOT consume
   `aua_including_tax` (ruling @5eef9bd41d).
2. **TX-k-1** (slot ~2, gold package).
3. **TX-i-3** (slot ~1, capability secret). It is a TERRAFORM APPLY on the `opal-gateway` root.
   Re-read gate G-S AT SEATING, never from this record. The secret and env names must match row
   W2-S2 (below).

### HELD

- **TX-r-2** (Gateway release). Waits on TX-i-3, and on G-O. G-O's INPUT exists at
  `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/G-O_OG-r-1_READBACK.md`
  @e2f11d1e3d (OG-r-1 is 18 PASS / 2 FAIL / 1 N/A; the dispositions are R-56 items 2, 3 and 4;
  the rollback is disclosed as NONE at runbook:252). The GRADE is the COO's, read at the cell
  against its own text, and has not been given. Its G-W blast radius MUST name every project drain
  in the release base at signing, including NFRA_MCPINDEX MX-c-4 if that has drained
  (1.0.0_SA_CTO 99018 s.5, never-class).
- **TX-r-3** (activation). Held on G-W (never-widen sign-off) and G-P (consumer promotion), plus
  its dependencies.

### Open items a successor inherits

- **W2-S1** is RULED @5eef9bd41d and bound (4) is DONE @5e8ba0e1d4. `aua_including_tax` is
  internal-only, marked at both definition sites. It is never served, never consumed downstream,
  and added to the contract only by the contract's owner.
- **W2-S2** (from TX-a-2): the Gold Lambda's env names `TAXSMA_GATEWAY_BASE_URL` and
  `TAXSMA_CAPABILITY_BEARER` were minted by the worker because neither the contract nor the
  decomposition names them. The prelude reads DISABLED while both are absent. TX-i-3 and TX-r-3
  must match these exact names, or rename them in one commit.
- **Notices owed before a spawn:** N-2 goes to `2.0.0_SA_COO~D` before TX-c-1 (decomposition s.6).
- **Disk practice:** each worker checkout is ~1.67 GB. Reuse ONE worktree per slot by switching it
  onto a fresh branch at the CLOUD tip; do not cut a new checkout per cell.
- **Worktree left in place:** `C:/tmp/wk-taxsma-2c` on branch `wk-mdpf_taxsma-1-2g`. That branch
  is fully drained (0 commits ahead of CLOUD). The tree carries only an untracked `.scratch/`,
  so a non-forced remove refuses. A resuming lane reuses the tree for TX-k-1 (slot ~2), or
  0.0.0_AB_MSTR removes it with the archive-then-remove it used at 98975.

### Drain discipline this lane used (so a successor inherits the method, not only the result)

Every drain did the following before merging:

1. Re-ran EVERY mechanical criterion at the branch tip.
2. Ran the forge scrub: a FAIL token in the evidence under a PASS verdict.
3. Checked the grant: every changed path is inside `<paths>` + deliverables + the order file.
4. Read any 8+ digit number in the added lines, in context.
5. Ran the commit-gate on every `.py`.
6. For a PRODUCTION file: read the added/deleted diff, and ran the Gold suite on BOTH sides (CLOUD
   and the branch tip) with the seat's own instrument.

Then it merged through `.tools/safe-merge.sh` with a bounded retry on shared-index contention, and
after the merge verified the first-parent file count and the order's status at HEAD.

-- 2.0.0_SA_COO~T
