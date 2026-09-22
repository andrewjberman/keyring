# R-P08 retest — bounded closure

Reviewer `3.0.0_SA_CVO~P`; authority `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and `CVO_P.md`.

Candidate **284436ca11140a0ede1ef3d53f8b3aa855d4a7a3** (LOCAL). Original finding/evidence **3580fb2fed** on aa1cfaea6b063acac5fc974d397d6a278daa17a0. Independent exact-pin run 2026-09-22T23:01:16.658301Z.

**R-P08 CLOSED at the demonstrated post-blob-read history boundary.** All **79 unchanged tests PASS**: 50 supplied repository/retention/composition tests, 21 prior independent original/receipt checks, and eight independent composition checks including both R-P08 expiry/revocation reproductions. No assertion or fixture was changed for this retest. Original failing evidence remains preserved.

The repair collects verified candidate references, finishes page blob reads, then rereads index identity/ref bindings and checks current owner authorization and accepted retention for each accumulated reference. Missing or denied references are omitted; binding mismatches refuse. This pass performs no additional blob read. Cursor creation remains based on the original index page, preserving the existing pagination behavior. The change is confined to repository.py; composition, retention and all three supplied test files match the prior candidate hashes.

Both original two-item controls now release an empty list after the second blob callback expires all reports or revokes current access. Their prior no-change history call still returns two references, and fresh report gets still refuse after the state transition. Existing positive/history pagination tests pass along with all other repository controls. R-P07 closure remains intact.

Evidence runner `retained_repository_retest_2844.py` imports the original pinned harness, overrides only candidate PIN and output path, and writes `retained_repository_retest_2844.json`. It preserves the original three independent assertion files and the original aa1c evidence. Repository SHA256 `c98091e89d556cf191114c49dd1c1d6e7873711d487740e3ea116311eeb54a2a`. R-P08 assertion SHA256 `de5dbe8fe55dec95def8bd858b43985d8a292e03bfe06a6dad38e31bfc47cd57`; original retention `a4ce15e3852ec4e96fa91981e08ed7a2898cf25416393fb4669542a2101a39e0`; receipt boundary `14ff47c5c1164171cd091007505b42f4230ef814dd851ea318be10e823f787bf`. Raw commands, hashes and process outputs are in JSON. Retest runner passed Ruff.

This is a sequential metadata recheck, **not an atomic authorization snapshot across owners** or a guarantee against every state change during the final metadata pass. This review closes the reproduced later-blob-read gap only. Actual modules run with synthetic ACTIVE policy/destination/clock/access and serialized/versioned storage doubles. Full S7 and P1-P8/S1-S7 remain **NOT_EVALUATED**. Runtime factories/callers, IAM, packaging, committed policy activation, physical disposal, live clock/concurrency and deployed read/write enforcement remain outstanding.

CVO~Y evidence **9d33387734** on **6cacc80887** remains attributed wire/Mock evidence, not integrated repository acceptance. A future integrated fenced consumer review must retain delayed commit/client-clock/expiry crossing, accepted-row readability and crash/recovery controls; post-success refusal alone cannot undo a committed index row. No operating gate changes follow from either bounded closure.
