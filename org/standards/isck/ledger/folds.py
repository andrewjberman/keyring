#!/usr/bin/env python
"""Row 5 -- the four derivation tables of sec 4, as FUNCTIONS.

A FOLD IS A FUNCTION: exactly one value for every reachable record set (R3-CRO-20 / R3-CVO-8).
Precedence is TOP-DOWN -- the first row whose condition holds wins -- and the last row is the
total-coverage default, which is what makes the function total rather than merely usually-defined.

THE FROZEN CONTRACT REQUIRES `status_basis: authored` ON ALL FIVE STATUS-BEARING RECORDS, and +38 is
immutable. So authoritative records stay AUTHORED -- always. What the ledger adds is not a new
`derived` value (that was a contract change dressed as a ledger rule, and the design withdrew it) but
a REJECTED WRITE: an authored value on a derivable axis that DISAGREES with the fold over the
admitted records is refused. LAW 3's enforcement plane arrives without a byte of the contract moving.

THE DERIVED VALUE LIVES IN A PROJECTION, WHICH IS NOT A RECORD. It has no record_type in the frozen
catalog, is never admissible as a write, and carries {axis, value, basis, derived_at_commit_seq} so
the `why` surface can show its working. A projection submitted as a batch member is REJECTED -- and
the refusal is the SAME one that rejects any non-catalog record_type, which is the point: a
projection is not "a record we chose not to store", it fails to be a record at all.

A VOIDED EVENT CONTRIBUTES NOTHING TO ANY FOLD. That is why `materializer.current_status` reads
`retired` only from an EFFECTIVE decommission: an upheld contest on a bad decommission voids it and
the fold falls through to row 2/3 (R4-CVO-3). The fold consults the same voided derivation the
machines do -- one definition, four consumers.
"""
from .machines import effective, voided_event_ids

DERIVABLE_AXES = {
    "entity": "current_status",
    "entity_binding": "status",
    "identity_relation": "verification_standing",
    "bridge_assertion": "verification_standing",
    "materializer": "current_status",
}


def _open_contest_against(records, target_field, target_value, target_kind):
    """An admitted `opened` contest with no `resolved` partner on the same contest_id."""
    opened = [r for r in records
              if r.get("record_type") == "contest_event"
              and r.get("event_kind") == "opened"
              and r.get("target_kind") == target_kind
              and r.get(target_field) == target_value]
    resolved_ids = {r.get("contest_id") for r in records
                    if r.get("record_type") == "contest_event"
                    and r.get("event_kind") == "resolved"}
    return [o for o in opened if o.get("contest_id") not in resolved_ids]


def entity_current_status(records, serial, primary, seqs):
    """sec 4 table 1. Row 1 outranks row 2: a contest on a RETIRED entity never changes the value."""
    relations = [r for r in records if r.get("record_type") == "identity_relation"]
    if any(r.get("relation_type") == "retirement" and r.get("subject_serial") == serial
           for r in relations):
        return "retired", [r.get("relation_id") for r in relations
                           if r.get("relation_type") == "retirement"
                           and r.get("subject_serial") == serial]
    unresolved = _open_contest_against(records, "target_entity_serial", serial, "entity")
    if unresolved:
        return "contested", [primary(c) for c in unresolved]
    receipts = [r for r in records
                if r.get("record_type") == "mint_receipt" and r.get("entity_serial") == serial]
    deferred = [r for r in receipts
                if r.get("collision_preflight") == "deferred_to_reconciliation"]
    if deferred and not any(r.get("relation_type") in ("canonicalized_as", "merged_into")
                            and r.get("subject_serial") == serial for r in relations):
        return "provisional", [primary(r) for r in deferred]
    return "active", [primary(r) for r in receipts]


def binding_status(records, binding_id, primary, seqs):
    """sec 4 table 2. Row 1 outranks row 2: a contest on a CLOSED binding leaves it closed."""
    closes = [e for e in effective(records, "binding_event", "binding_id", binding_id,
                                   primary, seqs)
              if e.get("event_kind") == "closed"]
    if closes:
        return "closed", [primary(e) for e in closes]
    unresolved = _open_contest_against(records, "target_binding_id", binding_id, "binding")
    if unresolved:
        return "disputed", [primary(c) for c in unresolved]
    opens = [e for e in effective(records, "binding_event", "binding_id", binding_id,
                                  primary, seqs)
             if e.get("event_kind") == "opened"]
    return "open", [primary(e) for e in opens]


def verification_standing(records, record_type, record_id, primary, seqs):
    """sec 4 table 3. The CHAIN HEAD's authored standing is the projection.

    A superseded assertion keeps its own authored standing and is never rewritten -- the projection
    is about the chain, not about the row. Single-valued by construction, because row 7 refuses a
    second assertion superseding the same target.
    """
    rows = [r for r in records if r.get("record_type") == record_type]
    by_id = dict((primary(r), r) for r in rows)
    superseded = {r.get("supersedes") for r in rows if r.get("supersedes")}
    node = by_id.get(record_id)
    if node is None:
        return None, []
    seen = set()
    while primary(node) in superseded:
        nxt = [r for r in rows if r.get("supersedes") == primary(node)]
        if not nxt or primary(nxt[0]) in seen:
            break
        seen.add(primary(node))
        node = nxt[0]
    return node.get("verification_standing"), [primary(node)]


def materializer_current_status(records, serial, primary, seqs):
    """sec 4 table 4. A VOIDED event contributes nothing -- that is the whole of R4-CVO-3."""
    events = effective(records, "lifecycle_event", "materializer_serial", serial, primary, seqs)
    voided = voided_event_ids(records, primary)
    basis_extra = sorted(voided) if voided else []
    decom = [e for e in events if e.get("event_kind") == "materializer_decommissioned"]
    if decom:
        return "retired", [primary(e) for e in decom] + basis_extra
    supers = [e for e in events if e.get("event_kind") == "materializer_superseded"]
    if supers:
        return "superseded", [primary(e) for e in supers] + basis_extra
    versions = [r for r in records
                if r.get("record_type") == "materializer_version"
                and r.get("materializer_serial") == serial]
    if versions:
        return "active", [primary(v) for v in versions]
    return "unknown", []


FOLDS = {
    ("entity", "current_status"):
        lambda recs, rec, primary, seqs: entity_current_status(recs, primary(rec), primary, seqs),
    ("entity_binding", "status"):
        lambda recs, rec, primary, seqs: binding_status(recs, primary(rec), primary, seqs),
    ("identity_relation", "verification_standing"):
        lambda recs, rec, primary, seqs: verification_standing(recs, "identity_relation",
                                                               primary(rec), primary, seqs),
    ("bridge_assertion", "verification_standing"):
        lambda recs, rec, primary, seqs: verification_standing(recs, "bridge_assertion",
                                                               primary(rec), primary, seqs),
    ("materializer", "current_status"):
        lambda recs, rec, primary, seqs: materializer_current_status(recs, primary(rec),
                                                                     primary, seqs),
}


def check_authored_vs_derived(records, batch_records, primary, seqs, reject):
    """An AUTHORED value on a derivable axis that disagrees with the fold is REJECTED.

    Only fires on a value the writer actually authored: an absent field authors nothing, and
    refusing that would be inventing a requirement the contract does not carry here.
    """
    for rec in batch_records:
        rtype = rec.get("record_type")
        axis = DERIVABLE_AXES.get(rtype)
        if not axis or rec.get(axis) is None:
            continue
        fold = FOLDS.get((rtype, axis))
        if fold is None:
            continue
        derived, basis = fold(records, rec, primary, seqs)
        if derived is not None and rec.get(axis) != derived:
            reject("L-05-%s.%s-authored-vs-derived" % (rtype, axis),
                   "%s authors %s=%r but the fold over the admitted records derives %r "
                   "(basis: %s). Authoritative records stay `authored`; an authored value that "
                   "DISAGREES with its fold is refused (sec 2, sec 3 row 5, sec 4)"
                   % (primary(rec), axis, rec.get(axis), derived, ", ".join(basis) or "none"))
