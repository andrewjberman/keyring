# AMGT_CORPUS ROUND 20 -- L8 COMPILE (no judgment criterion on the orders)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~03:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND20_DRAIN_END_PACKET.md` @`0`, msg 26884. The packet was read to EOF (5,374 B).
**L7:** `v-1`, `v-2` complete and merged per the packet. `v-3` is held on AMGT_RESAPP r51 cell 1, and nothing is registered. The six
outcomes' grade is the CTO's (ruling 2): a met served half with an unrendered page half is NOT REALIZED.

---

## 1. THE PAGE HALF'S CAUSE, RE-READ BY THIS SEAT

- **Portal:** `git -C portal grep -l dossier_fields 29c8226a -- src` finds **0 files**. The control `team_cases` finds 3, and portal
  HEAD is still `29c8226a`. The page consumes none of the six outcomes' served block.
- **Served:** IMB_LN_Equity's `/thesis` carries `dossier_fields` with `thesis_pillars`, `management`, `fund_of_record` and
  `last_stated_position`. AZN_LN_Equity's `model.team_cases` carries **base, upside and downside, all SERVED**, each with an EPS
  table.
- So the six outcomes are **served and not rendered.** The ask to DSGN_AMGTV1 is exactly what packet section 7 item 1 names.

## 2. ⭐ FWD-12'S PAGE HALF: WHAT THE PACKET'S "Upside/Downside read 'not in the pack yet' although served" ACTUALLY SHOWS

This seat read the v-2 walk's `089-AZN-LN-Model.png` and the served `/thesis` together.
- **The page renders only "THE RESEARCH TEAM'S BASE CASE".** The team's Upside and Downside are served (above) and not drawn.
- **The lines "Upside case: not in the pack yet -- the method is to be agreed" and "Downside case: ..." are not about the team's
  cases.** They render Opal's RULE cases: `model_cases.upside` / `.downside` are served `ABSENT` with reason "methodology to be
  discussed with Andrew". Beside them, "Opal's historical-multiple reference: not in the pack yet -- quote currency 'GBp' and
  reporting currency 'USD' differ ..." is `model_cases.base` ABSENT with `currency_mismatch`.
- **So the page states nothing false about the team's cases, but it misleads.** A bare "Upside case: not in the pack yet" sits
  on a page whose team Upside IS in the pack. It names neither whose case it is nor why "the pack" is the wrong noun for a
  rule-case absence. This is the whose-case defect that DSGN_AMGTV1's v-4 fixed for Base only (ADJUDICATION_v7, observation 3).
  **For the page ask:** render the team's Upside/Downside, and label the rule's absent cases as Opal's ("Opal's rule-based upside:
  the method is to be agreed").

## 3. THE WORKER'S TWO LIMITS -- AGREED

- **FWD-16's "PDF-only" 25/25** is a floor, because the payload has no pack-shape field and "every served citation ends in `.pdf`"
  is a proxy.
- **FWD-15's "machine verdict byte-unchanged" clause** is unexercised, because no team posture renders to compare.

## 4. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W2-S15` (6501's `/thesis` serves no `dossier_fields` block, so it carries no per-field ABSENT reason) | **CARRIED** -> AMGT_RESAPP | Counted as not carrying, which is right. The producer should serve the block with its ABSENT reasons. |
| `Z-S63`, `Z-S66` (ARMED) | **CARRIED** | v-3 waits on AMGT_RESAPP r51 cell 1 |
| `Z-S64` | **CARRIED** | the migration item |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | |

## 5. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2 cut. v-3 was held on a named external block. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** CARRIED with owners as above. **MET**
3. **Every judgment criterion graded:** 0 on the orders. The six outcomes are the CTO's grade. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S23",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T03:55:00Z",
    "one_line": "L8 round 20: the six outcomes are served and unrendered -- portal 29c8226a has 0 dossier_fields consumers (control team_cases 3); AZN's page shows only the team's Base while team Upside/Downside are SERVED; its 'Upside/Downside case: not in the pack yet' lines are Opal's RULE cases (served ABSENT, 'methodology to be discussed with Andrew'), unlabelled -- misleading beside a team Upside that is in the pack.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal grep -l dossier_fields 29c8226a -- src: 0 files; team_cases: 3 files; portal HEAD 29c8226a.",
        "Deployed /thesis IMB_LN_Equity: dossier_fields keys [thesis_pillars, management, fund_of_record, last_stated_position]; AZN_LN_Equity: model.team_cases base/upside/downside status SERVED with EPS tables; model_cases.upside/downside status ABSENT reason 'methodology to be discussed with Andrew', model_cases.base ABSENT cause currency_mismatch.",
        "Walk 20260930T032251Z shot 089-AZN-LN-Model.png: 'THE RESEARCH TEAM'S BASE CASE' table only; lines 'Upside case: not in the pack yet -- the method is to be agreed.', 'Opal's historical-multiple reference: not in the pack yet -- quote currency 'GBp' and reporting currency 'USD' differ ...', 'Downside case: not in the pack yet -- the method is to be agreed.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The drain-end packet asserts v-1 and v-2 VALID, the six render outcomes met on the served half and unmet on the page (0 portal dossier_fields consumers), and that AZN's Upside/Downside read 'not in the pack yet' although served.",
    "world_is": "True on the served and page halves; the AZN lines are the rule's absent cases, not a false statement about the team's -- but unlabelled beside a team Upside that is in the pack, which misleads a PM.",
    "notes": "FOR THE PAGE ASK TO DSGN_AMGTV1: render dossier_fields and the team's Upside/Downside; label the rule's absent cases as Opal's (the v-4 whose-case fix, extended past Base)."
  }
]
```
