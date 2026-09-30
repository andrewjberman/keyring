# DSGN_AMGTV1 task order -- `AV-p-4` -- THE SECURITY ANALYSIS SIDEBAR ICON SITS IN TOOLS, DIRECTLY BENEATH SECURITY SCANNER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-p-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~35</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN by the issuer at the cut on portal DEV 29c8226a -- sidebar.cjs 1 of 3 (FAIL as expected: the entry sits in the Analysis section between Philosophy and Positioning; the gate arm passes at base by design); green arm 3 of 3; admin-gate.test.ts 10 pass / 0 fail at base; on the issuer's green scratch root 9 of 10 with F49-AC8 (the App.tsx gate hunks) passing, the one fail being F49-AC10's `git rev-parse` at an outer root the scratch root lacks (environmental; your worktree has one); portal tsc -b rc=0 on the green arm. Blind spot: the sidebar's drawn position is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-p-4` (round 9, decomposition v9; DIRECT-ACT, Andrew-direct)

Andrew-direct, 2026-09-30 ~03:1xZ, verbatim: *"the Security Analysis icon in the portal sidebar is in the wrong location. It is a
tool, so it shoudl actually sit beneath the Security Scanner icon in the tools section."* The sidebar's one source is
`NAV_SECTIONS` in `portal/src/App.tsx`. Build, in that file only:
1. Move the `{ path: '/security-analysis', label: 'Security Analysis', icon: LayoutGrid, requiresDev: true, requiresAdmin: true }`
   entry, with its three-line AMGT_RESAPP comment above it, out of the section with id `analysis` and into the section with id
   `tools`, as the item DIRECTLY after `{ path: '/security-scanner', ... }`. You may add one comment line naming the move
   ("A tool, beneath Security Scanner (Andrew-direct 2026-09-30).").
2. Nothing else changes: the entry's label, icon and gate stay byte-for-byte; every other item of both sections keeps its order;
   the two `<Route path="/security-analysis...">` elements and their `ProtectedRoute requireDev requireAdmin` stay as they are.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component and test is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/App.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~35/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts` (it reads
`App.tsx`), and the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-p-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/sidebar.cjs"; echo "exit=$?"</invocation><expect>SECURITY ANALYSIS UNDER TOOLS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-p-4"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts; echo "exit=$?"</invocation><expect>10 pass and 0 fail -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the move read from `NAV_SECTIONS` (one entry, in Tools, directly beneath Security Scanner, every other item in its order,
label / icon / gate and both gated routes kept); AC2 the one test that reads `App.tsx` stays whole. This is a DIRECT-ACT cell: no
judgment criterion; its close is the issuer's walk, where the sidebar shows the icon beneath Security Scanner. Portal typecheck, if
you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~35/DSGN_AMGTV1.TO-AV-p-4.security-analysis-under-tools.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 9 = Andrew's direct word to this seat (decomposition v9), DIRECT-ACT path (one entry moved, LOCAL; no L2 /
L4-R / L8-L10). Base 29c8226a: sidebar.cjs 1 of 3; green 3 of 3; admin-gate 10 / 0 at base.

<direct_act>true</direct_act>
<status>complete</status>
<round>9</round>
<slot>~35</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
