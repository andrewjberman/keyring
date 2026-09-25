# NFRA_MCPORTAL task order -- `MP-p-1` -- ROUND 2, E5 + E6 client: plain refusals for non-JSON answers, and the whole history

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-p-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a page cell; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface.
comp-adversary: DECLARED-NOT-APPLICABLE -- enrichment round of a thread.
EGRESS CLASS, declared: NONE. Tests use a mocked fetch.
</preflight>

## 1. THE CELL -- `MP-p-1` (round 2, decomposition section R2.1)

Andrew's dashboard is the nested repo `mcportal` (React + Vite + TypeScript on bun), at `<worktree>/mcportal`. Its typed
client `src/api/admin.ts` parses every answer as JSON (`readJson`). With no API behind the page, the dev server's SPA
fallback answers `/api/admin/changes` with HTML and status 200. The Recent Changes page then shows a raw parse error,
"Unexpected token '<'", instead of a reason a person can act on (round-1 real run, row C-S11). Recent Changes also asks
for one principal, while the gateway will now serve every principal when no parameters are given.

Build:
1. **`src/api/admin.ts`**: `readJson` refuses a response whose `content-type` is not JSON. It refuses an HTML 200 too,
   with a plain, quotable reason, e.g. "the admin API did not answer (got text/html)". It never attempts the parse.
   Non-2xx handling stays.
2. **`src/pages/recent-changes/`**: Recent Changes calls `GET /api/admin/changes` with NO parameters, shows every
   principal's changes newest first (who, when, what, before, after, verdict), and shows the client's plain reason on a
   refusal.
3. **Tests**, in the repo's existing test style (`bun test`, react-dom/server rendering, mocked fetch), naming exactly:
   - "a non-JSON 200 is refused with a plain reason" (it plants an HTML 200);
   - "recent changes asks for every principal" (the fetch URL carries no query parameters).

## 2. BOUNDS

1. The sidebar order (`src/shell/pages.ts`) and the router (`src/App.tsx`) are untouched. Round 1's 4 tests stay green.
2. Commit inside the nested repo with `git -C mcportal commit --author "0.9.0_WK_NFRA_MCPORTAL~3
   <0.9.0_WK_NFRA_MCPORTAL~3@opal.agent>" -F <msgfile> -- <nested paths>`, where the msgfile is written with the Write
   tool. Your parent-side deliverables go through `safe-commit.sh`.
3. Standing: no push, no install beyond `bun install` of the existing lockfile, no vendor call, no AWS. REFUSE a
   criterion you cannot meet as written, and report the refusal with its measurement. Never repair a criterion, widen
   it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
mcportal/src/pages/recent-changes/**
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `mcportal/src/pages/mcp-server/entitlements/`, `mcportal/src/shell/`, `mcportal/package.json`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPORTAL-Z-W3-S<k>` (next free k for W3).

## 4. PROOF OF SPEC (literal; run from your worktree root, after both repos are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-p-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/p1.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 2 of 2; pass>=6; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-p-1.non-json-and-history-client.proof_of_spec.json`.
Report once: what you changed and where, the commit hashes in BOTH repos, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E5 (R-5) and E6's client. Chain C, a single cell; MP-d-1 builds the bundle from it.

<status>pending</status>
<round>2</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
