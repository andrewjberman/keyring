# /self-drive MDPF_TAXSMA,NFRA_OPLGTW,LGIC_NAMING,LGIC_ENFORCE,LGIC_CANON -- ticks 8-10 (2026-09-15 ~22:4xZ to ~23:2xZ)

state: ARMED | cadence 30m (CronCreate e5ff987a) | carrier org/XXX.md @6cfec7a785 | adjudicator: 1.0.0_SA_CTO.

Ticks 8 and 9 were quiet: no call, no gate flip, no log. Disk went 21G -> 16G -> 15G as workers spawned, and stayed
above the fabric's ~10G stop. All five projects read ADMITTED and EXECUTING; CAPACITY 3 of 3; goal loops 3 of 3 armed.

## Open calls in scope: 0; 1 FYI acted on in this seat's own lane

**NFRA_OPLGTW-S19 / S18 (2.0.0_SA_COO~O 97257, information only; the fix is a gate edit outside its surface).**
.tools/halt-gate-check.sh rooted the inbox and session files at the checkout holding the script. In a spine-v3
worker's linked worktree both are gitignored and ABSENT, so the gate read an absent inbox as "no messages" and passed
rc=0 -- a [STOP] to a worker's ISSUER did not halt that worker's apply -- and identity failed closed rc=3 (the sibling
W1-S6, and LGIC_ENFORCE-W3-S6 from the round-1 census, which this seat had left open as a known workaround).

- ACT: fixed @72897184fd. HALT_GATE_SHARED_ROOT derives from `git rev-parse --git-common-dir`, the MAIN checkout's
  .git from every worktree; the inbox defaults to it; identity reads this checkout's sessions dir first, then the
  shared one, so an issuer-provisioned worker serial still resolves as that worker. Outside a git checkout it falls
  back to the old rooting, so the HALT_GATE_* test overrides are unchanged.
- ARMS, one linked worktree at one HEAD: pre-fix rooting inbox_exists=no, resolve rc=1, serial empty; fixed
  inbox_exists=yes, resolve rc=0, serial 1.0.0_SA_CTO; main checkout unchanged. bash -n clean.
- NOT CLAIMED: an end-to-end [STOP] exercise; no STOP was planted in a live inbox. The measured coordinate is which
  directory the gate reads and whether it can name its principal from a worktree.
- CARRY: safe-apply runs the gate copy beside it, so an EXISTING worktree keeps the old gate and 2.0.0_SA_COO~O's
  mitigation stays in force there. A worktree cut from a CLOUD carrying 72897184fd needs no prefix. MDPF_TAXSMA's
  TX-i-* worktrees are not cut yet, so 2.0.0_SA_COO~T cuts them after this commit.
- NOT EXAMINED: .tools/lib/resolve-actor.sh and safe-apply's own second identity gate.
- Broadcast 97259-97262 to the three COO lanes and 0.0.0_AB_MSTR.

COMPLETION TEST: NOT DONE -- 0 of 5 projects read `status: complete`.
