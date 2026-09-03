# TO NFRA_COMPEFFICACY.TO-CE-TP-1 -- RULE T's BUDGET FORM: how a caller's ceiling reaches a tool, and what the tool says at expiry

<to_id>NFRA_COMPEFFICACY.TO-CE-TP-1</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>3.0.0_SA_CVO</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>WITHDRAWN 2026-09-03 ~02:25Z by the issuer 2.0.0_SA_COO (msg 92928) -- Andrew-direct at the COO terminal ~02:2xZ, VERBATIM: "Only tier2 agents are workers, MSTR does not "WORK" on projects, they are an integrator. COMPEFFICIENCY workers at this point number at 1, which is 0.8.0_AE_CloudComp". A Tier-1 seat does not hold an L7 task order, and 3.0.0_SA_CVO has no engagement before L8. The decision this file carried (Rule T's budget form: carrier, default, expiry grammar, non-application, falsifier; PRD s.4.4) is L4 content and lands with 1.0.0_SA_CTO as a PRD version; 3.0.0_SA_CVO stands down and any draft goes to 1.0.0_SA_CTO by one message as input. File retained as record; cell CE-tp-1 stays a cell, satisfied by the L4 landing. Record: org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_022xZ_L7_WORKERS_ARE_TIER2_ONLY_COMPEFFICACY_WORKER_COUNT_ONE.md. PRIOR: pending -- GO paired at cut. Authority: Andrew-direct 2026-09-03 ~00:5xZ at the 2.0.0_SA_COO terminal, VERBATIM "go ahead and cut the first three task orders" (record @774c108bb5), on his process-wide GO (CTO terminal ~23:1xZ). Decomp @ee52600980 (CVO grade PASS 00:52Z). Second of the first three tree task orders.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.3 @`264bc9fa92` (s.4.4 "RULE T (work)", s.4.4.1 measured baseline) · **Decomp cell:** `CE-tp-1` (STAGE 0, decide-first; OWNS item 5) · **Lane:** the deliverable lands at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/3.0.0_SA_CVO/` (TREE_DELIVERABLES resolves the owner from the folder); the PRD s.4.4 amendment is `1.0.0_SA_CTO`'s landing. **Rule 27 seating:** `3.0.0_SA_CVO` is a Tier-1 exec, outside Rule 27's Tier-2 bound; open TO census at cut: 2 ACTIVE rows on other projects (D3_MODELOVERLAY.TO-D3.5, OPAL_ADVIPOINTERS.P4-PINS-CERT-49F), stated. CVO is this project's DRIVER (PRD header) and authored s.4.4; certifier != author holds because the APPLICATION (CE-t-1) is CloudComp's and its grade is CVO's -- this TO is the SPEC, which CTO gates.

---

## WHY THIS CELL IS FIRST (decide before grade)

PRD s.4.4 states Rule T as a property -- *"a tool never exceeds a ceiling it was not told; prints the reached
denominator with a resume cursor"* -- and s.4.4.1 measures the baseline: **18 of 94 implementations set any
timeout, 14 different constants nobody chose, 76 of 94 have no ceiling at all; 5 of 106 paginate.** CVO 92843:
*"Rule T stays carried project-wide (T-1/T-2/T-16 alike)."* What does NOT exist is the FORM: by what mechanism a
caller's ceiling reaches the tool, and what the tool prints when it hits it. Without the form, every 4.4 grade is a
grade against prose, and the first target (comp-find, `.tools/comp-find:158` `timeout=600` inside a 120 s outer
ceiling -- measured this issuance) cannot be fixed the same way twice.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/3.0.0_SA_CVO/RULE_T_BUDGET_FORM.md` -- the form as a SPEC with
its Rule 24 record, plus the s.4.4 amendment text for `1.0.0_SA_CTO` to land at a PRD version. The form MUST decide:

1. **THE CARRIER** -- one mechanism by which a caller's ceiling reaches a tool (a flag, an environment variable, or
   both with a stated precedence), and the DEFAULT when the caller says nothing (a tool must have a ceiling it was
   told, not one it invented -- s.4.4 verbatim).
2. **THE EXPIRY DISCLOSURE GRAMMAR** -- the exact line(s) a tool prints at the ceiling: the REACHED denominator
   ("N of M scanned"), a resume cursor where pagination exists, and a token that makes an expiry DISTINGUISHABLE
   from a clean empty result (AC-4). The T-16 shape (`DEFERRED: N of M ... POINTERS ONLY`, always printed) is the
   precedent to adopt or improve, never a third dialect.
3. **NON-APPLICATION, stated** -- a tool whose output is a single boolean over a named subject has no population
   and owes no denominator (the gate header's own clause); name the class.
4. **THE FIRST TARGET, with its measured facts** -- comp-find: `timeout=600` at `:158` (subprocess), `timeout=20`
   at `:607`; the estate's outer ceiling 120 s (the harness), so the internal budget exceeds the caller's by 5x and
   nothing at the ceiling says so (PRD s.4.7's own specimen). The APPLICATION is CE-t-1 (CloudComp); this TO states
   what CE-t-1's ceiling exercise must produce, not the code.
5. **THE FALSIFIER** -- how a grader plants a run past the ceiling and what must appear (the s.4.4 leg of every 4.4
   grade from here on).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="TP1-AC1" cell_refs="CE-tp-1"/> `TP1-AC1` -- the form names ONE carrier with a stated precedence and a stated default; a reader can tell, for any tool, where its ceiling came from.
<criterion id="TP1-AC2" cell_refs="CE-tp-1"/> `TP1-AC2` -- the expiry grammar is written so that a clean empty and an expired scan cannot print the same line (a planted pair shown side by side in the deliverable).
<criterion id="TP1-AC3" cell_refs="CE-tp-1"/> `TP1-AC3` -- non-application is a named class with at least one live example, so a tool without a population is not written up as a violation (the RUN/DECLARED-NOT-APPLICABLE lesson of the gate's own enum).
<criterion id="TP1-AC4" cell_refs="CE-tp-1"/> `TP1-AC4` -- the first target's facts are cited by `file:line @ commit` and the form states what CE-t-1's ceiling exercise must produce, in the grammar of AC2.
<criterion id="TP1-AC5" cell_refs="CE-tp-1"/> `TP1-AC5` -- PRD s.4.4 versioned in place by `1.0.0_SA_CTO` to carry the form (one carrier), limb 5 still PASSING on the versioned PRD (read on the gate's own instrument before the commit).

<expected_criteria>TP1-AC1, TP1-AC2, TP1-AC3, TP1-AC4, TP1-AC5</expected_criteria>

## SURFACES (read, never modified by this TO)

PRD s.4.4 + s.4.4.1 @`264bc9fa92` · `.tools/comp-find:158` (`timeout=600`) and `:607` (`timeout=20`) at HEAD
@`774c108bb5` · `.tools/comp-adversary` (the DEFERRED-bucket precedent, CLEARED @`bbba0db0e9`) · the harness ceiling
(120 s foreground, 90 s collection -- CTO's row-5 harness facts).

## BOUNDS

- **No tool code changes under this TO.** The form is a spec; CE-t-1 applies it to comp-find under CloudComp's row.
- **No gate, no monitor** (PRD s.5; CLAUDE.md s.5 moratorium). The form is what graders compare against.
- **The two timeouts inside comp-find are FACTS here, not targets:** which one changes, and how, is CE-t-1's.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @ee52600980 (v0.1.1), cell CE-tp-1 (s.1c, OWNS item 5; STAGE 0 in s.2).
<owned_cells>CE-tp-1</owned_cells>
Read-dependencies, NOT claimed: CE-t-1 (the first application), CE-tp-2 (Rule P, already DONE as spec), CE-t-16 (the DEFERRED-bucket precedent).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 139 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_COMPEFFICACY, Rule T or comp-find (read at 2026-09-03 ~01:0xZ).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is a spec deliverable + a PRD section; no AWS principal, policy or resource is read or changed, so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @6f82252cea (2026-09-03 ~01:1xZ); 4 commits, 3 repo paths, 2 file:line cites, 5 tool mentions; cited commits 4 attempted / 4 verified / 0 UNVERIFIABLE; cited paths 3 attempted / 1 stable / 2 flagged (a flag = the path's blob moved after the cited pin -- the cited pins are DATED reads, not claims of current bytes); uncited siblings 0 with the cap declared; DEFERRED bucket not printed (--no-packet: stage 4 disabled by the caller, disclosed); --no-packet (stage 4 off, disclosed). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `TP1-AC1`..`TP1-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/3.0.0_SA_CVO/NFRA_COMPEFFICACY.TO-CE-TP-1.rule-t-budget-form.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE any `complete` flip. AC2's side-by-side pair is the
control that must be able to FAIL.
</proof_of_spec>

## ISSUANCE READERS AT THIS CUT (CVO review R-ii, LANDED by 1.0.0_SA_CTO @87a9491713 at 01:05Z)

The proof-of-spec ISSUANCE HOOK (`.tools/git-hooks/to-proof-of-spec-check.sh`), `to-check.py`, `to-liveness-join.py`,
`proof-of-spec-check.py`, `to-decomp-ref-lint.py` and the loop-quiescence reader now discover TOs under BOTH roots;
the hook REFUSES a tree TO without a `<proof_of_spec>` block (red-first on a probe, CTO's transcript). **This commit is
the first real tree task order through those readers** -- the ADMISSION gate (`to-pipeline-gate.py`, both roots, R-iv
row/folder identity) and the R-i tree hook run on it too. Nothing about this issuance is stated as a blind spot.


**DELIVERABLE REPORT:** to `2.0.0_SA_COO` + `1.0.0_SA_CTO` (the PRD landing) with per-criterion evidence; push
state stated as MEASURED or UNREAD. GO = this TO + the dispatch message.
