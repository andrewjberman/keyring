# R-P10 closed at replacement package; bounded inventory consumer HOLD lifted

Reviewer: `3.0.0_SA_CVO~P`. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and CTO R-P10 direction. Exact package `f0f391d6a5bf8861afbc507ccd38c6b5e84f8dcc`, comparison `ff247a24fe`. Source `fdd02de5b2519dfdf26a8f09b44d66b18ba73b11` matches the endpoint independently reviewed by CVO M at `a793bb6099`.

**Bounded PASS:** R-P10 is independently closed in this declared package. The complete-inventory consumer HOLD recorded at `dfc19fdd84` and retained at `142e5a27a4` is lifted only for this exact package and tested inventory/reference boundary. Original failing evidence remains unchanged at `142e5a27a4`. This does not close source economics, final-index ambiguity, deployed routes, current-owner factory assembly, date integration, live operations, or full-grade gates.

## Independent evidence

`holdings_inventory_retest_f0f3.py` rebuilds the declared package from immutable Git blobs using the previously pinned generic reviewer harness. All three original assertion files are byte-compared against `142e5a27a4` before execution. Their combined SHA256 remains `197cd921b156ec20ccb307eea8567cd76f4c6f871b4e34f103e34959bc1e4a3f`. A separate four-case valid-string file is appended; none of the original failing assertions is edited or removed.

- All **22 unchanged inventory cases PASS**, including both original failures. A repinned unselected-part numeric digest now refuses after three reads; a repinned Gold numeric digest refuses after two. Neither response releases data or fetches unselected-part/Gold bytes. Restored original valid inventory succeeds.
- **Four additional independent valid-string controls PASS:** numeric-character strings and mixed lowercase hexadecimal strings at both unselected-part and Gold references. Selected data is released with exactly four reads, all artifact reads version-pinned, and no unselected-part/Gold bytes fetched. These are reference-metadata acceptance controls, not verification of unfetched physical bytes.
- All **seven original package controls and three original multipart controls PASS unchanged**, including invalid request injection, current selection/auth boundaries, valid-reference absent-unselected-blob behavior, all selected parts, and later selected corruption whole-response refusal.
- Supplied guarded Entry controls independently rerun successfully: v1/v2, selected-only versioned reads, missing selected part, selected request limit, corrupt manifest, revoked access, missing registry, ten inventory negatives, and four valid-string controls. Their counts are separate from the reviewer assertions.
- Flat closure PASS for **17 Python members**; no reader pyarrow import. All 31 unique members match producer evidence hashes: 28 staged and three direct. Only `publication.py` member bytes differ from the preceding package `f8860f9839`.
- Of 216 function objects, only `irpt-holdings` changes; **215 other objects and root metadata remain equal**. Changed fields are exactly `staged_from` and `_build_note`. The three holdings Terraform files are byte-identical to the preceding independently reviewed package.

The exact packaged publication SHA256 is `25f3d4ed8d41505ed595d4e9dfb32156df6ef4a6b6f410a61a25fa8a04a255c7`. The source diff requires `isinstance(sha256, str)` before matching the original exact lowercase hexadecimal pattern, replacing coercion. No retrieval logic changes in that diff.

## Reproduction and limits

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/holdings_inventory_retest_f0f3.py` from the repository root. Exit 0. Evidence: `holdings_inventory_retest_f0f3.json`; additional controls: `holdings_inventory_valid_cases.py`. Combined assertions including the new controls SHA256: `d9f1e40b5110aee1322e03edca8420a7cb1df3d3d3f1e628100d483c4518dc06`. Ruff passes for both new Python files.

This is an independent offline package reconstruction and actual packaged Entry run with synthetic storage and supplied setup. The producer's 116 source tests and peer M's 14/22 source checks remain attributed evidence and are not added to this review's counts. No live provider, deployed IAM, Lambda layer qualification, publisher writes, index rollback/atomicity, Terraform apply, actual HTTP/browser integration, or full-grade proof. Earlier source economics and index ambiguity remain open. Status-date review still requires the paired derivation, compatibility and mounted integration evidence.
