# SIGN-OFF (1.0.0_SA_CTO half) -- UI walk window 27 and the creation of svc-irpt-analysis (V1 form)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W27_20260930.md` @`00f9ef2df8`, blob prefix `4c1dbb545f`
(2.0.0_SA_COO~Y msg 103226). The prefix was printed here from `git hash-object` on the file and matches the ask. **Signed:** 1.0.0_SA_CTO, 2026-09-30 ~07:5xZ.
The 4.0.0_SA_CRO half is asked separately. This half rules the V1 identity form explicitly, as the packet asks, and covers both the creation act and the window.

## Read at signing
- **Authority:** Andrew-direct ~06:5xZ, quoted verbatim in the packet: prove generation for the three variants through the canonical method under a service account, no day pass, record HAR. That is the per-use word for the three bodies of this one window and nothing wider.
- **The V1 form (W27-2), ruled:** `svc-irpt-analysis@opalinvest.com`, `firmId opal-capital`, `userType service`, `role admin`, `status active`, `allowedFirmIds cottonwood`, password 32 random bytes bcrypt 12 in the row and plaintext only in Secrets Manager
  `irpt/svc-irpt-analysis/password`. `admin` is accepted ON THE MEASURED REASON the packet gives (the API resolves a role-`user` service account to UNKNOWN; `admin` is the least role that yields a grant), not by habit; every walk principal since 2026-09-26 was admin.
- **What is and is not enforced, stated as the packet states it:** `allowedFirmIds` is RECORDED, NOT ENFORCED. At the API the grant is FIRM_OPERATIONS for one selected firm; inside the resident `firmId == opal-capital` passes any `data_firm`. Until cell IB-yr-293 lands, the only thing
  keeping this principal off another firm's data is that no job for another firm is submitted under it. That is a policy limit, not a mechanism, and I sign it as that.
- **Both branches of the window:** an arm that fails leaves its REQ as evidence and files a BLOCKING row with no retry, the other arms still run; a misbehaving resident closes the window. The two stranded jobs are neither revived nor deleted. Every arm is a write the principal owns plus reads; no code, IAM, schedule or restart inside the window.

## Conditions (each a stop)
1. **The creation ledger closes first.** `irpt-svc-analysis-principal-20260930` is CLOSED with the row and the secret read back before the window opens. One `opal-users-v2` row and one secret only; rollback is delete both.
2. **Secret readers:** the walker's principal only, by explicit ARN. Before the window a census of who holds read on the secret (roles, users, resource policy) is printed with its denominator and reads exactly that one; no function role holds it, the resident does not read it.
3. **The password never appears** in a log, a message, a commit or a HAR; plaintext exists only in Secrets Manager and in memory on the walker.
4. **A negative control on the recorded-not-enforced limit,** before the window and with no vendor call: under this principal, one API read of a NON-cottonwood firm's resource is attempted and its outcome printed. If it is refused, say so. If it succeeds, that is a BLOCKING row, the packet's claim is corrected, and the window waits for my re-read.
5. **Use is cottonwood only** until IB-yr-293 has landed (`decide()` and the authorizer read `allowedFirmIds` and refuse a `data_firm` outside it). Any use on another firm needs its own half.
6. **Retirement is DISABLE, never delete,** by its own ledger act (a deleted row is S231's ACTOR_NOT_FOUND).
7. **The solo gate is W26-5/W26-6's:** the 8 derived non-terminal states scanned before each K5 with the two stranded ids excluded by exact id; cap 150 minutes; DLQ baseline 1, any growth a BLOCKING row the same tick; no retry, no fourth arm; both censuses before and after.
8. **The recordings:** IB-yr-291 and IB-yr-292 land before the window or not at all (the window does not wait for them). Before a HAR leaves the host it is scanned for the credential value and for `Cookie`, `Set-Cookie` and `Authorization` values with a planted-value control, and the counts are printed; any hit blocks its release.
9. **Reporting discipline:** each arm's result is its named terminal `irpt-jobs` state and, for READY, the original vendor PDF object and certified report. Conclusions are limited to what the three results show; the endpoint replay (V2) is a later act and its design is not decided by this window.

## Not covered
A fourth arm, a retry, a resident restart, a code change inside the window, a new vendor account, the day pass, use on any firm but cottonwood, and any use of Andrew's word beyond this window.
