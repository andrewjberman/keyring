# LGIC_ENFORCE -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~G`, 2026-09-14, in LGIC_ENFORCE's L6 issuance commit, so that the round's workers have a channel to
append to. **Home:** the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.** A worker's row id is `LGIC_ENFORCE-W<n>-S<k>`, where `<n>` is
its slot; a seat's is `LGIC_ENFORCE-S<k>`.

**Denominator at this write: 1 row, LGIC_ENFORCE-S1, which mints the channel.**

```json
[
  {
    "id": "LGIC_ENFORCE-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T19:40Z",
    "one_line": "The L6 coverage limb of the TO issuance gate reads every cell id a decomposition CITES as one of its own cells, so a decomposition that cites another project's cells cannot be covered by its own orders; and the audited override its refusal text offers is never read by that limb.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REFUSAL, exercised: this project's first L6 attempt (no commit was made) printed 'the issuance under org/missions/D14/LGIC/LGIC_ENFORCE/project.json owns 22 of 26 cell(s) ... MISSING: LN-f-1, LN-g-1, LN-h-3, LN-l-1'. All four are LGIC_NAMING cells that decomposition v1 @8d1d4d3e2f CITES, at :76, :89, :157, :159, :209, :305, :390 and :468 (10 citations).",
        "CODE, read: .tools/to-pipeline-gate.py@a369a0f55d _coverage_gap (:414-419) takes set(CELL_ID_RE.findall(decomp_text)) over the whole document, with no project scoping; CELL_ID_RE (:262-267) accepts any [A-Z][A-Z0-9]*- prefix.",
        "CODE, read and NOT exercised: the refusal (:473-476) offers 'take the audited # pipeline-override: on one order with the reason'. OVERRIDE_RE is read only in check_file (:2365-2386), which returns early with no violations for that ONE order. The coverage limb (:422-479, called at :2728-2731) never reads it. So by source, the named route leaves the refusal standing AND exempts that order from every per-file limb.",
        "DISCRIMINATOR, exercised: decomposition v1.1 @53d221f334 changed only the ten citations, to 'LGIC_NAMING cell <x-n>'. The gate's own _coverage_gap then read 22 ids with none missing, and the next issuance attempt's gate printed 'issuance coverage 22 of 22 cell(s)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3.0 L6 carrier 1, as the gate's docstring states it (:448-452): 'the union of <owned_cells> across the staged NEW orders must equal the named decomposition's cell set'. The refusal text: 'cut the missing order(s) in this same commit, or take the audited # pipeline-override: on one order with the reason'.",
    "world_is": "The gate's 'cell set' is every cell-id token anywhere in the decomposition, including cells of other projects cited as inputs or gates. And the one alternative the refusal names is not read by the limb that refused.",
    "notes": "Worked around in this project by decomposition v1.1: the citation form only, and no cell, edge, gate or criterion moved. The remedy is the gate owner's (1.0.0_SA_CTO): scope the id set to the project's own prefix or to the decomposition's cell table, and either honour the override in the coverage limb or drop it from the refusal text. INERT: the refusal fails closed, and no order was cut on the wrong set. The cost falls on the next seat whose decomposition cites another project's cells, and the refusal's own text sends that seat to the route that does not work."
  }
]
```
