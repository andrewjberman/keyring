# TO NFRA_COMPEFFICACY.TO-CE-T-9R -- comp-trigger, THE REMEDIATED ORDER under CE-t-9 (S13, SPEC_ERROR -> L6): four planted cases, FOUR DISTINGUISHABLE outputs in the tool's own voice -- a function-existence check from the estate's own Lambda population, the S3-notification-only case separated through the existing machinery, PRD s.4.3's bar QUOTED and closed on

<to_id>NFRA_COMPEFFICACY.TO-CE-T-9R</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut. Authority: the round-4 L10 stamp @153522a509 (3.0.0_SA_CVO): NFRA_COMPEFFICACY-S13 GRADUATED, route SPEC_ERROR, loop_target 6, owner 2.0.0_SA_COO, remedy verbatim in surprise-channel/remediations/REMEDIATION_v1.md; decomp v0.2.3 @dcf07b4799 (CE-t-9 REMEDIATED; ROUND 5 fence); PRD v0.5 @5bbdab5ec7 (s.4.3 with the GRAIN sentence). This order REPLACES nothing: TO-CE-T-9 stays complete on the record and its grade is the L4 owner's at COMPLETION_GRADES; this order closes the CELL. Continuity and the S13 disarm owner: 0.8.0_AE_CloudComp base.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (s.4.3 the four states + the GRAIN sentence; s.7 row T-9) · **Decomp cell:** `CE-t-9` (REMEDIATED v0.2.3; closes on "four planted cases, four DISTINGUISHABLE outputs (PRD s.4.3 quoted)") · **Lane:** `.tools/comp-trigger` (ANY) + `org/modules/graph/comp_trigger.py` (the ENGINE) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-trigger.result.md` (AMENDED in place: a new dated `answer_state` block above the round-4 one, which stays as the record of what was measured then). **Rule 27 seating:** `0.8.0_AE_CloudComp` BASE holds NFRA_COMPEFFICACY only.

---

## THE CELL, AND WHY THIS ORDER EXISTS

The round-4 order TO-CE-T-9 landed the scope + delegation line on every answer (@`7737320640`) and its T9-AC2 was self-marked
PASS with a disclosed partial. The CVO's S13 row (@`153522a509`), mechanism verbatim: *"comp-trigger searches EventBridge
rule names/targets and Scheduler schedule names and has no function-existence check of its own, so SUBJECT_ABSENT_FROM_CORPUS,
PRESENT_WITH_ZERO_RESULTS and the S3-notification-only PARTIAL_OR_BLIND case all fall through one `if not matches:` branch
(org/modules/graph/comp_trigger.py:render() @7737320640) and print byte-identical bodies at rc 0; the scope + delegation line
this cell added prints on every miss and therefore separates nothing."*

THE BAR THIS ORDER CLOSES ON, QUOTED FROM PRD v0.5 s.4.3 @`5bbdab5ec7`, NOT RESTATED:
> **PASS** = four cases, four distinguishable outputs. **FAIL** = any two states print alike. This is FWD-2 and it is the
> load-bearing test of the project. **GRAIN (v0.5, T-7 F2, CTO adjudication):** distinguishability is judged within ONE
> invocation's output by the STATE TOKEN in the tool's own voice; two subcommands answering two questions may share an rc,
> but each must print which of the four states it is -- a bare REFUSE shape whose state is carried only by the echoed
> argument is FAIL on the token, not on the rc.

THE REMEDY, QUOTED FROM THE S13 REMEDIATION ROW: *"Minimally, a function-existence check (the Lambda population the estate
already carries -- the DESIRED plane's Terraform or the live graph's LAMBDA nodes, whichever the cell's BOUNDS admit) that
separates SUBJECT_ABSENT_FROM_CORPUS; and the S3-notification-only case separated from PRESENT_WITH_ZERO_RESULTS by the
cell's own closes-on ('S3-notification backend via existing machinery; existing machinery checked FIRST') or by a distinct
PARTIAL_OR_BLIND voice that prints only when the scope actually excludes something the subject has. The second clause of
T9-AC2 (the scope + delegation line) is met and stays."*

## DELIVERABLE

1. **The existence check.** Before the rule/schedule scan, comp-trigger resolves the subject against a Lambda population the
   estate already carries -- BOTH carriers are read-only and both already exist: the live graph's LAMBDA nodes (the comp-aws
   corpus, `comp-find --corpus aws`, vintage = the DB's own `built:` line) and the DESIRED plane's `aws_lambda_function`
   declarations under `infra/aws/terraform/`. The tool prints WHICH plane it resolved against, that plane's DENOMINATOR and
   VINTAGE on the answer line, and never guesses: a subject in neither population is SUBJECT_ABSENT_FROM_CORPUS in the tool's
   own voice (its own token, its own body, its own rc -- rc 3 is the family's NOT-FOUND form per cli.py's trace/blast dial;
   pick the value that keeps `--list` and the hit path at rc 0 and STATE IT); a subject present in one plane and absent in
   the other is said so, never collapsed.
2. **The S3-notification-only separation, through the existing machinery.** The round-4 order measured the delegation
   (comp-aws's S3_BUCKET node build, `org/modules/graph/comp_aws_cli.py:273-279`, `event_notifications` / `notify_sns` /
   `notify_sqs` stored on 28 of 28 live S3_BUCKET nodes). Consume it: when the subject EXISTS and no rule or schedule names
   it, comp-trigger reads the graph's S3_BUCKET notification fields; a bucket whose notification names the subject makes the
   answer PARTIAL_OR_BLIND in the tool's own voice, NAMING the bucket and the event class ("the scope excludes something the
   subject HAS"); no such bucket and the answer is PRESENT_WITH_ZERO_RESULTS. Zero new AWS calls: the graph is the carrier.
   The scope + delegation line from round 4 stays on every answer.
3. **The four cases, re-planted and quoted** in a NEW dated `answer_state` block at the top of `comp-trigger.result.md`:
   SUBJECT_ABSENT_FROM_CORPUS (a name in neither population), PRESENT_WITH_ZERO_RESULTS (`bd-price-update` or another real
   function with no trigger of any class), PARTIAL_OR_BLIND (`bd-allocation-processor`, the TF-confirmed S3-notification-only
   target on opal-data-bd), NOT_APPLICABLE (`--list` on an empty region) -- rc + full text per case, and a fifth line that
   DIFFS the four bodies pairwise (6 pairs, 6 "differ" verdicts, or the order is not done).
4. **Rule T's form stays wired** (`_compbudget.py`; the existence read and the S3 read are inside the budget; DEFERRED for a
   call that would outlive it) and the round-4 crash regression arm stays green.
5. **The battery** `.tools/tests/test_comp_trigger_battery.py` gains one arm per new behaviour (the existence check on both
   planes, the S3-notification separation, the pairwise-distinct bodies) with a planted mutant per arm going RED -- including
   the mutant that collapses the existence check back into `if not matches:` (the S13 shape) -- direct AND under pytest at the
   FILE grain; directory grain stated as it reads.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T9R-AC1" cell_refs="CE-t-9"/> `T9R-AC1` -- THE BAR, QUOTED: the deliverable's new `answer_state` block quotes PRD v0.5 s.4.3's PASS/FAIL sentence and GRAIN sentence verbatim (not restated) and shows four cases with four DISTINCT state tokens and four pairwise-DISTINCT bodies (6 of 6 pairs differ), rc + text per case, from real runs of the production binary.
<criterion id="T9R-AC2" cell_refs="CE-t-9"/> `T9R-AC2` -- EXISTENCE CHECK: the answer line names the plane resolved against (live graph LAMBDA nodes and/or DESIRED Terraform), its denominator and vintage; a name in neither reads SUBJECT_ABSENT_FROM_CORPUS in the tool's own token; a real function with no trigger reads PRESENT_WITH_ZERO_RESULTS; the two never share a body.
<criterion id="T9R-AC3" cell_refs="CE-t-9"/> `T9R-AC3` -- S3-NOTIFICATION SEPARATION VIA EXISTING MACHINERY: `bd-allocation-processor` reads PARTIAL_OR_BLIND naming the bucket and event class from the graph's S3_BUCKET notification fields (comp_aws_cli.py:273-279 cited); zero new AWS clients or calls added (diff shown); the scope + delegation line still prints on every answer.
<criterion id="T9R-AC4" cell_refs="CE-t-9"/> `T9R-AC4` -- battery: new arms for each behaviour with a planted RED mutant each (the `if not matches:` collapse among them), the round-4 crash arm still green, direct AND pytest at the FILE grain, directory grain stated as it reads; commit-gate clean on every .py touched.
<criterion id="T9R-AC5" cell_refs="CE-t-9"/> `T9R-AC5` -- the proof instance VALID with a `surprises` entry that resolves to `NFRA_COMPEFFICACY-S13@153522a509` carrying the fix commit as this seat's DISARM (the row's disarm_owner is this seat; the disposition stays 3.0.0_SA_CVO's at L9); push state MEASURED at report; the complete flip self-committed.

<expected_criteria>T9R-AC1, T9R-AC2, T9R-AC3, T9R-AC4, T9R-AC5</expected_criteria>

## SURFACES

`org/modules/graph/comp_trigger.py` @`7737320640` (render(), the `if not matches:` branch; live_rules()/live_schedules() with their UNAVAILABLE sentinels; the `_compbudget` carrier) · `.tools/comp-trigger` · `org/modules/graph/comp_aws_cli.py:273-279` (the S3_BUCKET notification fields -- READ, never changed) · the comp-aws corpus (`comp-find --corpus aws`, node_type LAMBDA / S3_BUCKET; vintage on its `built:` line) · `infra/aws/terraform/**` `aws_lambda_function` declarations (READ) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `.tools/tests/test_comp_trigger_battery.py` @`7737320640` · `deliverables/0.8.0_AE_CloudComp/comp-trigger.result.md` @`b1dab0b6a0` · the S13 rows: `surprise-channel/investigations/INVESTIGATION_v1.md` + `surprise-channel/remediations/REMEDIATION_v1.md` @`153522a509`.

## BOUNDS

- **READ-ONLY, always:** no EventBridge rule, Scheduler schedule, S3 notification, IAM, Terraform or graph resource is created, changed, enabled or disabled; the existence check and the notification read are reads of carriers the estate already builds; **zero new AWS clients or API calls** in comp_trigger.py (the graph is the carrier; a live Lambda ListFunctions call is NOT admitted -- the graph and Terraform are the two planes).
- **The graph's own vintage is printed, never assumed fresh;** a graph read that fails is UNAVAILABLE in the tool's voice, never "absent".
- **No new dependency; no new file outside the engine, the shim, the battery, the deliverable and the proof instance.** `_compbudget.py` and `comp_aws_cli.py` are consumed, not edited.
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; ids are minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author:** the grade is the L4 owner's; the L9 disposition of S13 is the CVO's.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @dcf07b4799 (v0.2.3), cell CE-t-9 (REMEDIATED; s.1a; ROUND 5 fence).
<owned_cells>CE-t-9</owned_cells>
Read-dependencies, NOT claimed: CE-t-6 (comp-blast's own subject-existence row -- a sibling pattern, not a dependency), CE-t-25 and CE-t-19 (in parallel at ~A and ~B; no dependency any way).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 21 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 4 -> 4, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY, comp-trigger or comp_trigger.py (read at 2026-09-03 09:27Z).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is comp-trigger's answer-state voice and two READ carriers the estate already builds (the comp-aws graph, the Terraform declarations); no AWS principal, policy or resource is created, changed or granted, and no new AWS API call is admitted (BOUNDS). The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @dcf07b4799 (2026-09-03T11:14:26Z); 5/5 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 6 attempted / 5 stable / 1 flagged = this order's proof instance (GONE by construction at cut; the deliverable exists from round 4 and is AMENDED, not created); uncited neighborhood 193 (25 shown, cap declared); --no-packet (stage 4 pointers only, the caller's choice, recorded in the declaration).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T9R-AC1`..`T9R-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-9R.comp-trigger-four-distinguishable-states.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. The `surprises`
entry for S13 is REQUIRED (it is the disarm carrier); T9R-AC1's pairwise diff and T9R-AC4's mutants are the controls that must be
able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_trigger.py --for "render()'s miss branch, where the subject is first resolved, and where the scope line is printed"`; `comp-find --corpus aws '<a real function name>' LAMBDA` and `comp-find --corpus aws 'bd-allocation-processor' S3_BUCKET` (the two carriers, denominators + vintage printed); `comp-read org/modules/graph/comp_aws_cli.py --for "how S3_BUCKET nodes store event notifications and their targets"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-trigger <function>` from a seat other than this one (~A or ~B is the nearest; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record) with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
