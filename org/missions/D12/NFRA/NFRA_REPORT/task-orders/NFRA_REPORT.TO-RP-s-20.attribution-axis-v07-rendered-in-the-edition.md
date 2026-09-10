# NFRA_REPORT.TO-RP-s-20 -- The attribution axis at PRD v0.7, RENDERED in the edition

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R3.md</decomp_doc>
<owned_cells>RP-s-20</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (manifest row S13; outcome FWD-4; acceptance property 3)

```
RP-s-20 mirrors manifest row S13. ACT: bring FWD-4's attribution axis to PRD v0.7 in BOTH
places it has to live -- the LAW and the RENDERED EDITION.

LIMB A -- THE LAW. ATTRIBUTION.md currently renders `opal-gateway` and `opal-globgrph` as
UNGROUPED, and its line 30 still reads "third member (Gateway, Graph, or both) | OPEN CALL AT
ANDREW, NOT DECIDED HERE". PRD v0.7 CLOSED that call: the axis has FOUR ratified members --
Dashboard | Website | Gateway | Graph -- and names those two surfaces as the referents of the
two new ones. `opal-gateway` is Gateway (the MCP server); `opal-globgrph` is Graph (the ECS
Fargate cluster). UNGROUPED is NOT retired: it now means a live surface outside all four, a
smaller set, and it must still RENDER rather than vanish.

LIMB B -- THE EDITION, and this is the limb the outcome actually needs. MEASURED AT THE CUT:
the rendered edition carries NO ATTRIBUTION AXIS AT ALL. EDITION_SPECIMEN.md sec.2's row table
has FIVE columns -- Property | Previous state | This edition | Delta | Citation -- and
compose_edition.py:428 emits exactly that header. A census of the rendered edition for
'UNGROUPED|Dashboard|Website|Gateway|Graph' returns 10 hits across 104 lines and NOT ONE is an
axis value ("Website security" is a row subject, "API Gateway" a service name, the only
"Dashboard" sits inside the function name getPlatinumFirmDashboard). So FWD-4's bar -- every
finding rolls up to a NAMED part of the business with an owner -- is not served by the artifact
a reader reads. ADD THE ATTRIBUTION so every row of the composed edition carries its axis value.

NEITHER ROUND-2 CELL IS AT FAULT AND THIS IS NOT A REPAIR OF THEIR WORK. ATTRIBUTION.md says in
its own words that "the per-row rendering ... is the composer's act (RP-s-15, S2), not this
cell's" -- RP-s-13 correctly deferred it and RP-s-15 was never told to do it. You are closing a
gap between two correctly-executed cells, not fixing a defect in either.
```

## DEPENDENCIES

This cell depends on: none -- this cell is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
THE MEMBER NAMES ARE RULED AND CLOSED. Do NOT re-open them, do NOT carry the old open call
forward, and do NOT invent a fifth member. Andrew-direct 2026-09-10 ~02:5xZ via 1.0.0_SA_CTO~Z
msg 20761, executed at PRD v0.7: "Dashboard | Website | Gateway | Graph". WHY FOUR, so you can
apply it rather than pattern-match it: opal-gateway (EC2, MCP server) and opal-globgrph (ECS,
3 of 3 services) are both live, both always-on, and FAIL DIFFERENTLY -- folding either into
Dashboard makes FWD-4's own bar false by construction.

UNGROUPED IS NOT RETIRED and removing it is a defect, not a simplification. It now means a live
surface outside all four. It must still RENDER. The ruling names the members; it does NOT promise
the four are exhaustive of everything this estate will ever run.

`canonical-schwab-si2` is Dashboard, RULED AND CLOSED (Andrew-direct 2026-09-09 ~22:3xZ). No cell
may render it ungrouped.

DO NOT RE-DERIVE THE ROW SET. compose_edition.py's ROW_FACTS are QUOTED transcriptions of round-1
findings, per its own build-ladder note. You are adding an axis value to rows that already exist;
you are not re-measuring what runs, not adding rows, and not running any live AWS read.

DO NOT WEAKEN THE COMPOSER'S DETERMINISM. RP-s-15 established that a re-run reproduces its own
edition byte-for-byte except the composed-at timestamp. AC6 guards it. If your change breaks
that, the change is wrong.

NO ALARM, TOPIC, SUBSCRIPTION, MONITOR OR NOTIFICATION. The standing moratorium is ARMED (1 of
12 NEVER clauses in the law). This cell renders a column; it raises nothing.

RUN EVERY CENSUS FROM THE MAIN CHECKOUT, NEVER FROM YOUR OWN WORKTREE. The comp-rail
(comp-find / comp-read / comp-which) resolves its corpus from the TOOL SCRIPT'S OWN on-disk
location, not your cwd -- so a comp-tool run inside a linked worktree silently scans the MAIN
ajb_workspace checkout and prints a large, confident, MEASURED denominator over the wrong tree.
A comp-tool ZERO obtained inside a worktree is NOT evidence of absence. Citable at
org/modules/graph/INSTRUMENT_LIMITS.md LIMIT 4 / 4a; carried in project.json `blocking` fact (6).
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule: RUN at this cut, 5 of 5 carriers, 20.3 s. C1=23 C2=6 C3=12 C4=20 C5=335.
  2 gates ARMED -- G-3 (owner CTO), G-7 (owner POD4). NEITHER is this project's and NEITHER
  binds this cell. (C2 moved 7 -> 6 since the round-2 cut; round-2 orders carry 7.)
comp-iam stats: RUN at this cut -- 195 roles, 188 services, 1084 operations, 304 permission
  gaps. DOES NOT BIND THIS CELL; recorded for the denominator only. This cell touches one
  markdown document and one local python script, no IAM surface and no AWS plane.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-20.attribution-axis-v07-rendered-in-the-edition.md
</paths>

READ-ONLY references you will need (do not write them):
`org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md` (v0.7 -- s.6 the ruling, s.8 row S13),
`org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R3.md`,
`org/missions/D12/NFRA/NFRA_REPORT/ledger/ROUND_ANALYSIS.round2.md`.

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverables are `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md`
and `.../compose_edition.py` (whose run regenerates `.../EDITION_SPECIMEN.md`).

## PROOF OF SPEC

⛔ **EVERY CRITERION BELOW SCORES THE RENDERED EDITION, NOT THE SOURCE AND NOT THE LAW DOCUMENT.**
That is directed by the round-2 analysis §3 and it is not a generic caution: a criterion that
greps `compose_edition.py` for a four-member list would PASS while the composed edition still
carries no attribution at all. Each invocation therefore RE-RUNS the composer first, then reads
the artifact it produced.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-20"><invocation>cd "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1" && timeout 120 python compose_edition.py >/dev/null && grep -c -E '^\| *Property.*Attribution|^\| *Attribution' EDITION_SPECIMEN.md</invocation><expect>a count of 1 or greater -- the freshly composed edition's row-table header carries an Attribution column</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-20"><invocation>cd "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1" && timeout 120 python compose_edition.py >/dev/null && timeout 120 python -c "import re;L=[l for l in open('EDITION_SPECIMEN.md',encoding='utf-8') if l.startswith('|') and not re.match(r'^\|[ :-]+\|',l)];hdr=L[0];rows=[l for l in L[1:] if l.count('|')==hdr.count('|')];V=('Dashboard','Website','Gateway','Graph','UNGROUPED');ok=[r for r in rows if any(v in r for v in V)];print('ROWS=%d WITH_AXIS_VALUE=%d' % (len(rows),len(ok)))"</invocation><expect>ROWS and WITH_AXIS_VALUE are EQUAL and both greater than zero -- every rendered row carries an axis value, with its denominator printed</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-20"><invocation>cd "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1" && timeout 120 python compose_edition.py >/dev/null && timeout 120 python -c "L=[l for l in open('EDITION_SPECIMEN.md',encoding='utf-8') if l.startswith('|')];g=[l for l in L if 'opal-gateway' in l];r=[l for l in L if 'opal-globgrph' in l];print('GATEWAY_ROWS=%d GATEWAY_OK=%d' % (len(g),sum('Gateway' in l for l in g)));print('GRAPH_ROWS=%d GRAPH_OK=%d' % (len(r),sum('Graph' in l for l in r)))"</invocation><expect>GATEWAY_ROWS and GATEWAY_OK equal and nonzero, GRAPH_ROWS and GRAPH_OK equal and nonzero -- the two v0.7 referents render their NEW members in the edition</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-20"><invocation>cd "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1" && timeout 120 python compose_edition.py >/dev/null && timeout 120 python -c "L=[l for l in open('EDITION_SPECIMEN.md',encoding='utf-8') if l.startswith('|')];ref=[l for l in L if 'opal-gateway' in l or 'opal-globgrph' in l];bad=[l for l in ref if 'UNGROUPED' in l];print('REFERENT_ROWS=%d STALE_UNGROUPED_ROWS=%d' % (len(ref),len(bad)))"</invocation><expect>REFERENT_ROWS of 2 or greater AND STALE_UNGROUPED_ROWS=0 -- BOTH v0.7 referents are present as rows and neither renders UNGROUPED. The REFERENT_ROWS half is load-bearing: without it this criterion passes VACUOUSLY on today's edition, where neither surface renders at all (exercised at the cut: REFERENT_ROWS=1)</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-20"><invocation>timeout 120 grep -c -i -E 'OPEN CALL AT ANDREW|NOT DECIDED HERE' "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md"</invocation><expect>a count of 0 -- the law document no longer carries the open call v0.7 closed</expect></criterion>
  <criterion id="AC6" cell_refs="RP-s-20"><invocation>cd "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1" && timeout 120 python compose_edition.py >/dev/null && cp EDITION_SPECIMEN.md /tmp/ed_a.md && timeout 120 python compose_edition.py >/dev/null && diff <(grep -v -i 'composed' /tmp/ed_a.md) <(grep -v -i 'composed' EDITION_SPECIMEN.md) | wc -l</invocation><expect>a count of 0 -- the composer still reproduces its own edition determinism, RP-s-15's property preserved, timestamp lines excluded</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, RENDERED): the composed edition's row table has an Attribution column at all
- **AC2** (mechanical, RENDERED, DENOMINATOR PRINTED): *every* rendered row carries an axis value -- this is the criterion that can actually fail on a half-done job
- **AC3** (mechanical, RENDERED): the two surfaces v0.7 moved render `Gateway` and `Graph` specifically
- **AC4** (mechanical, RENDERED, NEGATIVE): both referents are PRESENT as rows and neither renders `UNGROUPED` -- the mutant arm of AC3
- **AC5** (mechanical, LAW): the closed open-call prose is gone from `ATTRIBUTION.md`
- **AC6** (mechanical, REGRESSION): the composer's determinism survives the edit

### ⭐ THE RED ARM -- every criterion was EXERCISED against the world BEFORE this order was issued

A criterion that already passes cannot score the work, and a criterion that cannot run is not a
criterion. All six were run at the cut against the unmodified tree:

```
AC1  0                                        FAILS  (expect >=1)  -- no Attribution column exists
AC2  ROWS=25 WITH_AXIS_VALUE=4                FAILS  (expect equal) -- and the 4 are INCIDENTAL
                                                     ("Website security" a subject, "API Gateway" a name)
AC3  GATEWAY_ROWS=0 GATEWAY_OK=0
     GRAPH_ROWS=1   GRAPH_OK=0                FAILS  (expect equal and NONZERO)
AC4  REFERENT_ROWS=1 STALE_UNGROUPED_ROWS=0   FAILS  (expect REFERENT_ROWS>=2)
AC5  1                                        FAILS  (expect 0)
AC6  0                                        PASSES -- BY DESIGN, see below
```

⛔ **`opal-gateway` HAS NO ROW IN THE EDITION AT ALL** (`GATEWAY_ROWS=0`). So this cell does not
merely re-label existing rows -- **it must ADD the missing referent row.** That is measured, not
inferred, and it is the single most likely thing to be missed on a quick read of the ACT.

⚠ **AC6 PASSES AT ISSUANCE AND THAT IS CORRECT.** It is a REGRESSION guard on `RP-s-15`'s
determinism property, not a progress criterion: it must pass BEFORE and AFTER. Do not read its
pre-pass as a defect in the criterion set, and do not "fix" it.

⛔ **AC4's FIRST CUT WAS VACUOUS AND WAS REPAIRED BEFORE ISSUE.** As first written it asked only
"does either referent render UNGROUPED", which returned 0 on today's edition -- passing, because
neither renders at all. The `REFERENT_ROWS` half was added so the criterion cannot be satisfied by
absence. Recorded because it is the same defect class this order warns about, caught in this order.

⚠ AC1 and AC5 ARE WORD-PRESENCE COUNTS AND THEY ARE THE FLOOR, NOT THE BAR. AC2/AC3/AC4 are the
ones that discriminate, and AC2 prints its denominator so a partial job cannot read as a whole one.
This lane measured that 18 of 24 of its round-2 criteria were word-presence greps -- higher than the
round it was correcting -- and this cut is where that stops. The cell's ACT is the bar. If a
criterion passes on a deliverable that does not do the ACT, say so in your report rather than letting
the grep stand in for the work.

Every invocation runs under `timeout 120`; a timeout is recorded AS the output, so keep every invocation bounded.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>complete</status>
<round>3</round>
<sub_round>A</sub_round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN at the round-3 cut, 5 of 5 carriers, 20.312 s; C1=23 C2=6 C3=12 C4=20 C5=335; 2 gates ARMED (G-3 owner CTO, G-7 owner POD4), NEITHER this project's. C2 moved 7 -> 6 since the round-2 cut and that is a real change, not a transcription error.
comp-iam: RUN at the round-3 cut (`comp-iam stats`) -- 195 roles parsed, 188 services scanned, 1084 operations, 304 permission gaps. Does NOT bind this cell; recorded for the denominator only. NOT comparable to round 2's 836/96/31, which was a different subcommand over a different denominator.
comp-adversary: RUN on NFRA_REPORT_DECOMP_R3.md at the cut; grid in the issuance commit.
CELL-ID CONTROL: the analysis labels this cell `R3-1`. Measured against proof-of-spec-check.py::CELL_ID_RE, imported and applied -- `R3-1` REFUSED, `RP-s-20` MATCH, with `RP-s-13` as positive control and `bogus id` as negative. Cut as RP-s-20; a cell cut as R3-1 would have failed its own proof instance at L7.
DELIVERABLE FOLDER: derived from `<issued_to>` per row Z-S8 and the analysis's R3-2, which is honoured as an L6 cut mechanic rather than cut as a cell (DECOMP_R3 s.2, routed to 1.0.0_SA_CTO~Z in this lane's one send).
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 3) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** round 2 `L10 answered` -> `3.0.0_SA_CVO~Z` slug @`4fe64b8cac` -> `1.0.0_SA_CTO~Z` round-2 analysis @`2b44f4a62b` -> L5 recut `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R3.md` -> this issuance.
