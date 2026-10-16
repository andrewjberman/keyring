# NFRA_MCPINDEX ROUND 19 (ASSETS) -- L8 COMPILE + L9

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-16 ~18:4xZ, on `2.0.0_SA_COO~MI` msg 35179
(`deliverables/2.0.0_SA_COO~MI/round19/L8_PACKET_ROUND19.md` @6c6363b2c1, read whole).

**Terminality:** 3 of 3 orders complete (MX-c-24, MX-c-25, MX-c-26), round-close-check MAY-CLOSE (issuer). The release
catalog (blob `b81c48aa3c`) is on trunk and was taken by NFRA_OPLGTW `OG-ap-28` (release `bf9d23b518`, my half
@ffc2045889).

## This seat's read of the release catalog (`git cat-file -p b81c48aa3c`, parsed whole)

- **Totals:** 284 rows; `read_tool` on 192; `address` on exactly 4.
- **The four live rows:** `blackdiamond_live_{allocations,fees,transactions,unrealized}`. Each has bucket `opal-data-bd`,
  `firm: 49financial`, `firm_scope_rule: firm-scoped`, `read_tool` set to the matching `client_get_*` tool, and `address`
  `blackdiamond/49f-live/silver/<t>/`.
- **The legacy rows:** 9 `*_silver_legacy` rows, all now in `opal-data-assets`, with 0 `read_tool`. They are still OUT under
  the CTO's addendum @a0eb7cd450.

## L9

**1. The widening: does anything here widen a partner firm's read beyond its own rows? NO.**
- **Who sees the rows:** the four new rows are `firm: 49financial`. The issuer's host-side visibility matrix (the BEFORE arm
  on `d14445961d`, the AFTER arm on the release, equal sha256) shows them reaching the 49financial principal and opal-internal
  only: 0 cross-firm, 0 unknown firm.
- **What a partner can do with them:** a 49F principal sees its own rows' metadata. Seeing a row reads no data.
- **Who can read the data:** that goes through the `client_*` tools, which are master_admin only (OG-ad-1, still in
  `DATA_GRANT_TOOLS` and `TIER_ADMITTED_TOOLS` at `bf9d23b518`, read in my OG-ap-28 half). They read through the dedicated
  role whose four prefixes I measured single-firm (z08 on 100% of rows, my OG-ap-29 half).
- **Accepted.**

**2. Depth claims: is a monotone post-release grade the right reading of "stop pinning depth claims that age"? YES, with one
addition.**
- **What a depth claim is:** a floor measured at a time ("history reaches at least D as of T"). Data that moves forward
  satisfies a floor; data that moves backward violates it.
- **Monotone (served depth at least the claim)** passes the first and fails the second. That is the property a consumer relies
  on. Strict equality fails every forward publish, which is the noise this enrichment set out to stop.
- **Strict stays right at emit**, when claim and measurement share an instant.
- **The addition:** the row should say what kind of claim it is. Today a reader of a row cannot tell a floor from an exact
  value. Each depth claim should carry its `measured_at` and the word `floor`, so a reader knows it may be stale-but-true.
  Carried as an enrichment.

**3. MX-c-24 complete but not served.**
- MX-c-24 is graded on trunk (c24.AC1: bucket 197 of 197, vendor and firm 136 of 136, probe 8 of 8). It is **not** in
  `bf9d23b518`.
- On the host, the plain-words probe echoes `bucket` on 7 of 8 buckets and vendor/firm on 0 of 2.
- The outcome is therefore **NOT REALIZED** until a gateway release takes `NFRA_MCPINDEX.TO-MX-c-24` by name. I endorse
  the issuer's carried item 1.

## Rows of the round

- **Disposed by the issuer, read and accepted:** Z-S130 disposes the ten worker rows Z-W47-S1/S2, Z-W48-S1 and Z-W49-S1..S7,
  the five BLOCKING ones being the issuer's own order and check defects, fixed in A1 to A6 and re-graded. Z-S131 disposes
  Z-W49-S8/S9 and records S10.
- **Z-W49-S7** (the client-data check could not run; no hashed account-id list on site Z) is the box fact already ARMED as
  NFRA_MCPORTAL `Z-S63` on `0.0.0_AB_MSTR~Z`.
- **Watermark:** every round-19 row through `NFRA_MCPINDEX-Z-S131`.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S65",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T18:45Z",
    "one_line": "Round 19 L8/L9: no partner firm's read widens (the four new blackdiamond_live rows are firm 49financial, visible only to the 49financial principal and opal-internal, data behind master_admin-only tools and a measured single-firm role); a monotone post-release depth grade is the right reading, with strict at emit and each claim marked floor plus measured_at; MX-c-24 is graded on trunk but NOT REALIZED until a release takes it.",
    "class": "OBSERVATION",
    "spec_asserts": "The CTO's round-18 analysis enrichments for round 19: the discover echo (MX-c-24), the gold book open item (MX-c-25), the live 49F rows (MX-c-26); depth claims that age graded without false alarms; a widening confined to each firm's own rows.",
    "world_is": "Release catalog blob b81c48aa3c: 284 rows, read_tool 192, address 4 (blackdiamond_live_<t>, opal-data-bd, firm 49financial, firm-scoped, read_tool client_get_*); 9 legacy rows in opal-data-assets with no read_tool. Host visibility matrix after OG-ap-28 equals the cut (201 silver rows, firm 49financial 89, cottonwood 26, inflection 9, unknown 0). The discover probe on the host: bucket echoed 7 of 8, vendor/firm 0 of 2 (MX-c-24 not in bf9d23b518).",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-C-S63"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file -p b81c48aa3c6c0ce3e79628e55cc5e8501f73dcf3 (parsed by this seat)",
        "deliverables/2.0.0_SA_COO~MI/round19/L8_PACKET_ROUND19.md @6c6363b2c1 section 2 (host visibility matrix, discover probe)",
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-28_20261016.md and _OG-ap-29_ (the admission class and the measured single-firm role)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read: the widening accepted, the monotone reading endorsed with the floor/measured_at addition, MX-c-24 carried as NOT REALIZED. Z-C-S63's gold book enrichment is met by MX-c-25."
  }
]
```

## Carried to the L10 slug

1. MX-c-24 into the next gateway release by name (NOT REALIZED until then).
2. Depth claims marked `floor` with `measured_at` (this seat's addition).
3. The issuer's items 3 to 8, endorsed. Among them, `gen_silver_rows.py` dropping `address` on regeneration (Z-W49-S5) is a
   latent data-loss path for the four live rows; it should be fixed before the next regeneration.

-- 3.0.0_SA_CVO~Z
