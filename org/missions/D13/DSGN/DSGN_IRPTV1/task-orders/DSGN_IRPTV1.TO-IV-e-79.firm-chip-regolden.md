# TO DSGN_IRPTV1.TO-IV-e-79 -- Re-golden the five pinned tests that asserted the tab-body firm chip IV-e-73 removed (row W36-S3)

<to_id>DSGN_IRPTV1.TO-IV-e-79</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~36</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-28</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Decomp cell:** `IV-e-79` (decomp v9 addendum 2) | **outcome_ref:** FWD-1 (UIR-30, one firm mention) | **depends_on:** IV-e-73 (same slot, complete on this worktree) | **slot:** ~36, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-79` -- disarm row `DSGN_IRPTV1-W36-S3`. Your own previous order, IV-e-73 (UIR-30, one firm mention), made
`IR/global/FirmAttribution.tsx` render nothing unless its caller passes `show` (default false), so the tab bodies (ReportingTab,
HoldingsTab, AnalysisTab) no longer repeat the header's identity line; `IR/export/Preview.tsx` passes `show`. That is the ruled design
(CTO round-8 analysis UIR-30; IR = portal/src/pages/InvestorReporting). Five pinned tests asserted the OLD default and now fail (row
W36-S3, measured by you: 5 fail after, 0 before):

- `IR/__tests__/dsgn-irptv1/iv-e-23.firm-chip.test.ts` -- the chip face no longer contains the display name.
- `IR/__tests__/dsgn-irptv1/iv-e-38.header-identity.test.tsx` -- UIR-30 arm counts name occurrences 0, expected 1.
- `IR/__tests__/dsgn-irptv1/iv-e-56.firm-display.test.tsx` -- UIR-13d/e "attribution chip carries the display name".
- `IR/__tests__/fe-s-10/parity.test.ts` -- F10-AC5 (Global vs firm-scoped ReportingTab renders identical after stripping the
  `data-slot="firm-attribution"` element); its positive controls `expect(globalMarkup).not.toBe(firmMarkup)` and
  `globalMarkup.includes('49 Financial<')` relied on the chip being in the tab markup.
- `IR/__tests__/dsgn-irptv1/iv-e-23.parity-kept.test.ts` -- re-runs parity.test.ts in a child process; fails because it fails.

**Build (issuer ruling, 2.0.0_SA_COO~D, on row W36-S3):** re-golden each assertion to the ruled design, keeping every test's CLAIM and a
real control; a test is never deleted and no assertion is loosened to pass.
- The three FirmAttribution tests assert the display name on a mount that passes `show` (the Preview's use), AND that the default
  (no `show`) renders nothing -- each as its own arm.
- The header's name count (iv-e-38 UIR-30 arm) stays at exactly ONE mention on the page, where that one now lives (the header).
- parity.test.ts (KEPT test; its "never edited" line is superseded by this ruling, and the file names row W36-S3 at the edit): the parity
  claim stays -- Global and firm-scoped renders of one client at one revision are identical. With no chip in the tab, the renders are
  now byte-identical WITHOUT stripping; assert that, and replace the chip-based discriminator with a control that still proves the
  comparison can fail (for example, the same comparison over two different fixtures or revisions differs). Keep the `PARITY:` record
  line. iv-e-23.parity-kept.test.ts then passes unedited, or is re-goldened only as far as its child's output line changed.
- Product files are NOT edited in this order.

**Environment:** your worktree pair already carries IV-e-73's commits. Do not start any server. Work ONLY in your own <WS>. Finish and
commit before 02:45Z (a repository freeze forbids commits 03:00-05:00Z); if you cannot, commit what is proven and report what remains.

### ACCEPTANCE

<criterion id="IVE79-AC1" cell_refs="IV-e-79"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.firm-chip.test.ts ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-38.header-identity.test.tsx ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-56.firm-display.test.tsx ./src/pages/InvestorReporting/__tests__/fe-s-10/parity.test.ts ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.parity-kept.test.ts ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-73.one-firm-mention.test.tsx 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`IVE79-AC1` -- all five re-goldened files and IV-e-73's own test pass together. Base (this worktree at IV-e-73's head): FAIL (5 fail).
Each re-goldened control must be shown to bite: record in the proof instance one mutation per control (for example, restoring the
chip by defaulting `show` to true) that turns it red, then restore the committed bytes.

<expected_criteria>IVE79-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every product file is read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase,
  `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** synthetic ids only; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.firm-chip.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-38.header-identity.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-56.firm-display.test.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-10/parity.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-23.parity-kept.test.ts
portal/src/pages/InvestorReporting/fixtures/fe-s-10/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9 addendum 2, cell `IV-e-79`.
<owned_cells>IV-e-79</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE79-AC1. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~36/DSGN_IRPTV1.TO-IV-e-79.firm-chip-regolden.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE79-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; close row W36-S3 with a resolving row `DSGN_IRPTV1-W36-S<k>`.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- row W36-S3 (worker ~36 measured 0 fail before IV-e-73, 5 fail after, across the five named files); parity.test.ts :77-86 positive controls read the chip text in ReportingTab markup.
lane: the <paths> block IS the grant; the five files are written by no other open order of round 9.
</preflight>

Seating: slot ~36 (net-zero: the same worktree pair that ran IV-e-73), queue position 2 of 2.
