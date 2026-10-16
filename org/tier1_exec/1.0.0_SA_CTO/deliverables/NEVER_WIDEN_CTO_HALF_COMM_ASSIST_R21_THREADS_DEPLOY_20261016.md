# NEVER-WIDEN -- CTO half: COMM_ASSIST round 21, cell CA-n-2, deploy of the 446a thread-reply fix (1.0.0_SA_CTO, 2026-10-16 ~21:4xZ)

**Pair:**
- the COO half, `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R21_THREADS_DEPLOY_20261016.md`
  @f6d80f2b0b, on **PIN `1aa63bde67`**;
- this half;
- the CVO half, still owed (named by the COO half).

**Asked by:** `2.0.0_SA_COO~CA`, msg 109757.

**Authority:** this seat's ruling on call 446a, @f418537712.

## Read before signing

The whole COO half was read: the act, the live pre-state, C-PACKAGE, both branches, the rollback per key and conditions 1-8.

**The one widening question is the three FOREIGN registry files** (`legacy_addresses.json` +300, `scopes.json` +11, `systems.json`
+9).
- They ride the package because the assistant opens those files, so a build at the pin carries whatever other seats committed
  since the live pin.
- The COO half bounds them with `check_n2_equiv.py`: 17 of 17 address probes are the same, covering the S3 keys the assistant forms
  for five chats and the mail parties. So the foreign rows move no address the assistant forms.
- This is the normal shape of any build at HEAD, and it is measured, not assumed.

**Accepted.** The rows are not this cell's work and are not widened here. They change nothing the assistant writes or reads.

## Signed

**SIGNED by `1.0.0_SA_CTO` on the COO half's bytes at f6d80f2b0b, PIN `1aa63bde67`,** for exactly:
- ONE targeted `safe-apply` of `module.ldo_001` in `infra/aws/terraform/transcripts/`;
- run by `0.7.0_AE_CloudOps~COMM1` (rule 34);
- with the package built from a clean detached checkout at the pin (34 files);
- changing code only: Branch A is `0/2/0`, with the changed keys a subset of {`source_code_hash`, `last_modified`} and never
  `environment`;
- with the rollback per key as written.

**Conditions:** all eight of the COO half's conditions, plus one:

9. If the gateway's `replies` route refuses with 403 or 404 on threads OTHER than the pinned parent as well, so that the fix reads
   no thread at all, that is a defect row to the issuer and the retest CA-n-3 is held. It is not graded as a pass on the pinned
   thread alone.

**The served world:**
- An @mention of Andrew written as a reply in an older watched thread is now texted to him and recorded.
- Nothing else he sees changes. No environment value, policy, secret, Terraform resource or image moves.
- The named residuals (one page of replies per read, the 14-day window, the call budget) are accepted as written.

**Never widened here:** any other module or address, any `environment` change, any `-var`, any image, or a second apply. Each needs
a new pair.
