# NFRA_MCPINDEX -- ROUND-22 ANALYSIS (L10 answer; the round-23 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-19 ~16:0xZ.
**Answers:** `2.0.0_SA_COO~MI`'s slug, msg 35994. Record: `deliverables/2.0.0_SA_COO~MI/round22/` @31775abb84, @326cfa533a.
**Issuer:** `2.0.0_SA_COO~MI`.
**PRD:** v0.18 @4b8dcf3b86 (ADMITTED, CVO @2be4cf2645).

## 1. As read

- **The census, read from the SERVED page** (`evidence/GATEWAY_SURFACE_CENSUS_20261019.json`): 7 channels, 103 tools.
  - bucket opal-data-assets: 5 tools, 8 vendor/firm segments;
  - bucket opal-data-etfs: 18;
  - bucket opal-data-harvest: 14;
  - bucket opal-data-mdpf: 1;
  - bucket opal-data-portal-v2: 18;
  - store dynamodb: 4;
  - native m365: 43.
  - The served page lists NO `integration` channel today. The YCharts, Schwab and Black Diamond tools sit inside the channels
    above.
  - The denominator is what the page lists (PRD v0.18). If an integration channel appears on a later release, it enters by
    addendum.
- **FWD-23, NOT met.**
  - All 14 harvest tools are member (b), and 4 of them have no catalog row.
  - Fabric-wide: 94 member-(b) tools, and 106 rows with no served `read_tool`.
- **FWD-24 on harvest:** PASS 10, EMPTY-CORRECT 4, FAIL 0. The planted tool reads FAIL, so the negative arm holds. Senders are
  untested, which is correct: no sender is in harvest.
- **FWD-25:** one sheet generated, for the owner (`sheets/andrew.md`). Its harvest examples were not re-run as the principal,
  and it was not delivered. Every other bucket reads "NOT YET TESTED", which is honest and correct.

## 2. Ruling on the FWD-24 transport (the slug's ask): CONFIRMED

- The battery is ONE committed script. Its calls run through a signed-in session's own gateway connection.
- Each run records the calling principal by ROLE (owner, standard, read_only), never by identifier.
- No unattended credential is created for it. Minting one would be a new standing credential, a widening this outcome does not
  need.
- An owner run cannot produce `REFUSED-CORRECT`. Refusals are graded in-process on the host instead, through the installed
  code's entitlement decision for a named principal and tool, as `OG-ap-35`'s read-back did. No call is made as that person.

## 3. Ruling on FWD-25's proof arm (clarifies v0.18 R3, no ENDPOINT change)

- "Every example re-run as that principal" is met by two things together:
  - the example passes on a signed-in run;
  - the installed `decide()` on the host ADMITS that tool for that principal's current grant, read in-process, with no call
    as the person.
- A wait on the person's own session is not on the path (rule 27 L2).
- **The first non-owner sheet** goes to an employee whose current grant spans two buckets. Any of the 15 read_only, no-profile
  staff qualifies, because each already reaches harvest and etfs (`4.0.0_SA_CRO~Z` roster @dc5a0b1b0b, section 2). Seed it
  with `Adam Muller`, head of asset management, which matches Andrew's harvest seed.
- **Delivery:** the sheets are written to the default SharePoint folder that v0.18 names. Sending them to people waits on
  Andrew's word on the roster. That is a carrier choice, not a proof arm.

## 4. The round-23 list (ONE issuance; fan out by channel, cap 8)

1. **E1, FWD-23, harvest first:** `measure.py` reads the harvest rows, so the 14 harvest tools move to (a). The 4 rowless tools
   each get a row, or a (c) with its reason.
2. **E2, FWD-23 across the other channels:** one cell per channel (etfs, portal-v2 with mdpf, assets with its 8 segments,
   dynamodb, m365).
   - Each of that channel's (b) tools moves to (a) or (c).
   - Each of its rows without a served `read_tool` gets one, or is listed with its reason.
   - The fabric totals (94 and 106) must reach 0 or an explained remainder.
3. **E3, FWD-24 across the same channels:** the battery runs per channel, with verdicts PASS, EMPTY-CORRECT, REFUSED-CORRECT
   (in-process), PREVIEW-ONLY or FAIL.
   - Senders stay PREVIEW-ONLY while open call `c5c2` is held for Andrew.
   - The m365 reads run on the signed-in principal's own data only.
   - Every FAIL in gateway code goes to `2.0.0_SA_COO~O` as a defect cell. A FAIL in a catalog row is fixed here.
4. **E4, FWD-25:**
   - Re-run the owner sheet's examples under the section 3 rule.
   - Generate one sheet for Adam Muller with the in-process admit check, and write it to the default folder.
   - Print the count of employees without a live profile beside the count of sheets (the CVO's note @2be4cf2645).

**Out of this round:** grant changes. The six WIDENS and the eight unrecorded roles in the CRO roster are Andrew's, and they
are put to him in the live `1.0.0_SA_CTO~Z` session.
