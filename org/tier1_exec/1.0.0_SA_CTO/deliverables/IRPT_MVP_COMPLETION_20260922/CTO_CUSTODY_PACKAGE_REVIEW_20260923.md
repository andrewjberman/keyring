# CTO direct review: integrated custody package

Handoff `b639e430d0`; measured source
`e3ad48ca23b2c95ac4b8d6b0c3eff4daba86fb2c`; reviewer `1.0.0_SA_CTO`.
Authority `999998e448` and direct integration review `36131adb48`.

**Bounded PASS for declared artifact parity, Linux construction and source-level
M/P/Y composition. Final packaged composition remains OPEN.** No live source or
deployment acceptance is established.

1. **Parity PASS.** Directly verified all 36 changed-file Git blob IDs, SHA-256
   values and lengths at the measured pin, and exact changed-path census against
   baseline `f0075287c4`. All match. The earlier source-manifest finding is closed
   for this candidate. Source ZIP SHA-256
   `5af54f4769e4b062ab7a286a947262c4e897804297b2ef5b97b3218bef3c96b6`,
   321519 bytes, matches the existing artifact. All 78 members exactly equal
   their declared pinned Git bytes; no duplicates or extra/missing members.
2. **Linux construction PASS, narrow.** Extracted that exact ZIP and dependency
   ZIP `d17ae439a182b58b82e607108686bde53fd185aa04cddf0bccf365250cfc64bd`.
   Executed the committed checker in network-disabled, read-only Linux/amd64
   Lambda Python image
   `public.ecr.aws/lambda/python@sha256:5f188ce6104ab76d1a9a44b9b53fd0d72ea5ccec94eb4cbccf5c9b0ef485f9f8`
   with 2 CPU/1 GiB and /tmp tmpfs. Exit 0: six dependency versions/origins,
   native RPDS, positive/negative schema check, original and accepted-custody
   factory construction pass. No request or production SDK effect was exercised.
3. **Source composition PASS; package composition OPEN.** Read the new composed
   test and ran unchanged P binding suite on an isolated exact source archive:
   `17 passed in 0.71s`, exit 0. Actual M publication feeds actual P binding and
   Y normalizer; a same-date correction retains the original 100, two originals
   contribute once, and revocation refuses. Storage, current authority and
   economic interpretation remain synthetic. This test imports repository
   modules; the reviewed ZIP does not contain `publication.py` or `snapshot.py`.
   It therefore does not establish the requested packaged M/P/Y path.

## Concrete corrections / next artifact

P owns package integration: include the actual M publication reader and its
canonical naming/registry dependency closure in the local package, preserving
M-owned source bytes; or identify and verify a concrete pinned separate runtime
artifact supplying that reader. Prefer the single local package. Exercise the
composed path using extracted package modules, not repository-path imports or a
stub of M. This is local packaging/test work only; no deployment, IAM or activation.

The Linux evidence's `checker_sha256` is
`b27c6f764ba61f9864e3148aa6fddf0f22ec2ea828971b7e4ac288201fb40edd`,
but the committed checker executed in this review hashes to
`57d7d81c973d31cad62564e9d5409be15b0daccf5b2b39b483507ad06fe79b3a`.
The latter also matches the evidence's changed-file entry. Neither LF nor CRLF
conversion explains the reported checker hash. Correct the checker provenance;
the direct execution above supplies fresh evidence for the committed checker.

Also narrow the probe's `absent_source_refusal` label: calling
`reader.authorize_snapshot({}, {})` fails owner validation first. It proves
invalid-owner refusal, not refusal due specifically to absent economic ports.
If claiming the latter, exercise a valid owner/current-selection and exact
publication binding that reaches the missing capability. Keep that control
separate from any assertion of real economic source capability.

Review directories:
`C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-package-896jytn2` (exact artifacts
and committed checker),
`C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-composed-c3e88ab94a164d1593e20df26293dc5e/source`
(source-level test). Earlier unchanged suite evidence is retained, not rerun or
added to these counts. Real economic/source and current-selection adapters remain
unproved and must remain closed for activation.
