# TO NFRA_COMPEFFICACY.TO-CE-T-18 -- comp-pulse: the s.4 per-tool audit deliverable on the estate's highest-traffic marquis tool (8,364 runs, 8,359 of them the commit hook's `diff`) -- graded WITH ITS HOOK NATURE STATED in purpose_1line, the 4.3 four-case test, Rule T's form on its corpus-width sweeps, the verdict-bearing row where the pre-commit risk reflex's rc IS a verdict, and the traffic RE-MEASURED after unit 1 (T-1/T-2) as the cell requires

<to_id>NFRA_COMPEFFICACY.TO-CE-T-18</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~M</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete -- 2026-09-03: implementation `25684b8d96e1e25a8bca36011a575d9f9161034b`; refreshed proof VALID with 6/6 criteria and all four artifacts resolved; COO FWD-9 distinct-seat run at 16:56:26Z observed that SHA as an ancestor and returned comp-pulse shim rc 0 / PRESENT_WITH_ZERO_RESULTS / REFLEX CLEAN. Push state LOCAL: this seat never pushed.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (s.4; s.4.3 + GRAIN; s.4.4 + the verdict-bearing row; s.7 T-18) · **Decomp cell:** `CE-t-18` (STAGE 3; closes on "graded with the hook nature stated in purpose_1line") · **Lane:** `.tools/comp-pulse` (if a shim exists -- measure) + `org/modules/graph/comp_pulse.py` (the ENGINE, 707 lines) + the pre-commit risk reflex that calls it (`.tools/safe-commit.sh`'s `[risk-reflex] comp-pulse diff` stage -- READ; the reflex is CTO's mechanism) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~M/comp-pulse.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~M` (a CODEX seat, Andrew 13:4xZ) holds NFRA_COMPEFFICACY only.

---

## THE CELL

Manifest T-18 (PRD s.7 :646): `comp-pulse` -> `org/modules/graph/comp_pulse.py` (707); **8,364 runs, 8,359 = `diff` from the commit hook; 5 by
hand**; the L2 traffic source is runs.jsonl; bound: "it is a HOOK, not a morning read; its traffic was blind to T-1/T-2 until unit 1 --
re-measure after". The decomp's closes-on, verbatim: **"graded with the hook nature stated in purpose_1line."** MEASURED at cut: every
safe-commit on this device runs `comp-pulse diff` as THE PRE-COMMIT RISK REFLEX (NFRA_NERVES L5) and prints a REFLEX CLEAN / danger
line against a danger map (1,906 nodes today) -- so `diff`'s result is consumed by a gate and its rc, where it carries the reflex's
verdict, is VERDICT-BEARING; the by-hand modes (`--days`, `--top`, cochange) are graded measurements. The cell owes the audit WITH the
hook nature said first: an s.4 deliverable that describes comp-pulse as a tool an agent runs would be the wrong object.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-pulse.result.md`: the 31 required s.4 fields (4.1 identity from the ENGINE; `purpose_1line` STATES THE HOOK NATURE -- "the
pre-commit risk reflex; 8,359 of 8,364 runs are the hook's `diff`"; 4.2 disclosure from a QUOTED default run of `diff` AND of one by-hand
mode; 4.3 the four planted answer-state cases on the ratified enum -- SUBJECT_ABSENT_FROM_CORPUS (a path no danger map carries),
PRESENT_WITH_ZERO_RESULTS (a real file checked against the map with zero danger hits -- REFLEX CLEAN as a MEASURED result, quoted),
PARTIAL_OR_BLIND (the map STALE or ABSENT -- what does the reflex say, and does it say it in its own voice? the danger map's age is
printed today; a missing map must not read CLEAN), NOT_APPLICABLE (a mode with no population); rc + text quoted per case; the GRAIN
sentence; 4.4 Rule T's form via `.tools/_compbudget.py` on the corpus-width sweeps (the cochange / --days scans), with the VERDICT-BEARING
row applied to `diff` as the reflex consumes it: at BUDGET REACHED (or on an unreadable map) it never returns the CLEAN rc -- the T-25
shape, rc stated on `--help`; and the non-application half stated for `diff` on a small file set; 4.5 the passcraft moves; 4.6 usage at
BOTH instruments and the battery at BOTH grains -- WITH THE TRAFFIC RE-MEASURED after unit 1 (T-1/T-2's comp_log_auto wiring) so the
8,364 figure is dated and its post-unit-1 successor printed with its window). Then the ONE code change: the hook-nature line on `--help`,
the 4.3 tokens on every answer, the budget carrier, the verdict-bearing expiry / missing-map rc on `diff`, and a NEW battery
`.tools/tests/test_comp_pulse_battery.py`. **The reflex's consumer (`safe-commit.sh`'s stage) is READ and its behaviour on the new rc
stated -- never edited here (CTO's mechanism; a required change there is a FINDING).**

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T18-AC1" cell_refs="CE-t-18"/> `T18-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT, 4.1 identity from the ENGINE; `purpose_1line` states the HOOK nature with the measured ratio -- the cell's closes-on, quoted.
<criterion id="T18-AC2" cell_refs="CE-t-18"/> `T18-AC2` -- (AC-2) four PLANTED cases on the ratified enum produce four DISTINCT state tokens in the tool's own voice within one invocation (rc + text quoted); a STALE or ABSENT danger map never reads REFLEX CLEAN (the PARTIAL_OR_BLIND case exercised on the real binary with the map moved aside).
<criterion id="T18-AC3" cell_refs="CE-t-18"/> `T18-AC3` -- TRAFFIC RE-MEASURED: runs.jsonl census by mode and by caller with the window stated, before and after unit 1's wiring (the T-1/T-2 commits), denominator printed; the 8,364 figure dated.
<criterion id="T18-AC4" cell_refs="CE-t-18"/> `T18-AC4` -- (AC-4) Rule T's form: `--help` discloses the carrier; a planted small `--budget` on a sweep produces the s.4.4 expiry line beside a clean completion; `diff` under the verdict-bearing row never returns the clean rc at expiry or on an unreadable map (rc stated, exercised by an rc-only consumer); `safe-commit.sh`'s reflex stage READ and its handling of the new rc stated (a needed change there is a FINDING to the L4 owner, not an edit).
<criterion id="T18-AC5" cell_refs="CE-t-18"/> `T18-AC5` -- battery NEW with one arm per new behaviour and a RED mutant each (the missing-map-reads-CLEAN mutant among them), direct AND pytest at the FILE grain; commit-gate clean on every .py touched -- and the reflex itself still prints CLEAN on this cell's own commits (quoted from the commit output).
<criterion id="T18-AC6" cell_refs="CE-t-18"/> `T18-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself.

<expected_criteria>T18-AC1, T18-AC2, T18-AC3, T18-AC4, T18-AC5, T18-AC6</expected_criteria>

## SURFACES

`org/modules/graph/comp_pulse.py` (707 lines) @39515415cc · `.tools/comp-pulse` (measure whether a shim exists; the reflex may call the engine directly) · `.tools/safe-commit.sh` (the `[risk-reflex]` stage -- READ) · the danger map it reads (its path, age line, denominator 1,906 nodes today) · `.tools/_compbudget.py` @`2718cffc45` (consumed) · `org/modules/graph/comp_dataflow.py:cmd_gate` @`72e7846ca7` (the verdict-bearing precedent) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` (the traffic census) · PRD s.4 + s.7 T-18 @`5bbdab5ec7`.

## BOUNDS

- **The reflex's consumer is not edited** (`safe-commit.sh` is the L4 owner's mechanism); the danger map is READ, never rebuilt here (graph law: query, never rebuild).
- **`diff`'s CLEAN semantics on a complete run do not change**; only the expiry / unreadable-map path gains a non-clean rc.
- **No new dependency; no new file outside the engine, a shim if one exists, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` consumed, not edited.
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; surfaced_by = this seat; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

**PUSH (standing law carried onto this CODEX seat's face, 0.0.0_AB_MSTR 93721 on 2.0.0_SA_COO~A's finding 93715, 2026-09-03 15:0xZ):** a shared branch (CLOUD / DEV / PROD / main / SITEZ) is pushed ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and only on Andrew's word while he is at the terminal (LD-0367/0368, LD-0522). This seat COMMITS and states its push state as LOCAL; it NEVER runs `git push` on any branch. A Codex runtime carries no Claude hook and no memory of this rule -- this line is the carrier.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @39515415cc (v0.2.4), cell CE-t-18 (s.1a; STAGE 3; ROUND 6 fence).
<owned_cells>CE-t-18</owned_cells>
Read-dependencies, NOT claimed: CE-t-1 / CE-t-2 (unit 1's wiring, DONE -- the re-measure's boundary), CE-t-25 (the verdict-bearing precedent, DONE), CE-tp-1 (the form, DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 6 -> 6, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or this order's tool (read at 2026-09-03 14:23Z, the file's only token hit being the tool's own header line).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-pulse reads the repo's commit history and a local danger map; no AWS principal, policy or resource is read or changed by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @07601c54c9 (2026-09-03T14:24:55Z); 4/4 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged (2 flagged path(s): NFRA_COMPEFFICACY.TO-CE-T-18.comp-pulse-s4-audit.proof_of_spec.json GONE; comp-pulse.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (stage 4 pointers only, the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T18-AC1`..`T18-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~M/NFRA_COMPEFFICACY.TO-CE-T-18.comp-pulse-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. T18-AC2's missing-map case
and T18-AC5's mutants are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_pulse.py --for "where diff reads the danger map, what it returns when the map is stale or absent, and every corpus-width loop"`; `comp-read .tools/safe-commit.sh --for "the risk-reflex stage: how it invokes comp-pulse and what it does with the rc"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-pulse diff <file>` from a seat other than this lane (the base seat or ~B; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after, the traffic census, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
