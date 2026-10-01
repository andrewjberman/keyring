# AMGT_RESAPP ROUND 53 -- L8 COMPILE (no judgment criterion; ac-3 AC3's post-failure re-scope read against its controls)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~16:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round53/DRAIN_END_PACKET.md` @`9a1199bbac`, msg 27266. The packet was read to EOF (7,150 B). The CTO's
ask is msgs 27252 and 27253.
**L7 re-measured:** `ac-1`..`ac-4` read `complete` on their LAST `<status>` tag. There are 0 judgment criteria.

---

## 1. ac-3 AC3 -- RE-SCOPED AFTER IT FAILED: THIS SEAT's READ

**The deployed build.** `opal-amgt-scoped-api` returns CodeSha256 `/QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o=`, LastModified
15:22:01Z. This equals ac-3's close.

**The pre-act capture.** `0.7.0_AE_CloudOps~A/ac3-pre/bpng.json` holds 6 body hashes. The file was written at 15:12Z, before the
15:22Z build (committed at `e1367c77ba`).

**The re-run, by this seat, now:**

| run | rewrites | bodies moved of 6 | verdict |
|---|---|---|---|
| the amended check (`checks/ac_3_served.py --what bpng`) | 12 | **0** | YES |
| **this seat's negative arm:** the same script with the rewrite disabled (`if in_read` -> `if False`) | 0 | **6** (all of BP and NG: overlay, peers, thesis) | NO |

**What the 12 rewritten strings are.** This seat walked every `*_read` subtree of the six live bodies.
- **10 are `object_key` read paths:** `posture_read`, `peer_read` and `scores_read`, for example
  `posture/v1/BP-SLASH-_LN_Equity/2026-09-16.json`.
- **2 are `management_read.reason`**, naming the absent path: "no object under s3://opal-data-harvest/management/v1/BP-SLASH-_LN_Equity/".
- **None is a data value.**

**VERDICT: the re-scope is SOUND.**
- The rewrite touches exactly the strings that name the read path, which the act exists to move. It touches nothing else.
- The body comparison is a whole-body hash, so any other byte change still fails the check. The issuer's planted value outside
  `*_read` shows this (it FAILS), and so does the rejected wider rewrite (it FAILS on BP's citations).
- This seat's negative arm shows the check is not blind: without the rewrite, all 6 bodies move.
- **BP/_LN and NG/_LN read the same data at the encoded keys.**

**One boundary for the gate proposal (packet section 6 item 4):**
- This is the third check in this span whose comparand embedded the thing the act moves (after Z-S311 and FWD-30's plants).
- The check's own design was right after amendment. The defect was that it showed no positive arm BEFORE the cut.
- The proposed gate, "show the positive arm before the cut", would have caught all three.

## 2. THE REST, RE-READ OR NOTED

- **FWD-30 at close:** the `.tsv` reads TSM_US_Equity as the one NOT_OK, with 1 of 246 values differing and 0 unscaled. The close
  `.log` names no differing fact (0 "differs" lines). So the identity (HEADER `CURR_ENTP_VAL`, a page "unit not resolved --" phrase
  against an export UNRESOLVED string) is inferred from the 13:29Z run, as the packet itself says. The upstream fix is AMGT_CORPUS
  round 25 (`Z-S69`, raised at CORPUS ADJUDICATION_v27 as a served mislabel).
- **ac-2:** the HOLD is working as designed (`Z-S316`). The 8 dropped ASML sentences carry `quoted_spans []` and were served before
  the verbatim gate held. Round 54's census of non-verbatim served D-1 sentences is the right next cell.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S318` (BLOCKING: AC3 cannot pass by the specified act) | **GRADUATED** | the re-scope is sound (section 1: a 0/6 amended arm against this seat's 6/6 unamended arm; the 12 rewrites are all read paths) |
| `Z-W191-S1` (BLOCKING: ac-2's STOP on non-verbatim sentences) | **GRADUATED** | CTO msg 27185 and `Z-S316`: the HOLD is working as designed |
| `Z-S319` (ARMED: an MSYS-mangled `content-sha256`, so `source_code_hash` is corrupted at rc=0) | **CARRIED** as ARMED -> round-54 repair cell | Served output is unaffected (yang-lambda deploys the object VERSION, `Z-S321`). The interim guard is the act-start limb "head-object content-sha256 equals the local sha" on every RESAPP build pair. A corrupted hash can make a later apply read 0-diff on changed code, so it stays ARMED until the three scripts carry chatter-axis's read-back. |
| `Z-S316`, `Z-S320`, `Z-S321` | **CARRIED**, INERT | rulings and records |
| `Z-S314` | superseded by `Z-S316` | |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S318` and `Z-W191-S1` GRADUATED; `Z-S319` CARRIED as ARMED with its interim limb.
   **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S433",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T16:40:00Z",
    "one_line": "L8 round 53: ac-3 AC3's post-failure re-scope read SOUND -- amended check 0 of 6 bodies moved with 12 rewrites, this seat's no-rewrite negative arm 6 of 6 moved, and all 12 rewritten strings are *_read object_key/reason paths, never data; deployed /QP4upEV; FWD-30 95/96 with TSM's one fact inferred, not logged; Z-S318 and Z-W191-S1 graduate; Z-S319 stays ARMED to the round-54 repair.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AMGT-ac-1..ac-4 read 'complete' on their LAST <status> tag.",
        "Lambda opal-amgt-scoped-api CodeSha256 /QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o=, LastModified 2026-09-30T15:22:01Z; ac3-pre/bpng.json written 11:12 ET (15:12Z).",
        "python round53/checks/ac_3_served.py --what bpng --dir .../ac3-pre: rewrites 12, moved 0 of 6, YES; the same script with the rewrite disabled: rewrites 0, moved 6 of 6, NO.",
        "Live *_read strings containing an encoded key: 10 object_key (posture/v1, peers/v1, scores/v1 under BP-SLASH-_LN_Equity / NG-SLASH-_LN_Equity) and 2 management_read.reason; 0 others.",
        "round53/captures/fwd30_close_sweep_served_20260930T161018Z.tsv: TSM_US_Equity NOT_OK val_differ 1 of 246; .log lines containing 'differs': 0."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S318",
      "AMGT_RESAPP-Z-W191-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @9a1199bbac asserts 4/4 terminal, ac-3 AC3 re-scoped after failing (confined to *_read, planted control fails), 6/6 bodies equal, and FWD-30 95 of 96 at close.",
    "world_is": "True as re-run by this seat, with a negative arm of its own. The re-scope rewrites only read-path strings. TSM's single FWD-30 difference is not named in the close log.",
    "notes": "FOR THE ROUND-53 ANALYSIS: adopt 'show the positive arm before the cut' (third instance); Z-S319 stays ARMED until the three build scripts carry the read-back; the close sweep should log each differing fact."
  }
]
```
