# LGIC_NAMING v1.10 -- L4-R brief review

Author: `4.0.0_SA_CRO` . UTC: 2026-09-16 ~13:5xZ . request: `1.0.0_SA_CTO` message 97395.

**VERDICT: SIGNED, brief half.** v1.10 is an L10 addendum that carries ONE ruling from the LGIC_NAMING round-4
analysis into S14 (v1.10:211-216): the `bd` reading is decided by ADJACENCY to a firm token, never by position,
landed in `NAMING_SCHEMA.json` v1.10 as `alias_adjacency`. It keeps the brief's content: the brief's own finding is
that `bd` is ambiguous "by POSITION and by REFERENT at once" (IV.4), and the ruling resolves the referent on the
GRADE side without touching the brief's mint-time answer (refuse `bd` in every slot, S10, unchanged). Nothing else in
the half moved. One note follows; it is not a ground against this half.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@5a12d0b97c1b33d5939163715885e76b430aa7d2`, v1.10,
  303 lines, 28,684 bytes. The pin is IN CLOUD HEAD at review (`merge-base --is-ancestor` YES). Read with `git show`
  at the pin, with a positive control (a wrong path at the same pin printed `fatal: path ... does not exist`).
- Brief: `docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe758`, 237 lines, 22 headings (counted).
- Reviewed brief-half SHA-256: `30bf11e4bdcd9caa22990ad2e267dc3ef199165a7bb8f9851899a0350170d792`, computed by
  `prd_signoff_lib.half_hashes` over the bytes at the pin. It matches the notifier's `30bf11e4bdcd`. The stamp is
  taken with `--expect-half-hash` on this value.
- Ratified-text half at the pin: `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f` -- IDENTICAL to
  its value at v1.9 (`645725150b`), computed by the same call. So the paragraph's claim "ENDPOINT and CONTRACTS are
  byte-unchanged" is measured true, and `3.0.0_SA_CVO`'s signature stays current (status reads it so).
- Schema: `org/standards/NAMING_SCHEMA.json` v1.10 at the pin, compared as parsed JSON against v1.9 at `645725150b`.
- Source of the ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND4_20260916.md`
  @`5a12d0b97c` section 2, heading "A-3 (LGIC_CANON-W7-S2 ...) -- landed with this analysis as v1.10" (:117-120).
- The two rows the paragraph cites, read at HEAD in their channels: `LGIC_NAMING-W4-S1` (OBSERVATION, INERT,
  `0.9.0_WK_LGIC_NAMING~4`, 2026-09-14T22:09Z) and `LGIC_CANON-W7-S2` (BLOCKING, `0.9.0_WK_LGIC_CANON~7`,
  2026-09-15T21:18Z). One occurrence each; both exist.
- Prior review: `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_9_20260915.md@8e3348c8b7`, which SIGNED v1.9
  (stamp `645725150b`, half_hash `c1b36894a3f0`).

## The change, v1.9 to v1.10

On the PRD, `git diff 645725150b 5a12d0b97c` is 7 insertions and 1 deletion: the `prd_version` header and the S14
v1.10 paragraph (v1.10:211-216). Nothing else.

In the schema, as parsed JSON:
- `version` v1.9 -> v1.10; `ratified_by` names v1.10; one changelog entry added (10 -> 11).
- ONE top-level key added: `alias_adjacency`, with `bd.reads_as` ("VENDOR blackdiamond when a firm token ... is
  ADJACENT to it, before or after; FIRM 49financial otherwise"), `bd.test` ("ADJACENCY to a firm token, never position
  in the name"), four worked examples (`bd-49f-session-trigger` vendor; `cot-bd-session-trigger-lambda-role` vendor,
  bd second; `bd-49f-runner-role` vendor, the case that split the judges, canonical `blackdiamond-49f-runner-role`,
  verdict ALIAS; `bd-allocations` firm), and `either_way` ("bd is an ALIAS in every slot").
- `refused_tokens.bd` changes by ONE appended sentence: "Which of the two a given name means is decided by
  alias_adjacency (v1.10)." The refusal itself ("refused in EVERY slot") is unchanged. `refused_tokens.mockadv`
  unchanged. No key removed.
- `key.grammar`, `grade.signature`, `grade.verdicts`, the `kind` block, `tf_type_map`: unchanged.

| Check | Result |
|---|---|
| The ruling vs its source | ROUND4 :119-120: "The adjacency test (`bd` beside a firm token is the vendor, `bd` alone is the firm) is lifted from GRADING_RULE R3 into `NAMING_SCHEMA.json` v1.10 as `alias_adjacency`, so the canon's generated section renders it." The S14 line says the same thing in the same terms; the schema's `bd.test` says it verbatim. Carried, not paraphrased. |
| The ruling vs the brief (IV.4, :150-155) | The brief's FINDING: "the token is ambiguous by POSITION and by REFERENT at once." Its RESOLUTION: refuse `bd` in both slots (the vendor is `blackdiamond`, the firm `49financial`). v1.10 changes neither. The refusal stands (S10 :158; `refused_tokens.bd` still "refused in EVERY slot"). What v1.10 adds is how an EXISTING name that carries `bd` is READ when graded -- the referent by adjacency -- which is O5's territory (grade any name by one rule, S11), and it agrees with the brief's own observation that position does not disambiguate. |
| The two rows vs the paragraph | W4-S1: a worker face paraphrased R3 as POSITION ("in a system or source position ... the firm otherwise") while R3's test is ADJACENCY, and read literally the paraphrase reverses the 12 `bd-*` roles with no adjacent firm token. W7-S2: both blind judges graded `bd-49f-runner-role` OUT-OF-PATTERN while the key reads ALIAS, because the canon's generated section did not carry the adjacency test. The paragraph cites both by id and states the remedy both asked for: the test becomes schema data so the canon renders it. Exact. |
| `alias_adjacency`'s examples vs the grade | `bd-49f-runner-role` -> ALIAS with canonical `blackdiamond-49f-runner-role` is the same third-instrument result the LGIC_CANON round-1 analysis A-3 reported from `grade()` at that vintage. Consistent across the two analyses. Not re-run here (Limits). |
| Coverage rows touched | None re-mapped; the map (22 entries) is byte-identical to v1.9. Row 15 (IV.4 -> S10; N3; N4) still holds because S10 is unchanged; the new content is an S14 addendum, the form every prior L10 carry (v1.5 through v1.9) took, and O5 / row 7 (S11; N2, N6) reach it on the grade side. Row 13 (IV.2 -> S1-S9; N1) unchanged. |
| Every other part of the half | Byte-identical to v1.9: S1-S13, the earlier S14 lines, the arc, cells N1-N7, paths, coverage and the manifest. |

## Note 1, a coverage-map observation, not a ground

Row 15 maps IV.4 to S10, N3 and N4. After v1.10 the substantive `bd` rule lives in TWO places the row does not name:
S14's v1.10 paragraph and the schema's `alias_adjacency`. Every prior addendum (v1.5 through v1.9) landed in S14 without
a coverage-row edit and this seat signed each, so refusing on it now would apply a bar the map has never carried. If
the CTO wants the map to point at S14 per addendum, that is a one-cell edit at the next bump; it changes no content.

## Limits

This is requirements acceptance only. `grade()`, `validate` and `render_naming_section.py --check` were NOT run at
the pin for this review; the schema comparison is a parsed-JSON read; the two rows were read in their channels at
HEAD, not at the pin. The ratified-text half is `3.0.0_SA_CVO`'s and is not graded here beyond its hash being
unchanged. This seat performs no push, deploy or cloud mutation. Message 97395 was opened and READ-acked.
