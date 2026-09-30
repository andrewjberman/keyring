# Andrew-direct: investigate Inflection's Portal performance question

Date: 2026-09-28. Seat: `4.0.0_SA_CRO~I`. Channel: Andrew at this Codex terminal.

Verbatim instruction:

> I need you to do some investigative work for me. I do not know if you have access to the opalgateway mcp, if that is set up properly for Codex agents. If so, please go to the Outlook email of myself, andrew@opalinvest.com and check out the messages from today between me, Joe Brandenberg, and Yang Liu. I have also sent CRO Base to go get it for you in lossless form if you are unable. Once you have that information, I need you to go and analyze Joe's query, and make sure that Yang's response is actually correct in terms of the data we are displaying on the Portal.

The Opal Gateway MCP was not exposed to this Codex session. CRO base supplied its lossless mailbox extraction, including source message IDs, through the exact inbox message `20260928T222302Z_4.0.0_SA_CRO__ANDREW-DIRECT__investigate__Inflection_.md`. This seat read, acknowledged, acted on, and then archived that exact message. The extraction remains private in `tmp/cro-i-relay/20260928_dashboard_performance_numbers/EMAILS_VERBATIM.md`; it is not included in this commit. The sender's spelling is Joe Brandenburg.

Deliverable: [RCN-0019 investigation](RCN-0019_INFLECTION_PORTAL_PERFORMANCE_20260928.md), with a reproducible calculation and sanitized result file. Scope is investigation and reporting. No production mutation or outbound client email was authorized or performed.

Andrew's subsequent clarification, verbatim:

> I'm not concerned with Yang's logic as much as I am concerned with the Portal not showing the correct information for whatever reason. I just want to make sure the Portal's numbers are correct as total return numbers. If Yang quoted something incorrectly, I do not care; I only care that we are correctly representing the performance numbers as total return and that there is clear proof and provenance that we are doing so.

The final report therefore centers on total-return source provenance, deployed transformations, independent numerical reconciliation, and a confirmed Positioning period-boundary defect. Yield and investment-rationale commentary was removed from the final assessment.
