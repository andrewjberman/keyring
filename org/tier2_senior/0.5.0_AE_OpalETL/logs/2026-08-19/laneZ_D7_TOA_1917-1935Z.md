# 0.5.0_AE_OpalETL~Z — D7_TICKETING.TO-AC-SITEZ TO-A session (1917–1935Z)
**archetype:** TRACE

## What happened
- Session start per launcher: /watcher armed (Monitor task bj9j377l1, confirmed running via TaskOutput; no orphan for this serial), registered PID 3248, XXX.md steps A.1/A.2/A.3/D/E run (PATH 91/97 bare + forwarder exercised live; comp-to set to this TO).
- MSTR~Z KICKOFF received 191726Z (canonical triple: prd=D7_TICKETING_INTAKE_PRD.md, workstream=TO-AC, head_version=@36a7fbd70e). ACK'd same-turn with the TO-A plan (192007Z). TO flipped staged→pending as first act.
- **TO-A executed fully, READ-ONLY, in-session (~25 min):**
  - **U1:** 49F DL = `49@opalinvest.com`, Inflection DL = `inflection@opalinvest.com` — both MEASURED via direct toRecipients on real partner requests; Cottonwood DL NOT FOUND (scoped absence: Andrew-mailbox search only; probes cottonwood@/cot@/cca@ all empty, positive control to:49@ returned rows).
  - **U2:** App-2 (client adb3c23a-…, tenant 6810043e-…) APPLIED envelope = code default (live .env sets no GRAPH_SCOPES; 20 var names enumerated on-box) = 17 delegated scopes, never Application; NO Group.*/Mail.Read.Shared; consent adds are the four-way-pin drift hazard (2 measured incidents in IT_REQUEST.md).
  - **CVO-P0-1:** deployed gateway app has NO group/shared-mailbox read path — `/groups` 0 hits, other-mailbox `users/` 0 hits over 31 .py denominator, positive-controlled by sibling `shared` grep; on-box md5 == repo == EC2_MANIFEST @81615fbd3e; app exercised live by this session's own Graph reads. **TO-B does not collapse.** (Inline grep-rc echoes captured head's rc — discarded, zeros evidenced by positive control + denominator instead.)
  - **U3:** NO ticketing-center thread exists (Analyst is member of exactly 1 team, "Opal Capital"; both identities' teams enumerated). Proposal recorded: create "Ticketing Center" channel in "Opal Capital".
  - **Extra measured fact:** Analyst identity allowlist DENIES search_email (identity_scope_denied, fails closed) — TO-C mail-read needs 4.1 allowlisted at TO-B or a widening ruling.
- **Outputs sent 193134Z to MSTR~Z:** the Andrew one-liner (routed per kickoff bound 1) + capability read with ferry request to 2.0.0_SA_COO cc 1.0.0_SA_CTO + 0.7.0_AE_CloudOps. Deliverable: `deliverables/laneZ_D7_TOA_DL_DISCOVERY_CAPABILITY_READ_20260819.md`.
- Surprise channel (banked to MSTR~Z, no action): audit-archive-invoker printed 3 integrity findings at startup (2 non-append edits + jq-ban-override-audit.log missing) — plausibly device-axis baseline class.
- R8 hygiene note surfaced: gateway app IS repo-resident now (`infra/aws/ec2/opal-gateway/` tracked at deployed commit) — PRD's "not repo-resident" predates OPAL_GWRENAME.

## Post-close addenda (1936–1947Z)
- 1936Z Andrew-direct via MSTR~Z: intake identity = opalsupport@opalinvest.com, never opalbloomberg@ externally → deliverable §6a @88db84f6c2.
- 1936–1942Z COO~Z RAVC-4: CONFIRMED 3/3, TO-A closed clean both sides; their SendFromAliasEnabled asymmetry note (INFERRED) folded @56b5ae8796; routing rides MSTR~Z's ferry with the commit pointer.
- 1940Z CTO~Z FYI: §9.8.1 absorbed W-29 M-C/M-I @548b5c6 — binds my W4b certification window (no withheld K.1 artifacts in run dir or quoted in prose until verdict). W5 rerouted to DE~Z.
- **1947Z VINTAGE RE-PIN (MSTR~Z, grounded at ref): D7 close bar @36a7fbd70e → @fac13ccc3a** — verified on-disk: one PRD row added (8+/1-), D7 EXPLICITLY ACCEPTS the ticketing half of sovereign TO #42 (07-14 TAXSMA+ticketing scoping, 36d pending at dead 0.5.0_AE_OpalETL~A — the "taxsma scoping" item in my stale list). TO-A verdict unchanged; **TO-AC CLOSE (TAC-4 proof instance) must cite @fac13ccc3a and run the #42-tie check** — never the stale kickoff pin. #42's disposition (seat-or-supersede) routes to Andrew via D9/COO, NOT this seat.

## Blockers
None on TO-A. TO-C gated: TO-B + U3/U4 + MSTR~Z's 08-20 07:00 WDAC acceptance. Q3 gate-out at Andrew (via MSTR~Z routing).

## Compiler Tools
| Tool + command | Result | Note |
|---|---|---|
| comp-to D7_TICKETING.TO-AC-SITEZ.dl-discovery-plus-analyst-intake-duty | OK, race-free session TO_ID | startup E |
| comp-which "how do I grep the repo" | forwarder RAN (banner) | A.3 exercise, output-scored |
| comp-find "cottonwood" docs data/cot | 473 hits / 1184 files, firm canonical + domain grounding | found cot = Cottonwood Capital Advisors |
| comp-find "mailbox" / "groups" / "scope" infra/aws/ec2/opal-gateway | 17 / 1 / 18 hits with denominators | repo-proxy capability read; BRE alternation trap hit once (0-hit `\|` pattern), re-run with plain terms |
| raw grep infra/aws/ec2/opal-gateway (rail-checked) | GRAPH_SCOPES envelope + IT_REQUEST consent table | marker: Graph-consent doc, no comp-tool models Azure AD scopes |
| Gap noted | comp-estate/comp-iam model AWS, not Graph/M365 consent surfaces | the U2 read had no comp-tool route; on-box SSM + doc read were the instruments |
