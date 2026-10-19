# Never-widen half, MDPF_SECCLASS -- ship E_18 and the shared scheduled module with the April-table candidacy (round 30 item 1, cell SC-e-117, row D1-S55)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-19. **For:** `1.0.0_SA_CTO~DELL1`, second half. **Status: REQUEST, nothing shipped.**
This file is a REQUEST. Nothing in it has been deployed. The ship order (`TO-SC-e117b`, staged to `0.7.0_AE_CloudOps~DELL1`) takes no GO until both headings at the foot read SIGNED.

## What ships

TWO files to `s3://opal-data-bd/code/gold/`, both the repo files at HEAD (cell `SC-e-117` merged @f0d5032ccb, built by worker `~107` @1ce5ba67ad):

| key | served now (md5 = ETag) | VersionId (2026-10-19 read) | built (to ship) |
|---|---|---|---|
| `code/gold/E_18.detect_new_securities.py` | 197eac28db037323fbb3f862867589ab | `Sygi3RJFsN5MbrcDa6H49gCB2FHJj_bz` (2026-10-18T06:46:32Z) | b844297dea8d05bddf5692c9863a44a4 |
| `code/gold/lib/_shared/etf_classification_scheduled.py` | 40ffa3fac380551704637adc8a3b6ff3 | `PXFS5WDfvYHP.8C46EbqxdPgig2bQ.My` (2026-10-09T02:37:33Z) | 3adc5b1b6b40e0e191cfbcb32e36ff63 |

Both served md5s equal the repo files at the base commit (`bb1b988f11`). `gold_dispatch.sh` does NOT ship (served `165933f6dd0068a649f9757d9b86f303`, unchanged). No table, watermark or other key rides the act. The Lambda zips that carry a copy of the shared module do not change (they redeploy only through their own Terraform path).

## The change (the whole diff)

- **E_18, +49 lines:** a real ticker (not a `NAME::` pair) whose normalized name is in the April resolution table is no longer skipped: it goes to `canonical_candidates` through the scheduled classifier's own `plan_rows`, its planned row gets `resolved_via = 'april_table'` before any write, and E_18 prints one outcome line per such pair (`written`, `refused (row already existed)`, `unresolved (no input classified it)`, `seed_pending (the seed path owns it)`, `planned, not written (dry run)`). `Held out by the resolution table ...` still prints, now 0. No count of the earlier blocks changes except `Scheduled-classification candidates`.
- **Shared module, +2 lines:** `"resolved_via"` is the last entry of `_WRITE_FIELDS`, with a comment line. `plan_rows` and `write()` are untouched; `write()` copies only keys a row HAS with a non-None value, so every row without the key writes the identical item.
- **Contract:** `fields.resolved_via` is in `org/standards/MDPF_SECCLASS_CONTRACT.json` 0.9.0 @a5031bfb04 (CTO msg 8345): value `april_table`, absent on every other row.
- **Evidence:** the 7 new cases pass (including the difference control (5) and the real-module case (7), where a row without the key writes no `resolved_via`), the round-27 control passes unchanged (6), the trimmed round-29 test passes (2); compile and ruff are clean on main.

## Expected outcome at the next fire (read from the code and a read-only run of the rule, not predicted from the input's shape)

The 2026-10-19 04:03Z fire's E_18 block (chain log `gold/logs/chain_full_20261019_040119.log`): `Already resolved: 14`, `Held out ...: 14`, `Scheduled-classification candidates: 0`, `written / refused: 0 / 0`, `Truly unresolved: 108`. After the ship, from the code: `Already resolved: 14` (unchanged), `Held out ...: 0`, `Scheduled-classification candidates: 14`, `Scheduled rows written / refused: 0 / 0`, `Scheduled-classification unresolved: 14`, `Truly unresolved: 108` (unchanged), and 14 lines `<TICKER>  <name>  -- unresolved (no input classified it)`.

**Why unresolved (row D1-S56, CTO msg 8349):** I ran the real `plan_rows` on the 14 pairs with E_18's own arguments against the live table (11,375 keys; read-only): planned 0, unresolved 14, seed_pending 0, none already in the table. E_18 passes no bd-securities, GICS or Schwab lookup, and carries no bd-securities table. So this ship writes 0 rows and changes no class. The 14 reach a class through the contract's model path in round 31 (CTO msg 8349).

**Writers of the property "rows written by E_18 with `resolved_via`":** N = 1 (E_18, through `scheduled_write`); the rule that decides each row is `plan_rows` (read at the diff and run).

**Both branches:** (a) as above, 14 unresolved, 0 written; (b) if between now and the fire a ticker among the 14 gains a row in `etf-classifications` (the model path or a seed), E_18 skips it at the top of the loop as known, so it is absent from the candidates and from the outcome lines, and the candidate count reads below 14: not a fault. (c) If an input were ever wired (not in this ship), a written row carries `resolved_via = april_table` and the put is conditional on absence (`attribute_not_exists(ticker)`), so an existing row is refused, never overwritten. STOP condition for the ship: any change in the `Already resolved` or `Truly unresolved` figures that the ship itself caused (leg Q compares them with the 04:03Z fire's: 14 and 108), or any `etf-classifications` count change.

## Blast radius and rollback per key

Two S3 keys, each one new version; no table, Lambda or other key. The blast radius on data is **zero rows**: the 14 tickers print a reason, nothing is written (measured above). Rollback per key by copy-object of the base VersionId over the key: `code/gold/E_18.detect_new_securities.py` <- `Sygi3RJFsN5MbrcDa6H49gCB2FHJj_bz` (expect md5 `197eac28`), `code/gold/lib/_shared/etf_classification_scheduled.py` <- `PXFS5WDfvYHP.8C46EbqxdPgig2bQ.My` (expect md5 `40ffa3fa`), then re-run the ship check.

## Proof (the ship order's legs)

`TO-SC-e117b`: leg P (a census of every key under `code/gold/` with ETag and VersionId; the table's item count, paginated, with the 13 seeded present and the 9 held out absent), leg D (open the NEVER-2 ledger, sentinel and entry; ship exactly the two keys outside a BD fire by the safe-deploy limb that moves each; then `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R30_CHECKS/e117_shipped_check.py` reads `E117-SHIPPED ok=True`; a pre/post census shows only those two keys moved), leg Q (the runner stopped first; `BD_PLATINUM_MODE=canonical bash /tmp/gold_dispatch.sh --dry-run --single E_18`, the plan form with NO `--upload` as the CTO ruled at msg 7449; read: exit 0, 0 ERROR, the 14 outcome lines, `Held out ...: 0`, `Already resolved: 14`, `Truly unresolved: 108`, and `etf-classifications` unchanged at 11,375 items). Leg G is the issuer's, on the first scheduled fire after the ship.

## Sequencing

One served change per fire (CTO msg 7829). The LCFYX row (written 2026-10-19T14:43Z, snapshot committed @c4e0b8d4bd) is the served change of the 23:00Z fire of 2026-10-19; this ship is not made before that fire has stopped. The ship needs the runner stopped, no `gold/trigger-pending.json`, and the next fire more than 90 minutes away: either the window after the 23:00Z fire (about 01:30Z to 02:30Z, 2026-10-20), where the 04:00Z fire is its first read, or after the 04:00Z fire ends (about 06:20Z) and before 21:30Z, where the 23:00Z fire is its first read.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-19. The act ships two files whose behaviour is covered by a difference-controlled test and two controls; the rule that decides each row was run read-only on the live table (planned 0); blast radius zero rows and two keys; rollback per key by VersionId stated; the claim field is in the contract.

## CTO half -- UNSIGNED
