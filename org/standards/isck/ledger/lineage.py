#!/usr/bin/env python
"""Row 7 -- relation direction, cycle AND fork rejection on every chain, and the lifecycle machine.

WHY THESE FAILURES NEED THEIR OWN RULES: every one of them RESOLVES EVERY REFERENCE and dangles
nothing. The atomic batch {A supersedes B, B supersedes A} is internally consistent, forks nothing,
and has ZERO heads. Two roots for one materializer resolve everything, fork nothing, and are BOTH
heads. A referential-integrity checker passes all of them cleanly. What they break is the question
"which one is current?" -- and that question has no answer, rather than a wrong one, which is why
it has to be refused at the write.

DECOMMISSION IS TERMINAL (R4-CRO-4). `superseded -> decommissioned` is legal; anything ordered after
a decommission is not. A voided event advances nothing, and its replacement is admitted ONLY as an
upheld contest's consequence -- otherwise "correcting" an event would just be appending a second one.
"""
from .machines import _seq, effective, order_key, voided_event_ids

CYCLE_RELATION_TYPES = ("canonicalized_as", "merged_into", "successor_of", "replaces")
LIFECYCLE_DECOMMISSION = "materializer_decommissioned"
LIFECYCLE_SUPERSEDED = "materializer_superseded"


def cycle_edge(edges):
    """The edge that CLOSES a cycle, or None. Iterative DFS -- three-colour, over (from, to)."""
    graph = {}
    for src, dst, rec in edges:
        graph.setdefault(src, []).append((dst, rec))
    colour = {}
    for start in list(graph):
        if colour.get(start):
            continue
        colour[start] = 1
        stack = [(start, iter(graph.get(start, [])))]
        while stack:
            node, it = stack[-1]
            advanced = False
            for dst, rec in it:
                if colour.get(dst) == 1:
                    return rec
                if colour.get(dst) is None:
                    colour[dst] = 1
                    stack.append((dst, iter(graph.get(dst, []))))
                    advanced = True
                    break
            if not advanced:
                colour[node] = 2
                stack.pop()
    return None


def check_relations(records, relation_types, reject):
    """Legal direction rows only, and NO cycle in any identity chain.

    The cycle search runs over the UNION of the four cycle-bearing relation types, not one graph
    per type: a canonicalization that reaches back through a merge is still a cycle, and per-type
    graphs would each read acyclic while the estate has no canonical answer for anybody. The arm is
    named by the relation_type of the edge that CLOSES the cycle -- the edge a reader would remove.
    """
    edges = []
    for rec in records:
        if rec.get("record_type") != "identity_relation":
            continue
        rtype = rec.get("relation_type")
        if rtype not in relation_types:
            reject("L-07-unknown-kind",
                   "identity_relation %s carries relation_type %r, which is not one of the %d "
                   "legal direction rows (sec 3 row 7)"
                   % (rec.get("relation_id"), rtype, len(relation_types)))
        if rtype in CYCLE_RELATION_TYPES and rec.get("object_serial"):
            edges.append((rec.get("subject_serial"), rec.get("object_serial"), rec))
    closing = cycle_edge(edges)
    if closing is not None:
        rule = ("L-07-cycle-merge" if closing.get("relation_type") == "merged_into"
                else "L-07-cycle-canonicalize")
        reject(rule,
               "identity_relation %s closes a cycle over %s: an estate whose identity graph has a "
               "cycle has no canonical answer for any member of it (sec 3 row 7)"
               % (closing.get("relation_id"), "/".join(CYCLE_RELATION_TYPES)))


def check_supersedes(records, record_type, key_field, primary, reject, rules):
    """A supersedes chain is LINEAR: one root, no fork, no cycle, no cross-lineage."""
    rows = [r for r in records if r.get("record_type") == record_type]
    by_id = dict((primary(r), r) for r in rows)
    seen_target = {}
    for rec in sorted(rows, key=primary):
        target = rec.get("supersedes")
        if not target:
            continue
        if key_field and target in by_id:
            mine, theirs = rec.get(key_field), by_id[target].get(key_field)
            if mine != theirs:
                reject(rules["cross"],
                       "%s supersedes %s, which belongs to %r not %r -- lineage contamination "
                       "(sec 3 row 7)" % (primary(rec), target, theirs, mine))
        if target in seen_target:
            reject(rules["fork"],
                   "%s and %s both supersede %s: two successors of one prior are two heads, and "
                   "'which is current' stops having an answer (sec 3 row 7)"
                   % (seen_target[target], primary(rec), target))
        seen_target[target] = primary(rec)
    closing = cycle_edge([(primary(r), r.get("supersedes"), r) for r in rows
                          if r.get("supersedes")])
    if closing is not None:
        reject(rules["cycle"],
               "%s closes a cycle in the supersedes chain: every reference resolves, nothing "
               "forks, and the chain has ZERO heads (sec 3 row 7)" % primary(closing))
    if key_field and "second_root" in rules:
        roots = {}
        for rec in sorted(rows, key=primary):
            if rec.get("supersedes"):
                continue
            key = rec.get(key_field)
            if key in roots:
                reject(rules["second_root"],
                       "%s and %s are both roots for %s: two roots resolve everything, fork "
                       "nothing, and are both heads (R3-CRO-29, sec 3 row 7)"
                       % (roots[key], primary(rec), key))
            roots[key] = primary(rec)


def check_lifecycle_machine(records, batch_records, primary, seqs, reject):
    """The materializer lifecycle machine, over EFFECTIVE events. Decommission is TERMINAL."""
    voided = voided_event_ids(records, primary)
    consequences = set()
    for rec in records:
        if rec.get("record_type") == "contest_event" and rec.get("outcome") == "upheld":
            consequences.update(rec.get("consequence_refs") or [])

    for rec in batch_records:
        if rec.get("record_type") != "lifecycle_event":
            continue
        twin = [r for r in records
                if r.get("record_type") == "lifecycle_event"
                and primary(r) in voided
                and r.get("event_kind") == rec.get("event_kind")
                and r.get("materializer_serial") == rec.get("materializer_serial")]
        if twin and primary(rec) not in consequences:
            reject("L-07-replacement-without-upheld-contest-rejected",
                   "lifecycle event %s stands in for the voided %s but no upheld contest names it "
                   "in consequence_refs; a replacement is admitted ONLY as that consequence, or "
                   "'correcting' an event is just appending another one (sec 3 row 7)"
                   % (primary(rec), primary(twin[0])))

    serials = {r.get("materializer_serial") for r in records
               if r.get("record_type") == "lifecycle_event"}
    for serial in sorted(s for s in serials if s):
        events = effective(records, "lifecycle_event", "materializer_serial", serial,
                           primary, seqs)
        decoms = [e for e in events if e.get("event_kind") == LIFECYCLE_DECOMMISSION]
        supers = [e for e in events if e.get("event_kind") == LIFECYCLE_SUPERSEDED]
        if len(supers) > 1:
            same_batch = len({_seq(e, seqs) for e in supers}) == 1
            reject("L-07-two-effective-successors-same-batch-rejected" if same_batch
                   else "L-07-second-process-supersession-rejected",
                   "materializer %s has %d effective `materializer_superseded` events%s "
                   "(sec 3 row 7)"
                   % (serial, len(supers),
                      " in ONE batch -- a same-batch race, which arrival order cannot adjudicate"
                      if same_batch else ""))
        if len(decoms) > 1:
            reject("L-07-second-decommission-rejected",
                   "materializer %s has %d effective decommissions; decommission is TERMINAL "
                   "(sec 3 row 7, R4-CRO-4)" % (serial, len(decoms)))
        if decoms:
            after = [e for e in events
                     if order_key(e, seqs, primary) > order_key(decoms[0], seqs, primary)]
            if after:
                reject("L-07-transition-after-decommission-rejected",
                       "materializer %s has %d effective lifecycle event(s) ordered after its "
                       "decommission; decommission is TERMINAL (sec 3 row 7)"
                       % (serial, len(after)))
