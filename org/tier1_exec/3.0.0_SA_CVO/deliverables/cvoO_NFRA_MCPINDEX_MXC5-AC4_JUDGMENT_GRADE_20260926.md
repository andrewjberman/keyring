# L9 grade -- NFRA_MCPINDEX MXC5-AC4 (judgment), held branch wk-nfra_mcpindex-1-1d @ae03e6cf86

Grader: `3.0.0_SA_CVO~O`. Ask: `2.0.0_SA_COO~O` msg 26012 (acked). Instance:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/NFRA_MCPINDEX.TO-MX-c-5.classification-recut.proof_of_spec.json`.
Read in worktree `/c/tmp/mx-1` at @ae03e6cf86. Recorded 2026-09-26 ~05:1xZ. This row enters round 2's
ADJUDICATION as the grade of record at that round's L8.

**The criterion:** read_teams_attachment's classification, and each of the 14 new classes, is correct for what the
tool does, widens no tier, and does not read as a write.

**VERDICT: PASS**, with the three limits below.

## What SAFE means, read first

`destructive_ops.py:23` defines SAFE as "read-only; bypasses the guard". Line `:141` shows a SAFE tool never routes
through G1/G3. Lines `:182-190` show its `write_class` is None, so the write-entitlement gate never sees it. A SAFE
verdict therefore removes gates, and each one below was checked against the tool's code, not its comment.

| tool(s) | class | read against | holds? |
|---|---|---|---|
| read_teams_attachment | SAFE | `tools.py` def: the URL is refused unless http(s), then used only as a Graph `/shares/{token}/driveItem[/content]` key, so the request and the delegated token go to Graph, never to the URL's host | yes. A bounded content read within the caller's own Graph permissions. The attachment reference is already exposed by read_chat_messages / read_channel_messages, which are SAFE |
| 6 ycharts | SAFE | `ycharts/integration.py` diff: each is one GET through client.py (`/indices/table_data`, `/charts/general_data.json`, `/charts/fund_data.json`, ...) | yes. No vendor state changes. Tier reach is set elsewhere: Andrew-ruled B, "COMPARTMENTALIZED to the write-capable roster only" (`:40`), and `identity_scope.py:15` (iii) never adds ycharts for the concierge identity |
| 2 globgrph | SAFE | `globgrph/integration.py` diff: POST /cypher goes to the projection service, which opens Kuzu `read_only=True` (`projection_server.py` `KuzuAdapter.open_read_only`); GET /health | yes, with limit 1 |
| 5 schwab | SAFE | `schwab/integration.py` diff plus `schwab/export.py`: `prepare_download`'s only write is a RUNTIME# ticket, IF_ABSENT (`:105-122`), bound to the minting principal's tid/oid (`:144-145` refuses `wrong_principal`), single-use through one conditional update (`consume`, `:162`), and re-authorized against the current grant revision (`:148`, `:154`) | yes. No source data or external state changes, and a copied link fails for anyone but its minter, so the ticket is not a bearer widening |
| opal_data_refresh_upload | IRREVERSIBLE_SEND | `opal_portal/integration.py:98-107`: files:2, pipeline_runs:1, served_data; dry_run still writes pending/ | yes. The most restrictive class, and identical to the fail-closed default it replaces, so declaring it grants nothing. Who may call it is identity_scope's job (OA-f-1), not this class's |

**Tier widening:** none found. Every SAFE tool above either reads within the caller's own delegated permission
(Graph) or is fenced by a separate tier or roster gate (ycharts; the schwab grant model; identity_scope). The
classification opens the tools that fail-closed had denied to every tier. That is the criterion's purpose, and it
reaches no further than those gates already allow.

## Limits (non-blocking; for the round-2 L8 and the analysis)

1. **globgrph's SAFE rests on a property outside the gateway.** It holds only while the projection service opens
   Kuzu read-only. If that server changes, the class becomes wrong silently, because the gateway cannot see the
   change. Recommend the globgrph tool cell carry a planted write-clause control, a `CREATE` through
   `graph_cypher` that is expected to be refused, so the coupling is tested where the class is used.
2. **SAFE says nothing about vendor egress.** The six ycharts tools are paid vendor calls. Their SAFE class is
   correct about mutation, but a reader must not take "bypasses the guard" to mean "freely callable". Egress stays
   governed by the compartment gate and Andrew's egress word, which this session covers with per-call ledgering.
3. **The instance reads the classes; this grade reads the code.** Two of the fourteen rest on code outside the
   integration directory (schwab `export.py`; the projection server). The grade covers them at @ae03e6cf86 only.

-- 3.0.0_SA_CVO~O
