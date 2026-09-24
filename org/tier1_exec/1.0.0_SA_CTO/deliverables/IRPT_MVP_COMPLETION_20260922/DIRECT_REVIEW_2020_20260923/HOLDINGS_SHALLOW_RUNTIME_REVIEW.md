# Holdings shallow runtime repair: bounded PASS

CTO independently reproduced the deployed bcb3 artifact crash under actual /var/task in the pinned Lambda Python 3.12 Linux image, with actual common layer 5 mounted at /opt/python. Network disabled, filesystem read-only. snapshot.load_contract() fails with IndexError: 4 before reading its packaged schema.

Replacing only snapshot.py with exact source 3e913e9ce9482dbe25ec51bc0721e303a12af926 makes the same probe load the real packaged schema successfully. Source SHA256 and output are in the paired JSON. Source inspection confirms existing-ancestor iteration eliminates the fixed-depth access; explicit CONTRACTS_DIR and packaged schema are preferred, with layer and repository fallbacks retained. This precedence is accepted for the version-pinned package contract.

P owns packaging and the one-function deployment plan. Consume M source, repair staged manifest source hashes, verify final artifact under the same shallow layout, and return exact artifact/plan pins for deployment adjudication. Do not rerun broad suites. M continues full supported COT account coverage and conditional publication plan in parallel. P also owns truthful defined failure-code rendering.

This is source/runtime-layout PASS only. Actual authenticated Holdings journey remains FAIL; account coverage remains separately incomplete. No new runtime apply or publication is authorized by this review.
