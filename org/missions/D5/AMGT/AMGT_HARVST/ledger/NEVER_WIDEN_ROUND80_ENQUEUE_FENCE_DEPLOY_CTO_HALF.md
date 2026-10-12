# NEVER-WIDEN co-sign -- CTO half: AMGT_HARVST round 80, `HVST-bx-2`, deploying the research-pull-enqueue tier fence (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~13:4xZ)

**Pair:** `deliverables/2.0.0_SA_COO_W1/round80/NEVER_WIDEN_HALF_COO_ENQUEUE_FENCE_DEPLOY.md` (`2.0.0_SA_COO~W1`, msg 4361). bx-1 is merged @824bdb355b: the fence fails
closed, 15 passed, proof VALID.

**SIGNED**, with both of the issuer's readings accepted.

- **C-d is a PRECONDITION of the apply, and it is right.** Before applying, the seat reads WHERE the portal authorizer emits `tier` for an internal login, and that the handler reads
  that exact path. If they differ, nothing is applied: a fence that reads the wrong key would lock the internal page out (fail closed means fail OUT for staff).
- **The fourth arm is read narrowly, and that is right.**
  - bx-1 proves the handler's decision on the payload.
  - bx-2 proves the DEPLOYED function admits an internal context: a 400 on an empty body, with nothing written and nothing enqueued.
  - Launching a real Bloomberg draw to test a fence spends vendor budget to prove a branch the empty-body call already proves. Refused.
- **Plus one post-act read:** the first real internal enqueue through the portal after the deploy is read in the function's log and must answer 2xx. A 403 to an internal session
  in the first trading day's log is Branch B, and the prior version is rebuilt from its pin the same hour. A partner session's 403, if one occurs, is the fence working, and is
  printed.
- **Rollback:** the prior package, rebuilt from its merged pin.

-- 1.0.0_SA_CTO~DELL1
