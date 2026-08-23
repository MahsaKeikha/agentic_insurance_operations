# F154 | Agentic Insurance Operations | L3 Gold Standard | v1.0

A governed five-agent reference architecture for insurance operations support across intake, policy evidence, coverage analysis, claims handling, compliance, escalation, privacy, fairness, consumer protection, provenance, and qualified human approval.

F154 is a decision-support system. It is not an insurer, producer, adjuster of record, underwriter of record, claims authority, payment system, legal authority, or autonomous coverage engine. It cannot bind coverage, set premiums, approve or deny claims, issue binding coverage determinations, pay or settle claims, cancel or nonrenew policies, or rescind coverage.

## Insurance operations lifecycle

```text
Case Intake
        -> Policy and Coverage Evidence
        -> Claims Evidence and Operational Review
        -> Compliance, Fairness, and Privacy Review
        -> Escalation, Complaint, and Appeal Review
        -> Qualified Insurance Approval
        -> Human-Controlled Binding Action
```

The workflow fails closed when required reviews are missing or when material policy, coverage, claims-evidence, discrimination, fraud, privacy, complaint, appeal, regulatory, or provenance issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Intake Agent | Structures customer, policy, loss, claim, communication, date, jurisdiction, document, and urgency information | What case is being handled and what facts are verified? |
| Coverage Agent | Organizes declarations, forms, endorsements, limits, deductibles, exclusions, conditions, effective dates, and unresolved interpretation questions | What policy evidence is relevant without making a binding coverage decision? |
| Claims Agent | Tracks loss facts, evidence, chronology, damages, valuation inputs, reserves, investigation state, vendors, subrogation, and operational next steps | What claims work is supported by the evidence and what remains unresolved? |
| Compliance Agent | Reviews jurisdiction, consumer protection, claims-handling rules, fairness, privacy, notices, deadlines, complaints, and prohibited practices | What compliance, fairness, privacy, or regulatory issues require human review? |
| Escalation Agent | Routes ambiguity, fraud indicators, complaints, litigation, appeals, coverage disputes, severe losses, vulnerable customers, and authority questions | What requires specialized or higher-authority handling? |

Agents support insurance operations teams, customer service, adjusters, claims examiners, underwriting support, compliance, legal, special investigations, quality assurance, complaint teams, and authorized reviewers. They do not replace licensed or authorized professionals where law, contract, regulation, or organizational policy requires them.

## Repository structure

```text
AGENTS/
├── intake_agent.py
├── coverage_agent.py
├── claims_agent.py
├── compliance_agent.py
└── escalation_agent.py

SKILLS/
├── intake_reasoning.py
├── coverage_reasoning.py
├── claims_reasoning.py
├── compliance_reasoning.py
└── escalation_reasoning.py

TOOLS/
├── case_registry.py
├── policy_evidence.py
├── claim_checklist.py
├── compliance_checklist.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Case intake

The executable policy requires `case_intake_reviewed`.

Case intake should preserve policy identifier, claim identifier, named insured, claimant where appropriate, loss date, report date, jurisdiction, line of business, loss type, contact preference, communication needs, accessibility needs, urgent safety issues, and source provenance.

The system should distinguish reported facts, verified facts, third-party statements, estimates, allegations, assumptions, and unresolved questions.

## First notice of loss

FNOL can include who reported the loss, when it occurred, where it occurred, what happened, known injuries, property involved, emergency needs, police or fire involvement, witnesses, photographs, documents, and immediate mitigation actions.

F154 should not pressure users to characterize legal fault or coverage before evidence is available.

## Policy evidence architecture

The executable policy requires `policy_evidence_reviewed`. `policy_evidence_gap` blocks release when material policy form, endorsement, declarations, effective date, jurisdiction, limit, deductible, exclusion, or source issues remain unresolved.

`TOOLS/policy_evidence.py` can preserve form number, edition, endorsement, declarations, effective period, named insured, covered property or risk, limit, sublimit, deductible, exclusion, condition, jurisdiction, source, and document version.

## Policy hierarchy

Coverage analysis should identify the actual contract documents in force for the relevant date and jurisdiction. Marketing summaries, customer-service descriptions, quotes, binders, certificates, prior policies, or generic forms should not silently replace the operative contract.

## Declarations

Declarations can identify named insureds, locations, vehicles, properties, limits, deductibles, endorsements, forms, effective dates, and other schedule-specific information.

## Forms and endorsements

Endorsements can modify base policy language and can add, remove, narrow, or expand coverage. Form edition and effective date matter.

## Effective dates

A policy may be issued, renewed, changed, canceled, reinstated, or endorsed at different times. Coverage analysis should use the policy state applicable to the loss date.

## Limits and sublimits

Aggregate, occurrence, per-person, per-property, scheduled, category-specific, and other limits should not be mixed. Sublimits can materially affect otherwise covered losses.

## Deductibles and retentions

Deductibles, self-insured retentions, waiting periods, franchises, percentage deductibles, and other risk-sharing terms require contract-specific interpretation.

## Exclusions

An exclusion should not be assumed to apply merely because a keyword resembles the loss description. The operative wording, definitions, exceptions, causation, jurisdiction, and facts matter.

## Conditions

Notice, cooperation, proof of loss, mitigation, examination, appraisal, suit limitations, consent, preservation, and other conditions can affect claims handling. Binding consequences require qualified review.

## Definitions

Defined terms can change the meaning of ordinary language. Coverage review should preserve policy definitions rather than substituting general dictionary meanings.

## Coverage analysis architecture

The executable policy requires `coverage_analysis_reviewed`. `coverage_ambiguity_gap` blocks release when material coverage, exclusion, condition, causation, allocation, reservation-of-rights, or interpretation issues remain unresolved.

F154 can identify relevant provisions and organize arguments. It cannot issue a binding coverage determination.

## Coverage trigger

Coverage can depend on occurrence, claims-made reporting, loss timing, manifestation, discovery, policy period, retroactive date, or other trigger concepts depending on product and jurisdiction.

## Causation

Multiple causes can contribute to a loss. Proximate cause, concurrent causation, anti-concurrent-causation language, ensuing loss, efficient cause, and allocation questions can be legally sensitive.

## Reservation of rights

Potential coverage uncertainty may require authorized reservation-of-rights handling. F154 can flag the need but cannot issue legal notices without qualified review.

## Duty to defend and indemnify

Liability coverage can distinguish defense obligations from indemnity obligations. These are legal and contract-specific questions that require authorized review.

## Claims evidence architecture

The executable policy requires `claims_evidence_reviewed`. `claims_evidence_gap` blocks release when material loss facts, documentation, damage, valuation, causation, chronology, or investigation evidence remains unresolved.

`TOOLS/claim_checklist.py` can structure evidence requirements by claim type.

## Evidence sources

Evidence can include statements, photographs, video, invoices, estimates, medical documentation, repair records, telematics, weather data, police reports, fire reports, inspection reports, appraisals, expert reports, receipts, title records, communications, and other relevant sources.

Availability of evidence does not determine credibility automatically. Source, date, authenticity, chain of custody, completeness, and relevance matter.

## Chronology

Claims often depend on a sequence of events. A chronology should preserve event time, report time, source, confidence, and whether the item is disputed.

## Damage assessment

Damage review should separate observed damage, preexisting conditions, claimed damage, estimated repair scope, code upgrades, depreciation, betterment, total-loss analysis, and unresolved causation.

## Property claims

Property workflows can involve emergency mitigation, inspection, contents, dwelling or building scope, additional living expense, business interruption, depreciation, replacement-cost conditions, contractors, and appraisal.

## Auto claims

Auto workflows can involve liability investigation, vehicle damage, total loss, rental, towing, storage, injuries, medical payments, uninsured or underinsured motorist coverage, subrogation, salvage, and state-specific rules.

## Liability claims

Liability analysis can involve duty, breach, causation, damages, comparative fault, contractual obligations, defense, indemnity, tender, contribution, and litigation. F154 does not determine legal liability.

## Injury claims

Medical records, bills, treatment chronology, causation, prior conditions, impairment, wage loss, and future care can be sensitive and require privacy controls and qualified review.

F154 does not make medical diagnoses or medical-necessity determinations.

## Workers compensation

Workers compensation is highly jurisdiction specific and can involve compensability, medical treatment, disability, return to work, wage replacement, vocational issues, and statutory procedures. Specialized professionals remain responsible.

## Health insurance operations

Health claims can involve eligibility, benefits, network status, coding, medical necessity, prior authorization, coordination of benefits, appeals, and regulatory protections. Clinical determinations require qualified clinical review where applicable.

## Life insurance

Life claims can involve beneficiary status, contestability, policy status, cause of death, exclusions, assignment, ownership, and documentation. F154 does not make binding beneficiary or coverage decisions.

## Disability insurance

Disability claims can involve occupation definitions, elimination periods, functional evidence, earnings, medical documentation, offsets, rehabilitation, and recurring review. Qualified claims and clinical professionals retain authority.

## Commercial insurance

Commercial lines can involve complex schedules, layered programs, deductibles, retentions, coinsurance, business interruption, additional insureds, certificates, contractual indemnity, and multiple carriers.

## Reinsurance

Reinsurance operations can involve treaties, facultative agreements, attachments, limits, notices, bordereaux, recoveries, and allocation. F154 does not make binding reinsurance settlements.

## Reserves

Case reserves, expense reserves, incurred-but-not-reported estimates, and actuarial reserves serve different purposes. F154 can support documentation but cannot autonomously establish financial reserves where authority is restricted.

## Valuation

Claims valuation should preserve method, evidence, assumptions, taxes, depreciation, labor, materials, market conditions, limits, deductibles, salvage, prior damage, and uncertainty.

## Total loss

Total-loss determinations can depend on actual cash value, repair cost, statutory thresholds, salvage, taxes, fees, jurisdiction, and vehicle or property-specific evidence.

## Replacement cost and actual cash value

Replacement cost and actual cash value are distinct concepts and may depend on policy wording and jurisdiction. Depreciation should be traceable rather than arbitrary.

## Business interruption

Business-income claims can involve period of restoration, revenues, expenses, trends, continuing costs, extra expense, civil authority, dependent property, and policy limitations.

## Claims operations

Operational support can include task management, document requests, diary dates, vendor coordination, estimate review, communication preparation, escalation, quality checks, and status reporting.

## Timeliness

Claims handling is often subject to jurisdiction-specific acknowledgement, investigation, decision, payment, communication, and complaint deadlines. Systems should preserve due dates and evidence of compliance.

## Customer communications

Communications should distinguish factual status, requested documents, unresolved issues, rights, deadlines, and next steps. Automated language must not imply a final coverage or liability decision that has not been authorized.

## Accessibility and language access

Customers may require interpreters, accessible formats, relay services, plain language, alternate communication channels, or disability accommodations. These needs should be treated as operational requirements.

## Vulnerable customers

Catastrophe survivors, injured people, older adults, people with disabilities, grieving families, financially distressed customers, and people with limited language access may require additional care and escalation.

## Compliance architecture

The executable policy requires `compliance_fairness_reviewed`. `TOOLS/compliance_checklist.py` can preserve jurisdiction, rule, process, notice, deadline, evidence, exception, owner, and review status.

## Jurisdiction

Insurance regulation can vary substantially by state, country, province, territory, product, market, and customer type. F154 should not generalize one jurisdiction's rule to another.

## Unfair claims practices

Claims processes should not knowingly misrepresent policy provisions, impose unreasonable documentation requirements, delay without basis, use coercive settlement practices, or deny without appropriate review and explanation.

## Fairness and discrimination

`unfair_discrimination_risk` blocks release when protected-class, proxy-discrimination, disparate-treatment, disparate-impact, or unfair-practice concerns remain unresolved.

AI features should not convert sensitive characteristics or proxies into unfair outcomes.

## Underwriting boundary

`approve_or_bind_policy` is protected. F154 can support document collection or review but cannot accept risk, bind coverage, issue a policy, or make final underwriting decisions.

## Pricing boundary

`set_or_change_premium` is protected. F154 cannot establish or change premiums, rating factors, surcharges, discounts, or individualized prices as a binding action.

## Coverage determination boundary

`issue_coverage_determination` is protected. Coverage decisions remain under authorized claims, legal, or insurance professionals.

## Claim approval and denial boundary

`approve_or_deny_claim` is protected. A model output cannot itself approve, partially approve, or deny a claim.

## Payment and settlement boundary

`pay_or_settle_claim` is protected. F154 cannot issue checks, initiate electronic payments, accept releases, make settlement offers with binding authority, or commit funds.

## Cancellation, nonrenewal, and rescission boundary

`cancel_nonrenew_or_rescind_policy` is protected. These actions can have strict legal and notice requirements and remain under authorized human control.

## Fraud and special investigations

`fraud_special_investigation_risk` blocks release when fraud indicators, referral, investigation, accusation, or special-investigation issues require authorized handling.

Fraud indicators are not proof of fraud. F154 must not label a claimant, insured, provider, employee, or third party as fraudulent without appropriate evidence and authorized review.

## Special investigation units

SIU referrals can involve legal thresholds, regulatory reporting, law enforcement, surveillance, expert review, and strict privacy controls. F154 can flag potential referral conditions but cannot autonomously initiate intrusive investigations.

## Surveillance boundary

Insurance investigation must comply with law, privacy, proportionality, and company policy. F154 should not facilitate unlawful tracking, stalking, covert intrusion, credential theft, or unauthorized surveillance.

## Privacy architecture

The executable policy requires `privacy_security_reviewed`. `privacy_security_gap` blocks release when personal, medical, financial, location, identity, security, consent, access, or retention issues remain unresolved.

## Personal data

Insurance operations can contain addresses, phone numbers, identities, financial information, driving records, property information, family information, health information, photographs, geolocation, and legal records. Collection and access should be limited to legitimate need.

## Medical information

Medical data should receive heightened protection and access control. Claims personnel should receive only information needed for authorized functions.

## Data minimization

The system should avoid collecting sensitive information merely because it may be useful later. Retention should follow legal and organizational requirements.

## Security

Access controls, encryption, audit logs, secure document transfer, least privilege, credential protection, retention rules, incident response, and vendor controls are important for claims systems.

## Identity verification

Identity verification should be proportionate to the requested action and should not create unnecessary barriers for legitimate customers.

## Complaints

The executable policy requires `escalation_appeal_reviewed`. `complaint_appeal_regulatory_gap` blocks release when complaint, appeal, external review, regulator, notice, deadline, or consumer-protection issues remain unresolved.

## Appeals

Coverage, medical, valuation, underwriting, or claims decisions can have internal or external appeal rights depending on product and jurisdiction. The system should preserve deadlines and review authority.

## External review

Some products can include independent external review or ombudsman processes. F154 should not imply that internal review replaces available statutory rights.

## Regulatory complaints

Complaints from insurance departments, ombudsmen, consumer agencies, attorneys general, or other authorities require controlled handling and complete records.

## Litigation

Litigation, arbitration, appraisal, mediation, or formal dispute resolution should trigger appropriate legal and claims authority. F154 does not provide binding legal strategy.

## Legal holds

Potential litigation can require preservation of communications, documents, photographs, recordings, estimates, notes, and system logs. Authorized legal teams control hold scope.

## Subrogation

Subrogation can involve recovery from responsible third parties, other insurers, contractual indemnitors, manufacturers, or other sources. F154 can identify evidence and deadlines but cannot make binding recovery decisions.

## Salvage

Salvage handling can involve title, possession, valuation, storage, sale, environmental obligations, and state-specific rules.

## Contribution and other insurance

Multiple policies or parties can create contribution, priority, excess, escape, or other-insurance questions. These can require legal analysis.

## Catastrophe operations

Catastrophes can create large claim volumes, temporary processes, emergency vendors, regulatory bulletins, moratoria, extended deadlines, fraud risk, accessibility needs, and vulnerable-customer concerns.

Automation during catastrophes should not reduce review merely because volume is high.

## Emergency mitigation

Customers may need urgent steps to protect life or property. F154 can support general process information but should not require unsafe actions or make technical repair decisions beyond verified guidance.

## Vendor management

Repair networks, medical providers, appraisers, investigators, rental companies, contractors, restoration vendors, and other suppliers require scope, licensing, conflicts, privacy, quality, and performance controls.

## Conflict of interest

Claims handling should identify conflicts involving adjusters, experts, vendors, attorneys, insureds, claimants, repair facilities, or related parties.

## Payments controls

Binding payments should require authorized approval, identity and payee verification, payment limits, segregation of duties, fraud controls, reconciliation, and audit logs outside F154's autonomous authority.

## Recovery and overpayment

Recoveries of duplicate or erroneous payments can affect consumer rights and should follow authorized processes. F154 can flag discrepancies but cannot autonomously debit or recover funds.

## Documentation quality

Claims notes should separate fact, source, analysis, recommendation, authority, and final decision. They should avoid unsupported character judgments or inflammatory language.

## Explainability

High-impact decisions should have a traceable basis in policy language, evidence, applicable rules, and authorized human judgment. A model score alone is not an adequate explanation.

## Model governance

Any predictive model used in claims, pricing, fraud, underwriting, triage, or customer treatment should have defined purpose, validation, monitoring, fairness review, data provenance, drift controls, and human authority boundaries.

## AI in claims

AI can help classify documents, summarize files, identify missing information, extract policy provisions, support triage, detect inconsistencies, and prepare drafts. It should not silently convert probabilistic outputs into adverse customer decisions.

## Generative AI

Generated summaries can omit exceptions or hallucinate facts. Material policy language, amounts, dates, legal requirements, medical facts, and claim decisions should be checked against source records.

## Data quality

Names, addresses, dates, policy numbers, limits, deductibles, amounts, payment status, claim status, coding, and document links should be validated before they drive material actions.

## Duplicate records

Duplicate claims, policies, documents, contacts, payments, or vendors can create operational errors. Entity resolution should preserve uncertainty rather than merge records solely on approximate similarity.

## Financial calculations

Deductibles, depreciation, coinsurance, limits, reserves, taxes, recoveries, interest, benefit periods, and settlement calculations should preserve formulas, inputs, units, rounding, source, and reviewer.

## Regulatory reporting

Some events can require regulatory, fraud bureau, statistical, financial, market-conduct, catastrophe, or other reporting. F154 can track deadlines and evidence but cannot autonomously file binding reports unless separately authorized.

## Record retention

Policy, claim, complaint, payment, communication, investigation, and compliance records can have different retention periods. Legal holds can supersede normal deletion schedules.

## Auditability

Every material recommendation should be reconstructable from source documents, policy versions, evidence, calculations, communications, escalations, and approvals.

## Provenance

`provenance_documentation_gap` blocks release when policy, claim, evidence, communication, calculation, escalation, compliance, or decision provenance is incomplete.

F154 must never fabricate policy language, endorsements, limits, deductibles, claim facts, medical records, repair estimates, police reports, coverage status, approvals, payments, regulatory findings, or customer communications.

## Memory and state

The `memory/` layer can preserve case state, policy versions, claim evidence, tasks, communications, deadlines, calculations, coverage questions, complaints, escalations, compliance reviews, authorized decisions, and unresolved issues.

It should distinguish draft recommendations from binding decisions and current records from superseded versions.

## Observability

The `observability/` layer supports traceability across case intake, policy evidence, coverage questions, claim evidence, calculations, deadlines, fairness findings, privacy controls, fraud referrals, complaints, escalations, approvals, and protected-action attempts.

Useful telemetry includes stale policy documents, missing endorsements, overdue tasks, unresolved evidence, conflicting facts, deadline risk, repeated document requests, discrimination flags, privacy access, complaint status, and approval state.

## Required reviews

The executable policy requires all eight conditions:

```text
case_intake_reviewed
policy_evidence_reviewed
coverage_analysis_reviewed
claims_evidence_reviewed
compliance_fairness_reviewed
privacy_security_reviewed
escalation_appeal_reviewed
qualified_insurance_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- policy forms, endorsements, declarations, effective dates, jurisdictions, limits, deductibles, exclusions, or source evidence remain unresolved
- material coverage, exclusion, condition, causation, allocation, reservation-of-rights, or interpretation issues remain unresolved
- loss facts, documentation, damages, valuation, causation, chronology, or investigation evidence remains unresolved
- protected-class, proxy-discrimination, disparate-treatment, disparate-impact, or unfair-practice concerns remain unresolved
- fraud indicators or special-investigation issues require authorized human handling
- personal, medical, financial, location, identity, security, consent, access, or retention issues remain unresolved
- complaints, appeals, external review, regulators, notices, deadlines, or consumer-protection issues remain unresolved
- policy, claim, evidence, communication, calculation, escalation, compliance, or decision provenance is incomplete
- any required review is missing
- qualified insurance approval is missing

The system exposes blockers rather than manufacturing coverage, fault, fraud, valuation certainty, compliance clearance, claim approval, payment authority, or underwriting authority.

## Protected actions

The safety policy permanently protects:

```text
approve_or_bind_policy
set_or_change_premium
approve_or_deny_claim
issue_coverage_determination
pay_or_settle_claim
cancel_nonrenew_or_rescind_policy
```

These remain outside autonomous authority even after every review is satisfied.

## Human authority boundaries

F154 must not autonomously bind coverage, price insurance, approve or deny claims, issue binding coverage decisions, make final liability findings, initiate intrusive investigations, settle claims, issue payments, cancel or nonrenew policies, rescind coverage, make clinical determinations, or override compliance controls.

Authorized underwriters, adjusters, claims examiners, medical reviewers, actuaries, compliance professionals, legal professionals, SIU teams, supervisors, and payment authorities retain their respective responsibilities.

## Explicit failure states

```text
CASE INTAKE REVIEW REQUIRED
POLICY EVIDENCE REVIEW REQUIRED
COVERAGE ANALYSIS REVIEW REQUIRED
CLAIMS EVIDENCE REVIEW REQUIRED
COMPLIANCE AND FAIRNESS REVIEW REQUIRED
PRIVACY AND SECURITY REVIEW REQUIRED
ESCALATION AND APPEAL REVIEW REQUIRED
QUALIFIED INSURANCE APPROVAL REQUIRED
POLICY EVIDENCE GAP
COVERAGE AMBIGUITY GAP
CLAIMS EVIDENCE GAP
UNFAIR DISCRIMINATION RISK
FRAUD OR SPECIAL INVESTIGATION RISK
PRIVACY OR SECURITY GAP
COMPLAINT, APPEAL, OR REGULATORY GAP
PROVENANCE DOCUMENTATION GAP
POLICY BINDING PROHIBITED
AUTONOMOUS PRICING PROHIBITED
CLAIM APPROVAL OR DENIAL PROHIBITED
BINDING COVERAGE DETERMINATION PROHIBITED
CLAIM PAYMENT OR SETTLEMENT PROHIBITED
AUTONOMOUS CANCELLATION, NONRENEWAL, OR RESCISSION PROHIBITED
```

## End-to-end reference workflow

1. Register the case with policy, claim, customer, loss date, report date, jurisdiction, product, urgency, accessibility needs, and evidence sources.
2. Retrieve and version the operative declarations, forms, endorsements, schedules, limits, deductibles, exclusions, and conditions.
3. Build a loss chronology and separate reported facts, verified facts, disputed facts, estimates, and unknowns.
4. Identify relevant coverage provisions and unresolved interpretation questions without issuing a binding coverage decision.
5. Collect and validate claim evidence, damage information, valuation inputs, vendors, calculations, deadlines, and required documents.
6. Review jurisdictional claims-handling rules, customer notices, fairness, discrimination risk, privacy, security, and consumer protections.
7. Escalate fraud indicators, severe losses, legal disputes, complaints, appeals, coverage ambiguity, vulnerable customers, litigation, and regulatory issues to authorized specialists.
8. Preserve formulas, policy citations, evidence, communications, notes, deadlines, calculations, and decision provenance.
9. Run quality checks for document consistency, policy version, amounts, dates, duplicate records, unsupported conclusions, and missing approvals.
10. Apply fail-closed governance and require qualified insurance approval.
11. Release only a support package with clear unresolved items and authority boundaries.
12. Keep binding underwriting, pricing, coverage, claims, payment, cancellation, nonrenewal, and rescission actions under authorized human control.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test intake completeness, policy-document fidelity, coverage-question identification, claims-evidence discipline, chronology, calculations, fairness, privacy, fraud escalation, complaint handling, deadline awareness, provenance, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, policy-evidence gaps, coverage ambiguity, claims-evidence gaps, discrimination risk, fraud and SIU escalation, privacy and security gaps, complaint and regulatory gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed insurance-operations workflow.

## Reproducibility

Reproducible insurance review requires preserving policy versions, declarations, endorsements, loss chronology, evidence sources, calculations, valuation assumptions, claim notes, communications, compliance rules, complaint status, escalations, approvals, and unresolved questions.

## Extension points

Organization-specific implementations can add governed integrations for policy administration, claims systems, document management, customer communications, payment preparation, repair networks, medical review, fraud systems, regulatory libraries, complaint systems, litigation management, and analytics.

Any integration capable of binding coverage, changing price, changing policy status, approving or denying claims, issuing payments, making adverse customer decisions, initiating intrusive investigations, or filing binding regulatory actions should remain behind explicit authorization, least privilege, segregation of duties, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include FNOL support, policy-document retrieval, claim summarization, coverage-question triage, property and auto claim support, document-gap analysis, deadline tracking, complaint preparation, fraud referral support, quality assurance, catastrophe operations, claims analytics, subrogation support, and compliance review.

F154 is not an autonomous insurer, producer, underwriter, adjuster of record, claims examiner of record, actuary, legal authority, medical reviewer, fraud investigator, regulator, settlement authority, or payment authority.

## Design principles

1. Begin with the exact policy, endorsement set, effective period, jurisdiction, loss date, and verified case identity.
2. Separate reported facts, verified facts, disputed facts, estimates, legal questions, recommendations, and binding decisions.
3. Never infer coverage from generic product descriptions when operative policy language is available.
4. Never treat fraud indicators as proof of fraud or predictive scores as proof of misrepresentation.
5. Preserve fairness, nondiscrimination, privacy, accessibility, complaint rights, and consumer protections as core requirements.
6. Keep calculations, policy citations, evidence, dates, communications, and approvals fully traceable.
7. Never fabricate policy language, claim evidence, medical information, valuations, notices, approvals, payments, or regulatory status.
8. Fail closed when intake, policy evidence, coverage, claims evidence, fairness, privacy, escalation, provenance, or qualified approval is incomplete.
9. Keep underwriting, pricing, final coverage, claim decisions, settlement, payment, cancellation, nonrenewal, and rescission under authorized human control.

## Scope statement

F154 demonstrates a governed multi-agent architecture for insurance operations support. It combines specialized intake, coverage, claims, compliance, and escalation agents with deterministic case, policy-evidence, claims, compliance, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over underwriting, pricing, coverage determinations, claim approval or denial, settlement, payment, policy cancellation, nonrenewal, rescission, and regulated customer actions.

Author: Mahsa Keikha
