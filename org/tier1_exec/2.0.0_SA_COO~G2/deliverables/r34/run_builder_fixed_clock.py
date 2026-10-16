"""CONTROL runner (not a release artifact): runs the recovered builder at its own path with the build clock
held to a given UTC instant, so that the only non-content field (provenance.generated_at) is isolated.

usage: python -I run_builder_fixed_clock.py <builder path> <ISO UTC instant> -- <builder args...>
ASCII only.
"""
import datetime as dt
import runpy
import sys

builder = sys.argv[1]
instant = sys.argv[2]
assert sys.argv[3] == "--"
rest = sys.argv[4:]

FIXED = dt.datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)


class FixedDT(dt.datetime):
    @classmethod
    def now(cls, tz=None):
        return FIXED.astimezone(tz) if tz else FIXED.replace(tzinfo=None)


dt.datetime = FixedDT
sys.argv = [builder] + rest
runpy.run_path(builder, run_name="__main__")
