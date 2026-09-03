# TO NFRA_COMPEFFICACY.TO-CE-DISC-2 -- ratify the 4.3 ANSWER-STATE spellings as DATA (the enum every per-tool grade binds by)

<to_id>NFRA_COMPEFFICACY.TO-CE-DISC-2</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>1.0.0_SA_CTO</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut. Authority: Andrew-direct 2026-09-03 ~00:5xZ at the 2.0.0_SA_COO terminal, VERBATIM "go ahead and cut the first three task orders" (record @774c108bb5), on his process-wide GO ("lets take compefficacy through the whole canonical process", CTO terminal ~23:1xZ). Decomp @ee52600980 (CVO grade PASS 00:52Z). This is THE FIRST TASK ORDER CUT INTO THE PROJECT TREE.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.3 @`264bc9fa92` (s.4.3, s.4.7) · **Decomp cell:** `CE-disc-2` (STAGE 0, decide-first) · **Lane:** the PRD is CTO's (ANY_CTO at the tree home); the enum file is `org/standards/**` (ANY_EXEC). **Rule 27 seating:** `1.0.0_SA_CTO` is a Tier-1 exec, outside Rule 27's Tier-2 one-project bound; its open TO census at cut (`to-check --all`): 1 row, as a secondary on ADVI_PERFRP.TO-R2-DS.

---

## WHY THIS CELL IS FIRST (decide before grade)

PRD s.4.7, verbatim: *"Until the spellings are ratified (CTO gate), 4.3 binds deliverables by reading, not code by
enforcement."* Every per-tool 4.3 grade issued before this lands is a grade against unratified words. One has
already been issued (T-16, CLEARED @`bbba0db0e9`); twenty-three more are coming. **The census is done (s.4.7); the
decision is not.** This TO is the decision, landed as DATA a machine can compare against (spec s.3a: a gate-read
component is never prose).

## WHAT THE CENSUS SETTLED (PRD s.4.7, carried, not re-derived)

```
  4.3 state                      live carrier today                              what this TO decides
  NOT_DECIDABLE                  comp-schedule prints NOT-DECIDABLE (hyphen)     ADOPT the hyphen spelling
  NOT_APPLICABLE                 TWO spellings: NOT_APPLICABLE (underscore,      pick ONE; the OTHER carrier's change
                                 nerves_resolve) and DECLARED-NOT-APPLICABLE     is a FINDING with an owner, not this TO's edit
                                 (hyphen, to-pipeline-gate.py PREFLIGHT)         (the gate's token is Andrew-ruled; treat as fixed)
  SUBJECT_ABSENT_FROM_CORPUS     NO carrier in code; comp-find says OUT-OF-CORPUS mint; reconcile with comp-find's prose
  PRESENT_WITH_ZERO_RESULTS      NO carrier in code                              mint
```

## DELIVERABLE

1. **`org/standards/COMPTOOL_ANSWER_STATE.enum.json`** -- one file, DATA: the four states, ONE spelling each, the
   carrier each was adopted from or minted for, a `provenance` block citing PRD s.4.7 and this TO, and a
   `ratification` field (`"RATIFIED 1.0.0_SA_CTO <date> <this TO>"`). Rule 24 postulates (i)-(iv) as a short record
   inside the file or beside it (the s.4.7 text may be lifted verbatim).
2. **PRD s.4.3 versioned in place** to cite the file (one line), and s.4.7's "until ratified" clause closed by
   citation -- the PRD stays the ONE carrier of the schema; the enum file is what a grader compares against.
3. **The `NOT_APPLICABLE` split as a FINDING**: which value wins, which carrier must change (`nerves_resolve` OR
   the gate's `DECLARED-NOT-APPLICABLE`), and the OWNER of that change. No code is changed by this TO.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="DISC2-AC1" cell_refs="CE-disc-2"/> `DISC2-AC1` -- the enum file exists at the named path, parses, carries exactly FOUR states, each with exactly ONE spelling and its adopted-from/minted-for carrier named.
<criterion id="DISC2-AC2" cell_refs="CE-disc-2"/> `DISC2-AC2` -- `NOT-DECIDABLE` (hyphen) is the spelling, and comp-schedule's own output is cited as the reason (a live carrier is adopted, never re-minted).
<criterion id="DISC2-AC3" cell_refs="CE-disc-2"/> `DISC2-AC3` -- the `NOT_APPLICABLE` split has ONE winner in the file, and the finding names the losing carrier AND its owner; the file does NOT claim the losing carrier has changed.
<criterion id="DISC2-AC4" cell_refs="CE-disc-2"/> `DISC2-AC4` -- PRD s.4.3 cites the enum file (a version bump at the tree home), and `to-pipeline-gate.py` limb 5 still PASSES on the versioned PRD (read on the gate's own instrument before the commit).
<criterion id="DISC2-AC5" cell_refs="CE-disc-2"/> `DISC2-AC5` -- NEGATIVE control: a planted fifth state or a second spelling of an existing one is REJECTED by whatever consumer the file names (if none exists yet, the file says "binds by reading" and names the consumer that would reject -- an enum nobody can reject on is a document, not a gate).

<expected_criteria>DISC2-AC1, DISC2-AC2, DISC2-AC3, DISC2-AC4, DISC2-AC5</expected_criteria>

## SURFACES (read, never modified by this TO)

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md` s.4.3 (:374-385), s.4.7 (:457-490) @`264bc9fa92` ·
`.tools/comp-schedule` (NOT-DECIDABLE's carrier) · `.tools/to-pipeline-gate.py:55` (`DISPOSITION_RE`, the hyphen
`DECLARED-NOT-APPLICABLE`) · `nerves_resolve` (the underscore `NOT_APPLICABLE`; locate by `comp-find --name`) ·
`.tools/comp-find` (`OUT-OF-CORPUS` prose).

## BOUNDS

- **No tool's code changes under this TO.** A spelling change in a live carrier is a finding with an owner (DISC2-AC3); the executor for tool code is `0.8.0_AE_CloudComp` under its own row.
- **No gate.** The file binds by reading until a consumer adopts it; PRD s.5 "Any gate" stands. The generator's contract already shows the pattern (value enums by reference to a source) if a consumer is later wanted.
- **Re-read, not re-grade:** every 4.3 grade issued before this lands (T-16) is re-read ONCE against the file by `3.0.0_SA_CVO`; a regression re-opens a row, never a re-grade (FWD-9).

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @ee52600980 (v0.1.1), cell CE-disc-2 (s.1c, OWNS items 1 and 4; STAGE 0 in s.2).
<owned_cells>CE-disc-2</owned_cells>
Read-dependencies, NOT claimed: CE-t-16 (the one 4.3 grade already issued, re-read on landing), CE-t-5 (comp-schedule's spelling is the adopted one).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 139 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_COMPEFFICACY, comp-schedule or the answer-state enum (read at 2026-09-03 ~01:0xZ).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is a repo-local DATA file + a PRD section; no AWS principal, policy or resource is read or changed, so the lens has an empty population at this subject grain (the gate header's own non-application clause).
comp-adversary: RUN -- rc 0 at read-vintage @6f82252cea (2026-09-03 ~01:1xZ); 5 commits, 4 repo paths, 3 file:line cites, 5 tool mentions; cited commits 5 attempted / 5 verified / 0 UNVERIFIABLE; cited paths 4 attempted / 2 stable / 2 flagged (a flag = the path's blob moved after the cited pin -- the cited pins are DATED reads, not claims of current bytes); uncited siblings 0 with the cap declared; DEFERRED bucket not printed (--no-packet: stage 4 disabled by the caller, disclosed); --no-packet (stage 4 off, disclosed). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `DISC2-AC1`..`DISC2-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance from its own measurements at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/1.0.0_SA_CTO/NFRA_COMPEFFICACY.TO-CE-DISC-2.ratify-the-answer-state-spellings.proof_of_spec.json`
(the tree's `deliverables/<serial>/` layout, ruled @5f8b774a5d; the flip limb searches there) and validates it with
`.tools/proof-of-spec-check.py` BEFORE any `complete` flip. AC5 is a NEGATIVE control and is recorded as such.
</proof_of_spec>

## ISSUANCE READERS AT THIS CUT (CVO review R-ii, LANDED by 1.0.0_SA_CTO @87a9491713 at 01:05Z)

The proof-of-spec ISSUANCE HOOK (`.tools/git-hooks/to-proof-of-spec-check.sh`), `to-check.py`, `to-liveness-join.py`,
`proof-of-spec-check.py`, `to-decomp-ref-lint.py` and the loop-quiescence reader now discover TOs under BOTH roots;
the hook REFUSES a tree TO without a `<proof_of_spec>` block (red-first on a probe, CTO's transcript). **This commit is
the first real tree task order through those readers** -- the ADMISSION gate (`to-pipeline-gate.py`, both roots, R-iv
row/folder identity) and the R-i tree hook run on it too. Nothing about this issuance is stated as a blind spot.


**DELIVERABLE REPORT:** to `2.0.0_SA_COO` + `3.0.0_SA_CVO` (driver/grader) with per-criterion evidence and the
enum file's commit hash; push state stated as MEASURED (ls-remote) or UNREAD. GO = this TO + the dispatch message.
