# AMGT_RESAPP task order -- `AMGT-aw-4` -- A /freshness PORTAL PAGE: EVERY COVERED COMPANY, ITS LAST-REFRESHED DATE, A STALE INPUT FLAGGED (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~248</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a portal page and its test; no cron.
comp-iam: DECLARED-NOT-APPLICABLE -- the page reads the served `/api/scoped/amgt/freshness` through the existing API client.
comp-adversary: RUN by the issuer at the cut -- no portal page references `amgt/freshness` (research read); FWD-7's "one place" is a page a person opens (CVO v87, CTO ruling 3).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r73-248` (branch `wk-AMGT_RESAPP-248`, cut from the issuance commit with `--portal-ref 2146031c --node-modules link`, so `portal/` is at origin DEV and carries `node_modules`). Work and commit only there. Start every shell call with `cd /c/tmp/r73-248`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-4` (round 73, decomposition s.81)

PRD v0.40 FWD-7 DONE WHEN (PRD `:539-542`): a seat opens the one place on demand, sees every covered company with its last-refreshed
date, and finds a stale one without opening any folders. CTO ruling 3: the page renders `/freshness` and flags a stale input per name.

1. **The page** `portal/src/pages/Freshness/` (e.g. `Freshness.tsx`). It reads `GET /api/scoped/amgt/freshness` through a new
   function in `portal/src/api/endpoints/amgt-lead-panel.ts`, one row per covered name (`covered: true`):
   - the name, the last-refreshed date, and each input's clock (bloomberg, seekingalpha, serp, pack);
   - an input older than 7 trading days, or NEVER, is flagged stale in plain words ("Seeking Alpha last read 2026-09-11");
   - sortable by staleness.
   Follow the existing SecurityAnalysis patterns: React Query hook, the design system's table and card components.
2. **The hookup is NOT yours:** the route and nav entry in `portal/src/App.tsx` (~`:132`, `:467`) are a shared file. Export the page
   and name the exact hookup lines in your report; the issuer adds them at the merge.
3. **A test** `portal/src/pages/Freshness/Freshness.test.tsx`, run with `bun test`: a stale input is flagged; a covered name with
   every input fresh is not; a NEVER input reads stale.
4. **Commit inside the nested `portal/` repository** on a branch `wk-AMGT_RESAPP-248-portal` from `2146031c`. Report the portal commit
   hash; do not push. The outer worktree commit carries only your deliverables. The candidate's DEV push is Andrew's word through
   the integrator.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W248-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No push, no deploy, no store write, no vendor call. Do not edit `App.tsx`.
2. Plain words on the page; no internal names (identity, security key, crosswalk, dossier, model block, input ledger).
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/Freshness/
portal/src/api/endpoints/amgt-lead-panel.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~248/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-4"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; bun test src/pages/Freshness/Freshness.test.tsx; echo "exit=$?"</invocation><expect>every case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-4" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~248 <0.9.0_WK_AMGT_RESAPP~248@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~248/AMGT_RESAPP.TO-AMGT-aw-4.freshness-page.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the portal commit hash and branch;
- the exact App.tsx hookup lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 3, ruling 3. AC2 is the CVO/DSGN judgment on the rendered page (aw-8 walks it). The DEV push is Andrew's word.

<status>pending</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~248</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~03:2xZ):** CLOSED -- drained @4921e89618 (deliverables). Candidate on portal branch wk-AMGT_RESAPP-248-portal: worker 8adcf3f728 plus the issuer's App.tsx hookup fb939c4a (lazy route, requireInternal, Tools nav, requiresTier internal); bun test 6/6; tsc clean on the touched files. proof VALID. The CTO review was asked; the DEV push is Andrew's word through MSTR~Z. AC2 (judgment) goes to the CVO at L9 after aw-8 walks the page.

<status>complete</status>
