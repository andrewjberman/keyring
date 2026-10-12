# drive log 2.0.0_SA_COO~W1 -- 2026-10-12 01:5xZ-02:0xZ (desktop-hk1uu7n)

- 2026-10-12T02:00:00Z | AMGT_HARVST | L7 | 79 | MSTR~DELL1 msg 4203 (relaying site Z's manager): ledger harvst-bs3-zw-runner-20261009 past its 48 h window (64.6 h; author ~ZW, device sitez), legs PIN and ARM closed, GC and ACCEPT open | DRIVE FORWARD (NEVER-law: no half-landed deploy left silent): `deploy_ledger.py close-leg` GC on bs-3 AC4's evidence (bs3_gc_zero_age_dryrun.out lines 58-59, EXEMPT PID 10928 and 10528 on the c1be67f53c pin; negative control bs3_gc_dryrun.out 0 lines), then `hold` HELD-SOVEREIGN-GATED on Andrew's Barron's/WSJ sign-in, reread-event named. @90712c645f.
- 2026-10-12T02:00:00Z | AMGT_HARVST | L7 | 79 | NOT CLAIMED: the runner PID in the ledger (10928) was replaced by 21512 at bw-1's re-pin; the GC leg's proof is for the leg's own target, not a claim that the CURRENT runner is exempt (bw-1's ledger closed on its own GC read). ACCEPT is the CVO's at L9 and stays open: bbg has a completed cycle (20261010T221526Z), wsj and barrons have none.
- Idle otherwise: bs-4 r47 leg running (37 of 107 at 16:21Z on 10-11, completion near 2026-10-12T16:00Z); no ~ZW commit since 10-11 19:00Z.

## Compiler Tools

- `python .tools/deploy_ledger.py close-leg|hold --slug harvst-bs3-zw-runner-20261009` -> "leg GC closed. Remaining open: ['ACCEPT']", then HELD-SOVEREIGN-GATED (escalates to HELD-STALE after 4.0 d).
- `git diff --numstat` on the ledger json and completion record: 16/5 and 4/2 before commit (tool-written, not hand-edited).
