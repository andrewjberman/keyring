# Deploy Completion Record
**Date opened:** 2026-10-21T06:01:05.537655+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-17 batch16 (round-47 sixteenth batched release, in-flight cap 26): release 8e3eddf959 on live ref 13917ef993; window 2026-10-21 06:00Z-06:55Z, abort /health 200 by 06:30Z; ROLLBACK DECISION POINT 06:38:30Z; halt gate dry run 0.8 s empty inbox, bound 720 s used; callers in the slot (3-day audit read): 3 sign-in identities by count (a Teams poller, an occasional research and whoami caller, this seat's own calls of 10-20); rollback = redeploy the wrapper's pre-deploy tarball with DEPLOY_BASE_REF the live ref; halves COO 313a8c11d4 CTO f7ff5f9fc7 CVO 215c1d4ef0 on ask 291ffc35747a
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| release | ec2-baked-asset | release 8e3eddf959 deployed through safe-ec2-deploy.sh, marker equal, unit limits 5600M/6400M | proof: W/CODE16_SERVED.json |  | OPEN |
| read-back | verify | 30-minute unarmed read-back, 27 of 27, md5 0 differ, counts, in-flight guard in the deployed tree | proof: W/CODE16_SERVED.json |  | OPEN |
| proofs | verify | D1 per vendor, D2 transactions, eight-call load, projection, index_pairs | proof: W/RL17_PROOFS.json |  | OPEN |

## Log

- 20261021T060105Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
