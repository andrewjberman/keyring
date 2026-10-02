# CTO half -- the comparison catalogue served: irpt-ycharts-generate at 97eaff05ff, then its route (IRPT_BCKEND)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/CATALOGUE/NEVER_WIDEN_SIGNOFF_PACKET_GENERATE_CATALOGUE_20261002.md`
@ef923a2038, **blob `49517c7d7b`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104073. Rulings: batch 61 item 8, the list rule
IRPT-CATALOGUE-LIST-NAMED-ONLY-20261001, condition 11 of the Analysis whole-bundle half (@40aa13548a). This half is a separate file
bound to that blob.

## SIGNED, 2026-10-02 ~05:5xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: D1 one function's code (`irpt-ycharts-generate`, 112 members, 12 changed, of which only
`comparison_catalogue.py` changes behaviour on the handler's reachable import graph); D2 one API route (`GET analysis/comparisons`,
1 to add, already `DECLARED` in `routes.json`, the api root's one carrier). No IAM, queue, table or schema change. Every branch of the
read is stated, and a failed or denied Scan refuses -- never an empty or stale list. No page calls the route yet. Rollback per move.

**Condition 11 is met as written:** the list is served from at most one paged Scan per warm container per 300 s, whatever the request
rate (measured: one Scan for the first build, none for three more inside the window), not a full-table Scan per request.

The packet's order is a condition of this half: D1, then the served-reads check, then D2, then V1; each apply targeted. Batch 115 item 3
binds here too: the `ycharts` root is applied only by this packet's targeted plan.

Named by this half in addition:

1. The list now carries the 19 Cottonwood seed rows written 02:12Z, two of them single stocks (Berkshire A and B), as batch 103 item 6
   accepted by WMT's precedent; whether the series provider returns a series for each stays unmeasured until a request picks one.
2. Not verified by this seat: the zip's sha256 and census, the reach graph, the targeted plans, the 04:5xZ measure on the real table.

-- 1.0.0_SA_CTO
