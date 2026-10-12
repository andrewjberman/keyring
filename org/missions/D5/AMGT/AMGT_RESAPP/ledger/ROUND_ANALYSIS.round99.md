# AMGT_RESAPP -- ROUND 99, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~01:1xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4197, `surprise-channel/adjudications/ADJUDICATION_v120.md` @cba853b5db (MAY-CLOSE; 2 rows dismissed).

## 1. Graded

- **bf-1, the /14 second redeploy: APPLIED and holds**, by content (151 of 151 against merged pin `b3d4856531`) and live on `oEDHTRPq` (C-S97). As the CVO
  notes, it does NOT disarm AMGT_CORPUS C-S64: ROG's served team sheet still carries '660.45' in the period grid until /15. That row stays on AMGT_CORPUS's carrier,
  with /15 as its cell.
- **bf-2, the overlay tail read: MET (C-S98).** The CVO's own Logs Insights run reproduces every count: 32,528 invocations, 53 over 20 s, 12 cold, 49 pool-full,
  0 attributable to a route. Three of the four "unread" surfaces do not exist (no gateway access log, no function URL, no bucket request log). Only the client
  side is unread, and that is accepted: the pool warning already names the cause on the server side.
- **bf-3, the portal repoint: walked on DEV 0a06280a (C-S99).** The Model and Posture tabs render. Step 2 of the de-duplication is Andrew's PROD promote.

## 2. ENRICHMENT LIST (round 100, ONE issuance by `2.0.0_SA_COO~R1`)

1. **AMGT_CORPUS /15, the third redeploy** (ay-4 CTO half): from a merged pin, with bd-1's blobs unchanged; the baseline is `oEDHTRPq` (/14); the effect is BLOCK rows only; the
   post-act read is live vs live. It closes AMGT_CORPUS C-S64 on the served page.
2. **The connection pool** (bf-1 CTO half): read the HTTP pool size the code configures (or the client default) against the parallel storage reads' thread count,
   set them consistent, under a redeploy pair. Close: the next day's count of invocations over 20 s and of pool warnings, against 53 and 49.
   - These are TWO served changes, so they ride TWO applies, in this order: /15 first (its read is AMGT_CORPUS's grade), then the pool. They are never
     folded into one, so that each read attributes its own effect.
3. **ss-7 / pp-4:** STAGED on MDPF_DEMQUE's CRNCY answer. Carried.

## 3. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote (`dell1-20261011T033643Z-e7f2`). It gates the payload de-duplication's step 3.
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~01:5xZ) -- bg-2's deviation CONFIRMED: one shared S3 client per container is the lever; pool 32 sized to its measured peak

`2.0.0_SA_COO~R1` msg 4199, under `AMGT_RESAPP.TO-AMGT-bg-2` (evidence `deliverables/2.0.0_SA_COO~R1/round100_prep/checks/r100_cold_request.py`). A container's first overlay request builds
146 S3 clients (`scoped_amgt._s3_client()` per call) for about 242 requests.
- In fresh processes against the live pool, raising the pool alone from 10 to 32 read 11.1 s and then 11.4 s: no gain.
- ONE shared client read 7.8 s, peaking at 20 concurrent connections. So the pool is sized 32.

My item 2 said "set the pool consistent", and the measurement shows the pool was a symptom: client construction per call is the cost. **The cell as cut is
confirmed.** It is the same shape as the module's own `_dynamodb()` (AMGT-au-6): one lazily built client per container, reused across invocations (a boto3
client is safe to share across threads), with `max_pool_connections` 32.
- **Close (bg-3's pair):** the next day's count of invocations over 20 s and of pool warnings, against 53 and 49.
- **Plus a served-bytes arm:** the overlay, peers and thesis responses are byte-equal before and after (clocks apart). It is a performance change, and it must move no
  byte.

-- 1.0.0_SA_CTO~DELL1
