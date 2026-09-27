# Never-widen sign-off packet -- one generate + resident release: catalogue v2 with its consumer, and the Static-only tolerance

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~22:2xZ.
**Asked by:**
- CTO 101971 item 2 (the Static narrowing as the next resident version);
- ~Y 102007 and 102113 (catalogue v2 in generate AND resident together);
- ~M 102156 (the v2 consumer, in the same release).

**Ledger (opened before any write):** `irpt-generate-resident-catv2-static-20260927`: U1 and U2 are closed; D1 and D2
are open.

## 1. What ships (all committed in the backend; the cherry-picks' bytes are equal)

| change | commit | files |
|---|---|---|
| level_as_of_type tolerance for STATIC portfolios only (~Y P_STATIC_TOLERANCE, 737aea0b..) | 12a67ed5ee | extract.py, recipe.py (a comment), resident_worker.py, + tests |
| comparison catalogue v2, identity-verified by window 18's reads (~Y P_COMPARISON_CATALOGUE_V2, d6b2efdb..) | 4b563c98a0 | templates.json |
| the v2 policy consumer (~M 5dede2f029) | 65957b8afc | _scope/maintained_sources.py, + test |

**Held OUT**, because safe-commit's LGIC naming gate refused them for typed firm ids (routed back to ~Y, 102162):
~Y's CATALOGUE_GRANT (templates.json:116, 147, 178..) and FOREIGN_FIRM_NAME_CHECK (publication.py:81). Without the
GRANT, ~M's consumer matches no pinned hash on this catalogue. **Comparisons therefore stay REFUSED**, and this release
enables no comparison.

**Tests**, run suite by suite:
- test_calculation_settings 5; test_resident_worker 37 / 8 skipped;
- extract 23; generate 287 / 30 skipped; _scope 205.
- ~Y's live arms A-E for the Static narrowing are in LIVE_WINDOW15_EVIDENCE_20260927.md, and ~Y 102113 records
  12a67ed5ee as content-identical to the proved overlay.

## 2. The two moves

**D1 -- irpt-ycharts-generate** `G/TqLPdL..` -> `ykJltfTd..` (S3 version Iu3nADja.)
- Census: 111 -> 111 members. ONLY `templates.json` and `maintained_sources.py` differ.
- Dry plan (ycharts root): 0/1/0, code only. Rollback: re-apply at S3 version 84.Msfap. (G/TqLPdL).
- Generate's recipe, extract and resident_worker members are NOT moved: the Static narrowing is resident-side.

**D2 -- the resident** `/opt/irpt-resident/fe64236bbb-lt` -> `fe64236bbb-st`, on i-0167fd745ad906a66.
- Package SHA256SUMS vs lt: 225/225; ONLY maintained_sources.py, extract.py, recipe.py, resident_worker.py,
  templates.json and the bindings differ. Tar 75e672b1.. (S3 version 7Ry2IczL.).
- `resident_host_install_st_20260927.sh`, lt's script with its names, tar and member shas changed:
  - it checks the tar and eight member shas, and SHA256SUMS;
  - it runs the factory, and stops only on an EMPTY queue (0/0);
  - then install, a check for polls and no tracebacks, and an automatic roll back to lt on any failure. The lt root is
    kept.

## 3. Blast radius -- both branches of each producer rule

- **Read-back tolerance (resident):**
  - a STATIC model portfolio whose stored level_as_of_type differs is tolerated, as today (READY);
  - a DYNAMIC or absent one now goes ATTENTION TOLERANCE_REQUIRES_STATIC with 0 S3 puts, where today it is tolerated.
  - Reachable only by an Analysis submission (the walk windows today).
- **Comparison selection (generate + resident):** before, v1 catalogue, refused; after, v2 catalogue with no GRANT,
  still refused. Writers of the refusal: one rule (`maintained_sources.resolve_comparison_fields`), read at this commit.
- **Overview / everything else:** unchanged. ~Y 102113 reports the served generate with v2 ACCEPTS window 15's input.

## 4. Order and timing

D1 and D2 go in one turn, generate first, and only on a 0/0 queue. They stay clear of window 19 (they need a quiet
Analysis plane; window 19 is export-only) and of MSTR's 03:00Z freeze. The live proof of the Static branch is the next
Analysis window's K5; there is no vendor call in this act.

## What the halves sign against

This file's committed blob; the three commits and the two artifacts with their censuses, plans and rollbacks; the
held-out patches named; the blast radius in section 3.
