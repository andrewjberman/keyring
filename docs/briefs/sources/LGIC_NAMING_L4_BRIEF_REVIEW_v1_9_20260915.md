# LGIC_NAMING v1.9 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15 ~17:4xZ · request: `1.0.0_SA_CTO` message 97166.

**VERDICT: SIGNED, brief half.** v1.9 is an L10 addendum that carries two rulings from the LGIC_ENFORCE round-1
analysis into S14 (v1.9:205–210):
- a firm's forms live only in the identity registry, so `firm_forms` leaves the schema (RULING ONE);
- the Terraform-type to node-type map becomes data.

Both keep the brief's content. RULING ONE puts the short-form decision where the brief put it, with the spine. Nothing
else in the half moved. Two notes follow; neither is a ground against this half.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@645725150ba93cc98f7aaf2e3cabef2110581103`, v1.9,
  297 lines, 28,211 characters. **The pin is on branch `lgic-v19-landing` and is not in CLOUD** (CLOUD HEAD
  `2045fa4d8e` at review). Read with `git show` at the pin.
- Brief: `docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe758` (22 headings).
- Reviewed brief-half SHA-256: `c1b36894a3f0684ddfe7402dbf0739614fcf6d167da5fdb75e0c6666bc476a92`, computed by
  `prd_signoff_lib.half_hashes` over the bytes at the pin. It matches the notifier's `c1b36894a3f0`.
- Ratified-text half: `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f`, unchanged since v1.4.
- Schema: `org/standards/NAMING_SCHEMA.json` v1.9 at the pin, compared as parsed JSON against v1.8 at `2f554182b6`.
- Registry: `infra/logic/registry/scopes.json` at the pin (byte-identical to `2f554182b6`).
- Source of the rulings: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md@7b5331c8c0`
  §2: RULING ONE, RULING DEMO, and the C-S11 paragraph.
- Prior review: `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_8_20260915.md@02529e1bce`, which SIGNED v1.8
  (stamp `b136cdc308`).

## The change, v1.8 to v1.9

On the PRD, `git diff 2f554182b6 645725150b` is 7 insertions and 1 deletion: the `prd_version` header and the S14 v1.9
paragraph (v1.9:205–210).

In the schema:
- `version`, `ratified_by` and a v1.9 changelog entry change.
- `firm_forms` (four rows) is removed and replaced by `firm_forms_source`, a sentence naming the registry as the one
  carrier.
- `tf_type_map` is added: 34 Terraform types over 31 distinct node types, each with its own-name attribute. So is
  `tf_unmapped_own_name`, 30 types that RAISE at G1.1.
- `key.grammar`, `grade.signature`, `grade.verdicts` and the `kind` block are unchanged.

| Check | Result |
|---|---|
| RULING ONE vs the brief | The brief gives each firm "ONE canonical key and ONE sanctioned short form (the spine decides which)" (brief :147), and says "Which short form each firm keeps ... is the spine's call" (brief :221). Moving the forms into the identity registry puts that call in the spine's carrier, not in a second list. S4's per-slot rule (v1.9:133–136) is unchanged. |
| The registry holds what the schema dropped | `scopes.json` at the pin: 49financial/`49f`, inflection/`inf`, cottonwood/`cot`, demo/`demo`, each class FIRM. These are v1.8's four `firm_forms` rows, value for value. So the move loses no form. |
| The v1.9 line vs its source | "one change moves every name and every fence pattern (RULING ONE)". This matches the analysis's RULING ONE and FWD-7's grade: a new firm drew a WARN because it was not in `firm_forms` (W8-S2). `demo` still reads as a firm in the naming slot (DM, v1.7). Its tenancy is the registry's DEMO-TENANT class (RULING DEMO), which is a registry fact, not a naming one. |
| `tf_type_map` against S7 (live-plane node types, v1.1) | Of the 31 node types it maps to, 18 are `kind.by_type` keys, and the other 13 are all in `types_not_graded_by_kind`. So the map adds no node type the schema did not already account for. `tf_unmapped_own_name` is disjoint from the map. |
| `tf_type_map` against the brief's scope | Brief :74 excludes Terraform LABEL grammar. The map is not label grammar: it is the resource type a grade takes, which S7 and S11 already own. A type with its own name and no node type RAISES, so there is no fourth verdict (S11; brief IV.6). |
| Every other part of the half | Byte-identical to v1.8: S1–S13, the earlier S14 lines, the arc, cells N1–N7, paths, coverage and the manifest. |

## Note 1, not in this half: CONTRACTS still names firm forms as schema output

CONTRACTS row 1 (v1.9:107) lists "firm long and short forms" among the enumerations `NAMING_SCHEMA.json` produces. At
v1.9 the schema carries none. That row is in the ratified-text half, whose hash did not move, so no notifier routes it
to `3.0.0_SA_CVO`. The half and the correction are `3.0.0_SA_CVO`'s and `1.0.0_SA_CTO`'s. Not graded here.

## Note 2, landing order: the readers are not yet at the pin

At `645725150b`, code and registry text still name the removed field:
- `lib/opal_naming.py:248` reads `schema["firm_forms"]`; `:287-290`, `:347` and `:381` use it.
- `scopes.json:4` still says "NAMING_SCHEMA.json firm_forms owns which firm short forms exist", and `:210` cites it.

The v1.9 changelog says the readers (EN-r-3) and the rule (LN-g-1) land on this branch and reach CLOUD in one merge.
So the branch must not reach CLOUD before EN-r-3. RULING ONE asked for "the same commit, so the data and its readers
never disagree"; on the branch, that became the same merge. This is a build-sequencing fact, not a requirement defect.
`scopes.json:4` is not in RULING ONE's reader list, and it is filed as a row in LGIC_ENFORCE's surprise channel. `:210`
is the note RULING DEMO already corrects.

## Coverage

Apart from the S14 v1.9 paragraph, the brief half is byte-identical to v1.8. So the audit of all 22 coverage entries,
as amended at v1.6 for row 17, stands, and so do the v1.7 and v1.8 checks of the rulings.

## Limits

This is requirements acceptance only. No builder, `grade()` or `validate` was run at the pin; Note 2 is a source read,
not an exercise. RULING ADD, PLAN, ROWS and RED are LGIC_ENFORCE's and are not in this half. The ratified-text half is
`3.0.0_SA_CVO`'s.

The stamp reads the PRD at HEAD (`.tools/prd-signoff.py:174-176`), and v1.9 is not in CLOUD. So the stamp is committed
from this seat's own worktree, on branch `cro-lgic-naming-v19-signoff` (based at `645725150b`), for `1.0.0_SA_CTO` to
merge into `lgic-v19-landing`. Message 97166 was opened and READ-acked. This seat performs no push, deploy or cloud
mutation.
