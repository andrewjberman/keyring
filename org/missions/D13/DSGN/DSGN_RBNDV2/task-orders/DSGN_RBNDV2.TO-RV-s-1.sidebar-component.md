# TO DSGN_RBNDV2.TO-RV-s-1 -- FWD-2: the sidebar as its own component in the A-light grammar

<to_id>DSGN_RBNDV2.TO-RV-s-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~2</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>1</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-s-1` (decomp v1 @b475e9badc) | **outcome_ref:** FWD-2 | **depends_on:** -- (chain 2) | **slot:** ~2, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-s-1` -- THE SIDEBAR AS ITS OWN COMPONENT in the "A light" grammar (FWD-2, C-SIDEBAR).

Today the sidebar is inline in `portal/src/App.tsx`: `NAV_SECTIONS` (about :93-151), `SidebarLink` (about :165-232) and the `<aside>` (about :296-435); collapsed it is a 48px icon rail (`w-12`), expanded 224px. Move all three into `portal/src/ui/components/sidebar/AppSidebar.tsx` (and sibling files in that folder if you want them), with the SAME nav data (same labels, hrefs, order, sections, role gating, collapse behaviour, hooks and props the inline code uses) so behaviour is unchanged; `App.tsx` imports and mounts `AppSidebar` and keeps no `NAV_SECTIONS`, `SidebarLink` or `<aside>`. This is the only edit to `App.tsx`.

Restyle the EXPANDED sidebar to the fixture's sidebar section: ground `hsl(var(--bg-page))` (never a literal hex: the sibling token cell repoints that token to `#EAEAF7`), right border 1px `hsl(var(--hairline))`, width 232px (min 200), navy ink (`--rb-ink`, `--rb-ink-2`, `--rb-ink-3`), Lato; the wordmark; each section's label is the small-caps eyebrow (11px, 700, letter-spacing 0.14em, uppercase) with a 2px `--rb-accent` underline; section dividers 1px `--rb-rule`; links are text-led with no icon in the expanded state; the CURRENT page is the bold ink link with a 2px `--rb-accent` underline under its label and `aria-current="page"` (no filled tile); the foot is a 30px SQUARE with a 1px `--rb-ink-2` border holding the user's initial, with the user's name over their role in 12px (the round violet avatar is retired). The COLLAPSED 48px icon rail keeps the current icons and its behaviour, on the same ground and border. Radii 0 to 2px.

**Out of this cell:** the token values (sibling cell), the panel files, every page, and `portal/src/ui/components/catalyst/sidebar*.tsx` (unused, leave them).

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's (DEC-1 to DEC-5 of the PRD): you reproduce the fixture and invent nothing. Colours are read from tokens (`--bg-page`, `--hairline`, `--bg-surface`, the `--rb-*` family), never typed as a literal in a component, except where this cell says a literal is the point. Charts keep their colour (C6).

**Environment (every cell):** the portal worktree is `<WS>/portal`, based on the feature branch `feature/dsgn-rbndv2-light` at `ad7c100b5c` (= origin DEV when it was cut). The fixture you build to is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md` (read it first; it carries every value you need, so do not open the board URL). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints its VERDICT line only when every arm holds. Do not start any server: dev builds run on port 5174 only and 5174 serves the main checkout, not your worktree. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11); Lato; no non-ASCII in code.

### ACCEPTANCE

<criterion id="RB1S-AC1" cell_refs="RV-s-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~2; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-s.sidebar.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: SIDEBAR-OK</expect></criterion>
`RB1S-AC1` -- rendering `AppSidebar` expanded to static markup for a signed-in user on the Market Overview route: (1) every link label and href of the BASE `NAV_SECTIONS` appears in the same order inside the same section groups (the test carries the base list as a literal copied from `git show ad7c100b5c:src/App.tsx` in `<WS>/portal`, which is the behaviour-unchanged control); (2) exactly one link has `aria-current="page"` and it carries a 2px underline built from `--rb-accent`; (3) the markup contains no `rounded-full`, no filled active tile (`bg-[hsl(var(--semantic-action-primary))]`) and no literal `#EAEAF7`; (4) the root reads `--bg-page` for its ground. The test prints `VERDICT: SIDEBAR-OK` only when every arm holds.

<criterion id="RB1S-AC2" cell_refs="RV-s-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~2; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-s.app-seam.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: APP-SEAM-OK</expect></criterion>
`RB1S-AC2` -- reading `src/App.tsx` as text: it imports `AppSidebar` and renders it, and it contains none of `NAV_SECTIONS`, `function SidebarLink`, `const SidebarLink` or an `<aside` element (difference control: the same text checks run against `git show ad7c100b5c:src/App.tsx` report all four present, proving the test can fail). The test prints `VERDICT: APP-SEAM-OK` only when every arm holds.

<criterion id="RB1S-AC3" cell_refs="RV-s-1" judgment="true"/>
`RB1S-AC3` -- graded at the round-1 drain by Andrew's eye on `/market` (DEC-5), never self-graded and never by the CVO: the expanded sidebar reads as the "A light" board's sidebar (lavender ground, navy ink, eyebrow labels with the violet underline, underlined current page). RECORD; no verdict.


<expected_criteria>RB1S-AC1, RB1S-AC2, RB1S-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can. The seven `--rb-*` tokens and `--bg-page`'s new value are written by a sibling cell and land at the merge; build against the names.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/App.tsx
portal/src/ui/components/sidebar/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP.md</decomp_doc> v1 @b475e9badc, cell `RV-s-1`.
<owned_cells>RV-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB1S-AC1, RB1S-AC2, RB1S-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~2/DSGN_RBNDV2.TO-RV-s-1.sidebar-component.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB1S-AC1,RB1S-AC2,RB1S-AC3` BEFORE the flip. `RB1S-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming Andrew's read at the drain (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v1 section 6).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v1 -- every named existing file measured present at origin DEV ad7c100b5c; the write sets are pairwise disjoint (decomp v1 section 3 and 5).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~2, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_RBNDV2 2 --portal-ref feature/dsgn-rbndv2-light`.
