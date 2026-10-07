# CTO half -- MDPF_SECCLASS S29: `multi_asset` joins the Cottonwood and Black Diamond gold class lists -- WITHDRAWN 2026-10-07 ~00:5xZ

**Signer:** `1.0.0_SA_CTO`, 2026-10-07 ~00:2xZ. **Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S29_CLASS_LISTS_20261006.md`
(CLOUD c5d415b83b), COO half signed by `2.0.0_SA_COO~M`. Asked in msg 105846.

## What I read

The request in full: the act, the producers' rule, the before/after tables, blast radius, writers, both branches, rollback, acceptance.

## The half

- **Blast radius (signed as named):** at each firm's next scheduled gold run, the served key families the request lists.
  - Cottonwood (`opal-data-cot`): `gold/entities/clients/*.json` (219 mixes, of which four change composition), `gold/views/mix_daily_summary.json`,
    `platinum/firm/mix_summary.json`, `gold/artifacts/firm_mix_views.json`, `gold/views/firm_composition.json`, and the client compositions.
  - Black Diamond (`opal-data-bd`): the same families.
  - No historical published point changes; a history entry without the key reads 0.0.
  - Nothing outside these two firms is touched: Inflection and every runner were triaged HOLDS-NONE.
- **The expected outcome is read from the producers' own rule**, not predicted from the input's shape: the in-process `C_06` run on the real 10-05
  positions, and the COO's Black Diamond check.
  - Cottonwood: the four SGIIX holders go from 0.904-0.973 to 1.
  - Firm composition: the gap closes on both firms ($266,651.67 at Cottonwood, $5,438,537.08 at Black Diamond, to the cent).
  - Black Diamond's 47 multi-asset holders publish a `multi_asset` share. The class the canonical table already holds for those positions
    becomes visible; it is the table's verdict, not this act's.
- **Writers counted:** N printed per key (`D_04` live for mix_summary, `D_03` for firm_composition, `C_06` for client entities); `d08` writes
  nothing. I accept the count as read by the COO.
- **Both branches:**
  - (A) A run on the live code: covered above.
  - (B) A run reading a half-uploaded set: only possible at Cottonwood between 16:20Z and 18:53Z on 10-06. No scheduled run fell in that
    window; an ad hoc run is not ruled out ("not read").
  - Condition attached: before Cottonwood's next run the COO reads the 10-06 run history. If any Cottonwood gold run fell between 16:20Z and
    18:53Z, its outputs are re-read against the acceptance before the scheduled run proceeds.
- **Rollback per key:** `copy-object` of the prior VersionIds listed (five Cottonwood, three Black Diamond). Accepted.
- **Acceptance:** as stated (items 1-3), read from the served keys after each firm's run.

## Recorded, not blocking

The code reached S3 through the push deploy gate before this half existed (row `MDPF_SECCLASS-S35`, ARMED, disarm owner `2.0.0_SA_COO~M`). The
served move has not happened, so this half still precedes it. The gap is the gate's: a gold file deploys on push whether or not its served-move
half is signed. That belongs in the round analysis, not to this act.

**SIGNED.** The COO's 04:45Z / 11:00Z rollback rule is stood down by this half.

-- 1.0.0_SA_CTO

## WITHDRAWN (1.0.0_SA_CTO, 2026-10-07 ~00:5xZ)

Andrew-direct ~00:4xZ at the `2.0.0_SA_COO~M` terminal (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`): "there should be
no multi-asset class. There are 6 classes: cash, fixed income, equity, structured, alternatives, commodities." This act publishes
`multi_asset` as a seventh class, so this half no longer holds. The COO rolls the eight objects back to the prior VersionIds before Black
Diamond's ~05:25Z run (the rollback this half had stood down is reinstated). The short sums return until the 33 `multi_asset` rows are
remapped into the six classes by the rule Andrew picks; the class-list code then needs no seventh class at all.
