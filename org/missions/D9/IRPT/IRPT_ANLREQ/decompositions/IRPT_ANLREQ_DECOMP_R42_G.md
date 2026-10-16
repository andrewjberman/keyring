# IRPT_ANLREQ round 42, workstream ~G (ENGINE) -- decomposition: the resolve hop backs off a WAF challenge (growing spacing, 15-minute cap)

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** FWD-1 run 3 SET 2: ZQXWVK's resolve was challenged on each of its four receives and ended `RESOLVE_RETRY_EXHAUSTED` while four earlier resolves answered; AQ2's cookieless lookup at ~14:06Z (`WAFLOOK_READ.txt`, commit d871a499b3) read CLEAN (200, no WAF action, JSON), so the challenge is transient. CTO msgs 9429 and 9447: cut the bounded back-off in its own cell and pair NOW, not gated on SET 3: WAF_CHALLENGE on the resolve hop backs off like BUSY with growing spacing, capped at 15 minutes total, the class named on each retry, then the row ends as today; tests on both sides. The issuer's draft with its evidence: `deliverables/2.0.0_SA_COO~G2/WAF_BACKOFF_DESIGN_20261016.md` (commit 093448e534).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Where:** only the `RETRY` branch of the resolve poll in `ycharts/generate/resident_worker.py`. A new pure function `_resolve_retry_visibility(code, receives)` returns the growing schedule `RESOLVE_WAF_BACKOFF_S = (150, 300, 450)` (receive 1, 2, 3) for a code that ENDS with `:WAF_CHALLENGE`, and the flat `RESOLVE_RETRY_VISIBILITY_S` (60) for every other cause. Total 900 s: the CTO's cap, under `REDRIVE_SECONDS` (960, so the client cannot re-dispatch a row still waiting) and under the queue's maxReceiveCount (`RESOLVE_MAX_RECEIVES` 4 stays below 5). Receive 4 ends the row exactly as today.
- **Why these numbers:** the code's own record (`resident_worker.py` lines 860-864) puts the YCharts firewall window in (122, 373] s; the flat 60 s retry sits inside it. The 150 s attempt sits at the window's lower edge; the 450 s and 900 s attempts clear it.
- **Journal:** the RETRY line gains `visibility=<s>`; the class is already in `code=`.
- **Not changed:** the door's lookup (sessionless, batch 72 item 12), the lease, the BUSY path, `_end_exhausted_resolve`, the message shape.
- **This round is the source change and its tests (one worker cell).** The r34f tooling, the build over the running r34e root, the packet, the CTO's pair and the AQ2 apply with V2 in the service's own environment are the next round's cells, after this merges.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-129` | `resident_worker.py`: the constants, `_resolve_retry_visibility`, the RETRY branch using it and printing `visibility=`; new tests in `ycharts/generate/tests/test_resolve_upload.py` | the worker, its test file, the worker's folder, the order, the channel file | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |

## Edges and chains

- ONE chain. The r34f rebuild consumes this cell's merged bytes.

## Four-postulate record

(i) Domain: the RETRY causes of the resolve hop (WAF challenge, other provider refusals, BUSY). (ii) One schedule per cause class. (iii) One intent: a transient WAF window is waited out without the client re-dispatching. (iv) What this cut does NOT move: the door's lookup, the lease, the checker, the host, the Lambdas.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 262).
