# ANDREW-DIRECT 2026-10-20 ~12:50Z -- the Fidelity secret has been set; turn off autoshutdown for the box

Given at the laptop `0.0.0_AB_MSTR` terminal (Claude Code session), 2026-10-20T12:50Z (8:50 AM ET), right after the Fidelity status PDF
reached his Desktop. VERBATIM, typos kept:

> "tell htme the secret has been set, also we need to turn off autoshutdown for this box"

## What it names (his words only)

- Tell "htme" that "the secret has been set".
- "we need to turn off autoshutdown for this box".

## My reading, INFERRED from `Fidelity_Uploader_Status_20261020.pdf` (not his words; the receiver verifies)

- "htme" reads as "them": the dell1 Fidelity seats (4.0.0_SA_CRO~FIDELITY, the dell1 CTO), who sent the PDF.
- "the secret" reads as the Secrets Manager entry `fidelity/alongside/wealthscape-credentials` (us-east-1), which the PDF says the live
  run waits on. No value travels anywhere.
- "this box" reads as the Fidelity uploader host `i-028e830f7226cc685`, which the PDF says the overnight shutdown sweep stopped at 8:51 PM.
  It could mean another box; the receiver confirms the target against the PDF before changing anything.

## What this record does NOT rule

- It does not name any other instance, any other secret, or any other shutdown job. MSTR changes nothing in AWS: the owner of that host
  (dell1) applies the autoshutdown change under its own gates.
- It does not say the secret holds a working login. It is his statement that he set it.

-- 0.0.0_AB_MSTR (laptop), carrying Andrew's word
