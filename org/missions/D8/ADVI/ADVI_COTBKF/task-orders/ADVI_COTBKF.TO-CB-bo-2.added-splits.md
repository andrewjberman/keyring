# TO ADVI_COTBKF.TO-CB-bo-2.added-splits -- round 67 CB-bo-2: the splits the grown store added: which move a price, and whether each is real and dated before the days it moves

<to_id>ADVI_COTBKF.TO-CB-bo-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~100</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>67</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bo-2` (`decompositions/ADVI_COTBKF_DECOMP.round67.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code.**

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json`; row ADVI_COTBKF-D2-W97-S1 in the channel; `data/assets/scripts/silver/commonwealth_daily_valuation.py`
lines 465 to 580 (`SPLIT_STORE`, `load_store_splits`, `split_plan`, `apply_splits`: how a store split is confirmed, applied, left
unapplied or counted a disagreement).

**Why.** The split-history store the build reads has grown since the served run: 141 CUSIPs the accounts hold are listed today against
32 then. A `method_r28` re-run today moves 30 account-days (28 returns in one account over 2020-10-12 to 2020-11-18; 2 blank reasons),
3,034 price points over 4 CUSIPs. The CTO will re-mint those days too, NAMED, only if the added splits are real and dated before the
days they move. You establish that.

**Your item.**

1. **What was added, and when.** List the object versions of the store's `splits.parquet` partitions (the address is
   `lib/opal_naming` output for `("yahoo", "global", "silver", "price_history")`, as `load_store_splits` builds it; the bucket has
   versioning enabled). For the CUSIPs the accounts hold: which were listed at the served run's instant (find it from the round-34
   run's log or `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/fwd3_manifest.json`; expect 32) and which were added after (expect 109); for each added one,
   the instant its first version landed and how many split events it carries. Also: did any of the 32 CHANGE content since?
2. **Which of them move anything.** Using the control run's outputs if they are still on this box
   (`C:/dev/wk-cotbkf-80/.scratch/w97/r28*`, READ-ONLY; they are another worker's scratch, never write there) or your own run of
   `split_plan` on local inputs: of the added CUSIPs, how many have a split the build APPLIES, how many it leaves unapplied, how many
   are disagreements, and which CUSIPs account for the 3,034 changed price points (expect 4).
3. **Are those splits real, and dated before the days they move?** For each CUSIP that changes a price: the split date and ratio in
   the store; the first and last date of the price points it changes; and independent evidence the split happened on that date at that
   ratio: the custodian's own rows for the security (a split or stock-dividend transaction type, or a quantity step of that ratio in
   the silver transactions `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/`), and the as-traded closes either side of the date (the price ratio across it). Class
   each: `REAL_AND_BEFORE` (confirmed by an independent source, and every moved day is on or after... state precisely which side of
   the split date the moved days lie and whether that is the side a correct adjustment moves), `REAL_BUT_MISAPPLIED`,
   `NOT_CONFIRMED`, `CONTRADICTED`.
4. **The 30 account-days.** By CUSIP and by class from step 3: how many of the 28 changed returns and the 2 changed blank reasons
   each accounts for. The dates, written to `DRIFT_DATES.csv` (columns: date, account_days_drifted, cusips; no account column).
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~100/ADDED_SPLITS.json`. Top-level keys, exactly: `served_as_of` (the instant and its evidence), `held_listed_then`,
   `held_listed_now`, `added`, `changed_among_the_original`, `added_applied`, `added_unapplied`, `added_disagreements`,
   `price_moving_cusips` (a list of `{"cusip", "split_date", "ratio", "first_moved_date", "last_moved_date", "price_points",
   "class", "evidence"}`), `drift_account_days` (`{"returns": n, "blank_reasons": n}`), `drift_by_class`, `not_established`.

### ACCEPTANCE

<criterion id="CB67bo2-AC1" cell_refs="CB-bo-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~100/ADDED_SPLITS.json',encoding='utf-8'));m=d['price_moving_cusips'];print('ADDED-SPLITS-RECORD held_listed_then=%d held_listed_now=%d added=%d price_moving_cusips=%d price_points=%d drift_returns=%d drift_blank_reasons=%d classes=%s'%(d['held_listed_then'],d['held_listed_now'],d['added'],len(m),sum(x['price_points'] for x in m),d['drift_account_days']['returns'],d['drift_account_days']['blank_reasons'],sorted(set(x['class'] for x in m))))"</invocation><expect>ADDED-SPLITS-RECORD held_listed_then=32 held_listed_now=141 added=109</expect></criterion>
`CB67bo2-AC1` -- the then and now listings are the measured ones and every price-moving CUSIP carries a class. The CTO reads the classes.

<criterion id="CB67bo2-AC2" cell_refs="CB-bo-2" judgment="true"/>
`CB67bo2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each class rests on evidence independent of the store
(the custodian's rows or the traded prices), not on the store agreeing with itself; "dated before the days they move" is shown per
CUSIP with its dates; an unconfirmed split is called unconfirmed.

<expected_criteria>CB67bo2-AC1,CB67bo2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and version listings of the split store are allowed.
  No push.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json`
  in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow or return. Counts, dates, CUSIPs, ratios, version ids and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written (for example the listing then or now is not 32 or 141), stop. Write the
  reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W100-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read
  from the clock, APPENDED to the channel file (append mode; `git diff --numstat` must show added lines only).

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round67.md</decomp_doc> (round 67), cell `CB-bo-2`.
<owned_cells>CB-bo-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB67bo2-AC1, CB67bo2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~100/ADVI_COTBKF.TO-CB-bo-2.added-splits.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB67bo2-AC1,CB67bo2-AC2` BEFORE the flip. Mechanical: CB67bo2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the served run's instant and its evidence; listed then, now, added, and any change among the original 32; applied, unapplied, disagreements among the added; each price-moving CUSIP with its split date, ratio, moved dates, class and evidence; the 30 account-days by class; the `ADDED-SPLITS-RECORD` line; what is not established; a statement that nothing was written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and version listings on a bucket this build already reads; BLIND: comp-iam was not run by the issuer; a denied version listing is the refusal clause.
comp-adversary: RUN -- the then and now listings are pinned to the measured 32 and 141; a split is called real only on evidence independent of the store; NOT_CONFIRMED and CONTRADICTED are legal classes; BLIND: a corporate action the custodian's rows do not show and the traded prices do not make visible.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4844 (2026-10-11 11:43Z), items 1 and 3; row ADVI_COTBKF-D2-W97-S1; `deliverables/0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json`.
