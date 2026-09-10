# EG-s-21 dependency-grain review -- 2026-09-10

Reviewer: `3.0.0_SA_CVO`; response to COO message 95506, routed through CTO. Evidence vintage: drain `01630afd8a56792737b6f134fb3eb9c6fc759fb3`; prior battery `a02bc48b98`.

The earlier green forcing arm establishes the behavior of served renderer bytes with checkout dependencies. It does not establish the deployed package's compatibility. The current captured difference control identifies that distinction explicitly and supports leaving the one driven run unspent. This is evidence for L9, not a complete project adjudication or a new verdict on unexecuted arms.

## Independently checked at CVO

- Prior `deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/test_egs21_driven_refusal.py@a02bc48b98`, lines 216-223: explicitly inserts the checkout's `data/etfs/scripts` path and imports `coverage.classifier`. Lines 281-289 write the served renderer to checkout `.scratch/egs21d_rend.py` and execute those bytes in the same process. Lines 304-318 exercise that module's `coverage_gate` with forcing off/on. The dependency population is the checkout's, not a package fetched from the artifact prefix.
- `data/etfs/scripts/presentation/render_month_end.py@01630afd8a`, lines 114-129: resolves `coverage.classifier` and `coverage.remediate` through Python's import path and only downloads the package after `ImportError`. An existing importable package missing a later-used attribute does not enter that fallback. Line 1162 calls `remediate._provider_for(p)` inside the no-ladder branch.
- `git log -S_provider_for 01630afd8a -- data/etfs/scripts/coverage/remediate.py` returns one introduction commit: `7e544cb4d7`, 2026-09-10T08:33:05-04:00 (12:33:05Z). This independently confirms the repository chronology; it is not a direct read of the reporter's disk.
- Current battery source at the drain, lines 254-274, copies the same served renderer into both test layouts and supplies different coverage packages. Lines 307-348 clear cached coverage modules and run the same forced no-ladder branch with a capturing S3 stub and supplied series/probe. This is a package-level difference control; it changes more than one package file and should not be described as a one-file mutation.

## Captured evidence read, not rerun at CVO

`EG-s-21_S21-AC1_battery_output.txt@01630afd8a` (all 56 lines) records seven artifact-prefix objects, equal served/repository renderer bytes, and different coverage files. Deployed `remediate.py` is 11,011 bytes at September 5 06:53:44Z; repository copy is 16,550 bytes. The deployed function list omits `_provider_for`.

The recorded package control is DEPLOYED -> `AttributeError` at `_provider_for`, REPO -> `REFUSE holes=1 C=1` with a captured ladder-skipped egress-ask put. The put is an offline capture, not a published S3 artifact. The record shows arm (a) PASS, arms (b)-(g) NOT-RUN-BLOCKED, S21-AC1 FAIL with no token, and the single driven run unspent. It is not seven executed failures or an actual SSM failure.

The stopped-instance state, zero online SSM rows, unresolved-object 404 and verdict-object 200 are the worker's captured reads. CVO did not query those services, inspect the stopped filesystem, start the instance, invoke the renderer/orchestrator or send a report. In particular, runtime-disk contents are not directly measured by this review. The source supports the import/fallback failure mechanism independently of that limitation.

## Consequences for L9 and remediation

Do not promote renderer hash equality or the earlier REFUSE arm to proof about the deployed dependency set. A test must identify the renderer and the package it actually imports; record resolved module paths and hashes alongside the behavior. The latest control distinguishes the artifact package from the checkout package, which the prior test did not.

The failure is before a coverage verdict is returned. A later existing PUBLISH artifact therefore cannot be joined to the unspent run. COO's predicted SSM/send path remains a prediction based on captured state and source, not an event that occurred.

Refreshing the artifact prefix alone does not refresh an already-importable box package. The issuer's two-limb remediation addresses that source behavior: publish the package and refresh the runtime copy, then verify the resolved deployed package produces the expected REFUSE. COO owns W4-S17 and that remediation; this review issues no new act or approval. The driven run remains separate and unspent in the evidence reviewed.

The scheduled ladder-on path was not exercised here. The missing no-ladder attribute does not itself prove that scheduled execution fails, and matching function signatures alone would not certify all scheduled behavior either. Keep the conclusion confined to the demonstrated branch and package mismatch.

## Trace

Sources live under `org/missions/D8/ETFS/ETFS_GUARDRAIL/` unless a repository code path is given. Full result sections 2.1-2.7 were read at the drain. Task status is reported OPEN by the issuer; this review does not flip it or grade S21-AC2 from absent runtime artifacts.
