# Andrew-direct 2026-09-28 ~15:2xZ -- the nine NFRA gate asks answered (to 2.0.0_SA_COO~O, site Z)

Asked by `2.0.0_SA_COO~O` at round close-out ("anything you need me specifically to do"). Answers are verbatim in
substance. Each one is applied only to the gate it names.

| # | Gate (project) | Andrew's answer | What follows |
|---|---|---|---|
| 1 | G-ACCT (NFRA_OPALAI) | "write a text handoff to an agent who would do it in the elevated shell (will create a 2.0.0_SA_COO~O elevated)" | Handoff: `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/HANDOFF_G-ACCT_ELEVATED_20260928.md`. The checkout was cloned and the dry run measured by COO~O first. |
| 2 | G-AUTH (NFRA_OPALAI) | Asks exactly what is needed. An MFA can be sent to an agent, but a provisioned SERVICE account should not need the interactive process. | ANSWERED ~16:0xZ: **"use setup-token on the Analyst account, one relayed MFA is fine."** The Claude credential is a `claude setup-token` token from the dedicated Analyst account, set as Opal_Agent's `CLAUDE_CODE_OAUTH_TOKEN`. The gateway's Microsoft sign-in as Opal Bloomberg takes ONE relayed MFA. Both are in the handoff, steps 5-6. |
| 3 | G-ASKER (NFRA_OPALAI) | The colleague is **Menachem**. He may ask which clients hold which Opal assets in their accounts (e.g. model holdings for a given client). | Replaces the runbook's step-6 test colleague for this purpose. His identifier is held OFF-repo (no emails in the repo). His grant is written through the existing operator path (NFRA_OPLGTW G-E, row 9). |
| 4 | Z-S31 BD password (NFRA_MCPINDEX) | Andrew rotates it "shortly once your agents are all wrapped up and drained". | Held on Andrew; history purge scope unchanged (today's purge = 28 PNGs). |
| 5 | G-HDR (NFRA_MCPORTAL) | "Done." | MP-a-1's precondition is met; its re-cut reads the claim-keys line. |
| 6 | G-PYPI (NFRA_MCPORTAL) | "Go ahead." | The writer's one pinned-wheel fetch is authorized (as runbook step 7 already recorded). |
| 7 | G-C (NFRA_OPLGTW) | "Approved." | The controlled identity and its synthetic grant are approved. |
| 8 | G-D (NFRA_OPLGTW) | Ready to do the walkthrough "after the reboot (we are going to reboot this device after your workers are drained)". | Held on the reboot. OG-v-4 re-cuts on G-D. |
| 9 | G-E (NFRA_OPLGTW) | "Approved." | Menachem's concrete grant is approved; activation via OG-z-2 by an authorized operator once his verified tid/oid are recorded. |

Also this sitting: Andrew stopped this session's `/canonical-drive` cron ("kill the crons in this session"), and the
device reboots after this seat's workers drain.
