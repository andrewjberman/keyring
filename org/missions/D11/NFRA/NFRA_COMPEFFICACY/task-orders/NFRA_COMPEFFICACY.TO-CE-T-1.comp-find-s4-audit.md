# TO NFRA_COMPEFFICACY.TO-CE-T-1 -- comp-find: the s.4 per-tool audit deliverable, the 4.3 four-case test, and the ceiling brought under the caller's budget

<to_id>NFRA_COMPEFFICACY.TO-CE-T-1</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T03:49:30Z) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-1.comp-find-s4-audit.proof_of_spec.json; T1-AC1..AC6 self-assessed PASS (deliverable comp-find.result.md at the tree home); CVO grade (CONFORMING/CLEARED) pending -- certifier != author. Interim T-16-shape fix (88e870b115) reworked onto the landed PRD v0.4 s.4.4 form (2718cffc45) after that form landed mid-round (surprise NFRA_COMPEFFICACY-S1); a second, unrelated live-latency finding filed as NFRA_COMPEFFICACY-S2 (self-resolved, no code defect). Push state MEASURED: all three cell commits (88e870b115, b89b0493e5, 2718cffc45) ON origin/CLOUD as of 2026-09-03T03:43:18Z (ls-remote + is-ancestor). Prior history: pending -- GO paired at cut. Authority: Andrew-direct 2026-09-03 ~00:5xZ at the 2.0.0_SA_COO terminal, VERBATIM "go ahead and cut the first three task orders" (record @774c108bb5), on his process-wide GO (CTO terminal ~23:1xZ). Decomp @ee52600980 (CVO grade PASS 00:52Z). Third of the first three tree task orders; SUPERSEDES COO 92822 row 3 (the same work, now with a cell id).</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.3 @`264bc9fa92` (s.4 the schema; s.7 row T-1) · **Decomp cell:** `CE-t-1` (= manifest row T-1; STAGE 1, the rail pair's first) · **Lane:** `.tools/comp-find` (ANY) and `.tools/tests/**` (TOOL_BATTERIES, yours); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-find.result.md` (PRD v0.3 s.4 HOME; TREE_DELIVERABLES resolves you from the folder -- your T-16 file moved there @d101d4fe20 is the precedent). **Rule 27 seating:** `0.8.0_AE_CloudComp` BASE holds NFRA_COMPEFFICACY only (your 92793/92850 reading; the six open rows `to-check` attributes to the serial are `~X`/`~B`/`~Z` LANE TOs on other projects, not the base).

---

## THE CELL

Manifest T-1 (PRD s.7): `comp-find` -> `.tools/comp-find` (Python, self-contained, 615 lines at HEAD @`774c108bb5`);
**3,722 runs/30d (rail), the most-invoked search tool in the estate; Rule 21's rail (R-6)**. Already landed and
CLEARED on their own instruments: unit 1 (runs.jsonl logging, @`f34122edfb` ON origin) and the battery (unit 3b,
`.tools/tests/test_comp_find_battery.py` @`1e6206a267`, 6 arms, planted DENOMINATOR mutant 5 of 6 RED). **What is
NOT done: the s.4 deliverable itself, the 4.3 four-case test, and Rule T on the ceiling.** Decomp cell CE-t-1 reads
IN-FLIGHT with exactly those owed.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-find.result.md`: one fenced JSON block +
prose; the 31 required s.4 fields (4.1 identity from the ENGINE not a shim; 4.2 disclosure from a QUOTED default run;
4.3 the four planted answer-state cases; 4.4 bounds with the ceiling EXERCISED; 4.5 the passcraft 8 moves; 4.6 usage
at BOTH instruments and the battery at BOTH grains). Then the ONE code change this cell owes:

- **Rule T on comp-find's ceiling.** MEASURED at issuance: `.tools/comp-find:158` `timeout=600` (the search
  subprocess) and `:607` `timeout=20`; the harness's outer ceiling is 120 s, so the internal budget exceeds the
  caller's by 5x and nothing at the ceiling says so (PRD s.4.7 specimen: the 8-way census "exceeded a 120s foreground
  ceiling twice and completed only in the background"). Bring the internal budget under a ceiling the caller can set,
  and at expiry print the REACHED denominator with a resume cursor, distinguishable from a clean empty result.
  **Grammar:** CE-tp-1's form (TO-CE-TP-1, at CVO) when it lands; until then the T-16 `DEFERRED: N of M` shape as
  the interim, stated as interim in the deliverable. Neither the search semantics nor pagination changes (the 3b
  battery must stay 6 of 6 GREEN and the planted mutant RED).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T1-AC1" cell_refs="CE-t-1"/> `T1-AC1` -- the deliverable parses (one fenced JSON block), every required s.4 field present or explicitly ABSENT, 4.1 identity read from the engine path; graded CONFORMING by `3.0.0_SA_CVO`.
<criterion id="T1-AC2" cell_refs="CE-t-1"/> `T1-AC2` -- (AC-2) four PLANTED cases -- absent subject, present-with-zero-results, not-decidable, and a healthy hit -- produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case); `0 hit(s) across 0 file(s)` is OUT-OF-CORPUS, never a zero (comp-find's own doctrine, CLAUDE.md Rule 21).
<criterion id="T1-AC3" cell_refs="CE-t-1"/> `T1-AC3` -- (AC-4) driven past its ceiling on a COPY beside the tool (production sha before/after unchanged), comp-find emits the expiry disclosure carrying the reached denominator + cursor, and that line cannot be produced by a clean empty run (the pair shown side by side).
<criterion id="T1-AC4" cell_refs="CE-t-1"/> `T1-AC4` -- the ceiling is now a budget the caller can set (the carrier per CE-tp-1's form, or the interim stated), with the default disclosed in `--help`; `:158`'s hard 600 no longer outlives a 120 s caller silently.
<criterion id="T1-AC5" cell_refs="CE-t-1"/> `T1-AC5` -- battery: `.tools/tests/test_comp_find_battery.py` stays 6 of 6 GREEN on production, its DENOMINATOR mutant stays RED, and ONE new arm covers the expiry disclosure (a planted ceiling mutant that must go RED); stated at the FILE grain AND the directory grain (the whole-directory number, with CTO's three files noted if still aborting).
<criterion id="T1-AC6" cell_refs="CE-t-1"/> `T1-AC6` -- (AC-6 / FWD-9) the fix commit's push state MEASURED (ls-remote + is-ancestor) at report; CLEARED is not granted on a LOCAL commit -- the push is `0.0.0_AB_MSTR`'s act and the report says which state it read.

<expected_criteria>T1-AC1, T1-AC2, T1-AC3, T1-AC4, T1-AC5, T1-AC6</expected_criteria>

## SURFACES

`.tools/comp-find` (615 lines; `:158` `timeout=600`; `:607` `timeout=20`) @`774c108bb5` · `.tools/tests/test_comp_find_battery.py`
@`1e6206a267` · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` (the two usage instruments; the 80-char
`args_head` sink trap from unit 3a applies to any token acceptance) · PRD s.4 + s.7 T-1 @`264bc9fa92`.

## BOUNDS

- **Search behaviour and pagination do NOT change** (the 3b battery is the control). Rule P/T work beyond the ceiling is a later row.
- **No new dependency, no new file outside the two named** (the tool, its battery) plus the deliverable + proof instance. **AMENDED BY THE ISSUER 2026-09-03 ~02:59Z (msg 92959, on surprise 92944):** this bound was written before PRD s.4.4 existed; PRD v0.4 @`19bf1c7322` s.4.4 (L4, outranks a pre-spec TO bound) names ONE shared sibling module `.tools/_compbudget.py` as Rule T's carrier with comp-find as its reference target, so **`.tools/_compbudget.py` is IN SCOPE under CE-t-1** (never per-tool copies). Everything else in this section stands; acceptance T1-AC1..AC6 unchanged. The interim-grammar clause in DELIVERABLE is thereby exercised: the form HAS landed and is the grammar.
- **Truthful non-application stays truthful:** a scope with 0 files is OUT-OF-CORPUS and prints as such; do not convert it into a hit or a violation (PRD s.5).
- **Grade is CVO's; CLEARED is CVO's word after T1-AC6 reads ON origin.** Certifier != author.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @ee52600980 (v0.1.1), cell CE-t-1 (s.1a, = manifest T-1; STAGE 1 in s.2).
<owned_cells>CE-t-1</owned_cells>
Read-dependencies, NOT claimed: CE-tp-1 (the grammar, when it lands), CE-tp-2 (Rule P, DONE), CE-org-1 (the push that makes T1-AC6 readable), CE-t-2 (comp-read follows this cell).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 139 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_COMPEFFICACY or comp-find (read at 2026-09-03 ~01:0xZ).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-find is a repo-local Python tool over the git corpus; no AWS principal, policy or resource is read or changed by it or by this TO, so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @6f82252cea (2026-09-03 ~01:1xZ); 6 commits, 5 repo paths, 2 file:line cites, 9 tool mentions; cited commits 6 attempted / 6 verified / 0 UNVERIFIABLE; cited paths 5 attempted / 3 stable / 2 flagged (a flag = the path's blob moved after the cited pin -- the cited pins are DATED reads, not claims of current bytes); uncited siblings 0 with the cap declared; DEFERRED bucket not printed (--no-packet: stage 4 disabled by the caller, disclosed); --no-packet (stage 4 off, disclosed). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T1-AC1`..`T1-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-1.comp-find-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE any `complete` flip. T1-AC3's side-by-side pair and
T1-AC5's planted mutant are the controls that must be able to FAIL; a proof in which every criterion passes in the
same direction is not a proof.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read .tools/comp-find --for "where the search subprocess ceiling is set and what prints at expiry"` (and `--enumerate 'timeout'`, 3 hits at issuance). BEFORE COMMIT: `.tools/commit-gate.sh` on the tool and the battery; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-find` run from a seat other than yours (CVO's grade run is that seat) -- FWD-9.
</compiler_tools_mandate>

## ISSUANCE READERS AT THIS CUT (CVO review R-ii, LANDED by 1.0.0_SA_CTO @87a9491713 at 01:05Z)

The proof-of-spec ISSUANCE HOOK (`.tools/git-hooks/to-proof-of-spec-check.sh`), `to-check.py`, `to-liveness-join.py`,
`proof-of-spec-check.py`, `to-decomp-ref-lint.py` and the loop-quiescence reader now discover TOs under BOTH roots;
the hook REFUSES a tree TO without a `<proof_of_spec>` block (red-first on a probe, CTO's transcript). **This commit is
the first real tree task order through those readers** -- the ADMISSION gate (`to-pipeline-gate.py`, both roots, R-iv
row/folder identity) and the R-i tree hook run on it too. Nothing about this issuance is stated as a blind spot.


**DELIVERABLE REPORT:** to `3.0.0_SA_CVO` (grade) + `2.0.0_SA_COO` (sequencer) with per-criterion evidence, production
sha before/after, the battery numbers at both grains, and push state as MEASURED or UNREAD. GO = this TO + the
dispatch message.
