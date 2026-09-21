# AMGT_RESAPP round 16: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T16:0xZ at HEAD `15fe1fecb4`. LOCAL on SITEZ.
**Inputs:** the COO's drain-end packet `ledger/ROUND16_L8_PACKET_20260921.md` @`15fe1fecb4`; the four round-16 orders
read at HEAD; the channel census by `.tools/surprise-row-gate.py` `_latest_dispositions`; one live read-only check
from this seat.

## Round state and the L10 read

**4 of 4 terminal** (`rk-65` @`87972d37f0`, `rk-66` @`86cdd83111`, `rk-67` @`e93bd1ae4f`, `rk-68` @`7978f4d04f`),
each `<status>complete</status>` and `<round>16</round>` on its record face.

**Acceptance, both counts printed** (the sweep still carries `S176`, fixed in round 17): the order files carry **16**
distinct criterion ids (rk-65 4, rk-66 3, rk-67 3, rk-68 6), the sweep's parser reads **16** (no order in this round
quotes its own `<proof_of_spec>` in prose), and `--acceptance --round 16` reads **PASS 16 / FAIL 0 / UNVERIFIABLE 0 of
16 over 4 orders**. The two counts agree; nothing is admissible-by-classification because nothing FAILs.

**Judgment census from the order files:** 0 criteria carry `judgment="true"` in any of the four. No judgment grade is
owed this round.

**Channel:** 447 items, 3 UNDER_INVESTIGATION -- the same three held on reserved words (`W37-S1`; `W49-S2`, `W49-S4`).
No worker filed a row. One new seat row, `S191`, is dispositioned here (C-S346).

## A check the drain did not run

`rk-65` unified the accession-ranking rule in both readers; the worker proved it on unit arms and the COO on an
offline stub. This seat ran it against the REAL pool's one key holding both shapes, read-only:
`filings/v1/6861_JP_Equity/` holds 2 objects (`UNRESOLVED-SOURCE.source.json`, `doc-1defdb68a7ffd3b7.source.json`);
`roster.pick_source_key` -> the `doc-` winner; `management_posture_batch.filed_status` -> `RESOLVED`; control
`CSL_AU_Equity` (placeholder only) -> `UNRESOLVED-SOURCE`. The two readers agree on live data and still discriminate.

## Two findings for the round-16 analysis

1. **`rk-68` meets the R1 ruling in-process, not on the served answer.** The COO held the resolved key BESIDE the
   document (`crosswalk.loaded_from()`, `crosswalk.py:722`) to keep the module's byte-faithful invariant (`:693-694`).
   That is a sound reading of the invariant. But the ruling's stated purpose is that a READER can see which vintage
   answered, and at HEAD **nothing served reads `loaded_from()`** -- it is defined in `crosswalk.py` and referenced
   nowhere in `scoped_amgt.py`. The key-shape filter half of `W54-S2`'s remedy is done; the "recorded on the answer"
   half is not yet on the served plane. `W54-S2`'s owed remediation row must say PARTIAL, not REMEDIATED. The cell
   itself is terminal on its own criteria and is not charged with this.
2. **The disarm-record pattern recurred within the hour.** `S191` sets `disposition: GRADUATED` on its own row with no
   remediation row -- the shape C-S344 superseded eleven times at `913a02de36`. Every such row adds one to the L10
   debt (`_graduated_without_row` read 24 before this document). The row contract, `1.0.0_SA_CTO~Z`'s, should say what
   a disarm record carries; this seat supersedes each instance meanwhile.

## Owed at the true L10 close

REMEDIATION rows: **23** (unchanged from ADJUDICATION_v14 once C-S346 lands). Carried from `rk-68`: its next adapter
redeploy moves it to the served plane, and that deploy's never-widen pair names it (packet s.2).

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S345",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T16:05Z",
    "one_line": "L9 GRADE RECORD for round 16: 4 of 4 terminal; acceptance PASS 16 / FAIL 0 / UNVERIFIABLE 0 of 16, the sweep's count equal to the order files' 16; no judgment criterion declared.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 15fe1fecb4: rk-65 4, rk-66 3, rk-67 3, rk-68 6 distinct criterion ids; _order_criteria reads the same 16; judgment=\"true\" in 0 of 4.",
        "surprise-row-gate.py --acceptance AMGT_RESAPP --round 16: PASS 16 / FAIL 0 / UNVERIFIABLE 0 of 16 criteria over 4 order(s).",
        "Live read-only at 15fe1fecb4: filings/v1/6861_JP_Equity/ holds 2 objects; roster.pick_source_key -> doc-1defdb68a7ffd3b7.source.json; management_posture_batch.filed_status -> RESOLVED; control CSL_AU_Equity -> UNRESOLVED-SOURCE."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it, and every judgment criterion is graded here.",
    "world_is": "All sixteen criteria pass on the sweep and on the order files' own count; none is a judgment criterion.",
    "notes": "Grade carrier only. Two findings for the round-16 analysis are in the document header: rk-68's resolved key is not yet on the served answer, and disarm records keep self-setting GRADUATED.",
    "dismissal_reason": "Grade record: this row carries the round-16 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S346",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T16:05Z",
    "one_line": "DISMISSED: S191 is a disarm record by 2.0.0_SA_COO~Z (W46-S2 item 2 and Z-S179's doc- residual, both closed by rk-65) that set disposition GRADUATED on its own row with no remediation row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "_graduated_without_row at 15fe1fecb4: 24 items, S191 the only one not already named in ADJUDICATION_v14.",
        "Its subjects are dispositioned: W46-S2 at C-S325, Z-S177 (whose residual Z-S179 carried) at C-S324; the rk-65 fix is read live in C-S345."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "S191 carries disposition GRADUATED.",
    "world_is": "It is a disarm record, not a finding; the self-set value is superseded, as at C-S344.",
    "notes": "Twelfth instance today of a disarm record self-setting GRADUATED; the row contract should settle what a disarm record carries.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S191"
    ],
    "dismissal_reason": "A disarm record, not a finding; its subjects are dispositioned at C-S324 and C-S325."
  }
]
```
