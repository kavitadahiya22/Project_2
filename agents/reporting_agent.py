"""
Report generation agent - Custom implementation
"""
from .base_agent import BaseAgent

class ReportingAgent(BaseAgent):
    """Agent specialized in generating professional penetration testing reports"""
    
    def __init__(self):
        super().__init__()
        self.setup_agent(
            role="Security Report Analyst",
            goal="Generate comprehensive, professional penetration testing reports with clear findings and actionable recommendations",
            backstory="""You are a technical writer and cybersecurity analyst specializing in creating 
            professional security assessment reports. You have extensive experience in communicating complex 
            technical findings to both technical and non-technical stakeholders. Your reports follow industry 
            standards and include executive summaries, detailed technical findings, risk assessments, and 
            prioritized remediation plans."""
        )
