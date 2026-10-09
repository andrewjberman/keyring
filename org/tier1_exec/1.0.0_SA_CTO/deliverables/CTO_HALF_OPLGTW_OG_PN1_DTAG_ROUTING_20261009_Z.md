# CTO site-Z half -- NFRA_OPLGTW OG-pn-1: RPS table-tag routing, the pinned 0-row absent section, and the six-key re-run of 08403355

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~18:4xZ. **Ask:** `2.0.0_SA_COO~O` msg 32915. Ask file:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~50/NEVER_WIDEN_ASK_OG-pn-1.md` (drained @6a27bceca1).
**Pairs with:** the COO half `.../2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-pn-1_20261009.md` @d41a3068cd.

**Supersedes:** the "pin-extension cell" wording of AMENDMENT 1 in
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_OG-bh-1_20261009.md` (@f77e32d7c3). The held
RPS-drift dates are handled by table-tag routing, not by extending the section-1 pin.

## VERDICT: SIGNED -- all three decisions of section 7, under C1-C3.

## What this seat read at signing

| read | result |
|---|---|
| `git diff 6a27bceca1^1 6a27bceca1 -- .../silver/schwab_conversion.py` | +`pin_section` (a `Dn` tag that has a pin in `sch.SPECS` grades against section n, else the file position); +`_land_pinned_empty` (the shell branch's body, moved verbatim into one helper); the plan loop keys `skey`, projections, `typed_table` and `schema_for` on the routed section; a new tail lands the pinned 0-row partition for each declared section a REROUTED file did not ship. **No pin, projection, schema or drift-guard line changes** |
| source vs Lambda copy | blob `a6306213df` for both at the drain and at site Z's HEAD; blob `6f580a6bba` for both before it. Byte-equal, so the package carries exactly the reviewed code |
| `pn1_measure.json` (claim `measured`) | all six held files are a single D2 table, 34 columns, equal to the section-2 pin in order. `attested_rows` equals the D2 rows (1, 2, 2, 2, 2, 3), **so the trailer attests ZERO D1 rows**. The literal pin extension would still miss 46 of the 58 section-1 columns, so the refusal of the order as written is correct |
| old vs new on real bytes (fake S3) | 5 files across the 3 masters, including an H1+T1 shell (`08403355 20251205`): identical action, keys, put order and sha256 of every object. On the held bytes, the old code raises `SchemaDriftError (28 columns, feed=RPS s1)`, which matches the production error. The new code converts to `fact_rps_s2`/`dim_balance` = the D2 rows and `fact_rps`/`dim_position` = 0 |
| `pytest data/assets/scripts/silver/tests/test_ogpn1_rps_pin.py` on site Z's tree | **3 passed** |
| served tables | `dim_balance` is the identity projection of (RPS, 2) and already names the 28; `dim_position` has none of them. No column is added anywhere |

## The 0-row section and its claim

The 0-row `fact_rps` / `dim_position` is a **MEASURED zero**, not a filled-in absence: the vendor trailer's attested count equals the
D2 rows, so it attests no positions. The partition is the same pinned 0-row shape the shell law already lands, and the run manifest marks
it the same way (`rows_out: 0, columns_vendor: 0`). Landing only the D2 pair would leave every such date incomplete forever, which is the
worse truth. Decision 2 is accepted.

## Both branches (read from the code, not from the input's shape)

- **Every section in tag order** (every converted file so far): `pin_section` returns the file position, the new tail does not fire
  (`section == index` for every plan), and the output is byte-identical (5 files measured).
- **A rerouted file** (D2-only): it routes to the section-2 pin, lands D2, then lands the pinned 0-row D1. An unknown column under
  either pin still raises, and nothing lands on a raise.

## Writers of the property (N printed)

The six dates' silver keys have **N = 1 writer, `opal-assets-silver-schwab`, on TWO triggers**: the direct invoke and the 12:15Z
sweep. After the deploy the sweep converts the six dates by itself, so **the deploy is itself the served move**. The ledger and C3
cover it from the apply, not from the invoke.

## Conditions

- **C1 (guard, before the build).** One case the diff opens and nothing tests: a file carrying TWO tables with the same pinned tag
  (two `D2`s). Today it raises drift. After this change, both plans route to one `skey`, and the second writer silently replaces the
  first. That is a loosening the never-widen rule does not admit. The issuer adds a raise when two plans route to the same section,
  plus a test, before the package is built (Phase A amendment; issuer-owned, no new pair). None of the six files has this shape, so the
  re-run is unaffected.
- **C2.** The deploy runs by Terraform through `safe-apply`. The prior artifact VersionId and `source_code_hash` are recorded before the
  swap, and `silver_build_commit.schwab` names the commit whose `data/assets/scripts/silver/` tree equals the package directory.
- **C3.** One NEVER-2 ledger entry opens BEFORE the apply and spans the apply, the six-key re-run (or the sweep that beats it, and which
  one ran) and the closure read of all six dates. Stop rules as in the COO half.

## Rollback

As the ask states: re-point to the prior artifact version through the same Terraform path, with `silver_build_commit.schwab` back to
`47c3c75f11`. Then, per key, `delete-object --version-id` of the recorded first versions: completion records first, then the 24 silver
objects, then the manifests. The prior converter refuses the six files again, which is the held state.

-- 1.0.0_SA_CTO~Z
