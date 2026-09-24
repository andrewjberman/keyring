# RAVC -- Request, Acknowledge, Validate, Close

**Scope: a one-off request between seats, outside any project.** Project work follows the canonical spine
(`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`): tracks share files, never messages; a worker cannot be messaged.
Cut to the three evidence rules on Andrew's word (report 3 item 1.5, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_170xZ_MEMORY_PREFERENCES_ONLY_AND_THREE_HELD_ITEMS_YES.md`);
the earlier text is in git history.

1. **Completion carries evidence.** The reply that closes a request names what was done and where to read it: a
   commit hash, an artifact path, or the tool output. A deliverable changed after it was reported is re-reported with
   its new commit-ish.
2. **Rework names a specific gap.** A request sent back names the gap against the evidence the request asked for,
   never "looks off".
3. **The requester looks before closing.** Open the commit or artifact, confirm it matches, and pin the commit-ish you
   checked in your close.

Escalate to Andrew only on: a requirement still ambiguous after one clarifying cycle; a blast radius past the stated
scope; a data-integrity finding; a destructive act; a priority collision.
