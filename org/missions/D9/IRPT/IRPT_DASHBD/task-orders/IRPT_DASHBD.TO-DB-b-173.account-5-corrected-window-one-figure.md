# TO IRPT_DASHBD.TO-DB-b-173 -- ONE figure: account 5's window return after its 4 reasoned days are corrected (its 3 UNEXPLAINED days stay as served), against 0.35 pp; local stored files only; a direct act

<to_id>IRPT_DASHBD.TO-DB-b-173</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~139</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>93</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7081, ROUND-93 ANALYSIS section 3 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-173` (decomposition section 95) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-172 (drained @ab1112493b).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-139` (branch `wk-IRPT_DASHBD-139`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~139/`. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~139/` (create it).

**Why.** Round 92 left three windows open. Account 5 (the fifth of the round-90 plan order) has 7 differing days: 4 taken by `BD_EXCLUDES_SERVED_INCOME`, 3 UNEXPLAINED, each under 0.07 pp. PRD 11b: a window inside 0.35 pp after its reasoned days are corrected meets the clause and its remaining days are not graded one by one. Round 92's record prints only whether a window is closed with no UNEXPLAINED day,
not the window figure. The CTO asks for that one number.

**The cell (`DB-b-173`).** ONE figure, from stored LOCAL files. No S3 access, no vendor call, no credential.
1. **Method, unchanged:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/RULE_EXCL.md` (read-only; bound by hash; do not copy it, do not write a new rule). Section 2 gives the new reason's TEST and CORRECTION for a day; section 5 gives the window method: `G` (the gross window figure of round 90), `s'(d)` = the corrected return on each day taken by a
   served-side correction and `s(d)` otherwise, `R_c` = the product over the compared days of `(1 + s'(d)) - 1`, `G_c = G` here (no Black Diamond-side correction is taken for this account). The window gap is `|G_c - R_c| * 100` in pp.
2. **Inputs (private, read-only):** the issuer's pull `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~134/` (`DAY_READ_PLAN.json`: the fifth request is account 5; `pull/series_04.json`: Black Diamond's daily series for it), the stored tables `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/` (`read90.pkl`: the gold series), and the modules
   `deliverables/0.9.0_WK_IRPT_DASHBD~138/excl_income.py`, `~136/day_reasons.py`, `tieout/tieout_day_read.py` and `tieout/tieout_neither_reasons.py` (read-only; import by path whatever helps; do not edit them).
3. **Write ONE new tracked module** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~139/acct5_window.py` (ASCII, passes `bash .tools/commit-gate.sh`; run under `python -I`; prints COUNTS and the two gaps only). It reproduces round 92's classification of account 5's 7 differing days (4 taken by the new reason, 3 UNEXPLAINED; assert it, else stop),
   corrects the 4 reasoned days exactly as RULE_EXCL.md section 2 does, leaves the 3 UNEXPLAINED days as served, and prints: `uncorrected_gap_pp` (`|G - R0| * 100`, the negative arm; it must be above 0.35) and `corrected_gap_pp` (`|G_c - R_c| * 100`).
4. **Record** `ACCOUNT5_CORRECTED_WINDOW.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `rule` {`file`: "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/RULE_EXCL.md", `sha256` (of its bytes), `reused_unchanged`: true}; `code` {`file`, `sha256` (of its committed bytes), `tracked`: true}; `account_index_plan_order` 5; `reasoned_days` 4; `unexplained_days` 3;
   `uncorrected_gap_pp`; `corrected_gap_pp`; `inside_tolerance` (true exactly when `corrected_gap_pp` is at most 0.35); `reads` {`vendor_calls`: 0, `secret_reads`: 0, `s3_writes`: 0, `s3_reads`: 0}; `served_values_changed`: false; `limits` (one sentence: the figure is a recomputation, not a statement of which system is right). NO account id, client name, amount, date or run of eight or more digits. Report the two gaps to four decimals.

<criterion id="DB93-1-AC1" cell_refs="DB-b-173"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r93/p93_round93.py" . DB93-1-AC1</invocation><expect>DB93-1-AC1 PASS</expect></criterion>
`DB93-1-AC1` -- the record exists with the keys above; the rule is round 92's, unchanged, bound by hash; the code is tracked and hashes to the stated sha256; the reasoned and unexplained day counts equal round 92's committed record for the fifth account (4 and 3); the uncorrected gap is above 0.35 pp; the corrected gap differs from it and `inside_tolerance` equals (corrected gap at most 0.35);
zero vendor calls, secret reads, S3 reads and writes; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB93-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No S3, no vendor call, no credential.** Local stored files only. You never run `tieout_day_read.py pull` and never open a browser.
- **No client data in what you write.** Two gaps in pp and counts only in the repo; nothing derived from the private files goes anywhere but your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W139-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~139/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-173.account-5-corrected-window-one-figure.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 95 (round 93), cell `DB-b-173`.
<owned_cells>DB-b-173</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB93-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~139/IRPT_DASHBD.TO-DB-b-173.account-5-corrected-window-one-figure.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB93-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the two gaps to four decimals; whether the corrected gap is inside 0.35 pp; the module's commit; any row ids. Counts and the two gaps only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one figure from stored local files; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access is granted or needed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 19 synthetic arms dry-run) and its negative arm is the uncorrected gap above 0.35 pp.
lane: the <paths> block IS the grant.
</preflight>
