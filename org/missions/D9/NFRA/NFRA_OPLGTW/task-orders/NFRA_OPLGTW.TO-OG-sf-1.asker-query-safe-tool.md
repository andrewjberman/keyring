# NFRA_OPLGTW task order -- `OG-sf-1` -- `opal_asker_query` is a SAFE (read) tool, with the tool-classification census (R54)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sf-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sf-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~37</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the tests run offline.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is ruling R54 of org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md @e43ee663be, on row NFRA_OPALAI-Z-S62.
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-sf-1` (decomposition addendum R3-T.30, round 32 item 1)

The gateway's tool guard, `infra/aws/ec2/opal-gateway/app/destructive_ops.py`, classifies every MCP tool. A tool in
`SAFE_TOOLS` is a read and bypasses the write gates; a tool in none of `SAFE_TOOLS`, `DESTRUCTIVE_OPS` and
`TOOL_WRITE_CLASS` is "unknown" and is refused to EVERY tier (`write_class()` returns `"UNCLASSIFIED"`, and
`tools._run` answers `write_class_denied`). `opal_asker_query` (`app/tools.py:1208`, body in `app/asker_scope.py`) is
in none of the three, so the live gateway refuses it to everyone, master_admin included (row NFRA_OPALAI-Z-S62). It
reads a Teams message and a catalog answer and writes nothing. Ruling R54: it joins `SAFE_TOOLS`.

Do:
1. Add `"opal_asker_query"` to `SAFE_TOOLS` in `app/destructive_ops.py`, with a short comment in the style of the
   entries around it (NFRA_OPLGTW R54; a read: one Teams message and one catalog answer; no write, no send). Update the
   measured-count comment above the set to the count you measure after the edit (`len(SAFE_TOOLS)`), as that comment
   asks. Change nothing else in that file.
2. **The census.** Count every function in `app/tools.py` decorated with `@mcp.tool(...)` (the denominator), and list
   every one that is in none of `SAFE_TOOLS`, `DESTRUCTIVE_OPS`, `TOOL_WRITE_CLASS` after your edit. Write it to
   `W/tool_class_census.json` as `{"registered": <int>, "unclassified": [<sorted names>], "safe": <int>,
   "destructive": <int>, "write_class": <int>, "method": "<how you counted>"}`. If any name other than
   `opal_asker_query` was unclassified BEFORE your edit, do NOT classify it: list it and file a surprise row for it.
3. **Tests**, offline, in a new file `infra/aws/ec2/opal-gateway/tests/test_asker_safe_tool.py`, named EXACTLY:
   - `test_ogsf1_ac01`: `destructive_ops.classify("opal_asker_query")["class"]` is SAFE and
     `destructive_ops.write_class("opal_asker_query")` is `None`.
   - `test_ogsf1_ac02`: a call through `tools._run("opal_asker_query", {...}, fn)` as a SCOPED, non-master identity
     (an identity the existing identity-scope allowlist admits to this tool; read `app/identity_scope.py` and reuse the
     fakes of `tests/test_asker_scope.py` / `tests/test_asker_binding.py`) reaches `fn` (a fake that records it was
     called) and its result carries no `"code": "write_class_denied"`.
   - `test_ogsf1_ac03`: negative control. The same identity calling a made-up tool name that is in none of the three
     sets through the same `_run` is refused (any guard refusal), and `fn` is NOT called.
4. Run, each in its own process, and state totals: `tests/test_asker_safe_tool.py`, `tests/test_asker_scope.py`,
   `tests/test_asker_binding.py`, `tests/test_tool_classification_composition.py`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~37/`.

## 2. BOUNDS

- No release, no deploy, no host act, no AWS call. This cell is BUILT and HELD on your branch.
- Classify only `opal_asker_query`. No other tool's class moves.
- Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/tests/test_asker_safe_tool.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~37/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W37-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/sf1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/sf1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)registered in tools\.py \(denominator\): \d+.*opal_asker_query in SAFE_TOOLS: yes.*worker record agrees with this census: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tool is SAFE; a scoped identity's call is not `write_class_denied`; an unknown tool still is refused.
- `AC2`: the issuer's own static census agrees with yours, and the tool is in `SAFE_TOOLS`.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sf-1.asker-query-safe-tool.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the diff of `destructive_ops.py`; the census record; every test file run with its
   totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 1, ruling R54 (`ledger/ROUND_ANALYSIS.round31.md` @e43ee663be), on PRD v2.0 admitted at
  @5924aaedbe (both L4-R halves SIGNED). Row NFRA_OPALAI-Z-S62 disarms when this ships in release r29.
- Ships in the r29 release (`OG-rl-15`, R55), not cut in this issuance.
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>32</round>
<slot>~37</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
