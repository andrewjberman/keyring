# TO IRPT_BCKEND.TO-IB-pr-272 -- Three read-only answers for the Inflection chain: the 09-24 NNA rows, the silver no-op, and whether Orion positions take an as-of date

<to_id>IRPT_BCKEND.TO-IB-pr-272</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~99</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-26 ~P ANALYSIS rulings 1, 2 and 3
(`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round26P.md` @7c9ed807bb); rows W97-S3 (BLOCKING), S216 (BLOCKING), W97-S4 |
**Decomp cell:** `IB-pr-272` (decomposition section 25) | **outcome_ref:** FWD-3 (INF) | **depends_on:** none

---

## WORKER FACE

**The cell.** Read-only. Three questions about the Inflection chain, one record, no write anywhere but your deliverables folder and
the surprise channel. Record: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~99/ROUND27_DIAGNOSIS.json`, one
section per question (`nna`, `mirror`, `asof`), each with `answer` (plain sentences) and `evidence` (a list of
`{"kind": "s3"|"log"|"file"|"doc", "ref": "..."}`; an `s3` ref is a full `s3://bucket/key`, a `file` ref a repo path, optionally `:line`).

**1. `nna` -- the three 09-24 NNA rows the coverage guard will not drop (ruling 1, row W97-S3).** The gold chain run
`chain_full_20260930_145412` stopped at step 33 `INF_C_01`: `data/inf/scripts/gold/INF_C_01.canonical_nna.py:918` called
`data/inf/scripts/gold/lib/nna_coverage_guard.py` (raise at :385), because three SERVED NNA rows of partition 2026-09-24 would drop:
account 866 -20,000, 769 +10,000, 1096 +10,000 (signed net $0.00, gross $40,000). Log:
`s3://opal-data-inf/diagnostic/chain_logs/chain_full_20260930_145328.log`. Compare, for the three accounts on 2026-09-24, the transactions
in the last raw that produced the served rows (the served NNA partition and the raw it was built from; the last good full run was
`chain_full_20260927_113304`, raw `s3://opal-data-inf/bronze/transactions/2026-09-27.jsonl.gz`) with today's raw
(`bronze/transactions/2026-09-30.jsonl.gz`). For each account write `before` and `after` (the transaction ids, amounts and the
classification INF_C_01 gives them each time -- read its classifier, do not re-implement it), `household_id` and `client_id` (from
`opal-data-inf/silver/api_dims/accounts_v2/`). Then `branch`: **A** if the three rows are one transfer among related accounts now read
INTERNAL (set `same_household_or_client` true), **B** for anything else. You write nothing to `lib/nna_coverage_excusals.json` and you
never disable the guard: Branch A becomes the issuer's never-widen packet, Branch B an upstream repair cell.

**2. `mirror` -- why `fact_positions` did not move past 2026-09-27 on today's raw (ruling 2, row S216).** Today's run landed
`s3://opal-data-inf/bronze/positions/2026-09-30.jsonl.gz` (15:18:55Z) but `s3://opal-data-assets/orion/inflection/silver/fact_positions/`
and `orion/inflection/bronze/positions/` still end at 2026-09-27. The two stages between are the Lambdas `opal-assets-ingest-mirror`
(source `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/`) and `opal-assets-silver-orion` (`infra/aws/lambda/opal-assets/opal-assets-silver-orion/`),
the latter logging only START on 09-28 and 09-29. Read both functions' triggers, code and CloudWatch logs from 2026-09-27 to now; name
the `component` that failed, the `cause` with its log line or code line, and the `repair` you would propose (not performed). Row W97-S4
says the 09-28/09-29 raw positions never existed; say whether that alone explains the silence or whether 09-30's raw also stalled.

**3. `asof` -- does Orion's positions endpoint accept an as-of date (ruling 3, row W97-S4)?** From documentation ONLY: the pull scripts
`data/inf/manual_api/pull_inflection_positions_daily.py`, `pull_inflection_positions.py`, `probe_positions_mv_daily.py`,
`probe_inflec_positions_mv.py`, and any Orion API reference in the repo (use `comp-find` for it). `accepts_as_of` is YES, NO or
UNDETERMINED; `doc_ref` names what you read; `calls_made` is 0 -- you make no Orion call of any kind.

<criterion id="P27-2-AC1" cell_refs="IB-pr-272"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_2_diagnosis.py" . nna P27-2-AC1</invocation><expect>P27-2-AC1 PASS</expect></criterion>
`P27-2-AC1` -- the `nna` section: the three accounts each with before/after/household/client, a branch A or B consistent with them, and
every `s3`/`file` evidence ref opening. Base: FAIL (record absent).

<criterion id="P27-2-AC2" cell_refs="IB-pr-272"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_2_diagnosis.py" . mirror P27-2-AC2</invocation><expect>P27-2-AC2 PASS</expect></criterion>
`P27-2-AC2` -- the `mirror` section: a named component, cause and proposed repair, with evidence that opens. Base: FAIL.

<criterion id="P27-2-AC3" cell_refs="IB-pr-272"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_2_diagnosis.py" . asof P27-2-AC3</invocation><expect>P27-2-AC3 PASS</expect></criterion>
`P27-2-AC3` -- the `asof` section: YES/NO/UNDETERMINED from a named document, zero calls. Base: FAIL. (A third criterion because the
ruling asks three separate questions of one read; each is one clause.)

<expected_criteria>P27-2-AC1,P27-2-AC2,P27-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the channel), plus your deliverables folder and this order's file. Everything else READ only.
- **No write to AWS, no invoke, no vendor call, no edit of any code or excusal file.** Reads of S3, CloudWatch Logs, Lambda
  configuration and the repo only.
- **Refusal clause.** A question the data cannot answer is answered as such (UNDETERMINED with what was read), never guessed.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 25 (round 27, workstream ~P), cell `IB-pr-272`.
<owned_cells>IB-pr-272</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P27-2-AC1, P27-2-AC2, P27-2-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~99/IRPT_BCKEND.TO-IB-pr-272.inf-three-reads-nna-mirror-asof.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P27-2-AC1,P27-2-AC2,P27-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, the NNA branch, the mirror's component and cause, the as-of
answer, and any surprise row id (`IRPT_BCKEND-W99-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: read-only; no schedule, trigger or cron is created or moved (the mirror's trigger is READ as part of question 2).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only; 0 roles or policies touched.
comp-blast: RUN -- denominator: 0 writes outside the worker's deliverables and the append-only channel; three read surfaces (INF raw and served NNA, two opal-assets Lambdas and their logs, repo documentation).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache.
comp-adversary: RUN -- P27-2-AC1/AC2/AC3 base FAIL (record absent), measured at the cut.
lane: the <paths> block IS the grant.
</preflight>
