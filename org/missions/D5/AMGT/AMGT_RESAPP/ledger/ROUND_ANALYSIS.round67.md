# AMGT_RESAPP -- ROUND 67 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-05 ~00:3xZ

**Input:** CVO slug msg 29344, `surprise-channel/adjudications/ADJUDICATION_v80.md` @69ce44def1. The packet is
`deliverables/2.0.0_SA_COO~Z/round67/DRAIN_END_PACKET.md` @b0a3cdee6c.
**Precondition:** MET for the round's rows. Z-S346 is disarmed in fact (Z-S347). The 153 legacy ARMED rows were dispositioned in
prose at their rounds, and the CVO reconciles them as REMEDIATION_v14. That is bookkeeping on settled rows (the CORPUS precedent,
round-35 analysis), so it does not hold this analysis.

## 1. WHAT THE ROUND DELIVERED

- **aq-1:** the FWD-39 word-cloud list repair (own ticker root, short and long name words, the measured boilerplate, an inverted
  window with its reason).
- **aq-2:** FWD-36 tone and voters from `chatter_window`.
- **aq-3:** FWD-38 (d) `/ledger` provenance.
- **aq-4:** Z-S86, a covered name with no block.
- **aq-5:** the redeploy, with grant leg 1, code leg 2 and aq-6 as leg 3, the chatter_window read prefix (Z-S346 cured).
- **Live:** the function runs `2rFeF57l` (CORPUS al-5's build, which carries round 67).
- **Proofs:** all four AE deploy instances were reshaped under the DEPLOY genre (@fc5728daff; CVO verdict 29325).

**Round 67 is CLOSED.**

## 2. GRADES (CVO L9)

| outcome | grade | basis |
|---|---|---|
| FWD-39 | DONE WHEN **MET** (BA, AMD, VLO); ACCEPT **NOT met** on 6 of 199 served clouds | XOM exxon/mobil, GOOGL/GOOG google, NSRGY "nestl", HESAY "herm", AZN astra |
| FWD-36 | **NOT met** on 21 of 95 names | the producer's 212-name set misses them (Z-W220-S1); the 74 served read right, 0 voters reads "no clear tone" |
| FWD-38 (d) | **PASS** | all 6 classes name a source or a reason on NVDA as well |
| Z-S86 (DE) | `/peers` PASS; `/thesis` **FAIL** on plain words | it opens "identity UNRESOLVED -- no measured security key ..." |

## 3. WHY THE ISSUER'S CHECKS PASSED WHAT THE GRADES FAILED

1. **c23's population was the 95-name chatter universe, but clouds serve on 199 names.** XOM, GOOGL, NSRGY, HESAY and AZN sit outside
   the 95. A census whose population is narrower than the served surface reads a clean zero over the part it never looked at.
2. **aq-5's c24 graded on a LOCAL arm, which cannot see the function's IAM role.** It read the table with the seat's own credentials
   and passed, while the deployed role was denied (Z-S346). A local read of an S3 path is not evidence that the role can read it.

## 4. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **FWD-39, 6 own-name leaks + junk tokens** | **Round-68 cell, LOCAL + redeploy:** (a) an **accent-safe tokenizer** (NFKD, combining marks stripped), so "Nestle" and "Hermes" tokenize whole; (b) a **DECLARED own-name alias list** beside the declared stop-word list, seeded from the measured cases (google; exxon/mobil; astra), plus a rule that splits a compound name into its parts of 4 or more letters; (c) the measured headline boilerplate ("movers", "premarket", "sees", "estimates") and the "hon"/"hai" split join the declared lists; (d) **c23's census population = every name that serves a cloud** (199), never the 95. | The ACCEPT is "without the company's own name". The two root causes, name forms and a byte-unsafe tokenizer, are fixable in the code. A hand alias list is the declared-list pattern the PRD already uses for stop words. |
| 2 | **FWD-36, 21 names with no tone** (Z-W220-S1) | **Routed to the producer.** `chatter_window`'s writer is HARVST's `window_tone.build_window`; its build list becomes the UNION of the rank universe and RESAPP's covered set. A covered name with no mentions then gets FWD-17's explicit zero row ("no clear tone") rather than no row. This is **HARVST round 46** (`2.0.0_SA_COO~H`), a served write under a pair. RESAPP round 68 re-reads c24 after it lands. | FWD-36 is computed only from the table, and FWD-36 forbids request-time tone. The gap is the producer's population, not the route. The table's single writer is HARVST's. |
| 3 | **Z-S86, `/thesis` for DE** | **Round-68 cell, LOCAL:** `/thesis` for a covered name with no block reads like `/peers`: "<Company> is a covered name ... and its research pack is not in yet." No identity jargon. The same pass rewords `/ledger`'s "estate", "stage" and "input ledger" reasons in plain words (DSGN FWD-27). | One served name, two routes, two vocabularies. `/peers` already reads right. |
| 4 | **A local arm cannot see the role** (section 3, item 2) | **Standing for RESAPP's redeploy cells:** a code leg that adds an S3 read path carries a `simulate-principal-policy` arm on the function's role for EACH new path, `allowed`, before the code leg is called LANDED. A served check grades on the DEPLOYED function. | It is the measured cause of Z-S346. It costs one simulate call per new path. |
| 5 | **The round-68 redeploy** | One code-only redeploy cell (WORLD, AE~A) under a pair. Its proof follows the DEPLOY genre (`<proof_genre>DEPLOY</proof_genre>` on the order). Content diff against `2rFeF57l`, the deployed build, never against an older pin. | Two projects deploy this function; the content-diff-against-deployed rule keeps either from dropping the other's code. |

## 5. ENRICHMENT LIST (round 68, ONE issuance by `2.0.0_SA_COO~Z`)

1. The FWD-39 cloud repair (ruling 1): tokenizer, alias list, boilerplate, the census over every cloud-serving name.
2. `/thesis` plain words for a covered name with no block, and the `/ledger` wording (ruling 3).
3. The redeploy cell (ruling 5), with ruling 4's simulate arm wherever a read path is added.
4. After HARVST round 46 lands the widened `chatter_window`: a re-read of c24 on the deployed function.

**Routed separately:** HARVST round 46's `chatter_window` build list = rank universe UNION RESAPP covered set (ruling 2), to
`2.0.0_SA_COO~H` on the round-45 analysis's list.

## 6. ACTS FOR ANDREW (cited)

None in this round.
