# NFRA_CTLPLN -- remediations, v1

<sweep_watermark>2026-10-08T23:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-08 ~23:4xZ, on 1.0.0_SA_CTO msg 107476. 19 rows: INBOUND's 10 graduations (ADJUDICATION_v3.md
C-S4; drafted in org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_INBOUND_REMEDIATION_ROWS_HELD_20261008.json, held by the
row gate's L10 precondition until this compile) and 8 graduations of the other workstreams (C-S8), and S1's row, which C-S1 graduated without minting (the gate's S74 limb), written closed (ARMED standing, DISARMED): 3389 now admits the tailnet range only. 9 OPEN rows are ARMED: S33, S34,
W36-S2, W14-S2, W14-S32, W12-S1, Z-S3, W8-S7, W6-S17. Only S1 is closed.

```json
[
  {
    "id": "NFRA_CTLPLN-W31-S3",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The remote-job seam added fields (bid reviewer and unavailable_reason, accepted brief_sha256, complete coo and grade) that the tool, the skill and the tests carry, but the shared protocol file does not record them: 0 occurrences of brief_sha256 or unavailable_reason at HEAD.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W31-S3",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P2. The issuer hands the field text to 4.0.0_SA_CRO, who holds the protocol file. Done when the file names every field the tool sends.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W32-S5",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The box half of the same seam: the protocol file still shows the old payloads.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W32-S5",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P2. Closed by the same edit as W31-S3.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W31-S4",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Alongside has no recorded mail domain in the firm records, so its mail is never considered by mail_requests.py.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W31-S4",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P1, at the cut of item 5. The issuer rules whether a firm record is added and by whom. Done when the domain is recorded, or Alongside is named out of scope.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W31-S5",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Opal (internal) has no recorded mail domain in the firm records, so its mail is never considered.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W31-S5",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P1, at the cut of item 5. The issuer rules whether an Opal record is added. Done when the domain is recorded, or Opal mail is named out of scope.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W31-S6",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gateway's mail route admits only an exact sender address from a three-address table, so it cannot serve a mail read under clause 9; the read needs NFRA_OPLGTW's mail-domain admission (site Z).",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W31-S6",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P1. The CTO routes the gateway change to NFRA_OPLGTW. Done when one real domain-admitted read is served.",
    "owner": "1.0.0_SA_CTO",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W31-S12",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "assist.INTENT_SYSTEM (assist.py:844) says 'dev' only for a chat (C...), so a plain-English text cannot open a job on a mail item.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W31-S12",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P2, at the cut of item 5. Done when a plain-English text opens a job on an M tag in a test.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W36-S2",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "transcripts-pull/build.sh zips registry JSON as read with no line-ending step; the shared tree's remediations.json and scopes.json read w/crlf.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W36-S2",
      "adjudication row NFRA_CTLPLN-C-S4",
      "investigation row NFRA_CTLPLN-S36 (2.0.0_SA_COO~R, 2026-10-09T00:10:32Z): handed to NFRA_TRNSPT, owner of infra/aws/lambda/transcripts-pull/, on 1.0.0_SA_CTO msg 107481"
    ],
    "remedy": "P2. Give transcripts-pull/build.sh the LF step teams-chat-assist/build.sh has, or measure the deployed hash equals an LF build. Done when two builds from trees with different line endings give one hash.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v8"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~T2",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W39-S1",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CALLER_GRAPH_SCOPES['teams_route'] (graph_scope_map.py:98-99, unchanged at HEAD) omits Team.ReadBasic.All and Channel.ReadBasic.All; a host-overlay scoping of MS_INGEST_IDENTITY would cut them at token_broker.py:223.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row W39-S1",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P1, before the gateway release carrying the channel routes: add the two scopes, or read the host overlay and record MS_INGEST_IDENTITY unscoped. Done when one live call to each list route returns 200.",
    "owner": "1.0.0_SA_CTO",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-S33",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A refused End of Day redraft failed silently; CT-i-13 (live 22:32Z) restores the link line or texts the reason.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row S33",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P1. Done when the 2026-10-09 full-day read shows no End of Day event failed without a text.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-S34",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A later first draft reused the run-once key and was not texted; CT-i-13 (live 22:32Z) keys every draft uniquely.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 row S34",
      "adjudication row NFRA_CTLPLN-C-S4"
    ],
    "remedy": "P1. Done when the 2026-10-09 count shows sms_sent reconciling with texted plus updated, and no draft texted twice.",
    "owner": "2.0.0_SA_COO~R",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R",
      "round": "v8"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W14-S2",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "dell_create_policy.json CreateUpdateTagCompute allows ssm:CreateDocument, ssm:UpdateDocument and ssm:UpdateDocumentDefaultVersion on Resource *, and the deploy policy allows s3:PutObject on the ec2/ artifact prefixes those documents download; a Dell can rewrite a command document the estate's own controller sends to a host, and the code it fetches, with no SendCommand grant.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row W14-S2",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P1. The CTO rules whether a Dell keeps those document and artifact-prefix writes, or a cell adds a Deny on the documents the estate sends and the prefixes they fetch. Done when the ruling is recorded and the simulation reads the ruled answer for both Dells.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W14-S32",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ssm:PutParameter is allowed to both Dells on every parameter by the standing create policy, including /mdpf/custody_source, the operationally controlled bd-to-schwab cutover value; this seat's simulation reads it allowed for dell1 and dell2.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row W14-S32",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P1. The CTO rules: accept, or add a Deny of ssm:PutParameter on parameter/mdpf/custody_source to the create policy (a cell for the policy's owner). Done when the simulation reads the ruled answer for both Dells.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W12-S1",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Three Lambdas vendor an older 163-line trading_calendar.py (inf-etf-ownership-daily, bd-served-vintage-alarm, opal-assets-absence-check) that keeps the silent 2024-2027 fallback; lib/trading_calendar.py's fail-closed fix does not reach them until they are re-vendored and redeployed.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row W12-S1",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P2. Cut a re-vendor cell for the three copies (their parity workflow already lists them) and redeploy under a pair. Done when each copy equals lib/trading_calendar.py and the deployed package carries it.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-Z-S3",
    "project": "NFRA_CTLPLN",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "lib/trading_calendar.py's hardcoded fallback covers 2010-2027 and raises CalendarCoverageError outside it; a Lambda packaged without pandas_market_calendars runs on the fallback, so from 2028-01-01 its trading-day reads raise where they answered before.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row Z-S3",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P2, dated. Regenerate NYSE_HOLIDAYS_FALLBACK (lib/tests/gen_nyse_closures.py --write) and rebuild the importing functions before 2027-12-01. Done when the fallback covers 2028 and the deployed packages carry it.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W8-S7",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "dell_fence_census.py --live with its default --out rewrites tests/dell_fence_census.json, which is also check_fence_scoped_rows.py's 'before' baseline; any later live re-take breaks the sibling check and the --control arm.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row W8-S7",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P2. Separate the census's live output path from the sibling check's baseline. Done when a --live run with defaults leaves check_fence_scoped_rows.py and --control reading ok=True.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W6-S17",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The intake check 6, as amended, counts a .py file a wheel has and an installed copy lacks as missing rather than differ, so a wheel that adds a new module passes the check; the tool cannot tell that case from an installed copy whose files are gone.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row W6-S17",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P2. The issuer rules whether py_missing_not_in_installed_record fails check 6, and amends the criterion. Done when a wheel that adds a module the installed RECORD never listed fails check 6, or the ruling accepting it is recorded.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-D2-S1",
    "project": "NFRA_CTLPLN",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The dell2 Terraform kit's filesystem mirror holds aws 5.100.0, aws 6.67.0 and archive 2.8.1 only, while terraform.rc excludes registry installs; 5 of the 40 locked roots pin a provider version the mirror cannot serve and a sixth declares hashicorp/local, so an apply order on any of the six refuses at init on dell2.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row D2-S1",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P1. The CTO rules which remedy: the kit carries the missing windows_amd64 builds (archive 2.7.1 and 2.8.0, external 2.4.2, local 2.x), or the laptop re-locks the affected roots with terraform providers lock -platform=windows_amd64. Done when an init of each of the six roots succeeds on dell2 with no registry egress.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-S27",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "infra/logic/registry/remediations.json and scopes.json sit CRLF in the shared working tree and LF in a fresh checkout, so a package that bundles them hashes differently by checkout, and a written code rollback that must reproduce a reference hash from a commit cannot be executed.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 6729c4b1bf row S27",
      "adjudication row NFRA_CTLPLN-C-S8"
    ],
    "remedy": "P2. Add an eol=lf rule for infra/logic/registry/*.json to .gitattributes (or have each build normalise line endings, as teams-chat-assist's build does; see W36-S2), then renormalise. Done when git ls-files --eol shows no w/crlf under the registry and a rebuild at a commit reproduces its deployed hash.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-S1",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The laptop accepted Remote Desktop (3389) from any address on every network profile, including its Public-profile Ethernet, where C-RDP (v0.4) requires 3389 scoped to the tailnet only.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S1",
      "adjudication row NFRA_CTLPLN-C-S1 (ADJUDICATION_v1.md), which graduated S1 without minting this row",
      "read by 3.0.0_SA_CVO on the laptop 2026-10-09T00:06Z (Get-NetFirewallRule, inbound enabled Allow rules on 3389): 'Remote Desktop - User Mode (TCP-In) | profile=Any | remote=100.64.0.0/255.192.0.0' and the UDP-In twin, the same scope; network profiles Ethernet 6=Public, Tailscale=Private"
    ],
    "remedy": "Scope inbound 3389 to the tailnet range on every profile. Done: both enabled RDP Allow rules admit only 100.64.0.0/10. Site Z, dell1 and dell2 were not read here.",
    "owner": "3.0.0_SA_CVO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "3.0.0_SA_CVO",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-09T00:06Z"
    },
    "closed": true
  },
  {
    "id": "NFRA_CTLPLN-S9101",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "seeking-alpha's module calls pass source_dir, which modules/yang-lambda does not declare, so the root cannot init at all; AMENDMENT 9 step 4 (every one of six roots inits from the pack) cannot be met as written.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9101",
      "adjudication row NFRA_CTLPLN-C-S9"
    ],
    "remedy": "P1. The issuer either amends step 4 to five roots with seeking-alpha named as a configuration defect, or routes the module-argument fix to the root's owner. Done when step 4's denominator states which roots and seeking-alpha either inits or is excluded by name.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-S9103",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A Dell mirror that already holds aws 5.100.0 unpacked shadows the pack's zip of the same version, and seeking-alpha's lock (no Windows h1) is then refused.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9103",
      "adjudication row NFRA_CTLPLN-C-S9"
    ],
    "remedy": "P1. The kit's install replaces the Dell's mirror with the pack, never merges into it, and dell2's unpacked aws 5.100.0 is removed first. Done when a readback on dell2 inits seeking-alpha's providers from the pack.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v9"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-S9105",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The owned-paths gate admits a worker only as 0.9.0_WK_<CODE>~<digits> holding a non-terminal order issued to it; slot ~K9 is neither, so its org/devices/** edits for AMENDMENT 9 cannot be committed.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9105",
      "adjudication row NFRA_CTLPLN-C-S9"
    ],
    "remedy": "P1. The issuer re-seats the work under a numeric slot that the order is issued to, and that slot commits the three org/devices files from worktree C:/tmp/wk-ctlpln-k9. Done when the edits are on the trunk under a worker author and the order's proof cites them.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v9"
    },
    "closed": false
  }
]
```
