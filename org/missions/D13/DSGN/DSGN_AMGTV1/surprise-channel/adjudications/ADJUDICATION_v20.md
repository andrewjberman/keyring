# DSGN_AMGTV1 ROUND 22 -- L8 COMPILE + L9 READ -- three faces repaired on DEV, not on PROD; FWD-8 still carries system wording

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~07:5xZ
**Input:** `2.0.0_SA_COO~D`'s `round22/ROUND22_CLOSE.md` @`863ff402ec` (4,693 B, read to EOF), msg 28292. PRD v0.8 @`7912f7aee2`
ADMITTED (this seat's sign @`e491b51258`).
**L7 re-measured (LAST `<status>` tag):** AV-z-1, AV-z-2, AV-z-4 `complete`. **0 judgment criteria.**
**Rows past the slug (REMEDIATION_v1):** `Z-W69-S1` (1 of 42).

---

## 1. RE-READ BY THIS SEAT -- PNGs of walk `tmp/ui-walk/20261002T072805Z` (portal DEV a730d8ce, LOCAL)

| face | this seat's read | FWD |
|---|---|---|
| VLO Exec (067) | "Contact enrichment was skipped for this company." The raw key and `domains.json` are gone. **Still on the face:** officer "**Senior Vice**" with an age ending every role ("... President 60"); the SEC accession "FILING 0001628280-26-011499"; and the producer phrase "a SERP not scoped to the company's own domain is not the contract's search" | 11 met on codes; 7 NOT (RESAPP B3) |
| BA Peers (025) | Subject row 196.80 / 159,623 / 187,188, equal to the header (USD 196.80, 187B). No field code. The absent-column reasons still read as system text: "no share-count **factor code** and no share-count **row field**", "the solvency category carries only **RATIOS**", "among the **289 registry factors**", "not in the **comparison map**" | 8: subject row MET; "no internal system text" NOT |
| BA Posture (052) | Reason 2 now reads "The reason for this claim is held in the record; its cites follow." The "ABSENT" token is gone, and with it the reason: the face carries a placeholder where the claim was | 11 met; 10 weaker (a reason with no text) until RESAPP B4 |

**Instrument run by this seat:** `node posture.harness.cjs` at portal a730d8ce exits rc 1 with `TypeError: (0 , useLeadPanelApi_1.useCollectedChatter) is not a function`, which confirms row `Z-W69-S1`. The harness that grades Posture grades nothing, and no bound includes it.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W69-S1` | **GRADUATED** | a stale hook stub leaves posture.harness unrunnable outside every bound. Carried as an OPEN remediation row (REMEDIATION_v1), owner `2.0.0_SA_COO~D` |
| `Z-W56-S4` (REMEDIATION_v1, was OPEN) | **REMEDIATED in place** | AV-z-4 retired or re-graded errorEmpty's starred claims; `starredclaims` 3/3 at the drain |

## 3. L10 PRECONDITION

1. Every task order terminal: 3 of 3. **MET**
2. BLOCKING or ARMED rows: none new; comp-surprise open 0, ARMED 0 before this write. **MET**
3. Judgment criteria: 0. **MET (vacuous)**

## 4. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

- **None of this is on PROD.** a730d8ce is LOCAL DEV, and PROD is still b3a1d8a6. The demo at 13:00Z (09:00 ET) shows the
  pre-round-22 faces (the Lusha key, field codes, the "--" subject row) unless Andrew gives the promote word in time.
  Rollback is b3a1d8a6.
- Two FWD-11 calls are for the CTO, not this seat:
  - Is an SEC accession number on the face an "id"? It is a public document identifier; codeface does not flag it.
  - Is "a SERP not scoped ... is not the contract's search" machine reasoning on the face? It is not a code.
- FWD-8's "shows no internal system text" stays open on the absent-column reasons. The field codes were replaced with system
  vocabulary, not with words.

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S24",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T07:51:00Z",
    "one_line": "Round 22 L8/L9: 3 of 3 complete, 0 judgment; on walk 20261002T072805Z (DEV a730d8ce, LOCAL, not PROD) the Lusha key, the Peers field codes and the '--' subject row are gone; still open: Peers absent reasons in system vocabulary (FWD-8), VLO officer 'Senior Vice' + ages (FWD-7, RESAPP B3), Posture reason 2 a placeholder (FWD-10, RESAPP B4), 24 of 94 ticker bars (FWD-2, RESAPP B1); posture.harness unrunnable (W69-S1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: AV-z-1, AV-z-2, AV-z-4 complete; 0 judgment=\"true\".",
        "tmp/ui-walk/20261002T072805Z/shots/067-VLO-US-Exec-Management.png: 'Contact enrichment was skipped for this company.'; 'Senior Vice' / 'President and Chief Financial Officer 45'; 'FILING 0001628280-26-011499'.",
        "tmp/ui-walk/20261002T072805Z/shots/025-BA-US-Peers-expanded.png: subject 196.80 / 159,623 / 187,188; 'no share-count factor code and no share-count row field', '289 registry factors', 'comparison map', 'RATIOS'.",
        "tmp/ui-walk/20261002T072805Z/shots/052-BA-US-Posture-expanded.png: reason 2 'The reason for this claim is held in the record; its cites follow.'",
        "node src/pages/SecurityAnalysis/__harness__/posture.harness.cjs at portal a730d8ce: rc 1, TypeError useCollectedChatter is not a function."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W69-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Round-21 analysis section 3A: A1 no code-shaped token on Exec/Posture/Peers, A2 the Peers subject row from the header, A4 errorEmpty starred claims.",
    "world_is": "A1, A2 and A4 are met on DEV as read; FWD-8's system wording, FWD-7, FWD-10's placeholder reason and FWD-2 stay open; nothing of round 22 is on PROD.",
    "notes": "FOR THE CTO: the PROD promote of a730d8ce is Andrew's word before 13:00Z; the accession-number and SERP-sentence calls under FWD-11; FWD-8's absent-reason wording."
  }
]
```

-- 3.0.0_SA_CVO~Z
