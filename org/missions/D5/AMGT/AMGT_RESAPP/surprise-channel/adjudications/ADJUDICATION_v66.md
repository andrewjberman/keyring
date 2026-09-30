# AMGT_RESAPP ROUND 54 -- L8 COMPILE (no judgment criterion; ad-2 AC2's post-failure re-scope read against its negatives)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~21:3xZ
**Input:** `2.0.0_SA_COO~Z`'s `round54/DRAIN_END_PACKET.md` @`27b2146252`, msg 27378. The packet was read to EOF (6,304 B). The CTO's
ask is msg 27358.
**L7 re-measured:** `ad-1`..`ad-4` read `complete` on their LAST `<status>` tag. There are 0 judgment criteria.

---

## 1. ad-2 AC2 -- RE-SCOPED AFTER IT FAILED (AMENDMENT 2): THIS SEAT's READ

**What the amendment drops.** `checks/ad_2_hold.py` `VOLATILE = (generated_at, as_of_date, read_at, served_at, request_id)`, dropped at
**every depth**. This seat walked the live `/thesis` bodies for VLO and BA; 4 keys match in each:

| path | value (VLO) | what it is |
|---|---|---|
| `/generated_at` | `2026-09-30T21:25Z` | read-time (`_now_iso()`), correctly dropped |
| `/model/generated_at` | `2026-09-30T21:25Z` | read-time (`scoped_amgt.py:3417`), **the failure's cause**, correctly dropped |
| `/as_of_date` | `2026-02-25` | **STORED data**, the filing date the thesis reads from. The pre-amendment check already excluded it at the top level. |
| `/posture/generation/generated_at` | `2026-09-18T14:10:36Z` | **STORED data**, when the posture was drafted. **Newly hidden by "every depth".** |

**So the rewrite is wider than its failure.** The failure needed only the read-time `model.generated_at`, and the rule also blinds two
stored data stamps.

**Did the widening hide anything in THIS act?** No, measured.
- This seat compared all 12 pre-act served bodies (`0.7.0_AE_CloudOps~A/ad2-pre/served/`) with the live bodies now, on exactly the two
  stored stamps: **0 of 12 moved**.
- The issuer's negatives (a planted nested non-volatile key under `model`, and VLO `px_last` +1.00) FAIL, so the check discriminates
  non-volatile keys.

**VERDICT: SOUND for this act, measured. The rule itself is too wide.**
- A read-time stamp should be dropped by PATH (`/generated_at`, `/model/generated_at`), not by NAME at every depth.
- A stored stamp is data, and a check comparing "every other key equal" must see it.

**An addition for the accepted positive-arm discipline** (the packet's section 3 lesson, and this seat's proposal @`09a6f6dd39`):
- A synthetic "after" built from the saved pre-act body cannot vary a read-time field. The simulation copies the stamp it should have
  shown moving.
- **Cheapest fix: make two live pre-act reads a few seconds apart and diff them.** Every field that differs is read-time by
  measurement, and the check's volatile list is exactly that set, by path.
- That would have caught `model.generated_at` at the cut, and would not have blinded `posture.generation.generated_at`.

## 2. THE REST, RE-READ

- **FWD-30 at close:** `fwd30_close_sweep_served_20260930T205921Z.tsv` reads 96 rows, all `OK`, `val_compared` 32,468, `val_differ`
  **0**. TSM is now equal: ad-4's grader reads "unit not resolved -- raw figure N" as N, equal only against an UNRESOLVED export. The
  97th library folder, `Brookfield Corporation BN CA`, is unidentified and not graded (1 of 97), which is a universe/CORPUS act.
- **ad-3:** `infra/aws/terraform/harvest/upload_verified.sh` exists, and each of the four `build-and-upload*.sh` references it (3 lines
  each).

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S319` (ARMED: an MSYS-mangled `content-sha256`, corrupted `source_code_hash` at rc=0) | **GRADUATED** (disarmed) | ad-3: one verified upload helper with no path conversion and a read-back that refuses a mismatch, sourced by all four build scripts (section 2). It is VALID and drained @`71f1cafcab`. The interim act-start limb (v63) can retire. |
| `Z-S322` (`deploy_ledger.py open` stages its files into the shared index, so peers' drains absorbed the entry) | **CARRIED** | "the owner is yours to name": a fabric tool with no seat named, the same pattern as census class A. The CTO names the owner. |
| `Z-S321` | **CARRIED**, INERT | superseded in effect by ad-3 |

## 4. FOR THE ROUND-54 ANALYSIS

1. **ad-2's volatile rule:** drop by path, and make volatile-ness measured by two pre-act reads (section 1).
2. **`Z-S322`:** name its owner. A tool that stages for its caller breaks the author line and the lane check.
3. **The next posture batch diff** (179 held sentences; the `S:<section>:<n>` ids renumber) is to be read when it runs.
4. **Brookfield BN CA onboarding** is for CORPUS/universe, not RESAPP.

## 5. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S319` GRADUATED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S436",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T21:30:00Z",
    "one_line": "L8 round 54: ad-2 AC2's post-failure re-scope is SOUND for this act (the 2 stored stamps it newly blinds moved on 0 of 12 names) but too wide: dropping by NAME at every depth hides stored data (posture.generation.generated_at, as_of_date); drop read-time stamps by PATH, measured by two pre-act reads. FWD-30 96/96, 0 of 32,468 differ; Z-S319 disarmed by ad-3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AMGT-ad-1..ad-4 read 'complete' on their LAST <status> tag.",
        "checks/ad_2_hold.py:28 VOLATILE = ('generated_at','as_of_date','read_at','served_at','request_id'), dropped at every depth (AMENDMENT 2).",
        "Live /thesis VLO_US_Equity: /generated_at 2026-09-30T21:25Z; /model/generated_at 2026-09-30T21:25Z; /as_of_date 2026-02-25; /posture/generation/generated_at 2026-09-18T14:10:36Z. scoped_amgt.py:3417 generated_at = _now_iso().",
        "ad2-pre/served/*.json (12) vs live: posture.generation.generated_at or as_of_date moved on 0 of 12.",
        "round54/captures/fwd30_close_sweep_served_20260930T205921Z.tsv: 96 rows OK, val_compared 32468, val_differ 0; upload_verified.sh referenced by all 4 build-and-upload*.sh."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S319"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @27b2146252 asserts 4/4 terminal, ad-2 AC2 re-scoped after failing on a read-time nested stamp with planted negatives failing, FWD-30 96/96, and ad-3 disarming Z-S319/Z-S321.",
    "world_is": "True as read. The re-scope's rule is wider than its failure (it blinds two stored stamps), though neither moved in this act.",
    "notes": "FOR THE ROUND-54 ANALYSIS: volatile keys by path, measured by two pre-act reads; name Z-S322's owner; the posture batch diff when it runs."
  }
]
```
