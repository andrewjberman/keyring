# MDPF_SECCLASS decomposition -- ROUND 14 (2.0.0_SA_COO~M1, dell1, 2026-10-08 ~18:4xZ)

**Status: DECOMPOSED (one cell).** The issuer is this seat. Order: 1.0.0_SA_CTO~DELL1 msg 1050 (DECISION, SELF-DRIVE tick 18): "D1-S9
enters round 13 as cell 2, after e74".

Round 13 already holds one issuance (TO-SC-e74 @ed7c69af58). `to-pipeline-gate` keys ONE ISSUER PER ROUND to the round, so a second
issuance cannot be tagged 13. This cell is therefore cut as round 14. That keeps the CTO's order: it comes after e74. The CTO is told
of the numbering.

**Cut on:**
- Row `MDPF_SECCLASS-D1-S9` @90d90b9dc8.
- Scope from msg 1050: find the BD gold writer that still emits multi_asset, and route it through the six-class mapping. Then close
  leg G of `secclass-multi-asset-remap-b-m-20261007` on a served read of those 36 files, under a never-widen pair. The CTO signs on
  receipt.

**State the cell starts from (measured this session):**
1. `R12_CHECKS/served_multi_asset_split.py`, 2026-10-08 ~18:1xZ:
   - opal-data-bd: 36 of 25,265 keys hit, all post-switch.
   - opal-data-cot: 2 of 1,153 keys hit (row S60; COT's cell SC-e-67 is in round 12).
   - On 10-07 ~16:5xZ, BD read 0 post-switch hits.
2. BD multi_asset items by ticker: ABALX 12, AMECX 9, CAIBX 9, SCGB1 5, and 88 with no ticker. data_as_of is 2026-10-06 for 35 keys.
3. etf-classifications holds 0 multi_asset rows (ledger leg S). `comp-find 'multi_asset'` over `data/black_diamond`, `data/cot` and
   `_shared` reads 0 definition hits.
4. Ledger leg H closed @90d90b9dc8: the IRPT holdings of all three firms serve 0 multi_asset.

## Rule 24 record

- **Domain:** msg 1050's scope, 2 clauses: the trace and fix, and the leg-G close on a served read. Each is placed once.
  - The cell `SC-e-75` covers the trace, the fix, the pin and the half request.
  - The issuer's acts are the deploy under the pair and the leg-G served read.
- **(ii) Same grain:** one writer, one served set. **(iii) Intent coherence:** one intent, no served multi_asset in BD.
- **(iv) State coherence:** the cell changes repo code only. Served files move at the next scheduled BD gold fire after the issuer's
  deploy. The canonical table, the IRPT holdings and COT's files are not moved by this cell.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-75` | Row D1-S9: trace the BD gold writer that still emits multi_asset on 36 `opal-data-bd platinum/clients/*/concentration.json` (10-08 00:50-05:51Z). It is not a source literal: check the deployed bytes against the repo, and the class inputs. Route it through the six-class mapping, pin by test, and write the half request for the served keys | FWD-16 | WORLD (shipped BD gold; the deploy and the leg-G served read are the issuer's, under the pair) | -- |

## Write sets

- **SC-e-75:**
  - `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`
  - `data/black_diamond/scripts/gold/tests/test_d04_bd_no_multi_asset.py`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_MULTI_ASSET_TRACE_20261008.md`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_MULTI_ASSET_20261008.md`
  - rows appended to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.
  If the source is another file or an input object, the cell stops, files a row, and the issuer re-points.

## Dependency edges

None. **Chains:** 1, so M = 1. Fan-out 1 of 1, cap 8.
Issuer acts after the cell:
1. The half goes to the CTO.
2. Deploy to `s3://opal-data-bd/code/gold/` under a change-management ledger.
3. After the next scheduled BD gold fire, `R12_CHECKS/served_multi_asset_split.py` reads opal-data-bd post_switch=0. That closes
   leg G of `secclass-multi-asset-remap-b-m-20261007` (with COT's 2 files closed by SC-e-67).
