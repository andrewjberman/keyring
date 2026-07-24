"""comp-residue tests -- the controls run as a SUITE, not as one-off shell runs.

MUTANT DISCIPLINE: a detector that has only ever been seen to FIRE has not been tested.
Every assertion here that expects residue has a paired assertion proving the SAME code path
can come back CLEAN, and vice versa. If any single test can be deleted without another
reddening, that test was decoration.
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import residue_cli as R  # noqa: E402


class SurfaceStructureVsData(unittest.TestCase):
    """The structure-vs-data law: dict keys are AXES, list members are ROWS."""

    def test_dict_keys_are_structure(self):
        paths = R.surface({"a": {"b": 1}})
        self.assertIn("a", paths)
        self.assertIn("a.b", paths)

    def test_list_MEMBERS_are_not_structure(self):
        """Adding rows must NOT read as a new axis -- that is Route A, not residue."""
        one = R.surface({"roles": [{"name": "x"}]})
        two = R.surface({"roles": [{"name": "x"}, {"name": "y"}, {"name": "z"}]})
        self.assertEqual(one, two, "new LIST MEMBERS changed the surface -- rows misread as axes")

    def test_list_ROW_SCHEMA_is_structure(self):
        """A new FIELD on existing rows IS a new axis and must surface."""
        before = R.surface({"roles": [{"name": "x"}]})
        after = R.surface({"roles": [{"name": "x", "grain": "c0"}]})
        self.assertNotIn("roles[].grain", before)
        self.assertIn("roles[].grain", after, "a new row FIELD did not register as an axis")


class ResidueTiers(unittest.TestCase):
    """Three tiers, and prose is never traversal."""

    def test_code_mention_covers(self):
        unref, doc_only = R.residue({"alpha"}, code_blob="alpha", doc_blob="")
        self.assertEqual(unref, [])
        self.assertEqual(doc_only, [])

    def test_doc_only_is_NOT_covered(self):
        """THE CONTAMINATION GUARD: a doc ABOUT a missing axis must not close it."""
        unref, doc_only = R.residue({"dynamic_rails"}, code_blob="", doc_blob="dynamic_rails")
        self.assertEqual(unref, [], "doc mention should classify as doc_only, not unreferenced")
        self.assertEqual(doc_only, ["dynamic_rails"], "prose was counted as traversal")

    def test_unreferenced_when_nothing_mentions(self):
        unref, doc_only = R.residue({"dynamic_rails"}, code_blob="", doc_blob="")
        self.assertEqual(unref, ["dynamic_rails"])
        self.assertEqual(doc_only, [])

    def test_MUTANT_removing_the_code_mention_reddens(self):
        """The detector must MOVE a path into residue when its code reference disappears."""
        clean, _ = R.residue({"alpha"}, code_blob="alpha", doc_blob="")
        self.assertEqual(clean, [], "control: with the mention present there must be NO residue")
        mutated, _ = R.residue({"alpha"}, code_blob="", doc_blob="")
        self.assertEqual(mutated, ["alpha"], "MUTANT FAILED: removing the mention did not redden")


class Materiality(unittest.TestCase):
    def test_orphan_axis_vs_member(self):
        unref = ["roles.Consumer", "dynamic_rails", "dynamic_rails.D1"]
        orphans, members = R.classify_residue(unref)
        self.assertIn("dynamic_rails", orphans)
        self.assertIn("dynamic_rails.D1", orphans, "child of an orphan axis is itself orphan")
        self.assertIn("roles.Consumer", members, "`roles` is referenced, so its leaf is a MEMBER")


class ExitContract(unittest.TestCase):
    """REFUSE is a COVERAGE refusal -- nothing compared, nothing concluded. Never a PASS."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.src = os.path.join(self.tmp, "src.yaml")
        with open(self.src, "w", encoding="utf-8") as fh:
            fh.write("meta:\n  version: '9.9'\nalpha:\n  beta: 1\n")

    def test_missing_source_REFUSES_not_passes(self):
        rc = R.main(["check", os.path.join(self.tmp, "nope.yaml"), "--consumers", self.tmp])
        self.assertEqual(rc, R.RC_REFUSE)

    def test_unresolvable_consumers_REFUSE(self):
        rc = R.main(["check", self.src, "--consumers", os.path.join(self.tmp, "no_such_dir")])
        self.assertEqual(rc, R.RC_REFUSE)

    def test_head_is_read(self):
        obj, err = R.load_source(self.src)
        self.assertIsNone(err)
        self.assertEqual(R.read_head(obj, "meta.version"), "9.9")

    def test_positive_and_negative_control_pair(self):
        """Both directions on the REAL cli path, in one place, so neither can rot alone."""
        covering = os.path.join(self.tmp, "covering.py")
        with open(covering, "w", encoding="utf-8") as fh:
            fh.write("meta version alpha beta\n")
        self.assertEqual(R.main(["check", self.src, "--consumers", covering]), R.RC_PASS,
                         "POSITIVE CONTROL FAILED: the tool cannot return clean")
        blind = os.path.join(self.tmp, "blind.py")
        with open(blind, "w", encoding="utf-8") as fh:
            fh.write("nothing relevant\n")
        self.assertEqual(R.main(["check", self.src, "--consumers", blind]), R.RC_VERDICT,
                         "NEGATIVE CONTROL FAILED: the tool cannot fire")


if __name__ == "__main__":
    unittest.main(verbosity=2)
