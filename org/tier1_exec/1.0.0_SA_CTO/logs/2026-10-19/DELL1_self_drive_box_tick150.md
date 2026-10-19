# /self-drive dell1 box -- ticks 149-150 (`1.0.0_SA_CTO~DELL1`, 2026-10-19 17:18Z-18:18Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec.
Covers everything since the tick-148 log (@b1884bf8bb). **state: ARMED.**

## Inbox (0.8)

0 unread at 18:18Z. Read and acked: 8396, 8398, 8409, 8410, 8412, 8415, 8417, 8418, 8423, 8428.

## Acts

| project | act | hash |
|---|---|---|
| NFRA_FIDUPL (**new; Andrew: "the highest priority project on this box"**, ~18:05Z) | **L2:** endpoint FWD-1..8 from CRO~FIDELITY's brief. The thread is FWD-1: the Fidelity book landed each morning with no human sign-in. **L3:** registered under D8, macro NFRA, sibling of NFRA_AWSFTP, placement DELL1; index derived, check 0 violations. **L4:** PRD v0.1 DRAFT with 12 contracts: TOU gate, builder names, tenancy, fresh sign-in plus Quo OTP, two-call pull, raw landing, content business date, run record, Schwab window, Schwab isolation, one TF root, backfill. Forks (a)-(d) are at CRO~FIDELITY: browser vs HTTP sign-in, box reuse, credential home, tenancy. **COO lane 2.0.0_SA_COO~P1** seated by MSTR. Two acts added for Andrew | 24f0400d63, 3324161d52, 503421257d |
| COT carrier | **Amendment 1, carry-forward**, replacing the wait on Andrew's addendum 1 ("the t+2 aspect for insurance does not need to be separately labeled"). CTO half SIGNED after reading the gates and fail-open paths at e7d897445f. **Landed and verified by me:** the opal-data-cot ingest is f950cec3, equal to e7d897445f's file; opal-data-bd is c8764a43, unchanged. MDPF restatement is Andrew's open question 2 | b3e0434658 |
| seats | W1, R1, M1 and S1 exited on their own; all four ended within 12 s at 16:57Z. On my word, W1, R1 and M1 were respawned at 17:45Z after clean checks; S1 stays down. Row NFRA_CTLPLN-D1-S21 filed by MSTR, cause not claimed | msgs 8411/8417 |
| gateway | live moved to 6d1b5dcb64 (site Z OG-ap-50); no act | msg 8396 |

## Open calls (Step 1)

4 open, all acts only Andrew can do: 0cf5, 89c9, e141 and c3a6.

## ACTS ONLY ANDREW CAN DO

- **e141 (new):** confirm NFRA_FIDUPL's 8 DONE WHEN lines. Citation: L2, rule 27.
- **c3a6 (new):** his word on the Wealthscape Terms of Use for automated access before any automated sign-in. Citation: the brief marks
  it his call.
- **0cf5:** confirm ADVI_COTBOOKS's 6 DONE WHEN lines. Citation: L2, rule 27.
- **89c9:** the SOC2_MSLOGS round-2 re-derive. Citation: it needs his MFA session.
- **The SECCLASS partners-data repoint apply.** Citation: client-facing.
- **FWD-10 client-facing PROD push.** Citation: the portal PROD rule.

## Compiler Tools

`missions-tree-index.py derive --write` and `check`, with 0 violations. Other measurements: S3 gets and sha256 of the COT and BD ingest
objects, and the e7d897445f gates read.

-- 1.0.0_SA_CTO~DELL1
