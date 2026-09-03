# TO NFRA_COMPEFFICACY.TO-CE-T-7 -- comp-dataflow: the s.4 per-tool audit deliverable, the 4.3 four-case test with the HONEST-UNRESOLVED read preserved (4 of 4) and its print ENRICHED, and Rule T's form -- the tool never guesses through deploy-time config

<to_id>NFRA_COMPEFFICACY.TO-CE-T-7</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~A</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut. Authority: round 4 of the canonical loop on NFRA_COMPEFFICACY -- CVO's round-3 stamp @7ec9bf06dd (ZERO GRADUATION: proceed to the next L6 dispatches), decomp v0.2.2 @b7daeaa6f0 (STAGE 2; ROUND 4 fence: CE-t-7 at the ~A lane, in parallel with CE-t-9), on Andrew's words on the loop (@10a4beaffb, @de2d6d643c). No sequencing dependency (the row's depends_on is empty). Continuity at the lane that closed CE-t-2 and CE-t-3.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.4 @`19bf1c7322` (s.4 the schema, s.4.3 the enum as DATA, s.4.4 RULE T's FORM; s.7 row T-7 :608) · **Decomp cell:** `CE-t-7` (= manifest T-7; STAGE 2, "the 4.3 answer-state fixes, each closes on AC-2") · **Lane:** `.tools/comp-dataflow` (the bash shim, ANY) + `org/modules/graph/comp_dataflow.py` (the ENGINE) + `.tools/tests/**` (TOOL_BATTERIES); the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.result.md` (owner by path; the lane's own folder and agent home @`05b7e1c77e`). A lane refusal at commit is a ROW, never a self-grant. **Rule 27 seating:** `0.8.0_AE_CloudComp~A` holds NFRA_COMPEFFICACY only (CE-t-3 terminal @`7f4cbd3dc8`; continuity).

---

## THE CELL

Manifest T-7 (PRD s.7 :608): `comp-dataflow` -> `comp_dataflow.py`; 11 runs; `origin` / `gate` modes; no timeout; the
manifest's own words: "preserve 4/4 honest-unresolved; enrich unresolved print (CVO~A s.6); never guess through deploy-
time config". MEASURED at cut @`b7daeaa6f0`: the shim forwards to `org/modules/graph/comp_dataflow.py` (**476 lines**; the
VALUE-ORIGIN trace: every read source with its LAYER, served-origin reads flagged -- the item-9 violation class; `:33`
"UNRESOLVED and is COUNTED (a zero is never printed without its denominator)"; `:280` `is_unresolved = layer == "unknown"
and _DYNAMIC in resolved`; `:311` "producer lane (unresolved firm tree)"; `:348-352` the summary counts reads_scanned /
reads_unresolved / served_origin_unexempted / exempted; `:361` `cmd_origin`). The cell's closes-on, verbatim from the
decomp: **"4/4 honest-unresolved PRESERVED; unresolved print enriched; never guesses through deploy-time config."** The
4.3 voice this audit grades: an UNRESOLVED read is PARTIAL_OR_BLIND said in the tool's own voice with WHY it could not
resolve (a dynamic path part, a deploy-time-only value, a firm tree not on disk) -- and it must NEVER be resolved by
guessing through deploy-time config (an env var, a Terraform value, a served artifact) to make the count look smaller.
No battery exists for this tool at cut (0 files in `.tools/tests/`).

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.result.md`: one fenced JSON block
+ prose; the 31 required s.4 fields (4.1 identity from the ENGINE; 4.2 disclosure from a QUOTED default run; 4.3 the four
planted answer-state cases keyed on the RATIFIED enum `org/standards/COMPTOOL_ANSWER_STATE.enum.json` -- SUBJECT_ABSENT_
FROM_CORPUS: a script path that does not exist (the tool says absent, never "0 reads"); PRESENT_WITH_ZERO_RESULTS: a real
producer with zero reads of any layer; PARTIAL_OR_BLIND: the honest-unresolved class -- a producer whose read path has a
dynamic part the SOURCE plane cannot resolve, printed as UNRESOLVED with its reason and COUNTED in the denominator, the
4 known honest-unresolved specimens PRESERVED as unresolved (never resolved by guessing); NOT_APPLICABLE: a subcommand /
mode with no population for the subject; each case rc + text quoted, all planted on the SOURCE plane -- no AWS call is
needed by any case; 4.4 Rule T's form APPLIED via the ONE shared module `.tools/_compbudget.py` on the corpus-width
sweep (`gate [path ...]`) with the expiry line in the s.4.4 grammar, and the non-application half stated for `origin`
(one file, no corpus-width loop); 4.5 the passcraft moves; 4.6 usage at BOTH instruments and the battery at BOTH grains).
Then the ONE code change this cell owes: the ENRICHED unresolved print (the reason class on the line: DYNAMIC-PATH /
DEPLOY-TIME-ONLY / FIRM-TREE-ABSENT / OTHER, so a reader can tell WHY without opening the producer), the 4.3 tokens
machine-rejectable on every answer, the budget carrier wired with `--help` disclosing it, and a NEW battery file
`.tools/tests/test_comp_dataflow_battery.py` whose FIRST arm asserts the four honest-unresolved specimens still read
UNRESOLVED (the never-guess control).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="T7-AC1" cell_refs="CE-t-7"/> `T7-AC1` -- the deliverable parses (one fenced JSON block), every required s.4 field present or explicitly ABSENT, 4.1 identity read from the ENGINE path, the shim named as the shim.
<criterion id="T7-AC2" cell_refs="CE-t-7"/> `T7-AC2` -- (AC-2) four PLANTED cases keyed on the ratified enum produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case), all on the SOURCE plane (zero AWS calls).
<criterion id="T7-AC3" cell_refs="CE-t-7"/> `T7-AC3` -- HONEST-UNRESOLVED PRESERVED AND ENRICHED: the 4 of 4 known unresolved specimens (named by file at cut by the assignee from the tool's own current output, denominator stated) still read UNRESOLVED after the change, each now carrying its reason class on the line; the count is unchanged; a planted mutant that resolves one of them by reading deploy-time config goes RED.
<criterion id="T7-AC4" cell_refs="CE-t-7"/> `T7-AC4` -- (AC-4) Rule T's form applied: `--help` discloses the carrier via `_compbudget.py`; a planted small `--budget` on `gate` over a wide pathspec produces the s.4.4 expiry line with its source word and reached denominator, side by side with a clean completion line; `origin`'s non-application half stated in the class the form names.
<criterion id="T7-AC5" cell_refs="CE-t-7"/> `T7-AC5` -- battery: the NEW `.tools/tests/test_comp_dataflow_battery.py` with the never-guess control as its first arm, one arm per new behaviour, and a planted mutant per arm going RED; direct AND under pytest at the FILE grain; directory grain stated as it reads.
<criterion id="T7-AC6" cell_refs="CE-t-7"/> `T7-AC6` -- push state MEASURED at report (ls-remote + is-ancestor; LOCAL expected while Andrew gates the cadence, say which state was read); the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the seat commits itself.

<expected_criteria>T7-AC1, T7-AC2, T7-AC3, T7-AC4, T7-AC5, T7-AC6</expected_criteria>

## SURFACES

`.tools/comp-dataflow` (the shim) · `org/modules/graph/comp_dataflow.py` (476 lines; `:33` the counted-unresolved contract; `:280` `is_unresolved`; `:311` the unresolved firm tree; `:348-352` the summary; `:361` `cmd_origin`) @`b7daeaa6f0` · `.tools/_compbudget.py` @`2718cffc45` · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` @`19bf1c7322` · `org/mcp/comp-tool-runs.jsonl` + `org/mcp/comp-which-rail.log` · PRD s.4 + s.7 T-7 @`19bf1c7322` (and CVO~A's s.6 note the manifest cites for the enriched print) · precedents: `deliverables/0.8.0_AE_CloudComp~A/comp-read.result.md` @`e0f0e5a9e6`, `comp-which.result.md` @`d92fe43586`.

## BOUNDS

- **NEVER guess through deploy-time config:** no env var, Terraform value, served artifact or runtime lookup is consulted to resolve a read path; the SOURCE plane stays the plane; an unresolved read stays unresolved and COUNTED. The first battery arm is the control.
- **The item-9 semantics (served-origin flagging, the exemption list) do NOT change**; the enrichment is on the unresolved PRINT, not the classification.
- **No new dependency; no new file outside the engine, the shim, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` is consumed, not edited.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY), then keep working; never a message.
- **Certifier != author:** the s.7 row-state word is the L4 owner's version bump on the L8/L9 seat's documentation, read from the record.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @b7daeaa6f0 (v0.2.2), cell CE-t-7 (s.1a, = manifest T-7; STAGE 2 in s.2; ROUND 4 fence).
<owned_cells>CE-t-7</owned_cells>
Read-dependencies, NOT claimed: CE-disc-2 / CE-tp-1 (DONE as spec), CE-t-1 / CE-t-2 / CE-t-3 / CE-t-8 (the form's applications, terminal), CE-t-9 (in parallel at the base seat -- no dependency either way).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 20 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 3 -> 3, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or comp-dataflow (read at 2026-09-03 08:09Z).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-dataflow is a repo-local Python tool over parsed producer source on the working tree; no AWS principal, policy or resource is read or changed by it or by this TO, so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @03a3dc5aea (2026-09-03T08:16:42Z); 10/10 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged = this order's two OUTPUTS (the deliverable and the proof instance, GONE by construction at cut); uncited neighborhood 258 (25 shown, cap declared); --no-packet (stage 4 pointers only, the caller's choice, recorded in the declaration).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T7-AC1`..`T7-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json`
instance at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-7.comp-dataflow-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself.
T7-AC3's never-guess mutant and T7-AC5's planted mutants are the controls that must be able to FAIL; every `surprises`
entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_dataflow.py --for "where a read is classified resolved or unresolved, where the unresolved line is printed, and where the summary counts are computed"` and a real `comp-dataflow gate` sweep to NAME the current honest-unresolved specimens with their denominator. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the new battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-dataflow origin <script.py>` from a seat other than this lane (the base seat is the nearest; the L8 seat reads the record) -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` (the sequencer; the L8 seat reads the record, not a message) with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
