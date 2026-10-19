# NFRA_MCPORTAL -- round 1 L9: MP-z-2 AC3 and MP-z-6 AC2 graded (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v11. Fabric: site-z. Recorded: 2026-10-19 ~19:4xZ.

**Input:** `2.0.0_SA_COO~MP` msg 36087 (acked). The packet is
`deliverables/2.0.0_SA_COO~MP/gw/GW_R1_CLOSE_PACKET_20261019.md`, read whole.

`round-close-check --project NFRA_MCPORTAL --round 1`, read before this file: REFUSED, judgment=4, graded=2. The two ungraded
criteria are these.

**TO-MP-z-2 AC3: PASS, bounded.**

- **Images viewed by this seat:** `fwd20/render_20261013/mp_cp_after.png` and `mp_oc_after.png`.
- **The Control Plane reads at a glance.** One row per box, with status, commits, a seat count, then each project beside its
  commit count and last time, then the last commit.
- **Open Calls reads at a glance.** Box, project, asker, subject, age and state are in their own columns.
- **No identifier breaks mid-token.** Serials (`2.0.0_SA_COO~Y2`), project codes and call ids
  (`sitez-20261009T173038Z-21c5`) each sit whole on one line.
- **The bound:** the last-commit message column ends some messages mid-token with an ellipsis ("HG-t-18...", "from
  dell1..."). That is a deliberate elision, not a wrap or a break, and the full text is one click away in git.
- **Corroboration:** Andrew said "i see those displaying cleanly" (2026-10-16) of the live Control Plane.

**TO-MP-z-6 AC2: NOT MET.**

- **The criterion:** Andrew's own reading shows he got "the full breakdown he asked for -- every vendor or channel, the tools
  and indexes on each, and the current state of entitlements".
- **The 2026-10-16 words grade legibility, not completeness.** "gateway reads well" says the page reads. It does not say the
  breakdown is complete or right.
- **His LATEST reading of the same page says it is not.** Andrew-direct 2026-10-19 ~16:2xZ (`4.0.0_SA_CRO~Z` record
  @634d368d98), verbatim: "There are numerous cases where there are tools for Schwab and in the Indexes section it's talking
  about Black Diamond information. I do not understand why there would be Black Diamond indexes/tooling on a Schwab
  function." His reading of the indexes on each tool, one of the three things the criterion names, did not give him a
  breakdown he could use. It drove a deep audit, ratified as NFRA_MCPINDEX v0.19 (the routing arm, including the `display`
  class).
- **What AC1 measured stands.** The page equals the deployed code for `portal_index`, and the store for one principal. That
  proves the page renders the breakdown faithfully. It does not prove the breakdown he reads is the one he asked for. The
  judgment criterion exists for exactly that.
- **The cure path, named, not graded here:**
  1. the P1 display cell (CTO msg 36021): the per-index vendor and firm pair in the breakdown, from `2.0.0_SA_COO~O`;
  2. NFRA_MCPINDEX v0.19's classification of the Black Diamond-on-Schwab case as `link`, `code` or `display`;
  3. then Andrew's next read of /gateway, recorded verbatim. AC2 re-grades on that read.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S48",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-19T19:40Z",
    "one_line": "L9 grade, NFRA_MCPORTAL.TO-MP-z-2 AC3 (judgment, round 1): PASS, bounded -- Control Plane and Open Calls read at a glance on the issuer's live-data renders and no serial, project code or call id breaks mid-token; bound: the last-commit message column elides with an ellipsis mid-token, a deliberate truncation and not a wrap.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-z-2 AC3: Control Plane and Open Calls read easily at a glance, and no identifier breaks mid-token, graded on the issuer's rendered screenshots of both pages with live data (after AMENDMENT 1, 2026-10-13).",
    "world_is": "mp_cp_after.png: per-box rows (dell2, dell1, laptop, sitez) with status, commits, seat count, project/commit-count/last-time columns and last commit; serials such as 2.0.0_SA_COO~Y2 on one line. mp_oc_after.png: box, project, asked-by, subject, age, state columns; call ids such as sitez-20261009T173038Z-21c5 whole on one line. Last-commit messages end in an ellipsis, some mid-token.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/fwd20/render_20261013/mp_cp_after.png, mp_oc_after.png -- viewed by this seat",
        "deliverables/2.0.0_SA_COO~MP/gw/GW_R1_CLOSE_PACKET_20261019.md section 2 (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-MP-z-2 AC3 PASS, bounded."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S49",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-19T19:40Z",
    "one_line": "L9 grade, NFRA_MCPORTAL.TO-MP-z-6 AC2 (judgment, round 1): NOT MET -- the 2026-10-16 words ('gateway reads well') grade legibility, and Andrew's latest reading of the same page (2026-10-19 ~16:2xZ, record @634d368d98) says the Indexes on Schwab tools show Black Diamond information he cannot reconcile, so his own reading does not show the full breakdown he asked for.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-z-6 AC2: Andrew's own reading of the page shows he got the full breakdown he asked for -- every vendor or channel, the tools and indexes on each, and the current state of entitlements.",
    "world_is": "z6_andrew_read.md quotes 2026-10-16 ~18:5xZ: 'i see those displaying cleanly. gateway reads well.' -- no statement on vendors, tools, indexes or entitlements. Andrew-direct 2026-10-19 ~16:2xZ (4.0.0_SA_CRO~Z record @634d368d98): 'There are numerous cases where there are tools for Schwab and in the Indexes section it's talking about Black Diamond information. I do not understand why there would be Black Diamond indexes/tooling on a Schwab function.' AC1 PASS 4 of 4 (page == code for portal_index, page == store for one principal) proves faithful rendering, not that the breakdown read is the one asked for.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~16/z6_andrew_read.md (read whole)",
        "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261019_162xZ_GATEWAY_PAGE_SCHWAB_TOOLS_SHOW_BLACK_DIAMOND_INDEXES_DEEP_AUDIT_EVERY_TOOL_CALL.md @634d368d98 (read whole)",
        "task-orders/NFRA_MCPORTAL.TO-MP-z-6.fwd20-close-run.md:78-84 (AC2 text)",
        "deliverables/2.0.0_SA_COO~MP/gw/GW_R1_CLOSE_PACKET_20261019.md section 1 (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-MP-z-6 AC2 NOT MET. Re-grades on Andrew's next verbatim read of /gateway after the P1 display cell (CTO msg 36021, 2.0.0_SA_COO~O) and NFRA_MCPINDEX v0.19's link/code/display classification of the Black Diamond-on-Schwab case."
  }
]
```

-- 3.0.0_SA_CVO~Z
