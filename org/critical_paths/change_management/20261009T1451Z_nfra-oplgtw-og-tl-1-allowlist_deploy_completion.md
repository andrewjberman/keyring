# Deploy Completion Record
**Date opened:** 2026-10-09T14:51:19.234726+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T151601Z
**Deploy:** OG-ap-4: TRANSCRIPT_MEETING_ALLOWLIST becomes the 4 committed online_meeting_ids (one .env value, one restart)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| DEP | ec2-baked-asset | opal-gateway | safe-ec2-deploy of c97232408d from C:/tmp/og-tl1b with DEPLOY_BASE_REF=91811b648a; halt gate premise true as OG-ap-3 A3, no HALT_OVERRIDE | safe-ec2-deploy rc=0, DEPLOYMENT COMPLETE, from C:/tmp/og-tl1b at c97232408d72bc649c92da7e4e711c0ebf0a3950 with DEPLOY_BASE_REF=91811b648ab119e73e22f8d401dd09f45b8ab19b (the live ref read from EC2_MANIFEST's deployed_commit and cross-read by host md5), OPAL_AGENT_SERIAL unset, HALT_ACK=1, AGENT_NAME=0.7.0_AE_CloudOps~Z, and NO HALT_OVERRIDE. The halt gate passed FIRST TIME here because the premise was true by construction: the re-cut worktree is a full checkout carrying org/tier2_senior/0.7.0_AE_CloudOps~Z, so OG-ap-3 A3's lesson was applied at CUT time rather than after a refusal, and a dry run with HALT_GATE_REPO_ROOT set to this worktree (what safe-ec2-deploy.sh:57 pins) read rc 0 / rc 0 before the act. THE RE-CUT IS EXACT, not merely equivalent: the live ref's deploy-to-ec2.sh blob is 2091d3b4be, IDENTICAL to the reference hunk's own pre-image index, so replaying 4514246d65..78afad4283 on r29 reproduces the release blob c2cfc34065 by construction -- measured BEFORE applying. All three of the COO half's limbs hold: blob c2cfc34065 equals the release's, patch-id ace789196aa221ca56c58179cc056b6364301737 equals the reference's exactly, and the json blob is d57e815a7ca1987e35041698fbdc26ea1e3698be. git status read exactly two rows (the one modified script, the one added json), so the order's 'any other difference is a STOP' did not arise. The json was added because the live ref lacks it. One audited author override on that one commit (OVERRIDE 0.7.0_AE_CloudOps~Z 2, CLOUD_OPS_OR_ETL applied, on record in org/git-author-override-audit.log), as OG-tl-1 A1 ruled. | CLOSED 20261009T151418Z |
| RB | verify | opal-gateway | CTO C1: ENV_KEYS_BEFORE == ENV_KEYS_AFTER (a missing key is a STOP and rollback); only TRANSCRIPT_MEETING_ALLOWLIST moved by value; /health 200; tool count unchanged; shipped md5 equal the release | CTO C1 MEASURED, not eyeballed: the deploy's own ENV_KEYS_BEFORE and ENV_KEYS_AFTER lines were parsed and compared -- 52 keys each, set equal TRUE, list equal TRUE (order too), missing-after NONE, added-after NONE, and TRANSCRIPT_MEETING_ALLOWLIST present in both. A missing key is a STOP and rollback; none is missing. The remaining limbs via r29_verify.py after: VERIFY PASS 5 of 5 -- /health 200 and service active with MainPID 862375 (one restart); shipped md5 98 of 98 identical, not-ok [] (the allowlist json is read LAPTOP-side at deploy time from WORKSPACE_ROOT and is not a shipped file, so the shipped set is unchanged from r29); tool list unchanged 66 -> 66, added [] removed []. THE VALUE LIMB IS THE STRONG ONE AND IT WAS RUN DELIBERATELY WIDE: compared against the pre-r29 state with --expect-changed MAIL_BEARER,MAIL_BEARER_LABELS,TRANSCRIPT_MEETING_ALLOWLIST, it reads equal 48 of 51 and changed exactly those three. r29 moved the first two and THIS deploy moved the third, so 'only TRANSCRIPT_MEETING_ALLOWLIST moved here' is established by subtraction across BOTH deploys rather than by a single narrow window -- a stronger claim, and the one I could actually make since no before-state was captured for this deploy alone. That gap is named rather than hidden. No rollback trigger fired. | CLOSED 20261009T151418Z |

## Log

- 20261009T145119Z OPENED by 0.7.0_AE_CloudOps~Z with 2 leg(s)
- 20261009T151418Z LEG DEP closed: safe-ec2-deploy rc=0, DEPLOYMENT COMPLETE, from C:/tmp/og-tl1b at c97232408d72bc649c92da7e4e711c0ebf0a3950 with DEPLOY_B
- 20261009T151418Z LEG RB closed: CTO C1 MEASURED, not eyeballed: the deploy's own ENV_KEYS_BEFORE and ENV_KEYS_AFTER lines were parsed and compared -- 52
- 20261009T151601Z CLOSED -- all 2 legs proven
