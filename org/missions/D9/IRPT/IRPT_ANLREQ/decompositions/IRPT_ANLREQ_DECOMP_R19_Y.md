# IRPT_ANLREQ -- decomposition, round 19, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-19 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` @c18650ea00 (no PRD addendum; PRD v0.4 stands) answering the round-18 slug `REMEDIATION_v11.md` @8cf145cf49 and the CVO's L9 grade (5 PASS; 6 rows OPEN, 5 ARMED, one LIVE: `IRPT_ANLREQ-D2-W52-S33`).

**Thread:** FWD-1 is not live. The LIVE hazard is that `irpt-ycharts-generate`'s pinned reader `3f29017cfc` has no account check and no total-row check, so a two-account or total-row upload through the Lambda's door is held as one portfolio. The reader built in rounds 16-18 (r18.1) is unreleased. **Round 19's FIRST item is that reader's RELEASE PAIR**, with the pinned pair run in a scratch tree before the pair is cut (the CVO's AR186 condition). Nothing else is cut ahead of it.

## How the ENRICHMENT LIST maps (CTO section 2)

| item | carrier |
|---|---|
| 1. the reader's release pair (S33 LIVE, S35), the pinned pair run in a scratch tree first | cells `AR-y-191` (the start state, RUN in a scratch tree), `AR-y-192` (the release census of `irpt-ycharts-generate`: the map's members and pins, the four native unpinned members, the resident's pin rule), `AR-y-193` (the BUILD_ONLY release build with the planned pins); the PAIR itself and the APPLY are the issuer's act and an applier's order after these |
| 2. the vocabulary widening and the value backstop (S31, S32), built; they ride the NEXT reader release unless they merge before item 1's pair is cut | cell `AR-y-194`, NOT SPAWNED until the pair is cut (the CTO: nothing else in this round is cut ahead of item 1) |
| 3. the status rule's pair (W54-S5, W55-S1), all eight packagers | the issuer's pair on the round-18 records (`AR-y-172`, `AR-y-184`, `AR-y-185`); NOT a cell; follows the reader's pair |

**Standing, not a cell (row `IRPT_ANLREQ-D2-W53-S9`, owner this seat):** no rebuild of `irpt-ycharts-generate` is cut by any lane until each of its four native unpinned members is pinned or released under its own pair. This round's `AR-y-192` and `AR-y-193` are what pin them for this release.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-191` | a scratch-tree RUN of the Lambda's start state (`uploads.py` `f09b802cdc` + `template_reader.py` `3f29017cfc` + their pinned neighbours): the door's answers for the account, total-row, one-account and two-sheet sheets, and the re-open of a pinned-stored template under the pinned pair and under the widened pair | the worker's deliverables | LOCAL |
| `AR-y-192` | a read of the release: the map entry's members and pins for `irpt-ycharts-generate`, the four native unpinned members and what each is pinned to now, the planned pin moves so the release moves only the reader members, and the resident's pin rule, current pin, builder, deploy path and owning lane | the worker's deliverables | LOCAL |
| `AR-y-193` | the release BUILD (BUILD_ONLY, in a throwaway worktree): the package hash, a member manifest, and the proof that the members that differ from the baseline are exactly the planned ones; the map edit as a patch, not applied to the trunk | the worker's deliverables | WORLD (build only; nothing uploaded or applied) |
| `AR-y-194` | the vocabulary widening once more (plural tails, `acct`/`accnt`, `nos`, `seqno`, `serial`, `roth ira` and `trust` as modifiers) and ONE value backstop: a column whose header carries an account root and holds two or more distinct identifier-like values is read as an account column; `No. of Accounts` excluded only when its values are counts; each with a census line and a negative control | `intake/template_reader.py`, intake tests, the worker's deliverables | WORLD (BUILT, not released) |

## Edges and chains

- `AR-y-192` -> `AR-y-193`: the build follows the census's planned pin moves. `AR-y-191` and `AR-y-192` have no edge. `AR-y-194` waits for the pair to be cut (the CTO's ordering).
- M = 3 chains: {191}, {192, 193}, {194}.

fanout: 3 of 3 chains, cap 8, reason: three chains; `AR-y-193` waits on `AR-y-192`, and `AR-y-194` is held until the reader's release pair is cut.
