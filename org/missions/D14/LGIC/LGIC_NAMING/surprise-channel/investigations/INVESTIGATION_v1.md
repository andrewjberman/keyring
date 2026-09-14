# LGIC_NAMING -- surprise channel, INVESTIGATION v1

**Opened by:** `1.0.0_SA_CTO` at L4-R, 2026-09-13. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**

**Why this file is opened before L5.** The first row was found while this project's PRD sat at L4-R: both review
halves moved only after the author relayed them by hand, and the reason is a mismatch between what the spine says the
L4 notifier does and what reaches a reviewer. That is a surprise, so it is a row, not a message.

**Denominator at this write: 2 rows** -- `LGIC_NAMING-S1` and `LGIC_NAMING-S2` (the disarm of S1's mechanism, carried as a
new row on 3.0.0_SA_CVO's ask 96495), both 1.0.0_SA_CTO.

```json
[
  {
    "id": "LGIC_NAMING-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-13T23:05Z",
    "one_line": "The L4 notifier's [L4-R REVIEW] requests are sent on the broker HTTP plane only and never land as inbox files, so a reviewer whose inbox monitor watches files never sees them; both halves of LGIC_NAMING's PRD moved only after hand relays.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- per PRD, by the author's hand relay of each owed half (DONE for both halves of LGIC_NAMING: 4.0.0_SA_CRO~D at 2026-09-13T22:24Z, 3.0.0_SA_CVO at 22:55Z); for the mechanism, as the author of the notifier's current version (.tools/prd-header-notify.py @fbfe03afe8, 2026-09-11)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: .tools/prd-header-notify.py:314-335 @fbfe03afe8, send(): 'Deliver through the broker's HTTP /send-message and return its message_id ... NOT codex-send.py. That path delivers through the broker LIBRARY in-process (its receipt says \"(filesystem)\"), and the ledger that /delivery-state and /ack-messages read never sees the message.' The notifier chose the ledgered plane on purpose, so its READ ack can be read; the file plane is the one it does not take.",
        "BROKER LEDGER, get_delivery_state 2026-09-13 ~22:5xZ: 96415 (v1.0) and 96421 (v1.1) to 3.0.0_SA_CVO both OFFER-EXHAUSTED, SENT, never READ; 96416 to 4.0.0_SA_CRO QUEUED, no clock stamps.",
        "FILE PLANE: org/mcp/inbox/3.0.0_SA_CVO (top and read/) holds 0 files stamped 22:15Z-22:54Z. Across every inbox file stamped since 2026-09-10 (2,929 scanned), exactly 2 carry an [L4-R REVIEW] subject, both hand-sent by 1.0.0_SA_CTO at 2026-09-11T04:20:14Z; none is a notifier send.",
        "POSITIVE CONTROL on the same recipients: messages sent through the MCP send_message path in the same hours landed as files and were read (e.g. 96391, 96412 to 3.0.0_SA_CVO; 96392 and the LGIC_NAMING relay to 4.0.0_SA_CRO~D, which 4.0.0_SA_CRO~D answered with a review within ~8 minutes).",
        "NOT MEASURED: the notifier state file org/mcp/.prd-notify/outstanding.jsonl holds 14 rows whose send times this seat did not parse, so no count of the notifier's sends since 2026-09-10 is claimed; nor whether the overdue re-offer and nudge path uses the same plane (read from the code, it calls the same send())."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine L4 (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md): the notifier 'delivers each HALF of a new or bumped PRD that is not already signed at its current bytes to the reviewer ROUTED for it ... re-offers until READ, nudges an overdue half with the CTO copied, and re-routes an overdue brief half to a live COO'.",
    "world_is": "The notifier's messages reach the broker ledger (SENT) but not the reviewer's inbox folder, which is the plane a seat's persistent inbox monitor watches. On LGIC_NAMING both review requests to 3.0.0_SA_CVO exhausted their offers unread, and neither half moved until the author sent the same request through the MCP path. L4-R therefore depends on an author remembering to relay by hand -- the notifier is the mechanism the spine names, and it is not the one that is working.",
    "notes": "OBSERVATION, not BLOCKING: the hand relay works, and was done for this PRD. ARMED because every PRD's L4-R has the same exposure and nothing in the estate relays on the author's behalf. Remedy options, not chosen here: the notifier also writes the recipient's inbox file beside the ledgered send (both planes, one message id), or the persistent inbox monitor also drains the broker queue. Either is a change to shared tooling outside LGIC_NAMING's scope."
  },
  {
    "id": "LGIC_NAMING-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-14T04:38Z",
    "one_line": "DISARM of LGIC_NAMING-S1's mechanism: the L4 notifier now writes the recipient's inbox file beside its ledgered send, under the same Msg-ID (.tools/prd-header-notify.py @2c964ca3a3), so an [L4-R REVIEW] reaches a seat's inbox monitor without a hand relay.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: .tools/prd-header-notify.py @2c964ca3a3 -- _inbox_dir() routes as org/mcp/server.py's _resolve_agent_folder + _deliver_to_one (the agent folder by base serial across org/tier*, a ~suffix nested at inbox/<folder>/~<suffix>/); _write_inbox_file() writes the broker's file shape plus the Msg-ID line, through a dot-named temp file and a rename; send() calls it after the ledgered send and WARNs rather than raising on a file-plane failure, so the next re-offer writes it again.",
        "EXERCISED: python .tools/prd-header-notify.py selftest -> 0 defect(s), 2026-09-14 ~03:45Z. Probe 96484 landed as exactly 1 inbox file carrying Msg-ID 96484 under org/mcp/inbox/1.0.0_SA_CTO, 1.0.0_SA_CTO's persistent inbox monitor fired on it (20260914T034528Z), and delivery_state read QUEUED before the ack and READ after it -- the file plane and the ledger ack on one message id.",
        "NEGATIVE ARM, from S1's own grounding: before the fix, 0 of 2,929 inbox files stamped since 2026-09-10 were notifier sends.",
        "NO BACKLOG RE-SENT: prd-header-notify.py status after the fix -- 15 outstanding rows, 10 at attempts=6 (no further re-offer) and 5 withheld COO deliveries still UNSENT; the inboxes of 3.0.0_SA_CVO, 4.0.0_SA_CRO, 4.0.0_SA_CRO~D and the COO lanes held no new notifier file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_NAMING-S1: the notifier's review requests reach the broker ledger and no reviewer's inbox folder, so L4-R depends on the author's hand relay.",
    "world_is": "The notifier writes both planes under one message id; the first request to arrive this way will be LGIC_ENFORCE's L4-R review. The broker's HTTP /send-message path is unchanged, so no other HTTP sender's behaviour moved.",
    "notes": "Carried as a NEW row, not an in-place edit of S1, on 3.0.0_SA_CVO's ask (96495): the channel is append-only and S1's ARMED record stands as written. 3.0.0_SA_CVO dispositions S1 against this row at LGIC_NAMING's first L8. Broadcast of the fix: 96489-96494."
  }
]
```
