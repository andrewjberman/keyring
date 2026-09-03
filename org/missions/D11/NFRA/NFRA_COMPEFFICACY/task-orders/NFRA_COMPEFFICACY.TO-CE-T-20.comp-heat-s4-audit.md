# TO NFRA_COMPEFFICACY.TO-CE-T-20 -- comp-heat: the s.4 per-tool audit deliverable on a tool with ZERO CLI runs whose only consumer is a LIBRARY call (comp-similar's load_heat_live()) and the estate report's wiring -- graded AS A LIBRARY SURFACE with its CLI stated as unused; the 4.3 four-case test at the library grain; Rule T's form where it sweeps; the daily-report wiring is @09355b6d93's and not this cell's

<to_id>NFRA_COMPEFFICACY.TO-CE-T-20</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~I</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut. Authority: round 6 of the canonical loop on NFRA_COMPEFFICACY -- CVO's round-5 stamp -- the round-5 L10 precondition TERMINAL since 12:42Z (12 orders: 9 complete, 3 WITHDRAWN with rows, 0 pending; the stamp being written at 3.0.0_SA_CVO, ETA this tick, 93690) -- cut on the terminal precondition per /drive v2 obligation 2 (LD-0530) --, decomp v0.2.4 @39515415cc (STAGE 3 wide on Andrew's word "/drive COMPEFFICACY to completion." @dd040c447b; CE-t-20 at the ~I lane), PRD v0.5 @5bbdab5ec7 (s.4; s.7 row T-20).</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (s.7 T-20: "0 CLI runs; library consumer = comp-similar `load_heat_live()`; named in the estate report") · **Decomp cell:** `CE-t-20` ("0 CLI runs; library consumer only; invoked by nothing"; closes on "graded; the daily-report wiring is @09355b6d93's, not this cell's") · **Lane:** `.tools/comp-heat` (377 lines -- the engine IS the shim; measure) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~I/comp-heat.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~I` (a CODEX seat, Andrew 13:4xZ) holds NFRA_COMPEFFICACY only.

---

## THE CELL

Manifest T-20 (PRD s.7): `comp-heat` -> `.tools/comp-heat` (377); 0 CLI runs; library consumer = comp-similar's `load_heat_live()`; named
in the estate report. A tool nobody invokes at the CLI is graded at the grain where it IS used: as a LIBRARY (its import surface, what it
returns, its failure voice when the heat source is absent or stale) -- and the estate-report wiring that names it is @`09355b6d93`'s and is
recorded, not this cell's to touch. The decomp's closes-on: **"graded; the daily-report wiring is @09355b6d93's, not this cell's."**

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-heat.result.md`: the 31 required s.4 fields (4.1 identity: the file is the engine; state whether a CLI entry exists at all and
what `load_heat_live()` is; 4.2 disclosure from a QUOTED run of the library call (a two-line python driver) and of the CLI if one
exists; 4.3 the four planted answer-state cases on the ratified enum AT THE LIBRARY GRAIN -- SUBJECT_ABSENT_FROM_CORPUS (a heat key no
source carries), PRESENT_WITH_ZERO_RESULTS (a real key with zero heat, said so), PARTIAL_OR_BLIND (the heat source absent or stale -- the
library must RAISE or return a typed state in its own voice, never an empty structure that a caller reads as "no heat"; measure what it
does today and grade it), NOT_APPLICABLE (a mode with no population); rc / return + text quoted; the GRAIN sentence applied to a
library: the STATE is carried in the RETURN, not a print; 4.4 Rule T's form where the library sweeps a corpus (if it does; else the
non-application half stated) with rc execution-only (a library's return is a measurement; its consumer comp-similar's voice is graded
in CE-t-12); 4.5; 4.6 usage at BOTH instruments (0 CLI runs stated with the denominator; the library call census from comp-similar's
source) and the battery at BOTH grains). Then the ONE code change (a typed absent/stale state on the library return + the CLI's 4.3
tokens if a CLI exists) and a NEW battery `.tools/tests/test_comp_heat_battery.py` with a RED mutant per arm (the mutant returning an
empty structure for an absent source among them). **The estate-report wiring (@09355b6d93) is recorded and not changed.**

## ACCEPTANCE

<criterion id="T20-AC1" cell_refs="CE-t-20"/> `T20-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT; 4.1 states the engine/shim identity and the library surface; 4.2 quotes a real library-driver run (and the CLI if one exists).
<criterion id="T20-AC2" cell_refs="CE-t-20"/> `T20-AC2` -- (AC-2) four PLANTED cases at the library grain produce four DISTINCT typed states (return/raise + text quoted); an absent or stale heat source never comes back as an empty structure a caller reads as "no heat".
<criterion id="T20-AC3" cell_refs="CE-t-20"/> `T20-AC3` -- THE WIRING RECORDED, NOT CHANGED: the estate-report wiring @09355b6d93 and comp-similar's `load_heat_live()` call named with file:line; zero change to either consumer (diff shown); 0 CLI runs stated with the denominator.
<criterion id="T20-AC4" cell_refs="CE-t-20"/> `T20-AC4` -- (AC-4) Rule T's form applied where a sweep exists (`--budget` on the CLI or a budget parameter on the library call, disclosed) or its non-application stated in the form's own class; rc / return execution-only stated.
<criterion id="T20-AC5" cell_refs="CE-t-20"/> `T20-AC5` -- battery NEW with a RED mutant per arm, direct AND pytest at the FILE grain; commit-gate clean on every .py touched; comp-similar's consumption still passes (its battery arm re-run).
<criterion id="T20-AC6" cell_refs="CE-t-20"/> `T20-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself.

<expected_criteria>T20-AC1, T20-AC2, T20-AC3, T20-AC4, T20-AC5, T20-AC6</expected_criteria>

## SURFACES

`.tools/comp-heat` (377 lines) @39515415cc · `org/modules/graph/debtscan/comp_similar.py` (`load_heat_live()` -- READ) · the estate-report wiring @`09355b6d93` (READ) · the heat source it reads (measure) · `.tools/_compbudget.py` @`2718cffc45` (consumed if a sweep exists) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` · PRD s.4 + s.7 T-20 @`5bbdab5ec7`.

## BOUNDS

- **The consumers are READ, never edited** (comp-similar is CE-t-12's at ~F; the report wiring is @09355b6d93's).
- **No new dependency; no new file outside the engine, the NEW battery, the deliverable and the proof instance.**
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; surfaced_by = this seat; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @39515415cc (v0.2.4), cell CE-t-20 (s.1a; STAGE 3; ROUND 6 fence).
<owned_cells>CE-t-20</owned_cells>
Read-dependencies, NOT claimed: CE-t-12 (comp-similar, in parallel at ~F -- its call of this library is READ here), CE-tp-1 (DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 6 -> 6, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or this order's tool (read at 2026-09-03 14:23Z, the file's only token hit being the tool's own header line).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-heat reads a repo-local heat source; no AWS principal, policy or resource is read or changed by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @07601c54c9 (2026-09-03T14:27:30Z); 5/5 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 6 attempted / 4 stable / 2 flagged (2 flagged path(s): NFRA_COMPEFFICACY.TO-CE-T-20.comp-heat-s4-audit.proof_of_spec.json GONE; comp-heat.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (stage 4 pointers only, the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T20-AC1`..`T20-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~I/NFRA_COMPEFFICACY.TO-CE-T-20.comp-heat-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. T20-AC2's absent-source case
and T20-AC5's mutants are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read .tools/comp-heat --for "the library surface, what it returns when the heat source is absent or stale, whether a CLI entry exists, every corpus-width loop"`; `comp-read org/modules/graph/debtscan/comp_similar.py --for "load_heat_live and what it does with the return"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real library call from a seat other than this lane -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
