# TO DSGN_RBNDV2.TO-RV-r-2 -- FWD-4/FWD-3/FWD-1: the old dark inner grounds read white and silver inside a light panel (DIRECT-ACT, surprise row S3)

<to_id>DSGN_RBNDV2.TO-RV-r-2</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~6</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-r-2` (decomp v1 addendum 2) | **outcome_ref:** FWD-4, FWD-3, FWD-1 | **depends_on:** -- (direct act) | **slot:** ~6, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-r-2` -- on `/market` with live data, inside the white panels, the heat tables and tiles still paint dark navy grounds, while the panel's legibility rule turns their white text navy, so names read navy on navy. The grounds are spelled with the old dark surface tokens, which in `portal/src/index.css` alias the dark field `--bg-band`: `--bg-header`, `--bg-medium`, `--bg-card`, `--bg-dark`, `--bg-medium-alt`, and `--semantic-background-contentPanel` and `--semantic-background-hover` (see `portal/src/components/PerformanceHeatMap.tsx`, `BenchmarkHeatmap.tsx` and `market-performance/ExecutiveSummary.tsx`, read only). A panel root carries `data-panel-surface="light"`.

Add ONE unlayered rule block to `portal/src/index.css` (outside every `@layer`, near the other `[data-panel-surface="light"]` blocks): selector exactly `:root [data-panel-surface="light"]` (that exact text, so it is distinct from the existing rule whose selector is exactly `[data-panel-surface="light"]`, which you must not touch), declaring ONLY these seven custom properties, each as an `H S% L%` triple in the format the theme uses (`220 18% 71%`; integer or two-decimal percentages fine if each resolves within 1/255 per channel):

- `--semantic-background-contentPanel`, `--bg-medium`, `--bg-card`, `--bg-dark`, `--bg-medium-alt`: white `#FFFFFF`
- `--bg-header`: the silver tint `#EEF1F6`
- `--semantic-background-hover`: `#E6EBF4`

A custom property set on the panel root is inherited by everything inside it, so every dark inner ground becomes white or silver. Do not edit any component, page, the theme file, or the other blocks of `index.css`.

**Out of this cell:** every file except `portal/src/index.css` and your test.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. Colours stay token-defined; no shadow; radii 2/3/4px only (`portal/DESIGN.md` C11); no non-ASCII in code.

**Environment:** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light`. The base commit for your difference control is `ad7c100b5c` (it holds no such rule). Typecheck rule for a test: use only imports that `tsc -b` accepts here: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`; strip a root prefix with string slicing), and type any `process.env` read through a cast. The criterion's test file does not exist at the base: you write it from the criterion's text, and it prints its VERDICT line only when every arm holds. Do not start any server.

### ACCEPTANCE

<criterion id="RB1R2-AC1" cell_refs="RV-r-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~6; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-1-r2.surfaces.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: INNER-SURFACES-OK</expect></criterion>
`RB1R2-AC1` -- reading `src/index.css` as text with brace depth and `@layer` nesting tracked: a rule whose selector is exactly `:root [data-panel-surface="light"]` exists OUTSIDE every `@layer`; it declares exactly the seven custom properties above, each an HSL triple resolving to its stated hex (each channel within 1/255), and declares nothing else; the existing rule whose selector is exactly `[data-panel-surface="light"]` still declares only `--palette-white` and `--palette-mediumGray` (a control that this cell touched nothing else); (difference control: the same text checks run against `git show ad7c100b5c:src/index.css` run from the portal root report the new rule absent, proving the test can fail). The test prints `VERDICT: INNER-SURFACES-OK` only when every arm holds.

<criterion id="RB1R2-AC2" cell_refs="RV-r-2" judgment="true"/>
`RB1R2-AC2` -- graded at the round-1 close run by `2.0.0_SA_COO~RB` on the live `/market` walk, and then by Andrew's eye (DEC-5), never self-graded and never by the CVO: the heat tables and tiles read white and silver with legible names and figures, not navy. RECORD; no verdict.

<expected_criteria>RB1R2-AC1, RB1R2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/index.css
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 addendum 2, cell `RV-r-2`.
<owned_cells>RV-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1R2-AC1, RB1R2-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~6/DSGN_RBNDV2.TO-RV-r-2.inner-surface-token-remap.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1R2-AC1,RB1R2-AC2` BEFORE the flip, run from inside your worktree. `RB1R2-AC2` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~RB`'s close run and Andrew's read (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W6-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at addendum 2 -- `src/index.css` is written by no other open cell (cells t, r-1 merged; no cell is open).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~6, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 6 --portal-ref feature/dsgn-rbndv2-light`.
