# DSGN_AMGTV1 task order -- `AV-k-3` -- PEERS HAS A DESIGNED EMPTY STATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~53</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the render run serves a page build from disk with fixtured API reads.
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- peersempty.cjs 1 of 3 (FAIL as expected: fwd19 FAIL, missing "peers/empty (no designed branch is reachable)", perPanel.peers empty 0, peers-empty.png 0 bytes; the Peers tab on an ABSENT peer read renders no PanelEmpty; arm 3 is the control -- the base page reads fwd19 FAIL and a blank page NOT_EXERCISED -- and passes at base by design); green arm (scratch r14-green-c @b7931ed3, an issuer-spawned helper; 4 files, +47/-13) 3 of 3 (fwd19 PASS, peers-empty.png 148414 bytes reading "No peer set for this name yet."); bytes 3/3; portal tsc -b rc=0; all 16 page harnesses green with two granted re-anchors; merge-tree with AV-k-7's green arm 0 conflicts. Blind spots: a derived peer set with zero members is not graded (the ruling covers the served ABSENT read); the READ_FAILED face is graded only as not-the-empty-state; the sentence's quality is the L9 read; arm 3 reads C:/tmp/dsgn-r13-dist/final (the issuer holds it through round 14); arm 1 needs a full fwd19 PASS, so another panel's regression also fails it.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-3` (round 14, decomposition v14; serves FWD-19)

The CTO's ruling 4 (round-13 analysis): Peers gets a designed EMPTY state -- the order's expected defect from round 13 (fwd19 FAIL,
"peers/empty (no designed branch is reachable)"). This order follows AV-k-7 on the same worktree: keep its instrument changes whole
(both write `portal/scripts/ui-contract-check.mjs`). Build:
1. **`portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx`:** a completed read that finds no peer set (the served ABSENT peer read) renders
   a `PanelEmpty` sentence saying what is absent (e.g. "No peer set for this name yet." with a detail line), never "no data" and never a
   status word or code on the face; the served reason and the read status ride `data-` attributes (e.g.
   `data-peers-read-status="ABSENT"`). A FAILED read keeps its own failure line, not the empty state. A served peer set still renders its
   table unchanged.
2. **`portal/scripts/ui-contract-check.mjs`:** `--states-sweep`'s empty patch for peers is built from a SERVED absent shape (the round-13
   capture `peerSet.WMB_US_Equity.json`, re-keyed to the swept name), so the branch is reachable from a fixture (today the patch is
   `empty: null`). Change that patch only.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

**Granted harness changes (exact, tested on the green arm):** `peersReadFailed.harness.cjs` and `peersPattern.harness.cjs` each read the
visible "(read ABSENT)" text for one check; each moves that check onto `data-peers-read-status="ABSENT"` -- the same fact. The diffs are
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/grants/{peersReadFailed,peersPattern}.harness.cjs.peersempty.diff`.
No other harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/scripts/ui-contract-check.mjs
portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~53/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` (C12) and the issuer's checks, fixtures and grants under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/peersempty.cjs"; echo "exit=$?"</invocation><expect>PEERS HAS A DESIGNED EMPTY STATE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" K3 peersPattern.harness.cjs:13 peersReadFailed.harness.cjs peersCarry.harness.cjs tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>K3 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-3" judgment="true"/>
</proof_of_spec>

AC1 builds the page from your worktree's `portal/` (vite, into a temp dir), runs the graded render with `--states-sweep` (fwd19 PASS with
peers/empty present and its PNG written), renders the Peers tab statically on an ABSENT read (one designed empty sentence, no code) and
on BA's served peers (the table unchanged), and runs the negatives (the base page reads fwd19 FAIL; a blank page NOT_EXERCISED). AC1
takes about 15 minutes. Also keep AV-k-7's check green: `node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/foldopen.cjs"`
must still read 3 of 3 (report its line; about 11 minutes). AC2 is the bound on every harness that loads the Peers tab; AC3 no control
byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's render-run PNG `peers-empty.png`, never self-graded: a designed
empty state a person reads as such (FWD-19, C12).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~53/DSGN_AMGTV1.TO-AV-k-3.peers-has-a-designed-empty-state.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (the empty sentence as it reads), the output line of every criterion (and foldopen.cjs), the portal
and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 3 with ruling 4. Chained after AV-k-7 on slot ~53 (both write
ui-contract-check.mjs). Cross-chain overlap with AV-k-2 (chain ~52): PeersTab.tsx (k-2 adds one `causeAt` line to the error branch) and
the standalone no-permission block of ui-contract-check.mjs -- region-disjoint, merge-tree 0 conflicts, the issuer merges at the drain.
Base 118cd005: peersempty.cjs 1 of 3 (866 s); green r14-green-c @b7931ed3 3 of 3 (928 s).

<status>complete</status>
<round>14</round>
<slot>~53</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
