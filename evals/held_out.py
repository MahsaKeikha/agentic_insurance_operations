"""Held-out governance scenarios for F154."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"policy_evidence_gap": True}, False),
    (base() | {"coverage_ambiguity_gap": True}, False),
    (base() | {"claims_evidence_gap": True}, False),
    (base() | {"unfair_discrimination_risk": True}, False),
    (base() | {"fraud_special_investigation_risk": True}, False),
    (base() | {"privacy_security_gap": True}, False),
    (base() | {"complaint_appeal_regulatory_gap": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_insurance_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F154 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
