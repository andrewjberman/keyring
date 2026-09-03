# TO NFRA_COMPEFFICACY.TO-CE-T-8 -- comp-iam: the s.4 per-tool audit deliverable, the 4.3 four-case test with the effective-deny THREE-STATE as the graded voice ("no parsed deny" is never "allowed"), and Rule T's form on its AWS-plane calls

<to_id>NFRA_COMPEFFICACY.TO-CE-T-8</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked, 2026-09-03T07:15:00Z; committed by the assignee itself under the tree task-orders/** -> ANY lane grant @f9c97a52ce) -- proof-of-spec VALID (rc=0) at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-8.comp-iam-s4-audit.proof_of_spec.json; T8-AC1..AC6 self-assessed PASS (deliverable comp-iam.result.md at the tree home, fix commit eb7966105a, deliverable+proof commit dace2c42b8). CVO grade pending -- certifier != author. No surprises filed under this cell (S9's own precedent: an audit finding inside a per-tool deliverable is not a spec-vs-world row -- see finding F4). Push state MEASURED in the DELIVERABLE REPORT to 2.0.0_SA_COO, not asserted here. Prior history: pending -- GO paired at cut. Authority: round 3 of the canonical loop on NFRA_COMPEFFICACY -- CVO's round-2 stamp @88c961297b (ZERO GRADUATION: proceed to the next L6 dispatches), decomp v0.2.1 @070907b56e (STAGE 2's FIRST cell: CE-t-8 deny mode -> CE-t-6 -> CE-t-9 -> CE-t-7; ROUND 3 fence: CE-t-8 at the base seat), on Andrew's words on the loop (@10a4beaffb, @de2d6d643c). No sequencing dependency (the row's depends_on is empty). Continuity at the base seat that closed CE-g-5.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.4 @`19bf1c7322` (s.4 the schema, s.4.3 the enum as DATA, s.4.4 RULE T's FORM; s.7 row T-8 :609) · **Decomp cell:** `CE-t-8` (= manifest T-8; STAGE 2, "the 4.3 answer-state fixes, each closes on AC-2") · **Lane:** `.tools/comp-iam` (the 8-line bash shim, ANY) + `org/modules/graph/iam_cli.py` and its three siblings `comp_iam_live.py` / `comp_iam_census.py` / `comp_iam_investigate.py` (the ENGINE) + `.tools/tests/**` (TOOL_BATTERIES); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-iam.result.md` (owner by path). Lanes MEASURED at cut with `owned-paths-validate --check-agent`: the shim, the four engine files, `.tools/tests/`, the deliverables folder -- 7 of 7 PERMITTED for `0.8.0_AE_CloudComp`; a lane refusal at commit is a ROW, never a self-grant. **Rule 27 seating:** `0.8.0_AE_CloudComp` BASE holds NFRA_COMPEFFICACY only (CE-g-5 terminal @`7e3b23578d`; continuity on the same project).

---

## THE CELL

Manifest T-8 (PRD s.7 :609): `comp-iam` -> `.tools/comp-iam` (14 subcommands); 113 runs; "no timeout"; "cannot answer
deny" is a DECLARED BLIND SPOT. MEASURED at cut @`070907b56e`: the shim forwards to `org/modules/graph/iam_cli.py`
(**1,624 lines**; siblings `comp_iam_live.py` 461, `comp_iam_census.py` 230, `comp_iam_investigate.py` 299 -- 2,614 in
all); subcommands include `gaps`, `roles`, `services`, `service`, `role`, `stats`, `attach-census`, `resource-sweep`,
`simulate` (`cmd_simulate` `:668`, boto3 `simulate_principal_policy` `:726`, an OFFLINE stubbed mutant suite
`_simulate_self_test` `:816`); the false-deny modes are ALREADY DOCUMENTED IN THE TOOL'S OWN DOCSTRING (`:673-:692`):
(1) a conditioned statement evaluated with no `--context` returns `implicitDeny` BYTE-IDENTICAL to a real deny; (2) a
call carrying 2+ `--resource-arns` flips the HELD ones to `implicitDeny` -- one ARN per call. A third trap lives in
the census: `refresh-census` carries a 24 h TTL and the APPLIED plane is unusable past it (measured 664 h stale on
2026-09-01; it now fails CLOSED and loudly). **The cell's closes-on, verbatim from the decomp: "effective-deny
three-state; 'no parsed deny' is never 'allowed'."** That is the 4.3 voice this audit grades: every deny-shaped answer
comp-iam gives is ALLOWED / DENIED / NOT-DECIDABLE, and the absence of a parsed deny is NOT-DECIDABLE, never ALLOWED.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-iam.result.md`: one fenced JSON block +
prose; the 31 required s.4 fields (4.1 identity from the ENGINE `iam_cli.py`, never the shim; 4.2 disclosure from a
QUOTED default run; 4.3 the four planted answer-state cases keyed on the RATIFIED enum
`org/standards/COMPTOOL_ANSWER_STATE.enum.json` in the tool's own voice, with the deny three-state as the graded
surface -- SUBJECT_ABSENT_FROM_CORPUS: a role or service NOT in the census (the tool says absent, never "no gaps");
PRESENT_WITH_ZERO_RESULTS: a role present with zero gaps; PARTIAL_OR_BLIND: a conditioned statement simulated with no
`--context` AND a census past its TTL -- both must read NOT-DECIDABLE / refused, never DENIED and never ALLOWED;
NOT_APPLICABLE: a subcommand with no population for the subject; each case rc + text quoted; the OFFLINE stub suite at
`:816` is the fixture for the simulate cases so ZERO live IAM calls are needed to plant them; 4.4 Rule T's form APPLIED
via the ONE shared module `.tools/_compbudget.py` -- carrier `--budget` > env `COMP_BUDGET_S` > default, the source
word on the denominator line, every AWS-plane call and every corpus-width sweep (`resource-sweep`, `attach-census`)
under `remaining()` with the expiry line in the s.4.4 grammar, the DEFERRED bucket for calls that would outlive the
budget; the non-application half stated for the census-file subcommands that have no corpus-width loop; 4.5 the
passcraft moves; 4.6 usage at BOTH instruments and the battery at BOTH grains). Then the ONE code change this cell
owes: the budget carrier wired through `_compbudget.py` with `--help` disclosing it, and the three-state made
MACHINE-REJECTABLE wherever a deny-shaped answer is printed (a consumer can tell ALLOWED from DENIED from NOT-DECIDABLE
by token, and "no parsed deny" prints NOT-DECIDABLE). **Neither the census format nor the gap semantics change.**

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T8-AC1" cell_refs="CE-t-8"/> `T8-AC1` -- the deliverable parses (one fenced JSON block), every required s.4 field present or explicitly ABSENT, 4.1 identity read from the ENGINE path (`iam_cli.py`), the shim named as the shim.
<criterion id="T8-AC2" cell_refs="CE-t-8"/> `T8-AC2` -- (AC-2) four PLANTED cases keyed on the ratified enum produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case), planted through the OFFLINE stub suite where the case is a simulate case -- zero live IAM calls owed by this criterion.
<criterion id="T8-AC3" cell_refs="CE-t-8"/> `T8-AC3` -- THE THREE-STATE: every deny-shaped answer prints exactly one of ALLOWED / DENIED / NOT-DECIDABLE by token; a conditioned statement with no `--context` prints NOT-DECIDABLE (never DENIED); a batched multi-ARN call is REFUSED or split (never a HELD ARN read as denied); a census past its TTL prints NOT-DECIDABLE / refused (never ALLOWED); the pair (a real deny vs a false deny) shown side by side from the stub suite.
<criterion id="T8-AC4" cell_refs="CE-t-8"/> `T8-AC4` -- (AC-4) Rule T's form applied: `--help` discloses the carrier via `_compbudget.py`; a planted small `--budget` on a corpus-width sweep produces the s.4.4 expiry line with its source word and reached denominator, side by side with a clean completion line; an AWS-plane call that would outlive the budget lands in the DEFERRED bucket, never a hang; the non-application half stated for the census-file subcommands.
<criterion id="T8-AC5" cell_refs="CE-t-8"/> `T8-AC5` -- battery: `_simulate_self_test` stays GREEN (its arm count stated) plus ONE new arm per new behaviour (the three-state token, the budget carrier), each with a planted mutant RED; stated at the FILE grain, directory grain of `.tools/tests/` as it reads.
<criterion id="T8-AC6" cell_refs="CE-t-8"/> `T8-AC6` -- push state MEASURED at report (ls-remote + is-ancestor; LOCAL expected while Andrew gates the cadence, say which state was read); the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the seat commits itself.

<expected_criteria>T8-AC1, T8-AC2, T8-AC3, T8-AC4, T8-AC5, T8-AC6</expected_criteria>

## SURFACES

`.tools/comp-iam` (8 lines, the shim) · `org/modules/graph/iam_cli.py` (1,624 lines; `:47` `cmd_gaps` .. `:668` `cmd_simulate`, `:673-:692` the documented false-deny modes, `:726` `simulate_principal_policy`, `:816` `_simulate_self_test`) @`070907b56e` · `org/modules/graph/comp_iam_live.py`, `comp_iam_census.py`, `comp_iam_investigate.py` · `.tools/comp-iam-usage` · `.tools/_compbudget.py` @`2718cffc45` · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` @`19bf1c7322` · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` (the two usage instruments) · the estate's recorded traps for this tool: `docs/briefs/comp-iam-false-missing-tf-resource-collision-20260626.md`; the 24 h census TTL (`refresh-census`) · PRD s.4 + s.7 T-8 @`19bf1c7322` · precedents: `deliverables/0.8.0_AE_CloudComp/comp-find.result.md` @`6d04680f2b`, `deliverables/0.8.0_AE_CloudComp~A/comp-read.result.md` @`e0f0e5a9e6`.

## BOUNDS

- **ZERO IAM CHANGE.** No principal, policy, role, attachment or resource is created, changed or granted under this cell; `simulate-principal-policy` and `get_role` are the only live calls and both are READ-ONLY, under the seat's standing role, and only where the stub suite cannot plant the case. A live call that needs a context value the seat does not hold is NOT-DECIDABLE, not a reason to widen a policy.
- **Census format and gap semantics do NOT change**; the three-state is added to the VOICE, not to the census.
- **No new dependency; no new file outside the engine files named, the battery, the deliverable and the proof instance.** `_compbudget.py` is consumed, not edited (a needed change there is a ROW).
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), then keep working; never a message.
- **Certifier != author:** the s.7 row-state word is the L4 owner's version bump on the L8/L9 seat's documentation, read from the record.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @070907b56e (v0.2.1), cell CE-t-8 (s.1a, = manifest T-8; STAGE 2's first in s.2; ROUND 3 fence).
<owned_cells>CE-t-8</owned_cells>
Read-dependencies, NOT claimed: CE-disc-2 (the enum, DONE as spec), CE-tp-1 (Rule T's form, DONE as spec), CE-t-1 / CE-t-2 (the form's applications, terminal), CE-t-3 (in parallel at the ~A lane -- no dependency either way), CE-t-6 / CE-t-9 / CE-t-7 (STAGE 2's next cells, after this one).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 336 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or comp-iam (read at 2026-09-03 05:57Z).
comp-iam: DECLARED-NOT-APPLICABLE -- the subject is comp-iam's own VOICE and budget carrier in a repo-local engine; no AWS principal, policy or resource is created, changed or granted by this TO (BOUNDS: zero IAM change); the only live calls are the tool's existing read-only simulate/get_role under the seat's standing role, unchanged in scope. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @16328ba06c (2026-09-03T06:06:01Z); 9 commits, 9 repo paths, 0 file:line cites (the `:NN` pins are inside backticks), 10 tool mentions; cited commits 9 attempted / 9 verified / 0 UNVERIFIABLE; cited paths 9 attempted / 7 stable / 2 flagged (2 GONE at read-vintage = the deliverable file and the proof instance this TO CREATES -- expected, not stale); uncited siblings 775 with the cap (25) declared; DEFERRED bucket not printed (--no-packet: stage 4 disabled by the caller, disclosed); 5 declared exclusions (v1 contract). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T8-AC1`..`T8-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-8.comp-iam-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself.
T8-AC3's real-deny/false-deny pair and T8-AC5's planted mutants are the controls that must be able to FAIL; every
`surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/iam_cli.py --for "where a deny-shaped answer is printed, how the false-deny modes are guarded, and where a corpus-width sweep loops"` and `--enumerate 'implicitDeny|explicitDeny|allowed|NOT-DECIDABLE|timeout=|remaining'`; `comp-iam refresh-census` BEFORE any APPLIED-plane read (the 24 h TTL). BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; `_simulate_self_test` + the new arms direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-iam gaps` (or `stats`) from a seat other than this one (the ~A lane is the nearest; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record, not a message) with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
