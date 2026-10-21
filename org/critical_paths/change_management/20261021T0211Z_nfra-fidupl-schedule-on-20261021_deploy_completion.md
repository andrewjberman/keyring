# Deploy Completion Record
**Date opened:** 2026-10-21T02:11:46.074042+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T022230Z
**Deploy:** NFRA_FIDUPL FT-s-6: config pointer, one seed run (one Fidelity sign-in), secret version named; schedule ON held for ENABLE
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | config.json gains perg_secret_id=fidelity/alongside/perg-list with a dated backup | SSM key-name list shows perg_secret_id and json.tool valid; backup file present | SSM on i-028e830f7226cc685: backup config.json.bak-20261021 made (cp -p); sed added exactly one line (11 -> 12 lines); venv python -m json.tool: json-valid; key names now: perg_secret_id profile_dir quo_line_id quo_secret_id quo_sender region repo_root scope wealthscape_secret_id work_dir. perg_secret_id is the secret's NAME fidelity/alongside/perg-list; no value printed. | CLOSED 20261021T021245Z |
| L2 | activation | perg_seed.py run ONCE through SSM (one Fidelity sign-in) | the single counts line recorded verbatim | perg_seed.py run ONCE through SSM (command e23c793b-1295-4f4d-a86f-c223b2ae5de3), status Success, exit=0, no retry. Single stdout counts line, verbatim: OK: listed=31 distinct_firms=8 unattributed=1 | CLOSED 20261021T021412Z |
| L3 | verify | secret current version named; schedule_version.md written | describe-secret version id (first 8 chars) and fidupl_round_checks.py ft6v R1-FT6V-OK | describe-secret fidelity/alongside/perg-list at 2026-10-21T02:13:38Z: one version 8473b6cf-e3c0-4b5b-8dcc-94480a41b57b stage AWSCURRENT (value never read). ft6v: R1-FT6V-OK the per-G list secret has a current version 8473b6cf. fu6g: R1-FU6G-OK. NFRA_FIDUPL.TO-FT-s-6.schedule_version.md written in the deliverables folder. | CLOSED 20261021T021412Z |
| L4 | activation | three schedule rules ENABLED by safe-apply (HELD until the issuer's ENABLE after the CTO countersign) | plan exactly 3 rule State changes; ft6r R1-FT6R-OK | COO ENABLE 8938 and CTO countersign (NEVER_WIDEN_SCHEDULE_ON_CTO_COUNTERSIGN_20261021) on file. safe-apply of the saved reviewed plan, whole root, no -target, variables.tf schedule_enabled default true: Plan 0 to add, 3 to change, 0 to destroy (state DISABLED -> ENABLED on the three fidelity-alongside-fetch-leg-N-daily rules only). Apply complete! Resources: 0 added, 3 changed, 0 destroyed. Post-apply plan No changes rc=0. ft6r: R1-FT6R-OK the three schedule rules are ENABLED; fu6g: R1-FU6G-OK. Live describe-rule: cron(45 9), cron(15 10), cron(45 10), all ENABLED. Automation not started by hand. | CLOSED 20261021T022230Z |

## Log

- 20261021T021146Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 4 leg(s)
- 20261021T021245Z LEG L1 closed: SSM on i-028e830f7226cc685: backup config.json.bak-20261021 made (cp -p); sed added exactly one line (11 -> 12 lines); v
- 20261021T021412Z LEG L2 closed: perg_seed.py run ONCE through SSM (command e23c793b-1295-4f4d-a86f-c223b2ae5de3), status Success, exit=0, no retry. Sing
- 20261021T021412Z LEG L3 closed: describe-secret fidelity/alongside/perg-list at 2026-10-21T02:13:38Z: one version 8473b6cf-e3c0-4b5b-8dcc-94480a41b57b s
- 20261021T022230Z LEG L4 closed: COO ENABLE 8938 and CTO countersign (NEVER_WIDEN_SCHEDULE_ON_CTO_COUNTERSIGN_20261021) on file. safe-apply of the saved 
- 20261021T022230Z CLOSED -- all 4 legs proven
