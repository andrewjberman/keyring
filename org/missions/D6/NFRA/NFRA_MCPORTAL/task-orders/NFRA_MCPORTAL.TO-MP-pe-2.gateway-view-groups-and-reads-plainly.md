# NFRA_MCPORTAL task order -- `MP-pe-2` -- WORKSTREAM PE ROUND 1: the Gateway page groups tools by source and reads plainly

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pe-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pe-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~32</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a gap group, a tool listed in two groups, a group with no tools).
EGRESS CLASS, declared: none. Every fetch in a test is a stub.
</preflight>

## 1. THE CELL -- `MP-pe-2` (workstream PE round 1, decomposition sections PE.0 to PE.2)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pe-32`, branch `wk-NFRA_MCPORTAL-pe-32`;
- inside it, the mcportal worktree `C:/tmp/mp-pe-32/mcportal`, branch `wk-NFRA_MCPORTAL-pe-32-mcportal`, based on mcportal `f7760a6` (the commit live on origin DEV
  today). `node_modules` is linked. Do not run `bun install` or `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~32 <0.9.0_WK_NFRA_MCPORTAL~32@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh`. Never push either repo. Make NO network call of any kind.

**The defect and your half.** Andrew opens `/gateway` to see what the gateway offers. Today the page lists tools under "Microsoft 365" that have nothing to do with
Microsoft 365, and the page is one long scroll of every channel with no overview. The wrong grouping is made by the server (a parallel cell, `MP-pe-1`, fixes it and
adds new fields); your half is that a human can read and understand the page. The page's job: say what each group is, where its tools come from, and let a reader
find a group quickly. Read `src/pages/gateway/GatewayView.tsx`, `gateway.css`, `gateway.test.tsx` (its way of rendering with `renderToStaticMarkup` and its fixture)
and `src/api/admin.ts` first.

**The server's new contract** (fixed; build against it exactly, do not rename a field). `GET /api/admin/gateway/breakdown` now answers, besides today's fields:
- `channels[].kind` takes the values `integration`, `native`, `bucket`, `undeclared` (today `native` and `integration` only);
- a new top-level string `grouping_basis` (one sentence, ending `N tool(s) declare no source.`);
- `channels` arrive already ordered: `bucket` groups by id, then `integration`, then `native` (`m365`), then `undeclared`; keep the response order;
- a tool can be listed in TWO groups (a tool that reads two AWS buckets), so the sum of the groups' tool counts can exceed the number of different tools.
A group of kind `bucket` is named after an AWS bucket (its `id` and `name` are the bucket name, for example `opal-data-harvest`). A group of kind `undeclared` has
`id` `undeclared` and `name` `No source declared`: it holds tools whose source nobody has declared yet, a gap and not a source.

Build:
1. **`src/api/admin.ts`**: the `GatewayChannel.kind` type becomes `'native' | 'integration' | 'bucket' | 'undeclared'`; `GatewayBreakdown` gains
   `grouping_basis?: string` (optional, so an old response still parses).
2. **`GatewayView.tsx`**, in this order on the page:
   - the title and the refresh control as today;
   - the header line: `Read <time>. <G> groups, <T> tools. Kill switch: on|off.` where `G` is the number of channels in the response and `T` is the number of DIFFERENT
     tool names across all groups (count each name once, even if two groups list it);
   - the kill-switch and grant-store warnings as today;
   - the `grouping_basis` line, when present, as a short paragraph under the header (class `gateway-basis`, the existing muted style);
   - a SUMMARY TABLE (class `gateway-summary`) with the columns Group, Kind, Tools, Holders, one row per group in response order. The Group cell is a link
     (`<a href="#gateway-<channel id>">`) to that group's section; Kind is the plain words below; Tools is that group's tool count; Holders is the number of holder rows
     (`no one` when there are none);
   - then one section per group as today, with the section element given `id="gateway-<channel id>"` (keep `data-channel`), and its kind written in words under the
     heading. Plain words for the kinds: `bucket` reads `AWS bucket`; `integration` reads `Integration`; `native` reads `Built in (Microsoft Graph)`; `undeclared` reads
     `No source declared`. Keep the facts line (auth, min tier, rating) as it is.
   - A group of kind `undeclared` is marked as a gap: add the text `Source not declared: these tools are not tied to a bucket yet.` under its heading, in a new class
     `gateway-gap` that uses the same red text colour as the existing `.gateway-unreadable` (`#be2d36`). No other new colour, no new font, and follow `portal/DESIGN.md`
     through the existing page (light canvas, white hairline panels, navy ink, one band per page).
3. No new dependency, no timer, no alert, no write.

**AMENDMENT 1 (issuer, after rendering your build and LOOKING at it; these are my spec's faults, not yours).** Five changes, all in `GatewayView.tsx`/`gateway.css`:
   a. **No raw enum in the text.** Remove the `Kind: <enum>.` fragment from each section's facts line; the facts line becomes `Auth: <auth>. Min tier: <min tier>. Rating: <value>` (keep the
      rating reason as today). The kind is said once, in plain words, under the heading.
   b. **The plain words for `undeclared` change** to `Not declared (gap)` (summary table Kind cell and the section's kind line). The other three are unchanged (`AWS bucket`,
      `Integration`, `Built in (Microsoft Graph)`). The red sentence `Source not declared: these tools are not tied to a bucket yet.` stays under the heading.
      Reason: the heading `No source declared` was repeated three more times in one section.
   c. **Links use the page ink, not the browser's blue.** The Group links in the summary table take `color: var(--color-ink, #163372)` with an underline (a new rule `.gateway-summary a`);
      `portal/DESIGN.md` allows navy ink and the existing tokens only.
   d. **Singular and plural.** The header line reads `1 group` or `N groups`, and `1 tool` or `N tools` (it read `1 groups` for one).
   e. **No column of "none".** In a group's Tools table, show the `Graph scopes` column only when at least one tool in that group has graph scopes; otherwise omit the column
      (header and cells). The `Indexes` column stays.
   Update the assertions your existing tests make about the old text, and add tests for c to e under any names (the seven named tests below keep their names and meaning; the
   `a group with no declared source reads as a gap` test now reads the new words). Re-run AC1 (still `pass` at 57 or more, `fail` 0), `tsc -b` and `bun run build`, and list each changed
   assertion in your report as before.

**Tests**, by these exact names (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; put each name as the literal first
argument of its `test(...)`), in `src/pages/gateway/gateway.test.tsx` using `renderToStaticMarkup` and a fixture of four groups (one `bucket` named
`opal-data-harvest`, one `integration`, one `native`, one `undeclared`):
- `summary table lists every group with its kind and tool count`: the markup holds a `gateway-summary` table with a row per group, each showing its plain kind words and its count;
- `a summary row links to its group section`: each Group cell has an `href="#gateway-<id>"` and a section with that same `id` exists;
- `a bucket group reads AWS bucket`: the `opal-data-harvest` section reads `AWS bucket` and shows the bucket name as its heading;
- `a group with no declared source reads as a gap`: the `undeclared` section holds the gap sentence and the `gateway-gap` class; the other three do not;
- `the grouping basis line is shown`: the `grouping_basis` string appears; when it is absent nothing breaks and no empty paragraph is rendered;
- `the tool total counts a tool once when two groups list it`: a fixture where one tool name is listed in two groups reads the true distinct count in the header line.
The existing test `routes json equals the app routes` (elsewhere in `src`) must still pass. If an existing gateway test pins the old header words (`channels`) or the old
markup, change only that assertion to the new truth and name each change in your report.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion.
3. Standing rules: no push and no vendor call. Commit the mcportal files with plain `git commit` in the nested worktree and the workspace files via
   `.tools/safe-commit.sh`, each with your serial as author (CLAUDE.md 14a). If you cannot meet a criterion as written, REFUSE it with its measurement.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~32/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W32-S<k>` (the next free k for W32).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root `C:/tmp/mp-pe-32` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pe-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pe2.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 7 of 7; pass=57 or more; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~32/NFRA_MCPORTAL.TO-MP-pe-2.gateway-view-groups-and-reads-plainly.proof_of_spec.json`.
Report once, with:
- the check output;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc);
- any field of the contract you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PE round-1 issuance (decomposition v11) from Andrew's 2026-10-15 ~16:3xZ word (record @5025c60ba1): the human-facing /gateway view is
MCPORTAL's, and the page must be easy to read and understand. The drain runs `bun run build` and `tsc -b` once and looks at the page rendered (screenshot) before the
round is called done. Check dry-run at the base: AC1 FAIL in the issuer's tree (`mcportal/src/pages/gateway` absent there; the issuer's mcportal checkout is README
only); in the worker's nested worktree the six new names are absent and `routes json equals the app routes` is present, so the names read 1 of 7. Whether integration
channels should also be regrouped by bucket is open for Andrew (PE.6 item 3); this cell keeps them as integration groups.

<status>pending</status>
<round>1</round>
<workstream>PE</workstream>
<slot>~32</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
