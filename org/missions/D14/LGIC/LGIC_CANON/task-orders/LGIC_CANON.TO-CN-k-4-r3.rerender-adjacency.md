# TO LGIC_CANON.TO-CN-k-4-r3 -- re-render the canon's naming section after alias_adjacency; the producer exclusion prints its predicate

<to_id>LGIC_CANON.TO-CN-k-4-r3</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.5 (ADMITTED; both halves current) | **Decomp cell:** `CN-k-4` (decomposition v5.1, section 0e) | **outcome_ref:** FWD-1 | **depends_on:** none -- level 0; CN-k-5 continues on this slot after this drains

---

## WORKER FACE

### THE CELL

`CN-k-4`, round-3 re-cut -- rulings A-18 and A-20 (`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` s.2; row LGIC_CANON-S11). **You edit `infra/logic/02_DOCTRINE.md` (only BY RENDERING it) and `infra/logic/render_naming_section.py`.**

**WHY.** `org/standards/NAMING_SCHEMA.json` gained `alias_adjacency` (v1.10, @5a12d0b97c), and the canon's generated naming section (between `<!-- BEGIN GENERATED NAMING SECTION -->` and `<!-- END GENERATED NAMING SECTION -->`) was never re-rendered, so the canon and the schema disagree at HEAD on the `bd` reading. Measured at the cut: `python infra/logic/render_naming_section.py --content-diff` prints `CONTENT-DIFF: 17`, every DROPPED line under `/alias_adjacency/`, and `--check` is not FRESH.

What this cell must do, each measured below:
1. **Re-render.** `python infra/logic/render_naming_section.py --write`. If `--content-diff` still reads above 0 afterwards, the renderer does not yet render the dropped items: extend the renderer so the section carries them, then re-render. Never edit between the markers by hand.
2. **The `producer` exclusion's predicate, made mechanical (A-20).** The renderer's content-diff excludes `/key/legacy_served_paths/producer` as provenance (its exclusion table near `render_naming_section.py:339`). The exclusion is ACCEPTED only while NO consumer reads that field. Make `--content-diff` run a reader census over the repository's tracked files (`git ls-files`, excluding the renderer, `NAMING_SCHEMA.json` and the canon) for code or documents that read the `producer` field of `legacy_served_paths`, and print exactly:
   `EXCLUSION-PREDICATE producer: <n> consumer(s) of <m> file(s) scanned`
   and, ONLY while `<n>` is 0, a line `EXCLUDED: /key/legacy_served_paths/producer -- no consumer reads it`. When `<n>` is above 0 the exclusion drops and the item is compared like any other. State the census's match rule in the renderer's `--help` text.
3. **Commit, then grade.** `k3-contentdiff` plants a removal in the canon and restores it; it REFUSES on a canon with uncommitted edits in your tree.

**Read:** `infra/logic/render_naming_section.py` (`content_diff`, the exclusion table, `--write`, `--check`); `org/standards/NAMING_SCHEMA.json` `alias_adjacency`; `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-10.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="K4R3-AC1" cell_refs="CN-k-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k4-fresh</invocation><expect>PASS-K4-RERENDERED-AT-SCHEMA</expect></criterion>

<criterion id="K4R3-AC2" cell_refs="CN-k-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py k3-contentdiff</invocation><expect>PASS-K3-CONTENTDIFF-PLANTED</expect></criterion>

<criterion id="K4R3-AC3" cell_refs="CN-k-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_canon_r3.py k4-producer</invocation><expect>PASS-K4-PRODUCER-PREDICATE</expect></criterion>

<criterion id="K4R3-AC4" cell_refs="CN-k-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py k3-note</invocation><expect>PASS-K3-FIRM-NOTE-RENDERED</expect></criterion>

<criterion id="K4R3-AC5" cell_refs="CN-k-4" judgment="true"/>

<expected_criteria>K4R3-AC1, K4R3-AC2, K4R3-AC3, K4R3-AC4, K4R3-AC5</expected_criteria>

**AC1-AC3 read RED at the cut** (not FRESH; `CONTENT-DIFF: 17`; no predicate line). **AC4 reads PASS at the cut and must still pass** (the registry's FIRM-row note stays rendered). **K4R3-AC5, for `3.0.0_SA_CVO` at L9:** the census's match rule is stated and would count a real reader of the field, and the canon's generated `bd` reading now agrees with the schema's `alias_adjacency`.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including everything under `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_CANON-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_CANON-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/` -- slot numbers were used in earlier rounds, so `S1` is usually taken). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** Do not change `NAMING_SCHEMA.json` or the registry; the schema is the one owner of the section's content.

<paths>
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/02_DOCTRINE.md
infra/logic/render_naming_section.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v5.1, round-3 cell `CN-k-4` (section 0e).
<owned_cells>CN-k-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `K4R3-AC1`, `K4R3-AC2`, `K4R3-AC3`, `K4R3-AC4`, `K4R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-k-4-r3.rerender-adjacency.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> K4R3-AC1,K4R3-AC2,K4R3-AC3,K4R3-AC4,K4R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-k-4-r3.rerender-adjacency.md` BEFORE the `complete` flip.
Result file `rerender-adjacency.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`K4R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- repository documents only; no principal, policy or resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; every criterion reads the repository's own renderer and canon.
lane: the <paths> block is the grant; both files were granted to round-2 workers the same way.
contention: 02_DOCTRINE.md is also CN-k-5's; both sit on slot ~1 in sequence, so no two worktrees edit it at once.
</preflight>

Seating: slot ~1, queue position 1. Round 3 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND2_ANALYSIS.md` @4a55888962); issued by `2.0.0_SA_COO~G`. Decomposition v5.1, section 0e. Rulings carried: A-18, A-20, R-10.
