"""Row 1 -- global serial uniqueness across batches AND fabrics (design sec 3 row 1).

The reject is "a mint for a serial already minted (ANY fabric)". The accept siblings prove the rule
is not "reject everything": two DISTINCT serials admit, and the cross-fabric case has a legal path --
the second fabric mints a `provisional` serial of its OWN and reconciles by relation, which is a
different act from re-minting the first one.
"""
from . import arm
from . import fixtures as fx


@arm("L-01-dup-serial-cross-batch")
def dup_serial_cross_batch(store):
    fx.bootstrap(store, "ent:alpha", receipt="mr:1")
    store.admit([fx.mint_receipt("mr:2", "ent:alpha")])          # a SECOND mint, later batch


@arm("L-01-dup-serial-cross-fabric")
def dup_serial_cross_fabric(store):
    fx.bootstrap(store, "ent:alpha", receipt="mr:1", origin_fabric_id="fabric-a")
    fx.open_authority(store, fx.CTO, actor=fx.CTO)
    store.admit([fx.mint_receipt("mr:2", "ent:alpha", authority=fx.CTO)])


@arm("L-01-distinct-serials-accepted")
def distinct_serials(store):
    fx.bootstrap(store, "ent:alpha", receipt="mr:1")
    fx.bootstrap(store, "ent:beta", receipt="mr:2")


@arm("L-01-provisional-pair-reconciled-accepted")
def provisional_pair_reconciled(store):
    """The legal cross-fabric path: a provisional serial of its own, canonicalized to the first."""
    fx.bootstrap(store, "ent:alpha", receipt="mr:1", origin_fabric_id="fabric-a")
    fx.bootstrap(store, "ent:alpha-prov", receipt="mr:2", origin_fabric_id="fabric-b",
                 provisional=True, canonicalized_as="ent:alpha")
