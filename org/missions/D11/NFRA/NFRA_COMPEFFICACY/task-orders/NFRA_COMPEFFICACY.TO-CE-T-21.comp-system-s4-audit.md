# TO NFRA_COMPEFFICACY.TO-CE-T-21 -- comp-system: the s.4 per-tool audit deliverable on the current-state COMPILER (1,751 lines, 584 runs; writes infra/system/06_current_state.{md,json}; `--check` rc 0/2/1 as an auto-refresh oracle; the self-test carries the no-fabrication invariant) -- Andrew's ask "understand what this one does" answered by purpose_1line + 4.2, the 4.3 four-case test, Rule T's form on its cross-surface compile, the verdict-bearing row on `--check`

<to_id>NFRA_COMPEFFICACY.TO-CE-T-21</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~N</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete -- implementation adopted and committed at 2e1102da897dfc61e2bc08bf632d2e3f5c7106dd; T-21 result and proof validated before this flip; independent FWD-9 requested from COO; LOCAL ONLY, no push.</status>

**RESEAT 2026-09-03 16:5xZ (issuer 2.0.0_SA_COO, /drive v2 tick 6 seat triage):** `0.8.0_AE_CloudComp~P` NEVER READ this order -- its Codex thread 01a065f6 sat in `systemError` from the GO's delivery (turn-bridge: HARD-NUDGE x3 then TURN-BRIDGE-CANCELLED 14:39Z; the tick-3 rulings and the tick-5 nudge both TURN-BRIDGE-RETRY against the same error; broker delivery state: 93702 / 93733 / 93800 all QUEUED, READ 0 of 4; the app-server refusing model refresh with 404 since 15:04Z), while its heartbeat process kept the seat reading LIVE on the broker -- a forged liveness of the class DRIVE.md s.4 names. The three ~P processes were stopped by the issuer at 16:52Z. The order is RE-ADDRESSED whole to **`0.8.0_AE_CloudComp~N`** (a fresh Codex seat launched 16:52Z through the launcher that now mints its own session id, CTO @2f6dca8204); nothing was built under ~P; the deliverables lane moves to ~N. CORRECTION TO THE RECORD: the tick-2 log's "TEN READ-acks within ~60 s each" over-counted by one -- ~P's GO was never READ.


**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (s.4; s.4.3 + GRAIN; s.4.4 + the verdict-bearing row; s.7 T-21) · **Decomp cell:** `CE-t-21` (STAGE 3; closes on "graded; the unit-1 regen recorded as a side effect") · **Lane:** `.tools/comp-system` (the shim, if one exists -- measure) + `org/modules/graph/comp_system.py` (the ENGINE, 1,751 lines) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~N/comp-system.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~P` (a CODEX seat, Andrew 13:4xZ) holds NFRA_COMPEFFICACY only.

---

## THE CELL

Manifest T-21 (PRD s.7 :649): `comp-system` -> `org/modules/graph/comp_system.py` (1,751); 584 runs; compiles `infra/system/06_current_state.{md,json}`
(a NFRA_SYSTEM compiler reading across ALL scope classes / surfaces); `--check` returns 0/2/1 (an auto-refresh oracle: STALE vs
HEAD-advance); the self-test carries the no-fabrication invariant. Andrew's ask, verbatim in the row: *"understand what this one does"* --
answered by the deliverable's `purpose_1line` + 4.2, not by more code. The decomp's closes-on: **"graded; the unit-1 regen recorded as a
side effect"** (comp-system regenerated `06_current_state` on unit 1's commit; a side effect to record, not a scope widening). `--check`'s
rc is a VERDICT (STALE / current / error) consumed by whatever auto-refreshes on it -- the s.4.4 verdict-bearing row applies to it; the
compile itself is a graded measurement over a cross-surface sweep (Rule T's form applies to that sweep). This is also a tool whose OUTPUT
is a served record (`06_current_state`), so 4.2's disclosure must say what the compiled file asserts about its own vintage.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-system.result.md`: the 31 required s.4 fields (4.1 identity from the ENGINE; `purpose_1line` answers Andrew's question in one
sentence a reader with no context can use; 4.2 disclosure from a QUOTED default run and a `--check` run, incl. what `06_current_state`
prints about its own vintage; 4.3 the four planted answer-state cases on the ratified enum -- SUBJECT_ABSENT_FROM_CORPUS (a scope class /
surface no source carries), PRESENT_WITH_ZERO_RESULTS (a real surface compiling to zero rows, said so), PARTIAL_OR_BLIND (a source the
compile could not read -- the no-fabrication invariant's own case: the compiled record must say the source was unreadable, never fill
it), NOT_APPLICABLE (a mode with no population); rc + text quoted; the GRAIN sentence; 4.4 Rule T's form via `.tools/_compbudget.py` on
the cross-surface compile (a partial compile prints the expiry line and NEVER writes a `06_current_state` that reads complete -- the
no-fabrication invariant meets Rule T here, state how), with the VERDICT-BEARING row on `--check`: at BUDGET REACHED or on an unreadable
source it returns a non-clean rc distinct from 0 (current) and from its STALE/error values, carrying NOT-DECIDABLE -- rc stated on
`--help`; 4.5 the passcraft moves; 4.6 usage at BOTH instruments and the battery at BOTH grains). Then the ONE code change: the 4.3
tokens on every answer, the budget carrier with the no-fabrication guard on a partial compile, the verdict-bearing expiry rc on
`--check`, and a NEW battery `.tools/tests/test_comp_system_battery.py` whose first arm asserts the self-test's no-fabrication invariant
still holds. The unit-1 regeneration is RECORDED (which commit, which fields moved) as the side effect the cell names.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T21-AC1" cell_refs="CE-t-21"/> `T21-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT, 4.1 identity from the ENGINE; `purpose_1line` + 4.2 answer Andrew's "what does this one do" in the reader's terms (quoted), incl. what the compiled record asserts about its own vintage.
<criterion id="T21-AC2" cell_refs="CE-t-21"/> `T21-AC2` -- (AC-2) four PLANTED cases on the ratified enum produce four DISTINCT state tokens in the tool's own voice within one invocation (rc + text quoted); the unreadable-source case shows the compiled record saying so rather than filling (the no-fabrication invariant, exercised on the real binary with a source moved aside).
<criterion id="T21-AC3" cell_refs="CE-t-21"/> `T21-AC3` -- THE SIDE EFFECT RECORDED: unit 1's regeneration of `06_current_state` named by commit and by the fields that moved; zero widening of what comp-system compiles under this cell (diff shown).
<criterion id="T21-AC4" cell_refs="CE-t-21"/> `T21-AC4` -- (AC-4) Rule T's form: `--help` discloses the carrier; a planted small `--budget` on the compile produces the expiry line AND no `06_current_state` that reads complete (the partial is marked or not written -- state which, and why it satisfies the no-fabrication invariant); `--check` at BUDGET REACHED / on an unreadable source returns the non-clean NOT-DECIDABLE rc, exercised by an rc-only consumer, distinct from its 0/2/1 values (all stated on `--help`).
<criterion id="T21-AC5" cell_refs="CE-t-21"/> `T21-AC5` -- battery NEW with the no-fabrication arm first, one arm per new behaviour and a RED mutant each, direct AND pytest at the FILE grain; the engine's own self-test still passes (numbers quoted); commit-gate clean on every .py touched.
<criterion id="T21-AC6" cell_refs="CE-t-21"/> `T21-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself.

<expected_criteria>T21-AC1, T21-AC2, T21-AC3, T21-AC4, T21-AC5, T21-AC6</expected_criteria>

## SURFACES

`org/modules/graph/comp_system.py` (1,751 lines; the compile, `--check`, `--self-test`) @39515415cc · `.tools/comp-system` (measure whether a shim exists) · `infra/system/06_current_state.{md,json}` (the served record -- READ; a regen under this cell is recorded, not silently produced) · `.tools/_compbudget.py` @`2718cffc45` (consumed) · `org/modules/graph/comp_dataflow.py:cmd_gate` @`72e7846ca7` (the verdict-bearing precedent) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` · PRD s.4 + s.7 T-21 @`5bbdab5ec7`.

## BOUNDS

- **What comp-system compiles does not widen**; the no-fabrication invariant is strengthened, never relaxed (a partial compile never writes a record that reads complete).
- **`--check`'s 0/2/1 semantics on a complete run do not change**; only expiry / unreadable-source gains the non-clean rc.
- **No new dependency; no new file outside the engine, a shim if one exists, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` consumed, not edited.
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; surfaced_by = this seat; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

**PUSH (standing law carried onto this CODEX seat's face, 0.0.0_AB_MSTR 93721 on 2.0.0_SA_COO~A's finding 93715, 2026-09-03 15:0xZ):** a shared branch (CLOUD / DEV / PROD / main / SITEZ) is pushed ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and only on Andrew's word while he is at the terminal (LD-0367/0368, LD-0522). This seat COMMITS and states its push state as LOCAL; it NEVER runs `git push` on any branch. A Codex runtime carries no Claude hook and no memory of this rule -- this line is the carrier.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @39515415cc (v0.2.4), cell CE-t-21 (s.1a; STAGE 3; ROUND 6 fence).
<owned_cells>CE-t-21</owned_cells>
Read-dependencies, NOT claimed: CE-t-1 (unit 1's commit, the regen's trigger, DONE), CE-t-25 (the verdict-bearing precedent, DONE), CE-tp-1 (the form, DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 6 -> 6, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or this order's tool (read at 2026-09-03 14:23Z, the file's only token hit being the tool's own header line).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-system compiles from repo-local sources into a repo-local record; no AWS principal, policy or resource is read or changed by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @07601c54c9 (2026-09-03T14:25:19Z); 4/4 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged (2 flagged path(s): NFRA_COMPEFFICACY.TO-CE-T-21.comp-system-s4-audit.proof_of_spec.json GONE; comp-system.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (stage 4 pointers only, the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T21-AC1`..`T21-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~N/NFRA_COMPEFFICACY.TO-CE-T-21.comp-system-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. T21-AC2's unreadable-source
case and T21-AC5's mutants are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_system.py --for "the compile's source list and its unreadable-source path, --check's return values, the self-test's no-fabrication invariant, every corpus-width loop"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain; the engine's own --self-test. AFTER COMMIT: one real `comp-system --check` from a seat other than this lane (the base seat or ~A; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
