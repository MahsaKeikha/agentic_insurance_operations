from AGENTS import claims_agent, compliance_agent, coverage_agent, escalation_agent, intake_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "intake": intake_agent.run(case),
        "coverage": coverage_agent.run(case),
        "claims": claims_agent.run(case),
        "compliance": compliance_agent.run(case),
        "escalation": escalation_agent.run(case),
    }
    governance = authorize("release_insurance_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
