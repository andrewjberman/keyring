# AMGT_RESAPP ROUND 60 -- L8 COMPILE (the overlay carries the bar's label)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~14:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round60/DRAIN_END_PACKET.md` @`710cd8c5fc` (1,675 B, read to EOF), msg 27872.
**L7:** `aj-2` (the redeploy, WORLD, AE~A) complete per proof `1ccf6a59db`; `aj-1` landed (`9b4bf29d32`). No judgment criterion.

---

## 1. RE-READ BY THIS SEAT -- the DEPLOYED `opal-amgt-scoped-api`, every row

- **Code:** CodeSha256 `UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo=`, LastModified 2026-10-01T13:59:33Z, equal to the packet.
- **All 94 rows walked, not a sample:** for each TRENDING price row, this seat invoked `/security/{security_key}/overlay`. The
  overlay's `display_name` is present on **94 of 94** and **differs from the bar's label on 0 of 94**. AMD reads "Advanced Micro Devices
  Inc" on both. v71's residue (the header a PM opens from AMD's or TSM's bar shows less than the bar) is closed.
- **Negative arm, live:** a fabricated `ZZZZ_XX_Equity` serves `name` None, `display_name` None, `identity.identity_status`
  UNRESOLVED. No fallback invents a name, and the fabricated key stays distinguishable, as round 59's control requires.

The packet's grade reads moving fields, not HTTP status (round-59 ruling 1), and this seat's read uses the same fields.

## 2. DISPOSITIONS

No new rows. `AMGT_RESAPP-Z-C-S441`'s residue is closed by section 1.

## 3. L10 PRECONDITION

1. **Every task order terminal:** `aj-2` complete; `aj-1` landed. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open. **MET (vacuous)**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

**RESAPP's Friday feed, as this seat has read it on the deployed function across rounds 57-60:**
- monthly chatter, 95 rows, every name a person's;
- price rankings, 94 rows, every bar keyed and labelled, every bar opening onto its own name;
- breakout in percent;
- the T-1 fallback;
- FWD-35 on the scheduled generation.

What remains thin is not RESAPP's: 73 of 95 names carry no collected month, which is HARVST's backfill.

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S442",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T14:45:00Z",
    "one_line": "L8 round 60: the deployed function (UnSqZgCD..., 13:59:33Z) serves an overlay display_name on 94 of 94 price rows, differing from the bar's label on 0 (walked every row, not sampled); AMD reads 'Advanced Micro Devices Inc'; a fabricated key serves no name and identity UNRESOLVED; v71's AMD/TSM header residue closed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo= LastModified 2026-10-01T13:59:33Z.",
        "Deployed /lead-panel/rankings/trending/price 94 rows; /security/{key}/overlay invoked for all 94: display_name missing 0, differs from the row's display_name 0; AMD_US_Equity name and display_name 'Advanced Micro Devices Inc'.",
        "Deployed /security/ZZZZ_XX_Equity/overlay: name None, display_name None, identity.identity_status UNRESOLVED."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-C-S441"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @710cd8c5fc asserts the overlay name live with 0 of 94 differing and regressions YES.",
    "world_is": "True on the deployed function, every row walked.",
    "notes": "RESAPP's Friday feed is complete on the served plane as read across rounds 57-60; the chatter thinness (73 of 95 empty) is HARVST's."
  }
]
```
