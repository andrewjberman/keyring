# AMGT_RESAPP -- the citing rows for the round-76 rulings on the 53 BLOCKED remediation rows: 13 clocks closed, 4 held open against their rulings, 36 placed

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~22:4xZ (drafted under MSTR~Z's HOLD, msg 30373; committed on RELEASE)
**Input:** `1.0.0_SA_CTO~Z` `ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @`4a89bef967` (101 lines, 32 rows + ADDENDUM 1, msg 30363) and `2.0.0_SA_COO~Z` `round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @`fb9ca91ad5` (78 lines, 21 rows, msg 30367). Both were read to EOF. **Denominator: 53 distinct rows.** All 53 carry a remediation row, and each read OPEN before this commit.

## 1. Clocks moved in place (13)

| row | move | basis |
|---|---|---|
| `Z-S119`, `Z-S14`, `Z-C-S369`, `Z-C-S46`, `Z-W2-S10` | CLOSED_UNREMEDIATED, NOT_A_DEFECT | CTO section E |
| `Z-W5-S1`, `Z-W45-S2` | CLOSED_UNREMEDIATED, NOT_A_DEFECT | COO section E |
| `Z-S283` | CLOSED_UNREMEDIATED, ACCEPTED_BY_RULING | CTO section E (the citation rule) |
| `Z-S238` | CLOSED_UNREMEDIATED, ACCEPTED_BY_RULING | COO section E (not cut; returns as a new row when an outcome needs it) |
| `Z-C-S4` | CLOSED_UNREMEDIATED, CARRIED_BY its children (`Z-W3-S1` is a cell) | COO section E |
| `Z-W31-S3` | REMEDIATED | walks sign in as the UI walker; this round's walk did (az-6, `WALK_ROUND76.md`) |
| `Z-C-S24`, `Z-S6` | REMEDIATED | the CTO's condition is met: `prd-signoff.py status AMGT_RESAPP` reads the ratified half SIGNED and current at v0.41, bound to half_hash ff51e26ae300 (sign-off @`30bc4c03e6`) |

Eight of the 13 were ARMED, and each reads DISARMED with this move: `Z-W5-S1`, `Z-S238`, `Z-C-S4`, `Z-C-S46`, `Z-C-S24`, `Z-S6`, `Z-S14`, `Z-W2-S10`. Two (`Z-C-S369`, `Z-W31-S3`) were already DISARMED.

## 2. Ruled closed, but held OPEN here (4)

| row | the ruling | why the clock does not move |
|---|---|---|
| `Z-S2`, `Z-C-S2` (both ARMED) | NOT_A_DEFECT: the set grain is the issuer's loop, printed in the drain-end packet as "checked N of N" with the list | **The round-76 packet @`a74117fb6a` carries no such line.** The ruling names a mechanism that is not yet applied. Both rows close at the first packet that prints it |
| `Z-S220` | "RULED-CLOSED (design given)" and, in the same cell, "the row stays PARKED" | The ruling says both. It stays OPEN and parked on its stated condition (a web-search source is admitted), with the key design recorded |
| `Z-W212-S2` | closed by evidence: HARVST rebuild #7 gave every mention row a url | The COO's own record calls the served proof thin (3 items) and says the triage worker read no store. It closes on one store-side read with its denominator, which this seat or `2.0.0_SA_COO~H` can take |

## 3. Placed, still OPEN (36)

| placement | rows |
|---|---|
| CTO cells for round 77 (identity resolving; comparable / Peers V mapping; CSC present columns; ONE PAGER precedence; export chart line; name-search route; passage section coverage; translated text) | `Z-S117`, `Z-W7-S3`, `Z-W19-S6`, `Z-W20-S12`, `Z-W21-S4`, `Z-W20-S11`, `Z-S162` (part 1), `Z-W18-S13`, `Z-W21-S6`, `Z-W3-S1`, `Z-W173-S4`, `Z-S228`, `Z-W20-S8`, `Z-S221` |
| COO batched repair cell | `Z-C-S35`, `Z-W7-S7`, `Z-S343`, `Z-S218`, `Z-W88-S1`, `Z-C-S372`, `Z-S278`, `Z-W19-S16` |
| COO own cell | `Z-W37-S2` |
| rides a CTO-ruled cell | `Z-W21-S3`, `Z-S78` |
| re-owned to another lane | `Z-S242` (`0.7.0_AE_CloudOps`, one LF re-commit), `Z-W2-S3` and `Z-C-S3` (`0.8.0_AE_CloudComp`, `.terraform` in EPHEMERAL_DIRS), `Z-W173-S3` (`2.0.0_SA_COO~D`) |
| at Andrew (3 cards) | `Z-W22-S2`, `Z-W22-S3`, `Z-W22-S6`, `Z-W22-S7`, `Z-W22-S8` (FWD-11's social source); `Z-S162` part 3 (Peers V on a short set); `Z-S230` (the Bloomberg credential rotation) |
| held on Andrew's standing word | `Z-W45-S1` (no fleet re-run) |

The remediation rows' `owner` fields are not edited, because only clocks move in place. Where a ruling re-owns a row, this table is the carrier.

## 4. ARMED after this commit

`comp-surprise --armed --project AMGT_RESAPP` read 17 before. Five of those 17 are disarmed here: `Z-S6`, `Z-C-S46`, `Z-C-S24`, `Z-C-S4` and `Z-S238`. The expected read is 12, and it is re-measured after the commit.

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S467",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T22:45:00Z",
  "one_line": "The citing row for the round-76 rulings on the 53 BLOCKED remediation rows (CTO @4a89bef967, 32 rows + ADDENDUM 1; COO @fb9ca91ad5, 21 rows): 13 clocks moved in place (10 CLOSED_UNREMEDIATED, 3 REMEDIATED), 36 placed and still OPEN, and 4 ruled closed but held OPEN -- Z-S2 and Z-C-S2 because the 'checked N of N' packet line the ruling names is absent from the round-76 packet, Z-S220 because its ruling says both closed and parked, Z-W212-S2 because its store-side proof is unread.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md @4a89bef967 (101 lines): RULED-CELL 11, RULED-CLOSED 11, RE-OWNED 3, AT ANDREW 7; ADDENDUM 1 three rows",
    "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md @fb9ca91ad5 (78 lines): REPAIR-CELL 8, OWN-CELL 1, RIDES 2, OFFERED 2, RULED-CLOSED 5, RE-OWNED 2, HELD-ANDREW 1",
    "remediations/REMEDIATION_v1..v21 read by 3.0.0_SA_CVO~Z: 53 of 53 ruled ids carry a remediation row, each remediation.state OPEN before this commit",
    "prd-signoff.py status AMGT_RESAPP: v0.41 @b5f90bbf8d ADMITTED, ratified-text SIGNED current (sign-off @30bc4c03e6, half_hash ff51e26ae300...)",
    "round76/DRAIN_END_PACKET.md @a74117fb6a: no 'checked N of N' line"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_RESAPP-Z-S119", "AMGT_RESAPP-Z-S14", "AMGT_RESAPP-Z-C-S369", "AMGT_RESAPP-Z-C-S46", "AMGT_RESAPP-Z-W2-S10",
   "AMGT_RESAPP-Z-W5-S1", "AMGT_RESAPP-Z-W45-S2", "AMGT_RESAPP-Z-S283", "AMGT_RESAPP-Z-S238", "AMGT_RESAPP-Z-C-S4",
   "AMGT_RESAPP-Z-W31-S3", "AMGT_RESAPP-Z-C-S24", "AMGT_RESAPP-Z-S6",
   "AMGT_RESAPP-Z-S2", "AMGT_RESAPP-Z-C-S2", "AMGT_RESAPP-Z-S220", "AMGT_RESAPP-Z-W212-S2",
   "AMGT_RESAPP-Z-S117", "AMGT_RESAPP-Z-W7-S3", "AMGT_RESAPP-Z-W19-S6", "AMGT_RESAPP-Z-W20-S12", "AMGT_RESAPP-Z-W21-S4",
   "AMGT_RESAPP-Z-W20-S11", "AMGT_RESAPP-Z-S162", "AMGT_RESAPP-Z-W18-S13", "AMGT_RESAPP-Z-W21-S6", "AMGT_RESAPP-Z-W3-S1",
   "AMGT_RESAPP-Z-W173-S4", "AMGT_RESAPP-Z-S228", "AMGT_RESAPP-Z-W20-S8", "AMGT_RESAPP-Z-S221",
   "AMGT_RESAPP-Z-C-S35", "AMGT_RESAPP-Z-W7-S7", "AMGT_RESAPP-Z-S343", "AMGT_RESAPP-Z-S218", "AMGT_RESAPP-Z-W88-S1",
   "AMGT_RESAPP-Z-C-S372", "AMGT_RESAPP-Z-S278", "AMGT_RESAPP-Z-W19-S16", "AMGT_RESAPP-Z-W37-S2",
   "AMGT_RESAPP-Z-W21-S3", "AMGT_RESAPP-Z-S78",
   "AMGT_RESAPP-Z-S242", "AMGT_RESAPP-Z-W2-S3", "AMGT_RESAPP-Z-C-S3", "AMGT_RESAPP-Z-W173-S3",
   "AMGT_RESAPP-Z-W22-S2", "AMGT_RESAPP-Z-W22-S3", "AMGT_RESAPP-Z-W22-S6", "AMGT_RESAPP-Z-W22-S7", "AMGT_RESAPP-Z-W22-S8",
   "AMGT_RESAPP-Z-S230", "AMGT_RESAPP-Z-W45-S1"
  ],
  "spec_asserts": "Every BLOCKED remediation row names a live owner and one outcome; a row ruled closed moves its clocks.",
  "world_is": "53 of 53 carry a ruling. 13 clocks moved; 4 rulings name a condition the world does not yet meet; 36 are placed with an owner.",
  "notes": "FOR 1.0.0_SA_CTO~Z: (1) Z-S2 / Z-C-S2 close at the first drain-end packet that prints 'checked N of N' with its list -- the round-76 packet does not. (2) Z-S220's cell says RULED-CLOSED and PARKED; it is carried as parked. FOR 2.0.0_SA_COO~Z: Z-W212-S2 closes on one store-side read of the gold mention url column with its denominator."
 }
]
```

-- 3.0.0_SA_CVO~Z
