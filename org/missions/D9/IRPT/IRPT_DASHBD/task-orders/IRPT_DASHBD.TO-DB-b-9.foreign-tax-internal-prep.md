# TO IRPT_DASHBD.TO-DB-b-9 -- Foreign tax paid to internal: census every reader of the shared code table, measure each served delta, and prepare the adapter's override retirement as a patch (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-9</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-2 analysis @f5fbeaa543 item E3; ADDENDUM 1 A4 (@7a888d7675), row
IRPT_DASHBD-S6 limb (e) | **Decomp cell:** `DB-b-9` (decomposition section 3) | **outcome_ref:** FWD-1 (the flow term's correctness) |
**depends_on:** none (queued on this slot after TO-DB-b-7)

---

## WORKER FACE

**The cell.** The shared Schwab code table `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`
classes `FTP/FC/WD` (foreign tax paid, about 2,449 rows) and `FTR/FC/WD` (foreign tax reclaimed, about 4 rows) as EXTERNAL, so a
withholding reads as a client withdrawal. The ruling (CTO ADDENDUM 1 A4): both codes move to INTERNAL (tax) in the table's owner's edit
(`4.0.0_SA_CRO`); every served engine that reads the table moves under ONE packet with both halves; and the IRPT adapter's own override
(which corrects for the table today) retires in the SAME act. **You prepare that act; you do not perform any part of it.** You never
edit the table, never deploy, never run a served producer with `--upload`.

**Where things are (read only).**
- The table above (read its schema and the two codes' current rows).
- The served 49F engine's reader: `data/assets/scripts/gold/runners_49f/a05_ref_txn_classification.py`. Inflection and Cottonwood carry
  their own `a05_ref_txn_classification.py` (`data/inf/scripts/gold/runners_inf/`, `data/cot/scripts/gold/runners_cot/`): find out
  whether each reads THIS table, and census every other file in the repository that reads it (`comp-find` the table's file name; print
  the denominator).
- The IRPT adapter's override: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` lines 584-596 (`WITHHOLDING_CODE`,
  `crosses = crosses & ~wh`) and the census fields beside it.

**What you produce (all under your deliverables folder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/`).**
1. `FTP_INTERNAL_BLAST_R3.json`: `{"codes": ["FTP/FC/WD","FTR/FC/WD"], "table": "<the table's path>", "files_scanned": n,
   "readers": [{"path","firm","served": true|false}], "per_reader_delta": [{"path","firm","rows": n,"abs_usd": x,"net_usd": x,
   "partitions": n}], "adapter_override_patch": "<repo-relative path of the patch>"}`. For each SERVED reader, the delta is what its
   served output would move if the two codes were internal: rows touched, absolute and net dollars, partitions -- measured from the
   landed data that reader's own code reads (its silver), never estimated. Say for each reader whether it is served and where.
2. `ADAPTER_OVERRIDE_RETIREMENT_R3.patch`: a `git diff` of `account_return_daily.py` removing the override (the classification then
   comes from the table alone). Write it as a file; do NOT apply it to the repository.
3. `FTP_ADAPTER_EQUIVALENCE_R3.json`: the adapter run twice with `--dry-run` over at least 20 trading-day partitions for the six sample
   accounts -- "today" (the code at HEAD with the table as it is) and "after" (the patched code with an edited COPY of the table in
   which the two codes are internal), each run in a scratch copy, never the CRO's file. `{"partitions","accounts","withholding_rows",
   "max_abs_diff_external_flow","max_abs_diff_total_return_daily","runs": [{"label":"today","code":"<commit>","table":"<sha256>"},
   {"label":"after","code":"patched","table":"<sha256>"}]}`. Both differences must be 0: the retirement plus the edit together leave
   the adapter's output exactly where it is.
4. A one-page `FTP_INTERNAL_BLAST_R3.md` in plain English for the packet: which served surfaces move, by how much, and what does not.

<criterion id="DB-9-AC1" cell_refs="DB-b-9"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/p3_9_ac1_ftp_blast_record.py" .</invocation><expect>DB-9-AC1 PASS</expect></criterion>
`DB-9-AC1` -- the census names both codes, a positive scan denominator and the 49F engine among the readers; every served reader carries
a measured delta row; the patch applies cleanly at HEAD (`git apply --check`). Base: FAIL (no record).

<criterion id="DB-9-AC2" cell_refs="DB-b-9"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/p3_9_ac2_adapter_equivalence.py" .</invocation><expect>DB-9-AC2 PASS</expect></criterion>
`DB-9-AC2` -- the adapter's output is unchanged (0 difference in external flow and daily return) when the patch and the edited table move
together, over at least 20 partitions crossing withholding rows. Base: FAIL (no record).

<expected_criteria>DB-9-AC1,DB-9-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS:** reads only. No write to any bucket, no deploy, no Lambda invoke, no vendor call.
- **Refusal clause.** A reader whose served output you cannot measure from landed data is a row naming the reader and what is missing;
  a non-zero equivalence difference is a row with the rows that differ, never a patch adjusted until it reads zero.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): the table under `org/tier1_exec/4.0.0_SA_CRO/deliverables/`, `data/assets/scripts/gold/`,
`data/inf/scripts/gold/runners_inf/`, `data/cot/scripts/gold/runners_cot/`, `lib/`, `infra/logic/registry/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 3 (round 3, workstream B), cell `DB-b-9`.
<owned_cells>DB-b-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-9-AC1, DB-9-AC2. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-9.foreign-tax-internal-prep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-9-AC1,DB-9-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, the readers with their served deltas, and any surprise row
id (`IRPT_DASHBD-W1-S<k>`, k >= 6).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a measurement cell; no schedule moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the worker's session; no role changes.
comp-blast: RUN -- the cell writes only under its deliverables folder; the served blast radius of the later act is what the cell measures (49F, Inflection and Cottonwood each carry an a05_ref_txn_classification.py; which read the table is the census).
comp-routes: DECLARED-NOT-APPLICABLE.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-9-AC1 base FAIL (no record), DB-9-AC2 base FAIL (no record), dry-run at the base 2026-10-02 ~06:5xZ.
lane: the <paths> block IS the grant.
</preflight>
