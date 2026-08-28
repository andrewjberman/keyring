"""The arm registry: arm id -> the write-then-query that exercises it.

AN ARM IS A TEST WITH A DECLARED DIRECTION. A `reject` arm builds a batch the ledger MUST refuse;
an `accept` arm builds one it MUST admit. The runner compares the OBSERVED verdict against the
manifest's DECLARED kind -- never against the arm's own opinion of itself, which is why the kind
lives in the manifest (derived from the design) and not in the decorator.

NOTE: THE DECORATOR TAKES NO KIND, DELIBERATELY. If an arm declared its own direction, an arm written
to the implementation's behaviour would declare whatever that behaviour is and score itself green --
the transcribed-harness class (a harness transcribed from the implementation scores its own blind
spot as a pass). The direction comes from the design, through the census, through the manifest.

An arm function takes a fresh `store` and either returns (the ledger admitted everything it was
given) or raises `engine.Rejected` (the ledger refused). Anything else -- any other exception -- is
an ERROR, which is neither an accept nor a reject and is never silently folded into either.
"""

REGISTRY = {}


def arm(arm_id):
    """Register the implementation of one manifest arm id."""
    def deco(fn):
        if arm_id in REGISTRY:
            raise RuntimeError("arm %s registered twice -- two implementations, one id" % arm_id)
        REGISTRY[arm_id] = fn
        return fn
    return deco


def load_all():
    """Import every arm module so the registry is populated. Returns the registry."""
    from . import row_01_uniqueness      # noqa: F401
    from . import row_02_resolver        # noqa: F401
    from . import row_03_append_only     # noqa: F401
    from . import row_04_binding         # noqa: F401
    from . import row_05_folds           # noqa: F401
    from . import row_06_mint_epoch      # noqa: F401
    from . import row_07_lineage         # noqa: F401
    from . import rows_08_11_surfaces    # noqa: F401
    from . import row_13_contests        # noqa: F401
    from . import row_12_replay          # noqa: F401
    return REGISTRY
