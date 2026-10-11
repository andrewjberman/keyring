# IRPT_ANLREQ round 5, workstream ~G -- decomposition: the first of the attach release's four cells

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `1.0.0_SA_CTO~DELL2` msg 4971: "The attach release, in order, each its own cell or pair: (1) the builder writes the
three bindings, off by default; (2) the packager's users row and credential, under a pair; (3) the one message on the
commentary-ready queue read by the laptop and named; (4) I3 last: binding it makes every READY invoke a live Lambda."
And msg 4920: the attach release is this lane's own order and pair, and "its pair names every message then waiting on each
queue it binds".

## Round 4 of this workstream, closed (one cell)

`AR-g-32` is complete and merged @41138b9305. Re-run by the issuer in the worker's tree before the merge:
`ar_g32_checks.py g32` read `AR-G32-OK passed=34`, `regress` read `AR-G32-REGRESS-OK research=281 factory=19`. The packager
makes no ticket read and pre-checks its own store by an id known before the render. Tree only; it rides the dead-letter
release st31 INERT (no binding). Two things the attach release's pair will name: the live pre-check treats the repository's
`ReportDenied("artifact unavailable")` as "no package" by its message text, and it calls the repository's private
`_binding` and `_owner`.

## Finding (read by the issuer at HEAD before cutting)

Two gaps stand between the tree and a bound resident, not one:

1. **The builder writes none of the three bindings.** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`
   holds 0 occurrences of `analysis_ready_queue_url`, `commentary_ready_queue_url` or a `packager` key; its bindings block
   (lines 223-242) has no optional member.
2. **The runtime never builds the live ticket port.** `reports/resident_installed.py` `build_resident_runtime` (line 392)
   calls `make_packager(...)` with no `ticket_ports`, so `attach` stays the module's refusing form
   (`PACKAGER_PRINCIPAL_UNSET`); nothing reads a `packager` binding. A resident bound to the commentary-ready queue today
   would refuse every message into the dead-letter queue.

## Cell (round 5, workstream ~G): attach cell 1 of 4

| cell | lane | what EXISTS at the end |
|---|---|---|
| `AR-g-41` | worker | The builder can write the three bindings and writes NONE unless asked (a build with no new flag gives the same bindings as today). The runtime reads a `packager` binding and builds the live ticket port from it; a commentary-ready queue bound WITHOUT a packager binding is refused at start, by name. Built and tested in the tree; NOT deployed, and no release in this cell |

## The other three attach cells (not cut here; each needs something this cell does not)

2. **The packager's users row and credential**, under a never-widen pair. Its executor writes a row in the users table and
   a secret; who that is, is the pair's first line.
3. **The one message on the commentary-ready queue** (1 visible at 13:04Z, queue created 2026-10-11T05:25:59Z): read by the
   laptop's executor and named. This box may not receive on that queue.
4. **I3 last**: the analysis-ready queue has a live consumer (`outlook-global-commentary-draft-lambda`, Enabled, batch 1).

## Four-postulate record

(i) Domain: attach cell 1 only. (ii) One cell, two files that must agree (what the builder writes, what the runtime
reads). (iii) One intent: a binding can be turned on by a release flag, and is off otherwise. (iv) What this cell does NOT
move: any host, any queue, any principal, any credential. A build with no new flag is byte-for-byte the bindings of today
except the two generated lines (pin and time).

fanout: 1 of 4 chains, cap 8; cells 2 to 4 are pairs and reads, not tree orders.
