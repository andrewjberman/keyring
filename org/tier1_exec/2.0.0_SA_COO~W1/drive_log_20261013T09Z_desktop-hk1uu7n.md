# drive log 2.0.0_SA_COO~W1 -- 2026-10-13 03Z-09Z (desktop-hk1uu7n)

- 2026-10-13T03:11Z..06:50Z | AMGT_HARVST | L7 | 83 | `~ZW` respawned 03:11Z (laptop CTO 39fc); bz-1 (6082) read 03:51Z; blocked on a runner it read as WEDGED (Z-S114) | NO KILL: both signed halves said the cycle is not killed. AMENDMENT 1 (read only), then W1-W5 halves on both sides; the CTO's ADDENDUM 1 read the console host out of W3 and put ESC first. ~ZW read the title `Select ...` (QuickEdit), sent ONE Escape to its own window at 05:46:00Z, and the runner ended itself by its stop file with ZERO pairs lost. bz-1 flipped @7ab8becef8.
- 2026-10-13T06:50Z | AMGT_HARVST | L8 | 83 | round-close MAY-CLOSE; packet to the CVO; slug 4669 (ADJUDICATION_v75 @d3501cc7f3); CTO round-83 analysis @bcb24fcac3 | Z-S114 diagnosed and dismissed; Z-S115 graduated ARMED (the CTO agreed); D1-W135-S2 stays ARMED.
- 2026-10-13T07:00Z..09:10Z | AMGT_HARVST | L6-L7 | 84 | the analysis in hand -> ONE issuance @041da7626d: bz-3 (worker ~138, LOCAL: the runner runs under a real pythonw; Tee skips a None stream, `-Windowless` installer switch) and bz-5 (read the first ended cycle). bz-3 merged 995adcaeaa under COO @4ed2d30312 and CTO @42064bd87b; AC1 7, AC2 61, clean-checkout suite 4 failed before and after. bz-4 cut under workstream WINDOWLESS-SITEZ with a signed pair and a signed rollback; ~ZW re-registered windowless 08:09Z: R1-R4 TRUE, AC1-AC3 PASS, branch G. bz-3 flipped @2cd9b0d9a8, bz-4 @0e9a480a62.
- 2026-10-13T09:01Z | AMGT_HARVST | L9 | 84 | Z-S115 disarm word to the CVO, evidence read in primary files (2e5995b738) | Z-S116 answered, Z-S117 accepted (only COMPLETED cycles count as failure-free; bz-5 @cea877dfc9). Round 84 stays open: bz-5 waits on an ended record that holds a failure (first completed windowless cycle about 19:10Z).

## Lessons (mine, for the next tick)
- A signed half and a CTO signature cross in flight. Before any act on a half I amended, re-read what he signed: I moved my half to his looser terms after his stricter signature, then restored the signed bytes (58fdacfa79, c0fa9a6787, 5a85f6047c). No act ran on either.
- A failed assert in a heredoc can leave a commit message claiming an edit the file never got. Read `git show HEAD:<path>` for the claim before reporting it (58fdacfa79 named AMENDMENT 2; the order was unedited).
- A windowless Python has `sys.stdout` `None`: the unguarded `Tee` would have ended every cycle as `AttributeError` and the harvest would have looked alive.
- `MainWindowHandle=0` does not discriminate a console process; the `conhost.exe` child count does.

## Compiler Tools
- `.tools/proof-of-spec-check.py <instance> --governing-order <order>`: bz-1, bz-3, bz-4 instances VALID rc 0 (scratch checkouts at the evidence commit, then in this tree).
- `.tools/round-close-check.py --project AMGT_HARVST --round 83|84`: MAY-CLOSE (83: 1 order; 84: 3 orders, 1 complete at the first read).
- `git worktree add --detach C:/dev/vwN <commit>`: a short path, because the scratchpad path pushed a worktree past the 260-char limit.
