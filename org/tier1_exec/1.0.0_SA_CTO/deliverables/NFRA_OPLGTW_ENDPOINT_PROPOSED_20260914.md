# NFRA_OPLGTW — proposed endpoint

Author: `1.0.0_SA_CTO~A`. Date: 2026-09-14. State: PROPOSED; Andrew has commissioned the project, but has not yet confirmed these individual DONE WHEN bars.

Input: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/SPEC.md@39a8c5eeca03666d3ef81dbccce6859506b572af`, revision 2, dated 2026-09-14, 26,224 bytes; no separate generated line.

Target: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`, section `ENDPOINT (step 2, /endpoint --forward)`. This endpoint is not yet landed in that PRD.

## ENDPOINT (step 2, /endpoint --forward)

### FWD-1 — Menachem uses Schwab data from his work Claude account

DONE WHEN: EXERCISED — a deliberate connection and reconnection walkthrough succeeds.

ACCEPT: Menachem signs in with his work account, asks a Schwab question in Claude, and can continue after signing out and back in without installing developer software.

PROOF: An observed owner-and-member walkthrough, including an expired sign-in and a fresh connection.

SOURCE: supplied brief lines 10–30, 101–125, 181–211.

### FWD-2 — Schwab answers are accurate and keep the masters separate

DONE WHEN: EXERCISED — chosen questions and date comparisons are checked against independently prepared examples.

ACCEPT: Menachem gets understandable holdings and balance answers for the master and date he selected, with SmartX and BlackDiamond clearly separate and without adding overlapping balances or different days together.

PROOF: Deliberately chosen examples with independently known answers, including a comparison between masters and between dates.

SOURCE: supplied brief lines 14–18, 81–99, 127–147.

### FWD-3 — Each person sees only the Schwab information granted to them

DONE WHEN: EXERCISED — allowed and forbidden requests are deliberately tried under different signed-in accounts.

ACCEPT: Menachem can see the approved accounts and information, while requests for hidden personal details, another person's access, or changes to source data are refused without revealing the protected information.

PROOF: Controlled allowed and denied examples, including misleading text inside a file and attempts to ask indirectly for hidden information.

SOURCE: supplied brief lines 32–99, 127–147, 163–179, 195–216.

### FWD-4 — Menachem downloads the same approved information he can query

DONE WHEN: EXERCISED — the download journey and deliberate misuse attempts are run and the resulting file is opened.

ACCEPT: Menachem opens the download link, signs in, and receives a clearly labeled spreadsheet file containing the approved information. A copied or expired link does not give someone else access, and original source files remain unavailable in this first release.

PROOF: An opened filtered download, a copied-link attempt by another account, an expired-link attempt, and a refused original-file request.

SOURCE: supplied brief lines 20–30, 81–99, 149–161, 199–205.

### FWD-5 — Answers disclose their scope, date, and limitations

DONE WHEN: EXERCISED — complete, missing, outdated, and oversized examples are deliberately requested.

ACCEPT: Menachem can tell which master and date an answer describes and whether information is missing or cut short. An incomplete result is never presented as a complete total, and unavailable information is not guessed.

PROOF: Read the actual answers for deliberately varied availability and size cases and compare their statements with the underlying examples.

SOURCE: supplied brief lines 32–45, 127–147, 201–213.

### FWD-6 — Opal can change or revoke access without a new user setup

DONE WHEN: EXERCISED — an authorized operator changes and removes a controlled grant, then repeats prior requests and downloads.

ACCEPT: An authorized Opal operator can expand approved dates, accounts, or information separately, and can remove access so that later questions and old download links stop working. Menachem cannot change his own permissions, and files he already downloaded are not claimed to be recalled.

PROOF: Deliberate grant-change and revocation runs using a controlled account, with old requests and links repeated afterward.

SOURCE: supplied brief lines 71–99, 149–179, 195–209.

### FWD-7 — Existing Gateway users retain their working experience

DONE WHEN: EXERCISED — existing workflows are repeated alongside deliberately busy Schwab use and a restart.

ACCEPT: Existing users can still complete their usual Gateway work while Schwab questions and downloads are running, and signing back in after a restart does not restore removed access or leave users repeatedly asking for permission they cannot receive.

PROOF: Repeat representative existing user journeys alongside controlled query and download load, expiry, and restart cases.

SOURCE: supplied brief lines 49–55, 101–125, 143–147, 185–215.

### FWD-8 — Opal can support and withdraw the pilot without disturbing source data

DONE WHEN: EXERCISED — support and withdrawal walkthroughs are deliberately completed using the prepared operating instructions.

ACCEPT: An Opal operator can explain a failed connection or denied request, see who used which master without exposing private values in the support record, and turn off the new access while existing source data and collection continue unchanged.

PROOF: An operator follows the onboarding, troubleshooting, audit-read, and rollback instructions against controlled examples and records the result.

SOURCE: supplied brief lines 149–179, 181–219.

## Provenance and next act

The outcome derivation reads the supplied brief, not task orders or a project status projection. NOT READ for Phase 0 derivation: project register, task orders, project JSON. The separate sequence preflight reported the requested code UNKNOWN because it is not registered yet; that read supplied no endpoint content.

The canonical spine L2 requires Andrew to confirm every DONE WHEN line. Registration and PRD preparation are commissioned; endpoint confirmation is not represented as having occurred. Every proposed bar can be exercised deliberately rather than waiting for an organic failure or calendar event.
