# KEYFILL registry ratification after two fail-closed recompiles - 4.0.0_SA_CRO~X

**archetype:** VALIDATE
**Date:** 2026-08-29
**Task Order:** NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT
**Status:** IN PROGRESS

---

## Objective

Independently ratify or refuse the 72-card KEYFILL registry compile at the settled authority pin,
without loosening the key receiver predicate. Verify every member/blob/subject triple, the candidate
digest, the key admission and basis denominators, collision disposition, negative controls, and the
registry contract before recording `ratified_at_commit`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `python .tools/comp-find compiled_at_commit org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST --files --all` | PASS | Measured that only the compiler and registry carried the field; the v1 schema did not. |
| RAT harness | `python org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ratify_keyfill_registry.py` | PASS | Final dry run at `92f1b8da9d` printed 72/72 blobs, digest match, 43/29 admission, and basis 61/10/1/0. |
| Producer schema control | direct call to `compile_card_registry_ext.py:validate_root()` | PASS | Shipped simulated-RAT root passed; the three-field mutant was refused with every forbidden key named. |
| Git object checks | `rev-parse`, `show`, `cat-file`, blob and SHA-256 comparisons | PASS | Bound registry, compile receipt, 72 cards, subjects, settled receipt, and compile commits to exact Git objects. |

**What worked:** The independent RAT harness held one settled pin across all 72 cards and made the
admission, subject-disposition, receipt-link, and schema checks repeatable. Scoped `comp-find`
confirmed the schema mismatch without a raw repository grep.

**What failed:** Invoking `.tools/comp-find` directly under Windows produced no output; invoking the
repository script through Python produced the required denominator. The first positive-control
implementation treated a descriptive `subject.id` as a path and failed closed; it was corrected to
use the card's pinned `artifact.location.home` source.

**Gap found:** The compiler exposes `validate_root()` but no dedicated CLI self-test switch for its
positive and negative schema fixtures. CRO exercised the function directly and recorded both arms.

---

## Work Completed

### 1. Refused the mixed-pin compile

- Re-read compile `ddbba3f141` against settled pin
  `cf66984cfc39e7f45c0799c75be43c4ec1fb7934`.
- Verified all 72 member blobs and the candidate digest, then independently found five path-like
  `.comp-graph` subjects absent at the pin but present in the live working tree.
- Named the compiler mechanism: subject classification fell back from `blob_at(pin, sid)` to
  `os.path.exists()` and therefore reported 21 present / 16 absent instead of pin truth 16 / 21.
- Issued STOP to COO, DT, and CVO. The registry remained unratified.

### 2. Refused the schema-invalid recompile

- Re-read corrected compile `a4601f4c26`; the member set, digest, key predicate, controls, basis
  census, and corrected subject disposition all passed.
- Simulated the RAT field and validated the resulting artifact against
  `CARD_POPULATION_REGISTRY.v1.schema.json`.
- Refused because `compile_note`, `compiled_at_commit`, and `subject_disposition` were forbidden root
  properties under `additionalProperties:false`. No member failed; the registry artifact failed at
  its root.
- Issuer ruling 79961 kept the schema frozen and moved required compile evidence to a digest-linked
  sibling receipt.

### 3. Ratified the v1-valid compile pair

- Re-read `92f1b8da9d564f8e5ed8740e1e1a2278577507e5`: seven-key v1 registry root plus
  `card_population_registry.v1.compile_receipt.json`.
- Verified the receipt's registry SHA-256, candidate digest, settled compile pin, receipt SHA-256,
  exact 16/21/32/3 disposition, zero exact duplicates, and seven basename name-misses.
- Recomputed 72/72 card blobs and subjects at the pin. Admission was 43 ADMITTED and 29
  NOT_ADMITTED: 27 `trust.key.declared_mapping`, one `trust.key.key_expression`, and one
  `trust.key.basis`.
- Independently counted `basis_by_field.key_expression` over all 72: measured 61, held 10, absent 1,
  inferred 0. The null-key fixture was NOT_ADMITTED on `trust.key.key_expression`.
- Applied only `ratified_at_commit=d17eee2dc036bb3049d47f8dfd713ab5292b4f4f` and wrote the PASS
  ratification report. Cards, schema, and compile receipt were not modified.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Refuse a compile whose subject census reads the live tree. | A pinned registry cannot mix committed and working-tree clocks. |
| Refuse an otherwise-correct registry that violates its own closed-root schema. | Contract validation applies to the artifact being ratified, not a convenient subset. |
| Keep `.comp-graph/graph.json` in ABSENT-at-pin without a new historical subtype. | The registry records state at one pin; no consumer requested an ever-tracked axis. |
| Preserve all 72 extension members while labeling only 43 key-admissible. | The declared all-non-blank key predicate was not loosened and no governed transform was invented. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ratify_keyfill_registry.py` | Added repeatable member, predicate, receipt-link, subject, control, and schema RAT checks. | No - local evidence bundle pending |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/card_population_registry.v1.json` | Set only `ratified_at_commit` after all gates passed. | No - local evidence bundle pending |
| `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT_RATIFICATION_REPORT.json` | Wrote full PASS report with per-member results and compile-receipt citation. | No - local evidence bundle pending |

---

## Blockers

None. The local RAT evidence bundle still requires proof-of-spec validation and a pathspec commit.

---

## Current State

The canonical compile input is `92f1b8da9d564f8e5ed8740e1e1a2278577507e5`; its registry and
compile receipt were clean and exact before RAT. The registry now carries
`ratified_at_commit=d17eee2dc036bb3049d47f8dfd713ab5292b4f4f`, and the PASS report is at
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT_RATIFICATION_REPORT.json`.
The report cites the compile receipt by path, Git blob, and SHA-256. JOIN remains gated until the RAT
bundle is proof-checked and committed; unrelated shared-worktree changes remain untouched.

---

## Next Steps

1. **[4.0.0_SA_CRO~X] Write and validate the two-row proof-of-spec instance** - close KF-RAT-AC1 and KF-RAT-AC2 against the exact PASS report.
2. **[4.0.0_SA_CRO~X] Pathspec-commit the RAT bundle and mark the task order complete** - keep unrelated dirty paths out of the commit.
3. **[2.0.0_SA_COO~X] Release JOIN only after receiving the RAT commit and measured push state** - the hash, not prose, gates the next act.
4. **[3.0.0_SA_CVO~X] Certify the committed RAT evidence** - independently re-read the receipt SHA and schema result.
