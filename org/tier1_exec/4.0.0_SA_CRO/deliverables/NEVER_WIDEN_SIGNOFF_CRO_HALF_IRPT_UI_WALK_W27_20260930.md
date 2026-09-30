# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 27: the three-variant proof under the canonical identity, with the endpoint recording built in

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W27_20260930.md`
blob `4c1dbb545f` (at `00f9ef2df8`; the working file's hash equals the committed blob, 2026-09-30 ~07:5xZ). Supersedes W26 (this seat's W26 half is
withdrawn with it; that window was never opened).
- **Word diff:** W26's three bodies, cap and solo gate unchanged; the per-window principal and its credential and credoff are REMOVED; in their place a durable
  `svc-irpt-analysis` principal created once under its own ledger, its password living permanently in Secrets Manager; and two recordings of the vendor traffic (a
  per-job endpoint ledger in `receipt.json`, and a Playwright HAR of the login capture). Cells `IB-yr-291`, `-292`, `-293` land before the window or not at all.
- **Asked by:** 2.0.0_SA_COO~Y, msg 103227. **Other half:** 1.0.0_SA_CTO, which the packet asks to rule the V1 identity form explicitly. **This seat is not in the act.**

## VERDICT: SIGNED on blob 4c1dbb545f, with six conditions

This is the widest standing grant this seat has signed for the walk: a permanent admin-role principal, `firmId opal-capital`, whose scope INSIDE the resident is
`OPAL_GLOBAL` (any firm's data), with a firm restriction that is recorded and enforced nowhere. It is signed because Andrew ruled it in so many words ("We have a
long-lived token, just use it"; "svc account or otherwise"), because it removes S231's stranding cause and a per-window credential ceremony that added no protection, and
because the window submits for one firm only. The conditions below are the price of it: they make the restriction real before the reach is used.

### Read here (measured by this seat, 2026-09-30 ~07:5xZ)

- **`decide()` never reads `role`.** In `ycharts/generate/current_authority.py` the only occurrence of "role" is a docstring (line 6). Scope is `OPAL_GLOBAL` when
  `firmId == OPAL_HOME_FIRM` or `userType == GLOBAL_USER_TYPE`, else `OWN_FIRM` (the code, lines 100-102, 117-118). The packet's account holds.
- **`allowedFirmIds` is read by nothing.** No occurrence in `current_authority.py` or `_scope/resolve.py`. So the packet is right that the cottonwood restriction is
  recorded, not enforced, and that `IB-yr-293` is the enforcement.
- **`classify_principal`'s branch order** (`_scope/resolve.py` docstring): branch 2 OPAL_GLOBAL needs an explicit roster (empty by default), branch 4 needs role admin
  and a verified firm and yields FIRM_OPERATIONS "never OPAL_GLOBAL". The packet's reason for `admin` is what the code says. This seat read the docstring and did not re-run the
  installer census behind "no deployed Entry populates the roster".
- **The secret does not exist yet:** `irpt/svc-irpt-analysis/password` reads `ResourceNotFoundException`, consistent with "created once under its own ledger".

## Conditions

1. **`IB-yr-293` is landed and proven BEFORE the window opens, not merely before use on another firm.** The packet lets the window run while 293 is pending (only "cottonwood only" by
   convention). For a principal whose resident scope is global, a convention is not a restriction. Proof required in the ledger: a job submitted under this principal for a
   firm other than cottonwood is REFUSED by a named code (a negative control, run against the resident with no vendor call reached), and a cottonwood job is not.
   If 293 cannot land, the window runs only with the principal `active` for the window's span and set to a non-active status the moment its jobs are terminal, the
   status flip recorded with its timestamp.
2. **The CTO half rules the V1 form and this half signs the same attributes:** `firmId opal-capital`, `userType service`, `role admin`, `status active`,
   `allowedFirmIds cottonwood`. If the CTO rules a different form, this half re-affirms on the new blob.
3. **Creation ledger CLOSED before the window, with read-backs:** the `opal-users-v2` row read back with the attributes above and NO password field in the read (the bcrypt hash
   is not printed), the secret's existence and version read back without its value, and the secret's resource policy or the IAM statements that grant it listed:
   readable by the walker's principal only, by explicit ARN; the resident and every function role shown NOT to hold it (the packet's own claim, proved by
   `iam simulate-principal-policy` or by an explicit deny read, not asserted). The plaintext is never printed, logged or committed.
4. **The HAR is scrubbed by a check, not a promise.** The post-processing strips `Cookie`, `Set-Cookie` and `Authorization` values; before the file leaves the walker's host the
   ledger records a scan of the output for those header names with values, and for the known session-cookie name patterns, with the count (zero) and the scan's method. The raw HAR
   never enters the repo; only the scrubbed file and the endpoint census diff do.
5. **The vendor word is read literally:** three variants, cottonwood, one submission each, no retry, ad hoc now, the HAR as part of the walk (Andrew @51edcd3ee6, quoted in the
   packet). A fourth body, a retry, a second firm or a wider ROE needs its own word. Solo gate per W26-6 (the eight derived non-terminal states, the two stranded ids
   by exact id, count and page state printed) reads before each K5.
6. **Retirement is disable, never delete,** and the disable is on a stated trigger: the principal is set to a non-active status when the round that uses it ends or
   when 293 is reverted or found broken, with an owner (2.0.0_SA_COO~Y) named in the ledger. A standing admin credential with no owner and no exit is not covered.

## Named items (not refusal grounds)

1. **The two-party property is gone.** In W22-W26 a second seat's credoff meant the walker could not re-login. With a permanent password readable by the walker it can, by
   design. The compensating control is condition 3 (who can read the secret) and condition 1 (what the principal can do). Andrew's word was to drop the ceremony; this half
   records what that costs.
2. **`IB-yr-292` is a code change** to the session-capture script behind an environment flag; it lands under its own gates before the window and is not covered by this half
   beyond "not in the window".
3. **Global reach inside the resident is real** until 293. The packet names it correctly; this half names it as the reason for condition 1.
4. This seat did not re-open rows S230-S233 or the endpoint census `YCHARTS_GENERATION_ENDPOINT_CENSUS_20260930.md`.

## What this half signs against

Packet blob `4c1dbb545f`; Andrew's direct @`51edcd3ee6` as quoted; CTO 103196 and ~Y's 103213; W26's text as superseded; the V1 identity form in W27-2 as the CTO half rules
it; the three bodies in W27-3; the recordings in W27-4 with condition 4; the interval in W27-5; and conditions 1-6 above.
