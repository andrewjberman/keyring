# AMGT_CORPUS ROUND 14 -- L8 COMPILE (no judgment criterion on the orders)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~21:4xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND14_DRAIN_END_PACKET.md` @`e7b3f1f975`, msg 26712. The packet was read to EOF (8,921 B).
**L7 re-measured, not adopted:** `p-1`..`p-5` all read `complete` on their LAST `<status>` tag. 0 judgment criteria.
The issuer names three calls of its own (packet section 6); they are weighed in section 3.

---

## 1. THE SERVED ACT (p-5), RE-READ ON THE STORE

- **The store, read by this seat through the project's own reader** (`dossier.read_dossier("ML_FP_Equity")`):
  - URI `s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=ML_FP_Equity/as_of=2026-09-29.d667004f7e2ea259.json`,
    which is the canonical prefix;
  - `thesis_pillars` holds **5** entries, each with keys `citation`, `pillar`, `terms` and `text`;
  - the bodies are **197, 226, 141, 165 and 215 characters**: "Irreplaceable brand and pricing power", "Mix shift to premium",
    "FCF Generation", "Beyond tires", "EV-agnostic positioning";
  - this matches the issuer's V leg (`evidence/r14_after.txt`: 320 continuation objects and 190 dossier objects, each over 95
    partitions; field diff over 95 of 95, `thesis_pillars` changed on ML_FP_Equity only).
- **The data half is served.** `Z-W1-S16` (ML_FP's empty pillar) and `Z-W5-S5` (ARMED: the first pass served ML_FP ABSENT)
  are resolved in the store.

## 2. THE RENDER HALF, RE-READ ON THE DEPLOYED FUNCTION

This seat made one read-only invocation of `/api/scoped/amgt/security/ML_FP_Equity/thesis` through AMGT_RESAPP's capture
library:
- CodeSha256 `lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=`;
- HTTP 200, 530,489 B;
- **0 of 5 pillar leads** anywhere in the payload.

That equals p-4's row and the issuer's real run. **The six render-owned outcomes (FWD-10, 11, 12, 15, 16, 18) stay unmet, and
their owner is AMGT_RESAPP.** This project's half is done; the page cannot show what `/thesis` does not pass.

## 3. THE ISSUER'S THREE CALLS

| call | this seat's read | verdict |
|---|---|---|
| **p-1 AC2 accepted with `temp_new_entries 1`, attributed to a sibling on unfixed code** | The entry `amgt_corpus_census_ni2_stj4` has mtime **2026-09-29T19:17:45Z**, before p-1's fix drained at 19:22:30Z. At 19:17:45Z the sibling `wk-crps14-5r` sat at `7853b637d4`, whose `readonly_proof.py` has **no `rmtree` call**. The fix `83ca76edc8` adds the first, `shutil.rmtree(scratch)`. ⚠ A first read by this seat counted "3 rmtree" in that file and briefly doubted the packet. Those 3 are the analyzer's own vocabulary (`SHUTIL_MUTATORS` and the write-target parser), not calls. The packet's "0 rmtree calls" is right. | **AGREED.** The system temp dir now holds 98 `amgt_corpus*` entries, all from pre-fix runs, for operator cleanup. |
| **p-4: FWD-12 unmet although team_cases are served 33 of 33** | The FWD-12 clause includes the render, and portal DEV renders the Base case only | **AGREED.** A served payload the page does not show is not the outcome. |
| **p-5: a lead's trailing period stripped (`Z-W5-S6`)** | The served leads read as headings (above). This matches the colon precedent the issuer cites. | **AGREED**, no change |

## 4. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S16` (ML_FP's one pillar has an empty paragraph) | **GRADUATED** | section 1: 5 of 5 bodies non-empty on the served object |
| `Z-W5-S5` (ARMED: the first pass served ML_FP ABSENT) and its disarm `Z-S60` | **GRADUATED** | section 1 |
| `Z-W1-S17` (the temp census counts a shared dir; siblings bleed into it) | **CARRIED** -> analysis | the source stops once every worktree holds `975dbcd17f`; the 98 legacy entries are operator cleanup |
| `Z-W3-S8` (FWD-17's drive stubbed typed `--write` and the dossier clock) | **CARRIED** -> analysis | whether the CLI limb needs its own exercise |
| `Z-W4-S5` (`BP/` and `NG/` partitions raise SlashSafeKeyError; the sweep reads 93 of 95) | **CARRIED** -> analysis | a key-encoding repair cell, or accepted |
| `Z-S59` (`safe-merge --continue` committed 6 foreign paths) | **CARRIED** -> the tool's owner | Confirmed by this seat. Merge `34bbf74213` carries six 4.0.0_SA_CRO~Z files under `AMGT_RECONN_SOURCES_20260929/` (the ANDREW_DIRECT, BBG_EXCEL_ACCESS_VERIFIED, BBG_GUIDES_FOLLOWUP and README records, and `scripts/bbg_excel_holdings_probe.py` + `bbg_excel_probe_queries.json`) under 2.0.0_SA_COO~X's author line. The content is intact and the authorship is wrong. Same class as AMGT_HARVST `Z-S37`. |
| `Z-W5-S4`, `Z-W5-S6` | **CARRIED** as INERT notes | ruled in the pair / agreed above |
| `Z-S58` (Hitachi's organic arm NO_EVIDENCE) | **CARRIED** -> analysis | Hitachi 6501 JP has no crosswalk row (newest vintage 2026-09-25; AMGT_RESAPP ADJUDICATION_v58). p-2 observed the WILL-ADD and REFUSES-ambiguous limbs on planted folders. |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` (ARMED) | **CARRIED**, unchanged | no landed remedy, as in v16 |

`_latest_dispositions('.', 'AMGT_CORPUS')` before this row returned **108 items: 67 GRADUATED, 41 UNDER_INVESTIGATION**, read
from 18 files, with 0 unknown `adjudicates` targets.

## 5. L10 PRECONDITION

1. **Every task order terminal:** 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W5-S5` GRADUATED on this seat's store read; `Z-W2-S11`, `Z-S3` and
   `Z-S6`..`Z-S9` CARRIED as in v16 with no landed remedy. **MET**
3. **Every judgment criterion graded:** 0 on the orders; the issuer's three calls were weighed and agreed. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S17",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T21:45:00Z",
    "one_line": "L8 round 14: the served ML_FP dossier on the canonical prefix carries 5 pillars with bodies of 141-226 chars (Z-W1-S16, Z-W5-S5 graduate); the deployed /thesis (lg6NJ2JL...) returns 0 of 5 pillar leads, so the six render outcomes stay AMGT_RESAPP's; the issuer's three calls agreed; Z-S59 confirmed (6 CRO~Z paths under COO~X's merge).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-p-1..p-5 read 'complete' on their LAST <status> tag.",
        "dossier.read_dossier('ML_FP_Equity') -> uri s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=ML_FP_Equity/as_of=2026-09-29.d667004f7e2ea259.json; thesis_pillars 5, keys [citation, pillar, terms, text], text lengths 197/226/141/165/215.",
        "Deployed /api/scoped/amgt/security/ML_FP_Equity/thesis via AMGT_RESAPP capture_lib: CodeSha256 lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=, status 200, 530489 B, pillar leads present 0 of 5.",
        "p-1 temp entry: %LOCALAPPDATA%/Temp/amgt_corpus_census_ni2_stj4 mtime 2026-09-29 15:17:45 -0400 (19:17:45Z); wk-crps14-5r at that time = 7853b637d4, readonly_proof.py with no shutil.rmtree call (its 3 'rmtree' strings are SHUTIL_MUTATORS and the write-target parser); fix 83ca76edc8 adds 'shutil.rmtree(scratch)'; 98 amgt_corpus* entries in system temp.",
        "git show --stat 34bbf74213: 6 files under org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/ in a 2.0.0_SA_COO~X merge.",
        "L8: _latest_dispositions('.', 'AMGT_CORPUS') 108 items, 67 GRADUATED, 41 UNDER_INVESTIGATION, 18 files."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S16",
      "AMGT_CORPUS-Z-W5-S5",
      "AMGT_CORPUS-Z-S60"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @e7b3f1f975 asserts 5 of 5 orders VALID and merged, the p-5 served act landed 4 of 4 with ML_FP serving 5 pillars, and 6 render outcomes unmet on the deployed /thesis, owner AMGT_RESAPP.",
    "world_is": "True as read. The store half is served and measured by this seat on the object; the render half is not, measured by this seat on the deployed function. The packet's '0 rmtree calls' was briefly doubted on a string count and is right on the code.",
    "notes": "FOR THE ROUND-14 ANALYSIS: (1) the six render acts are AMGT_RESAPP's -- one served-reader change passing pillars, management, posture, model rows and terms through /thesis, plus the portal render; (2) Hitachi 6501 JP's crosswalk row (shared with AMGT_RESAPP); (3) Z-W4-S5 slash-key read path; (4) Z-W3-S8 typed --write limb; (5) Z-S59 routes to safe-merge.sh's owner, the same class as AMGT_HARVST Z-S37; (6) 98 amgt_corpus* temp entries and the crash-damaged wk-crps14-5 await Andrew's word."
  }
]
```
