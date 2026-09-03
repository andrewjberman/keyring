# TO NFRA_COMPEFFICACY.TO-CE-T-6 -- comp-blast: the s.4 per-tool audit deliverable on the blast-radius tool (167 runs / 30 d, no timeout; kuzu-backed, 27,134 nodes) -- graded; the 4.3 four-case test where NOT-FOUND is NEVER a zero radius (subject-existence + graph vintage + node denominator on every answer); Rule T's form on the traversal; AND the three comp-trace flags carried INTO blast (`--exact`, `--all`, the direction spellings) each answering in blast's own universe -- comp-trace itself UNTOUCHED (PRD v0.6: not retired)

<to_id>NFRA_COMPEFFICACY.TO-CE-T-6</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~G</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete -- lane commits 6df07696eac80fb5322e498d6b121bd9a56d0d02, 9879a8d5ab, c3f3310c00306017e45004c9102199f4e57fffaf, and T6-AC7 follow-on; proof-of-spec-check VALID before this flip; COO distinct-seat FWD-9 accepted with rc 0 and 507/507 traversal; origin/CLOUD ancestry rc=1 and no push. Authority: ROUND 6b, PRD v0.6 @7138c4a176, decomp v0.2.5 @e2b6c1fc96. ADDENDUM 17:3xZ: T6-AC7 (S31's disarm, the budget bounds the whole call) complete -- budgeted universe load serves stale immediately under the Rule-T clock, with age/reason disclosure and no rebuild/wait; S31 disarmed by 0.8.0_AE_CloudComp~G via investigation carrier S32.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.6 @`7138c4a176` (s.4; s.4.3 the enum as DATA + the GRAIN sentence; s.4.4 + the verdict-bearing row; s.6 R-4 as corrected; s.7 rows T-6 and T-19) · **Decomp cell:** `CE-t-6` (closes on "subject-existence + graph vintage + node denominator; NOT-FOUND != zero radius; + the three comp-trace flags carried into blast") · **Lane:** `.tools/comp-blast` (the shim) + its ENGINE under `org/modules/graph/` (name it from the shim's own header; the resolver that answered 58.2% of trace's ids in S17 is the surface the four states must speak through) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~G/comp-blast.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~G` (a CODEX seat) holds NFRA_COMPEFFICACY only.

---

## THE CELL

Manifest T-6 (PRD s.7): `comp-blast` -> `.tools/comp-blast`; 167 runs / 30 d; no timeout; the blast-radius answer over the kuzu graph (27,134 nodes at S17's read). The decomp's closes-on: **subject-existence + graph vintage + node denominator on every answer; NOT-FOUND is never a zero radius** -- S17 measured the failure the other way round: a stratified sample of 158 real comp-trace ids through blast's resolver answered 58.2% at best (41 AMBIGUOUS rc 5, 25 NOT-FOUND rc 3), and blast REJECTED `--exact`, `--all` and the direction spellings that trace's callers use. The L2 ruling (PRD v0.6): comp-trace is NOT retired; **the three flags are CARRIED INTO BLAST under this cell**, each answering in blast's own universe (kuzu ids), with the four answer-states -- so a caller who brings a trace-shaped flag gets blast's answer or a NAMED state, never a usage error; and comp-trace's own bytes are untouched (its callers are not redirected here; that was T-19's retired act).

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-blast.result.md`: the 31 required s.4 fields (4.1 identity from the ENGINE, the shim named as the shim, the graph it reads with its `built:` vintage line; 4.2 disclosure from a QUOTED default run on a real subject and from a run on an ABSENT subject; 4.3 the four planted answer-state cases on the ratified enum -- SUBJECT_ABSENT_FROM_CORPUS (an id no node carries: rc 3 NOT-FOUND stays, the token added, the denominator and vintage printed -- NEVER "radius 0"), PRESENT_WITH_ZERO_RESULTS (a real node with no edges in the asked direction: radius 0 WITH the node named and the denominator), PARTIAL_OR_BLIND (an AMBIGUOUS resolution rc 5 in the tool's own voice, naming the candidates and their count; and a budget-cut traversal), NOT_APPLICABLE (a mode/direction with no population); rc + text quoted; the GRAIN sentence; 4.4 Rule T's form via `_compbudget.py` on the traversal (the tool has NO timeout today: the form is added on the traversal loop with the default budget, the cursor as in s.4.4, and the VERDICT-BEARING row only if blast's rc is a verdict for any consumer -- census the consumers (167 runs) and state it; if rc is execution-only, the row is recorded as NOT APPLICABLE with the census as the reason); 4.5; 4.6 usage at BOTH instruments and the battery at BOTH grains). **THE CARRY:** `--exact` (resolve the subject by exact id only, no fuzzy candidates -- AMBIGUOUS becomes NOT-FOUND with the exact token), `--all` (every direction; today's default named), and the direction spellings trace's callers use (enumerate them from S17's evidence and trace's `--help`; each maps onto blast's existing direction argument -- aliases, not new semantics). Then the code change (tokens, the carry, the budget carrier) and a NEW battery `.tools/tests/test_comp_blast_battery.py` with a RED mutant per arm (the mutant printing radius 0 on NOT-FOUND among them; a mutant that lets `--exact` return a fuzzy candidate; a mutant that maps a direction alias onto the wrong direction).

## ACCEPTANCE

<criterion id="T6-AC1" cell_refs="CE-t-6"/> `T6-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT; 4.1 from the ENGINE with the graph's `built:` vintage quoted; the shim named as the shim.
<criterion id="T6-AC2" cell_refs="CE-t-6"/> `T6-AC2` -- (AC-2) four PLANTED cases on the ratified enum produce four DISTINCT state tokens (rc + text quoted); NOT-FOUND carries the token, the node denominator and the vintage and NEVER a radius; AMBIGUOUS names its candidates.
<criterion id="T6-AC3" cell_refs="CE-t-6"/> `T6-AC3` -- THE CARRY: `--exact`, `--all` and every direction spelling enumerated from S17 + trace's `--help` are ACCEPTED by blast and answer in blast's universe (a table: flag -> blast argument -> one real run's rc + first line); comp-trace's files byte-identical before/after (sha quoted); no caller redirected.
<criterion id="T6-AC4" cell_refs="CE-t-6"/> `T6-AC4` -- (AC-4) Rule T's form on the traversal: `--help` discloses the carrier, the budget and the cursor; a planted small `--budget` produces the expiry line, PARTIAL_OR_BLIND, the denominator and a cursor followed to completion; the verdict-bearing row applied or recorded NOT APPLICABLE with the consumer census (denominator printed).
<criterion id="T6-AC5" cell_refs="CE-t-6"/> `T6-AC5` -- battery NEW with a RED mutant per arm, direct AND pytest at the FILE grain; commit-gate clean on every .py touched.
<criterion id="T6-AC6" cell_refs="CE-t-6"/> `T6-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the lane commits itself; FWD-9: one real post-commit `comp-blast` run with a carried flag from a seat other than this lane (ask the issuer for the distinct seat if no free lane exists; the issuer's seat qualifies).

<criterion id="T6-AC7" cell_refs="CE-t-6"/> `T6-AC7` -- ADDENDUM (issuer 2.0.0_SA_COO 17:3xZ on 1.0.0_SA_CTO 93837 + 3.0.0_SA_CVO 93833, row S31 @ce5c7babea): THE BUDGET BOUNDS THE WHOLE CALL, NOT ONLY THE TRAVERSAL -- a budgeted comp-blast call (`--budget N`, or the 90 s default) never runs or waits on a kuzu rebuild: `load_kuzu_universe(refresh=True)` at cli.py:799/:1053 (re-locate by content) is entered under the same Rule T clock as the traversal and, when the served graph is stale, SERVES THE EXISTING GRAPH IMMEDIATELY labeled stale with its age on the disclosure line (CE-g-5's `ensure_fresh(wait_for_peer=False)` contract, the comp-find --corpus aws pattern) -- the rebuild is never started inside a budgeted call; an unbudgeted call (`--budget 0`, or `--force`) keeps today's refresh path and SAYS SO on its first line. Evidence: S31's own probe re-run (`.tools/comp-blast gold:A_00.accounts_dimension --exact --budget 60` against a stale graph) returns inside 60 s with the stale label and age and NO rebuild.lock created (the lock's absence read from infra/aws/globgrph/ after the call, plus the process table showing no kuzu_nessie_load.py child); one new RED-first battery arm; S31 disarmed by the lane (disarm_owner 0.8.0_AE_CloudComp~G) with the row cited; the proof instance refreshed and VALID; comp-trace untouched.
<expected_criteria>T6-AC1, T6-AC2, T6-AC3, T6-AC4, T6-AC5, T6-AC6, T6-AC7</expected_criteria>

## SURFACES

`.tools/comp-blast` (the shim) · the engine it names under `org/modules/graph/` @e2b6c1fc96's HEAD · the kuzu graph (READ; `built:` line is the vintage) · `.tools/comp-trace` and its engine (READ ONLY -- byte-identical after; the flag spellings are read from its `--help`) · S17@a140eed779 (the measurement) · `.tools/_compbudget.py` @`2718cffc45` (consumed) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` · PRD s.4 + s.6 R-4 + s.7 T-6/T-19 @`7138c4a176`.

## BOUNDS

- **comp-trace is NOT retired and is NOT edited**; its callers are not redirected; the carry lives in blast only. Aliases, not new semantics: a carried flag maps onto an EXISTING blast argument or answers with a NAMED state.
- **The graph is READ; never rebuilt** (query, never rebuild -- CLAUDE.md rule 20).
- **No new dependency; no new file outside the engine, the shim, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` consumed, not edited.
- **A spec-vs-world divergence is a ROW** in `surprise-channel/investigations/INVESTIGATION_v1.md` (append your row and COMMIT IT IN THE SAME ACT, pathspec the file only; a co-worker's valid row is ADMITTED by the gate since @07cb6153e3 -- no override needed for a row whose surfacer holds an open order on this project; an INVALID foreign row is reported to the issuer, never amended), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

**PUSH (standing law on this CODEX seat's face):** a shared branch (CLOUD / DEV / PROD / main / SITEZ) is pushed ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and only on Andrew's word while he is at the terminal (LD-0367/0368, LD-0522). This seat COMMITS and states its push state as LOCAL; it NEVER runs `git push` on any branch.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @e2b6c1fc96 (v0.2.5), cell CE-t-6 (s.1a; STAGE 2; ROUND 6b; the CE-t-19 dependency DROPPED at v0.2.5).
<owned_cells>CE-t-6</owned_cells>
Read-dependencies, NOT claimed: CE-t-19 (CLOSED NOT-RETIRED; S17 is read as evidence), CE-t-25 (the verdict-bearing precedent, DONE), CE-tp-1 (DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (read at 2026-09-03 15:40Z); 0 armed gates name NFRA_COMPEFFICACY or this order's tool.
comp-iam: DECLARED-NOT-APPLICABLE -- comp-blast reads a repo-local graph; no AWS principal, policy or resource is read or changed by this order.
comp-adversary: RUN -- rc 0 at read-vintage @5bb91c894d (2026-09-03T16:21:57Z); 6/6 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 5 attempted / 3 stable / 2 flagged (NFRA_COMPEFFICACY.TO-CE-T-6.comp-blast-s4-audit.proof_of_spec.json GONE; comp-blast.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T6-AC1`..`T6-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~G/NFRA_COMPEFFICACY.TO-CE-T-6.comp-blast-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the lane commits itself. T6-AC2's NOT-FOUND-never-a-radius
arm and T6-AC3's byte-identical trace are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read .tools/comp-blast --for "the engine it names, every flag it accepts, the direction argument's spellings, the rc mapping"`; `comp-read <the engine> --for "the resolver (exact vs fuzzy), the NOT-FOUND and AMBIGUOUS paths, the traversal loop, where a radius is printed"`; `comp-read .tools/comp-trace --for "every flag it accepts and the direction spellings"` (READ ONLY). BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-blast` run with a carried flag from a seat other than this lane (FWD-9).
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after (blast AND trace, trace unchanged), the carry table, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
