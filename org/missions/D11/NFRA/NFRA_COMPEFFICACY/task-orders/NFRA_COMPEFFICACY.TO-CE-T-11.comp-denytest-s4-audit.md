# TO NFRA_COMPEFFICACY.TO-CE-T-11 -- comp-denytest: the s.4 per-tool audit deliverable on the VERIFY-pillar deny-test (413 lines; 2 runs/30 d, 8 ever; the expected verdict DERIVED from the plan's change type so an author can neither pick nor hold the criterion wrong) -- a DENY-TEST is verdict-bearing by construction (FWD-10 row); the 4.3 four-case test on the OFFLINE plane; "zero population without an IAM change is CORRECT" recorded; the RETIRE-candidate on usage SURFACED, never acted here

<to_id>NFRA_COMPEFFICACY.TO-CE-T-11</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~E</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut. Authority: round 6 of the canonical loop on NFRA_COMPEFFICACY -- CVO's round-5 stamp -- the round-5 L10 precondition TERMINAL since 12:42Z (12 orders: 9 complete, 3 WITHDRAWN with rows, 0 pending; the stamp being written at 3.0.0_SA_CVO, ETA this tick, 93690) -- cut on the terminal precondition per /drive v2 obligation 2 (LD-0530) --, decomp v0.2.4 @39515415cc (STAGE 3 wide on Andrew's word "/drive COMPEFFICACY to completion." @dd040c447b; CE-t-11 at the ~E lane), PRD v0.5 @5bbdab5ec7 (s.4; s.4.4 incl. the verdict-bearing row; s.7 row T-11).</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` · **Decomp cell:** `CE-t-11` (STAGE 3; "CLEARED (audit) / RETIRE-candidate"; closes on "graded; RETIRE-candidate on usage SURFACED to Andrew, never acted here") · **Lane:** `.tools/comp-denytest` (12-line shim) + `.tools/comp-denytest.py` (the ENGINE, 413 lines) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~E/comp-denytest.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~E` (a CODEX seat, Andrew 13:4xZ) holds NFRA_COMPEFFICACY only.

---

## THE CELL

Manifest T-11 (PRD s.7): `comp-denytest` -> `.tools/comp-denytest.py`; 2 runs / 30 d, 8 ever; "zero population when no IAM change is CORRECT". The
shim's own header: `--from-plan <plan.json> --principal --resource --action` or `--change-type deny-add|allow-removal` (refused if it
contradicts the plan); the expected verdict is DERIVED (deny-add => explicitDeny, allow-removal => implicitDeny). A DENY-TEST's rc IS its
verdict (the s.4.4 verdict-bearing row applies by construction; `iam_cli.py`'s NOT-DECIDABLE rc 2 is the family precedent, and the
simulate false-deny modes on the record -- an `implicitDeny` on a CONDITIONED grant, a poisoned multi-ARN batch -- are exactly the
PARTIAL_OR_BLIND cases this tool must SAY rather than grade). The decomp's closes-on: **"graded; RETIRE-candidate on usage SURFACED to
Andrew, never acted here."**

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-denytest.result.md`: the 31 required s.4 fields (4.1 identity from the ENGINE, the shim named as the shim; 4.2 disclosure from a
QUOTED default run against a FIXTURE plan (no IAM change exists to test live, and that zero is CORRECT -- say so in the tool's voice);
4.3 the four planted answer-state cases on the ratified enum, ALL ON THE OFFLINE PLANE (fixture plans + the simulate stub suite the T-8
cell used; zero live IAM evaluation is owed by this audit): SUBJECT_ABSENT_FROM_CORPUS (a plan naming no such principal/resource),
PRESENT_WITH_ZERO_RESULTS (a plan with no deny-add / allow-removal change -- the correct zero), PARTIAL_OR_BLIND (a simulate whose verdict
cannot be read -- the conditioned-grant false-deny class -- printed as NOT-DECIDABLE with a NON-CLEAN rc, never as a verdict),
NOT_APPLICABLE (a change-type the tool does not test); rc + text quoted; the GRAIN sentence; 4.4 Rule T's form via `_compbudget.py`
where the tool has a timeout-bearing subprocess (the simulate call) with the VERDICT-BEARING row: BUDGET REACHED or an unreadable
simulate never returns the PASS rc; the whole rc vocabulary on `--help`; non-application stated where there is no loop; 4.5; 4.6
usage at BOTH instruments (8 runs ever -- the RETIRE-candidate evidence, stated as a finding for Andrew with the denominator, NOT acted)
and the battery at BOTH grains). Then the ONE code change (tokens, carrier, the non-clean rc on the undecidable path) and a NEW battery
`.tools/tests/test_comp_denytest_battery.py` with a RED mutant per arm (the mutant that grades a conditioned-grant implicitDeny as a real
deny among them).

## ACCEPTANCE

<criterion id="T11-AC1" cell_refs="CE-t-11"/> `T11-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT; 4.1 from the ENGINE; 4.2 quotes a real fixture run and states the correct zero in the tool's voice.
<criterion id="T11-AC2" cell_refs="CE-t-11"/> `T11-AC2` -- (AC-2) four PLANTED cases on the ratified enum, offline, produce four DISTINCT state tokens within one invocation (rc + text quoted); the conditioned-grant false-deny reads NOT-DECIDABLE with a non-clean rc, never a verdict.
<criterion id="T11-AC3" cell_refs="CE-t-11"/> `T11-AC3` -- THE RETIRE-CANDIDATE SURFACED, NOT ACTED: the usage census (runs.jsonl + rail log, 8 ever, denominator printed) recorded as a finding addressed to Andrew through the L4 owner's grade; zero retirement act (no shim, registry or carrier touched for that purpose -- diff shown).
<criterion id="T11-AC4" cell_refs="CE-t-11"/> `T11-AC4` -- (AC-4) Rule T's form where a subprocess carries a timeout, `--help` disclosing the carrier and the rc vocabulary; the verdict-bearing row exercised: expiry / unreadable simulate never returns the PASS rc (an rc-only consumer reads it as NOT clean); non-application stated where no loop exists.
<criterion id="T11-AC5" cell_refs="CE-t-11"/> `T11-AC5` -- battery NEW with a RED mutant per arm, direct AND pytest at the FILE grain; commit-gate clean on every .py touched; zero live IAM calls in the battery and in the audit (diff + a call census).
<criterion id="T11-AC6" cell_refs="CE-t-11"/> `T11-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself.

<expected_criteria>T11-AC1, T11-AC2, T11-AC3, T11-AC4, T11-AC5, T11-AC6</expected_criteria>

## SURFACES

`.tools/comp-denytest` (12 lines) · `.tools/comp-denytest.py` (413 lines) @39515415cc · `org/modules/graph/iam_cli.py:50` STATE_NOT_DECIDABLE + `cmd_simulate` :668 and its documented false-deny modes :673-692 (READ; the family precedent and the stub suite :816 the T-8 cell used) · `.tools/_compbudget.py` @`2718cffc45` (consumed) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` · PRD s.4 + s.7 T-11 @`5bbdab5ec7`; the memory rows on simulate false-denies (a conditioned grant; a poisoned multi-ARN batch).

## BOUNDS

- **ZERO live IAM evaluation and ZERO IAM change** under this order -- fixtures and the stub suite only; a plan that would touch IAM is never applied.
- **No retirement act** (the candidate is surfaced through the grade; Andrew decides); the derived-verdict rule (the author cannot pick the criterion) is not weakened.
- **No new dependency; no new file outside the engine, the shim, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` consumed, not edited.
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; surfaced_by = this seat; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @39515415cc (v0.2.4), cell CE-t-11 (s.1a; STAGE 3; ROUND 6 fence).
<owned_cells>CE-t-11</owned_cells>
Read-dependencies, NOT claimed: CE-t-8 (comp-iam, DONE -- the deny three-state and the stub suite), CE-t-25 (the verdict-bearing precedent, DONE), CE-tp-1 (DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 6 -> 6, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or this order's tool (read at 2026-09-03 14:23Z, the file's only token hit being the tool's own header line).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is comp-denytest's own voice and rc on fixture plans and the offline stub suite; no AWS principal, policy or resource is created, changed, granted or evaluated live by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @07601c54c9 (2026-09-03T14:26:03Z); 4/4 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged (2 flagged path(s): NFRA_COMPEFFICACY.TO-CE-T-11.comp-denytest-s4-audit.proof_of_spec.json GONE; comp-denytest.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (stage 4 pointers only, the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T11-AC1`..`T11-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~E/NFRA_COMPEFFICACY.TO-CE-T-11.comp-denytest-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. T11-AC2's false-deny case
and T11-AC5's mutants are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read .tools/comp-denytest.py --for "how the expected verdict is derived from the plan, how the simulate result is read, what rc each outcome returns, every subprocess with a timeout"`; `comp-read org/modules/graph/iam_cli.py --for "the stub suite and the documented false-deny modes"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-denytest` fixture run from a seat other than this lane -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
