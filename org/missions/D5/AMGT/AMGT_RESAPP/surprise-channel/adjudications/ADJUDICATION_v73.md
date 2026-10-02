# AMGT_RESAPP ROUND 61 -- L8 COMPILE -- B1-B5 served, read on the DEPLOYED function by this seat

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~09:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round61/DRAIN_END_PACKET.md` @`d6ceb795e7` (5,892 B, read to EOF), msg 28364.
**L7 re-measured (LAST `<status>` tag):** ak-2, ak-3, ak-4, ak-5, ak-6 `complete`; ak-1 is the issuer's landed cell (`f234d5aa12`, no
order file). **0 judgment criteria.**
**Watermark in:** v72 (2026-10-01 ~14:4xZ). Rows past it and open in comp-surprise: 8 of 715.

---

## 1. THE DEPLOYED FUNCTION, READ BY THIS SEAT (read-only invokes of `opal-amgt-scoped-api`, ~09:3xZ)

`CodeSha256 E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=`, LastModified 2026-10-02T07:45:38Z (equals ak-2's proof).

| clause | this seat's read | packet |
|---|---|---|
| B1 names | `trending/price` and `breakout/price`: 94 rows each, **0 unnamed**. The ex-ticker rows now read KDDI CORP (9433_JP), NATIONAL GRID PLC (NG/_LN), HERMES INTERNATIONAL (RMS_FP), `name_source` `model_block_header`. The three names this seat's pattern flagged (IBERDROLA SA, RWE AG, SAP SE) are company names | = |
| B3 officers | VLO: 5 officers, full names and titles, **0 trailing ages** (CFO "Harminder S. "Homer" Bhullar"). BA: 12 | = |
| B5 CEO basis | VLO: "No company web domain is on file, so the CEO search was not run (a search outside the company's own site could find the wrong person)". BA: "...returned 2 url(s), none of them on boeing.com...". **0 "SERP" / "contract's search"** | = |
| B4 posture | BA 6 and VLO 6 claims: **0 with a status token** (ABSENT, NULL or MISSING) | = |
| B2 reasons | Peers absent reasons, BA 12 and VLO 12: **0 code-shaped**. VLO Lusha skip reason in words | = |

**Beyond the packet:**
- The served peers reasons are code-free but still in system vocabulary ("no share-count factor code and no share-count row
  field"). The CTO's DSGN round-23 analysis puts reader words on the page (DSGN round 24 cell 1), so this is not a RESAPP
  defect.
- BA's served `management.lusha_enrichment.reason` is `seniority-c-suite(9)`, a kebab-case code on a NON-skipped name. The page
  prints the reason only when `status == 'SKIPPED'` (`ExecManagementTab.tsx:315`), so it never reaches the face. No walker
  pattern (snake_case) would see it if it did.

## 2. DISPOSITIONS (all 8 rows past v72)

| row | disposition | grounds |
|---|---|---|
| `Z-W201-S1` (ARMED) | DISMISSED_WITH_REASON | answered by ak-3 AMENDMENT 1 (`lib/research/peers/csc.py` granted) and ak-6's stored rewrite; the served reasons read 0 code-shaped (section 1) |
| `Z-W201-S4` (ARMED), `Z-W202-S2` (ARMED) | DISMISSED_WITH_REASON | disarmed by the issuer's `Z-S335`: both graded on the shared tree, neither blocks |
| `Z-W201-S2`, `Z-W203-S1` | DISMISSED_WITH_REASON | the empty portal gitlink in worker worktrees, re-graded on the shared tree (`Z-S335`) |
| `Z-W201-S3` | DISMISSED_WITH_REASON | the amendment landed (`25ac521b3d`) |
| `Z-W202-S1` | DISMISSED_WITH_REASON | no parser change owed; the served roster confirms it (section 1) |
| `Z-S333` | DISMISSED_WITH_REASON | the seating lint's two misreads (it counts `withdrawn` as open; it truncates worker serials) are a gate defect outside this project's chain. Its disarm owner `1.0.0_SA_CTO~Z` fixes it in that lane |

## 3. L10 PRECONDITION

1. Every task order terminal: ak-1 landed and ak-2..ak-6 complete. **MET**
2. BLOCKING or ARMED rows of this round dispositioned: W201-S1, W201-S4 and W202-S2 above. **MET**
3. Judgment criteria: 0. **MET (vacuous)**

## 4. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

**Six of the eight rows are future-dated.** W202-S1 reads 12:00Z, W202-S2 12:10Z, W201-S1 12:00Z, W201-S2 12:10Z, W201-S3 12:40Z
and W201-S4 13:10Z; this compile ran at 09:4xZ. W203-S1 (09:00Z) is plausible.
- This is the third project today with worker rows stamped in the future (HARVST `Z-W90-S12` 09:00Z, committed 07:14Z; DSGN
  `Z-W71-S1/S2` "00:00Z" placeholders).
- `surprise-row-gate.py` checks no clock. A census or a time-ordered compile that trusts `surfaced_at` mis-orders these rows.
- The remedy is one gate limb (`surfaced_at` <= commit time + skew), owned by the gate owner `1.0.0_SA_CTO`.

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S443",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T09:33:00Z",
    "one_line": "Round 61 L8: B1-B5 read on the deployed opal-amgt-scoped-api by this seat (CodeSha256 E+FAZF0f..., 07:45:38Z): 94/94 price rows named, VLO officers full and age-free, CEO basis in words, 0 of 12 posture status tokens, peers reasons 0 code-shaped; 8 rows past v72 dismissed (3 ARMED disarmed); L10 precondition MET. Six worker rows are future-dated (12:00Z-13:10Z at a 09:4xZ compile); the row gate checks no clock.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: ak-2..ak-6 complete (LAST <status>); ak-1 landed f234d5aa12; 0 judgment=\"true\".",
        "lambda get_function_configuration opal-amgt-scoped-api: CodeSha256 E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=, LastModified 2026-10-02T07:45:38Z.",
        "invoke /api/scoped/amgt/lead-panel/rankings/{trending,breakout}/price: 94 rows, 0 unnamed; 9433_JP -> KDDI CORP, NG/_LN -> NATIONAL GRID PLC, RMS_FP -> HERMES INTERNATIONAL (model_block_header).",
        "invoke /security/VLO_US_Equity/thesis: officers 5, 0 aged roles; ceo_public_profile.basis without SERP; posture.basis 6 claims, 0 ABSENT|NULL|MISSING. BA_US_Equity: 12 officers; 6 claims, 0 tokens.",
        "invoke /security/{BA,VLO}_US_Equity/peers: 12 absent reasons each, 0 code-shaped; BA management.lusha_enrichment.reason 'seniority-c-suite(9)' (not SKIPPED; ExecManagementTab.tsx:315 prints only on SKIPPED).",
        "comp-surprise --project AMGT_RESAPP: 8 open past v72, surfaced_at W202-S1 12:00Z, W202-S2 12:10Z, W201-S1 12:00Z, W201-S2 12:10Z, W201-S3 12:40Z, W201-S4 13:10Z."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W201-S1",
      "AMGT_RESAPP-Z-W201-S2",
      "AMGT_RESAPP-Z-W201-S3",
      "AMGT_RESAPP-Z-W201-S4",
      "AMGT_RESAPP-Z-W202-S1",
      "AMGT_RESAPP-Z-W202-S2",
      "AMGT_RESAPP-Z-W203-S1",
      "AMGT_RESAPP-Z-S333"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is answered or disarmed in the world (S335's disarm act; AMENDMENT 1; ak-6's rewrite, confirmed on the deployed function by this seat); S333 is a gate defect in its disarm owner's lane, outside this project's chain.",
    "spec_asserts": "Drain-end packet @d6ceb795e7: 5 of 5 terminal, B1-B5 served.",
    "world_is": "True as read on the deployed function.",
    "notes": "FOR THE CTO: a row-gate limb that refuses surfaced_at later than the commit time (three projects today carry future-dated or placeholder worker stamps)."
  }
]
```

-- 3.0.0_SA_CVO~Z
