# TO IRPT_DASHBD.TO-DB-b-167 -- a stated reason for each of the 12 segments that neither flow convention closes, from a closed list written before the read, each reasoned segment recomputed with its cause corrected and closing within 0.35 pp, the rest UNEXPLAINED per account; a read, no served byte moves

<to_id>IRPT_DASHBD.TO-DB-b-167</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~133</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>89</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6956 (2026-10-13 ~13:47Z), ROUND-89 ANALYSIS @8208cabf27 section 4 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-167` (decomposition section 91) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-166 (drained @39f0418a38 and @f4f25b487e).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-133` (branch `wk-IRPT_DASHBD-133`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/`. Your private folder (client data lives only here, outside the repo) is
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~133/` (create it).

**Why.** The previous cell (`DB-b-166`) computed the tie-out under both flow conventions: Black Diamond's default closes 76 of the 88 flow-bearing gradable stored segments that all-end misses, and
none the other way; 12 segments close under neither. The product's acceptance for the tie-out requires that every day the two systems disagree carries a stated reason, so each of the 12 owes one.
The CTO's ruling: give each of the 12 one reason from a closed list written before the read; show it by a count or a date pair from the stored rows; recompute the segment with that cause corrected and it must
close within 0.35 pp, or it is not a reason and the segment stays UNEXPLAINED.

**The cell (`DB-b-167`).** A read and a private count over worker ~108's stored tables. You change no served code and rule nothing beyond the closed list.
1. **Read the model first.** `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_flow_timing.py` (the previous cell's tracked module: `load`, `relink`, `CONVENTIONS`, the gross formula, the rule that picks the
   88 flow-bearing gradable segments and the 12 that neither convention closes; import it by path, do not edit it) and the earlier classifier
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/class90.py` (the accrual identity `ident` and the accrual-corrected return used there). The stored tables are in
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`: `table90.pkl` (per segment: `a`, `seg` {start, end}, `o` our figures, `b` Black Diamond's, `v2`), `read90.pkl` (`gold[account][date]`
   with `r`, `mv`, `flow`, `inc`, `inc_recv`, `price_reason`; `bd[...]` Black Diamond's points; `txn`, the transaction rows with `trade_date`, `settle_date`, `return_date`, `external_flow`, `income`),
   `members90.pkl`. The trading calendar is `lib/trading_calendar.py`.
2. **The rule FIRST, committed before any read of the 12.** Before you look at the rows of any of the 12 segments, write `RULE.md` in your folder and commit it alone. It states, for each reason on the closed
   list below, so that another seat would count the same way: its TEST (what in the stored rows makes it apply, named by column) and its CORRECTION (the single change made to the recomputation when that cause is
   removed), and that the segment must then close within 0.35 pp under Black Diamond's default convention (the `bd_default` relink of the previous cell; for `BD_ACCRUED_INCOME` the accrual-adjusted return of
   `class90.py`, relinked the same way). You may read CODE and SCHEMAS (column names, vocabularies) to write the rule; you may not look at the 12 segments' rows. If the rule proves unworkable after the read starts, do
   NOT edit it: add a dated `RULE_ADDENDUM.md` and report the count under both readings.
3. **THE CLOSED LIST (fixed by the issuer, in this order; the first reason whose single correction re-closes the segment takes it):**
   `MISSING_PRICE` (a day inside the window with no usable price: `price_reason` set) · `FLOW_ABSENT_ONE_SIDE` (a day with a flow on one system's rows and none on the other's) ·
   `FLOW_ON_NON_TRADING_DAY` (a flow dated on a day that is not a trading day) · `INCOME_OFF_FLOW_DAY` (income recorded on a different day than the other system carries it) ·
   `BD_ACCRUED_INCOME` (Black Diamond's values and gains include accrued income; the dollar identity of `class90.py`) · `UNEXPLAINED`. A reason is SHOWN by a count or by day offsets taken from the stored rows, never asserted.
   A segment closed only by two corrections together is counted `combined_only` and stays `UNEXPLAINED`. No other reason may be used; a cause you think is missing is a surprise row.
4. **The count.** Reproduce the 12 first: with the previous cell's module, 88 flow-bearing gradable segments, 12 closing under neither convention, `uncorrected_closes_among_12` 0. Then, per segment, apply the tests in
   the list's order, apply the correction, recompute, and keep the reason only if it closes at 0.35 pp. Per account, count the segments left UNEXPLAINED. Write ONE new tracked module
   `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_neither_reasons.py` (ASCII, passes `bash .tools/commit-gate.sh`) that does this and prints counts only.
5. **If any segment is UNEXPLAINED**, file ONE surprise row (`spec_asserts` + `world_is`, counts only: the number of UNEXPLAINED segments, the number of accounts, which tests came near) and put its id in
   `surprise_row`; FWD-8 is then unmet for those accounts, and the issuer grades it.
6. **Record** `NEITHER_12_REASONS.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `rule` {`file`: "RULE.md", `sha256` (of its committed bytes), `commit` (the hash that carried it),
   `written_before_count`: true}; `reasons_list` (the six names above, in order); `code` {`file`, `sha256` (of its committed bytes), `tracked`: true}; `population` {`flow_segments`: 88, `neither_segments`: 12,
   `accounts`}; `by_reason` {the six names: int, summing to 12}; `evidence` {for each reason above 0 except UNEXPLAINED: {`kind`: "count" or "day_offsets", `values`: [ints]}}; `corrected` {`reasoned`,
   `closed_within_tolerance`, `demoted_to_unexplained`, `combined_only`} (`reasoned` = 12 minus UNEXPLAINED = `closed_within_tolerance`); `uncorrected_closes_among_12` 0; `unexplained_per_account` [ints, one per
   account with any]; `fwd8_unmet_accounts` (their number); `surprise_row` (only when UNEXPLAINED is above 0); `reads` {`vendor_calls`: 0, `secret_reads`: 0, `s3_writes`: 0}; `served_values_changed`: false;
   `on_a_copy`: true; `limits` (a sentence on what the count cannot say). NO account id, client name, amount, security name or run of eight or more digits in the record or your report: counts, day offsets and words only.

<criterion id="DB89-1-AC1" cell_refs="DB-b-167"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r89/p89_round89.py" . DB89-1-AC1</invocation><expect>DB89-1-AC1 PASS</expect></criterion>
`DB89-1-AC1` -- the rule is written and committed before the read and its bytes are unchanged; the six-name closed list is exactly as above; the code file is tracked and hashes to the stated sha256; the 12 reproduce; the six
counts sum to 12; every reason above zero is shown by a count or day offsets; every reasoned segment closed within 0.35 pp when its cause was corrected (reasoned = closed); the uncorrected control reads 0; the UNEXPLAINED
per account sum to the UNEXPLAINED count and name a surprise row exactly when above zero; zero vendor calls, secret reads and S3 writes; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB89-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. `tieout_flow_timing.py`, the reader of record, `class90.py` and the stored tables are READ ONLY.
- **No vendor call and no secret read.** You run no Black Diamond fetch, read no cookie or credential file, open no browser. Black Diamond's figures come from the stored tables.
- **No served write.** No S3 access (the tables are local), no Lambda, Terraform or IAM act, no deploy, no push.
- **No client data in what you write.** Counts, day offsets and words only. Whatever you derive from the private tables goes nowhere but the private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is
  NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W133-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_neither_reasons.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-167.reasons-for-the-twelve-segments-neither-convention-closes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 91 (round 89), cell `DB-b-167`.
<owned_cells>DB-b-167</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB89-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/IRPT_DASHBD.TO-DB-b-167.reasons-for-the-twelve-segments-neither-convention-closes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB89-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the rule's commit (before the read); the six counts; the number of accounts with UNEXPLAINED segments and the count in each; `combined_only`; what the
evidence for each used reason is (counts or day offsets); the module's commit; any row ids. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access is granted or needed; the stored tables are local.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 23 synthetic arms dry-run) and the analysis names the negative arm.
lane: the <paths> block IS the grant.
</preflight>
