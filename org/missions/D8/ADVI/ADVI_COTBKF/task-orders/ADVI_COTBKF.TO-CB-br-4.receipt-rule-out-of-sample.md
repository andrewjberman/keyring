# TO ADVI_COTBKF.TO-CB-br-4.receipt-rule-out-of-sample -- round 70 CB-br-4: the late-receipt rule tested on accounts held out from the fitting, on method_r29's flows; the 410 by class of receipt

<to_id>ADVI_COTBKF.TO-CB-br-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~114</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-br-4` (`decompositions/ADVI_COTBKF_DECOMP.round70.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_70_20261011.md` section 2 item 5 and section 3 item 4; the round-69 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~109/RESIDUAL_RECEIPT_PREDICATE.json` and its `.md` (the rule:
over the 28 calendar days before, net external outflows O against the prior value B, a full outflow when O / (O + B) is at least 0.99;
the day carries only receipts beside sweeps, a cash withdrawal or foreign tax; reads blank, reason `RECEIPT_AFTER_EXIT`); the round-68
classing it was scored against, `.../0.9.0_WK_ADVI_COTBKF~105/OUTLIERS_ON_A_REAL_BASE.json`.

**The three objections that stand** (the reviewer's, upheld by the CTO): the rule was tested on the days it was fitted to; it reads the
flow column that `method_r29` changes; and it would blank 410 measured days, 10 account-months entirely. "A rule that blanks 410
measured days is adopted on a test it could have failed."

**Your item.**

1. **Reproduce the round-69 result first**, on the served `method_r28` table: 410 measured days blanked; 148 of the 162 target days;
   0 of the other 17. If you cannot, that is the refusal clause.
2. **A test it could fail: hold-out by ACCOUNT.** Split the accounts into two halves by a rule fixed BEFORE you look at any outcome
   (the parity of a hash of the account id: state the hash) so no account is in both. On half A ONLY, re-derive the two constants the
   way round 69 did (the look-back at which the target count stops rising; the share below which most added days are not targets),
   WITHOUT looking at half B. Then apply half A's constants to half B, and state: half B's target days blanked and missed, its
   non-target outlier days blanked, and its total measured days blanked. Then swap the halves and repeat. Report whether the two
   halves choose the same constants, and how the held-out results compare with the in-sample ones. If half A's own evidence does not
   single out a constant, say so: do not carry 28 and 0.99 over by default.
3. **On `method_r29`'s flows.** Re-run the rule (round 69's constants, and each half's) on a `method_r29` build's returns table. One
   built WITH the served hold list is in this worktree's scratch if it is still there (`.scratch/w107/fwd3_hold_method_r29/` and
   `fwd3_hold_method_r28/`: this worktree's own); if not, say so and use the build you can find, stating which. Print: days blanked
   under r28 flows, under r29 flows, and the days that are blanked under one and not the other, with why (which of the 44 flow-changed
   account-days sit in a 28-day window).
4. **The 410 by class of receipt:** income, by type (dividend, interest, reinvested distribution, the others the rule lists); a fee
   refund; a 12b1 credit; a day with more than one. For each: days, days with an absolute return at or below 0.10, account-months
   that lose a measured day, and account-months that lose EVERY measured day (the 10: which class are they).
5. **What a blank costs:** for the blanked days, the sum is not asked; the count of account-months and account-years whose return
   could no longer be chained because a measured day became blank inside them (a count), next to how many already could not.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~114/RESIDUAL_RECEIPT_OUT_OF_SAMPLE.json` and a short `.md`. Top-level keys, exactly: `reproduced` (`{"blanked", "targets_blanked",
   "non_targets_blanked"}`), `holdout` (a list of two `{"fit_half", "constants_chosen", "same_as_round_69", "test_half_targets",
   "test_half_targets_blanked", "test_half_non_targets_blanked", "test_half_total_blanked"}`), `on_r29_flows` (`{"build",
   "blanked_r28", "blanked_r29", "only_r28", "only_r29", "why"}`), `by_receipt_class` (a list), `months_losing_every_day`,
   `chain_breaks_added`, `verdict_inputs` (three plain sentences: what the hold-out shows, what the r29 flows change, what the 410
   are; NO recommendation to adopt or not), `not_established`.

### ACCEPTANCE

<criterion id="CB70br4-AC1" cell_refs="CB-br-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~114/RESIDUAL_RECEIPT_OUT_OF_SAMPLE.json',encoding='utf-8'));r=d['reproduced'];h=d['holdout'];o=d['on_r29_flows'];print('RECEIPT-OUT-OF-SAMPLE-RECORD reproduced_blanked=%d reproduced_targets=%d holdouts=%d test_targets_blanked=%s test_non_targets_blanked=%s same_constants=%s blanked_r28=%d blanked_r29=%d receipt_classes=%d months_losing_every_day=%d'%(r['blanked'],r['targets_blanked'],len(h),'+'.join(str(x['test_half_targets_blanked']) for x in h),'+'.join(str(x['test_half_non_targets_blanked']) for x in h),'+'.join(str(x['same_as_round_69']) for x in h),o['blanked_r28'],o['blanked_r29'],len(d['by_receipt_class']),d['months_losing_every_day']))"</invocation><expect>RECEIPT-OUT-OF-SAMPLE-RECORD reproduced_blanked=410 reproduced_targets=148 holdouts=2</expect></criterion>
`CB70br4-AC1` -- round 69's result is reproduced, and the rule is tested on two held-out halves and on `method_r29`'s flows, with the
410 split by class of receipt. The CTO reads whether it could have failed and did not.

<criterion id="CB70br4-AC2" cell_refs="CB-br-4" judgment="true"/>
`CB70br4-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the split was fixed before any outcome was read and no
account is in both halves; each half's constants come from that half's evidence alone; the r29 run uses a build with the served hold
list or says it does not; the record states inputs to a verdict and recommends nothing.

<expected_criteria>CB70br4-AC1,CB70br4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids and reason codes only. A build log line carrying `read_account=` is never echoed.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W114-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round70.md</decomp_doc> (round 70), cell `CB-br-4`.
<owned_cells>CB-br-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB70br4-AC1, CB70br4-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~114/ADVI_COTBKF.TO-CB-br-4.receipt-rule-out-of-sample.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB70br4-AC1,CB70br4-AC2` BEFORE the flip. Mechanical: CB70br4-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the reproduced round-69 counts; the split rule and each half's size; the constants each half chooses and whether they are round 69's; the held-out results beside the in-sample ones; the r28 against r29 flow comparison and which build was used; the 410 by class of receipt; the account-months losing every measured day and their class; the chain breaks added; the three verdict-input sentences; the `RECEIPT-OUT-OF-SAMPLE-RECORD` line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the split is by account and fixed by a stated hash before any outcome is read; each half derives its own constants and may fail to single one out; the rule is re-run on r29 flows from a build with the served hold list; the record is barred from recommending; BLIND: the target labels on both halves are one worker's classing, 102 of 179 placed by rule.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-70 analysis @991f749df1 (msg 5340), section 3 item 4; PRD ADDENDUM v0.7 @72d624cd26; `3.0.0_SA_CVO` REMEDIATION_v40 @90e1a7cbda.
