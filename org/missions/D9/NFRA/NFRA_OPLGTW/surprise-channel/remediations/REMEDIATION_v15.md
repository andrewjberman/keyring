# NFRA_OPLGTW -- surprise channel, REMEDIATION v15 (site Z) -- THE ROUND-32 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z` for `3.0.0_SA_CVO~O`, 2026-10-09 ~17:0xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 32 is terminal: 14 of 14 orders complete. round-close-check reads MAY-CLOSE.

**L9**, in `ADJUDICATION_v23.Z.md`:
- C-S59: OG-bf-1 AC3 PASS.
- C-S60: OG-da-1 AC3 PASS, bounded (1 of 6 callers has called since the deploy).

**L8:** C-S61 (26 dismissed) and C-S62 (15 graduated, below).

**12 rows are left OPEN on purpose:** they belong to round 33, still in flight (bh-1, tl-1 and ab-2 pending), and none is
BLOCKING or ARMED. The row gate needs every BLOCKING or ARMED row in the project dispositioned, so the in-flight W48-S1 and
W49-S5 are dismissed (resolved by W48-S3 and W49-S6), and W49-S1, W49-S3, W49-S4 graduate with their issuer as owner.
W35-S1 graduates too: its round-30 order OG-dr-1 still reads `pending`, a stale order the issuer closes or re-cuts.

**For the CTO's round-32 analysis:**
- **W44-S4: a widening still to come.** The tg-1 mirror makes the concierge's `/login` consent ask the full GRAPH_SCOPES
  envelope (Mail.Send, Mail.ReadWrite, Files.ReadWrite.All and more). tg-1 is built and held for r30. r30's never-widen ask
  must name each scope the consent gains, and the CVO half reads it before the release.
- **W42-S1: still live.** The grant-writer Lambda refuses `calendar_months` until it is rebuilt from r29.
- **W43-S7: still live.** A cold 13-month read takes about 4 minutes per master.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-W38-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "proof-of-spec-check count-bar misreads a pytest summary placed after \"passed N\", so a verbatim line cannot be recorded",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W38-S1, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "fix the count-bar so it reads the criterion count, not a summary parenthetical",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W39-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "sdd-daily-pull.ps1 -Mode enumerate exits without Release-SessionLock, leaving a stale lock on SI2",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W39-S1, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "release the lock on the enumerate branch",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W39-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the enumerate summary prints a one-file type range as 2..0",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W39-S2, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "index the date range by file, not by character (cosmetic)",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W39-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "opal-assets (cot-rebalancer-runner-daily cron) and opal-gateway (mcportal-grant-writer code hash) each carry an unrelated unapplied change that a whole-root apply would also make",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W39-S5, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "route each drift to its owner; until then every apply on those roots stays targeted",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-S69",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lambda-source-map.json is stale for opal-assets-silver-schwab after the Leg C deploy (artifact_sha256, last_deployed_commit, last_deployed_at)",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-S69, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "refresh the three fields to the deployed AzrzJS+9 build",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S70",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the advi-49f-gold-dispatch zip cannot carry BUILD_MANIFEST.json, which both OG-bf-1-Y halves and the source map _build_note say it does",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-S70, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "commit a BUILD_MANIFEST.json for the function, or correct the _build_note and the halves",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W42-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "the grant-writer Lambda ships a stale copy of data_entitlement.py and the contract, so it refuses every calendar_months grant (Phase C used the CLI)",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W42-S1, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "rebuild and redeploy the grant-writer package from r29 under its own pair",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W43-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "a cold 13-month availability read for Alyssa costs about 221-235 s per master (443-470 s for both) against the query caps",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W43-S7, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "decide warming or a cap before Alyssa relies on 13-month reads",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W44-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "sender_upn is null on every channel path until User.ReadBasic.All is consented (fails closed)",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W44-S2, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "put the consent to Andrew, or accept null on channel paths in the PRD",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W44-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "two tests outside tg-1 paths (test_transcript_tools, test_login_admit_r24) pin the concierge as scoped and fail after the mirror",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W44-S3, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "re-pin both tests in the r30 release cell",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W49-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "the transcripts bucket KMS key policy gives the gateway role no use of the key, so no s3:PutObject grant alone can make the .pptx pair write once released",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W49-S1, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "add the gateway role to the key policy readers/writers under a pair before the E2 release",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W49-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "two writers share the market_update prefix with different object-name rules (deck_<sha16>.pptx vs the sanitized original), so one deck can land twice under two keys",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W49-S3, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "pick one naming rule for the prefix before both writers ship",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W49-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "the market_update PutObject grant was not added: the only registry-read form puts the hand-kept token transcripts in advi_billing_gateway_iam.tf, which the naming gate refuses",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W49-S4, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "add the registry row (or an R20 entry) the naming gate needs, then the grant",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W35-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "the 21:49Z gateway stop drained cleanly; Z-S67 trigger stays inferred, and a restart-free route to the same lost answer exists in server.py; its round-30 order OG-dr-1 still reads pending",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W35-S1, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "close OG-dr-1 or re-cut it, and carry the restart-free route to a cell",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W44-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "after the OG-tg-1 mirror, the concierge /login consent asks the full GRAPH_SCOPES envelope (Mail.Send, Mail.ReadWrite, Files.ReadWrite.All and more); tg-1 is BUILT and HELD for r30, not deployed",
    "evidence": [
      "investigation row NFRA_OPLGTW-Z-W44-S4, read via comp-surprise ~16:3xZ"
    ],
    "remedy": "the r30 never-widen ask names the consent envelope delta per scope; the CVO half reads it before the release",
    "owner": "2.0.0_SA_COO~O",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v15"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
