# TO NFRA_COMPEFFICACY.TO-CE-T-14 -- comp-drift: the s.4 per-tool audit deliverable on the propagation-drift ORCHESTRATOR (853 lines; 1 run/30 d; walks drift-topology.yaml CALLING the seam engines, never re-implementing them; exit 0 clean / 1 integrity-break / 2 UNVERIFIABLE) -- rc IS a verdict (FWD-10 row: a budget-cut walk never returns 0), the 4.3 four-case test with UNVERIFIABLE kept distinct as the tool's own PARTIAL_OR_BLIND voice, the --deep cost guard under Rule T's form, the overlap with comp-similar recorded BY NAME ONLY

<to_id>NFRA_COMPEFFICACY.TO-CE-T-14</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~G</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete -- lane commit 9334701e712cb99f606e4ab755a7788f4c053d04; proof-of-spec-check VALID before this flip; report push state measured local-only (origin/CLOUD 351f309e0a6ded1a5a5bdf3aacec18a5f9f8dbee, ancestry rc=1). Authority: round 6 of the canonical loop on NFRA_COMPEFFICACY, decomp v0.2.4 @39515415cc, PRD v0.5 @5bbdab5ec7.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` · **Decomp cell:** `CE-t-14` (STAGE 3; closes on "graded; overlap with comp-similar recorded as BY NAME ONLY") · **Lane:** `.tools/comp-drift` (15-line shim; exports COMP_DRIFT_BASH for the engine subprocesses) + `org/modules/graph/drift_cli.py` (the ENGINE, 853 lines) + `drift-topology.yaml` (READ) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~G/comp-drift.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~G` (a CODEX seat, Andrew 13:4xZ) holds NFRA_COMPEFFICACY only.

---

## THE CELL

Manifest T-14 (PRD s.7): `comp-drift` -> `.tools/comp-drift`; 1 run / 30 d; orchestrator over seam engines; `--deep` cost-guarded. The shim's
own header: `coverage` (the coverage ledger -- what is unguarded today), `<target>` (walk one artifact's chain), `sweep [--deep]` (fan out
across every seam -> board); `--json` on any; **exit 0 clean / 1 integrity-break / 2 UNVERIFIABLE**. So its rc IS a verdict: the s.4.4
verdict-bearing row (FWD-10) applies -- a budget-cut sweep must never return 0, and UNVERIFIABLE (rc 2) is the tool's own PARTIAL_OR_BLIND
voice already. The decomp's closes-on: **"graded; overlap with comp-similar recorded as BY NAME ONLY."**

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-drift.result.md`: the 31 required s.4 fields (4.1 identity from the ENGINE, the shim named as the shim, the seam engines it CALLS
enumerated from drift-topology.yaml with denominators (never re-implemented -- PRD arch-gate b); 4.2 disclosure from a QUOTED default
`coverage` run and a `sweep` run; 4.3 the four planted answer-state cases on the ratified enum -- SUBJECT_ABSENT_FROM_CORPUS (a target no
topology names), PRESENT_WITH_ZERO_RESULTS (a real artifact whose chain walks clean -- rc 0 with its denominator), PARTIAL_OR_BLIND (a seam
engine that could not run -- the tool's own UNVERIFIABLE, rc 2, in its own voice, naming the engine), NOT_APPLICABLE (a mode with no
population); rc + text quoted; the GRAIN sentence; 4.4 Rule T's form via `_compbudget.py` on the `sweep` fan-out (and on `--deep`, whose
cost guard is measured and stated in the form's terms) with the VERDICT-BEARING row: at BUDGET REACHED the sweep prints the line AND
returns a NON-CLEAN rc distinct from 0 (clean) and 1 (integrity-break) -- whether that is the existing 2 (UNVERIFIABLE, "the walk could
not be completed" is exactly what a partial sweep is) or a new value is the cell's measured call, stated on `--help`; the cursor as in
s.4.4; 4.5; 4.6 usage at BOTH instruments and the battery at BOTH grains). Then the ONE code change (tokens, the budget carrier, the
non-clean expiry rc) and a NEW battery `.tools/tests/test_comp_drift_battery.py` with a RED mutant per arm (the mutant returning 0 on a
partial sweep among them). **The overlap with comp-similar is recorded BY NAME ONLY** (different corpus, different question), never
merged or re-scoped here.

## ACCEPTANCE

<criterion id="T14-AC1" cell_refs="CE-t-14"/> `T14-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT; 4.1 from the ENGINE with the seam engines enumerated from the topology (denominator); the shim named as the shim.
<criterion id="T14-AC2" cell_refs="CE-t-14"/> `T14-AC2` -- (AC-2) four PLANTED cases on the ratified enum produce four DISTINCT state tokens within one invocation (rc + text quoted); UNVERIFIABLE names the seam engine that could not run.
<criterion id="T14-AC3" cell_refs="CE-t-14"/> `T14-AC3` -- OVERLAP RECORDED BY NAME ONLY: the comp-similar overlap stated as a name-level note with the two tools' corpora and questions; zero re-scoping or merging (diff shown); the seam engines' check logic untouched (arch-gate b).
<criterion id="T14-AC4" cell_refs="CE-t-14"/> `T14-AC4` -- (AC-4) Rule T's form + the verdict-bearing row: `--help` discloses the carrier and the whole rc vocabulary; a planted small `--budget` on `sweep` produces the expiry line AND a non-clean rc (never 0), read by an rc-only consumer as NOT clean, with the cursor followed to a complete sweep whose rc is the true verdict; the `--deep` cost guard measured and stated.
<criterion id="T14-AC5" cell_refs="CE-t-14"/> `T14-AC5` -- battery NEW with a RED mutant per arm, direct AND pytest at the FILE grain; commit-gate clean on every .py touched.
<criterion id="T14-AC6" cell_refs="CE-t-14"/> `T14-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself.

<expected_criteria>T14-AC1, T14-AC2, T14-AC3, T14-AC4, T14-AC5, T14-AC6</expected_criteria>

## SURFACES

`.tools/comp-drift` (15 lines) · `org/modules/graph/drift_cli.py` (853 lines) @39515415cc · `drift-topology.yaml` (READ) · the seam engines it calls (READ only) · `.tools/_compbudget.py` @`2718cffc45` (consumed) · `org/modules/graph/comp_dataflow.py:cmd_gate` @`72e7846ca7` (the verdict-bearing precedent) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` · PRD s.4 + s.7 T-14 @`5bbdab5ec7`.

## BOUNDS

- **The seam engines are CALLED, never edited or re-implemented** (arch-gate b); the topology is READ.
- **The clean / integrity-break semantics on a complete sweep do not change**; only expiry gains the non-clean path.
- **No new dependency; no new file outside the engine, the shim, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` consumed, not edited.
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; surfaced_by = this seat; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @39515415cc (v0.2.4), cell CE-t-14 (s.1a; STAGE 3; ROUND 6 fence).
<owned_cells>CE-t-14</owned_cells>
Read-dependencies, NOT claimed: CE-t-12 (comp-similar, in parallel at ~F -- the overlap is a name-level note), CE-t-25 (the verdict-bearing precedent, DONE), CE-tp-1 (DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 6 -> 6, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or this order's tool (read at 2026-09-03 14:23Z, the file's only token hit being the tool's own header line).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-drift orchestrates repo-local seam engines; no AWS principal, policy or resource is read or changed by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @07601c54c9 (2026-09-03T14:26:46Z); 5/5 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged (2 flagged path(s): NFRA_COMPEFFICACY.TO-CE-T-14.comp-drift-s4-audit.proof_of_spec.json GONE; comp-drift.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (stage 4 pointers only, the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T14-AC1`..`T14-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~G/NFRA_COMPEFFICACY.TO-CE-T-14.comp-drift-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. T14-AC4's partial-sweep rc
and T14-AC5's mutants are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/drift_cli.py --for "the three modes, how the seam engines are invoked, the rc mapping 0/1/2, the --deep cost guard, every fan-out loop"`; `comp-read drift-topology.yaml --for "the seams and their engines"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real budget-cut `comp-drift sweep` from a seat other than this lane, read through an rc-only consumer -- FWD-9 and FWD-10's DONE WHEN from a second seat.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after, the rc vocabulary, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
