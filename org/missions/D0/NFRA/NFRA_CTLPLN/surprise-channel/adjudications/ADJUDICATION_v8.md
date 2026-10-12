# NFRA_CTLPLN: CVO L9 grades and L8 dispositions at the round-6 close (2026-10-12)

L9/L8 by `3.0.0_SA_CVO~L` (laptop), on 2.0.0_SA_COO~C msg 108474. HEAD 5b2a1ffc1e.

**L9.** TO-APPLY-9 AC2 MET (C-S16); TO-APPLY-31 AC2 MET (C-S17). These were the two items that left round-close-check at REFUSED.

**L8.** Five rows are DISMISSED: W61-S8, W62-S1, W62-S6, W62-S7 and W62-S8 (C-S18 to C-S22).

**Not dispositioned here:**
- **W61-S1 stays ARMED.** It is live on this laptop at ~06:3xZ, read by this seat (see below). Its disarm owner is Andrew,
  because the act needs elevation.
- **D1-S8 stays HELD to GRADUATE** (ADJUDICATION_v7). TO-CT-x-1 is now complete @ef9332dbfd, but three round-7 orders read
  `staged`: TO-CT-u-3, TO-CT-u-4 and TO-CT-u-5 (93 orders read, 90 complete, 1 cancelled). The row gate counts `staged`
  as non-terminal (`TERMINAL_TO_WORDS`, `.tools/surprise-row-gate.py:179`), so it still refuses a new remediation row.

**W61-S1 as read by this seat, 2026-10-12 ~06:3xZ.**
- The firewall rule "OpenSSH Server (Tailscale only)" is enabled, Allow, Profile=Any, RemoteAddress=Any.
- It is the only inbound allow rule on 22. sshd is Running and listens on 0.0.0.0:22 and :::22.
- No `PasswordAuthentication` line is set, so password login is on by default. No `administrators_authorized_keys` and no
  user `authorized_keys` exist.
- The Wi-Fi interface is category Public; Tailscale is Private.
- So the laptop accepts an SSH password login from its Wi-Fi network. One elevated line closes it:
  `Set-NetFirewallRule -DisplayName "OpenSSH Server (Tailscale only)" -RemoteAddress 100.64.0.0/10`.
  `Stop-Service sshd` also closes it until FWD-27's per-box cell runs.

<sweep_watermark>2026-10-12T06:40Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S16",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "L9: NFRA_CTLPLN.TO-APPLY-9 AC2 MET -- the targeted apply added exactly the signed statement to the transcripts key, changed no other statement, and the statement is live today as signed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-APPLY-9 (cell CT-a-1, amendment 3): ONE targeted update of aws_kms_key.transcripts adding Sid DellAgentUsersDecryptOnly, Allow, kms:Decrypt + kms:DescribeKey, principals exactly the two Dell agent users, Resource *; zero removed lines; NamedReadersUseTheKey unchanged; both never-widen halves' conditions carried.",
    "world_is": "PRIOR9 vs AFTER9 key policy (0.7.0_AE_CloudOps~E deliverables), parsed: the sids go from 2 to 3, the one added statement is exactly the signed one field by field, and 0 existing statements changed. APPLY9 reads 'Plan: 0 to add, 1 to change, 0 to destroy' under -target and 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. LIVE today (kms get-key-policy, key 44a2284f..., alias/opal-data-transcripts): DellAgentUsersDecryptOnly is byte-equal to AFTER9; a planted mutant (kms:Encrypt added) compares unequal. The live policy also carries three statements and a changed NamedReadersUseTheKey added later by other orders (NFRA_TRNSPT TR-p-18/TR-r-21/TR-k-21 and CT-a-1 amendments 25-28); none is this act's. The grant is APPLIED; this seat made no decrypt call, so EXERCISED is not claimed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PRIOR9_key_policy_transcripts_20261007.json vs AFTER9_key_policy_transcripts_20261007.json, parsed by this seat",
        "org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/APPLY9_transcripts_key_20261007.txt:96,123",
        ".tools/aws kms get-key-policy --key-id 44a2284f-1e14-4ea1-b6cb-f6121bfde35a, 2026-10-12 ~06:3xZ",
        "git log infra/aws/terraform/transcripts/main.tf: 386a6f9d3d, 42f4a3777c, 24cee5a20d, 0693227a69, 3c68dab9c9, 5cf0b9a367"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a hazard: the judgment criterion is MET."
  },
  {
    "id": "NFRA_CTLPLN-C-S17",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "L9: NFRA_CTLPLN.TO-APPLY-31 AC2 MET -- the round-8 drafting contract was live from 2026-10-09 23:03Z and its one real drafting call answered ok=True outcome=post.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-APPLY-31 (cell CT-i-14): code-only targeted deploy of module.ldo_001, branch A 0/2/0; the drafting contract means only post can reach Teams; APPLIED until the first real drafting call, whose draft_contract outcome is the exercise.",
    "world_is": "The issuer's closure records branch A 0/2/0, both functions at SFSTGBQX... from 23:03Z, ledger 20261009T2245Z closed, proof VALID. This seat counted log events in the window the round-8 code was live (2026-10-09 23:03:08Z to 2026-10-11 02:16:55Z, when CA r14's deploy replaced both functions; today both read nIQW+3Xv...). In /aws/lambda/teams-global-chat-assist-handler-lambda the filter draft_contract returns 1 event, at 2026-10-10T20:47:32Z, structured {event: draft_contract, ok: True, outcome: post, applied: 0, not_applied: 0}. The positive control, ingress_poll in the ingress group, returns 1634 events in the same window. One call is the exercise the order named; the outcome is the contract's post, not a refusal. Message content was not read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.7.0_AE_CloudOps~CTL/task_orders/NFRA_CTLPLN.TO-APPLY-31.teams-agent-r8-draft-contract-code-deploy-laptop.md <closure>",
        ".tools/aws logs filter-log-events (handler group, pattern draft_contract, window above): 1 event, no nextToken",
        ".tools/aws logs filter-log-events (ingress group, pattern ingress_poll, same window): 1634 events, no nextToken",
        ".tools/aws lambda get-function-configuration, both functions: nIQW+3Xv..., LastModified 2026-10-11T02:16:5xZ",
        "data/transcripts/scripts/teams_chat/assist.py:649 (the draft_contract log line's fields)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a hazard: the judgment criterion is MET, and EXERCISED by one real call."
  },
  {
    "id": "NFRA_CTLPLN-C-S18",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "W61-S8 disarmed in code: ssh-tailnet-verify's password arm now reads the server's advertised methods (PreferredAuthentications=none) and prints ADVERTISED:<list> when a password is offered.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W61-S8: under BatchMode the password arm read REFUSED whatever PasswordAuthentication was, so a box could read done with password login on.",
    "world_is": ".tools/ssh-tailnet-verify.py at HEAD 5b2a1ffc1e: lines 14-17 and 112 drive ssh with PreferredAuthentications=none and PubkeyAuthentication=no and read the server's method list; line 157 returns ADVERTISED:<methods>; line 23: done only when password_arm=REFUSED. The drain ae15aef88e (2.0.0_SA_COO~C) re-ran selftest 8/8 and read the laptop as password_arm ADVERTISED, which matches this seat's sshd_config read (no PasswordAuthentication line).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/ssh-tailnet-verify.py:14-23,59,112,157 read at HEAD 5b2a1ffc1e",
        "git show --stat ae15aef88e"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W61-S8"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The arm now discriminates, and it reads the laptop correctly as ADVERTISED. No remedy is owed."
  },
  {
    "id": "NFRA_CTLPLN-C-S19",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "W62-S1 overtaken by ruling before any apply: PRD v0.24/v0.25 fences by route class, leaves the content GET and the 2 partner-reached data-proxy routes open as today, and binds CT-u-7 to a no-regression clause.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W62-S1: a tier-only fence answers partner pages' content GET and data-proxy reads 403.",
    "world_is": "No fence is applied (CT-u-7 is not cut). PRD v0.25 FWD-28 (signed @4af2d1a4f1): class (ii) internal-only, class (i) open as today, content GET open to every verified login, and 'no page a partner login can open today changes what it shows that login'. The drain 6a1607d1e0 replaced the tier-only tests with test_route_class_fence.py and test_get_open_put_delete_fenced.py. RESIDUAL for CT-u-7: the row names six partner pages reading the data proxy, while the later census of the same worker (DATA_PROXY_ROUTE_CLASS_CENSUS.md, ROUTES total=41) finds 2 routes reached by partner pages. CT-u-7's no-regression proof must render those six pages as a partner, not rely on the census alone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md v0.25 @579b691872, FWD-28",
        "git show --stat 6a1607d1e0",
        "DATA_PROXY_ROUTE_CLASS_CENSUS.md @7b375c4002 line 7 and section 4"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W62-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The CTO ruled before the fence was applied, and FWD-28's ACCEPT carries the guard. The residual is a criterion note for CT-u-7, not a separate remedy."
  },
  {
    "id": "NFRA_CTLPLN-C-S20",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "W62-S6 resolved by amendment 2: no generated firm-set module ships, so no firm token reaches the naming gate; the class-(i) firm check is carried by FWD-28 v0.25 behind an opal_naming registry row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W62-S6 (BLOCKING): the naming limb refuses firm_access_generated.py, so the data-proxy fence cannot land from CT-u-6's paths.",
    "world_is": "6a1607d1e0 merges CT-u-6 amendment 2: portal_data_proxy/lambda_function.py changes 39 lines and no firm_access_generated.py is in the commit; the issuer's ruling line reads 'W62-S6 resolved in code by PRD v0.25 (no firm token)'. CTO msg 108446 rules the firm check for the 2 class-(i) routes lands when the module is an opal_naming target under infra/logic/registry/, cut as a cell (no R20 departure, no hand-typed name). FWD-28 v0.25 ACCEPT states the same, so FWD-28 cannot grade REALIZED until that row lands.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show --stat 6a1607d1e0 (10 files; no firm_access_generated.py)",
        "1.0.0_SA_CTO msg 108446",
        "NFRA_CTLPLN_PRD.md v0.25 FWD-28 ACCEPT"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W62-S6"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The block is gone from the merged code. The remaining work, the registry row, is owned by the ENDPOINT and the CTO ruling, so a second carrier here would duplicate it."
  },
  {
    "id": "NFRA_CTLPLN-C-S21",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "W62-S7 accepted as ruled: an internal caller on an unmatched data-proxy path gets the handler's own 404; every non-internal caller gets 403. Nothing leaks.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-u-6 AMENDMENT 2: an unmatched path answers 403.",
    "world_is": "The issuer ruled in 6a1607d1e0: 'an internal caller on an unmatched path gets the handler's own 404 (no data leaks, accepted)'. A 404 to an internal caller discloses nothing that a 403 would hide, and a second 41-route table inside the gate would be the second list FWD-28 forbids.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 6a1607d1e0 (commit message rulings; INVESTIGATION_v1.md W62-S7 block)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W62-S7"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The issuer's ruling holds; there is no exposure."
  },
  {
    "id": "NFRA_CTLPLN-C-S22",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T06:40Z",
    "one_line": "W62-S8 is by design: the two class-(i) routes stay ungated in the handler, as today, so their only login check is the API Gateway authorizer, per CTO ruling 108445 and PRD v0.25.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CT-u-6: the gate fails closed on a missing, empty or null tier.",
    "world_is": "The fail-closed rule holds for the 39 class-(ii) routes. For the 2 class-(i) routes, FWD-28 v0.25 states 'class (i) stays as today, open to every verified login' until the registry row lands; the issuer's ruling in 6a1607d1e0 cites CTO 108445. The authorizer in front of the proxy is unchanged by this round, so the behavior today is unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_CTLPLN_PRD.md v0.25 FWD-28 ACCEPT",
        "git show 6a1607d1e0 (commit message rulings)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W62-S8"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The ruling and the spec state it, and the round leaves it as before. The firm check that tightens it is FWD-28's registry-row step."
  }
]
```
