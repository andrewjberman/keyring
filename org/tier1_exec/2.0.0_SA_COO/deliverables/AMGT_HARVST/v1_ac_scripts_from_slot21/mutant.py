"""MUTANT CONTROL for HVST-v-1: a passing assertion never mutated has never been tested.

Mutates the fix to a NO-OP (`_null_empty_mappings` -> identity) in the live module and re-runs the
new suite test's own body. The test must FAIL, and fail for the ORIGINAL reason (parquet refusing a
struct with no child field). Then restores the real function and re-runs to show it passes again.
"""
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

from lib.opal_data_harvest import silver_from_bronze as sfb  # noqa: E402
from lib.opal_data_harvest import test_silver_from_bronze as tsfb  # noqa: E402

TEST = tsfb.test_empty_mapping_in_a_listing_row_is_nulled_and_writes_for_every_publisher
real = sfb._null_empty_mappings


def run():
    try:
        TEST()
        return None
    except BaseException as exc:  # noqa: BLE001 -- the failure IS the measurement
        return exc


print("MUTANT CONTROL -- test: %s" % TEST.__name__)

sfb._null_empty_mappings = lambda value: value
print("mutation applied: _null_empty_mappings -> identity (the fix removed, nothing else touched)")
err = run()
if err is None:
    print("MUTANT RESULT: the test still PASSED -- DID-NOT-FIRE (the assertion tests nothing)")
else:
    print("MUTANT RESULT: FIRED -- %s: %s" % (type(err).__name__, str(err).splitlines()[0]))
    print("  last frame: %s" % traceback.format_tb(err.__traceback__)[-1].strip().replace("\n", " | "))

sfb._null_empty_mappings = real
print("mutation reverted")
err2 = run()
print("POST-REVERT: %s" % ("PASSED (the mutation, not the test, was the difference)" if err2 is None
                           else "STILL FAILING: %s" % err2))

print("mutant denominator: 1 mutation, 1 test, expected FIRED then PASSED")
print("VERDICT: %s" % ("FIRED-AS-EXPECTED" if err is not None and err2 is None else "CHECK"))
