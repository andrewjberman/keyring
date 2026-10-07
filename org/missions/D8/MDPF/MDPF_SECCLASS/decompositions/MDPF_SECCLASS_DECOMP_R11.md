# MDPF_SECCLASS decomposition -- ROUND 11 (2.0.0_SA_COO~M1, dell1, 2026-10-07 ~14:4xZ)

**Status: DECOMPOSED.** The issuer is this seat. Order: 1.0.0_SA_CTO~DELL1 msg 328: "cut round 11 in ONE issuance from section 3."

**Cut on:**
- PRD v0.15 @54e82922e4, ADMITTED. It adds contract note C-CASH-TOKEN, Andrew-direct via 2.0.0_SA_COO~M2 ~14:1xZ, verbatim: "most of
  those items literally have "Cash" as a token within, which would be the "Cash" asset class. The others could likely be
  websearched."
- The round-10 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_10_20261007.md` @a856d1525f:
  section 3 items 1-7, read with rulings 2.1-2.4.
- `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R10_20261007.md` @d9ce041409.

**State the round starts from (measured this session):**
1. Portal candidate `cand-dell1-secclass-e59-r10` @c0ec00e6 passed the laptop CTO review (106294, additive). Its DEV landing is on
   Andrew's word through 0.0.0_AB_MSTR. Candidate e53-r9 passed on one condition (106245: 0 `multi_asset` in every firm's served
   composition files). This seat's read-only census runs for it (`R12_CHECKS/served_multi_asset_census.py`).
2. Held lines on origin, DO NOT MERGE:
   - held-38 r2 @53af7b1bd3: e55, e56, e57, e61, e62;
   - held-34 r2 @cbbda93539: e44, e63;
   - held-d04 @24a219520b: e60.
   held-32 (e42) may merge to CLOUD, because its push gate reads MATCH.
3. TO-DEPLOY-e42 is live on 49F (ETag 4092c5b8, 13:44:30Z). Its L2 post-run read is this seat's at 2026-10-08T12:45Z. The
   TO-DEPLOY-e21 flip is ~S's (CTO msg 301).
4. Row W41-S4: silver `bd_assets_dim.parquet` has no canonical columns, because the scheduled `--union-bronze` path,
   `build_union_dim()` in `data/black_diamond/scripts/silver/build_bd_assets_dim.py` (~:340-372), freezes the column set
   (`assert len(out.columns) == len(dim.columns)`) and blends only added rows.
5. The direct plan for a first-held security is `plan_rows` / `classify_asset_class` in
   `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`, a shipped `_shared` member, which held-34 r2 already edits.

## Rule 24 record

- **Domain:** section 3 items 1-7, every step of each. The denominator is 7 items with 19 steps. Each step is placed once, as one of:
  - a cell: 2 cells, SC-e-65 and SC-e-66;
  - an issuer act: the portal landings and their condition, every held-line merge behind its pair, the e42 L2 read and close, the
    e21 flip (~S), the E_18 deploy, the producer-live count, the sector apply and write, the CASH row write, the web-search research;
  - a deferred cell: SC-e-45 and SC-e-46 are cut when their issuer acts land.
- **(ii) Same grain:** one write set per cell. **(iii) Intent coherence:** one intent per cell.
- **(iv) State coherence:**
  - A table rule (SC-e-65) writes no row until its deploy runs.
  - A builder fix (SC-e-66) changes no served file until the next scheduled run, under its pair.

## The cells

| cell | item | what | serves | base | risk | depends on |
|---|---|---|---|---|---|---|
| `SC-e-65` | 6 | C-CASH-TOKEN: in the scheduled producer's direct plan, a held security whose ticker or name carries CASH as a whole token is planned cash/Cash. BDCASHIN and FCASH go in; CASHMERE stays out. The row names the rule. | FWD-7, FWD-13, FWD-17 | held-34 r2 (cbbda93539) | WORLD (infra floor) | -- |
| `SC-e-66` | 7 | W41-S4: the union path writes `asset_class_canonical`, `sub_asset_class_canonical` and `class_source` for every row, from the canonical table through the one client. It drops the frozen column-set assert, adds the three columns and keeps every other column's values byte-for-byte. Half request for the served file. | FWD-1, FWD-2 | round HEAD (cecc5f9013) | SERVED (shipped BD silver: held) | -- |

## Write sets

- **SC-e-65:**
  - `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`
  - `infra/aws/lambda/v2_portal/_shared/tests/test_cash_token.py`
- **SC-e-66:**
  - `data/black_diamond/scripts/silver/build_bd_assets_dim.py`
  - `data/black_diamond/scripts/silver/tests/test_assets_dim_union_canonical.py`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SILVER_UNION_CANONICAL_20261007.md`
- Both may append rows to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Dependency edges

None. **Chains:** 2 single-cell chains, so M = 2. Fan-out 2 of 2, cap 8. SC-e-65 drains to the held-34 r3 line; SC-e-66 drains to a new
held line, `secclass-r11-held-silver`.

## Issuer acts (not cells), in section 3 order

1. SC-e-59 to DEV on Andrew's word (0.0.0_AB_MSTR's push). Then e53 is rebased on it and tsc re-run, and lands with the census read
   as its condition. Then the CVO grades SC10-e59-AC2 and FWD-1 on the live page.
2. Each held line merges behind its signed pair, every pair asked of this seat with live reads: e44 + e63 + e65 (one pair, naming
   W44-S2's widened input), e55, e57 + e61, e56 + e62 (through IRPT_BCKEND), e48, e49, e32/e50 (S55's re-plan first), e60, e66.
3. The TO-DEPLOY-e42 L2 read at 2026-10-08T12:45Z and its close (~S flips). The TO-DEPLOY-e21 flip (~S).
4. FWD-5: the E_18 deploy, then the producer's live canonical count; then SC-e-45.
5. FWD-12: the sector writer's apply on a laptop cloud-operations seat, then the sector write; then SC-e-46.
6. The live CASH row write under its pair. The remaining Cottonwood tickers (CQP and others) are researched by web search, research
   only and no downloads, and land through seed or AI with their source.
7. C-S13's D_04 line is built (e60, held) and releases behind its pair.

## Not read at this cut

The real names of the Cottonwood cash-token tickers: the worker reads them from the 10-05 Cottonwood build. Whether any other silver
reader needs the new columns.
