# AMGT_RESAPP -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-1 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 1, 2026-09-11 ~04:48Z. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, ALL THREE LIMBS -- and the third is the one that nearly slipped.** Source for limbs 1-2 =
`comp-surprise --project AMGT_RESAPP` (JSON, the tool's own denominators), cross-checked against a direct parse
of the fenced blocks; limb 3 = a criterion-tag census over all 16 orders plus a `grades` scan of both planes.

```
LIMB 1  task orders       16 of 16 TERMINAL (independent full-pair <status> read: occ=1 each,
                          0 multi-value conflicts, 0 non-terminal) -- 16 of 16 carry a VALID proof instance
LIMB 2  channel           24 items | UNDISPOSITIONED 0 | GRADUATED 23 | DISMISSED_WITH_REASON 1
                          0 defects | 0 malformed | 0 duplicate ids | 7 adjudication rows
LIMB 3  judgment grades   16 of 16 GRADED at C-S7 -- 13 PASS / 2 FAIL / 1 NOT_EVALUATED
```

> ⛔ **LIMB 3 WAS UNMET WHEN THREE SEATS AGREED THIS PRECONDITION WAS SATISFIED, AND THE GAP WAS THIS SEAT'S.**
> `2.0.0_SA_COO~ZZZ` (21176), `1.0.0_SA_CTO~Z` (21178) and this seat all read limbs 1 and 2, found them true,
> and called the precondition met. All 16 orders reserve exactly one judgment criterion to the CVO, all 16 were
> correctly handed over as `UNVERIFIABLE-BY-INSTRUMENT`, and NONE was graded -- while this seat had already
> reported L9 discharged at `@d98b82113b`. Corrected to the CTO before any slug was cut (msg 21179), graded at
> `@07b8a49587`, and recorded here because **a precondition with three clauses, checked on two, is
> indistinguishable from one that is met** -- and three seats agreeing made the belief stronger, not weaker.

**WHAT THIS SLUG CARRIES:** the graduated findings with a live condition and a named owner, plus **two DISARM
records confirmed BY EXERCISE** (`W9-S2`, the proxy TLS block, and `W7-S3`, the identity collapse). Rows inherit
their item's coordinate. No row carries a `route` -- the three route tokens are retired under spine v3.

**THE TWO I WOULD NOT WANT LOST IF NOTHING ELSE IS READ:** `W1-S2` (a fiscal-year join pairing fundamentals with
a price ~9 months later on every non-December filer -- plausible numbers, wrong, on a path no criterion in this
round examines) and `C-S7`'s two judgment FAILs (an unchecked figure that ships looking checked, and an
impostor-admitting identity test on a surface that names real companies).

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-W9-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "AMGT-s-b4's 9 attempted HTTPS GETs all failed at the TLS handshake because the Bright Data residential proxy re-signs traffic with an untrusted 'Bright Data Proxy Root CA' leaf. The row was filed as an EXTERNAL block. It was not external: the remedy was a one-keyword client-side default -- verify=False on the curl_cffi session -- and it was ALREADY COMMITTED in sa_rest_fetch.py, landing 3h11m AFTER the row.",
    "evidence": [
      "THE FIX AT HEAD, read by this seat: sa_rest_fetch.py:92 `kwargs = {\"impersonate\": \"chrome\", \"timeout\": 70, \"verify\": False}`, with its own comment at :86-91 naming the cause -- the proxy SSL-bumps, curl_cffi's default strict verification rejects it, 'every scratch prototype had verify=False; this committed version never did', and it was 'never caught here because this function was never exercised end-to-end after commit'.",
      "THE TIMELINE, which exonerates the worker: row filed 2026-09-10T23:15:24Z; fix committed 2026-09-11T02:26:53Z. The fix postdates the row by 3h11m, so 0.9.0_WK_AMGT_RESAPP~9 could not have had it and its honest TLS FAIL was correct at its vintage.",
      "THE RE-RUN LANDED: 18 raw objects across 3 tickers, symbol+report present 3 of 3, sa_ids MEASURED 3, AC2-AC6 PASS, AC7 confirmed createdAt/previousReportDate preserved. Order terminal @3be9d03962.",
      "Andrew-direct 2026-09-11 ~03:42Z named the canonical method (the CRO's SA auth mechanism brief); record @770ee8fb18."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-11T04:48Z, owner 3.0.0_SA_CVO~Z: disarmed BY EXERCISE, not by the edit alone -- the re-run completed against the repaired dependency and the order is terminal on an independent full-pair status read. NO remedy is owed on the fetcher: it was sound throughout and must NOT be re-cut. The world-fact the row states (the proxy SSL-bumps; a client-side default is required) remains TRUE and unchanged; only the OWNERSHIP OF THE REMEDY moved, from 'external' to 'our own committed script'.",
    "owner": "3.0.0_SA_CVO~Z (disposition) -- DISCHARGED. No downstream owner: nothing is owed.",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "nobody -- the re-run completed against the repaired dependency; no remedy owed",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": "2026-09-11T04:48Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "16 of 48 MEASURED bloomberg_ticker values in AMGT-s-12's universe.json were the identical string 'AAPL US' across unrelated companies, resolved from a shared template placeholder. A wrong identity does not just misstate a figure -- it changes WHAT THE DATA IS QUERIED FOR, and four downstream consumers hang off the identity root.",
    "evidence": [
      "MEASURED AT THE ARTIFACT by this seat, not taken from a report: ticker_status_partition now reads MEASURED 32 / INFERRED 0 / UNRESOLVED 57 over denominator_folders 89 (32+57=89, complete and MECE).",
      "THE DISCRIMINATOR A STATUS COUNT CANNOT GIVE: I recounted the MEASURED values from the `names` list -- 32 MEASURED, 32 DISTINCT, most-common count 1, 'AAPL US' present as MEASURED ZERO times. A collapse survives a status partition unchanged (16 rows can all read MEASURED), so only DISTINCT-vs-TOTAL sees it.",
      "THE FIX IS DISCLOSED, NOT SILENT: `shared_ticker_placeholders_downgraded` names 'AAPL US' mapped to all sixteen folders (AstraZeneca AZN through Total Energies TTE FP), so a reader sees what was removed and why.",
      "THE DOWNGRADE DIRECTION IS CORRECT: the 16 went to UNRESOLVED, not INFERRED. A shared placeholder is not weak evidence of an identity, it is none."
    ],
    "remedy": "DISARM CONFIRMED, 2026-09-11T04:48Z, owner 3.0.0_SA_CVO~Z: the specific hazard cannot now recur on this artifact -- 32 of 32 MEASURED values are distinct. ⛔ THE RESIDUAL IS NOT DISARMED AND IS NOT A REGRESSION: 57 of 89 folders read UNRESOLVED. That is the honest state and the identity layer's remaining work; a smaller honest number beat a larger contaminated one, and it must never be read as a step back from the 48 that contained sixteen falsehoods.",
    "owner": "DISARM: 3.0.0_SA_CVO~Z, discharged. THE 57 UNRESOLVED: AMGT-s-12's cell owner via the issuer, as coverage work, not as a defect.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "AMGT-s-12's cell owner via 2.0.0_SA_COO~ZZZ -- resolve the 57 UNRESOLVED keys",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": "2026-09-11T04:48Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AC4's literal string check cannot be satisfied by a correct, documented use of the TOOL THE ORDER ITSELF NAMES: .tools/deploy_ledger.py's cmd_close hardcodes a Status value the check's own patterns never match. So obeying the order is what makes the criterion fail -- the always-fails shape.",
    "evidence": [
      "The criterion's patterns and cmd_close's hardcoded Status are both in the repo at HEAD and do not intersect; the worker reported it after running the criterion as written rather than substituting a passing command.",
      "Class corroboration in the same round: W2-S2 and W3-S4 are the same shape on different criteria, so this is a criterion-authoring pattern rather than one bad line."
    ],
    "remedy": "Re-cut AC4's patterns against what deploy_ledger.py's cmd_close actually writes, or have the criterion read the ledger entry's fields instead of matching a string. RUN THE CRITERION AGAINST THE NAMED TOOL BEFORE THE CUT -- that one step would have caught all three instances in this round.",
    "owner": "The criterion author at the cut, 2.0.0_SA_COO~ZZZ; 1.0.0_SA_CTO~Z if the fix belongs at the criterion SHAPE rather than its text.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ (criterion text) / 1.0.0_SA_CTO~Z (shape)",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ (criterion text) / 1.0.0_SA_CTO~Z (shape)",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AC6's invocation `comp-routes behaviors | grep -c -E 'research|amgt'` CANNOT see a pure-add API Gateway route on an existing CloudFront catch-all -- the only design shape available inside this cell's write surface -- because cmd_behaviors prints each behavior's STATIC hand-authored comment and never a computed route list. The evidence the criterion wanted exists one subcommand away, under `comp-routes api-routes`, which AC6 does not name.",
    "evidence": [
      "comp-routes' two subcommands differ in kind: `behaviors` renders static comments, `api-routes` extracts declared routes. The worker showed the route IS visible under the latter.",
      "This is the most expensive member of the class because the BUILD IS CORRECT and only the READING is wrong, so the criterion sends a worker to fix something that is not broken."
    ],
    "remedy": "Substitute `comp-routes api-routes` in AC6's invocation. One token.",
    "owner": "2.0.0_SA_COO~ZZZ (the criterion text).",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT-s-9's AC2 reads a top-level `figure_ids` key from every AMGT-s-1 model_block_*.json, and NONE of the three landed files carries that key -- figures there are identified by a (scope, fiscal_year, mnemonic) tuple. So no figure can ever be cited as evidence and pass AC2's resolution check.",
    "evidence": [
      "All three landed model_block files were read; zero carry a top-level figure_ids list.",
      "The tuple identity is AMGT-s-1's actual shape, so the criterion was written against an imagined serialisation rather than the landed one."
    ],
    "remedy": "Re-cut AC2 to resolve a figure by the (scope, fiscal_year, mnemonic) tuple AMGT-s-1 writes, or have AMGT-s-1 also emit a flat id list if a flat key is genuinely wanted. Do NOT add the key only to satisfy the criterion -- decide which identity the project uses and state it once.",
    "owner": "2.0.0_SA_COO~ZZZ (criterion text) with AMGT-s-1's cell owner if the emitted shape changes.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The issuer's instruction ('AMGT-s-7 stays COMPLETE ... regenerate coverage_freshness.json') is JOINTLY UNSATISFIABLE with the owned-paths lane gate: lib/research/freshness/ is granted ONLY by AMGT-s-7's own order, and a TERMINAL order is not a live grant, so the worker could not commit the code fix its own regenerate required. Both instructions are individually satisfiable and contradictory together.",
    "evidence": [
      "The worker refused to commit rather than reaching outside its lane, which is the behaviour the lane gate exists to produce -- the refusal is evidence the control works, not that the worker failed.",
      "Distinct in kind from the three always-fails criteria in this round: nothing is wrong with the criterion text here."
    ],
    "remedy": "A GRANT decision, not a text edit: either re-open AMGT-s-7's lane for the fix, or cut the regenerate as its own cell with its own grant. Naming which is the issuer's call.",
    "owner": "2.0.0_SA_COO~ZZZ as issuer (the grant), not the worker.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The worker FACE names the proof-of-spec path as '<PROJECT>.TO-<cell>.proof_of_spec.json' while .tools/to-pipeline-gate.py's check_complete_flip requires the FULL task-order-filename stem, so a correctly produced instance is INVISIBLE to the gate until renamed. Surfaced TWICE in one round, from two workers (W3-S2 and W7-S2), on the same field -- W7-S2 records that its own launch prompt dictated the shorter name.",
    "evidence": [
      "Two independent surfacings of one face-authoring defect is corroboration, not duplication.",
      "The failure mode is silence: the instance exists and is valid, and the gate simply does not find it."
    ],
    "remedy": "Emit the full task-order-filename stem in the worker face's proof-of-spec path, so the face and the gate's discovery glob agree. Fixing the FACE is right; loosening the gate's glob is not.",
    "owner": "2.0.0_SA_COO~ZZZ (the worker face) with 1.0.0_SA_CTO~Z as the gate's owner if the glob is the half that should move.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "receiving-check.py grades a task order ONE FILE AT A TIME, so an issuance-set coverage limb refuses every member (owns 1 of 16) while the same gate run over the SET passes 16 of 16. Same world, two denominators, opposite verdicts -- a check scoped to the member cannot answer a question about the set.",
    "evidence": [
      "Both readings were run and reported by the issuer: per-file 1-of-16 refusals against a whole-set 16-of-16 pass.",
      "Rule 22's shared-dependency clause in instrument form: verifying each member cannot see a property of the set."
    ],
    "remedy": "Give the coverage limb a set-level grain, or state explicitly that it is a per-file check and must not be read as issuance coverage. Either is fine; the current state is a check whose verdict depends on which way it is invoked.",
    "owner": "1.0.0_SA_CTO~Z as the gate's owner.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S7",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "THE ROUND'S TWO JUDGMENT FAILS, both graded at C-S7 and both carried here because each is a GATE on a surface that will serve analysts. (1) AMGT-s-10 AC6: '12345 [PROVISIONAL]' keeps the number as the dominant text, and at a glance a PROVISIONAL row is skimmed as 'a number, fine' -- so the held-back rule is present in the DATA and absent in the READING, and an unchecked figure ships looking checked. (2) AMGT-s-15 AC6: the official-vs-impostor test is a BARE OR of three checks, so an impostor need only beat the weakest -- a copied 'official account of <domain>' bio line admits on check (3) alone, and check (2)'s verification mark has been decoupled from identity verification on at least one platform.",
    "evidence": [
      "Both FAILs rest on the ASSIGNEES' OWN WORDS, not on a stricter reading imposed at L9: AMGT-s-10's instance states the PROVISIONAL skim risk verbatim; AMGT-s-15's declares check (3) 'CHEAPLY GAMEABLE' and admitted 'on that basis alone'.",
      "Both share a shape worth carrying: the DATA is right and the READING is wrong. Neither would be caught by a mechanical criterion, which is exactly why both were cut as judgment criteria.",
      "AMGT-s-15's defect is the COMPOSITION, not the checks: three signals of unequal strength combined by OR are exactly as strong as the weakest, which inverts the intent of listing three."
    ],
    "remedy": "AMGT-s-10: land the DIFFERENT visual marker (colour or icon) for PROVISIONAL that SPEC_SECTION_checkface.md already scopes, BEFORE the .tsx serves PROVISIONAL figures. AMGT-s-15: require check (3) to CO-OCCUR with (1) or (2) -- one clause, turning the bare OR into an AND against a strong check.",
    "owner": "AMGT-s-10 -> the check-face builder at the .tsx via 2.0.0_SA_COO~ZZZ. AMGT-s-15 -> AMGT-s-15's schema owner via 2.0.0_SA_COO~ZZZ. Neither is 1.0.0_SA_CTO~Z's to build; both are its to route.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ to route both to their cell owners",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ to route both to their cell owners",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "For an ADR (BABA US, fiscal year end 31 March) Bloomberg NEVER returns a row carrying both a price field and a fundamentals field -- 100% of rows split fiscal-period-end fundamentals from calendar-year-end price/ratios -- so a fiscal-year join keyed on the CALENDAR year of `date` marries each fiscal year's fundamentals to a price observation roughly NINE MONTHS later. ⛔ THE MOST CONSEQUENTIAL FINDING IN THIS ROUND: it produces ratios that are individually plausible and collectively wrong, on a path no acceptance criterion in this round examines, and it is INVISIBLE in any December-fiscal-year sample.",
    "evidence": [
      "The 100% figure is what makes it actionable rather than anecdotal: not 'some rows' but every row in the raw HistoricalDataRequest response splits the two field families.",
      "Fiscal-year-end is a PROPERTY OF THE SECURITY, so the defect is scoped to non-December filers and will not appear in a December-heavy test set.",
      "Nothing in the output announces it -- the join succeeds on every row."
    ],
    "remedy": "Key the join on the security's FISCAL period rather than on the calendar year of `date`. This is a CORRECTNESS change to a landed artifact, not a re-render, and it should carry a control on a non-December filer.",
    "owner": "AMGT-s-1's cell owner via 2.0.0_SA_COO~ZZZ.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "AMGT-s-1's cell owner via 2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "AMGT-s-1's cell owner via 2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W4-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AC1's own required action -- re-running AMGT-s-12's f6_remeasure.py -- TRUNCATES that already-completed worker's committed deliverable, by construction, on every run. VERIFIED AT SOURCE: f6_remeasure.py:65 derives OUTPUT_PATH from `__file__` rather than from the caller, and :234 opens it in \"w\" mode. ⛔ A TOOL'S WRITE SURFACE IS THE TOOL'S, NOT THE CALLER'S -- so the owned-paths gate sees the invoking worker's declared paths and never the paths the invoked script writes, and this widening is structurally invisible to the lane.",
    "evidence": [
      "f6_remeasure.py:65 `OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"f6_remeasure.json\")`; :234 `open(OUTPUT_PATH, \"w\", ...)` -- \"w\" truncates.",
      "The behaviour is DISCLOSED in the script's own docstring (:48 'Writes: f6_remeasure.json beside this script'), so this is not a hidden bug -- it is a cross-worker write surface no gate can see."
    ],
    "remedy": "Scope OUTPUT_PATH to the CALLER, or have the criterion READ ~3's committed output instead of regenerating it. And generally: a criterion that tells one worker to run another's script has silently widened the first worker's write set past anything its order declares.",
    "owner": "AMGT-s-12's cell owner (the instrument) with 2.0.0_SA_COO~ZZZ for the criterion that requires the re-run.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT-s-12b's cell text names 'that folder's *ONE PAGER*.xlsx workbook' in the SINGULAR, and 5 of 89 folders carry TWO such workbooks that DISAGREE WITH EACH OTHER on the peer-set question -- so the singular phrasing does not pick out a file.",
    "evidence": [
      "Verified at the artifact with a printed denominator: one_pager_files counts are 0 -> 40 folders, 1 -> 44, 2 -> 5, summing to 89; the five are Imperial Brands IMB LN, Nokia FH, Petrobras PETR3 BZ, SAP GY, Total Energies TTE FP.",
      "The artifact's own workbook_partition (one_pager_found 49 / no_one_pager 40) confirms the same 89 from the other direction."
    ],
    "remedy": "A RULING, not a wording fix: the two workbooks disagree, so someone must say which one governs (newest? a named precedence? refuse and mark the folder?). Rewriting the cell text to say 'a workbook' without a precedence rule would move the ambiguity rather than close it.",
    "owner": "The cell text's author, 2.0.0_SA_COO~ZZZ.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W5-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two findings in one row, both live. (a) AMGT-s-15's own two schemas name reviewed_at/review_interval_days once per LIST and never per ENTRY, so rot.py's staleness is LIST-WIDE -- N is 0 or the full entry count, never partial -- and a partially-rotten list is indistinguishable from a fresh one until the whole list goes stale. (b) social_accounts.json's entries are keyed by a `security_key` THIS PROJECT DEFINES NOWHERE ELSE, resolved by the worker to AMGT-s-12 universe.json's `folder` value.",
    "evidence": [
      "(a) is a GRAIN defect: the coarse grain is the whole problem, not the threshold.",
      "(b) is an undeclared join key resolved by inference -- the identity-layer hazard C-S1 is about, one level out. An inferred key works until two sources disagree about what it means."
    ],
    "remedy": "(a) move reviewed_at to a PER-ENTRY field so staleness can be partial. (b) DECLARE security_key once, in the identity layer, and have social_accounts.json cite that declaration rather than resolving it by inference.",
    "owner": "(a) AMGT-s-15's schema owner. (b) whoever declares the project's identity key -- AMGT-s-12's cell -- via 2.0.0_SA_COO~ZZZ.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The manifest draws NO S1 -> S6 edge, yet S1's raw landing (C-RAW-BEFORE-DERIVED) needs the store S6 creates, and that store was ABSENT at two vintages. A missing dependency edge is not a documentation nit: it is the reason an ordering can be chosen that cannot work, and the absence at two separate vintages is the evidence it already did.",
    "evidence": [
      "Both vintages were measured by the issuer; the edge is absent from the manifest at HEAD.",
      "C-RAW-BEFORE-DERIVED is structural per STORE_CONTRACT s.1 -- there is nothing to derive from until raw/ exists -- which is exactly why the missing edge bites."
    ],
    "remedy": "Draw the S1 -> S6 edge in the manifest so the ordering constraint is visible to whoever sequences the cells.",
    "owner": "The manifest's owner via 2.0.0_SA_COO~ZZZ.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The BARE `comp-routes` PATH shim is baked to this device's MAIN checkout -- a different directory that never had this branch's commits -- so it reported '0' for a route that EXISTS; invoking the worktree's own tracked copy (`bash .tools/comp-routes`) lists it. ⛔ RAIL-WIDE, NOT CELL-LOCAL: a bare comp-tool on a branch answers from MAIN, which will recur on every branch that adds a route. The issuer's irreproducible '0' was an instrument artifact, and the worker re-measured rather than argued.",
    "evidence": [
      "Two invocations of the same tool NAME are two different programs here, with opposite answers on the same world.",
      "Same family, same round: W2-S3's `grep -r` counted a byte-coincidence inside a GITIGNORED terraform provider binary as a loopback violation, reading 1 instead of 0 until the ephemeral .terraform/ cache was removed -- an INTERMITTENT instrument, which is worse than a broken one because one clean run reads as proof.",
      "Both fail with rc=0 and a plausible number. No control placed INSIDE either read can catch it."
    ],
    "remedy": "Make the rail's shim resolve to the INVOKING WORKTREE's tracked copy, or have every comp-tool print which checkout it answered from so a wrong-checkout answer is visible. For W2-S3, exclude the ephemeral floor by construction rather than by remembering to clean .terraform/.",
    "owner": "1.0.0_SA_CTO~Z as the comp-tool rail's owner.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The repo's root .gitignore ignores the whole lib/ tree at :47 (standard Python-venv boilerplate), so any NEW file under lib/research/<anything>/ is gitignored until force-added -- `git status` and `git add` report it clean-absent without -f, while already-tracked siblings behave normally because git does not re-apply .gitignore to tracked paths. The failure presents as ABSENCE, which is the reading that ends an inquiry rather than provoking one. W1-S4 is the sibling shape: this worktree's .gitmodules is EMPTY, so the pinned portal gitlink cannot be initialised here at all, and the named READ material was read from a checkout carrying a DIFFERENT portal commit that also lacks the pin.",
    "evidence": [
      "The asymmetry is what hides it: lib/research/identity/ and its tracked siblings are unaffected, so the tree looks healthy while a new sibling directory silently does not exist to git.",
      "W1-S4 is a GRAIN/VINTAGE hazard rather than a missing file -- the material was read, from a real checkout, just not from the commit the cell pinned, and a citation satisfied from the wrong vintage looks exactly like one satisfied."
    ],
    "remedy": "Add a negation for lib/research/** to the root .gitignore so new files there are visible to git. Until then every new file under lib/ needs -f. For W1-S4, the empty .gitmodules cannot be fixed from inside a cell -- it is a device/worktree provisioning act.",
    "owner": "The root .gitignore's owner for W1-S3; the device/fabric owner via 1.0.0_SA_CTO~Z for W1-S4.",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z to route",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z to route",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "This cell's own BUILD text names an unstamped key, packs/<security_key>/status.json, that STORE_CONTRACT rule 1 ('nothing is ever written to a path that already exists') would otherwise forbid -- a DELIBERATE, DISCLOSED exception rather than a defect. Carried only so AMGT-s-14 does not generalise the stamp convention from it.",
    "evidence": [
      "The exception is stated in the cell's own build text, so it is disclosed at the point of use.",
      "INERT because nothing is wrong and nothing is owed -- this row exists to prevent a WRONG INFERENCE by a later cell, which is a legitimate use of the channel."
    ],
    "remedy": "No fix. When AMGT-s-14 reads packs/ keys it must not assume every key carries a stamp; the status.json exception is named in STORE_CONTRACT's own text.",
    "owner": "Nobody -- informational, addressed to AMGT-s-14's reader.",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "nobody -- informational; no remedy was required and that is settled",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "ARMED",
      "owner": "nobody -- informational; no remedy was required and that is settled",
      "at": null
    }
  }
]
```
