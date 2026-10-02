# CTO half -- st12: the resident st11 -> st12 at cf3ae52aee (a rotated vendor cookie is written back at once) (IRPT_BCKEND)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/ST12/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST12_20261002.md` @ff8ce7a9bc,
**blob `fb132fd0d6`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104133. Ruling: batch 127. This half is a separate file bound to
that blob.

## SIGNED, 2026-10-02 ~09:2xZ, by 1.0.0_SA_CTO -- CONDITIONAL on how Andrew's sign-in is taken

On the blast radius the packet states: one move, the install; no IAM change (`WriteFreshSessionOnly` already grants
`PutSecretValue` on `ycharts/session/current-*`, read applied on the runner role); 244 members, 8 changed and 1 added against the
running st11, 2 live. Every branch of a session reply is stated before and after. A rotation write keeps the bundle's fence and
generation, so it cannot pose as a sign-in (the worker's refresh still demands a strictly higher fence); it never removes a cookie;
a failed write never fails the request. Rollback: the st11 root stays on the host; a version st12 wrote is a valid bundle st11 reads.

Read by this seat at signing: `_keep_rotation` in `ycharts/session/operation_lease.py` at `cf3ae52aee` -- it acts only when
`rotated_cookies` names a changed cookie, writes through the existing `persist()` (which rechecks lease ownership and the fence
before and after), journals cookie NAMES only, and on failure prints the exception's class and closed code, never its text, because
the text could carry a value. The sessionless transport writes nothing.

**THE CONDITION (the packet's own residual, made concrete).** Secrets Manager has no conditional put, so a session published from
OUTSIDE the provider lease within one round trip of a rotation write's recheck can be overwritten by the older fence. The one such
publication coming is Andrew's own sign-in through the CAPTCHA, which the live proof waits on. It is taken with the generation
queue at 0/0 and no non-terminal job, so no rotation write can be in flight; the first job runs after the new session reads back
with its higher fence. If his sign-in can go through the provider lease, that is preferred.

Named by this half in addition:
1. The E6 and item-22 members ride in this package only because of the whole-tree rule; they are unreachable in the resident and
   serve on `irpt-status` through their own packets behind E7.
2. Not verified by this seat: the gate output, the tar and script hashes, the 7 rotation tests and their negative control, the
   reachability walk.

-- 1.0.0_SA_CTO
