# ANDREW DIRECT -- shut off the Opal_Terminal key if site Z does not use it (2026-10-13 ~16:3xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `1.0.0_SA_CTO~DELL2`, answering the Opal_Terminal card (open call
`dell2-20261011T063600Z-e260`). **Verbatim:**

> As long as SITEZ does not use Opal_Terminal then we can shut it off.

Earlier in the same session he said the key "was sent via taildrop, so it should be accessible via the taildrop folder on the desktop
of this box", and asked whether dell2 and dell1 use that key.

## What this seat measured (2026-10-13 ~16:2xZ to 16:3xZ)

- **The condition holds.** IAM user `Opal_Terminal` has ONE access key, Active, created 2026-07-10 22:08Z.
  `get-access-key-last-used` reads LastUsedDate `None`, so no machine has ever used it, site Z included. There is no console login
  profile.
- **dell2 and dell1 do not use it.** This box signs as `cloudops-dell2-agent-user`, its only profile. IAM holds a separate
  `cloudops-dell1-agent-user`, created 2026-10-07.
- **This box does not hold the key.** `Desktop/taildrop-20261012/` is empty, and no key file is in Downloads.
- **The shut-off was REFUSED to this seat:** `iam:UpdateAccessKey` hits an explicit deny in
  `cloudops-dell-agent-iam-roles-policy`. Dell agent users may not change IAM users, by design. The key is still Active.

## The act left

Set the key Inactive. This is reversible: setting it Active again restores it.
- Who can do it: Andrew in the IAM console (Users > Opal_Terminal > Security credentials > Make inactive), or a seat on an identity
  without the Dell deny.
- Afterwards, FWD-8 of NFRA_TRNSPT is graded by an IAM simulation of the second-reader role's trust, not by a live read under the key.

-- recorded by 1.0.0_SA_CTO~DELL2
