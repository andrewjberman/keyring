# MDPF_SECHIST task order -- `SH-t-26` -- THE POSITIONING FRONTIER LABEL IS PROMOTED TO PROD FROM THE APPROVED LIST, WITH ITS RECEIPT AND THE CI CONCLUSION

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R6.md</decomp_doc>
<owned_cells>SH-t-26</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H1</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<to_id>MDPF_SECHIST.TO-SH-t26</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-14 ~18:5xZ): `python .tools/open-calls.py approval-status --branch cand/dell1/sechist-frontier-label` reads `state=APPROVED valid=yes row=dell1-20261014T141244Z-c822 by=andrew head_sha=c77f23624df0a400273da28063813930d7e63afb commits=1 class=client-facing`; the merge-forward landed (origin/DEV `1c5f9dae`, the candidate is in it); `portal-release-build.sh --features cand/dell1/sechist-frontier-label` returned `RELEASE result=READY branch=release/20261014T184507Z base=6a5926fc1194 head=fa10e75861ab`, 1 feature, 0 unapproved; origin/PROD reads `6a5926fc11` at the cut. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `SH-t-26` (round 6, workstream PROMOTE)

Andrew approved the client-facing row `dell1-20261014T141244Z-c822` (Andrew-direct ~18:3xZ 2026-10-14, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_183xZ_FIVE_CALLS_ANSWERED_AND_BD_ASOF_CITATION.md`), and the CTO seated this lane for the promote (CTO msgs 5698, 5710). The feature is ONE display-only change to the Positioning page (`/positioning`, a partner-firm page): it passes `returns_frontier` and `returns_frontier_holdings` through the adapter and shows a carried holding's frontier date under its windows and a one-line note under the table. With neither key served the page renders as before. Do, in order:

1. **Confirm the base.** `cd C:/dev/ajb_workspace/portal && git fetch origin PROD DEV -q && git rev-parse origin/PROD && git merge-base --is-ancestor c77f23624d origin/DEV && echo IN-DEV`. If it does not print `IN-DEV`, STOP and report. If `origin/PROD` is `6a5926fc1194...`, the release `release/20261014T184507Z` (head `fa10e75861ab`) is current: go to step 2. If PROD has MOVED, do NOT promote that release: rebuild with `bash .tools/portal-release-build.sh --features cand/dell1/sechist-frontier-label` from the workspace root (it cuts a new release from the new PROD), name the deviation in your receipt, and promote the new release.
2. **Verify the release.** `bash .tools/portal-release-build.sh --check release/20261014T184507Z` (or the rebuilt release's name). It refuses the whole release on any pinned token (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote.
3. **Promote** the release with `/prod-deploy`. The release carries ONE feature, seven files (`src/api/portal-proxy.ts` types, `src/pages/Positioning/shared/etfAdapter.ts`, `tabs/HoldingsTab.tsx`, the new `tabs/ReturnsFrontier.tsx`, and three harness files under `src/pages/Positioning/__harness__/`); no other candidate is in it, and `~D1`'s CANON release is a separate build that follows yours on the NEW PROD.
4. **Read the CI conclusion** on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. **Write** `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_SH_T26.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Positioning | /positioning | client-facing), `## CI` (the conclusion and the run it came from, as read).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `MDPF_SECHIST-D1-S<k>` (next free), `disarm_owner` `2.0.0_SA_COO~H1`.

## 2. BOUNDS

1. One feature only, exactly the approved list; never `--features` anything else, never live DEV whole.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh` (already run by the issuer for this feature).
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write. The producer apply of SH-t-24 (`etf-positioning-producer`) is NOT yours and does not start until the issuer reports your promote read on PROD.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.4.0_DT_ClientPlatform~H1/
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="SH6-t26-AC1" cell_refs="SH-t-26"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in src/api/portal-proxy.ts src/pages/Positioning/shared/etfAdapter.ts src/pages/Positioning/tabs/HoldingsTab.tsx src/pages/Positioning/tabs/ReturnsFrontier.tsx src/pages/Positioning/__harness__/frontierLabel.harness.cjs src/pages/Positioning/__harness__/frontierFixture.json src/pages/Positioning/__harness__/frontierNoCarry.golden.json; do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse c77f23624d:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>seven lines `EQUAL <path>` (one per path, none `DIFFERS`)</expect></criterion>
  <criterion id="SH6-t26-AC2" cell_refs="SH-t-26"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `6a5926fc` (the pre-promote head: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="SH6-t26-AC3" cell_refs="SH-t-26"><invocation>grep -c -E "positioning|client-facing|completed|success" "C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_SH_T26.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Then write the proof-of-spec instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.4.0_DT_ClientPlatform~H1/MDPF_SECHIST.TO-SH-t26.positioning-label-promoted-to-prod.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block, AC1 to AC3 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> SH6-t26-AC1,SH6-t26-AC2,SH6-t26-AC3` (the ids are ONE comma-separated argument) on the committed bytes and report its verdict line, THEN stand down.

Report once to `2.0.0_SA_COO~H1`:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut 2026-10-14 ~18:5xZ on the CTO's seating (msg 5710). The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home, commits under its own lane, and reports to `2.0.0_SA_COO~H1` and `1.0.0_SA_CTO~DELL1`. The class is client-facing and Andrew approved the row, so no further word is owed for the promote itself. The SH-t-24 producer apply follows this promote (CTO half condition C1). Deadline per the CTO: finish before tonight's 21:00Z dell1 restart, or start after the re-seat.

<status>complete -- 2026-10-14T19:0xZ by the issuer (2.0.0_SA_COO~H1): DT lane 0.4.0_DT_ClientPlatform~H1 promoted ONE feature, release/20261014T184507Z, PROD 6a5926fc1194 -> fa10e75861ab (tag portal-v2.1.220), CI run 38619242657 completed/success, proof instance VALID (rc=0, re-run by the issuer). Re-read by the issuer: ls-remote PROD fa10e75861ab; gh run list headSha fa10e758 completed/success.</status>
<round>6</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform~H1</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
