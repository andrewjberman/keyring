"""Conformance suite for the boundary-report TYPE.

MUTANT DISCIPLINE: the type exists to make three specific silent failures LOUD. Each is
paired here -- a conformant control that MUST pass, and the mutant that MUST redden. A
validator that has only ever been seen to ACCEPT has not been tested.

The three the type was built for:
  1. N/A rendered as 0            -> BR003   (false denominator)
  2. method as free text          -> BR002   (unaggregatable within a month)
  3. address coerced across spaces-> BR006/BR008 (vocabulary poverty inside the type
                                     built to detect vocabulary poverty)
"""

from __future__ import annotations

import copy
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import boundary_report as B  # noqa: E402


def conformant():
    """A minimal VALID report. If this ever fails, the validator is over-strict."""
    return {
        "tool": "comp-residue",
        "source": "org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml",
        "address_space": "yaml_key_path",
        "head": "1.2",
        "surface_total": 111,
        "cells": {
            "covered": {"applicable": True, "count": 46, "method": "mention"},
            "member": {"applicable": True, "count": 28, "method": "mention"},
            "doc_only": {"applicable": True, "count": 21, "method": "mention"},
            "orphan": {"applicable": True, "count": 16, "method": "mention"},
        },
        "items": [
            {"address": "dynamic_rails.D1_value_grain", "cell": "orphan",
             "method": "mention", "evidence": "no code mention in 57 CODE consumers"},
        ],
    }


def codes(report):
    return sorted({v.code for v in B.validate(report)})


class PositiveControl(unittest.TestCase):
    """The validator MUST be able to accept. Otherwise it is not a validator."""

    def test_conformant_report_passes(self):
        self.assertEqual(B.validate(conformant()), [],
                         "POSITIVE CONTROL FAILED: a valid report was rejected")


class Q3_ApplicabilityIsNotZero(unittest.TestCase):
    """THE headline invariant: N/A and 0 are different values."""

    def test_MUTANT_na_rendered_as_zero_REDDENS(self):
        r = conformant()
        # a DAG has no prose plane -- the WRONG way to say so:
        r["cells"]["doc_only"] = {"applicable": False, "count": 0, "method": None}
        r["surface_total"] = 90
        self.assertIn("BR003", codes(r),
                      "MUTANT FAILED: N/A rendered as 0 was accepted -- false denominator")

    def test_the_RIGHT_way_to_say_not_applicable_passes(self):
        r = conformant()
        r["cells"]["doc_only"] = {"applicable": False, "count": None, "method": None}
        r["surface_total"] = 90  # 46 + 28 + 16, doc_only EXCLUDED from the accounting
        self.assertEqual(B.validate(r), [],
                         "a correctly-expressed N/A cell must be accepted")

    def test_could_not_measure_is_NOT_does_not_apply(self):
        """applicable=true + count=null is a DIFFERENT claim and must not pass silently."""
        r = conformant()
        r["cells"]["orphan"] = {"applicable": True, "count": None, "method": "mention"}
        self.assertIn("BR003", codes(r))

    def test_absent_applicable_is_not_false(self):
        r = conformant()
        del r["cells"]["orphan"]["applicable"]
        self.assertIn("BR003", codes(r), "absence must not default to false")

    def test_accounting_EXCLUDES_non_applicable_cells(self):
        """Summing an N/A cell into the denominator is the exact defect. Must not balance."""
        r = conformant()
        r["cells"]["doc_only"] = {"applicable": False, "count": None, "method": None}
        r["surface_total"] = 111  # still counting the 21 that are NOT applicable
        self.assertIn("BR004", codes(r))


class Q2_MethodIsAnEnum(unittest.TestCase):
    def test_MUTANT_free_text_method_REDDENS(self):
        r = conformant()
        r["cells"]["orphan"]["method"] = "we grepped the consumers for names"
        self.assertIn("BR002", codes(r),
                      "MUTANT FAILED: prose method accepted -- corpus becomes unaggregatable")

    def test_enum_member_passes(self):
        r = conformant()
        r["cells"]["orphan"]["method"] = "traversal"
        self.assertEqual(B.validate(r), [])

    def test_non_applicable_cell_must_not_carry_a_method(self):
        r = conformant()
        r["cells"]["doc_only"] = {"applicable": False, "count": None, "method": "mention"}
        r["surface_total"] = 90
        self.assertIn("BR002", codes(r))

    def test_failure_direction_is_carried_on_the_enum(self):
        """An aggregate must be able to state the BIAS of its own denominator."""
        self.assertTrue(B.METHODS["mention"]["under_reports"])
        self.assertFalse(B.METHODS["traversal"]["under_reports"])
        self.assertFalse(B.METHODS["traversal"]["over_reports"])
        self.assertTrue(B.METHODS["declared"]["over_reports"])


class Q1_AddressesAreNativeNeverCoerced(unittest.TestCase):
    def test_MUTANT_missing_address_space_REDDENS(self):
        r = conformant()
        del r["address_space"]
        self.assertIn("BR001", codes(r),
                      "MUTANT FAILED: a report without an address space claims false comparability")

    def test_unknown_address_space_is_ALLOWED_but_REPORTED(self):
        """A closed set here would be the frozen-enumeration defect. New shapes stay visible."""
        r = conformant()
        r["address_space"] = "some_new_shape_v1"
        self.assertIn("BR008", codes(r), "a new address space must be reported, not silent")

    def test_native_dag_address_passes_unchanged(self):
        r = conformant()
        r["address_space"] = "dag_node_id"
        r["items"] = [{"address": "lambda:inf-gold-trigger", "cell": "orphan", "method": "traversal"}]
        self.assertEqual(B.validate(r), [],
                         "a native DAG address must pass WITHOUT being coerced to a key-path")

    def test_item_requires_an_address(self):
        r = conformant()
        r["items"][0].pop("address")
        self.assertIn("BR001", codes(r))


class ClosedSets(unittest.TestCase):
    def test_unknown_cell_rejected(self):
        r = conformant()
        r["cells"]["invented_cell"] = {"applicable": True, "count": 0, "method": "mention"}
        self.assertIn("BR005", codes(r))

    def test_item_cell_must_be_in_the_closed_set(self):
        r = conformant()
        r["items"][0]["cell"] = "probably_fine"
        self.assertIn("BR007", codes(r))


class AggregateDenominator(unittest.TestCase):
    def test_denominator_note_reports_applicability_not_a_sum_of_zeros(self):
        """The line an aggregate MUST print: 'of N tools, how many even HAVE this cell?'"""
        with_doc = conformant()
        no_doc = copy.deepcopy(conformant())
        no_doc["cells"]["doc_only"] = {"applicable": False, "count": None, "method": None}
        no_doc["surface_total"] = 90
        note = B.denominator_note([with_doc, no_doc])
        self.assertIn("doc_only: 1/2 tools applicable", note,
                      "the aggregate must distinguish N/A from zero at the fleet level")
        self.assertIn("orphan: 2/2 tools applicable", note)


ANTICIPATED_REQUIRED_TOKENS = ("owner:", "trigger:")
KNOWN_STATUSES = {"LIVE", "ANTICIPATED", "RETIRED-CANDIDATE"}


def anticipated_violations(vocab):
    """ANTICIPATED terms whose note fails the owner+trigger contract.

    boundary_report's header calls that contract "grep-provable". This IS that grep,
    run. It lives in the test file rather than the module because the L0a semantic
    type is exec-locked (ANY_EXEC) and this lane authors tests, not the type.
    """
    bad = []
    for term, meta in vocab.items():
        if meta.get("status") != "ANTICIPATED":
            continue
        note = meta.get("note", "")
        if not all(tok in note for tok in ANTICIPATED_REQUIRED_TOKENS):
            bad.append(term)
    return sorted(bad)


def status_violations(vocab):
    """Terms carrying a status outside the closed set -- the contract's bypass."""
    return sorted(t for t, m in vocab.items() if m.get("status") not in KNOWN_STATUSES)


class AnticipatedCarriesOwnerAndTrigger(unittest.TestCase):
    """The header's strongest sentence, converted from prose into a check.

    CVO~Z proved by mutant (verdict 20260725T170032Z) that this contract had ZERO
    enforcement: injecting an owner-less ANTICIPATED term left the suite green at
    17/17 with nothing objecting, and zero tests anywhere referenced ANTICIPATED.
    The bucket was empty because a RULING emptied it, not because a CONTROL kept it
    empty -- care, standing in for a control, inside the artifact built to name that
    substitution.

    NOTE THE SHAPE OF THE FIXTURES, it is the whole point: the mutant and the control
    run against SYNTHETIC vocabularies, never the live one. A test that merely looped
    over the live dict would pass vacuously today (0 ANTICIPATED entries) and would be
    the very untested assertion it was written to replace -- green from emptiness
    rather than from correctness.
    """

    def test_MUTANT_anticipated_without_owner_or_trigger_REDDENS(self):
        mutant = {"made_up_space": {"status": "ANTICIPATED",
                                    "note": "no owner, no trigger, pure invention"}}
        self.assertEqual(anticipated_violations(mutant), ["made_up_space"],
                         "MUTANT FAILED: an ANTICIPATED term carrying neither owner nor "
                         "trigger was accepted -- 'a forgotten term with better branding'")

    def test_MUTANT_owner_without_trigger_REDDENS(self):
        """Half the contract is not the contract: an owner with no trigger never expires."""
        mutant = {"half_kept": {"status": "ANTICIPATED",
                                "note": "owner: 1.0.0_SA_CTO~Z, but no trigger named"}}
        self.assertEqual(anticipated_violations(mutant), ["half_kept"],
                         "MUTANT FAILED: owner alone cannot retire a term; the trigger is "
                         "what makes ANTICIPATED distinguishable from forgotten")

    def test_POSITIVE_CONTROL_conformant_anticipated_is_accepted(self):
        """The check MUST be able to accept, or it is not a check."""
        ok = {"future_space": {
            "status": "ANTICIPATED",
            "note": "owner: 1.0.0_SA_CTO~Z; trigger: comp-foo's first conformant emission"}}
        self.assertEqual(anticipated_violations(ok), [],
                         "POSITIVE CONTROL FAILED: a conformant ANTICIPATED entry was rejected")

    def test_RETIRED_CANDIDATE_is_not_subject_to_the_contract(self):
        """RETIRED-CANDIDATE carries no owner BY DEFINITION -- that is the honest label."""
        retired = {"yaml_key_path": {"status": "RETIRED-CANDIDATE",
                                     "note": "no owner/trigger nameable without invention"}}
        self.assertEqual(anticipated_violations(retired), [])

    def test_MUTANT_misspelled_status_silently_EXEMPTS_and_the_status_check_catches_it(self):
        """A status typo is the contract's quiet bypass -- documented AND closed.

        anticipated_violations keys on an exact string, so 'Anticipated' is not
        checked at all: the term reads as anticipated to a human and is invisible to
        the control. That hole cannot be closed by the owner/trigger predicate itself
        -- it needs a second one over the status vocabulary.
        """
        mutant = {"typo": {"status": "Anticipated", "note": "no owner, no trigger"}}
        self.assertEqual(anticipated_violations(mutant), [],
                         "documenting the hole: a typo'd status is not seen by the contract")
        self.assertEqual(status_violations(mutant), ["typo"],
                         "MUTANT FAILED: an out-of-set status must be caught by the "
                         "status check, or the contract stays bypassable by typo")

    def test_LIVE_vocabulary_satisfies_the_owner_trigger_contract(self):
        """Live application. VACUOUS TODAY (0 ANTICIPATED) and that is a TRUE state, not
        a passing one -- it starts doing real work the moment the count stops being 0."""
        self.assertEqual(anticipated_violations(B.KNOWN_ADDRESS_SPACES), [])

    def test_LIVE_statuses_are_all_in_the_closed_set(self):
        """NOT vacuous: this runs over every declared term, today."""
        self.assertEqual(status_violations(B.KNOWN_ADDRESS_SPACES), [],
                         "a status outside the closed set silently exempts its term")


if __name__ == "__main__":
    unittest.main(verbosity=2)
