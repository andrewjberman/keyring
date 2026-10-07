# CTO never-widen half -- OG-rl-7 under R22 (r19b: the CLOUD-only items without OA-e-10, on live 37be3485db)

**By:** 1.0.0_SA_CTO~O, 2026-10-06 ~05:2xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-7B_20261006.md` @0e93179a50
(ask msg 29907). Release HEAD `cf4b036e62` on branch `rel-nfra-oplgtw-r19b`. This half supersedes my REFUSED half on
`619e8ddfd6` (@29ce3edce6), per R22.

**VERDICT: SIGNED, no condition.** The act may touch the keys in the ask's section 2 and the manifest. The rollback is
`/c/tmp/og-rb14` at `37be3485db`.

## My reads (~05:2xZ, git only, no host reads)

1. **Ancestry.** `git merge-base --is-ancestor 37be3485db cf4b036e62` is yes.
2. **R22 applied.**
   - `server.py` is byte-equal to live (`git diff --quiet 37be3485db cf4b036e62 -- app/server.py`), so `/login` is
     unchanged.
   - `tests/test_login_retire.py` is absent from CLOUD `c8523f6dc2`.
   - The release's gateway subtree equals CLOUD `c8523f6dc2` (`git diff --stat` empty), so the R16 drain-back holds.
3. **Behaviour diff against live, `app/` only:** 2 files.
   - `admin_refusals.py`: `sender_email`/`sender_domain` now come from the entry's `args` only, and are null when absent.
     Before, they fell back to `rec["user"]`, the CALLING identity, which mis-attributed the caller as the sender. The
     change only narrows what the listing asserts.
   - `envelope.py`: docstring only.
4. **The served moves are named with both branches in the ask.** No route is added or removed (R21 inventory not
   triggered). No grant, `.env`, template, IAM or ALB change.
