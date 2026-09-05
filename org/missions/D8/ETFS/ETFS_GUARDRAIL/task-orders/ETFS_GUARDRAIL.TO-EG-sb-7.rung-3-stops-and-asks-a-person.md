# TO ETFS_GUARDRAIL.TO-EG-sb-7 -- rung 3 STOPS AND ASKS A PERSON: names the dates, the partner and the provider, writes the ask where the refusal already lands, and never leaves Opal on its own

<to_id>ETFS_GUARDRAIL.TO-EG-sb-7</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- proof-of-spec instance `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-sb-7.rung-3-stops-and-asks-a-person.proof_of_spec.json` VALID (rc=0). All 5 criteria S7B-AC1..AC4 PASS by output (8/8 tests, +2 over EG-s-7's 6; HTTP_CLIENT_IMPORTS=0 ASK_WRITER=1; direct-call check ASKS=1 PROVIDER=Black Diamond AUTH=PER-USE with write=False making no S3 call; commit gate clean); S7B-AC5 judgment RECORDED for CVO L9 grading. No surprise row this cell. Flip made by the assignee per the tree-convention grant. Prior: pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S7b; s.0 ruling card 4; s.6 ruling 4; ENDPOINT FWD-8 and the "WHY FWD-8 SURVIVED THE FOLD" note) | **Decomp cell:** `EG-sb-7` | **outcome_ref:** FWD-8 | **verb:** wire | **depends_on:** `EG-s-7` (your previous order)

---

## THE CELL

`EG-sb-7` (PRD s.7.2 S7b): *"same module, rung 3 -- STOPS AND ASKS A PERSON. DIFFERENT ACTOR, not a later step. Per-use egress, no standing grant. Names the dates it wants and waits."* FWD-8's DONE WHEN: *"EXERCISED -- the system has actually stopped and asked, rather than going ahead on its own."* ACCEPT: *"if the only way to fill a gap is to ask the outside provider for it, the system stops, names the days it wants, and waits for a person to say yes."* Ruling card 4: standing pre-authorization for targeted egress was NOT granted; rung 3 stays per-use-authorized. The PRD's own reason FWD-8 is not folded into FWD-7: FWD-8 fires BEFORE we leave Opal and ASKS; FWD-7 (`EG-s-8`) fires AFTER egress has failed and REPORTS.

Rung 3 is therefore a STOP that produces an ARTIFACT a person can act on, and NOTHING that leaves Opal. The artifact: `platinum/reports/<month>/coverage_egress_ask.json` in `opal-data-etfs` (the reporter box's role already writes `platinum/reports/*`; the orchestrator already reads it) -- `{"month", "generated_at", "asks": [{"date", "partner", "provider", "class": "D", "reason"}...], "authorization": "PER-USE -- a person decides; nothing here is executed by any process"}`. The provider per partner: cottonwood -> Black Diamond (the monolith's `blackdiamond/cottonwood/` upstream); 49financial -> Schwab (`schwab/08242234/`); inflection -> Orion (`orion/inflection/`, or whatever `EG-s-12`'s result says the deployed producer reads). The ask reaches a person through the refusal alert on the EXISTING topic (`EG-s-8` makes the orchestrator's refusal text carry it) -- this order writes the artifact and its shape; it wires no send.

## DELIVERABLE

1. In `data/etfs/scripts/coverage/remediate.py` (your own module from `EG-s-7`): `rung3_stop_and_ask(partner, month, unresolved, *, s3=None, write=True) -> dict` -- builds the ask from the D-class (and, stated separately, the still-UNKNOWN) days, writes the artifact when `write=True` under the `platinum/reports/<month>/` prefix, and RETURNS without any further act. `remediate_month` calls it as its last step when `unresolved` is non-empty. The module still carries no HTTP client (S7-AC2's property stays true).
2. Two more arms in `data/etfs/scripts/coverage/tests/test_remediate.py`: (g) two D days for two partners -> the ask names both dates, both partners, both providers, and the function returns without any invoke or HTTP call (assert on the stubs); (h) zero unresolved -> NO ask artifact is written (`put_object` never called for the ask key) -- the stop fires only when there is something to ask.
3. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/rung-3-stops-and-asks-a-person.result.md` -- criteria with invocation, output, rc, denominator; the ask's JSON shape as an example; the provider map with its sources.

## ACCEPTANCE

<criterion id="S7B-AC1" cell_refs="EG-sb-7"><invocation>python -m pytest data/etfs/scripts/coverage/tests/test_remediate.py -q</invocation><expect>passed</expect></criterion>
`S7B-AC1` -- the battery is green with arms (g) and (h) added (record N passed; N must exceed EG-s-7's count by 2).

<criterion id="S7B-AC2" cell_refs="EG-sb-7"><invocation>python -c "import re; s=open('data/etfs/scripts/coverage/remediate.py').read(); print('HTTP_CLIENT_IMPORTS=%d ASK_WRITER=%d' % (len(re.findall(r'^\s*(?:import|from)\s+(?:requests|urllib|http)\b', s, re.M)), len(re.findall(r'def rung3_stop_and_ask\(', s))))"</invocation><expect>HTTP_CLIENT_IMPORTS=0 ASK_WRITER=1</expect></criterion>
`S7B-AC2` -- still no HTTP client in the module after rung 3 lands, and exactly one ask-writer exists (the ask is data; the egress is a person's).

<criterion id="S7B-AC3" cell_refs="EG-sb-7"><invocation>python -c "import json,sys; sys.path.insert(0,'data/etfs/scripts'); from coverage import remediate as r; a=r.rung3_stop_and_ask('cottonwood','2026-08',[{'date':'2026-08-04','class':'D','reason':'no partition'}], write=False); print('ASKS=%d PROVIDER=%s AUTH=%s' % (len(a['asks']), a['asks'][0]['provider'], a['authorization'][:8]))"</invocation><expect>ASKS=1 PROVIDER=Black Diamond AUTH=PER-USE</expect></criterion>
`S7B-AC3` -- the ask names the date, the partner's provider and its per-use authorization, and `write=False` makes no S3 call.

<criterion id="S7B-AC4" cell_refs="EG-sb-7"><invocation>bash .tools/commit-gate.sh data/etfs/scripts/coverage/remediate.py data/etfs/scripts/coverage/tests/test_remediate.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S7B-AC4` -- the commit gate is clean.

<criterion id="S7B-AC5" cell_refs="EG-sb-7" judgment="true"/>
`S7B-AC5` -- graded by the CVO at L9: rung 3 is a DIFFERENT ACTOR (a person) and not a later automated step; no standing egress grant exists anywhere in the module or the estate this order touched; the ask is complete enough that a person can say yes without a follow-up question (dates, partner, provider). RECORD; NO VERDICT.

<expected_criteria>S7B-AC1, S7B-AC2, S7B-AC3, S7B-AC4, S7B-AC5</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override. The orchestrator (which will carry the ask into the refusal text) is `EG-s-8`, your NEXT order -- not this one.
- **NO PROVIDER CALL, NO HTTP CLIENT, NO CREDENTIAL, NO STANDING GRANT.** A rung-3 "ask" that does anything but write the artifact and return has EXCEEDED ruling card 4.
- **No live S3 write in this order:** every exercise runs with `write=False` or a stubbed s3. The artifact's live write happens inside the renderer's gate (`EG-s-6`) on a real unresolved month.
- **No fabrication** (property 9): an unresolved day stays missing; the ask is not a value.
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
data/etfs/scripts/coverage/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-sb-7`.
<owned_cells>EG-sb-7</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo-module cell that adds no grant and touches no policy; the reporter role's platinum/reports/* write already exists (iam.tf:45-52).
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`).
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S7B-AC1` .. `S7B-AC5`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-sb-7.rung-3-stops-and-asks-a-person.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S7B-AC1,S7B-AC2,S7B-AC3,S7B-AC4,S7B-AC5` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
