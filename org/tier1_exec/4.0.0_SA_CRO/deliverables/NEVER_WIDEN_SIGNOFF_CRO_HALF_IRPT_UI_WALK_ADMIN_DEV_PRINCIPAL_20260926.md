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
