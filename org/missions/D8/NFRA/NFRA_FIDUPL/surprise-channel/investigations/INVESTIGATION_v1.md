# NFRA_FIDUPL -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `2.0.0_SA_COO~P1` at the L6 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_FIDUPL-D1-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_FIDUPL-D1-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_FIDUPL-D1-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "NFRA_FIDUPL-D1-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~P1",
    "surfaced_at": "2026-10-19T20:15:59Z",
    "one_line": "The naming builder homes the code and state tiers of scope alongside in opal-data-alongside, a bucket that does not exist, and admits no meta or _ops tier, so round 1 puts the run record in the bronze tier as table _runs and delivers box code by SSM instead of an S3 code home.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (owns the confirmation of the _runs home and the final code home; this seat only surfaces)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -c \"import sys; sys.path.insert(0,'lib'); import opal_naming as o; print(o.address('fidelity','alongside','state','daily_pull','20261016','run.json'))\" (2026-10-19 ~20:0xZ) printed s3://opal-data-alongside/fidelity/alongside/state/daily_pull/20261016/run.json",
        "the same call with tier 'code' printed s3://opal-data-alongside/fidelity/alongside/code/canonical-fidelity/x; with tier 'meta' and with '_ops' it raised: tier is not one of NAMING_SCHEMA.json key.tier (enum bronze, silver, gold, platinum, state, code)",
        "address('fidelity','alongside','bronze','_runs','20261016','run.json') printed s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261016/run.json",
        "CTO msg 8473: opal-data-alongside is NOT provisioned"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-NAMES: every address is lib/opal_naming.py address() output; the Schwab run record lives under {source}/{scope}/_ops/daily_pull/ and meta/pulls/ and its code under an S3 code prefix.",
    "world_is": "For scope alongside the builder gives the code and state tiers a bucket that does not exist and has no tier for a run record, so a builder-clean run record and code home exist only in the bronze tier of opal-data-assets (the _runs table) and by SSM delivery to the box.",
    "notes": "Decision recorded in decompositions/NFRA_FIDUPL_DECOMP.md section 7 items 1 and 2. Nothing acts on a typed path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:30:11Z",
    "one_line": "The live Quo probe proves the line resolution, the sender filter and the incoming and from fields, but not the createdAfter parameter or the createdAt timestamp that the recency window depends on, so the window path is unexercised against live Quo.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-1 criterion FU1-AC2: the reader's seam against the real Quo, read only; the reader returns the newest code inside a recency window opened at the SMS-send step (worker reference section 2).",
    "world_is": "The probe printed QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4 and sent no createdAfter parameter and read no createdAt value; the live acceptance of createdAfter and the createdAt format on this line are UNMEASURED until the FU-x-1 live sign-in.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python infra/aws/ec2/canonical-fidelity/quo_otp.py --probe (worktree wk-NFRA_FIDUPL-1, 2026-10-19 ~20:30Z) printed QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4 with rc 0",
        "quo_otp.py _poll_once sends createdAfter in the %Y-%m-%dT%H:%M:%SZ form and _parse_created accepts the %Y-%m-%dT%H:%M:%S.%fZ form measured in org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py line 118 (2026-09-10)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Worker-side observation only; no action taken. The FU-x-1 live trace is the exercise that proves the window path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:34:29Z",
    "one_line": "The worktree's sparse-checkout definition omits infra/aws/ec2/canonical-fidelity, the new directory the order names, so safe-commit refuses to stage FU-s-1's module and tests and the cell cannot be committed from this worktree.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-1 WHAT TO BUILD: build infra/aws/ec2/canonical-fidelity/quo_otp.py and tests/test_quo_otp.py in worktree C:/tmp/fidupl-w1 on branch wk-NFRA_FIDUPL-1, and commit them there with safe-commit (worker face, the grant block).",
    "world_is": "git sparse-checkout list in the worktree names .tools, infra/aws/ec2/canonical-schwab-si2, infra/aws/ec2/inf-exporter, infra/logic/registry, lib, org/devices, org/missions/D8/NFRA/NFRA_FIDUPL, org/modules/graph, org/ref, org/standards, org/surprise_channel/schemas and two org/tier1_exec paths, and does not name infra/aws/ec2/canonical-fidelity; HEAD tracks zero files under that directory, so it is a new path the cut did not admit; safe-commit refused with 'matched paths that exist outside of your sparse-checkout definition' (rc=1, nothing committed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C C:/tmp/fidupl-w1 sparse-checkout list (2026-10-19 ~20:34Z) printed the list above, with no infra/aws/ec2/canonical-fidelity entry; git config core.sparseCheckout = true",
        "git ls-tree -r --name-only HEAD infra/aws/ec2/canonical-fidelity in the worktree returned 0 files; git status --short shows ?? infra/aws/ec2/canonical-fidelity/",
        "bash .tools/safe-commit.sh --author ... -F .scratch/msg_code.txt -- infra/aws/ec2/canonical-fidelity/quo_otp.py infra/aws/ec2/canonical-fidelity/tests/test_quo_otp.py exited rc=1 with 'exist outside of your sparse-checkout definition'; git log -1 shows HEAD 38d4f70df7 unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken: the worker did not change the sparse-checkout definition, did not force the stage and did not rebuild the tree. The two files exist untracked on disk and passed FU1-AC1 (R1-FU1-OK passed=14) and FU1-AC2 (QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4) in the worktree. A COO-side cut that adds the directory to the sparse definition, or a re-cut of this worktree, is the unblock; the worker's branch then commits the two paths and the proof instance."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:51:22Z",
    "one_line": "Every selector and request field name in PlaywrightDriver, PlaywrightGUI and ContextSession that no capture measured is listed here for FU-x-1 to prove live: the page selectors, the factor token source, the G-selector dialog, and the status.json and downloadExport.do bodies.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 WHAT TO BUILD A: PlaywrightDriver drives the real Wealthscape pages; its live selectors and request bodies are UNMEASURED and FU-x-1 proves them (worker reference section 9, signin.py).",
    "world_is": "Unmeasured assumptions in the round-1 code. Login page: input[name='username'], input[type='password'], button[type='submit'] (username, password and next steps), button[data-action='authorize'] and input[name='securityCode'] (authorize and code entry). Factor: the factor name is read from the authenticators[].uri key of the POST /user/session/login response and clicked by [data-authenticator='<name>']; the HAR shows the keys authenticators[].uri and authenticators[].title but the value token OTPSMS was not read (values are never printed). G-selector dialog: text=User Options, text=G Number Selection, select[name='gNumber'] with option values, button:has-text('Save'); the dialog's current-G read and its Set As Default checkbox were never observed. status.json body {iEtype, dateString, startPage, pageLength} and the downloadExport.do params are the reference values, not captured in the HAR. accountList.json length value '300' is assumed (the key name length is measured).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/c/Users/Test/Downloads/wealthcentral.advisorchannel.com2.har (98 MB, 441 entries) read by a stdlib script that printed only method, URL path and JSON or form key names (.scratch/har/har_keys.py, not committed), 2026-10-19 ~20:50Z",
        "key names measured: POST /auth/login form username, productId, wealthscapeDomain; POST ecaap /user/factor/password/authentication json username, password; POST ecaap /user/session/login response authenticators[].uri and authenticators[].title; POST ecaap /user/factor/otp/sms/authentication json phone, template; PUT the same path json securityCode; POST /ssc/platform-authorization/api/v2/authorize json loginType, loginSite, appName",
        "no status.json or downloadExport.do entry appears in the HAR (zero matches for those paths in the key-name output)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. FU-x-1 owns the proof: a live run that finds a selector, token or body different from the list above files its own row and does not guess."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:51:22Z",
    "one_line": "The HAR's accountList.json request carries an accountNumber form field that the cell's probe does not send, and the HAR holds no status.json or downloadExport.do entry, so the account.txt read and the probe's request shape are not HAR-proven.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 WHAT TO BUILD B: probe_g_switch posts accountList.json with form fields length, sourceCode=BROK, custodianCode=FID; main reads account.txt through one status.json list and one downloadExport.do (worker reference section 4).",
    "world_is": "The captured accountList.json POST carries four form fields: length, accountNumber, sourceCode, custodianCode. The probe sends three (no accountNumber), which is the cell's specified shape, so the server's acceptance of the three-field form is UNMEASURED. ContextSession duplicates the session surface that fetch.PlaywrightSession (FU-s-3) owns; it is a stand-in until FU-s-3 lands and is to be replaced by that adapter.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "key-name output of the Downloads HAR (.scratch/har/keys.txt, not committed): POST /ssc/accountsearch/wc/channel/accountList.json form:length, form:accountNumber, form:sourceCode, form:custodianCode; response accountListResponse.numberOfAccounts",
        "signin_recon.py _count_accounts sends fields {length, sourceCode, custodianCode} and reads accountListResponse.numberOfAccounts (commit ccd25ab7db)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. The FU-x-1 live run of --run-live is the proof of the three-field form and of the status.json and downloadExport.do shapes."
  }
]
```
