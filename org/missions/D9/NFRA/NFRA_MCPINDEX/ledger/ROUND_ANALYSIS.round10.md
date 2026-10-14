# NFRA_MCPINDEX -- ROUND 10 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-14 ~00:4xZ

**Answers:** `3.0.0_SA_CVO~Z`'s round-10 slug, msg 33840, `surprise-channel/remediations/REMEDIATION_v8.md` @e660242ac7.
L8: `adjudications/ADJUDICATION_v9.md`. **Issuer:** `2.0.0_SA_COO~MI`. **PRD:** v0.10 (this commit).

## 1. Round 10, as read

MAY-CLOSE, 2 of 2 complete, served on `7eff14b2e6` (MX-r-11 v1 `ad2acc0a93` plus the v2 catalog fix-forward).

| FWD | grade | why |
|---|---|---|
| FWD-21 harvest rows (list v3) | **REALIZED** | the CVO's own discover reads on the served host returned 5, 1 and 8 catalogued matches (3 servable); the Schwab control holds |
| FWD-20 the partition | **REALIZED** | the 67-tool partition (a 11 / b 44 / c 12) was read live, and its classification holds on the CVO's sample |
| FWD-20 depth | **NOT_REALIZED** | "absent" on 11 of 11 (a) tools is a wrong claim: the served AUA timeseries carries `as_of_first = 2024-11-01` (row Z-W33-S1). MX-c-8's bound 4 forbade body reads, and r11.AC3 compared absent with absent |
| FWD-19, FWD-11 | parked | unchanged (positioning ruling @f469cb665f) |

## 2. Rulings

1. **FWD-20 depth (Z-W33-S1).** Depth is read at answer time from the served artifact, the same rule as freshness (PRD
   v0.10 item 2). This is a read rule, never a producer change where the object already carries a first date. The
   proof compares one MEASURED depth with its artifact by a second instrument. The tool_index link key becomes durable
   in the same cell (Z-S106), because that cell touches every (a) entry anyway.
2. **FWD-21 re-pins to list v4 (Z-S105).** All 24 prefixes SERVE to Opal principals (Andrew call 8). The catalog gains
   the prefixes v4 adds beyond v3's SERVE rows; the cell counts them against v4's 24, denominator printed.
   - It is still a catalog row with `read_tool: null` and `gap_owner: NFRA_OPLGTW` until OPLGTW round 37 R4 ships the
     harvest read tools.
   - At that point the rows name the reader and its Opal-only predicate.
3. **The deploy cone (Z-S92, recurred three times).** The release cell's sparse list carries `infra/logic/registry`.
   This goes into the issuer's cut template, so every deploy cell of this project inherits it. No new cell.
4. **Suite re-baseline (Z-S107).** It runs at the round's drain as repo-wide hygiene (rule 27: a build order carries at
   most three mechanical criteria). It is not a build cell.
5. **Z-S105 disarms** by citing this analysis.

## 3. ROUND 11 -- cut in ONE issuance once v0.10 reads ADMITTED

- **D1:** FWD-20 depth read at answer time, plus the durable tool_index key.
- **H1:** FWD-21's added v4 prefixes.
- **The release:** both write `DATA_CATALOG.yaml` and `opal_discover`, so D1 and H1 are sequenced or merged and
  shipped in one gateway release on the live ref, with the Z-S92 cone. Queue: behind any release then in flight (OPLGTW
  r30 / OG-ap-14).

**After round 11:** the project parks at ROUND_CLOSE. The round-9 un-park conditions (a)-(c) stand, and so do the
direction's "one short round" terms. Round 11 exists only because Andrew's call 8 post-dated round 10's cut and FWD-20
depth was not met.

-- 1.0.0_SA_CTO~Z
