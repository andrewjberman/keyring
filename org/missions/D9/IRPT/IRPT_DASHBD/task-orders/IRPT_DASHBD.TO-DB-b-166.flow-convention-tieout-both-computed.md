# TO IRPT_DASHBD.TO-DB-b-166 -- the tie-out decided by computing: over the stored tie-out set, relink every flow segment under Black Diamond's published default (additions at the start of the day, the rest at the end) and under all flows at the end, grade each at 0.35 pp, and let a rule written before the count name the convention; a read, no served byte moves

<to_id>IRPT_DASHBD.TO-DB-b-166</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~132</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>88</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6931 (2026-10-13 ~13:11Z), ROUND-88 ANALYSIS @e53edd32d7 section 4 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-166` (decomposition section 90) | **outcome_ref:** FWD-8 / C-FLOWTIME | **depends_on:** none open (reads worker ~108's stored tables).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-132` (branch `wk-irpt-dashbd-88-132`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~132/`. Your private folder (client data lives only here, outside the repo) is
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~132/`.

**Why.** Black Diamond publishes its default flow timing: a positive net addition is weighted at the START of its day; a withdrawal, or a day with no net addition, at the END (help
article 97, learn.bdreporting.com, "Calculations: Performance Calculations"); the alternative, on request, is all flows at the end of the day. The served system links every flow at the END.
Nothing published says which one the firm's accounts use. The CTO: recompute under BOTH, compare each to Black Diamond's reported return for the same segments, grade at 0.35 pp; the one that
ties is measured as the firm's; if neither or both, report it. Black Diamond's reported returns are already stored in the tables below: you make NO vendor call.

**The cell (`DB-b-166`).** A read and a private count. You change no served code and rule nothing beyond the declared rule.
1. **Read the model first.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~127/flowtime_count.py` already loads worker ~108's stored tables
   (`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`: `members90.pkl`, `read90.pkl`, `table90.pkl`), relinks each segment under START, MID and END, forms the
   gross vendor figure `(1 + bdr) * (1 + fees/mean) - 1`, ties it at TOL_PP 0.35 and names the 51 contested segments (`mem["FLOW_TIMING_CONVENTION_DOLLARS_TIE"]`). Read it and
   `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py` (the reader of record: conventions "end" and "start", GUARD_FRAC 2 percent, LARGE_FLOW 25 percent, the fee rules). Reuse their
   rules as they are; do not edit either file.
2. **Write ONE new tracked module** `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_flow_timing.py` (ASCII, passes `bash .tools/commit-gate.sh`). It defines the relink under two conventions:
   `end` (every flow at the end of its day: r = (V_t - F_t) / V_(t-1) - 1) and `bd_default` (a day whose net flow F_t is greater than zero is linked at the START, r = V_t / (V_(t-1) + F_t) - 1; a
   day with F_t zero or negative is linked at the END as above). Use the same day set, the same first-day and missing-value handling and the same guard as `flowtime_count.py` and the reader of
   record, and state each such choice in the module's docstring. It reads the stored tables by the paths above and prints COUNTS ONLY.
3. **The declared rule (fixed before the count; you do not change it).** Over the FLOW-BEARING, GRADABLE segments (a segment with at least one day whose served flow is non-zero and whose Black
   Diamond figure is present): a segment CLOSES under a convention when its relinked gross return is within 0.35 pp of the vendor figure. `both` = closes under both; `only_bd_default`
   = under `bd_default` and not `end`; `only_end` = under `end` and not `bd_default`; `neither`. Verdict: `BD_DEFAULT` iff only_end is 0 and only_bd_default is at least 1; `END` iff only_bd_default
   is 0 and only_end is at least 1; `BOTH_TIE_INDISTINGUISHABLE` iff both are 0; `MIXED_NEITHER_DECIDES` iff both are above 0. Compute the same four counts for the contested 51 alone.
4. **Controls (reproduced by your module, not copied).** Under the existing START relink the contested 51 close 50 of 51; under END 0 of 51. Report both as `controls`
   {`start_within_contested_51`, `end_within_contested_51`}; a result other than 50 and 0 means your machinery differs from the reader of record: stop and file a row, do not adjust to fit.
5. **Negative arm.** For `BD_DEFAULT` or `END`, `negative_arm` is true (the convention not chosen misses at least one flow segment the chosen one hits, which the rule already requires). For
   `BOTH_TIE_INDISTINGUISHABLE` or `MIXED_NEITHER_DECIDES` it is false, and you file ONE surprise row (`spec_asserts` + `world_is`, counts only) naming the verdict, and put its id in
   `surprise_row`. If the stored set cannot decide (both ties, none to compare), say so in the row: the issuer decides about widening the window or a vendor read; you take neither step.
6. **Record** `FLOW_CONVENTION_TIEOUT.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `conventions` {`bd_default` {`rule`, `source`}, `end` {`rule`, `source`}} with
   `bd_default.source` naming "learn.bdreporting.com article/97" and `end.source` naming the served behaviour; `code` {`file` (the tracked module above), `sha256` (of its committed
   bytes), `tracked`: true}; `population` {`flow_segments`, `contested_51`: 51}; `crosstab_flow` and `crosstab_contested_51` {`both`, `only_bd_default`, `only_end`, `neither`}, each summing to its
   population; `controls`; `verdict`; `negative_arm`; `surprise_row` (only when owed); `reads` {`vendor_calls`: 0, `secret_reads`: 0, `s3_writes`: 0}; `served_values_changed`: false;
   `limits` (a sentence on what the count cannot say: it describes these stored segments and the two named conventions, not any other timing).
   NO account id, client name, amount, security name or run of eight or more digits in the record or your report: counts and words only.

<criterion id="DB88-1-AC1" cell_refs="DB-b-166"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r88/p88_round88.py" . DB88-1-AC1</invocation><expect>DB88-1-AC1 PASS</expect></criterion>
`DB88-1-AC1` -- the record exists with the keys above, its code file is tracked and hashes to the stated sha256, the two crosstabs sum to their populations, the controls read 50 and 0, the verdict equals the declared rule's
verdict from `crosstab_flow`, a BOTH or MIXED verdict names a surprise row, the negative arm matches the verdict, zero vendor calls, zero secret reads, zero S3 writes, no served value changed, and no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB88-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The reader of record and ~127's script are READ ONLY.
- **No vendor call and no secret read.** You do not run `bd_help_read.py` or any Black Diamond fetch, read no cookie or credential file, and open no browser. Black Diamond's figures come from the stored tables.
- **No served write.** No S3 put, copy or delete (no S3 access is needed: the tables are local); no Lambda, Terraform or IAM act; no deploy; no push.
- **No client data in what you write.** Counts and booleans only. Nothing you derive from the private tables goes anywhere but the private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you
  could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W132-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~132/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_flow_timing.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-166.flow-convention-tieout-both-computed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 90 (round 88), cell `DB-b-166`.
<owned_cells>DB-b-166</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB88-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~132/IRPT_DASHBD.TO-DB-b-166.flow-convention-tieout-both-computed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB88-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the verdict; the two crosstab count sets; the controls; the module's commit; each handling choice you made that the reader of record did not fix; the
negative-arm sentence; any row ids. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access is granted or needed; the stored tables are local.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record, 17 synthetic arms dry-run) and the CTO's analysis names the negative arm.
lane: the <paths> block IS the grant.
</preflight>
