# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the admin + internal + Dev UI-walk principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`
blob `1301fcffcda6401269e72f85017ed3a56f7e8e2c` @`d6c195b6dd`. The blob is the same at HEAD and on disk (read
2026-09-26 ~13:3xZ).
**First half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md` (msg 101160).
**Asked by:** 2.0.0_SA_COO~P msg 101154 and 1.0.0_SA_CTO msg 101160. This seat is not in the act.

## VERDICT: REFUSED on blob 1301fcff -- one defect, one amendment, then this seat signs the new blob

The authority, the key list and the rollback are sound (section 2). The defect is the AUDIT: the page the walk exists to
exercise sends POSTs as part of ordinary reading, and one of them persists a record. So the packet's limit ("page reads
only") and its audit ("0 requests whose method is not GET/HEAD outside `/auth/login` and `/auth/refresh`") both fail on
a CORRECT walk. Branch (d) fires every time: a BLOCKING row plus an escalation to Andrew, on a walk that did nothing
wrong. A detector that fires on the correct case cannot tell it from the wrong one, so the half covers only one
branch and cannot be signed.

## 1. The defect, measured at source (`portal/src` at HEAD)

- **The page issues `resolve-scope` on load.** `portal/src/pages/InvestorReporting/index.tsx:79-89` runs it as a query
  when the page mounts. The route is `POST ${IR_ROUTE_BASE}/directory/resolve`
  (`portal/src/api/endpoints/investor-reporting.ts:208`). It is a read, sent as a POST.
- **The page issues `selection-create` on each selection.** `index.tsx:157` calls `api.createSelection`, and the route
  is `POST ${IR_ROUTE_BASE}/selections` (`investor-reporting.ts:206`). The handler PERSISTS a record:
  - `create_selected_set` "Persist[s] the exact requested members before exposing their URL reference"
    (`infra/aws/lambda/investor-reporting/directory/entry.py:261-269`);
  - the store holds "Immutable selected-set records in the existing tenant-keyed request table"
    (`infra/aws/lambda/investor-reporting/_scope/selection_store.py:1`).
- The walk grades IVE30-AC3 plus the round-3 and round-4 criteria, and it cannot select an account without this write.

## 2. What this seat measured and accepts

- **Authority:** Andrew's verbatim choice "Agent on an admin+dev login" is in the CTO's record at `@e2eae53ae3`.
  Unlike blob fe8e8d89, the principal's class is Andrew's own word.
- **Rollback of K1 and K2:** unchanged from fe8e8d89. This seat's half `@909dd40acc` measured the served
  auth-handler's status guards and the refresh row re-read, and found `opal-users-v2` has no stream or event-source
  mapping. That closure was re-verified at 08:4xZ: 0 walk rows of 79, and a positive control found 1.
- **One world-effect surface is closed by a mechanism this principal does not hold.** Trade approve, reject and
  execute require membership in a `trade-users` group, looked up by e-mail; the `role` and the Dev bypass do not grant
  it (`infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py:118-135`). The walk's `.test`
  e-mail is in no group. So the session cannot approve or execute a trade, including the PENDING_APPROVAL PFOE
  submission `TRADE-20260925-183318-731E1A`. This finding is at source only.
- **The superadmin radius as stated** (`/auth/admin/*` create, delete and reset; all firms; every admin page) is
  accepted on the CTO half's terms. The bound is the interval plus the script, and the HAR proves the script.

## 3. The amendment that makes this signable (one edit, a new blob)

1. **Grade the audit by ROUTE, not by method.** The HAR census prints a count per route, with its denominator, and
   requires:
   - allowed non-GET: `POST /auth/login`, `POST /auth/refresh`, `POST .../investor-reporting/directory/resolve`,
     `POST .../investor-reporting/selections`;
   - **zero** of: `POST .../analysis/inputs`, `POST .../analysis`, `POST .../export`, any request to `/auth/admin/`,
     and any other non-GET/HEAD anywhere.

   Branch (d) fires on a nonzero forbidden count, never on an allowed route.
2. **Name the selection records as a key (K3).**
   - What: each `selection-create` writes an immutable selected-set row in the IRPT request table, keyed by firm and
     reference.
   - The packet states the disposition: delete after the walk, with the rows named in the ledger, or accept them as
     residue with their count recorded.
   - Add the table to the step-2 pre-read census and the step-7 re-read.
3. **Reword the CTO limit** from "page reads only" to "page reads, plus the page's own selection records (K3)", so
   the limit describes a walk that can happen.

This seat signs the amended blob on sight if it carries these three and nothing else changes. The CTO half re-signs
on the new blob, because both halves bind to the blob.

## Not measured by this seat

- The served bytes of the portal bundle, the IRPT directory Lambda and the trade-workflow-handler. The findings above
  are source at HEAD.
- Whether any other page component fires a non-GET on load. The route-graded census in amendment 1 catches one if it
  does.

---

## v3 (~13:4xZ): SIGNED on blob 07b7a000 -- K4 included

**Packet v3:** blob `07b7a0006c5739e5d7659596b2fc5c8d92910956` @`5c7787839b`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101182).

**v2 (blob `4ae2693b` @`b108b016cb`) was never signed by this half.** Its K4 said the upload "makes no vendor call".
2.0.0_SA_COO~Y (msg 101180) reported one resident YCharts `securities_info` GET, and 2.0.0_SA_COO~P re-cut K4 as v3
before this half landed. The CTO's re-sign (msg 101177) is on v2, so the CTO half is owed again on v3.

**The three amendments from the v1 refusal are carried**, checked against the v1->v2 diff:
- the HAR is graded by route, with a class table and a zero out-of-class count;
- K3, the SELECTION# rows, is named, with a before/after census. The rows are retained: content-addressed, carrying no
  identity, and shared across principals, so a delete could break another holder's reference;
- the limit reads "page use only: reads plus the page's own selection writes".

This seat accepts K3 as retained.

**K4 is accepted as re-cut (v2->v3 diff).** It changes only the K4 section, the limit line ("Plus K4: ~Y's ONE upload
and the ONE resident `securities_info` GET it causes") and the not-covered line ("Any vendor call other than K4's one
resident `securities_info` GET"). Nothing else changed.
- **The act:** exactly ONE `POST .../analysis/inputs`, tenant `cottonwood`. The outcome is read through DynamoDB and
  S3 only, never by re-POST.
- **The vendor call is named:** ONE batched YCharts `securities_info` GET by the resident, 2 symbols, no prices, under
  the standing host-workflow authorization (CTO 100667 (1)). It is ledgered with the resident's log line as its
  receipt, and it is the only vendor call the window admits.
- **The write set** is given per branch (NORMALIZED / NEEDS_CORRECTION / RETRY), taken from ~Y's write set
  @`5d70021540`, and all of it is retained as the acceptance evidence of ledger `irpt-upload-hop2-20260924` S1.
- **The audit's K4 class** is exactly one `/analysis/inputs` POST by ~Y. A second one is branch (d).

This seat did not re-read `intake/upload_resolution.py` or `resident_worker.py`. The GET count rests on
2.0.0_SA_COO~Y's reading of its own producer.

---

## v5 (~14:1xZ): SIGNED on blob 6813377a -- K5 included

**Packet v5:** blob `6813377a97a08f2f8bc6a9115fe4a35478d720b1` @`7079ca4934`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101215). The CTO said YES to hop 3 in this window in msg 101205, with a 14:35Z cutoff.

**v4 (blob `446b3ad9` @`9fa4927cec`) was never signed by this half.** Its K5 named the four vendor writes and nothing
else. 2.0.0_SA_COO~Y (msg 101211) reported that the recipe also makes YCharts reads and that a RETRY is redelivered.
v5's diff against v4 is exactly that line and the matching not-covered wording (this seat's condition, msg 101212).
The CTO half is signed on v4 (@`c1c1e77077`) and says it stands on a re-cut that adds only this line (msg 101219).
The packet asks that both halves NAME the blob at HEAD, so 1.0.0_SA_CTO names `6813377a` in its record.

**Diff v3 -> v4 (carried into v5):** the K5 section, the limit line, one route-table row ("POST, exactly 1, by ~Y,
`/analysis`"), the forbidden line "any second `/analysis` POST", the vendor not-covered line, and the sign-against line.
Nothing else changed.

**K5 accepted:**
- **The act:** exactly ONE `POST .../analysis` (Overview) by 2.0.0_SA_COO~Y on K4's normalized input. It is observed
  by DynamoDB and S3 reads only: no re-POST, no retry. A provider error is the reported outcome.
- **Vendor writes:** named and kept -- one YCharts `holdings_upload`, `portfolio_create`, `report_create`, and one PDF
  download.
- **Vendor reads and redelivery:** named. They are the recipe's YCharts reads (identity, template, upload echo,
  7-setting read-back, validate), and queue redelivery of at most 5 receives, each resuming from the job row's
  checkpoints so that no create repeats. The redelivery is the queue's, not a retry by ~Y.
- **Authority:** Andrew-direct ~03:0xZ, verbatim "egress is permitted for API calls" (CTO msg 101098 / 101100), which
  makes vendor API calls in this session ledgered rather than per-use.
- **What leaves the platform:** the input is the two-row synthetic file
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv` (`AAPL,10.01` / `VNQ,2.02`, read here), so no
  client holdings or identity reach YCharts.
- **Cutoff:** this signature lands before 14:35Z. If the CTO half does not name `6813377a` at HEAD by then, K5 is
  skipped per the packet, and this signature does not extend it.

**Not measured by this seat:** whether `irpt-ycharts-generate` runs this live. Its `lambda_handler` refuses a live
transport without `IRPT_LIVE_YCHARTS_CALL` (`ycharts/generate/job.py:602`), and the resident path is ~Y's to state. A
refusal is K5's reported outcome, not a new act.

---

## v7 (~15:0xZ): SIGNED on blob 3edebd85 -- window 2 (new principal, K4 + K5 again, K6)

**Packet v7:** blob `3edebd851f9c5c3a035d83f17293278796a5f1c3` @`683e73871e`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101253). Asked by the CTO in msg 101242; the CTO half is signed on v7 (msgs 101257, 101259).

**v6 (blob `71146fdd` @`34f4619882`) was never signed by this half.** Its K5 bound window 1's input
`portfolio_99e76df8..`, owned by the deleted principal, while its K5 order line said "K4's new input"
(2.0.0_SA_COO~Y msg 101249). v7 changes only that line and one header line (diff v6->v7 read), so K5 has one
reading: exactly one POST on the input THIS window's K4 normalizes.

**Window 1's principal is gone, read by this seat at 14:56Z:**
- `opal-users-v2` holds 0 `usr_irptuiwalk` / `irpt-uiwalk` rows of 79 scanned, with a positive control of 1 of 79;
- `/irpt/ui-walk-principal` holds 0 parameters.

**Diff v5 -> v6 (carried into v7), all accepted:**
- a NEW principal of the same K1 shape, and its times;
- K4 and K5 run again as signed in v5, in order, one POST each. The 14:35Z cutoff is replaced by the principal's own
  60-min life;
- **K6:** ONE 49F account-level Performance read by the page (one `/selections` POST under K3, one Performance GET). It
  is deploy (B)'s real BEFORE baseline per ruling (c). The report it retains (`REPORT#` / `RETENTION#` rows and object)
  is kept, and no vendor call is made;
- deploy (B) stays OUT of the window, and no FWD-1 re-trace rides it.

**One item named, not a condition on K1-K4 or K6:**
- K5's vendor authority is Andrew-direct "egress is permitted for API calls", which CTO msg 101098 records as "Egress
  for this session", in the same message that re-armed the FAST leases to 15:01Z.
- Window 2 opens after 15:01Z.
- This half reads "this session" as Andrew's working session, not the lease. That reading is 1.0.0_SA_CTO's to
  confirm, because the CTO recorded the word.
- If the CTO says it lapsed with the lease, K5 is struck by this half and hop 3 goes to Andrew's own upload and
  Generate.

---

## v8 (~16:4xZ): SIGNED on blob acca1b3e -- window 3 (new principal, K4 + K5 again; K6 not re-run)

**Packet v8:** blob `acca1b3e275ae7f724127869f39bb17409f1560f` @`b17feaa434`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101321). The CTO signed on the same blob (msg 101324).

**Diff v7 -> v8, read:** one header block only (11 lines), accepted:
- a new principal and its times;
- K4 and K5 re-run;
- K6 done and not re-run;
- the IAM simulation pinned: ~Y @`2789ac3bbd`, and P's corroboration @`c2349731ac`.

**The header governs the unchanged K6 section.** The K6 section's text still reads as an act, while the header says K6
is not run. Any Performance GET in window 3 is an ordinary page read under the GET class, and it retains a report as
every human read does. No second K6 baseline is taken.

**The egress item named at v7 is closed.** The CTO half grounds K5's vendor GET in "this session's egress arm"
(@`ce6aa15a17`, Andrew-direct ~03:0xZ, "egress is permitted for API calls"), the self-drive arming record, not the
15:01Z lease. Andrew's resume "recs approved for all" (@`a6700b211e`) lifted the pause. K5 runs.

**Window 2 is closed:** ledger `irpt-ui-walk-principal-w2-20260926` CLOSED 15:40Z (packet header). This seat did not
re-read that principal's deletion.

---

## v9 (~17:4xZ): SIGNED on blob c8da5676 -- window 4 (R1 AFTER read, the first real export), with one condition on K7

**Packet v9:** blob `c8da567612cac3d21df2e296ef4c2f0d6b920b0a` @`825b320ab0`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101371).

**Diff v8 -> v9, read:**
- a header block;
- the K7 and K8 sections;
- one route-table row ("POST, exactly 1, by ~D, `/export`").

Nothing else changed. K4 and K5 are not run.

**Window 3 is gone, read by this seat at 17:38Z:** `opal-users-v2` holds 0 `usr_irpt*` / `irpt-uiwalk` /
`irpt-walk` rows of 79 scanned, with a positive control of 1 of 79, and `/irpt` holds 0 SSM parameters.

**K8 (E1) accepted as written:**
- exactly one `POST .../export`, then the receipt and one download read;
- the writes are named and kept (bundle, grant, `pending.json`, PDF, receipt, one `SendCommand`);
- the one render token lives under the S148 fence and is deleted on every terminal path, with P reading
  `ParameterNotFound` after;
- no vendor call.

This is the first time a PDF is served. It is a PDF of a report its requester already reads (export deploy (B)
radius, branch R).

**CONDITION on K7 (R1): a REOPEN is not the AFTER measurement.**
- The packet itself says the page may reopen K6's retained report `RPT-39e26fcd..` (the accepted pointer). If it does,
  the YTD shown is the same stored value K6 computed on the pre-D1 build. It matches 0.06854 whether or not D1 changed
  the computation, so the check cannot fail and proves nothing about D1.
- So R1 satisfies export deploy (B)'s AFTER arm (ruling (c), msg 101313) ONLY if the answer is a RECOMPUTE on the D1
  build: a new `REPORT#` id, or the adapter log for that request showing the compute path on the D1 code.
- **If it is a reopen, this is NOT a STOP and NOT a rollback.** The AFTER arm stays OWED. Ledger
  `irpt-export-deploy-b-20260926` keeps R1 open, and the result names it "reopen, not the AFTER read". A recompute is
  obtained in a later window, by whatever the adapter's own reuse rule requires. That rule was not read here.
- Latency: only a recompute's time is an S147 measurement, as the packet already says.

**v9 K7 VOID (~17:5xZ), on 1.0.0_SA_CTO's HOLD (msg 101397).** v9's K7 gate "YTD equals 0.06854, else STOP and roll
back" rests on a wrong baseline: K6's report reads YTD 0.07333839362957217 over 01-02..09-25, and 0.06854 is its 09-24
point (this seat's export-B half @`6fb82db891`; 2.0.0_SA_COO~P msg 101394). A correct page read would therefore have
rolled back a working deploy. This seat missed it at v9. Its own reopen condition did not test the number itself.
- This half's v9 signature does NOT cover K7 as written, and window 4 does not run on v9.
- R1 is closed by the recompute proof (`RPT-e0a917d2`, 184 of 184 points equal).
- This half signs v10 on sight if its only diff is K7 re-cut as the CTO set: the page read the export uses passes when
  a computed or reopened report for that account renders, and it triggers no rollback. K8 follows K7.

## v10 (~18:0xZ): SIGNED on blob 32c85e40 -- only K7 re-cut

**Packet v10:** blob `32c85e40136fbda4ddca0121a7e629d4f91a08b5` @`d0c7306a20`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101402).

**Diff v9 -> v10, read:** one header line, one bullet's wording ("K7, the page read K8 exports"), and the K7 section.
Nothing else changed. K7 now:
- closes R1 by the recompute proof (`RPT-e0a917d2` equals `RPT-39e26fcd`, YTD 0.07333839362957217, series identical);
- withdraws the 0.06854 baseline;
- passes when a computed or reopened report for that account renders, and triggers no rollback.

The one addition beyond the CTO's wording is ONE reload if the gateway cuts the browser off (S147). A second
Performance GET is inside the GET class, so it is accepted. K8 is unchanged and follows K7. v9's K7 void no longer
applies.
