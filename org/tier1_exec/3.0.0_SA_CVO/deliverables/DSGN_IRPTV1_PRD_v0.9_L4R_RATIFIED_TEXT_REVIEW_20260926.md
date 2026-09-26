# L4-R review -- DSGN_IRPTV1 PRD v0.9, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`a7f4039787` (v0.9). **Half:** ratified-text,
`half_hash` `fd1beac474bd`, ENDPOINT hash `037ce301186c`, both re-measured with `prd_signoff_lib` at the pin and
matching delivery 101285. **Prior:** SIGNED at v0.8 @`0fe69145c8`. **Delta:** the ENDPOINT adds FWD-19, and FWD-1 to
FWD-18 are byte-unchanged. **Source read:** Andrew-direct record @`07c4b8b84e`, both verbatim passages and C1-C4.

**Verdict: REFUSE.** FWD-19 is correctly sourced. But Andrew's word that FWD-19 carries makes the unchanged FWD-5
wrong in part: two clauses, taken together, cannot both pass at the close. The fix is small.

## R1 -- FWD-5 still promises a client-level return (BLOCKING)

- FWD-5, PRD :80-88:
  - title: "An advisor reads a client's performance the way they read a model's";
  - DONE WHEN: "reads a real client's return, spread and the lagging account in one screen";
  - ACCEPT: "an accounts table with one row per account by name and masked tail, an uncovered account shown as a row
    with its reason".
- FWD-19, PRD :205-211: Performance "never shows a return for the whole client".
- Andrew, record @`07c4b8b84e` C3: "Performance is computed and shown per ACCOUNT ... A Performance request never
  carries a client- or relationship-level selection". The verbatim: "Performance is always going to be
  account-level, not client level".
- ROUTE STRUCTURE Call 3, PRD :299: the list of every account's figure is PARKED.

Consequences:
- "A real client's return" is now forbidden outright.
- "The lagging account in one screen" and "an uncovered account shown as a row" both need every account's figure on
  one screen, which is the parked Call 3 list.
- A one-account report has one row, so FWD-5's multi-row accounts table cannot fill.

As written, FWD-5 can never grade REALIZED once C25 lands.

Per `/endpoint` step F0, an outcome shown wrong is amended in place, id unchanged. The PRD says "FWD-1..18 are
unchanged". **Two fixes; the choice is the CTO's:**
- **(a) Amend FWD-5 to account level.**
  - Title: "An advisor reads an account's performance the way they read a model's".
  - DONE WHEN: "reads each of a real client's accounts -- its return and spread -- and finds the lagging one by
    switching, on one tab, instead of opening Black Diamond or SmartX".
  - ACCEPT: the accounts table becomes "the account chooser lists the client's accounts by name and masked tail; an
    account that cannot be computed says so in plain words".
- **(b) Un-park Call 3** (Andrew may, per :299). Then "the lagging account in one screen" and the uncovered-account
  row stand, and only "a real client's return" becomes "each account's return".

## R2 -- a seat serial inside the ENDPOINT section (same bump)

FWD-19's SOURCE names "the route proposal of `4.0.0_SA_CRO`", and the ENDPOINT section also carries a record path
under `1.0.0_SA_CTO/`. At v0.8 the section held no serial. This is a census over the section at both pins, using the
serial pattern. The spine's L4-R clause bars a seat name inside the section. **Fix:** cite both by pin (record
@`07c4b8b84e`, route proposal @`889160ce2c`) without the seat attribution.

## R3 -- one FWD-19 clause has an uncited source (same bump)

FWD-19 ACCEPT "opens on the client's largest account with the others one click away" is the CTO's Call 1 ruling (b)
(@`ce6aa15a17`, PRD :293). It is not in Andrew's C1-C4 or the verbatim. The SOURCE line cites only the record and the
proposal. **Fix:** add the Call 1 ruling to FWD-19's SOURCE.

## Checked and clean (not re-opened by the bump)

- **FWD-19's other ACCEPT clauses carry C1-C4.**
  - Clients only in search and header: C1.
  - The accounts listed inside the client: C2.
  - Performance says whose figure it is and never shows a client return: C3.
  - Switching changes neither the client nor the holdings total: the proposal's tab-local focus.
- **The DONE WHEN is an EXERCISED act a seat can take**: a real multi-account client, read one account, switch.
- **Ids:** FWD-1 to FWD-19, no gap and no reuse; the header `endpoint_outcomes` matches. CONTRACTS is byte-unchanged
  since v0.8.
- **FWD-1 (observation, not blocking).** "picks Anna Thiessen's Cottonwood brokerage account" reads naturally as
  choosing the client and then focusing the account, and "her year-to-date return" as that account's. Its ACCEPT is
  reconcilable with FWD-19. THE THREAD hop 3 ("the account found and chosen" in the one search box) is brief-half
  text that C25 changes; aligning its wording at the next bump is advised.
- **FWD-2 and FWD-6** agree with FWD-19: the header picks only the client, and Holdings is the client aggregate with
  in-view account narrowing.

## Instruments

| question | instrument | result |
|---|---|---|
| half and ENDPOINT hash | `prd_signoff_lib` on `git show a7f4039787:<prd>` | `fd1beac474bd`, `037ce301186c`; match the delivery |
| what changed in the ENDPOINT | `git diff 31a61d0466 a7f4039787` on the PRD | FWD-19 added (:205-214); FWD-1..18 unchanged |
| Andrew's words | the record @`07c4b8b84e`, read in full | C1-C4 and both verbatim passages quoted above |
| cited clauses | `git show a7f4039787:<prd>` printed at :80-88, :205-214, :293, :299 | quoted above as printed |
| seat serials in the section | regex census of the ENDPOINT slice at both pins | v0.8: none; v0.9: `1.0.0_SA_CTO`, `4.0.0_SA_CRO` |

-- `3.0.0_SA_CVO`, 2026-09-26 ~16:0xZ
