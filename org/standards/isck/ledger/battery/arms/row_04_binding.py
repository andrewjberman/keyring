"""Row 4 -- bindings open and close BY EVENT, one machine per `binding_id`.

The four accept arms carry the discriminating weight. "Reject a second open" and "reject every
second event" are the same picture without `L-04-close-event-accepted`; and the whole point of
refusing the forbidden re-open is that there IS a legal way to re-open -- a NEW binding_id --
which `L-04-reopen-as-new-binding-accepted` proves. A machine that only ever says no would pass
all five reject arms.

`L-04-voided-close-then-replacement-accepted` is the one that reaches across rows: a close that is
voided by an upheld contest does NOT count, and the contest's single replacement event takes its
position. It is cited by rows 4 AND 13 in the design and is ONE arm -- one test discharging two
responsibilities.
"""
from . import arm
from . import fixtures as fx

BINDING = "bind:1"


def _binding_row(binding_id=BINDING, **extra):
    rec = {"record_type": "entity_binding", "binding_id": binding_id,
           "entity_serial": "ent:alpha", "valid_from": "2026-01-01T00:00:00Z"}
    rec.update(extra)
    return rec


def _event(event_id, kind, binding_id=BINDING, occurred_at="2026-02-01T00:00:00Z"):
    return {"record_type": "binding_event", "event_id": event_id, "binding_id": binding_id,
            "event_kind": kind, "occurred_at": occurred_at}


def _seed(store):
    store.admit(fx.minted_pair("ent:alpha"))
    return store


@arm("L-04-open-accepted")
def open_accepted(store):
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])


@arm("L-04-close-event-accepted")
def close_event_accepted(store):
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_event("bev:2", "closed", occurred_at="2026-03-01T00:00:00Z")])


@arm("L-04-second-open-rejected")
def second_open(store):
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_event("bev:2", "opened", occurred_at="2026-03-01T00:00:00Z")])


@arm("L-04-second-close-rejected")
def second_close(store):
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_event("bev:2", "closed", occurred_at="2026-03-01T00:00:00Z")])
    store.admit([_event("bev:3", "closed", occurred_at="2026-04-01T00:00:00Z")])


@arm("L-04-open-after-close-rejected")
def open_after_close(store):
    """The forbidden re-open: same binding_id, an `opened` ordered after its `closed`."""
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_event("bev:2", "closed", occurred_at="2026-03-01T00:00:00Z")])
    store.admit([_event("bev:3", "opened", occurred_at="2026-04-01T00:00:00Z")])


@arm("L-04-reopen-as-new-binding-accepted")
def reopen_as_new_binding(store):
    """The LEGAL path the forbidden re-open exists to point at."""
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_event("bev:2", "closed", occurred_at="2026-03-01T00:00:00Z")])
    store.admit([_binding_row("bind:2", valid_from="2026-04-01T00:00:00Z"),
                 _event("bev:3", "opened", binding_id="bind:2",
                        occurred_at="2026-04-01T00:00:00Z")])


@arm("L-04-close-by-mutation")
def close_by_mutation(store):
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_binding_row(valid_to="2026-03-01T00:00:00Z")])       # the row, mutated


@arm("L-04-close-without-event")
def close_without_event(store):
    _seed(store)
    store.admit([_binding_row("bind:9", valid_to="2026-03-01T00:00:00Z"),
                 _event("bev:9", "opened", binding_id="bind:9")])


@arm("L-04-voided-close-then-replacement-accepted")
def voided_close_then_replacement(store):
    """An upheld contest voids the close; its ONE replacement event takes that position.

    Cited by rows 4 and 13 -- one test, two responsibilities. Without the voiding, this batch is
    exactly `L-04-second-close-rejected`; the ONLY difference is that bev:2 is voided, which is
    what makes it a real test of the VOIDED derivation rather than of the close rule.
    """
    _seed(store)
    store.admit([_binding_row(), _event("bev:1", "opened")])
    store.admit([_event("bev:2", "closed", occurred_at="2026-03-01T00:00:00Z")])
    store.admit([{"record_type": "contest_event", "event_id": "ctev:1", "contest_id": "ctev:1",
                  "event_kind": "opened", "target_kind": "binding_event",
                  "target_event_id": "bev:2", "occurred_at": "2026-03-02T00:00:00Z"}])
    store.admit([_event("bev:3", "closed", occurred_at="2026-03-05T00:00:00Z"),
                 {"record_type": "contest_event", "event_id": "ctev:2", "contest_id": "ctev:1",
                  "event_kind": "resolved", "outcome": "upheld", "target_kind": "binding_event",
                  "target_event_id": "bev:2", "consequence_refs": ["bev:3"],
                  "occurred_at": "2026-03-05T00:00:00Z"}])
