# AMGT_CORPUS ROUND 15 -- L8 COMPILE + L9 ON THE ISSUER'S TWO CALLS

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~22:1xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND15_DRAIN_END_PACKET.md` @`bb54b9a183`, msg 26735. The packet was read to EOF (4,084 B).
**L7:** there were no worker orders (`fanout: 0 of 2 chains`). `CRPS-q-1` was resolved at L5 by measurement; `CRPS-q-2` is the
issuer's served act under the pair COO `ca6e2ef4f2` / CTO `411236c2b7`.

---

## 1. THE SERVED ACT (q-2), RE-READ BY THIS SEAT

- **The pool:** the S3 listing of `crosswalk/v1/` holds 6 objects. The newest is `2026-09-29.json`, written 2026-09-29T21:54:52Z,
  599,016 B.
- **Record diff:** this seat diffed the records of `2026-09-25.json` against `2026-09-29.json` itself.
  - Result: **236 -> 237, added `['6501_JP_Equity']`, removed 0, changed 0.**
  - This equals the V leg. The pair's never-widen held on the output.
- **Resolution census over the live library:** 96 folders, **96 resolved, 0 unresolved**.
  - "Hitachi 6501 JP" -> `6501_JP_Equity`, crosswalk_vintage 2026-09-29, display ticker `6501 JP`.
  - This closes the one read failure that AMGT_RESAPP ADJUDICATION_v58 measured on the same library.
- **Vendor egress:** the one Bloomberg call ran inside the scripted registration run. R-21 (`b390c36444`) records Andrew's word:
  "all the egress you want for vendors ... the pull should be deterministic/scripted in nature". It is broad on authority and
  narrow on mechanism. **A scripted, re-runnable call is within it.**

## 2. q-1, RE-READ

- `dossier.read_dossier("BP/_LN_Equity")` reads its served object:
  `.../security_key=BP-SLASH-_LN_Equity/as_of=2026-09-29.bfadf68ffd84f85c.json`.
- `dossier.read_dossier("NG/_LN_Equity")` does the same: `.../NG-SLASH-_LN_Equity/as_of=2026-09-29.c7418dc61657779e.json`.
- The read path is sound. `Z-W4-S5`'s 93 of 95 was the sweep passing partition names as keys.

## 3. L9 -- THE ISSUER'S TWO CALLS

| call | verdict | grounds |
|---|---|---|
| **The identity choice:** `6501 JP` read from the folder's own name, because no ONE PAGER exists, then measured by the call | **AGREED** | Two things settle it. The measured name "HITACHI LTD" AGREES with the folder. Hitachi, Ltd. trades on Tokyo under code 6501. The record adds only that one key and moves no other JP record (0 of 6). |
| **q-1 resolved at L5, with no build** | **AGREED** | The defect never existed in the read path (section 2). A test would pin the sweep's decoding, which is coverage and not a fix. |

## 4. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W4-S5` (the slash-key partitions raise; the sweep reads 93 of 95) | **GRADUATED** | section 2 |
| `Z-S58` (Hitachi arrived after the run; FWD-4's organic arm reads NO_EVIDENCE) | **GRADUATED** | Hitachi now resolves (section 1). The organic population is 0 of 96 today. The WILL-ADD and REFUSES-ambiguous limbs were driven on planted folders in round 14 (p-2). |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` (ARMED) | **CARRIED**, unchanged | no landed remedy, as in v16 and v17 |
| `Z-W1-S17`, `Z-W3-S8`, `Z-S59` and the other INERT notes | **CARRIED** | as in v17 |

## 5. FOR THE ROUND-15 ANALYSIS

1. **The standing mechanism the packet raises:** every library folder newer than the crosswalk gets its row when it arrives.
   Today that was a manual act, and the crosswalk had gone four days without a vintage while a folder was waiting. This is a
   producer question, not a monitor; the CTO rules on it.
2. **The six render outcomes** stay with AMGT_RESAPP. This project re-grades them on the deployed function once they land
   (round-14 ruling 7).

## 5a. L10 PRECONDITION

1. **Every task order terminal:** 0 orders cut. Both cells are closed on evidence: q-1 by measurement, and q-2 by an entry
   CLOSED 3 of 3. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** the ARMED set is CARRIED as before with no landed remedy. **MET**
3. **Every judgment item graded:** 2 of 2 AGREED. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S18",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T22:20:00Z",
    "one_line": "L8/L9 round 15: this seat's diff of crosswalk/v1 2026-09-25 -> 2026-09-29 reads 236 -> 237, added only 6501_JP_Equity, 0 removed, 0 changed; the live library resolves 96 of 96; BP/ and NG/ dossiers read through the slash-safe path; the issuer's two calls agreed; Z-W4-S5 and Z-S58 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-objects-v2 opal-data-harvest crosswalk/v1/: 6 objects, newest 2026-09-29.json 2026-09-29T21:54:52Z 599016 B.",
        "boto3 get_object of crosswalk/v1/2026-09-25.json and 2026-09-29.json: records 236 -> 237, added ['6501_JP_Equity'], removed [], changed 0.",
        "Resolution census: library.list_folders -> 96 folders, resolved 96, unresolved []; 'Hitachi 6501 JP' -> 6501_JP_Equity, crosswalk_vintage 2026-09-29, display_ticker '6501 JP'.",
        "dossier.read_dossier('BP/_LN_Equity') -> security_key=BP-SLASH-_LN_Equity/as_of=2026-09-29.bfadf68ffd84f85c.json; dossier.read_dossier('NG/_LN_Equity') -> security_key=NG-SLASH-_LN_Equity/as_of=2026-09-29.c7418dc61657779e.json.",
        "R-21 b390c36444 (1.0.0_SA_CTO~Z, recording ANDREW-DIRECT 2026-09-24): vendor egress broad on authority, narrow on mechanism -- every vendor call in a deterministic scripted producer."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W4-S5",
      "AMGT_CORPUS-Z-S58"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @bb54b9a183 asserts q-1 resolved at L5 by measurement (95 of 95 reads) and q-2's Hitachi registration landed under the pair (added 1, removed 0, changed 0; census 96 of 96 resolved).",
    "world_is": "True as read, each figure re-measured by this seat on S3 and on the live library.",
    "notes": "FOR THE ROUND-15 ANALYSIS: a crosswalk row for each new library folder as it arrives is today a manual act (a four-day gap left Hitachi unresolved); a producer question for the CTO, not a monitor."
  }
]
```
