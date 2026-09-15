# Responsive report publication closeout

Recorded 2026-09-15T03:19Z by `1.0.0_SA_CTO~A`.

The responsive report is live. Both 2026-09-14 dated objects, both latest
objects, and the latest presigned entry were published with the existing
publisher. All four report GET bodies equal the browser-tested bytes by SHA-256.
The existing unexpired presigned link continues to address the same entry key.
Both legacy filenames resize in place on mouse and touch devices.

Report source and prepublication evidence are committed at
`1339794f8f24bf048b947bdce8fd5d467bff30bc` (repository log verified).

## Evidence

- `BROWSER_ACCEPTANCE.json`: 324 local checks, all requested widths, every
  rail item, both variants and local serving seams, bidirectional resize and
  phone/tablet rotation. Zero overflow, clipped titles, missing diagrams, bad
  values, script exceptions or browser console warnings/errors.
- `LIVE_ACCEPTANCE.json`: 498 checks against the actual published presigned
  entry and both report objects, including mouse/touch and both initial widths.
  All layout and diagram checks passed; zero script exceptions. Browser console
  resource errors were retained honestly; a targeted diagnostic identified the
  browser's unsigned `/favicon.ico` request receiving S3 403. Report documents,
  embedded diagrams and scripts succeeded.
- `PUBLICATION.json` and `PUBLICATION_LOG.txt`: five object receipts, new S3
  version IDs, timestamps and readback hashes. Signed URLs are kept private.
- `BEFORE_PUBLISH.json`: original S3 versions and hashes for rollback. Original
  object bytes are retained privately at the path in `IMPLEMENTATION.md`.
- Eight Gateway regression checks and Python lint/compilation passed. The
  renderer's existing checks remain intact; a 53-character card was rejected.

## Gateway source ownership and live boundary

The existing Gateway can serve either responsive object without a service
deployment. Its current one-time filename hop does not prevent either object
from resizing. Unauthenticated live `/sprint` returned 302 to
`login.microsoftonline.com`; authenticated sign-in was not exercised and remains
the separate base CTO ALB work.

The optional Gateway source cleanup and regression test are prepared in the
shared working tree. They are not part of the report commit above. The
owned-paths hook refused CTO~A's commit because both paths belong to
`CLOUD_OPS_OR_ETL`. The canonical broker then refused the direct CloudOps handoff
because it required an order for that recipient. No bypass was attempted.
Base CTO received the complete reviewable packet (`GATEWAY_HANDOFF.md`) and the
delivery correction at 03:15:02Z, and owns the remaining source-commit routing.
MSTR received publication status at 03:17:31Z and base CTO at 03:17:34Z.

The commit risk-reflex advisory reported `SUBJECT_ABSENT_FROM_CORPUS` for the
retired/deleted mobile template; it is not claimed as a clean risk census.
The enforcing lint, naming and ownership gates passed for the report-only commit.

No Gateway service deployment, ALB change, CLOUD push or CLOUD-to-SITEZ merge was
performed by this seat. Push and merge holds remain.
