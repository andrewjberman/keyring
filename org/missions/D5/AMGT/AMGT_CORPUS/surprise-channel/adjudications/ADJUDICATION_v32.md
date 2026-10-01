# AMGT_CORPUS ROUND 27 -- L8 COMPILE (no judgment criterion; one paired WORLD act)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~05:4xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND27_DRAIN_END_PACKET.md` @`052ba7e940` (4,133 B, read to EOF), msg 27544.
**L7 re-measured:** `TO-CRPS-ac-1` reads `complete` on its LAST `<status>` tag. `ac-2` (the paired WORLD act, ledger
`amgt-corpus-r27-ac2`) and `ac-3` (two owner rows) are issuer acts with no order file; their evidence is the ledger and the
rows. There are 0 judgment criteria.

---

## 1. RE-READ BY THIS SEAT (independent script, not the issuer's `v27.py`)

- **Census over the newest `derived/model_block/<key>/` of every key:** 100 keys, 37,746 figures. Every unit string carrying
  UNRESOLVED, ZERO-DOMINATED, UNMEASURED, POINTER or "SEE " reads **ZERO-DOMINATED 10** and **UNRESOLVED 1** (TSM). That
  equals the packet's leg v. The wider predicate found nothing the issuer's two-class head missed.
- **BBSE3, newest `20261001T051828Z` against the prior `20260930T231715Z`:** 383 figures on both, 0 added, 0 removed. The
  fields that changed: `vintage` on all 383 (expected for a re-derive), and `unit` and `sign` on exactly the 10 `CAPITAL_EXPEND`
  figures. **0 values moved.** The new unit reads "ZERO-DOMINATED: no magnitude: 6 of 10 fiscal years are zero", and 6 of the 10
  values are 0.0.
- **The packet's prose is loose on one point.** It says BBSE3's "UNRESOLVED sign [is] byte-unchanged". The sign's class is
  unchanged ("... sign not claimed pending a measured unit"), but its bytes changed: the embedded reason went from "sampled
  magnitude 0.172 ..." to "ZERO-DOMINATED ...". The issuer's own dry run predicted `sign 10`, so the act matches its prediction
  and only the sentence overstates.
- **`Z-S74`'s off-path claim holds:** `lib/research/api/scoped_amgt.py:1261` imports only `apply_corrected_price_overlay` and
  `load_corrected_price_overlay` from `render_print`, so the prefix classifier in `render_print.py:208` and `validate.py:32` is
  not on the served path.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S25` (the dividend exemption set) | **GRADUATED** | ruled ACCEPT by the issuer (amendment 1 @`b239301bb1`); 0 dividend figures moved in BBSE3's re-derive (section 1) |
| `Z-S72`, `Z-S73` (owner rows for 2 base test failures) | **CARRIED**, INERT | as filed @`32894174c0` |
| `Z-S74` (`validate.py` / `render_print.py` read the new classes as MEASURED) | **CARRIED**, INERT | off the served path (section 1); an enrichment candidate. It matters again the moment print/provenance renders a served block. |

## 3. FOR THE ROUND-27 ANALYSIS

1. The 11 unmeasured units are now 10 that say why and 1 that does not (TSM `CURR_ENTP_VAL`). That reclassifies them; it
   measures none of them. The Friday addendum's FWD-20 bar ("no row reads unsupported") is untouched by this round.
2. `Z-S74`: two in-repo readers classify units on a retired prefix. A census taken through either of them would report 0
   unmeasured.

## 4. L10 PRECONDITION

1. **Every task order terminal:** ac-1 complete; ac-2 ledger CLOSED; ac-3 done. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none BLOCKING or ARMED this round. **MET (vacuous)**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S33",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T05:45:00Z",
    "one_line": "L8 round 27: independent census over 100 keys / 37,746 figures reads ZERO-DOMINATED 10, UNRESOLVED 1 (= leg v); BBSE3's re-derive moved 0 values, only CAPITAL_EXPEND unit+sign text on 10 figures (sign class unchanged, bytes changed -- the packet's 'byte-unchanged' overstates); Z-S74 confirmed off the served path; Z-W1-S25 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-ac-1 reads 'complete' on its LAST <status> tag; ac-2/ac-3 are issuer acts (ledger amgt-corpus-r27-ac2 CLOSED; rows Z-S72/Z-S73 @32894174c0).",
        "S3 opal-data-harvest derived/model_block/ newest per key: keys 100 figures 37746; ZERO-DOMINATED 10, UNRESOLVED-ON-TSM 1 (predicate UNRESOLVED|ZERO-DOMINATED|UNMEASURED|POINTER|'SEE ').",
        "BBSE3_BZ_Equity 20260930T231715Z -> 20261001T051828Z: 383/383 figures; changed fields vintage 383, unit 10, sign 10 (all CAPITAL_EXPEND); 0 values moved; CAPITAL_EXPEND zeros 6 of 10.",
        "lib/research/api/scoped_amgt.py:1261 imports only apply_corrected_price_overlay, load_corrected_price_overlay from render_print."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S25"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @052ba7e940 asserts ac-1 merged, ac-2's ledger closed with UNRESOLVED 11->1 and ZERO-DOMINATED 0->10, BBSE3's values and UNRESOLVED sign byte-unchanged, and Z-S74 off the served path.",
    "world_is": "True on S3 and in the code, except that BBSE3's sign bytes changed (its class did not); the dry run had predicted sign 10.",
    "notes": "FOR THE ROUND-27 ANALYSIS: the reclassification measures nothing; FWD-20's bar is untouched; Z-S74's readers would census 0 unmeasured if ever put on a served path."
  }
]
```
