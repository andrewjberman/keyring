# TO LGIC_CANON.TO-CN-k-1 -- the canon at v1.0, with its generated naming section

<to_id>LGIC_CANON.TO-CN-k-1</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; brief half signed by 4.0.0_SA_CRO, ratified-text half by 3.0.0_SA_CVO, both current) | **Decomp cell:** `CN-k-1` (round 1) | **outcome_ref:** FWD-1, FWD-6 | **depends_on:** -- (level 0; spawned at issuance) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`CN-k-1` -- the canon at v1.0 (PRD DEC-1; cell candidate C1). `infra/logic/02_DOCTRINE.md` is v0.3 today, last touched @c9048873d1 (register entry X7 added and X2 granted by `1.0.0_SA_CTO` and `4.0.0_SA_CRO`). It is THE one document: a seat handed a pipeline tree judges it from here alone. **Edit it in place to v1.0, and write one new script:**

1. **Every rule carries three parts:** its authority, its census tag and its non-application (DEC-1 d). Print, on its own line in the canon, exactly `RULES CARRYING ALL THREE PARTS: <n> of <d>`. A rule is a line starting `**R<n>`, and its block runs to the next rule, `##`/`###` heading or `---` line; the checker recounts the same way.
2. **The naming axis becomes a GENERATED section** (DEC-1 b; `4.0.0_SA_CRO` R2). Write `infra/logic/render_naming_section.py`:
   - Between the two exact marker lines `<!-- BEGIN GENERATED NAMING SECTION -->` and `<!-- END GENERATED NAMING SECTION -->` it renders the schema's naming content: the key grammar, the per-slot firm forms, the resource grammar and its last slot (the kinds), and the refused tokens.
   - It reads `org/standards/NAMING_SCHEMA.json`, and the firm forms from the file that carries them at HEAD: `NAMING_SCHEMA.json` `firm_forms` while that field exists, else the FIRM rows of `infra/logic/registry/scopes.json`. NAMING_SCHEMA v1.9 moves them to the registry, in another project's round, and it may land while you work.
   - Inside the section it writes one stamp line per file it read, exactly `stamp: <repo-relative path> <version or -> sha256:<64 hex>`. The hash is SHA-256 of the file's bytes with CRLF normalised to LF, so every checkout of one commit hashes the same.
   - `--write` replaces the section in place. `--check` exits 0 only when every stamped hash equals the live file's AND the section's bytes equal a fresh render, and exits non-zero otherwise. `--canon PATH` and `--schema PATH` override the default paths (the checker runs `--check --canon` on a scratch copy).
   - It reads the schema and the registry and never writes either.
3. **No naming enumeration appears outside the generated section.** R1's hand-kept grammar strings and firm-form lists go, and R1 cites the section. The checker's census: outside the section, no line carries `{system}-{scope}-{function}` or `{source}/{scope}/{tier}`, and no run of adjacent back-ticked tokens holds two or more firm forms, two or more refused tokens, two or more tiers, two or more cadences, or three or more kinds.
4. **Every item of section 6, "WHAT THIS DOCUMENT DOES NOT RULE", is closed or names its decider** (DEC-1 a). A closed item carries `RULED` or `CLOSED`, or is struck (`- ~~`); an open one carries `decider: <full serial, or Andrew>`.
5. **D10 s.2 and s.6 are absorbed in place of the pointer** (DEC-1 c). Read `docs/architecture/D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md` s.2 (the five axes) and s.6 (the exception register), and carry into the canon anything they say that it does not. Every line that still cites D10's s.2 or s.6 says `absorbed`: the citation becomes provenance, not a place the reader must go.
6. **R1's non-application names only the LEGACY root `code/` homes** (row LGIC_CANON-S1). LGIC_NAMING v1.3 puts every NEW code home in the grammar's code tier, `{source}/{scope}/code/{built_tier}/{file}`, so only the legacy root homes stay outside R1.
7. **Section 4 keeps the register SCHEMA and points at `06_CONFORMANCE_LEDGER.md` section 6 for its ENTRIES** (decomposition section 8, choice 2). Today both files carry the entries: two carriers of one list. Keep the `PERMANENT | CONDITIONAL` schema line.
8. **The header and the change log read v1.0.**

No rule's substance changes except where items 3, 5 and 6 say so. A defect you find in the schema or the registry is a surprise row against LGIC_NAMING or LGIC_ENFORCE, never an edit to them.

**Co-writers.** `1.0.0_SA_CTO` and `4.0.0_SA_CRO` write register entries in this file and the ledger. If one lands while you work, the drain merges it; do not revert it.

**Read:** `infra/logic/02_DOCTRINE.md`; `org/standards/NAMING_SCHEMA.json`; `infra/logic/registry/scopes.json`; `docs/architecture/D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md` s.2 and s.6; `infra/logic/06_CONFORMANCE_LEDGER.md` section 6; the PRD's DEC-1 (`org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md`); row LGIC_CANON-S1 in `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="K1-AC1" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-census</invocation><expect>VERDICT: PASS-K1-CENSUS-OK</expect></criterion>
`K1-AC1` -- the canon's printed `RULES CARRYING ALL THREE PARTS` line equals the checker's recount, and every rule carries all three parts.

<criterion id="K1-AC2" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-render</invocation><expect>VERDICT: PASS-K1-RENDER-FRESH</expect></criterion>
`K1-AC2` -- `render_naming_section.py --check` exits 0: the section's bytes equal a fresh render of the stamped files.

<criterion id="K1-AC3" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-stale</invocation><expect>VERDICT: PASS-K1-STALE-REFUSED</expect></criterion>
`K1-AC3` -- on a scratch copy with a doctored stamp, `--check` exits non-zero, while the clean copy exits 0 (N4).

<criterion id="K1-AC4" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-noenum</invocation><expect>VERDICT: PASS-K1-NO-ENUM-OUTSIDE</expect></criterion>
`K1-AC4` -- a census of the schema's enumerations outside the generated section returns 0, denominator printed.

<criterion id="K1-AC5" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-s6</invocation><expect>VERDICT: PASS-K1-S6-CLOSED</expect></criterion>
`K1-AC5` -- every item of section 6 is closed or names its decider.

<criterion id="K1-AC6" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-d10</invocation><expect>VERDICT: PASS-K1-D10-ABSORBED</expect></criterion>
`K1-AC6` -- D10 s.2 and s.6 are absorbed: the five axes and the register schema are in the canon, and every D10 s.2/s.6 citation says `absorbed`.

<criterion id="K1-AC7" cell_refs="CN-k-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py k1-r1code</invocation><expect>VERDICT: PASS-K1-R1-LEGACY-CODE</expect></criterion>
`K1-AC7` -- R1's non-application names only the LEGACY root `code/` homes (S1).

<criterion id="K1-J1" cell_refs="CN-k-1" judgment="true"/>
`K1-J1` -- graded at L9 by 3.0.0_SA_CVO: a seat can apply each rule from this document alone. RECORD; NO VERDICT.

<expected_criteria>K1-AC1, K1-AC2, K1-AC3, K1-AC4, K1-AC5, K1-AC6, K1-AC7, K1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves (PRD DEC-9).** No cell of this project moves data, repoints a trigger, edits a bucket policy, writes to AWS, runs Terraform, or calls anything off Opal infrastructure.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` holds this round's (`check_canon_r1.py`, the checker every criterion calls, and the fixtures its criteria name). Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Pins.** Pin every artifact your proof cites by the commit that carries it, never `PENDING-THIS-COMMIT`: a later commit touching the instance leaves such a pin stale (rows LGIC_NAMING-S18, W1-S7 and W2-S6 carry the class).
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/logic/02_DOCTRINE.md
infra/logic/render_naming_section.py
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v3, cell `CN-k-1`, round 1 (sections 3 and 0c).
<owned_cells>CN-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `K1-AC1`, `K1-AC2`, `K1-AC3`, `K1-AC4`, `K1-AC5`, `K1-AC6`, `K1-AC7`, `K1-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-k-1.canon.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> K1-AC1,K1-AC2,K1-AC3,K1-AC4,K1-AC5,K1-AC6,K1-AC7,K1-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `canon.r1.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the cut -- --budget 540, 5 of 5 carriers scanned within budget (27.3 s used), 25 gates armed, 0 lines naming LGIC_CANON. This project registers G-C (worker admission, checked after this issuance), G-R (CLEARED: the registry is at HEAD, LGIC_ENFORCE cell r-1 @a925c8a642), G-N (Andrew's: C6 is not cut until a genuinely new firm exists) and G-V19R (the generated naming section re-rendered in whichever merge lands second, CN-k-1's drain or GROUP V19's).
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 1's write set: three documents and one render script under infra/logic/, and records under this project's deliverables/; no cell adds an operation, a policy, a principal or a resource, so the lens would receive an empty input.
comp-adversary: RUN at the cut on the PRD at v1.3 (@5b2336a5e4), read-vintage HEAD @2373f96073 -- 12 of 12 cited commits verified; 18 cited paths, 12 stable, 6 flagged (2 GONE, this project's to mint: 10_ONBOARDING_CHECKLIST.md and render_naming_section.py; 4 MOVED: 02_DOCTRINE.md and 06_CONFORMANCE_LEDGER.md @c9048873d1, SEQUENCE.yaml, NAMING_SCHEMA.json v1.8). Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). infra/logic/ sits in lane PLATFORM_LOGIC_DOCS and a path directly under deliverables/ in TREE_DELIVERABLES; each is admitted to this worker only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 1. Round 1 of LGIC_CANON, its first issuance, cut from decomposition v3 by `2.0.0_SA_COO~G`, seated on this project by `1.0.0_SA_CTO` @52ea4c8cac on Andrew-direct ~16:1xZ ("parallelize harder"). The fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/`.
