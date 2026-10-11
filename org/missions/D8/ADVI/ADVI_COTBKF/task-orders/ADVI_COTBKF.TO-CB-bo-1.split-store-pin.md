# TO ADVI_COTBKF.TO-CB-bo-1.split-store-pin -- round 67 CB-bo-1: the build reads the split store at a named instant and records it; the served table is reproducible again

<to_id>ADVI_COTBKF.TO-CB-bo-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~99</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>67</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bo-1` (`decompositions/ADVI_COTBKF_DECOMP.round67.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json` (what moved and by how much); row ADVI_COTBKF-D2-W97-S1 in the channel;
`data/assets/scripts/silver/commonwealth_daily_valuation.py` lines 465 to 500 (`SPLIT_STORE`, `load_store_splits`), the `store_as_of`
parameter near line 847 and the `main` near lines 905 to 945; how `commonwealth_sweep_regrade.py` and `commonwealth_fwd3_serve.py` call
the split load (`store_splits`), and what `fwd3_manifest.json` records (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/fwd3_manifest.json`; the served run's
logs sit beside the round-34 worker's deliverables).

**The defect.** The build reads dell1's split-history store (`lib/opal_naming` address of `("yahoo", "global", "silver",
"price_history")`, one `cusip=<CUSIP>/splits.parquet` each) LIVE, at whatever it holds when the build runs, and records nothing about
what it read. The store has grown: it lists 141 CUSIPs the accounts hold today against 32 in the served run's log. So a `method_r28`
re-run today differs from the served table on 30 of 1,691,729 account-days, with no code change. A served table that cannot be
reproduced from its own recorded inputs is the finding. The bucket has object versioning ENABLED (issuer read, 2026-10-11).

**Your item.**

1. **Read at a NAMED state.** Give the split load an `as_of` (a UTC instant): for each CUSIP partition, the version of
   `splits.parquet` that was CURRENT at that instant (the newest version whose LastModified is at or before it; a partition whose
   first version is later, or whose current entry at that instant is a delete marker, is NOT listed). Read it by its VersionId. Expose
   it on every entry point that loads the store (`commonwealth_daily_valuation.py`, `commonwealth_sweep_regrade.py`, and
   `commonwealth_fwd3_serve.py` where it re-derives) as `--split-store-as-of <ISO-8601 UTC>`. **Without the flag the build REFUSES**
   to read the split store (`REFUSED: the split store is read only at a named instant; pass --split-store-as-of`): an unpinned read
   is the defect, so it does not stay as a default. If an existing `store_as_of` parameter already carries part of this, build on it
   and say what it did before.
2. **Record what was read.** `fwd3_manifest.json` gains `split_store`: the address, the `as_of`, the CUSIPs listed and held, and a
   sha256 over the sorted `(cusip, version_id)` pairs read. The run's log prints the same on one line beginning `SPLIT-STORE-PIN`.
   (The mint adapter copies this into the mint's manifest in the re-mint order; you do not edit the adapter.)
3. **Tests** (synthetic, a faked versioned bucket): a version written after `as_of` is not read; a partition created after `as_of` is
   not listed; a delete marker current at `as_of` hides the partition; without the flag the load refuses; two loads at the same
   `as_of` return the same pairs and the same digest.
4. **Proof A -- the served table is reproducible again.** Find the instant the served run read the store (the round-34 run's own log
   or manifest time; say which you used and why). Run the `method_r28` chain with the served build's settings (the commands are in
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json`) and `--split-store-as-of` that instant. Its daily returns must equal `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` on
   (account, date, return, blank_reason): 1,691,729 rows, 0 differing; and its log must list 32 held CUSIPs. If it does not, do not
   tune the instant to fit: report the differing count at the instant the evidence gives, and at most two neighbouring instants you
   can justify from the evidence.
5. **Proof B -- two runs at one pin agree.** Run the valuation step (not the whole chain) twice at one `as_of` of TODAY, at least
   20 minutes apart, and show `security_day_price.parquet` and the `SPLIT-STORE-PIN` line are identical. (The CTO's wording is "an
   hour apart"; say how far apart yours were. The issuer re-runs it later for the hour.)
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json`. Top-level keys, exactly: `flag`, `refuses_without_flag`, `served_as_of` (the instant and its evidence),
   `proof_a` (`{"rows", "differing", "held_cusips"}`), `proof_b` (`{"as_of", "minutes_apart", "price_rows_equal", "pin_digest_equal"}`),
   `today` (`{"as_of", "listed", "held", "digest"}`), `tests_added`, `tests_changed`, `not_established`.

### ACCEPTANCE

<criterion id="CB67bo1-AC1" cell_refs="CB-bo-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB67bo1-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB67bo1-AC2" cell_refs="CB-bo-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json',encoding='utf-8'));a=d['proof_a'];b=d['proof_b'];print('SPLIT-STORE-PIN-RECORD refuses_without_flag=%s proof_a_rows=%d proof_a_differing=%d proof_a_held=%d proof_b_price_rows_equal=%s proof_b_digest_equal=%s proof_b_minutes_apart=%d'%(d['refuses_without_flag'],a['rows'],a['differing'],a['held_cusips'],b['price_rows_equal'],b['pin_digest_equal'],b['minutes_apart']))"</invocation><expect>SPLIT-STORE-PIN-RECORD refuses_without_flag=True proof_a_rows=1691729 proof_a_differing=0 proof_a_held=32 proof_b_price_rows_equal=True proof_b_digest_equal=True</expect></criterion>
`CB67bo1-AC2` -- an unpinned read refuses; at the served run's instant the served table is reproduced row for row with 32 held CUSIPs;
two runs at one pin agree.

<expected_criteria>CB67bo1-AC1,CB67bo1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** the mint adapter (`commonwealth_account_return_daily.py`), `commonwealth_flows.py`, any manifest already committed,
  anything under `data/assets/scripts/gold/` or `lib/`. You do not write to the split store or ask for anything of its owner.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and version listings of the split store are allowed.
  No push.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json`
  in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow or return. Counts, dates, CUSIPs, ratios, version ids and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W99-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file (append
  mode; `git diff --numstat` must show added lines only). **Proof A failing at the instant the evidence gives IS a finding to report
  under this clause, not a reason to search for an instant that passes.**

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/analysis/commonwealth_price_census.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round67.md</decomp_doc> (round 67), cell `CB-bo-1`.
<owned_cells>CB-bo-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB67bo1-AC1, CB67bo1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/ADVI_COTBKF.TO-CB-bo-1.split-store-pin.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB67bo1-AC1,CB67bo1-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the flag and where it is accepted; the refusal text without it; the served run's instant and the evidence for it; Proof A (rows, differing, held CUSIPs) with its commands and durations; Proof B (as_of, minutes apart, equal or not); today's pin line; tests added and changed, by name; the diff stat and the diff of `load_store_splits`; the pytest line; the `SPLIT-STORE-PIN-RECORD` line; a statement that nothing was written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a hand-run build; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and version listings on a bucket this build already reads; whether the dell2 identity may list object versions there is NOT established and the cell reports it if denied; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- Proof A is the positive control that failed in round 66, now at a named instant, and tuning the instant to fit is barred; an unpinned read refuses, so the defect cannot return as a default; Proof B shows determinism at one pin; BLIND: a version expired by a lifecycle rule would make an old instant unreadable, which the cell would see as a missing version.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4844 (2026-10-11 11:43Z), items 1 and 3; row ADVI_COTBKF-D2-W97-S1; `deliverables/0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json`.
