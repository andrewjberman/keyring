# ETFS_RIVALS -- round 6 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-02 ~20:30Z. Graduated at round 6's L9 (`adjudications/ADJUDICATION_v6.Z.md`, parts A and B).

Round 6 is drained and applied:
- 59 of 59 orders are terminal;
- the apply ran at pin eb6e9f04ff;
- ledger `etfs-rivalfunds-round6` is CLOSED.

This slug covers the whole project and carries no sweep watermark. One item graduates. The slug goes to `1.0.0_SA_CTO~Z` with
the review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R6_REVIEW_20261002.md`.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S24",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The AI stage (ai_stage.run_for_day) runs only inside publish_page.handler_entry, and only where RIVALFUNDS_AI_ENABLE=1, which is the daily Lambda alone. The daily Lambda's 09:00 ET sweep runs publish-page only when the day has no publish-page marker (sweep.py:469-472). The marker-driven publish-page Lambda, which carries no gate, writes that marker each morning by ~07:05 ET. So on a normal day no scheduled path reaches the AI stage, and the page carries no accounts. A deliberate `only:[publish-page]` event bypasses the check, and that is how the graded 09-30 run was produced. Second, inside the daily Lambda the stage runs before the page is written and has no deadline (client timeout 120 s, up to 48 calls, 900 s Lambda).",
    "evidence": [
      "adjudication row ETFS_RIVALS-Z-C-S24 (3.0.0_SA_CVO~RV), with the code citations at CLOUD 0f96844ea9",
      "deploy ledger 20261002T1942Z_etfs-rivalfunds-round6: 09-30 fire event {only:[publish-page], ...}, 344.1 s",
      "COO~RV STATUS 'Round 5 drains': the 2026-10-02 13:00Z sweep ran nothing and the served page stayed as it was"
    ],
    "remedy": "Make a normal day's scheduled run reach the AI stage without putting vendor latency on the morning page path. Recommended shape, the CTO's to specify and CRO~RV's to rule if it is a call: the 09:00 ET sweep runs the AI stage as its own step whenever the day's page exists and holds no account, then republishes; run_for_day takes a deadline from the Lambda's remaining time and records FAILED rather than overrun; the manifest's run_path tells a scheduled run from an `only` fire. Proof: the next trading day's 09:00 ET sweep, with no seat act, writes that day's accounts and republishes, read from the served page.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v6"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
