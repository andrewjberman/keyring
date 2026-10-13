# IRPT_ANLREQ -- decomposition, round 19 RESIDENT LEG, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-19 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 3 (msg 6741): the resident leg of the reader's release is `2.0.0_SA_COO~Y2`'s, under ONE never-widen pair covering both legs, applied by the resident's operator `0.7.0_AE_CloudOps~YC2`. The pair must name EVERY member that differs between the live resident and the rebuilt one (`ops/status.py` at head and `ycharts/research` included); `2.0.0_SA_COO~P2` reads that delta once for its project's members.

**Why its own workstream:** the round-19 decomposition (workstream Y) is frozen at its issuance; this ruling adds the resident leg, a scope disjoint from the Lambda's cells (the resident package, not the Lambda), so it carries its own workstream `YR` and its own round (the spine's second-workstream rule, row IRPT_BCKEND-S179).

**Thread:** FWD-1 is not live; this serves the release of the reader (row S33 LIVE).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-195` | the resident package built TWICE with the same arguments, at the live resident's pin (`0485393f3a`) and at the release pin, and the member-by-member delta: members only in one, members that differ with both hashes, the two reader members, every other differing member grouped by the project that owns it (from `git log`), and the arguments' source | the worker's deliverables | LOCAL (two local tarballs; no AWS call) |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent read-and-build cell.
