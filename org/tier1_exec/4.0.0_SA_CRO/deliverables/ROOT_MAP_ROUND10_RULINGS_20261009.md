# Root map, LGIC_BLANKFIX round 10 E4 -- the nine held entries, ruled

**By:** `4.0.0_SA_CRO` (registry owner of `infra/logic/registry/**`, CTO ruling 106332), 2026-10-09 ~08:0xZ.
**Asked by:** `1.0.0_SA_CTO` msg 107830, on the round-9 analysis @a691359c6f item E4: rule each held entry's blocker so dell1's
cell writes the entries and fills the holes they open. Entries as drafted:
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/MAP_ENTRIES_round8.json`.

## R10-1. shared-infra: system `cloudops`

| field | value | why |
|---|---|---|
| system | `cloudops` | The root is the estate's shared base (the organization CloudTrail trail, the drift producer, shared alarms and IAM). Its maintainer is platform operations: `cloudops` is the PLATFORM_SUBSYSTEM row whose owner Andrew confirmed (D12 "Platform Operations", ~18:4xZ 2026-10-07). A plurality of name tokens (advi 9 of 89) is not an owner, as the worker said; the maintainer is. |
| scope | `global` | as drafted: seven stores across five scopes, so no one scope is true of the root |
| source | `cloudops` | the HOME value: the root's own system. The 27 secrets belong to many vendors, so no vendor is true of the root |
| fills | `[]` | as drafted: the default fills no blank, so every name keeps the system its own tokens give it |
| exceptions | measured by the cell | each name whose canonical form leads with another system, as the round-6 measurement does. A long list is the measured truth that the root is shared. Splitting it is that root's own migration (R19), not this entry |

## R10-2. astn-pipeline: system `news`; the `astn` token stays unresolved

- `astn` names a closed macro, not a system: ASTN_WSJFT, "CEO Daily WSJ & FT News Digest", closed 2026-08-25 in the
  spring clean (`org/projects/ASTN_WSJFT.json`; `systems.json` `unresolved[token=astn]`). What the root does is a WSJ and FT
  news digest, which is the `news` system's (news-intelligence, D8; Andrew confirmed the owner ~18:4xZ 2026-10-07).
- Entry: system `news`, scope `global` (W3-S11, confirmed in round 8), source `news` (the HOME value; the feeds are two vendors
  and Bright Data), fills `[]` (the default must not fill a blank of an `astn-*` name).
- The 13 names that raise on the token keep their names: the cell drafts `none_owed` name rulings on the R9-1 precedent
  (trade). They leave when a project reclaims the digest ("we can reinvent a project", the closing phase) or the root is torn
  down.
- If Andrew reopens ASTN as its own macro, this entry's system moves with it. That is a "not yet" with no cost while it waits.

## R10-3. The five multi-vendor roots: scope `global`, source = the product

The refusal is the schema's own rule, and the schema also gives the answer. `NAMING_SCHEMA.json` `key.scope_rule`: "A PRODUCT
key is a scope only beneath a VENDOR source (a feed for the product: pathfinder/etfs), never beneath itself as the source --
mdpf/global/..., never mdpf/mdpf/...". The registry already enters a product's own roots this way: `investor-reporting/*` take
system `irpt`, scope `global`, source `irpt`. So:

| root | system | scope | source | fills |
|---|---|---|---|---|
| mdpf-pipeline | mdpf | global | mdpf | `["system"]` |
| etfs-reports | etfs | global | etfs | `["system"]` |
| etfs-canon | etfs | global | etfs | `["system"]` |
| etfs-netassets | etfs | global | etfs | `["system"]` |
| harvest | harvest | global | harvest | `["system"]` |

- `scope` leaves `fills` on etfs-reports and etfs-canon: `global` is a HOME value and fills nothing. `source` is never in
  `fills` on these roots, because their feeds are several vendors.
- A single item that is a vendor's feed for the product (etfs-netassets' trueshares and pathfinder pulls; harvest's
  `raw/<vendor>/` keys) takes `<vendor>/etfs` or `<vendor>/harvest` in its own key ruling, per the same schema line. That is
  the cell's per-item work, not the root default.
- Exceptions stay as measured in round 8 (harvest's 11 amgt names; 0 on the others).

## R10-4. The two empty roots: RETIRE, confirmed

Measured 2026-10-09 ~08:0xZ, read-only:

| root | tracked files | Terraform state (`opal-313476888478-terraform-state`) |
|---|---|---|
| canonical-schwab-si2-schedule | `main.tf` (terraform, provider and locals blocks only), `.terraform.lock.hcl` | `canonical-schwab-si2-schedule/tfstate`: serial 5, **0 resources**, last written 2026-08-04T05:12:30Z |
| opal-assets-absence | `main.tf` (the same, after teardown @c32875f7a5) | `opal-assets-absence/tfstate`: serial 3, **0 resources**, last written 2026-07-18T01:17:42Z |

Both were torn down and applied, so removing the folders orphans nothing. The act: `git rm` the tracked files of both roots,
and delete each box's untracked leftovers (`org/` stray folders, `.build/`, `frontier-token.tfplan`) there. The two empty state
objects stay: an S3 delete is an act only Andrew can do, and nothing needs it. After the removal the census reads
`roots_total=85`, so FWD-2's "every root" is 85, not 87.
