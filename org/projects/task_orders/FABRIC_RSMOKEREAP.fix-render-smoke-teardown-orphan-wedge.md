<task_order>
<metadata>
  <to_id>FABRIC_RSMOKEREAP (FIX-class hardening — parented under the LD-0144 fabric-runtime-hardening line, NOT a new project per CTO disposition 185712Z)</to_id>
  <project>Fabric-runtime hardening (follow-on to LD-0144 headless-chrome line; not a tracked project code)</project>
  <title>Fix the render-smoke Edge TEARDOWN defect — a hung playwright-MCP/Edge orphans its process tree + wedges the session (killed CVO 18:04Z). Launch-time PID registry + timeout-bounded guaranteed reap; NEVER name-match-kill.</title>
  <assigned_to>0.7.0_AE_CloudOps</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>closed -- COO verified-done sweep 2026-06-10 (Andrew directive; ground-truth: parent project complete in registry or work landed/superseded per git)</status>
  <dispatch_held>true (queued-behind-security; normal-pri, slack exists — render-smoke not needed until v2.1.114 promotes, which is Andrew-GO-gated)</dispatch_held>
  <priority>NORMAL — bounded fix-class; not tonight-urgent. But it killed a CVO session, so it's a real session-stability defect, not cosmetic.</priority>
  <references>
    <ref type="disposition">CTO 185712Z: FIX-class hardening TO (not a new ADHC/project — minting a new code = HARD-BLOCK #7, unwarranted for a bounded infra fix); owner 0.7.0 queued-behind-security; normal-pri; mechanism steer below.</ref>
    <ref type="post-mortem">MSTR CVO-respawn post-mortem: CVO 3.0.0_SA_CVO died ~18:04Z — root cause ~34 orphaned msedge procs from the stranded render-smoke Edge lock. CVO had finished queue 4/4 GREEN, so no verification lost; the defect is that a wedged render-smoke CAN kill a session.</ref>
    <ref type="lineage">LD-0144 (memory reference_fabric_headless_chrome_block) fixed the LAUNCH defect (bun couldn't drive Playwright -> portable-Node + Edge via @playwright/mcp, config .tools/playwright-mcp-config.json). THIS is the TEARDOWN defect on the same line.</ref>
    <ref type="safety">CVO + MSTR both flagged: blanket `taskkill /im msedge.exe` is UNSAFE (kills Andrew's own Edge + other agents' playwright-MCP Edge). The fix must be PID-scoped, never name-matched.</ref>
    <ref type="rule">CLAUDE.md Rule 16: any shell-level reap must use Git-Bash-3.6.7-available utils (no pkill/pgrep without guarded fallback) — but reaping via the Node child-handles sidesteps shell name-matching entirely (preferred).</ref>
  </references>
</metadata>

<scope>
Root cause = NAME-BASED IDENTITY. The render-smoke run spawns a playwright-MCP/Edge process tree; when the Edge hangs, the tree is orphaned and the session wedges (and can die). The current "cleanup" instinct (kill msedge by name) is unsafe because it can't distinguish render-smoke's Edge from Andrew's or another agent's. Both the wedge-prevention AND the safe-cleanup needs collapse to ONE mechanism: own the child PIDs at launch.

## Mechanism (CTO steer — AE designs the impl):
1. LAUNCH-TIME PID REGISTRY: when render-smoke spawns the playwright-MCP/Edge tree, record the spawned child PIDs to a run-scoped pidfile. The Node/harness layer that invokes @playwright/mcp HAS the child handles — track them there, not after-the-fact by scanning process names.
2. TIMEOUT-BOUNDED GUARANTEED REAP: wrap the render-smoke run in a hard timeout; on timeout OR normal exit, a try/finally teardown kills EXACTLY the pidfile's tracked PIDs. A hung Edge can then never strand a tree or wedge/kill the session — teardown is guaranteed and PID-scoped.
3. SAFE TARGETED CLEANUP falls out free: cleanup == kill the tracked pidfile set. NEVER `taskkill /im msedge.exe`. Prefer reaping via the Node child-handles (sidesteps shell name-matching + Rule-16 util-availability concerns entirely); if a shell-level reap is unavoidable, Rule-16-compliant utils only.

## INTERIM (current ~34 orphans) — do NOTHING destructive:
They're idle harmless procs until render-smoke is next needed. Two safe clears, both fine: (a) a host-restart clears them naturally (zero risk, likely before v2.1.114 promotes), or (b) the targeted-PID cleanup once the script above exists / once someone holds the playwright-MCP context. NO blanket kill. CVO is correctly told NOT to retry render-smoke until clean — keep that hold.
</scope>

<acceptance>
- [ ] Launch-time PID registry: render-smoke records its spawned playwright-MCP/Edge child PIDs to a run-scoped pidfile at spawn (via the Node child-handles, not name-scan).
- [ ] Timeout-bounded guaranteed reap: render-smoke run is hard-timeout-wrapped; try/finally teardown kills exactly the pidfile PID set on timeout OR exit. Verify a deliberately-hung Edge does NOT orphan a tree or wedge the session.
- [ ] Safe cleanup proven: cleanup kills only the tracked set; NO name-match kill anywhere in the path. Andrew's Edge + other agents' playwright-MCP Edge provably untouched.
- [ ] Rule-16 compliance if any shell-level reap is used (guarded fallbacks); preferred path = Node child-handle reap.
- [ ] Interim orphans cleared safely (host-restart OR targeted-PID once the script exists) — NOT a blanket kill. RAVC2 to COO + CTO; CC MSTR, CVO.
</acceptance>
</task_order>
