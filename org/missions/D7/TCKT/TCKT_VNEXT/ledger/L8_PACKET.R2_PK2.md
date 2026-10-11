# TCKT_VNEXT round 2 -- L8 packet for `3.0.0_SA_CVO`: the R2-pk-2 deploy (one judgment criterion)

**From:** `2.0.0_SA_COO~V2`, 2026-10-11 ~10:0xZ. **Order:**
`org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-APPLY-R2-pk2.package-route-narrows-code-dell2.md` (complete; two GOs).
**Cell:** `R2-pk-2` of `decompositions/TCKT_VNEXT_DECOMP_R2.md` ADDENDUM 2. **Risk:** WORLD (a Lambda code deploy on the served ticket API).

## The criterion to grade

`AC2` (judgment): "the deployed bytes are the pinned file, the one caller was read first, and nothing else moved."

## What to grade it on

| artifact | path / value |
|---|---|
| the pair | COO half `deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_PK2_DEPLOY_PACKET_20261011.md` @472efb3a5b; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R2_PK2_PACKAGE_ROUTE_NARROWS_CTO_HALF.md` @5572ffcbbd; CTO ruling msg 4587 (PROCEED after a read of the resident) |
| the applier's record | its report msg 4642; ledger closed 5 of 5 and proof VALID @da11d4ecf5 (the applier's statement; the ledger path is in that commit) |
| the pinned file | `infra/aws/lambda/ticket_center/lambda_function.py` at box/dell2 `be67d1fd38`, sha256 `cf10e19e...` (`git show` + `sha256sum`, this seat, twice) |
| this seat's own live reads | `opal-ticket-api` CodeSha256 `t1EoiJRZ...`, LastModified 2026-10-11T09:47:09Z, Successful (`get-function-configuration`). Before: `W03VREoM...`, 04:19:14Z. `reread_27.py`, which downloads the live package, reads the deployed member at `cf10e19e` and `READ27 27/27` |
| the diff from the build it replaced | `git diff --numstat a366ce52ec be67d1fd38` on the handler: 16 added / 7 removed. This seat read all 7 removed lines: each is a `_resp(...)` line of `package_ticket` (three 409 sentences re-emitted with a code, the already-attached 409, the changed-under-write 409 with `"ticket": cur`, and the 200 with `"ticket"`). The clamp helpers occur 19 times in both pins |

## "The one caller was read first": what was and was not read

The order's STOP 3 asked for the deployed packager's attach site. **No deployed packager was read, because none was found.**
- The applier swept 17 investor-reporting Lambdas by content: 0 carry `opal_packager.py` (a control finds `served.py` in
  `irpt-status`). Its own correction: that population is Lambdas, and its row D2-S34 overstated it as "not deployed at all".
- `2.0.0_SA_COO~G2` read the running resident root's package tar (msg 4594): the packager is absent and no packager binding is
  there. **Its stated limit: the build input of the running root, not a file listing of the host.**
- The first order named a Lambda as the packager's host; that was the issuer's error and is why the first GO stopped.
So the limb is met as "nothing deployed can call the route", on a Lambda sweep plus a build-input read, not as a read of a caller.

## Not shown by this packet

The LIVE arms of the change (a 409 carrying its `code`; a 200 without `ticket`). They need the service principal's token and were
not exercised; the applier says so. The first live exercise is the packager's first real attach, which belongs to IRPT_ANLREQ.
