# ANDREW-DIRECT 2026-10-16 ~16:1xZ -- SOC2_MSLOGS is metadata only; its purpose is a remediation strategy that proves internal security

**Channel:** Andrew at the terminal of `4.0.0_SA_CRO~DELL1` (dell1), replying to the CRO's summary of the SOC2_MSLOGS brief
(`docs/briefs/soc2-mslogs-compromise-exposure-brief-20261016.md` @0113e9f438). **Recorded by:** `4.0.0_SA_CRO~DELL1`, same turn.

VERBATIM:

> Yeah we dont need to see the body of an email and stuff like that, this is metadata focused/analytics focused, do not need anything
> further. this is just a remediation strategy so we have something to prove that we have internal security

Two follow-on messages, same terminal, ~16:1xZ, VERBATIM:

> yeah like get the raw audit pull, dont redact it unnecessarily

> but this application/log system as I understand does not ahve anything that sensitive

**Fact beside the second message (from the PII read, not a ruling):** `org/tier1_exec/1.0.0_SA_CTO/deliverables/WFSPINE_AUDIT_CONTENT_AND_PII_20261016.md`
found the audit records carry no message body or document content. They do carry IP addresses on every event and sign-in (location
over time), account and recipient addresses, mail subjects in some Exchange events, and file and folder names (which can name clients).
Under "dont redact it unnecessarily" these are stored as Microsoft records them; protection is by the door and the KMS key, not by
redaction.

## How the brief carries it (AMENDMENT 1 to the brief, same commit)

- **Content is out, permanently:** no email body, no Teams message text, no document content is read or stored. The TCKT_MTADTA
  content outcome (FWD-10, C-CONTENT) does not carry over.
- **Scope is capped:** "do not need anything further". The outcomes stay as the brief's thread plus O1-O9, with no additions.
- **Purpose:** a remediation strategy and the evidence that Opal has internal security. O9 (show an auditor) and O8 (protected,
  survives the attacker) are the reason the project exists; the compromise reads (O1-O4) are the remediation strategy itself.
- **Raw bronze, confirmed by his word:** "get the raw audit pull, dont redact it unnecessarily". The C-FIELDS levers (subject hash,
  address class tokens, IP flag) are retired; bronze is the audit records as Microsoft ships them (the brief's F3). The records are
  metadata (who, what action, which item, when, from where) and carry no message body or file content.

## Routing
One line naming this record to `1.0.0_SA_CTO~DELL1`, who writes the endpoint (org/XXX.md). The locked plan still returns to
`2.0.0_SA_COO~S1`.
