# Andrew-direct -- 2026-09-21 ~16:23Z, at the `1.0.0_SA_CTO` terminal (live chat, mid-turn)

**Channel:** direct conversation with `1.0.0_SA_CTO`, mid-turn.
**Time:** 2026-09-21 ~16:23Z (measured `date -u`).

## VERBATIM, ENTIRE

> "We need to keep moving so if there is no mechanism for us to access these buckets, and our work
> is dependent on these buckets existing, then we need to create opal-data-inflectionwealth and
> opal-data-cottonwoodcapital and take care to not create them with restrictive bucket policies that
> land us in this situation."

## What I found before routing this, so the cell doesn't have to re-derive it

`infra/logic/registry/scopes.json`'s `inflection` firm entry (`display_name: "Inflection Wealth
Management"`) and `cottonwood` firm entry (`display_name: "Cottonwood Capital Advisors"`) confirm
Andrew's proposed names are the real, LGIC-consistent long forms -- matching the pattern the
`49financial` entry already uses (`bucket: "opal-data-<long>"`, no abbreviation).

**The exact mechanism of the original mistake is already documented in the registry, not just in
today's measurement:** `infra/logic/registry/exemptions.json`'s `opal-data-inflection` and
`opal-data-cottonwood` rows already name the fix -- three operator identities (`Andrew_Berman`,
`Andrew_Berman_Console`, `Opal_Terminal`) that should have been exempt from the per-firm Deny fence
from the first apply. Each row states its own consequence in writing: *"the fence applied with an
empty exemption list denied EVERY identity this estate holds, including the applying identity."*
Their `signoff_ref` shows why the fix never landed: the change-management ledger entry
(`20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md`) is still **OPEN/RED,
unsigned** -- and the identity that would need to sign and re-apply is itself locked out by the
policy it needs to fix. Root-only, per `IB-rtf-7`'s own preflight. This is not a new failure mode;
it is the SAME registry entry admitting it never got applied.

## The correct fix, so it is not repeated

1. **New buckets, registry-addressed, never hand-typed** (CLAUDE.md Rule 30). Update the `bucket`
   field on the `inflection` and `cottonwood` firm entries in `scopes.json` to
   `opal-data-inflectionwealth` / `opal-data-cottonwoodcapital`; `bucket_provisioned: false` until
   built. Do NOT rename the firms' `key`/`short`/aliases/tenant-codes -- those are referenced
   throughout the codebase and Andrew asked for new BUCKETS, not a firm rename.
2. **The exemption rows already exist and are correctly written** -- copy the SAME three-identity
   pattern from the `opal-data-inflection`/`opal-data-cottonwood` rows into new
   `opal-data-inflectionwealth`/`opal-data-cottonwoodcapital` rows in `exemptions.json`, citing this
   incident. **The load-bearing requirement: these rows must be in the policy the FIRST apply
   generates, not added as a later patch.** That ordering is the entire root cause.
3. **Mark the old buckets abandoned, not touched.** No delete (CLAUDE.md: S3 deletes need human
   confirmation, and nothing here asks for it). Add them to `scopes.json` as a LOCKED alias so the
   naming builder and any future cell does not re-target them; correct the stale alias note on
   `inflection`'s entry (*"opal-data-inflection does not exist yet"* -- it does, and is now
   additionally abandoned) while touching this file.
4. **Standard mechanism, nothing new:** `lib/opal_naming.py` for the address; a change-management
   ledger entry opened before the apply, its OPEN sentinel committed immediately; `.tools/safe-apply.sh`
   only; both never-widen halves (CTO + COO) before the apply, same as every served-property change
   in this project.

## Routing

This is infrastructure/registry work inside `IRPT_BCKEND`'s own decomposition -- a new cell, cut by
`2.0.0_SA_COO~B` under Rule 27, not built here. Sent with this full research so no round trip is
needed to re-derive the mechanism.

**PUSH STATE:** LOCAL -- this seat does not push a shared branch.
