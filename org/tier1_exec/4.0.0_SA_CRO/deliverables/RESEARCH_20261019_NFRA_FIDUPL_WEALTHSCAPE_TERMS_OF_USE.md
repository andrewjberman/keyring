# RESEARCH 2026-10-19 -- NFRA_FIDUPL: what the Wealthscape Terms of Use say about automated access

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1) | **Project:** NFRA_FIDUPL | **Feeds:** the open call
`dell1-20261019T180827Z-c3a6` (Andrew's word on the Terms of Use before any automated Fidelity sign-in).

**Source (measured):** the Terms of Use page `www2.advisorchannel.com/wc/channel/jsp/common/logininfo/TOU_RIA.html`.
Wealthscape served it inside Andrew's signed-in session in all three captures on 2026-10-19 (HAR1 entry #147). The
HTML was stripped to 89,241 characters of text and searched for automated-access terms. Below are quotes of the
platform's public terms. No client data is involved.

## The clauses

1. **Robots and agentic AI are prohibited:**
   > "The use of agentic AI, robots, or other similar technologies to access or use Wealthscape and other
   > Fidelity-sponsored websites is prohibited. Any such usage may be available in Fidelity's sole discretion and may be
   > subject to additional terms and conditions. Please contact your relation[ship ...]"

   The extract cuts off mid-word, so the rest of the sentence was not read.
2. **Automated repeated access needs Fidelity's approval:**
   > "You should not access the Fidelity Sites through devices or services that are designed to provide high-speed,
   > automated, repeated access, unless such devices are approved or made available by Fidelity."
3. **Access only by the means Fidelity provides:**
   > "You may not obtain or attempt to obtain unauthorized access to such parts of the Fidelity sites ... through any
   > means not intentionally made available by Fidelity for your specific use."
4. **Termination:** the Wealthscape service agreement says Fidelity "may terminate ... the Services to me if I breach
   this Agreement" and that "Any unauthorized use of the Services, whatsoever, shall result in automatic termination of
   this Agreement."

## What it implies (inferred; the decision is Andrew's)

- A box that signs in with Playwright, reads the SMS code and downloads the export is the "robots or similar
  technologies" use clause 1 prohibits, unless Fidelity approves it (clauses 1 and 2).
- The consequence runs to the login itself (clause 4). That login is how the ALONGSIDE, LLC domain ($1.56B, 4,959
  accounts) is reached at all.
- **Paths that stay inside the terms:**
  - **Integration Xchange outbound transmission.** It is "made available by Fidelity", and this login is entitled to
    view and add transmission rules (`RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md` section 1).
  - **Fidelity's written approval** of the automated download, through the relationship manager that clause 1 names.
  - **A person** downloads the six scheduled files from Export Status each morning, and they land through the same
    bronze, manifest and Terraform chain.
- The chain NFRA_FIDUPL builds serves all three paths: schedule, landing by business date, run record, Terraform, and
  the Alongside scope. Only the automated sign-in (PRD fork a, FWD-1's "nobody signed in", FWD-3's failed sign-in) is
  contingent.

## Not checked

- The full text around clause 1, after the cut-off.
- Whether Alongside's agreement with Fidelity adds or waives terms.
- Whether Fidelity has approved any automation for Alongside. This needs Fidelity or counsel to answer, not a capture.
