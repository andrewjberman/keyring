# NFRA_OPLGTW -- adjudication v16 (site Z): round 24's L8 (OG-up-1, OG-hg-1, the r25 release OG-rl-11)

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T10:25:00Z. Trigger: `2.0.0_SA_COO~O` msg 30784 (round 24 TERMINAL, 3 of 3
complete). This seat compiles on `1.0.0_SA_CTO~Z`'s ruling msg 30783 (`3.0.0_SA_CVO~O` and `1.0.0_SA_CTO~O` are not
live); the slug's one send goes to `1.0.0_SA_CTO~Z`.

**Terminality.** All 3 orders read `<status>complete</status>`, round 24. The round carries no judgment criterion, so
it has no L9 grade. This seat re-ran the 8 checks at CLOUD @e9e43448dc, 10:1xZ:
- PASS, 6 of 8: hg1.AC1 (4 of 4 cases), hg1.AC2, up1.AC1 (5 of 5), up1.AC3 (2 of 2), rl11.AC2 (66 tools, status tool
  OK, inline wait <= 60 s, ssm Success), rl11.AC3 (ssm Success).
- FAIL on re-run, 2 of 8, both on the one conjunct that compares live to a CLOUD that has since moved: up1.AC2
  ("allowlist file changed since live: 1") and rl11.AC1 ("gateway files differing live..CLOUD 10"). Every other
  conjunct of both holds: failures beyond the live baseline 0; deployed 240ac2fe5a descends from 7d65a28db0; host
  shipped files equal the release bytes 5 of 5; ledger entry 1, sentinel gone; floor yes/yes. The 10 files are r26's
  6 (OG-al-2, OG-up-2) plus the ETFS_RIVALS chart route's 4 (`git diff --name-only 240ac2fe5a HEAD`, 11 with the
  runbook). So the two criteria are not re-runnable once the next round's cells drain; they are not read here as a
  round-24 failure.
- hg1.AC2 passes on "failed no more than baseline": `.tools/test-haltgt-recipient-scoping.sh` reads 0 passed, 9
  failed, equal to its cut baseline of 9. A suite that passes 0 of 9 guards nothing; recorded in C-S46.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 386 investigation items, 43 adjudication rows, 86
remediation rows; 5 OPEN, 0 ARMED. This file adjudicates the 5:
- **GRADUATED (4), C-S44:** Z-S64 and Z-W28-S11 (to the CTO); Z-S65 and Z-W28-S13 (to the issuer).
- **DISMISSED_WITH_REASON (1), C-S45:** Z-W28-S12.
- **C-S46** records the in-place advance of Z-S63 and Z-W28-S7 to REMEDIATED and the two instrument notes above.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S44",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-07T10:25:00Z",
    "one_line": "Round 24 L8: 4 rows GRADUATE OPEN -- the rivalfunds audit record cannot say which page was served (Z-S64), the scoped identity's narrowed consent does not narrow its token until it signs in again (Z-W28-S11), the status tool sends a caller-supplied id into the URL path unchecked on live r25 (Z-S65), and the status tool's displayed_date is null against the served manifest (Z-W28-S13).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-S64: audit.py _safe_args drops every arg of a tool absent from _ARGS_ALLOWLIST (audit.py:116-119 at HEAD) and rivalfunds_view passes no bytes, so the page, audit and archive routes write one indistinguishable record; the ETFS_RIVALS round-13 ruling names the gateway access record (status, identity, size, time) as the proof of a served audit page, and no single record holds all four. The r26 chart route adds a fourth route with the same args dropped (rivalfunds_view.py:252-256: day, fund, route). Z-W28-S11: the consent URL and the silent-acquire request narrow to 9 scopes, but the token Entra returns from the existing refresh token still lists the 17 consented Graph scopes plus CallTranscripts.Read.All; the release does not change the identity's Graph reach until a fresh /login consent. Z-S65: live 240ac2fe5a formats the caller's execution_id into the status path after an empty-string check only; the shape check exists on CLOUD (integration.py:170, _EXECUTION_ID_RE.fullmatch, commit 82da719ba2, with tests/test_opal_portal_status_id_shape.py) and is not deployed. Z-W28-S13: _manifest_date's key list (integration.py:157 at HEAD, unchanged from live) matches none of the served manifest's five keys, so displayed_date is null where the order says the tool returns the displayed date; r26 does not carry a fix. Its second half (the read-only tool sits behind the mutating spec's min_tier) is a disclosed property of the per-spec floor, carried in the same remediation row.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S64",
      "NFRA_OPLGTW-Z-W28-S11",
      "NFRA_OPLGTW-Z-S65",
      "NFRA_OPLGTW-Z-W28-S13"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S64, #Z-W28-S11, #Z-S65, #Z-W28-S13 (read whole by this seat)",
        "git grep at HEAD and at 240ac2fe5a over app/integrations/opal_portal/integration.py: _EXECUTION_ID_RE.fullmatch at HEAD :170, absent at 240ac2fe5a; _manifest_date key list identical at both",
        "git grep at HEAD over app/audit.py (:72 _ARGS_ALLOWLIST, :116-119 the fail-closed omit) and app/rivalfunds_view.py (:185-269, 9 audit.log_call sites, none passing bytes)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~28/r25_after_stage_scopes.out and r25_manifest_keys.out (the worker's runs; not re-run by this seat)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S45",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-07T10:25:00Z",
    "one_line": "Round 24 L8: Z-W28-S12 is DISMISSED_WITH_REASON -- the host key is named TAXSMA_WORKBOOK_IDENTITY, it names the scoped concierge, and the release's consent covers its caller scope, so the pre-GO read found no STOP.",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "The order's key name OG_TAXSMA_WORKBOOK_IDENTITY is a deploy-shell input the host never reads (deploy-to-ec2.sh:174); config.py:280 reads TAXSMA_WORKBOOK_IDENTITY. The worker read the key under its host name and found it true and covered: consent_scopes = 9 with Files.ReadWrite.All. rl11.AC3 re-run by this seat: identity keys read, fields=yes, ssm=Success, RESULT: PASS. The order's '8, or 9 under a Tax binding' resolves to 9 on this host.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W28-S12"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S12",
        "deliverables/2.0.0_SA_COO~O/r25/checks/rl11.AC3.sh re-run by this seat: RESULT: PASS exit=0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A naming difference between the order and the host, read correctly by the worker; the condition it guards (a true key not covered by consent) is measured false. The issuer may correct the key name in the next order that cites it; no remediation row is owed."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S46",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-07T10:25:00Z",
    "one_line": "Round 24 L8: Z-S63 and Z-W28-S7 advanced in place to REMEDIATED on this seat's re-runs; two instrument notes -- up1.AC2 and rl11.AC1 stop passing once the next round drains into CLOUD, and hg1.AC2's baseline suite passes 0 of 9.",
    "class": "OBSERVATION",
    "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read. Z-S63's remedy: the tool returns right after /trigger and a read-only status tool carries the polling. Z-W28-S7's remedy: (1) the halt gate reads the order from the shared root and the LAST status tag; (2) the release form names the deploy identity.",
    "world_is": "Z-S63: r25 @240ac2fe5a is live (rl11.AC1: host shipped files equal the release bytes 5 of 5) and rl11.AC2 reads the send split served: 66 tools, status tool OK, inline wait <= 60 s, no real send run, ssm Success. The first real send through the split is not read by this seat. Z-W28-S7: hg1.AC1 passes 4 of 4 cases (part 1); RELEASE_ORDER_FORM.md:43 carries the DEPLOY IDENTITY step and :51 the manifest commit (part 2). Instrument note 1: up1.AC2 and rl11.AC1 each compare live to CLOUD HEAD, so both read FAIL at 10:1xZ only because r26's 6 files and the chart route's 4 have drained into CLOUD; the round-24 orders were closed before that. A check that pins the comparison to the round's own drain commit would stay re-runnable. Instrument note 2: hg1.AC2 accepts .tools/test-haltgt-recipient-scoping.sh at 0 passed, 9 failed because the cut baseline was 9 failed; the gate's recipient-scoping behaviour is therefore unguarded on this device. Round 25's cells (OG-al-2, OG-up-2) were built and drained before this slug existed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/r25/checks/ hg1.AC1, hg1.AC2, up1.AC1, up1.AC2, up1.AC3, rl11.AC1, rl11.AC2, rl11.AC3 re-run by this seat 2026-10-07 10:1xZ: 6 PASS, 2 FAIL on the live..CLOUD conjunct",
        "git diff --name-only 240ac2fe5a HEAD -- infra/aws/ec2/opal-gateway: 11 files (10 beside the runbook)",
        "deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md:43 and :51",
        "remediations/REMEDIATION_v10.md#NFRA_OPLGTW-Z-S63 and #NFRA_OPLGTW-Z-W28-S7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~Z
