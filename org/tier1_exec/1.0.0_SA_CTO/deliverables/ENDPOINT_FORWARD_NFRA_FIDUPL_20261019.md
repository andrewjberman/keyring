# ENDPOINT (step 2, /endpoint --forward) -- NFRA_FIDUPL: the auto_fidelity uploader, landing the Wealthscape daily export every morning like Auto-Schwab (`1.0.0_SA_CTO~DELL1`, 2026-10-19 ~18:1xZ)

**Brief:** `docs/briefs/auto-fidelity-uploader-brief-20261019.md` @ea34e538ae (`4.0.0_SA_CRO~FIDELITY`, 251 lines, measured 2026-10-19).

**Order:** Andrew-direct 2026-10-19 ~17:55Z at the 4.0.0_SA_CRO~FIDELITY terminal
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1755Z_AUTO_FIDELITY_UPLOADER_TERRAFORM.md`), VERBATIM:
"I would like to build out a terraform for auto_fidelity uploader, essentially taking the same structure we did for schwab and applying it
to fidelity and making a terraform around it. once that is done, we need to make sure that we can pull the relevant tables from it every
morning at the same time that schwab does, so we can have consistency on timing for that ingestion."

**Project code (proposed at L3):** `NFRA_FIDUPL`, macro NFRA, directive D8. This is the sibling of `NFRA_AWSFTP`, which is on HOLD; the
brief names this project as the interim path ahead of the official custodian feed.

```
  FWD-1  An Opal analyst opens the Fidelity Alongside book for the prior
         business day and finds the day's Fidelity files already there that
         morning, with nobody having signed in to Wealthscape to fetch them
         DONE WHEN  EXERCISED -- one live trace driven on demand: the uploader
                    signs in by itself, reads the text-message code by itself,
                    lists and downloads the day's files, and lands them; the
                    analyst then opens them. The first scheduled morning is the
                    organic case
         ACCEPT     The analyst can read that day's Fidelity accounts, positions,
                    balances, prices, securities and transactions, and can be shown
                    that no person signed in or typed a code for them; a step done
                    by hand fails it
         SOURCE     brief Part I, candidate thread; O1; O3

  FWD-2  The Fidelity files arrive in the same morning window as the Schwab
         files, every day
         DONE WHEN  EXERCISED -- the scheduled chain is started on demand by
                    the same trigger the schedule uses and lands the day's files
                    with their record; the live schedule is read and fires
                    inside the Schwab window; one run is started on demand for a
                    day Fidelity has not yet produced, and its record says so.
                    The first scheduled morning is the organic case
         ACCEPT     Someone reading the morning ingestion sees Fidelity and Schwab
                    land within the same window and reads them as one routine; if
                    Fidelity has not produced its files by then, the record says so
                    instead of the run quietly landing nothing
         SOURCE     brief O2; Part III second test; Part V first item

  FWD-3  Each morning, one record says whether Fidelity landed, and if not,
         which step stopped it
         DONE WHEN  EXERCISED -- a morning record is read, and one deliberately
                    failed sign-in is read as such
         ACCEPT     An operator reading one morning's record can tell what was
                    listed, downloaded, skipped or failed, and the business date it
                    holds; and on a bad morning whether to look at Fidelity, at the
                    text-message line, at the export schedule or at the box; it
                    sends no message to anyone, it is only there to be read
         SOURCE     brief O4; Part III third test

  FWD-4  Every file is filed under the business date it actually contains
         DONE WHEN  EXERCISED -- a Monday export, which holds Friday's data,
                    is pulled on demand and read (the 2026-10-19 files, holding
                    2026-10-16, are served now); the same Friday files are
                    pulled a second time on demand and land once. The first
                    scheduled Monday is the organic case
         ACCEPT     Asking for a given business day returns the files whose content
                    is that day, and a weekend run that re-serves Friday's data does
                    not create a Saturday or Sunday that never traded
         SOURCE     brief O5

  FWD-5  The Fidelity files are kept as Fidelity sent them, in the same
         families of tables the Schwab work already converts
         DONE WHEN  APPLIED -- the landed families are compared with Schwab's
         ACCEPT     A data engineer extending the Schwab conversion to Fidelity
                    recognises the same kinds of tables (accounts, positions,
                    balances, transactions, securities, prices), finds them exactly
                    as Fidelity delivered them, and does not have to reverse-engineer
                    a screen
         SOURCE     brief O6; Part II (silver is a later project)

  FWD-6  Fidelity history from before the schedule started can be filled in
         DONE WHEN  EXERCISED -- one past window is fetched and read
         ACCEPT     An analyst can see Fidelity transactions from before the day the
                    schedule began, and positions and balances for earlier dates
                    wherever Fidelity can supply them; any dates Fidelity cannot
                    supply are named, not silently missing
         SOURCE     brief O7; Part V backfill item

  FWD-7  The whole uploader is set up and taken down from one place, beside
         the Schwab setup
         DONE WHEN  APPLIED -- the uploader is stood up from that one place
         ACCEPT     An engineer can read one setup that names the schedule, the
                    machine, where the logins are kept and what the uploader is
                    allowed to touch, and nothing about it exists only as a manual
                    console step
         SOURCE     brief O8; Andrew's order ("making a terraform around it")

  FWD-8  The Fidelity run never disturbs the Schwab morning pull
         DONE WHEN  EXERCISED -- both run on the same morning and Schwab's run
                    reads unchanged
         ACCEPT     On a morning when both run, the Schwab files land exactly as they
                    would have without Fidelity, and the Fidelity run waits for or
                    avoids anything the Schwab pull needs to itself
         SOURCE     brief Part II (the Schwab box is relied on and not changed);
                    Part V last item
```

## Questions the brief leaves open, and who settles them (none is an outcome)

- **The Wealthscape Terms of Use for automated access:** the brief marks this as Andrew's call (Part V), and it stands before any
  automated sign-in. This is an act only Andrew can do: his reading and word on Fidelity's terms.
  **Measured 2026-10-19 18:31Z** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_WEALTHSCAPE_TERMS_OF_USE.md`
  @e999b31f1f): the terms prohibit "agentic AI, robots, or other similar technologies" unless Fidelity approves. FWD-1's "nobody
  signed in" and FWD-3's failed sign-in therefore rest on that act or on Fidelity's written approval. The in-terms paths the research
  names are Fidelity's written approval, an Integration Xchange transmission, or a person's daily download; the rest of the chain
  (schedule, landing, record, Terraform, scope) serves all three and is built regardless.
- **Tenancy:** the export's domain is ALONGSIDE, LLC and spans several partner firms. Where it lands, and whether it is split, is an L4
  ruling under the cross-firm rule and the naming canon (brief Part IV, finding 6).
- **Browser-driven or raw sign-in; a reused Schwab box or a new one; vault or Secrets Manager:** L4 design forks. They go to the CRO for
  past patterns, per the routing table.
- **Registry rows for the Fidelity source and its scope(s)** are owed before any address is built (rule 30, brief finding 5).

## Provenance

- **Brief:** @ea34e538ae, read whole. Every outcome traces to a brief line (SOURCE column).
- **NOT READ:**
  - the research doc's HAR captures, which are not in the repo;
  - the Terms of Use;
  - any task order, since none exists;
  - the project register beyond the D8 members line and NFRA_AWSFTP's row (read only to place the project).
- **NOT YET LANDED:** this is the step-2 endpoint. The L4 PRD carries it under `ENDPOINT (step 2, /endpoint --forward)`.
- **L2 is not complete until Andrew confirms the DONE WHEN lines** (the canonical loop: he confirms the CTO's DONE WHEN).

## Amendments

- **2026-10-19 ~18:4xZ (`1.0.0_SA_CTO~DELL1`):** FWD-2 and FWD-4 DONE WHEN amended in place, ids unchanged, on
  `3.0.0_SA_CVO~DELL1`'s refusal @5c277d3352 (both read as waits). Each is now proven by an act a seat drives on demand, the organic
  morning kept as the case it is not waiting on. The ACCEPT lines are unchanged. The Terms of Use finding is recorded under the open
  questions.

-- 1.0.0_SA_CTO~DELL1
