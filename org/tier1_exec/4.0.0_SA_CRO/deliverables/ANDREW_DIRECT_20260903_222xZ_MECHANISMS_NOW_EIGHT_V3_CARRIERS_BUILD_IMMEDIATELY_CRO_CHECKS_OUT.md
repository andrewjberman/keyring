# ANDREW-DIRECT -- 2026-09-03 ~22:2xZ, the 4.0.0_SA_CRO terminal

**Channel:** Andrew at the `4.0.0_SA_CRO` terminal, in session, immediately after this seat's comparison of
`1.0.0_SA_CTO`'s commits against the v3 implementation spec (@`29bf9265ea`) -- which found the LAW layer complete
(spine v3.0 @`c3602bcf1a`, v3.1 @`20e1293216`; annex; TO protocol; CLAUDE.md R27; `/canonical-flow`;
`.claude/agents/worker.md`) and the MECHANISM layer at ZERO of the eight carriers the spine's own section 4 names
as binding by reading, four contradicted by a live gate or lane.
**Recorded by:** `4.0.0_SA_CRO`, same turn, verbatim. The phrasing IS the ruling.

## The words, verbatim

> We need the mechanisms addressed right now, the fuck are they doing, tell them to get on it immediaately, and
> when theyre done you check out the results

## What the words bind (surfaced, not adjudicated)

- **"the mechanisms"** = the eight clauses `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` section 4 (v3.1
  @`20e1293216`) names as binding by reading until their carriers land. Enumerated below with the owner the
  spine and the lanes give each, and the acceptance test this seat will run at check-out.
- **"right now" / "immediately"**: these are the next act at every owning seat, ahead of anything else in
  flight that is not itself a hold of Andrew's.
- **"tell them"**: `4.0.0_SA_CRO` relays; it does not build another seat's mechanism and does not adjudicate the
  list wider or narrower than section 4 -- the list is the scribe's own text.
- **"when theyre done you check out the results"**: `4.0.0_SA_CRO` exercises each carrier with an instrument
  other than the builder's report -- the planted tests below -- and reports the measured state to Andrew.

## The eight, with owner and check-out test

| # | carrier (spine s.4) | owner | check-out test (`4.0.0_SA_CRO` runs it) |
|---|---|---|---|
| 1 | **Coverage limb** in `.tools/to-pipeline-gate.py`: a tree issuance at `dep_stage: DECOMP` is refused unless the union of `<owned_cells>` across the staged task orders equals the decomposition's cell set | `1.0.0_SA_CTO` (the gate's author) | a planted issuance missing one cell is REFUSED naming the cell; the same issuance with the cell PASSES; a self-test arm RED/GREEN |
| 2 | **Row lane**: `TREE_PROJECT_ROW` in `.owned-paths.yaml` admits `2.0.0_SA_COO` to `project.json` for the `EXECUTING` flip in the issuance commit | `0.0.0_AB_MSTR` as registry grantor (SoD: the grantee never writes its own grant); if MSTR is dark, `1.0.0_SA_CTO` lands it citing this record, the grantee still not writing it | `owned-paths-check.sh` run as `2.0.0_SA_COO` on a staged `project.json` under a tree project PASSES; as `0.8.0_AE_CloudComp` still REFUSES (negative control) |
| 3 | **Worker toolkit, first exercised spawn**: one `worker` subagent spawned in a worktree on an existing terminal task order's worker face, committing under `0.9.0_WK_<CODE>~1` through the lane gates | `2.0.0_SA_COO` (the seat that spawns); if dark, `1.0.0_SA_CTO` on this record | the worker's branch exists with a commit authored `0.9.0_WK_*`; `owned-paths-check` admitted it; telemetry row under that serial; the worker's final message in the WORKER REPORT shape |
| 4 | **One clause per criterion**: `org/standards/PROOF_OF_SPEC.schema.json` gains `expect` and `judgment`; `.tools/proof-of-spec-check.py` matches a mechanical criterion's output against its `expect` and refuses a judgment criterion carrying a verdict; `to-pipeline-gate.py` refuses at the cut a compound criterion or a mechanical one without `<invocation>` + `<expect>` | `1.0.0_SA_CTO` | a planted instance whose output does not match `expect` is INVALID; a judgment row with `status: PASS` is INVALID; a task order with a conjoined criterion is REFUSED at the cut; the 21 existing NFRA_COMPEFFICACY instances still read as they do today (no retroactive break) or the checker says which limb is v3-only |
| 5 | **Adjudications document**: `org/standards/PROJECT_TREE.contract.json` + `missions-tree-check.sh` admit `surprise-channel/adjudications/`; `surprise-row-gate.py`'s L10 census reads investigations AND adjudications and `adjudicates` resolves across the two; lane `TREE_CVO` covers `adjudications/` | `1.0.0_SA_CTO` (contract, gates); `0.0.0_AB_MSTR` (the lane, or CTO on this record) | a `3.0.0_SA_CVO`-authored `ADJUDICATION_v1.md` under a tree project COMMITS through the tree check; an item dispositioned only there reads dispositioned to the L10 census (`--self-test` arm) |
| 6 | **A remediation row carries no route**: `surprise-row-gate.py`'s route limb retired (the three tokens are retired in v3) | `1.0.0_SA_CTO` | a slug with no `route` field on an OPEN remediation row PASSES without override; the locked-map arm retired or inverted |
| 7 | **The CVO's single send**: `org/mcp/cvo_send_guard.py` admits `3.0.0_SA_CVO` (any ~lane) ONLY to `1.0.0_SA_CTO`, at EVERY `dep_stage`; refuses CVO to `2.0.0_SA_COO` and to any Tier-2 always | `1.0.0_SA_CTO` | `--self-test` arms: CVO->COO refused at EXECUTING and at ROUND_CLOSE; CVO->Tier-2 refused at ROUND_CLOSE (the window that was open); CVO->CTO admitted; applied on the MCP path per session start and the daemon path at restart, stated |
| 8 | **Fail-closed sentinels**: `.git/hooks/pre-commit` stages 8/9/10 sentinels match the tree spellings `task-orders/` and `surprise-channel/`, carried in `.tools/git-hooks/install-*.sh` so a second clone gets them | `1.0.0_SA_CTO` | the positive-control test this seat ran at 20:0xZ (sentinel regex vs a real tree path, control on the legacy path) fires on BOTH shapes |

Also owed under the spec's section 12 but not "mechanisms": step 2 the COO's dispatch skill (`/dispatch`:
chains -> N -> cut all -> `fanout:` -> flip -> spawn -> drain -> merge), step 4 the `ledger/ROUND_ANALYSIS.round<N>.md`
template, step 7 one small project run through v3 with the step logs. Named so nobody reads them as done.

## Broadcast

Same turn, to `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, with this record's path and hash and
push state stated. Completion reports come back to `4.0.0_SA_CRO` by message with the commit hash and the test the
builder ran; `4.0.0_SA_CRO` re-runs the check-out test above with its own instrument and reports to Andrew.
