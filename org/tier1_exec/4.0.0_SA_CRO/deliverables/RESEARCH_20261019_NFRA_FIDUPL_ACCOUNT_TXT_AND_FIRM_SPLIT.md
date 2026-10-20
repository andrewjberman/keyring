# RESEARCH 2026-10-19 -- NFRA_FIDUPL: account.txt has no firm key; a split by crosswalk covers 1,418 of 5,007 accounts

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1) | **Feeds:** FWD-9 (each firm's files in its own place) and C-TENANCY. Follows
`RESEARCH_20261019_NFRA_FIDUPL_G_NUMBERS.md`.
**Input:** `account.txt`, the Accounts file of Andrew's v1.0.1 custom export: 5,007 rows, 141 columns, quoted CSV, no header row. It is
held on dell1 and not committed. Counts and column positions only; no account numbers, names or values.

## 1. account.txt carries no firm identifier (measured)

- **G number:** 0 cells across all 141 columns equal any of the login's 31 G numbers, with or without the leading `G`.
- **Low-cardinality code columns** (40 or fewer distinct values, at least half filled) are the only place a firm, rep or branch code could
  hide. All are account attributes:

  | Column | Holds | Distinct values |
  |---|---|---|
  | c2 | source/type | `B` / `P` / `I` / `F` |
  | c3 | cost-basis method | STTS / FIFO / ... |
  | c27 | an account class | 4 |
  | c29-c33 | core money-market sweep | FDRXX / FCASH / SPAXX / QIWSQ |
  | c50 | a 1-character code | 6 |
  | c92 | `000` / CGF / FAC | 3 |
  | c94 | a 1-character code | 3 |
  | c95 | registration type | 25, e.g. Traditional IRA, Roth IRA |
  | c96 | a 1-character code | 5 |
  | various | Y/N flags | 2 |

  None splits by firm.
- **Medium-cardinality short codes:**
  - c65 is a date (2021-04-02 to 2026-10-16);
  - c107 is a 2-letter state;
  - c85 is a 1 to 5 letter code (214 values, 43% filled);
  - c133 and c138 are decimal rates.

  None is a firm or rep key.
- c1 is the Fidelity account number: 5,007 of 5,007 match `FI101626.naa`.
- **Conclusion:** neither the standard nor the custom export lets the book be split by a field in the file.

## 2. Split by crosswalk against the per-firm sources Opal already holds (measured)

Account numbers were normalised to `[A-Z0-9]` and joined to `account.txt` c1:

| Firm | Source | Claims (of 5,007) |
|---|---|---|
| inflection | Orion `s3://opal-data-assets/orion/inflection/silver/fact_assets/date=2026-10-19/` (custodian Fidelity_Inflection / Fidelity_LH; accountNumber + secondaryAccountNumber) | **779** |
| cottonwood | Black Diamond `.../blackdiamond/cottonwood/silver/fact_allocations/date=2026-10-16/` (Custodian = Fidelity IWS) | **639** |
| 49financial | Black Diamond `.../blackdiamond/49f/silver/fact_bd_allocation/date=2026-08-18/` (newest partition; account_number + original_account_number) | **0** |
| **claimed by exactly one firm** | | **1,418** |
| claimed by more than one firm | | **0** |
| **unclaimed** | | **3,589** |

- **Orion Inflection Fidelity accounts missing from the Alongside file:** 201 of 980. The reason is unmeasured: closed accounts, or G
  numbers outside this login.
- **The 3,589 unclaimed** include every account of the 17 non-registry G numbers (Keil, Abiding, Lighthouse, VM, one advisor). They also
  include 49 Financial's Fidelity accounts, if it has any: its one G number is in the login, but Black Diamond's 49F data holds none of
  these account numbers.

## 2a. Addendum (~20:05Z): the G-number switch exists (Andrew's screenshots, 2026-10-19 16:01-16:02 ET)

These are read from three screenshots Andrew took. No traffic has been captured yet.
- **Where:** User Options (header), then User Menu, then AUTHENTICATION & SECURITY SETTINGS, then **"G Number Selection"**. Andrew reports
  that the page sits under the channel's `/app/service/user` path.
- **What the page holds:** `Current: <G> - ALONGSIDE, LLC`, `Default: <G> - ALONGSIDE, LLC`, a `G Number List` dropdown, and a
  `Set As Default` checkbox. The page text reads: "Only those G Numbers to which your ID has access will be listed".
- The dropdown lists the same 31 G numbers and labels as `criteria-fields.json`, in the same order (section 1 of the G-number research).
- **Implication (inferred):** the session's CURRENT G number can be changed without changing the default. If `accountList.json` returns
  only the current G's accounts, then 31 switches and 31 list calls a day give a complete account-to-G-to-firm map. The one Alongside
  export can then be split on it, with no extra exports. **Not yet measured:** the switch endpoint and its parameters, and whether
  `accountList.json` actually narrows after a switch.

## 2b. Addendum (2026-10-20 ~14:35Z): the G-number switch, MEASURED from Andrew's HAR 4

**Source:** `wealthcentral.advisorchannel.com4.har` on dell1 (off git), recorded 2026-10-20 14:26:36Z to 14:28:00Z. It has 115 entries
and contains 13 switches: Inflection's 5, Cottonwood's 7 and 49 Financial's 1. G numbers are shown hashed or masked.

**The mechanism is a legacy server-rendered JSP form, not an API:**

1. **Open the form:** GET `https://wealthcentral.advisorchannel.com/ac/wc/channel/jsp/support/ria_changegnum.jsp` returns 302 to GET
   `https://www2.advisorchannel.com/wc/channel/jsp/support/ria_changegnum.jsp` (200, about 6.6 KB HTML). It sends the session cookies
   only: no `x-xsrf-token` and no hidden CSRF field.
2. **The form**, `name="pgChangeGN"`, posts to `action="ria_changegnum.jsp"`:
   - `select name="gnumClientNm"`: 31 options, each `value="G" + 8 digits`;
   - `input name="isDefault" value="Y"`: the "Set As Default" checkbox;
   - `input value="Apply"`: the submit button;
   - `input type="hidden" name="process" value="change"`;
   - `input type="button" value="Cancel" onclick="cancelWC()"`.

   The page renders `Current: <G> - <label>` and `Default: <G> - <label>` in table cells.
3. **Switch:** POST `https://www2.advisorchannel.com/wc/channel/jsp/support/ria_changegnum.jsp`, content type
   `application/x-www-form-urlencoded`, body `gnumClientNm=<G>&process=change`. **Leave `isDefault` out to change only the current
   G.** It responds 200 with the same page (about 7.1 KB) and sets the cookies `ATC`, `ATCTO`, `bm_sv`, `zpc`, so the session token
   is re-issued on each switch.

**Verified per switch (13 of 13):**
- The response's `Current:` equals the requested G.
- `Default:` stays the ALONGSIDE G every time. No request carried `isDefault`.
- The switches ran 4 to 9 s apart, by a person.

**Not measured in this HAR (owed by the live cell):**
- **Whether `accountList.json` narrows after a switch.** The capture holds no account-list call after any switch.
- Whether the `wealthcentral` SSC APIs follow the re-issued `ATC`.
- Whether the scheduled export, which runs under the default, is unaffected. It should be, since the default never changed.

**State left behind:** the capture ends with the session's CURRENT G set to 49 FINANCIAL's G (its last POST, 14:27:53Z). The default is
unchanged, so the next sign-in starts on ALONGSIDE. The uploader should switch back to the ALONGSIDE G at the end of every per-G sweep,
so the session ends where it started.

**Uploader recipe (inferred from the above; the live cell proves it):** inside the signed-in Playwright session, for each G in the run-time
list (SSM SecureString, CTO msg 8638):
1. POST `ria_changegnum.jsp` with `gnumClientNm=<G>&process=change`.
2. Assert that the response's `Current:` cell equals `<G>`.
3. Call `accountList.json` (POST, form `length=2000&accountNumber=&sourceCode=BROK&custodianCode=FID`, header `x-xsrf-token`).
   Page through it and record the account-to-G map.
4. After the last G, switch back to ALONGSIDE and assert it.

## 3. What would attribute the rest (unmeasured; for the CTO, with Andrew's hands where noted)

- **Per-G account lists from Wealthscape.** The login has a `defaultGNumber`, which implies a current-G-number context. If the UI lets
  the user switch the active G number, then `accountList.json` (paged at 2,000) under each G number returns that G's accounts. That is
  about 31 small calls a day inside the session the uploader already holds, and it attributes every account directly. **Andrew's check:**
  is there a G number / firm selector in the Wealthscape header, profile or account search?
- **Per-firm export filter:** Andrew recalls none. He will re-check.
- **The crosswalk in section 2** works today for Inflection and Cottonwood (1,418 accounts, 0 conflicts). It can serve as round 1's split,
  with the unclaimed 3,589 listed rather than dropped, which FWD-9 explicitly allows: "with any accounts no firm claims listed".
