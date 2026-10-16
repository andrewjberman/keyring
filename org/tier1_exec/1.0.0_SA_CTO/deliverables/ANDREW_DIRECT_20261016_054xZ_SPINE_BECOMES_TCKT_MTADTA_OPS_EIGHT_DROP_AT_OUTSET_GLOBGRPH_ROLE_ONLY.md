# ANDREW_DIRECT 2026-10-16 ~05:4xZ -- the M365 spine becomes TCKT_MTADTA (Ticket Center analytics): eight ops accounts, everything else dropped at the outset, readable only through a globgrph-group IAM role

Channel: the laptop `1.0.0_SA_CTO` terminal. Recorded by 1.0.0_SA_CTO, same turn.

## His words, VERBATIM

> I think the M365 spine is actually going to be referenced in the context of ticket-center analytics. We want to track this
> metadata for the sake of monitoring ticket-center-focused operational workflows. i think accordingly this goes under the TCKT
> macro, perhaps a TCKT_MTADTA. I want the application qualified as ticket-center analytics, the premise is that we will identify
> from the sequences what workflows need to be absorbed into ticket center request sequences. Accordingly it should only cover
> operational team members, i.e. andrew@opalinvest.com, alyssa@opalinvest.com, bobby@opalinvest.com, manav@opalinvest.com,
> yang@opalinvest.com, menachem@opalinvest.com, jim@opalinvest.com, jeanette@opalinvest.com. That means that all other
> domains/accounts should be dropped at the outset and not stored. I think this goes in opal-data-trino with the folder being
> m365-metadata. everything is stored in bronze, then silver parquet, then gold analytics tables we will decide upon later when we
> have more data. opal-data-trino should only be viewable by an iam role associated with globgrph group. Therefore, if we want to
> access it, we need to make a call to a lambda with the relevant iam role that will have the role group. If we do it like that, if
> yang or my account was compromised, it would not matter right?

## What it settles (the receiving seat surfaces; it does not widen or narrow)

| # | item | his word |
|---|---|---|
| 1 | Purpose | Ticket Center analytics: from the sequences, identify which ops workflows should be absorbed into Ticket Center request sequences. The application is "qualified as ticket-center analytics". |
| 2 | Macro and code | Under TCKT; "perhaps a TCKT_MTADTA". This replaces NFRA_WFSPINE (NFRA, dell1). The register move is the owning fabric's CTO's L3 act. The box is NOT named in this word: dell1 was placed for NFRA_WFSPINE on his f086 word, while TCKT projects run on dell2. Open, and asked of him. |
| 3 | Population | EIGHT accounts: andrew@, alyssa@, bobby@, manav@, yang@, menachem@, jim@, jeanette@ (all @opalinvest.com). |
| 4 | Filter location | "all other domains/accounts should be dropped at the outset and not stored": call 142a's option (a), the drop at collection. That is a deliberate departure from R9 (bronze is raw); this word is his acknowledgement of it, for the R20 register entry. |
| 5 | Home | bucket `opal-data-trino`, folder `m365-metadata`; bronze, then silver parquet, then gold analytics tables decided later "when we have more data". |
| 6 | Access | `opal-data-trino` is viewable ONLY by an IAM role associated with the globgrph group; access is by calling a Lambda that holds that role. |
| 7 | Question | Whether a compromise of his or Yang's account would then not matter. Answered in session (below). |

## The answer given to item 7 (summary)

**Not entirely.** Role-only access with a Lambda front door removes most of the exposure, but not all of it:
- **Their Microsoft 365 accounts:** a compromised M365 account does not reach the AWS copy, unless that identity federates into
  AWS. But Andrew's account holds Cloud Application Administrator, so a compromise of it could add a credential to the collector
  app or consent new permissions, and read the tenant's audit log directly from Microsoft, bypassing the S3 copy. Yang's ordinary
  account cannot.
- **AWS identities:** "only the role" holds only if the bucket policy, and ideally a dedicated KMS key, DENY everyone else. That
  includes admin principals such as `Andrew_Berman`, because an admin can otherwise edit the policy, assume the role, invoke the
  Lambda or change its code.
- **The Lambda:** it is an access path too. Whoever may invoke it can read through it, so invoke rights and what it returns
  (aggregates, not raw rows) are part of the control.
- **Data about other people:** dropping the other accounts' EVENTS does not remove other people's DATA. The eight users' own
  events still name recipients, shared-with addresses, chat members and client names in subjects and file names.
