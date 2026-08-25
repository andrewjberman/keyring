<task_order>
<id>SCTY_MCPGUARD.S0</id>
<title>SCTY_MCPGUARD S0 -- DESTRUCTIVE-SURFACE ENUMERATION: enumerate every destructive/write Graph call the m365 gateway exposes + its blast-radius profile, as the auditable registry every guardrail TO (G1-G6) consumes</title>
<issued_to>CloudOps/AE gateway-surface owner (0.7.0_AE_CloudOps -- CloudOps + gateway/OTP owner; coordinate with 0.8.0_AE_CloudComp who grounded the gateway call-path for NFRA_MSGRAPH S2). Pin owner on GO.</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project SCTY_MCPGUARD is complete; this TO was last touched 2026-06-26, predating the project close 2026-07-07. Closed as a record act, not a work verdict. Prior status: pending -- GO HELD for Andrew's PRD review (his direct ask; deliverables ready for review). Not blocking (S5-phased). On Andrew go-ahead -> GO this S0 -> G1-G6 cut on its output.</status>
<priority>P2 -- the gating enumeration; every guardrail TO (G1-G6) consumes this registry. Recon-first (no guardrail spec commits before the destructive surface is known). Not-urgent (aligned to NFRA_MSGRAPH S6 multi-user, later).</priority>
<project>SCTY_MCPGUARD</project>

<context>
Andrew-direct (verbatim "so they dont accidentally delete the whole onedrive"). CTO PRD docs/architecture/SCTY_MCPGUARD_PRD.md (0019b1743). MCPGUARD is the SAFETY layer above PREMCP's AUTH layer -- it governs WHAT a destructive call can do once authorized. The m365 MCP gateway is now the SINGLE MS-Graph chokepoint (Andrew-sovereign: NFRA_MSGRAPH consumes Graph THROUGH it), so the guardrails enforce at ONE place. The 6 guardrails (G1 blast-radius cap ... G6 audit/alert) all need the SAME input: a complete, auditable map of WHICH gateway calls are destructive + HOW MUCH they can destroy (blast radius). This S0 produces that map. CTO's contain-don't-classify framing: a guard keys off the DESTRUCTIVE CALL, not the caller's intent -- so the enumeration is of CALLS + their reach, not of intents.
</context>

<scope>
  0. [ANDREW-DIRECT 2026-06-26: "we can also scope permissions at the SERVER layer"] The STRONGEST containment is least-privilege at the SERVER/permission layer -- do NOT grant a destructive capability to a consumer that does not need it, so the destructive call is IMPOSSIBLE (not merely guarded). So S0 ALSO maps CONSUMER -> CAPABILITY-NEED: which gateway consumers (the NFRA_MSGRAPH derive, each agent class, the human users) actually need READ vs WRITE vs DESTRUCTIVE. This consumer->capability map is the input for SERVER-LAYER per-consumer scoping (the gateway exposes only the tools/Graph-scopes a consumer needs -- a read-only consumer literally cannot invoke a destructive tool). Server-layer scoping is the FIRST line (reduces the surface); the G1-G6 app-layer guardrails are the SECOND line, covering only the residual WRITE-CAPABLE consumers (the human users who legitimately delete/move). A read-only consumer (e.g. the MS derive) needs NO destructive guardrail because it has no destructive capability. This is the defense-in-depth layering: server-layer least-privilege (PREMCP AUTH layer) + app-layer destructive guardrails (MCPGUARD SAFETY layer).
  1. ENUMERATE every gateway-exposed Graph operation, CLASSIFY each by destructiveness: READ (no mutation) / WRITE (creates/modifies, recoverable) / DESTRUCTIVE (deletes/overwrites/moves-at-scale, potentially unrecoverable). Ground against the ACTUAL gateway tool surface (NFRA_OPLMCP source -- the m365 MCP server's tool definitions + the underlying Graph endpoints each calls), Rule 22: read the source, do not assume the tool list. Cover the write/destructive Graph verbs (DELETE /driveItem, PUT/PATCH content, POST move/copy, permission grants/revokes, batch operations). For each, note WHICH consumer classes need it (feeds the scope-0 consumer->capability map).
  2. BLAST-RADIUS PROFILE per destructive call: the MAXIMUM reach of a single invocation -- single-item vs folder-recursive vs whole-drive vs cross-site; bounded vs unbounded; recoverable (recycle-bin) vs permanent. This is the input G1 (blast-radius cap) keys off -- it must know which calls CAN touch a whole tree.
  3. REVERSIBILITY per destructive call: does Graph route it to the recycle bin (recoverable) or permanently delete? This is the input G4 (reversibility-first/undo) keys off.
  4. CURRENT-STATE: for each, note whether ANY guard exists today (the gateway's current posture) -- the gap map G1-G6 close.
  5. EMIT as a structured, auditable REGISTRY (the artifact every guardrail TO consumes) -- machine-readable (call -> class -> blast-radius -> reversibility -> current-guard -> gap), committed to the project dir.
</scope>

<locked_invariants>
  1. CONTAIN-DON'T-CLASSIFY (CTO framing): enumerate CALLS + their blast-radius/reversibility, NOT caller intents. A guard mitigates both fat-finger + hijacked-agent because both end at the same destructive call -- so the surface is the call, not the actor.
  2. READ-ONLY enumeration: this S0 is a SURFACE MAP, it executes NO destructive call. Enumerate from source/schema, not by invoking deletes. (Inert-data discipline: the gateway tool definitions are read as text/schema, nothing destructive is run.)
  3. SINGLE-CHOKEPOINT: the gateway is the one MS-Graph chokepoint (NFRA_MSGRAPH) -- the enumeration covers the gateway's surface, which IS the full destructive surface (no MS-Graph path bypasses the gateway by design).
</locked_invariants>

<compiler_tools_mandate>
  <step><run>comp-which "what destructive or write tools does the m365 mcp gateway expose"</run><expect>routes to the gateway tool surface (NFRA_OPLMCP) -- enumerate from there, ground in source.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. COMPLETE enumeration of the gateway's Graph operations, each classified READ/WRITE/DESTRUCTIVE, grounded in the gateway source (Rule 22 -- file:line or tool-def cited, not assumed).
  2. BLAST-RADIUS profile per destructive call (single/folder/tree/drive/cross-site; bounded/unbounded; the G1 input).
  3. REVERSIBILITY per destructive call (recycle-bin vs permanent; the G4 input).
  4. CURRENT-GUARD + GAP per call (what G1-G6 must add).
  5. Emitted as a structured auditable REGISTRY artifact committed to org/projects/SCTY_MCPGUARD/ -- the SoT every guardrail TO consumes.
  6. RAVC COO + CTO; CTO arch-gates the enumeration completeness; this unblocks the G1-G6 guardrail cut.
  7. Session log Compiler Tools section reproduces every &lt;run&gt; with observed output.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/SCTY_MCPGUARD_PRD.md (0019b1743)</ref>
  <ref type="auth-layer">docs/architecture/SCTY_PREMCP_PRD.md (the AUTH layer below; S2B exploit-catalog cross-map)</ref>
  <ref type="gateway">the live m365 MCP gateway (NFRA_OPLMCP) -- the single MS-Graph chokepoint; enumerate its tool surface</ref>
  <ref type="chokepoint-context">NFRA_MSGRAPH (the gateway is the single MS-Graph chokepoint because the MS derive consumes Graph through it)</ref>
</references>
</task_order>
