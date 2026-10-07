# CTO never-widen half -- NFRA_OPLGTW OG-rl-11 (the r25 gateway release: send split + scoped consent) -- SIGNED

- **Seat:** 1.0.0_SA_CTO~O, 2026-10-07 ~04:2xZ.
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-11_20261007.md`
  @8a769f4b54 (msg 30545). The COO half is SIGNED there.
- **Release sha signed:** `240ac2fe5abde944f15358ab563cb4b2ab63f09f` (`rel-nfra-oplgtw-r25`), on live `7d65a28db0`.

## What this seat read itself

1. `git diff --stat 7d65a28db0 240ac2fe5a` is 8 files, +873/-28, all under `infra/aws/ec2/opal-gateway/`. They are
   the 8 files of the ask's section 1.
2. `git diff --stat 240ac2fe5a HEAD -- infra/aws/ec2/opal-gateway` is the runbook only.
3. The whole diff of `opal_portal/integration.py`:
   - The 45-iteration poll is removed. A real send does one 2 s sleep and one status GET (20 s timeout), then returns
     with `execution_id`.
   - The idempotency check runs BEFORE the upload. Its record is written only AFTER `/trigger` returned, so a
     failed trigger leaves no record and a re-send is allowed.
   - `opal_data_refresh_status` issues GETs only: the status route and the served manifest.
   - The send's `next` text names the fallback: the portal's displayed date, when the status tool is not available
     to the caller's identity.
4. R33 and msg 30365 are met as ruled. R33 named part 1 only. Part 2 (OA-f-14) rides because it is on CLOUD
   (@af10f7d42b), and its release-side condition, the live-host identity read, is in the ask's section 3(c).

## Signed for

- **Part 1 (the send).** A real send returns within 60 s of `/trigger`. A repeat of the same two files (name and
  size) within 30 minutes in the same gateway process does not trigger again. One read-only tool is added (66 tools).
- **Part 2 (consent).** The one scoped identity's consent narrows from 17 to 9 Graph scopes. `Files.ReadWrite.All`
  stays because the Tax workbook route mints under that identity (read TRUE on the live host). An unscoped identity
  stays at 17.
- **Rollback for both:** redeploy `/c/tmp/og-rb19` at `7d65a28db0`.
- **The four limits the ask discloses** are accepted. This seat adds a fifth, read from the diff: two DIFFERENT
  files with the same names and the same sizes, re-sent within 30 minutes, return the earlier execution. A corrected
  re-pull of equal size therefore waits out the window or a gateway restart. The response says so in `next`.

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act. If it is not `7d65a28db0`, re-cut and re-ask.
2. **Timing against the daily Bloomberg send (about 11:00Z).** The ledger is CLOSED, with every post-deploy read
   passed, by 09:30Z on 2026-10-07. If GO cannot meet that, GO waits until that day's send is confirmed served. The
   first live exercise of the new send path must not start inside a half-finished release.
3. The rollback triggers of the ask's section 4.5, each rolling back in the same session.
4. No `/login` for the concierge between GO and the ledger close. Its FIRST `/login` after the release is a planned
   act outside a send window, followed by the 9 probes re-read, because that is when the narrowing takes hold (row
   Z-W28-S11).
5. No `confirm=True` send is run by this project.
6. No grant, state-store, `.env`, secret, Terraform or IAM write, and NO allowlist row. Whether the concierge may
   call `opal_data_refresh_status` is put to Andrew by this seat. Until he answers, its caller confirms a send from
   the portal's displayed date.

The CVO half is REQUIRED and is asked by relay.

-- 1.0.0_SA_CTO~O
