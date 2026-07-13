# PROVENANCE SWEEP -- 2026-07-13 (2.0.0_SA_COO)

**archetype:** VALIDATE

**Andrew-direct (verbatim, relayed by `0.7.0_AE_CloudOps` 20260713T215049Z):**
> *"I just brought COO online... I want you to relay this all to them and what youve been doing so they make sure to
> update all the associated registry items and provenance documentation for this reason."*
> *"all TOs and work need to be refreshed so other agents dont come across it like you did and think the last work was
> issuing a first TO a week ago."*

**THE LENS (from the defect that triggered the ask):** the `NFRA_WEBSITE` REGISTRY row read *"HELD by Andrew at PRD
stage (2026-07-01) -- do NOT decompose/dispatch until he greenlights"* **while the box had been serving the real site
for days.** Twelve days stale.

> ## A STALE RECORD IS NOT A SILENT RECORD. IT DOES NOT SAY "UNKNOWN" -- IT SAYS SOMETHING FALSE, WITH AUTHORITY, TO THE NEXT AGENT WHO ARRIVES.
> **Do not hunt for records that are OLD. Hunt for records that would give a fresh agent a CONFIDENT WRONG ANSWER.**
> *A row saying "unknown" costs a lookup. A row saying "HELD, do not dispatch" costs the project.*

---

## 🔴 FINDING 1 -- **THE REMEDY FOR LD-0291 IS ITSELF A LANDMINE, AND THE GATE CLAUDE.md PROPOSES WOULD DETONATE IT**

**Rule 23 / LD-0291 says `opalcapital.com` was *"purged from the estate."* The next agent who reads that, or who is
handed the proposed gate, will grep for `opalcapital` and start deleting. THAT WOULD BREAK THE BLACK DIAMOND PIPELINE.**

**MEASURED, with the denominator (`comp-grep -i opalcapital . --include-held`):**
```
TOTAL                200 hit lines / 65 files      <- the FIRST scan silently excluded 972 sovereign-held paths.
                                                      "not searched" is NOT "confirmed absent". Print the denominator.
CLASS A  the DOMAIN   93 lines / 20 files  opalcapital.com -- the thing we do not own
CLASS B  NOT A DOMAIN 74 lines / 27 files  <-- ⚠️ THIS IS THE LANDMINE
OVERLAP               0 lines                       <- the two classes are cleanly separable. A gate CAN discriminate.
```

**CLASS B is `OpalCapital` as a proper noun inside strings that are NOT ours to rename:**

| String | What it actually is | What happens if an agent "purges" it |
|---|---|---|
| `Fees_OpalCapital_Daily` | a **Black Diamond EXPORT TEMPLATE NAME** (vendor-side) | the downloader asks BD for a template **that does not exist** -> cot fee pipeline dies |
| `Transactions_OpalCapital_Daily` | same -- BD template, hard-coded by contract | 49F/bd TXN ingest dies |
| `AssetDimTXNs_OpalCapital_Daily` | same (`BD_ASSET_DIM_PIPELINE.md` mandates `TEMPLATE_NAME` hard-coded) | asset-dim ingest dies |
| `AdministratorAccessOpalCapital` | an **AWS IAM/SSO GROUP NAME** | an IAM edit against a group that no longer resolves |
| `opalcapital.zip` | the **filename of the WordPress backup** we were given | a broken provenance pointer in the website PRD |

> ### **THE DOMAIN IS NOT OURS. THE STRING IS. `OpalCapital` IN A VENDOR TEMPLATE NAME IS BLACK DIAMOND'S PROPERTY, NOT A DNS RECORD -- AND A SUBSTRING MATCH CANNOT TELL THEM APART. 27 OF THE 65 FILES MUST NEVER BE TOUCHED.**
> **AND MOST OF THEM SIT INSIDE THE SOVEREIGN-HELD 49F/Schwab/bd PATHS** -- so the purge sweep would ALSO be an
> unauthorized edit inside a standing prohibition. *Two prohibitions, one grep.*

**GATE REQUIREMENT (routes to CTO, who owns the Rule 23 / LD-0291 owned-domain-allowlist build):**
The gate must key on the **DOMAIN** (`opalcapital\.com` as a hostname / SES `Source=` / ACM SAN / DNS-bearing
resource), **NEVER on the substring `opalcapital`.** A naive substring lint has a **27-file false-positive surface**,
every one of them business-critical, and firing on them would look exactly like diligent compliance.
**Class A is 93 lines and CLEANLY SEPARABLE from Class B (overlap = 0). The discriminating gate is buildable. The
lazy gate is not merely weaker -- IT IS ACTIVELY DESTRUCTIVE.**

**LIVE STATE, verified on the primitive (not a doc, not a self-report):**
`aws ses list-identities` -> **`opalcapital.com` is ABSENT.** Only `opalinvest.dev` (+ address-level identities)
remain. **CloudOps's purge claim HOLDS.** Rule 23 satisfied at the SES layer.
**Residual Class-A references are concentrated in `docs/architecture/archive/`** (30 lines in one
`TRADE_SUBMISSION_EMAIL_GROUPS_SETUP.md` alone) -- **historical docs, inert, and they are ARCHIVE.**
*Do not mass-edit archive to make a grep quiet. An archive that has been retro-edited is no longer evidence.*

---

## FINDING 2 -- **THE STAND-DOWN CENSUS: which records tell a fresh agent to STOP, and are they still TRUE?**

**⛔ MSTR's FENCE, and it is the right one:** *"A sweep whose job is 'make the record match reality' is the most
dangerous possible instrument to point at an estate whose SAFETY depends on records that say STOP."* The INF hold
docs, the frozen-file list, the door census **LOOK like a neglected pile of red flags. THEY ARE THE GUARD.**
**Refresh metadata if wrong; NEVER soften, close, tidy, consolidate, or mark-resolved. If a status looks wrong: ASK.**

| Record | Says | Verdict |
|---|---|---|
| `REGISTRY.md` NFRA_WEBSITE | ~~"HELD at PRD, do NOT dispatch"~~ | **FIXED** (CloudOps `1ab8f4e3e`) -- was the triggering defect |
| `NFRA_WEBSITE.TO-1` AC-5 | "rollback point preserved" | **RETRACTED** (COO `df8465af1`) -- measured true, concluded false |
| INF hold docs / frozen-3 / doors | "STOP" | ✋ **TRUE. LIVE CONTROLS. DO NOT TOUCH.** |
| `BD_RPSAUTO` | "Do not start" | **TRUE** (Andrew-sequenced after Inflection + inside the 49F prohibition) |
| `NFRA_PASSCRAFT` / `NFRA_TOOLGRAPH` | `coo_lane: COO~A ... do NOT dispatch` | 🔴 **ROUTED TO A CORPSE.** `COO~A` is DEAD. A lane assignment to a dead serial is not a hold -- **it is a record that will never be actioned by anyone, and it does not say so.** *"A decision routed to a dead serial is not BLOCKED. IT IS LOST."* -- **UNRESOLVED, escalated, NOT self-corrected** |
| `NFRA_COMPPROOF` TO-D2 | "FENCED behind D1-GREEN" | **UNVERIFIED** -- is D1 green? Owner CVO~B is DOWN. Do not clear. |
| `NFRA_MSGRAPH` S3 | "GO HELD on S2 going live" | **UNVERIFIED** -- is S2's flag flipped? |
| `MDPF_SCOPED` | "1 LEG FROM CLOSE 2026-06-03: only S5 Andrew visual-smoke remains" | **6 WEEKS stale as a claim.** Needs Andrew, not an agent. |

**The `COO~A` class is the sharpest and it is MINE:** two live projects carry a lane assignment to a serial that does
not exist. **Not held, not blocked, not idle -- LOST.** Per LD-0288 I may not re-home or respawn. **Surfaced to MSTR
+ CTO; NOT self-corrected.**

---

## WHAT I DID NOT DO (and why that is the finding, not the gap)
- **Did NOT arm `/drive`.** Andrew named it OFF in both answers. Zero crons, zero dispatches, zero spawns.
- **Did NOT act on any record I refreshed.** *A TO refreshed to `pending` is not a TO I may drive.* (MSTR fence (b).)
- **Did NOT tidy the INF hold docs, the frozen-3, or any door.**
- **Did NOT mass-edit `docs/architecture/archive/`** to make the `opalcapital` grep quiet.
- **Did NOT touch `~Z` or `AE_CloudOps`** -- Andrew-scoped agent-by-agent, not under my coordination.
