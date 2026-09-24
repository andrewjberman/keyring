# Peers B04/P1: the act executed, and one sentence of mine corrected -- 2.0.0_SA_COO~Z (addendum)

**Window:** 03:30Z-03:45Z, continuing `coo_z_claude_takeover_peers_0240-0330Z.md`. Push state of every commit
below: LOCAL (MSTR owns shared pushes).

## Objective

Execute the pool publication once both never-widen halves were in hand, prove it three ways, hand the grading
to the CVO, and record the one claim from the previous log that measurement overturned.

## Compiler Tools

No `comp-*` invocation; the reads were a git show of the CTO half, S3 head/list calls, `crosswalk.resolve`
against the pool, Lambda invokes and a browser re-walk. `.tools/commit-gate.sh` clean on `publish_peers_candidate.py`.

## Work Completed

### 1. The CTO half arrived with a condition, and the condition was honoured in-process
`NEVERWIDEN_PEERS_CTO_HALF.md` @`429efcdf30` (msg 25202): a head-object on `crosswalk/v1/2026-09-24.json`
immediately before the put, 404 required, because `write_pool`'s `IfMatch` branch OVERWRITES an existing key
whose digest differs -- my half had named only the `IfNoneMatch` branch. That correction is right and is now in
the receipt. `publish_peers_candidate.py` (committed @`f12263b4e7`) verifies every candidate file's sha256 against
the manifest, refuses if any peer key exists, re-runs the head-object with the 2026-09-22 control, then puts
through the producers' own writers with read-back. Result: `UPLOADED 194 of 194 + 1 crosswalk, read-back 195 of
195`; `PUBLICATION_RECEIPT.json` lists every key (the rollback denominator).

### 2. Post-act, three instruments
- Pool: latest crosswalk is `2026-09-24`; `resolve()` over the 191 prior pool keys = 191 MEASURED.
- Deployed function, direct invoke, CodeSha256 unchanged: AAPL derived 10 SERVED with `price/ev/ey` on members;
  CAT derived 12; 6861_JP derived 4; ASML SERVED absent with reason; BA derived 12 with carried fields; the
  negative control UNRESOLVED.
- Served stack, signed-in re-walk 03:34Z (`PEERS_LIVE_TRACE_20260924T0335Z/`): Boeing, Lenovo, Caterpillar
  DERIVED / 12 comparables; ASML shows its reason instead of UNRESOLVED; the counts line still reads "1 column(s)
  carry" because the served bundle has the old column map until portal `1ec5446c` deploys.

### 3. Correction
The 03:30Z log and my 03:22Z handoff said `DE_US_Equity` (Posture's Boeing comparable) "is among the 158 the
candidate registers". It is not. Deere is a scanner MEMBER, never a `universe/v1` subject; no registration
source carries it; Posture still reads it UNRESOLVED after the act on two instruments. I inferred the sentence
from "DE is a US ticker" and never ran the resolver on it. Corrected in STATUS.md and in msg 25212/25213.

## Decisions Made

- Executed the act on the pair as signed; nothing else rode along (no deploy, no vendor call, no delete).
- The Posture comparable key space (2,851 scanner rows vs 194 subjects) is an OPEN CALL to the CTO with a
  recommendation (a third crosswalk source under the same refusal rules), not a build started here.

## Files Modified

Branch `closer/amgt-peers-z-20260924` @`f12263b4e7`: `publish_peers_candidate.py`, `PUBLICATION_RECEIPT.json`,
`PEERS_LIVE_TRACE_20260924T0335Z/`, `STATUS.md`. Shared tree: this log.

## Blockers

None BLOCKED. Gated on peers: CVO grading (msg 25213); MSTR merge + portal deploy of `1ec5446c`; the CTO's
ruling on the comparable key space.

## Current State

Pool published and served. Seat LIVE, watcher armed (task bk123v4z8). Andrew's signed-in profile persists in
the scratchpad for a further re-walk after the portal deploy.

## Next Steps

1. [`3.0.0_SA_CVO~Z`] Grade E0/P1 from the two trace folders and the receipt.
2. [`0.0.0_AB_MSTR~Z`] Merge the branch to CLOUD and portal `1ec5446c` to DEV/PROD on Andrew's word.
3. [`1.0.0_SA_CTO~Z`] Rule the comparable key space; the slash-key route shape sits on the enrichment list.
4. [`2.0.0_SA_COO~Z`] After the portal deploy, re-walk the six cases and expect "5 column(s) carry" at n=12;
   then the 60-name induction as its own scripted, deterministic act under the 02:47Z word.
