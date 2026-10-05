# DSGN_AMGTV1 task order -- `AV-zr-1` -- DIRECT ACT: SECURITY ANALYSIS IS OPEN TO EVERY OPAL EMPLOYEE (requireInternal, no Dev or admin gate)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~102</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; a static read of the route gate in two source files. The scoped AMGT API checks only the edge-injected firm identity (lib/research/api/scoped_amgt.py `_firm_id`), no Dev or admin role, so no backend change is needed for an internal viewer.
comp-adversary: RUN by the issuer at the cut on portal DEV 71097b53 -- access40.cjs 2 of 4 (arm 1 FAIL: the nav entry carries requiresDev + requiresAdmin and no internal tier; arm 2 FAIL: both routes sit behind ProtectedRoute requireDev requireAdmin; KEEP and PLANTED pass). It reads 4 of 4 on a scratch copy with the intended three-line edit.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zr-1` (round 40, decomposition v40; a DIRECT ACT)

Andrew-direct 2026-10-05 ~15:0xZ (org/tier1_exec/2.0.0_SA_COO/deliverables/
ANDREW_DIRECT_20261005_150xZ_SECURITY_ANALYSIS_ALL_OPAL_EMPLOYEES_REQUIREINTERNAL_LEADPANEL_LOAD_TO_COO_Z.md), verbatim: "It should be
visible for all Opal Employees", "should not require admin access to see", "but yes, requireInternal is the correct approac".

In `portal/src/App.tsx` the Security Analysis page is gated to Dev users who are also admins:
- the nav entry (`~:134`) is `{ path: '/security-analysis', label: 'Security Analysis', icon: LayoutGrid, requiresDev: true,
  requiresAdmin: true }`;
- both routes (`~:470-471`, `/security-analysis` and `/security-analysis/:securityKey`) sit behind `<ProtectedRoute requireDev
  requireAdmin>`.

Change it to the house pattern for Opal-only pages:
1. **Nav entry:** `{ path: '/security-analysis', label: 'Security Analysis', icon: LayoutGrid, requiresTier: 'internal' }`. That is
   the internal tier, as Investor Reporting's entry reads it, with no `requiresDev` and no `requiresAdmin`.
2. **Both routes:** `<ProtectedRoute requireInternal>`, with no `requireDev` and no `requireAdmin`. This is Ticket Center's guard:
   `requireInternal` is `claims.firmId === 'opal-capital'` in `src/components/ProtectedRoute.tsx`.
3. **The comments** above the nav entry and above the routes: replace the "Dev + admin ONLY (Andrew-direct 2026-09-17 ...)" lines
   with one line citing the record above, e.g. "Open to every Opal employee: requireInternal (Andrew-direct 2026-10-05 ~15:0xZ)".
   - Leave Investor Reporting's entry, route and comments exactly as they are; its gate is unchanged.
   - In the 2026-09-22 comment that says Investor Reporting matches "Security Analysis's Dev + admin gate below", drop only the
     clause naming Security Analysis.

Partner firms stay out through the deny-by-default firm allowlist (`src/lib/firmAccess.ts`). Do not add `/security-analysis` to it.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only `portal/src/App.tsx` changes (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep the file's line endings.

## 3. SURFACES

<paths>
portal/src/App.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~102/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zr-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round40/checks/access/access40.cjs"; echo "exit=$?"</invocation><expect>SECURITY ANALYSIS IS OPEN TO EVERY OPAL EMPLOYEE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zr-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~102/DSGN_AMGTV1.TO-AV-zr-1.security-analysis-all-opal-employees.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W102-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** the Andrew-direct record above, which supersedes the Security Analysis gate words of 2026-09-17 and 2026-09-22 for this
  page only.
- **Sequencing:** MSTR~Z msg 29616 answered (a). r39 71097b53 pushed first; this edit stacks on it.
- **Not this cell:** the Lead Panel's slow load (Andrew: to COO~Z, msg sent 15:03Z).

<status>complete</status>
<round>40</round>
<slot>~102</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
