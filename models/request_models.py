"""
Pydantic models for API requests and responses
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class PentestType(str, Enum):
    """Types of penetration tests"""
    NETWORK = "network"
    WEB_APPLICATION = "web_application"
    WIRELESS = "wireless"
    SOCIAL_ENGINEERING = "social_engineering"
    COMPREHENSIVE = "comprehensive"

class Severity(str, Enum):
    """Vulnerability severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class PentestRequest(BaseModel):
    """Request model for penetration testing"""
    target: str = Field(..., description="Target IP address, domain, or URL")
    pentest_type: PentestType = Field(default=PentestType.COMPREHENSIVE, description="Type of penetration test")
    scope: Optional[List[str]] = Field(default=None, description="Specific scope or services to test")
    exclude: Optional[List[str]] = Field(default=None, description="IPs or services to exclude")
    depth: Optional[int] = Field(default=3, ge=1, le=5, description="Testing depth level (1-5)")
    timeout: Optional[int] = Field(default=300, ge=60, le=3600, description="Timeout in seconds")
    
    class Config:
        json_schema_extra: Dict[str, Dict[str, Any]] = {
            "example": {
                "target": "192.168.1.1",
                "pentest_type": "network",
                "scope": ["ssh", "http", "https"],
                "depth": 3,
                "timeout": 300
            }
        }

class Vulnerability(BaseModel):
    """Vulnerability finding model"""
    id: str
    title: str
    description: str
    severity: Severity
    cvss_score: Optional[float] = None
    affected_service: Optional[str] = None
    port: Optional[int] = None
    evidence: Optional[str] = None
    recommendation: str
    references: Optional[List[str]] = None

class PentestResult(BaseModel):
    """Penetration test result model"""
    target: str
    pentest_type: str
    status: str
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_seconds: Optional[int] = None
    vulnerabilities: List[Vulnerability]
    summary: str
    recommendations: List[str]
    raw_output: Optional[Dict[str, Any]] = None

class PentestResponse(BaseModel):
    """Response model for penetration testing"""
    success: bool
    message: str
    task_id: str
    result: Optional[PentestResult] = None
    
    class Config:
        json_schema_extra: Dict[str, Dict[str, Any]] = {
            "example": {
                "success": True,
                "message": "Penetration test completed successfully",
                "task_id": "pentest_20241201_123456",
                "result": {
                    "target": "192.168.1.1",
                    "pentest_type": "network",
                    "status": "completed",
                    "start_time": "2024-12-01T12:34:56",
                    "vulnerabilities": [],
                    "summary": "No critical vulnerabilities found",
                    "recommendations": ["Update system patches"]
                }
            }
        }
