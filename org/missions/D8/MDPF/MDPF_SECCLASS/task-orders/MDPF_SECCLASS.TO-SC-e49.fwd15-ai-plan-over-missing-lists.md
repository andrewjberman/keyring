# TO MDPF_SECCLASS.TO-SC-e49 -- round 9 SC-e-49: FWD-15 via FWD-11 -- the AI classifier's plan over each firm's missing list, held-first, after the direct-match plan: plans, dry run, half request

<to_id>MDPF_SECCLASS.TO-SC-e49</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~36</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-49` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-15, FWD-11 | **depends_on:** MDPF_SECCLASS.TO-SC-e54 (the contract's closed sub-class bound the plan grades
against). Slot `~36`, second in its queue; the issuer hands it once `TO-SC-e54` has drained.

---

## WORKER FACE

### THE CELL

`SC-e-49`: "FWD-15 (2.3): the FWD-11 runner planned over SC-e-33's per-firm missing lists, held-first, after the direct-match plan;
dry run with 0 model calls; the model-call count named for the issuer's run; half request" (DECOMP_R9). Analysis ruling 2.3
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`): "The path is FWD-11's producer run
over FWD-15's own list (held, no entry, per firm), held-first, after the direct-match plan. Vendor: FWD-11's recorded word (ADDENDUM,
C-VENDOR), the same model and the same payload (name and ticker); no new word is needed for it." Ruling 2.5 binds the verdict: a
DIRECT or AI verdict lands only if its sub-class is a member of the contract's closed list for its class (SC-e-54's
`fields.sub_asset_class.values_by_class`).

**Inputs (round 8, on the trunk; `M/` = `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`):**
- `M/MISSING_LIST_{49financial,cottonwood,inflection}_20261007.json` (TO-SC-e33): 451 + 341 + 773 = 1,565 held securities with no
  shared-list entry, each `{key, name, cusip, amount}`; claim `inferred` (local producer builds as-of 2026-10-05, W25-S1).
- The AI runner `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py` and its model module
  `infra/aws/lambda/v2_portal/_shared/etf_classification_model.py` (TO-SC-e31: six-class vocabulary; `--model --write` is the only
  mode that calls the model). The direct-match plan is the one TO-SC-e31/e32 used (read them for its entry point).
- Known from round 8: the runner sends the `NAME::` key to the model as its "ticker" (W26-S7); the AI runner builds no
  `identifier_namespace` (W26-S5). Carry both into the plan's per-entry fields; do not fix the runner here.

**Build (NO model call, NO table write):**
1. `M/R11_CHECKS/fwd15_ai_plan.py`: for each firm, read its missing list, run the direct-match plan first, then mark every entry
   it does not place as `AI` (or `UNPLACED-KEY` when no declared key form fits, or `PRESENT` when a fresh consistent read finds the
   key now present); order entries by `amount`, largest first; write `M/FWD15_AI_PLAN_<firm>_20261007.json` in the shape the issuer
   check reads (`firm, as_of, source, claim, missing_list, model_calls, planned_model_calls, entries[{key, amount, route, ...}]`), and
   print `FWD15-AI-PLAN firms=3 entries=<n> direct=<n> ai=<n> unplaced_key=<n> present=<n> model_calls=0`. The model client is
   never constructed (assert it with a counter on the transport, as TO-SC-e32's writer did).
2. `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD15_AI_20261007.md`: COO and CTO halves UNSIGNED; sections `## The act` (the issuer's run
   of the runner over the three plans, held-first, chunked), `## Blast radius` (one table, the keys and attributes that would be
   put, per firm, the planned model calls and the at-most count with the client's retry, the local candidate diff), the vendor word
   it rests on (FWD-11's recorded word), `Rollback per key` (a conditional delete of each key the run creates).
3. ASCII only.

### ACCEPTANCE

<criterion id="SC9-e49-AC1" cell_refs="SC-e-49"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/fwd15_plan_check.py</invocation><expect>FWD15-PLAN ok=True</expect></criterion>
`SC9-e49-AC1` -- each firm's plan covers its missing list exactly, held-first, with 0 model calls and the planned count stated.

<criterion id="SC9-e49-AC2" cell_refs="SC-e-49"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/fwd15_ai_plan.py</invocation><expect>model_calls=0</expect></criterion>
`SC9-e49-AC2` -- the planner runs end to end over the three real lists and calls no model.

<criterion id="SC9-e49-AC3" cell_refs="SC-e-49"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD15_AI_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC9-e49-AC3` -- the half request names the act, the blast radius with a candidate diff, and the rollback per key.

<expected_criteria>SC9-e49-AC1,SC9-e49-AC2,SC9-e49-AC3</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`firms=0 of 3`, all three plans absent); AC2 FAIL as expected (no planner);
AC3 FAIL as expected (`NOT-READY: ... absent`). Issuer controls on AC1's check: three synthetic plans built from the real missing
lists read `ok=True firms=3 of 3 entries=1565`; reversing one firm's order read `ok=False problems=['cottonwood:order']`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **No model call and no table write.** The run is the issuer's act under the signed half. Do not edit the runner, the model module,
  the contract or the missing lists; the R11 issuer check is READ-ONLY to you.
- **No package install and no download of any kind** (row S49).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W36-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/fwd15_ai_plan.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD15_AI_PLAN_49financial_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD15_AI_PLAN_cottonwood_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD15_AI_PLAN_inflection_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD15_AI_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-49`.
<owned_cells>SC-e-49</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e49-AC1, SC9-e49-AC2, SC9-e49-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~36/MDPF_SECCLASS.TO-SC-e49.fwd15-ai-plan-over-missing-lists.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e49-AC1,SC9-e49-AC2,SC9-e49-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** per firm the counts per route and the planned model calls, the at-most count with retries, how many AI entries carry a
NAME:: key (W26-S7), the half path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing; the model run is an issuer act with its own pair.
comp-iam: RUN -- round 8 (W25-S1): the held lists are inferred local builds; no role is declared by this cell. The model run's credentials are the issuer act's question.
comp-adversary: RUN -- the vendor word (FWD-11's recorded word, ruling 2.3: no new word); the missing lists (1,565 keys, inferred); the bound (ruling 2.5, via SC-e-54); W26-S5 and W26-S7 carried. BLIND: the served-bytes held read (a laptop seat's act, ruling 2.9).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 FWD-11, FWD-15 @90f99888cd; analysis rulings 2.3, 2.5 @1ca9e97fc9; DECOMP_R9 @5d70aab6c9; TO-SC-e31, e32, e33.
