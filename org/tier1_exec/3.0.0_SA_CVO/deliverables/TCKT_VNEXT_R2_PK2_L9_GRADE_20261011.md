# TCKT_VNEXT round 2 -- L9 grade of TO-APPLY-R2-pk2 AC2 (the package route narrows)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T10:04:42Z. Row TCKT_VNEXT-D2-S35.
**Input:** `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R2_PK2.md @5047fa86e6 (msg 4656)`. This seat downloaded the live package and read CloudTrail and the packager's source itself.

| limb of AC2 | verdict | this seat's evidence |
|---|---|---|
| the deployed bytes are the pinned file | **MET** | The live package hashes to the function's CodeSha256. Its one member is byte-equal to the handler at `be67d1fd38` and differs from the handler at the build it replaced |
| nothing else moved | **MET** | The package holds 1 member. CloudTrail since 04:00Z shows one code update at 09:47:09Z and no configuration update |
| the one caller was read first | **MET, in a narrower sense than the words** | No deployed caller exists to read (the applier's sweep of 17 functions and the resident's build input; not re-run here). This seat read the caller's source: its attach branches on the status alone and reads nothing from the 200 body, so removing `ticket` from that body cannot break it |

**Verdict: AC2 MET.**

## What this grade does not cover

- **The live arms were not exercised.** No request has shown a 409 carrying its code or a 200 without `ticket` on these bytes. The
  first is the packager's first real attach.
- **That attach is itself blocked upstream.** The packager's read of the ticket is refused 403 (IRPT_ANLREQ row D2-W66-S1). The
  packager reads `ticket.package` from the GET, not from this route, so this change does not affect that read.
- "No deployed packager" rests on a build input, not a listing of the host. If a packager is ever found running, this limb is re-read.
