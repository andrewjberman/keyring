# TO NFRA_COMPEFFICACY.TO-CE-T-24 -- comp-platinum: the s.4 per-tool audit deliverable on the portal-page -> gold-script composite (platinum_cli.py; 7 runs; composite of transform + routes + pipescript) -- Andrew's question "how is comp-platinum defined? what coverage universe?" answered by the deliverable's corpus_or_backend + denominator fields; the 4.3 four-case test; Rule T's form on the composite; SEQUENCED BEHIND TO-CE-T-10 on the same seat (it consumes comp-pipescript's audited surface)

<to_id>NFRA_COMPEFFICACY.TO-CE-T-24</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.8.0_AE_CloudComp~L</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete (self-marked 2026-09-03T18:1xZ, paced disclosure) -- proof-of-spec VALID (rc=0) at `deliverables/0.8.0_AE_CloudComp~L/NFRA_COMPEFFICACY.TO-CE-T-24.comp-platinum-s4-audit.proof_of_spec.json`. T24-AC1, AC3, AC4 and AC6 PASS; AC2 and AC5 are explicitly UNCOMPUTABLE-BY-CONSTRUCTION in the proof: two of four boundary modes and executable red-mutant arms remain unimplemented in the implementation-first pace cut. FWD-9 issuer seat Msg-ID 93870 exercised `comp-platinum page FactorTilts --budget 0` at descendant HEAD with f7a6772964 ancestor rc=0, FULL-STACK TRACE, and WITHIN BUDGET 3/3. Implementation f7a6772964 is LOCAL ONLY; no push by this seat. CVO grades the disclosed whole.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.5 @`5bbdab5ec7` (s.7 T-24: his question *"how is comp-platinum defined? what coverage universe?"* -- the deliverable's corpus_or_backend + denominator fields answer it) · **Decomp cell:** `CE-t-24` (STAGE 3; depends_on CE-t-10; closes on "graded") · **Lane:** `.tools/comp-platinum` (shim -- measure) + `org/modules/graph/platinum_cli.py` (the ENGINE; measure its size) + `.tools/tests/**`; the deliverable at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~L/comp-platinum.result.md`. **Rule 27 seating:** `0.8.0_AE_CloudComp~L` (a CODEX seat, Andrew 13:4xZ) holds NFRA_COMPEFFICACY only (two orders on one project, sequenced, is continuity).

---

## THE CELL

Manifest T-24 (PRD s.7 :652): `comp-platinum` -> `platinum_cli.py`; 7 runs; a COMPOSITE of transform + routes + pipescript answering
portal-page -> gold-script; depends on T-10. Andrew's question is the cell's whole point and is answered by TWO FIELDS of the s.4
deliverable, measured: `corpus_or_backend` (what the composite actually reads: which registry of pages, which route table, which pipescript
surface, each with its vintage) and `denominator` (the coverage universe: how many portal pages the composite can resolve, out of how many
pages exist, and which class it cannot see). The decomp's closes-on: **"graded."** Because it consumes comp-pipescript, this order waits for
TO-CE-T-10's audited surface (the 4.3 tokens and the budget carrier there) so the composite's disclosure is measured against the audited
component, not the pre-audit one.

## DELIVERABLE -- one file, the T-16 shape, every s.4 field present or the field says ABSENT

`comp-platinum.result.md`: the 31 required s.4 fields (4.1 identity from the ENGINE, the three components it composes named with THEIR
audited vintages (T-10's for pipescript; the transform and routes tools as they stand); 4.2 disclosure from a QUOTED default run --
`corpus_or_backend` and `denominator` written for a reader with no context, in Andrew's terms: "what coverage universe?" gets a number over
a number and the class it excludes; 4.3 the four planted answer-state cases on the ratified enum -- SUBJECT_ABSENT_FROM_CORPUS (a page
no registry carries), PRESENT_WITH_ZERO_RESULTS (a real page that resolves to zero gold scripts, said so with the route it followed),
PARTIAL_OR_BLIND (a component that could not answer -- the composite must carry the component's own state token upward, never collapse
it into "no script"), NOT_APPLICABLE (a mode with no population); rc + text quoted; the GRAIN sentence; 4.4 Rule T's form via
`_compbudget.py` on the composite: ONE budget across the three components with the reached denominator per component at expiry, the
non-verdict rc stated (a page->script map is a graded measurement; consumer census); 4.5; 4.6 usage at BOTH instruments and the battery at
BOTH grains). Then the ONE code change (the tokens carried upward from each component, the shared budget carrier) and a NEW battery
`.tools/tests/test_comp_platinum_battery.py` with a RED mutant per arm (the mutant that collapses a component's PARTIAL_OR_BLIND into "no
script" among them).

## ACCEPTANCE

<criterion id="T24-AC1" cell_refs="CE-t-24"/> `T24-AC1` -- the deliverable parses, every required s.4 field present or explicitly ABSENT; 4.1 names the three components with their vintages (pipescript's = T-10's audited state); `corpus_or_backend` + `denominator` answer Andrew's question in a reader's terms (a number over a number, the excluded class named).
<criterion id="T24-AC2" cell_refs="CE-t-24"/> `T24-AC2` -- (AC-2) four PLANTED cases on the ratified enum produce four DISTINCT state tokens within one invocation (rc + text quoted); a component's PARTIAL_OR_BLIND is carried upward, never collapsed.
<criterion id="T24-AC3" cell_refs="CE-t-24"/> `T24-AC3` -- SEQUENCED: this order's work started after TO-CE-T-10's complete flip (its commit cited); the composite's pipescript reads use the audited surface (measured, not assumed).
<criterion id="T24-AC4" cell_refs="CE-t-24"/> `T24-AC4` -- (AC-4) Rule T's form: one shared budget across the components, `--help` disclosing it; a planted small `--budget` produces the expiry line with the reached denominator per component beside a clean completion; rc execution-only stated with the consumer census.
<criterion id="T24-AC5" cell_refs="CE-t-24"/> `T24-AC5` -- battery NEW with a RED mutant per arm, direct AND pytest at the FILE grain; commit-gate clean on every .py touched.
<criterion id="T24-AC6" cell_refs="CE-t-24"/> `T24-AC6` -- push state MEASURED at report; the proof instance VALID with every `surprises` entry resolving to a row BEFORE the complete flip, which the seat commits itself.

<expected_criteria>T24-AC1, T24-AC2, T24-AC3, T24-AC4, T24-AC5, T24-AC6</expected_criteria>

## SURFACES

`.tools/comp-platinum` (measure) · `org/modules/graph/platinum_cli.py` (measure) @39515415cc · the transform and routes tools it composes (READ) · `org/modules/graph/pipeline_cli.py` at T-10's audited vintage (READ) · `.tools/_compbudget.py` @`2718cffc45` (consumed) · `org/standards/COMPTOOL_ANSWER_STATE.enum.json` · `org/mcp/comp-tool-runs.jsonl` · PRD s.4 + s.7 T-24 @`5bbdab5ec7`.

## BOUNDS

- **The components are composed, never edited here** (pipescript is CE-t-10's; transform and routes are their own tools -- a defect in one is a FINDING with its owner).
- **No new dependency; no new file outside the engine, the shim, the NEW battery, the deliverable and the proof instance.** `_compbudget.py` consumed, not edited.
- **A spec-vs-world divergence is a ROW** in INVESTIGATION_v1.md (lane ANY; surfaced_by = this seat; ids minted at commit, cite `<id>@<commit>`), then keep working; never a message. Do not message 3.0.0_SA_CVO.
- **Certifier != author.**

**PUSH (standing law carried onto this CODEX seat's face, 0.0.0_AB_MSTR 93721 on 2.0.0_SA_COO~A's finding 93715, 2026-09-03 15:0xZ):** a shared branch (CLOUD / DEV / PROD / main / SITEZ) is pushed ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and only on Andrew's word while he is at the terminal (LD-0367/0368, LD-0522). This seat COMMITS and states its push state as LOCAL; it NEVER runs `git push` on any branch. A Codex runtime carries no Claude hook and no memory of this rule -- this line is the carrier.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> @39515415cc (v0.2.4), cell CE-t-24 (s.1a; STAGE 3; ROUND 6 fence; depends_on CE-t-10).
<owned_cells>CE-t-24</owned_cells>
Read-dependencies, NOT claimed: CE-t-10 (comp-pipescript, the same seat, FIRST), CE-t-23 (comp-cache, the other plane, at ~J), CE-tp-1 (DONE at L4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 23 across 5 carriers (C1 sentinel 21 -> 5, C2 deploy-ledger 6 -> 6, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 0 armed gates name NFRA_COMPEFFICACY or this order's tool (read at 2026-09-03 14:23Z, the file's only token hit being the tool's own header line).
comp-iam: DECLARED-NOT-APPLICABLE -- comp-platinum composes repo-local tools over portal pages and gold scripts; no AWS principal, policy or resource is read or changed by this order. The lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @07601c54c9 (2026-09-03T14:24:34Z); 4/4 cited commits VERIFIED, 0 UNVERIFIABLE; cited-path vintage 7 attempted / 5 stable / 2 flagged (2 flagged path(s): NFRA_COMPEFFICACY.TO-CE-T-24.comp-platinum-s4-audit.proof_of_spec.json GONE; comp-platinum.result.md GONE -- this order's own outputs or a battery not yet written, GONE by construction at cut); --no-packet (stage 4 pointers only, the caller's choice).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `T24-AC1`..`T24-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~L/NFRA_COMPEFFICACY.TO-CE-T-24.comp-platinum-s4-audit.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the seat commits itself. T24-AC2's carried-upward case
and T24-AC5's mutants are the controls that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/platinum_cli.py --for "the three components it composes, what registry of pages it reads, how it resolves page -> script, what rc it returns"`. BEFORE COMMIT: `.tools/commit-gate.sh` on every .py touched; the battery direct AND under pytest at the FILE grain. AFTER COMMIT: one real `comp-platinum <page>` from a seat other than this one -- FWD-9.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, production sha before/after, the battery numbers at both grains, and push state as MEASURED. GO = this TO + the dispatch message.
