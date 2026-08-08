#!/usr/bin/env python3
"""
WHOIS Lookup Module - Query WHOIS information
"""

import whois
from typing import Dict, Any, Optional


class WHOISService:
    """WHOIS lookup service"""
    
    def query(self, ip: str) -> Dict[str, Any]:
        """
        Query WHOIS information for an IP
        
        Args:
            ip: IP address
            
        Returns:
            Dict with WHOIS data
        """
        try:
            domain = whois.whois(ip)
            return {
                "success": True,
                "registrar": domain.registrar,
                "creation_date": str(domain.creation_date) if domain.creation_date else None,
                "expiration_date": str(domain.expiration_date) if domain.expiration_date else None,
                "name_servers": domain.name_servers,
                "org": domain.org,
                "country": domain.country,
                "emails": domain.emails,
                "dnssec": domain.dnssec
            }
        except Exception as e:
            return {"error": str(e), "success": False}
