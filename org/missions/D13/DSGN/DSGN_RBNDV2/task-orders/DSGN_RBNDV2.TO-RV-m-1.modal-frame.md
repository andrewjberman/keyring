# TO DSGN_RBNDV2.TO-RV-m-1 -- FWD-3: the one shared modal frame (ModalFrame) in the A-light fixture

<to_id>DSGN_RBNDV2.TO-RV-m-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~8</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<round>2</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-m-1` (decomp v2 @95d724679e) | **outcome_ref:** FWD-3 | **depends_on:** -- (chain 1, first) | **slot:** ~8, queue position 1 of 6

---

## WORKER FACE

### THE CELL

`RV-m-1` -- THE ONE SHARED MODAL FRAME (FWD-3, C-MODAL). Modals have no shared frame today: 10 files import `portal/src/ui/components/catalyst/dialog.tsx` and about as many more draw their own `fixed inset-0` overlay.

Create `portal/src/ui/components/modal/ModalFrame.tsx` and export `ModalFrame` (and `ModalFrameProps`) with EXACTLY this API, which five adoption cells (`RV-m-2` to `RV-m-6`, later orders in YOUR queue) build against:

```ts
export interface ModalFrameProps {
  open: boolean
  onClose: () => void
  title: ReactNode
  size?: 'sm' | 'md' | 'lg' | 'xl'   // content max width 28rem, 36rem, 48rem, 64rem; default 'md'
  footer?: ReactNode
  closeOnBackdrop?: boolean              // default true
  className?: string                    // on the content wrapper
  children: ReactNode
}
export function ModalFrame(props: ModalFrameProps): JSX.Element | null
```

It renders nothing when `open` is false. When open it renders INLINE (no `createPortal`, so `renderToStaticMarkup` can test it) a full-viewport overlay `fixed inset-0` with a high z-index and a navy scrim (a token-based navy at about 40 percent, for example `bg-[color-mix(in_srgb,var(--rb-ink)_40%,transparent)]`), centring a dialog surface with `role="dialog"`, `aria-modal="true"` and `aria-labelledby` pointing at the title element's id (generate the id with `useId`). The surface is the A-light panel: `bg-[hsl(var(--bg-surface))]`, a 1px `border-[hsl(var(--hairline))]`, square corners, NO shadow, and it carries `data-panel-surface="light"` (this attribute is what makes the round-1 ink rule and the inner-surface token remap apply to everything inside the modal, so a modal body written for a dark ground reads on the white surface). Header: the eyebrow title (11px, 700, letter-spacing 0.14em, uppercase, `var(--rb-ink-2)`, with a 2px `border-[var(--rb-accent)]` underline and 4px below), padding `22px 30px 16px`, a 1px `var(--rb-rule)` rule below, and on the right a square close button (`aria-label="Close"`, 1px `hsl(var(--hairline))` border) calling `onClose`. Body: padding `24px 30px`, scrolls (`overflow-y-auto`, max height of the viewport minus the margins). Footer (only when `footer` is given): a 1px `var(--rb-rule)` rule above, padding `16px 30px`, actions right-aligned. Behaviour: Escape calls `onClose`; a click on the scrim (not on the surface) calls `onClose` when `closeOnBackdrop` is not false; on open the surface takes focus and on close focus returns to the element that had it (use an effect); body scroll is not locked beyond what the page already does. Also write `portal/src/ui/components/modal/README.md` (about 20 lines) that states the API and how a modal adopts it.

**Out of this cell:** every adopting modal file (the next five orders in your queue), `catalyst/dialog.tsx` (left as is), and `index.css`.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. The light look is Andrew's: you reproduce the fixture and invent nothing. TOKEN FORMATS (a defect in round 1 came from mixing them): the `--rb-*` tokens (`--rb-rule`, `--rb-row-rule`, `--rb-ink`, `--rb-ink-2`, `--rb-ink-3`, `--rb-quiet`, `--rb-accent`) are HEX values, so you read them as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`; `--bg-surface`, `--bg-page`, `--hairline` and the `--semantic-*` tokens are HSL triples, so you read them as `hsl(var(--X))`. No shadow anywhere, radii 2/3/4px only (`portal/DESIGN.md` C11), no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. You are given the worker face only: open your order file only to edit its status or amend a criterion the issuer has ruled on, and do NOT read anything below its `## RECORD FACE` line.

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `adc70061` (the difference-control base). The fixture is `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md`; read it first. Round 1 is merged on the branch: the `--rb-*` tokens, the ground `#EAEAF7`, the white panel primitives, and two scoped rules keyed on `data-panel-surface="light"` (text-white idioms resolve to navy ink; the old dark surface tokens resolve to white and silver). An element carrying `data-panel-surface="light"` therefore reads as a light surface for everything inside it. Do not start any server.

### ACCEPTANCE

<criterion id="RB2M1-AC1" cell_refs="RV-m-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/ui/components/modal/__tests__/dsgn-rbndv2/rb-2-m1.frame.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: MODAL-FRAME-OK</expect></criterion>
`RB2M1-AC1` -- rendering `ModalFrame` to static markup: with `open` false the markup is empty; with `open` true and a title, a body and a footer, the markup contains `role="dialog"`, `aria-modal="true"`, an `aria-labelledby` whose id matches the title element's id, `data-panel-surface="light"` on the surface, `bg-[hsl(var(--bg-surface))]`, `border-[hsl(var(--hairline))]`, `var(--rb-accent)` for the title underline and `var(--rb-rule)` for the header rule, a button with `aria-label="Close"`, and the footer content; the markup contains no `shadow`, no `rounded-lg`, no `rounded-xl`, no `hsl(var(--rb-`; the source file contains an Escape key handler and a scrim click handler; (difference control: the same text arms run on the string `<div role="dialog">` alone must FAIL the surface arms, proving the test can fail). The test prints `VERDICT: MODAL-FRAME-OK` only when every arm holds.

<criterion id="RB2M1-AC2" cell_refs="RV-m-1" judgment="true"/>
`RB2M1-AC2` -- graded at the round-2 close by the COO on a modal opened in the live walk, then the CVO and Andrew (DEC-5), never self-graded: the frame reads as the A-light panel (white, silver edge, eyebrow title with the violet underline, hairline rules, no shadow). RECORD; no verdict.


<expected_criteria>RB2M1-AC1, RB2M1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/ui/components/modal/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v2.md</decomp_doc> v2 @95d724679e, cell `RV-m-1`.
<owned_cells>RV-m-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB2M1-AC1, RB2M1-AC2. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~8/DSGN_RBNDV2.TO-RV-m-1.modal-frame.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB2M1-AC1,RB2M1-AC2` BEFORE the flip, run from inside your worktree. `RB2M1-AC2` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's round-2 close walk and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and name any shared-file hookup the merge must add; surprise rows in the investigation file (id `DSGN_RBNDV2-W8-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v2 -- every named existing file measured present at the feature branch adc70061; write sets are pairwise disjoint (decomp v2 section 3).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~8, queue position 1 of 6; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 8 --portal-ref feature/dsgn-rbndv2-light`.
