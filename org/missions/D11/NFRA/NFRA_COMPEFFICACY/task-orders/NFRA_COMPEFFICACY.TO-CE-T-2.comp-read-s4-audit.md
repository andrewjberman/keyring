# TO NFRA_COMPEFFICACY.TO-CE-T-2 -- comp-read: the s.4 per-tool audit deliverable, the 4.3 four-case test, and Rule T on its one timeout-carrying subprocess

<to_id>NFRA_COMPEFFICACY.TO-CE-T-2</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~A</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T05:33:58Z) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-2.comp-read-s4-audit.proof_of_spec.json; T2-AC1..AC6 self-assessed PASS; CVO grade pending -- certifier != author.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.4 @`19bf1c7322` (s.4 the schema, s.4.3 the enum as DATA, s.4.4 RULE T's FORM; s.7 row T-2) · **Decomp cell:** `CE-t-2` (= manifest T-2; STAGE 1, the rail pair's second) · **Lane:** `.tools/comp-read` (ANY) and `.tools/tests/**` (TOOL_BATTERIES); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-read.result.md`.

---

## THE CELL

Manifest T-2 (PRD s.7 :603): `comp-read` -> `.tools/comp-read` (Python, **1,038 lines at HEAD @`f54000091d`**); 2,401 runs
(rail); Rule 21's single-file instrument (the `--for` / `--enumerate` modes every seat reads with). Already landed and
CLEARED on their own instruments: unit 1 (runs.jsonl logging, @`f34122edfb` ON origin), the shebang routing
@`8ed23144cb`, the battery `.tools/tests/test_comp_read_enumerate.py` (8 of 8 at the decomp's read). **What is NOT
done: the s.4 deliverable itself, the 4.3 four-case test against the RATIFIED enum, and Rule T's form on the tool.**
MEASURED at cut: comp-read carries NO corpus-width loop (one file per call) and ONE timeout-carrying subprocess --
`:1027-1030` `subprocess.run(... timeout=20)`, the telemetry sink -- and no `--budget` / `COMP_BUDGET_S` / `_compbudget`
carrier (0 hits); the PAGE contract is present (`:488` "PAGE i of N", `:494` MORE line). Decomp cell CE-t-2 reads
IN-FLIGHT with exactly those owed; its finding "`--enumerate` writes no rail row" is a FINDING to carry, not this
cell's fix.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-read.result.md`: one fenced JSON block +
prose; the 31 required s.4 fields (4.1 identity from the ENGINE not a shim; 4.2 disclosure from a QUOTED default run;
4.3 the four planted answer-state cases keyed on the RATIFIED enum `org/standards/COMPTOOL_ANSWER_STATE.enum.json`
(SUBJECT_ABSENT_FROM_CORPUS, PRESENT_WITH_ZERO_RESULTS, PARTIAL_OR_BLIND, NOT_APPLICABLE) in the tool's own voice;
4.4 bounds with Rule T's form APPLIED as s.4.4 states it for a tool of this class -- the carrier `--budget` > env
`COMP_BUDGET_S` > default via the ONE shared module `.tools/_compbudget.py` (never a per-tool copy), the source word on
the denominator line, the `:1030` subprocess timeout derived from `remaining()`, and the NON-APPLICATION half stated
honestly: with no corpus-width loop the expiry line may never be reachable in practice -- say so, with the one line a
planted `--budget` of 0.001 s DOES produce; 4.5 the passcraft moves; 4.6 usage at BOTH instruments and the battery
at BOTH grains). Then the ONE code change this cell owes: the budget carrier wired through `_compbudget.py`, the `:1030`
timeout from `remaining()`, `--help` disclosing the carrier. **Neither the read semantics nor the pagination changes**
(the 8-arm battery is the control).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T2-AC1" cell_refs="CE-t-2"/> `T2-AC1` -- the deliverable parses (one fenced JSON block), every required s.4 field present or explicitly ABSENT, 4.1 identity read from the engine path.
<criterion id="T2-AC2" cell_refs="CE-t-2"/> `T2-AC2` -- (AC-2) four PLANTED cases keyed on the ratified enum -- a file absent from the corpus, a file present with zero hits for the pattern, a partial/blind read (a binary or an unreadable file), and a healthy hit -- produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case).
<criterion id="T2-AC3" cell_refs="CE-t-2"/> `T2-AC3` -- (AC-4) Rule T's form applied: `--help` discloses the carrier (`--budget` > env `COMP_BUDGET_S` > default) via `_compbudget.py`; a planted `--budget 0.001` produces the s.4.4 expiry line with its source word and reached denominator, distinguishable from a clean run's completion line (the pair shown side by side); the `:1030` timeout reads from `remaining()`; the non-application half (no corpus-width loop) stated in the deliverable in the class the form names.
<criterion id="T2-AC4" cell_refs="CE-t-2"/> `T2-AC4` -- battery: `.tools/tests/test_comp_read_enumerate.py` stays GREEN on production at the FILE grain, its arms unchanged, plus ONE new arm for the budget carrier (a planted mutant that ignores `--budget` must go RED); directory grain stated as it reads (CTO's three files noted if still aborting).
<criterion id="T2-AC5" cell_refs="CE-t-2"/> `T2-AC5` -- the "`--enumerate` writes no rail row" finding carried in the deliverable with an OWNER named (a `comp-which-rail.log` matter), not fixed here.
<criterion id="T2-AC6" cell_refs="CE-t-2"/> `T2-AC6` -- push state MEASURED at report (ls-remote + is-ancestor; LOCAL expected under Andrew's push hold, say which state was read); the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the seat commits itself (lane ANY on task-orders/**).

<expected_criteria>T2-AC1, T2-AC2, T2-AC3, T2-AC4, T2-AC5, T2-AC6</expected_criteria>

## SURFACES

`.tools/comp-read` (1,038 lines; `:488`/`:494` the PAGE contract; `:1027-1030` `subprocess.run(... timeout=20)`) @`f54000091d` · `.tools/_compbudget.py` @`2718cffc45` (the form's one shared module; comp-find is the reference application) · `.tools/tests/test_comp_read_enumerate.py` · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` @`19bf1c7322` · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` (the two usage instruments; the 80-char `args_head` sink trap applies) · PRD s.4 + s.7 T-2 @`19bf1c7322`.

## BOUNDS

- **Read semantics and pagination do NOT change** (the 8-arm battery is the control). The `--for` scoring and the `--enumerate` banding are not touched.
- **No new dependency; no new file outside the two named** (the tool, its battery) plus the deliverable + proof instance. `_compbudget.py` is consumed, not edited (its owner is CE-g-5's seat this round; a needed change there is a ROW, not an edit).
- **Truthful non-application stays truthful:** a tool with no corpus-width loop does not manufacture a scan denominator; it prints the form's line for its class.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), then keep working; never a message.
- **Certifier != author:** the s.7 row-state word is the L4 owner's version bump on the L8/L9 seat's documentation, read from the record.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @f54000091d (v0.2), cell CE-t-2 (s.1a, = manifest T-2; STAGE 1 in s.2; ROUND 2 fence "CE-t-2 in PARALLEL at a second Tier-2 seat").
<owned_cells>CE-t-2</owned_cells>
Read-dependencies, NOT claimed: CE-t-1 (the client-side form's first application, terminal @fc5ec7106c), CE-tp-1 (Rule T's form, DONE as spec), CE-disc-2 (the enum, DONE as spec), CE-t-3 (comp-which follows this cell), CE-g-5 (the engine layer, in parallel at the base seat -- no dependency either way).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 0 armed gates name NFRA_COMPEFFICACY or comp-read (read at 2026-09-03 04:36Z).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-read is a repo-local Python tool over one file; no AWS principal, policy or resource is read or changed by it or by this TO, so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @8c366948b3 (2026-09-03T04:42:21Z); cited commits 8 attempted / 8 verified / 0 UNVERIFIABLE; cited paths 6 attempted / 4 stable / 2 flagged (both = the deliverable and the proof instance this TO CREATES -- expected, not stale). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T2-AC1`..`T2-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-2.comp-read-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself.
T2-AC3's side-by-side pair and T2-AC4's planted mutant are the controls that must be able to FAIL; every `surprises`
entry opens with a row id that resolves in the project's channel (the SURPRISES limb refuses the flip otherwise).
</proof_of_spec>
