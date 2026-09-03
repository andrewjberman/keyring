# T-16 filled in the schema, the batteries lane found dead at the directory grain, the tree-index wrapper -- 0.8.0_AE_CloudComp

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, IMPLEMENT, COORDINATE

**Date:** 2026-09-02, 21:50Z -> 23:05Z (third log of one session; continues @c198ab5c48)
**Task Order:** none. Two rows: the T-16 s.4 per-tool pass (3.0.0_SA_CVO 92628/92791, sequenced
2.0.0_SA_COO 92788 row 1) and the missions-tree-index pytest wrapper (2.0.0_SA_COO 92788 row 2).
**Status:** both LANDED and reported. Queue empty of named work. One ARMED hazard owned here (F6).

## Objective

1. Fill the PRD's s.4 result schema for comp-adversary from measured runs -- the first per-tool
   deliverable of NFRA_COMPEFFICACY, in the shape Andrew told the fabric to stop deviating from.
2. Wrap `.tools/missions-tree-index.py --self-test` for pytest in the 3b shape.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-find | `--name 'NFRA_COMPEFFICACY' --all` | PASS | found the PRD in CVO's deliverables after TWO directory guesses found nothing -- a name search, not a path I invented |
| comp-read | `--for` + `--enumerate` on the PRD, the engine, the gate, both manifests | PASS | the engine's two `timeout=` sites, the gate's PREFLIGHT_TOOLS row, the manifest's exclusion-list row |
| comp-read | `--enumerate` with my `/DENOMINATOR/,/^$/` sed range | FALSE EMPTY | the range matched only the 0-hit form; two real results printed nothing until re-run unfiltered |
| comp-adversary | 7 composes: default, absent, zero-pin, capped, directory, json, + 2 mutant-copy runs | PASS/measured | every 4.2/4.3/4.4 value quoted from a saved capture |
| comp-passcraft | `recon comp-adversary` | PASS | moves 1-3 observed; 4-8 hand-run; archetype UNCLASSIFIED -> hand-classified |
| pytest | `--collect-only -q` per file (22) and on the directory | DIRECTORY 0 | rc 3, INTERNALERROR SystemExit; 8 of 22 abort; 6 collect 37 |
| safe-commit | 3 commits | 1 REFUSED then 2 landed | the refusal was a lane (ANY_EXEC) on the schema's own path |

**What worked:** exercising, not reading -- the ceiling at 1 s did not fire (my first story would have
said it did), at 0.01 s it printed its own words; a directory subject produced a traceback the docstring
never mentions; the directory sweep produced 0 where every file said 1.
**What failed:** two of my output filters hid the result again (a sed range on comp-read; `tail -6` on
safe-commit that cut the refusal text off) -- third and fourth time today. And two directory GUESSES
for the PRD before one name search.
**Gap found:** the batteries lane has no directory-grain check anywhere; every acceptance in it today
was per-file.

## Work Completed

Three commits under this author line. Push state measured 22:50:54Z vs origin/CLOUD `def32cc1eb`
(control held): `64b930be4f` ON ORIGIN; `6eac560149` committed after the read, LOCAL by construction;
this log's commit likewise.

### 1. T-16 s.4 result -- `64b930be4f`, 229 lines, 31 of 31 fields
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_COMPEFFICACY_T16_comp-adversary.result.md`.
One fenced JSON block (parsed and field-checked before commit), prose with the four planted cases
quoted, the ceiling exercise, six findings, the lane-sweep census.
- 4.1: engine = shim, self-contained (626); `--help` prints name + v1, no engine path, no `--version`;
  registered NOWHERE a router reads (manifest :33 exclusion list; comp-tools.yaml 0 of 905) -- F5.
- 4.2: seven of eight disclosure fields PRESENT with the line quoted; `timeout` PRESENT-BUT-WRONG.
- 4.3: PASS -- absent (rc 2, one ERROR line), zero-pin (rc 0, "a signal, never a clean pass"),
  capped (rc 0, "showing 1 of 18", "POINTERS ONLY"), directory (rc 1, Python traceback at :94).
  Distinguishable; the fourth is not in the tool's voice -- F1. A .json subject composes as prose.
- 4.4: `timeout=60` :279 per digest, `timeout=120` :297 comp-state. EXERCISED on a copy beside the
  tool: 60 -> 1 s did not fire; 60 -> 0.01 s fired 12 of 12: `DEFERRED: comp-read unavailable:
  TimeoutExpired` per digest, rc 0, and the roll-up ("selected: 12 of 18 / NOT DIGESTED: 6 of 18")
  byte-identical to the healthy run -- F2. Work caps constant; time unbudgeted (Rule T owed).
  Usage line names one flag of four -- F3.
- 4.5: [correct-but-unwired] PROBED: to-pipeline-gate.py:54 lists it in PREFLIGHT_TOOLS and checks a
  TO's DECLARATION; it never invokes the tool. By design -- F4 is not a defect.
- 4.6: runs.jsonl 12 rows, all since 17:42Z (3a gave it its first row); rail log 0 invocation rows;
  hook-driven 0 of 12; stage-4 battery collects 1 in 0.09 s with a mutant; the August path-truncation
  battery (mine) aborts collection.
- Proposed: CLEARED-candidate on ONE unit (F1, ~3 lines before :94; F2/F3 ride it).

### 2. The lane finding on the schema's own path
s.4 :218 names `org/projects/NFRA_COMPEFFICACY/results/<tool>.result.md`; safe-commit refused:
`lane=ANY_EXEC`. An AE is the named filler of a path only an exec can commit. No override used; the
bytes moved to this seat's lane (sha equal before and after); the schema directory not left behind.
Three closes offered to 3.0.0_SA_CVO (grant the path / change the path / certifier files on CLEARED).

### 3. F6 -- the batteries lane is dead at the directory grain (surfaced 92794, ARMED, owner me)
`pytest --collect-only -q .tools/tests/` -> rc 3, INTERNALERROR SystemExit, 0 collected; the control
with the August file ignored -> still 0. Census of 22: 8 ABORT at import (4 mine, 1 CVO~C, 1 CTO,
2 CTO~X), 6 collect 37 tests, 8 collect 0 cleanly (one of those takes >60 s to collect nothing).
Every per-file acceptance today was true at the file grain and blind at this one. Not started; the
eight offered as one unit on CVO's word. Memory entry written.

### 4. missions-tree-index wrapper -- `6eac560149`, 140 lines
`.tools/tests/test_missions_tree_index_selftest.py`. Four arms on the printed contract (W1 RAN, W2
18/18, W3 body agrees with the summary, E a copy beside the tool with INDEX-MISSING inverted must RUN
and be RED -- rc 1, 17/18). Import-inert; `MISSIONS_TREE_INDEX_TOOL` aims it. Bars: collect 0.05 s;
pytest 4/4 with the denominator printed; direct == pytest; external mutant (INDEX-DRIFT inverted) ->
"arms failed (3 of 4)", no crash. Tool untouched (sha 614b272778ca7cd7 throughout). Built as `_wip_`,
renamed at commit.

## Decisions Made

1. Filled 4.3 with the PRD's grading vocabulary as it stands (4.7: the spellings are not ratified;
   CTO gates); minted nothing into code.
2. Recorded the directory crash as a FINDING with the fix proposed, not applied -- the pass is the
   audit; CVO names execution units (the delegation protocol Andrew set).
3. Did not fix the eight aborting batteries, including my four, without a named unit -- said so on
   the record, with the census and authors, so the naming is one line.
4. Exercised the ceiling on a COPY beside the tool, twice, checking the production sha before and
   after each; the first attempt's null result (1 s did not fire) is in the deliverable as a value.
5. Moved the deliverable rather than override a lane; surfaced the spec mismatch with three closes
   instead of picking one.
6. Stated the wrapper's acceptance at the FILE grain explicitly, because the directory grain is dead.

## Files Modified

Commit messages `64b930be4f`, `6eac560149` carry per-file rationale and bounds. Memory (outside the
repo): `reference_pytest_over_a_directory_collects_zero_when_any_module_raises_systemexit_at_import`,
`feedback_check_the_lane_of_a_path_a_spec_names_before_building_to_it`; two index lines.

## Blockers

None BLOCKED. Awaiting, each with its citing message:
- 3.0.0_SA_CVO: grade of T-16 (92803); unit naming for F1 and for F6's eight files; the s.4 path/lane
  close (92803). Until the path close lands, every per-tool result from this seat sits in this lane.
- 1.0.0_SA_CTO: F5 is a registration act on the manifest (comp-adversary excluded by list; absent from
  comp-tools.yaml) -- the manifest owner's, if wanted.
- Rule T on comp-adversary: carried project-wide with T-1/T-2.

## Current State

For a reader with no prior context:
- **The first NFRA_COMPEFFICACY per-tool result exists**, in the s.4 schema, at this seat's lane, for
  comp-adversary. It is CLEARED-candidate on one small unit. The schema's path is exec-only.
- **`pytest .tools/tests/` collects nothing.** Eight files abort the session at import; the fix per
  file is a `__main__` guard (revives the sweep) or the import-inert shape (collects >0, fast). Until
  then any "collects under pytest" claim in this lane is a per-file claim only.
- **comp-adversary's four answer-states are distinguishable**, its ceiling prints `DEFERRED: comp-read
  unavailable: TimeoutExpired` per digest with rc 0 and an unchanged roll-up, and it is registered in
  no router's catalog.
- **`.tools/tests/` now holds four import-inert batteries** (stage-4, comp-find, deploy-ledger-
  malformed, missions-tree-index) that collect in under 0.1 s each.

## Next Steps

- **[3.0.0_SA_CVO]** grade 64b930be4f; name F1 (and F2/F3 riding) as a unit; name F6's eight as a unit
  or split by author; pick the s.4 path close.
- **[0.8.0_AE_CloudComp]** on the word: F1 (~3 lines at :93, text distinguishable from "artifact not
  found", the stage-4 battery gains an arm for it); F6 (a `__main__` guard on eight files is one commit;
  the import-inert rewrite is one per file).
- **[1.0.0_SA_CTO]** F5 registration if the tool should be routable; the KUZUSPLIT PRD amendment (T-22).
- **[2.0.0_SA_COO]** row 3 of the tree manifest is closed by 6eac560149; nothing else sequenced here.
- **[Andrew]** nothing open at this seat.
