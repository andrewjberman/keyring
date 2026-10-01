# AMGT_RESAPP ROUND 52 -- L8 COMPILE + L9 (ab-3 AC2)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~12:5xZ
**Input:** `2.0.0_SA_COO~Z`'s `round52/DRAIN_END_PACKET.md` @`54f5805c8d`, msg 27140. The packet was read to EOF (6,329 B).
**L7 re-measured:** `ab-1`..`ab-6` read `complete` on their LAST `<status>` tag. There is 1 judgment criterion (`ab-3` AC2).

---

## 1. THE SERVED STATE, RE-READ

- **The build:** `opal-amgt-scoped-api` returns CodeSha256 **`nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w=`**, LastModified
  2026-09-30T11:43:22Z. This equals ab-6's close.
- **ASML's driver chart:** `/api/scoped/amgt/security/ASML_NA_Equity/thesis` returns 200 with `thesis_driver_chart.status` **SERVED**,
  `source` **filing**, series "Issued ordinary shares outstanding (nominal EUR0.09) ...", and points from 2023. **The round-51 carried
  unmet (zz-8 AC2) is met.**
- **6501:** `/thesis` returns 200. `dossier_fields` carries every field ABSENT with the reason "no research dossier exists for this
  name", so the page can say why (the DSGN n-4 read at v13 agrees).
- **FWD-30, not gradeable at close: the packet's diagnosis is confirmed.**
  - The sweep `.tsv` sums **131** `val_differ` over 96 names, with `val_unscaled` 0.
  - The `.log` names a header mnemonic on **all 131** differing lines, and 0 differing lines name anything else.
  - Every sampled line reads the cell as the displayed figure concatenated with its tooltip: `EQY_BETA` "1.05" + "1.048774 | RATIO
    ...", and `PX_LAST` "HKD 73.75" + "73.75 | PRICE ...".
  - This is a grader parsing gap opened by DSGN r12's hover figures, **not a value move**. The issuer rightly did not re-tune the
    grader at close.

## 2. L9 -- `ab-3` AC2: "each mapping row's `relation` follows from its two quotes read side by side"

This seat read all 9 rows of `0.9.0_WK_AMGT_RESAPP~187/PAGE_FWD_MAP_ROUND52.json`.

**VERDICT: PARTIAL -- 8 of 9 follow; FWD-27's does not.**

| row | quotes (RESAPP / DSGN) | relation | follows? |
|---|---|---|---|
| FWD-21 -> FWD-6 | Thesis on one screen under ONE dark band / three cards under the main chart | partly-covers | yes. Both present the Thesis; the one-band layout is not covered. |
| FWD-22 -> FWD-4 | LABELLED TILES, not a mnemonic list / four cards each leading with one figure | partly-covers | yes. Labelled headline figures, a different form. |
| FWD-23 -> FWD-6 | evidence folded until asked for / each opens a window with its sentences and their evidence | partly-covers | yes |
| FWD-24 -> FWD-9 | the Model sheet as a table, a refusal as ONE line / every missing line says in one sentence ... | partly-covers | yes. The one-line refusal is covered; the table is not. |
| FWD-25 -> FWD-8 | the columns that EXIST, absent ones openable / explains missing columns once and neatly | partly-covers | yes |
| FWD-26 -> FWD-10 | verdict as a headline, reasons as cards / a verdict card with numbered reasons that each open | partly-covers | yes. The reasons' form differs. |
| **FWD-27 -> FWD-11** | **"The Lead Panel's controls read as the Dashboard's controls do" / "every footer reads as a time and a source"** | partly-covers | **no.** The quotes concern different objects: controls, and footers. Side by side they share nothing. The overlap (a "Source:" footer) is in RESAPP FWD-27's DONE WHEN, which the row does not quote. On its two quotes the relation reads `none`. |
| FWD-28 -> FWD-11 | four DESIGNED empty states / empty states are the same pieces | partly-covers | yes |
| FWD-29 -> none | the render check PASSES and CAN FAIL / (no DSGN quote) | none | yes |

**Effect on what was already executed (ruling 4, @`44d6bc3e31`): none on substance.** FWD-27 was carried WHOLE to DSGN FWD-18, and
this seat's v0.29/v0.4 review found its properties intact. Only Addendum C's placement note "FWD-27 -> DSGN FWD-18 (beside DSGN
FWD-11)" rests on the unsupported relation. Under the addendum's own condition ("if the CVO's L9 grade of the map's AC2 changes a
row's relation, this section is amended at the round-52 L10"), that line should read like FWD-29's: no DSGN owner before v0.4. That
is a wording change under an unchanged obligation.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S312`, `Z-S311` (the zz-8 AC2 premise was false; ASML's driver chart was carried unserved) | **GRADUATED** | `thesis_driver_chart` is SERVED from `filing` on the deployed build (section 1) |
| `Z-S314` (ARMED: any live `--rebuild-pool` run regresses served `/thesis` sentences) | **CARRIED** as ARMED -> the round-53 cell (`disarm_owner` `2.0.0_SA_COO~Z`) | Only a manual invocation reaches it: this seat scanned 208 local scheduled tasks, and 0 invoke `rebuild-pool` or `draft`. It stays ARMED until the regeneration keeps served sentences. |
| `Z-S313` | **CARRIED**, INERT | superseded in standing by `Z-S314` |
| `Z-S315` (the harvest.store docstring is false) | **CARRIED** -> round 53 | text only |
| `Z-W186-S1` (ab-1 AC2's expect wording) | **CARRIED**, INERT | the issuer's wording gap |

## 4. FOR THE ROUND-52 ANALYSIS

1. **The FWD-30 grader must read the DISPLAYED value, not the cell's whole text.** Until it does, FWD-30 has no post-DSGN-r12 grade.
   Pairing the grader fix with a planted tooltip cell would prove it reads the figure only.
2. Addendum C's FWD-27 placement line (section 2).
3. Z-S314's cell.
4. The sequencing of the slash-key move with RESAPP's consumers.

## 5. L10 PRECONDITION

1. **Every task order terminal:** 6 of 6. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S312`/`Z-S311` GRADUATED; `Z-S314` CARRIED as ARMED to its cell, with its
   owner. **MET**
3. **Every judgment criterion graded:** 1 of 1, PARTIAL (FWD-27). **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S432",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T12:50:00Z",
    "one_line": "L9 round 52: ab-3 AC2 PARTIAL -- 8 of 9 mapping relations follow from their quotes; FWD-27's 'partly-covers' does not (controls vs footers; the overlap lives only in the unquoted DONE WHEN). Served: nKWCfQRQ, ASML thesis_driver_chart SERVED from filing, 6501 dossier_fields ABSENT with reason; FWD-30's 131 diffs are all header cells read as figure+tooltip (grader gap, not a value move); Z-S312/Z-S311 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AMGT-ab-1..ab-6 read 'complete' on their LAST <status> tag.",
        "Lambda opal-amgt-scoped-api CodeSha256 nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w=, LastModified 2026-09-30T11:43:22Z.",
        "Invoke /api/scoped/amgt/security/ASML_NA_Equity/thesis: 200, thesis_driver_chart.status SERVED, source filing; 6501_JP_Equity/thesis: 200, dossier_fields every field ABSENT 'no research dossier exists for this name'.",
        "round52/captures/fwd30_value_sweep_post_ab6_stubbed_20260930T122939Z.tsv: sum val_differ 131, sum val_unscaled 0; .log: 131 differing lines all name HEADER EQY_BETA/PX_LAST/CURR_ENTP_VAL, 0 others; sample page='1.051.048774 | RATIO ...'.",
        "PAGE_FWD_MAP_ROUND52.json row FWD-27: resapp_quote 'The Lead Panel's controls read as the Dashboard's controls do', dsgn_quote 'every footer reads as a time and a source', relation partly-covers.",
        "Scheduled tasks scanned 208; actions matching rebuild-pool/draft 0."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S312",
      "AMGT_RESAPP-Z-S311"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @54f5805c8d asserts 6/6 terminal, ab-6 live at nKWCfQRQ with ASML's chart served from the filing, FWD-30 not gradeable because the grader reads header tooltips, and presents ab-3 AC2 for judgment.",
    "world_is": "True as read. The map's FWD-27 relation does not follow from its two quotes. Nothing already executed loses an obligation; only Addendum C's placement note rests on it.",
    "notes": "FOR THE ROUND-52 ANALYSIS: FWD-30's grader reads the displayed figure (with a planted tooltip control); Addendum C's FWD-27 line to 'no DSGN owner before v0.4'; Z-S314 stays ARMED to its round-53 cell."
  }
]
```
