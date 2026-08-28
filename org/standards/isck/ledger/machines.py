#!/usr/bin/env python
"""The EFFECTIVE-event machines (design sec 3 rows 4, 6, 7, 13) and the VOIDED derivation.

A MACHINE IS EVALUATED OVER THE FINAL STATE, NOT OVER THE ARRIVING BATCH. Sec 2c admits a batch
atomically against (store U batch), so "is this a second open?" is a question about the whole
estate after the batch lands -- including a same-batch race, where two opens arrive together and
neither is "second" by arrival order. Evaluating per-record would admit that pair.

ORDER IS TOTAL AND IS `(occurred_at, commit_seq, event id)`, in that order, everywhere. Event time
first because that is what the design's semantics are about; commit_seq second because event time
ties are real and admission order breaks them deterministically; the event id last because a
same-instant same-batch pair still needs ONE answer (R4-CRO-5). A machine that ordered by event
time alone would be non-deterministic on a same-timestamp pair and would give two replays two
different answers about one estate.

VOIDED IS NOT A FIELD -- IT IS DERIVED, AND FROM EXACTLY TWO SOURCES (round-4 item 8, R4-CRO-7):
  * an admitted `upheld` contest on an EVENT whose consequence is exactly ONE replacement event of
    the same event_kind and the same carrier key, or
  * an admitted `nullified` contest on the event -- no replacement; the only way a false
    decommission, a false close or a false epoch-open is undone.
`opened`, `dismissed` and `merged` contests void NOTHING. A voided event advances no machine and
feeds no fold. This is the single derivation every machine below consults, so "effective" means the
same thing in all four -- if each machine decided voidedness for itself they would drift, and the
drift would show up as one machine retiring a materializer that another still considers live.
"""

CORRECTIVE_OUTCOMES = ("upheld", "nullified")
EVENT_CARRIER_KEY = {
    "binding_event": "binding_id",
    "lifecycle_event": "materializer_serial",
    "authority_epoch_event": "authority_id",
}


def _seq(record, seqs):
    return seqs.get(id(record), 0)


def order_key(record, seqs, primary):
    """(occurred_at, commit_seq, event id) -- the one ordering, used by every machine."""
    return (record.get("occurred_at") or "", _seq(record, seqs), primary(record))


def voided_event_ids(records, primary):
    """Event ids voided by an admitted corrective contest. The ONE derivation (see module docstring)."""
    voided = set()
    for rec in records:
        if rec.get("record_type") != "contest_event":
            continue
        if rec.get("event_kind") != "resolved":
            continue
        if rec.get("outcome") not in CORRECTIVE_OUTCOMES:
            continue
        target = rec.get("target_event_id")
        if target:
            voided.add(target)
    return voided


def effective(records, record_type, key_field, key_value, primary, seqs):
    """Admitted, not voided, of one carrier key -- in the total order."""
    voided = voided_event_ids(records, primary)
    rows = [r for r in records
            if r.get("record_type") == record_type
            and r.get(key_field) == key_value
            and primary(r) not in voided]
    rows.sort(key=lambda r: order_key(r, seqs, primary))
    return rows


def check_binding_machine(records, primary, seqs, reject):
    """Row 4 -- one machine per `binding_id` over EFFECTIVE binding events.

    A binding opens once and closes once. Re-opening is a NEW binding_id, never a second `opened`
    on the old one: the interval is the identity, so a reopened interval that kept its id would
    make "when was this binding open?" unanswerable.
    """
    keys = {r.get("binding_id") for r in records
            if r.get("record_type") == "binding_event" and r.get("binding_id")}
    for key in sorted(k for k in keys if k):
        events = effective(records, "binding_event", "binding_id", key, primary, seqs)
        opens = [e for e in events if e.get("event_kind") == "opened"]
        closes = [e for e in events if e.get("event_kind") == "closed"]
        if len(opens) > 1:
            reject("L-04-second-open-rejected",
                   "binding %s has %d effective `opened` events; a binding opens ONCE and a "
                   "re-open is a new binding_id (sec 3 row 4)" % (key, len(opens)))
        if len(closes) > 1:
            reject("L-04-second-close-rejected",
                   "binding %s has %d effective `closed` events (sec 3 row 4)" % (key, len(closes)))
        if opens and closes:
            first_close = min(closes, key=lambda e: order_key(e, seqs, primary))
            later_open = [o for o in opens
                          if order_key(o, seqs, primary) > order_key(first_close, seqs, primary)]
            if later_open:
                reject("L-04-open-after-close-rejected",
                       "binding %s has an `opened` ordered after its `closed`: the forbidden "
                       "re-open (sec 3 row 4)" % key)


def check_binding_rows(records, stored_before, primary, reject):
    """Row 4 -- a binding CLOSES BY EVENT, never by mutating the row, and never without one."""
    for rec in records:
        if rec.get("record_type") != "entity_binding":
            continue
        rid = primary(rec)
        before = stored_before.get(rid)
        if before is not None and before.get("valid_to") != rec.get("valid_to"):
            reject("L-04-close-by-mutation",
                   "binding %s changed `valid_to` in place; a close is an EVENT, and a mutated "
                   "row leaves no record of who closed it or when (sec 3 row 4)" % rid)
        if rec.get("valid_to") and before is None:
            closed = [r for r in records
                      if r.get("record_type") == "binding_event"
                      and r.get("binding_id") == rid
                      and r.get("event_kind") == "closed"]
            if not closed:
                reject("L-04-close-without-event",
                       "binding %s carries `valid_to` with no `closed` binding_event in "
                       "(store U batch) (sec 3 row 4)" % rid)
