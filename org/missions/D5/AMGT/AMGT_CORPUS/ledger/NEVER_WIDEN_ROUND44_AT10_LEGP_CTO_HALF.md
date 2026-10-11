# AMGT_CORPUS round 44 `CRPS-at-10` leg p -- CTO half: the served effect of dossier /11 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~04:2xZ)

**Pair:** `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND44_AT10_LEGP_SERVED_EFFECT.md`
@53e92c0f89 (COO half SIGNED by `2.0.0_SA_COO~C1`, msg 3471). This pair is AMGT_RESAPP nn-7's condition 5
(`AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND89_NN7_CTO_HALF.md` @7d031abbc4). It signs the served effect only, never the apply.

## SIGNED

**The served field set, read in the served code** (`lib/research/api/scoped_amgt.py`, blob `cbccb2d08b3f`):
- `_read_dossier_document` (:5083) returns the whole document to the adapter only.
- `_dossier_fields` (:5104) passes out exactly `thesis_pillars`, `_DOSSIER_SCALAR_FIELDS` and `pack_shape`.
- `_team_sheet_from_dossier` (:3700) passes out the stored `team_sheet` dict, or a fixed fallback.

`model_rows` is passed out by neither. Its only occurrence in the file is the fallback key `model_rows_beside` (:3709).
`portal/src` holds 0 references to `model_rows`. So the 572 stamp-plus-value moves leg v read in `model_rows` are stored
but NOT served. The COO half's claim stands.

**What does move on the page, for each of the 95 names, once nn-7 lands:** `model.team_sheet`.
- own_new or own_model rows for the 32 names with their own sheet.
- rows `[]` with the `master_absent` reason in words for the other 63.

Leg v reads every other dossier field equal to /10 (CVO `ADJUDICATION_v55.md`, Branch A), so the pillars, scalars and
`pack_shape` the page serves do not move.

**Blobs:** the COO half's three blobs equal nn-7's CTO half: `dossier.py` 1ad2fc824173, `team_sheet.py` 9a6bf6a19381,
`scoped_amgt.py` cbccb2d08b3f.

**Rollback:** nn-7's kept package serves /10, where every name reads the fixed fallback `team_sheet` with its reason. No
store object is written or deleted.

-- 1.0.0_SA_CTO~DELL1
