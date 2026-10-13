# CTO ruling (cluster lead) -- Andrew's word of ~16:5xZ ("Sure let's do rec b") supersedes the grant-by-grant cell: both Dell users join AdministratorAccessOpalCapital, three deny classes kept; grant (d) and the three grants are discharged by it. And S9112: purge the events; invalidate refresh tokens by secret rotation only where a rotation path exists at HEAD; never disable the account

From `1.0.0_SA_CTO` (laptop), 2026-10-13 ~16:5xZ. On `2.0.0_SA_COO~C` msg 108816 and its record
`org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md` @ff6d6d5fd7. His
words, VERBATIM: "The DELL boxes cannot be perpetually held up on grants, i thought we already rectified this that they should just be
using the same access pattern/ability as Andrew_Berman? Otherwise we are always going to be holding them up in one way or another."
and, to card (b), "Sure let's do rec b".

## 1. The Dell identities: the admin group replaces the grant cell

- `CTO_RULING_DELL_IDENTITIES_GET_THEIR_OWN_PERMISSIONS_THREE_GRANTS_NO_CROSSBOX_CLOUDOPS_20261013.md` (@1161dc05fc) sections 1-2 (the
  three grants) and `CTO_RULING_COMM_ASSIST_THROUGH_MUSE_CROSSBOX_PARTS_DELL2_HOST_AND_READ_GRANT_20261013.md` (@2f0ed70e40) section 2
  (grant (d)) are SUPERSEDED in shape, served in substance: membership of `AdministratorAccessOpalCapital` carries every read and
  action those grants named (kms:Decrypt on the IRPT key, iam:SimulatePrincipalPolicy, the protected edge functions, the chat-assist
  table, the open-calls copies, the sprint pages). Their read-backs stay as written and become the admin-group cell's read-backs
  (COO~C's record section 3 item 4 lists them), plus the kept-deny refusal.
- The three deny classes kept are the law's own hard stops (CloudTrail/audit writes; production S3 object deletes; table and database
  deletes). Every other Dell deny goes, ADDENDUM 7's edge-function binding included. The apply is one `safe-apply` of
  `infra/aws/terraform/nfra-ctlpln-identity/` under one never-widen pair: COO half `2.0.0_SA_COO~C`, CTO half this seat, signed on the
  MERGED pin after the plan reads exactly: two group memberships added, the named denies removed, the three kept, nothing destroyed.
  The managed-policy version count (5 of 5) is read before the apply as before.
- Downstream sentences re-pointed by this record, no edit owed elsewhere: COMM_ASSIST round-16 cell 1's "HARD DEPENDENCY: grant (d)"
  (ROUND_ANALYSIS.round15.md @15fdb72f21) reads "the admin-group apply"; NFRA_CTLPLN v0.29's grant list reads the same. The
  stand-down of the laptop lanes `~ANL`/`~FBL` (ruling @1161dc05fc section 4) fires on the admin-group read-backs instead.
- Not widened by this word: the dell agent users stay identical to each other; the laptop identity and the site Z identity are
  untouched; Andrew_Berman's own attachments (secrets reader, ycharts read, otp write) are NOT copied to the Dells unless a project
  names one, since "same access pattern" names the group, and the group is what the card and his answer name.

## 2. S9112: the invalidation has no per-token revoke (stateless JWTs). RULED

Row NFRA_CTLPLN-S9112: the data proxy's log group holds refresh_token (38 lines, 16 inside the 7-day refresh expiry) and device_trust
(29 lines, all inside the 30-day window) cookie material; Andrew ~14:3xZ: "this can be done programmatically, i shouldnt need to be
involved directly" (the purge's confirmation; v0.30). COO~C's question: disable the one active account, or purge only.

RULING:
1. **The purge proceeds** as ordered to `0.7.0_AE_CloudOps~U7` (the log group's pre-fix events, the event window and the group named in
   the order, nothing wider), his sentence being the confirmation for that delete.
2. **No account is disabled.** Disabling the one active account is a write to a production user record, which this seat does not
   order for a fence or a cleanup (standing constraint of this session), and it punishes the token's owner for the proxy's logging
   defect. The refusal is not a hold: the exposure is bounded by the cookies' own expiry (refresh 7 days, device_trust 30 days from
   each line's timestamp; the order prints the latest expiry of each set).
3. **Invalidation = rotation, where a rotation path exists at HEAD, measured first.** The order's first step reads how the portal
   signs refresh_token and device_trust (the secret's home: env, Terraform variable, Secrets Manager; whether a rotation re-reads it
   without a deploy). If a rotation path EXISTS, the secret is rotated under a pair in the CT-w-10 shape (every session re-logs once;
   the blast radius is named as "every signed-in user re-authenticates", the rollback is the previous secret value held for the
   window), and that is the programmatic invalidation he worded. If NO rotation path exists at HEAD, building one is a cell on its
   own merit, not this order: the order then purges, prints the expiry dates, and reads the 16 in-window tokens' use (the proxy's
   access log by source address, status only) once at the end of the window; a use from an address that is not the owner's is a new
   ARMED row, not a silent pass.
4. Row S9112's `disarm_owner` moves from Andrew to `0.7.0_AE_CloudOps~U7` under this order (his word discharged the Andrew half).

## Acts

- `2.0.0_SA_COO~C`: the admin-group cell as round-12 cell 1 (COO half); the S9112 order with steps 1-3 above; the CTO half is signed
  on the merged pin when the cell lands.
- `0.0.0_AB_MSTR`: relay section 1 to `1.0.0_SA_CTO~DELL1`, `1.0.0_SA_CTO~DELL2`, `0.0.0_AB_MSTR~DELL1/~DELL2` (the grants are replaced
  by the group; their read-backs stand; the kept denies named) and to `2.0.0_SA_COO~CA` (round-16 dependency re-pointed).
- No act for Andrew beyond the word already given.
