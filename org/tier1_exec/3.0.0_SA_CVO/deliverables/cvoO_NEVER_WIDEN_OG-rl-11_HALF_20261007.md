# CVO never-widen half -- NFRA_OPLGTW OG-rl-11 (the r25 gateway release: send split + scoped consent) -- SIGNED

- **Seat:** 3.0.0_SA_CVO~O, 2026-10-07 ~04:20Z.
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-11_20261007.md`
  @8a769f4b54, relayed by `1.0.0_SA_CTO~O` msg 30552. COO half SIGNED in the ask; CTO half SIGNED @62a89fbf07.
- **Release sha signed:** `240ac2fe5abde944f15358ab563cb4b2ab63f09f` (`rel-nfra-oplgtw-r25`), on live `7d65a28db0`.

## What this seat read itself (~04:1xZ)

1. `rel-nfra-oplgtw-r25` is the release sha; its one parent is `7d65a28db0`; `EC2_MANIFEST.json` reads
   `deployed_commit` `7d65a28db0`. `git diff --stat`: 8 files, +873/-28, the ask's table. Release against CLOUD in
   the gateway tree: the runbook only.
2. **Tests, run by this seat on the release bytes:** `test_scoped_consent_r253.py` 7 passed,
   `test_opal_portal_send_split.py` 5 passed, `test_entitlement_admin.py` 9 passed.
3. **Part 2, the union, by subtraction.** The one scoped identity's allowlist is 11 seed tools
   (`identity_scope.py:54-78`) plus `opal_data_refresh_upload`, client-qualified (`identity_tool_allowlist.txt`, 1
   row): 12 tools. All 12 have a `TOOL_GRAPH_SCOPES` entry; 12 minus the map's keys is empty. Their union is 8
   scopes; `TAXSMA_WORKBOOK_IDENTITY` (a `<tid>/<oid>` binding, so unioned) adds `Files.ReadWrite.All`: 9, the ask's
   list exactly. `consent_scopes` reads the configuration per call, so the 9 is the code's answer on the host, not
   a typed list: a caller key later pointed at this identity widens the consent by itself.
4. **Part 2, the three legs.** Consent URL and redeem both go through `_consent_scope_list` with the same email;
   the silent acquire intersects the tier's scopes with the consent and falls back to `User.Read`. An unscoped
   identity gets `None` and keeps `GRAPH_SCOPES` on all three.
5. **Part 2, the callers of `get_token`.** 9 modules call it: 8 have a `CALLER_GRAPH_SCOPES` entry and the ninth is
   `tools.py`, whose tools are the tool map's own keys.
6. **Part 1, the send, read whole.** The 45-iteration poll is gone: one 2 s sleep, one status GET (20 s timeout),
   return. The re-send check runs before the upload and keys on the date stamp plus each file's name and size; the
   record is written only after `/trigger` returns 200. The new tool is declared `OpClass.SAFE` and issues GETs only.
7. **Who can call the new tool.** Signed-in identities at the integration's tier. The scoped concierge cannot: the
   allowlist is unchanged and deny-by-default, so no row admits `opal_data_refresh_status`. Its confirmation of a
   send stays the portal's displayed date until Andrew answers the CTO's question.

## Signed for

- **Part 1:** a real send returns within 60 s of `/trigger`; an identical re-send inside 30 minutes in the same
  gateway process does not trigger; one read-only tool is added (66 tools). Writers: N = 1 each.
- **Part 2:** the one scoped identity's consent narrows 17 -> 9; an unscoped identity stays at 17. Writers: 3 call
  sites through one function over one map and one caller table.
- **Rollback for both:** redeploy `/c/tmp/og-rb19` at `7d65a28db0`.
- **Limits accepted as disclosed:** the ask's four, and the CTO's fifth (same names and sizes inside the window
  return the earlier execution).

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act; if it is not `7d65a28db0`, re-cut and re-ask.
2. The CTO half's condition 2 stands for this half too: ledger CLOSED with every post-deploy read passed by 09:30Z
   on 2026-10-07, or GO waits until that day's Bloomberg send is confirmed served.
3. The rollback triggers of the ask's section 4.5, each rolling back in the same session. The real-holder read
   (2150 = 2150 = 2150, 0 unheld) and the portal login are re-read from the INSTALLED code after this release.
4. No `/login` for the concierge between GO and the ledger close. Its first `/login` after the release is a planned
   act outside a send window, and the delegated leg of the send (site resolve and the item read) is re-read on the
   9-scope token before a real send relies on it. Until then the narrowing is unproven on a real token (Z-W28-S11).
5. No `confirm=True` send by this project; no grant, state-store, `.env`, secret, Terraform, IAM or allowlist write.

## Not signed, filed for the owners

- **Row Z-S65 (filed by this seat).** `opal_data_refresh_status` formats the caller's `execution_id` into the URL
  path unchecked, and httpx collapses `../`, so a caller can steer the service account's GET to another portal path.
  The return is narrow (a top-level `status` key or an HTTP code) and the callers are internal, so this does not
  hold the release. A one-line shape check closes it; it belongs in the next cut.
- **The re-send key is name and size.** A corrected Bloomberg re-pull is the same two file names and very likely
  the same sizes, so inside 30 minutes it is answered `already_triggered: true` and not sent. The response says so.
  The SharePoint item's eTag or modified time would tell a corrected file from a retry.
- **Two identical sends started at the same instant can both trigger:** the check and the record are separate
  critical sections. The case R33 targets, a retry after a dropped transport, is sequential and is covered.

-- 3.0.0_SA_CVO~O
