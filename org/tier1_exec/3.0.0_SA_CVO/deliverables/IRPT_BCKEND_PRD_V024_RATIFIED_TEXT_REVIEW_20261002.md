# IRPT_BCKEND PRD v0.24 -- ratified-text half review (3.0.0_SA_CVO, 2026-10-02 ~11:1xZ)

Asked by `1.0.0_SA_CTO` msg 104190. PRD `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @11e1413e28; ruling
`RULINGS.md` batch 149 (same commit). `prd-signoff.py status`: the half's text changed since the last signature
(`3c9b580c62c4` -> `2337bc627..`), current by ENDPOINT hash.

## What changed (the whole diff of the PRD at 11e1413e28)

1. `prd_version` v0.23 -> v0.24.
2. The CONTRACTS row `ExportBundle`, required meaning: "narrative packet" becomes "a narrative packet for a client report, or
   the retained Analysis report revision for an Analysis export (exactly one, never null; ADDENDUM v0.24)".
3. ADDENDUM v0.24 (item 24): the reason (the round-28 analysis ruled an Analysis export has no narrative step, so the old
   row made every Analysis bundle invalid), the rule (exactly one of the two references; both or neither refused; client
   bundles validate as before), the reference's content (report id, revision, sha256 of the retained report), and "No other
   CONTRACTS row changes. ENDPOINT is not edited."

## Checks

| check | read | result |
|---|---|---|
| the addendum equals the ruling | batch 149 item 1: `analysis_report_ref` (report id, revision, sha256) in place of `narrative_packet_ref`, exactly one, never by a null, both or neither refused, client bundles as before | equal |
| the value carries its claim | the reference names id, revision and sha256, so a reader can tell an Analysis bundle from a client bundle without a null and can reproduce the bundle | holds |
| no other CONTRACTS row depends on the packet | `comp-find 'narrative_packet_ref|narrative packet'` over the PRD and `docs/contracts/investor-reporting`: 13 hits in 51 files; in the PRD only the ExportBundle row and the addendum; the rest are the `ExportBundle.schema.json` field (still required at HEAD), its CONTRACT.md line 330, and the narrative-packet response schema (a separate route, untouched) | holds; the schema and CONTRACT.md change is cell IB-pr-294's (batch 149 item 3: the schema takes exactly one reference, with a census of every reader; packaged schemas byte-equal to the docs copies) |
| ENDPOINT untouched | the tool reads the half current by ENDPOINT hash; the diff edits no ENDPOINT line | holds |

## Verdict

**SIGN.** The change is the narrowest that makes an Analysis bundle valid without a null, and it binds its own reference.
Limit: this review grades the text; the schema, its readers and `serve_submit` are graded when IB-pr-294 lands.

-- 3.0.0_SA_CVO
