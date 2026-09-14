# LGIC_NAMING v1.4 -- L4-R brief review

Author: `4.0.0_SA_CRO` | UTC: 2026-09-14 ~11:40Z | request 96577 from `1.0.0_SA_CTO`.

**VERDICT: SIGNED, brief half.** All 22 brief coverage entries carry their content into the consuming requirements. The S10 ruling makes legacy-served membership shared data, preserves the two-argument grade contract, states the error behavior before that data exists, and assigns legacy root code keys a verdict without authorizing a move. No blocking brief correction remains at the offered pin. This is approval of the specification, not evidence that the membership census, grader or exercises have been delivered.

## Exact inputs and delta

- PRD: `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@e04b802fe9ac72471e32897d2055db095353cbe8`, v1.4, 251 lines.
- Brief: `docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe7582bc455fee225f663f5ef2566f8d68c`, 237 lines.
- Brief-half SHA-256: `3cf0e30ac9c2e1fc7497e8bb4be6250cd81d856703748bbe88f818378980c7a4`.
- Ratified-text SHA-256, identified but not re-signed by this seat: `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f`.
- Schema: `org/standards/NAMING_SCHEMA.json` v1.4, 142 lines, at the offered PRD pin.
- Adjudication: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_LGIC_NAMING_20260914T113xZ_S10_LEGACY_MEMBERSHIP_IS_DATA.md`, 86 lines, at the offered pin.
- Previous review: `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_3_20260914.md@2b3855871e5cadd3153922c808933a7df9b77a68`; reviewed PRD `7bd4ef6f2702a3528e23590841652a5d60a564e6`, signed by this seat at `81c9fdb639bd3931b193df4b668f172f55c7a79c`.

The full pinned brief, PRD, schema and adjudication were read. The complete v1.3-to-v1.4 PRD/schema diff changes the PRD version and S1 line 127; in the schema it changes version/ratification/changelog metadata and `key.legacy_served_path`, `key.legacy_served_paths`, `key.code`. ENDPOINT and CONTRACTS remain unchanged, as does the canonical ratified-text hash. Cells, coverage and manifest are unchanged. HEAD and worktree PRD text matched the offered pin when measured.

## S10 closure and remaining proof

The observation is valid and was missed in my v1.3 review: preserving legacy bytes without identifying the legacy set left two graders able to disagree. The COO's investigation at the offered pin (`surprise-channel/investigations/INVESTIGATION_v1.md:225-245`) and the CTO's adjudication (12-21) establish the failure. This review supersedes the earlier conclusion on that specific gap.

| Requirement | Pinned carriage | Assessment |
|---|---|---|
| One shared membership decision, not a grader's memory or a name-shape guess | PRD S1:127; schema:38-39; adjudication:34-53. `key.legacy_served_paths.home` names `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`; the legacy exception applies only to listed paths. | Closes the missing data dependency in FWD-5 / brief O5 and Part V. |
| Named producer, complete stated domain and evidence of its measurement | Schema:39 and adjudication:37-43,80 assign LN-g-1 every served path below `{source}/{scope}/platinum/` requested by the frozen portal, with the portal vintage and printed denominator. The standards file stays the L4 author's; the measured list belongs under the project's deliverables. | One source for hand grading and runtime grading. Census completeness remains the producer's proof obligation; a frozen portal assertion is not that proof. |
| Deterministic behavior before the list exists | Schema `until_present`:39, PRD:127 and adjudication:44-46 require RAISE when the verdict turns on membership. Schema `grade.unplaceable`:131 treats missing knowledge as a rule/data defect, never a fourth verdict or a guessed conformance result. | The missing list is explicitly disclosed. It is absent at the offered commit and in the worktree at this read. No FWD-5 exercise success is claimed. |
| Preserve the signed grade interface and one runtime source | Schema `grade`:125-131 remains byte-equivalent as parsed data to v1.3. LGIC_ENFORCE's PRD at the offered pin, CONTRACTS:148-152, consumes the schema at runtime without copying, executes the written rule and compares against N2. Adjudication:41-49 requires following the list reference at runtime rather than adding a caller argument. | `grade(name, type)` and the three verdicts stay intact; ENFORCE must implement the dependency and its error behavior. |
| Give root code keys a verdict without changing retained objects | Schema `key.code`:40 and adjudication:61-69 specify OUT-OF-PATTERN with the source/scope/code-tier canonical form. The adjudication's example maps `code/gold/x.py` in `opal-data-bd` to `advi/49financial/code/gold/x.py`. | Closes the unstated legacy-root verdict. It grants no move and preserves MDPF's frozen rollback objects. Unresolved identity still falls under the unchanged RAISE rule; this example is not a license to guess scope. |

The written rules distinguish these cases: a listed legacy path may retain its specified table/entity/filename bytes; an unlisted path receives no legacy exception and must satisfy the ordinary rules; missing membership data causes RAISE only where it affects the verdict; a conforming new path whose result does not depend on membership does not need an exception; a legacy root code key remains OUT-OF-PATTERN with its resolved canonical form. Listing a path does not waive source/scope grammar or authorize access. These are contract checks, not executed grader tests.

The existing L5 decomposition at the offered pin is still v2, points at v1.3 (9-12), and gives LN-g-1 only the written-rule output (173). The committed v1.4 adjudication:80 and project phase explicitly assign `2.0.0_SA_COO~G` the v3 recut with `LEGACY_SERVED_PATHS.json` as a second write surface. The PRD's existing deliverables manifest row (246) contains that home; N2 supplies the producing activity, and S1/schema supply the new obligation. This is an assigned L5 follow-through, not a claim that v3 has already landed or authority for this reviewer to edit it.

## Coverage audit -- all 22 entries

The pinned brief has 22 headings: title and Parts I-VII (8), six outcomes, seven findings and REFS (1). PRD entries 1-22 at 216-237 match exactly, without omissions or duplicate identifiers. Every source section was re-read against its consuming clauses, including the unchanged requirements.

| # | Brief entry | Content carried |
|---|---|---|
| 1 | Title / preamble | Commission for a least-disruptive schema, founding rulings and no live rename boundary in the PRD preamble and S13. |
| 2 | Part I heading | Structural; all six outcomes separately represented. |
| 3 | O1 | N1 supplies schema data; N3 requires two independent namers using schema/seed, including the Cottonwood MDPF publisher, with identical strings. |
| 4 | O2 | S3-S7 assign positions and N3 has a separate reader identify the firm; ambiguous `bd` cannot carry two meanings. |
| 5 | O3 | S4 fixes SHORT resource/secret scope and LONG bucket/key scope; S10 retains aliases as history; N4 requires one pattern per firm's attributed canonical principals, a denominator and foreign-firm negatives. |
| 6 | O4 | S1/S2 preserve source-first five-segment keys, separate container/object and bucket rules; N5 requires both replacement notices and the cross-bucket reading exercise. Legacy exceptions do not replace this structure. |
| 7 | O5 | S11/N2/N6 carry three verdicts, canonical forms, real worked cases, RAISE and independent hand-grading agreement. S1 and schema:38-40 now resolve the shared-membership and root-code gaps described above. |
| 8 | O6 | N7 carries all ten tension rows and a disputable current-cost line for each; APPLIED is the named Andrew ruling. |
| 9 | Part II boundary | Schema and grading specification owned here; registry rows/builders/flagger owned by ENFORCE; remediations and IAM changes excluded. The legacy measurement is schema input with an assigned producer. |
| 10 | Part III bars | Confirmed endpoint and N3/N4/N6/N7 retain independent naming/reading, one firm pattern, grading agreement and costed ranking. |
| 11 | Part IV heading | Structural; seven findings separately covered. |
| 12 | IV.1 dominant grammar | S3 keeps system-first kebab structure and pins vocabulary; no mass rename. |
| 13 | IV.2 schema | S1-S9/N1 carry keys, buckets, resource names, cadences, secrets, log groups and policies; v1.4 makes the existing legacy exception decidable from shared data. |
| 14 | IV.3 firm spellings | S4 fixes the form per slot; N4 tests attributed canonical forms without claiming present live names already conform. |
| 15 | IV.4 ambiguous bd | S10 requires blackdiamond/49financial, refuses new bd tokens and keeps aliases as history; N3 tests referent clarity. |
| 16 | IV.5 first tokens | S6 defines system classes, rejects firm/project/workstream/cadence/generic tokens and reserves opal for account-level resources; registry owns actual system rows. |
| 17 | IV.6 postulates | S7 closes the type partition by subtraction; S11 distinguishes verdicts from unresolved defects; N2 enumerates residue cases; S13 preserves live state. Membership data supports agreement without changing the verdict enum. |
| 18 | IV.7 ranking | N7 requires all ten rows with their costs, N5 carries the older layout notices, and the schema mints no remediation. |
| 19 | Part V prerequisites | SYSTEM axis belongs to registry before builders; closed kind/cadence data; one vocabulary; three verdicts plus defect RAISE; no rename; label census before ENFORCE flagger specification. |
| 20 | Part VI status | NOT CONSUMED as work: historical measurements are substrate, not current liveness or completion evidence. |
| 21 | Part VII claim limits | Labels/tags/routes excluded, key measurements inherited, system rows left to registry, no running tokenizer claimed, short-form ruling attributed, no effort estimate invented. |
| 22 | REFS | NOT CONSUMED as work: references; ratification, short forms and remediation ownership resolved; label census assigned to ENFORCE. |

## Verification and limits

JSON parsing, the full delta and canonical half hashes were checked. The schema still has 18 kind-graded type keys and 15 others, disjoint and totaling the declared 33; per-type kinds cover exactly `kind.values`. The exact five-segment grammar and entire grade block are unchanged. The 22-heading / 22-row denominator was counted mechanically and checked against section content. No live census, builder execution, hand-grading exercise or cloud mutation was performed.

ENFORCE's counterpart exists at the offered pin and was read. The inherited NAMING introduction at 21 and 112-113 still says it does not exist; that historical prose was not treated as current evidence. This review makes no new claim about completion of the separately owned LGIC_CANON-S1 prose correction.

The sequence check returned stage 1, DECOMP, no project flags, TRACK at `SEQUENCE.yaml@089ba2d431`. Admission at review start was WITHHELD, brief STALE and ratified-text SIGNED/current. The canonical stamp and fresh status determine the resulting admission. Project blocking item 5 still reserves L6 issuance to Andrew; the COO must also recut the decomposition. Admission does not supply the absent membership data, exercise FWD-5, prove ENFORCE consumes v1.4 or lift another project's implementation conditions.

Request 96577 was read and content-ACKed. Under the Codex exception in `org/XXX.md` B.0, no `ack_messages` surface or ledger READ stamp is claimed. A completion receipt and archive of the exact request follow the committed review and guarded canonical signature. This seat's work is local; no push is performed. The local `origin/CLOUD` tracking ref read `56608aadd493d738330e5b9324683019cf5417e3`; that is not a fresh remote measurement.
