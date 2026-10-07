# NFRA_OPLGTW -- ROUND 20 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-06 ~08:5xZ

**L10 on `3.0.0_SA_CVO~O`'s round-20 slug** (msg 29976, `surprise-channel/remediations/REMEDIATION_v8.md` @5b1e8736eb):
- 10 rows: 7 dismissed and 3 OPEN for this seat.
- Z-W15-S58 is REMEDIATED.
- The r20 guards W1-W3 held on the deployed host.
- No L9 grade.

**The issuer's terminal message** is msg 29974: round 20 is terminal at 3 of 3. r20 `2c27f3a795` went LIVE at 08:17:45Z
and CLOUD equals live.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 20 did

- **OG-lg-1, then OG-rl-8 (r20, LIVE).** `/login` runs the R24 rule as amended by R25:
  - the effective set is unchanged from live (every verified, non-email-denied tenant identity);
  - the backstop fails closed;
  - opalbloomberg@ is admitted, with its allowlist still fencing dispatch.
  - The CVO's W2 was read on the installed code: a non-restricted identity is ADMITTED via `tier_graph_tools`, and a
    restricted one gets 403.
  - Each `/login` request writes one `gw_login` record carrying no secret, which closes S52 on the host and in the lake.
- **OG-fl-1.** It fixed a product defect: the engine's RSS-poll objects are now built once. `test_ogx2_ac01` runs
  deterministically (20 of 20 by the worker, 8 of 8 by the CVO).

## 2. Outcome grades

Unchanged: **0 REALIZED, 0 NOT_REALIZED, 8 HELD, 0 DEFERRED.** Every FWD waits on a human act:
- OG-v-7 (Andrew's own tests, then Alyssa);
- G-E (Menachem's tid/oid);
- Z-W15-S41 (Andrew's grant word);
- R7's host-side flag.

## 3. Rulings

**R26 -- the three rows routed to this seat.**

- **Z-S57 (the kit is half retired). This seat's R20 was WRONG, and the row is OPEN.**
  - R20 marked Z-S55 REMEDIATED on a read of `README.md` alone.
  - At HEAD, `.tools/m365-mcp-kit/` also holds `.mcp.json` (the local Lokka server) and `.claude/skills/{onedrive,
    outlook,sharepoint}/SKILL.md`. That listing was read this turn, 5 files in all.
  - A colleague who opens the directory is offered a server that cannot connect.
  - **The remedy is OG-dc-2:** the directory holds `README.md` only, and the other 4 files are removed.
  - Z-S55's REMEDIATED stands only as of R20's narrower read. Z-S57 carries the remainder.
- **Z-W15-S64 (the Glue table sees `gw_login` as `ts` and `outcome` only): (b).**
  - The RAW lake prefix is the `/login` instrument of record. The JSON records carry every field, and the Glue table is
    left as is (build ladder: no schema change for a reader nobody runs today).
  - The Schwab pilot runbook's support section names the prefix and the `gw_login` fields.
  - Querying `/login` at scale through the table re-opens this as a Terraform schema cell.
- **Z-W15-S65 (`EC2_MANIFEST.json` `file_checksums` is unmaintained): the opal-gateway map is EMPTIED to `{}`.**
  - `{}` is the estate's convention: every other service's row carries `{}`, as does `EC2_DEPLOYMENT_PROTOCOL.md:147`.
  - Add a `_checksums_note`: "not maintained; `deployed_commit` plus the release's host md5 read are the record".
  - A stale value that reads as measured is worse than no value.
  - No code reads the map. The census found 54 hits, 1 SURFACED, and that one is a check-script comment.

## 4. THE ENRICHMENT LIST ROUND 21 CUTS (one issuance, `2.0.0_SA_COO~O`, all LOCAL, no release)

1. **OG-dc-2: Z-S57.** Remove `.tools/m365-mcp-kit/.mcp.json` and the three Lokka skills; the directory holds
   `README.md` only.
2. **OG-mf-1: Z-W15-S65.** Set the opal-gateway row's `file_checksums` to `{}` and add `_checksums_note`.
3. **OG-o-6: Z-W15-S64.** One paragraph in the runbook's support section naming the raw lake prefix and the
   `gw_login` fields as the `/login` instrument.

**After round 21, NFRA_OPLGTW owes no engineering cell to any FWD.** The issuer cuts no round 22 unless a slug, a
human act or a ruling creates one. The project parks on:
- Z-W15-S41 (at Andrew);
- OG-v-7 (Andrew's own tests, then Alyssa);
- G-E (Menachem's tid/oid);
- R7's host-side flag;
- Z-S43 (the meeting invitation).

**Carried to NFRA_OPALAI, not cut here:** R25.3, the scoped identity's consent envelope narrowed to its allowlist's
Graph scopes.

## 5. What this analysis does not do

It deploys, applies and grants nothing. It re-measured only:
- the `.tools/m365-mcp-kit/` listing (5 files);
- the `file_checksums` census (comp-find, 54 hits across 57,753 files, 1 SURFACED).
