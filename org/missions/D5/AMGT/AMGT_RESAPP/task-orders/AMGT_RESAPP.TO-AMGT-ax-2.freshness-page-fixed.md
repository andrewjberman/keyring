# AMGT_RESAPP task order -- `AMGT-ax-2` -- THE /freshness PAGE MADE USABLE: CURRENT PACK FIELD, A NEVER-COLLECTED INPUT STATED ONCE, BRAND CONTRAST, SORTS THAT REORDER (CTO RULING 3b-3e)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ax-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~253</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a portal page and its tests; no cron.
comp-iam: DECLARED-NOT-APPLICABLE -- the page reads the served route through the existing API client.
comp-adversary: RUN by the issuer at the cut -- the aw-8 walk (row Z-W251-S3): the page flags 95 of 95 stale, its text is low contrast on a navy card, and the sorts leave the first rows unchanged; the route reads 0 NEVER on pack (r73 c49 YES) while the page shows NEVER.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r74-253` (branch `wk-AMGT_RESAPP-253`, cut from the issuance commit with `--portal-ref fb939c4a --node-modules link`, so `portal/` is at aw-4's /freshness candidate). Work and commit only there. Start every shell call with `cd /c/tmp/r74-253`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ax-2` (round 74, decomposition s.82)

CTO ruling 3, items b-e. All of these are on the page, `portal/src/pages/Freshness/` (aw-4's files at `fb939c4a`):
- **(b) The current pack field.** The page must read the route's CURRENT `pack` value. The route serves a date for 95 of 95, but the
  page shows NEVER. Find the field mismatch (name, nesting or a stale mapping in `freshnessRows.ts`) and fix it.
- **(c) An input collected for NO covered name** (web search, `serp`, today) is stated ONCE above the table ("Web search is not
  collected yet"). It is not flagged on every row. The stale rule applies only to the inputs the pipeline collects for that name.
- **(d) Contrast from the brand tokens:** the design system's text and surface colour tokens, never a hand-picked colour.
- **(e) The sorts reorder.**

**Tests** (`bun test`) in `portal/src/pages/Freshness/`:
- a row with a dated pack is not flagged for pack;
- an input absent for every name is stated once and flags no row;
- clicking each sort button changes the first row's order (a click test per button).

**A render:** write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~253/render_freshness.txt`, the page's rendered text over a captured `/freshness` body from the DEPLOYED
route (save it as `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~253/freshness_body.json`). Print the count of rows flagged stale and the first five rows per sort.

**Commit inside the nested `portal/` repository** on branch `wk-AMGT_RESAPP-253-portal` from `fb939c4a`; report the commit hash and do
not push. The candidate goes to the CTO, who reviews it FROM A RENDER on the deployed route. The DEV push is Andrew's word.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W253-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No push, no deploy, no store write. Do not edit `App.tsx`.
2. Plain words; no internal names (identity, security key, crosswalk, dossier, model block, input ledger).
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/Freshness/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~253/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ax-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; bun test src/pages/Freshness/; echo "exit=$?"</invocation><expect>every case passes, including a click test per sort button; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ax-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~253 <0.9.0_WK_AMGT_RESAPP~253@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~253/AMGT_RESAPP.TO-AMGT-ax-2.freshness-page-fixed.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the portal commit hash and branch;
- the render's stale count and the first five rows per sort;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-73 analysis item 2, ruling 3b-3e. AC2 is the CVO/CTO judgment on the render. The DEV push is Andrew's word.

<status>pending</status>
<round>74</round>
<slot>0.9.0_WK_AMGT_RESAPP~253</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~07:0xZ):** CLOSED -- drained @5378ac7af5 (deliverables); portal candidate 6de76f0509 on wk-AMGT_RESAPP-253-portal (on fb939c4a), not pushed. AC1 14 pass. AC2 is the CVO/CTO judgment on the render. Rows: S1 INERT (the pack-field premise did not reproduce); S2 RULED: 95 of 95 stale is correct under ruling 3c, since Seeking Alpha has never been read for 92 names, which is real staleness, not a page defect.

<status>complete</status>
