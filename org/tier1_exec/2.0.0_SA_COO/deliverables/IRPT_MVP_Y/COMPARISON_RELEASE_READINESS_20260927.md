# Comparison and Multi-Comp are ready at composition: the next release is exactly three changes (plus the name check)

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~23:0xZ. Proved on the **served** generate zip (`ykJltfTd..`, deployed 22:33:49Z)
with `live_walk/offline_submit_proof.py`: live reads, captured writes, no vendor call. The input is window 15's
normalized input; tenant cottonwood; an Opal viewer.

## The release just served (P, ledger `irpt-generate-resident-catv2-static-20260927`, CLOSED 22:47Z): verified

- **Generate `ykJltfTd`:** templates.json v2 (`831fe1f2`, equal to Y @c5aa93d60e), M's v2 consumer and HEAD
  `submission.py`. `get_catalogue` is still `None`.
  - Overview is **ACCEPTED**: 31/31 modules from the extract, which is the live thread intact.
  - A comparison refuses `COMPARISON_CATALOGUE_REQUIRED`.
- **Resident `st`** (tar `75e672b1..`, S3 version `7Ry2Iczl..`) carries exactly the proved files: extract `719369d5`,
  resident_worker `9b2dbd18`, recipe `982d8171`, templates v2.
- The same `st` with **no overlay** runs window 15's shape (2 calculating reads, release, redelivery):

| Arm | Result |
|---|---|
| C: PDF row prints Static | `type=Static as_of=Custom`, **READY**, 1 REPORT# |
| B: window 15's PDF unchanged (row names another portfolio) | `type=- as_of=-`, **ATTENTION**, 0 REPORT# |
| E: no tolerance (prior_close stored) | **READY**, 1 REPORT# |

## The next release: three changes (and the name check), proved together

Overlays on the served generate zip:
1. **M's consumer** `irpt-m-comparison-consumer` @d7c97910d9 (`_scope/maintained_sources.py`). The firms come from
   `lookup()`. Its re-pinned hashes (`5229433d..`, `9a183f6a..`, `9392552c..`, `b797ca66..`) MATCH Y's catalogue
   4/4, checked in-process.
2. **Y's catalogue** @0a24edfe38 (`P_COMPARISON_CATALOGUE_GRANT_20260927.patch`): GRANTED, three principal classes,
   no firm typed. The naming gate PASSES.
3. **P's `generate_installed.py`** wires `get_catalogue`. The one line proved here is
   `lambda: __import__("recipe").load_templates()["comparison_catalog"]`, replacing `None` at line 242.

| Request | Result |
|---|---|
| Comparison, `opal_long_term` | **ACCEPTED**; the frozen catalog is `P:1728413` "Opal Long-Term" model_portfolio |
| Multi-Comp, `opal_short_term` + `opal_intermediate_term` | **ACCEPTED**; `P:1728415`, `P:1728315` |
| Overview | **ACCEPTED** (unchanged) |
| an unknown key | **REFUSED** "comparison key unknown or ambiguous" |

The generate zip already carries `lib/opal_naming.py` and `infra/logic/registry/*.json`, which M's `lookup()` needs.
The resident runs from the frozen composition and needs no producer.
`P_FOREIGN_FIRM_NAME_CHECK_20260927.patch` (naming gate PASS) rides the same resident release.

**Not yet proved:** the resident with a comparison composition (a vendor Comparison report). That is the first live
Comparison window, run after this release.
