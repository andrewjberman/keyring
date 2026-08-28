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


ROOT_FAMILIES = ("0.0.0_AB_MSTR", "1.0.0_SA_CTO")
EPOCH_CLOSED, EPOCH_OPEN = "CLOSED", "OPEN"


def check_epoch_actor(batch_records, principal, reject):
    """Row 6 -- `actor` is AUTHORED DATA, so bind it to the writer BEFORE trusting it.

    The order is the whole control (CVO~X 054009Z). `actor` is a string inside a record the writer
    composed, so a writer can type a trusted-looking family name into it. Checking the FAMILY first
    and the writer second admits the spoof, because a spoofed actor passes the family predicate by
    construction -- it was chosen to. So: bind actor to the authenticated submitting principal, and
    only then ask whether that principal is a root family.

    A batch carrying an epoch event with NO authenticated principal is refused: the ledger cannot
    bind what it was never told, and an unauthenticated epoch transition is the one write that
    rewrites who may mint.
    """
    for rec in batch_records:
        if rec.get("record_type") != "authority_epoch_event":
            continue
        actor = rec.get("actor")
        if principal is None or actor != principal:
            reject("L-06-epoch-actor-spoof-rejected",
                   "epoch event %s claims actor %r but the authenticated submitting principal is "
                   "%r; `actor` is authored data and is bound to the writer BEFORE the family "
                   "predicate is applied (sec 3 row 6)"
                   % (rec.get("event_id"), actor, principal))
        if actor not in ROOT_FAMILIES:
            reject("L-06-unauthorized-epoch-transition-rejected",
                   "epoch event %s has actor %r, which is not one of the ROOT families %s "
                   "(sec 3 row 6, R4-CRO-6)"
                   % (rec.get("event_id"), actor, " / ".join(ROOT_FAMILIES)))


def epoch_intervals(records, authority_id, primary, seqs, reject=None):
    """Walk the TOTAL machine for one authority. Start CLOSED; return its OPEN intervals.

    TOTAL means every event has a defined verdict from every state -- `opened` only from CLOSED,
    `closed` only from OPEN -- so there is no state where the machine shrugs. A voided event is not
    a transition and never appears here.
    """
    events = effective(records, "authority_epoch_event", "authority_id", authority_id,
                       primary, seqs)
    state, opened_at, intervals, seen_open = EPOCH_CLOSED, None, [], False
    for ev in events:
        kind, when = ev.get("event_kind"), ev.get("occurred_at")
        if kind == "opened":
            if state == EPOCH_OPEN and reject:
                reject("L-06-overlapping-epoch-rejected",
                       "authority %s receives `opened` while already OPEN: two overlapping "
                       "intervals make 'was it open at t' ambiguous (sec 3 row 6)" % authority_id)
            state, opened_at, seen_open = EPOCH_OPEN, when, True
        elif kind == "closed":
            if state == EPOCH_CLOSED and reject:
                rule = ("L-06-duplicate-close-rejected" if seen_open
                        else "L-06-close-without-open-rejected")
                reject(rule, "authority %s receives `closed` while already CLOSED (sec 3 row 6)"
                       % authority_id)
            intervals.append((opened_at, when))
            state, opened_at = EPOCH_CLOSED, None
    if state == EPOCH_OPEN:
        intervals.append((opened_at, None))
    return intervals


def check_epoch_machine(records, primary, seqs, reject):
    """Row 6 -- the TOTAL epoch machine, per authority_id, over EFFECTIVE events."""
    authorities = {r.get("authority_id") for r in records
                   if r.get("record_type") == "authority_epoch_event"}
    for authority in sorted(a for a in authorities if a):
        epoch_intervals(records, authority, primary, seqs, reject)


def authority_open_at(records, authority_id, when, primary, seqs):
    for start, end in epoch_intervals(records, authority_id, primary, seqs):
        if start is not None and start <= when and (end is None or when < end):
            return True
    return False


def check_mint(records, batch_records, primary, seqs, reject):
    """Row 6 -- mint-receipt authentication, mint-fact equality, one receipt per serial.

    AUTHORIZATION IS AN ADMISSION-TIME FACT (R3-CRO-34). The authority must be OPEN at the
    receipt's `minted_at` as evaluated when THIS batch is admitted -- so a `closed` backfilled
    later never re-opens an already admitted mint's verdict. That is why this runs over the batch's
    own records: an admitted mint is never re-judged. The different question -- "which authorities
    were open at t?" -- is answered by event time on the replay surface, and the two must not be
    collapsed.
    """
    receipts = [r for r in records if r.get("record_type") == "mint_receipt"]
    by_serial = {}
    for rec in receipts:
        by_serial.setdefault(rec.get("entity_serial"), []).append(rec)
    for serial, found in sorted(by_serial.items(), key=lambda kv: str(kv[0])):
        if len(found) > 1:
            reject("L-06-second-receipt-for-serial",
                   "entity %s has %d mint receipts in (store U batch); a serial is minted ONCE "
                   "(sec 3 row 6)" % (serial, len(found)))

    entities = dict((primary(r), r) for r in records if r.get("record_type") == "entity")
    for rec in batch_records:
        if rec.get("record_type") != "mint_receipt":
            continue
        authority, when = rec.get("minting_authority"), rec.get("minted_at")
        has_events = any(r.get("record_type") == "authority_epoch_event"
                         and r.get("authority_id") == authority for r in records)
        if not has_events:
            reject("L-06-authority-unregistered",
                   "minting authority %r has no authority_epoch_event in (store U batch): an "
                   "unregistered authority is never OPEN (sec 3 row 6)" % authority)
        if not authority_open_at(records, authority, when, primary, seqs):
            reject("L-06-authority-closed-before-mint",
                   "minting authority %r is not OPEN at minted_at %s, evaluated as of this "
                   "batch's own admission (sec 3 row 6, R3-CRO-34)" % (authority, when))
        ent = entities.get(rec.get("entity_serial"))
        if ent is not None:
            if ent.get("minted_at") != rec.get("minted_at"):
                reject("L-06-minted-at-mismatch",
                       "entity %s says minted_at %r, its receipt says %r; the entity's mint facts "
                       "must EQUAL the receipt's (sec 3 row 6)"
                       % (primary(ent), ent.get("minted_at"), rec.get("minted_at")))
            if ent.get("minting_authority") != rec.get("minting_authority"):
                reject("L-06-authority-mismatch",
                       "entity %s says minting_authority %r, its receipt says %r (sec 3 row 6)"
                       % (primary(ent), ent.get("minting_authority"),
                          rec.get("minting_authority")))
