# NFRA_OPSEC202609 -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Assembled by:** `3.0.0_SA_CVO~Z` (L8: the CVO assembles, any seat surfaces -- `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY`.
**Project state at this write:** L3 @32daebf403, L4 @43b75ffbd6 (PRD v0.4, `dep_stage: PRD`); L5 is
`2.0.0_SA_COO~Z`'s; no task orders yet; L7 has not started. This file is opened BEFORE L7 because the first row
is about the loop's own L10 handoff mechanism on this device, found while the L8 owner read the tool it will use.
**Append-only during the round.** Denominator at this write: **1 row** (S1 appended by `3.0.0_SA_CVO~Z` 07:17Z).

## L8 read -- what the CVO checked on each row

- **S1** (surfaced by `3.0.0_SA_CVO~Z` directly; the row is its first home, no message precursor). Grounding
  RESOLVES at this seat: the three cited lines of `.tools/prd-header-notify.py` read as quoted at @e906c6f156,
  and the same tool's L4 path was EXERCISED on this project minutes earlier -- its `[PRD LANDED]` row 19465 sits
  `QUEUED` at the BASE serial `2.0.0_SA_COO` (delivery state read at this seat), while every live site-Z seat is
  a `~Z` lane and the base inboxes are unwatched here. Held `UNDER_INVESTIGATION`: the DISARM is an act at L10
  (a lane-addressed pointer beside the mechanical re-offer), which has not happened yet, and DISARMED is not
  REMEDIATED -- the remedy is a lane-aware recipient in the tool, owned by the gate/notifier surface. Nothing to
  route now; a route needs every task order terminal, and none exists.

```json
[
 {
  "id": "NFRA_OPSEC202609-Z-S1",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (L8 owner, reading the L10 handoff tool before the act)",
  "surfaced_at": "2026-09-03T07:17:37Z",
  "one_line": "The L10 route handoff (.tools/prd-header-notify.py kind:route) and the L4 handoff in the same tool address BASE serials (RECIPIENT default 2.0.0_SA_COO; ROUTE_OWNER {2: 1.0.0_SA_CTO, 5: 2.0.0_SA_COO, 6: 2.0.0_SA_COO}) with no lane resolution -- on site Z every live seat is a ~Z lane and the base inboxes are unwatched, so the notification re-offers until READ to an inbox nobody reads; already exercised on this project at L4 (row 19465 QUEUED at 2.0.0_SA_COO, 0 rows at 2.0.0_SA_COO~Z).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "3.0.0_SA_CVO~Z -- DISARM at L10 (not yet due): beside the mechanical route notification, send the stamped row's pointer to the route owner's LIVE lane serial on this device (2.0.0_SA_COO~Z or 1.0.0_SA_CTO~Z), the same act 1.0.0_SA_CTO~Z performed for the L4 -> L5 handoff (msg 19471). The L4 instance is already disarmed by that pointer. DISARMED != REMEDIATED: the remedy is 1.0.0_SA_CTO's (notifier/gate surface).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/prd-header-notify.py:49 @e906c6f156 -- RECIPIENT = os.environ.get(\"PRD_NOTIFY_TO\", \"2.0.0_SA_COO\") -- a BASE serial, env-overridable for the L4 path only",
    ".tools/prd-header-notify.py:68 @e906c6f156 -- ROUTE_OWNER = {2: \"1.0.0_SA_CTO\", 5: \"2.0.0_SA_COO\", 6: \"2.0.0_SA_COO\"} -- BASE serials, no env override, no lane lookup",
    ".tools/prd-header-notify.py:364 @e906c6f156 -- the route send passes \"to\": owner straight from ROUTE_OWNER; :101 owner = ROUTE_OWNER.get(t); nothing between them consults liveness or a lane",
    "EXERCISED on this project, L4 path: get_delivery_state(message_id=19465) read at 3.0.0_SA_CVO~Z 2026-09-03T07:1xZ -> QUEUED, 1.0.0_SA_CTO~Z -> 2.0.0_SA_COO, 'no clock stamps yet'; 1.0.0_SA_CTO~Z 19471 reports 0 rows at 2.0.0_SA_COO~Z for it",
    "get_live_agents at 3.0.0_SA_CVO~Z 2026-09-03T06:49Z: 4 live -- 0.0.0_AB_MSTR~Z, 1.0.0_SA_CTO~Z, 2.0.0_SA_COO~Z, 3.0.0_SA_CVO~Z -- no base serial registered on this device; org/XXX.md: a lane's inbox is org/mcp/inbox/{base}/~{lane}/ and the base inbox is a different directory",
    "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md v2.3 L10 Tool: '.tools/prd-header-notify.py kind:route delivers a new route row to its owner and re-offers until READ'; Handoff: 'the stamped row to the route owner and to no one else'",
    "the L4 workaround that disarms one instance: 1.0.0_SA_CTO~Z 19471 sent the same identity to 2.0.0_SA_COO~Z by message and named the QUEUED base row -- the handoff reached its owner by a second carrier, not by the notifier"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Spine L10: 'prd-header-notify.py kind:route delivers a new route row to its owner and re-offers until READ' and 'the stamped row to the route owner and to no one else'; spine L4: 'prd-header-notify.py (post-commit) delivers a new or bumped header to 2.0.0_SA_COO and re-offers until READ. The handoff to L5 is that notification, never a dispatch.'",
  "world_is": "On site Z the owner named by the tool is a BASE serial that is not registered and whose inbox no Monitor watches; the notification is written and re-offered to a dead inbox indefinitely (READ never arrives, so the re-offer never stops), and the loop's L4 -> L5 and L10 -> owner handoffs reach their owners only by a second, hand-sent carrier. The tool's docstring names the very failure ('COO would never have been told') and the mechanism reproduces it one axis over -- right seat class, wrong instance.",
  "notes": "WHY A ROW AND NOT A MESSAGE: it is a spec-vs-world mismatch on this project's own loop, found off-task by the seat that will run L10; the row is the carrier. NOT CHASED: no edit to the tool from this seat -- a live post-commit hook edit in the shared tree is the never-rules-gate outage shape, and the surface is 1.0.0_SA_CTO's. REMEDY SHAPE, offered not prescribed: resolve the owner's live lane on the sending device (the broker's live-agents view already carries it), falling back to the base serial only when no lane of that base is live; or an env override for routes in the same shape as PRD_NOTIFY_TO. CLOSING CONDITION: (a) DISARMED when the L10 stamp on this project is followed by a lane-addressed pointer that reads READ on the delivery ledger; (b) REMEDIATED when a route notification on this device reads READ at a ~Z lane with no hand-sent pointer beside it (that is the falsifier: the mechanical carrier alone reaches the owner). The L4 instance (19465) stays QUEUED as a measured artifact of the defect; nobody should ack it from the base serial to make the number look right."
 }
]
```
