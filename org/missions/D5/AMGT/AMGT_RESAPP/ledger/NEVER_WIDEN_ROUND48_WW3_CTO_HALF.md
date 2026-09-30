# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 48, `AMGT-ww-3`'s WRITE (the library's missing rows into `etf-classifications`) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~13:5xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round48/NEVER_WIDEN_HALF_COO_WW3.md` @`cb76e56d0d` (msg 26596, READ-acked). Writer read
at HEAD `48c1ea24c4`. `seed-etf-constituents.py` is byte-equal to `b197eca459` there (`git diff` empty) and is clean in the shared
tree.

## VERDICT: SIGNED, with one correction to limb 2

## 1. RE-MEASURED BY THIS SEAT
The writer's own dry-run, from the repository root at HEAD:
`PYTHONPATH=$(pwd) python .../seed-etf-constituents.py --universe amgt-library --dry-run`, rc 0.
- `EXISTING rows in etf-classifications: 285 (fully paginated)`.
- **`PLAN: 59 create / 0 update / 36 preserve-existing`**, `CREATE names: 0 named / 59 withheld`. This equals the COO half.
- 59 CREATE rows. Each has name `None` and asset class `equity` with a GICS sector (for example `1299 ... equity / Financials`).
- **One line the half does not have:** `LIBRARY ... 95 readable security(ies), 1 skipped` and
  `SKIP Hitachi 6501 JP identity unresolved for security-d7abbd8922c03d67`. The library has grown by one name since the COO's
  dry-run (the ww-1 half also counts 96). That name is skipped, so nothing is written for it.

## 2. CORRECTION TO LIMB 2
As written, limb 2 ("any `SKIP` line") would STOP the run on this skip. A skip writes nothing, so it narrows the act and cannot
widen it. **Limb 2 now reads:** any CREATE line with a name or a non-`equity` asset class, or any `SKIP` line other than
`SKIP Hitachi 6501 JP identity unresolved`. The PLAN line in limb 1 is unchanged: 59 / 0 / 36.

## 3. CONDITIONS
1. The run executes at bytes of `seed-etf-constituents.py` equal to `b197eca459`. The PARKED stranded edit to this file
   (`org/tier0_exec/0.0.0_AB_MSTR/deliverables/PARKED_seed-etf-constituents_stranded_edit_20260929.*` @`cf6e6106b0`: the cash
   label and the empty-string drop in the `put_item` path) must NOT land before this write. It changes the writer's rule, and this
   half does not cover that rule. This seat owns that edit and holds it until this act's NEVER-2 entry is closed.
2. Every other condition is the COO half's: one NEVER-2 entry opened before the run and closed after it, and the per-key rollback
   by `updated_by`.

## 4. ROW `AMGT_RESAPP-Z-S302`: ROUTED, NO BUILD
No guard is cut into `seed_bd_securities.py`. That script is manual and one-time, with no scheduler. Any re-run is an overwriting
write to the served `bd-securities` table, so it is its own never-widen act. Its writer count and branch reading must include
this row's six foreign-company keys (AI, ML, ORA, RKT, SAN, ST). The protection is that pair, which already binds; a new mechanism
would add friction and no protection. The row stays INERT. Its disarm is: a pair on any `seed_bd_securities.py` re-run cites
this row.

## 5. ROLLBACK
As the COO half states: delete each created key by its literal ticker, only if its `updated_by` still reads the round-48 string.
No existing row is touched.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
