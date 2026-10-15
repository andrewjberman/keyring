# TO DSGN_RBNDV2.TO-RV-r-3 -- FWD-2/FWD-1: the sidebar reads the --rb tokens in their own format (DIRECT-ACT, CVO grade C-S1)

<to_id>DSGN_RBNDV2.TO-RV-r-3</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~7</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-r-3` (decomp v1 addendum 3) | **outcome_ref:** FWD-2, FWD-1 | **depends_on:** -- (direct act) | **slot:** ~7, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-r-3` -- the sidebar's violet accent never renders. `portal/src/index.css` defines the `--rb-*` tokens as HEX values (`--rb-accent: #5F3BE3`, `--rb-ink: #0A1733`, `--rb-ink-2`, `--rb-ink-3`, `--rb-rule`). `portal/src/ui/components/sidebar/AppSidebar.tsx` and `SidebarLink.tsx` wrap them as `hsl(var(--rb-X))`, which is invalid at computed-value time for a hex value, so the section-eyebrow underline falls back to currentColor (navy) and the current page's underline (`2px solid hsl(var(--rb-accent))`) is dropped. The panel primitives use the tokens correctly, as `var(--rb-X)`.

In those two files replace every `hsl(var(--rb-X))` with `var(--rb-X)` and change nothing else (about 13 sites; `AppSidebar.tsx` lines near 54, 55, 111, 120, 147, 156, 159 and `SidebarLink.tsx` lines near 8, 32, 35, 51, 52, 63). Tokens that are genuinely HSL triples (`--bg-page`, `--hairline`, `--bg-surface`, `--semantic-*`) keep their `hsl(var(...))` wrapper. Where the existing sidebar tests (`src/ui/components/sidebar/__tests__/dsgn-rbndv2/`) assert the `hsl(var(--rb-...))` text, update only those assertions to the `var(--rb-...)` form, keeping every other arm.

**Out of this cell:** every file outside `portal/src/ui/components/sidebar/`.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow; radii 2/3/4px only (`portal/DESIGN.md` C11); no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast.

**Environment:** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light`; the base commit for a difference control is `adc70061`. Do not start any server.

### ACCEPTANCE

<criterion id="RB1R3-AC1" cell_refs="RV-r-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-r3.token-format.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SIDEBAR-TOKEN-FORMAT-OK</expect></criterion>
`RB1R3-AC1` -- reading `src/ui/components/sidebar/AppSidebar.tsx` and `SidebarLink.tsx` as text: neither contains the substring `hsl(var(--rb-`; `SidebarLink.tsx` contains `2px solid var(--rb-accent)` and `AppSidebar.tsx` contains `border-[var(--rb-accent)]`; every `--rb-` name used in the two files is one of the five names defined in `src/index.css` `:root` (the test reads the defined names from the CSS text); (difference control: the same text checks run on `git show adc70061:src/ui/components/sidebar/AppSidebar.tsx` and `SidebarLink.tsx`, run from the portal root, must report the `hsl(var(--rb-` substring present, proving the test can fail). The test prints `VERDICT: SIDEBAR-TOKEN-FORMAT-OK` only when every arm holds.

<criterion id="RB1R3-AC2" cell_refs="RV-r-3" judgment="true"/>
`RB1R3-AC2` -- graded by `2.0.0_SA_COO~RB`'s re-walk of `/market` (the eyebrow underline renders violet `rgb(95, 59, 227)` and the current page shows its underline), and then by Andrew's eye (DEC-5); never self-graded. RECORD; no verdict.

<expected_criteria>RB1R3-AC1, RB1R3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/ui/components/sidebar/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 addendum 3, cell `RV-r-3`.
<owned_cells>RV-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1R3-AC1, RB1R3-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~7/DSGN_RBNDV2.TO-RV-r-3.sidebar-token-format.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1R3-AC1,RB1R3-AC2` BEFORE the flip, run from inside your worktree. `RB1R3-AC2` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~RB`'s re-walk and Andrew's read (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W7-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at addendum 3 -- `src/ui/components/sidebar/` is written by no other open cell.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~7, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 7 --portal-ref feature/dsgn-rbndv2-light`.
