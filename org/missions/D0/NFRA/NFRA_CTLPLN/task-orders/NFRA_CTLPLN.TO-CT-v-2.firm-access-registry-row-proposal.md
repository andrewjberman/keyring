# TO NFRA_CTLPLN.TO-CT-v-2 -- round 7 CT-v-2: a PROPOSAL for where the firm-access sets live in the opal_naming registry, so the data proxy's two open routes can gain their firm check with no hand-typed firm token

<to_id>NFRA_CTLPLN.TO-CT-v-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~64</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-v-2` (`decompositions/NFRA_CTLPLN_DECOMP.round7.md`) | **outcome_ref:** FWD-28 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-28 (PRD v0.25): the data proxy `opal-portal-data-proxy` has 41 routes. 39 answer 403 unless the caller's tier is `internal` (live). Two routes (`POST /sentiment/keyword-intelligence`, `GET /aum/metrics`) are called by pages the partner firms may open, so they stay open to every verified login until they can check the caller's `firmId` against the firm set the portal admits for the calling page, WITHOUT a hand-typed firm name in code. A first design (a generator reading `portal/src/lib/firmAccess.ts` and writing a Python module with the firm ids) was refused at commit by the naming gate: firm tokens may appear only in registry files, in a generated block or file produced by `lib/opal_naming.py generate`, or inside `key()/address()/name()/lookup()` arguments (`.tools/naming-gate.py:1-40`). The rule (CLAUDE.md section 4, rule 30): a builder refusal is a missing registry row to add, never a workaround. The CTO has ruled: do it as a registry row, not an R20 departure.
You write ONE proposal document. You change nothing else. A later order applies it.

### WHAT THE PROPOSAL MUST CONTAIN

File: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~64/PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md`. Read first: `lib/opal_naming.py` (the `VIEWS` table at about line 97, `WHOLE_FILE_TARGETS` at about line 123, the renderer table and its per-target registry-file map at about line 132, `generate()`), `.tools/naming-gate.py` (its header and the generated-target list near line 747), `infra/logic/registry/` (list the files and read the one that holds firms and the one that holds `systems`), `infra/logic/02_DOCTRINE.md` R1-R21, `portal/src/lib/firmAccess.ts` (`FIRM_ALLOWED_PATHS`, `FIRM_EXEMPT_PATHS`, `INTERNAL_FIRM_ID`), the existing generated carrier `portal/src/pages/InvestorReporting/header/firmDisplayNames.generated.ts` and its registry source as the closest worked example, and the data proxy's route census `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md`.
Answer, each with the file and line it rests on:
1. **Where the truth lives.** Today the firm->pages matrix is hand-kept in `firmAccess.ts` (the portal's source). Which of these is the right single source: (a) a new registry file the portal's `firmAccess.ts` and the Lambda are BOTH generated from; (b) `firmAccess.ts` stays the source and a generated carrier reads it; (c) the existing firm registry gains a `pages` column. Give the tradeoff in one paragraph each and RECOMMEND one. Name the ONE-WRITER consequence for the portal (it is a separate repository checkout; say what it means for a generated `firmAccess` file there).
2. **The exact registry rows** (file, key, value shape) for the chosen option, with the firm names that exist today read from the matrix (print the denominator: how many firms, how many page paths).
3. **The generated target**: the new `VIEWS` entry (path, syntax, definitions), whether it joins `WHOLE_FILE_TARGETS`, the renderer-table entry (which registry files it reads), and the name of the generated module the Lambda imports, which must sit in `infra/aws/lambda/portal_data_proxy/` and be added to that function's `files` list in `infra/aws/lambda/ci/lambda-source-map.json` (the apply cell does that edit).
4. **The handler diff**, as a patch in the document (not applied): the two class-(i) routes gain `firmId in <generated set for that route>` OR `tier == internal`; every other route unchanged; an unknown firm refused.
5. **The tests** that must exist, including the drift check (the generated file equals a fresh render) and a test that fails if a firm token appears outside the generated file.
6. **Whether this needs an R20 register entry or a gate edit**: answer NO or YES with the rule number, citing `infra/logic/02_DOCTRINE.md`.
7. **The order of acts and who does each** (registry edit, regenerate, handler, test, apply under a signed pair with a NEVER-2 ledger), and the pre-apply read that proves the open routes' callers still pass.
8. **Open questions for the CTO**, at most five, each one line.
LAST line of the document: `PROPOSAL-FIRM-ACCESS rows=<n> targets=<n> questions=<n>`.

### RULES FOR THIS CELL

You write the one document and the surprise rows the rules allow. You edit no source file, no registry file, no Lambda, no test, no `.tf`, and you change nothing under `portal/`. You run no `terraform` and make no AWS call. `lib/opal_naming.py` may be run READ-ONLY (its `--help`, `check` or `show` verbs; never `generate` into the repo). No firm name is typed into any file you write EXCEPT inside the proposal document, where the firm names appear only as quoted rows of the matrix (the document is not a code file). No non-ASCII. The law files CLAUDE.md and org/XXX.md are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W64-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTv2-AC1" cell_refs="CT-v-2"><invocation>grep -c "PROPOSAL-FIRM-ACCESS rows=" org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~64/PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md</invocation><expect>1</expect></criterion>
`CTv2-AC1` -- the proposal exists and ends with its counts line.

<criterion id="CTv2-AC2" cell_refs="CT-v-2" judgment="true"/>
`CTv2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO: the recommendation in section 1 is the right single source, and the handler patch in section 4 would pass the naming gate.
</proof_of_spec>

<expected_criteria>CTv2-AC1,CTv2-AC2</expected_criteria>

Run CTv2-AC1 from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~64/NFRA_CTLPLN.TO-CT-v-2.firm-access-registry-row-proposal.proof_of_spec.json` (CTv2-AC2 is a judgment row with NO verdict), validate it with `python .tools/proof-of-spec-check.py <instance> CTv2-AC1,CTv2-AC2`, and flip `<status>` to `complete` only when the mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round7.md</decomp_doc>
<owned_cells>CT-v-2</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a proposal that types firm tokens into a code carrier (forbidden; the document is the only file and holds quoted rows); a recommendation that makes the portal checkout a second writer (question 1 names the one-writer consequence); a patch that passes tests but trips the naming gate (question 6 and the CVO's judgment); BLIND: the portal repository's own commit rules, which the CTO rules.
lane: the <paths> block IS the grant; `deliverables/0.9.0_WK_NFRA_CTLPLN~64/` needs no entry.
</preflight>

Source: `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round6.md` section 4 (E10), CTO msg 108445, row NFRA_CTLPLN-W62-S6.
