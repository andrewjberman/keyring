# /self-drive NFRA four -- tick 1 (1.0.0_SA_CTO~O, site Z, 2026-09-29 ~18:55Z)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4 (13,43 * * * *). The prior loop's cron 0eef1ea2 died in the 11:34 ET crash (last log tick 32, 14:13Z).

## Measured

- **Sequence check:** no flags on any of the 4 projects.
- **Open TOs:** 13 of 180 (the same as tick 32). OPLGTW 5 of 54, OPALAI 4 of 35, MCPORTAL 2 of 18, MCPINDEX 2 of 73.
  OPALAI's 4 includes OA-e-3, which is complete; its TO flip was dropped by the drain (row S45).
- **Completion test:** 0 of 4 complete; 4 REACHABLE.
- **Seats:** 2.0.0_SA_COO~O, ~MI and 3.0.0_SA_CVO~O LIVE at the restart; 2.0.0_SA_COO~AI spawned by 0.0.0_AB_MSTR~Z at
  18:51:58Z (msg 26657); 2.0.0_SA_COO~MP not live (MCPORTAL's 2 orders wait on Andrew's acts).

## Post-crash order (MSTR~Z 1755Z record) -- steps 1-2

**1. Residue.** The crash left none in scope. The open deploy entry `nfra-mcpindex-bd-playwright-strip` is healthy:
7 of 9 legs are closed, and L5 and L9 wait by design on tonight's 21:38Z-22:00Z scheduled fires. The one real loose end
predates the crash: drains d45ab2cf53 and 33076ebc84 dropped their workers' files, and 10 files are still missing at CLOUD HEAD.
- Scan: 5 of 167 first-parent CLOUD merges since 09-26 carry drops; 3 are already restored or superseded.
- Row `NFRA_OPALAI-Z-S45`, ARMED, disarm_owner 2.0.0_SA_COO~AI (@ae5f28c218).
- A direct commit by this seat was refused by the lane gate. The disarm ask went to 2.0.0_SA_COO~AI (18:54Z).

**2. Worktrees.** 34 in scope of 58 linked (inventory 1.0.0_SA_CTO~Z @626d53db16).
- NFRA_OPLGTW: 2.0.0_SA_COO~O DISPOSE 10.
- NFRA_MCPINDEX: 2.0.0_SA_COO~MI KEEP 1 (wk-mcpindex-r4-15), DISPOSE 13.
- NFRA_OPALAI + NFRA_MCPORTAL + cto_o_tflocal: this seat, DISPOSE 10 (@ae5f28c218).
- 3.0.0_SA_CVO~O CONCURS on all three tables (msgs 26642, 26658). Two conditions: no rel-/dep-/rb- branch is deleted
  while 093fc247c6 is live, and wk-NFRA_OPALAI-10 and the OA-f-3 worker branch stay until S45's blob check passes.
- Every disposal removes a checkout only; every branch is kept.

## Calls (Step 1)

- **R1 (3.0.0_SA_CVO~O msg 26642), who commits OA-e-3:** ruled by the driver. The write is a re-drain by 2.0.0_SA_COO~AI,
  because the lane config admits no direct commit by 1.0.0_SA_CTO~O. The CVO recorded its own correction (msg 26658).
- No other open calls in scope.

## Acts only Andrew can do (each cited)

- **Say yes to 33 checkout removals** (OPLGTW 10, MCPINDEX 13, OPALAI/MCPORTAL/tflocal 10), branches kept. They are
  recursive directory deletes, and CLAUDE.md Agent Autonomy reserves "recursive deletion" for human confirmation.
- Carried from tick 32, unchanged: release the site Z push (his hold on the shared-branch push; MX-t-10 waits on
  41ba3f747f reaching laptop CLOUD); G-C, one new unprivileged M365 user (tenant admin); G-ACCT steps 5-6 (his sign-in
  and MFA); MCPORTAL G-2ND (his second sign-in); MCPORTAL G-CLOSE and OPLGTW G-D (the person-operated runs).

## Compiler Tools

- `comp-which` exercised at startup (forwarder ran; 104 of 104 comp-tools resolve). `sequence-check.py --project` x4.
- The drop scan is ad hoc git plumbing (`git diff --name-only` over merge-base, parents and result). No comp-tool
  answers "which merge dropped branch files"; the first run crashed on argv length and was re-run without pathspecs,
  with the denominator printed.
