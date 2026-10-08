# TO MDPF_SECCLASS.TO-SC-e77 -- round 15 SC-e-77: the D1-S11 row set (106 new rows) plus remaps of AI rows that break Andrew's alternatives rule

<to_id>MDPF_SECCLASS.TO-SC-e77</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~67</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-77` (`decompositions/MDPF_SECCLASS_DECOMP_R15.md`) |
**outcome_ref:** FWD-16, FWD-17 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-77`, row D1-S11. In the trace `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.json`, groups B (25 securities, the ticker has no
row) and D (81 securities, no row under any key) total 106 securities and $5.82M that need a canonical row. Andrew-direct
2026-10-08 ~19:0xZ, VERBATIM: "Hedge funds, private funds, real estate funds, all of this falls to Alternatives."

**Build:**
1. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/S11_ROW_SET_20261008.tsv`. The header is `key, name, action, asset_class, sub_asset_class, current_class, rule, evidence`,
   and the format is the one `R15_CHECKS/sc_r15_rows_set.py` reads.
   - One NEW line per B/D security: keyed by its ticker (group B) or its trace `name_key` (group D).
     - The class must be one of the six, from the security's own evidence: its name, its old map class in the trace, or the issuer's
       fund type.
     - A hedge, private or real estate fund reads `alternatives` with `rule=andrew-alternatives`.
     - `evidence` gives the basis in one phrase.
   - One REMAP line per existing AI-landed row (`updated_by` `mdpf-secclass-model` or the e32/e49 runner's value; read-only scan of
     etf-classifications) whose name is a hedge, private or real estate fund and whose class is not alternatives. Set
     `rule=andrew-alternatives` and `current_class` = its class now.
2. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py`. Shape it on `R11_CHECKS/clean_name_write_v2.py`; the default is a dry run that counts
   every mutating call and asserts it is 0.
   - NEW is a put conditioned on `attribute_not_exists(ticker)`.
   - REMAP is an update of `asset_class` and `sub_asset_class` conditioned on the current class.
   - `--write` needs `--half` (both headings SIGNED) and `--snapshot` (written first).
   - `--rollback <snapshot> [--write]` deletes the NEW rows this run put, and restores the REMAP rows, each only while the row still
     reads this run's value.
   - The dry run prints `S11-ROWS-DRY-RUN new=<n> remap=<n> refused_present=<n> refused_stale=<n> puts=0`.
3. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S11_ROWS_20261008.md`, with `## The act`, `## Blast radius` and
   `Rollback per key`. The blast radius is each line's before and after, plus the candidate served-mix delta from the trace's dollars.
   Leave both halves unsigned.

### ACCEPTANCE

<criterion id="SC15-e77-AC1" cell_refs="SC-e-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/sc_r15_rows_set.py</invocation><expect>S11-ROW-SET ok=True</expect></criterion>
`SC15-e77-AC1` -- every B/D security appears once as NEW, every class is in the six, rule rows read alternatives, REMAP lines are rule rows moving off a non-alternatives class.
<criterion id="SC15-e77-AC2" cell_refs="SC-e-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py</invocation><expect>refused_stale=0 puts=0</expect></criterion>
`SC15-e77-AC2` -- the dry run against the live table plans every line, refuses none, and writes nothing.
<criterion id="SC15-e77-AC3" cell_refs="SC-e-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S11_ROWS_20261008.md</invocation><expect>HALF-READY</expect></criterion>
`SC15-e77-AC3` -- the half request carries the act, the blast radius with a candidate diff, and the rollback per key.

<expected_criteria>SC15-e77-AC1,SC15-e77-AC2,SC15-e77-AC3</expected_criteria>

JUDGMENT, not self-graded: 3.0.0_SA_CVO grades at L9 whether each class, and each `rule=andrew-alternatives` mark, is right.

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~19:2xZ):
- SC15-e77-AC1: FAIL, as expected (the set is absent; denominator bd=106).
- SC15-e77-AC2: FAIL, as expected (the writer is absent).
- SC15-e77-AC3: FAIL, as expected (the half is absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan): no write to any table or bucket, no deploy, no invoke, no model call. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W67-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/S11_ROW_SET_20261008.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S11_ROWS_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R15.md</decomp_doc> (round 15), cell `SC-e-77`.
<owned_cells>SC-e-77</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC15-e77-AC1, SC15-e77-AC2, SC15-e77-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~67/MDPF_SECCLASS.TO-SC-e77.s11-row-set.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC15-e77-AC1,SC15-e77-AC2,SC15-e77-AC3`. Record a judgment criterion as
`UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming 3.0.0_SA_CVO, never as PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the table write is the issuer's act under the pair.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only scan/get under the seat's role).
comp-adversary: RUN -- a key already present (put on absence refuses); a row changed since the set (conditional refuses); BLIND: which names are truly hedge/private/real estate funds (CVO judgment).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL1 msgs 1061, 1066, 1071; Andrew-direct 2026-10-08 ~19:0xZ (alternatives rule); trace @3d9077bdc5; DECOMP_R15.

### AMENDMENT 1 -- AC2 admits exactly the one already-present key, RAL (issuer 2.0.0_SA_COO~M1, 2026-10-08 ~19:4xZ; row MDPF_SECCLASS-D1-W67-S1)

RAL (group B, $70) was landed by the e49 model runner at 2026-10-08T19:01:52Z, after the trace was cut, as equity / Information
Technology. That is the same class this set gives it, so a NEW put would change nothing, and the put on absence rightly refuses it.
AC1 keeps RAL as a NEW line, so the B/D denominator stays 106. AC2's expectation is now
`refused_present=1 refused_stale=0 puts=0`, with the one refused key being RAL. Any other refused key still fails AC2, which the
worker confirms from the REFUSED_PRESENT line. Gate limb: none grades an amendment to an existing order.

### AMENDMENT 2 -- add the 21 liquid-alt mutual funds as REMAP lines (issuer 2.0.0_SA_COO~M1, 2026-10-08 ~20:2xZ; 1.0.0_SA_CTO~DELL1 msg 1130)

Andrew-direct ~20:1xZ, VERBATIM: "1. Approved." That approves the CTO's recommendation (a). Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_201xZ_LIQUID_ALTS_TO_ALTERNATIVES_ETF_STRATEGY_SLEEVES_ENDPOINT_CONFIRMED.md`.
Hedged-equity, long/short, market-neutral and absolute-return mutual funds move from structured/Hedge to alternatives. Volatility notes
and ETNs (VXX and its kind) stay structured. The order is reopened to `issued` for this step only.
1. Re-run the live read-only scan behind row D1-W67-S2: the AI-landed rows reading structured/Hedge that are such mutual funds
   (21 at the row's scan). Add one REMAP line per fund:
   - `rule=andrew-alternatives`, `current_class=structured`, `asset_class=alternatives`;
   - no sub-class, because the contract holds none for alternatives other than real estate and absent stays absent;
   - an `evidence` phrase naming the strategy.
   A row that is a volatility note, ETN or listed option line stays out. Also move GSRTX's live sibling row
   `NAME::GOLDMAN SACHS ABSOLUTE RET TRCKR INSTL` into the set as a REMAP, so the two share classes agree on alternatives.
2. Re-run AC1, AC2 and AC3. AC2's expectation is unchanged (`refused_present=1 refused_stale=0 puts=0`, RAL). The remap count goes up
   by the lines added.
3. Update the half request's blast radius with the added lines and their served-mix effect. Leave both halves unsigned. Re-validate
   the proof instance and flip.
Gate limb: to-pipeline-gate does not fire on a modification except GATE (viii), and this order declares <placeholders>NONE</placeholders>.

### AMENDMENT 3 -- AC2 no longer counts no-op present keys (issuer 2.0.0_SA_COO~M1, 2026-10-08 ~20:3xZ; row MDPF_SECCLASS-D1-W67-S3)

While e49's AI leg runs, group-B tickers keep landing with the same class this set gives them: RAL at 19:01Z, OXYWS at 20:08Z. A put
on absence refuses each one, and refusing changes nothing. So a fixed `refused_present` count cannot hold. AC2's expectation is now
`refused_stale=0 puts=0`.
The issuer reads every `REFUSED_PRESENT` line before signing. Each must show a live class equal to the set line's class. A present key
with a different class is a re-plan, not a no-op.
Scope confirmed: the 7 arbitrage, event-driven, multi-strategy and managed-futures mutual funds are hedge-fund strategies under
Andrew's rule, and they stay. JHQTX is a seed row: it is corrected in the seed source, not by this writer.
Gate limb: to-pipeline-gate GATE (viii) grades this modification.

