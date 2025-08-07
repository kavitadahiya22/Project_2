"""
Vulnerability assessment agent - Custom implementation
"""
from .base_agent import BaseAgent

class VulnAssessmentAgent(BaseAgent):
    """Agent specialized in vulnerability assessment"""
    
    def __init__(self):
        super().__init__()
        self.setup_agent(
            role="Vulnerability Assessment Expert",
            goal="Identify, analyze, and categorize security vulnerabilities in discovered services and applications",
            backstory="""You are a senior cybersecurity consultant with extensive experience in vulnerability 
            assessment and management. You have deep knowledge of CVE databases, CVSS scoring, and modern 
            attack techniques. You excel at analyzing scan results, identifying false positives, and providing 
            accurate risk assessments with actionable remediation guidance."""
        )
