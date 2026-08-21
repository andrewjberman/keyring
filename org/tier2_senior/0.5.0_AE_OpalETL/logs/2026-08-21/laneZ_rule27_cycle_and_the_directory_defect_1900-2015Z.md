# 0.5.0_AE_OpalETL~Z — the first Rule-27 cycle, and a defect in my own live build (1900–2015Z)

**Serial** `0.5.0_AE_OpalETL~Z` · **2026-08-21** · site Z

## What landed

| commit | what |
|---|---|
| `to-check` fix | 3 defects, 3 **independent** mutants; the assignee query was wrong in BOTH directions |
| GSI fix | claim enrichment resolves via `email-index`, **built not applied**; code + IAM + an 8-test battery |
| M5 correction | a schema value of mine asserted something the same document calls unobservable |

## THE ONE THAT MATTERS: I SHIPPED A DEFECT THAT MISSES EVERY REAL OPAL HUMAN

`_directory_snapshot` resolved a claimer by **constructing** `PK = "USER#" + email`. Measured over
the whole live table, token-walked: **31 of 48 PROFILE rows use that shape; 17 carry an opaque
`USER#usr_<hex>` PK — and those 17 include 15 of the 20 opal-capital principals.** The five internal
rows that *did* resolve are all service/test/vendor accounts. **I ran the deployed lookup itself for
`andrew@opalinvest.com`: NO ITEM.**

**THE ROOT IS IN MY OWN ANTI-ASSUMPTION BANNER.** The docstring read *"KEY SHAPE IS MEASURED, NOT
ASSUMED (live describe-table + a bounded 3-item sample)."* With 31/48 rows email-form, **a 3-item
sample was overwhelmingly likely to be all-email and could not have falsified the rule.** A sample
with no power, wearing a measurement's clothes, in the sentence written to prevent exactly that.

**THREE SEATS VERIFIED W-A AND ALL THREE RAN THE SAME RUNG.** We each proved the deployed bytes were
byte-identical to HEAD with a discriminating negative control, at three independent seats. *That
check was true and irrelevant.* **Correctly-deployed code that does not work is still correctly
deployed.** Rule 22a names the rung we skipped — EXERCISED — and WA-1/WA-2, the rows that would have
caught it, were the ones left UNCOMPUTABLE **because exercising them needed a real ticket.**
**The uncomputable rows were not bookkeeping. They were the only rows pointed at this failure.**

**AND E-2's DEGRADATION IS WHY NOBODY TRIPPED OVER IT.** Every miss renders as *"An Opal advisor"* —
indistinguishable from a user who genuinely has no directory row. **A well-built fallback converted a
systemic defect into a plausible edge case.** Not an argument against the fallback; the argument for
keeping its tokens distinct, which is the only reason it was diagnosable at all.

## Three things I got wrong on the way, each caught by a control

- **The mutant harness returned all zeros** — `WORKSPACE` derives from `__file__`, so a scratch copy
  scanned an empty tree. Every mutant "passed" vacuously and read as *"the fixes are not
  independent."* A baseline assertion against the live CLI now runs before any verdict.
- **A mutant that did not mutate.** It replaced the first `return ""` — the empty-to_id **guard** —
  returning `""` for an empty string, while the *text-changed* assert passed. It reported
  *"not independent"* and meant *"never fired."*
- **I nearly picked a fixture that dodged the defect.** `user@opalinvest.com` resolves; choosing it
  as the test actor would have made WA-1 pass. **One keystroke from fixture-shopping.**

## What I did NOT do

**Spend the authorised test ticket.** WA-1 requires identity resolved server-side; on a real internal
claimer that could not pass. The defect was already proven by measurement **without writing to the
production table**, and the authorisation does not expire. Held until after the apply, so one
exercise validates the whole chain.

## The estate lesson I applied to myself twice

**"A REMEDY IS A CLAIM"** (`1.0.0_SA_CTO~Z`, after replacing a proxy with another unverified proxy
*inside the correction that ruled against it*). I had verified my own replacement against **a fake I
wrote to match my own design** — the same shape as the old stub encoding the code's assumption. So I
measured it on the live index, and it also surfaced a hazard I had not considered: **a GSI is
sparse**, so a row without an `email` attribute would be invisible. 0 of 48 today — stated as
*measured today*, not as a property.

**"READ EACH VALUE'S WORDING FOR A SECOND CLAIM."** Applied to my own axis within minutes: M5 said
*"no human received it"* — a receipt outcome the same document calls structurally unobservable. Fixed
in the **wording**, not a footnote, because a note is read by whoever reads the note and a value name
is read by everyone who reads a cell.

## Open, none of it mine to move

- The **apply** (GSI code + the new `dynamodb:Query` grant) — a call at Andrew, carried by CTO~Z.
- The **test ticket** — mine to run the moment the apply lands.
- **D7 TOs** — gate open; I execute when they cut.
