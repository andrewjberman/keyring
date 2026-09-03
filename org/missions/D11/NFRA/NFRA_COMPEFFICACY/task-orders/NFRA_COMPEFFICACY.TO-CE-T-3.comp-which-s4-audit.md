# TO NFRA_COMPEFFICACY.TO-CE-T-3 -- comp-which: the s.4 per-tool audit deliverable, the 4.3 four-case test with the NOFIT-POSTERIOR path as a planted case, and Rule T's form on its subprocess ceilings

<to_id>NFRA_COMPEFFICACY.TO-CE-T-3</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~A</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T07:01:54Z) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-3.comp-which-s4-audit.proof_of_spec.json; T3-AC1..AC6 self-assessed PASS (deliverable comp-which.result.md at the lane's own folder); CVO grade (CONFORMING/CLEARED) pending -- certifier != author. Rule T wired onto BOTH of comp-which's timeout-carrying subprocesses (the comp-find fallback and the self-report telemetry sink) sharing ONE Clock; a real, measured near-timeout condition found (82.759s direct for an unscoped fallback call, not a regression -- the old fixed 60s ceiling would also have killed it) and a real bug in the routing-test harness's own sandbox mirror found and fixed (build_mirror() was missing the new _compbudget.py sibling dependency) -- both caught and closed within this cell's own session, neither a surprise row (no spec-vs-world divergence, no code ever shipped in the broken state). Zero surprises filed. Push state MEASURED 2026-09-03T07:01:54Z (ls-remote + is-ancestor): origin/CLOUD @3bd8d2ef04; both this cell's commits (e8f67c34f5, d92fe43586) read LOCAL ONLY (is-ancestor rc=1) -- the expected state while Andrew gates the push cadence. Prior history: pending -- GO paired at cut. Authority: round 3 of the canonical loop on NFRA_COMPEFFICACY -- CVO's round-2 stamp @88c961297b (ZERO GRADUATION: proceed to the next L6 dispatches), decomp v0.2.1 (STAGE 1: CE-t-1 -> CE-t-2 -> CE-t-3; ROUND 3 fence: CE-t-3 at 0.8.0_AE_CloudComp~A), on Andrew's words on the loop (@10a4beaffb, @de2d6d643c). CE-t-2 is terminal @bf3f270e0c, so this cell's sequencing dependency is met. STAGE 1's last cell; continuity at the lane that closed CE-t-2.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.4 @`19bf1c7322` (s.4 the schema, s.4.3 the enum as DATA, s.4.4 RULE T's FORM; s.7 row T-3 :604) · **Decomp cell:** `CE-t-3` (= manifest T-3; STAGE 1, the router) · **Lane:** `.tools/comp-which` (ANY), `.tools/comp-which-routing-test.py` (its battery; `.tools/**`) and `.tools/tests/**` (TOOL_BATTERIES); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-which.result.md` (owner by path; the lane's own folder, now also its agent home @`05b7e1c77e`). **Rule 27 seating:** `0.8.0_AE_CloudComp~A` holds NFRA_COMPEFFICACY only (CE-t-2 terminal; this is continuity on the same project).

---

## THE CELL

Manifest T-3 (PRD s.7 :604): `comp-which` -> `.tools/comp-which` (Python, **2,329 lines at HEAD @`05b7e1c77e`**); 520 runs.jsonl
+ 9,643 rail; paginates; ceilings **20 s / 60 s** (the PRD's own reading; the 60 s is the routing test's `_run_comp_which`
timeout, `:37`). Rule 21's ROUTER: every `comp-which "<question>"` on the estate lands here. Decomp cell CE-t-3 reads
OPEN with its closes-on: **"the NOFIT-POSTERIOR path graded as a 4.3 case"** -- comp-which's honest no-match
(`:1545-1551`: 108 no-matches measured; "NOFIT-POSTERIOR is a no-match, never a route") is the tool's own
PRESENT_WITH_ZERO_RESULTS voice and must be planted, quoted and shown distinguishable from a route. The tool's
Popen + wait(timeout=) + kill() pattern at `:1647-1651` (the corrected 84-minute-hang source) is the ceiling Rule T's
form binds.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-which.result.md`: one fenced JSON block +
prose; the 31 required s.4 fields (4.1 identity from the ENGINE; 4.2 disclosure from a QUOTED default run; 4.3 the four
planted answer-state cases keyed on the RATIFIED enum `org/standards/COMPTOOL_ANSWER_STATE.enum.json` -- with the
NOFIT-POSTERIOR no-match as the PRESENT_WITH_ZERO_RESULTS case and a route with a low-confidence hedge as the
PARTIAL_OR_BLIND case, each in the tool's own voice; 4.4 Rule T's form APPLIED via the ONE shared module
`.tools/_compbudget.py` -- carrier `--budget` > env `COMP_BUDGET_S` > default, the source word on the denominator line,
every subprocess ceiling (`:1647-1651` and any other `wait(timeout=)`/`timeout=`) derived from `remaining()`, the
expiry line in the s.4.4 grammar distinguishable from a clean completion; 4.5 the passcraft moves; 4.6 usage at BOTH
instruments -- `org/mcp/comp-tool-runs.jsonl` (520) and `org/mcp/comp-which-rail.log` (9,643) -- and the battery at
BOTH grains). Then the ONE code change this cell owes: the budget carrier wired, the ceilings from `remaining()`,
`--help` disclosing the carrier. **Routing semantics do NOT change** (the curated rules, the learned affinity, the
ROUTE-POSTERIOR families at `:1552`, the NOFIT decision -- none of it moves; `.tools/comp-which-routing-test.py` is the
control and must read as it reads today).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T3-AC1" cell_refs="CE-t-3"/> `T3-AC1` -- the deliverable parses (one fenced JSON block), every required s.4 field present or explicitly ABSENT, 4.1 identity read from the engine path.
<criterion id="T3-AC2" cell_refs="CE-t-3"/> `T3-AC2` -- (AC-2) four PLANTED cases keyed on the ratified enum, the NOFIT-POSTERIOR no-match among them, produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case); a no-match is never printed as a route.
<criterion id="T3-AC3" cell_refs="CE-t-3"/> `T3-AC3` -- (AC-4) Rule T's form applied: `--help` discloses the carrier via `_compbudget.py`; a planted small `--budget` produces the s.4.4 expiry line with its source word and reached denominator, side by side with a clean completion line; every subprocess ceiling reads from `remaining()`; the `:1647-1651` kill path still fires on a planted hang (the 84-minute class stays closed).
<criterion id="T3-AC4" cell_refs="CE-t-3"/> `T3-AC4` -- battery: `.tools/comp-which-routing-test.py` reads exactly as before on production (its arms unchanged, its count stated), plus ONE new arm for the budget carrier with a planted mutant that ignores `--budget` going RED; directory grain of `.tools/tests/` stated as it reads.
<criterion id="T3-AC5" cell_refs="CE-t-3"/> `T3-AC5` -- usage at both instruments with denominators (runs.jsonl rows and rail rows over the window used), and any routing-friction finding carried with an OWNER named (the comp-learns backlog is the carrier), not fixed here.
<criterion id="T3-AC6" cell_refs="CE-t-3"/> `T3-AC6` -- push state MEASURED at report (ls-remote + is-ancestor; LOCAL expected while Andrew gates the cadence, say which state was read); the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the seat commits itself.

<expected_criteria>T3-AC1, T3-AC2, T3-AC3, T3-AC4, T3-AC5, T3-AC6</expected_criteria>

## SURFACES

`.tools/comp-which` (2,329 lines; `:37` the routing test's 60 s; `:1545-1552` NOFIT-POSTERIOR and the ROUTE families; `:1647-1651` the Popen/wait/kill ceiling) @`05b7e1c77e` · `.tools/comp-which-routing-test.py` (the battery) · `.tools/_compbudget.py` @`2718cffc45` · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` @`19bf1c7322` · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` (the two usage instruments; the 80-char `args_head` sink trap applies) · `org/modules/graph/comp-learns-backlog.md` (routing-friction findings' carrier) · PRD s.4 + s.7 T-3 @`19bf1c7322` · the precedents: `deliverables/0.8.0_AE_CloudComp/comp-find.result.md` @`6d04680f2b`, `deliverables/0.8.0_AE_CloudComp~A/comp-read.result.md` @`e0f0e5a9e6`.

## BOUNDS

- **Routing semantics do NOT change**: no curated rule, affinity term, family constant or NOFIT decision moves under this cell; a routing-friction finding is carried to the backlog with an owner (T3-AC5).
- **No new dependency; no new file outside the two named** (the tool, its battery) plus the deliverable + proof instance. `_compbudget.py` is consumed, not edited (a needed change there is a ROW).
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), then keep working; never a message.
- **Certifier != author:** the s.7 row-state word is the L4 owner's version bump on the L8/L9 seat's documentation, read from the record.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @070907b56e (v0.2.1), cell CE-t-3 (s.1a, = manifest T-3; STAGE 1 in s.2; ROUND 3 fence).
<owned_cells>CE-t-3</owned_cells>
Read-dependencies, NOT claimed: CE-t-2 (terminal @bf3f270e0c; the precedent), CE-t-1 (the form's first application), CE-tp-1 / CE-disc-2 (DONE as spec), CE-t-8 (in parallel at the base seat -- no dependency either way).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 336 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or comp-which (read at 2026-09-03 05:57Z).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-which is a repo-local Python router over the estate's tool catalog and logs; no AWS principal, policy or resource is read or changed by it or by this TO, so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @740dfea64b (2026-09-03T05:59:23Z); 10 commits, 7 repo paths, 0 file:line cites (the `:NN` pins are inside backticks), 12 tool mentions; cited commits 10 attempted / 10 verified / 0 UNVERIFIABLE; cited paths 7 attempted / 5 stable / 2 flagged (both flagged = GONE at read-vintage: the deliverable file and the proof instance this TO CREATES -- expected, not stale); uncited siblings 255 with the cap (25) declared; DEFERRED bucket not printed (--no-packet: stage 4 disabled by the caller, disclosed); 5 declared exclusions (v1 contract). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T3-AC1`..`T3-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-3.comp-which-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself.
T3-AC3's side-by-side pair and T3-AC4's planted mutant are the controls that must be able to FAIL; every `surprises`
entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read .tools/comp-which --for "where the routing decision becomes NOFIT-POSTERIOR, where each subprocess ceiling is set, and what the tool prints at the end of a route"` and `--enumerate 'timeout=|wait\(|NOFIT-POSTERIOR|ROUTE-POSTERIOR'`. BEFORE COMMIT: `.tools/commit-gate.sh` on the tool and the battery; the routing test direct at the FILE grain. AFTER COMMIT: one real `comp-which "<question>"` from a seat other than this lane (the base seat is the nearest; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record, not a message) with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
