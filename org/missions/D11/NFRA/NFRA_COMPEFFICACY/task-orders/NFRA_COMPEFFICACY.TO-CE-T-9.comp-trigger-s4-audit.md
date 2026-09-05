# TO NFRA_COMPEFFICACY.TO-CE-T-9 -- comp-trigger: the s.4 per-tool audit deliverable, the 4.3 four-case test, and the SCOPE DECLARED IN THE HEADER (EventBridge + Scheduler only; S3-notification triggers out of scope BY DESIGN, said on every answer, never a silent zero)

<to_id>NFRA_COMPEFFICACY.TO-CE-T-9</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T09:20:00Z; committed by the assignee itself under the tree task-orders/** -> ANY lane grant @f9c97a52ce) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-9.comp-trigger-s4-audit.proof_of_spec.json; T9-AC1..AC6 self-assessed PASS (AC2 disclosed-partial on its own text-distinguishability clause, per the row's own status_reason; deliverable comp-trigger.result.md at the tree home, fix commit 7737320640, deliverable+proof commit b1dab0b6a0). CVO grade pending -- certifier != author. No surprises filed under this cell (F3's bounded, undetermined coverage question rides the deliverable per S9's own precedent). Push state MEASURED in the DELIVERABLE REPORT to 2.0.0_SA_COO, not asserted here. Prior history: pending -- GO paired at cut. Authority: round 4 of the canonical loop on NFRA_COMPEFFICACY -- CVO's round-3 stamp @7ec9bf06dd (ZERO GRADUATION: proceed to the next L6 dispatches), decomp v0.2.2 @b7daeaa6f0 (STAGE 2: CE-t-8 -> CE-t-6 (after CE-t-19) -> CE-t-9 -> CE-t-7; ROUND 4 fence: CE-t-9 at the base seat), on Andrew's words on the loop (@10a4beaffb, @de2d6d643c). No sequencing dependency (the row's depends_on is empty). Continuity at the base seat that closed CE-t-8.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.4 @`19bf1c7322` (s.4 the schema, s.4.3 the enum as DATA, s.4.4 RULE T's FORM; s.7 row T-9 :610) · **Decomp cell:** `CE-t-9` (= manifest T-9; STAGE 2, "the 4.3 answer-state fixes, each closes on AC-2") · **Lane:** `.tools/comp-trigger` (the bash shim, ANY) + `org/modules/graph/comp_trigger.py` (the ENGINE) + `.tools/tests/**` (TOOL_BATTERIES); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-trigger.result.md` (owner by path). A lane refusal at commit is a ROW, never a self-grant. **Rule 27 seating:** `0.8.0_AE_CloudComp` BASE holds NFRA_COMPEFFICACY only (CE-t-8 terminal @`accf86b136`; continuity).

---

## THE CELL

Manifest T-9 (PRD s.7 :610): `comp-trigger` -> `comp_trigger.py`; 80 runs; "EventBridge+Scheduler only; blind to S3
notifications (COO preflight)". MEASURED at cut @`b7daeaa6f0`: the shim forwards to `org/modules/graph/comp_trigger.py`
(**344 lines**, read-only forensics: "what fires X / is the trigger enabled / did it actually fire / does terraform
declare it", the denominator on every scan, no write path); its own docstring `:20-21` says it "never reads S3 -- the mdpf
sentinel class (bucket-notification triggers) is out of v1 scope ON PURPOSE: the sentinel key is Door 6"; the absent-
trigger text `:194-195` says "an S3-notification/sentinel trigger would not appear here; v1 scans EventBridge rules +
Scheduler schedules only". So the blind spot is DECLARED in prose today; the cell's closes-on, verbatim from the decomp:
**"scope declared in header OR S3-notification backend via existing machinery; existing machinery checked FIRST."**
The 4.3 voice this audit grades: a subject whose trigger lives in a class the tool does not scan must read
NOT_APPLICABLE / out-of-scope on the answer line itself -- never PRESENT_WITH_ZERO_RESULTS ("no trigger") -- and every
answer carries the scope it was computed over. No battery exists for this tool at cut (0 files in `.tools/tests/`).

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-trigger.result.md`: one fenced JSON block
+ prose; the 31 required s.4 fields (4.1 identity from the ENGINE; 4.2 disclosure from a QUOTED default run; 4.3 the four
planted answer-state cases keyed on the RATIFIED enum `org/standards/COMPTOOL_ANSWER_STATE.enum.json` -- SUBJECT_ABSENT_
FROM_CORPUS: a Lambda/function name that does not exist in the account (the tool says absent, never "no trigger");
PRESENT_WITH_ZERO_RESULTS: a real function with no EventBridge rule and no Scheduler schedule; PARTIAL_OR_BLIND: a
function whose ONLY trigger is an S3 bucket notification (the mdpf sentinel class) -- must read out-of-scope/
NOT_APPLICABLE with the scope stated, never "no trigger"; NOT_APPLICABLE: a subcommand with no population; each case rc +
text quoted; live AWS READS ONLY, under the seat's standing role, one call per case; 4.4 Rule T's form APPLIED via the
ONE shared module `.tools/_compbudget.py` on every AWS-plane call and every sweep (list rules / list schedules /
CloudTrail lookups), the DEFERRED bucket for a call that would outlive the budget; 4.5 the passcraft moves; 4.6 usage
at BOTH instruments and the battery at BOTH grains). Then the ONE decision this cell owes, in the decomp's own words:
**existing machinery checked FIRST** -- does the estate already hold an S3-notification / sentinel reader (the shared
event graph, comp-aws, the mdpf sentinel tooling) that comp-trigger can DELEGATE to, or a scope declaration in the
HEADER (the answer line carries "scope: EventBridge rules + Scheduler schedules; S3 bucket notifications NOT scanned")?
Either is a valid close; the header declaration is the floor and lands regardless; the delegation lands ONLY if the
machinery exists and is measured (its file:line @ commit), never built here. Then the ONE code change: the header scope
line on every answer + the 4.3 out-of-scope voice for the S3-notification class (+ the delegation if found), the budget
carrier wired with `--help` disclosing it, and a NEW battery file `.tools/tests/test_comp_trigger_battery.py`.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T9-AC1" cell_refs="CE-t-9"/> `T9-AC1` -- the deliverable parses (one fenced JSON block), every required s.4 field present or explicitly ABSENT, 4.1 identity read from the ENGINE path, the shim named as the shim.
<criterion id="T9-AC2" cell_refs="CE-t-9"/> `T9-AC2` -- (AC-2) four PLANTED cases keyed on the ratified enum produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case); the S3-notification-only function reads out-of-scope / NOT_APPLICABLE with the scope on the line, NEVER "no trigger".
<criterion id="T9-AC3" cell_refs="CE-t-9"/> `T9-AC3` -- SCOPE DECLARED: every answer line carries the scope it was computed over (EventBridge rules + Scheduler schedules; S3 bucket notifications NOT scanned) -- quoted from a real run; the existing-machinery question answered with a measurement (file:line @ commit of what was found, or a MEASURED ZERO with its denominator), and the delegation landed ONLY if found.
<criterion id="T9-AC4" cell_refs="CE-t-9"/> `T9-AC4` -- (AC-4) Rule T's form applied: `--help` discloses the carrier via `_compbudget.py`; a planted small `--budget` on a sweep produces the s.4.4 expiry line with its source word and reached denominator, side by side with a clean completion line; an AWS-plane call that would outlive the budget lands in the DEFERRED bucket.
<criterion id="T9-AC5" cell_refs="CE-t-9"/> `T9-AC5` -- battery: the NEW `.tools/tests/test_comp_trigger_battery.py` with one arm per new behaviour (the scope line, the out-of-scope voice, the budget carrier) and a planted mutant per arm going RED; direct AND under pytest at the FILE grain; directory grain stated as it reads.
<criterion id="T9-AC6" cell_refs="CE-t-9"/> `T9-AC6` -- push state MEASURED at report (ls-remote + is-ancestor; LOCAL expected while Andrew gates the cadence, say which state was read); the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the seat commits itself.

<expected_criteria>T9-AC1, T9-AC2, T9-AC3, T9-AC4, T9-AC5, T9-AC6</expected_criteria>

## SURFACES

`.tools/comp-trigger` (the shim) · `org/modules/graph/comp_trigger.py` (344 lines; `:20-21` the declared S3 blind spot; `:194-195` the absent-trigger text; `:278` argparse) @`b7daeaa6f0` · `.tools/_compbudget.py` @`2718cffc45` · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` @`19bf1c7322` · the existing-machinery candidates to CHECK FIRST (never build): `comp-aws` / the shared event graph (`org/modules/graph/`), the mdpf sentinel tooling (`comp-schedule` C1 carrier) · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` · PRD s.4 + s.7 T-9 @`19bf1c7322` · precedents: `deliverables/0.8.0_AE_CloudComp/comp-iam.result.md` @`dace2c42b8`, `comp-find.result.md` @`6d04680f2b`.

## BOUNDS

- **READ-ONLY, always:** comp-trigger has no write path and gains none; no EventBridge rule, Scheduler schedule, S3 notification, IAM or Terraform resource is created, changed, enabled or disabled under this cell -- live calls are list/describe/lookup only, under the seat's standing role.
- **Existing machinery is CHECKED, never built:** an S3-notification backend lands only as a delegation to something the estate already runs, measured at file:line; if none exists the header declaration is the close and the gap is a FINDING with an owner.
- **No new dependency; no new file outside the engine, the shim, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` is consumed, not edited.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), then keep working; never a message.
- **Certifier != author:** the s.7 row-state word is the L4 owner's version bump on the L8/L9 seat's documentation, read from the record.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @b7daeaa6f0 (v0.2.2), cell CE-t-9 (s.1a, = manifest T-9; STAGE 2 in s.2; ROUND 4 fence).
<owned_cells>CE-t-9</owned_cells>
Read-dependencies, NOT claimed: CE-disc-2 / CE-tp-1 (DONE as spec), CE-t-1 / CE-t-2 / CE-t-3 / CE-t-8 (the form's applications, terminal), CE-t-7 (in parallel at the ~A lane -- no dependency either way), CE-t-5 (comp-schedule, STAGE 3 -- the sentinel carrier it may delegate to is read, not changed).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 20 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 3 -> 3, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or comp-trigger (read at 2026-09-03 08:09Z).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is comp-trigger's own VOICE, scope line and budget carrier; no AWS principal, policy or resource is created, changed or granted (BOUNDS: read-only, always); the tool's existing list/describe/lookup calls under the seat's standing role are unchanged in scope. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @a9aea6f3ce (2026-09-03T08:16:17Z); 9/9 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged = this order's two OUTPUTS (the deliverable and the proof instance, GONE by construction at cut); uncited neighborhood 261 (25 shown, cap declared); --no-packet (stage 4 pointers only, the caller's choice, recorded in the declaration).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T9-AC1`..`T9-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-9.comp-trigger-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself.
T9-AC2's S3-notification case and T9-AC5's planted mutants are the controls that must be able to FAIL; every `surprises`
entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_trigger.py --for "where an answer line is printed, where the scan's classes are enumerated, and where a subject with no trigger is reported"`; `comp-which "does the estate have an S3 bucket-notification / sentinel trigger reader"` and `comp-find -i 'NotificationConfiguration|bucket_notification|sentinel' org/modules/graph .tools infra/aws --files` (existing machinery FIRST, denominators printed). BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the new battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-trigger <function>` from a seat other than this one (the ~A lane is the nearest; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record, not a message) with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
