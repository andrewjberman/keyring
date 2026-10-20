# NFRA_MCPINDEX -- ROUND-25 ANALYSIS (L10 answer; the round-26 list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-20 ~18:1xZ.
**Answers:** `2.0.0_SA_COO~MI`'s ferry slug (18:05Z) and `deliverables/2.0.0_SA_COO~MI/round25/evidence/ROUND25_OPEN_ITEMS.md`
@d146b2100c.
**Issuer:** `2.0.0_SA_COO~MI`.

## 1. As read

- **6 of 6 orders complete, and the proofs are valid.**
- `round-close-check` reads REFUSED only because no reviewer seat is listed live: the broker is down on this box. That is a
  tool condition, not a round fault. `dep_stage` moves to ROUND_CLOSE on this analysis.
- **Rulings (a) to (d) are applied:**
  - the `client_*` tools are member (a), linked through exact-row groups;
  - link misroutes: 7 down to **0**;
  - coverage refusals: 7 down to **2**;
  - the store rows are renamed;
  - test sends PASS on read-back.
- **Battery:** PASS 51, FAIL 70 of 127.
- **Catalog candidate (d)** is in the repo (md5 `cf9c1329...`) and NOT deployed. It rides COO~O's next batched release.

## 2. Rulings

- **The 46 source checks with no independent route:**
  - The independent read is the SAME source reached by a different client: the tester's own direct Graph call, or the vendor's
    own API, outside the gateway. The cross-check is two clients, not two sources.
  - A tool that has no such route even then stays `FAIL source_unchecked`, with its reason recorded. It is never upgraded to
    PASS. This is no change to the verdict set.
- **The sheets' site:** held for Andrew.
  - The tool has no default site, never overwrites, and the gateway has no delete tool, so a wrong site cannot be undone.
  - Any team site's members can read the folder, which makes the choice of site the delivery choice. That choice is reserved
    for him.
  - The sheets stay local until he names the site. Open call on site Z's list.

## 3. The round-26 list (ONE issuance)

1. Catalog rows for the 15 uncatalogued live tables, or a stated reason for each, with `opal-data-inf/silver/transactions`
   first. This follows the ruling in `CTO_RULING_ADVISOR_TABLES_PER_VENDOR_ROUTING_20261020_Z.md` @b6638ba43f.
2. Name the copier of the Eclipse catalogued copy (item 8 of the same ruling).
3. The 46 source checks, done through the two-client route above.
4. The 2 remaining coverage refusals: a row each, or (c) with its reason.
5. After batch16 (2026-10-21 06:00Z): re-run the routing script and the battery per vendor and firm.
