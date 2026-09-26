# Governance verdict -- may the ~O fabric keep driving NFRA_MCPINDEX and NFRA_OPLGTW?

Adjudicator: `3.0.0_SA_CVO~O`. Fork: `1.0.0_SA_CTO~O` msg 25998 (acked), self-drive ~O tick 1. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d, whose
Andrew-verbatim terms route a governance fork to this seat. Recorded 2026-09-26 ~03:5xZ.

## What the device guard protects

It exists to stop two devices driving one project, because that is the collision behind ONE ISSUER PER ROUND
(CLAUDE.md rule 27). The register's `device: LAPTOP` is how the guard learns that fact. So the question is not what the
register says. It is whether any laptop seat still drives these projects, and whether the ~O seats hold every leg they
act in.

## Verdict

**NFRA_MCPINDEX: YES.**
- The laptop released it. The re-seat commit @23bbeff325 cites 0.0.0_AB_MSTR ACK d36628dc: "Clear to move to
  1.0.0_SA_CTO~O".
- Every lead is ~O. `project.json` names `leads.cto` 1.0.0_SA_CTO~O, `leads.coo` 2.0.0_SA_COO~O and `leads.cvo`
  3.0.0_SA_CVO~O.
- No laptop seat has issued into it since the wind-down. The last laptop-issuer commits are 2.0.0_SA_COO~M's
  wind-down records (7466d470e1, f072dcdf4d, 2026-09-21). Since then the only laptop-lane commit on the tree is
  0.0.0_AB_MSTR's integration merge d9a28ef1aa, which merges and issues nothing.
- In the last 4 days the tree's authors are COO~O 13, CTO~O 6, DS~D 3, workers 3, CVO~O 1 and MSTR 1.
- Andrew's goal names it: "Finish all D6 opal_ai work, including the MCPINDEX" (record @c83c7de329).
- The guard's purpose is met, so its refusal would guard nothing.

**NFRA_OPLGTW: YES for the COO leg; NOT YET for the CTO and CVO legs.**
- COO leg: `coo_lane` is 2.0.0_SA_COO~O, and every commit on the tree since 2026-09-20 is COO~O's (5799432c1c,
  e2f11d1e3d, aa5a73bdb1, 768e6df290, e15cf70f1a). No other issuer exists. Andrew's 2026-09-26 "lift fully" (record
  @680212eda9) removed the stop. Its own gates (G-C/G-D, G-E/G-F) still bind.
- CTO and CVO legs: `project.json` still reads `leads.cto` **1.0.0_SA_CTO~A** and `leads.cvo` **3.0.0_SA_CVO** (base).
  1.0.0_SA_CTO~A is NOT REGISTERED (get_agent_status, this turn). OPLGTW has no record like MCPINDEX's @23bbeff325
  moving the PRD-owner seat to ~O. Without one, a CTO~O ruling on OPLGTW's PRD or its L10 analysis, or a CVO~O slug
  on its rounds, acts in a seat the carrier gives to another lane.
- **Condition that un-parks it:** a re-seat record for OPLGTW's CTO and CVO legs, in the same shape as @23bbeff325.
  It must carry a release from ~A's side, or Andrew's word, since ~A is not live to give one. It also updates `leads`
  in the same commit. Until then OPLGTW's round work stays with COO~O, and no CTO or CVO act on OPLGTW issues from ~O.
  The goal's words ("any and all MCP server work, entitlements") make OPLGTW in scope. Scope does not answer whose
  seat it is.

**The register fix: two carriers, not one.**
- DIRECTIVES.yaml, D9 `device: LAPTOP`: to 0.0.0_AB_MSTR~Z, as the REC puts it.
- The projects' own `project.json` fields `placement: LAPTOP` and `fabric: laptop` are also stale on both projects
  (read this turn). Under L3 the CTO writes every carrier, so these go with the CTO's re-seat record, not to MSTR.
  A guard that reads `project.json` would refuse on them after the register itself is fixed.

## The loop instruction (msg 26000)

Not armed this turn. `org/ref/LIVE_ARMS.md` holds no row for 3.0.0_SA_CVO~O, and the startup protocol reads "a row
absent there arms nothing". It also says a seat never writes its own row: 1.0.0_SA_CTO lands rows and names the
chooser. Andrew's template gives loop instructions to "every COO". The CVO pairing is the arming record's own reading
(`paired_with`), which the canonical-drive skill supports (CVO MODE, obligation 6). **Un-park condition:** when
1.0.0_SA_CTO~O lands the LIVE_ARMS row, naming the chooser and the message, this seat arms `/canonical-drive 30m` in
CVO MODE over NFRA_OPALAI, NFRA_MCPORTAL and NFRA_MCPINDEX the same turn. NFRA_OPLGTW joins after its re-seat.

Meanwhile nothing is dropped. This seat's inbox and surprise-channel watchers deliver every drain and every row as
they land. Every L8 this fabric has had so far was triggered that way.

-- 3.0.0_SA_CVO~O
