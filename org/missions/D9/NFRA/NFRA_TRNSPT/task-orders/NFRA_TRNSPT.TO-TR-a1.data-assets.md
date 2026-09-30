# TO NFRA_TRNSPT.TO-TR-a1 -- the versioned, hash-pinned data assets: authors, client domains, model aliases, name dictionary, allowlist

<to_id>NFRA_TRNSPT.TO-TR-a1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~4</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-a-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-a-1`, communications item 1b (PRD section 3): "the alias table, the client-domain table, the author-address table, the name
dictionary and allowlist as versioned data assets." C-WIPE: "a vendored, hash-pinned dictionary (public name lists) applied
case-sensitively, behind an ALLOWLIST (Opal model names, products, tickers, finance terms, theme labels), plus the client firms'
names and advisor names." PRD ruling 6.7: contract files are DATA, authored in round 1.

**Andrew-direct 2026-09-30 (call 2), verbatim -- the word for the download:** "This may be overengineering, should be easy enough
to rig up a dictionary of "any" name tokens and hashing any number strings greater than 4 characters (e.g. 08242253 or z09302843).
I'm sure you could download a lib of all names and just include that as a utility/service for the script."
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_03xxZ_TRNSPT_OPEN_CALLS_ANSWERED_TICKET_CENTER_OWN_INGESTION.md`).
That word covers ONE fetch of public name lists; nothing else leaves Opal infrastructure.

**Measured at the cut:** author addresses `Manav@opalinvest.com`, `manav.shah@49financial.com`, `Yang@opalinvest.com` (Yang's
49financial address unmeasured -- carry a `null` row with `claim: absent`); client domains `49financial.com`, `inflectionwealth.com`,
`cottonwoodmail.com` with firm keys `49f`, `inflection`, `cottonwood` (v3 section 6). Model aliases in prose (v3 section 6): LTC /
49 Long Term, ULT / Ultra Long Term / LTA, UST, PFOE, DIVZ, Dividend Income Strategy, Short / Intermediate / Long Term; a real
2026-09-23 reply used "Long-Term Portfolio", "Dividend Income Portfolio", "Ultra Short-Term Portfolio", "LT", "ULT", "UST". IRPT's
`comparison_keys` values: read them from the investor-reporting source (`comp-find 'comparison_keys' infra/aws/lambda/investor-reporting --limit 20`
and the file that defines the enum) and map every alias to one key; an alias with no key gets `comparison_key: null, claim: absent`.

**Build (all under `data/transcripts/assets/`):**
1. `authors.json` `{"authors":[{"name","address","role":"author","claim":"measured|absent","basis"}], "_provenance"}`.
2. `client_domains.json` `{"domains":[{"domain","firm_key","firm_name","claim":"measured","basis"}], "_provenance"}`; the list is
   open-ended by Andrew's word ("including"); note it.
3. `model_aliases.json` `{"models":[{"comparison_key","canonical","aliases":[...],"claim"}], "_provenance"}`.
4. `allowlist.json` `{"tokens":[...], "_provenance"}`: every canonical and alias above, Opal products and tickers (DIVZ, IDVZ,
   PFOE, PFDE, and the ETF names in `research_transcripts/README.md`), finance terms that collide with names (Long, Short, Term,
   Dividend, Income, Growth, Value, Ultra, Treasury, Aggregate, Index, Fund, Portfolio, Benchmark, Grant as a model if one exists,
   Hunt inside a ticker), and the theme-label seeds of v3 section 5 (theme labels are WIPED, so they go in a separate
   `theme_labels` list, not the allowlist).
5. `names/given_names.txt` and `names/surnames.txt`: ONE fetch each from a public list -- the US SSA national baby-names file
   (`https://www.ssa.gov/oact/babynames/names.zip`) distilled to unique names, and the US Census 2010 surnames file
   (`https://www2.census.gov/topics/genealogy/2010surnames/names.zip`) distilled to the name column -- Title-case, one per line,
   sorted, UTF-8, LF; record each source URL, the fetch time and the sha256 of the DOWNLOADED archive in the lock. If a fetch
   fails, stop on that file and file a surprise row: never substitute a hand-typed list.
6. `README.md` (what each asset is, how it is updated, that every change re-pins the lock).
7. `ASSETS.lock.json` `{"files": {"<rel>": {"sha256","provenance","fetched_utc"}}, "name_dictionary_entries": <given + surnames>,
   "pinned_utc"}` covering every file in the folder except itself and README.md.
8. Tests `data/transcripts/scripts/tests/test_assets_lock.py`: every pinned sha matches; the three measured addresses and three
   domains present (lower-cased compare); every alias maps to a key or carries `claim: absent`; no allowlist token appears in the
   theme-label list; dictionary entries >= 50,000; the given-names file contains "Will" and "Grant" (so the wipe's case-sensitive
   guard has something to guard).

### ACCEPTANCE

<criterion id="TR1-a1-AC1" cell_refs="TR-a-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_assets_lock.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-a1-AC1` -- the assets are pinned, measured facts present, aliases mapped or marked absent.

<criterion id="TR1-a1-AC2" cell_refs="TR-a-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_assets_check.py</invocation><expect>ASSETS-PINNED</expect></criterion>
`TR1-a1-AC2` -- the issuer's check: every file pinned with provenance, nothing unpinned, the dictionary at size.

<expected_criteria>TR1-a1-AC1,TR1-a1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran", AC2 ASSETS-BAD no lock -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Egress:** exactly the two public name-list fetches Andrew's word covers. No other network call.
- **Size:** keep the two name files under 3 MB together (distil, do not vendor the yearly archives).
- **The wipe (TR-w-1) is the next order in your queue** and reads these files by these names.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W4-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/assets/
data/transcripts/scripts/tests/test_assets_lock.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-a-1`.
<owned_cells>TR-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-a1-AC1, TR1-a1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/NFRA_TRNSPT.TO-TR-a1.data-assets.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-a1-AC1,TR1-a1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the file list with sizes and shas, the two source URLs and archive shas, the alias-to-key table, the ASSETS-PINNED line, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- data.
comp-iam: DECLARED-NOT-APPLICABLE -- data; no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the measured addresses, domains and alias forms are inlined.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-CRITERION, C-WIPE, C-GOLD-FIELDS, S09, ruling 6.7; decomposition round 1 cell TR-a-1.
