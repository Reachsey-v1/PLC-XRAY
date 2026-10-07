# PLC X-RAY GUI User Guide

1. Click **Open GXW** and select a Mitsubishi `.gxw` project.
2. The application analyzes a copy/read-only view; the source project is not modified.
3. Use **Overview** to review project identity, SHA-256, coverage and the verification gate.
4. Use **Programs / POUs** to inspect framing and terminal status.
5. Use **Device Cross-Reference** to inspect direct/symbol-resolved references.
6. Use **Writer Audit** to find potential duplicate writers. Multiple writers are review findings, not automatic faults.
7. Use **Instruction Audit** to review exact lexical instruction observations, including FMOV/BMOV/ZRST/MOV/MOVP/DMOV/INCP/LDP/LDF/DMUL/DDIV/ADD/SUB/MUL/DIV. A zero count means **NOT VERIFIED**, not proven absence.
8. Use **Trace / WHY** for a device such as `M3004` or `Y344`. The trace is limited to decoded evidence and does not invent rung/scan/task semantics.
9. Use **Global Search** for labels, comments, programs and devices.
10. Use **Evidence & Verification** to see the confidence model and native-verification boundary.
11. Export PLC-IR JSON or the engineering HTML report when needed.

### Final verification

PLC X-RAY does not replace Mitsubishi GX Works. Before declaring a project READY, perform native GX Works open/compile, online checks, controlled commissioning and physical safety verification according to your engineering procedure.
