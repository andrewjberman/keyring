# IRPT_ANLREQ -- decomposition, round 14, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-14 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_14_20261011.md` @1edb90ada7 (msg 5849): section 2 rules five questions; section 3 is the ENRICHMENT
LIST, seven items. No PRD addendum; the endpoint is unchanged. The outcome served is TCKT_VNEXT FWD-3 (a bad holdings sheet is
turned back from the form with what to fix), on surfaces this workstream holds.

**Thread:** FWD-1 is not live. Hop 2 (the upload door) accepts a two-account sheet and a totals-row sheet today
(row `IRPT_ANLREQ-D2-W52-S10`).

## How the seven items map

| item | carrier |
|---|---|
| 1a. the multi-sheet fixture, read first | inside cell `AR-y-142` (it is the reader's own fixture) |
| 1b. what the LIVE provider answers for a total label | cell `AR-y-141` finds HOW it is asked and WHO can ask with no new grant; the ask itself is ONE read-only Tier-2 order the issuer cuts from that record in this round (not a worker's: a worker makes no live call) |
| 2. the census in the template reader and its findings, built not released | cell `AR-y-142` |
| 3. words for every finding code; a raw code only inside a closed Details | service half: cell `AR-y-143`; form half: cell `AR-y-144` |
| 4. the first answer carries what the POST can decide; the form re-posts, bounded, only for pricing | service half: `AR-y-143`; form half: `AR-y-144` |
| 5. the release under its own pair | cell `AR-y-145` (the release census: consumers and both branches), NOT SPAWNED until `AR-y-143` is merged; the pair and the apply order are the issuer's, written on it |
| 6. counts of past uploads, in the next served-read window | ONE read-only Tier-2 order to the seat that holds the decrypt, cut by the issuer when `AR-y-142` has fixed the two closed lists the count uses; counts only, no file content |
| 7. every order and record that names `parse.py` as the form's door is corrected | cell `AR-y-146` lists every mention with its owning lane; the issuer corrects its own files and passes the others to their lanes |

Ruling 3 (who edits `ops/status.py`): MEASURED by the issuer, `python .tools/owned-paths-validate.py --check-path 2.0.0_SA_COO~Y2
infra/aws/lambda/investor-reporting/ops/status.py` prints `PERMIT ... lane=IRPT_COMPLETION_Y`: this lane. It is in `AR-y-143`'s grant.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-141` | a record: how the provider is asked about a symbol, what symbol each total label becomes, who can ask with no new grant, the exact invocation | the worker's deliverables | LOCAL |
| `AR-y-142` | the template reader refuses a sheet with an account column of two or more distinct values, a repeated header row, or a row labelled as a total, each with words and a row number; an accepted answer says only the first sheet was read; both closed lists with their Rule 24 record | `infra/aws/lambda/investor-reporting/intake/template_reader.py`, two test files | WORLD (the path's floor; nothing released) |
| `AR-y-143` | every finding code the reader can emit has words; the door's FIRST answer carries the findings the POST can decide; a sheet that needs pricing still answers RESOLVING first | `infra/aws/lambda/investor-reporting/intake/uploads.py`, `infra/aws/lambda/investor-reporting/ops/status.py`, two test files | WORLD (the path's floor; nothing released) |
| `AR-y-144` | the form shows a first-answer finding with no second press; re-posts a RESOLVING answer a bounded number of times with a stated wait; then shows the findings or says it is still working; a raw code only inside a closed Details | portal `src/pages/TicketCenter/` | LOCAL |
| `AR-y-145` | the release census of the upload door: which functions package the reader, their live and built digests, every consumer of the door's answer with one read through each, and both branches of a sheet accepted yesterday | the worker's deliverables | WORLD (live single-resource reads) |
| `AR-y-146` | every mention of `parse.py` as the form's door, with its file, line and owning lane | the worker's deliverables | LOCAL |

## Edges and chains

- `AR-y-142` -> `AR-y-143` (the codes the reader emits are what the words and the first answer carry): ONE queue, slot ~52.
- `AR-y-143` -> `AR-y-145` (the census is of the built state): slot ~53 after `AR-y-141`.
- `AR-y-141`, `AR-y-144`, `AR-y-146` have no edge. M = 4 chains: {142, 143, 145}, {141}, {144}, {146}.

fanout: 4 of 4 chains, cap 8, reason: four independent chains; slot ~53 takes {141} and then the tail of the build chain.
