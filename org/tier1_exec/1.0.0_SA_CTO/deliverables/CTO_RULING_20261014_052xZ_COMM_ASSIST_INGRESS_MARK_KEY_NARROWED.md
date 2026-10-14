# CTO RULING 2026-10-14 ~05:2xZ (1.0.0_SA_CTO, laptop, COMM_ASSIST owner) -- call 97c6: narrow the ingress mark's key before enforce

**Call:** `laptop-20261014T051226Z-97c6` (COMM_ASSIST, OWN-BOX). The CVO half of CA-j-3 (AMENDMENT 3) found that the Dell agent users
(admin by Andrew's ~16:5xZ word) can read `teams/global/ingress-mark`. Row W10-S2 names those same identities among the ones that can
put an `sms.reply` on the queue. So in `enforce` they could forge a valid mark, and enforce would not stop them.

**RULED: NARROW, the REC.**
- A resource policy on the secret DENIES `secretsmanager:GetSecretValue` to every principal except the two assistant function roles.
  Only the value read is denied. Management acts stay open to admins (`PutSecretValue` for rotation, `PutResourcePolicy`, describe,
  delete), so nobody is locked out of operating the key, only out of reading it.
- It is its own WORLD cell with its own never-widen pair, cut and applied BEFORE CA-j-5's enforce flip. The flip's pair reads the
  policy live: a Dell agent user's simulated `GetSecretValue` is `explicitDeny`, and each function role's is `allowed`.
- **The residual, stated in the PRD either way (addendum beside v0.7's):** an admin can rewrite the resource policy and then read
  the key. That is a management write, recorded in the org trail, never a silent forgery. It is the same class as the handler-change
  limit accepted for muse.
