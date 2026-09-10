# AMGT_RESAPP -- ENDPOINT (step 2, `/endpoint --forward`)

**archetype:** SCRIBE (spec) · **author** `1.0.0_SA_CTO~Z` (L2) · **2026-09-10 ~17:3xZ`**

| | |
|---|---|
| **Source brief** | `docs/briefs/amgt-resapp-security-analysis-20260910.md` @`19ce7d5b4d` (v2), 22,244 bytes, `4.0.0_SA_CRO~Z` |
| **Directive** | D5 Alternative Research (placement SITEZ) |
| **Project** | `AMGT_RESAPP` |
| **Status** | ⛔ **NOT YET LANDED IN A PRD.** No PRD exists. Macro named by Andrew (`AMGT`); the Rule 24 record is owed. See section 3. |

> **THIS IS A CARRIER, NOT THE HOME.** Section 2 below is the block that goes into the PRD verbatim
> under the section title `ENDPOINT (step 2, /endpoint --forward)` the moment a PRD exists. It is
> written here rather than left in a terminal because an endpoint that lives only in a session is
> the carrier problem step 2 exists to close.

---

## 1. THE VERSION HAZARD, RESOLVED BEFORE READING

`4.0.0_SA_CRO~Z` flagged that the brief exists in two states. Verified here rather than taken on
report, with a positive control:

| | |
|---|---|
| v1 @`046337e2df` | **IS** an ancestor of `origin/SITEZ` — 15,429 bytes |
| v2 @`19ce7d5b4d` | **NOT** on origin, working tree only — 22,244 bytes |

Content check, one variable apart: `O10`/`O11`/`O12`/`F12`/`F13`/`StockTwits` appear **0 times in
v1** and **4/2/3/2/1/1 times in v2**. **An endpoint cut from origin would have silently dropped the
entire validation territory and the whole social limb, and would have looked complete.** Read from
the working tree.

⚠ One check of mine returned a false negative and is recorded so it is not repeated: a literal
search for `PART III-B` returns **0 in both versions**. The section exists as `## III-B -- WHAT
QUALIFIES` at brief line 131, under `# PART III`. The zero was my string, not the section.

---

## 2. THE BLOCK -- paste into the PRD verbatim

```
ENDPOINT (step 2, /endpoint --forward)

  FWD-1  An analyst gets a first-draft pack for a covered name without opening
         a spreadsheet or a data terminal
         DONE WHEN  EXERCISED -- an analyst has actually done it, not merely could
         ACCEPT     An analyst opens a company the firm already covers and the
                    model numbers, the business description and the segment
                    breakdown are already on screen. They did not open a
                    spreadsheet or a data terminal to get them.
         SOURCE     brief O1; III-B bar 1

  FWD-2  An analyst gets the same pack for a company the firm has never covered,
         by typing its ticker
         DONE WHEN  EXERCISED -- a real uncovered name has been pulled and read
         ACCEPT     An analyst types the ticker of a company the firm has never
                    covered and gets the same assembled page -- and the page says
                    plainly that it is being fetched now rather than shown from
                    an earlier save.
         SOURCE     brief O2

  FWD-3  An analyst can defend every number on the page in a meeting
         DONE WHEN  EXERCISED -- a figure has actually been challenged and
                    answered from the page
         ACCEPT     Someone asks where a figure came from, on what basis, and as
                    of when. The analyst answers by pointing at the screen --
                    not from a spreadsheet and not from memory.
         SOURCE     brief O3; III-B bar 2; F3 (state the basis beside the number)

  FWD-4  An analyst reads what has recently been said about the company without
         leaving the page
         DONE WHEN  EXERCISED -- an analyst has read one and followed it out
         ACCEPT     Recent commentary about the company is on the same page --
                    news, analyst writing, and mentions from the company's own
                    investor channel -- ordered by how recent and how often it
                    came up, each item clickable through to the original.
         SOURCE     brief O4

  FWD-5  Adam forwards a printed pack without reformatting it
         DONE WHEN  EXERCISED -- Adam has actually forwarded one
         ACCEPT     Adam prints a pack and sends it on unchanged. It replaces the
                    document he circulates today, rather than looking like a
                    screenshot of a dashboard.
         SOURCE     brief O5; III-B bar 3 (the displacement test)

  FWD-6  An analyst returning to a company can say what changed
         DONE WHEN  EXERCISED -- someone has actually compared two versions
         ACCEPT     An analyst returns to a company researched before and can say
                    what moved, naming the earlier version that shows it.
                    Refreshing adds a version; it does not overwrite the old one.
         SOURCE     brief O6; III-B bar 5

  FWD-7  Adam can see which covered companies have gone stale
         DONE WHEN  EXERCISED -- Adam has used it to find a stale name
         ACCEPT     Adam looks in one place, sees every company the team covers
                    with the date its research was last refreshed, and finds one
                    that has gone stale without opening any folders.
         SOURCE     brief O7

  FWD-8  The comparison block is about the company on the page
         DONE WHEN  EXERCISED -- an analyst who distrusted it has stopped
         ACCEPT     The list of comparable companies is genuinely about the
                    company being shown. Where a sensible comparison cannot be
                    worked out, the page says so rather than showing another
                    company's list.
         SOURCE     brief O8; III-B bar 4; F6 (48 of 54 measured wrong today)

  FWD-9  Machine-written prose is never mistaken for a firm view
         DONE WHEN  APPLIED -- the marking is in place and sits beside the
                    evidence the sentence was drawn from
         ACCEPT     An analyst can tell at a glance which sentences a machine
                    wrote and which the firm owns, and the machine-written ones
                    sit next to the evidence behind them. They are a starting
                    point someone edits, not a finished claim.
         SOURCE     brief O9; III-B bar 6

  FWD-10 A figure that failed its check is visible as failed
         DONE WHEN  EXERCISED -- a check has actually refused something and the
                    refusal was seen on the page
         ACCEPT     A figure that failed or skipped its check looks different
                    from one that passed, and the analyst can tell which. A
                    failure shows as a marked value -- never as a blank, a zero,
                    or a row that quietly disappeared.
         SOURCE     brief O10; III-B ("a check that cannot FAIL is not a check")

  FWD-11 An analyst sees social discussion admitted by a written rule
         DONE WHEN  EXERCISED -- an analyst has read the feed and can point at
                    why an item was admitted
         ACCEPT     Recent social discussion about the company is on the page --
                    its own official accounts and the wider conversation -- and
                    each item is there because it met a written rule the analyst
                    can read, not because it contained the ticker letters.
         SOURCE     brief O11; F12 (the surface is reachable); F13 (the
                    cashtag-native venue is absent, so the feed's own limits
                    are part of what the rule must state)

  FWD-12 An analyst can see where each input came from and re-run any one alone
         DONE WHEN  EXERCISED -- one input has actually been re-run by itself
                    while the others stayed where they were
         ACCEPT     For each kind of input -- market data, filings, news, social,
                    web -- the page shows where it came from, when it last ran,
                    and whether that run worked; and any one can be re-run on its
                    own. A single button that refreshes everything under one
                    timestamp does not count.
         SOURCE     brief O12

  FWD-13 Everything on one page is about the same company
         DONE WHEN  EXERCISED -- checked on a name that more than one business
                    uses, and found not mixed
         ACCEPT     The numbers, the recent commentary, the comparison list and
                    the social posts on a page are all about the same company.
                    Where the page cannot confirm that two sources describe the
                    same company, it says so rather than showing them together.
         SOURCE     brief III-B ("An identity" as its own class); PART V (the
                    ticker, the symbol and the investor-page identity are three
                    different keys; the social layer has no shared identifier);
                    F6 (the measured instance of exactly this failure)

  FWD-14 The lists the page depends on do not rot in silence
         DONE WHEN  EXERCISED -- a list has actually gone out of date and
                    somebody was told by the system rather than by a wrong page
         ACCEPT     The list of publishers the page will quote, and the map of
                    companies to their official social accounts, each have a
                    named person responsible; and when one goes out of date
                    somebody is told.
         SOURCE     brief PART V ("an enumerated list with no owner lapses
                    silently ... the same failure that left two keys dead")
```

---

## 3. WHERE THIS LANDS -- THE MACRO IS NAMED, THE RECORD IS NOT WRITTEN

> ⭐ **ANDREW-DIRECT 2026-09-10 ~17:4xZ AT THIS TERMINAL, VERBATIM: *"AMGT is a new macro, short
> for 'Asset Management'"* and *"can get that registered."*** The value is his and it is settled;
> what remains is the FORM the register demands, not the decision.
>
> Checked here against the register's own grammar, with negative controls: `AMGT` matches
> `^[A-Z]{4}$` (`AMG` and `amgt` both refused), and `AMGT_RESAPP` carries `AMGT` as its prefix, so
> the macro-equals-prefix convention every existing census line asserts holds on the first member.
>
> **THE LANDING SHAPE IS THEREFORE THE TREE PATH:**
> `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`

⛔ **WHAT IS STILL MISSING IS A RULE-24 RECORD, AND IT IS NOT THIS SEAT'S TO WRITE.**

`AMGT_RESAPP` appears on the D5 directive row as its first project, carrying `"no-json"` -- so no
project register file exists. **And D5 has NO RATIFIED MACRO ENUM.** Measured with a positive
control: `org/missions/MACROS.yaml` carries macro enums for **D0, D8, D11, D12 only**; `D5` is
absent, and a project may not register under a macro the directive's enum does not list.

`org/missions/MACROS.yaml` is DATA, not prose -- `.tools/missions-tree-index.py` reads it and refuses
(R2) a project registering under a macro its directive's enum does not list. Measured with a positive
control: enums exist for **D0, D8, D11, D12 only**; `D5` is absent. The file's own rules:

| act | owner | state |
|---|---|---|
| author the D5 enum `[AMGT]` **with its Rule 24 four-postulate record and word-boundary token census** | `2.0.0_SA_COO` -- *"a bare edit is not a proposal"* | **OWED** |
| flip `ratification` to RATIFIED, quoting the record carrying Andrew's word | **Andrew only** -- nobody else flips it | his word is GIVEN; the record to quote does not exist yet |
| apply the register act (D5 LAPTOP -> SITEZ, mint `AMGT_RESAPP`) | `0.0.0_AB_MSTR~Z` | routed 20260910T145158Z, **not yet applied** |

⚠ **THIS SEAT IS NOT WRITING THE ENUM AND NOT FLIPPING THE RATIFICATION.** Andrew's word settles
WHICH macro; it does not make this seat the author of the COO's record or the holder of his flip.
Relayed verbatim to both lanes rather than acted on here.

⭐ **AND NOTHING ABOUT THE FOURTEEN OUTCOMES DEPENDS ON ANY OF IT.** L4 can be drafted against the
block in section 2 today; only the file it lands in waits.

**NOTHING DOWNSTREAM IS BLOCKED BY THE HOME QUESTION.** L4 can be drafted against this block; only
the file it lands in is undecided.

---

## 4. WHAT L2 CHANGED FROM THE BRIEF, AND WHY

The brief's territory is `O1`-`O12`. This endpoint carries **fourteen** outcomes. The two additions
are stated so `4.0.0_SA_CRO~Z` can contest them:

**`FWD-13` (one company per page) is NEW and it is the brief's own finding generalised.** `O8`
constrains the COMPARISON block to be about the right company. But the brief names identity as its
own qualification class in III-B, and PART V names **three separate keys** plus a fourth social
layer "with no ISIN". `F6` is the measured proof that this failure is real and survives for months.
⛔ **An identity defect on the news, social or investor-page axis would be the SAME failure as `F6`
and no outcome named it** -- the domain had an uncovered member.

**`FWD-14` (lists that rot) is NEW and comes from PART V rather than Part I.** The brief calls out
that both living lists rot, that an enumerated list with no owner lapses silently, and that this is
the same failure that left two keys dead. ⭐ **A silent lapse cannot be caught by any per-item
check** -- which is III-B's own shared-defect bar pointed at the lists themselves.

**`FWD-9` is the only APPLIED bar; the other thirteen are EXERCISED.** That is deliberate and it is
the honest reading of a product whose whole test is displacement: the brief's III-B bars are written
as things a PERSON does, not as things a system has. **Marking generated prose is genuinely a
property of the built page**, so it is APPLIED. Everything else is only real when someone used it.

⚠ **THIS MAKES THE ENDPOINT EXPENSIVE ON PURPOSE.** Thirteen EXERCISED bars means thirteen outcomes
that no build alone can close. That is the correct shape here and it is exactly the trap this estate
met on the sibling reporting project, where eight outcomes were graded as met against artefacts that
had never run. **A bar that says EXERCISED does not enforce itself -- grade the state line.**

**NO THRESHOLD IS SET ANYWHERE ABOVE.** The brief refuses to set one and is right: a number invented
at L1 is treated as ratified by every later stage because it is sitting in a document. **The
qualification VALUES for all six III-B classes are L4's**, and this seat has not taken them.

---

## 5. PROVENANCE (mandatory)

```
GROUNDED ON:  docs/briefs/amgt-resapp-security-analysis-20260910.md @19ce7d5b4d, 22,244 bytes,
              read IN FULL from the working tree (lines 1-330), not from origin
              version discrimination: git merge-base --is-ancestor on BOTH copies, with the v1
                ancestry read as the positive control; token counts one variable apart
              org/missions/MACROS.yaml -- directive macro enums, regex over the directives block
                with a positive control (the matcher finds D0)
              python .tools/directives-check.py --code D5 --json -- for the LANDING PATH ONLY

NOT READ:     the task-order register, in any form -- Phase 0 reads the brief and nothing else,
                and blending intent with what is already moving is unrecoverable downstream
              org/projects/AMGT_RESAPP.json -- it does not exist ("no-json" on the directive row)
              docs/architecture/D5_ALT_RESEARCH_PRD.md -- the DIRECTIVE PRD exists, and was NOT
                consulted: this is a PROJECT endpoint and reading the parent would import
                outcomes nobody wrote for AMGT_RESAPP
              every sibling project named in brief PART II -- their code, their decomps, their
                task orders. The brief asserts a shared PATTERN and no shared code, and this
                seat did not verify that claim because no outcome above depends on it

DISCLOSED:    directives-check was read AFTER the fourteen outcomes were derived and NO OUTCOME
              IS DERIVED FROM IT. It answers only section 3's "where does the PRD go".
```

**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` pushes.
