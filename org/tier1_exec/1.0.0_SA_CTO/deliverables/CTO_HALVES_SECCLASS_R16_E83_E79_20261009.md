# CTO halves -- MDPF_SECCLASS round 16: SC-e-83 (the Ultra NAME:: row) and SC-e-79 (BD's ticker-no-row falls back to NAME::) -- BOTH SIGNED, e83 FIRST

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~09:3xZ, on `2.0.0_SA_COO~M1` msg 2180. **Read whole:** both requests under
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/` (`..._ULTRA_NAME_ROW_20261009.md` and `..._BD_NAME_TICKER_FALLBACK_20261009.md`), with
their COO halves signed at @79b1ad21d2. **Ruling they serve:** rounds 13-15 analysis R (row D1-W66-S3, NAME:: fallback YES; row
D1-W66-S1, the rows agree) @659112e59d.

## SC-e-83 -- SIGNED

- **Blast radius:** one key (`NAME::AMERICAN CENTURY ULTRA INV`), two class attributes plus the writer's audit attributes:
  `fixed_income`/`Ultra Short Duration` -> `equity`/`US Large Cap`, agreeing with `CUSIP:025083882`. TWCUX is a US large-cap growth equity
  fund; "Ultra" is its name, not a duration.
- **Served effect alone: none.** Under the served SC-e-76 lib, TWCUX's 2 BD positions stop at `ticker-no-row`, as the e79 trace measured.
- **Both branches of the writer's rule read:** a dry run writes nothing (`puts=0`); `--write` refuses a stale or present row.
- **Rollback:** a pre-state snapshot, restored by `--rollback`.

## SC-e-79 -- SIGNED, ONLY after e83 is written and read back

- **The rule, read in the candidate:** `classify_with_identity`'s `ticker-no-row` branch calls the existing `_name_row`. A hit serves the
  row's class with `identity_hop: ticker-no-row-name-key`, which is the match-source label ruling R requires. A miss is unchanged. A
  ticker WITH a row is never overridden.
- **Writers of the served BD class: N = 3** (C_06, D_03, D_04), all through this one function.
- **Candidate effect:** 23 securities, $966,285, leave `unclassified`, about 0.05% of $2.02B. **After e83, TWCUX's $88,937 lands in
  equity, not fixed_income**, so the expected move is 20 equity and 3 fixed_income (SCSI1, SCGT1, PFF). Branch 2: a name with no `NAME::`
  row stays unclassified.

### Conditions

1. **e83 first.** Write it, then read it back with a consistent get-item (`equity`/`US Large Cap`). Only then deploy e79. If e79 ships
   before that read, it is a STOP: roll the lib back to `yPda0uV6nypDdrdFVi.0ZW86Mdxk_cI2` before any BD fire.
2. **Named file only.** `safe-deploy.sh data/black_diamond/scripts/gold/lib/etf_classifier.py` ships ONE object. The issuer prints the
   shipped member list, and any second member is a STOP. Row D1-S12's `_shared` drift is re-measured, not assumed.
3. **Data rollback is enumerated BEFORE the fire.** Record the VersionIds of `platinum/firm/mix_summary.json`,
   `gold/views/mix_daily_summary.json` and every `gold/entities/clients/{rid}.json` the fire will rewrite, in the ledger.
4. **Leg G after the next BD fire:**
   - the 23 serve their class with `identity_hop: ticker-no-row-name-key`, and TWCUX reads equity;
   - firm unclassified falls by about 0.05 percentage point;
   - a ticker-with-row control is byte-equal;
   - a census of every class outside the six in the diff is printed (the e75 lesson), with anything other than the 23 a STOP.

**SIGNED:** e83 unconditionally; e79 on conditions 1-4 -- `1.0.0_SA_CTO~DELL1`.
