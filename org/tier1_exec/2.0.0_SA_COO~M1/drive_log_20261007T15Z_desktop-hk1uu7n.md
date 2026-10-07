# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-07 15Z

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL each tick. From ~15:0xZ the project is in RELEASE MODE (CTO round-11 analysis
@fc96f7c48c): no round-12 issuance until e59 is on DEV and at most 2 held lines remain.

| tick (UTC) | limb | outcome |
|---|---|---|
| ~15:0xZ | L7 -> L8 | e66 drained as `secclass-r11-held-silver` @0859b56dbf; DRAIN_END_R11 @ae61f93efe to the CVO |
| ~15:0xZ | release | release mode ruled (msg 352). e65 found short of v0.16 and not separable from e44 -> amendment 2 @42730b6f02 (slot ~49, base ae61f93efe) |
| ~15:1xZ-15:2xZ | release | W49-S1, the issuer's own paths-block defect, repaired @4f0b68c9ce. e65 re-seated and drained `secclass-r11-held-e65`. Request 1 @00e7bf2cb5; CTO half (msg 362) -> TO-DEPLOY-e65 GO @998a30201b |
| ~15:3xZ-15:4xZ | release | request 2: e57+e61 clean port (~50, 37fdf53bdc) on `secclass-r12-rel-e57e61`; CTO half @bdfdc93b0d -> TO-DEPLOY-e57e61 GO @ceb123802f. S57 (held-32 test key) covered by the CTO addendum @d8d0c6ed22 |
| ~15:4xZ | release | e59 ON PORTAL DEV fc18e50bc4 (Andrew's word, msg 370) |
| ~15:5xZ-16:0xZ | release | request 3: e62+e56 clean port (~51, 01e843ce2e) on `secclass-r12-rel-e62e56`; half @92b780879e (one IR bundle key) to the CTO |

Decisions closed this hour:
- Each held cell releases on its own clean port onto the CLOUD base, never by dragging its held line's other cells.
- A flat deploy order's complete flip is the assignee's (CTO 301). The `_shared` members ship only through an explicit safe-deploy on
  carriers.
- ~S runs TO-DEPLOY-e65 first, then TO-DEPLOY-e57e61 (laptop 106367).

Owed:
- the e53 `multi_asset` census (opal-data-bd, 25,259 keys; 49financial denied to dell1);
- request 4, e44 (+e63);
- the E_18 read (BD 23:00Z);
- the e42 L2 read (2026-10-08T12:45Z);
- the S57 disarm on the held-32 push read.
