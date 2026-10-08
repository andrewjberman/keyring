# ETFS_RIVALS -- round 28 L8/L9 (CTO rulings R19, R20, R24; ROUND_ANALYSIS.round22 ADDENDUM 6) (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~21:20Z. Packet: COO~RV msg 31984 (@954c16bb49).

**aw-1 J1: NOT MEASURED (no real accounts under `a1-chain/7` exist; its oracle is the first 13:00Z sweep after the round-28 Lambda deploy). tc-1 J1: NOT MEASURED (the cell is unmerged; its merge waits on RIV-tw-1's J1, the 2026-10-09 11:00Z vehicle run, C-S80).** Every mechanical result in the packet reproduces on this seat's own runs.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S85",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T21:20:12Z",
    "one_line": "Round 28 L9: RIV-aw-1 J1 NOT MEASURED and RIV-tc-1 J1 NOT MEASURED, both by design (no model output yet; tc-1 unmerged). The issuer's mechanical record reproduces: aw-1.AC1 and aw-1.AC2 PASS on merged CLOUD, the suite 919 passed and 3 skipped, 40 of 42 check files PASS, and on the branch tc-1.AC1, tw-1.AC1 and tw-1.AC2 PASS. Rows W21-S1 and W21-S2 are INERT as filed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-aw-1 J1: on the first 13:00Z sweep after the deploy, the 26 served account items carry 0 period codes, state their two dates, and cite every dollar figure; the accounts read as plain English to a portfolio manager. RIV-tc-1 J1: graded on the first scheduled vehicle run after its merge.",
    "world_is": "- This seat's runs, site Z, 2026-10-08 ~21:05-21:15Z, merged CLOUD (box/sitez @c23f472d71; aw-1's tip a2283fc349 is an ancestor): aw-1.AC1 'AC1 RESULT: PASS 0 failures' (control j PASSES); aw-1.AC2 'AC2 RESULT: PASS 0 failures' (control j PASSES); `python -m pytest rivalfunds/tests -q` from data/etfs/scripts: 919 passed, 3 skipped; round15/checks/*.AC*.py: 40 of 42 end PASS 0 failures, and the two others are tc-1.AC1 (FAIL a, b, c, d, e, g) and tw-1.AC1 (FAIL e), both of which grade the unmerged branch. These equal the packet.\n- On the branch wk-ETFS_RIVALS-22 @b0b65368fb (worktree C:/tmp/wk-riv-r28-22, git status unchanged by the runs): tc-1.AC1, tw-1.AC1 and tw-1.AC2 each 'PASS 0 failures'.\n- aw-1, the words the model will receive (read from the merged module): PROMPT_VERSION 'a1-chain/7'; SYSTEM names the three periods as 'the last 30 days, the last 90 days and the last 365 days', forbids 'a code, a key, a fact id or a short form', asks for the period's two ISO dates once in `text`, and rule (5) requires a `cited` id for every dollar amount, percent and rank. P_ACTIVITY_30D and P_DIRECTION carry no period code and pass the window(s) as PERIOD / PERIODS. The prompt is a plausible means to J1; it is not J1, which only the model's served output can show.\n- W21-S1 (period names exempted from the figure match): `regrade_rows` / `regrade_day` have no caller in data/etfs/scripts/rivalfunds/ outside tests (Grep, this seat), so the loosening of an older stored account's re-grade reaches only an operator-run re-grade. INERT, as filed.\n- W21-S2 (a correction chat that raises keeps the first reply, graded FAIL with `correction_error` in the manifest): the outcome is visible on the page as a FAIL, not a silent PASS. It does replace run_day's re-run of the fund for that error class; the issuer kept it. INERT.\n- C-S83 (the period codes on the page) stays OPEN: its proof is the served sweep, the same read as aw-1 J1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round28/L8_PACKET_ROUND28.md @954c16bb49",
        "org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-RIV-aw-1.ai-accounts-name-periods-in-words-and-cite-every-figure.md (last <status> complete)",
        "data/etfs/scripts/rivalfunds/ai_accounts.py at 022fd6b063 (SYSTEM, P_ACTIVITY_30D, P_DIRECTION printed by this seat)",
        "surprise-channel/investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-W21-S1, ETFS_RIVALS-Z-W21-S2",
        "branch wk-ETFS_RIVALS-22 @b0b65368fb"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
