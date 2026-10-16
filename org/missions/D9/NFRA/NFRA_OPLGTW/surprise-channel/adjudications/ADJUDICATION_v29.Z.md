# NFRA_OPLGTW -- round 37 judgment criteria (site Z): two graded, five held for a real-call read

Author: 3.0.0_SA_CVO~Z. Round: v29. Fabric: site-z. Recorded: 2026-10-16 ~10:1xZ.
**Input:** `2.0.0_SA_COO~O` msgs 34894 and 34902 (acked). `python .tools/round-close-check.py --project NFRA_OPLGTW --round 37` at
~10:0xZ: 79 orders, judgment 7, graded 0, verdict REFUSED. The seven ungraded criteria are the AC3 of OG-ap-14, ap-18, ap-19,
ap-20, ap-21, ap-23 and hv-2.

## Graded

**NFRA_OPLGTW.TO-OG-ap-14 AC3: NOT MET.**
- **The criterion:** after this release AND the Bloomberg mirror grant write (`TO-OG-mg-1`), `0.0.3_BG_BBGTerminal` re-runs its
  own exercise of the 8 tools, read as on 10-13, and 8 of 8 ALLOWED is the arm.
- **What is on record:**
  - `TO-OG-mg-1` reads `<status>pending</status>`.
  - The BBGTerminal seat's log folders for 2026-10-14, 10-15 and 10-16 hold no exercise or capability file.
  - `AP14_SERVED.json` records `bbg_identity_admitted_8: 8`. That is a synthetic principal in-process on the host at
    10-14 ~11:3xZ, not the seat's own exercise, which is what the criterion names.
- **Owed:** OG-mg-1 complete, then the BBGTerminal seat's own 8-tool re-exercise. Any tool still denied after both is a
  BLOCKING row.

**NFRA_OPLGTW.TO-OG-hv-2 AC3: NOT MET.**
- **The criterion:** FWD-21's driven call, a real Opal asset manager in their own work Claude getting one covered name's pack
  and chatter. A1 lets Andrew's own work Claude run the FIRST read as a stand-in, graded PARTIAL at best, never PASS.
- **What is on record:**
  - `HV2_SERVED.json` is the installed-code arm: an Opal stand-in read 4362 bytes of a pack, a non-Opal principal was
    refused on `packs/` and `wsj/harvest/`, and an off-prefix read was refused. Those are AC2's arms.
  - A token census of `FWD-21 ... driven call|stand-in ... pack|chatter` over `org/missions/D9/NFRA/NFRA_OPLGTW` (2786
    files) finds only the order, its proof instance, and one row saying no asset manager is named. No record of the
    stand-in read exists.
- **Owed:** Andrew's stand-in read, which lifts this to PARTIAL. The named asset manager's own driven call (A3: named on
  10-14, Andrew's act this week) is the arm that can lift it further.

## Held: five criteria NOT MEASURED, because no answer was read

The AC3 of **OG-ap-18, ap-19, ap-20, ap-21 and ap-23** each say "read as a research user / an analyst would want them ...
**graded on a real call; never simulated here**", and each names what the reader must see:
- ap-18: newest-part counts, `data_status` on a quiet name, `not_held` for a CUSIP;
- ap-19: freshness in trading days, `data_status` on a quiet day, the 14-day news cap stated;
- ap-20: weights in percentage points with their unit, three dates in one row, coverage from each partner's csv;
- ap-21: the section asked for, its as-of, the 50 KB projection flagged;
- ap-23: a firm's data date stated, figures with units, rows never merged across firms, Schwab masters never summed.

**What exists to read.** The served records (`GT_SERVED`, `G36_SERVED`, `G5A_SERVED`, `P21_SERVED`, `CODE_SERVED`, and their
`.raw.txt` SSM stdout) hold per-tool booleans, counts and `answer_keys`. They hold no answer body. Every `answer_keys` list
stops at 12 names in sorted order, so several named markers (`data_status`, `freshness_td`, unit fields) cannot even be
confirmed absent or present. A field name is not a reading. Grading any of the five MET, or PARTIAL, from these would grade
the shape of an answer nobody has read.

**What closes them.** One real call per release, its answer read by this seat against the markers above. Either instrument
does it:
- (a) the opalgateway MCP on this box, which is disconnected since ~09:0xZ with `429 rate_limited (scope identity)` and
  needs a reconnect (`/mcp`);
- (b) the applier re-running each release's served harness with ONE projected answer body per named tool written to the
  record (no secrets; client answers already mask accounts as `****<last4>`).

Until one of them lands, these five carry no verdict, and round 37 stays REFUSED on them. That is the round's true state.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S76",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T10:15Z",
    "one_line": "Round 37: NFRA_OPLGTW.TO-OG-ap-14 AC3 NOT MET (OG-mg-1 pending; the BBGTerminal seat's own 8-tool re-exercise is not on record) and NFRA_OPLGTW.TO-OG-hv-2 AC3 NOT MET (no FWD-21 stand-in read on record; the named asset manager's driven call owed); AC3 of ap-18, ap-19, ap-20, ap-21 and ap-23 NOT MEASURED, because no served record holds an answer body to read.",
    "class": "OBSERVATION",
    "spec_asserts": "Each AC3 is a judgment criterion graded by the CVO on a real call or on the named seat's own act (task orders OG-ap-14 :131-134, OG-hv-2 :123-132, OG-ap-18 :98, OG-ap-19 :87, OG-ap-20 :86, OG-ap-21 :79, OG-ap-23 :69).",
    "world_is": "TO-OG-mg-1 <status>pending</status>; BBGTerminal logs 2026-10-14..16 hold no exercise file; AP14_SERVED bbg_identity_admitted_8 is a synthetic in-process principal. FWD-21 stand-in census 0 records over 2786 files. GT/G36/G5A/P21/CODE_SERVED (+ raw stdout) hold booleans, counts and answer_keys capped at 12 names, and no answer body. The opalgateway MCP on this box is disconnected (429 rate_limited, scope identity).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "round-close-check --project NFRA_OPLGTW --round 37 at ~10:0xZ (judgment 7, graded 0, REFUSED)",
        "task-orders/NFRA_OPLGTW.TO-OG-mg-1*.md last <status>; org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-1{4,5,6}/",
        "deliverables/0.7.0_AE_CloudOps~Z/AP14_SERVED.json, HV2_SERVED.json, GT_SERVED.json, G36_SERVED.json, G5A_SERVED.json, P21_SERVED.json(.raw.txt), CODE_SERVED.json(.raw.txt)",
        "comp-find FWD-21 stand-in census over org/missions/D9/NFRA/NFRA_OPLGTW (8 hits, 2786 files)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Two criteria graded NOT MET with the act owed named. Five held NOT MEASURED; each closes on one real-call answer per release, read by this seat (the opalgateway MCP reconnected, or the applier's harness writing one projected answer body per named tool). This seat does not grade an answer it has not read."
  }
]
```

-- 3.0.0_SA_CVO~Z
