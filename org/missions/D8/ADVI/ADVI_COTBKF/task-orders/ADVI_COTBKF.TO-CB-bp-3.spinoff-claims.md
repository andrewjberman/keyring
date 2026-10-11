# TO ADVI_COTBKF.TO-CB-bp-3.spinoff-claims -- round 68 CB-bp-3: the four spin-off events: the reconstruction with the factor and without it, against the custodian's own price; a claim per event

<to_id>ADVI_COTBKF.TO-CB-bp-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~103</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bp-3` (`decompositions/ADVI_COTBKF_DECOMP.round68.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_68_20261011.md` section 2 item 2 (the ruling, word for word); the round-67 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~100/ADDED_SPLITS.json` and its `.md` (the four events and the
evidence already gathered); row ADVI_COTBKF-D2-W100-S1; `data/assets/scripts/silver/commonwealth_daily_valuation.py` (`split_plan`,
`apply_splits`, `as_traded_store`, and the docstring near line 860 on scaling closes before a confirmed split to as-traded);
`data/assets/scripts/analysis/commonwealth_price_census.py` lines 50 to 75 (the stores, and its comment that the custodian's mark on a
held position is a close for that security on that day).

**The ruling you serve.** "For each of the four events, on the dates before the event where an account held the security, the
reconstructed close WITH the factor and WITHOUT it is set beside the custodian's price. The factor is applied for an event if and only
if it is the one that reproduces the custodian's price. ... An event with no held date to compare on is left UNAPPLIED and named. No
vendor is asked; this reads what is held."

The four events (CUSIP, date, factor): 00206R102, 2022-04-11, 1.324; 438516106, 2025-10-30, 1.061; 460146103, 2021-10-01, 1.056;
717081103, 2020-11-17, 1.054.

**Your item.**

1. **Which print is the custodian's own price, and when does it exist?** Establish, from the code and the local price caches
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3/price_cache/`, read-only), which store carries the CUSTODIAN'S price on a held position (not a vendor's close), its
   `source` values, and its first and last date. Say plainly which store you take as the custodian's print and why; if a second store
   is a candidate, report both separately and do not merge them. The CTO's rule needs the custodian's price on dates BEFORE each
   event: say for each event how many such dates exist.
2. **The two reconstructions.** For each event and each date before it on which an account held the security AND the custodian's
   print exists: the build's reconstructed close WITHOUT the factor (the store basis as the build reads it at the served instant's
   pin, `2026-10-09T11:52:52Z`, where these four entries are not in the split store) and WITH the factor (the close times the factor, as
   `apply_splits` scales a close before a confirmed split), each beside the custodian's price. Per event: the dates compared, and
   for each reconstruction the count within 0.5 percent of the custodian's price, the median ratio to it, and the worst ratio.
3. **A claim per event.** `APPLY` (the WITH reconstruction reproduces the custodian's price and the WITHOUT one does not),
   `DO_NOT_APPLY` (the reverse), `UNAPPLIED_NO_HELD_DATE` (no date to compare on: the rule's own outcome, named), `UNDECIDED` (both
   or neither reproduce it: say which and by how much). Do not let the round-67 class decide it: that evidence showed the events are
   real, not which reconstruction matches the custodian.
4. **What the price source's history is already adjusted for** (the CTO says it did not establish this): from the code and the data
   only, is the store's close an adjusted series (adjusted for splits, for dividends, for spin-offs)? Give the evidence you have
   (a known share split in the universe and what the series does across it) and say what is not established.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~103/SPINOFF_CLAIMS.json`. Top-level keys, exactly: `custodian_print` (`{"store", "why", "first_date", "last_date"}`),
   `other_candidate_prints` (a list), `events` (a list of `{"cusip", "event_date", "factor", "held_dates_before_event",
   "dates_compared", "with_factor": {"within_half_percent", "median_ratio", "worst_ratio"}, "without_factor": {...}, "claim",
   "evidence"}`), `source_adjusted_for`, `not_established`.

### ACCEPTANCE

<criterion id="CB68bp3-AC1" cell_refs="CB-bp-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~103/SPINOFF_CLAIMS.json',encoding='utf-8'));e=d['events'];print('SPINOFF-CLAIMS-RECORD events=%d cusips=%s claims=%s dates_compared=%s custodian_print=%s'%(len(e),','.join(sorted(x['cusip'] for x in e)),','.join(x['claim'] for x in sorted(e,key=lambda x:x['cusip'])),','.join(str(x['dates_compared']) for x in sorted(e,key=lambda x:x['cusip'])),d['custodian_print']['store']))"</invocation><expect>SPINOFF-CLAIMS-RECORD events=4 cusips=00206R102,438516106,460146103,717081103</expect></criterion>
`CB68bp3-AC1` -- all four events carry a claim and the count of dates it rests on. The CTO reads the claims.

<criterion id="CB68bp3-AC2" cell_refs="CB-bp-3" judgment="true"/>
`CB68bp3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the print taken as the custodian's is shown to be the
custodian's and not a vendor's; each claim follows from the two reconstructions on the dates listed; an event with no date to compare
on is UNAPPLIED_NO_HELD_DATE, not decided from other evidence.

<expected_criteria>CB68bp3-AC1,CB68bp3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** No vendor is asked: no Yahoo, no Bloomberg, no network call beyond the
  read-only S3 gets the build's own loaders make.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and listings the build already makes are allowed.
  No push. No `--refresh`.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, prices per security, ratios,
  version ids and reason codes only. A build log line that prints `read_account=` is never echoed: filter it out before you read a log.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W103-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round68.md</decomp_doc> (round 68), cell `CB-bp-3`.
<owned_cells>CB-bp-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB68bp3-AC1, CB68bp3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~103/ADVI_COTBKF.TO-CB-bp-3.spinoff-claims.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB68bp3-AC1,CB68bp3-AC2` BEFORE the flip. Mechanical: CB68bp3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** which store is the custodian's print, why, and its date range; any other candidate print, separately; per event: held dates before it, dates compared, the two reconstructions' counts and ratios, the claim; what the price source is adjusted for and the evidence; the `SPINOFF-CLAIMS-RECORD` line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement.
comp-iam: DECLARED-NOT-APPLICABLE local caches and the build's own read-only gets; no vendor call.
comp-adversary: RUN -- the custodian's print must be shown to be the custodian's, with any second candidate kept separate; UNAPPLIED_NO_HELD_DATE and UNDECIDED are legal claims, so a missing comparison is not decided from the round-67 evidence; BLIND: a custodian print that is itself derived from the same vendor series.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-68 analysis @b3a272fffc (msg 5008), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v38 @931dc9ea93.
