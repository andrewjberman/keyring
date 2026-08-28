"""Row 2 -- referential integrity for every reference in sec 2d (61 arms).

THESE ARMS ARE GENERATED FROM THE REFERENCE TABLE, NOT HAND-WRITTEN, and that is a correctness
decision rather than a convenience one. Sixty near-identical fixtures differing in one field is
precisely the shape where a transcription slip produces a GREEN arm: paste the wrong target class
into one of them and it still rejects, still passes, and now tests nothing. Generating them from
the same table the resolver reads means an arm cannot disagree with the policy it is testing --
and the reject arms below assert WHICH refusal they got, so an arm that rejects for the wrong
reason is an ERROR, never a pass.

THE SEED UNIVERSE IS ONE ATOMIC BATCH, which is the admission model proving itself: the seventeen
seed records reference each other in cycles (a run needs a version, a version needs a materializer,
a surface needs a run and a frontier), and no ordering of them could ever be written down. They
resolve because sec 2c validates the batch's FINAL STATE, not each insert. If admission were
per-record this file could not exist.

PER (record, field) PAIR, two arms and one difference between them:
  reject  the field points at an id that PARSES as a record id but was never admitted
  accept  the same record with the field pointing at the seed of its target class
Everything else -- every other reference on the record -- is identical and resolvable, so the arm
isolates ONE field. Without that, a reject arm passes because some OTHER field dangled, which is
branch-scoped rejection attribution: the verdict is right and the reason is wrong.
"""
from . import arm
from . import fixtures as fx

# One seed per record class. The prefix is the class's own id prefix (sec 2d's parse list).
SEED = {
    "entity": "ent:seed", "mint_receipt": "mr:seed", "entity_binding": "bind:seed",
    "identity_relation": "rel:seed", "contest_event": "ctev:seed", "materializer": "mat:seed",
    "materializer_version": "matv:seed", "materialization_run": "run:seed",
    "source_frontier": "sf:seed", "surface_version": "sv:seed", "state_observation": "obs:seed",
    "bridge_assertion": "br:seed", "coherence_evaluation": "ce:seed",
    "migration_receipt": "mig:seed", "lifecycle_event": "lce:seed", "binding_event": "bev:seed",
    "authority_epoch_event": "aep:seed",
}
DANGLING = dict((cls, sid.split(":")[0] + ":never-admitted") for cls, sid in SEED.items())
# A TERMINAL second seed per class. Without it a seed's SAME-CLASS reference points at itself --
# `matv:seed supersedes matv:seed` -- which resolved cleanly and dangled nothing until row 7 could
# see it, and then read as a supersedes cycle with zero heads. The seed chain is therefore
# seed -> seed2, and an ARM record points at `seed` (the HEAD), so it extends the chain instead of
# forking it. Every one of those three positions is load-bearing.
SEED2 = dict((cls, sid + "2") for cls, sid in SEED.items())


def _base(store, record_type, primary_value, same_class=None):
    """A minimally-admissible record of `record_type`: primary id plus EVERY sec 2d reference."""
    field = store.primary[record_type]
    rec = {"record_type": record_type, field: primary_value}
    for (rec_t, fld), _spec in sorted(store.refs.items()):
        if rec_t != record_type:
            continue
        cls = TARGETS.get((rec_t, fld), "entity")
        if cls == record_type:
            if same_class is None:
                continue                      # a TERMINAL seed carries no same-class reference
            value = same_class[cls]
        else:
            value = SEED[cls]
        if "[]." in fld:
            container, sub = fld.split("[].", 1)
            rec.setdefault(container, []).append({sub: value})
        elif fld.endswith("[]"):
            rec[fld[:-2]] = [value]
        else:
            rec[fld] = value
    from ledger import engine as _eng
    for field, values in sorted(_eng.enum_fields(record_type).items()):
        # A record built to test a REFERENCE must be legal in every OTHER respect, or its arm is
        # refused by whichever rule it violates instead. Enum fields take their first schema value
        # -- derived, so a contract change moves the fixtures with it rather than stranding them.
        rec.setdefault(field, values[0])
    if record_type in ("entity", "mint_receipt"):
        # row 6 -- an entity's mint facts must EQUAL its receipt's, so both sides of every
        # generated pair carry the SAME ones. Before this, a row-2 arm about a reference field
        # was being refused by L-06-minted-at-mismatch: the right verdict for the wrong rule.
        rec["minting_authority"] = fx.ROOT
        rec["minted_at"] = "2026-01-01T00:00:00Z"
    return rec


def _terminal(store, cls, sid):
    """The end of every same-class chain: legal, referenced, and referring to no sibling."""
    rec = _base(store, cls, sid)
    if cls == "mint_receipt":
        rec["entity_serial"] = SEED2["entity"]
    if cls == "authority_epoch_event":
        # a DISTINCT authority: two `opened` events on one authority are overlapping intervals,
        # which row 6 refuses -- the terminal seed exists to be referenced, not to re-open ROOT
        rec.update({"authority_id": "auth:terminal", "event_kind": "opened", "actor": fx.ROOT,
                    "occurred_at": "2019-01-01T00:00:00Z"})
    return rec


def build_universe(store):
    """Every seed record, admitted as ONE atomic batch -- the cycles resolve at final state."""
    batch = []
    for cls, sid in sorted(SEED2.items()):
        batch.append(_terminal(store, cls, sid))
    for cls, sid in sorted(SEED.items()):
        rec = _base(store, cls, sid, same_class=SEED2)
        if cls == "mint_receipt":
            rec["entity_serial"] = SEED["entity"]
            rec["minting_authority"] = fx.ROOT
            rec["minted_at"] = "2026-01-01T00:00:00Z"
        if cls == "entity":
            rec["minted_at"] = "2026-01-01T00:00:00Z"
            rec["minting_authority"] = fx.ROOT
        if cls == "authority_epoch_event":
            # the universe registers its own minting authority, in the SAME batch as the mint it
            # authorises -- sec 2c resolves the pair at final state, so no ordering is implied
            rec["authority_id"] = fx.ROOT
            rec["event_kind"] = "opened"
            rec["actor"] = fx.ROOT
            rec["occurred_at"] = "2020-01-01T00:00:00Z"
        batch.append(rec)
    store.admit(batch, actor=fx.ROOT)
    return store


# (record, field) -> target class, read from sec 2d at import time (never a typed list).
TARGETS = {}


def _load_targets():
    """Target classes come from the ENGINE's reading of sec 2d -- ONE parse, not two.

    An arm module that parsed the table itself would be a second instrument reading the same
    substrate: it would agree with the resolver about a row they both misread, and the pair would
    corroborate nothing. The arms consume exactly what the resolver enforces.
    """
    from ledger import engine as eng
    for key, spec in eng.reference_fields().items():
        classes = [c for c in spec["classes"] if c in SEED]
        TARGETS[key] = classes[0] if classes else "entity"


def _make_arms():
    from ledger import engine as eng
    _load_targets()
    for (record_type, field), spec in sorted(eng.reference_fields().items()):
        _register_pair(record_type, field, spec["policy"])


def _register_pair(record_type, field, policy):
    cls = TARGETS.get((record_type, field), "entity")
    rid = SEED[record_type].split(":")[0] + ":arm"
    expected = "L-02-unresolved-%s.%s" % (record_type, field)

    def _shape(store, value):
        """The arm's batch: the record under test, plus whatever OTHER rules require.

        An arm isolates ONE field, so every rule that is not row 2 must be satisfiable in the same
        batch -- otherwise the arm's verdict is right for the wrong reason. Two responsibilities
        reach in here, and both were found by running the arms rather than by reading them:
          row 6  an `entity` needs a mint_receipt in (store U batch), so an entity arm carries its
                 own receipt; without it every entity arm refused with L-06 and the attribution
                 control turned the reject arm into an ERROR instead of a false green.
          row 1  a serial may be minted ONCE, so a mint_receipt arm cannot point at the already
                 minted `ent:seed`. When the field RESOLVES it mints a fresh entity in the same
                 batch -- the sec 2c bootstrap pair, which is the legal shape.
        """
        rec = _base(store, record_type, rid, same_class=SEED)
        if "[]." in field:
            container, sub = field.split("[].", 1)
            rec[container] = [{sub: value}]
        elif field.endswith("[]"):
            rec[field[:-2]] = [value]
        else:
            rec[field] = value
        batch = [rec]
        if record_type == "entity":
            batch.append(fx.mint_receipt(SEED["mint_receipt"].split(":")[0] + ":arm-companion",
                                         rid))
        if record_type == "mint_receipt" and str(value).startswith("ent:") \
                and value != DANGLING["entity"]:
            rec[field] = "ent:arm-minted"
            batch.append(fx.entity("ent:arm-minted"))
        return batch

    @arm(expected)
    def unresolved(store, _v=DANGLING[cls]):
        build_universe(store)
        try:
            store.admit(_shape(store, _v))
        except Exception as exc:
            rule = getattr(exc, "rule", None)
            if rule != expected:
                raise AssertionError(
                    "rejected for the WRONG reason: expected %s, got %s -- a reject arm whose "
                    "refusal comes from another field is a green arm testing nothing"
                    % (expected, rule)) from exc
            raise

    @arm("L-02-resolved-%s.%s-accepted" % (record_type, field))
    def resolved(store, _v=SEED[cls]):
        build_universe(store)
        store.admit(_shape(store, _v))

    unresolved.__name__ = "unresolved_%s_%s" % (record_type, field)
    resolved.__name__ = "resolved_%s_%s" % (record_type, field)


@arm("L-02-opaque-migration-ref-accepted")
def opaque_migration_ref(store):
    """PARSE-STRICT: a value that does NOT parse as a record id is stored OPAQUE, not refused."""
    build_universe(store)
    rec = _base(store, "migration_receipt", "mig:arm")
    rec["migrated_record_ref"] = "legacy-system/row/8842"      # parses as no record id
    store.admit([rec])


_make_arms()
