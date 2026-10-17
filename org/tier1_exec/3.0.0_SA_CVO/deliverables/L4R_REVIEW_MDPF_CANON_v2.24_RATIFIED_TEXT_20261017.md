# L4-R review -- MDPF_CANON PRD v2.24 @3de758b21d, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-17 ~01:5xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 7101 (acked). Half hash `640d56ab0283`.
**Graded:** the whole diff 1fb9ac96ab -> 3de758b21d. It makes one ENDPOINT change, FWD-10 appended (FWD-1 to FWD-9 byte-unchanged), adds
FWD-10 to `endpoint_outcomes`, and adds the v2.24 change-log entry. CONTRACTS is unchanged.

## Verdict: SIGN

## FWD-10 against its source

- **Andrew's words** (`ANDREW_DIRECT_20261017_010xZ_COTTONWOOD_SUPERVISED_ONLY_MATCH_BD.md` @f67b4711f1): "make sure 'Cottonwood' asset
  tracking for the dashboard only includes the Supervised assets (and matches that ... number you see there)". This re-affirms 2026-08-25
  ("their book be displayed as only that which is Supervised on their behalf", a78c51158c).
- **How FWD-10 carries them:** the head and ACCEPT say the same two things. Cottonwood shows only supervised assets, and the total matches
  BD for the day.
- **The "or the page says plainly by how much and why" branch** is the honest exit for the gap the CRO measured inside BD (Dashboard
  versus export). It does not widen the outcome.
- **The rule is placed where it is enforced:** "history applies today's flags, and the served meta says so in a field" is a value carrying
  its claim, placed where a consumer can reject on it.
- **The negative arm is consistent:** 554,632,228.45 minus 33,071,069.62 = 521,561,158.83, against BD Supervised 530,421,988. That is
  the $8.86M the CTO's (b) ruling names.
- **No contradiction with FWD-9 (f):** FWD-9 (f) defines the Cottonwood Trend's Total as `partner_custody_total` and Other AUM as that
  total minus `model_aua`. The v2.24 ruling filters at the one producer of `partner_custody_total`, so (f)'s identities hold on the
  narrower book, and "the groups sum to the Total to the cent" still binds.
- **No contradiction with 49 Financial and Inflection:** their whole-book rule of 2026-08-25 is kept, and is tested by byte-identity.

## Carried, not grounds

1. **The Global consequence is the CTO's inference, not Andrew's words.** FWD-10 (a) says "the Global composite folds Cottonwood's
   supervised book through its sums". Andrew spoke of Cottonwood's tracking.
   - What follows: the Global total, and FWD-9 (b)'s Global "Client Supervised" band (which is `non_model_aua` minus the SMA lines),
     each fall by Cottonwood's Unsupervised accounts, about $33.07M on 2026-10-15.
   - This is mechanically forced by one producer, and the blast radius names Global. But the Global view is drawn for demo tenants too.
   - The never-widen pair should print the Global total before and after, and so should the DEV approval row Andrew reads before PROD,
     so that the Global move is something he sees, not something he infers. If he wants Global on the whole book, that is a second path
     and a PRD change.
2. **The (b) exit asks for a cause that may not be knowable.** "Names the remaining difference and its cause" needs a cause. Route 1
   (Andrew's BD Dashboard export) may not name one, and route 2 is a vendor question.
   - Suggested wording: "names the remaining difference and, where established, its cause".
   - If not that, then qualify the wait on the outcome with its reason and Andrew's word (rule 27, L2: a genuinely essential wait).
3. **A measurement sits inside ENDPOINT.** "(measured 0 of 130 on 2026-10-16)" belongs in the change log or the cell's preconditions,
   not in the outcome text. The negative arm's dollar figures are the test's own fixture and may stay.
4. **Client figures in the PRD.** The negative arm writes Cottonwood firm-level dollar totals into a committed file. This is the same
   class as the committed served fixtures (MDPF_CANON C-S96, recorded for the CTO's round-11 analysis), so it is not re-raised here as a
   ground.

-- 3.0.0_SA_CVO
