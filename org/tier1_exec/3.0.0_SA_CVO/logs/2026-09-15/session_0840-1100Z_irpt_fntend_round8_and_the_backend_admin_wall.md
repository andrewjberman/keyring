# 3.0.0_SA_CVO -- session 2026-09-15 ~08:40Z to ~11:00Z -- IRPT_FNTEND round 8 L8-L10; the portal is the only admin wall; S66 to Andrew

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Continues:** `session_0720-0840Z_mdpf_taxsma_l4r_refuse_then_sign.md` (@977e0dc559).

**Watchers:** no crons. Both Monitors were re-armed from the main root at each 30-minute expiry and confirmed with
TaskOutput. Now: inbox `b1m666bc1`, surprise intake `bynhyttw2`.
- One read ran `cd portal` and moved the session cwd. It was returned to the main root before any re-arm.

## DONE (every act committed; LOCAL -- ls-remote 10:22Z, origin/CLOUD = 6a5b276f8b)

### IRPT_FNTEND round 8 -- L8, L9 and the L10 slug

1. **Drain-end packet 96994** (2.0.0_SA_COO~F): 4 of 4 orders complete, 18 new rows, 4 judgment criteria.

   A fork compiled and graded the round:
   - C-S99..C-S107 @f5a69ab530;
   - REMEDIATION_v5 @db4e444efb, 10 rows;
   - the record and step log @29f54c47c7.
2. **A late between-rounds row.**
   - IRPT_FNTEND-S68 (2.0.0_SA_COO~F, @be5a2a5441, 09:42Z) landed after the packet and before the fork's carrier commit.
     Round 9 was not issued, so no census would compile it.
   - The parent measured it and directed the fork to carry it. 2.0.0_SA_COO~F confirmed it independently (97028).
   - C-S108 @23cad64541 carries S68, GRADUATED to cell (A), with the promote proceeding with F25-AC8 named (97020).
   - The gate's L10 limb had refused the first REMEDIATION_v5 on S68. The bytes were held with no override and admitted
     after C-S108.
3. **Parent re-verification**, by this seat's own reads before the slug:
   - census: 19 new rows (246 against 227), 0 uncarried;
   - REMEDIATION_v5: 10 rows, W1-S74 and W3-S40 DISARMED;
   - standing census: 71 graduated minus 88 remediation ids = 0 missing;
   - portal gate at DEV 10c2f07d: App.tsx:423 and :575 requireAdmin requireInternal; ProtectedRoute.tsx:39 checks role
     and :44 checks firmId opal-capital; 0 partner allowlist entries;
   - origin DEV 9adad7ce contains 43f18c17 and keeps the gate.
4. **The backend wall, read at HEAD.**
   - `infra/aws/lambda/investor-reporting/_scope/resolve.py:186-187` resolves role=admin with a verified firm as
     FIRM_OPERATIONS. Its own note: the header set cannot separate an Opal admin from a partner admin.
   - `_authz/served.py:568-580` refuses only a missing contract version, an absent verified firm, or a binding mismatch.
   - `_authz/enforce.py:272` refuses only UNKNOWN.
   - **So the portal is the ONLY admin wall.** A partner firm's admin calling the API directly would get its own firm's
     data. No route serves yet: IRPT_BCKEND B15 builds them.
5. **Slug sent** 10:37:19Z, 3711 bytes. Step log L10 row @496a89e4b5.
6. **1.0.0_SA_CTO's round-8 analysis** (97045, @4d9f719f8d):
   - S66 goes to ANDREW, and the CTO recommends yes: the backend refuses non-(admin AND opal-capital) before any route
     serves.
   - W3-S41 is fixed in proof-of-spec-check @ae97defa81.
   - Round 9 is ONE issuance of cells A-G, all test-side or render text.
   - 0.0.0_AB_MSTR seats round 9's COO, and 2.0.0_SA_COO~F frees.

### Intake

- **LGIC_ENFORCE (68 rows).** S16 disarms W1-S18, and S13's fix is now exercised. Every ARMED row seen has a disarm or
  disposition.
  - S17: the shared index briefly held the pre-drain blobs of 2 drained paths.
    - This seat is named only among the authors of the 7 commits in that window, none touching either path, and the
      writer is unidentified.
    - The shared index read 0 staged entries when checked.
- **NFRA_OPLGTW channel opened.** S1 (2.0.0_SA_COO~O, INERT): the Gateway suite fails
  test_scoped_deny_by_default at the cut base, because it expects opal_data_refresh_upload DENIED to the Bloomberg
  identity while the allowlist overlay grants it. It is graded at that project's round-1 L8.
- **Inbox:** 96994, 97028 and 97045 READ-acked.

## OPEN

- **S66 is Andrew's decision**, through 1.0.0_SA_CTO's REC yes: a backend admin wall before B15 serves.
- **IRPT_FNTEND round 9:** L8/L9 at drain-end. Grade W3-S41's fix @ae97defa81, and cells A-G against REMEDIATION_v5's
  OPEN rows.
- **LGIC_ENFORCE round 1, LGIC_NAMING round 3, NFRA_OPLGTW round 1:** L8/L9 at each drain-end.
- **MDPF_TAXSMA:** the brief half is owed by 4.0.0_SA_CRO. Backfill (b) continues per gap between rounds.
