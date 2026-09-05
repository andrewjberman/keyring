# TO NFRA_COMPEFFICACY.TO-CE-T-25 -- comp-dataflow `gate` under FWD-10: a verdict-bearing tool never returns its clean verdict from a partial run -- at BUDGET REACHED the Rule T line prints AND the rc is non-clean, distinct from both the clean and the failing verdict, carrying NOT-DECIDABLE in the tool's own voice; EXERCISED by an rc-only consumer

<to_id>NFRA_COMPEFFICACY.TO-CE-T-25</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~A</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T12:13:54Z) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-25.comp-dataflow-gate-under-fwd10.proof_of_spec.json; T25-AC1..AC5 self-assessed PASS (deliverable comp-dataflow.fwd10.result.md at the lane's own folder); CVO grade (CONFORMING/CLEARED) pending -- certifier != author. cmd_gate now returns RC_NOT_DECIDABLE (4) at BUDGET REACHED, always, distinct from RC_CLEAN (0) and RC_FINDINGS (1); EXERCISED end-to-end per FWD-10's DONE WHEN (a real rc-only consumer correctly bails, the cursor followed to completion yields the true verdict) -- which surfaced and required fixing a SEPARATE, previously-unknown bug (total_units measured before the --cursor filter, so a resumed sweep could never reach a true verdict) in the same commit. S14 disarmed via surprise-channel row NFRA_COMPEFFICACY-S16@710819ddc6 (hazard_standing INERT, disposition left for 3.0.0_SA_CVO's own L9 adjudication per the TO's own words). Push state MEASURED 2026-09-03T12:13:54Z (ls-remote + is-ancestor): origin/CLOUD @3bd8d2ef04; all three of this cell's commits (72e7846ca7, 710819ddc6, 1bf60cae74) read LOCAL ONLY (is-ancestor rc=1) -- the expected state while Andrew gates the push cadence. Prior history: pending -- GO paired at cut. Authority: the round-4 L10 stamp @153522a509 (S14 SCOPE_CHANGE, REQUIRES_UNNAMED_OUTCOME, loop_target 2) -> the L2 re-entry adjudicated by 1.0.0_SA_CTO (CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260903T0930Z.md, CALL 1 ruled (a)) -> PRD v0.5 @5bbdab5ec7 (FWD-10 appended; s.4.4 gains the `verdict-bearing` row) -> decomp v0.2.3 @dcf07b4799 (CE-t-25 ADDED; ROUND 5 fence). Continuity and the S14 disarm owner: 0.8.0_AE_CloudComp~A, the lane that built cmd_gate's Rule T form in CE-t-7.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (FWD-10; s.4.4 the `verdict-bearing` row; s.7 row T-7) · **Decomp cell:** `CE-t-25` (ADDED v0.2.3; closes on the FWD-10 ACCEPT clause quoted) · **Lane:** `.tools/comp-dataflow` (ANY) + `org/modules/graph/comp_dataflow.py` (the ENGINE) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.fwd10.result.md` (a NEW file beside the round-4 audit, which stays as its record). **Rule 27 seating:** `0.8.0_AE_CloudComp~A` holds NFRA_COMPEFFICACY only.

---

## THE CELL, AND WHY THIS ORDER EXISTS

The round-4 order TO-CE-T-7 (@`8fdc3d0602`) wired Rule T's form onto cmd_gate exactly as s.4.4 v0.4 said -- and its own F4 named the
consequence: a BUDGET-REACHED partial sweep with 0 findings among the files it reached returns rc 0, byte-identical to a complete
clean sweep, on a tool whose rc IS its verdict. The CVO routed it SCOPE_CHANGE (S14 @`153522a509`); the L4 owner named the outcome
at L2 and re-issued the PRD as v0.5. Nothing was built against the old form; this is the first order against the new one.

THE BAR THIS ORDER CLOSES ON, QUOTED FROM PRD v0.5 @`5bbdab5ec7`, NOT RESTATED:
> **FWD-10** A tool whose exit code is its verdict never returns the clean verdict from a partial run: at budget expiry it says
> so in its own voice and exits in a way no reader can mistake for clean, and it tells the reader where to resume.
> **DONE WHEN** EXERCISED -- a budget-cut sweep of a verdict-bearing tool has been read by an rc-only consumer (a hook, a
> script, an `&&`) as NOT clean, and its resume cursor has been followed to completion.
> **ACCEPT** for every marquis tool whose rc carries a verdict (a gate, a deny-test, a check): at BUDGET REACHED the line
> prints as Rule T requires AND the rc is a non-clean value distinct from both the clean verdict and the failing one, carrying
> the PARTIAL_OR_BLIND state in the tool's voice (`NOT-DECIDABLE`); a consumer that reads only the rc cannot read a prefix as
> CLEAN; the cursor resumes as in s.4.4.
> **s.4.4 `verdict-bearing` row:** a tool whose rc IS its verdict -- a gate, a deny-test, a check -- prints the BUDGET REACHED
> line exactly as above and returns a NON-CLEAN rc distinct from both the clean verdict and the failing one, carrying
> PARTIAL_OR_BLIND in its own voice ("NOT-DECIDABLE", the enum's tool-voice token; iam_cli.py returns it as rc 2 today); the
> "rc stays 0" clause above governs every NON-verdict tool and nothing else; the cursor is unchanged. A verdict-bearing tool
> that returns its clean rc at expiry FAILS Rule T whatever its line says.

## DELIVERABLE

1. **cmd_gate at BUDGET REACHED** prints the s.4.4 line exactly as today AND returns a non-clean rc distinct from the clean
   verdict (0) and from the failing verdict (the rc a COMPLETE sweep with findings returns today -- MEASURE it and state it),
   carrying `NOT-DECIDABLE` as the state token on the line; the resume cursor is unchanged. `iam_cli.py`'s rc 2 is the
   family precedent -- adopt the same value unless cmd_gate's existing rc vocabulary already occupies 2, in which case pick
   the next unoccupied value and STATE the whole rc vocabulary on `--help` (clean / findings / NOT-DECIDABLE / usage-or-crash).
2. **EXERCISED by an rc-only consumer** (the FWD-10 DONE WHEN): a real shell conjunction or a tiny hook script reads a
   `--budget`-cut `gate` sweep over the full 532-file tree as NOT clean (it does not proceed past the `&&`), then the cursor is
   followed with `--cursor` to completion and the final complete sweep's rc is the true verdict. Both runs quoted, rc + line.
3. **The non-verdict half untouched and stated:** `origin` (one file, no sweep) keeps its rc semantics and shows neither
   flag -- the structural non-application already recorded in CE-t-7; the "rc stays 0" clause now governs only non-verdict
   tools and comp-dataflow's `gate` is not one.
4. **The battery** `.tools/tests/test_comp_dataflow_battery.py` gains arms: budget-cut sweep -> NOT-DECIDABLE rc + line;
   complete clean sweep -> rc 0; complete sweep with findings -> the failing rc; the planted mutant that returns 0 at expiry
   goes RED; the round-4 arms (never-guess first) stay green; direct AND under pytest at the FILE grain.
5. **The deliverable** `comp-dataflow.fwd10.result.md`: the FWD-10 ACCEPT clause and the s.4.4 row quoted verbatim, the rc
   vocabulary table, the two exercised runs, the S14 disarm line (fix commit), production sha before/after.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T25-AC1" cell_refs="CE-t-25"/> `T25-AC1` -- THE BAR, QUOTED: the deliverable quotes FWD-10's ACCEPT clause and the s.4.4 `verdict-bearing` row verbatim; a real `--budget`-cut `gate` sweep prints the BUDGET REACHED line AND returns the non-clean rc carrying `NOT-DECIDABLE`, distinct from both the clean rc and the measured failing rc; the whole rc vocabulary is on `--help` and in the deliverable.
<criterion id="T25-AC2" cell_refs="CE-t-25"/> `T25-AC2` -- EXERCISED (FWD-10 DONE WHEN): an rc-only consumer (a shell conjunction or a tiny hook, quoted) reads the budget-cut sweep as NOT clean and does not proceed; the cursor is then followed to completion and the complete sweep's rc is the true verdict; both runs quoted with rc + line.
<criterion id="T25-AC3" cell_refs="CE-t-25"/> `T25-AC3` -- NON-APPLICATION STATED: `origin`'s rc semantics unchanged (diff shown); the round-4 cursor resume still skips exactly the completed units; the item-9 semantics (served-origin flagging, exemptions) untouched.
<criterion id="T25-AC4" cell_refs="CE-t-25"/> `T25-AC4` -- battery: the three verdict arms + the RED mutant that returns 0 at expiry, the round-4 arms still green, direct AND pytest at the FILE grain, directory grain stated as it reads; commit-gate clean on every .py touched.
<criterion id="T25-AC5" cell_refs="CE-t-25"/> `T25-AC5` -- the proof instance VALID with a `surprises` entry resolving to `NFRA_COMPEFFICACY-S14@153522a509` carrying the fix commit as this lane's DISARM (disarm_owner 0.8.0_AE_CloudComp~A; the disposition stays 3.0.0_SA_CVO's); push state MEASURED at report; the complete flip self-committed.

<expected_criteria>T25-AC1, T25-AC2, T25-AC3, T25-AC4, T25-AC5</expected_criteria>

## SURFACES

`org/modules/graph/comp_dataflow.py` @`8fdc3d0602` (cmd_gate, the budget carrier, the cursor) · `.tools/comp-dataflow` · `.tools/_compbudget.py` @`2718cffc45` (consumed, not edited -- unless the family's expiry rc belongs in the shared module, in which case that is a FINDING routed up, not an edit here) · `org/modules/graph/iam_cli.py:50` STATE_NOT_DECIDABLE (the rc-2 precedent, READ) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `.tools/tests/test_comp_dataflow_battery.py` @`8fdc3d0602` · `deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.result.md` @`803539f490` (its F4 is the origin of this cell; READ) · the S14 rows @`153522a509` · `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260903T0930Z.md` @`5bbdab5ec7`.

## BOUNDS

- **SOURCE plane only, zero AWS calls;** no change to what the gate FLAGS (item-9 semantics), only to what it RETURNS at expiry.
- **`_compbudget.py` is consumed, not edited** by this order: if the expiry rc for verdict-bearing tools belongs in the shared module (so the next verdict-bearing cell inherits it), say so in a FINDING with the proposed shape -- the L4 owner and the sequencer place it; do not land a shared-module change under a one-tool cell.
- **No new dependency; no new file outside the engine, the shim, the battery, the deliverable and the proof instance.**
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @dcf07b4799 (v0.2.3), cell CE-t-25 (ADDED v0.2.3; s.1a; ROUND 5 fence).
<owned_cells>CE-t-25</owned_cells>
Read-dependencies, NOT claimed: CE-t-7 (DONE -- this cell's parent), CE-tp-1 (the form, DONE at L4), CE-t-8 (the rc-2 precedent, DONE), CE-t-9 / CE-t-19 (in parallel; no dependency any way).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 21 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 4 -> 4, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or comp-dataflow (read at 2026-09-03 09:27Z).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-dataflow is a repo-local Python tool over parsed producer source; the change is to its exit code at budget expiry; no AWS principal, policy or resource is read or changed. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @dcf07b4799 (2026-09-03T11:14:53Z); 6/6 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged = this order's two OUTPUTS (the new deliverable and the proof instance, GONE by construction at cut); uncited neighborhood 574 (25 shown, cap declared); --no-packet (stage 4 pointers only, the caller's choice, recorded in the declaration).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T25-AC1`..`T25-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-25.comp-dataflow-gate-under-fwd10.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. The `surprises`
entry for S14 is REQUIRED (the disarm carrier); T25-AC2's consumer and T25-AC4's mutant are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_dataflow.py --for "cmd_gate's return paths: the clean rc, the findings rc, and what happens at BUDGET REACHED"`; `comp-read org/modules/graph/iam_cli.py --for "how STATE_NOT_DECIDABLE maps to the process exit code"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real budget-cut `comp-dataflow gate` from a seat other than this lane, read through a shell conjunction (the base seat or ~B is the nearest; the L8 seat reads the record) -- FWD-9 and FWD-10's DONE WHEN from a second seat.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record) with per-criterion evidence, production sha before/after, the rc vocabulary, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
