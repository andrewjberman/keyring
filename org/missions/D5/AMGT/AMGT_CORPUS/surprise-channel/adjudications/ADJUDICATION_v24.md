# AMGT_CORPUS ROUND 21 -- L8 COMPILE (no judgment criterion)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~04:4xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND21_DRAIN_END_PACKET.md` @`8`, msg 26909. The packet was read to EOF (5,843 B).
**L7 re-measured, not adopted:** `w-1`, `w-3` read `complete` on their LAST `<status>` tag. `w-2` is held on AMGT_RESAPP r51 `zz-1`,
and nothing is registered. 0 judgment criteria.

---

## 1. RE-RUNS BY THIS SEAT

- **w-1 AC1:** "w1 pack_shape folders 96 pdf 48 docx 25 mixed 4 none 19 errors 0 sum_ok True control IMB_LN_Equity docx
  ADBE_US_Equity pdf AZN_LN_Equity pdf 6501_JP_Equity none". This reproduces.
- **w-3 AC1:** "w3 facts 9 of 9 answered resolved 8 unresolved 1 resolved_with_evidence 8 unresolved_with_reason 1 control
  SAP_GY_CURR_ENTP_VAL MILLIONS agrees True". This reproduces.
- **Neither run wrote a tracked file.** The one new status entry during the runs is the issuer's untracked
  `evidence/r21_w1_expected_moves.txt`, stamped 04:29:47Z, the output of the expected-moves measurement the packet says started
  at 04:29:46Z.

## 2. WHAT THE RE-RUNS SAY FOR THE ANALYSIS

1. **FWD-16's round-20 "PDF-only 25/25" was a floor, and it was low.** v23 agreed it was a floor because citations ending in `.pdf`
   are a proxy. The measured `pack_shape` is **pdf 48, mixed 4, docx 25, none 19**. The served proxy found 25; the dossier's own
   A/B picks find 48 PDF-only packs. The grade should be re-read on `pack_shape` once it is served.
2. **The unit discriminator's resolved cases are plausible on their face.** Revenue near 0.4x market cap, and enterprise value near
   1x (0.88-1.36), are the magnitudes a large-cap fundamental has. The ABSOLUTE hypothesis sits near 1e-6, far outside any band.
   **TSM is left UNRESOLVED by rule:** there is no same-currency anchor (TWD fundamentals against a USD market cap), and no FX rate
   is invented. That is the never-guess behaviour the cell was cut for. The worker's mutant ("first hit, else MILLIONS") failed 2
   tests, which is the control that the rule does not default.
3. **The issuer caught a gap in its own cut:** `dossier.write_one` writes nothing without a `METHOD_VERSION` bump, so `pack_shape`
   is not served by a plain `--write`. That is named, and the pair is being prepared. The 8 resolved units likewise need an apply
   writer before the five model blocks re-derive under a pair. **Both served acts are ahead, not done.**

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W2-S16` (TSM has no same-currency anchor; `REVENUE_PER_SH` unmeasured on 6501/8316, so their SALES resolves on the market-cap read alone) | **CARRIED** -> the analysis | (a) is the rule working. (b) means two of the eight resolved facts rest on one read, not two, which should be stated beside their MILLIONS. |
| `Z-W2-S15` | **CARRIED** -> AMGT_RESAPP | routed |
| `Z-S63`, `Z-S66` (ARMED) | **CARRIED** | w-2 waits on AMGT_RESAPP r51 `zz-1` |
| `Z-S64` | **CARRIED** | the migration item |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2 cut. w-2 was held on a named external block. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** CARRIED with owners. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S24",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T04:45:00Z",
    "one_line": "L8 round 21: w-1 and w-3 AC1 re-run and reproduce (pack_shape pdf 48 / docx 25 / mixed 4 / none 19; 8 of 9 units resolved, TSM UNRESOLVED by rule); FWD-16's round-20 proxy floor of 25 PDF-only is low against the measured 48; both served acts (pack_shape rewrite, unit apply + re-derive) are ahead, not done.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-w-1 and w-3 read 'complete' on their LAST <status> tag.",
        "w-1 AC1 re-run: 'w1 pack_shape folders 96 pdf 48 docx 25 mixed 4 none 19 errors 0 sum_ok True ...'.",
        "w-3 AC1 re-run: 'w3 facts 9 of 9 answered resolved 8 unresolved 1 resolved_with_evidence 8 unresolved_with_reason 1 control SAP_GY_CURR_ENTP_VAL MILLIONS agrees True'.",
        "git status during the re-runs: the only new entry is untracked evidence/r21_w1_expected_moves.txt, mtime 04:29:47Z (the issuer's measurement)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The drain-end packet asserts w-1 and w-3 VALID and merged, 8 of 9 units resolved MILLIONS with TSM UNRESOLVED, pack_shape serving needing a METHOD_VERSION bump plus a paired rewrite, and w-2 blocked.",
    "world_is": "True as read on this seat's re-runs. The measured pack_shape shows the served FWD-16 proxy undercounted PDF-only packs (25 vs 48).",
    "notes": "FOR THE ROUND-21 ANALYSIS: re-grade FWD-16 on served pack_shape; state that 6501's and 8316's SALES_REV_TURN MILLIONS rest on one cross-field read (Z-W2-S16 b); an apply writer is owed before the five model blocks re-derive."
  }
]
```
