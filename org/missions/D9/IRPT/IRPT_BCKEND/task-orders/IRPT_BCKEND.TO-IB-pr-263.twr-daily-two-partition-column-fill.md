# TO IRPT_BCKEND.TO-IB-pr-263 -- The two 49F twr_daily partitions missing bmv/emv/cf_net/cf_gross are filled by the producer's own path

<to_id>IRPT_BCKEND.TO-IB-pr-263</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~S</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>superseded</status>
<superseded_by>row IRPT_BCKEND-S236 (0.4.0_DS_ClientPlatform~S @6b5755c32c, 2026-09-30 15:3xZ): the four columns are NOT derivable on either date by the producer's own path -- date=2024-07-08 is the series' first day (no prior canonical_valuation partition; 4,074 of 4,074 rows REFUSED-NO-BMV) and date=2025-01-09 is not a trading day (NYSE closure; 4,808 of 4,808 NO-PRIOR-TRADING-DAY); c02_twr_engine.py attaches bmv/emv/cf_net/cf_gross only on the OK branch (:273-276), so a re-emit at DEPLOYED bytes returns the same 11 columns (rc 0, no S3 write, all five ETags equal the BEFORE record). The issuer rules (round 26, inside its own decomposition): the need is met by the finding -- both partitions are non-performance days by the producer's own rule, and the reader guard that trips on them (f49_engine.py:134, the retiring engine's reader) no longer serves 49F since the r3 re-switch; no schema bump is cut. S219 is dispositioned by S236; a reader-side skip of zero-OK partitions is cut only if a live reader of twr_daily is shown to touch those two dates.</superseded_by>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-25 ~P ANALYSIS section 2, row S219 ("One or more readers: the
four columns are filled by the DS lane as a cell ~P issues"; `org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round25P_sweep3_4.md`
@dd4c69b696); the issuer's reader census at the cut (decomposition section 24: 19 first-party code files name `twr_daily`, 2 of them
definitions -- the census is the trigger, its list is in the section) | **Decomp cell:** `IB-pr-263` (decomposition section 24) |
**outcome_ref:** FWD-3 (49F, the retiring engine's table stays sound for every reader until it retires) | **depends_on:** none

---

## WORKER FACE

**The cell.** Row S219 (surprise channel, `IRPT_BCKEND-S219`, re-minted from `W61-S2`): in the live 49F table
`s3://opal-data-49financial/gold/advi/canonical/twr_daily/` (bucket from `lib.opal_naming.lookup('49financial')`, never typed), two of
559 partitions -- `date=2024-07-08` (the engine's first day) and `date=2025-01-09` -- carry `schema_version` 1.2 like every neighbour but
are entirely missing `bmv`, `emv`, `cf_net`, `cf_gross`. Their neighbours (`date=2024-07-09`, `date=2025-01-08`, `date=2025-01-10`) carry
the full column set at the same schema_version. Measured again at the cut (2026-09-30 14:1xZ): `date=2024-07-08` has 11 columns and
4,074 rows, none of the four. The adapter's engine reader refuses any full-history read that touches either date
(`infra/aws/lambda/investor-reporting/performance/f49_engine.py:134`, "engine table schema changed"), and that guard is kept.

**Your act.** Fill the four columns on exactly those two partitions BY THE PRODUCER'S OWN PATH: the writer of this table is
`data/assets/scripts/gold/runners_49f/c02_twr_engine.py` (your lane under CLAUDE.md rule 13). Re-emit the two days through the
runner as it emits any day (read its own CLI and day selection; `chain_49f_entrypoint.py` is the chain's entry), so the rows are the
producer's arithmetic, not a hand-typed patch. If the producer cannot emit a single historical day, or if it turns out the four columns
were NEVER populated for those two runs by design, do not improvise: write the reason in a surprise row (`IRPT_BCKEND-S<k>`, lane ANY,
append-only), record it in your report, and stop -- the remedy is then a `schema_version` bump the guard can key on, which the CTO
rules. Every other partition stays byte-identical (P26-3-AC1 reads three neighbours' ETags against the BEFORE record).

**Ledger (NEVER-2).** `python .tools/deploy_ledger.py open --slug twr-daily-two-partition-column-fill-20260930 --title "<one line>"
--author 0.4.0_DS_ClientPlatform~S --leg "B1|verify|BEFORE read|the two partitions' column sets and ETags read and recorded"
--leg "W1|activation|re-emit date=2024-07-08 and date=2025-01-09|producer invocation + rc, the two new ETags"
--leg "A1|verify|AFTER read|four columns present on both, neighbours' ETags unchanged"` BEFORE the first S3 write; `close-leg` each with
its proof; `close` at the end. Commit the entry AND the sentinel `org/critical_paths/.open_deploys/twr-daily-two-partition-column-fill-20260930.json`.

**Reference for the shape you must reproduce:** the BEFORE record at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/twr_daily_partition_etags_BEFORE_20260930.json` (read-only).

<criterion id="P26-3-AC1" cell_refs="IB-pr-263"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/p26_3_ac1_twr_daily_gap_filled.py" .</invocation><expect>P26-3-AC1 PASS</expect></criterion>
`P26-3-AC1` -- both gap partitions carry bmv, emv, cf_net, cf_gross plus every base column, with rows; the three neighbours' ETags equal
the BEFORE record. Base: FAIL (`date=2024-07-08` missing the four columns), measured at the cut.

<criterion id="P26-3-AC2" cell_refs="IB-pr-263"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/p26_ledger_closed.py" . twr-daily-two-partition-column-fill-20260930 P26-3-AC2</invocation><expect>P26-3-AC2 PASS</expect></criterion>
`P26-3-AC2` -- the ledger entry for the slug is CLOSED with every leg closed and no sentinel. Base: FAIL (no entry), measured at the cut.

<expected_criteria>P26-3-AC1,P26-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS writes admitted:** the two `twr_daily` partition objects named above, and nothing else in any bucket. No other partition, no
  manifest rewrite beyond what the producer writes for those two days, no Terraform.
- **Refusal clause.** If the producer's own path cannot produce the two days, stop with the row; do not hand-write parquet.

<paths>
data/assets/scripts/gold/runners_49f/
lib/opal_naming.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/twr-daily-two-partition-column-fill-20260930.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 24 (round 26, workstream ~P), cell `IB-pr-263`.
<owned_cells>IB-pr-263</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P26-3-AC1, P26-3-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~S/IRPT_BCKEND.TO-IB-pr-263.twr-daily-two-partition-column-fill.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P26-3-AC1 P26-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO~P` (one message, under 150 words): the commit hashes, each criterion's last line, the two new ETags, and
any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule changes; the daily 49F chain is untouched.
comp-iam: DECLARED-NOT-APPLICABLE -- 0 roles touched; the DS runner already writes this prefix.
comp-blast: RUN -- two parquet objects in one gold table; readers at HEAD: f49_engine.py (guarded read), perfrp_emit_core/perfrp_rollup (r_net), c04_validation_battery, parity_period_returns, holdings_performance.py -- the fill ADDS columns the schema declares and changes no existing value.
comp-routes: DECLARED-NOT-APPLICABLE.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- P26-3-AC1 base FAIL (four columns absent on date=2024-07-08, 11 columns / 4,074 rows); P26-3-AC2 base FAIL (no entry); the ledger check's positive control on the CLOSED W24 entry PASS.
seating: 0.4.0_DS_ClientPlatform~S holds no other project (one project per Tier-2 instance); spawned by the issuer under /mstr-spawn in the issuance turn.
lane: the <paths> block IS the grant.
</preflight>
