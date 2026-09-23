# Replacement inventory package: reconstruction PASS; consumer acceptance HOLD

Reviewer: `3.0.0_SA_CVO~P`. Authority: CTO IRPT_MVP_COMPLETION_20260922/CONTRACT.md. Exact package `f8860f9839357a80951fa9fce6ca2ed406997734`, comparison `55fae26e37`. The existing package HOLD recorded at `dfc19fdd84` remains. M's bounded source closure `95d2117e97` is retained within its tested cases; renewed package testing finds an additional malformed-reference case.

## R-P10 — P2: numeric digest accepted in complete-inventory metadata

The packaged `publication.py` is exactly `fd4690b4ffca23f2616fe5f19d90737af6fe3a58`, SHA256 `b4c248c49451b4141d27c8fdc5630ba7e563ea91e264bce6b3c46bb7f3a6e1cb`. `HoldingsPublication.validate_reference` applies the digest regular expression to `str(ref.get("sha256", ""))`. A JSON integer containing 64 decimal digits therefore passes metadata validation as though it were a SHA256 string.

The independent probe starts from a valid accepted multipart document and retained one-account selection. It separately sets an unselected partition reference's `sha256`, then the Gold reference's `sha256`, to `int('1' * 64)`. It serializes each changed manifest, recomputes that manifest's actual SHA256/length reference, and updates the current index to the new reference. Thus neither case depends on stale manifest hashes. The actual reconstructed `entry.lambda_handler` releases selected `data` after four storage reads in both cases. Neither unselected-part bytes nor Gold bytes are fetched. Restoring the original valid inventory succeeds.

Expected: refuse the whole response for malformed reference types, without fetching unselected objects. These failures concern the accepted inventory contract; the test does not demonstrate cross-tenant disclosure, live storage mutation, or an external path for injecting metadata. The source economics, index final-write ambiguity, and M-FACT-01/Y-R01 findings are separate. Their peer closures do not establish this validator's type handling.

Requested repair: require an actual digest string before applying its pattern in the shared reference validator. Supply the corrected endpoint and a replacement package with exact staged provenance. Retest the unchanged independent assertions and earlier controls. This reviewer does not edit producer implementation.

## Measured package proof

- 31 unique members: 28 staged, 3 direct; every reconstructed member matches the producer evidence hash. Only `publication.py` bytes differ from the previously reviewed multipart package `c9e4529553eb98b17347f81c77f199e0b5bf9868`.
- Only `irpt-holdings` changes among 216 function objects; all 215 other objects and root metadata are equal. Changed fields are exactly `staged_from` and `_build_note`. All three holdings Terraform source files remain byte-identical to the prior review.
- Flat import closure passes for 17 Python members. Supplied guarded Entry controls pass, including v1/v2 selection, versioned reads, corrupt manifest, revoked access, selected-part absence/limit, missing canonical registry, and ten repinned malformed inventory negatives. Reader does not import pyarrow.
- All seven original reviewer controls plus three multipart controls pass unchanged. They retain the valid-reference/absent-unselected-physical-blob distinction, complete selected part reads, and later selected corruption whole-response refusal.
- New independent inventory matrix: **20 PASS, 2 FAIL** across 22 repinned cases; both failures are numeric digests. Missing/null references, foreign bucket/key, null/literal-null version, short digest, boolean/string/zero length refuse for both unselected-part and Gold references. Restored valid control passes. Probe exits 1 intentionally to preserve the observed failure.
- Ruff passes for both new Python artifacts. The producer's reported 96 holdings source tests were not independently rerun in this package review and are not added to these counts.

## Reproduction and limits

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/holdings_inventory_probe_f886.py` from the repository root. It reconstructs Git-pinned members into a temporary directory, reuses the pinned generic reviewer harness, preserves the prior seven plus three assertions by hash, and appends `holdings_inventory_cases.py`. Evidence is in `holdings_inventory_probe_f886.json`, including per-case results and exact member hashes.

Prior assertion SHA256: `3b0de64f00ec8f6f505ecd124bee85212c90a4fa662163ef93a686f3c23d274d`. Combined assertion SHA256: `197cd921b156ec20ccb307eea8567cd76f4c6f871b4e34f103e34959bc1e4a3f`.

Offline declared package and synthetic accepted storage only. The independent assertions reuse supplied setup; they independently mutate and repin inventory and call the actual packaged Entry. No deployed IAM, provider economics, actual publisher, Lambda layer qualification, Terraform apply, live routes, disposal/server-clock/concurrency, or full-grade evidence. All broader integration gates remain unchanged. Status-date review remains separately pending paired implementation pins; `48a58f9b11` is preparation and legacy-schema evidence only.
