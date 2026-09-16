# Responsive daily report

Owner: `1.0.0_SA_CTO~A`. Authority: `ANDREW_DIRECT.md`; Msg96840 scope and
Msg96849/96851 correction. Report day: 2026-09-14.

Both legacy output filenames now contain the same responsive document. Above
940px it shows the rail and selected detail; at smaller widths every item is
expanded in its original order. Chart labels adapt below 600px. Resizing and
rotation preserve the selected item and document. Titles remain fully visible;
the renderer still rejects sprint card text over 52 characters.

The presigned entry opens that document without device detection. The Gateway
source skips its old narrow-screen redirect for responsive reports, retaining
the redirect for archived fixed layouts. Authentication, roster checks, object
selection, cache controls and security headers are unchanged.

## Validation before publication

- Both 2026-09-14 variants passed all existing renderer validation, palette,
  visualization parameter and directive coverage checks. Renderer changes are
  limited to the mobile filename's template mapping.
- A 53-character card negative control was rejected.
- Eight Gateway regression checks passed, including legacy redirect retention
  and responsive redirect suppression.
- Microsoft Edge 153.0.4234.32 via Playwright: 324 browser measurements across
  both files, the presigned entry, latest Gateway handler and both explicit
  dated variants. Mouse and touch contexts at 1280/1024/900/390px; every rail
  entry; phone and tablet rotation; narrowing and widening the same document.
- Zero horizontal overflow, clipped titles, missing diagrams, invalid rendered
  values, script exceptions or browser console warnings/errors. Both activity
  charts rendered in every case. Selection and URL survived every resize.
- Phone and desktop screenshots were inspected. Evidence is in
  `BROWSER_ACCEPTANCE.json` and `PREVIEW_390.png` / `PREVIEW_1280.png`.
- Python compilation and scoped `git diff --check` passed.

Browser Gateway checks replace only the identity/roster and S3 seams and silence
audit writes. They do not prove live ALB sign-in. The ALB egress/sign-in work is
separate and belongs to base CTO.

## Publication and rollback

Before publication, all four live report objects were read and their embedded
report data compared with the tested render: identical. Five original objects
(dated pair, latest pair, entry page) were saved privately under
`%LOCALAPPDATA%/CodexSeatScratch/1.0.0_SA_CTO~A/daily-responsive/before-publish/`.
`BEFORE_PUBLISH.json` records their hashes and S3 version IDs without signed URLs.
The existing publisher is the publication path, followed by object readback and
live presigned browser checks. Publication receipts are recorded separately.

Publishing both aliases makes the responsive report available to the existing
Gateway without a service deployment. Its deployed legacy entry redirect can
still choose a filename once; either filename now resizes correctly. The source
cleanup removes that unnecessary hop on the next Gateway release. No Gateway
service deployment or ALB change is part of this publication.

CLOUD push and CLOUD-to-SITEZ merge remain held.
