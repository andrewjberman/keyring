#!/usr/bin/env python
"""Row 13 -- cross-record contest integrity: the three limit-11 promises as REJECTED WRITES.

THE WHOLE POINT OF THIS ROW IS THAT THESE ARE WRITES, NOT PROJECTION STATES (R3-CRO-25 / R3-CVO-9).
"An upheld contest needs a consequence on the same target dated after"; "a resolved needs an
opened"; "superseded_by freezes standing" -- the contract can state these and cannot enforce them,
so a reader has to trust that nobody wrote the impossible. Here the impossible is refused at the
write, which is the difference between a promise and a plane.

ORDER IS `(occurred_at, commit_seq, id)` -- the same total order the machines use. A same-instant
pair is decided by the id (R4-CRO-5), which is why `L-13-same-instant-pair-ordered-by-id-accepted`
exists: without the id, an opened and its resolution sharing a timestamp would be unorderable and
the ledger would have to refuse a legal pair.

`dismissed` AND `merged` CONSUME NO CORRECTIVE SLOT (R4-CVO-4). A dismissal followed by a new
challenge is legal; a merge's survivor resolves later on the same target. Only `upheld` and
`nullified` are corrective, and only ONE of them may ever land on a given event target -- two would
make the fold ambiguous about which correction is in force.
"""
from .machines import order_key

ID_PREFIXES = ("ent:", "mat:", "matv:", "run:", "sf:", "sv:", "bind:", "ct:", "ctev:", "rel:",
               "br:", "obs:", "mr:", "mig:", "ce:", "lce:", "aep:", "bev:")
CORRECTIVE = ("upheld", "nullified")
EVENT_TARGET_KINDS = ("lifecycle_event", "binding_event", "authority_epoch_event")
CARRIER_KEY = {"lifecycle_event": "materializer_serial", "binding_event": "binding_id",
               "authority_epoch_event": "authority_id"}
TARGET_FIELDS = ("target_entity_serial", "target_binding_id", "target_event_id")


def _typed_target(rec):
    return (rec.get("target_kind"),
            tuple(rec.get(f) for f in TARGET_FIELDS))


def check_contests(records, batch_records, primary, seqs, reject):
    contests = [r for r in records if r.get("record_type") == "contest_event"]
    by_id = dict((primary(r), r) for r in records)
    opened = {}
    resolved = {}
    for rec in contests:
        cid = rec.get("contest_id")
        if rec.get("event_kind") == "opened":
            if cid in opened:
                reject("L-13-duplicate-opened",
                       "contest %s is opened twice (%s, %s): one contest, one opening "
                       "(sec 3 row 13)" % (cid, primary(opened[cid]), primary(rec)))
            opened[cid] = rec
        elif rec.get("event_kind") == "resolved":
            if cid in resolved:
                reject("L-13-duplicate-resolved",
                       "contest %s is resolved twice (%s, %s): two admitted resolutions with "
                       "different outcomes make the fold ambiguous (sec 3 row 13)"
                       % (cid, primary(resolved[cid]), primary(rec)))
            resolved[cid] = rec

    for rec in [r for r in batch_records if r.get("record_type") == "contest_event"]:
        cid = rec.get("contest_id")
        if rec.get("event_kind") == "opened":
            _check_opened(rec, records, by_id, primary, seqs, reject)
            continue
        open_ev = opened.get(cid)
        if open_ev is None:
            reject("L-13-resolved-without-opened",
                   "contest %s is resolved with no admitted `opened` in (store U batch): a "
                   "resolution of nothing (sec 3 row 13)" % cid)
        if _typed_target(rec) != _typed_target(open_ev):
            reject("L-13-resolved-target-differs",
                   "contest %s resolves against %r but was opened against %r (sec 3 row 13)"
                   % (cid, _typed_target(rec), _typed_target(open_ev)))
        if order_key(rec, seqs, primary) <= order_key(open_ev, seqs, primary):
            reject("L-13-resolved-before-opened-rejected",
                   "contest %s resolves at or before its own opening under "
                   "(occurred_at, commit_seq, id) (sec 3 row 13, R4-CRO-5)" % cid)
        outcome = rec.get("outcome")
        if outcome == "merged":
            _check_merge(rec, open_ev, opened, resolved, contests, primary, seqs, reject)
        if outcome == "nullified":
            _check_nullified(rec, reject)
        if outcome == "upheld":
            _check_upheld(rec, open_ev, records, by_id, primary, reject)
        if outcome in CORRECTIVE:
            _check_single_corrective(rec, contests, primary, reject)


def _check_opened(rec, records, by_id, primary, seqs, reject):
    """An opening against an EVENT must be ordered after the event it challenges."""
    if rec.get("target_kind") not in EVENT_TARGET_KINDS:
        return
    target = by_id.get(rec.get("target_event_id"))
    if target is None:
        return
    if order_key(rec, seqs, primary) <= order_key(target, seqs, primary):
        reject("L-13-opened-before-target-event-rejected",
               "contest %s challenges event %s but is not ordered AFTER it: a challenge that "
               "precedes what it challenges is not a challenge (sec 3 row 13)"
               % (rec.get("contest_id"), primary(target)))


def _check_nullified(rec, reject):
    """VOID is for EVENTS only, and it names nothing (R4-CRO-7)."""
    if rec.get("target_kind") not in EVENT_TARGET_KINDS:
        reject("L-13-nullified-on-non-event-rejected",
               "contest %s nullifies a %r target; nullification voids an EVENT, and an entity or "
               "a binding is not an event (sec 3 row 13, R4-CRO-7)"
               % (rec.get("contest_id"), rec.get("target_kind")))
    if rec.get("consequence_refs") or rec.get("surviving_contest_id"):
        reject("L-13-nullified-with-consequence-rejected",
               "contest %s nullifies AND names a consequence or a survivor; a nullification has "
               "no replacement -- that is the whole difference from `upheld` (R4-CRO-7)"
               % rec.get("contest_id"))


def _check_upheld(rec, open_ev, records, by_id, primary, reject):
    refs = rec.get("consequence_refs") or []
    opening_at = (open_ev or {}).get("occurred_at") or ""
    for ref in refs:
        if not str(ref).startswith(ID_PREFIXES):
            reject("L-13-consequence-unparsable",
                   "contest %s names consequence %r, which parses as no record id (sec 3 row 13)"
                   % (rec.get("contest_id"), ref))
        target = by_id.get(ref)
        if target is None:
            reject("L-13-consequence-unresolved",
                   "contest %s names consequence %s, which resolves to nothing in "
                   "(store U batch) (sec 3 row 13)" % (rec.get("contest_id"), ref))
        if (target.get("occurred_at") or "") <= opening_at:
            reject("L-13-consequence-predates-opening",
                   "contest %s names consequence %s dated %s, at or before the opening at %s: a "
                   "consequence that predates its cause (sec 3 row 13)"
                   % (rec.get("contest_id"), ref, target.get("occurred_at"), opening_at))

    if rec.get("target_kind") in EVENT_TARGET_KINDS:
        voided = by_id.get(rec.get("target_event_id")) or {}
        if len(refs) != 1:
            reject("L-13-event-upheld-without-single-replacement-rejected",
                   "contest %s upholds against event %s with %d consequence(s); an event "
                   "correction is EXACTLY ONE replacement (sec 3 row 13, round-4 item 8)"
                   % (rec.get("contest_id"), rec.get("target_event_id"), len(refs)))
        replacement = by_id.get(refs[0]) or {}
        key_field = CARRIER_KEY.get(rec.get("target_kind"))
        if replacement.get("event_kind") != voided.get("event_kind") or \
                (key_field and replacement.get(key_field) != voided.get(key_field)):
            reject("L-13-event-replacement-kind-or-key-differs-rejected",
                   "contest %s replaces %s (%s on %s) with %s (%s on %s): a replacement carries "
                   "the SAME event_kind and the SAME carrier key, or it is a different event "
                   "wearing the correction (sec 3 row 13)"
                   % (rec.get("contest_id"), rec.get("target_event_id"),
                      voided.get("event_kind"), voided.get(key_field),
                      refs[0], replacement.get("event_kind"), replacement.get(key_field)))
    else:
        for ref in refs:
            target = by_id.get(ref) or {}
            if _target_mismatch(rec, target):
                reject("L-13-consequence-wrong-target",
                       "contest %s upholds against %r but names consequence %s, which acts on a "
                       "different typed target (sec 3 row 13)"
                       % (rec.get("contest_id"), _typed_target(rec), ref))


def _target_mismatch(contest, consequence):
    kind = contest.get("target_kind")
    if kind == "entity":
        subject = consequence.get("subject_serial") or consequence.get("entity_serial")
        return subject is not None and subject != contest.get("target_entity_serial")
    if kind == "binding":
        key = consequence.get("binding_id")
        return key is not None and key != contest.get("target_binding_id")
    return False


def _check_single_corrective(rec, contests, primary, reject):
    """One corrective outcome per event target. `dismissed`/`merged` consume no slot."""
    if rec.get("target_kind") not in EVENT_TARGET_KINDS:
        return
    target = rec.get("target_event_id")
    others = [c for c in contests
              if c.get("event_kind") == "resolved"
              and c.get("outcome") in CORRECTIVE
              and c.get("target_event_id") == target
              and primary(c) != primary(rec)]
    if others:
        reject("L-13-second-corrective-outcome-rejected",
               "event %s already carries the corrective outcome %s (%s); a second would make the "
               "fold ambiguous about which correction is in force. `dismissed` and `merged` "
               "consume no slot (sec 3 row 13, R4-CVO-4)"
               % (target, others[0].get("outcome"), primary(others[0])))


def _check_merge(rec, open_ev, opened, resolved, contests, primary, seqs, reject):
    """Survivor continuity (R3-CRO-35): the absorbing contest must be LIVE, on the SAME target."""
    survivor_id = rec.get("surviving_contest_id")
    cid = rec.get("contest_id")
    if survivor_id == cid:
        reject("L-13-merged-into-self",
               "contest %s merges into itself, which leaves no survivor (sec 3 row 13)" % cid)
    survivor = opened.get(survivor_id) or next(
        (c for c in contests if primary(c) == survivor_id and c.get("event_kind") == "opened"),
        None)
    if survivor is None:
        reject("L-13-merged-into-unopened",
               "contest %s merges into %r, which is not an admitted `opened` contest "
               "(sec 3 row 13)" % (cid, survivor_id))
    if _typed_target(survivor) != _typed_target(rec):
        reject("L-13-merged-cross-target-rejected",
               "contest %s merges into %s, which contests a DIFFERENT typed target: an absorbing "
               "contest must be about the same thing (R3-CRO-35)" % (cid, survivor_id))
    if survivor.get("contest_id") in resolved:
        reject("L-13-merged-into-resolved-rejected",
               "contest %s merges into %s, whose own resolution is already admitted: the absorber "
               "must be LIVE (R3-CRO-35)" % (cid, survivor_id))
    edges = {}
    for c in contests:
        if c.get("event_kind") == "resolved" and c.get("outcome") == "merged":
            edges[c.get("contest_id")] = c.get("surviving_contest_id")
    edges[cid] = survivor_id
    seen, node = set(), cid
    while node in edges:
        if node in seen:
            reject("L-13-merge-cycle-rejected",
                   "the merge edge %s -> %s closes a cycle in the merge graph: A into B and B into "
                   "A leaves NO survivor (R3-CRO-35)" % (cid, survivor_id))
            break
        seen.add(node)
        node = edges[node]
