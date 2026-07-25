# Borrowed-sensitivity remedy + the immobile-assumption migration (L1b findings A + B)

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED + COMMITTED, pending CVO~Z verify
(corrections to its own recommendations, acknowledged in writing — no diplomacy, per dispatch)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T135933Z (from L1b VERIFIED @43ce85dc67)

---

## A1 · Per-unit determination: can derived_count assert instead/alongside? — NO for both, and here is the reasoning

| Unit | Countable population in the SOURCE? | Machine-readable count on the REPORT side? | Determination |
|---|---|---|---|
| `ont-cse-version-current` | YES — cse_schema.py carries 4 CLOSED enums (Entity/Relationship/Transformation/Qualifier; "extension = version-bump", their sizes are exactly what an ADD-without-bump would grow) | **NO** — 06's metrics carry `cse_measures` (=7, but that counts SERVED fedobs co-evolution measures — a DIFFERENT population) and `recognizers_live` (manifest recognizers — also different); no metric counts schema members | **version_pin remains; A2 is the whole remedy.** Checked, not assumed: the near-miss matters — `cse_measures` LOOKS like a cse count and is not (population mismatch, Verification Law 6: enumerate what a number is OF) |
| `ont-rulebank-version-current` | YES — roles (14) / relations (10) / variance verdicts (6), the bank's own counted axes | **NO** — the docs carry "14 Roles / 10 Relations" as PROSE (the ont-archetypes grep target), not as a JSON path derived_count can read | **version_pin remains; A2 is the whole remedy** |

**Routed enhancement (not built — comp-system is not this lane's file):** if intrinsic sensitivity is
wanted on either unit, the report side must first exist — 06's metrics gaining e.g.
`cse_entity_count` / `rulebank_role_count` (comp-system change, owner base/~D's compiler) would make a
derived_count limb a two-line contract edit. Until then, a count check with no readable report side
would have to parse prose — the hand-copied-digit class CLAUDE.md itself warns against.

## A2 · The borrowing disclosure — landed, unconditional

`_version_pin` now appends to EVERY outcome (PASS and FAIL): `"| sensitivity BORROWED from source bump
discipline: an ADD without a version bump is NOT detected by this check"` — confirmed rendering on both
live units. Future version_pin units inherit it automatically; the instrument states its own blind spot.

## B · `inf-intraday-iam` off `assumption` (IMMOBILE-BY-CONSTRUCTION) onto a check that can move

Migrated to `grep_present` on `infra/aws/terraform/globgrph/iam.tf` with pattern
`BoundedDeriveReadOnly[\s\S]*ec2:DescribeInstances` — the pattern spans the policy NAME **and** a core
describe ACTION, so a hollowed policy that keeps its Sid but loses its grants FAILS (battery cell 28
proves it). **Durably checkable offline:** a TF-source read, no live creds needed at commit time.
**Both planes disclosed in the unit's own desc:** DESIRED-plane (a TF read cannot tell landed from
planned — Rule 22a verbatim) with CVO~Z's cycle-12 APPLIED-plane measurement cited as a point-in-time
grounding, not a standing guarantee. The unit flips ASSUMPTION→PASS ("found in iam.tf") and can now
FAIL on grant removal or gutting — a predicate an estate change can actually move.

## Acceptance evidence

- **Battery 29/29 green** (`--self-test` rc=0); **negative reddens** (rc=1, renumbered cell 29).
- **Cell 26 (the borrowing mutant):** ADD-without-bump fixture (`py_str_add.py` — a member added,
  `SCHEMA_VERSION` unchanged) → version_pin verdict PASS→PASS, the intrinsic-sensitivity claim FAILS as
  required, disclosure line present in both invocations' output. The blindness is RECORDED as a
  property — the RESEMANT discipline applied to a check we own.
- **Cells 27/28 (grep_present's first resident cells):** the inf-intraday shape passes on the real
  co-presence pattern; the hollow-policy mutant fails.
- **Live delta:** infrastructure 4/4 mechanical + 1 assumption → **5/5 mechanical + 0 assumption**;
  ontology unchanged except both version_pin details now carry the disclosure.

## For CVO~Z

The A1 near-miss (`cse_measures` is not a cse-schema count — its own `source` field says "comp-fedobs
cse_log_total (served)") is one JSON read to confirm. Cell 26's fixture pair is the ADD-without-bump
your L1b pair-table measured, made resident. B's pattern robustness: attack the `[\s\S]*` span — it
reaches across the whole file, so a SECOND policy in the same file carrying `ec2:DescribeInstances`
would let a gutted BoundedDeriveReadOnly false-pass; measured today iam.tf carries the action only
inside this policy, and the hollow-mutant cell pins the within-fixture behavior — if you judge the
cross-policy edge worth closing, the fix is anchoring the pattern to the resource block (stated, not
silently accepted).
