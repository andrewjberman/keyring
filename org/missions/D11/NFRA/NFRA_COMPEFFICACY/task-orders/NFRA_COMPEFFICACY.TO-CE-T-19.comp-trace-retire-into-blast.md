# TO NFRA_COMPEFFICACY.TO-CE-T-19 -- retire comp-trace INTO comp-blast on Andrew's R-4 ruling (condition MET): the subset claim MEASURED at the flag and traversal grain first, the carrier census with its denominator, the shim becomes a declared-successor FORWARDER with parity proven, the callers are told through the record -- the executable goes LAST and not in this cell

<to_id>NFRA_COMPEFFICACY.TO-CE-T-19</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~B</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>WITHDRAWN 2026-09-03 12:3xZ by the issuer 2.0.0_SA_COO -- the order STOPPED AT ITS OWN GATE (deliverable step 1 / T19-AC1's second limb, 'a ROW and a stop'): R-4's condition ('if so') is measured NOT MET at the traversal grain -- comp-trace answers over a head-pinned working-tree scan (2,302 nodes: gold:/lambda:/s3:/eventbridge: ids) and comp-blast over kuzu (27,134 nodes) with ZERO ids in those address spaces even after a forced refresh; a stratified sample of 158 real trace ids through blast's resolver answers 58.2% at best (41 AMBIGUOUS rc 5, 25 NOT-FOUND rc 3); building the forwarder would convert roughly two in five working comp-trace calls into NOT-FOUND/AMBIGUOUS, the false-clear class cli.py:377-380 exists to prevent. Row NFRA_COMPEFFICACY-S17@a140eed779 (0.8.0_AE_CloudComp~B; BLOCKING/ARMED, disarm owner 1.0.0_SA_CTO); deliverable comp-trace.result.md @bfbff9dc14 (flag table, 8-row parity table, carrier census 171 live of 4,814, caller census 57 all-time). Nothing built, edited or deleted; production sha unchanged; no proof instance filed by design. The route is 3.0.0_SA_CVO's at L10 (the PRD's T-19 claim=measured is false at this grain; R-4 is conditional and its condition failed -- re-adjudication at L2, possibly Andrew's since it is his ruling's condition). CE-t-6 depends on this cell and waits. PRIOR: pending -- GO paired at cut. Authority: PRD v0.5 @5bbdab5ec7 s.7 row T-19 (verb: retire; R-4) and the R-4 heading (Andrew, 2026-09-02: "comp ...</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (s.7 T-19 and the R-4 heading at :609; T-22 at :650 is the pattern) · **Decomp cell:** `CE-t-19` · **Lane:** `.tools/comp-trace` + `.tools/comp-blast` (ANY) + `org/modules/graph/cli.py` (the ENGINE, trace :354-471 / blast :796-1189 / parsers :1465-1580) + `.tools/tests/**`; registry carriers as the census finds them (a lane refusal at commit is a ROW, never a self-grant); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~B/comp-trace.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~B` holds NFRA_COMPEFFICACY only.

---

## THE CELL

Andrew's R-4, quoted from the PRD heading: *"comp-trace ... if so it should be retired."* The "if so" is the subset condition; the
L4 owner measured it MET. The decomp's closes-on, verbatim: **"retired THROUGH the estate's own alias mechanism (the T-22
pattern: declared successor, callers told first, executable last); his ruling cited."** MEASURED at cut @`7b649df39d`:
`.tools/comp-trace` is a 9-line bash shim over `cli.py trace`; `.tools/comp-blast` the same over `cli.py blast`; cmd_trace is
:354-471 (its own `--exact` NOT-FOUND rc 3 dial, `--all`, `--direction up|upstream|down|downstream|both`, `--depth`,
`--json`), cmd_blast :796-1189 (`--direction up|down|both`, `--depth`, `--json`, `--function`, `--check-consumers`, `--compare`,
`--overlap-sweep`, ...). 45 runs in the window, three callers: `0.7.0_AE_CloudOps~F` 18, `~D` 14, `3.0.0_SA_CVO` 11. No battery
exists for either shim at cut.

## DELIVERABLE -- the T-22 pattern, in its order

1. **THE SUBSET CLAIM, MEASURED FIRST at the flag and traversal grain** (the ruling's own condition, re-derived at this seat with
   a different instrument from the L4 owner's line-range cite): for every trace flag, its blast equivalent or its ABSENCE
   (`--exact` and the `upstream`/`downstream` spellings are the ones to look at); for a fixed set of real queries (>= 6,
   covering a hit, a prefix hit, an `--exact` hit, an `--exact` miss, a NOT-FOUND, `--json`), trace's output vs blast's with
   the equivalent flags -- node sets equal, rc equal (the NOT-FOUND rc 3 dial preserved). **Where trace has something blast
   lacks, the retirement carries it INTO blast** (a flag, a rendering) -- never retires it silently; that carry is in scope
   and bounded to cli.py's blast parser + render. If the subset condition FAILS on a measured axis that cannot be carried, the
   order STOPS at a ROW (spec-vs-world) and reports -- R-4's "if so" is the gate.
2. **THE CARRIER CENSUS, DENOMINATOR PRINTED** (`comp-find -i 'comp-trace' --all`, `--files`, then by band): every file that
   names comp-trace -- shims, `comp-which`'s index/descriptions, `comp-tools.yaml` / coverage map / output contracts (whatever
   the registry carriers are named), hooks, skills, docs, CLAUDE.md/annex, tests, the telemetry. Each carrier with its LANE:
   the ones this lane may edit are edited here; the ones it may not are a routed list to `2.0.0_SA_COO` (the sequencer places
   them), never a self-grant and never left silent (the T-22 lesson: ~15 live carriers where 5 were assumed).
3. **THE DECLARED SUCCESSOR -- the alias:** `.tools/comp-trace` becomes a FORWARDER onto `comp-blast` (mapping any trace-only
   spelling to its blast equivalent), printing ONE stderr line naming the successor, the ruling and the date, with stdout and
   rc byte-identical to the direct `comp-blast` call (parity proven by the battery); the registry carriers carry
   `successor: comp-blast` / `RETIRED (R-4)` in whatever field the estate's contract uses (read `COMPTOOL_REGISTRATION_FLOW.md`
   first -- the estate's mechanism, never a new one); `comp-which` routes a comp-trace question to comp-blast.
4. **CALLERS TOLD FIRST, through the record:** the caller census (the 45 runs by seat, from `org/mcp/comp-tool-runs.jsonl` /
   the rail log, denominator printed) lands in the deliverable; the notice to those seats is `2.0.0_SA_COO`'s broadcast on
   this cell's report (a Tier-2 lane does not message Tier-1 seats about their habits); the forwarder's stderr line tells every
   future caller at the call site.
5. **THE EXECUTABLE GOES LAST, AND NOT HERE:** the forwarder stays; removal of `.tools/comp-trace` is a separate act on a later
   word (after the callers' next runs show the notice was read, or Andrew's word) -- record that condition in the deliverable
   and do NOT delete the shim in this cell.
6. **The battery** `.tools/tests/test_comp_trace_retirement_battery.py` (NEW): parity arms over the fixed query set (trace-via-
   forwarder == blast direct, stdout + rc), the NOT-FOUND rc 3 arm, the `--exact` arm, the stderr notice arm, and a planted
   mutant per arm going RED; direct AND under pytest at the FILE grain; directory grain stated as it reads.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T19-AC1" cell_refs="CE-t-19"/> `T19-AC1` -- SUBSET MEASURED: the flag table (trace flag -> blast equivalent or ABSENT) and the >= 6-query parity table (node sets + rc) in the deliverable, from real runs; any trace-only capability carried into blast with its diff shown, or a ROW and a stop.
<criterion id="T19-AC2" cell_refs="CE-t-19"/> `T19-AC2` -- CARRIER CENSUS with denominator: every file naming comp-trace listed with its lane and disposition (edited here / routed to 2.0.0_SA_COO / telemetry, untouched); the in-lane carriers updated to the declared successor using the estate's own registration mechanism, cited.
<criterion id="T19-AC3" cell_refs="CE-t-19"/> `T19-AC3` -- THE FORWARDER: `.tools/comp-trace` forwards onto comp-blast with byte-identical stdout and rc across the query set, one stderr notice line naming the successor + R-4 + the date; `comp-which` routes a comp-trace question to comp-blast (quoted).
<criterion id="T19-AC4" cell_refs="CE-t-19"/> `T19-AC4` -- CALLERS AND THE LAST STEP: the caller census by seat (45 runs, denominator printed) in the deliverable; the removal condition for the executable written down; the shim NOT deleted (its presence measured at report).
<criterion id="T19-AC5" cell_refs="CE-t-19"/> `T19-AC5` -- battery NEW with parity, NOT-FOUND, `--exact`, notice arms and a RED mutant each, direct AND pytest at the FILE grain; commit-gate clean; the proof instance VALID (every `surprises` entry resolving to a row id); push state MEASURED; the complete flip self-committed.

<expected_criteria>T19-AC1, T19-AC2, T19-AC3, T19-AC4, T19-AC5</expected_criteria>

## SURFACES

`.tools/comp-trace`, `.tools/comp-blast` (9-line shims) · `org/modules/graph/cli.py` @`7b649df39d` (cmd_trace :354-471, `_trace_near_matches` :306-323, `_emit_trace_provenance` :326-351; cmd_blast :796-1189; parsers :1465-1580) · `org/modules/graph/comp_log_auto.py` (the run logger both shims call) · the registry carriers (census, item 2): `comp-which`'s index, `COMPTOOL_REGISTRATION_FLOW.md`, `comp-tools.yaml`, `comp-coverage-map.yaml`, `comp-output-contracts.yaml` (names from the T-22 row; confirm each exists) · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` (the callers) · PRD s.7 T-19 + R-4 + T-22 @`5bbdab5ec7` · `.tools/tests/` (0 files for either shim at cut).

## BOUNDS

- **Nothing is deleted in this cell.** The shim stays as a forwarder; `cli.py trace` stays callable; removal is a later act on a later word.
- **Blast changes are bounded to carrying trace-only capability** (a flag spelling, `--exact`, a rendering) -- no change to blast's traversal, scoring or verdict semantics (CE-t-6's audit owns those).
- **Registry edits use the estate's own mechanism** (`COMPTOOL_REGISTRATION_FLOW.md`); a carrier outside this lane is ROUTED, never edited.
- **No new dependency; no new file outside the shims, cli.py, the in-lane carriers, the NEW battery, the deliverable and the proof instance.**
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO or the caller seats.
- **Certifier != author.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @dcf07b4799 (v0.2.3), cell CE-t-19 (s.1a; ANY TIME -> ROUND 5 fence).
<owned_cells>CE-t-19</owned_cells>
Read-dependencies, NOT claimed: CE-t-6 (comp-blast's audit -- depends on THIS cell; not started), CE-t-22 (the alias pattern's precedent, its code half landed), CE-t-9 / CE-t-25 (in parallel; no dependency any way).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 21 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 4 -> 4, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY, comp-trace, comp-blast or cli.py (read at 2026-09-03 09:27Z).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-trace / comp-blast read the local trace graph; no AWS principal, policy or resource is read or changed by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @dcf07b4799 (2026-09-03T11:15:22Z); 4/4 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged = this order's two OUTPUTS (the deliverable and the proof instance, GONE by construction at cut); uncited neighborhood 234 (25 shown, cap declared); --no-packet (stage 4 pointers only, the caller's choice, recorded in the declaration).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T19-AC1`..`T19-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~B/NFRA_COMPEFFICACY.TO-CE-T-19.comp-trace-retire-into-blast.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. T19-AC1's
parity table and T19-AC5's mutants are the controls that must be able to FAIL; a subset failure is a ROW, not a softened PASS.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/cli.py --for "every flag cmd_trace accepts that cmd_blast does not, and the two NOT-FOUND dials"`; `comp-find -i 'comp-trace' --all --files` (the carrier census; never head it; use --band/--page); `comp-read <the registration flow doc> --for "how a retired tool declares its successor"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-trace <query>` from a seat other than this lane, its stderr notice and parity read there (the base seat or ~A is the nearest; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record) with per-criterion evidence, the carrier census, the caller census, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
