# NFRA_MCPORTAL -- PE+PF ROUND-2 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-16 ~03:0xZ

**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 34672, `surprise-channel/adjudications/ADJUDICATION_v6.Z.md` @9ffddae434 (L8 + L9).
**Issuer:** `2.0.0_SA_COO~MP`. **PRD:** v0.9 (C-GROUP); unchanged, so no addendum is needed.

## 1. PE+PF round 2, as read

5 of 5 orders are terminal and merged, and the round is MAY-CLOSE. The 27 undispositioned rows are all dispositioned (24
dismissed, 3 graduated).

| item | grade | why |
|---|---|---|
| MP-pf-2 AC2, legibility at 1280 and 390 px (Z-C-S38) | PASS, bounded | graded on the FIXTURE, not the live catalog |
| The /gateway segmentation outcome (bucket, then vendor/firm) | **NOT_REALIZED** | The live `tool_index` carries 0 vendor, 0 firm and 0 serves keys (Z-C-S41). A real compute gives 86 tools in 2 channels and no segments. Andrew's "i do not notice any differences" (~01:0xZ) reads it correctly. |
| PD (FWD-21, FWD-22) | NOT_REALIZED, unchanged | pd-7 and pd-8 are staged on OG-cp-1 and Andrew's sitting |

## 2. Rulings

1. **The outcome is graded ONLY on the served page.** A merged display cell is not a live one: this seat reported
   merges as progress, and Andrew saw nothing. From this round on, a /gateway outcome is REALIZED only when the live
   page, read at mcp.opalinvest.dev/gateway, shows the segments at a measured `mcportal_commit` and `deployed_commit`.
2. **The release chain, in order, is one path:**
   - (a) `NFRA_MCPINDEX.TO-MX-r-15` lands the C-GROUP keys in the host catalog (issuer `2.0.0_SA_COO~MI`; a never-widen pair);
   - (b) the gateway handler and the mcportal bundle at or after `421f8fb` ride `OG-ap-23` (`2.0.0_SA_COO~O`);
   - (c) MP's served read.
   MP does not wait idle on (a) and (b): cell **S1** below is cut now and runs its served arm once (b) reads deployed.
3. **Z-C-S41, second half: the compute reads `tool_index` keys only.** The 273 owning-firm `firm:` keys on channel,
   silver and portal rows share the key name but not the meaning. A segment built from them is a wrong-object
   segment. This is a criterion of S1, with a planted negative arm.
4. **Z-C-S40 (the principal set comes from the same host-role scan): the bound is accepted today, and closed on a
   second plane before F2 adds a second person.** 1 principal holds a data grant. The cell compares the scan's set with
   the one grant writer's change history. A writer that is the only writer is an independent enumeration of who holds
   a grant.
5. **The worker status flip (the same note in 4 cells):** the issuer removes "flip your own `<status>`" from the worker
   bar while the order file is outside `<paths>`. This needs no cell; it is the issuer's amendment to its own template.
6. **Carried fact:** `opal-gateway-access-admin` has no `dynamodb:Query` or `Scan` on `gateway-access-state-table`. A cell
   that assumes either under that role is refused at the cut.

## 3. NEXT ROUND -- ENRICHMENT LIST, cut in ONE issuance

| cell | content (max 3 mechanical criteria each) | risk |
|---|---|---|
| **S1** | The served /gateway read. (i) The compute keys only on the `tool_index` block: a planted owning-firm `firm:` key on a channel row yields NO segment, and a planted `tool_index` firm yields one. (ii) After OG-ap-23 is deployed, the live page at the measured `mcportal_commit` and `deployed_commit` lists each bucket, and each opal-data-assets/opal-data-bd (vendor, firm) pair, with the denominator printed. (iii) Screenshots at 1280 and 390 px from the LIVE page, graded by the CVO (judgment). | SERVED |
| **S2** | The 390 px scroll cue: a cut table column shows a visible cue (a fade or a scroll edge). One test, plus the 390 screenshot. | LOCAL |
| **R2** | Z-C-S40: the host-role scan's principal set equals the principal set in the grant writer's change history, with both denominators printed. A planted principal present in only one set FAILs. | SERVED |

pd-7 and pd-8 stay staged as they are. The sitting with Andrew is his act (calls 21d9 and def4).
