# NFRA_OPLGTW -- surprise channel, REMEDIATION v19 (site Z) -- THE ROUND-36 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-13 ~20:2xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 36 reads MAY-CLOSE (re-run by this seat), with 4 of 4 orders complete and 0 judgment criteria. Nothing was
deployed. L8 is at `adjudications/ADJUDICATION_v27.Z.md`:
- **Dismissed (4):** Z-W61-S1, Z-W61-S2, Z-W63-S1 and Z-W62-S1. The packet omitted Z-W62-S1 from its rows and
  counted 4 new rows; there are 5.
- **Graduated (1):** Z-S101, below.
- **Z-S95 is partly met.** The 502s are localised to the ALB/target connection, but the cause is inferred. They still
  recur: 2 of 1440 polls failed in the 24 h to ~20:2xZ, re-read by this seat. Next step: read the host journal for the
  failing instants.
- **Built, not met:** Z-S100 and Z-S91 wait on the per-family releases.
- **For the release pair:** OG-fd-2 also moves schwab's drain before the lanes. Its ask discloses this at `:12`; the
  packet's "no existing key changed" does not.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S101",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "OG-pf-1 and OG-tg-1 ('r30'), OG-bd-2 and OG-sh-1 are built and drained but not on the live ref 185dc04888 (DATA_GRANT_TOOLS 0 live vs 5 at HEAD), and no release order was ever cut for r30, so Andrew's 10-09 Opal-users-only and mirror words are built, not served",
    "evidence": [
      "NFRA_OPLGTW-Z-S101 (2.0.0_SA_COO~O)",
      "3.0.0_SA_CVO~Z re-read of DATA_GRANT_TOOLS at 185dc04888 and HEAD",
      "ledger/CTO_RULING_R37_ONE_RELEASE_PF1_TG1_BD2_SH1_20261013.md @8f236865cc"
    ],
    "remedy": "One release in round 37 on the live ref, after NFRA_MCPORTAL MP-z-5's ledger closes. It carries pf-1 + tg-1 + bd-2 + sh-1, a CTO + COO pair names all four, and every other unreleased app/ diff is listed as excluded or carried. The two grant writes stay a separate act. The cut template gains this rule: a deferred-release build cell names the release order it rides.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v19"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
