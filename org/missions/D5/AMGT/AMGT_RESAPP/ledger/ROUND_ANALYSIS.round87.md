# AMGT_RESAPP -- ROUND 87, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~20:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3124, `surprise-channel/adjudications/ADJUDICATION_v105.md` @862968c744 (MAY-CLOSE). Issuer packet:
`deliverables/2.0.0_SA_COO~R1/round87/DRAIN_END_PACKET.md`.

## 1. Graded

- **R2, NU's description: MET at the API.** One key; NU serves 0 description sentences. Outside that section, 0 of 98 are restated or
  glued.
- **R1, the FAILED withhold: MET on the deployed bytes, NOT EXERCISED live.**
  - The deployed `scoped_amgt.py` is byte-equal to the pin and carries the withhold (ll-3, proof VALID, 12 of 12 controls).
  - At the pin the FAILED list was empty, because ll-2 had already emptied NU, so no live FAILED description existed to withhold.
  - The bound was ruled in-round (msg 3091). An unexercised branch is not an exercised outcome, so round 88 drives it (item 1).
- **Leg p: `/9` is SERVED** (live `b7Lj1J`, 19:51:25Z). `r87_dossier` reads YES: /9 is deployed, not /8. This unblocks AMGT_CORPUS round-43
  item 1, its own read of the served /9.
- **R3, the stale-row pass: MET.** 125 of 125 open rows disposed once: CLOSED 66, DISMISSED 30, CARRIED 29, with 0 carried without an owner.
  Open remediation is now 29.
- **The one real run at close:** every arm YES, the round-84 to 86 set shows no regression, and the live hash is equal before and after.

## 2. ENRICHMENT LIST (round 88, ONE issuance by `2.0.0_SA_COO~R1`)

1. **The FAILED withhold, driven (planted arm).**
   - Run the DEPLOYED reader code (`scoped_amgt.py` at the live pin) on a COPY of the served drafting store.
   - On that copy, one name's company_description verdict is planted to FAILED.
   - Expected: that name serves 0 description sentences, `withheld_failed` is set, and the failed_on / rule detail reaches /overlay.
   - Unplanted control: the same copy's other names serve unchanged.
   - Organic negative arm: the live store, which has none.
   - Nothing is written to the served store.
2. **NU's empty-state card on the page.** The CVO carried the page wording to DSGN_AMGTV1, but DSGN_AMGTV1 is CLOSED (@78294bf9ee), so the
   wording belongs here. It is a portal DEV candidate: a withheld or empty description renders a plain empty-state line. Use one ui-walk on
   NU as the read. Any PROD promote is a separate pair.
3. **D1-S18:** the scoped watchlist route refuses an off-list selected_tenant, as the other scoped routes do.
4. **AMGT_RESAPP-S3:** `library.py` refuses a SET but nonexistent `OPAL_RESEARCH_LIBRARY_ROOT`.
5. **The 29 carried rows owned by `2.0.0_SA_COO~R1`:** each is cut as a cell or dispositioned in the issuance commit. Only a row whose act
   needs a seat becomes a cell.

## 3. ACTS ONLY ANDREW CAN DO (cited)

- FWD-16: lifting his 2026-09-15 news hold, which he set by name.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1
