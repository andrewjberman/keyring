# AMGT_RESAPP ROUND 59 -- L8 COMPILE + L9 (the price identity join, DEMO-BLOCKING)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~13:0xZ
**Input:** `2.0.0_SA_COO~Z`'s `round59/DRAIN_END_PACKET.md` @`2e64642a83` (2,004 B, read to EOF), msg 27834.
**L7:** `ai-2` (the redeploy, WORLD, AE~A) complete per proof `a30a3443fc`; `ai-1` a landed issuer act (`e52b6d1bb5`).

---

## 1. RE-READ BY THIS SEAT -- the DEPLOYED `opal-amgt-scoped-api`

- **Code:** CodeSha256 `E6PdHVFB9z1xUcvCRtNIALjgAaCzNtolAdzaKmCssvM=`, LastModified 2026-10-01T12:34:04Z, equal to the packet.
- **TRENDING price** and **BREAKOUT price**, each: **94 rows, 0 without `security_key`** (62 in this seat's v70), **0 without
  `display_name`**, 0 whose label equals its key, `identity_status` MEASURED on 94 of 94; `name` on 70. Top four by label: Advanced
  Micro Devices Inc, LENOVO GROUP LTD, ASML Holding NV, Taiwan Semiconductor Manufacturing Co Ltd ADR, each keyed.
- v70's finding (two thirds of the price bars could not open a name) is closed on the served plane.

## 2. L9 -- the packet's judgment item: the overlay-200 control (`Z-S332`)

**Measured by this seat, live:** `/security/{key}/overlay` returns **200** for AMD_US_Equity, TSM_US_Equity **and for a fabricated
`ZZZZ_XX_Equity`**. The nested `identity.identity_status` reads MEASURED, MEASURED and **UNRESOLVED** respectively.

**Grade: the executor's re-grade is SOUND; the CTO half's condition 3 as worded was not a control.** "A 200 on AMD's and TSM's
overlay" passes for any key, real or invented. `identity_status` is the field that tells a real key from a fabricated one, and the
fabricated-key arm is the negative control the condition lacked. This is the same class as RESAPP round 55's bound (ADJUDICATION_v67:
a compared field the act does not move proves nothing), seen from the other side: a status every request returns proves nothing. The
packet places the defect in the issuer's and the CTO's wording, not in the act. This seat agrees.

**One residue, not this cell's criterion:** the overlay's `identity` block carries no `name` for AMD_US_Equity or TSM_US_Equity
(`name` None). A PM who clicks those bars opens a header that may show ticker-level identity rather than the company name the bar
showed. The bar label and the header label come from different reads. A thing to look at on the next walk, not a defect graded here.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S332` (the overlay-200 control wording) | **GRADUATED** | confirmed live: fabricated key 200 / UNRESOLVED (section 2) |

The serve-time-only join (the 09-30 generation still stores 62 unkeyed rows; producer unchanged, ruling 2) is recorded as the packet
states it. It is a later enrichment, not a Friday need.

## 4. L10 PRECONDITION

1. **Every task order terminal:** `ai-2` complete; `ai-1`, `ai-3` landed. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open. **MET**
3. **Every judgment criterion graded:** the control item, SOUND re-grade. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S441",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T13:05:00Z",
    "one_line": "L8+L9 round 59: the deployed function (E6PdHVFB..., 12:34:04Z) serves TRENDING and BREAKOUT price at 94 rows each with 0 unkeyed (v70: 62), 0 without display_name, all MEASURED -- v70's price identity gap closed; Z-S332 confirmed live (a fabricated key's overlay also answers 200, identity_status UNRESOLVED), so the executor's identity_status re-grade is the sound control; residue: overlay identity carries no name for AMD/TSM.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 E6PdHVFB9z1xUcvCRtNIALjgAaCzNtolAdzaKmCssvM= LastModified 2026-10-01T12:34:04Z.",
        "Deployed /lead-panel/rankings/{trending,breakout}/price: rows 94 each; security_key null 0; display_name null 0; display_name == security_key 0; identity_status MEASURED 94; name non-null 70.",
        "Deployed /security/{AMD_US_Equity,TSM_US_Equity,ZZZZ_XX_Equity}/overlay: 200, 200, 200; identity.identity_status MEASURED, MEASURED, UNRESOLVED; identity.name None on all three."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S332",
      "AMGT_RESAPP-Z-C-S440"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @2e64642a83 asserts every price bar keyed and labelled on the deployed function and that the overlay-200 control did not discriminate.",
    "world_is": "True on the deployed function; the overlay's identity block carries no company name for the newly keyed AMD and TSM.",
    "notes": "FOR THE ROUND-59 ANALYSIS: a status every request returns is not a control -- grade on identity_status with a fabricated-key arm; look at the header a PM opens from AMD's bar on the next walk."
  }
]
```
