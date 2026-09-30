# AMGT_CORPUS ROUND 17 -- L8 COMPILE + L9 ON THE ONE JUDGMENT ITEM

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~01:0xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND17_DRAIN_END_PACKET.md` @`1d85152810`, msg 26815. The packet was read to EOF (5,309 B).
**L7 re-measured, not adopted:** `s-1` reads `complete` on its LAST `<status>` tag. `s-2` is BLOCKED on AMGT_RESAPP (`Z-S66`),
and nothing is registered.

---

## 1. THE SERVED ACT (Hitachi's model block), RE-READ

- **S3, read by this seat:** `opal-data-harvest` `derived/model_block/6501_JP_Equity/20260929T232834Z/model_block.json` exists,
  LastModified 2026-09-29T23:28:38Z, with `fiscal_year_row_count` / `fiscal_years` 11.
  - This equals the D leg.
  - Control: `derived/model_block/8035_JP_Equity/` lists 5 objects.
- **`field_map.json` at `ead621d685`, diffed by this seat element by element against its first parent:**
  - `securities`: 98 -> 99, adding only `"6501 JP Equity"`.
  - `fields`: 66 mnemonics before and after.
    - 176 key additions, all under a `6501` path.
    - 37 `measured_on` lists each gain exactly `"6501 JP Equity"` and lose nothing.
    - **0 other changes, 0 removals, 0 type changes.** 1 + 176 + 37 = 214 additions, equal to the packet's figure.
  - A first pass by this seat reported "37 changed" because it compared whole lists. Read element by element, every one is a
    Hitachi append. **CTO ruling (b), "Hitachi's per-security entries only", holds on the bytes.**
- **The census check `s1_AC1.sh`** reads the worker's committed pre-act census JSON, not the live store, so it still prints
  "present 95 absent 1 ... hitachi absent". That is right for its input. The live V-leg read (96 of 96) is what the S3 object
  above corroborates.

## 2. L9 -- THE RESIDUE ATTRIBUTION

**The claim:** the 05:42:34Z residue (`field_map.json` +NVDA, `0.9.0_WK_AMGT_CORPUS~1/ingest_run.json`) is "most likely this
seat's prior-session drain test run". It rests on mtime, timing and content, with no process trace.

**Verdict: AGREED, and strengthened on one point the packet did not test.**

| basis | this seat's read |
|---|---|
| **Timing** | 2.0.0_SA_COO~X's round-10 drains landed at 05:41:54Z (`58d076cc23`, wk-crps10-2) and 05:46:05Z (`5b0b728ab1`, wk-crps10-1). The 05:42:34Z residue falls between them. |
| **Content, NVDA** | The live research library holds **0 of 96** folders naming NVDA or Nvidia. So a field_map row for "NVDA US Equity" did not come from a library run. |
| **Content, the untested point** | The residue's `ingest_run.json` reads `scan_vintage 2026-09-25T23:58:50Z`, `resolved_folders 95` and **`put_performed 2`**. Two puts would be a served write if they were real. **This seat scanned `opal-data-harvest` `amgt/harvest/` (2,958 objects): 0 were written between 05:40 and 05:46Z on 2026-09-29.** The two puts never reached S3, which fits `substrate.py`'s stub client (`:386`, a stub `put_object` that counts). A stubbed test run is exactly what the attribution claims. |

The backup `.runtime/crash-investigation-20260929/uncommitted-backups/field_map_and_ingest_run_0542Z.patch` (190,803 B) holds
both diffs. The shared tree was restored on Andrew's approval.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S63` (ARMED: a scheduled fire forks the registration ledger) | **CARRIED** | Half closed by AMGT_RESAPP `yy-6`. `Z-S66` names the remaining `add_security` path. |
| `Z-S66` (ARMED: `add_security` builds `crosswalk/v1` without `served=`) | **CARRIED** -> AMGT_RESAPP | the `write_pool` union cell, then r-1 re-signs with the fork test run through `add_security` |
| `Z-S65` (ARMED: `build_unit_map` downgrades shared fields on one ambiguous name) | **CARRIED** -> the analysis | Withheld this round under stop limb 3. The producer's merge still does it, so the next name with an ambiguous unit meets it again. |
| `Z-S64` (INERT: the model-block writer bypasses `slash_safe_key`) | **CARRIED** | The worker's S3 list shows `BP/` stored under a literal `/` (not re-read by this seat). A key form for the analysis. |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | as in v16-v19 |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 1 of 1 cut. `s-2` was held at the issuer on a named external block, not cut. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S63`, `Z-S65` and `Z-S66` CARRIED with owners and conditions; the older ARMED
   set CARRIED. **MET**
3. **Every judgment item graded:** 1 of 1 AGREED. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S20",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T01:05:00Z",
    "one_line": "L8/L9 round 17: Hitachi's model block is on S3 (derived/model_block/6501_JP_Equity/20260929T232834Z, 11 FY rows); field_map at ead621d685 adds only Hitachi (1 + 176 + 37 = 214, 0 changed or removed); the 05:42Z residue attribution is agreed -- its ingest_run's 'put_performed 2' never reached S3 (0 of 2,958 objects written 05:40-05:46Z), consistent with a stubbed test run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-s-1 reads 'complete' on its LAST <status> tag.",
        "S3 opal-data-harvest derived/model_block/6501_JP_Equity/: 1 object, 20260929T232834Z/model_block.json, LastModified 2026-09-29T23:28:38Z, fiscal_years 11; control derived/model_block/8035_JP_Equity/ 5 objects.",
        "field_map.json ead621d685^1 -> ead621d685: securities 98 -> 99 (+'6501 JP Equity'); fields 66 -> 66 mnemonics; 176 key adds all under 6501; 37 measured_on lists each + '6501 JP Equity', 0 removed; 0 other changes.",
        "git log 2026-09-29T05:30-06:00Z: 58d076cc23 05:41:54Z and 5b0b728ab1 05:46:05Z (2.0.0_SA_COO~X round-10 drains).",
        "Residue patch: ingest_run.json scan_vintage 2026-09-25T23:58:50Z, resolved_folders 95, put_performed 2; field_map +'NVDA US Equity'. Live library: 96 folders, 0 NVDA/Nvidia.",
        "S3 opal-data-harvest amgt/harvest/ scan: 2958 objects, 0 with LastModified in 2026-09-29T05:40-05:46Z."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The drain-end packet @1d85152810 asserts s-1 VALID and merged, Hitachi's model block landed with the field_map change Hitachi-only, s-2 blocked on AMGT_RESAPP, and offers the residue attribution for L9.",
    "world_is": "True as read on S3 and on the field_map bytes. The residue attribution holds, and the one fact that could have made it a served write -- two recorded puts -- is shown not to have reached the store.",
    "notes": "FOR THE ROUND-17 ANALYSIS: Z-S65 (build_unit_map downgrades shared fields on one ambiguous name) will recur on the next such name; the model-block admission of newly registered names (admits_new_registrations False); Z-S64's key form."
  }
]
```
