"""Controls for proof-of-spec-check's CELL_ID_RE -- one positive + one negative per anchored branch.

Added 2026-08-30 with the L3W3 hex-slug and CARD-R branches (0.8.0_AE_CloudComp~Y 84774 measured
21 of 34 certified L3W3 cells invisible to the letters-only slug branch). The negatives are shaped
like their positives so a widening that admits them fails here, not at a certifier.
"""
import importlib.util
import pathlib

_SRC = pathlib.Path(__file__).resolve().parent.parent / "proof-of-spec-check.py"
_spec = importlib.util.spec_from_file_location("posc", _SRC)
posc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(posc)
RE = posc.CELL_ID_RE


def _hit(s):
    return RE.search(s) is not None


def test_legacy_letters_slug_still_matches():
    assert _hit("L3W1-ncyj-1")
    assert _hit("L3W2-xkbc-4")
    assert _hit("L3W3-fadd-2")
    assert _hit("L3W3-m-9")


def test_l3w3_hex_slug_branch():
    for s in ("L3W3-dc02-1", "L3W3-b8a2-7", "L3W3-c69f-5"):
        assert _hit(s), s
    # negatives shaped like the positives: uppercase hex, 3-char slug, non-hex letters, no index
    for s in ("L3W3-DC02-1", "L3W3-dc0-1", "L3W3-zz02-1", "L3W3-dc02-"):
        assert not _hit(s), s


def test_card_r_branch():
    for s in ("CARD-R-0961-1", "CARD-R-f9fa-3", "CARD-R-b7dd-4", "CARD-R-m-5"):
        assert _hit(s), s
    # NOTE: a 1-4 LETTER slug such as "zz" is matched by the LEGACY branch via the "R-zz-99"
    # substring (prefix R) -- that is the pre-existing letters-only class, not this branch, so
    # the negatives here are shaped to fail BOTH: 5-char slug, no index, uppercase m, wrong prefix.
    for s in ("CARD-R-09611-1", "CARD-R-0961", "CARD-R-M-5", "CARD-Q-0961-1"):
        assert not _hit(s), s


def test_ingest_negative_control_stays_excluded():
    assert _hit("INGEST-T1-3")
    assert not _hit("INGEST-ZZ-99")


if __name__ == "__main__":
    import sys
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS", name)
            except AssertionError as e:
                fails += 1
                print("FAIL", name, e)
    print("cell-id-re controls: %d failed" % fails)
    sys.exit(1 if fails else 0)


def test_l3s7b_hex_slug_branch():
    # 2026-08-30 (1.0.0_SA_CTO~X): the sec-7b rectangle's ids. Before this branch, L3S7B-1c16-1 was
    # INVISIBLE to the harvest (slug opens with a digit -> letters-only branch fails; L3W3 branch is
    # prefix-anchored) while L3S7B-m-7 matched via the legacy branch -- so a face's <owned_cells>
    # would have harvested the issuer's mechanism cells and none of the lane cells.
    for s in ("L3S7B-1c16-1", "L3S7B-4017-3", "L3S7B-0b5f-2", "L3S7B-4565-1", "L3S7B-8304-4", "L3S7B-m-7"):
        assert _hit(s), s
    # negatives shaped like the positives: uppercase hex, 3-char slug, non-hex letters, no index, wrong prefix
    for s in ("L3S7B-1C16-1", "L3S7B-1c1-1", "L3S7B-zz16-1", "L3S7B-1c16-", "L3S7A-1c16-1"):
        assert not _hit(s), s
