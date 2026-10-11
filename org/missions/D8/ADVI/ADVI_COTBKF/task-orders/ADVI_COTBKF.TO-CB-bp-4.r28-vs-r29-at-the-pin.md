# TO ADVI_COTBKF.TO-CB-bp-4.r28-vs-r29-at-the-pin -- round 68 CB-bp-4: method_r29 against the served table at the served instant's pin; the dates a re-mint would replace

<to_id>ADVI_COTBKF.TO-CB-bp-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~104</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bp-4` (`decompositions/ADVI_COTBKF_DECOMP.round68.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bp-1, CB-bp-3

---

## WORKER FACE

### THE CELL

**RULE: counts, dates, month labels, reason codes and rule names only.** Never an account id, never an account's value, flow or
return.

**This is a MEASUREMENT. It writes NOTHING remote. It runs the chain from YOUR worktree, a clean checkout, with no file from another
worktree's scratch on any command line.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_68_20261011.md` sections 1, 2 item 1 and 3 item 4; the round-66 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/R28_VS_R29.json` and its `.md` (the same comparison on today's
store: 2 account-days); `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json` (the pin and Proof A's commands); the round-68 records of CB-bp-1 (`.../0.9.0_WK_ADVI_COTBKF~101/
CLEAN_CHAIN.json`: how the chain now runs clean) and CB-bp-3 (`.../0.9.0_WK_ADVI_COTBKF~103/SPINOFF_CLAIMS.json`).

**Why.** The withholding rule's effect was measured on today's split store, which has grown since the table was served. The served
table was built at `2026-10-09T11:52:52Z`. The list of dates a re-mint replaces must be stated against the SERVED table, at that pin.

**Your item.**

1. **Control.** Run the `method_r28` chain at `--split-store-as-of 2026-10-09T11:52:52Z` with the served build's settings. Its daily returns
   equal `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` on (account, date, return, blank_reason): 1,691,729 rows, 0 differing.
   If not, STOP: refusal clause.
2. Run `method_r29` at the same pin, same settings. The two runs print the same `SPLIT-STORE-PIN` line and equal
   `after/security_day_price.parquet`.
3. Compare r29 with the SERVED table on (account, date): the eight classes of round 66 (`both_measured_same`,
   `both_measured_different`, `measured_served_only`, `measured_r29_only`, `both_blank_same_reason`, `both_blank_reason_changed`,
   `row_served_only`, `row_r29_only`), summing to the union; the changed account-days by origin (a withholding day with no withdrawal
   row; another day of the same account; another account); month verdicts changed; ABSENT changed.
4. **The spin-off result applied.** Read CB-bp-3's claims. At this pin the four events are NOT in the split store (it lists 32
   partitions; they landed a day later): confirm that from your run's log, and state plainly that the claims change nothing at this
   pin. Do not build a mechanism to apply them.
5. `CHANGED_DATES_AT_PIN.csv` (columns: date, account_days_changed; no account column): the dates a re-mint under `method_r29` at
   this pin would replace, stated against the served table.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~104/R28_VS_R29_AT_PIN.json`. Top-level keys, exactly: `pin` (`{"as_of", "listed", "held", "sha256"}`), `control` (`{"rows",
   "differing"}`), `inputs_equal`, `rows_union`, `classes`, `changed_account_days`, `changed_dates`, `changed_by_origin`,
   `month_verdicts_changed`, `month_absent_changed`, `spinoff_events_in_store_at_pin`, `same_dates_as_round_66` (true | false, with
   the difference if false), `not_established`.

### ACCEPTANCE

<criterion id="CB68bp4-AC1" cell_refs="CB-bp-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~104/R28_VS_R29_AT_PIN.json',encoding='utf-8'));c=d['classes'];print('R28-VS-R29-AT-PIN-RECORD as_of=%s listed=%d control_rows=%d control_differing=%d rows_union=%d class_sum=%d changed_account_days=%d changed_dates=%d spinoff_events_in_store_at_pin=%d'%(d['pin']['as_of'],d['pin']['listed'],d['control']['rows'],d['control']['differing'],d['rows_union'],sum(c.values()),d['changed_account_days'],d['changed_dates'],d['spinoff_events_in_store_at_pin']))"</invocation><expect>R28-VS-R29-AT-PIN-RECORD as_of=2026-10-09T11:52:52Z listed=32 control_rows=1691729 control_differing=0</expect></criterion>
`CB68bp4-AC1` -- at the served instant's pin the control reproduces the served table and the comparison is recorded with its classes
summing to the union.

<criterion id="CB68bp4-AC2" cell_refs="CB-bp-4" judgment="true"/>
`CB68bp4-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the list is stated against the served table at the
served instant's pin; the two runs differ in the rule only; the chain ran from a clean checkout; every changed day is traced to its
origin or called unexplained.

<expected_criteria>CB68bp4-AC1,CB68bp4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and listings the build already makes are allowed.
  No push. No `--refresh`.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, prices per security, ratios,
  version ids and reason codes only. A build log line that prints `read_account=` is never echoed: filter it out before you read a log.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W104-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round68.md</decomp_doc> (round 68), cell `CB-bp-4`.
<owned_cells>CB-bp-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB68bp4-AC1, CB68bp4-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~104/ADVI_COTBKF.TO-CB-bp-4.r28-vs-r29-at-the-pin.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB68bp4-AC1,CB68bp4-AC2` BEFORE the flip. Mechanical: CB68bp4-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the commands and durations of the two runs; the control line; both `SPLIT-STORE-PIN` lines; the `R28-VS-R29-AT-PIN-RECORD` line; the eight class counts; changed account-days by origin; the changed dates (count, first, last) and whether they are round 66's; month verdicts and ABSENT changed; the spin-off events in the store at this pin; a statement that the chain ran from a clean checkout and nothing was written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a hand-run local re-derivation.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and version listings on stores this build already reads; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- the control (r28 at the pin equals the served table) gates the comparison; both runs must print one pin line; the list is stated against the served table, not against a same-day re-run; the cell is held until the clean-chain and spin-off cells drain; BLIND: the served S3 objects are not re-read, the comparison is against their local copy.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-68 analysis @b3a272fffc (msg 5008), section 3 item 4; `3.0.0_SA_CVO` REMEDIATION_v38 @931dc9ea93.
